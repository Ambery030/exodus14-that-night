#!/usr/bin/env python3
"""Stage 0.98: wind–tide storage and post-wind release diagnostic.

This experiment keeps MI_EAST_RELIEF_V1 and the three resolved synthetic sandy
backbones fixed.  It asks whether a rising external micro-tide can coexist with
an east-to-west wind tilt, store water/head in the western lagoon, and then
produce a physically noticeable return after the wind falls away.

The tide phases are sensitivity clocks, not an ancient tide prediction.  The
"alarm" labels are transparent operational proxies for a reason to retreat;
they are not a psychological or fatality model.  No Egyptians are simulated.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from stage091 import GridSpec
from stage096_coupled_pilot import MobilityCase, simulate_case
from stage096_map_informed_lock import build_map_informed_geometry
from stage097_text_locked_sweep import RIDGE_FAMILIES


CENTRAL_MIXED = (
    MobilityCase("mixed_people_stock_central", 0.60, 0.30, 13.0),
)


@dataclass(frozen=True)
class Case:
    label: str
    wind_m_s: float
    tide_amplitude_m: float
    low_clock_h: float
    wind_stop_clock_h: float


def _hours_until(start_h: float, target_h: float) -> float:
    return (target_h - start_h) % 24.0


def _clock_to_text(hour: float) -> str:
    minutes = int(round(hour * 60.0)) % (24 * 60)
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def _geometry_factory(inlet_x_fraction: float):
    def build(grid, family, mean_stage_m, marine):
        return build_map_informed_geometry(
            grid,
            family,
            mean_stage_m,
            marine,
            inlet_x_fraction=inlet_x_fraction,
        )

    return build


def _first_time(frame: pd.DataFrame, mask: pd.Series) -> float:
    rows = frame[mask]
    return float(rows["time_h"].iloc[0]) if len(rows) else float("nan")


def analyse(case: Case, summary: dict[str, object], hydro: pd.DataFrame) -> dict[str, object]:
    event_start = float(summary["event_zero_local_hour"])
    calm_h = _hours_until(event_start, case.wind_stop_clock_h) + 0.5
    low_h = _hours_until(event_start, case.low_clock_h)
    pre_calm = hydro[hydro["time_h"] <= calm_h].copy()
    after_calm = hydro[
        (hydro["time_h"] >= calm_h) & (hydro["time_h"] <= calm_h + 2.5)
    ].copy()
    # Restrict the overlap diagnostic to the rising limb after the low tide
    # being tested.  Otherwise the preceding semidiurnal cycle is counted too.
    simultaneous = pre_calm[
        (pre_calm["time_h"] >= low_h)
        & (pre_calm["time_h"] <= calm_h)
        & (pre_calm["external_tide_tendency_m_h"] > 0.0)
        & (pre_calm["wind_speed_m_s"] >= 6.0)
        & (pre_calm["west_minus_east_eta_m"] > 0.0)
    ].copy()
    initial_west = float(hydro["west_zone_volume_m3"].iloc[0])
    calm_index = int((hydro["time_h"] - calm_h).abs().idxmin())
    calm_row = hydro.loc[calm_index]
    # Route-local rewet clock: first time the resolved sandy backbones rise
    # 2 cm above their local minimum.  This replaces the older whole-zone
    # median clock, which was not a human-route observable.
    route_depth = hydro["resolved_route_probe_median_depth_m"].to_numpy(float)
    route_time = hydro["time_h"].to_numpy(float)
    valid_window = route_time <= calm_h + 2.5
    local_rewet_h = float("nan")
    local_min_h = float("nan")
    if np.any(valid_window):
        candidate_indices = np.flatnonzero(valid_window)
        min_index = int(candidate_indices[np.argmin(route_depth[valid_window])])
        local_min_h = float(route_time[min_index])
        target_depth = float(route_depth[min_index] + 0.02)
        later = np.flatnonzero(
            (np.arange(len(route_time)) > min_index)
            & (route_time <= calm_h + 2.5)
            & (route_depth >= target_depth)
        )
        if len(later):
            local_rewet_h = float(route_time[int(later[0])])

    first_rewet_h = local_rewet_h
    route_loss_h = float(summary.get("parallel_route_loss_h", float("nan")))
    rewet_to_loss_h = (
        route_loss_h - first_rewet_h
        if math.isfinite(first_rewet_h) and math.isfinite(route_loss_h)
        else float("nan")
    )
    peak_width = float(hydro["active_aggregate_width_m"].max())
    minimum_post_width = float(after_calm["active_aggregate_width_m"].min()) if len(after_calm) else 0.0
    width_loss_fraction = (
        max(0.0, 1.0 - minimum_post_width / peak_width) if peak_width > 0.0 else 0.0
    )
    post_speed_p95 = float(after_calm["resolved_route_probe_speed_p95_m_s"].max()) if len(after_calm) else 0.0
    post_speed_max = float(after_calm["resolved_route_probe_speed_max_m_s"].max()) if len(after_calm) else 0.0
    post_hu_p95 = float(after_calm["resolved_route_probe_hu_p95_m2_s"].max()) if len(after_calm) else 0.0
    post_hu_max = float(after_calm["resolved_route_probe_hu_max_m2_s"].max()) if len(after_calm) else 0.0
    post_depth_rise = float(after_calm["resolved_route_probe_depth_rise_cm_min"].max()) if len(after_calm) else 0.0
    post_width_loss_rate = (
        max(0.0, -float(after_calm["active_width_change_m_min"].min()))
        if len(after_calm) else 0.0
    )
    lane_drop = (
        int(after_calm["active_complete_lanes"].max() - after_calm["active_complete_lanes"].min())
        if len(after_calm) else 0
    )
    acute = post_hu_max >= 0.70
    urgent = (
        lane_drop >= 1
        and width_loss_fraction >= 0.50
        and (
            post_speed_p95 >= 0.20
            or post_depth_rise >= 0.10
            or (math.isfinite(rewet_to_loss_h) and rewet_to_loss_h <= 1.5)
        )
    )
    noticeable = (
        width_loss_fraction >= 0.25
        or post_speed_p95 >= 0.10
        or post_depth_rise >= 0.05
    )
    if acute:
        alarm_proxy = "acute_instability_screen"
    elif urgent:
        alarm_proxy = "urgent_retreat_pressure"
    elif noticeable:
        alarm_proxy = "noticeable_progressive_return"
    else:
        alarm_proxy = "weak_or_unresolved_return"

    return {
        "case": case.label,
        "wind_m_s": case.wind_m_s,
        "tide_amplitude_m": case.tide_amplitude_m,
        "external_low_clock": _clock_to_text(case.low_clock_h),
        "wind_calm_clock": _clock_to_text((case.wind_stop_clock_h + 0.5) % 24.0),
        "first_route_clock": summary.get("first_parallel_route_clock", ""),
        "route_local_depth_min_clock": (
            _clock_to_text(event_start + local_min_h) if math.isfinite(local_min_h) else ""
        ),
        "route_local_rewet_2cm_clock": (
            _clock_to_text(event_start + local_rewet_h) if math.isfinite(local_rewet_h) else ""
        ),
        "simultaneous_parallel_route_loss_clock": summary.get("parallel_route_loss_clock", ""),
        "first_half_width_collapse_clock": summary.get("first_half_width_collapse_clock", ""),
        "all_segments_closed_clock": summary.get("all_segments_closed_clock", ""),
        "parallel_window_h": summary.get("parallel_window_h", 0.0),
        "current_cycle_rising_tide_wind_tilt_overlap_h": (
            float(simultaneous["time_h"].max() - simultaneous["time_h"].min())
            if len(simultaneous) > 1 else 0.0
        ),
        "max_pre_calm_west_minus_east_head_m": float(
            pre_calm["west_minus_east_eta_m"].max()
        ),
        "max_pre_calm_surface_head_span_m": float(
            pre_calm["surface_head_p95_p05_m"].max()
        ),
        "max_pre_calm_tilt_energy_j": float(
            pre_calm["surface_tilt_potential_energy_j"].max()
        ),
        "west_storage_gain_at_calm_m3": float(calm_row["west_zone_volume_m3"] - initial_west),
        "sill_flux_at_calm_m3_s": float(calm_row["sill_flux_m3_s"]),
        "sea_minus_lagoon_head_at_calm_m": float(calm_row["sea_minus_lagoon_head_m"]),
        "cumulative_boundary_inflow_at_calm_m3": float(calm_row["cumulative_boundary_inflow_m3"]),
        "post_calm_peak_route_speed_p95_m_s": post_speed_p95,
        "post_calm_peak_route_speed_max_m_s": post_speed_max,
        "post_calm_peak_route_hu_p95_m2_s": post_hu_p95,
        "post_calm_peak_route_hu_max_m2_s": post_hu_max,
        "post_calm_peak_depth_rise_cm_min": post_depth_rise,
        "post_calm_peak_width_loss_m_min": post_width_loss_rate,
        "post_calm_width_loss_fraction": width_loss_fraction,
        "post_calm_complete_lane_drop": lane_drop,
        "rewet_to_route_loss_h": rewet_to_loss_h,
        "alarm_proxy": alarm_proxy,
        "tide_phase_status": "sensitivity_clock_not_ancient_prediction",
    }


def build_cases() -> list[Case]:
    cases = [
        Case("combined_reference", 19.0, 0.15, 3.5, 4.0),
        Case("wind_only_control", 19.0, 0.0, 3.5, 4.0),
        Case("tide_only_control", 0.0, 0.15, 3.5, 4.0),
    ]
    for wind in (18.5, 19.0, 19.5):
        for low_clock in np.arange(2.5, 6.01, 0.5):
            for stop_clock in (3.5, 4.0, 4.5):
                cases.append(
                    Case(
                        f"phase_w{wind:.1f}_low{low_clock:04.1f}_stop{stop_clock:04.1f}",
                        wind,
                        0.15,
                        float(low_clock),
                        stop_clock,
                    )
                )
    return cases


def run(
    outdir: Path,
    nx: int,
    ny: int,
    selected: set[str] | None = None,
    wind_filter: set[float] | None = None,
) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    event_start = 16.0
    grid = GridSpec(60_000.0, 20_000.0, nx, ny)
    family = RIDGE_FAMILIES[0]
    records: list[dict[str, object]] = []
    all_cases = build_cases()
    if selected:
        all_cases = [case for case in all_cases if case.label in selected]
    elif wind_filter:
        all_cases = [
            case
            for case in all_cases
            if case.label.endswith("_control") or case.wind_m_s in wind_filter
        ]
    for index, case in enumerate(all_cases, 1):
        print(f"[{index}/{len(all_cases)}] {case.label}", flush=True)
        summary, rows = simulate_case(
            family,
            case.wind_m_s,
            grid,
            mean_stage_m=-0.20,
            tide_amplitude_m=case.tide_amplitude_m,
            low_tide_h=_hours_until(event_start, case.low_clock_h),
            output_interval_s=600.0,
            wind_full_h=6.0,
            wind_decay_h=3.0,
            wind_tail_m_s=12.0 if case.wind_m_s > 0.0 else 0.0,
            wind_ramp_h=1.0,
            geometry_mirrored_x=False,
            wind_direction_deg=180.0,
            geometry_factory=_geometry_factory(0.50),
            geometry_label="MI_EAST_RELIEF_V1_fixed_for_stage098",
            mobility_cases=CENTRAL_MIXED,
            traffic_horizons_h=(_hours_until(event_start, 5.5),),
            event_zero_local_hour=event_start,
            total_duration_h=_hours_until(event_start, 8.0),
            wind_tail_end_h=_hours_until(event_start, case.wind_stop_clock_h),
            wind_final_decay_h=0.5,
        )
        hydro = pd.DataFrame(row for row in rows if "mobility_case" not in row)
        traffic = pd.DataFrame(row for row in rows if "mobility_case" in row)
        record = analyse(case, summary, hydro)
        if len(traffic):
            parallel = traffic[traffic["network_bound"] == "parallel"]
            record["central_mixed_n_max_safe_by_0530"] = (
                float(parallel["n_max_safe_equivalent"].max()) if len(parallel) else 0.0
            )
            record["central_first_entry_clock"] = (
                str(parallel["first_entry_clock"].iloc[0]) if len(parallel) else ""
            )
            record["central_last_exit_clock"] = (
                str(parallel["last_exit_clock"].iloc[0]) if len(parallel) else ""
            )
        records.append(record)
        if case.label in {"combined_reference", "wind_only_control", "tide_only_control"} or selected:
            hydro.to_csv(outdir / f"timeseries_{case.label}_{nx}x{ny}.csv", index=False)

    frame = pd.DataFrame(records)
    frame.to_csv(outdir / f"screen_summary_{nx}x{ny}.csv", index=False)
    metadata = {
        "scope": "idealized wind-tide storage/release mechanism screen; no ancient reconstruction",
        "geometry": "MI_EAST_RELIEF_V1 with three resolved synthetic backbones",
        "grid": {"nx": nx, "ny": ny, "length_x_m": 60000.0, "width_y_m": 20000.0},
        "fixed": {
            "mean_stage_m": -0.20,
            "inlet_x_fraction": 0.50,
            "tide_amplitude_m": 0.15,
            "wind_direction": "east-to-west",
            "wind_peak_local": "17:00-22:00",
            "wind_decay_local": "22:00-01:00 to 12 m/s tail",
        },
        "alarm_proxy": {
            "noticeable": "at least 25% width loss, 0.10 m/s p95 return speed, or 0.05 cm/min route-depth rise",
            "urgent": "at least one complete lane lost and 50% width loss plus visible current, depth rise, or <=1.5 h route-loss clock",
            "acute": "local maximum h*u >= 0.70 m2/s; retained only as instability screen",
            "warning": "operational proxy, not a psychological or fatality model",
        },
    }
    (outdir / "run_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="outputs_stage098_wind_tide_release")
    parser.add_argument("--nx", type=int, default=60)
    parser.add_argument("--ny", type=int, default=48)
    parser.add_argument("--selected", default="")
    parser.add_argument("--wind-filter", default="")
    args = parser.parse_args()
    selected = {item for item in args.selected.split(",") if item}
    wind_filter = {
        float(item) for item in args.wind_filter.split(",") if item.strip()
    }
    run(
        Path(args.outdir),
        args.nx,
        args.ny,
        selected or None,
        wind_filter or None,
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Stage 0.99: frozen-hydro chariot/soil/queue mechanism screen.

This module does not rerun or modify Stage 0.98 hydrodynamics.  It reads one
archived time series as a read-only forcing record and places a deliberately
reduced, deterministic chariot queue model on top of it.

The soil numbers are sensitivity parameters, not recovered Ballah properties.
"kPa-equivalent support" is a mobility-screen index: it compares a declared
wheel/hoof demand with a surface whose support degrades under repeated passes
and rewetting.  It is not a full Bekker/Wong terramechanics calibration.

No casualty or drowning count is calculated.  Collision/trampling outputs are
exposure proxies only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
LOCKED_HYDRO = ROOT / "outputs_stage098_refine120" / (
    "timeseries_phase_w19.0_low04.5_stop04.0_120x96.csv"
)
LOCKED_SUMMARY = ROOT / "outputs_stage098_refine120" / "screen_summary_120x96.csv"
EVENT_ZERO_LOCAL_H = 16.0
CHOSEN_CHARIOTS = 600
CREW_PER_CHARIOT = 2
HORSES_PER_CHARIOT = 2
ROUTE_LENGTH_M = 7_000.0
BACKBONE_WIDTHS_M = (60.0, 45.0, 30.0)


@dataclass(frozen=True)
class SoilCase:
    name: str
    base_support_kpa: tuple[float, float, float]
    remould_fraction: float
    pass_scale: float
    rewet_sensitivity_per_m: float
    soft_patch_fraction: float = 0.0
    soft_patch_support_kpa: float = 120.0


@dataclass(frozen=True)
class TrafficCase:
    name: str
    entry_clock_h: float
    base_speed_m_s: float
    dynamic_envelope_m: float
    column_count: int
    entry_headway_s: float
    longitudinal_pitch_m: float
    team_length_m: float
    wheel_demand_kpa: float
    hoof_demand_kpa: float
    recognition_delay_min: float
    turn_delay_min: float
    turn_success_fraction: float
    route_choice_error_fraction: float = 0.0


@dataclass
class RunResult:
    soil_case: str
    traffic_case: str
    chosen_chariots: int
    entrants: int
    reached_far_shore: int
    returned_to_origin: int
    immobilized: int
    first_failure_position_m: float | None
    trapped_at_hydro_closure: int
    outside_at_hydro_closure: int
    first_entry_clock: str | None
    first_mobility_failure_clock: str | None
    retreat_recognition_clock: str | None
    first_return_cue_clock: str
    all_route_closed_clock: str
    mobility_before_return_gate: bool
    entrants_before_morning_disturbance_gate: bool
    all_600_reach_far_shore: bool
    all_mobile_can_retreat: bool
    max_in_network: int
    max_queued: int
    immobilized_lane_count: int
    collision_conflict_exposures: int
    compressed_queue_chariot_minutes: float
    crew_horse_interaction_exposure_person_minutes: float
    closest_approach_to_israelite_rear_m: float
    pursuit_contact_proxy: bool
    casualties_simulated: bool = False


SOILS = (
    SoilCase(
        "firm_sand_control",
        (520.0, 480.0, 440.0),
        remould_fraction=0.18,
        pass_scale=120.0,
        rewet_sensitivity_per_m=0.8,
    ),
    SoilCase(
        "marginal_wet_sand",
        (390.0, 350.0, 320.0),
        remould_fraction=0.48,
        pass_scale=55.0,
        rewet_sensitivity_per_m=2.0,
    ),
    SoilCase(
        "patchy_sand_over_soft",
        (420.0, 360.0, 315.0),
        remould_fraction=0.58,
        pass_scale=42.0,
        rewet_sensitivity_per_m=2.8,
        soft_patch_fraction=0.08,
        soft_patch_support_kpa=155.0,
    ),
)


TRAFFIC = (
    TrafficCase(
        "central_dense",
        entry_clock_h=4.00,
        base_speed_m_s=1.8,
        dynamic_envelope_m=3.0,
        column_count=12,
        entry_headway_s=8.0,
        longitudinal_pitch_m=10.0,
        team_length_m=6.0,
        wheel_demand_kpa=220.0,
        hoof_demand_kpa=300.0,
        recognition_delay_min=6.0,
        turn_delay_min=3.0,
        turn_success_fraction=0.55,
    ),
    TrafficCase(
        "central_dense_high_turnability",
        entry_clock_h=4.00,
        base_speed_m_s=1.8,
        dynamic_envelope_m=3.0,
        column_count=12,
        entry_headway_s=8.0,
        longitudinal_pitch_m=10.0,
        team_length_m=6.0,
        wheel_demand_kpa=220.0,
        hoof_demand_kpa=300.0,
        recognition_delay_min=6.0,
        turn_delay_min=3.0,
        turn_success_fraction=0.90,
    ),
    TrafficCase(
        "central_dense_low_turnability",
        entry_clock_h=4.00,
        base_speed_m_s=1.8,
        dynamic_envelope_m=3.0,
        column_count=12,
        entry_headway_s=8.0,
        longitudinal_pitch_m=10.0,
        team_length_m=6.0,
        wheel_demand_kpa=220.0,
        hoof_demand_kpa=300.0,
        recognition_delay_min=6.0,
        turn_delay_min=3.0,
        turn_success_fraction=0.20,
    ),
    TrafficCase(
        "optimistic_spacing",
        entry_clock_h=3.75,
        base_speed_m_s=2.2,
        dynamic_envelope_m=2.5,
        column_count=16,
        entry_headway_s=10.0,
        longitudinal_pitch_m=14.0,
        team_length_m=6.0,
        wheel_demand_kpa=190.0,
        hoof_demand_kpa=270.0,
        recognition_delay_min=4.0,
        turn_delay_min=2.0,
        turn_success_fraction=0.80,
    ),
    TrafficCase(
        "compressed_disorder",
        entry_clock_h=4.25,
        base_speed_m_s=1.5,
        dynamic_envelope_m=4.0,
        column_count=9,
        entry_headway_s=6.0,
        longitudinal_pitch_m=7.0,
        team_length_m=6.0,
        wheel_demand_kpa=250.0,
        hoof_demand_kpa=340.0,
        recognition_delay_min=8.0,
        turn_delay_min=5.0,
        turn_success_fraction=0.30,
    ),
    TrafficCase(
        "soft_edge_error_5pct",
        entry_clock_h=4.00,
        base_speed_m_s=1.8,
        dynamic_envelope_m=3.0,
        column_count=12,
        entry_headway_s=8.0,
        longitudinal_pitch_m=10.0,
        team_length_m=6.0,
        wheel_demand_kpa=220.0,
        hoof_demand_kpa=300.0,
        recognition_delay_min=6.0,
        turn_delay_min=3.0,
        turn_success_fraction=0.55,
        route_choice_error_fraction=0.05,
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clock_to_elapsed(clock_h: float) -> float:
    return (clock_h - EVENT_ZERO_LOCAL_H) % 24.0


def elapsed_to_clock(elapsed_h: float | None) -> str | None:
    if elapsed_h is None or not math.isfinite(elapsed_h):
        return None
    seconds = int(round(((EVENT_ZERO_LOCAL_H + elapsed_h) % 24.0) * 3600.0))
    return (
        f"{(seconds // 3600) % 24:02d}:"
        f"{(seconds % 3600) // 60:02d}:{seconds % 60:02d}"
    )


def _deterministic_patch(lane: int, segment: int, fraction: float) -> bool:
    if fraction <= 0.0:
        return False
    token = (lane * 73_856_093 + segment * 19_349_663 + 83_492_791) % 10_000
    return token < round(fraction * 10_000)


def _deterministic_fraction(vehicle: int, segment: int) -> float:
    token = (vehicle * 2_654_435_761 + segment * 2_246_822_519) & 0xFFFFFFFF
    return token / 0xFFFFFFFF


def _interpolator(hydro: pd.DataFrame, column: str):
    x = hydro["time_h"].to_numpy(float)
    y = hydro[column].to_numpy(float)

    def value(t: float) -> float:
        return float(np.interp(t, x, y))

    return value


def _locked_clocks() -> tuple[float, float]:
    summary = pd.read_csv(LOCKED_SUMMARY)
    row = summary[summary["case"] == "phase_w19.0_low04.5_stop04.0"].iloc[0]

    def parse(value: str) -> float:
        hour, minute = (int(item) for item in value.split(":"))
        return clock_to_elapsed(hour + minute / 60.0)

    return parse(str(row["route_local_rewet_2cm_clock"])), parse(
        str(row["all_segments_closed_clock"])
    )


def _backbone_for_column(column: int, count: int) -> int:
    # Proportional allocation by the frozen 60:45:30 m width ratio.
    cumulative = np.cumsum(np.asarray(BACKBONE_WIDTHS_M) / sum(BACKBONE_WIDTHS_M))
    fraction = (column + 0.5) / count
    return int(np.searchsorted(cumulative, fraction, side="right"))


def simulate(
    soil: SoilCase,
    traffic: TrafficCase,
    dt_s: float = 5.0,
    event_log: list[dict[str, object]] | None = None,
    state_archive: dict[str, object] | None = None,
    snapshot_times_h: tuple[float, ...] = (),
    route_length_m: float = ROUTE_LENGTH_M,
    israelite_rear_exit_clock_h: float = 5.5,
    israelite_rear_speed_m_s: float = 0.60,
) -> RunResult:
    hydro = pd.read_csv(LOCKED_HYDRO)
    active_width = _interpolator(hydro, "active_aggregate_width_m")
    route_depth = _interpolator(hydro, "resolved_route_probe_median_depth_m")
    rewet_h, closure_h = _locked_clocks()
    entry_h = clock_to_elapsed(traffic.entry_clock_h)
    morning_disturbance_h = clock_to_elapsed(5.5)  # declared model clock, not translation
    segment_count = 28
    segment_m = route_length_m / segment_count

    n = CHOSEN_CHARIOTS
    lane = np.arange(n, dtype=int) % traffic.column_count
    order = np.arange(n, dtype=int) // traffic.column_count
    entry_time = entry_h + order * traffic.entry_headway_s / 3600.0
    position = np.full(n, -1.0, dtype=float)
    status = np.zeros(n, dtype=np.int8)  # 0 outside,1 outbound,2 far,3 immobile,4 turning,5 returning,6 origin,7 trapped
    turn_ready = np.full(n, np.inf)
    last_segment = np.full(n, -1, dtype=int)
    pass_count = np.zeros((traffic.column_count, segment_count), dtype=int)
    blocked = np.zeros((traffic.column_count, segment_count), dtype=bool)
    ever_immobilized = np.zeros(n, dtype=bool)
    first_failure_h: float | None = None
    first_failure_position_m: float | None = None
    recognition_h: float | None = None
    collision_exposure = 0
    max_in_network = 0
    max_queued = 0
    queue_vehicle_seconds = 0.0
    crew_horse_person_seconds = 0.0
    closest_gap = route_length_m
    first_contact_h: float | None = None

    # The last locked mixed group is represented only as a rear trajectory.
    # 0.60 m/s over 7 km ending at 05:30 implies a last-entry clock ~02:16.
    israelite_rear_exit_h = clock_to_elapsed(israelite_rear_exit_clock_h)
    israelite_rear_entry_h = (
        israelite_rear_exit_h
        - route_length_m / israelite_rear_speed_m_s / 3600.0
    )

    start = entry_h
    stop = closure_h + 20.0 / 60.0
    steps = int(math.ceil((stop - start) * 3600.0 / dt_s)) + 1
    pending_snapshots = sorted(float(value) for value in snapshot_times_h)
    snapshot_index = 0
    if state_archive is not None:
        state_archive.setdefault("snapshots", [])
    for step in range(steps):
        t = start + step * dt_s / 3600.0
        newly = (status == 0) & (entry_time <= t) & (active_width(t) > 0.0)
        status[newly] = 1
        position[newly] = 0.0

        if first_failure_h is not None and recognition_h is None:
            recognition_h = first_failure_h + traffic.recognition_delay_min / 60.0
        if recognition_h is not None:
            candidates = (status == 1) & (turn_ready == np.inf)
            # Dense-queue turning is a deterministic sensitivity, not chance.
            eligible = np.array(
                [
                    _deterministic_fraction(int(i), 997) < traffic.turn_success_fraction
                    for i in np.flatnonzero(candidates)
                ],
                dtype=bool,
            )
            indices = np.flatnonzero(candidates)
            turners = indices[eligible]
            nonturners = indices[~eligible]
            status[turners] = 4
            turn_ready[turners] = recognition_h + traffic.turn_delay_min / 60.0
            # Non-turners remain outbound/queued; they are not declared dead.
            status[nonturners] = 1
        ready = (status == 4) & (turn_ready <= t)
        status[ready] = 5

        open_columns = min(
            traffic.column_count,
            max(0, int(active_width(t) // traffic.dynamic_envelope_m)),
        )
        closed_column = lane >= open_columns
        moving_mask = ((status == 1) | (status == 5)) & closed_column
        status[moving_mask & (t >= closure_h)] = 7

        depth = route_depth(t)
        depth_min = float(hydro["resolved_route_probe_median_depth_m"].min())
        rewet_excess = max(0.0, depth - depth_min)

        # Fixed lane order prevents overtaking; the declared pitch sets density.
        queued_now = 0
        for col in range(traffic.column_count):
            ids = np.flatnonzero(lane == col)
            # Outbound: leaders have smaller order values.
            for idx in ids:
                if status[idx] != 1:
                    continue
                seg = min(segment_count - 1, max(0, int(position[idx] // segment_m)))
                if blocked[col, seg] or col >= open_columns:
                    queued_now += 1
                    continue
                ahead = ids[(order[ids] < order[idx]) & np.isin(status[ids], [1, 3, 4])]
                cap = route_length_m
                if len(ahead):
                    nearest = ahead[np.argmin(np.maximum(0.0, position[ahead] - position[idx]))]
                    if position[nearest] >= position[idx]:
                        cap = position[nearest] - traffic.longitudinal_pitch_m
                proposed = min(cap, position[idx] + traffic.base_speed_m_s * dt_s)
                new_seg = min(segment_count - 1, max(0, int(proposed // segment_m)))
                if new_seg > last_segment[idx]:
                    backbone = _backbone_for_column(col, traffic.column_count)
                    support = soil.base_support_kpa[backbone]
                    # A declared 1 km firm entrance apron prevents the model
                    # from trapping vehicles before they have meaningfully
                    # entered the sea-space.  This is a substrate hypothesis,
                    # not a Stage 0.98 terrain alteration or an ancient fact.
                    firm_apron = new_seg < 4
                    if firm_apron:
                        support = max(support, 520.0)
                    if (
                        not firm_apron
                        and _deterministic_patch(col, new_seg, soil.soft_patch_fraction)
                    ):
                        support = min(support, soil.soft_patch_support_kpa)
                    passes = pass_count[col, new_seg]
                    remould = (
                        0.0
                        if firm_apron
                        else min(
                            soil.remould_fraction,
                            soil.remould_fraction * passes / soil.pass_scale,
                        )
                    )
                    support *= max(0.05, 1.0 - remould)
                    support *= max(0.25, 1.0 - soil.rewet_sensitivity_per_m * rewet_excess)
                    demand = max(traffic.wheel_demand_kpa, traffic.hoof_demand_kpa)
                    if (
                        traffic.route_choice_error_fraction > 0.0
                        and _deterministic_fraction(int(idx), new_seg)
                        < traffic.route_choice_error_fraction
                    ):
                        support = min(support, soil.soft_patch_support_kpa)
                    pass_count[col, new_seg] += 1
                    if support < demand:
                        status[idx] = 3
                        ever_immobilized[idx] = True
                        position[idx] = new_seg * segment_m
                        blocked[col, new_seg] = True
                        if event_log is not None:
                            event_log.append(
                                {
                                    "event": "mobility_failure",
                                    "time_h": t,
                                    "clock": elapsed_to_clock(t),
                                    "vehicle": int(idx),
                                    "column": int(col),
                                    "backbone": int(backbone),
                                    "segment": int(new_seg),
                                    "position_m": float(position[idx]),
                                    "support_kpa_equivalent": float(support),
                                    "demand_kpa_equivalent": float(demand),
                                    "rewet_excess_m": float(rewet_excess),
                                    "prior_passes": int(passes),
                                    "firm_apron": bool(firm_apron),
                                }
                            )
                        if first_failure_h is None:
                            first_failure_h = t
                            first_failure_position_m = position[idx]
                        # Conflict proxy: followers closer than reaction + braking distance.
                        reaction_brake = traffic.base_speed_m_s * 1.5 + traffic.base_speed_m_s**2 / 2.0
                        followers = ids[(order[ids] > order[idx]) & (status[ids] == 1)]
                        collision_exposure += int(
                            np.sum(
                                (
                                    position[idx]
                                    - position[followers]
                                    - traffic.team_length_m
                                )
                                <= reaction_brake
                            )
                        )
                        continue
                    last_segment[idx] = new_seg
                position[idx] = proposed
                if position[idx] >= route_length_m - 1e-6:
                    position[idx] = route_length_m
                    status[idx] = 2

            # Returners: those closest to origin leave first.
            returning = ids[status[ids] == 5]
            for idx in returning[np.argsort(position[returning])]:
                ahead_home = returning[position[returning] < position[idx]]
                floor = 0.0
                if len(ahead_home):
                    nearest = ahead_home[np.argmax(position[ahead_home])]
                    floor = position[nearest] + traffic.longitudinal_pitch_m
                position[idx] = max(floor, position[idx] - 0.75 * traffic.base_speed_m_s * dt_s)
                if position[idx] <= 1e-6:
                    position[idx] = 0.0
                    status[idx] = 6

        if t >= closure_h:
            status[np.isin(status, [1, 3, 4, 5])] = 7

        while (
            state_archive is not None
            and snapshot_index < len(pending_snapshots)
            and t >= pending_snapshots[snapshot_index]
        ):
            state_archive["snapshots"].append(
                {
                    "requested_time_h": pending_snapshots[snapshot_index],
                    "captured_time_h": float(t),
                    "clock": elapsed_to_clock(t),
                    "vehicle": np.arange(n, dtype=int).copy(),
                    "column": lane.copy(),
                    "position_m": position.copy(),
                    "status": status.copy(),
                    "ever_immobilized": ever_immobilized.copy(),
                    # Optional forensic state.  These arrays do not affect the
                    # Stage 0.99 dynamics or legacy outputs; later audits need
                    # them to test whether a return trip can traverse the same
                    # already-trafficked and locally blocked surface.
                    "last_segment": last_segment.copy(),
                    "pass_count": pass_count.copy(),
                    "blocked": blocked.copy(),
                }
            )
            snapshot_index += 1

        in_network = int(np.sum(np.isin(status, [1, 3, 4, 5, 7])))
        max_in_network = max(max_in_network, in_network)
        max_queued = max(max_queued, queued_now)
        queue_vehicle_seconds += queued_now * dt_s
        immobilized_in_queue = int(np.sum(status == 3))
        crew_horse_person_seconds += immobilized_in_queue * CREW_PER_CHARIOT * dt_s

        rear_position = min(
            route_length_m,
            max(
                0.0,
                (t - israelite_rear_entry_h)
                * 3600.0
                * israelite_rear_speed_m_s,
            ),
        )
        outbound = position[status == 1]
        if len(outbound) and rear_position < route_length_m:
            raw_gap = rear_position - float(outbound.max())
            closest_gap = min(closest_gap, max(0.0, raw_gap))
            if raw_gap <= 0.0 and first_contact_h is None:
                first_contact_h = t
                if event_log is not None:
                    event_log.append(
                        {
                            "event": "pursuit_contact",
                            "time_h": t,
                            "clock": elapsed_to_clock(t),
                            "israelite_rear_position_m": float(rear_position),
                            "leading_chariot_position_m": float(outbound.max()),
                        }
                    )

    entrants = int(np.sum(status != 0))
    immobilized = int(np.sum(ever_immobilized))
    trapped = int(np.sum(status == 7))
    outside = int(np.sum(status == 0))
    first_entry_clock = elapsed_to_clock(float(entry_time[status != 0].min())) if entrants else None
    result = RunResult(
        soil_case=soil.name,
        traffic_case=traffic.name,
        chosen_chariots=n,
        entrants=entrants,
        reached_far_shore=int(np.sum(status == 2)),
        returned_to_origin=int(np.sum(status == 6)),
        immobilized=immobilized,
        first_failure_position_m=first_failure_position_m,
        trapped_at_hydro_closure=trapped,
        outside_at_hydro_closure=outside,
        first_entry_clock=first_entry_clock,
        first_mobility_failure_clock=elapsed_to_clock(first_failure_h),
        retreat_recognition_clock=elapsed_to_clock(recognition_h),
        first_return_cue_clock=elapsed_to_clock(rewet_h) or "",
        all_route_closed_clock=elapsed_to_clock(closure_h) or "",
        mobility_before_return_gate=(first_failure_h is not None and first_failure_h < rewet_h),
        entrants_before_morning_disturbance_gate=(entry_h < morning_disturbance_h and entrants > 0),
        all_600_reach_far_shore=int(np.sum(status == 2)) == CHOSEN_CHARIOTS,
        all_mobile_can_retreat=(int(np.sum(status == 6)) + int(np.sum(status == 2)) == entrants),
        max_in_network=max_in_network,
        max_queued=max_queued,
        immobilized_lane_count=int(np.sum(blocked.any(axis=1))),
        collision_conflict_exposures=collision_exposure,
        compressed_queue_chariot_minutes=queue_vehicle_seconds / 60.0,
        crew_horse_interaction_exposure_person_minutes=crew_horse_person_seconds / 60.0,
        closest_approach_to_israelite_rear_m=closest_gap,
        pursuit_contact_proxy=closest_gap <= 1e-6,
    )
    if state_archive is not None:
        state_archive.update(
            {
                "soil_case": soil.name,
                "traffic_case": traffic.name,
                "route_length_m": route_length_m,
                "israelite_rear_exit_clock_h": israelite_rear_exit_clock_h,
                "israelite_rear_speed_m_s": israelite_rear_speed_m_s,
                "first_contact_clock": elapsed_to_clock(first_contact_h),
                "column_count": traffic.column_count,
                "backbone_widths_m": BACKBONE_WIDTHS_M,
                "status_codes": {
                    0: "outside",
                    1: "outbound",
                    2: "far_shore",
                    3: "immobile",
                    4: "turning",
                    5: "returning",
                    6: "origin",
                    7: "trapped_at_hydro_closure",
                },
            }
        )
    return result


def run(outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    locked = {
        "hydro_path": str(LOCKED_HYDRO.relative_to(ROOT)),
        "hydro_sha256": sha256(LOCKED_HYDRO),
        "summary_path": str(LOCKED_SUMMARY.relative_to(ROOT)),
        "summary_sha256": sha256(LOCKED_SUMMARY),
        "world_status": "READ_ONLY_STAGE098",
        "chosen_chariots": CHOSEN_CHARIOTS,
        "crew_per_chariot": CREW_PER_CHARIOT,
        "horses_per_chariot": HORSES_PER_CHARIOT,
        "route_length_m": ROUTE_LENGTH_M,
        "backbone_widths_m": BACKBONE_WIDTHS_M,
        "soil_calibration_status": "sensitivity_not_Ballah_calibration",
        "fatality_model": False,
    }
    (outdir / "frozen_inputs.json").write_text(
        json.dumps(locked, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    rows = [asdict(simulate(soil, traffic)) for soil in SOILS for traffic in TRAFFIC]
    pd.DataFrame(rows).to_csv(outdir / "chariot_soil_screen.csv", index=False)
    (outdir / "parameter_manifest.json").write_text(
        json.dumps(
            {
                "soils": [asdict(item) for item in SOILS],
                "traffic": [asdict(item) for item in TRAFFIC],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="outputs_stage099_chariot_soil")
    args = parser.parse_args()
    run(ROOT / args.outdir)


if __name__ == "__main__":
    main()

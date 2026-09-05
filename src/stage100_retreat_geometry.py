#!/usr/bin/env python3
"""Stage 1.00: geometry-derived chariot retreat and crew-abandonment bounds.

Reads Stage 0.99 results as immutable inputs.  It does not rerun soil or hydro.
The model replaces hand-set turn-success fractions with explicit swept-width,
turn-service-time, and available-firm-width sensitivities.  It separately asks
whether crew could abandon vehicles and retreat on foot.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "outputs_stage099_chariot_soil" / "chariot_soil_screen.csv"
OUTDIR = ROOT / "outputs_stage100_retreat_geometry"
BACKBONES_M = (60.0, 45.0, 30.0)
COLUMNS = (5, 4, 3)
DYNAMIC_ENVELOPE_M = 3.0
ROUTE_LENGTH_M = 7_000.0
RECOGNITION_CLOCK_H = 4.25  # 04:15 central Stage 0.99
REWET_CLOCK_H = 5.0 + 40.0 / 60.0
CLOSURE_CLOCK_H = 6.0 + 40.0 / 60.0
RETURN_SPEED_M_S = 1.35
FIRST_FAILURE_POSITION_M = 1_000.0


def sha256(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return digest


def available_pockets(
    swept_width_m: float,
    usable_width_fraction: float,
    mode: str,
) -> int:
    total = 0
    for width, columns in zip(BACKBONES_M, COLUMNS):
        usable = width * usable_width_fraction
        if mode == "shoulder_only":
            turn_width = max(0.0, usable - columns * DYNAMIC_ENVELOPE_M)
        elif mode == "full_width_after_halt":
            turn_width = usable
        else:
            raise ValueError(mode)
        total += int(turn_width // swept_width_m)
    return total


def vehicle_retreat_rows(frame: pd.DataFrame) -> list[dict[str, object]]:
    source = frame[
        (frame["traffic_case"] == "central_dense")
        & frame["soil_case"].isin(["marginal_wet_sand", "patchy_sand_over_soft"])
    ]
    rows: list[dict[str, object]] = []
    time_to_closure_s = (CLOSURE_CLOCK_H - RECOGNITION_CLOCK_H) * 3600.0
    travel_back_s = FIRST_FAILURE_POSITION_M / RETURN_SPEED_M_S
    service_window_s = max(0.0, time_to_closure_s - travel_back_s)
    for _, item in source.iterrows():
        mobile_candidates = int(
            item["entrants"] - item["reached_far_shore"] - item["immobilized"]
        )
        for mode in ("shoulder_only", "full_width_after_halt"):
            for usable_fraction in (1.0, 0.75, 0.50):
                for swept in (10.0, 15.0, 20.0):
                    for turn_time in (30.0, 45.0, 60.0):
                        pockets = available_pockets(swept, usable_fraction, mode)
                        capacity = pockets * int(service_window_s // turn_time)
                        returned = min(mobile_candidates, capacity)
                        trapped_vehicles = int(item["immobilized"]) + (
                            mobile_candidates - returned
                        )
                        rows.append(
                            {
                                "soil_case": item["soil_case"],
                                "turn_mode": mode,
                                "usable_firm_width_fraction": usable_fraction,
                                "swept_turn_width_m": swept,
                                "turn_service_s": turn_time,
                                "turn_pockets": pockets,
                                "service_window_min": service_window_s / 60.0,
                                "far_shore_before_retreat": int(item["reached_far_shore"]),
                                "actually_immobilized": int(item["immobilized"]),
                                "mobile_retreat_candidates": mobile_candidates,
                                "vehicle_turn_capacity": capacity,
                                "vehicles_returned_bound": returned,
                                "vehicles_trapped_bound": trapped_vehicles,
                                "no_far_shore_escape_gate": int(item["reached_far_shore"]) == 0,
                                "no_vehicle_return_gate": returned == 0,
                            }
                        )
    return rows


def crew_escape_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for decision_clock, decision_label in (
        (RECOGNITION_CLOCK_H, "dismount_at_recognition_0415"),
        (REWET_CLOCK_H, "dismount_at_first_rewet_cue_0540"),
    ):
        to_rewet_s = max(0.0, REWET_CLOCK_H - decision_clock) * 3600.0
        to_closure_s = max(0.0, CLOSURE_CLOCK_H - decision_clock) * 3600.0
        for speed in (0.5, 0.8, 1.0, 1.3):
            before_rewet = speed * to_rewet_s
            before_closure = speed * to_closure_s
            rows.append(
                {
                    "decision": decision_label,
                    "foot_speed_m_s": speed,
                    "distance_reachable_before_rewet_m": before_rewet,
                    "distance_reachable_before_closure_m": before_closure,
                    "first_failure_at_1km_can_reach_origin_before_rewet": (
                        FIRST_FAILURE_POSITION_M <= before_rewet
                    ),
                    "first_failure_at_1km_can_reach_origin_before_closure": (
                        FIRST_FAILURE_POSITION_M <= before_closure
                    ),
                    "entire_7km_route_recoverable_before_closure": (
                        ROUTE_LENGTH_M <= before_closure
                    ),
                }
            )
    return rows


def run() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    frame = pd.read_csv(INPUT)
    vehicles = pd.DataFrame(vehicle_retreat_rows(frame))
    crew = pd.DataFrame(crew_escape_rows())
    vehicles.to_csv(OUTDIR / "vehicle_turn_bounds.csv", index=False)
    crew.to_csv(OUTDIR / "crew_abandonment_bounds.csv", index=False)
    manifest = {
        "input": str(INPUT.relative_to(ROOT)),
        "input_sha256": sha256(INPUT),
        "stage099_status": "READ_ONLY",
        "backbones_m": BACKBONES_M,
        "columns": COLUMNS,
        "dynamic_envelope_m": DYNAMIC_ENVELOPE_M,
        "turn_numeric_status": "geometry_sensitivity_not_ancient_calibration",
        "recognition_clock": "04:15",
        "first_rewet_cue": "05:40",
        "closure_clock": "06:40",
        "casualties_simulated": False,
    }
    (OUTDIR / "frozen_stage099_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    run()

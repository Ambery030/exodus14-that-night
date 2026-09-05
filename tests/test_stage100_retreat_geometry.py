import pandas as pd

from stage100_retreat_geometry import (
    INPUT,
    available_pockets,
    crew_escape_rows,
    sha256,
    vehicle_retreat_rows,
)


def test_stage099_input_is_frozen():
    assert sha256(INPUT) == "05ecb2af255b86bd5db2a70b1c8f816673394b6a4389deadb6c2f62eed8f6031"


def test_more_usable_width_never_reduces_turn_pockets():
    for swept in (10.0, 15.0, 20.0):
        narrow = available_pockets(swept, 0.50, "shoulder_only")
        full = available_pockets(swept, 1.00, "shoulder_only")
        assert full >= narrow


def test_vehicle_bookkeeping_is_bounded():
    rows = vehicle_retreat_rows(pd.read_csv(INPUT))
    for row in rows:
        assert 0 <= row["vehicles_returned_bound"] <= row["mobile_retreat_candidates"]
        accounted = (
            row["far_shore_before_retreat"]
            + row["vehicles_returned_bound"]
            + row["vehicles_trapped_bound"]
        )
        assert accounted == 600


def test_first_failure_crew_can_walk_back_before_closure_in_all_speeds():
    for row in crew_escape_rows():
        assert row["first_failure_at_1km_can_reach_origin_before_closure"] is True


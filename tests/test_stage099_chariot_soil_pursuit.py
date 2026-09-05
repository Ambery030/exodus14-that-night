from stage099_chariot_soil_pursuit import (
    CHOSEN_CHARIOTS,
    LOCKED_HYDRO,
    SOILS,
    TRAFFIC,
    sha256,
    simulate,
)


def test_locked_hydro_hash_is_stable():
    assert sha256(LOCKED_HYDRO) == "050c0abccddf3db2c7997dc79c40d4b7d1cd6ac7253460909459904c0d85d5f3"


def test_firm_control_does_not_manufacture_failure():
    result = simulate(SOILS[0], TRAFFIC[0])
    assert result.chosen_chariots == CHOSEN_CHARIOTS
    assert result.reached_far_shore == CHOSEN_CHARIOTS
    assert result.immobilized == 0
    assert result.casualties_simulated is False


def test_marginal_case_enters_before_failure_and_fails_before_return():
    result = simulate(SOILS[1], TRAFFIC[0])
    assert result.entrants == CHOSEN_CHARIOTS
    assert result.first_failure_position_m is not None
    assert result.first_failure_position_m >= 1_000.0
    assert result.mobility_before_return_gate is True
    assert result.casualties_simulated is False


def test_bookkeeping_never_creates_or_kills_chariots():
    result = simulate(SOILS[2], TRAFFIC[2])
    accounted = (
        result.reached_far_shore
        + result.returned_to_origin
        + result.trapped_at_hydro_closure
        + result.outside_at_hydro_closure
    )
    assert accounted == CHOSEN_CHARIOTS
    assert result.immobilized <= result.trapped_at_hydro_closure


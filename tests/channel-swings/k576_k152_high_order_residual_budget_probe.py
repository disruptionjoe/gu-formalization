#!/usr/bin/env python3
"""Independent controls and hostile mutations for K576."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k576_probe_target", HERE / "k576_k152_high_order_residual_budget.py")
K576 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K576)


def checks(payload: dict) -> list[bool]:
    partition = payload["orthogonal_partition"]
    controls = payload["controls"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K576-K152-HIGH-ORDER-RESIDUAL-BUDGET",
        partition["low_orders"] == [2, 3, 4, 5, 6, 7],
        partition["high_orders"] == [8, 9, 10, 11, 12],
        partition["all_low_order_coherent_cross_terms_retained"] is True,
        partition["all_high_order_coherent_cross_terms_must_be_retained"] is True,
        payload["budget_identity"]["equal_share_is_sufficient_not_required"] is True,
        controls["target_count"] == 6,
        controls["positive_high_order_allowance_count"] == 5,
        controls["low_order_tightening_required_count"] == 1,
        controls["low_order_tightening_target_labels"] == ["projection_sine=1/10"],
        controls["loosest_projection_25_over_9_high_order_allowance_exact"] is not None,
        decision["orders_two_through_seven_already_fit_projection_sine_one_half_budget"] is True,
        decision["orders_eight_through_twelve_are_the_first_target_for_projection_sine_one_half"] is True,
        decision["projection_sine_one_tenth_also_requires_low_order_tightening"] is True,
        decision["equal_share_is_a_planning_allocation_not_a_mathematical_necessity"] is True,
        decision["complete_reference_specific_floor_still_required"] is True,
        decision["native_K152_interval_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K576.build()
    controls = checks(payload)
    rejected = 0
    mutations = [
        lambda p: p["orthogonal_partition"].__setitem__("low_orders", [2, 3, 4, 5, 6]),
        lambda p: p["orthogonal_partition"].__setitem__("high_orders", [7, 8, 9, 10, 11, 12]),
        lambda p: p["orthogonal_partition"].__setitem__("all_low_order_coherent_cross_terms_retained", False),
        lambda p: p["controls"].__setitem__("positive_high_order_allowance_count", 6),
        lambda p: p["controls"].__setitem__("low_order_tightening_required_count", 0),
        lambda p: p["controls"].__setitem__("low_order_tightening_target_labels", []),
        lambda p: p["decision"].__setitem__("orders_two_through_seven_already_fit_projection_sine_one_half_budget", False),
        lambda p: p["decision"].__setitem__("projection_sine_one_tenth_also_requires_low_order_tightening", False),
        lambda p: p["decision"].__setitem__("complete_reference_specific_floor_still_required", False),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K576.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K576 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())

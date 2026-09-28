#!/usr/bin/env python3
"""Independent controls and hostile mutations for K579."""

from __future__ import annotations

import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k579_probe_target", HERE / "k579_k577_order_eight_group_complete_uppers.py")
K579 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K579)


def checks(payload: dict) -> list[bool]:
    fixed = payload["fixed_control"]
    rows = payload["group_complete_upper_bank"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K579-K577-ORDER-EIGHT-GROUP-COMPLETE-UPPERS",
        fixed["groups"] == 23,
        fixed["ordered_descriptors"] == 2400,
        fixed["hybrid_terms_per_group"] == 18,
        fixed["face_programs_reused"] == 517,
        fixed["low_coordinate_subsets_replayed_per_complete_cover"] == 524286,
        Fraction(fixed["group_second_derivative_sum_exact"]) == Fraction(fixed["complete_second_derivative_abs_upper_exact"]),
        Fraction(fixed["group_raw_remainder_sum_exact"]) == Fraction(fixed["raw_complete_remainder_exact"]),
        len(rows) == 23,
        sum(row["ordered_descriptors"] for row in rows) == 2400,
        all(Fraction(row["normalized_complete_integral_abs_upper_exact"]) > 0 for row in rows),
        payload["linearity_theorem"]["cross_terms_retained"] is True,
        payload["linearity_theorem"]["occurrencewise_absolute_value_used"] is False,
        decision["all_order_eight_groups_have_complete_noncompact_upper"] is True,
        decision["K577_targets_met"] + decision["K577_targets_failed"] == 23,
        decision["complete_order_eight_signed_sum_retracted"] is False,
        decision["native_K152_interval_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K579.build()
    controls = checks(payload)
    mutations = [
        lambda p: p["fixed_control"].__setitem__("groups", 22),
        lambda p: p["fixed_control"].__setitem__("ordered_descriptors", 2399),
        lambda p: p["fixed_control"].__setitem__("group_second_derivative_sum_exact", "0"),
        lambda p: p["fixed_control"].__setitem__("group_raw_remainder_sum_exact", "0"),
        lambda p: p["group_complete_upper_bank"].pop(),
        lambda p: p["group_complete_upper_bank"][0].__setitem__("normalized_complete_integral_abs_upper_exact", "0"),
        lambda p: p["linearity_theorem"].__setitem__("cross_terms_retained", False),
        lambda p: p["linearity_theorem"].__setitem__("occurrencewise_absolute_value_used", True),
        lambda p: p["decision"].__setitem__("all_order_eight_groups_have_complete_noncompact_upper", False),
        lambda p: p["decision"].__setitem__("K577_targets_failed", 0),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K579.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K579 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())

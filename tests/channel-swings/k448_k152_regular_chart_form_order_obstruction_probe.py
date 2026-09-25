#!/usr/bin/env python3
"""Independent controls and hostile mutations for K448."""

from __future__ import annotations

import copy
import json

from k448_k152_regular_chart_form_order_obstruction import demo


def controls(r: dict) -> list[bool]:
    raw, regular, decision = r["raw_cutoff_forms"], r["regular_chart_forms"], r["decision"]
    return [
        r["classification"] == "INTERNAL_STRUCTURAL_ONLY", r["direction"] == "observed_to_native",
        raw["defect_inertias"] == [[8, 0, 0], [7, 0, 0], [7, 0, 0]],
        raw["fine_compression_strictly_above_independent_coarse_form"] is True,
        raw["all_three_sectors_positive_definite"] is True,
        regular["defect_inertias"] == [[5, 3, 0], [5, 2, 0], [5, 2, 0]],
        regular["all_three_sectors_indefinite"] is True,
        regular["fine_compression_ge_independent_coarse"] is False,
        regular["fine_compression_le_independent_coarse"] is False,
        regular["one_sided_minmax_transfer_available"] is False,
        regular["nonlinear_regular_pullback_preserves_raw_form_order"] is False,
        decision["K163_first_entry_was_isolated_accident"] is False,
        decision["obstruction_is_full_rank_and_sector_wide"] is True,
        decision["independent_rediscretization_can_supply_native_K152_gap"] is False,
        decision["requires_exact_compression_or_two_sided_defect_bound"] is True,
        decision["coercivity_or_exterior_gap_proved"] is False,
        decision["native_K152_interval_emitted"] is False,
    ]


def main() -> int:
    result = demo(); assert all(controls(result))
    specs = [
        (("classification",), "SUPPORTED"), (("direction",), "native_to_observed"),
        (("raw_cutoff_forms", "defect_inertias"), []), (("raw_cutoff_forms", "fine_compression_strictly_above_independent_coarse_form"), False),
        (("raw_cutoff_forms", "all_three_sectors_positive_definite"), False), (("regular_chart_forms", "defect_inertias"), []),
        (("regular_chart_forms", "all_three_sectors_indefinite"), False), (("regular_chart_forms", "fine_compression_ge_independent_coarse"), True),
        (("regular_chart_forms", "fine_compression_le_independent_coarse"), True), (("regular_chart_forms", "one_sided_minmax_transfer_available"), True),
        (("regular_chart_forms", "nonlinear_regular_pullback_preserves_raw_form_order"), True),
        (("decision", "K163_first_entry_was_isolated_accident"), True), (("decision", "obstruction_is_full_rank_and_sector_wide"), False),
        (("decision", "independent_rediscretization_can_supply_native_K152_gap"), True),
        (("decision", "requires_exact_compression_or_two_sided_defect_bound"), False),
        (("decision", "coercivity_or_exterior_gap_proved"), True), (("decision", "native_K152_interval_emitted"), True),
    ]
    rejected = 0
    for path, value in specs:
        candidate = copy.deepcopy(result); target = candidate
        for key in path[:-1]: target = target[key]
        target[path[-1]] = value; rejected += int(not all(controls(candidate)))
    assert rejected == len(specs)
    print(json.dumps({"controls_passed": len(controls(result)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__": raise SystemExit(main())

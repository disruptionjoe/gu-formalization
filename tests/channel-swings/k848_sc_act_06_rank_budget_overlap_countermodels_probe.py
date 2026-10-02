#!/usr/bin/env python3
"""Hostile mutations for K848."""
from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location("k848", HERE / "k848_sc_act_06_rank_budget_overlap_countermodels.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="NONE-NOT-A-KILL"),
        lambda p: p["common_base"].update(old_middle_cohomology_dimension=3),
        lambda p: p["controls"]["complementary_pass"].update(repaired_complex_valid=False),
        lambda p: p["controls"]["complementary_pass"].update(new_middle_cohomology_dimension=1),
        lambda p: p["controls"]["complementary_pass"].update(middle_exact_after_repair=False),
        lambda p: p["controls"]["duplicate_response_fail"].update(response_effective_rank_on_old_cohomology=1),
        lambda p: p["controls"]["duplicate_response_fail"].update(new_middle_cohomology_dimension=0),
        lambda p: p["controls"]["duplicate_response_fail"].update(middle_exact_after_repair=True),
        lambda p: p["controls"]["old_gauge_overlap_fail"].update(symmetry_effective_rank_in_response_kernel=1),
        lambda p: p["controls"]["old_gauge_overlap_fail"].update(new_middle_cohomology_dimension=0),
        lambda p: p["controls"]["old_gauge_overlap_fail"].update(middle_exact_after_repair=True),
        lambda p: p["comparison"].update(all_raw_response_plus_symmetry_ranks=[2, 1, 2]),
        lambda p: p["comparison"].update(all_raw_budgets_equal_old_h=False),
        lambda p: p["comparison"].update(raw_rank_threshold_decides_exactness=True),
        lambda p: p["comparison"].update(quotient_complementarity_decides_exactness=False),
        lambda p: p["decision"].update(K845_threshold_is_only_a_coarse_necessary_test=False),
        lambda p: p["decision"].update(response_rows_already_in_old_equation_span_get_zero_credit=False),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),
        lambda p: p["probe_contract"].update(hostile_mutations_rejected=19),
    ]
    rejected = 0
    for mutate in mutations:
        packet = copy.deepcopy(base)
        mutate(packet)
        try:
            MODULE.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["probe_contract"]["hostile_mutations_rejected"]
    print(f"K848 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

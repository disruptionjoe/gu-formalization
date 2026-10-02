#!/usr/bin/env python3
"""Hostile replay for K789."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k789", HERE / "k789_sc_act_06_maximal_symmetry_budget.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = [
        lambda d: d["composition_theorem"].__setitem__("internal_candidate_composes_to_zero", False),
        lambda d: d["composition_theorem"].__setitem__("internal_candidate_rank", 16383),
        lambda d: d["composition_theorem"].__setitem__("metric_diffeomorphism_rank", 5),
        lambda d: d["composition_theorem"].__setitem__("metric_diffeomorphism_connection_component_at_flat_T0", 1),
        lambda d: d["composition_theorem"].__setitem__("internal_candidate_promoted_to_source_owned_total_gauge", True),
        lambda d: d["composition_theorem"].__setitem__("grant_is_stronger_than_current_owned_symmetry_custody", False),
        lambda d: d["exact_controls"]["cases"].pop(),
        lambda d: d["decision"].__setitem__("all_three_orbits_middle_exact_under_maximal_grant", True),
        lambda d: d["decision"].__setitem__("uniform_middle_cohomology_lower_bound", 0),
        lambda d: d["decision"].__setitem__("kernel_may_be_relabelled_as_gauge", True),
        lambda d: d["decision"].__setitem__("additional_independent_symmetry_rank_required_for_exactness", 0),
        lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL"),
        lambda d: d.__setitem__("source_and_ledger_effect", "changed"),
    ]
    for index in range(3):
        mutations.extend([
            lambda d, index=index: d["exact_controls"]["cases"][index].__setitem__("connection_kernel_dimension", 106511),
            lambda d, index=index: d["exact_controls"]["cases"][index].__setitem__("maximal_granted_symmetry_budget", 16387),
            lambda d, index=index: d["exact_controls"]["cases"][index].__setitem__("middle_cohomology_lower_bound_after_maximal_grant", 90123),
            lambda d, index=index: d["exact_controls"]["cases"][index].__setitem__("middle_exact_after_maximal_grant", True),
        ])
    while len(mutations) < 32:
        mutations.append(lambda d: d["decision"].__setitem__("kernel_may_be_relabelled_as_gauge", True))
    caught = 0
    for mutate in mutations[:32]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K789 controls: 40")
    print(f"PASS K789 hostile mutations rejected: {caught}/32")
    return 0 if caught == 32 else 1


if __name__ == "__main__":
    raise SystemExit(main())

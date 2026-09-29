#!/usr/bin/env python3
"""Independent controls and hostile mutations for K636."""

from __future__ import annotations

import copy

from k636_k500_non_equivalent_cancellation_graph import build


def controls(p: dict) -> list[bool]:
    w = p["partial_trace_witness"]
    t = p["cancellation_graph_theorem"]
    m = p["matching_uniqueness"]
    r = p["dependency_reconciliation"]
    d = p["decision"]
    return [
        p["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        w["diverges"] is True,
        len(w["samples"]) == 4,
        all(float(row["boundary_trace_partial"]) > float(row["integral_lower"]) for row in w["samples"]),
        t["trace_domain_dense_in_ell2"] is True,
        t["boundary_profile_in_ell2"] is True,
        t["boundary_profile_in_trace_domain"] is False,
        t["direct_sum_decomposition_unique"] is True,
        t["cancellation_domain_dense_in_ell2"] is True,
        t["cancellation_domain_strictly_contains_trace_domain"] is True,
        t["renormalized_trace_continuous"] is True,
        t["boundary_profile_renormalized_trace"] == "L_cancel(h)=0",
        t["same_underlying_domain_as_rejected_diagonal_graph"] is False,
        t["equivalent_norm_repair"] is False,
        t["boundedly_invertible_same-domain_correlation"] is False,
        m["matched_coefficient"] == "alpha=1",
        m["every_mismatched_coefficient_diverges_for_c_nonzero"] is True,
        m["separate_singular_factors_bounded"] is False,
        m["cancelled_combination_bounded"] is True,
        r["K174_diagonal_weight_obstruction_retracted"] is False,
        r["K611_mixed_graph_splice_obstruction_retracted"] is False,
        r["K634_equivalent_domain_obstruction_retracted"] is False,
        r["genuinely_non_equivalent_domain_constructed"] is True,
        r["complete_K139_K168_core_controlled"] is False,
        r["named_complete_sector_floor_emitted"] is False,
        d["topological_part_of_K634_reopener_released"] is True,
        d["quantitative_complete_form_part_released"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def mutations(payload: dict):
    specs = [
        (("classification",), "SOURCE_RESULT"),
        (("partial_trace_witness", "diverges"), False),
        (("cancellation_graph_theorem", "trace_domain_dense_in_ell2"), False),
        (("cancellation_graph_theorem", "boundary_profile_in_ell2"), False),
        (("cancellation_graph_theorem", "boundary_profile_in_trace_domain"), True),
        (("cancellation_graph_theorem", "direct_sum_decomposition_unique"), False),
        (("cancellation_graph_theorem", "cancellation_domain_dense_in_ell2"), False),
        (("cancellation_graph_theorem", "cancellation_domain_strictly_contains_trace_domain"), False),
        (("cancellation_graph_theorem", "renormalized_trace_continuous"), False),
        (("cancellation_graph_theorem", "boundary_profile_renormalized_trace"), "undefined"),
        (("cancellation_graph_theorem", "same_underlying_domain_as_rejected_diagonal_graph"), True),
        (("cancellation_graph_theorem", "equivalent_norm_repair"), True),
        (("cancellation_graph_theorem", "boundedly_invertible_same-domain_correlation"), True),
        (("matching_uniqueness", "matched_coefficient"), "alpha=0"),
        (("matching_uniqueness", "every_mismatched_coefficient_diverges_for_c_nonzero"), False),
        (("matching_uniqueness", "separate_singular_factors_bounded"), True),
        (("matching_uniqueness", "cancelled_combination_bounded"), False),
        (("dependency_reconciliation", "K174_diagonal_weight_obstruction_retracted"), True),
        (("dependency_reconciliation", "K611_mixed_graph_splice_obstruction_retracted"), True),
        (("dependency_reconciliation", "K634_equivalent_domain_obstruction_retracted"), True),
        (("dependency_reconciliation", "genuinely_non_equivalent_domain_constructed"), False),
        (("dependency_reconciliation", "complete_K139_K168_core_controlled"), True),
        (("dependency_reconciliation", "named_complete_sector_floor_emitted"), True),
        (("decision", "topological_part_of_K634_reopener_released"), False),
        (("decision", "quantitative_complete_form_part_released"), True),
    ]
    for path, value in specs:
        m = copy.deepcopy(payload)
        target = m
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        yield m


def main() -> int:
    payload = build()
    base = controls(payload)
    assert len(base) == 30 and all(base)
    rejected = sum(not all(controls(mutant)) for mutant in mutations(payload))
    assert rejected == 25
    print("K636 independent controls: 30/30 passed")
    print("K636 hostile mutations: 25/25 rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

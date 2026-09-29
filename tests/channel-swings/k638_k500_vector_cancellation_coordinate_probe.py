#!/usr/bin/env python3
"""Independent controls and hostile mutations for K638."""

from __future__ import annotations

import copy

from k638_k500_vector_cancellation_coordinate import build


def controls(p: dict) -> list[bool]:
    c = p["native_coordinate_census"]
    t = p["vector_graph_theorem"]
    m = p["matrix_matching_uniqueness"]
    d = p["dependency_reconciliation"]
    return [
        p["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        c["ordered_edge_pairs"] == 4,
        c["polarity_blocks_per_pair"] == 4,
        c["declared_label_count"] == 16,
        len(set(c["declared_exchange_labels"])) == 16,
        c["all_sixteen_monomials_included"] is True,
        c["cross_polarity_cancellation_required"] is False,
        c["bookkeeping_dimension_proved_minimal"] is False,
        c["linear_independence_of_physical_channel_ranges_proved"] is False,
        t["base_domain_dense"] is True,
        t["all_labeled_boundary_profiles_in_ambient_Hilbert_space"] is True,
        t["no_nonzero_labeled_boundary_profile_in_base_trace_domain"] is True,
        t["direct_sum_decomposition_unique"] is True,
        t["vector_cancellation_domain_dense"] is True,
        t["vector_cancellation_domain_strictly_larger"] is True,
        t["matched_vector_trace_continuous"] is True,
        t["each_boundary_coordinate_maps_to_zero"] is True,
        t["K636_scalar_graph_is_one_coordinate_restriction"] is True,
        t["same_domain_equivalent_norm_repair"] is False,
        m["every_nonidentity_subtraction_matrix_has_a_divergent_direction"] is True,
        m["cross_channel_mixing_can_cancel_all_inputs_without_identity"] is False,
        m["componentwise_matching_is_unique_on_declared_coordinate"] is True,
        m["separate_singular_exchange_factors_bounded"] is False,
        m["complete_matched_combination_lower_bounded"] is False,
        len(p["exact_finite_controls"]) == 4,
        all(row["matched_vector_equals_core"] for row in p["exact_finite_controls"]),
        d["actual_K176_label_census_bound_to_graph"] is True,
        d["named_complete_sector_floor_emitted"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def mutations(payload: dict):
    specs = [
        (("classification",), "SOURCE_RESULT"),
        (("native_coordinate_census", "ordered_edge_pairs"), 3),
        (("native_coordinate_census", "polarity_blocks_per_pair"), 2),
        (("native_coordinate_census", "declared_label_count"), 1),
        (("native_coordinate_census", "all_sixteen_monomials_included"), False),
        (("native_coordinate_census", "cross_polarity_cancellation_required"), True),
        (("native_coordinate_census", "bookkeeping_dimension_proved_minimal"), True),
        (("native_coordinate_census", "linear_independence_of_physical_channel_ranges_proved"), True),
        (("vector_graph_theorem", "base_domain_dense"), False),
        (("vector_graph_theorem", "all_labeled_boundary_profiles_in_ambient_Hilbert_space"), False),
        (("vector_graph_theorem", "no_nonzero_labeled_boundary_profile_in_base_trace_domain"), False),
        (("vector_graph_theorem", "direct_sum_decomposition_unique"), False),
        (("vector_graph_theorem", "vector_cancellation_domain_dense"), False),
        (("vector_graph_theorem", "vector_cancellation_domain_strictly_larger"), False),
        (("vector_graph_theorem", "matched_vector_trace_continuous"), False),
        (("vector_graph_theorem", "each_boundary_coordinate_maps_to_zero"), False),
        (("vector_graph_theorem", "K636_scalar_graph_is_one_coordinate_restriction"), False),
        (("vector_graph_theorem", "same_domain_equivalent_norm_repair"), True),
        (("matrix_matching_uniqueness", "every_nonidentity_subtraction_matrix_has_a_divergent_direction"), False),
        (("matrix_matching_uniqueness", "cross_channel_mixing_can_cancel_all_inputs_without_identity"), True),
        (("matrix_matching_uniqueness", "componentwise_matching_is_unique_on_declared_coordinate"), False),
        (("matrix_matching_uniqueness", "separate_singular_exchange_factors_bounded"), True),
        (("matrix_matching_uniqueness", "complete_matched_combination_lower_bounded"), True),
        (("dependency_reconciliation", "actual_K176_label_census_bound_to_graph"), False),
        (("dependency_reconciliation", "named_complete_sector_floor_emitted"), True),
        (("source_and_ledger_effect",), "moved"),
    ]
    for path, value in specs:
        mutant = copy.deepcopy(payload)
        target = mutant
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        yield mutant


def main() -> int:
    payload = build()
    base = controls(payload)
    assert len(base) == 31 and all(base)
    rejected = sum(not all(controls(mutant)) for mutant in mutations(payload))
    assert rejected == 26
    print("K638 independent controls: 31/31 passed")
    print("K638 hostile mutations: 26/26 rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

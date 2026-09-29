#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K637."""

from __future__ import annotations

import copy

from k637_k77_natural_commutant_selection_ceiling import build


def controls(p: dict) -> list[bool]:
    t = p["naturality_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    packets = p["cross_characteristic_packets"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(packets) == 2,
        all(row["block_size"] == 64 for row in packets),
        all(row["distinct_diagonal_generator"] for row in packets),
        all(row["cyclic_shift_generator"] for row in packets),
        all(row["single_block_fixed_dimension"] == 1 for row in packets),
        all(row["independent_two_block_fixed_dimension"] == 2 for row in packets),
        all(row["block_exchange_fixed_dimension"] == 1 for row in packets),
        all(row["labeled_grading_involution_squares_to_identity"] for row in packets),
        all(row["labeled_grading_involution_fixed_by_internal_basis_gauge"] for row in packets),
        all(not row["labeled_grading_involution_fixed_by_block_exchange"] for row in packets),
        t["induced_algebra_dimension"] == 8192,
        t["internal_basis_gauge_fixed_dimension"] == 2,
        t["labeled_grading_is_basis_natural"] is True,
        t["labeled_grading_is_action_polynomial"] is False,
        t["unlabeled_exchange_fixed_dimension"] == 1,
        t["normalization_selects_unique_nonscalar_member"] is False,
        t["action_only_selected_nonscalar_operator"] is False,
        o["K635_large_algebra_retracted"] is False,
        o["K633_polynomial_scalar_ceiling_retracted"] is False,
        o["seed_labeled_block_grading_available"] is True,
        o["independently_action_owned_source_endomorphism_found"] is False,
        o["K596_K598_released"] is False,
        d["existing_data_selects_a_unique_nonscalar_operator"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def mutations(payload: dict):
    specs = [
        (("classification",), "SOURCE_RESULT"),
        (("cross_characteristic_packets", 0, "block_size"), 63),
        (("cross_characteristic_packets", 0, "distinct_diagonal_generator"), False),
        (("cross_characteristic_packets", 0, "cyclic_shift_generator"), False),
        (("cross_characteristic_packets", 0, "single_block_fixed_dimension"), 2),
        (("cross_characteristic_packets", 0, "independent_two_block_fixed_dimension"), 1),
        (("cross_characteristic_packets", 0, "block_exchange_fixed_dimension"), 2),
        (("cross_characteristic_packets", 0, "labeled_grading_involution_squares_to_identity"), False),
        (("cross_characteristic_packets", 0, "labeled_grading_involution_fixed_by_internal_basis_gauge"), False),
        (("cross_characteristic_packets", 0, "labeled_grading_involution_fixed_by_block_exchange"), True),
        (("naturality_theorem", "induced_algebra_dimension"), 1),
        (("naturality_theorem", "internal_basis_gauge_fixed_dimension"), 8192),
        (("naturality_theorem", "labeled_grading_is_basis_natural"), False),
        (("naturality_theorem", "labeled_grading_is_action_polynomial"), True),
        (("naturality_theorem", "unlabeled_exchange_fixed_dimension"), 2),
        (("naturality_theorem", "normalization_selects_unique_nonscalar_member"), True),
        (("naturality_theorem", "action_only_selected_nonscalar_operator"), True),
        (("ownership_reconciliation", "K635_large_algebra_retracted"), True),
        (("ownership_reconciliation", "K633_polynomial_scalar_ceiling_retracted"), True),
        (("ownership_reconciliation", "seed_labeled_block_grading_available"), False),
        (("ownership_reconciliation", "independently_action_owned_source_endomorphism_found"), True),
        (("ownership_reconciliation", "K596_K598_released"), True),
        (("decision", "existing_data_selects_a_unique_nonscalar_operator"), True),
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
    assert len(base) == 27 and all(base)
    rejected = sum(not all(controls(mutant)) for mutant in mutations(payload))
    assert rejected == 24
    print("K637 independent controls: 27/27 passed")
    print("K637 hostile mutations: 24/24 rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

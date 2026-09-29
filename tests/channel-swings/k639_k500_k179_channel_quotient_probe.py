#!/usr/bin/env python3
"""Independent controls and hostile mutations for K639."""

from __future__ import annotations

import copy

from k639_k500_k179_channel_quotient import build


def controls(p: dict) -> list[bool]:
    r = p["complete_family_replay"]
    q = p["quotient_theorem"]
    d = p["dependency_reconciliation"]
    return [
        p["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        r["term_count"] == 2958,
        r["family_sha256"] == "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686",
        r["all_terms_map_to_declared_K638_labels"] is True,
        r["all_terms_map_to_surviving_labels"] is True,
        len(r["surviving_label_counts"]) == 6,
        sum(r["surviving_label_counts"].values()) == 2958,
        len(r["surviving_monomial_counts"]) == 6,
        r["orders_covered"] == list(range(2, 13)),
        q["declared_dimension"] == 16,
        q["surviving_dimension"] == 6,
        q["kernel_dimension"] == 10,
        len(q["surviving_basis"]) == 6,
        len(q["null_labels"]) == 10,
        len(q["opposite_polarity_null_labels"]) == 8,
        len(q["off_diagonal_minus_minus_null_labels"]) == 2,
        len(q["quotient_matrix"]) == 6,
        all(len(row) == 16 for row in q["quotient_matrix"]),
        q["quotient_matrix_rank"] == 6,
        q["separating_functional_rank"] == 6,
        q["surviving_operator_monomials_linearly_independent_on_finite_particle_core"] is True,
        q["minimal_algebraic_operator_coordinate_proved"] is True,
        q["independent_physical_channel_ranges_proved"] is False,
        d["K638_sixteen_label_bookkeeping_retracted"] is False,
        d["K638_physical_minimality_warning_resolved_only_algebraically"] is True,
        d["K179_coefficient_family_retracted"] is False,
        d["complete_K139_K168_core_controlled"] is False,
        d["named_complete_sector_floor_emitted"] is False,
        d["K473_released"] is False,
        d["native_K152_interval_emitted"] is False,
        p["source_and_ledger_effect"] == "none",
        p["decision"]["ten_bookkeeping_directions_quotiented"] is True,
    ]


def mutations(payload: dict):
    specs = [
        (("classification",), "SOURCE_RESULT"),
        (("complete_family_replay", "term_count"), 16),
        (("complete_family_replay", "family_sha256"), "bad"),
        (("complete_family_replay", "all_terms_map_to_declared_K638_labels"), False),
        (("complete_family_replay", "all_terms_map_to_surviving_labels"), False),
        (("complete_family_replay", "orders_covered"), [2]),
        (("quotient_theorem", "declared_dimension"), 6),
        (("quotient_theorem", "surviving_dimension"), 16),
        (("quotient_theorem", "kernel_dimension"), 0),
        (("quotient_theorem", "null_labels"), []),
        (("quotient_theorem", "opposite_polarity_null_labels"), []),
        (("quotient_theorem", "off_diagonal_minus_minus_null_labels"), []),
        (("quotient_theorem", "quotient_matrix_rank"), 5),
        (("quotient_theorem", "separating_functional_rank"), 5),
        (("quotient_theorem", "surviving_operator_monomials_linearly_independent_on_finite_particle_core"), False),
        (("quotient_theorem", "minimal_algebraic_operator_coordinate_proved"), False),
        (("quotient_theorem", "independent_physical_channel_ranges_proved"), True),
        (("dependency_reconciliation", "K638_sixteen_label_bookkeeping_retracted"), True),
        (("dependency_reconciliation", "K638_physical_minimality_warning_resolved_only_algebraically"), False),
        (("dependency_reconciliation", "K179_coefficient_family_retracted"), True),
        (("dependency_reconciliation", "complete_K139_K168_core_controlled"), True),
        (("dependency_reconciliation", "named_complete_sector_floor_emitted"), True),
        (("dependency_reconciliation", "K473_released"), True),
        (("dependency_reconciliation", "native_K152_interval_emitted"), True),
        (("source_and_ledger_effect",), "moved"),
        (("decision", "ten_bookkeeping_directions_quotiented"), False),
        (("target_claim",), "SC-META-53"),
        (("direction",), "native_to_observed"),
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
    assert len(base) == 34 and all(base)
    rejected = sum(not all(controls(mutant)) for mutant in mutations(payload))
    assert rejected == 28
    print("K639 independent controls: 34/34 passed")
    print("K639 hostile mutations: 28/28 rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

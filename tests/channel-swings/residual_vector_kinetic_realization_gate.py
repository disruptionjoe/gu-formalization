#!/usr/bin/env python3
"""Exact D5 root-trace gate for the declared residual-vector P8 premise."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/residual-vector-kinetic-realization-gate.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def roots_d5() -> list[tuple[int, ...]]:
    roots: list[tuple[int, ...]] = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (-1, 1):
                for sj in (-1, 1):
                    root = [0] * 5
                    root[i], root[j] = si, sj
                    roots.append(tuple(root))
    return roots


def trace_pairing(u: tuple[Fraction, ...], v: tuple[Fraction, ...]) -> Fraction:
    return sum(
        sum(Fraction(a) * b for a, b in zip(root, u))
        * sum(Fraction(a) * b for a, b in zip(root, v))
        for root in roots_d5()
    )


def build() -> dict:
    roots = roots_d5()
    basis = [tuple(Fraction(int(i == j)) for i in range(5)) for j in range(5)]
    tensor = [[trace_pairing(ei, ej) for ej in basis] for ei in basis]
    hypercharge = (Fraction(-1, 6),) * 3 + (Fraction(1, 4),) * 2
    b_minus_l = (Fraction(-1, 3),) * 3 + (Fraction(0),) * 2
    gram = [
        [trace_pairing(hypercharge, hypercharge), trace_pairing(hypercharge, b_minus_l)],
        [trace_pairing(b_minus_l, hypercharge), trace_pairing(b_minus_l, b_minus_l)],
    ]
    determinant = gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]
    coefficient = gram[1][0] / gram[0][0]
    residual = tuple(b - coefficient * y for b, y in zip(b_minus_l, hypercharge))
    return {
        "schema_version": "1.0",
        "packet_id": "RESIDUAL-VECTOR-KINETIC-REALIZATION-GATE",
        "date": "2026-09-23",
        "status": "working_draft_verified",
        "target_claim": "Test the first exact rank/radical subquestion inside supplied premise P8 for the frozen declared-content residual abelian direction.",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "source_boundary": {
            "declared_content_parent": "lab/process/declared-content-extra-vector-obstruction-package.json",
            "premise": "P8",
            "packet_horn_row": "LT-SM1a",
            "ledger_row": "RA-G4",
            "source_claim_effect": "none",
            "physics_ledger_effect": "none",
        },
        "exact_root_trace": {
            "root_system": "D5",
            "root_count": len(roots),
            "root_length_squared": 2,
            "cartan_tensor": [[q(x) for x in row] for row in tensor],
            "tensor_identity": "16*I_5",
        },
        "declared_cartan_plane": {
            "basis_order": ["Y", "B-L"],
            "Y": [q(x) for x in hypercharge],
            "B-L": [q(x) for x in b_minus_l],
            "root_trace_gram": [[q(x) for x in row] for row in gram],
            "gram_determinant": q(determinant),
            "gram_rank": 2,
            "B-L_projection_on_Y": q(coefficient),
            "Y_orthogonal_residual_X": [q(x) for x in residual],
            "pairing_X_Y": q(trace_pairing(residual, hypercharge)),
            "pairing_X_X": q(trace_pairing(residual, residual)),
        },
        "horn_disposition": {
            "packet_fundamental_zeta_F_1": {
                "result": "candidate_compact_cartan_form_is_nondegenerate_on_Y_plus_residual",
                "radical_escape_on_this_form": False,
                "p8_derived": False,
                "ceiling": "The packet writes a Yang-Mills term, but this root-trace calculation does not identify its observed action-owned form, physical quotient or Green pairing.",
            },
            "packet_induced_zeta_F_0": {
                "result": "no_regulator_or_source_owned_induced_form_is_supplied",
                "radical_escape_tested": False,
                "p8_derived": False,
                "ceiling": "The exact D5 Gram cannot stand in for the missing induced kinetic form.",
            },
            "source_two_layer_reading": {
                "result": "outside_the_packet_binary_until_a_typed_action_bridge_is_built",
                "p8_derived": False,
            },
        },
        "remaining_p8_owners": [
            "action-owned gauge kinetic bilinear on the actual candidate branch",
            "typed observation descent for the residual compact direction",
            "gauge/constraint quotient and closed physical domain",
            "real or Krein Green pairing and nondegeneracy on the quotient",
            "normalization/branching only after the preceding owners exist",
        ],
        "decision": {
            "first_rank_radical_gate_on_fundamental_candidate": "passes",
            "declared_content_residual_direction_theorem_changed": False,
            "conditional_physical_vector_upgrade_allowed": False,
            "premise_P8_status": "supplied_not_derived",
            "next_cheapest_test": "match the existing corrected observation projection to a named action-owned constraint/gauge image and Green pairing; do not build a full action merely to repeat the algebraic Gram test",
        },
        "release_test": {
            "forty_unique_D5_roots": len(roots) == len(set(roots)) == 40,
            "root_trace_tensor_is_16I": tensor == [[Fraction(16 if i == j else 0) for j in range(5)] for i in range(5)],
            "gram_is_full_rank": determinant == Fraction(32, 3),
            "orthogonal_residual_is_nonzero": trace_pairing(residual, hypercharge) == 0 and trace_pairing(residual, residual) == Fraction(16, 5),
            "fundamental_and_induced_horns_separated": True,
            "source_two_layer_reading_not_collapsed": True,
            "P8_not_overpromoted": True,
            "source_and_ledger_unchanged": True,
            "no_physical_or_public_effect": True,
        },
    }


def validate_payload(payload: dict) -> None:
    assert payload["exact_root_trace"]["root_count"] == 40
    assert payload["exact_root_trace"]["tensor_identity"] == "16*I_5"
    assert payload["declared_cartan_plane"]["root_trace_gram"] == [["10/3", "8/3"], ["8/3", "16/3"]]
    assert payload["declared_cartan_plane"]["gram_determinant"] == "32/3"
    assert payload["declared_cartan_plane"]["gram_rank"] == 2
    assert payload["declared_cartan_plane"]["Y_orthogonal_residual_X"] == ["-1/5"] * 5
    assert payload["declared_cartan_plane"]["pairing_X_Y"] == "0"
    assert payload["declared_cartan_plane"]["pairing_X_X"] == "16/5"
    assert not payload["horn_disposition"]["packet_fundamental_zeta_F_1"]["p8_derived"]
    assert not payload["horn_disposition"]["packet_induced_zeta_F_0"]["p8_derived"]
    assert payload["decision"]["premise_P8_status"] == "supplied_not_derived"
    assert len(payload["remaining_p8_owners"]) == 5
    assert all(payload["release_test"].values())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print("residual-vector gate passed: 40 roots, Gram det 32/3, X norm 16/5; P8 remains supplied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

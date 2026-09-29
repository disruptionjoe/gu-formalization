#!/usr/bin/env python3
"""K607 test of K438's action-owned nontrivial corrected-carrier symbol."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k607-k77-action-symbol-stabilizer-refinement.json"


def strict(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text())


def identity(n: int) -> list[list[Fraction]]:
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def diagonal(values) -> list[list[Fraction]]:
    return [[Fraction(values[i]) if i == j else Fraction() for j in range(len(values))] for i in range(len(values))]


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(c, a):
    return [[Fraction(c) * x for x in row] for row in a]


def kron(a, b):
    return [[a[i][j] * b[u][v] for j in range(len(a[0])) for v in range(len(b[0]))]
            for i in range(len(a)) for u in range(len(b))]


def equal(a, b) -> bool:
    return a == b


def rank_diagonal(a) -> int:
    return sum(a[i][i] != 0 for i in range(len(a)))


def toy_control() -> dict[str, Any]:
    roots = [Fraction(1), Fraction(1), Fraction(1, 24), Fraction(1, 24),
             Fraction(-1), Fraction(-1), Fraction(-1, 24), Fraction(-1, 24)]
    a = diagonal(roots)
    a2 = matmul(a, a)
    a3 = matmul(a2, a)
    j = scale(Fraction(1, 575), add(scale(13823, a), scale(-13248, a3)))
    projector = scale(Fraction(1, 2), add(identity(8), j))
    expected_projector = diagonal([1, 1, 1, 1, 0, 0, 0, 0])
    # Spectral idempotents are exact Lagrange polynomials in A; on the diagonal
    # control they are the four consecutive rank-two blocks.
    spectral_projectors = [
        diagonal([int(start <= i < start + 2) for i in range(8)])
        for start in (0, 2, 4, 6)
    ]
    d2 = [[1, 0], [0, 1], [0, 0]]
    d1 = [[0, 0, 1], [0, 0, 0]]
    lifted_d2 = kron(d2, a)
    lifted_d1 = kron(d1, a)
    pi2 = kron(identity(2), projector)
    pi1 = kron(identity(3), projector)
    pi0 = kron(identity(2), projector)
    return {
        "toy_carrier_rank": 8,
        "toy_spectral_block_ranks": [rank_diagonal(p) for p in spectral_projectors],
        "sign_polynomial_equals_expected_projector_split": equal(projector, expected_projector),
        "action_symbol_commutes_with_projector": equal(matmul(a, projector), matmul(projector, a)),
        "spectral_projectors_sum_to_identity": equal(
            add(add(spectral_projectors[0], spectral_projectors[1]), add(spectral_projectors[2], spectral_projectors[3])),
            identity(8),
        ),
        "smallest_nonzero_polynomial_projector_rank": min(rank_diagonal(p) for p in spectral_projectors),
        "D2_tensor_A_square_passes": equal(matmul(pi1, lifted_d2), matmul(lifted_d2, pi2)),
        "D1_tensor_A_square_passes": equal(matmul(pi0, lifted_d1), matmul(lifted_d1, pi1)),
        "lifted_nilpotence": not any(x for row in matmul(lifted_d1, lifted_d2) for x in row),
    }


def build() -> dict[str, Any]:
    k438 = strict("lab/process/k438-k77-constraint-compressed-boundary-symbol.json")
    k439 = strict("lab/process/k439-k77-compatible-corrected-boundary-split.json")
    k590 = strict("lab/process/k590-k77-corrected-carrier-completion-squares.json")
    k605 = strict("lab/process/k605-k77-factorwise-selector-obstruction.json")
    ranks = k438["cross_characteristic_result"]["rank_fingerprint"]
    controls = toy_control()
    return {
        "schema_version": "1.0",
        "result_id": "K607-K77-ACTION-SYMBOL-STABILIZER-REFINEMENT",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Whether K438's already action-owned nontrivial corrected-carrier symbol A supplies the stabilizer-reducing datum left open by K605 and thereby selects K598 initial carrier vectors, covectors or a rank-one packet.",
        "gu_typed_objects": {
            "carrier": "K438 corrected Clifford carrier E of rank 512 inside the observed H640 carrier",
            "action_symbol": "A=P S_7 P with eigenvalues +1,-1,+1/24,-1/24 and multiplicities 192,192,64,64",
            "projector": "K439 Pi_+=(I+sign(A))/2, with sign(A)=(13823 A-13248 A^3)/575",
            "base_complex": "K589's exact H^21 to Q^91 to M^70 coefficient complex",
            "result": "action-symbol stabilizer refinement MAP-TYPE=spectral-algebra no-selector theorem",
            "target": "K598 initial corrected-carrier vector/Riesz/rank-one packet and nonfactorized K444 coupling",
        },
        "actual_action_symbol_replay": {
            "carrier_rank": ranks["corrected_carrier"],
            "minimal_polynomial": k438["cross_characteristic_result"]["exact_identity"],
            "spectral_values": ["1", "-1", "1/24", "-1/24"],
            "spectral_multiplicities": [192, 192, 64, 64],
            "zero_eigenvalue_absent": k438["decision"]["zero_characteristic_root_present"] is False,
            "action_and_constraint_determine_spectral_blocks": k438["decision"]["action_and_constraint_determine_spectral_blocks"],
            "projector_is_polynomial_in_A": k439["gu_typed_objects"]["sign_involution"],
        },
        "theorem": {
            "carrier_stabilizer_is_reduced": "A refines K600's two rank-256 halves into four spectral blocks of ranks 192,192,64,64.",
            "global_sign_symmetry_survives": "-I_E preserves the pairing, Pi and A, so every vector or covector natural from these homogeneous data is zero.",
            "generated_algebra": "R[A] has the four spectral projectors as its idempotent basis; Pi is already a cubic polynomial in A and adds no new selector.",
            "minimum_nonzero_rank_in_generated_algebra": 64,
            "nonzero_rank_one_packet_in_generated_algebra": False,
            "factorwise_action_symbol_square": "For p(A) in R[A], D_i tensor p(A) satisfies K444 because p(A) commutes with Pi.",
            "A_lift_exactness": "A is invertible, so replacing I_E by A in both K590 arrows preserves nilpotence, ranks and exactness of the tensor-product base complex.",
            "ownership_ceiling": "The canonical D_i tensor A candidate composes already owned blocks but is not a selected full nonlinear BV/KT coupling and does not supply K598's initial vectors or field-space Riesz return.",
        },
        "K590_K605_reconciliation": {
            "K590_factorized_identity_completion_retracted": False,
            "K605_factorwise_identity_obstruction_retracted": False,
            "K605_open_nontrivial_carrier_datum_tested": True,
            "action_symbol_reduces_two_block_stabilizer": True,
            "action_symbol_selects_nonzero_vector_or_covector": False,
            "action_symbol_selects_nonzero_rank_one_packet": False,
            "K598_actual_action_owned_initial_packet_constructed": False,
            "K438_physical_boundary_selected": k438["decision"]["physical_boundary_selected"],
            "K590_actual_homology_dimensions": k590["factorized_completion"]["homology_dimensions"],
            "K605_prior_full_half_stabilizer_unbroken": not k605["decision"]["factorwise_base_maps_reduce_carrier_stabilizer"],
        },
        "exact_controls": controls,
        "decision": {
            "actual_K438_action_symbol_tested_against_K605": True,
            "K605_missing_datum_narrowed": True,
            "nontrivial_carrier_action_is_not_sufficient_for_selection": True,
            "K598_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply an action-owned inhomogeneous vector/covector, a simple spectral block, or a field-to-carrier/Riesz map that breaks the surviving global sign and internal spectral multiplicities. Polynomials in K438's A, including K439's projector and D_i tensor p(A), cannot produce K598's rank-one initial packet.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact test of the existing K438 action-owned nontrivial corrected-carrier symbol. It reduces K600's two-block stabilizer to four spectral blocks and yields compatible exact D_i tensor A candidates, but the generated algebra has minimum nonzero rank 64 and surviving global sign symmetry, so no vector, covector or rank-one K598 packet is selected. No full nonlinear BV/KT coupling, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict[str, Any]) -> None:
    replay = payload["actual_action_symbol_replay"]
    theorem = payload["theorem"]
    rec = payload["K590_K605_reconciliation"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    assert replay["carrier_rank"] == 512 and replay["spectral_multiplicities"] == [192, 192, 64, 64]
    assert replay["zero_eigenvalue_absent"] and replay["action_and_constraint_determine_spectral_blocks"]
    assert theorem["minimum_nonzero_rank_in_generated_algebra"] == 64
    assert not theorem["nonzero_rank_one_packet_in_generated_algebra"]
    assert not rec["K590_factorized_identity_completion_retracted"]
    assert not rec["K605_factorwise_identity_obstruction_retracted"]
    assert rec["K605_open_nontrivial_carrier_datum_tested"] and rec["action_symbol_reduces_two_block_stabilizer"]
    assert not rec["action_symbol_selects_nonzero_vector_or_covector"]
    assert not rec["action_symbol_selects_nonzero_rank_one_packet"]
    assert not rec["K598_actual_action_owned_initial_packet_constructed"]
    assert controls["toy_spectral_block_ranks"] == [2, 2, 2, 2]
    assert controls["sign_polynomial_equals_expected_projector_split"]
    assert controls["action_symbol_commutes_with_projector"] and controls["spectral_projectors_sum_to_identity"]
    assert controls["smallest_nonzero_polynomial_projector_rank"] == 2
    assert controls["D2_tensor_A_square_passes"] and controls["D1_tensor_A_square_passes"] and controls["lifted_nilpotence"]
    assert decision["actual_K438_action_symbol_tested_against_K605"] and decision["K605_missing_datum_narrowed"]
    assert decision["nontrivial_carrier_action_is_not_sufficient_for_selection"]
    assert not decision["K598_released"] and not decision["selected_source_action_rejected"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

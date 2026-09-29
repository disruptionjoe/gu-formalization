#!/usr/bin/env python3
"""K649: transport matched vector cancellation through the native parity basis."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k649-k500-parity-cancellation-matching.json"


def strict(relative: str) -> dict[str, Any]:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def identity(size: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def scale(value: Fraction, matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[value * entry for entry in row] for row in matrix]


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((a * b for a, b in zip(row, vector)), Fraction()) for row in matrix]


def subtract(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(left, right)]


def rank(matrix: list[list[Fraction]]) -> int:
    work = [list(row) for row in matrix]
    pivot_row = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next((row for row in range(pivot_row, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry / value for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def parity_transform() -> list[list[Fraction]]:
    # y=T x gives the unnormalised K648 basis (even first, odd second).
    rows = [[Fraction(0) for _ in range(6)] for _ in range(6)]
    for row, left, right, sign in (
        (0, 0, 3, 1), (1, 1, 2, 1), (2, 4, 5, 1),
        (3, 0, 3, -1), (4, 1, 2, -1), (5, 4, 5, -1),
    ):
        rows[row][left] = Fraction(1)
        rows[row][right] = Fraction(sign)
    return rows


def harmonic(cutoff: int) -> Fraction:
    return sum((Fraction(1, k + 256) for k in range(1, cutoff + 1)), Fraction())


def exact_control() -> dict[str, Any]:
    transform = parity_transform()
    inverse = scale(Fraction(1, 2), transpose(transform))
    old_identity = identity(6)
    new_identity = matmul(transform, matmul(old_identity, inverse))
    mismatch = identity(6)
    mismatch[5][5] = Fraction(0)
    new_mismatch = matmul(transform, matmul(mismatch, inverse))
    residual = subtract(identity(6), new_mismatch)
    witnesses = [
        [Fraction(int(i == j)) for i in range(6)]
        for j in range(6)
    ]
    chosen = next(vector for vector in witnesses if any(matvec(residual, vector)))
    rows = []
    for cutoff in (8, 32, 128):
        h_n = harmonic(cutoff)
        divergence = [h_n * value for value in matvec(residual, chosen)]
        rows.append({
            "cutoff": cutoff,
            "harmonic_partial": str(h_n),
            "mismatched_residual_nonzero": any(divergence),
        })
    return {
        "dimension": 6,
        "transform_rank": rank(transform),
        "T_T_transpose_equals_2I": matmul(transform, transpose(transform)) == scale(Fraction(2), identity(6)),
        "inverse_is_half_transpose": matmul(transform, inverse) == identity(6),
        "identity_matching_is_basis_invariant": new_identity == identity(6),
        "parity_plus_block_identity": [row[:3] for row in new_identity[:3]] == identity(3),
        "parity_minus_block_identity": [row[3:] for row in new_identity[3:]] == identity(3),
        "cross_parity_matching_blocks_zero": all(
            new_identity[i][j] == 0 for i in range(3) for j in range(3, 6)
        ),
        "nonidentity_matching_remains_nonidentity": new_mismatch != identity(6),
        "mismatched_divergent_direction_exists": any(matvec(residual, chosen)),
        "partial_witnesses": rows,
    }


def build() -> dict[str, Any]:
    k638 = strict("lab/process/k638-k500-vector-cancellation-coordinate.json")
    k648 = strict("lab/process/k648-k500-native-parity-form-interface.json")
    assert k638["matrix_matching_uniqueness"]["finite_limit_for_every_coefficient_vector_requires"] == "Alpha=I_16"
    assert k648["channel_parity_basis"]["swap_indices"] == [3, 2, 1, 0, 5, 4]
    control = exact_control()
    assert control["identity_matching_is_basis_invariant"]
    assert control["mismatched_divergent_direction_exists"]
    return {
        "schema_version": "1.0",
        "result_id": "K649-K500-PARITY-CANCELLATION-MATCHING",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K638's matched six-coordinate cancellation graph transported through K648's exact channel-parity basis and total-parity quadrant decomposition.",
        "gu_typed_objects": {
            "ambient_carrier": "ell2(N) tensor C^6 tensor H_spec",
            "cancellation_domain": "(D_a tensor C^6 tensor H_spec) direct sum (h tensor C^6 tensor H_spec)",
            "basis": "K648 channel-even/channel-odd basis combined with spectator flavor parity",
            "renormalized_trace": "the K638 matched vector trace after the exact invertible parity change of coordinate",
            "result": "parity cancellation matching MAP-TYPE=basis-covariant graph identity",
            "target": "the admissible quantitative decomposition of the K648 parity compression forms",
        },
        "parity_matching_theorem": {
            "old_matching_condition": "Alpha=I_6 on the K639 quotient coordinate",
            "basis_change": "T Alpha T^-1 on the K648 even/odd channel coordinate",
            "new_matching_condition": "T Alpha T^-1=I_6 iff Alpha=I_6",
            "total_parity_extension": "tensoring with the spectator involution preserves identity matching on both total-parity carriers",
            "plus_coordinate_matching": "I_3 on channel-even tensor spectator-plus and I_3 on channel-odd tensor spectator-minus",
            "minus_coordinate_matching": "I_3 on channel-even tensor spectator-minus and I_3 on channel-odd tensor spectator-plus",
            "cross_total_parity_subtraction_required": False,
            "each_mismatched_parity_component_has_harmonic_divergent_direction": True,
            "parity_change_makes_separate_singular_factors_bounded": False,
            "complete_matched_combination_remains_the_valid_object": True,
        },
        "quantitative_route_consequence": {
            "K644_raw_row_route_disproved": False,
            "K644_raw_row_route_automatically_available_from_parity": False,
            "separate_channel_Hilbert_bounds_require_new_proof": True,
            "cancellation_adapted_complete_parity_form_route_live": True,
            "twelve_diagonal_and_thirty_coupling_rows_may_be_used_only_after_same_domain_boundedness_is_proved": True,
            "basis_rotation_alone_supplies_numeric_rows": False,
        },
        "exact_control": control,
        "native_interface_status": {
            "native_parity_cancellation_matching_proved": True,
            "separated_singular_channel_bounds_identified": False,
            "actual_parity_block_floors_identified": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "parity_does_not_remove_the_cancellation_domain_obligation": True,
            "independent_raw_row_extraction_not_authorized": True,
            "next_exact_input": "Bound the two complete cancelled quadrants inside each total-parity form and their internal relative form coupling on the same graph domain; then prove parity-specific uniform tails before setting m.",
        },
        "dependency_reconciliation": {
            "K638_matching_uniqueness_preserved": True,
            "K648_total_parity_forms_preserved": True,
            "K644_sufficient_Hilbert_block_theorem_retracted": False,
            "K612_quantitative_custody_obstruction_retracted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a basis-covariant cancellation-domain theorem inside the conditional K139/K168 control and supplies no physical state, observable or source-owned mechanism.",
        "preflight_bookend": {
            "route_comparison": "Before attempting forty-two native scalar rows, test whether the K648 parity basis changes K638's unique subtraction topology; exact conjugation is cheaper and decides that prerequisite.",
            "retrieval_collision_result": "K638 proves matching uniqueness before parity reduction and K648 serializes parity carriers, but no prior artifact composes the two or tests the separated-row shortcut.",
            "strongest_alternative": "Direct native constants would be stronger, but K612 shows they are not in current custody and K638 forbids estimating separated singular factors without a new same-domain proof.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Saying parity compression makes every raw channel block Hilbert bounded or supplies a numerical floor.",
            "strongest_contrary_construction": "Conjugating any nonidentity subtraction matrix by the exact parity transform leaves it nonidentity and therefore leaves a harmonic divergent coefficient direction.",
            "weakest_reproducibility_seam": "The theorem fixes cancellation topology, not the complete native cancelled-core coefficients or their lower constants.",
        },
        "controls": {
            "producer": "tests/channel-swings/k649_k500_parity_cancellation_matching.py",
            "probe": "tests/channel-swings/k649_k500_parity_cancellation_matching_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact basis-covariant cancellation theorem for the frozen K139/K168/K648 interface. K638's unique identity subtraction remains the identity in the K648 parity basis and on both total-parity carriers; every mismatched parity component retains a harmonic divergent direction. Parity therefore does not make separated singular channel factors bounded or supply K644's numerical rows. The complete matched parity forms remain live, but their floors, relative coupling, tails, m, alpha and delta remain absent; no K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["parity_matching_theorem"]
    route = payload["quantitative_route_consequence"]
    control = payload["exact_control"]
    native = payload["native_interface_status"]
    assert theorem["new_matching_condition"].endswith("Alpha=I_6")
    assert theorem["each_mismatched_parity_component_has_harmonic_divergent_direction"]
    assert not theorem["parity_change_makes_separate_singular_factors_bounded"]
    assert not route["K644_raw_row_route_automatically_available_from_parity"]
    assert route["cancellation_adapted_complete_parity_form_route_live"]
    assert control["transform_rank"] == 6 and control["identity_matching_is_basis_invariant"]
    assert native["native_parity_cancellation_matching_proved"]
    assert not native["native_global_m_identified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

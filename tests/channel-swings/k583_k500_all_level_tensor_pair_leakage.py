#!/usr/bin/env python3
"""K583 all-level tensor-pair identity for K500 rank-one leakage."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k583-k500-all-level-tensor-pair-leakage.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K177 = load("k177_for_k583", "k177_laplace_simplex_exchange_prefix.py")


def f(value: Any) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matvec(matrix: Sequence[Sequence[Any]], vector: Sequence[Any]) -> list[Fraction]:
    v = [f(value) for value in vector]
    return [sum((f(value) * v[j] for j, value in enumerate(row)), Fraction()) for row in matrix]


def inner(left: Sequence[Any], right: Sequence[Any]) -> Fraction:
    return sum((f(x) * f(y) for x, y in zip(left, right, strict=True)), Fraction())


def tensor_pair_square(matrix: Sequence[Sequence[Any]], vector: Sequence[Any]) -> Fraction:
    v = [f(value) for value in vector]
    wv = matvec(matrix, v)
    return sum((wv[i] * v[j] - v[i] * wv[j]) ** 2 for i in range(len(v)) for j in range(len(v)))


def leakage_square(matrix: Sequence[Sequence[Any]], vector: Sequence[Any]) -> Fraction:
    v = [f(value) for value in vector]
    norm = inner(v, v)
    if norm <= 0:
        raise ValueError("nonzero vector required")
    wv = matvec(matrix, v)
    return inner(wv, wv) / norm - inner(v, wv) ** 2 / norm**2


def control(name: str, matrix: Sequence[Sequence[Any]], vector: Sequence[Any], shift: int = 7) -> dict[str, Any]:
    direct = leakage_square(matrix, vector)
    norm = inner(vector, vector)
    tensor = tensor_pair_square(matrix, vector)
    shifted = [[f(value) + (shift if i == j else 0) for j, value in enumerate(row)] for i, row in enumerate(matrix)]
    shifted_tensor = tensor_pair_square(shifted, vector)
    shifted_direct = leakage_square(shifted, vector)
    return {
        "name": name,
        "matrix": [[q(f(value)) for value in row] for row in matrix],
        "vector": [q(f(value)) for value in vector],
        "vector_norm_square": q(norm),
        "direct_leakage_square": q(direct),
        "tensor_pair_square": q(tensor),
        "tensor_identity_rhs": q(2 * norm**2 * direct),
        "identity_passes": tensor == 2 * norm**2 * direct,
        "scalar_shift": shift,
        "scalar_shift_invariant": shifted_tensor == tensor and shifted_direct == direct,
        "off_diagonal_exchange_present": any(f(matrix[i][j]) != 0 for i in range(len(matrix)) for j in range(len(matrix)) if i != j),
    }


def build() -> dict[str, Any]:
    controls = [
        control("K501 diagonal", [[2, 0, 0], [0, -1, 0], [0, 0, 4]], [1, 2, 0]),
        control("exchange block", [[0, 2, -1], [2, 1, 3], [-1, 3, 4]], [1, -2, 1]),
        control("reducing line", [[3, 2, 0], [2, 3, 0], [0, 0, -4]], [1, 1, 0]),
    ]
    q00 = K177.seed_census(0)
    q10 = K177.seed_census(1)
    native_rows = []
    for census in (q00, q10):
        order1 = census["orders"][1]["matched_older_letter_contractions"]
        later = sum(row["matched_older_letter_contractions"] for row in census["orders"][2:])
        native_rows.append({
            "seed": census["seed"],
            "charge": census["charge"],
            "order_1_matched_exchange_coordinates": order1,
            "orders_2_through_12_matched_exchange_coordinates": later,
            "level_one_scalar_multiplier_specialization_valid": order1 == 0,
            "higher_level_scalar_multiplier_specialization_complete": later == 0,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K583-K500-ALL-LEVEL-TENSOR-PAIR-LEAKAGE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Every K500 bath-number block with cyclic vector v_n and self-adjoint native normal action W_n, including levels where K177 matched exchange contractions make W_n non-diagonal in continuum coordinates.",
        "gu_typed_objects": {
            "carrier": "one K162 q00 or q10 bath-number level in the regular-coordinate Hilbert image",
            "pairing": "regular Hilbert pairing transported from physical M=S* S",
            "form": "self-adjoint full normal action W_n, diagonal plus matched exchange blocks",
            "result": "all-level tensor-pair leakage identity MAP-TYPE=orthogonal-block-norm",
            "target": "the levelwise K500 cyclic/noncyclic cross norm",
        },
        "theorem": {
            "cyclic_projection": "P_v=|v><v|/||v||^2 for v!=0",
            "rank_one_leakage": "lambda(W,v)^2=||(1-P_v)Wv||^2/||v||^2",
            "tensor_pair_identity": "lambda(W,v)^2=||Wv tensor v-v tensor Wv||^2/(2||v||^4)",
            "self_adjoint_orientation": "for self-adjoint W, ||P_v W(1-P_v)||=||(1-P_v)W P_v||=lambda(W,v)",
            "scalar_shift_invariance": "the antisymmetrized tensor cancels every scalar multiple of v",
            "multiplier_specialization": "K578's pairwise multiplier formula is the diagonal-coordinate specialization of this tensor identity",
            "all_level_uniform_certificate": "certify ||W_n v_n tensor v_n-v_n tensor W_n v_n||^2 <= 2 mu^2 ||v_n||^4 for every supported n; then the complete K500 leakage is at most mu",
            "word_norm_lower_not_required": True,
            "diagonal_multiplier_not_required": True,
        },
        "native_exchange_typing": {
            "K177_rows": native_rows,
            "level_one_exchange_free_for_q00_q10": all(row["order_1_matched_exchange_coordinates"] == 0 for row in native_rows),
            "higher_exchange_coordinates_present_for_q00_q10": all(row["orders_2_through_12_matched_exchange_coordinates"] > 0 for row in native_rows),
            "K580_first_level_result_preserved": True,
            "K580_scalar_multiplier_formula_extended_unchanged_to_all_levels": False,
        },
        "exact_controls": {
            "rows": controls,
            "row_count": len(controls),
            "all_tensor_identities_pass": all(row["identity_passes"] for row in controls),
            "all_scalar_shift_controls_pass": all(row["scalar_shift_invariant"] for row in controls),
            "off_diagonal_exchange_control_present": any(row["off_diagonal_exchange_present"] for row in controls),
            "K501_diagonal_value_replayed": controls[0]["direct_leakage_square"] == "36/25",
            "reducing_line_zero_replayed": controls[2]["direct_leakage_square"] == "0",
        },
        "decision": {
            "native_all_level_leakage_identity_emitted": True,
            "higher_level_multiplier_assumption_rejected": True,
            "actual_uniform_tensor_pair_upper_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "noncyclic_floor_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Bound the actual antisymmetrized vectors W_n v_n tensor v_n-v_n tensor W_n v_n uniformly relative to ||v_n||^2, retaining K177's exchange terms; K580 remains the exact n=1 base case.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "An exact all-level tensor-pair identity for K500 normalized leakage that remains valid for the full self-adjoint normal action when higher matched exchange blocks invalidate a scalar-multiplier description. It supplies the correct native uniform certificate but no numerical uniform upper, complete K500 leakage, noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["theorem"]
    typing = payload["native_exchange_typing"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    if not theorem["word_norm_lower_not_required"] or not theorem["diagonal_multiplier_not_required"]:
        raise AssertionError("K583 tensor certificate was weakened")
    if controls["row_count"] != 3 or not controls["all_tensor_identities_pass"] or not controls["all_scalar_shift_controls_pass"]:
        raise AssertionError("K583 exact controls failed")
    if not controls["off_diagonal_exchange_control_present"] or not controls["K501_diagonal_value_replayed"] or not controls["reducing_line_zero_replayed"]:
        raise AssertionError("K583 control coverage changed")
    if not typing["level_one_exchange_free_for_q00_q10"] or not typing["higher_exchange_coordinates_present_for_q00_q10"]:
        raise AssertionError("K583 native exchange typing changed")
    if not typing["K580_first_level_result_preserved"] or typing["K580_scalar_multiplier_formula_extended_unchanged_to_all_levels"]:
        raise AssertionError("K583 mistyped K580")
    if not decision["native_all_level_leakage_identity_emitted"] or not decision["higher_level_multiplier_assumption_rejected"]:
        raise AssertionError("K583 decision lost")
    if decision["actual_uniform_tensor_pair_upper_emitted"] or decision["complete_K500_uniform_leakage_emitted"] or decision["noncyclic_floor_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K583 overclaimed downstream closure")


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

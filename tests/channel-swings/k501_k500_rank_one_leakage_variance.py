#!/usr/bin/env python3
"""K501 exact rank-one leakage and multiplier-variance identity."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k501-k500-rank-one-leakage-variance.json"


class CertificateError(ValueError):
    pass


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(left, right, strict=True)), Fraction())


def matvec(matrix: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]) -> list[Fraction]:
    return [dot(row, vector) for row in matrix]


def leakage_square(matrix: Sequence[Sequence[Any]], vector: Sequence[Any]) -> Fraction:
    w = [[q(value) for value in row] for row in matrix]
    v = [q(value) for value in vector]
    size = len(v)
    if size < 2 or len(w) != size or any(len(row) != size for row in w):
        raise CertificateError("a square matrix and a nontrivial matching vector are required")
    if any(w[i][j] != w[j][i] for i in range(size) for j in range(size)):
        raise CertificateError("the leakage identity requires a self-adjoint rational control")
    norm_sq = dot(v, v)
    if norm_sq <= 0:
        raise CertificateError("the cyclic level vector must be nonzero")
    wv = matvec(w, v)
    expectation = dot(v, wv)
    result = dot(wv, wv) / norm_sq - expectation * expectation / (norm_sq * norm_sq)
    if result < 0:
        raise AssertionError("orthogonal residual square became negative")
    return result


def multiplier_variance(weights: Sequence[Any], multipliers: Sequence[Any]) -> Fraction:
    a = [q(value) for value in weights]
    m = [q(value) for value in multipliers]
    if not a or len(a) != len(m) or any(value <= 0 for value in a):
        raise CertificateError("equal nonempty multiplier and positive-weight sequences are required")
    total = sum(a, Fraction())
    mean = sum((weight * value for weight, value in zip(a, m, strict=True)), Fraction()) / total
    second = sum((weight * value * value for weight, value in zip(a, m, strict=True)), Fraction()) / total
    variance = second - mean * mean
    if variance < 0:
        raise AssertionError("weighted variance became negative")
    return variance


def build() -> dict[str, Any]:
    vector = [1, 2, 0]
    diagonal = [2, -1, 4]
    matrix = [[Fraction(diagonal[i] if i == j else 0) for j in range(3)] for i in range(3)]
    shifted = [[matrix[i][j] + (7 if i == j else 0) for j in range(3)] for i in range(3)]
    direct = leakage_square(matrix, vector)
    shifted_direct = leakage_square(shifted, vector)
    variance = multiplier_variance([1, 4], [2, -1])
    constant_variance = multiplier_variance([1, 4], [3, 3])
    if direct != variance or shifted_direct != direct or direct != Fraction(36, 25):
        raise AssertionError("rank-one leakage control changed")
    return {
        "schema_version": "1.0",
        "result_id": "K501-K500-RANK-ONE-LEAKAGE-VARIANCE",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "One bath-number block in K500's regular-coordinate cyclic/noncyclic split, with a one-dimensional cyclic line and self-adjoint normal action.",
        "gu_typed_objects": {
            "result": "rank-one normal-action leakage MAP-TYPE=orthogonal-block-norm",
            "carrier": "one K162 bath-number level in the regular-coordinate Hilbert image",
            "pairing": "regular Hilbert pairing transported from physical M=S* S",
            "form": "the self-adjoint bath-level normal action W_n",
            "target": "the levelwise K500 cyclic/noncyclic cross norm",
        },
        "theorem": {
            "projection": "P_v=|v><v|/||v||^2 for nonzero v",
            "leakage_square": "||P_v W(1-P_v)||^2=||(1-P_v)Wv||^2/||v||^2=||Wv||^2/||v||^2-|<v,Wv>|^2/||v||^4",
            "self_adjoint_orientation": "||P_v W(1-P_v)||=||(1-P_v)W P_v||",
            "scalar_shift_invariance": "replacing W by W+cI leaves the leakage unchanged",
            "multiplier_specialization": "for v components with weights a_i and diagonal multipliers m_i, leakage squared is the weighted variance of m_i",
            "zero_test": "leakage vanishes exactly when Wv lies in span(v); for a multiplier this means constant multiplier on the support of v",
        },
        "exact_control": {
            "vector": ["1", "2", "0"],
            "diagonal_multiplier": ["2", "-1", "4"],
            "support_weights": ["1", "4"],
            "weighted_mean": "-2/5",
            "leakage_square_direct": qstr(direct),
            "weighted_variance": qstr(variance),
            "scalar_shift": "7",
            "shifted_leakage_square": qstr(shifted_direct),
            "constant_multiplier_variance": qstr(constant_variance),
        },
        "decision": {
            "K500_leakage_reduced_to_one_vector_variance_per_level": True,
            "full_level_matrix_required": False,
            "native_all_level_variances_evaluated": False,
            "next_exact_input": "Bound the normalized orthogonal residual of W_n v_n uniformly in n, or supply word-norm lower bounds that convert existing absolute action-column estimates into normalized leakage bounds.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact rank-one leakage identity only. It supplies no native uniform all-level bound, noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public or physical conclusion.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

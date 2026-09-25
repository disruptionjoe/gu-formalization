#!/usr/bin/env python3
"""K450 exact cofinal restriction theorem for the fixed limiting K139 form.

The theorem is algebraic: if ``V_j`` are nested physical subspaces and both
the Hilbert Gram and regular form are restrictions of one fixed limiting
pairing/form, then their matrices obey exact congruence under every refinement.
The generalized defect is identically zero.  This does not apply to an
independently rebuilt cutoff form such as the K447 control.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Iterable


Matrix = list[list[Fraction]]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def diagonal(values: Iterable[Fraction]) -> Matrix:
    values = list(values)
    return [[value if i == j else Fraction() for j in range(len(values))] for i, value in enumerate(values)]


def congruence(matrix: Matrix, injection: Matrix) -> Matrix:
    return matmul(transpose(injection), matmul(matrix, injection))


def refinement_pair() -> tuple[Matrix, Matrix, Matrix, Matrix]:
    """Return a non-diagonal exact two-cell restriction control."""
    injection = [
        [Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(1)],
    ]
    fine_gram = diagonal([Fraction(1, 2)] * 4)
    fine_form = [
        [Fraction(5, 3), Fraction(1, 7), Fraction(-2, 11), Fraction(3, 13)],
        [Fraction(1, 7), Fraction(7, 4), Fraction(5, 17), Fraction(-1, 19)],
        [Fraction(-2, 11), Fraction(5, 17), Fraction(11, 5), Fraction(2, 23)],
        [Fraction(3, 13), Fraction(-1, 19), Fraction(2, 23), Fraction(13, 6)],
    ]
    return injection, fine_gram, congruence(fine_gram, injection), fine_form


def demo() -> dict:
    injection, fine_gram, coarse_gram, fine_form = refinement_pair()
    coarse_form = congruence(fine_form, injection)
    zero = [[Fraction() for _ in row] for row in coarse_form]
    reconstructed_defect = [
        [congruence(fine_form, injection)[i][j] - coarse_form[i][j] for j in range(len(coarse_form))]
        for i in range(len(coarse_form))
    ]
    if coarse_gram != diagonal([Fraction(1), Fraction(1)]):
        raise AssertionError("physical indicator refinement is not Gram isometric")
    if reconstructed_defect != zero:
        raise AssertionError("restriction of one fixed form acquired a defect")
    return {
        "schema_version": "1.0",
        "result_id": "K450-K152-LIMITING-FORM-COFINAL-RESTRICTION",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "fixed_limiting_form": "a_K139 on its fixed regular form domain",
            "nested_family": "K162 dyadic physical indicator/exterior ranges V_j",
            "physical_gram_identity": "M_j=J_j^* M_(j+1) J_j",
            "regular_form_identity": "A_j=J_j^* A_(j+1) J_j",
            "generalized_defect": "D_j=J_j^* A_(j+1) J_j-A_j=0",
            "physical_Gram_relative_radius": "0",
            "uniform_on_every_level": True,
            "cofinal_limit_bound": True,
            "requires_independent_rediscretization": False,
        },
        "exact_control": {
            "fine_dimension": 4,
            "coarse_dimension": 2,
            "non_diagonal_fine_form": True,
            "gram_isometry": coarse_gram == diagonal([Fraction(1), Fraction(1)]),
            "form_congruence": congruence(fine_form, injection) == coarse_form,
            "defect_is_zero": reconstructed_defect == zero,
        },
        "scope_boundary": {
            "applies_to_exact_restrictions_of_one_fixed_limiting_form": True,
            "applies_to_independently_rebuilt_cutoff_forms": False,
            "K447_independent_defect_erased": False,
            "complete_shifted_form_dual_residual_serialized": False,
            "coercivity_serialized": False,
            "next_distinct_spectrum_serialized": False,
            "native_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--demo", action="store_true"); args = parser.parse_args()
    if not args.demo: parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True)); return 0


if __name__ == "__main__": raise SystemExit(main())

#!/usr/bin/env python3
"""K468 quantitative perturbation-contraction certificate for K77 packets."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
I: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(2)), Fraction(0)) for j in range(2)) for i in range(2))  # type: ignore[return-value]


def inv(a: Matrix) -> Matrix:
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if determinant == 0:
        raise ValueError("singular perturbed differential")
    return ((a[1][1] / determinant, -a[0][1] / determinant), (-a[1][0] / determinant, a[0][0] / determinant))


def norm_inf(a: Matrix) -> Fraction:
    return max(sum((abs(x) for x in row), Fraction(0)) for row in a)


def qmatrix(a: Matrix) -> list[list[str]]:
    return [[str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}" for x in row] for row in a]


def certify(perturbation: Matrix) -> tuple[Matrix, Matrix, Matrix]:
    if norm_inf(perturbation) >= 1:
        raise ValueError("Neumann norm must be strictly below one")
    differential = add(I, perturbation)
    contraction = inv(differential)
    if mul(differential, contraction) != I or mul(contraction, differential) != I:
        raise ValueError("adapted contraction identity failed")
    return differential, contraction, mul(differential, contraction)


def demo() -> dict[str, Any]:
    perturbation: Matrix = ((Fraction(1, 2), Fraction(0)), (Fraction(0), Fraction(-1, 3)))
    differential, contraction, identity = certify(perturbation)
    return {
        "schema_version": "1.0",
        "result_id": "K468-K77-PERTURBATION-CONTRACTION-CERTIFICATE",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "base": "dh+hd=I with h^2=0",
            "perturbation": "D=d+delta, D^2=0",
            "quantitative_hypothesis": "||h delta||<1 (equivalently use the matching Neumann side)",
            "adapted_contraction": "h_delta=h(1+delta h)^(-1)=(1+h delta)^(-1)h",
            "conclusion": "D h_delta+h_delta D=I, hence zero cohomology",
            "closed_domain_preservation_still_required": True,
        },
        "exact_two_term_control": {
            "base_differential": qmatrix(I),
            "perturbation": qmatrix(perturbation),
            "perturbation_norm_infinity": "1/2",
            "perturbed_differential": qmatrix(differential),
            "adapted_contraction": qmatrix(contraction),
            "left_and_right_identity": qmatrix(identity),
            "cohomology_dimensions": [0, 0],
        },
        "boundary_control": {
            "perturbation": qmatrix(((-Fraction(1), Fraction(0)), (Fraction(0), -Fraction(1)))),
            "norm_infinity": "1",
            "perturbed_differential_singular": True,
            "cohomology_dimensions": [2, 2],
            "admitted": False,
        },
        "native_status": {
            "K464_adapted_contraction_route_constructive": True,
            "actual_action_coefficients_present": False,
            "native_K77_packet_selected": False,
            "physical_cohomology_claimed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

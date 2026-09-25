#!/usr/bin/env python3
"""K467 demand-derived accuracy scheduler for the K457 Gram payload."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from typing import Any


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rational_sqrt(value: Fraction) -> Fraction:
    if value < 0:
        raise ValueError("nonnegative square required")
    n, d = isqrt(value.numerator), isqrt(value.denominator)
    if n * n != value.numerator or d * d != value.denominator:
        raise ValueError("exact control requires a rational square")
    return Fraction(n, d)


def schedule(a: Fraction, g: Fraction, deficit: Fraction, c: Fraction, tail: Fraction) -> dict[str, Fraction]:
    if not (a > deficit > 0 and g > 0 and c > 0 and tail >= 0):
        raise ValueError("require a>d>0, g>0, c>0 and tail>=0")
    energy = deficit * a * g / ((a + g) * (a - deficit))
    m_dual = c * energy
    norm_budget = rational_sqrt(m_dual)
    if tail >= norm_budget:
        raise ValueError("tail exhausts the M-dual norm budget")
    return {
        "shifted_energy_budget": energy,
        "M_dual_square_budget": m_dual,
        "finite_norm_budget": norm_budget - tail,
        "finite_Gram_square_budget": (norm_budget - tail) ** 2,
    }


def demo() -> dict[str, Any]:
    a, g, deficit = Fraction(3), Fraction(2), Fraction(1)
    coercivity = Fraction(5, 3)
    tail = Fraction(3011499, 838860800)
    result = schedule(a, g, deficit, coercivity, tail)
    return {
        "schema_version": "1.0",
        "result_id": "K467-K152-RESIDUAL-ACCURACY-SCHEDULER",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "composition": {
            "K270_energy_budget": "d*a*g/((a+g)(a-d))",
            "K466_bridge_requirement": "eta_M^2 <= c*E_budget",
            "K457_finite_requirement": "sqrt(Q_12)+epsilon_tail <= sqrt(c*E_budget)",
            "K463_coercivity_input": "c=lambda_-+s>0",
        },
        "exact_control": {
            "a": q(a),
            "g": q(g),
            "target_deficit_d": q(deficit),
            "c": q(coercivity),
            "tail": q(tail),
            **{name: q(value) for name, value in result.items()},
        },
        "release_rule": {
            "finite_Gram_entries": 59586,
            "evaluate_before_native_c_and_energy_budget": False,
            "native_constants_present": False,
            "native_accuracy_released": False,
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

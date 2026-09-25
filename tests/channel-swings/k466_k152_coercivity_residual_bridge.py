#!/usr/bin/env python3
"""K466 exact coercivity bridge from M-dual to shifted form-dual energy."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dual_square(diagonal, covector):
    if len(diagonal) != len(covector) or any(x <= 0 for x in diagonal):
        raise ValueError("positive matching diagonal required")
    return sum((x * x / a for x, a in zip(covector, diagonal)), Fraction(0))


def bridge(metric, shifted_form, covector, coercivity):
    if coercivity <= 0:
        raise ValueError("positive coercivity required")
    if any(a < coercivity * m for a, m in zip(shifted_form, metric)):
        raise ValueError("shifted form does not dominate cM")
    m_dual = dual_square(metric, covector)
    form_dual = dual_square(shifted_form, covector)
    return m_dual, form_dual, m_dual / coercivity


def demo() -> dict[str, Any]:
    metric = (Fraction(2), Fraction(3))
    shifted = (Fraction(6), Fraction(12))
    covector = (Fraction(2), Fraction(3))
    coercivity = Fraction(3)
    m_dual, form_dual, ceiling = bridge(metric, shifted, covector, coercivity)
    equality = bridge(metric, tuple(coercivity * x for x in metric), covector, coercivity)
    return {
        "schema_version": "1.0",
        "result_id": "K466-K152-COERCIVITY-RESIDUAL-BRIDGE",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "hypothesis": "R+sM >= cM > 0",
            "inverse_order": "(R+sM)^(-1) <= c^(-1) M^(-1)",
            "residual_bound": "ell^*(R+sM)^(-1)ell <= c^(-1) ell^*M^(-1)ell",
            "requires_quantitative_c": True,
        },
        "nonidentity_metric_control": {
            "M_diagonal": [q(x) for x in metric],
            "shifted_form_diagonal": [q(x) for x in shifted],
            "ell": [q(x) for x in covector],
            "c": q(coercivity),
            "M_dual_square": q(m_dual),
            "shifted_form_dual_square": q(form_dual),
            "bridge_ceiling": q(ceiling),
            "bound_holds": form_dual <= ceiling,
        },
        "sharp_control": {
            "shifted_form_equals_cM": True,
            "shifted_form_dual_square": q(equality[1]),
            "bridge_ceiling": q(equality[2]),
            "equality_holds": equality[1] == equality[2],
        },
        "native_status": {
            "K463_formula_can_supply_c": True,
            "native_quantitative_c_serialized": False,
            "K152_shifted_residual_numerically_bounded": False,
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

#!/usr/bin/env python3
"""K465 exact metric-type audit for the K457 residual payload."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def diagonal_dual_square(diagonal: tuple[Fraction, ...], covector: tuple[Fraction, ...]) -> Fraction:
    if len(diagonal) != len(covector) or any(value <= 0 for value in diagonal):
        raise ValueError("positive matching diagonal required")
    return sum((x * x / weight for x, weight in zip(covector, diagonal)), Fraction(0))


def demo() -> dict[str, Any]:
    metric = (Fraction(2), Fraction(3))
    covector = (Fraction(1), Fraction(1))
    shifted_one = (Fraction(4), Fraction(6))
    shifted_two = (Fraction(8), Fraction(3))
    m_dual = diagonal_dual_square(metric, covector)
    form_one = diagonal_dual_square(shifted_one, covector)
    form_two = diagonal_dual_square(shifted_two, covector)
    return {
        "schema_version": "1.0",
        "result_id": "K465-K152-RESIDUAL-METRIC-TYPE-CORRECTION",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "identity": {
            "physical_metric": "M=S^*S",
            "serialized_vector": "S^(-*) ell",
            "serialized_square": "ell^* M^(-1) ell",
            "K152_shifted_form_dual_square": "ell^* (R+sM)^(-1) ell",
            "same_without_additional_bridge": False,
        },
        "exact_separation_control": {
            "M_diagonal": [q(x) for x in metric],
            "ell": [q(x) for x in covector],
            "M_dual_square": q(m_dual),
            "shifted_form_one_diagonal": [q(x) for x in shifted_one],
            "shifted_form_one_square": q(form_one),
            "shifted_form_two_diagonal": [q(x) for x in shifted_two],
            "shifted_form_two_square": q(form_two),
            "same_M_dual_different_shifted_form_duals": form_one != form_two,
        },
        "correction": {
            "registry_id": "K457-DUAL-METRIC-20260925",
            "K457_M_dual_payload_retained": True,
            "K457_shifted_form_dual_serialization_retracted": True,
            "numerical_Gram_evaluation_triggered": False,
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

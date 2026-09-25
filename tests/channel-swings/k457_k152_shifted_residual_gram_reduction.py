#!/usr/bin/env python3
"""K457 exact finite-Gram reduction of the complete shifted residual."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K176 = load("k176_for_k457", "k176_last_contraction_exchange_orbit_tail.py")
K179 = load("k179_for_k457", "k179_matched_normal_order_coefficient_family.py")


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def residual_square_interval(finite_square: Fraction, tail: Fraction) -> tuple[Fraction, Fraction]:
    if finite_square < 0 or tail < 0:
        raise ValueError("nonnegative finite square and tail required")
    # Exact controls use rational square roots; the general theorem is serialized symbolically.
    root_num = isqrt(finite_square.numerator)
    root_den = isqrt(finite_square.denominator)
    if root_num * root_num != finite_square.numerator or root_den * root_den != finite_square.denominator:
        raise ValueError("control finite square must be a rational square")
    finite_norm = Fraction(root_num, root_den)
    lower = max(Fraction(0), finite_norm - tail) ** 2
    upper = (finite_norm + tail) ** 2
    return lower, upper


def demo() -> dict[str, Any]:
    terms = K179.coefficient_family()
    groups = Counter((int(term["seed_impurity"]), str(term["output_signature"])) for term in terms)
    gram_entries = sum(size * (size + 1) // 2 for size in groups.values())
    tail = K176.exchange_tail(12)
    control_lower, control_upper = residual_square_interval(Fraction(9, 16), tail)
    return {
        "schema_version": "1.0",
        "result_id": "K457-K152-SHIFTED-RESIDUAL-GRAM-REDUCTION",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "residual_identity": {
            "finite_part": "r_12=S^(-*)[(R0+W_ref-rho*M)u] with exchange orders through 12 expanded by K179",
            "tail": "t_>12=S^(-*) sum_(n>12) W_ex,n G^n u",
            "complete_residual": "r=r_12+t_>12",
            "finite_square": "Q_12=sum_(i,j in coherent groups) c_i*c_j*<v_i,v_j>",
            "two_sided_bound": "max(0,sqrt(Q_12)-epsilon)^2 <= ||r||^2 <= (sqrt(Q_12)+epsilon)^2",
        },
        "finite_gram_payload": {
            "resolved_vectors": len(terms),
            "coherent_groups": len(groups),
            "self_and_cross_entries": gram_entries,
            "orders_7_through_12_entries_reused_from_K279": 59234,
            "orders_2_through_6_entries": gram_entries - 59234,
            "all_K179_coefficients_retained": True,
            "all_cross_terms_within_coherent_groups_required": True,
        },
        "tail_budget": {
            "epsilon": qstr(tail),
            "epsilon_less_than_1_over_250": tail < Fraction(1, 250),
            "post_left_adjoint": True,
        },
        "exact_control": {
            "finite_square": "9/16",
            "lower": qstr(control_lower),
            "upper": qstr(control_upper),
            "contains_finite_square": control_lower <= Fraction(9, 16) <= control_upper,
        },
        "release_test": {
            "complete_shifted_form_dual_residual_serialized": True,
            "complete_shifted_form_dual_residual_numerically_evaluated": False,
            "finite_gram_payload_fully_typed": True,
            "finite_gram_payload_numerically_complete": False,
            "coercivity_serialized": False,
            "next_distinct_spectrum_serialized": False,
            "native_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "K455_column_reference_released": True,
            "K455_residual_reference_released": True,
            "next_exact_input": "Evaluate or rigorously enclose the 59,586 coherent finite Gram entries only to the accuracy demanded by an independently proved complement-spectrum and left-floor packet.",
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

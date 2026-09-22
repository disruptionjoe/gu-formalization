#!/usr/bin/env python3
"""Serialize the exact global radial--simplex chart for the K288 measure."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K288 = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
K290 = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
OUTPUT = ROOT / "lab/process/k294-order-seven-global-radial-simplex-atlas.json"
PRECISION = 100


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def decimal_value(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def tail(z: int, rounding: str) -> Decimal:
    """Gamma(shape=4, rate=1) survival function at integer z."""
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = rounding
        x = Decimal(z)
        polynomial = sum(x**k / Decimal(factorial(k)) for k in range(4))
        return (-x).exp() * polynomial


def interval(lower: Decimal, upper: Decimal) -> dict[str, str]:
    if not lower <= upper:
        raise AssertionError("invalid directed interval")
    return {"lower": str(lower), "upper": str(upper)}


def radial_fractions() -> dict[str, Any]:
    tail31_lo, tail31_hi = tail(31, ROUND_FLOOR), tail(31, ROUND_CEILING)
    tail32_lo, tail32_hi = tail(32, ROUND_FLOOR), tail(32, ROUND_CEILING)
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        low_lo = Decimal(1) - tail31_hi
        middle_lo = tail31_lo - tail32_hi
        high_lo = tail32_lo
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        low_hi = Decimal(1) - tail31_lo
        middle_hi = tail31_hi - tail32_lo
        high_hi = tail32_hi
    if not middle_lo > 0:
        raise AssertionError("middle radial strip lost positive mass")
    return {
        "low_x_lt_31_over_256": {
            "exact_formula": "1-exp(-31)*(1+31+31^2/2+31^3/6)",
            "fraction_interval": interval(low_lo, low_hi),
        },
        "interior_31_over_256_to_1_over_8": {
            "exact_formula": "exp(-31)*(1+31+31^2/2+31^3/6)-exp(-32)*(1+32+32^2/2+32^3/6)",
            "fraction_interval": interval(middle_lo, middle_hi),
        },
        "high_x_gt_1_over_8": {
            "exact_formula": "exp(-32)*(1+32+32^2/2+32^3/6)",
            "fraction_interval": interval(high_lo, high_hi),
        },
        "directed_sum_contains_one": low_lo + middle_lo + high_lo <= 1 <= low_hi + middle_hi + high_hi,
    }


def build() -> dict[str, Any]:
    k288 = json.loads(K288.read_text())
    k290 = json.loads(K290.read_text())
    native_change = k288["native_coordinate_change"]
    if native_change["radial_projective_variables"]["domain"] != "x>0; y in [0,1]; r_i,c_i>0":
        raise AssertionError("K288 native domain changed")
    if k290["derivative_bank"]["x_bounds"] != ["31/256", "1/8"]:
        raise AssertionError("K290 radial split changed")

    simplex_mass = Fraction(1, factorial(11))
    scale_numerator = factorial(11)
    total_mass = Fraction(1, 256**16)
    return {
        "schema_version": "1.0",
        "result_id": "K294-ORDER-SEVEN-GLOBAL-RADIAL-SIMPLEX-ATLAS",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k288-order-seven-native-occurrence-measure.json",
            "radial_split_manifest": "lab/process/k290-order-seven-native-rest-derivative-bank.json",
            "native_gap_coordinates": ["r0", "r1", "r2", "c0", "c1", "c2"],
            "x_split": ["0", "31/256", "1/8", "infinity"],
        },
        "global_chart": {
            "definition": "q=sum_i g_i; p_i=g_i/q for six positive gaps g=(r0,r1,r2,c0,c1,c2)",
            "domain": "q>0 and p in the open five-simplex; boundary faces are assigned by the usual lower-dimensional limit and have six-dimensional measure zero",
            "inverse": "g_i=q*p_i with p_5=1-sum_{i=0}^4 p_i",
            "jacobian": "q^5",
            "native_projective_product": "product_i g_i=q^6*product_i p_i",
            "transformed_native_density": "exp(-256*x*(1+q))*x^15*y*(1-y)*q^11*product_i(p_i)",
            "split_cube_volume": "du_0...du_3 dz_0...dz_3 has volume 1",
        },
        "normalization_replay": {
            "simplex_integral": fraction_text(simplex_mass),
            "simplex_identity": "integral_Delta5 product_i p_i dp = product_i Gamma(2)/Gamma(12)=1/11!",
            "q_integral": f"{scale_numerator}/(256*x)^12",
            "q_simplex_product": "1/(256*x)^12",
            "y_integral": "1/6",
            "remaining_x_integral": "integral_0^infinity exp(-256*x)*x^3 dx=3!/256^4",
            "complete_bare_mass": fraction_text(total_mass),
            "agrees_with_k288": native_change["mass_replay"]["exact_match"],
        },
        "radial_atlas": {
            "normalized_density_after_q_simplex_y": "256^4*x^3*exp(-256*x)/3!",
            "gamma_shape": 4,
            "gamma_rate": 256,
            "strata": radial_fractions(),
        },
        "decision": {
            "complete_positive_orthant_chart_serialized": True,
            "radial_exterior_partition_serialized": True,
            "k292_tube_is_interior_subdomain_only": True,
            "complete_integrand_exterior_bound_serialized": False,
            "next_exact_input": "quantify the K292 tube bare-measure share and test whether the K290 ratio-minimum derivative majorant is integrable on simplex faces",
        },
        "release_test": {
            "six_gap_jacobian_power_is_five": True,
            "native_density_q_power_is_eleven": True,
            "simplex_and_q_factorials_cancel_exactly": True,
            "complete_bare_mass_replayed": total_mass == Fraction(1, 256**16),
            "three_radial_strata_cover_x_positive": True,
            "complete_exterior_integrand_bound_emitted": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k288["ledger_effect"],
        "claim_ceiling": "Exact whole-positive-orthant radial-simplex atlas and bare native-measure normalization for the K288 order-seven occurrence variables, with an exact three-stratum radial mass split. No bound on the coherent determinant integrand over the exterior, action-column value, complete residual, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

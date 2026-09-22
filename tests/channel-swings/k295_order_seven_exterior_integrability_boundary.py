#!/usr/bin/env python3
"""Quantify the K292 tube mass and the K290 exterior integrability boundary."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K290 = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
K292 = ROOT / "lab/process/k292-order-seven-disjoint-native-tube-atlas.json"
K294 = ROOT / "lab/process/k294-order-seven-global-radial-simplex-atlas.json"
OUTPUT = ROOT / "lab/process/k295-order-seven-exterior-integrability-boundary.json"
PRECISION = 100
H = Fraction(1, 32768)
BASE = [Fraction(1, 32), Fraction(1, 64), Fraction(1, 128), Fraction(1, 40), Fraction(1, 80), Fraction(1, 160)]


def d(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def f(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def upper_decimal(value: Fraction, exponent_argument: Fraction) -> Decimal:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        return d(value) * (-d(exponent_argument)).exp()


def build() -> dict[str, Any]:
    k290 = json.loads(K290.read_text())
    k292 = json.loads(K292.read_text())
    k294 = json.loads(K294.read_text())
    if k292["fixed_control"]["transverse_shape_radius"] != f(H):
        raise AssertionError("K292 tube radius changed")
    xmin, xmax = Fraction(31, 256), Fraction(1, 8)
    width = xmax - xmin
    minima = [value - H for value in BASE]
    maxima = [value * Fraction(5, 4) + H for value in BASE]
    if not all(value > 0 for value in minima):
        raise AssertionError("tube lost positivity")
    q_min = sum(minima)
    product_max = Fraction(1)
    for value in maxima:
        product_max *= value
    volume = Fraction(k292["volume_identity"]["total_native_volume"])
    algebraic_prefactor = xmax**15 * product_max * volume * width * Fraction(1, 6)
    exponent_argument = 256 * xmin * (1 + q_min)
    tube_mass_upper = upper_decimal(algebraic_prefactor, exponent_argument)
    total_mass = Fraction(k294["normalization_replay"]["complete_bare_mass"])
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        share_upper = tube_mass_upper / d(total_mass)
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        exterior_lower = Decimal(1) - share_upper
    if not share_upper < Decimal("1e-20"):
        raise AssertionError("tube mass diagnostic changed scale")

    table = []
    for order in range(5):
        exponent = 1 - order
        integrable = exponent > -1
        divergence = "none" if integrable else "logarithmic" if exponent == -1 else "power"
        table.append(
            {
                "shape_derivative_order": order,
                "ratio_minimum_power_from_k290": -order,
                "native_density_power": 1,
                "combined_face_power": exponent,
                "one_gap_integrable_at_zero": integrable,
                "majorant_divergence": divergence,
            }
        )

    return {
        "schema_version": "1.0",
        "result_id": "K295-ORDER-SEVEN-EXTERIOR-INTEGRABILITY-BOUNDARY",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "derivative_manifest": "lab/process/k290-order-seven-native-rest-derivative-bank.json",
            "tube_manifest": "lab/process/k292-order-seven-disjoint-native-tube-atlas.json",
            "global_atlas_manifest": "lab/process/k294-order-seven-global-radial-simplex-atlas.json",
            "x_interval": [f(xmin), f(xmax)],
            "tube_scale_interval": ["1/1", "5/4"],
            "tube_shape_radius": f(H),
        },
        "tube_bare_measure_upper": {
            "method": "supremum of exp(-256*x*(1+sum g))*x^15*product(g_i) on the tube times exact K292 drdc volume, exact x width, exact y integral 1/6 and unit split-cube volume",
            "gap_sum_lower": f(q_min),
            "gap_product_upper": f(product_max),
            "exact_algebraic_prefactor_before_exponential": f(algebraic_prefactor),
            "exponential_argument_lower": f(exponent_argument),
            "bare_mass_abs_upper": str(tube_mass_upper),
            "fraction_of_complete_bare_mass_upper": str(share_upper),
            "complete_bare_mass": f(total_mass),
            "exterior_fraction_lower": str(exterior_lower),
            "interpretation": "The K292 tube carries at most this share of the bare native measure. This does not compare the coherent determinant integrand inside and outside the tube.",
        },
        "pointwise_majorant_face_audit": {
            "k290_rule": "for m>=1 the endpoint-safe old-kernel derivative majorant contains ratio_min^-m",
            "native_face_weight": "the projective product contributes one power of the vanishing gap s",
            "combined_behavior": "s^(1-m) before determinant coalescent cancellation",
            "one_gap_integrability": table,
            "first_nonintegrable_order": 2,
            "fourth_order_global_extension_legal": False,
            "true_integrand_divergence_proved": False,
            "reason": "K290 took absolute factorwise bounds before retaining the companion and Cauchy determinant zeros; failure of this majorant is not failure of the coherent integrand.",
        },
        "decision": {
            "k292_interior_tube_has_nonnegligible_bare_measure_share": False,
            "k290_pointwise_fourth_derivative_bank_extends_to_simplex_faces": False,
            "complete_exterior_integrand_bound_serialized": False,
            "required_repair": "construct coalescent-face charts that retain determinant zeros and integrate the native gap weight before taking the fourth-derivative absolute envelope; treat radial low/high strata with the K294 gamma weight",
            "next_exact_input": "a cancellation-preserving size-three/size-four coalescent-face derivative packet on the K294 simplex chart, beginning with one vanishing-gap face and its codimension-two intersections",
        },
        "release_test": {
            "exact_k292_volume_used": volume == Fraction(2021, 96714065569170333976494080),
            "complete_native_bare_mass_used": total_mass == Fraction(1, 256**16),
            "tube_share_strictly_below_one": share_upper < 1,
            "orders_zero_and_one_integrable_under_current_majorant": all(row["one_gap_integrable_at_zero"] for row in table[:2]),
            "orders_two_through_four_nonintegrable_under_current_majorant": all(not row["one_gap_integrable_at_zero"] for row in table[2:]),
            "true_integrand_divergence_claimed": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k290["ledger_effect"],
        "claim_ceiling": "Rigorous upper bound on the K292 tube's share of the K288 bare native measure and an exact integrability audit of the K290 ratio-minimum pointwise derivative majorant at one-gap simplex faces. The current fourth-order majorant is nonintegrable from order two onward; no divergence of the true coherent integrand, complete exterior-integrand bound, action-column value, residual, native K152 interval, physical state, source/ledger move, canon, paper or public claim is established.",
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

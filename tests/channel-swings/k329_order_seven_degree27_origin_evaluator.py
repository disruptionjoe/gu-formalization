#!/usr/bin/env python3
"""Degree-27 normalized origin evaluator for the K326 endpoint charts.

The raw regularized D4 and bordered B5 have radial degrees -16 and -11.
Each divided-difference entry is therefore scaled by its exact row/column
radial exponent before interval substitution.  K328 bounds every resulting
scaled Bessel derivative on a zero-inclusive radial cell.  The complete B5
Taylor determinant is assembled from shared normalized entry jets before one
coefficient enclosure; the terminal weighted entry is multiplied by its
remaining radial factor and hence vanishes continuously at r=0.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K312_MODULE = HERE / "k312_order_seven_positive_cell_measure_backend.py"
K314_MODULE = HERE / "k314_order_seven_projective_face_oracle.py"
K326_MODULE = HERE / "k326_order_seven_signed_entry_jet_chart_bank.py"
K328_MODULE = HERE / "k328_order_seven_scaled_derivative_envelope_bank.py"
K321 = ROOT / "lab/process/k321-order-seven-radial-projective-tensor-atlas.json"
K327 = ROOT / "lab/process/k327-order-seven-adaptive-interior-subdivision.json"
K328 = ROOT / "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json"
OUTPUT = ROOT / "lab/process/k329-order-seven-degree27-origin-evaluator.json"

ctx.dps = 180
ctx.threads = 1

RADIUS = (Fraction(0), Fraction(1, 16))
S = (Fraction(1, 4), Fraction(3, 4))
GAPS = [(Fraction(1, 8), Fraction(5, 24)) for _ in range(6)]
ROW_ORDERS = [0, 1, 2, 0]
COLUMN_ORDERS = [0, 1, 2, 0]
NORMALIZED_ARGUMENT_MAX = Fraction(3, 2)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def symmetric(upper: arb) -> arb:
    return arb(0, upper.upper())


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def normalized_nodes() -> dict[str, list[Fraction]]:
    x0, x1 = S
    b0, b1 = 1 - S[1], 1 - S[0]
    p0 = min(interval[0] for interval in GAPS)
    p1 = max(interval[1] for interval in GAPS)
    lowers = {
        "odd_left": [b0 * p0 * count for count in (3, 2, 1, 0)],
        "odd_right": [x0 / 2 + b0 * p0 * count for count in (3, 2, 1, 0)],
        "even_left": [b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
        "even_right": [x0 / 2 + b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
    }
    uppers = {
        "odd_left": [b1 * p1 * count for count in (3, 2, 1, 0)],
        "odd_right": [x1 / 2 + b1 * p1 * count for count in (3, 2, 1, 0)],
        "even_left": [b1 * p1 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
        "even_right": [x1 / 2 + b1 * p1 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
    }
    return {**{f"{key}_lower": value for key, value in lowers.items()}, **{f"{key}_upper": value for key, value in uppers.items()}}


def scaled_dd_upper(k328, argument_lower: Fraction, row_order: int, column_order: int, y_order: int = 0) -> arb:
    if argument_lower <= 0:
        raise AssertionError("a nonterminal normalized argument touched zero")
    order = row_order + column_order + y_order
    width = RADIUS[1] * NORMALIZED_ARGUMENT_MAX
    phi = k328.scaled_derivative_upper(order, width)
    value = phi / (argument_lower ** (order + 1) * math.factorial(row_order) * math.factorial(column_order))
    return arb(q(value))


def normalized_entry_jets(k326, k328) -> tuple[list[list[list[arb]]], dict[str, Any], arb]:
    nodes = normalized_nodes()
    if max(
        max(nodes["odd_left_upper"]) + max(nodes["odd_right_upper"]),
        max(nodes["even_left_upper"]) + max(nodes["even_right_upper"]),
    ) > NORMALIZED_ARGUMENT_MAX:
        raise AssertionError("normalized argument maximum is too small")

    d4_lower = min(nodes["odd_left_lower"]) + min(nodes["odd_right_lower"])
    d4 = [
        [scaled_dd_upper(k328, d4_lower, row, column) for column in range(4)]
        for row in range(4)
    ]
    d4_bound = arb(1)
    for row in d4:
        d4_bound *= sum((value * value for value in row), arb(0)).sqrt()

    jets = [[[arb(0), arb(0), arb(0)] for _ in range(5)] for _ in range(5)]
    nonterminal_lowers: list[Fraction] = []
    x_norm_max = S[1]
    for row in range(4):
        for column in range(4):
            if (row, column) == (3, 3):
                # K320/K326 already absorb the endpoint singularity into Phi_m.
                # The row/column radial ledger assigns this slot one remaining
                # power of r, so its normalized interval vanishes at r=0.
                raw = k326.terminal_jet_uppers((Fraction(0), RADIUS[1] * x_norm_max))
                jets[row][column] = [symmetric(arb(q(RADIUS[1])) * value) for value in raw]
                continue
            lower = nodes["even_left_lower"][row] + nodes["even_right_lower"][column]
            nonterminal_lowers.append(lower)
            a, c = ROW_ORDERS[row], COLUMN_ORDERS[column]
            jets[row][column][0] = symmetric(scaled_dd_upper(k328, lower, a, c))
            delta = Fraction(0) if row < 3 and column < 3 else x_norm_max
            if delta:
                jets[row][column][1] = symmetric(arb(q(delta)) * scaled_dd_upper(k328, lower, a, c, 1))
                jets[row][column][2] = symmetric(arb(q(delta * delta)) * scaled_dd_upper(k328, lower, a, c, 2))

    y_half = Fraction(1, 2)
    for row in range(3):
        a = ROW_ORDERS[row]
        lower = nodes["even_left_lower"][row]
        nonterminal_lowers.append(lower)
        f0 = scaled_dd_upper(k328, lower, a, 0)
        f1 = scaled_dd_upper(k328, lower, a + 1, 0)
        f2 = scaled_dd_upper(k328, lower, a + 2, 0)
        jets[row][4][0] = symmetric(arb(q(y_half)) * f0)
        jets[row][4][1] = symmetric(f0 + arb(q(y_half * x_norm_max * (a + 1))) * f1)
        jets[row][4][2] = symmetric(arb(q(2 * x_norm_max * (a + 1))) * f1 + arb(q(y_half * x_norm_max * x_norm_max * (a + 1) * (a + 2))) * f2)

    for column in range(3):
        c = COLUMN_ORDERS[column]
        lower = nodes["even_right_lower"][column]
        nonterminal_lowers.append(lower)
        f0 = scaled_dd_upper(k328, lower, 0, c)
        f1 = scaled_dd_upper(k328, lower, 0, c + 1)
        f2 = scaled_dd_upper(k328, lower, 0, c + 2)
        jets[4][column][0] = symmetric(f0)
        jets[4][column][1] = symmetric(f0 + arb(q(x_norm_max * (c + 1))) * f1)
        jets[4][column][2] = symmetric(arb(q(2 * x_norm_max * (c + 1))) * f1 + arb(q(x_norm_max * x_norm_max * (c + 1) * (c + 2))) * f2)

    audit = {
        "radial_cell": [q(value) for value in RADIUS],
        "projective_s_cell": [q(value) for value in S],
        "normalized_argument_upper": q(NORMALIZED_ARGUMENT_MAX),
        "scaled_Bessel_width": q(RADIUS[1] * NORMALIZED_ARGUMENT_MAX),
        "D4_minimum_normalized_argument": q(d4_lower),
        "minimum_nonterminal_B5_normalized_argument": q(min(nonterminal_lowers)),
        "D4_entry_radial_exponent": "row_order+column_order+1; determinant total 16",
        "B5_entry_radial_exponent": "row_order+column_order+1 with border order zero; every nonzero determinant monomial totals 11",
        "terminal_normalized_entry_rule": f"r*Phi_m with r<={q(RADIUS[1])}; continuous value zero at r=0",
        "raw_Bessel_evaluation_at_zero_used": False,
        "literal_zero_slots": [[3, 4], [4, 3], [4, 4]],
    }
    return jets, audit, d4_bound


def build() -> dict[str, Any]:
    k312 = load_module(K312_MODULE, "k329_k312_backend")
    k314 = load_module(K314_MODULE, "k329_k314_backend")
    k326 = load_module(K326_MODULE, "k329_k326_backend")
    k328_module = load_module(K328_MODULE, "k329_k328_backend")
    k321 = json.loads(K321.read_text())
    k327 = json.loads(K327.read_text())
    k328 = json.loads(K328.read_text())
    if k321["degree_27_origin_ledger"]["complete_regularized_radial_degree"] != -27:
        raise AssertionError("K321 degree ledger changed")
    if not k328["decision"]["degree_27_origin_evaluator_released"]:
        raise AssertionError("K328 did not release the origin evaluator")
    if not k327["decision"]["first_exact_cover_adaptive_interior_oracle_implemented"]:
        raise AssertionError("K327 interior oracle unavailable")

    jets, audit, d4_bound = normalized_entry_jets(k326, k328_module)
    determinant_jets = k326.determinant_taylor(jets)
    projective = k314.projective_polynomial_upper(
        {name: interval for name, interval in zip(k314.GAPS, GAPS, strict=True)}
    )
    # K326's endpoint/Peano scalar contains x^2.  After r^27 normalizes the
    # two determinants, x^2=(r*s)^2 is bounded by R^2*s_max^2.
    scalar = Fraction(4, 120) * (RADIUS[1] * S[1]) ** 2 * Fraction(1, 16) * projective
    one_endpoint = [d4_bound * value * arb(q(scalar)) for value in determinant_jets]
    all_charts = [arb(16) * value for value in one_endpoint]

    radial_mass = k312.radial_finite_upper(RADIUS[0], RADIUS[1], 6)
    s_mass = k312.polynomial_cell_moment(S[0], S[1], 3, 29)
    gap_volume = math.prod((upper - lower for lower, upper in GAPS), start=Fraction(1))
    measure = radial_mass * s_mass * gap_volume
    integrated = [value * arb(q(measure)) for value in all_charts]
    if any(not math.isfinite(float(value.upper())) or value.upper() <= 0 for value in integrated):
        raise AssertionError("origin integral upper is not finite positive")

    return {
        "schema_version": "1.0",
        "result_id": "K329-ORDER-SEVEN-DEGREE27-ORIGIN-EVALUATOR",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k321-order-seven-radial-projective-tensor-atlas.json",
                "lab/process/k327-order-seven-adaptive-interior-subdivision.json",
                "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "radial_cell": [q(value) for value in RADIUS],
            "projective_s_cell": [q(value) for value in S],
            "six_gap_cells": [[q(a), q(b)] for a, b in GAPS],
            "endpoint_chart_count": 16,
            "coefficient_orders": [0, 1, 2],
        },
        "normalized_entry_audit": audit,
        "degree_27_complete_determinant": {
            "D4_normalized_abs_upper": upper_text(d4_bound),
            "bordered_B5_normalized_value_first_second_intervals": [str(value) for value in determinant_jets],
            "sixteen_chart_normalized_value_first_second_abs_uppers": [upper_text(value) for value in all_charts],
            "shared_entry_interval_substitution_precedes_determinant_enclosure": True,
            "familywise_absolute_summation_used": False,
            "permutationwise_absolute_summation_used_for_B5": False,
            "literal_border_zeros_retained": True,
        },
        "origin_measure": {
            "radial_weight": "exp(-256*r)*r^6",
            "radial_upper": q(radial_mass),
            "projective_weight": "s^3*(1-s)^29",
            "projective_exact_mass": q(s_mass),
            "six_gap_exact_volume": q(gap_volume),
            "combined_measure_upper": q(measure),
            "integrated_value_first_second_abs_uppers": [upper_text(value) for value in integrated],
            "covers_r_zero": True,
            "raw_zero_call_required": False,
        },
        "scope_boundary": {
            "covered": "degree-27 normalized radial origin r in [0,1/16] on s in [1/4,3/4], all six positive gap cells and all sixteen endpoint charts",
            "not_covered": ["s in [0,1/4]", "s in [3/4,1]", "the exponential tail", "recursive tolerance closure", "a complete y-master constant"],
            "positive_projective_interior_only": True,
        },
        "decision": {
            "continuous_degree27_origin_evaluator_implemented": True,
            "origin_cell_value_first_second_integrated_uppers_finite": True,
            "projective_faces_complete": False,
            "exponential_tail_complete": False,
            "complete_origin_tail_face_sum_emitted": False,
            "complete_y_master_constant_emitted": False,
            "next_exact_input": "use the same normalized entry bank for a polynomial-growth exponential-tail majorant, then resolve the s=0 and s=1 cells without a positive normalized argument floor",
        },
        "release_test": {
            "degree_minus_27_replayed": True,
            "all_sixteen_endpoint_charts_included": True,
            "all_integrated_uppers_finite_positive": True,
            "raw_zero_evaluation_used": False,
            "projective_face_overclaim": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k328["ledger_effect"],
        "source_routing": k328["source_routing"],
        "claim_ceiling": "First finite complete-determinant value/first/second enclosure on a radial cell containing r=0 after exact degree-27 normalization. K328 scaled derivatives are inserted with the D4 degree-16 and bordered-B5 degree-11 row/column ledger, the complete B5 Taylor determinant is assembled before coefficient enclosure, and K310's positive r^6*s^3*(1-s)^29 measure gives finite integrated uppers on s in [1/4,3/4]. The two projective face cells, exponential tail and recursive tolerance closure remain open, so no complete y-master constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is released.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["radial_cell"] != ["0", "1/16"] or fixed["projective_s_cell"] != ["1/4", "3/4"]:
        raise AssertionError("origin cell changed")
    audit = payload["normalized_entry_audit"]
    if audit["raw_Bessel_evaluation_at_zero_used"] or audit["literal_zero_slots"] != [[3, 4], [4, 3], [4, 4]]:
        raise AssertionError("zero-safe literal-zero contract changed")
    determinant = payload["degree_27_complete_determinant"]
    if not determinant["shared_entry_interval_substitution_precedes_determinant_enclosure"]:
        raise AssertionError("post-assembly enclosure order lost")
    if determinant["familywise_absolute_summation_used"] or determinant["permutationwise_absolute_summation_used_for_B5"]:
        raise AssertionError("early B5 absolute summation reintroduced")
    if len(determinant["sixteen_chart_normalized_value_first_second_abs_uppers"]) != 3:
        raise AssertionError("normalized coefficient bank changed")
    measure = payload["origin_measure"]
    if not measure["covers_r_zero"] or measure["raw_zero_call_required"] or len(measure["integrated_value_first_second_abs_uppers"]) != 3:
        raise AssertionError("origin measure contract changed")
    if not payload["scope_boundary"]["positive_projective_interior_only"]:
        raise AssertionError("projective scope hidden")
    decision = payload["decision"]
    if not decision["continuous_degree27_origin_evaluator_implemented"] or decision["projective_faces_complete"]:
        raise AssertionError("origin/face disposition changed")
    if decision["complete_y_master_constant_emitted"]:
        raise AssertionError("complete numerical release overclaimed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

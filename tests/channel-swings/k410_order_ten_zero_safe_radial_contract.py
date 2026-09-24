#!/usr/bin/env python3
"""Certify the zero-safe radial scaling needed by the K409 Peano terms."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K279 = ROOT / "lab/process/k279-higher-order-andreief-structural-closure.json"
K405 = ROOT / "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json"
K409 = ROOT / "lab/process/k409-order-ten-positive-peano-contract.json"
OUTPUT = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"

ctx.dps = 180
ctx.threads = 1

MAX_ORDER = 2
WIDTHS = (Fraction(1, 64), Fraction(1, 16), Fraction(1), Fraction(4))


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def nu_term_bound(order: int, nu: int, width: Fraction) -> Fraction:
    if nu == 0:
        return width**order
    if not 1 <= nu <= order + 1:
        raise AssertionError("impossible Bessel order in derivative recurrence")
    return Fraction(2 ** (nu - 1) * math.factorial(nu - 1), 1) * width ** (order + 1 - nu)


def scaled_derivative_upper(order: int, width: Fraction) -> Fraction:
    total = Fraction(0)
    for index in range(order + 1):
        nu = abs(1 - order + 2 * index)
        total += math.comb(order, index) * nu_term_bound(order, nu, width)
    return Fraction(2, 2**order) * total


def bessel_derivative_abs(argument: arb, order: int) -> arb:
    total = arb(0)
    for index in range(order + 1):
        nu = abs(1 - order + 2 * index)
        total += math.comb(order, index) * argument.bessel_k(nu)
    return arb(2) ** (1 - order) * total


def positive_control(order: int, width: Fraction, argument: Fraction) -> dict[str, Any]:
    w = arb(q(argument))
    scaled = w ** (order + 1) * bessel_derivative_abs(w, order)
    bound = scaled_derivative_upper(order, width)
    return {
        "order": order,
        "width": q(width),
        "argument": q(argument),
        "scaled_interval": str(scaled),
        "rational_upper": q(bound),
        "contained": scaled.upper() <= arb(q(bound)).lower(),
    }


def peano_kernel(t: arb) -> arb:
    node = arb(1) / 256
    if t.upper() <= node.lower():
        return ((-256 * t).exp() - 1 + 256 * t) / (256**2)
    if t.lower() >= node.upper():
        return (-256 * t).exp() / (256**2)
    raise AssertionError("control interval straddles the Peano join")


def build() -> dict[str, Any]:
    k279 = json.loads(K279.read_text())
    k405 = json.loads(K405.read_text())
    k409 = json.loads(K409.read_text())
    order_row = next(row for row in k279["orders"] if row["order"] == 10)
    if order_row["small_rho_power"] != 9:
        raise AssertionError("K279 order-ten origin power changed")
    if k405["fixed_control"]["positive_time_variables"] != 22:
        raise AssertionError("K405 axis census changed")
    if k409["one_axis_identity"]["kernel_zero_order_at_origin"] != 2:
        raise AssertionError("K409 Peano zero order changed")

    rows = []
    controls = []
    for width in WIDTHS:
        bounds = [scaled_derivative_upper(order, width) for order in range(MAX_ORDER + 1)]
        rows.append({"width": q(width), "orders": [0, 1, 2], "Phi_abs_uppers": [q(value) for value in bounds]})
        for order in range(MAX_ORDER + 1):
            for argument in (width / 4, width):
                controls.append(positive_control(order, width, argument))
    if not all(row["contained"] for row in controls):
        raise AssertionError("scaled derivative control escaped")

    peano_controls = []
    for value in (Fraction(1, 4096), Fraction(1, 512), Fraction(1, 256), Fraction(1, 128), Fraction(1, 16)):
        t = arb(q(value))
        kernel = peano_kernel(t)
        upper = t * t / 2
        peano_controls.append({
            "t": q(value),
            "kernel_interval": str(kernel),
            "quadratic_upper": q(value * value / 2),
            "contained": kernel.lower() >= 0 and kernel.upper() <= upper.lower(),
        })
    if not all(row["contained"] for row in peano_controls):
        raise AssertionError("Peano quadratic bound failed")

    zero_limits = []
    for order in range(MAX_ORDER + 1):
        leading = order + 1
        indices = [i for i in range(order + 1) if abs(1 - order + 2 * i) == leading]
        limit = Fraction(2, 2**order) * sum(
            (Fraction(math.comb(order, i) * 2 ** (leading - 1) * math.factorial(leading - 1), 1) for i in indices),
            start=Fraction(0),
        )
        zero_limits.append(q(limit))

    raw_kernel_count = 10 + 2
    derivative_cost = 2
    radial_jacobian_degree = 22 - 1
    peano_gain = 2
    raw_second_degree = -(raw_kernel_count + derivative_cost)
    final_degree = radial_jacobian_degree + raw_second_degree + peano_gain
    if final_degree != 9:
        raise AssertionError("order-ten radial degree does not replay K279")

    return {
        "schema_version": "1.0",
        "result_id": "K410-ORDER-TEN-ZERO-SAFE-RADIAL-CONTRACT",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k279-higher-order-andreief-structural-closure.json",
                "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json",
                "lab/process/k409-order-ten-positive-peano-contract.json",
            ],
            "order": 10,
            "raw_time_axes": 22,
            "maximum_active_axis_derivative_order": 2,
            "raw_kernel_factors_per_gram_entry": raw_kernel_count,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "scaled_bessel_bank": {
            "definition": "Phi_m(w)=w^(m+1)*abs((2*K1)^(m)(w))",
            "derivative_recurrence": "abs((2*K1)^(m)(w)) <= 2^(1-m)*sum_k binom(m,k) K_|1-m+2k|(w)",
            "positive_order_rule": "w^nu*K_nu(w) decreases from 2^(nu-1)*(nu-1)! for integer nu>0",
            "zero_order_rule": "w*K0(w)<=w*K1(w)<=1",
            "rows": rows,
            "continuous_zero_limits": zero_limits,
            "raw_Bessel_evaluation_at_zero_used": False,
            "all_bounds_exact_rational": True,
        },
        "peano_majorant": {
            "global_bound": "0<=K_256(t)<=t^2/2 for all t>=0",
            "lower_piece_proof": "exp(-x)-1+x<=x^2/2 with x=256*t",
            "upper_piece_proof": "2*exp(-x)<=x^2 for x>=1",
            "join": "t=1/256",
            "controls": peano_controls,
        },
        "all_zero_radial_ledger": {
            "gram_raw_kernel_degree": -raw_kernel_count,
            "two_active_derivatives_degree_cost": -derivative_cost,
            "complete_second_derivative_degree": raw_second_degree,
            "twenty_two_axis_radial_jacobian_degree": radial_jacobian_degree,
            "active_peano_zero_gain": peano_gain,
            "final_radial_degree": final_degree,
            "K279_order_ten_small_rho_power_replayed": final_degree == order_row["small_rho_power"],
            "origin_integrable": final_degree > -1,
            "scope": "the all-twenty-two-axis origin of the first K409 hybrid; later hybrids have fixed positive preceding nodes and require the a successor partial-face ledger",
        },
        "decision": {
            "zero_safe_scaled_derivative_bank_emitted": True,
            "global_quadratic_peano_majorant_emitted": True,
            "all_zero_origin_integrability_closed": True,
            "partial_face_preconditioners_emitted": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "compile the exact K405 zero and coalescence masks reachable in every K409 hybrid domain, then exercise the complete coherent derivative evaluator away from those faces",
        },
        "release_test": {
            "orders_zero_through_two_covered": len(rows[0]["Phi_abs_uppers"]) == 3,
            "all_positive_controls_contained": all(row["contained"] for row in controls),
            "zero_limits_2_2_4": zero_limits == ["2", "2", "4"],
            "peano_quadratic_controls_contained": all(row["contained"] for row in peano_controls),
            "radial_degree_nine_replayed": final_degree == 9,
            "raw_zero_evaluation_not_used": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k409["ledger_effect"],
        "source_routing": k409["source_routing"],
        "claim_ceiling": "Exact rational zero-inclusive envelopes for the value, first and second derivatives of 2*K1, a global K_256(t)<=t^2/2 Peano majorant, and the complete degree-nine all-zero radial integrability ledger for the first order-ten hybrid. Partial coalescence-face preconditioners, recursive whole-domain coverage, all twenty-two numerical hybrid integrals, the complete order-ten remainder and integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["order"], fixed["raw_time_axes"], fixed["maximum_active_axis_derivative_order"], fixed["raw_kernel_factors_per_gram_entry"]) != (10, 22, 2, 12):
        raise AssertionError("K410 fixed census changed")
    bank = payload["scaled_bessel_bank"]
    if bank["raw_Bessel_evaluation_at_zero_used"] or not bank["all_bounds_exact_rational"] or bank["continuous_zero_limits"] != ["2", "2", "4"]:
        raise AssertionError("K410 zero-safe bank changed")
    if not all(row["contained"] for row in payload["peano_majorant"]["controls"]):
        raise AssertionError("K410 Peano controls failed")
    ledger = payload["all_zero_radial_ledger"]
    if ledger["final_radial_degree"] != 9 or not ledger["K279_order_ten_small_rho_power_replayed"] or not ledger["origin_integrable"]:
        raise AssertionError("K410 radial ledger changed")
    decision = payload["decision"]
    if not decision["all_zero_origin_integrability_closed"] or decision["partial_face_preconditioners_emitted"] or decision["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K410 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K410 release test failed")


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

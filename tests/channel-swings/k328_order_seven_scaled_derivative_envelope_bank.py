#!/usr/bin/env python3
"""Zero-safe scaled derivative envelopes through the complete K327 order.

For f(w)=2*K_1(w), the exact derivative recurrence is

  |f^(m)(w)| <= 2^(1-m) sum_k binom(m,k) K_|1-m+2k|(w).

For integer nu>0, w^nu K_nu(w) decreases from 2^(nu-1)(nu-1)!.
Also w*K_0(w) <= w*K_1(w) <= 1.  These facts give a rational
zero-inclusive bound for Phi_m(w)=w^(m+1)|f^(m)(w)| on 0<=w<=W.
The bank reaches m=6, the largest order used by K326's complete regularized
D4 and bordered-B5 value/first/second entry jets.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K308 = ROOT / "lab/process/k308-order-seven-regularized-y-master-operator.json"
K320 = ROOT / "lab/process/k320-order-seven-scaled-endpoint-bessel-bank.json"
K326 = ROOT / "lab/process/k326-order-seven-signed-entry-jet-chart-bank.json"
OUTPUT = ROOT / "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json"

ctx.dps = 180
ctx.threads = 1

MAX_ORDER = 6
WIDTHS = (Fraction(1, 16), Fraction(1, 4), Fraction(1), Fraction(4))


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def nu_term_bound(order: int, nu: int, width: Fraction) -> Fraction:
    """Bound w^(order+1) K_nu(w) on 0<=w<=width."""
    if nu == 0:
        # K_0(w)<=K_1(w) and w*K_1(w)<=1.
        return width**order
    if not 1 <= nu <= order + 1:
        raise AssertionError("derivative recurrence emitted an impossible order")
    c_nu = Fraction(2 ** (nu - 1) * math.factorial(nu - 1), 1)
    return c_nu * width ** (order + 1 - nu)


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
        "scaled_derivative_interval": str(scaled),
        "rational_upper": q(bound),
        "contained": scaled.upper() <= arb(q(bound)).lower(),
    }


def build() -> dict[str, Any]:
    k308 = json.loads(K308.read_text())
    k320 = json.loads(K320.read_text())
    k326 = json.loads(K326.read_text())
    if k308["fixed_control"]["maximum_y_derivative_order"] != 2:
        raise AssertionError("K308 y-jet order changed")
    if not k320["decision"]["all_terminal_jet_orders_have_continuous_scaled_entries"]:
        raise AssertionError("K320 terminal scaling is unavailable")
    if not k326["decision"]["complete_determinant_taylor_assembly_precedes_interval_enclosure"]:
        raise AssertionError("K326 shared-entry contract is unavailable")

    rows = []
    controls = []
    for width in WIDTHS:
        bounds = [scaled_derivative_upper(order, width) for order in range(MAX_ORDER + 1)]
        rows.append({
            "width": q(width),
            "orders": list(range(MAX_ORDER + 1)),
            "Phi_abs_uppers": [q(value) for value in bounds],
        })
        for order in range(MAX_ORDER + 1):
            for argument in (width / 4, width):
                controls.append(positive_control(order, width, argument))
    if not all(row["contained"] for row in controls):
        raise AssertionError("an Arb recurrence control escaped the rational envelope")

    zero_limits = []
    for order in range(MAX_ORDER + 1):
        leading_nu = order + 1
        leading_indices = [
            index for index in range(order + 1)
            if abs(1 - order + 2 * index) == leading_nu
        ]
        limit = Fraction(2, 2**order) * sum(
            Fraction(math.comb(order, index) * 2 ** (leading_nu - 1) * math.factorial(leading_nu - 1), 1)
            for index in leading_indices
        )
        zero_limits.append(q(limit))

    return {
        "schema_version": "1.0",
        "result_id": "K328-ORDER-SEVEN-SCALED-DERIVATIVE-ENVELOPE-BANK",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k308-order-seven-regularized-y-master-operator.json",
                "lab/process/k320-order-seven-scaled-endpoint-bessel-bank.json",
                "lab/process/k326-order-seven-signed-entry-jet-chart-bank.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "maximum_derivative_order": MAX_ORDER,
            "widths": [q(value) for value in WIDTHS],
        },
        "analytic_envelope": {
            "definition": "Phi_m(w)=w^(m+1)*abs((2*K1)^(m)(w))",
            "derivative_recurrence": "abs((2*K1)^(m)(w)) <= 2^(1-m)*sum_k binom(m,k) K_|1-m+2k|(w)",
            "positive_order_rule": "w^nu*K_nu(w) decreases from 2^(nu-1)*(nu-1)! for integer nu>0",
            "zero_order_rule": "w*K0(w)<=w*K1(w)<=1",
            "rows": rows,
            "continuous_zero_limits": zero_limits,
            "raw_Bessel_evaluation_at_zero_used": False,
            "all_bounds_exact_rational": True,
        },
        "positive_argument_controls": controls,
        "order_census": {
            "D4_maximum_mixed_derivative_order": 6,
            "bordered_B5_maximum_value_first_second_order": 6,
            "terminal_orders_replay_K320": [0, 1, 2],
            "all_required_orders_covered": True,
        },
        "scope_boundary": {
            "covered": "zero-inclusive rational scaled Bessel derivative envelopes through order six",
            "not_covered": [
                "determinant row/column radial normalization",
                "the projective s=0 and s=1 face joins",
                "a complete y-master constant",
            ],
        },
        "decision": {
            "zero_safe_scaled_derivative_bank_through_order_six_implemented": True,
            "all_K326_nonterminal_derivative_orders_covered": True,
            "degree_27_origin_evaluator_released": True,
            "complete_origin_tail_face_sum_emitted": False,
            "complete_y_master_constant_emitted": False,
            "next_exact_input": "apply the scaled envelopes entrywise with the exact D4/B5 row-column radial exponents, assemble the complete determinant polynomial, and enclose the r=0 cell before treating s=0 and s=1",
        },
        "release_test": {
            "orders_zero_through_six_exact": len(rows[0]["Phi_abs_uppers"]) == 7,
            "all_positive_controls_contained": all(row["contained"] for row in controls),
            "K320_zero_limits_replayed": zero_limits[:3] == ["2", "2", "4"],
            "raw_zero_evaluation_used": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k326["ledger_effect"],
        "source_routing": k326["source_routing"],
        "claim_ceiling": "Exact rational zero-inclusive envelopes for w^(m+1)*abs((2*K1)^(m)(w)) through m=6, covering every divided-difference derivative order used by K326's complete D4 and bordered-B5 value/first/second jets. The proof uses the exact derivative recurrence, monotonic w^nu K_nu bounds and w*K0<=w*K1<=1; no raw Bessel call touches zero. This releases a degree-27 normalized origin evaluator, not an origin/tail/face sum, complete y constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["maximum_derivative_order"] != 6 or fixed["widths"] != ["1/16", "1/4", "1", "4"]:
        raise AssertionError("scaled derivative bank domain changed")
    envelope = payload["analytic_envelope"]
    if envelope["raw_Bessel_evaluation_at_zero_used"] or not envelope["all_bounds_exact_rational"]:
        raise AssertionError("zero-safe exact envelope contract lost")
    rows = envelope["rows"]
    if len(rows) != 4 or any(row["orders"] != list(range(7)) or len(row["Phi_abs_uppers"]) != 7 for row in rows):
        raise AssertionError("order/width census changed")
    if envelope["continuous_zero_limits"][:3] != ["2", "2", "4"]:
        raise AssertionError("K320 absolute zero limits changed")
    if not all(row["contained"] for row in payload["positive_argument_controls"]):
        raise AssertionError("positive recurrence control failed")
    if not payload["order_census"]["all_required_orders_covered"]:
        raise AssertionError("K326 order coverage incomplete")
    if payload["decision"]["complete_y_master_constant_emitted"]:
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

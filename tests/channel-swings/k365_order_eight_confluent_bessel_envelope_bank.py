#!/usr/bin/env python3
"""Extend K349 zero-safe scaled Bessel envelopes through confluent order eight."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K349 = ROOT / "lab/process/k349-order-eight-zero-safe-radial-contract.json"
K352 = ROOT / "lab/process/k352-order-eight-mask-native-preconditioner-compiler.json"
K364 = ROOT / "lab/process/k364-order-eight-nested-face-dual-obstruction.json"
OUTPUT = ROOT / "lab/process/k365-order-eight-confluent-bessel-envelope-bank.json"

ctx.dps = 180
ctx.threads = 1

MAX_ORDER = 8
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


def zero_limit(order: int) -> Fraction:
    return Fraction(2 * math.factorial(order), 1)


def build() -> dict[str, Any]:
    k349 = json.loads(K349.read_text())
    k352 = json.loads(K352.read_text())
    k364 = json.loads(K364.read_text())
    demand = k364["confluent_derivative_demand"]
    if demand["maximum_kernel_derivative_order_required"] != MAX_ORDER:
        raise AssertionError("K364 derivative demand changed")

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
        raise AssertionError("scaled derivative control escaped")

    limits = [q(zero_limit(order)) for order in range(MAX_ORDER + 1)]
    predecessor_rows = k349["scaled_bessel_bank"]["rows"]
    predecessor_replayed = all(
        row["Phi_abs_uppers"][:3] == predecessor["Phi_abs_uppers"]
        for row, predecessor in zip(rows, predecessor_rows, strict=True)
    )
    return {
        "schema_version": "1.0",
        "result_id": "K365-ORDER-EIGHT-CONFLUENT-BESSEL-ENVELOPE-BANK",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K349, K352, K364)],
            "maximum_derivative_order": MAX_ORDER,
            "widths": [q(value) for value in WIDTHS],
            "exact_rational_bounds": len(WIDTHS) * (MAX_ORDER + 1),
            "positive_Arb_controls": len(controls),
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "scaled_bessel_bank": {
            "definition": "Phi_m(w)=w^(m+1)*abs((2*K1)^(m)(w))",
            "derivative_recurrence": "abs((2*K1)^(m)(w)) <= 2^(1-m)*sum_k binom(m,k) K_|1-m+2k|(w)",
            "positive_order_rule": "w^nu*K_nu(w) decreases from 2^(nu-1)*(nu-1)! for integer nu>0",
            "zero_order_rule": "w*K0(w)<=w*K1(w)<=1",
            "rows": rows,
            "continuous_zero_limits": limits,
            "zero_limit_formula": "lim_(w->0+) Phi_m(w)=2*m!",
            "raw_Bessel_evaluation_at_zero_used": False,
            "all_bounds_exact_rational": True,
            "scope": "compact cumulative-argument widths through four; analytic unbounded tails remain separate",
        },
        "positive_controls": controls,
        "demand_reconciliation": {
            "maximum_row_divided_difference_order": demand["maximum_row_divided_difference_order"],
            "maximum_column_divided_difference_order": demand["maximum_column_divided_difference_order"],
            "active_peano_derivative_order": demand["active_peano_derivative_order"],
            "maximum_total_order": demand["maximum_kernel_derivative_order_required"],
            "all_required_orders_present": demand["required_orders"] == list(range(MAX_ORDER + 1)),
            "K349_orders_zero_through_two_replayed_exactly": predecessor_replayed,
        },
        "decision": {
            "zero_safe_confluent_scaled_derivative_bank_complete_through_order_eight": True,
            "K364_derivative_dependency_closed": True,
            "uniform_integrand_weighted_boundary_majorant_complete": False,
            "analytic_unbounded_tail_complete": False,
            "next_exact_input": "combine this bank with K366's multiscale determinant Newton fronts in a zero-inclusive closed-strip evaluator",
        },
        "release_test": {
            "orders_zero_through_eight_present": all(row["orders"] == list(range(9)) for row in rows),
            "exactly_36_rational_bounds": len(rows) * 9 == 36,
            "exactly_72_positive_controls": len(controls) == 72,
            "all_positive_controls_contained": all(row["contained"] for row in controls),
            "zero_limits_equal_2_times_factorial": limits == [q(2 * math.factorial(order)) for order in range(9)],
            "K349_orders_zero_through_two_replayed": predecessor_replayed,
            "raw_zero_evaluation_not_used": True,
            "uniform_strip_bound_not_overclaimed": True,
            "analytic_tail_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k364["ledger_effect"],
        "source_routing": k364["source_routing"],
        "claim_ceiling": "Exact rational zero-inclusive scaled envelopes for (2*K1) derivatives through order eight at cumulative-argument widths 1/64, 1/16, 1 and 4, with continuous limits 2*m! and 72 positive 180-digit Arb controls. This exactly covers K364's maximum row-three plus column-three confluent divided-difference order and the active second derivative while replaying K349 orders zero through two. It is a compact-width primitive bank, not a determinant-level uniform strip majorant, analytic unbounded tail, recursive cover, complete K348 hybrid, order-eight remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["maximum_derivative_order"], fixed["exact_rational_bounds"], fixed["positive_Arb_controls"]) != (8, 36, 72):
        raise AssertionError("K365 fixed census changed")
    bank = payload["scaled_bessel_bank"]
    if bank["raw_Bessel_evaluation_at_zero_used"] or not bank["all_bounds_exact_rational"] or bank["continuous_zero_limits"] != [q(2 * math.factorial(order)) for order in range(9)]:
        raise AssertionError("K365 zero-safe bank changed")
    demand = payload["demand_reconciliation"]
    if (demand["maximum_row_divided_difference_order"], demand["maximum_column_divided_difference_order"], demand["active_peano_derivative_order"], demand["maximum_total_order"]) != (3, 3, 2, 8):
        raise AssertionError("K365 derivative demand changed")
    if not demand["K349_orders_zero_through_two_replayed_exactly"] or not all(row["contained"] for row in payload["positive_controls"]):
        raise AssertionError("K365 predecessor or positive control failed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K365 release test failed")
    if payload["decision"]["uniform_integrand_weighted_boundary_majorant_complete"] or payload["decision"]["analytic_unbounded_tail_complete"]:
        raise AssertionError("K365 overclaimed numerical closure")


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

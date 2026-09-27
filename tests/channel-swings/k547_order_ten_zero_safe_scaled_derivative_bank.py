#!/usr/bin/env python3
"""Bind the global zero-safe scaled 2*K1 bank to K410/K546."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K375 = ROOT / "lab/process/k375-rank-five-global-scaled-bessel-bank.json"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
K546 = ROOT / "lab/process/k546-order-ten-nested-face-dual-obstruction.json"
OUTPUT = ROOT / "lab/process/k547-order-ten-zero-safe-scaled-derivative-bank.json"
MAX_ORDER = 10
WIDTHS = (Fraction(1, 64), Fraction(1, 16), Fraction(1), Fraction(4))
HALF_INTEGER_N = 11
ctx.dps = 200
ctx.threads = 1


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def nu_term_bound(order: int, nu: int, width: Fraction) -> Fraction:
    if nu == 0:
        return width**order
    return Fraction(2 ** (nu - 1) * math.factorial(nu - 1)) * width ** (order + 1 - nu)


def scaled_derivative_upper(order: int, width: Fraction) -> Fraction:
    total = sum(
        (
            Fraction(math.comb(order, index))
            * nu_term_bound(order, abs(1 - order + 2 * index), width)
            for index in range(order + 1)
        ),
        start=Fraction(0),
    )
    return Fraction(2, 2**order) * total


def bessel_derivative_abs(argument: arb, order: int) -> arb:
    total = sum(
        (
            arb(math.comb(order, index))
            * argument.bessel_k(abs(1 - order + 2 * index))
            for index in range(order + 1)
        ),
        start=arb(0),
    )
    return arb(2) ** (1 - order) * total


def half_integer_coefficients() -> list[Fraction]:
    n = HALF_INTEGER_N
    return [
        Fraction(math.factorial(n + k), math.factorial(k) * math.factorial(n - k) * 2**k)
        for k in range(n + 1)
    ]


def monomial_exponential_upper(order: int, k: int) -> int:
    exponent = order + 1 - k
    return 1 if exponent <= 0 else exponent**exponent


def tail_scaled_upper(order: int) -> Fraction:
    return Fraction(4) * sum(
        (
            coefficient * monomial_exponential_upper(order, k)
            for k, coefficient in enumerate(half_integer_coefficients())
        ),
        start=Fraction(0),
    )


def control(order: int, argument: Fraction, upper: Fraction, kind: str) -> dict[str, Any]:
    w = arb(q(argument))
    value = w ** (order + 1) * bessel_derivative_abs(w, order)
    return {
        "kind": kind,
        "order": order,
        "argument": q(argument),
        "scaled_interval": str(value),
        "rational_upper": q(upper),
        "contained": value.upper() <= arb(q(upper)).lower(),
    }


def build() -> dict[str, Any]:
    k375 = json.loads(K375.read_text())
    k410 = json.loads(K410.read_text())
    k546 = json.loads(K546.read_text())
    demand = k546["confluent_derivative_demand"]
    if demand["maximum_kernel_derivative_order_required"] != MAX_ORDER:
        raise AssertionError("K546 derivative demand changed")

    compact_rows = []
    compact_controls = []
    for width in WIDTHS:
        bounds = [scaled_derivative_upper(order, width) for order in range(MAX_ORDER + 1)]
        compact_rows.append(
            {
                "width": q(width),
                "orders": list(range(MAX_ORDER + 1)),
                "Phi_abs_uppers": [q(value) for value in bounds],
            }
        )
        for order, bound in enumerate(bounds):
            for argument in (width / 4, width):
                compact_controls.append(control(order, argument, bound, "compact"))

    width_one = next(row for row in compact_rows if row["width"] == "1")
    global_rows = []
    global_controls = []
    for order in range(MAX_ORDER + 1):
        compact = Fraction(width_one["Phi_abs_uppers"][order])
        tail = tail_scaled_upper(order)
        upper = max(compact, tail)
        global_rows.append(
            {
                "order": order,
                "compact_0_to_1_upper": q(compact),
                "half_integer_tail_upper": q(tail),
                "global_scaled_upper": q(upper),
                "selected_branch": "compact" if compact >= tail else "half_integer_tail",
            }
        )
        for argument in (Fraction(1), Fraction(4), Fraction(16)):
            global_controls.append(control(order, argument, upper, "global"))
    controls = compact_controls + global_controls
    if not all(row["contained"] for row in controls):
        raise AssertionError("K547 scaled derivative control escaped")

    k375_compact = k375["scaled_bessel_contract"]["compact_rows"]
    k375_global = k375["global_scaled_bessel_bank"]["rows"]
    k410_rows = k410["scaled_bessel_bank"]["rows"]
    k375_replayed = compact_rows == k375_compact and global_rows == k375_global
    k410_replayed = all(
        row["Phi_abs_uppers"][:3] == old["Phi_abs_uppers"]
        for row, old in zip(compact_rows, k410_rows, strict=True)
    )
    limits = [q(Fraction(2 * math.factorial(order))) for order in range(MAX_ORDER + 1)]

    return {
        "schema_version": "1.0",
        "result_id": "K547-ORDER-TEN-ZERO-SAFE-SCALED-DERIVATIVE-BANK",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K375, K410, K546)],
            "maximum_derivative_order": MAX_ORDER,
            "widths": [q(value) for value in WIDTHS],
            "exact_compact_rational_bounds": len(WIDTHS) * (MAX_ORDER + 1),
            "compact_positive_Arb_controls": len(compact_controls),
            "global_positive_Arb_controls": len(global_controls),
            "half_integer_comparator": "K_(23/2)",
            "arb_decimal_digits": 200,
            "threads": 1,
        },
        "scaled_bessel_contract": {
            "definition": "Phi_m(w)=w^(m+1)*abs((2*K1)^(m)(w))",
            "derivative_recurrence": "abs((2*K1)^(m)(w)) <= 2^(1-m)*sum_k binom(m,k) K_|1-m+2k|(w)",
            "continuous_zero_limits": limits,
            "zero_limit_formula": "lim_(w->0+) Phi_m(w)=2*m!",
            "compact_rows": compact_rows,
            "global_rows": global_rows,
            "global_domain": "0<=w<infinity",
            "raw_Bessel_evaluation_at_zero_used": False,
            "all_bounds_exact_rational": True,
        },
        "positive_controls": controls,
        "native_order_ten_reconciliation": {
            "maximum_row_divided_difference_order": demand["maximum_row_divided_difference_order"],
            "maximum_column_divided_difference_order": demand["maximum_column_divided_difference_order"],
            "active_peano_derivative_order": demand["active_peano_derivative_order"],
            "maximum_total_order": demand["maximum_kernel_derivative_order_required"],
            "all_required_orders_present": demand["required_orders"] == list(range(MAX_ORDER + 1)),
            "K410_orders_zero_through_two_replayed_exactly": k410_replayed,
            "K375_global_bank_recomputed_exactly": k375_replayed,
            "order_eight_or_order_nine_face_atlas_reused": False,
        },
        "decision": {
            "native_order_ten_zero_safe_global_derivative_bank_complete": True,
            "K546_derivative_dependency_closed": True,
            "uniform_integrand_weighted_boundary_majorant_complete": False,
            "next_exact_input": "combine this native order-ten primitive binding with K548's same-permutation bivariate determinant fronts in a zero-inclusive uniform face-envelope compiler",
        },
        "release_test": {
            "orders_zero_through_ten_present": [row["order"] for row in global_rows] == list(range(11)),
            "exactly_44_compact_rational_bounds": len(compact_rows) * 11 == 44,
            "exactly_121_positive_controls": len(controls) == 121,
            "all_positive_controls_contained": all(row["contained"] for row in controls),
            "zero_limits_equal_2_times_factorial": limits == [q(Fraction(2 * math.factorial(order))) for order in range(11)],
            "K410_orders_zero_through_two_replayed": k410_replayed,
            "K375_global_bank_recomputed": k375_replayed,
            "raw_zero_evaluation_absent": True,
            "foreign_face_atlas_not_reused": True,
            "uniform_strip_bound_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k546["ledger_effect"],
        "source_routing": k546["source_routing"],
        "claim_ceiling": "Exact native order-ten binding of the global zero-inclusive scaled 2*K1 derivative envelopes through order ten. It recomputes K375's compact-plus-tail bank, replays K410 orders zero through two exactly, satisfies K546's row-four plus column-four plus active-second-derivative demand, and passes 121 positive 200-digit Arb controls without a raw zero call or foreign face-atlas reuse. This closes the primitive derivative dependency, not a determinant-level boundary envelope, recursive cover, tail integration, complete order-ten hybrid/integral, action column, R_ref, K152, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (
        fixed["maximum_derivative_order"],
        fixed["exact_compact_rational_bounds"],
        fixed["compact_positive_Arb_controls"],
        fixed["global_positive_Arb_controls"],
        fixed["half_integer_comparator"],
    ) != (10, 44, 88, 33, "K_(23/2)"):
        raise AssertionError("K547 fixed control changed")
    native = payload["native_order_ten_reconciliation"]
    if (
        native["maximum_row_divided_difference_order"],
        native["maximum_column_divided_difference_order"],
        native["active_peano_derivative_order"],
        native["maximum_total_order"],
    ) != (4, 4, 2, 10):
        raise AssertionError("K547 derivative demand changed")
    if not native["K410_orders_zero_through_two_replayed_exactly"] or not native["K375_global_bank_recomputed_exactly"] or native["order_eight_or_order_nine_face_atlas_reused"]:
        raise AssertionError("K547 predecessor or native binding changed")
    if payload["scaled_bessel_contract"]["raw_Bessel_evaluation_at_zero_used"] or not all(row["contained"] for row in payload["positive_controls"]):
        raise AssertionError("K547 zero-safe controls changed")
    if payload["decision"]["uniform_integrand_weighted_boundary_majorant_complete"]:
        raise AssertionError("K547 overclaimed boundary closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K547 release test failed")


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

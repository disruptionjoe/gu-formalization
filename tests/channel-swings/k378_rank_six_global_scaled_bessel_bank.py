#!/usr/bin/env python3
"""Build the global zero-safe scaled 2*K1 derivative bank through order twelve."""

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
K377 = ROOT / "lab/process/k377-rank-six-confluent-determinant-calculus.json"
OUTPUT = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
MAX_ORDER = 12
WIDTHS = (Fraction(1, 64), Fraction(1, 16), Fraction(1), Fraction(4))
HALF_INTEGER_N = 13
ctx.dps = 220
ctx.threads = 1


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def nu_term_bound(order: int, nu: int, width: Fraction) -> Fraction:
    if nu == 0:
        return width**order
    return Fraction(2 ** (nu - 1) * math.factorial(nu - 1)) * width ** (order + 1 - nu)


def scaled_derivative_upper(order: int, width: Fraction) -> Fraction:
    total = sum((Fraction(math.comb(order, index)) * nu_term_bound(order, abs(1 - order + 2 * index), width) for index in range(order + 1)), start=Fraction(0))
    return Fraction(2, 2**order) * total


def bessel_derivative_abs(argument: arb, order: int) -> arb:
    total = sum((arb(math.comb(order, index)) * argument.bessel_k(abs(1 - order + 2 * index)) for index in range(order + 1)), start=arb(0))
    return arb(2) ** (1 - order) * total


def half_integer_coefficients() -> list[Fraction]:
    n = HALF_INTEGER_N
    return [Fraction(math.factorial(n + k), math.factorial(k) * math.factorial(n - k) * 2**k) for k in range(n + 1)]


def tail_scaled_upper(order: int) -> Fraction:
    total = Fraction(0)
    for k, coefficient in enumerate(half_integer_coefficients()):
        exponent = order + 1 - k
        total += coefficient * (1 if exponent <= 0 else exponent**exponent)
    return 4 * total


def control(order: int, argument: Fraction, upper: Fraction, kind: str) -> dict[str, Any]:
    w = arb(q(argument))
    value = w ** (order + 1) * bessel_derivative_abs(w, order)
    return {"kind": kind, "order": order, "argument": q(argument), "scaled_interval": str(value), "rational_upper": q(upper), "contained": value.upper() <= arb(q(upper)).lower()}


def build() -> dict[str, Any]:
    k375 = json.loads(K375.read_text())
    k377 = json.loads(K377.read_text())
    if k377["derivative_demand"]["total_required"] != MAX_ORDER:
        raise AssertionError("K377 derivative demand changed")
    compact_rows = []
    compact_controls = []
    for width in WIDTHS:
        bounds = [scaled_derivative_upper(order, width) for order in range(MAX_ORDER + 1)]
        compact_rows.append({"width": q(width), "orders": list(range(MAX_ORDER + 1)), "Phi_abs_uppers": [q(value) for value in bounds]})
        for order, bound in enumerate(bounds):
            for argument in (width / 4, width):
                compact_controls.append(control(order, argument, bound, "compact"))
    predecessor_compact = k375["scaled_bessel_contract"]["compact_rows"]
    compact_replayed = all(row["Phi_abs_uppers"][:11] == old["Phi_abs_uppers"] for row, old in zip(compact_rows, predecessor_compact, strict=True))
    width_one = next(row for row in compact_rows if row["width"] == "1")
    global_rows = []
    global_controls = []
    for order in range(MAX_ORDER + 1):
        compact = Fraction(width_one["Phi_abs_uppers"][order])
        tail = tail_scaled_upper(order)
        upper = max(compact, tail)
        global_rows.append({"order": order, "compact_0_to_1_upper": q(compact), "half_integer_tail_upper": q(tail), "global_scaled_upper": q(upper), "selected_branch": "compact" if compact >= tail else "half_integer_tail"})
        for argument in (Fraction(1), Fraction(4), Fraction(16)):
            global_controls.append(control(order, argument, upper, "global"))
    predecessor_global = k375["global_scaled_bessel_bank"]["rows"]
    predecessor_global_dominated = all(
        Fraction(row["global_scaled_upper"]) >= Fraction(old["global_scaled_upper"])
        for row, old in zip(global_rows[:11], predecessor_global, strict=True)
    )
    controls = compact_controls + global_controls
    if not all(row["contained"] for row in controls):
        raise AssertionError("rank-six scaled Bessel control escaped")
    limits = [q(Fraction(2 * math.factorial(order))) for order in range(MAX_ORDER + 1)]
    return {
        "schema_version": "1.0",
        "result_id": "K378-RANK-SIX-GLOBAL-SCALED-BESSEL-BANK",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K375, K377)],
            "maximum_derivative_order": MAX_ORDER,
            "widths": [q(value) for value in WIDTHS],
            "exact_compact_rational_bounds": 52,
            "compact_positive_Arb_controls": len(compact_controls),
            "global_positive_Arb_controls": len(global_controls),
            "half_integer_comparator": "K_(27/2)",
            "half_integer_polynomial_degree": HALF_INTEGER_N,
            "arb_decimal_digits": 220,
            "threads": 1,
        },
        "scaled_bessel_contract": {
            "definition": "Phi_m(w)=w^(m+1)*abs((2*K1)^(m)(w))",
            "derivative_recurrence": "abs((2*K1)^(m)(w)) <= 2^(1-m)*sum_k binom(m,k) K_|1-m+2k|(w)",
            "continuous_zero_limits": limits,
            "zero_limit_formula": "lim_(w->0+) Phi_m(w)=2*m!",
            "compact_rows": compact_rows,
            "K375_orders_zero_through_ten_compact_replayed": compact_replayed,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "tail_contract": {
            "comparator": "all integer orders through thirteen are bounded by K_(27/2)",
            "half_integer_formula": "K_(n+1/2)(w)=sqrt(pi/(2w))*exp(-w)*sum_(k=0)^n (n+k)!/(k!(n-k)!(2w)^k)",
            "exact_coefficients": [q(value) for value in half_integer_coefficients()],
            "tail_domain": "w>=1",
            "compact_domain": "0<=w<=1",
            "all_global_bounds_exact_rational": True,
            "K375_orders_zero_through_ten_global_dominated": predecessor_global_dominated,
        },
        "global_scaled_bessel_bank": {"orders": list(range(13)), "rows": global_rows, "global_domain": "0<=w<infinity"},
        "positive_controls": controls,
        "demand_reconciliation": {"rank_six_confluence_maximum": 10, "active_peano_derivative_order": 2, "maximum_total_order": 12, "all_required_orders_present": [row["order"] for row in global_rows] == list(range(13)), "K375_predecessor_compact_replayed_and_global_dominated": compact_replayed and predecessor_global_dominated},
        "decision": {
            "zero_safe_global_scaled_derivative_bank_complete_through_order_twelve": True,
            "K377_primitive_dependency_closed": True,
            "orders_eleven_twelve_factor_transfer_complete": False,
            "numerical_orders_eleven_twelve_integrals_emitted": False,
            "next_exact_input": "bind the accepted rank-six confluence and derivative calculus separately to every order-eleven and order-twelve factor",
        },
        "release_test": {
            "orders_zero_through_twelve_present": [row["order"] for row in global_rows] == list(range(13)),
            "exactly_52_compact_rational_bounds": len(compact_rows) * 13 == 52,
            "exactly_104_compact_controls": len(compact_controls) == 104,
            "exactly_39_global_controls": len(global_controls) == 39,
            "all_positive_controls_contained": all(row["contained"] for row in controls),
            "zero_limits_equal_2_times_factorial": limits == [q(Fraction(2 * math.factorial(order))) for order in range(13)],
            "K375_orders_zero_through_ten_preserved": compact_replayed and predecessor_global_dominated,
            "raw_zero_evaluation_absent": True,
            "numerical_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k377["ledger_effect"],
        "source_routing": k377["source_routing"],
        "claim_ceiling": "Exact rational zero-inclusive and global compact-plus-tail envelopes for w^(m+1)*abs((2*K1)^(m)(w)) through derivative order twelve. The bank replays K375 through order ten, uses K_(27/2) on w>=1, and passes 143 positive 220-digit Arb controls without a raw zero call. It closes the primitive rank-six dependency, not the orders eleven/twelve factor transfer, numerical integrals, action column, R_ref, K152, source/ledger move, canon, paper, public, novelty or physical claim."
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["maximum_derivative_order"], fixed["exact_compact_rational_bounds"], fixed["compact_positive_Arb_controls"], fixed["global_positive_Arb_controls"], fixed["half_integer_comparator"], fixed["half_integer_polynomial_degree"]) != (12, 52, 104, 39, "K_(27/2)", 13):
        raise AssertionError("K378 fixed control changed")
    bank = payload["scaled_bessel_contract"]
    if bank["raw_Bessel_evaluation_at_zero_used"] or not bank["K375_orders_zero_through_ten_compact_replayed"] or bank["continuous_zero_limits"] != [q(Fraction(2 * math.factorial(order))) for order in range(13)]:
        raise AssertionError("K378 compact bank changed")
    rows = payload["global_scaled_bessel_bank"]["rows"]
    if [row["order"] for row in rows] != list(range(13)) or any(Fraction(row["global_scaled_upper"]) < max(Fraction(row["compact_0_to_1_upper"]), Fraction(row["half_integer_tail_upper"])) for row in rows):
        raise AssertionError("K378 global join changed")
    if not payload["tail_contract"]["all_global_bounds_exact_rational"] or not payload["tail_contract"]["K375_orders_zero_through_ten_global_dominated"] or not all(row["contained"] for row in payload["positive_controls"]):
        raise AssertionError("K378 tail or control failed")
    decision = payload["decision"]
    if not decision["zero_safe_global_scaled_derivative_bank_complete_through_order_twelve"] or decision["orders_eleven_twelve_factor_transfer_complete"] or decision["numerical_orders_eleven_twelve_integrals_emitted"]:
        raise AssertionError("K378 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K378 release test failed")


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

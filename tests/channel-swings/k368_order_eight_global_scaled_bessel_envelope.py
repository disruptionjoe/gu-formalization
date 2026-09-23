#!/usr/bin/env python3
"""Join K365 compact bounds to a global half-integer Bessel tail comparator."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K365 = ROOT / "lab/process/k365-order-eight-confluent-bessel-envelope-bank.json"
OUTPUT = ROOT / "lab/process/k368-order-eight-global-scaled-bessel-envelope.json"
MAX_ORDER = 8
HALF_INTEGER_N = 9
ctx.dps = 180
ctx.threads = 1


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def half_integer_coefficients(n: int = HALF_INTEGER_N) -> list[Fraction]:
    return [
        Fraction(math.factorial(n + k), math.factorial(k) * math.factorial(n - k) * 2**k)
        for k in range(n + 1)
    ]


def monomial_exponential_upper(order: int, k: int) -> int:
    exponent_ceiling = order + 1 - k
    if exponent_ceiling <= 0:
        return 1
    return exponent_ceiling**exponent_ceiling


def tail_scaled_upper(order: int) -> Fraction:
    coefficients = half_integer_coefficients()
    return Fraction(4) * sum(
        coefficient * monomial_exponential_upper(order, k)
        for k, coefficient in enumerate(coefficients)
    )


def bessel_derivative_abs(argument: arb, order: int) -> arb:
    total = arb(0)
    for index in range(order + 1):
        nu = abs(1 - order + 2 * index)
        total += math.comb(order, index) * argument.bessel_k(nu)
    return arb(2) ** (1 - order) * total


def build() -> dict[str, Any]:
    k365 = json.loads(K365.read_text())
    compact = next(row for row in k365["scaled_bessel_bank"]["rows"] if row["width"] == "1")
    compact_bounds = [Fraction(value) for value in compact["Phi_abs_uppers"]]
    rows = []
    controls = []
    for order in range(MAX_ORDER + 1):
        tail = tail_scaled_upper(order)
        global_upper = max(compact_bounds[order], tail)
        rows.append({
            "order": order,
            "compact_0_to_1_upper": q(compact_bounds[order]),
            "half_integer_tail_upper": q(tail),
            "global_scaled_upper": q(global_upper),
            "selected_branch": "compact" if compact_bounds[order] >= tail else "half_integer_tail",
        })
        for argument in (Fraction(1), Fraction(4), Fraction(16)):
            w = arb(q(argument))
            scaled = w ** (order + 1) * bessel_derivative_abs(w, order)
            controls.append({
                "order": order,
                "argument": q(argument),
                "scaled_interval": str(scaled),
                "global_rational_upper": q(global_upper),
                "contained": scaled.upper() <= arb(q(global_upper)).lower(),
            })
    if not all(row["contained"] for row in controls):
        raise AssertionError("K368 positive control escaped global envelope")
    return {
        "schema_version": "1.0",
        "result_id": "K368-ORDER-EIGHT-GLOBAL-SCALED-BESSEL-ENVELOPE",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K365.relative_to(ROOT))],
            "maximum_derivative_order": MAX_ORDER,
            "compact_join_argument": "1",
            "half_integer_comparator": "K_(19/2)",
            "half_integer_polynomial_degree": HALF_INTEGER_N,
            "exact_half_integer_coefficients": [q(value) for value in half_integer_coefficients()],
            "positive_Arb_controls": len(controls),
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "tail_contract": {
            "derivative_recurrence": "abs((2*K1)^(m)(w)) <= 2^(1-m) sum_k binom(m,k) K_|1-m+2k|(w)",
            "order_monotonicity": "K_nu(w) is increasing in nu>=0 by its positive cosh(nu*t) integral representation",
            "comparator_step": "all integer orders through nine are no larger than K_(19/2), so every derivative recurrence is at most 2*K_(19/2)",
            "half_integer_formula": "K_(n+1/2)(w)=sqrt(pi/(2w))*exp(-w)*sum_(k=0)^n (n+k)!/(k!(n-k)!(2w)^k)",
            "rationalization": "sqrt(pi/2)<2 and w^(m+1/2-k) exp(-w) <= p^p for p=max(1,m+1-k) on w>=1",
            "tail_domain": "w>=1",
            "compact_domain": "0<=w<=1",
            "raw_Bessel_evaluation_at_zero_used": False,
            "all_global_bounds_exact_rational": True,
        },
        "global_scaled_bessel_bank": {
            "definition": "Phi_m(w)=w^(m+1)*abs((2*K1)^(m)(w))",
            "rows": rows,
            "global_domain": "0<=w<infinity",
            "orders": list(range(MAX_ORDER + 1)),
        },
        "positive_controls": controls,
        "decision": {
            "global_zero_safe_scaled_derivative_bank_complete_through_order_eight": True,
            "compact_and_tail_domains_joined": True,
            "determinant_level_whole_radial_face_majorants_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "recompute K367 determinant coefficients with these global primitive bounds and integrate the K353 face-normal powers under K348 weights",
        },
        "release_test": {
            "orders_zero_through_eight_present": [row["order"] for row in rows] == list(range(9)),
            "exactly_27_positive_controls": len(controls) == 27,
            "all_positive_controls_contained": all(row["contained"] for row in controls),
            "half_integer_comparator_is_19_over_2": HALF_INTEGER_N == 9,
            "all_tail_bounds_positive": all(Fraction(row["half_integer_tail_upper"]) > 0 for row in rows),
            "global_upper_dominates_both_branches": all(Fraction(row["global_scaled_upper"]) >= Fraction(row["compact_0_to_1_upper"]) and Fraction(row["global_scaled_upper"]) >= Fraction(row["half_integer_tail_upper"]) for row in rows),
            "raw_zero_evaluation_absent": True,
            "determinant_face_majorants_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k365["ledger_effect"],
        "source_routing": k365["source_routing"],
        "claim_ceiling": "Exact rational global envelopes for w^(m+1)*abs((2*K1)^(m)(w)) through derivative order eight. K365 controls 0<=w<=1; an explicit K_(19/2) half-integer comparator controls w>=1, and 27 positive 180-digit Arb checks are contained. This closes the primitive compact-plus-tail dependency, not a determinant-level whole-radial face majorant, recursively disjoint K363 owner cover, complete K348 hybrid, order-eight remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["maximum_derivative_order"], fixed["half_integer_comparator"], fixed["half_integer_polynomial_degree"], fixed["positive_Arb_controls"]) != (8, "K_(19/2)", 9, 27):
        raise AssertionError("K368 fixed control changed")
    rows = payload["global_scaled_bessel_bank"]["rows"]
    if [row["order"] for row in rows] != list(range(9)):
        raise AssertionError("K368 order bank changed")
    if any(Fraction(row["global_scaled_upper"]) < max(Fraction(row["compact_0_to_1_upper"]), Fraction(row["half_integer_tail_upper"])) for row in rows):
        raise AssertionError("K368 branch join changed")
    contract = payload["tail_contract"]
    if contract["raw_Bessel_evaluation_at_zero_used"] or not contract["all_global_bounds_exact_rational"]:
        raise AssertionError("K368 zero-safe exactness changed")
    if not all(row["contained"] for row in payload["positive_controls"]):
        raise AssertionError("K368 control containment changed")
    decision = payload["decision"]
    if not decision["global_zero_safe_scaled_derivative_bank_complete_through_order_eight"] or decision["determinant_level_whole_radial_face_majorants_complete"] or decision["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K368 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K368 release test failed")


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

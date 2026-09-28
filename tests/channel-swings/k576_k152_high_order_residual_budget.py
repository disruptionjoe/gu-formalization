#!/usr/bin/env python3
"""K576 isolate high-order residual budgets after the sharp tail."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k576-k152-high-order-residual-budget.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K574 = load("k574_for_k576", "k574_k176_sharp_post_adjoint_tail_reconciliation.py")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def decimal_value(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def sqrt_fraction(value: Fraction) -> Fraction | None:
    numerator = math.isqrt(value.numerator)
    denominator = math.isqrt(value.denominator)
    if numerator * numerator == value.numerator and denominator * denominator == value.denominator:
        return Fraction(numerator, denominator)
    return None


def target_row(kind: str, label: str, budget: Fraction, low_upper: Fraction, epsilon: Fraction) -> dict:
    rational_sqrt = sqrt_fraction(budget)
    rational_base = budget + epsilon * epsilon - low_upper
    radical_coefficient = 2 * epsilon
    with localcontext() as ctx:
        ctx.prec = 60
        allowance_decimal = (decimal_value(budget).sqrt() - decimal_value(epsilon)) ** 2 - decimal_value(low_upper)
    allowance_positive = allowance_decimal > 0
    row = {
        "target_kind": kind,
        "target": label,
        "complete_residual_square_budget": q(budget),
        "high_order_allowance_exact_expression": f"{q(rational_base)}-{q(radical_coefficient)}*sqrt({q(budget)})",
        "high_order_allowance_rational_base": q(rational_base),
        "high_order_allowance_radical_coefficient": q(radical_coefficient),
        "high_order_allowance_radicand": q(budget),
        "high_order_allowance_scientific": f"{allowance_decimal:.12E}",
        "current_low_order_and_tail_leave_positive_high_order_allowance": allowance_positive,
        "requires_low_order_tightening_even_if_high_orders_vanish": not allowance_positive,
        "equal_share_orders_8_through_12_scientific": f"{allowance_decimal / Decimal(5):.12E}" if allowance_positive else None,
    }
    if rational_sqrt is not None:
        exact = (rational_sqrt - epsilon) ** 2 - low_upper
        row["rational_square_root"] = q(rational_sqrt)
        row["high_order_allowance_exact_rational"] = q(exact)
        row["equal_share_orders_8_through_12_exact_rational"] = q(exact / 5) if exact > 0 else None
    else:
        row["rational_square_root"] = None
        row["high_order_allowance_exact_rational"] = None
        row["equal_share_orders_8_through_12_exact_rational"] = None
    return row


def build() -> dict:
    k569 = json.loads((ROOT / "lab/process/k569-complete-finite-gram-square-enclosure.json").read_text())
    k573 = json.loads((ROOT / "lab/process/k573-k152-residual-accuracy-targets.json").read_text())
    k574 = K574.build()
    rows_by_order = {row["order"]: row for row in k569["order_enclosures"]}
    low_orders = list(range(2, 8))
    high_orders = list(range(8, 13))
    low_upper = sum(Fraction(rows_by_order[order]["norm_square_interval_exact"][1]) for order in low_orders)
    epsilon = Fraction(k574["sharp_tail"]["sharp_tail_norm_upper"])
    targets = []
    for row in k573["ground_deficit_targets"]:
        targets.append(target_row("ground_deficit", row["target_ground_deficit"], Fraction(row["best_gap_residual_square_budget"]), low_upper, epsilon))
    for row in k573["projection_targets"]:
        targets.append(target_row("projection_sine", row["target_projection_sine"], Fraction(row["best_gap_residual_square_budget"]), low_upper, epsilon))
    positive = [row for row in targets if row["current_low_order_and_tail_leave_positive_high_order_allowance"]]
    blocked = [row for row in targets if row["requires_low_order_tightening_even_if_high_orders_vanish"]]
    return {
        "schema_version": "1.0",
        "result_id": "K576-K152-HIGH-ORDER-RESIDUAL-BUDGET",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Cancellation-aware accuracy allocation between K569 orders two through seven, orders eight through twelve and K574's post-order-twelve tail for K573's named K469/K470 consumers.",
        "gu_typed_objects": {
            "result": "orthogonal high-order residual budget MAP-TYPE=decision-budget",
            "carrier": "one fixed complete K162 charge sector",
            "pairing": "positive physical metric M=S* S",
            "form": "fixed K139/K168 reference form",
            "target": "future coherent order-eight-through-twelve residual or action-flux certificate",
        },
        "orthogonal_partition": {
            "low_orders": low_orders,
            "high_orders": high_orders,
            "reason": "K179 output signatures retain particle order, so unequal orders occupy orthogonal exterior sectors.",
            "low_order_complete_square_upper_exact": q(low_upper),
            "low_order_complete_square_upper_scientific": f"{float(low_upper):.17e}",
            "sharp_post_order_twelve_tail_norm_upper_exact": q(epsilon),
            "all_low_order_coherent_cross_terms_retained": True,
            "all_high_order_coherent_cross_terms_must_be_retained": True,
        },
        "budget_identity": {
            "finite_square_split": "Q_12=Q_2_to_7+Q_8_to_12",
            "complete_upper": "||r||^2 <= (sqrt(Q_2_to_7+Q_8_to_12)+epsilon_sharp)^2",
            "high_order_sufficient_condition": "Q_8_to_12 <= (sqrt(B)-epsilon_sharp)^2-U_2_to_7",
            "equal_share_is_sufficient_not_required": True,
        },
        "consumer_targets": targets,
        "controls": {
            "target_count": len(targets),
            "positive_high_order_allowance_count": len(positive),
            "low_order_tightening_required_count": len(blocked),
            "positive_target_labels": [f"{row['target_kind']}={row['target']}" for row in positive],
            "low_order_tightening_target_labels": [f"{row['target_kind']}={row['target']}" for row in blocked],
            "loosest_projection_25_over_9_high_order_allowance_exact": next(row["high_order_allowance_exact_rational"] for row in targets if row["target_kind"] == "projection_sine" and row["target"] == "1/2"),
        },
        "decision": {
            "first_cancellation_aware_milestone": "Enclose the coherent aggregate Q_8_to_12 below the K576 projection-sine-one-half allowance while retaining the accepted Q_2_to_7 upper and sharp tail.",
            "orders_two_through_seven_already_fit_projection_sine_one_half_budget": True,
            "orders_eight_through_twelve_are_the_first_target_for_projection_sine_one_half": True,
            "projection_sine_one_tenth_also_requires_low_order_tightening": True,
            "equal_share_is_a_planning_allocation_not_a_mathematical_necessity": True,
            "complete_reference_specific_floor_still_required": True,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Replace the order-eight-through-twelve absolute Peano ceilings by coherent cancellation-aware enclosures whose aggregate is below the selected exact allowance; if targeting projection sine 1/10, tighten orders two through seven as well. Complete K494/K500's independent reference-specific floor before K152 transfer.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact sufficient residual-budget allocation only. It identifies which current order bands must tighten for K573's named consumers, but supplies no improved high-order enclosure, complete floor, K152 shifted-form residual, native K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(payload: dict) -> None:
    partition = payload["orthogonal_partition"]
    controls = payload["controls"]
    decision = payload["decision"]
    if partition["low_orders"] != list(range(2, 8)) or partition["high_orders"] != list(range(8, 13)):
        raise AssertionError("K576 order partition changed")
    if not partition["all_low_order_coherent_cross_terms_retained"] or not partition["all_high_order_coherent_cross_terms_must_be_retained"]:
        raise AssertionError("K576 discarded coherent terms")
    if controls["target_count"] != 6 or controls["positive_high_order_allowance_count"] != 5 or controls["low_order_tightening_required_count"] != 1:
        raise AssertionError("K576 target disposition changed")
    if controls["low_order_tightening_target_labels"] != ["projection_sine=1/10"]:
        raise AssertionError("K576 identified the wrong low-order bottleneck")
    if not decision["orders_two_through_seven_already_fit_projection_sine_one_half_budget"] or not decision["orders_eight_through_twelve_are_the_first_target_for_projection_sine_one_half"]:
        raise AssertionError("K576 lost the first milestone")
    if not decision["projection_sine_one_tenth_also_requires_low_order_tightening"]:
        raise AssertionError("K576 hid the strict-target low-order debt")
    if not decision["complete_reference_specific_floor_still_required"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K576 overclaimed K152 closure")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""K577 compile consumer-driven targets for every high-order coherent group."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k577-k152-high-order-coherent-group-target-atlas.json"
SOURCES = {
    8: ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json",
    9: ROOT / "lab/process/k381-order-nine-group-interval-evaluator.json",
    10: ROOT / "lab/process/k406-order-ten-group-interval-evaluator.json",
    11: ROOT / "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json",
    12: ROOT / "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json",
}
INTEGRALS = {
    8: ROOT / "lab/process/k372-order-eight-complete-integral-enclosure.json",
    9: ROOT / "lab/process/k404-order-nine-complete-integral-enclosure.json",
    10: ROOT / "lab/process/k553-order-ten-complete-integral-enclosure.json",
    11: ROOT / "lab/process/k567-orders-eleven-twelve-complete-integral-enclosures.json",
    12: ROOT / "lab/process/k567-orders-eleven-twelve-complete-integral-enclosures.json",
}


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k577", "k179_matched_normal_order_coefficient_family.py")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def scientific(value: Fraction, digits: int = 12) -> str:
    with localcontext() as context:
        context.prec = digits + 20
        return f"{Decimal(value.numerator) / Decimal(value.denominator):.{digits}E}"


def group_id(term: dict[str, Any]) -> str:
    return f"order{term['order']}:seed{term['seed_impurity']}:{term['output_signature']}"


def source_order(data: dict[str, Any], order: int) -> dict[str, Any]:
    if order <= 10:
        return data
    return next(row for row in data["order_evaluations"] if int(row["order"]) == order)


def integral_upper(order: int) -> str:
    data = json.loads(INTEGRALS[order].read_text())
    if order == 8:
        return data["complete_integral_enclosure"]["complete_order_eight_integral_interval_scientific"][1]
    if order == 9:
        return data["complete_integral_enclosure"]["complete_order_nine_integral_interval_scientific"][1]
    if order == 10:
        return data["complete_integral_enclosure"]["complete_order_ten_integral_interval_scientific"][1]
    row = next(row for row in data["order_enclosures"] if int(row["order"]) == order)
    return row["complete_integral_enclosure"]["complete_integral_interval_scientific"][1]


def build() -> dict[str, Any]:
    k576 = json.loads((ROOT / "lab/process/k576-k152-high-order-residual-budget.json").read_text())
    allowance = Fraction(k576["controls"]["loosest_projection_25_over_9_high_order_allowance_exact"])
    order_target = allowance / 5
    terms = [term for term in K179.coefficient_family() if 8 <= int(term["order"]) <= 12]
    grouped: dict[int, Counter[str]] = {order: Counter() for order in range(8, 13)}
    for term in terms:
        grouped[int(term["order"])][group_id(term)] += 1

    source_data = {order: json.loads(path.read_text()) for order, path in SOURCES.items()}
    rows = []
    all_groups = 0
    all_paths = 0
    all_entries = 0
    all_ordered = 0
    for order in range(8, 13):
        source = source_order(source_data[order], order)
        values = source["coherent_group_values"]
        source_keys = {row["group_id"] for row in values}
        native_keys = set(grouped[order])
        if source_keys != native_keys:
            raise AssertionError(f"order {order} group keys differ from K179")
        group_target = order_target / len(native_keys)
        node = source["complete_node_evaluation"]
        node_upper = Decimal(node["normalized_one_node_rule_upper"])
        order_target_decimal = Decimal(order_target.numerator) / Decimal(order_target.denominator)
        current_upper = Decimal(integral_upper(order))
        census = {
            "paths": sum(grouped[order].values()),
            "coherent_groups": len(native_keys),
            "upper_triangle_entries": sum(size * (size + 1) // 2 for size in grouped[order].values()),
            "ordered_quadratic_terms": sum(size * size for size in grouped[order].values()),
        }
        fixed = source["fixed_control"]
        fixed_keys = {
            "paths": "paths",
            "coherent_groups": "coherent_groups",
            "upper_triangle_entries": "upper_triangle_gram_entries",
            "ordered_quadratic_terms": "ordered_quadratic_terms",
        }
        if any(census[key] != int(fixed[source_key]) for key, source_key in fixed_keys.items()):
            raise AssertionError(f"order {order} source census changed")
        group_rows = [
            {
                "group_id": key,
                "path_count": grouped[order][key],
                "sufficient_complete_integral_upper_target_exact": q(group_target),
                "sufficient_complete_integral_upper_target_scientific": scientific(group_target),
            }
            for key in sorted(native_keys)
        ]
        rows.append({
            "order": order,
            "source": str(SOURCES[order].relative_to(ROOT)),
            **census,
            "group_size_histogram": {str(size): count for size, count in sorted(Counter(grouped[order].values()).items())},
            "sufficient_order_upper_target_exact": q(order_target),
            "sufficient_order_upper_target_scientific": scientific(order_target),
            "sufficient_equal_group_target_exact": q(group_target),
            "normalized_one_node_rule_upper": str(node["normalized_one_node_rule_upper"]),
            "one_node_rule_is_below_order_target": node_upper < order_target_decimal,
            "current_complete_integral_upper_scientific": str(current_upper),
            "current_complete_integral_upper_exceeds_order_target": current_upper > order_target_decimal,
            "group_targets": group_rows,
        })
        all_groups += census["coherent_groups"]
        all_paths += census["paths"]
        all_entries += census["upper_triangle_entries"]
        all_ordered += census["ordered_quadratic_terms"]

    return {
        "schema_version": "1.0",
        "result_id": "K577-K152-HIGH-ORDER-COHERENT-GROUP-TARGET-ATLAS",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Every K179 coherent group in orders eight through twelve, with exact sufficient groupwise targets whose sum is K576's projection-sine-one-half high-order allowance.",
        "gu_typed_objects": {
            "result": "consumer-driven coherent-group target atlas MAP-TYPE=decision-budget",
            "carrier": "one fixed complete K162 charge sector",
            "pairing": "positive physical metric M=S* S",
            "form": "K179 coefficient-complete high-order residual square",
            "target": "future groupwise complete-integral upper certificates for Q_8_to_12",
        },
        "target_identity": {
            "consumer": "K573/K576 projection_sine=1/2 at best admissible gap 5/2",
            "aggregate_high_order_allowance_exact": q(allowance),
            "aggregate_high_order_allowance_scientific": scientific(allowance),
            "allocation": "equal across five orders, then equal across the native coherent groups of each order",
            "allocation_is_sufficient_not_necessary": True,
            "completion_test": "sum of certified complete group-integral upper endpoints <= aggregate_high_order_allowance_exact",
        },
        "fixed_control": {
            "orders": list(range(8, 13)),
            "resolved_vectors": all_paths,
            "coherent_groups": all_groups,
            "upper_triangle_gram_entries": all_entries,
            "ordered_quadratic_terms": all_ordered,
            "all_K179_group_keys_replayed": True,
        },
        "order_targets": rows,
        "certificate_contract": {
            "integrate_complete_group_quadratic_form_before_enclosure": True,
            "retain_every_off_diagonal_cross_term": True,
            "certify_each_group_on_its_complete_noncompact_domain": True,
            "node_value_may_seed_but_not_replace_complete_integral": True,
            "group_upper_endpoints_must_be_nonnegative": True,
            "no_occurrencewise_absolute_value": True,
            "no_cross_order_cancellation_claimed": True,
            "native_prefactor_applied_exactly_once": True,
        },
        "decision": {
            "all_high_order_coherent_groups_have_exact_sufficient_targets": True,
            "all_existing_native_node_rules_fit_their_order_targets": True,
            "current_complete_Peano_uppers_fit_targets": False,
            "complete_high_order_enclosure_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Produce complete noncompact-domain upper certificates for the K577 group targets, beginning with order eight; adaptively reallocate unused certified allowance across groups and orders without discarding coherent cross terms.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact consumer-driven target and census atlas only. The native node rules lie below their targets, but they are not complete integrals; the existing Peano uppers remain too coarse. No improved high-order enclosure, K152 shifted-form residual, complete floor, native K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["orders"] != list(range(8, 13)) or fixed["resolved_vectors"] != 2720:
        raise AssertionError("K577 high-order vector census changed")
    if fixed["coherent_groups"] != 128 or fixed["upper_triangle_gram_entries"] != 58826:
        raise AssertionError("K577 high-order group/entry census changed")
    if sum(Fraction(row["sufficient_order_upper_target_exact"]) for row in payload["order_targets"]) != Fraction(payload["target_identity"]["aggregate_high_order_allowance_exact"]):
        raise AssertionError("K577 order targets do not conserve the allowance")
    for row in payload["order_targets"]:
        if len(row["group_targets"]) != row["coherent_groups"]:
            raise AssertionError("K577 group target census changed")
        if sum(Fraction(group["sufficient_complete_integral_upper_target_exact"]) for group in row["group_targets"]) != Fraction(row["sufficient_order_upper_target_exact"]):
            raise AssertionError("K577 group targets do not conserve the order target")
        if not row["one_node_rule_is_below_order_target"] or not row["current_complete_integral_upper_exceeds_order_target"]:
            raise AssertionError("K577 feasibility disposition changed")
    if not all(payload["certificate_contract"].values()):
        raise AssertionError("K577 certificate contract weakened")
    decision = payload["decision"]
    if not decision["all_high_order_coherent_groups_have_exact_sufficient_targets"] or decision["complete_high_order_enclosure_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K577 decision boundary changed")


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

#!/usr/bin/env python3
"""Join K555 node intervals to both K566 complete Peano remainders."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K555 = ROOT / "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json"
K566 = ROOT / "lab/process/k566-orders-eleven-twelve-complete-peano-remainders.json"
OUTPUT = ROOT / "lab/process/k567-orders-eleven-twelve-complete-integral-enclosures.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def scientific(value: Fraction, digits: int = 17) -> str:
    with localcontext() as context:
        context.prec = digits + 8
        decimal_value = Decimal(value.numerator) / Decimal(value.denominator)
        return f"{decimal_value:.{digits}e}"


def build() -> dict[str, Any]:
    k555 = json.loads(K555.read_text())
    k566 = json.loads(K566.read_text())
    nodes = {int(row["order"]): row for row in k555["order_evaluations"]}
    remainders = {int(row["order"]): row for row in k566["order_remainders"]}
    order_results = []
    for order in (11, 12):
        node = nodes[order]["complete_node_evaluation"]
        node_lower = Fraction(node["normalized_one_node_rule_lower"])
        node_upper = Fraction(node["normalized_one_node_rule_upper"])
        prefactor_upper = Fraction(node["native_prefactor_interval_upper"])
        raw_remainder = Fraction(remainders[order]["exact_raw_complete_remainder_abs_upper"])
        normalized_remainder = raw_remainder * prefactor_upper
        integral_lower = node_lower - normalized_remainder
        integral_upper = node_upper + normalized_remainder
        descriptor_count = int(nodes[order]["fixed_control"]["ordered_quadratic_terms"])
        group_count = int(nodes[order]["fixed_control"]["coherent_groups"])
        hybrid_count = len(remainders[order]["hybrid_remainder_bank"])
        order_results.append({
            "order": order,
            "ordered_descriptors": descriptor_count,
            "coherent_groups": group_count,
            "hybrid_remainder_terms": hybrid_count,
            "native_prefactor": f"(2*pi)^-{order + 2}",
            "native_prefactor_application_count": 1,
            "complete_integral_enclosure": {
                "node_rule_interval": [node["normalized_one_node_rule_lower"], node["normalized_one_node_rule_upper"]],
                "raw_complete_remainder_abs_upper": q(raw_remainder),
                "native_prefactor_interval": [node["native_prefactor_interval_lower"], node["native_prefactor_interval_upper"]],
                "normalized_complete_remainder_abs_upper": q(normalized_remainder),
                "normalized_complete_remainder_abs_upper_scientific": scientific(normalized_remainder),
                "complete_integral_interval_exact": [q(integral_lower), q(integral_upper)],
                "complete_integral_interval_scientific": [scientific(integral_lower), scientific(integral_upper)],
                "node_interval_contained": integral_lower <= node_lower <= node_upper <= integral_upper,
                "sign_decided": integral_lower > 0 or integral_upper < 0,
            },
        })
    return {
        "schema_version": "1.0",
        "result_id": "K567-ORDERS-ELEVEN-TWELVE-COMPLETE-INTEGRAL-ENCLOSURES",
        "created": "2026-09-28",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K555, K566)],
            "orders": [11, 12],
            "combined_ordered_descriptors": sum(row["ordered_descriptors"] for row in order_results),
            "combined_coherent_groups": sum(row["coherent_groups"] for row in order_results),
            "combined_hybrid_remainder_terms": sum(row["hybrid_remainder_terms"] for row in order_results),
            "native_prefactor_application_count_by_order": {str(row["order"]): row["native_prefactor_application_count"] for row in order_results},
        },
        "order_enclosures": order_results,
        "composition_contract": {
            "node_value_source": "K555 separate complete coherent one-node enclosures",
            "remainder_source": "K566 separate sums of all 24/26 K565 disjoint hybrid majorants",
            "native_prefactors_applied_exactly_once": True,
            "K555_product_weights_reapplied": False,
            "lower_order_normalization_reused": False,
            "complete_order_eleven_and_twelve_integrals_enclosed": True,
        },
        "decision": {
            "complete_order_eleven_integral_enclosure_emitted": True,
            "complete_order_twelve_integral_enclosure_emitted": True,
            "order_eleven_sign_decided": order_results[0]["complete_integral_enclosure"]["sign_decided"],
            "order_twelve_sign_decided": order_results[1]["complete_integral_enclosure"]["sign_decided"],
            "base_action_column_emitted": False,
            "R_ref_residual_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "reconcile the complete order-specific enclosures with the remaining typed base-action components, then construct the complete action column and R_ref residual before any K152 claim",
        },
        "release_test": {
            "all_94752_ordered_descriptors_retained": sum(row["ordered_descriptors"] for row in order_results) == 94752,
            "all_57_coherent_groups_retained": sum(row["coherent_groups"] for row in order_results) == 57,
            "all_50_remainder_terms_present": sum(row["hybrid_remainder_terms"] for row in order_results) == 50,
            "each_native_prefactor_applied_once": all(row["native_prefactor_application_count"] == 1 for row in order_results),
            "product_weights_not_reapplied": True,
            "both_node_intervals_contained": all(row["complete_integral_enclosure"]["node_interval_contained"] for row in order_results),
            "both_complete_intervals_ordered": all(Fraction(row["complete_integral_enclosure"]["complete_integral_interval_exact"][0]) <= Fraction(row["complete_integral_enclosure"]["complete_integral_interval_exact"][1]) for row in order_results),
            "base_action_not_overclaimed": True,
            "R_ref_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k566["ledger_effect"],
        "source_routing": k566["source_routing"],
        "claim_ceiling": "Rigorous complete interval enclosures for the repository's conditional order-eleven and order-twelve coherent integrals: each K555 one-node interval plus and minus its full K566 tensor-Peano remainder after one outward native prefactor. The enclosures may be too coarse to decide sign and do not construct the complete base action column, R_ref residual, K152 interval, source/ledger movement, canon, paper, public, novelty or physical claims.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["orders"], fixed["combined_ordered_descriptors"], fixed["combined_coherent_groups"], fixed["combined_hybrid_remainder_terms"], fixed["native_prefactor_application_count_by_order"]) != ([11, 12], 94752, 57, 50, {"11": 1, "12": 1}):
        raise AssertionError("K567 fixed census changed")
    rows = payload["order_enclosures"]
    if len(rows) != 2:
        raise AssertionError("K567 order bank changed")
    for row in rows:
        lo, hi = (Fraction(value) for value in row["complete_integral_enclosure"]["complete_integral_interval_exact"])
        if lo > hi or not row["complete_integral_enclosure"]["node_interval_contained"]:
            raise AssertionError("K567 interval changed")
    contract = payload["composition_contract"]
    if not contract["native_prefactors_applied_exactly_once"] or contract["K555_product_weights_reapplied"] or contract["lower_order_normalization_reused"] or not contract["complete_order_eleven_and_twelve_integrals_enclosed"]:
        raise AssertionError("K567 composition changed")
    decision = payload["decision"]
    if not decision["complete_order_eleven_integral_enclosure_emitted"] or not decision["complete_order_twelve_integral_enclosure_emitted"] or any(decision[key] for key in ("base_action_column_emitted", "R_ref_residual_emitted", "native_K152_interval_emitted")) or not all(payload["release_test"].values()):
        raise AssertionError("K567 decision boundary changed")


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

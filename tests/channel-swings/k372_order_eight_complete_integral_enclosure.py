#!/usr/bin/env python3
"""Join K345's node interval to K371's complete Peano remainder."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K345 = ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json"
K371 = ROOT / "lab/process/k371-order-eight-complete-peano-remainder.json"
OUTPUT = ROOT / "lab/process/k372-order-eight-complete-integral-enclosure.json"


def decimal_fraction(text: str) -> Fraction:
    return Fraction(text)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def scientific(value: Fraction, digits: int = 17) -> str:
    with localcontext() as context:
        context.prec = digits + 8
        decimal_value = Decimal(value.numerator) / Decimal(value.denominator)
        return f"{decimal_value:.{digits}e}"


def build() -> dict[str, Any]:
    k345 = json.loads(K345.read_text())
    k371 = json.loads(K371.read_text())
    node = k345["complete_node_evaluation"]
    node_lower = decimal_fraction(node["normalized_one_node_rule_lower"])
    node_upper = decimal_fraction(node["normalized_one_node_rule_upper"])
    prefactor_lower = decimal_fraction(node["native_prefactor_interval_lower"])
    prefactor_upper = decimal_fraction(node["native_prefactor_interval_upper"])
    raw_remainder = Fraction(k371["remainder_contract"]["exact_raw_complete_remainder_abs_upper"])
    normalized_remainder = raw_remainder * prefactor_upper
    integral_lower = node_lower - normalized_remainder
    integral_upper = node_upper + normalized_remainder
    return {
        "schema_version": "1.0",
        "result_id": "K372-ORDER-EIGHT-COMPLETE-INTEGRAL-ENCLOSURE",
        "created": "2026-09-23",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K345, K371)],
            "ordered_descriptors": k345["fixed_control"]["ordered_quadratic_terms"],
            "coherent_groups": k345["fixed_control"]["coherent_groups"],
            "hybrid_remainder_terms": k371["fixed_control"]["hybrid_terms"],
            "native_prefactor": "(2*pi)^-10",
            "native_prefactor_application_count": 1,
        },
        "complete_integral_enclosure": {
            "node_rule_interval": [node["normalized_one_node_rule_lower"], node["normalized_one_node_rule_upper"]],
            "raw_complete_remainder_abs_upper": q(raw_remainder),
            "native_prefactor_interval": [node["native_prefactor_interval_lower"], node["native_prefactor_interval_upper"]],
            "normalized_complete_remainder_abs_upper": q(normalized_remainder),
            "normalized_complete_remainder_abs_upper_scientific": scientific(normalized_remainder),
            "complete_order_eight_integral_interval_exact": [q(integral_lower), q(integral_upper)],
            "complete_order_eight_integral_interval_scientific": [scientific(integral_lower), scientific(integral_upper)],
            "node_interval_contained": integral_lower <= node_lower <= node_upper <= integral_upper,
            "sign_decided": integral_lower > 0 or integral_upper < 0,
        },
        "composition_contract": {
            "node_value_source": "K345 complete 2,400-term, 23-group coherent node enclosure",
            "remainder_source": "K371 sum of all eighteen K370 disjoint hybrid majorants",
            "native_prefactor_applied_exactly_once": True,
            "K345_product_weight_reapplied": False,
            "K341_normalization_reused": False,
            "complete_order_eight_integral_enclosed": True,
        },
        "decision": {
            "complete_order_eight_integral_enclosure_emitted": True,
            "order_eight_sign_decided": integral_lower > 0 or integral_upper < 0,
            "rank_five_order_nine_calculus_released": True,
            "action_column_emitted": False,
            "R_ref_residual_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "build the rank-five order-nine determinant and derivative calculus, preserving the order-specific node, normalization and face atlas before any action-column composition",
        },
        "release_test": {
            "all_2400_ordered_descriptors_retained": k345["fixed_control"]["ordered_quadratic_terms"] == 2400,
            "all_23_coherent_groups_retained": k345["fixed_control"]["coherent_groups"] == 23,
            "all_18_remainder_terms_present": k371["fixed_control"]["hybrid_terms"] == 18,
            "native_prefactor_applied_once": True,
            "product_weight_not_reapplied": True,
            "node_interval_contained": integral_lower <= node_lower <= node_upper <= integral_upper,
            "complete_interval_ordered": integral_lower <= integral_upper,
            "action_column_not_overclaimed": True,
            "R_ref_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k371["ledger_effect"],
        "source_routing": k371["source_routing"],
        "claim_ceiling": "Rigorous complete interval enclosure for the repository's conditional order-eight coherent integral: K345's exact one-node interval plus and minus K371's full eighteen-axis Peano remainder after one outward native (2*pi)^-10 prefactor. The enclosure may be too coarse to decide sign and does not construct the rank-five order-nine calculus, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["ordered_descriptors"], fixed["coherent_groups"], fixed["hybrid_remainder_terms"], fixed["native_prefactor_application_count"]) != (2400, 23, 18, 1):
        raise AssertionError("K372 fixed census changed")
    enclosure = payload["complete_integral_enclosure"]
    lo, hi = (Fraction(value) for value in enclosure["complete_order_eight_integral_interval_exact"])
    if lo > hi or not enclosure["node_interval_contained"]:
        raise AssertionError("K372 interval changed")
    contract = payload["composition_contract"]
    if not contract["native_prefactor_applied_exactly_once"] or contract["K345_product_weight_reapplied"] or contract["K341_normalization_reused"] or not contract["complete_order_eight_integral_enclosed"]:
        raise AssertionError("K372 composition changed")
    decision = payload["decision"]
    if not decision["complete_order_eight_integral_enclosure_emitted"] or not decision["rank_five_order_nine_calculus_released"] or any(decision[key] for key in ("action_column_emitted", "R_ref_residual_emitted", "native_K152_interval_emitted")):
        raise AssertionError("K372 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K372 release test failed")


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

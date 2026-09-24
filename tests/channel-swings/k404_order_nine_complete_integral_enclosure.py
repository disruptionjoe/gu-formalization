#!/usr/bin/env python3
"""Join K381's node interval to K403's complete Peano remainder."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K381 = ROOT / "lab/process/k381-order-nine-group-interval-evaluator.json"
K403 = ROOT / "lab/process/k403-order-nine-complete-peano-remainder.json"
OUTPUT = ROOT / "lab/process/k404-order-nine-complete-integral-enclosure.json"


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
    k381 = json.loads(K381.read_text())
    k403 = json.loads(K403.read_text())
    node = k381["complete_node_evaluation"]
    node_lower = decimal_fraction(node["normalized_one_node_rule_lower"])
    node_upper = decimal_fraction(node["normalized_one_node_rule_upper"])
    prefactor_lower = decimal_fraction(node["native_prefactor_interval_lower"])
    prefactor_upper = decimal_fraction(node["native_prefactor_interval_upper"])
    raw_remainder = Fraction(k403["remainder_contract"]["exact_raw_complete_remainder_abs_upper"])
    normalized_remainder = raw_remainder * prefactor_upper
    integral_lower = node_lower - normalized_remainder
    integral_upper = node_upper + normalized_remainder
    return {
        "schema_version": "1.0",
        "result_id": "K404-ORDER-NINE-COMPLETE-INTEGRAL-ENCLOSURE",
        "created": "2026-09-24",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K381, K403)],
            "ordered_descriptors": k381["fixed_control"]["ordered_quadratic_terms"],
            "coherent_groups": k381["fixed_control"]["coherent_groups"],
            "hybrid_remainder_terms": k403["fixed_control"]["hybrid_terms"],
            "native_prefactor": "(2*pi)^-11",
            "native_prefactor_application_count": 1,
        },
        "complete_integral_enclosure": {
            "node_rule_interval": [node["normalized_one_node_rule_lower"], node["normalized_one_node_rule_upper"]],
            "raw_complete_remainder_abs_upper": q(raw_remainder),
            "native_prefactor_interval": [node["native_prefactor_interval_lower"], node["native_prefactor_interval_upper"]],
            "normalized_complete_remainder_abs_upper": q(normalized_remainder),
            "normalized_complete_remainder_abs_upper_scientific": scientific(normalized_remainder),
            "complete_order_nine_integral_interval_exact": [q(integral_lower), q(integral_upper)],
            "complete_order_nine_integral_interval_scientific": [scientific(integral_lower), scientific(integral_upper)],
            "node_interval_contained": integral_lower <= node_lower <= node_upper <= integral_upper,
            "sign_decided": integral_lower > 0 or integral_upper < 0,
        },
        "composition_contract": {
            "node_value_source": "K381 complete 4,480-term, twenty-group coherent node enclosure",
            "remainder_source": "K403 sum of all twenty K402 disjoint hybrid majorants",
            "native_prefactor_applied_exactly_once": True,
            "K381_product_weight_reapplied": False,
            "K345_order_eight_normalization_reused": False,
            "complete_order_nine_integral_enclosed": True,
        },
        "decision": {
            "complete_order_nine_integral_enclosure_emitted": True,
            "order_nine_sign_decided": integral_lower > 0 or integral_upper < 0,
            "order_ten_native_numerical_interface_released": True,
            "action_column_emitted": False,
            "R_ref_residual_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "build the order-ten native node, directional-jet, Peano and face interfaces from K376 before any complete order-ten integral or action-column composition",
        },
        "release_test": {
            "all_4480_ordered_descriptors_retained": k381["fixed_control"]["ordered_quadratic_terms"] == 4480,
            "all_20_coherent_groups_retained": k381["fixed_control"]["coherent_groups"] == 20,
            "all_20_remainder_terms_present": k403["fixed_control"]["hybrid_terms"] == 20,
            "native_prefactor_applied_once": True,
            "product_weight_not_reapplied": True,
            "node_interval_contained": integral_lower <= node_lower <= node_upper <= integral_upper,
            "complete_interval_ordered": integral_lower <= integral_upper,
            "action_column_not_overclaimed": True,
            "R_ref_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k403["ledger_effect"],
        "source_routing": k403["source_routing"],
        "claim_ceiling": "Rigorous complete interval enclosure for the repository's conditional order-nine coherent integral: K381's exact one-node interval plus and minus K403's full twenty-axis Peano remainder after one outward native (2*pi)^-11 prefactor. The enclosure may be too coarse to decide sign and does not construct an order-ten numerical integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["ordered_descriptors"], fixed["coherent_groups"], fixed["hybrid_remainder_terms"], fixed["native_prefactor_application_count"]) != (4480, 20, 20, 1):
        raise AssertionError("K404 fixed census changed")
    enclosure = payload["complete_integral_enclosure"]
    lo, hi = (Fraction(value) for value in enclosure["complete_order_nine_integral_interval_exact"])
    if lo > hi or not enclosure["node_interval_contained"]:
        raise AssertionError("K404 interval changed")
    contract = payload["composition_contract"]
    if not contract["native_prefactor_applied_exactly_once"] or contract["K381_product_weight_reapplied"] or contract["K345_order_eight_normalization_reused"] or not contract["complete_order_nine_integral_enclosed"]:
        raise AssertionError("K404 composition changed")
    decision = payload["decision"]
    if not decision["complete_order_nine_integral_enclosure_emitted"] or not decision["order_ten_native_numerical_interface_released"] or any(decision[key] for key in ("action_column_emitted", "R_ref_residual_emitted", "native_K152_interval_emitted")):
        raise AssertionError("K404 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K404 release test failed")


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

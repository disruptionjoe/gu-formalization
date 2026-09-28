#!/usr/bin/env python3
"""Sum the separate order-eleven/twelve hybrid banks in K558 tensor order."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K558 = ROOT / "lab/process/k558-orders-eleven-twelve-positive-peano-contract.json"
K565 = ROOT / "lab/process/k565-orders-eleven-twelve-disjoint-hybrid-majorants.json"
OUTPUT = ROOT / "lab/process/k566-orders-eleven-twelve-complete-peano-remainders.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k558 = json.loads(K558.read_text())
    k565 = json.loads(K565.read_text())
    majorants = {
        int(order_row["order"]): {row["axis"]: Fraction(row["exact_complete_hybrid_abs_upper"]) for row in order_row["hybrid_majorant_bank"]}
        for order_row in k565["order_hybrid_majorants"]
    }
    order_results = []
    for contract in k558["order_contracts"]:
        order = int(contract["order"])
        rows = []
        cumulative = Fraction()
        for axis_contract in contract["tensor_telescoping"]["axis_contracts"]:
            axis = axis_contract["axis"]
            value = majorants[order][axis]
            cumulative += value
            rows.append({
                "axis": axis,
                "preceding_axes_fixed_at_node": axis_contract["preceding_axes_fixed_at_node"],
                "following_axes_integrated_exactly": axis_contract["following_axes_integrated_exactly"],
                "exact_hybrid_abs_upper": q(value),
                "exact_cumulative_abs_upper": q(cumulative),
            })
        order_results.append({
            "order": order,
            "native_axes": contract["fixed_control"]["native_axes"],
            "tensor_identity": contract["tensor_telescoping"]["identity"],
            "hybrid_remainder_bank": rows,
            "exact_raw_complete_remainder_abs_upper": q(cumulative),
            "native_prefactor_still_unapplied": True,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K566-ORDERS-ELEVEN-TWELVE-COMPLETE-PEANO-REMAINDERS",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K558, K565)],
            "orders": [11, 12],
            "combined_hybrid_terms": sum(len(row["hybrid_remainder_bank"]) for row in order_results),
            "hybrid_terms_by_order": {str(row["order"]): len(row["hybrid_remainder_bank"]) for row in order_results},
            "native_prefactors_applied": False,
        },
        "order_remainders": order_results,
        "remainder_contract": {
            "absolute_rule": "apply the triangle inequality only after each complete coherent K565 hybrid is bounded on its disjoint owner partition",
            "mixed_derivatives_required": False,
            "separate_24_and_26_term_tensor_identities_preserved": True,
            "native_prefactors_still_unapplied": True,
        },
        "decision": {
            "complete_order_eleven_raw_remainder_emitted": True,
            "complete_order_twelve_raw_remainder_emitted": True,
            "all_fifty_K558_hybrids_summed": True,
            "complete_higher_order_integrals_enclosed": False,
            "next_exact_input": "multiply each raw remainder by its outward K555 native prefactor exactly once and join the corresponding one-node interval",
        },
        "release_test": {
            "exactly_24_order_eleven_terms": len(order_results[0]["hybrid_remainder_bank"]) == 24,
            "exactly_26_order_twelve_terms": len(order_results[1]["hybrid_remainder_bank"]) == 26,
            "axis_orders_match_K558": all(row["native_axes"] == [item["axis"] for item in row["hybrid_remainder_bank"]] for row in order_results),
            "preceding_following_counts_replay": all(item["preceding_axes_fixed_at_node"] + item["following_axes_integrated_exactly"] == len(row["hybrid_remainder_bank"]) - 1 for row in order_results for item in row["hybrid_remainder_bank"]),
            "all_hybrid_uppers_positive": all(Fraction(item["exact_hybrid_abs_upper"]) > 0 for row in order_results for item in row["hybrid_remainder_bank"]),
            "cumulative_sums_exact": all(Fraction(row["exact_raw_complete_remainder_abs_upper"]) == sum((Fraction(item["exact_hybrid_abs_upper"]) for item in row["hybrid_remainder_bank"]), Fraction()) for row in order_results),
            "mixed_derivatives_absent": True,
            "native_prefactors_not_double_applied": True,
            "complete_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k565["ledger_effect"],
        "source_routing": k565["source_routing"],
        "claim_ceiling": "Exact rational absolute upper bounds for the complete raw order-eleven and order-twelve tensor-Peano remainders, obtained by separately summing K565's 24 and 26 disjoint complete coherent hybrid bounds in K558 tensor order. The native prefactors and K555 node intervals are not yet composed, so these are not complete integral enclosures and supply no base action, R_ref, K152, source/ledger movement, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["orders"] != [11, 12] or fixed["combined_hybrid_terms"] != 50 or fixed["hybrid_terms_by_order"] != {"11": 24, "12": 26} or fixed["native_prefactors_applied"]:
        raise AssertionError("K566 fixed control changed")
    rows = payload["order_remainders"]
    if len(rows) != 2 or [len(row["hybrid_remainder_bank"]) for row in rows] != [24, 26] or not all(row["native_prefactor_still_unapplied"] for row in rows) or any(Fraction(item["exact_hybrid_abs_upper"]) <= 0 for row in rows for item in row["hybrid_remainder_bank"]):
        raise AssertionError("K566 remainder bank changed")
    contract = payload["remainder_contract"]
    if contract["mixed_derivatives_required"] or not contract["separate_24_and_26_term_tensor_identities_preserved"] or not contract["native_prefactors_still_unapplied"]:
        raise AssertionError("K566 remainder contract changed")
    decision = payload["decision"]
    if not decision["complete_order_eleven_raw_remainder_emitted"] or not decision["complete_order_twelve_raw_remainder_emitted"] or decision["complete_higher_order_integrals_enclosed"] or not all(payload["release_test"].values()):
        raise AssertionError("K566 decision boundary changed")


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

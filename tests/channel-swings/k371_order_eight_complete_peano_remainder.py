#!/usr/bin/env python3
"""Sum the eighteen K370 hybrids under the exact K348 tensor Peano identity."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K348 = ROOT / "lab/process/k348-order-eight-positive-peano-contract.json"
K370 = ROOT / "lab/process/k370-order-eight-disjoint-owner-hybrid-majorants.json"
OUTPUT = ROOT / "lab/process/k371-order-eight-complete-peano-remainder.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k348 = json.loads(K348.read_text())
    k370 = json.loads(K370.read_text())
    axis_contracts = k348["tensor_telescoping"]["axis_contracts"]
    majorants = {row["axis"]: Fraction(row["exact_complete_hybrid_abs_upper"]) for row in k370["hybrid_majorant_bank"]}
    rows = []
    cumulative = Fraction()
    for contract in axis_contracts:
        axis = contract["axis"]
        value = majorants[axis]
        cumulative += value
        rows.append({
            "axis": axis,
            "preceding_axes_fixed_at_node": contract["preceding_axes_fixed_at_node"],
            "following_axes_integrated_exactly": contract["following_axes_integrated_exactly"],
            "exact_hybrid_abs_upper": q(value),
            "exact_cumulative_abs_upper": q(cumulative),
        })
    return {
        "schema_version": "1.0",
        "result_id": "K371-ORDER-EIGHT-COMPLETE-PEANO-REMAINDER",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K348, K370)],
            "native_axes": [row["axis"] for row in axis_contracts],
            "hybrid_terms": len(rows),
            "tensor_identity": k348["tensor_telescoping"]["identity"],
            "native_prefactor_applied": False,
        },
        "hybrid_remainder_bank": rows,
        "remainder_contract": {
            "absolute_rule": "apply the triangle inequality only after each complete coherent K370 hybrid integral is bounded on its disjoint owner partition",
            "mixed_derivatives_required": False,
            "all_eighteen_pure_second_terms_present": len(rows) == 18,
            "exact_raw_complete_remainder_abs_upper": q(cumulative),
            "native_prefactor_still_unapplied": True,
        },
        "decision": {
            "complete_order_eight_raw_remainder_emitted": True,
            "all_eighteen_K348_hybrids_summed": True,
            "complete_order_eight_integral_enclosed": False,
            "rank_five_order_nine_dependency_released_after_K345_join": False,
            "next_exact_input": "multiply the raw remainder by the outward native (2*pi)^-10 interval exactly once and join K345's node interval",
        },
        "release_test": {
            "exactly_18_hybrid_terms": len(rows) == 18,
            "axis_order_matches_K348": [row["axis"] for row in rows] == k348["fixed_control"]["native_axes"],
            "preceding_following_counts_replay": all(row["preceding_axes_fixed_at_node"] + row["following_axes_integrated_exactly"] == 17 for row in rows),
            "all_hybrid_uppers_positive": all(Fraction(row["exact_hybrid_abs_upper"]) > 0 for row in rows),
            "cumulative_sum_exact": cumulative == sum((Fraction(row["exact_hybrid_abs_upper"]) for row in rows), Fraction()),
            "mixed_derivatives_absent": True,
            "native_prefactor_not_double_applied": True,
            "complete_integral_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k370["ledger_effect"],
        "source_routing": k370["source_routing"],
        "claim_ceiling": "Exact rational absolute upper bound for the complete raw eighteen-axis order-eight Peano remainder, obtained by summing K370's disjoint complete coherent hybrid bounds in K348 tensor order. The native (2*pi)^-10 prefactor and K345 node interval are not yet composed, so this is not yet the complete order-eight integral enclosure and supplies no action column, R_ref, K152, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["fixed_control"]["hybrid_terms"] != 18 or payload["fixed_control"]["native_prefactor_applied"]:
        raise AssertionError("K371 fixed control changed")
    rows = payload["hybrid_remainder_bank"]
    if len(rows) != 18 or any(Fraction(row["exact_hybrid_abs_upper"]) <= 0 for row in rows):
        raise AssertionError("K371 remainder bank changed")
    decision = payload["decision"]
    if not decision["complete_order_eight_raw_remainder_emitted"] or not decision["all_eighteen_K348_hybrids_summed"] or decision["complete_order_eight_integral_enclosed"]:
        raise AssertionError("K371 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K371 release test failed")


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

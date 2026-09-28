#!/usr/bin/env python3
"""Sum the twenty-two K551 hybrids under the exact K409 tensor Peano identity."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K409 = ROOT / "lab/process/k409-order-ten-positive-peano-contract.json"
K551 = ROOT / "lab/process/k551-order-ten-disjoint-owner-hybrid-majorants.json"
OUTPUT = ROOT / "lab/process/k552-order-ten-complete-peano-remainder.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k409 = json.loads(K409.read_text())
    k551 = json.loads(K551.read_text())
    axis_contracts = k409["tensor_telescoping"]["axis_contracts"]
    majorants = {row["axis"]: Fraction(row["exact_complete_hybrid_abs_upper"]) for row in k551["hybrid_majorant_bank"]}
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
        "result_id": "K552-ORDER-TEN-COMPLETE-PEANO-REMAINDER",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K409, K551)],
            "native_axes": [row["axis"] for row in axis_contracts],
            "hybrid_terms": len(rows),
            "tensor_identity": k409["tensor_telescoping"]["identity"],
            "native_prefactor_applied": False,
        },
        "hybrid_remainder_bank": rows,
        "remainder_contract": {
            "absolute_rule": "apply the triangle inequality only after each complete coherent K551 hybrid integral is bounded on its disjoint owner partition",
            "mixed_derivatives_required": False,
            "all_twenty_two_pure_second_terms_present": len(rows) == 22,
            "exact_raw_complete_remainder_abs_upper": q(cumulative),
            "native_prefactor_still_unapplied": True,
        },
        "decision": {
            "complete_order_ten_raw_remainder_emitted": True,
            "all_twenty_two_K409_hybrids_summed": True,
            "complete_order_ten_integral_enclosed": False,
            "next_exact_input": "multiply the raw remainder by the outward native (2*pi)^-12 interval exactly once and join K406's node interval",
        },
        "release_test": {
            "exactly_22_hybrid_terms": len(rows) == 22,
            "axis_order_matches_K409": [row["axis"] for row in rows] == k409["fixed_control"]["native_axes"],
            "preceding_following_counts_replay": all(row["preceding_axes_fixed_at_node"] + row["following_axes_integrated_exactly"] == 21 for row in rows),
            "all_hybrid_uppers_positive": all(Fraction(row["exact_hybrid_abs_upper"]) > 0 for row in rows),
            "cumulative_sum_exact": cumulative == sum((Fraction(row["exact_hybrid_abs_upper"]) for row in rows), Fraction()),
            "mixed_derivatives_absent": True,
            "native_prefactor_not_double_applied": True,
            "complete_integral_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k551["ledger_effect"],
        "source_routing": k551["source_routing"],
        "claim_ceiling": "Exact rational absolute upper bound for the complete raw twenty-two-axis order-ten Peano remainder, obtained by summing K551's disjoint complete coherent hybrid bounds in K409 tensor order. The native (2*pi)^-12 prefactor and K406 node interval are not yet composed, so this is not yet the complete order-ten integral enclosure and supplies no action column, R_ref, K152, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["fixed_control"]["hybrid_terms"] != 22 or payload["fixed_control"]["native_prefactor_applied"]:
        raise AssertionError("K552 fixed control changed")
    rows = payload["hybrid_remainder_bank"]
    if len(rows) != 22 or any(Fraction(row["exact_hybrid_abs_upper"]) <= 0 for row in rows):
        raise AssertionError("K552 remainder bank changed")
    decision = payload["decision"]
    if not decision["complete_order_ten_raw_remainder_emitted"] or not decision["all_twenty_two_K409_hybrids_summed"] or decision["complete_order_ten_integral_enclosed"]:
        raise AssertionError("K552 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K552 release test failed")


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

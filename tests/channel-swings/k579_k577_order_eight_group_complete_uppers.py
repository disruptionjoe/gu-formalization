#!/usr/bin/env python3
"""K579 complete order-eight group uppers from the K369/K370 owner cover."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K345 = ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json"
K369 = ROOT / "lab/process/k369-order-eight-whole-radial-face-majorants.json"
K370 = ROOT / "lab/process/k370-order-eight-disjoint-owner-hybrid-majorants.json"
K371 = ROOT / "lab/process/k371-order-eight-complete-peano-remainder.json"
K372 = ROOT / "lab/process/k372-order-eight-complete-integral-enclosure.json"
K577 = ROOT / "lab/process/k577-k152-high-order-coherent-group-target-atlas.json"
OUTPUT = ROOT / "lab/process/k579-k577-order-eight-group-complete-uppers.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def scientific(value: Fraction, digits: int = 14) -> str:
    with localcontext() as context:
        context.prec = digits
        return f"{Decimal(value.numerator) / Decimal(value.denominator):.{digits - 1}E}"


def decimal_fraction(value: str) -> Fraction:
    return Fraction(Decimal(value))


def build() -> dict[str, Any]:
    k345 = json.loads(K345.read_text())
    k369 = json.loads(K369.read_text())
    k370 = json.loads(K370.read_text())
    k371 = json.loads(K371.read_text())
    k372 = json.loads(K372.read_text())
    k577 = json.loads(K577.read_text())

    descriptor_seconds: dict[str, Fraction] = defaultdict(Fraction)
    descriptor_counts: dict[str, int] = defaultdict(int)
    for row in k369["descriptor_majorant_bank"]:
        group = row["group_id"]
        descriptor_seconds[group] += Fraction(row["normalized_second_abs_upper"])
        descriptor_counts[group] += 1

    complete_second = Fraction(
        k369["complete_coherent_majorant"]["normalized_complete_second_derivative_abs_upper"]
    )
    raw_complete_remainder = Fraction(
        k371["remainder_contract"]["exact_raw_complete_remainder_abs_upper"]
    )
    native_prefactor_upper = decimal_fraction(
        k372["complete_integral_enclosure"]["native_prefactor_interval"][1]
    )
    product_weight = Fraction(k345["complete_node_evaluation"]["native_product_weight"])
    nodes = {row["group_id"]: row for row in k345["coherent_group_values"]}
    targets = {
        row["group_id"]: row
        for order in k577["order_targets"]
        if order["order"] == 8
        for row in order["group_targets"]
    }

    groups = []
    for group_id in sorted(targets):
        group_second = descriptor_seconds[group_id]
        scale = group_second / complete_second
        hybrid_uppers = [
            Fraction(row["exact_complete_hybrid_abs_upper"]) * scale
            for row in k370["hybrid_majorant_bank"]
        ]
        raw_remainder = sum(hybrid_uppers, Fraction())
        normalized_remainder = raw_remainder * native_prefactor_upper
        node = nodes[group_id]
        normalized_node_upper = (
            decimal_fraction(node["coherent_node_value_upper"])
            * product_weight
            * native_prefactor_upper
        )
        complete_upper = normalized_node_upper + normalized_remainder
        target = Fraction(targets[group_id]["sufficient_complete_integral_upper_target_exact"])
        groups.append(
            {
                "group_id": group_id,
                "path_count": targets[group_id]["path_count"],
                "ordered_descriptors": descriptor_counts[group_id],
                "group_second_derivative_abs_upper_exact": q(group_second),
                "share_of_complete_second_exact": q(scale),
                "normalized_node_upper_exact_from_outward_decimal": q(normalized_node_upper),
                "normalized_complete_remainder_abs_upper_exact": q(normalized_remainder),
                "normalized_complete_integral_abs_upper_exact": q(complete_upper),
                "normalized_complete_integral_abs_upper_scientific": scientific(complete_upper),
                "K577_sufficient_target_exact": q(target),
                "K577_target_met": complete_upper <= target,
                "upper_to_target_ratio_scientific": scientific(complete_upper / target),
            }
        )

    group_second_sum = sum(descriptor_seconds.values(), Fraction())
    group_raw_remainder_sum = sum(
        (Fraction(row["normalized_complete_remainder_abs_upper_exact"]) / native_prefactor_upper for row in groups),
        Fraction(),
    )
    targets_met = sum(row["K577_target_met"] for row in groups)
    return {
        "schema_version": "1.0",
        "result_id": "K579-K577-ORDER-EIGHT-GROUP-COMPLETE-UPPERS",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "All 23 K577 order-eight coherent groups on their complete noncompact K348 domains, using the existing K369 whole-radial and K370 disjoint-owner cover without occurrencewise sign claims.",
        "gu_typed_objects": {
            "carrier": "K179 order-eight q00/q10/q01 coherent action-column groups",
            "pairing": "continuum positive-Fock Gram pairing",
            "form": "complete signed coherent group quadratic integral",
            "result": "groupwise complete noncompact upper atlas MAP-TYPE=interval-upper",
            "target": "K577 order-eight sufficient complete-integral targets",
        },
        "linearity_theorem": {
            "descriptor_partition": "K369's 2,400 ordered descriptors partition exactly by the 23 native group_id values before the final coherent sum.",
            "face_owner_linearity": "Every K369 face upper and both terms of every K370 hybrid upper are a common nonnegative cover factor times normalized_complete_second_derivative_abs_upper.",
            "group_replay": "Replace only that complete second-derivative sum by the exact descriptor sum for one group; retain the same transition constant, all face owners, recursive interior cells and eighteen-axis Peano identity.",
            "node_join": "A complete group integral has absolute upper <= outward group node upper + the groupwise complete Peano remainder after one native prefactor.",
            "cross_terms_retained": True,
            "occurrencewise_absolute_value_used": False,
        },
        "fixed_control": {
            "groups": len(groups),
            "ordered_descriptors": sum(descriptor_counts.values()),
            "hybrid_terms_per_group": len(k370["hybrid_majorant_bank"]),
            "face_programs_reused": len(k369["whole_radial_face_bank"]),
            "low_coordinate_subsets_replayed_per_complete_cover": k370["fixed_control"]["low_coordinate_subsets_replayed"],
            "complete_second_derivative_abs_upper_exact": q(complete_second),
            "group_second_derivative_sum_exact": q(group_second_sum),
            "raw_complete_remainder_exact": q(raw_complete_remainder),
            "group_raw_remainder_sum_exact": q(group_raw_remainder_sum),
            "native_prefactor_upper_exact_from_outward_decimal": q(native_prefactor_upper),
            "native_prefactor_application_count": 1,
        },
        "group_complete_upper_bank": groups,
        "decision": {
            "all_order_eight_groups_have_complete_noncompact_upper": True,
            "K577_targets_met": targets_met,
            "K577_targets_failed": len(groups) - targets_met,
            "current_group_cover_is_decision_useful_for_25_over_9_budget": targets_met > 0,
            "complete_order_eight_signed_sum_retracted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Replace the shared worst-case K369 transition/interior majorants by group-adaptive determinant and radial bounds; the complete current cover is finite for every group but remains too coarse wherever K577_target_met is false.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Rigorous complete noncompact-domain absolute uppers for every native order-eight coherent group, conserving the full K369 descriptor and K371 remainder totals. These are group-resolved versions of the current coarse Peano cover; they do not improve the signed K372 sum, move K152, or change source, ledger, canon, paper, public, novelty or physical conclusions.",
    }


def validate(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    rows = payload["group_complete_upper_bank"]
    if fixed["groups"] != 23 or fixed["ordered_descriptors"] != 2400 or fixed["hybrid_terms_per_group"] != 18:
        raise AssertionError("K579 fixed census changed")
    if Fraction(fixed["group_second_derivative_sum_exact"]) != Fraction(fixed["complete_second_derivative_abs_upper_exact"]):
        raise AssertionError("K579 group derivative sums do not conserve K369")
    if Fraction(fixed["group_raw_remainder_sum_exact"]) != Fraction(fixed["raw_complete_remainder_exact"]):
        raise AssertionError("K579 group remainders do not conserve K371")
    if len(rows) != 23 or len({row["group_id"] for row in rows}) != 23:
        raise AssertionError("K579 group bank changed")
    if any(Fraction(row["normalized_complete_integral_abs_upper_exact"]) <= 0 for row in rows):
        raise AssertionError("K579 emitted a nonpositive group upper")
    if not payload["linearity_theorem"]["cross_terms_retained"] or payload["linearity_theorem"]["occurrencewise_absolute_value_used"]:
        raise AssertionError("K579 weakened coherent assembly")
    decision = payload["decision"]
    if decision["K577_targets_met"] + decision["K577_targets_failed"] != 23:
        raise AssertionError("K579 target disposition incomplete")
    if not decision["all_order_eight_groups_have_complete_noncompact_upper"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K579 decision boundary changed")


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

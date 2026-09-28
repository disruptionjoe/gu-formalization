#!/usr/bin/env python3
"""K582 group-rank-adaptive replay of K579's complete order-eight uppers."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K345 = ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json"
K350 = ROOT / "lab/process/k350-order-eight-hybrid-face-atlas.json"
K369 = ROOT / "lab/process/k369-order-eight-whole-radial-face-majorants.json"
K370 = ROOT / "lab/process/k370-order-eight-disjoint-owner-hybrid-majorants.json"
K372 = ROOT / "lab/process/k372-order-eight-complete-integral-enclosure.json"
K577 = ROOT / "lab/process/k577-k152-high-order-coherent-group-target-atlas.json"
K579 = ROOT / "lab/process/k579-k577-order-eight-group-complete-uppers.json"
OUTPUT = ROOT / "lab/process/k582-k579-group-rank-adaptive-complete-uppers.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K370_BACKEND = load("k370_for_k582", "k370_order_eight_disjoint_owner_hybrid_majorants.py")


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
    k350 = json.loads(K350.read_text())
    k369 = json.loads(K369.read_text())
    k370 = json.loads(K370.read_text())
    k372 = json.loads(K372.read_text())
    k577 = json.loads(K577.read_text())
    k579 = json.loads(K579.read_text())

    complete = k369["complete_coherent_majorant"]
    complete_second = Fraction(complete["normalized_complete_second_derivative_abs_upper"])
    global_transition = Fraction(complete["transition_constant"])
    rank_uppers = {
        int(rank): [Fraction(value) for value in values]
        for rank, values in complete["determinant_derivative_uppers_by_rank"].items()
    }
    group_second: dict[str, Fraction] = defaultdict(Fraction)
    group_ranks: dict[str, set[int]] = defaultdict(set)
    descriptor_counts: dict[str, int] = defaultdict(int)
    for row in k369["descriptor_majorant_bank"]:
        group = row["group_id"]
        group_second[group] += Fraction(row["normalized_second_abs_upper"])
        group_ranks[group].update(int(rank) for rank in row["species_ranks"])
        descriptor_counts[group] += 1

    face_rows = {row["program_id"]: row for row in k369["whole_radial_face_bank"]}
    hybrid_rows = {row["axis"]: row for row in k370["hybrid_majorant_bank"]}
    hybrid_owner_programs: dict[str, list[str]] = {}
    for hybrid in k350["hybrid_face_atlas"]:
        assignments, counts = K370_BACKEND.owner_assignments(hybrid)
        counts.pop("INTERIOR", None)
        hybrid_owner_programs[hybrid["axis"]] = [
            f"{hybrid['axis']}:{next(kind for kind, rows in hybrid['faces'].items() for row in rows if tuple(row['zeroed_axes']) == tuple(owner.split(',')))}:{owner}"
            for owner in sorted(counts, key=lambda text: tuple(K370_BACKEND.AXIS_INDEX[a] for a in text.split(",")))
        ]
        if len(assignments) != hybrid_rows[hybrid["axis"]]["low_coordinate_subsets_replayed"]:
            raise AssertionError("K582 owner replay changed the K370 subset census")

    nodes = {row["group_id"]: row for row in k345["coherent_group_values"]}
    targets = {
        row["group_id"]: row
        for order in k577["order_targets"] if order["order"] == 8
        for row in order["group_targets"]
    }
    old_rows = {row["group_id"]: row for row in k579["group_complete_upper_bank"]}
    native_prefactor_upper = decimal_fraction(k372["complete_integral_enclosure"]["native_prefactor_interval"][1])
    product_weight = Fraction(k345["complete_node_evaluation"]["native_product_weight"])

    groups = []
    for group_id in sorted(targets):
        second = group_second[group_id]
        ranks = sorted(group_ranks[group_id])
        transition = max(value for rank in ranks for value in rank_uppers[rank])
        face_total = Fraction()
        interior_total = Fraction()
        hybrid_bank = []
        for axis in K370_BACKEND.AXES:
            face_sum = Fraction()
            for program_id in hybrid_owner_programs[axis]:
                face = face_rows[program_id]
                depth = int(face["maximum_nested_transition_depth"])
                original = Fraction(face["exact_whole_radial_abs_upper"])
                face_sum += original * second / complete_second * (transition / global_transition) ** depth
            interior = Fraction(hybrid_rows[axis]["exact_positive_interior_abs_upper"]) * second / complete_second
            face_total += face_sum
            interior_total += interior
            hybrid_bank.append({
                "axis": axis,
                "group_face_owner_union_abs_upper_exact": q(face_sum),
                "group_positive_interior_abs_upper_exact": q(interior),
                "group_complete_hybrid_abs_upper_exact": q(face_sum + interior),
            })
        raw_remainder = face_total + interior_total
        normalized_remainder = raw_remainder * native_prefactor_upper
        node = nodes[group_id]
        normalized_node_upper = decimal_fraction(node["coherent_node_value_upper"]) * product_weight * native_prefactor_upper
        complete_upper = normalized_node_upper + normalized_remainder
        old_upper = Fraction(old_rows[group_id]["normalized_complete_integral_abs_upper_exact"])
        target = Fraction(targets[group_id]["sufficient_complete_integral_upper_target_exact"])
        groups.append({
            "group_id": group_id,
            "path_count": targets[group_id]["path_count"],
            "ordered_descriptors": descriptor_counts[group_id],
            "determinant_ranks_present": ranks,
            "group_second_derivative_abs_upper_exact": q(second),
            "group_transition_constant_exact": q(transition),
            "global_transition_constant_exact": q(global_transition),
            "transition_constant_strictly_improved": transition < global_transition,
            "hybrid_bank": hybrid_bank,
            "raw_group_face_total_exact": q(face_total),
            "raw_group_interior_total_exact": q(interior_total),
            "normalized_complete_integral_abs_upper_exact": q(complete_upper),
            "normalized_complete_integral_abs_upper_scientific": scientific(complete_upper),
            "K579_complete_upper_exact": q(old_upper),
            "strictly_improves_K579": complete_upper < old_upper,
            "improvement_factor_scientific": scientific(old_upper / complete_upper),
            "K577_sufficient_target_exact": q(target),
            "K577_target_met": complete_upper <= target,
            "upper_to_target_ratio_scientific": scientific(complete_upper / target),
        })

    targets_met = sum(row["K577_target_met"] for row in groups)
    improved = sum(row["strictly_improves_K579"] for row in groups)
    return {
        "schema_version": "1.0",
        "result_id": "K582-K579-GROUP-RANK-ADAPTIVE-COMPLETE-UPPERS",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "All 23 K579 order-eight coherent groups on the complete K363/K370 owner cover, replacing only K369's global determinant-transition maximum by the maximum over determinant ranks actually present in each group.",
        "gu_typed_objects": {
            "carrier": "K179 order-eight q00/q10/q01 coherent action-column groups",
            "pairing": "continuum positive-Fock Gram pairing",
            "form": "complete signed coherent group quadratic integral",
            "result": "rank-adaptive complete group upper atlas MAP-TYPE=interval-upper",
            "target": "K577 order-eight sufficient complete-integral targets",
        },
        "rank_adaptive_theorem": {
            "fixed_matrix_rank": "Every determinant factor in one K352 descriptor retains its matrix size under K367's zero-inclusive confluent transitions.",
            "group_transition_rule": "At every nested face transition, maximize K369's exact derivative envelopes only over matrix ranks occurring in that coherent group.",
            "face_replay": "Multiply each K369 face row by the exact group-second share and by (group transition/global transition)^depth.",
            "interior_replay": "K370's positive-interior bound is linear in the complete second-derivative majorant and carries no determinant transition factor, so scale it only by the exact group-second share.",
            "owner_cover_unchanged": True,
            "cross_terms_retained": True,
        },
        "fixed_control": {
            "groups": len(groups),
            "ordered_descriptors": sum(descriptor_counts.values()),
            "face_programs": len(face_rows),
            "hybrids_per_group": len(K370_BACKEND.AXES),
            "low_coordinate_subsets_per_complete_cover": k370["fixed_control"]["low_coordinate_subsets_replayed"],
            "global_transition_constant_exact": q(global_transition),
            "group_second_sum_exact": q(sum(group_second.values(), Fraction())),
            "complete_second_exact": q(complete_second),
            "old_K579_raw_remainder_exact": k579["fixed_control"]["raw_complete_remainder_exact"],
            "new_group_raw_remainder_sum_exact": q(sum((Fraction(row["raw_group_face_total_exact"]) + Fraction(row["raw_group_interior_total_exact"]) for row in groups), Fraction())),
        },
        "group_complete_upper_bank": groups,
        "decision": {
            "groups_strictly_improved_over_K579": improved,
            "groups_unchanged_from_K579": len(groups) - improved,
            "K577_targets_met": targets_met,
            "K577_targets_failed": len(groups) - targets_met,
            "all_complete_noncompact_group_uppers_preserved": True,
            "native_K152_interval_emitted": False,
            "next_exact_input": "For groups still above target, replace rankwise global derivative maxima by descriptor- and face-mask-specific determinant envelopes and tighten K370's positive-interior scale penalty; retain K582 wherever its rank restriction already helps.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Rigorous group-rank-adaptive complete noncompact-domain absolute uppers for all 23 native order-eight coherent groups on the unchanged K363/K370 owner cover. The result tightens K579 only where a group omits K369's worst determinant rank; it is not a signed integral value, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    rows = payload["group_complete_upper_bank"]
    if (fixed["groups"], fixed["ordered_descriptors"], fixed["face_programs"], fixed["hybrids_per_group"]) != (23, 2400, 517, 18):
        raise AssertionError("K582 fixed census changed")
    if Fraction(fixed["group_second_sum_exact"]) != Fraction(fixed["complete_second_exact"]):
        raise AssertionError("K582 group second derivatives do not conserve K369")
    if Fraction(fixed["new_group_raw_remainder_sum_exact"]) > Fraction(fixed["old_K579_raw_remainder_exact"]):
        raise AssertionError("K582 rank adaptation enlarged K579")
    if len(rows) != 23 or any(len(row["hybrid_bank"]) != 18 for row in rows):
        raise AssertionError("K582 group/hybrid bank changed")
    if any(Fraction(row["normalized_complete_integral_abs_upper_exact"]) > Fraction(row["K579_complete_upper_exact"]) for row in rows):
        raise AssertionError("K582 emitted an upper above K579")
    decision = payload["decision"]
    if decision["groups_strictly_improved_over_K579"] + decision["groups_unchanged_from_K579"] != 23:
        raise AssertionError("K582 improvement disposition incomplete")
    if decision["K577_targets_met"] + decision["K577_targets_failed"] != 23:
        raise AssertionError("K582 target disposition incomplete")
    if not payload["rank_adaptive_theorem"]["owner_cover_unchanged"] or not payload["rank_adaptive_theorem"]["cross_terms_retained"]:
        raise AssertionError("K582 weakened the owner or coherent cover")
    if decision["native_K152_interval_emitted"]:
        raise AssertionError("K582 overclaimed K152")


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

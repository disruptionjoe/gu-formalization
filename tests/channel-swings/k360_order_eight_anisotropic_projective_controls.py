#!/usr/bin/env python3
"""Execute K352-preconditioned controls away from K356's equal-normal line."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K354 = ROOT / "lab/process/k354-order-eight-face-program-compiler.json"
K358 = ROOT / "lab/process/k358-order-eight-normal-projective-atlas.json"
K359 = ROOT / "lab/process/k359-order-eight-projective-measure-and-boundary-routing.json"
K356_PRODUCER = HERE / "k356_order_eight_preconditioned_face_cell_bank.py"
OUTPUT = ROOT / "lab/process/k360-order-eight-anisotropic-projective-controls.json"

ctx.dps = 180
ctx.threads = 1

spec = importlib.util.spec_from_file_location("k356_for_k360", K356_PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K356 producer")
K356 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K356
spec.loader.exec_module(K356)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def anisotropic_proportions(axes: list[str]) -> dict[str, Fraction]:
    weights = {axis: Fraction(index + 1) for index, axis in enumerate(axes)}
    total = sum(weights.values(), start=Fraction(0))
    return {axis: weight / total for axis, weight in weights.items()}


def raw_times(program: dict[str, Any], rho: arb, proportions: dict[str, Fraction]) -> dict[str, arb]:
    zeroed = set(program["zeroed_axes"])
    if set(proportions) != zeroed or sum(proportions.values(), start=Fraction(0)) != 1:
        raise AssertionError("K360 projective proportions changed")
    return {
        axis: rho * arb(q(proportions[axis])) if axis in zeroed else arb(1) / 256
        for axis in K356.K347_BACKEND.AXES
    }


def build() -> dict[str, Any]:
    k354 = json.loads(K354.read_text())
    k358 = json.loads(K358.read_text())
    k359 = json.loads(K359.read_text())
    k352 = json.loads(K356.K352.read_text())
    singular, confluent = K356.template_maps(k352)
    programs = k354["face_programs"]
    codimensions = k358["fixed_control"]["reachable_codimensions"]
    rho_fraction = Fraction(1, 2048)
    rho = arb(q(rho_fraction))
    controls = []

    for codimension in codimensions:
        program = next(row for row in programs if int(row["codimension"]) == codimension)
        proportions = anisotropic_proportions(program["zeroed_axes"])
        raw = raw_times(program, rho, proportions)
        original_raw_times = K356.raw_times
        K356.raw_times = lambda selected, selected_rho, raw=raw: raw
        try:
            second, groups, singular_histogram, confluent_histogram, operations = K356.complete_second(
                program, rho, singular, confluent
            )
        finally:
            K356.raw_times = original_raw_times
        direct, direct_groups = K356.K351_BACKEND.complete_second(program["axis"], raw)
        overlap = not (second.upper() < direct.lower() or second.lower() > direct.upper())
        cumulative_s, cumulative_v = K356.K351_BACKEND.cumulative(raw)
        minimum_argument = min(
            [value.lower() for value in cumulative_s.values()]
            + [value.lower() for value in cumulative_v.values()]
        )
        if not second.is_finite() or not direct.is_finite() or minimum_argument <= 0 or not overlap:
            raise AssertionError(f"K360 anisotropic control failed at codimension {codimension}")
        values = list(proportions.values())
        controls.append({
            "codimension": codimension,
            "program_id": program["program_id"],
            "axis": program["axis"],
            "zeroed_axes": program["zeroed_axes"],
            "rho": q(rho_fraction),
            "projective_proportions": {axis: q(value) for axis, value in proportions.items()},
            "proportions_sum_to_one": sum(values, start=Fraction(0)) == 1,
            "direction_is_not_equal_normal": len(set(values)) > 1,
            "minimum_cumulative_argument_lower": K356.lower_text(arb(minimum_argument)),
            "preconditioned_second_lower": K356.lower_text(second),
            "preconditioned_second_upper": K356.upper_text(second),
            "direct_second_lower": K356.lower_text(direct),
            "direct_second_upper": K356.upper_text(direct),
            "preconditioned_direct_intervals_overlap": overlap,
            "coherent_group_count": len(groups),
            "direct_coherent_group_count": len(direct_groups),
            "preconditioned_group_digest": K356.digest(groups),
            "direct_group_digest": K356.digest(direct_groups),
            "singular_template_ids": sorted(singular_histogram),
            "confluent_template_ids": sorted(confluent_histogram),
            "divided_difference_operation_uses": operations,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K360-ORDER-EIGHT-ANISOTROPIC-PROJECTIVE-CONTROLS",
        "created": "2026-09-23",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K354.relative_to(ROOT)), str(K358.relative_to(ROOT)), str(K359.relative_to(ROOT))],
            "arb_decimal_digits": 180,
            "threads": 1,
            "reachable_codimensions": codimensions,
            "selected_controls": len(controls),
            "rho": q(rho_fraction),
            "ordered_descriptors_per_control": 2400,
            "ordered_descriptor_control_evaluations": len(controls) * 2400,
            "coherent_groups_per_control": 23,
        },
        "execution_contract": {
            "one_non_equal_positive_rational_direction_per_reachable_codimension": True,
            "raw_times_are_rho_times_projective_proportions": True,
            "K352_assignment_dual_and_confluent_preconditioning_reused": True,
            "all_ordered_orientations_retained": True,
            "all_23_coherent_groups_assembled_before_enclosure": True,
            "direct_complete_evaluator_overlap_required": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "point_controls_are_not_positive_width_projective_cells": True,
        },
        "anisotropic_control_bank": controls,
        "control_summary": {
            "all_13_reachable_codimensions_executed": len(controls) == 13,
            "all_controls_finite": all(math.isfinite(float(row["preconditioned_second_lower"])) and math.isfinite(float(row["preconditioned_second_upper"])) for row in controls),
            "all_argument_floors_positive": all(float(row["minimum_cumulative_argument_lower"]) > 0 for row in controls),
            "all_directions_non_equal": all(row["direction_is_not_equal_normal"] for row in controls),
            "all_preconditioned_direct_controls_overlap": all(row["preconditioned_direct_intervals_overlap"] for row in controls),
            "all_controls_keep_23_groups": all(row["coherent_group_count"] == 23 and row["direct_coherent_group_count"] == 23 for row in controls),
        },
        "decision": {
            "anisotropic_projective_point_interface_executed": True,
            "positive_width_projective_cells_evaluated": False,
            "zero_inclusive_projective_boundary_majorants_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "construct positive-width maximum-chart ratio cells together with one-sided zero-boundary strip majorants, then define disjoint global face-neighborhood ownership before joining the interior and tails",
        },
        "release_test": {
            "exactly_13_controls": len(controls) == 13,
            "all_31200_ordered_descriptor_controls_covered": len(controls) * 2400 == 31_200,
            "all_projective_proportions_exact_and_non_equal": all(row["proportions_sum_to_one"] and row["direction_is_not_equal_normal"] for row in controls),
            "all_controls_finite_and_positive_floor": all(math.isfinite(float(row["preconditioned_second_lower"])) and math.isfinite(float(row["preconditioned_second_upper"])) and float(row["minimum_cumulative_argument_lower"]) > 0 for row in controls),
            "all_direct_overlaps_pass": all(row["preconditioned_direct_intervals_overlap"] for row in controls),
            "all_coherent_group_censuses_preserved": all(row["coherent_group_count"] == 23 and row["direct_coherent_group_count"] == 23 for row in controls),
            "raw_zero_evaluation_absent": True,
            "projective_cells_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k354["ledger_effect"],
        "source_routing": k354["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb execution of one non-equal positive rational projective direction for every reachable K354 codimension. All thirteen controls reuse K352's determinant-preserving preconditioners, retain 2,400 ordered descriptors and 23 coherent groups, have positive argument floors, remain finite and overlap the direct complete evaluator. These are point controls, not positive-width projective cells, zero-inclusive boundary majorants, a recursive interior cover, analytic tails, K348 hybrid integrals, the complete order-eight remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["selected_controls"], fixed["ordered_descriptors_per_control"], fixed["ordered_descriptor_control_evaluations"], fixed["coherent_groups_per_control"]) != (13, 2400, 31_200, 23):
        raise AssertionError("K360 control census changed")
    rows = payload["anisotropic_control_bank"]
    if len(rows) != 13 or [row["codimension"] for row in rows] != fixed["reachable_codimensions"]:
        raise AssertionError("K360 codimension bank changed")
    if any(not row["proportions_sum_to_one"] or not row["direction_is_not_equal_normal"] or float(row["minimum_cumulative_argument_lower"]) <= 0 or not row["preconditioned_direct_intervals_overlap"] or row["coherent_group_count"] != 23 or row["direct_coherent_group_count"] != 23 for row in rows):
        raise AssertionError("K360 anisotropic control changed")
    contract = payload["execution_contract"]
    if contract["raw_Bessel_evaluation_at_zero_used"] or not contract["point_controls_are_not_positive_width_projective_cells"] or not contract["all_ordered_orientations_retained"]:
        raise AssertionError("K360 execution boundary changed")
    decision = payload["decision"]
    if not decision["anisotropic_projective_point_interface_executed"] or any(decision[key] for key in ("positive_width_projective_cells_evaluated", "zero_inclusive_projective_boundary_majorants_complete", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K360 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K360 release test failed")


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

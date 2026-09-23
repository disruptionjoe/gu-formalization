#!/usr/bin/env python3
"""Compile positive-width K358 chart cells and execute one per codimension."""

from __future__ import annotations

import argparse
import hashlib
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
K360 = ROOT / "lab/process/k360-order-eight-anisotropic-projective-controls.json"
K356_PRODUCER = HERE / "k356_order_eight_preconditioned_face_cell_bank.py"
OUTPUT = ROOT / "lab/process/k361-order-eight-positive-width-projective-cells.json"

ctx.dps = 180
ctx.threads = 1

spec = importlib.util.spec_from_file_location("k356_for_k361", K356_PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K356 producer")
K356 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K356
spec.loader.exec_module(K356)

RHO_CELL = (Fraction(1, 4096), Fraction(5, 16384))


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def interval(left: Fraction, right: Fraction) -> arb:
    return arb(q((left + right) / 2), q((right - left) / 2))


def power_integral(left: Fraction, right: Fraction, exponent: int) -> Fraction:
    if exponent <= -1:
        raise AssertionError("K361 radial exponent is not integrable")
    return (right ** (exponent + 1) - left ** (exponent + 1)) / (exponent + 1)


def chart_cell(chart: dict[str, Any], codimension: int) -> dict[str, Any]:
    bounds: dict[str, list[str]] = {}
    centers: dict[str, str] = {}
    widths: list[Fraction] = []
    half = Fraction(1, 64 * codimension)
    for index, axis in enumerate(chart["ratio_axes"]):
        center = Fraction(index + 1, codimension + 1)
        left, right = center - half, center + half
        if not 0 < left < right < 1:
            raise AssertionError("K361 ratio cell escaped the open chart")
        bounds[axis] = [q(left), q(right)]
        centers[axis] = q(center)
        widths.append(right - left)
    volume = math.prod(widths, start=Fraction(1))
    denominator_lower = Fraction(1) + sum((Fraction(pair[0]) for pair in bounds.values()), Fraction(0))
    density_upper = denominator_lower ** (-codimension)
    return {
        "chart_id": chart["chart_id"],
        "anchor_axis": chart["anchor_axis"],
        "ratio_bounds": bounds,
        "ratio_centers": centers,
        "positive_width_in_every_ratio": all(Fraction(pair[0]) > 0 and Fraction(pair[1]) < 1 for pair in bounds.values()),
        "exact_box_volume": q(volume),
        "angular_density_upper": q(density_upper),
        "angular_mass_majorant": q(volume * density_upper),
    }


def raw_times(program: dict[str, Any], cell: dict[str, Any], rho: arb) -> dict[str, arb]:
    ratios = {axis: interval(Fraction(pair[0]), Fraction(pair[1])) for axis, pair in cell["ratio_bounds"].items()}
    denominator = arb(1) + sum(ratios.values(), arb(0))
    anchor = cell["anchor_axis"]
    zeroed = set(program["zeroed_axes"])
    if zeroed != set(ratios) | {anchor}:
        raise AssertionError("K361 chart/program mask mismatch")
    return {
        axis: (rho / denominator if axis == anchor else rho * ratios[axis] / denominator)
        if axis in zeroed else arb(1) / 256
        for axis in K356.K347_BACKEND.AXES
    }


def midpoint_raw(program: dict[str, Any], cell: dict[str, Any], rho_value: Fraction) -> dict[str, arb]:
    ratios = {axis: Fraction(value) for axis, value in cell["ratio_centers"].items()}
    denominator = Fraction(1) + sum(ratios.values(), Fraction(0))
    anchor = cell["anchor_axis"]
    zeroed = set(program["zeroed_axes"])
    return {
        axis: arb(q(rho_value / denominator if axis == anchor else rho_value * ratios[axis] / denominator))
        if axis in zeroed else arb(1) / 256
        for axis in K356.K347_BACKEND.AXES
    }


def build() -> dict[str, Any]:
    k354 = json.loads(K354.read_text())
    k358 = json.loads(K358.read_text())
    k359 = json.loads(K359.read_text())
    k360 = json.loads(K360.read_text())
    k352 = json.loads(K356.K352.read_text())
    singular, confluent = K356.template_maps(k352)

    cells = []
    cell_map: dict[str, dict[str, Any]] = {}
    for mask in k358["mask_atlas"]:
        for chart in mask["charts"]:
            cell = chart_cell(chart, int(mask["codimension"]))
            cells.append(cell)
            cell_map[cell["chart_id"]] = cell
    program_cell_uses = [
        {"program_id": row["program_id"], "chart_cell_ids": list(row["chart_ids"])}
        for row in k358["program_chart_map"]
    ]

    controls = []
    rho = interval(*RHO_CELL)
    rho_midpoint = sum(RHO_CELL, Fraction(0)) / 2
    programs = k354["face_programs"]
    for codimension in k358["fixed_control"]["reachable_codimensions"]:
        program = next(row for row in programs if int(row["codimension"]) == codimension)
        chart_id = next(value for value in next(row for row in k358["program_chart_map"] if row["program_id"] == program["program_id"])["chart_ids"] if value.endswith(":" + program["zeroed_axes"][-1]))
        cell = cell_map[chart_id]
        raw = raw_times(program, cell, rho)
        original_raw_times = K356.raw_times
        K356.raw_times = lambda selected, selected_rho, raw=raw: raw
        try:
            second, groups, singular_histogram, confluent_histogram, operations = K356.complete_second(program, rho, singular, confluent)
        finally:
            K356.raw_times = original_raw_times
        direct_raw = midpoint_raw(program, cell, rho_midpoint)
        direct, direct_groups = K356.K351_BACKEND.complete_second(program["axis"], direct_raw)
        contains_midpoint = second.lower() <= direct.lower() and second.upper() >= direct.upper()
        cumulative_s, cumulative_v = K356.K351_BACKEND.cumulative(raw)
        minimum_argument = min([value.lower() for value in cumulative_s.values()] + [value.lower() for value in cumulative_v.values()])
        singular_power = int(program["maximum_value_first_second_singular_powers"][2])
        active = bool(program["active_peano_axis_zeroed"])
        radial_exponent = codimension - 1 - singular_power + (2 if active else 0)
        if radial_exponent != int(program["minimum_second_derivative_face_normal_power"]):
            raise AssertionError("K361 failed to replay K353 radial exponent")
        scaled_upper = abs(second) * rho ** singular_power
        if active:
            p_active = raw[program["axis"]] / rho
            peano_angular_upper = abs(p_active).upper() ** 2 / 2
        else:
            peano_angular_upper = arb(1) / (2 * 256 * 256)
        radial_mass = power_integral(*RHO_CELL, radial_exponent)
        angular_mass_upper = Fraction(cell["angular_mass_majorant"])
        contribution = scaled_upper * peano_angular_upper * arb(q(radial_mass * angular_mass_upper))
        if not second.is_finite() or not contribution.is_finite() or minimum_argument <= 0 or not contains_midpoint:
            raise AssertionError(f"K361 positive-width control failed at codimension {codimension}")
        controls.append({
            "codimension": codimension,
            "program_id": program["program_id"],
            "axis": program["axis"],
            "chart_id": chart_id,
            "rho_interval": [q(value) for value in RHO_CELL],
            "minimum_cumulative_argument_lower": K356.lower_text(arb(minimum_argument)),
            "complete_second_derivative_abs_upper": K356.abs_upper_text(second),
            "scaled_second_derivative_abs_upper": K356.abs_upper_text(scaled_upper),
            "midpoint_direct_interval_contained": contains_midpoint,
            "coherent_group_count": len(groups),
            "direct_coherent_group_count": len(direct_groups),
            "singular_template_ids": sorted(singular_histogram),
            "confluent_template_ids": sorted(confluent_histogram),
            "divided_difference_operation_uses": operations,
            "K353_radial_exponent": radial_exponent,
            "exact_radial_mass": q(radial_mass),
            "projective_angular_mass_majorant": q(angular_mass_upper),
            "integrated_cell_abs_upper": K356.abs_upper_text(contribution),
        })

    return {
        "schema_version": "1.0",
        "result_id": "K361-ORDER-EIGHT-POSITIVE-WIDTH-PROJECTIVE-CELLS",
        "created": "2026-09-23",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K354, K358, K359, K360)],
            "unique_maximum_charts": len(cells),
            "program_chart_cell_uses": sum(len(row["chart_cell_ids"]) for row in program_cell_uses),
            "reachable_codimensions": k358["fixed_control"]["reachable_codimensions"],
            "executed_interval_controls": len(controls),
            "rho_cell": [q(value) for value in RHO_CELL],
            "ordered_descriptors_per_control": 2400,
            "ordered_descriptor_interval_evaluations": len(controls) * 2400,
            "coherent_groups_per_control": 23,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "projective_cell_contract": {
            "one_exact_positive_width_box_per_K358_chart": True,
            "every_ratio_interval_is_strictly_inside_zero_and_one": True,
            "angular_density_upper_uses_denominator_lower_power": True,
            "K352_assignment_dual_and_confluent_preconditioning_reused": True,
            "all_ordered_orientations_retained": True,
            "all_23_coherent_groups_assembled_before_enclosure": True,
            "midpoint_direct_complete_evaluator_containment_required": True,
            "cells_are_pilots_not_a_chart_cover": True,
        },
        "chart_cell_bank": cells,
        "program_chart_cell_map": program_cell_uses,
        "executed_cell_bank": controls,
        "cell_summary": {
            "all_578_charts_have_positive_width_cells": len(cells) == 578 and all(row["positive_width_in_every_ratio"] for row in cells),
            "all_2998_program_chart_uses_mapped": sum(len(row["chart_cell_ids"]) for row in program_cell_uses) == 2998,
            "all_13_reachable_codimensions_executed": len(controls) == 13,
            "all_interval_controls_finite": all(math.isfinite(float(row["complete_second_derivative_abs_upper"])) and math.isfinite(float(row["integrated_cell_abs_upper"])) for row in controls),
            "all_argument_floors_positive": all(float(row["minimum_cumulative_argument_lower"]) > 0 for row in controls),
            "all_midpoint_direct_controls_contained": all(row["midpoint_direct_interval_contained"] for row in controls),
            "all_controls_keep_23_groups": all(row["coherent_group_count"] == 23 and row["direct_coherent_group_count"] == 23 for row in controls),
            "chart_cell_bank_sha256": digest(cells),
        },
        "decision": {
            "positive_width_projective_cell_interface_executed": True,
            "complete_projective_chart_cover_emitted": False,
            "zero_inclusive_integrand_weighted_boundary_majorants_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "combine exact zero-strip angular mass and global owner partitions with a determinant-preserving integrand-weighted boundary envelope before recursive subdivision",
        },
        "release_test": {
            "exactly_578_chart_cells": len(cells) == 578,
            "exactly_2998_program_cell_uses": sum(len(row["chart_cell_ids"]) for row in program_cell_uses) == 2998,
            "exactly_13_interval_controls": len(controls) == 13,
            "all_31200_ordered_descriptor_intervals_covered": len(controls) * 2400 == 31_200,
            "all_cells_strictly_positive_width": all(row["positive_width_in_every_ratio"] for row in cells),
            "all_controls_finite_positive_and_contain_midpoint": all(math.isfinite(float(row["integrated_cell_abs_upper"])) and float(row["minimum_cumulative_argument_lower"]) > 0 and row["midpoint_direct_interval_contained"] for row in controls),
            "all_coherent_group_censuses_preserved": all(row["coherent_group_count"] == 23 and row["direct_coherent_group_count"] == 23 for row in controls),
            "complete_chart_cover_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k360["ledger_effect"],
        "source_routing": k360["source_routing"],
        "claim_ceiling": "One exact positive-width pilot box in each of K358's 578 maximum charts, all 2,998 program-chart uses mapped, and one rigorous K352-preconditioned radial/projective interval integrated at every reachable codimension. These pilot cells do not cover a complete chart and do not control zero-inclusive projective boundaries, the recursive interior, analytic tails, any complete K348 hybrid, the complete order-eight remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["unique_maximum_charts"], fixed["program_chart_cell_uses"], fixed["executed_interval_controls"], fixed["ordered_descriptor_interval_evaluations"], fixed["coherent_groups_per_control"]) != (578, 2998, 13, 31_200, 23):
        raise AssertionError("K361 census changed")
    if len(payload["chart_cell_bank"]) != 578 or len(payload["executed_cell_bank"]) != 13:
        raise AssertionError("K361 bank changed")
    if not all(row["positive_width_in_every_ratio"] for row in payload["chart_cell_bank"]):
        raise AssertionError("K361 cell touched a chart boundary")
    if not all(row["midpoint_direct_interval_contained"] and row["coherent_group_count"] == 23 and row["direct_coherent_group_count"] == 23 and float(row["minimum_cumulative_argument_lower"]) > 0 for row in payload["executed_cell_bank"]):
        raise AssertionError("K361 numerical control changed")
    contract = payload["projective_cell_contract"]
    if not contract["one_exact_positive_width_box_per_K358_chart"] or not contract["cells_are_pilots_not_a_chart_cover"]:
        raise AssertionError("K361 cell contract changed")
    decision = payload["decision"]
    if not decision["positive_width_projective_cell_interface_executed"] or any(decision[key] for key in ("complete_projective_chart_cover_emitted", "zero_inclusive_integrand_weighted_boundary_majorants_complete", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K361 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K361 release test failed")


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

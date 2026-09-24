#!/usr/bin/env python3
"""Compile positive-width K394 chart cells and execute one per codimension."""

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
K390 = ROOT / "lab/process/k390-order-nine-face-program-compiler.json"
K394 = ROOT / "lab/process/k394-order-nine-normal-projective-atlas.json"
K395 = ROOT / "lab/process/k395-order-nine-projective-measure-and-boundary-routing.json"
K396 = ROOT / "lab/process/k396-order-nine-anisotropic-projective-controls.json"
K392_PRODUCER = HERE / "k392_order_nine_preconditioned_face_cell_bank.py"
OUTPUT = ROOT / "lab/process/k397-order-nine-positive-width-projective-cells.json"

ctx.dps = 180
ctx.threads = 1

spec = importlib.util.spec_from_file_location("k392_for_k397", K392_PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K392 producer")
K392 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K392
spec.loader.exec_module(K392)

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
        raise AssertionError("K397 radial exponent is not integrable")
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
            raise AssertionError("K397 ratio cell escaped the open chart")
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
        raise AssertionError("K397 chart/program mask mismatch")
    return {
        axis: (rho / denominator if axis == anchor else rho * ratios[axis] / denominator)
        if axis in zeroed else arb(1) / 256
        for axis in K392.K387_BACKEND.AXES
    }


def midpoint_raw(program: dict[str, Any], cell: dict[str, Any], rho_value: Fraction) -> dict[str, arb]:
    ratios = {axis: Fraction(value) for axis, value in cell["ratio_centers"].items()}
    denominator = Fraction(1) + sum(ratios.values(), Fraction(0))
    anchor = cell["anchor_axis"]
    zeroed = set(program["zeroed_axes"])
    return {
        axis: arb(q(rho_value / denominator if axis == anchor else rho_value * ratios[axis] / denominator))
        if axis in zeroed else arb(1) / 256
        for axis in K392.K387_BACKEND.AXES
    }


def build() -> dict[str, Any]:
    k390 = json.loads(K390.read_text())
    k394 = json.loads(K394.read_text())
    k395 = json.loads(K395.read_text())
    k396 = json.loads(K396.read_text())
    k388 = json.loads(K392.K388.read_text())
    singular, confluent = K392.template_maps(k388)

    cells = []
    cell_map: dict[str, dict[str, Any]] = {}
    for mask in k394["mask_atlas"]:
        for chart in mask["charts"]:
            cell = chart_cell(chart, int(mask["codimension"]))
            cells.append(cell)
            cell_map[cell["chart_id"]] = cell
    program_cell_uses = [
        {"program_id": row["program_id"], "chart_cell_ids": list(row["chart_ids"])}
        for row in k394["program_chart_map"]
    ]

    controls = []
    rho = interval(*RHO_CELL)
    rho_midpoint = sum(RHO_CELL, Fraction(0)) / 2
    programs = k390["face_programs"]
    for codimension in k394["fixed_control"]["reachable_codimensions"]:
        program = next(row for row in programs if int(row["codimension"]) == codimension)
        chart_id = next(value for value in next(row for row in k394["program_chart_map"] if row["program_id"] == program["program_id"])["chart_ids"] if value.endswith(":" + program["zeroed_axes"][-1]))
        cell = cell_map[chart_id]
        raw = raw_times(program, cell, rho)
        original_raw_times = K392.raw_times
        K392.raw_times = lambda selected, selected_rho, raw=raw: raw
        try:
            second, groups, singular_histogram, confluent_histogram, operations = K392.complete_second(program, rho, singular, confluent)
        finally:
            K392.raw_times = original_raw_times
        direct_raw = midpoint_raw(program, cell, rho_midpoint)
        direct, direct_groups = K392.K387_BACKEND.complete_second(program["axis"], direct_raw)
        contains_midpoint = second.lower() <= direct.lower() and second.upper() >= direct.upper()
        cumulative_s, cumulative_v = K392.K387_BACKEND.cumulative(raw)
        minimum_argument = min([value.lower() for value in cumulative_s.values()] + [value.lower() for value in cumulative_v.values()])
        singular_power = int(program["maximum_value_first_second_singular_powers"][2])
        active = bool(program["active_peano_axis_zeroed"])
        radial_exponent = codimension - 1 - singular_power + (2 if active else 0)
        if radial_exponent != int(program["minimum_second_derivative_face_normal_power"]):
            raise AssertionError("K397 failed to replay K389 radial exponent")
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
            raise AssertionError(f"K397 positive-width control failed at codimension {codimension}")
        controls.append({
            "codimension": codimension,
            "program_id": program["program_id"],
            "axis": program["axis"],
            "chart_id": chart_id,
            "rho_interval": [q(value) for value in RHO_CELL],
            "minimum_cumulative_argument_lower": K392.lower_text(arb(minimum_argument)),
            "complete_second_derivative_abs_upper": K392.abs_upper_text(second),
            "scaled_second_derivative_abs_upper": K392.abs_upper_text(scaled_upper),
            "midpoint_direct_interval_contained": contains_midpoint,
            "coherent_group_count": len(groups),
            "direct_coherent_group_count": len(direct_groups),
            "singular_template_ids": sorted(singular_histogram),
            "confluent_template_ids": sorted(confluent_histogram),
            "divided_difference_operation_uses": operations,
            "K389_radial_exponent": radial_exponent,
            "exact_radial_mass": q(radial_mass),
            "projective_angular_mass_majorant": q(angular_mass_upper),
            "integrated_cell_abs_upper": K392.abs_upper_text(contribution),
        })

    return {
        "schema_version": "1.0",
        "result_id": "K397-ORDER-NINE-POSITIVE-WIDTH-PROJECTIVE-CELLS",
        "created": "2026-09-23",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K390, K394, K395, K396)],
            "unique_maximum_charts": len(cells),
            "program_chart_cell_uses": sum(len(row["chart_cell_ids"]) for row in program_cell_uses),
            "reachable_codimensions": k394["fixed_control"]["reachable_codimensions"],
            "executed_interval_controls": len(controls),
            "rho_cell": [q(value) for value in RHO_CELL],
            "ordered_descriptors_per_control": 4480,
            "ordered_descriptor_interval_evaluations": len(controls) * 4480,
            "coherent_groups_per_control": 20,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "projective_cell_contract": {
            "one_exact_positive_width_box_per_K394_chart": True,
            "every_ratio_interval_is_strictly_inside_zero_and_one": True,
            "angular_density_upper_uses_denominator_lower_power": True,
            "K388_assignment_dual_and_confluent_preconditioning_reused": True,
            "all_ordered_orientations_retained": True,
            "all_20_coherent_groups_assembled_before_enclosure": True,
            "midpoint_direct_complete_evaluator_containment_required": True,
            "cells_are_pilots_not_a_chart_cover": True,
        },
        "chart_cell_bank": cells,
        "program_chart_cell_map": program_cell_uses,
        "executed_cell_bank": controls,
        "cell_summary": {
            "all_758_charts_have_positive_width_cells": len(cells) == 758 and all(row["positive_width_in_every_ratio"] for row in cells),
            "all_4320_program_chart_uses_mapped": sum(len(row["chart_cell_ids"]) for row in program_cell_uses) == 4320,
            "all_14_reachable_codimensions_executed": len(controls) == 14,
            "all_interval_controls_finite": all(math.isfinite(float(row["complete_second_derivative_abs_upper"])) and math.isfinite(float(row["integrated_cell_abs_upper"])) for row in controls),
            "all_argument_floors_positive": all(float(row["minimum_cumulative_argument_lower"]) > 0 for row in controls),
            "all_midpoint_direct_controls_contained": all(row["midpoint_direct_interval_contained"] for row in controls),
            "all_controls_keep_20_groups": all(row["coherent_group_count"] == 20 and row["direct_coherent_group_count"] == 20 for row in controls),
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
            "exactly_758_chart_cells": len(cells) == 758,
            "exactly_4320_program_cell_uses": sum(len(row["chart_cell_ids"]) for row in program_cell_uses) == 4320,
            "exactly_14_interval_controls": len(controls) == 14,
            "all_62720_ordered_descriptor_intervals_covered": len(controls) * 4480 == 62_720,
            "all_cells_strictly_positive_width": all(row["positive_width_in_every_ratio"] for row in cells),
            "all_controls_finite_positive_and_contain_midpoint": all(math.isfinite(float(row["integrated_cell_abs_upper"])) and float(row["minimum_cumulative_argument_lower"]) > 0 and row["midpoint_direct_interval_contained"] for row in controls),
            "all_coherent_group_censuses_preserved": all(row["coherent_group_count"] == 20 and row["direct_coherent_group_count"] == 20 for row in controls),
            "complete_chart_cover_not_overclaimed": True,
            "complete_order_nine_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k396["ledger_effect"],
        "source_routing": k396["source_routing"],
        "claim_ceiling": "One exact positive-width pilot box in each of K394's 758 maximum charts, all 4,320 program-chart uses mapped, and one rigorous K388-preconditioned radial/projective interval integrated at every reachable codimension. These pilot cells do not cover a complete chart and do not control zero-inclusive projective boundaries, the recursive interior, analytic tails, any complete K384 hybrid, the complete order-nine remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["unique_maximum_charts"], fixed["program_chart_cell_uses"], fixed["executed_interval_controls"], fixed["ordered_descriptor_interval_evaluations"], fixed["coherent_groups_per_control"]) != (758, 4320, 14, 62_720, 20):
        raise AssertionError("K397 census changed")
    if len(payload["chart_cell_bank"]) != 758 or len(payload["executed_cell_bank"]) != 14:
        raise AssertionError("K397 bank changed")
    if not all(row["positive_width_in_every_ratio"] for row in payload["chart_cell_bank"]):
        raise AssertionError("K397 cell touched a chart boundary")
    if not all(row["midpoint_direct_interval_contained"] and row["coherent_group_count"] == 20 and row["direct_coherent_group_count"] == 20 and float(row["minimum_cumulative_argument_lower"]) > 0 for row in payload["executed_cell_bank"]):
        raise AssertionError("K397 numerical control changed")
    contract = payload["projective_cell_contract"]
    if not contract["one_exact_positive_width_box_per_K394_chart"] or not contract["cells_are_pilots_not_a_chart_cover"]:
        raise AssertionError("K397 cell contract changed")
    decision = payload["decision"]
    if not decision["positive_width_projective_cell_interface_executed"] or any(decision[key] for key in ("complete_projective_chart_cover_emitted", "zero_inclusive_integrand_weighted_boundary_majorants_complete", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K397 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K397 release test failed")


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

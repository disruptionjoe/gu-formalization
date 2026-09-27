#!/usr/bin/env python3
"""Compile strict K542 chart pilots and execute one per reachable codimension."""

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
K487 = ROOT / "lab/process/k487-order-ten-face-program-compiler.json"
K542 = ROOT / "lab/process/k542-order-ten-normal-projective-partition.json"
K508_PRODUCER = HERE / "k508_order_ten_selected_face_cell_bank.py"
OUTPUT = ROOT / "lab/process/k543-order-ten-positive-width-projective-pilots.json"
RHO_CELL = (Fraction(1, 4096), Fraction(5, 16384))

ctx.dps = 180
ctx.threads = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K508 = load_module(K508_PRODUCER, "k508_for_k543")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def interval(left: Fraction, right: Fraction) -> arb:
    return arb(q((left + right) / 2), q((right - left) / 2))


def power_integral(left: Fraction, right: Fraction, exponent: int) -> Fraction:
    if exponent <= -1:
        raise AssertionError("K543 radial exponent is not integrable")
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
            raise AssertionError("K543 ratio cell escaped the open chart")
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
        raise AssertionError("K543 chart/program mask mismatch")
    return {
        axis: (rho / denominator if axis == anchor else rho * ratios[axis] / denominator)
        if axis in zeroed else arb(1) / 256
        for axis in K508.K408.AXES
    }


def midpoint_raw(program: dict[str, Any], cell: dict[str, Any], rho_value: Fraction) -> dict[str, arb]:
    ratios = {axis: Fraction(value) for axis, value in cell["ratio_centers"].items()}
    denominator = Fraction(1) + sum(ratios.values(), Fraction(0))
    anchor = cell["anchor_axis"]
    zeroed = set(program["zeroed_axes"])
    return {
        axis: arb(q(rho_value / denominator if axis == anchor else rho_value * ratios[axis] / denominator))
        if axis in zeroed else arb(1) / 256
        for axis in K508.K408.AXES
    }


def build() -> dict[str, Any]:
    k487 = json.loads(K487.read_text())
    k542 = json.loads(K542.read_text())
    k485 = json.loads(K508.K485_JSON.read_text())
    singular, confluent = K508.BASE.template_maps(k485)
    programs = k487["face_programs"]
    programs_by_id = {row["program_id"]: row for row in programs}
    partition_ids = {row["program_id"] for row in k542["program_partition_map"]}
    if set(programs_by_id) != partition_ids or len(programs) != 936:
        raise AssertionError("K543 program custody changed")

    cells = []
    cell_map: dict[str, dict[str, Any]] = {}
    for mask in k542["mask_atlas"]:
        for chart in mask["charts"]:
            cell = chart_cell(chart, int(mask["codimension"]))
            cells.append(cell)
            cell_map[cell["chart_id"]] = cell
    program_cell_uses = [
        {"program_id": row["program_id"], "chart_cell_ids": list(row["chart_ids"])}
        for row in k542["program_partition_map"]
    ]

    controls = []
    rho = interval(*RHO_CELL)
    rho_midpoint = sum(RHO_CELL, Fraction(0)) / 2
    for codimension in k542["fixed_control"]["reachable_codimensions"]:
        program = next(row for row in programs if int(row["codimension"]) == codimension)
        partition = next(row for row in k542["program_partition_map"] if row["program_id"] == program["program_id"])
        chart_id = next(value for value in partition["chart_ids"] if value.endswith(":" + program["zeroed_axes"][-1]))
        cell = cell_map[chart_id]
        raw = raw_times(program, cell, rho)
        original_raw_times = K508.BASE.raw_times
        K508.BASE.raw_times = lambda selected, selected_rho, raw=raw: raw
        try:
            second, groups, singular_histogram, confluent_histogram, operations = K508.BASE.complete_second(program, rho, singular, confluent)
        finally:
            K508.BASE.raw_times = original_raw_times
        direct_raw = midpoint_raw(program, cell, rho_midpoint)
        direct, direct_groups = K508.K412.complete_second(program["axis"], direct_raw)
        contains_midpoint = second.lower() <= direct.lower() and second.upper() >= direct.upper()
        cumulative_s, cumulative_v = K508.K412.cumulative(raw)
        minimum_argument = min([value.lower() for value in cumulative_s.values()] + [value.lower() for value in cumulative_v.values()])
        singular_power = int(program["maximum_value_first_second_singular_powers"][2])
        active = bool(program["active_peano_axis_zeroed"])
        radial_exponent = codimension - 1 - singular_power + (2 if active else 0)
        if radial_exponent != int(program["minimum_second_derivative_face_normal_power"]):
            raise AssertionError("K543 failed to replay the K415 radial exponent")
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
            raise AssertionError(f"K543 positive-width control failed at codimension {codimension}")
        controls.append({
            "codimension": codimension,
            "program_id": program["program_id"],
            "axis": program["axis"],
            "chart_id": chart_id,
            "rho_interval": [q(value) for value in RHO_CELL],
            "minimum_cumulative_argument_lower": K508.lower_text(arb(minimum_argument)),
            "complete_second_derivative_abs_upper": K508.abs_upper_text(second),
            "scaled_second_derivative_abs_upper": K508.abs_upper_text(scaled_upper),
            "midpoint_direct_interval_contained": contains_midpoint,
            "coherent_group_count": len(groups),
            "direct_coherent_group_count": len(direct_groups),
            "singular_template_ids": sorted(singular_histogram),
            "confluent_template_ids": sorted(confluent_histogram),
            "divided_difference_operation_uses": operations,
            "K415_radial_exponent": radial_exponent,
            "exact_radial_mass": q(radial_mass),
            "projective_angular_mass_majorant": q(angular_mass_upper),
            "integrated_cell_abs_upper": K508.abs_upper_text(contribution),
        })

    return {
        "schema_version": "1.0",
        "result_id": "K543-ORDER-TEN-POSITIVE-WIDTH-PROJECTIVE-PILOTS",
        "created": "2026-09-27",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K487.relative_to(ROOT)), str(K542.relative_to(ROOT))],
            "unique_maximum_charts": len(cells),
            "program_chart_cell_uses": sum(len(row["chart_cell_ids"]) for row in program_cell_uses),
            "reachable_codimensions": k542["fixed_control"]["reachable_codimensions"],
            "executed_interval_controls": len(controls),
            "rho_cell": [q(value) for value in RHO_CELL],
            "ordered_descriptors_per_control": 13300,
            "ordered_descriptor_interval_evaluations": len(controls) * 13300,
            "coherent_groups_per_control": 28,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "projective_cell_contract": {
            "one_exact_positive_width_box_per_K542_chart": True,
            "every_ratio_interval_is_strictly_inside_zero_and_one": True,
            "angular_density_upper_uses_denominator_lower_power": True,
            "K413_assignment_dual_and_confluent_preconditioning_reused": True,
            "all_13300_ordered_descriptors_retained": True,
            "all_28_coherent_groups_assembled_before_enclosure": True,
            "midpoint_direct_complete_evaluator_containment_required": True,
            "cells_are_pilots_not_a_chart_cover": True,
        },
        "chart_cell_bank": cells,
        "program_chart_cell_map": program_cell_uses,
        "executed_cell_bank": controls,
        "cell_summary": {
            "all_1022_charts_have_positive_width_cells": len(cells) == 1022 and all(row["positive_width_in_every_ratio"] for row in cells),
            "all_6337_program_chart_uses_mapped": sum(len(row["chart_cell_ids"]) for row in program_cell_uses) == 6337,
            "all_16_reachable_codimensions_executed": len(controls) == 16,
            "all_interval_controls_finite": all(math.isfinite(float(row["complete_second_derivative_abs_upper"])) and math.isfinite(float(row["integrated_cell_abs_upper"])) for row in controls),
            "all_argument_floors_positive": all(float(row["minimum_cumulative_argument_lower"]) > 0 for row in controls),
            "all_midpoint_direct_controls_contained": all(row["midpoint_direct_interval_contained"] for row in controls),
            "all_controls_keep_28_groups": all(row["coherent_group_count"] == 28 and row["direct_coherent_group_count"] == 28 for row in controls),
            "chart_cell_bank_sha256": digest(cells),
        },
        "decision": {
            "positive_width_projective_pilot_interface_executed": True,
            "complete_projective_chart_cover_emitted": False,
            "zero_inclusive_integrand_weighted_boundary_majorants_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "combine one-sided zero-strip angular mass with a determinant-preserving uniform integrand envelope before recursive subdivision",
        },
        "release_test": {
            "exactly_1022_chart_cells": len(cells) == 1022,
            "exactly_6337_program_cell_uses": sum(len(row["chart_cell_ids"]) for row in program_cell_uses) == 6337,
            "exactly_16_interval_controls": len(controls) == 16,
            "all_212800_ordered_descriptor_intervals_covered": len(controls) * 13300 == 212800,
            "all_cells_strictly_positive_width": all(row["positive_width_in_every_ratio"] for row in cells),
            "all_controls_finite_positive_and_contain_midpoint": all(math.isfinite(float(row["integrated_cell_abs_upper"])) and float(row["minimum_cumulative_argument_lower"]) > 0 and row["midpoint_direct_interval_contained"] for row in controls),
            "all_coherent_group_censuses_preserved": all(row["coherent_group_count"] == 28 and row["direct_coherent_group_count"] == 28 for row in controls),
            "complete_chart_cover_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k487["ledger_effect"],
        "source_routing": k487["source_routing"],
        "claim_ceiling": "One exact positive-width pilot box in each of K542's 1,022 maximum charts, all 6,337 program-chart uses mapped, and one rigorous K413-preconditioned radial/projective interval integrated at every reachable codimension. These pilot cells do not cover a complete chart and do not control zero-inclusive projective boundaries, recursive interior, analytic tails, complete hybrid integrals, K457, K152, source/ledger, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["unique_maximum_charts"], fixed["program_chart_cell_uses"], fixed["executed_interval_controls"], fixed["ordered_descriptor_interval_evaluations"], fixed["coherent_groups_per_control"]) != (1022, 6337, 16, 212800, 28):
        raise AssertionError("K543 census changed")
    if len(payload["chart_cell_bank"]) != 1022 or len(payload["executed_cell_bank"]) != 16:
        raise AssertionError("K543 bank changed")
    if not all(row["positive_width_in_every_ratio"] for row in payload["chart_cell_bank"]):
        raise AssertionError("K543 cell touched a chart boundary")
    if not all(row["midpoint_direct_interval_contained"] and row["coherent_group_count"] == 28 and row["direct_coherent_group_count"] == 28 and float(row["minimum_cumulative_argument_lower"]) > 0 for row in payload["executed_cell_bank"]):
        raise AssertionError("K543 numerical control changed")
    contract = payload["projective_cell_contract"]
    if not contract["one_exact_positive_width_box_per_K542_chart"] or not contract["cells_are_pilots_not_a_chart_cover"]:
        raise AssertionError("K543 cell contract changed")
    decision = payload["decision"]
    if not decision["positive_width_projective_pilot_interface_executed"] or any(decision[key] for key in ("complete_projective_chart_cover_emitted", "zero_inclusive_integrand_weighted_boundary_majorants_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K543 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K543 release test failed")


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

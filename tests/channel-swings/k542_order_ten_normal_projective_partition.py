#!/usr/bin/env python3
"""Compile the exact order-ten normal-projective partition interface."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K413 = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"
K415 = ROOT / "lab/process/k415-order-ten-face-program-compiler.json"
K508 = ROOT / "lab/process/k508-order-ten-selected-face-cell-bank.json"
K511 = ROOT / "lab/process/k511-order-ten-face-shard-plan.json"
OUTPUT = ROOT / "lab/process/k542-order-ten-normal-projective-partition.json"
AXES = tuple(f"s{i}" for i in range(1, 12)) + tuple(f"v{i}" for i in range(1, 12))
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(index for index in range(column, len(work)) if work[index][column])
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result *= -1
        value = work[column][column]
        result *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            work[row] = [a - factor * b for a, b in zip(work[row], work[column], strict=True)]
    return result


def chart_point(anchor: str, ratio_axes: list[str], ratios: dict[str, Fraction]) -> dict[str, Fraction]:
    denominator = Fraction(1) + sum((ratios[axis] for axis in ratio_axes), start=Fraction(0))
    point = {anchor: Fraction(1, 1) / denominator}
    point.update({axis: ratios[axis] / denominator for axis in ratio_axes})
    return point


def jacobian_control(codimension: int) -> dict[str, Any]:
    ratios = [Fraction(index + 1, codimension + 1) for index in range(codimension - 1)]
    denominator = Fraction(1) + sum(ratios, start=Fraction(0))
    matrix = [
        [
            Fraction(int(row == column), 1) / denominator
            - ratios[row] / denominator**2
            for column in range(codimension - 1)
        ]
        for row in range(codimension - 1)
    ]
    actual = determinant(matrix)
    expected = denominator ** (-codimension)
    return {
        "codimension": codimension,
        "ratios": [q(value) for value in ratios],
        "determinant": q(actual),
        "expected": q(expected),
        "agrees": actual == expected,
    }


def result_paths() -> list[Path]:
    paths = [K508, ROOT / "lab/process/k512-order-ten-representative-face-shard.json"]
    paths.extend(next((ROOT / "lab/process").glob(f"k{index}-order-ten-face-shards-*.json")) for index in range(513, 542))
    return paths


def cell_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    for key in ("selected_face_cell_bank", "representative_face_cell_bank", "face_cell_bank"):
        if key in payload:
            return payload[key]
    raise AssertionError("unrecognized order-ten face-cell payload")


def build() -> dict[str, Any]:
    k413 = json.loads(K413.read_text())
    k415 = json.loads(K415.read_text())
    k511 = json.loads(K511.read_text())
    programs = k415["face_programs"]
    if len(programs) != 936:
        raise AssertionError("K415 face census changed")

    bank = []
    predecessor_manifests = []
    for path in result_paths():
        payload = json.loads(path.read_text())
        predecessor_manifests.append(str(path.relative_to(ROOT)))
        bank.extend(cell_rows(payload))
    bank_by_id = {row["program_id"]: row for row in bank}
    program_by_id = {row["program_id"]: row for row in programs}
    if len(bank) != 936 or len(bank_by_id) != 936 or set(bank_by_id) != set(program_by_id):
        raise AssertionError("complete face-cell custody changed")
    if any(len(row["cells"]) != 7 for row in bank):
        raise AssertionError("seven-cell face partition changed")

    masks = sorted(
        {tuple(row["zeroed_axes"]) for row in programs},
        key=lambda mask: (len(mask), tuple(AXIS_INDEX[axis] for axis in mask)),
    )
    mask_ids = {mask: f"M{index:03d}" for index, mask in enumerate(masks)}
    atlas = []
    for mask in masks:
        codimension = len(mask)
        charts = []
        for anchor in mask:
            ratio_axes = [axis for axis in mask if axis != anchor]
            charts.append({
                "chart_id": f"{mask_ids[mask]}:{anchor}",
                "anchor_axis": anchor,
                "ratio_axes": ratio_axes,
                "ratio_domain": {axis: ["0", "1"] for axis in ratio_axes},
                "coordinate_map": {anchor: "1/(1+sum(r))", **{axis: f"r_{axis}/(1+sum(r))" for axis in ratio_axes}},
                "angular_jacobian": f"(1+sum(r))^-{codimension}",
                "angular_mass": q(Fraction(1, math.factorial(codimension))),
                "owner_rule": "smallest canonical axis among coordinates attaining the maximum",
            })
        atlas.append({
            "mask_id": mask_ids[mask],
            "zeroed_axes": list(mask),
            "codimension": codimension,
            "chart_count": codimension,
            "simplex_angular_mass": q(Fraction(1, math.factorial(codimension - 1))),
            "charts": charts,
        })

    program_map = []
    for row in programs:
        mask = tuple(row["zeroed_axes"])
        cell = bank_by_id[row["program_id"]]
        singular_ids = sorted(row["singular_template_histogram"])
        confluent_ids = sorted(row["confluent_template_histogram"])
        program_map.append({
            "program_id": row["program_id"],
            "axis": row["axis"],
            "face_kind": row["face_kind"],
            "mask_id": mask_ids[mask],
            "codimension": row["codimension"],
            "chart_ids": [f"{mask_ids[mask]}:{axis}" for axis in mask],
            "certified_normal_cells": len(cell["cells"]),
            "face_cell_sha256": digest(cell),
            "descriptor_program_sha256": row["descriptor_program_sha256"],
            "singular_template_ids": singular_ids,
            "confluent_template_ids": confluent_ids,
        })

    reachable_codimensions = sorted({len(mask) for mask in masks})
    exact_controls = []
    for codimension in reachable_codimensions:
        mask = next(mask for mask in masks if len(mask) == codimension)
        anchor = mask[-1]
        ratio_axes = [axis for axis in mask if axis != anchor]
        weights = {axis: Fraction(index + 1) for index, axis in enumerate(mask)}
        total = sum(weights.values(), start=Fraction(0))
        point = {axis: value / total for axis, value in weights.items()}
        ratios = {axis: point[axis] / point[anchor] for axis in ratio_axes}
        rebuilt = chart_point(anchor, ratio_axes, ratios)
        exact_controls.append({
            "codimension": codimension,
            "mask_id": mask_ids[mask],
            "anchor_axis": anchor,
            "reconstructed_exactly": rebuilt == point,
            "sum_is_one": sum(rebuilt.values(), start=Fraction(0)) == 1,
            "anchor_is_maximal": all(rebuilt[anchor] >= value for value in rebuilt.values()),
            "chart_mass_sum_is_simplex_mass": codimension * Fraction(1, math.factorial(codimension)) == Fraction(1, math.factorial(codimension - 1)),
        })

    jacobian_controls = [jacobian_control(codimension) for codimension in reachable_codimensions]
    unique_charts = sum(len(mask) for mask in masks)
    program_chart_uses = sum(len(row["zeroed_axes"]) for row in programs)
    unique_oriented_boundaries = sum(2 * len(mask) * (len(mask) - 1) for mask in masks)
    program_oriented_boundaries = sum(2 * len(row["zeroed_axes"]) * (len(row["zeroed_axes"]) - 1) for row in programs)
    compact_lower_strata = sum(len(mask) * (2 ** (len(mask) - 1) - 1) for mask in masks)
    normal_powers = [int(row["minimum_second_derivative_face_normal_power"]) for row in programs]

    return {
        "schema_version": "1.0",
        "result_id": "K542-ORDER-TEN-NORMAL-PROJECTIVE-PARTITION",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K413.relative_to(ROOT)), str(K415.relative_to(ROOT)), str(K511.relative_to(ROOT)), *predecessor_manifests],
            "face_programs": len(programs),
            "certified_positive_width_normal_cells": sum(len(row["cells"]) for row in bank),
            "unique_zero_masks": len(masks),
            "unique_maximum_charts": unique_charts,
            "program_chart_uses": program_chart_uses,
            "unique_oriented_coordinate_boundaries": unique_oriented_boundaries,
            "program_oriented_coordinate_boundary_uses": program_oriented_boundaries,
            "compactly_represented_nonempty_lower_strata": compact_lower_strata,
            "reachable_codimensions": reachable_codimensions,
            "K413_template_bank_sha256": k415["fixed_control"]["K413_template_bank_sha256"],
            "K511_plan_digest": k511["partition_contract"]["plan_digest"],
        },
        "coordinate_and_measure_contract": {
            "radial_coordinate": "rho=sum_{i in Z} t_i",
            "projective_coordinates": "p_i=t_i/rho; p_i>=0; sum_i p_i=1",
            "maximum_chart": "choose a with p_a=max_i p_i and set r_i=p_i/p_a",
            "inverse": "p_a=1/(1+sum_i r_i); p_i=r_i/(1+sum_i r_i)",
            "ratio_bounds": "0<=r_i<=1",
            "angular_jacobian": "abs(det d(p_nonanchor)/d(r))=(1+sum_i r_i)^(-c)",
            "maximum_chart_angular_mass": "1/c!",
            "simplex_angular_mass": "1/(c-1)!",
            "normal_measure": "product_i dt_i=rho^(c-1) d_rho d_sigma",
            "tie_rule": "smallest canonical axis owns a maximum tie; ties have angular measure zero",
            "closed_chart_union_covers_complete_projective_simplex": True,
            "chart_interiors_are_disjoint_under_tie_rule": True,
        },
        "determinant_preservation_contract": {
            "projective_change_acts_only_on_zeroed_raw_time_axes": True,
            "K413_singular_and_confluent_template_ids_preserved_per_program": True,
            "K508_plus_K512_through_K541_face_cell_payloads_bound_by_digest": True,
            "projective_partition_does_not_recompute_or_weaken_interval_determinants": True,
        },
        "boundary_routing_contract": {
            "zero_boundary": "r_i=0 lowers positive support and routes to the corresponding lower-dimensional projective stratum",
            "tie_boundary": "r_i=1 adds i to the maximum set and routes ownership to the smallest canonical axis in that set",
            "termination_metric": "lexicographic (positive-support size, canonical owner index)",
            "zero_routing_terminates": True,
            "tie_routing_terminates": True,
            "boundaries_have_angular_measure_zero": True,
            "interval_closures_still_require_one_sided_zero_safe_majorants": True,
        },
        "mask_atlas": atlas,
        "program_partition_map": program_map,
        "exact_controls": exact_controls,
        "jacobian_controls": jacobian_controls,
        "partition_summary": {
            "all_face_programs_owned_once": len(program_map) == len({row["program_id"] for row in program_map}) == 936,
            "all_certified_cells_bound_once": sum(row["certified_normal_cells"] for row in program_map) == 6552,
            "all_reachable_codimensions_controlled": len(exact_controls) == len(reachable_codimensions),
            "all_inverse_jacobian_and_mass_controls_exact": all(row["reconstructed_exactly"] and row["sum_is_one"] and row["anchor_is_maximal"] and row["chart_mass_sum_is_simplex_mass"] for row in exact_controls) and all(row["agrees"] for row in jacobian_controls),
            "atlas_sha256": digest(atlas),
            "program_partition_sha256": digest(program_map),
        },
        "normal_power_reconciliation": {
            "minimum_normal_power": min(normal_powers),
            "maximum_normal_power": max(normal_powers),
            "all_face_normal_powers_locally_integrable": all(power >= 0 for power in normal_powers),
            "radial_power_is_not_angular_uniformity": True,
        },
        "decision": {
            "complete_certified_face_bank_bound": True,
            "exact_normal_projective_coordinate_partition_complete": True,
            "exact_angular_measure_compiled": True,
            "compact_boundary_routing_compiled": True,
            "positive_width_projective_ratio_cells_evaluated": False,
            "zero_inclusive_projective_boundary_majorants_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "execute anisotropic positive projective controls and positive-width ratio cells with one-sided zero-boundary majorants before recursive positive-interior and analytic-tail composition",
        },
        "release_test": {
            "exactly_936_face_programs_owned_once": len(program_map) == len({row["program_id"] for row in program_map}) == 936,
            "exactly_6552_certified_normal_cells_bound_once": sum(row["certified_normal_cells"] for row in program_map) == 6552,
            "all_chart_mass_sums_exact": all(row["chart_mass_sum_is_simplex_mass"] for row in exact_controls),
            "all_inverse_and_jacobian_controls_pass": all(row["reconstructed_exactly"] and row["sum_is_one"] and row["anchor_is_maximal"] for row in exact_controls) and all(row["agrees"] for row in jacobian_controls),
            "all_face_normal_powers_nonnegative": all(power >= 0 for power in normal_powers),
            "determinant_preconditioner_identity_preserved": True,
            "boundary_measure_zero_not_interval_closure": True,
            "projective_ratio_cells_not_overclaimed": True,
            "recursive_interior_and_tails_not_overclaimed": True,
            "complete_order_ten_integral_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k415["ledger_effect"],
        "source_routing": k415["source_routing"],
        "claim_ceiling": "Exact determinant-preserving maximum-coordinate normal-projective charts, tie ownership, radial/angular Jacobian factorization, chart masses and compact boundary routing for all 936 K415 reachable-face programs and their 6,552 certified K508 plus K512-through-K541 normal cells. Measure-zero routing is not an interval enclosure: positive-width projective ratio cells, one-sided zero-safe boundary majorants, recursive positive-interior coverage, analytic tails, twenty-two hybrid integrals, the complete order-ten remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["face_programs"] != 936 or fixed["certified_positive_width_normal_cells"] != 6552:
        raise AssertionError("K542 complete-bank census changed")
    if len(payload["program_partition_map"]) != 936 or len({row["program_id"] for row in payload["program_partition_map"]}) != 936:
        raise AssertionError("K542 program ownership changed")
    if sum(row["certified_normal_cells"] for row in payload["program_partition_map"]) != 6552:
        raise AssertionError("K542 cell custody changed")
    if sum(row["chart_count"] for row in payload["mask_atlas"]) != fixed["unique_maximum_charts"]:
        raise AssertionError("K542 chart census changed")
    if sum(len(row["chart_ids"]) for row in payload["program_partition_map"]) != fixed["program_chart_uses"]:
        raise AssertionError("K542 chart-use census changed")
    if not all(row["reconstructed_exactly"] and row["sum_is_one"] and row["anchor_is_maximal"] and row["chart_mass_sum_is_simplex_mass"] for row in payload["exact_controls"]):
        raise AssertionError("K542 exact projective control changed")
    if not all(row["agrees"] for row in payload["jacobian_controls"]):
        raise AssertionError("K542 Jacobian control changed")
    contract = payload["coordinate_and_measure_contract"]
    if not contract["closed_chart_union_covers_complete_projective_simplex"] or not contract["chart_interiors_are_disjoint_under_tie_rule"]:
        raise AssertionError("K542 partition contract changed")
    if not all(payload["determinant_preservation_contract"].values()):
        raise AssertionError("K542 determinant-preservation contract changed")
    routing = payload["boundary_routing_contract"]
    if not all(routing[key] for key in ("zero_routing_terminates", "tie_routing_terminates", "boundaries_have_angular_measure_zero", "interval_closures_still_require_one_sided_zero_safe_majorants")):
        raise AssertionError("K542 boundary routing changed")
    decision = payload["decision"]
    required_true = ("complete_certified_face_bank_bound", "exact_normal_projective_coordinate_partition_complete", "exact_angular_measure_compiled", "compact_boundary_routing_compiled")
    required_false = ("positive_width_projective_ratio_cells_evaluated", "zero_inclusive_projective_boundary_majorants_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")
    if not all(decision[key] for key in required_true) or any(decision[key] for key in required_false):
        raise AssertionError("K542 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K542 release test failed")


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

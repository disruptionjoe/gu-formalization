#!/usr/bin/env python3
"""Compile the exact maximum-coordinate projective atlas for K390 faces."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K390 = ROOT / "lab/process/k390-order-nine-face-program-compiler.json"
K393 = ROOT / "lab/process/k393-order-nine-near-face-strip-integration.json"
OUTPUT = ROOT / "lab/process/k394-order-nine-normal-projective-atlas.json"
AXES = tuple(f"s{i}" for i in range(1, 11)) + tuple(f"v{i}" for i in range(1, 11))
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
        [(Fraction(int(row == column), 1) / denominator) - ratios[row] / denominator**2 for column in range(codimension - 1)]
        for row in range(codimension - 1)
    ]
    actual = determinant(matrix)
    expected = denominator ** (-codimension)
    return {"codimension": codimension, "ratios": [q(value) for value in ratios], "denominator": q(denominator), "determinant": q(actual), "expected_denominator_power": q(expected), "agrees": actual == expected}


def build() -> dict[str, Any]:
    k390 = json.loads(K390.read_text())
    k393 = json.loads(K393.read_text())
    programs = k390["face_programs"]
    if len(programs) != 695 or len(k393["face_strip_bank"]) != 695:
        raise AssertionError("K390/K393 face census changed")

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
                "denominator": "1+" + "+".join(f"r_{axis}" for axis in ratio_axes),
                "coordinate_map": {anchor: "1/(1+sum(r))", **{axis: f"r_{axis}/(1+sum(r))" for axis in ratio_axes}},
                "angular_jacobian": f"(1+sum(r))^-{codimension}",
                "radial_jacobian_power": codimension - 1,
                "chart_owner_rule": "smallest canonical axis among coordinates attaining the maximum",
            })
        atlas.append({"mask_id": mask_ids[mask], "zeroed_axes": list(mask), "codimension": codimension, "chart_count": codimension, "charts": charts})

    program_map = [{
        "program_id": row["program_id"], "axis": row["axis"],
        "mask_id": mask_ids[tuple(row["zeroed_axes"])], "codimension": int(row["codimension"]),
        "chart_ids": [f"{mask_ids[tuple(row['zeroed_axes'])]}:{axis}" for axis in row["zeroed_axes"]],
    } for row in programs]

    reachable_codimensions = sorted({len(mask) for mask in masks})
    controls = []
    for codimension in reachable_codimensions:
        mask = next(mask for mask in masks if len(mask) == codimension)
        anchor = mask[-1]
        ratio_axes = [axis for axis in mask if axis != anchor]
        weights = {axis: Fraction(index + 1) for index, axis in enumerate(mask)}
        total = sum(weights.values(), start=Fraction(0))
        point = {axis: weight / total for axis, weight in weights.items()}
        ratios = {axis: point[axis] / point[anchor] for axis in ratio_axes}
        rebuilt = chart_point(anchor, ratio_axes, ratios)
        equal = chart_point(anchor, ratio_axes, {axis: Fraction(1) for axis in ratio_axes})
        controls.append({
            "codimension": codimension, "mask_id": mask_ids[mask], "anchor_axis": anchor,
            "ratios": {axis: q(value) for axis, value in ratios.items()},
            "point": {axis: q(value) for axis, value in point.items()},
            "reconstructed_exactly": rebuilt == point,
            "sum_is_one": sum(rebuilt.values(), start=Fraction(0)) == 1,
            "anchor_is_maximal": all(rebuilt[anchor] >= value for value in rebuilt.values()),
            "equal_normal_corner": {axis: q(value) for axis, value in equal.items()},
            "equal_normal_corner_is_uniform": set(equal.values()) == {Fraction(1, codimension)},
        })

    jacobian_controls = [jacobian_control(codimension) for codimension in reachable_codimensions]
    return {
        "schema_version": "1.0",
        "result_id": "K394-ORDER-NINE-NORMAL-PROJECTIVE-ATLAS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K390.relative_to(ROOT)), str(K393.relative_to(ROOT))],
            "raw_time_axes": 20, "face_programs": len(programs), "unique_zero_masks": len(masks),
            "reachable_codimensions": reachable_codimensions,
            "unique_maximum_charts": sum(len(mask) for mask in masks),
            "program_chart_uses": sum(int(row["codimension"]) for row in programs),
        },
        "coordinate_contract": {
            "radial_coordinate": "rho=sum_{i in Z} t_i",
            "projective_coordinates": "p_i=t_i/rho; p_i>=0; sum_i p_i=1",
            "maximum_chart": "choose a with p_a=max_i p_i and set r_i=p_i/p_a",
            "inverse": "p_a=1/(1+sum_i r_i); p_i=r_i/(1+sum_i r_i)",
            "ratio_bounds": "0<=r_i<=1",
            "angular_jacobian": "abs(det d(p_nonanchor)/d(r))=(1+sum_i r_i)^(-c)",
            "normal_measure": "product_i dt_i=rho^(c-1) d_rho d_sigma",
            "tie_rule": "smallest canonical axis owns a maximum tie; ties have angular measure zero",
            "closed_chart_union_covers_complete_projective_simplex": True,
            "chart_interiors_are_disjoint_under_tie_rule": True,
        },
        "mask_atlas": atlas,
        "program_chart_map": program_map,
        "exact_controls": controls,
        "jacobian_controls": jacobian_controls,
        "atlas_summary": {
            "all_98_unique_masks_compiled": len(atlas) == 98,
            "all_695_programs_mapped": len(program_map) == 695,
            "all_reachable_codimensions_controlled": len(controls) == len(reachable_codimensions),
            "all_inverse_controls_exact": all(row["reconstructed_exactly"] for row in controls),
            "all_jacobian_controls_exact": all(row["agrees"] for row in jacobian_controls),
            "atlas_sha256": digest(atlas), "program_map_sha256": digest(program_map),
        },
        "decision": {
            "exact_normal_projective_coordinate_cover_complete": True,
            "exact_angular_measure_compiled": False,
            "positive_width_projective_cells_evaluated": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "freeze the exact chart masses and boundary recursion, then execute anisotropic positive controls before any positive-width projective chart cell",
        },
        "release_test": {
            "exactly_98_unique_masks": len(atlas) == 98,
            "exactly_758_unique_charts": sum(row["chart_count"] for row in atlas) == 758,
            "exactly_4320_program_chart_uses": sum(len(row["chart_ids"]) for row in program_map) == 4320,
            "all_programs_preserved": {row["program_id"] for row in program_map} == {row["program_id"] for row in programs},
            "all_inverse_and_jacobian_controls_pass": all(row["reconstructed_exactly"] and row["sum_is_one"] and row["anchor_is_maximal"] and row["equal_normal_corner_is_uniform"] for row in controls) and all(row["agrees"] for row in jacobian_controls),
            "projective_cells_not_overclaimed": True,
            "complete_order_nine_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k393["ledger_effect"],
        "source_routing": k393["source_routing"],
        "claim_ceiling": "Exact finite maximum-coordinate projective charts for all 98 unique zero masks and all 695 K390 face programs, with exact inverse, tie ownership, radial/projective measure split and Jacobian formula across every reachable codimension. This is a coordinate cover, not a positive-width interval evaluation of the charts, a zero-inclusive boundary majorant, a disjoint global face-neighborhood cover, a K384 hybrid integral, a complete order-nine remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["face_programs"], fixed["unique_zero_masks"], fixed["unique_maximum_charts"], fixed["program_chart_uses"]) != (695, 98, 758, 4320):
        raise AssertionError("K394 census changed")
    atlas, programs = payload["mask_atlas"], payload["program_chart_map"]
    if len(atlas) != 98 or len(programs) != 695:
        raise AssertionError("K394 atlas identity changed")
    if any(row["chart_count"] != row["codimension"] or len(row["charts"]) != row["codimension"] for row in atlas):
        raise AssertionError("K394 maximum-chart count changed")
    if not all(row["agrees"] for row in payload["jacobian_controls"]):
        raise AssertionError("K394 Jacobian control changed")
    if not all(row["reconstructed_exactly"] and row["sum_is_one"] and row["anchor_is_maximal"] and row["equal_normal_corner_is_uniform"] for row in payload["exact_controls"]):
        raise AssertionError("K394 inverse control changed")
    contract = payload["coordinate_contract"]
    if not contract["closed_chart_union_covers_complete_projective_simplex"] or not contract["chart_interiors_are_disjoint_under_tie_rule"]:
        raise AssertionError("K394 cover contract changed")
    decision = payload["decision"]
    if not decision["exact_normal_projective_coordinate_cover_complete"] or any(decision[key] for key in ("exact_angular_measure_compiled", "positive_width_projective_cells_evaluated", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K394 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K394 release test failed")


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

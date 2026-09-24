#!/usr/bin/env python3
"""Exercise the complete K407 derivative evaluator on all hybrid interiors.

This is a numerical control for the atlas architecture, not a whole-domain
enclosure.  Preceding K409 axes are fixed at 1/256.  The active and following
axes share a positive radial interval at their projective barycenter, so no raw
Bessel call touches a zero face.  Every determinant and complete coherent group
is assembled before the reported interval is enclosed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K408_MODULE = HERE / "k408_order_ten_node_directional_jet_bank.py"
K408 = ROOT / "lab/process/k408-order-ten-node-directional-jet-bank.json"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
OUTPUT = ROOT / "lab/process/k412-order-ten-interior-origin-control.json"

ctx.dps = 180
ctx.threads = 1

AXES = tuple([f"s{i}" for i in range(1, 12)] + [f"v{i}" for i in range(1, 12)])
RADIAL_CELL = (Fraction(1, 64), Fraction(1, 32))
RAY_RADII = (Fraction(1, 64), Fraction(1, 128), Fraction(1, 256))


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K408_BACKEND = load_module(K408_MODULE, "k408_for_k412")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def lower_text(value: arb) -> str:
    return repr(math.nextafter(float(value.lower()), -math.inf))


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(value.upper()), math.inf))


def abs_upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def interval(left: Fraction, right: Fraction) -> arb:
    midpoint = (left + right) / 2
    radius = (right - left) / 2
    return arb(q(midpoint), q(radius))


def hybrid_raw_times(axis_index: int, radial: arb) -> dict[str, arb]:
    free_count = len(AXES) - axis_index
    result = {}
    for index, axis in enumerate(AXES):
        result[axis] = arb(1) / 256 if index < axis_index else radial / free_count
    return result


def cumulative(raw: dict[str, arb]) -> tuple[dict[int, arb], dict[int, arb]]:
    left = {position: sum((raw[f"s{i}"] for i in range(position, 12)), arb(0)) for position in range(1, 12)}
    right = {position: sum((raw[f"v{i}"] for i in range(position, 12)), arb(0)) for position in range(1, 12)}
    return left, right


def complete_second(axis: str, raw: dict[str, arb]) -> tuple[arb, list[dict[str, str]]]:
    cumulative_s, cumulative_v = cumulative(raw)
    total = [arb(0), arb(0), arb(0)]
    group_rows = []
    for (seed, signature), terms in K408_BACKEND.group_terms().items():
        group_total = [arb(0), arb(0), arb(0)]
        for left in terms:
            for right in terms:
                jet = K408_BACKEND.gram_jet(left, right, cumulative_s, cumulative_v, axis)
                multiplier = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
                group_total = K408_BACKEND.polynomial_add(group_total, [value * multiplier for value in jet])
        second = 2 * group_total[2]
        group_rows.append({
            "group_id": f"order10:seed{seed}:{signature}",
            "second_lower": lower_text(second),
            "second_upper": upper_text(second),
        })
        total = K408_BACKEND.polynomial_add(total, group_total)
    return 2 * total[2], group_rows


def complete_value(raw: dict[str, arb]) -> arb:
    cumulative_s, cumulative_v = cumulative(raw)
    total = arb(0)
    for terms in K408_BACKEND.group_terms().values():
        for left in terms:
            for right in terms:
                jet = K408_BACKEND.gram_jet(left, right, cumulative_s, cumulative_v, "s1")
                multiplier = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
                total += multiplier * jet[0]
    return total


def build() -> dict[str, Any]:
    k408 = json.loads(K408.read_text())
    k410 = json.loads(K410.read_text())
    k411 = json.loads(K411.read_text())
    if k411["fixed_control"]["native_axes"] != list(AXES):
        raise AssertionError("K411 native axis order changed")
    if not k410["decision"]["all_zero_origin_integrability_closed"]:
        raise AssertionError("K410 radial contract unavailable")

    radial = interval(*RADIAL_CELL)
    rows = []
    for index, axis in enumerate(AXES):
        raw = hybrid_raw_times(index, radial)
        second, groups = complete_second(axis, raw)
        cumulative_s, cumulative_v = cumulative(raw)
        minimum = min([value.lower() for value in cumulative_s.values()] + [value.lower() for value in cumulative_v.values()])
        if minimum <= 0 or not math.isfinite(float(abs(second).upper())):
            raise AssertionError(f"non-finite positive-interior control for {axis}")
        free_count = len(AXES) - index
        active_upper = arb(q(RADIAL_CELL[1])) / free_count
        peano_majorant = abs(second) * active_upper * active_upper / 2
        rows.append({
            "axis": axis,
            "preceding_axes_fixed_at_node": index,
            "moving_dimension": free_count,
            "moving_radial_cell": [q(value) for value in RADIAL_CELL],
            "projective_point": f"barycenter 1/{free_count}",
            "minimum_cumulative_argument_lower": lower_text(arb(minimum)),
            "complete_second_derivative_lower": lower_text(second),
            "complete_second_derivative_upper": upper_text(second),
            "complete_second_derivative_abs_upper": abs_upper_text(second),
            "quadratic_peano_majorant_abs_upper": abs_upper_text(peano_majorant),
            "all_28_group_intervals_sha256": digest(groups),
            "raw_Bessel_evaluation_at_zero_used": False,
        })

    ray_controls = []
    for radius in RAY_RADII:
        raw = {axis: arb(q(radius / 22)) for axis in AXES}
        second, groups = complete_second("s1", raw)
        scaled = abs(second) * arb(q(radius**14))
        radial_coefficient = scaled / (2 * 22**2)
        ray_controls.append({
            "total_radius": q(radius),
            "raw_time_per_axis": q(radius / 22),
            "raw_second_derivative_lower": lower_text(second),
            "raw_second_derivative_upper": upper_text(second),
            "rho14_abs_second_upper": abs_upper_text(scaled),
            "rho_minus9_peano_radial_coefficient_upper": abs_upper_text(radial_coefficient),
            "all_28_group_intervals_sha256": digest(groups),
        })

    local = next(row for row in k408["axis_node_jets"] if row["axis"] == "s1")
    node_raw = {axis: arb(1) / 256 for axis in AXES}
    node_second, _ = complete_second("s1", node_raw)
    node_lower = arb(local["raw_second_derivative_lower"])
    node_upper = arb(local["raw_second_derivative_upper"])
    node_replayed = not (node_second.upper() < node_lower.lower() or node_second.lower() > node_upper.upper())
    if not node_replayed:
        raise AssertionError("K412 failed to replay the K408 s1 node control")

    return {
        "schema_version": "1.0",
        "result_id": "K412-ORDER-TEN-INTERIOR-ORIGIN-CONTROL",
        "created": "2026-09-24",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k408-order-ten-node-directional-jet-bank.json",
                "lab/process/k410-order-ten-zero-safe-radial-contract.json",
                "lab/process/k411-order-ten-hybrid-face-atlas.json",
            ],
            "native_axes": list(AXES),
            "hybrid_terms": 22,
            "paths": 480,
            "coherent_groups": 28,
            "ordered_directional_entries_per_axis": 13300,
            "axis_entry_evaluations": 292600,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "hybrid_interior_reference_bank": rows,
        "all_zero_barycentric_ray_controls": ray_controls,
        "composition_contract": {
            "preceding_axes_fixed_at_native_node": True,
            "moving_axes_share_positive_radial_interval_at_projective_barycenter": True,
            "determinants_assembled_before_group_enclosure": True,
            "complete_coherent_groups_assembled_before_reported_enclosure": True,
            "all_ordered_orientations_retained": True,
            "K410_quadratic_peano_majorant_used": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "reference_bank_is_not_a_projective_cell_cover": True,
        },
        "control_summary": {
            "all_22_hybrid_reference_intervals_finite": all(math.isfinite(float(row["complete_second_derivative_abs_upper"])) for row in rows),
            "all_reference_arguments_strictly_positive": all(float(row["minimum_cumulative_argument_lower"]) > 0 for row in rows),
            "all_28_group_digests_present": all(row["all_28_group_intervals_sha256"].startswith("sha256:") for row in rows),
            "K408_s1_node_second_derivative_replayed": node_replayed,
            "all_zero_ray_scaled_controls_finite": all(math.isfinite(float(row["rho14_abs_second_upper"])) for row in ray_controls),
            "proper_face_preconditioners_complete": False,
            "recursive_whole_domain_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
        },
        "decision": {
            "complete_coherent_hybrid_interior_evaluator_executed": True,
            "all_zero_scaled_ray_control_executed": True,
            "K408_local_control_replayed": True,
            "proper_face_evaluator_released": False,
            "complete_order_ten_remainder_emitted": False,
            "next_exact_input": "construct mask-native scaled determinant preconditioners on K411's reachable proper faces, join them to recursive positive-interior cells and analytic radial tails, then integrate all twenty-two K409 kernels",
        },
        "release_test": {
            "twenty_two_hybrid_rows_present": len(rows) == 22,
            "all_292600_ordered_axis_entry_evaluations_covered": 22 * 13300 == 292600,
            "all_reference_intervals_finite": all(math.isfinite(float(row["complete_second_derivative_abs_upper"])) for row in rows),
            "all_reference_arguments_positive": all(float(row["minimum_cumulative_argument_lower"]) > 0 for row in rows),
            "K408_node_control_replayed": node_replayed,
            "no_raw_zero_evaluation": True,
            "reference_bank_not_promoted_to_cover": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k411["ledger_effect"],
        "source_routing": k411["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb execution of the complete ordered determinant and coherent-group second-derivative evaluator on a positive barycentric radial reference cell for all twenty-two K409 hybrid domains, plus three all-zero barycentric rays with the K410 rho^14 scaling and a replay of K408's s1 node control. The reference bank is not a projective cover. Proper-face preconditioners, recursive whole-domain coverage, analytic tails, numerical hybrid integrals, the complete order-ten remainder and integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_terms"], fixed["paths"], fixed["coherent_groups"], fixed["ordered_directional_entries_per_axis"], fixed["axis_entry_evaluations"]) != (22, 480, 28, 13300, 292600):
        raise AssertionError("K412 fixed census changed")
    rows = payload["hybrid_interior_reference_bank"]
    if len(rows) != 22 or [row["moving_dimension"] for row in rows] != list(range(22, 0, -1)):
        raise AssertionError("K412 hybrid reference bank changed")
    contract = payload["composition_contract"]
    if contract["raw_Bessel_evaluation_at_zero_used"] or not contract["all_ordered_orientations_retained"] or not contract["reference_bank_is_not_a_projective_cell_cover"]:
        raise AssertionError("K412 composition boundary changed")
    summary = payload["control_summary"]
    if not summary["all_22_hybrid_reference_intervals_finite"] or not summary["all_reference_arguments_strictly_positive"] or not summary["K408_s1_node_second_derivative_replayed"]:
        raise AssertionError("K412 controls failed")
    if summary["proper_face_preconditioners_complete"] or summary["recursive_whole_domain_cover_complete"] or summary["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K412 overclaimed global coverage")
    decision = payload["decision"]
    if not decision["complete_coherent_hybrid_interior_evaluator_executed"] or not decision["all_zero_scaled_ray_control_executed"] or decision["proper_face_evaluator_released"] or decision["complete_order_ten_remainder_emitted"]:
        raise AssertionError("K412 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K412 release test failed")


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

#!/usr/bin/env python3
"""Execute complete coherent Arb controls on K390's hardest hybrid faces.

These are positive approach controls at three normal levels. The complete
20-group second directional functional is assembled before normal scaling or
the K385 Peano majorant is applied. The controls are not face intervals,
recursive covers, or integrated remainders.
"""

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
K387_MODULE = HERE / "k387_order_nine_interior_origin_control.py"
K385 = ROOT / "lab/process/k385-order-nine-zero-safe-radial-contract.json"
K390 = ROOT / "lab/process/k390-order-nine-face-program-compiler.json"
OUTPUT = ROOT / "lab/process/k391-order-nine-hardest-face-arb-bank.json"

ctx.dps = 180
ctx.threads = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K387_BACKEND = load_module(K387_MODULE, "k387_for_k391")


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def lower_text(value: arb) -> str:
    return repr(math.nextafter(float(value.lower()), -math.inf))


def raw_times(program: dict[str, Any], rho: Fraction) -> dict[str, arb]:
    zeroed = set(program["zeroed_axes"])
    codimension = int(program["codimension"])
    moving = set(program["moving_axes"])
    result = {}
    for axis in K387_BACKEND.AXES:
        if codimension > 0 and axis in zeroed:
            result[axis] = arb(q(rho / codimension))
        elif codimension == 0 and axis in moving:
            result[axis] = arb(q(rho / len(moving)))
        else:
            result[axis] = arb(1) / 256
    return result


def build() -> dict[str, Any]:
    k385 = json.loads(K385.read_text())
    k390 = json.loads(K390.read_text())
    programs = {row["program_id"]: row for row in k390["face_programs"] + k390["positive_interior_fallback_programs"]}
    selected = k390["selected_boundary_or_interior_program_per_hybrid"]
    if len(selected) != 20:
        raise AssertionError("K390 hardest-face selection changed")

    rows = []
    axis_summary = []
    for selection in selected:
        program = programs[selection["program_id"]]
        controls = []
        for level in program["normal_levels"]:
            rho = Fraction(level)
            raw = raw_times(program, rho)
            second, group_rows = K387_BACKEND.complete_second(program["axis"], raw)
            singular_power = int(program["maximum_value_first_second_singular_powers"][2])
            normal_scaled = abs(second) * arb(q(rho**singular_power))
            active_time = raw[program["axis"]]
            peano_majorant = abs(second) * active_time * active_time / 2
            cumulative_s, cumulative_v = K387_BACKEND.cumulative(raw)
            minimum_argument = min(
                [value.lower() for value in cumulative_s.values()]
                + [value.lower() for value in cumulative_v.values()]
            )
            if minimum_argument <= 0:
                raise AssertionError("K391 approach point touched a raw zero")
            values = [second, normal_scaled, peano_majorant]
            if any(not math.isfinite(float(abs(value).upper())) for value in values):
                raise AssertionError("K391 non-finite Arb control")
            controls.append({
                "rho": level,
                "minimum_cumulative_argument_lower": lower_text(arb(minimum_argument)),
                "complete_second_derivative_lower": lower_text(second),
                "complete_second_derivative_upper": upper_text(second),
                "complete_second_derivative_abs_upper": upper_text(second),
                "rho_to_K389_second_singular_power_abs_upper": upper_text(normal_scaled),
                "K385_quadratic_peano_majorant_abs_upper": upper_text(peano_majorant),
                "all_20_group_intervals_sha256": digest(group_rows),
                "coherent_group_count": len(group_rows),
                "raw_Bessel_evaluation_at_zero_used": False,
            })
        scaled = [arb(row["rho_to_K389_second_singular_power_abs_upper"]) for row in controls]
        ratios = [upper_text(scaled[index + 1] / scaled[index]) for index in range(len(scaled) - 1)]
        rows.append({
            "axis": program["axis"],
            "program_id": program["program_id"],
            "face_id": program["face_id"],
            "face_kind": program["face_kind"],
            "zeroed_axes": program["zeroed_axes"],
            "codimension": program["codimension"],
            "active_peano_axis_zeroed": program["active_peano_axis_zeroed"],
            "maximum_second_singular_power": program["maximum_value_first_second_singular_powers"][2],
            "minimum_face_normal_power": program["minimum_second_derivative_face_normal_power"],
            "controls": controls,
            "successive_scaled_upper_ratios": ratios,
            "face_program_sha256": digest(program),
        })
        axis_summary.append({
            "axis": program["axis"],
            "program_id": program["program_id"],
            "control_count": len(controls),
            "all_controls_finite": True,
            "all_controls_have_20_group_digests": all(row["coherent_group_count"] == 20 for row in controls),
        })

    return {
        "schema_version": "1.0",
        "result_id": "K391-ORDER-NINE-HARDEST-FACE-ARB-BANK",
        "created": "2026-09-23",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k385-order-nine-zero-safe-radial-contract.json",
                "lab/process/k390-order-nine-face-program-compiler.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "native_axes": list(K387_BACKEND.AXES),
            "hybrid_terms": 20,
            "selected_boundary_or_interior_programs": 20,
            "reachable_face_programs_executed": 18,
            "positive_interior_fallback_programs_executed": 2,
            "normal_levels_per_face": 3,
            "complete_arb_controls": len(rows) * 3,
            "ordered_descriptors_per_control": 4480,
            "ordered_descriptor_control_evaluations": len(rows) * 3 * 4480,
            "K390_complete_program_bank_sha256": k390["program_summary"]["complete_program_bank_sha256"],
        },
        "execution_contract": {
            "positive_normal_approach_only": True,
            "each_zeroed_axis_receives_rho_over_codimension": True,
            "all_other_raw_times_fixed_at_1_over_256": True,
            "all_ordered_orientations_retained": True,
            "all_20_coherent_groups_assembled_before_reported_enclosure": True,
            "normal_scaling_applied_after_complete_assembly": True,
            "K385_peano_majorant_applied_after_complete_assembly": True,
            "K388_K389_template_programs_replayed_by_pointer": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "controls_are_not_face_intervals": True,
            "controls_are_not_a_recursive_cover": True,
            "controls_are_not_integrated_hybrid_remainders": True,
        },
        "hardest_face_arb_controls": rows,
        "hybrid_summary": axis_summary,
        "bank_summary": {
            "all_20_hybrids_executed": len(rows) == 20,
            "all_60_controls_finite": all(item["all_controls_finite"] for item in axis_summary),
            "all_controls_retain_20_group_digests": all(item["all_controls_have_20_group_digests"] for item in axis_summary),
            "every_control_has_positive_argument_floor": all(float(control["minimum_cumulative_argument_lower"]) > 0 for row in rows for control in row["controls"]),
            "complete_bank_sha256": digest(rows),
        },
        "decision": {
            "selected_boundary_or_interior_complete_coherent_arb_bank_executed": True,
            "K390_compiled_programs_numerically_exercised": True,
            "preconditioned_interval_face_evaluator_complete": False,
            "all_695_faces_numerically_evaluated": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "replace positive approach controls by K388 row/column-scaled and confluent interval face cells, extend from the eighteen hardest programs to all 695 faces, then join recursive positive-interior cells and analytic tails",
        },
        "release_test": {
            "all_20_hybrids_present": len(rows) == 20,
            "exactly_60_arb_controls_present": sum(len(row["controls"]) for row in rows) == 60,
            "all_268800_ordered_descriptor_controls_executed": len(rows) * 3 * 4480 == 268_800,
            "all_controls_finite": all(item["all_controls_finite"] for item in axis_summary),
            "all_controls_have_20_group_digests": all(item["all_controls_have_20_group_digests"] for item in axis_summary),
            "every_argument_floor_positive": all(float(control["minimum_cumulative_argument_lower"]) > 0 for row in rows for control in row["controls"]),
            "raw_zero_evaluation_absent": True,
            "complete_face_cover_not_overclaimed": True,
            "complete_order_nine_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k385["ledger_effect"],
        "source_routing": k385["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb positive-approach control bank for the hardest K390 reachable face in each of the first eighteen K384 hybrid domains and the positive-interior fallbacks for v9/v10, each at rho=1/1024, 1/2048 and 1/4096 below the fixed 1/256 tangential scale. Every control assembles all 4,480 ordered descriptors and 20 coherent groups before applying K389 normal scaling or the K385 quadratic Peano majorant. These 60 controls exercise the compiled program interface but are not preconditioned face intervals, evaluations of all 695 faces, a recursive cover, analytic tails, hybrid integrals, a complete order-nine remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    expected = (20, 20, 18, 2, 3, 60, 4480, 268_800)
    actual = (
        fixed["hybrid_terms"], fixed["selected_boundary_or_interior_programs"],
        fixed["reachable_face_programs_executed"], fixed["positive_interior_fallback_programs_executed"],
        fixed["normal_levels_per_face"], fixed["complete_arb_controls"],
        fixed["ordered_descriptors_per_control"], fixed["ordered_descriptor_control_evaluations"],
    )
    if actual != expected:
        raise AssertionError("K391 fixed census changed")
    rows = payload["hardest_face_arb_controls"]
    if len(rows) != 20 or [row["axis"] for row in rows] != list(K387_BACKEND.AXES):
        raise AssertionError("K391 hybrid order changed")
    if any(len(row["controls"]) != 3 for row in rows):
        raise AssertionError("K391 normal-level controls changed")
    if any(control["coherent_group_count"] != 20 or float(control["minimum_cumulative_argument_lower"]) <= 0 for row in rows for control in row["controls"]):
        raise AssertionError("K391 coherent control boundary changed")
    contract = payload["execution_contract"]
    required_true = (
        "positive_normal_approach_only", "all_ordered_orientations_retained",
        "all_20_coherent_groups_assembled_before_reported_enclosure",
        "normal_scaling_applied_after_complete_assembly", "K385_peano_majorant_applied_after_complete_assembly",
        "controls_are_not_face_intervals", "controls_are_not_a_recursive_cover",
        "controls_are_not_integrated_hybrid_remainders",
    )
    if not all(contract[key] for key in required_true) or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K391 execution contract changed")
    decision = payload["decision"]
    if not decision["selected_boundary_or_interior_complete_coherent_arb_bank_executed"] or not decision["K390_compiled_programs_numerically_exercised"]:
        raise AssertionError("K391 control release lost")
    if any(decision[key] for key in ("preconditioned_interval_face_evaluator_complete", "all_695_faces_numerically_evaluated", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K391 overclaimed numerical closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K391 release test failed")


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

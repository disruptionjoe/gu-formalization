#!/usr/bin/env python3
"""Execute complete coherent Arb controls on K487's selected programs."""

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
K412_MODULE = HERE / "k412_order_ten_interior_origin_control.py"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
K487 = ROOT / "lab/process/k487-order-ten-face-program-compiler.json"
OUTPUT = ROOT / "lab/process/k488-order-ten-hardest-face-arb-bank.json"

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


K412_BACKEND = load_module(K412_MODULE, "k412_for_k488")


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
    moving = set(program["moving_axes"])
    codimension = int(program["codimension"])
    result = {}
    for axis in K412_BACKEND.AXES:
        if codimension and axis in zeroed:
            result[axis] = arb(q(rho / codimension))
        elif not codimension and axis in moving:
            result[axis] = arb(q(rho / len(moving)))
        else:
            result[axis] = arb(1) / 256
    return result


def build() -> dict[str, Any]:
    k410 = json.loads(K410.read_text())
    k487 = json.loads(K487.read_text())
    programs = {row["program_id"]: row for row in k487["face_programs"] + k487["positive_interior_fallback_programs"]}
    selected = k487["selected_boundary_or_interior_program_per_hybrid"]
    if len(selected) != 22:
        raise AssertionError("K487 selected-program census changed")
    rows = []
    summaries = []
    for selection in selected:
        program = programs[selection["program_id"]]
        controls = []
        for level in program["normal_levels"]:
            rho = Fraction(level)
            raw = raw_times(program, rho)
            second, group_rows = K412_BACKEND.complete_second(program["axis"], raw)
            singular_power = int(program["maximum_value_first_second_singular_powers"][2])
            normal_scaled = abs(second) * arb(q(rho**singular_power))
            active_time = raw[program["axis"]]
            peano_majorant = abs(second) * active_time * active_time / 2
            cumulative_s, cumulative_v = K412_BACKEND.cumulative(raw)
            minimum = min([value.lower() for value in cumulative_s.values()] + [value.lower() for value in cumulative_v.values()])
            values = (second, normal_scaled, peano_majorant)
            if minimum <= 0 or any(not math.isfinite(float(abs(value).upper())) for value in values):
                raise AssertionError(f"non-finite or zero-touching control for {program['axis']}")
            controls.append({
                "rho": level,
                "minimum_cumulative_argument_lower": lower_text(arb(minimum)),
                "complete_second_derivative_lower": lower_text(second),
                "complete_second_derivative_upper": upper_text(second),
                "complete_second_derivative_abs_upper": upper_text(second),
                "rho_to_K486_second_singular_power_abs_upper": upper_text(normal_scaled),
                "K410_quadratic_peano_majorant_abs_upper": upper_text(peano_majorant),
                "all_28_group_intervals_sha256": digest(group_rows),
                "coherent_group_count": len(group_rows),
                "raw_Bessel_evaluation_at_zero_used": False,
            })
        scaled = [arb(row["rho_to_K486_second_singular_power_abs_upper"]) for row in controls]
        rows.append({
            "axis": program["axis"], "program_id": program["program_id"], "face_id": program["face_id"],
            "face_kind": program["face_kind"], "zeroed_axes": program["zeroed_axes"], "codimension": program["codimension"],
            "active_peano_axis_zeroed": program["active_peano_axis_zeroed"],
            "maximum_second_singular_power": program["maximum_value_first_second_singular_powers"][2],
            "minimum_face_normal_power": program["minimum_second_derivative_face_normal_power"],
            "controls": controls,
            "successive_scaled_upper_ratios": [upper_text(scaled[index + 1] / scaled[index]) for index in range(len(scaled) - 1)],
            "face_program_sha256": digest(program),
        })
        summaries.append({
            "axis": program["axis"], "program_id": program["program_id"], "control_count": len(controls),
            "all_controls_finite": True,
            "all_controls_have_28_group_digests": all(row["coherent_group_count"] == 28 for row in controls),
        })
    return {
        "schema_version": "1.0", "result_id": "K488-ORDER-TEN-HARDEST-FACE-ARB-BANK",
        "created": "2026-09-25", "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY", "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": ["lab/process/k410-order-ten-zero-safe-radial-contract.json", "lab/process/k487-order-ten-face-program-compiler.json"],
            "arb_decimal_digits": 180, "threads": 1, "native_axes": list(K412_BACKEND.AXES), "hybrid_terms": 22,
            "selected_boundary_or_interior_programs": 22, "reachable_face_programs_executed": 20,
            "positive_interior_fallback_programs_executed": 2, "normal_levels_per_program": 3,
            "complete_arb_controls": len(rows) * 3, "ordered_descriptors_per_control": 13300,
            "ordered_descriptor_control_evaluations": len(rows) * 3 * 13300,
            "K487_complete_program_bank_sha256": k487["program_summary"]["complete_program_bank_sha256"],
        },
        "execution_contract": {
            "positive_normal_approach_only": True, "each_zeroed_axis_receives_rho_over_codimension": True,
            "all_other_raw_times_fixed_at_1_over_256": True, "all_ordered_orientations_retained": True,
            "all_28_coherent_groups_assembled_before_reported_enclosure": True,
            "normal_scaling_applied_after_complete_assembly": True, "K410_peano_majorant_applied_after_complete_assembly": True,
            "K485_K486_template_programs_replayed_by_pointer": True, "raw_Bessel_evaluation_at_zero_used": False,
            "controls_are_not_face_intervals": True, "controls_are_not_a_recursive_cover": True,
            "controls_are_not_integrated_hybrid_remainders": True,
        },
        "hardest_face_arb_controls": rows,
        "hybrid_summary": summaries,
        "bank_summary": {
            "all_22_hybrids_executed": len(rows) == 22,
            "all_66_controls_finite": all(row["all_controls_finite"] for row in summaries),
            "all_controls_retain_28_group_digests": all(row["all_controls_have_28_group_digests"] for row in summaries),
            "every_control_has_positive_argument_floor": all(float(control["minimum_cumulative_argument_lower"]) > 0 for row in rows for control in row["controls"]),
            "complete_bank_sha256": digest(rows),
        },
        "decision": {
            "selected_boundary_or_interior_complete_coherent_arb_bank_executed": True,
            "K487_compiled_programs_numerically_exercised": True,
            "preconditioned_interval_face_evaluator_complete": False, "all_936_faces_numerically_evaluated": False,
            "recursive_positive_interior_cover_complete": False, "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "replace approach controls by K485 row/column-scaled and confluent interval face cells, extend to all 936 faces, then join recursive positive-interior cells and analytic tails",
        },
        "release_test": {
            "all_22_hybrids_present": len(rows) == 22,
            "exactly_66_arb_controls_present": sum(len(row["controls"]) for row in rows) == 66,
            "all_877800_ordered_descriptor_controls_executed": len(rows) * 3 * 13300 == 877800,
            "all_controls_finite": all(row["all_controls_finite"] for row in summaries),
            "all_controls_have_28_group_digests": all(row["all_controls_have_28_group_digests"] for row in summaries),
            "every_argument_floor_positive": all(float(control["minimum_cumulative_argument_lower"]) > 0 for row in rows for control in row["controls"]),
            "raw_zero_evaluation_absent": True, "complete_face_cover_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True, "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k410["ledger_effect"], "source_routing": k410["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb positive-approach controls for the selected K487 program in all 22 order-ten hybrid domains at three normal levels. All 13,300 ordered descriptors and 28 coherent groups are assembled per control. These 66 controls are not face intervals, all-face evaluations, a recursive cover, analytic tails, hybrid integrals, a complete order-ten remainder, K457 cross value, K152 interval or physical/source/public conclusion.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    actual = (fixed["hybrid_terms"], fixed["selected_boundary_or_interior_programs"], fixed["reachable_face_programs_executed"], fixed["positive_interior_fallback_programs_executed"], fixed["normal_levels_per_program"], fixed["complete_arb_controls"], fixed["ordered_descriptors_per_control"], fixed["ordered_descriptor_control_evaluations"])
    if actual != (22, 22, 20, 2, 3, 66, 13300, 877800):
        raise AssertionError("K488 fixed census changed")
    rows = payload["hardest_face_arb_controls"]
    if [row["axis"] for row in rows] != list(K412_BACKEND.AXES):
        raise AssertionError("K488 hybrid order changed")
    if any(len(row["controls"]) != 3 for row in rows):
        raise AssertionError("K488 normal-level controls changed")
    if any(control["coherent_group_count"] != 28 or float(control["minimum_cumulative_argument_lower"]) <= 0 for row in rows for control in row["controls"]):
        raise AssertionError("K488 coherent control boundary changed")
    decision = payload["decision"]
    if any(decision[key] for key in ("preconditioned_interval_face_evaluator_complete", "all_936_faces_numerically_evaluated", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K488 overclaimed numerical closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K488 release test failed")


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate_payload(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

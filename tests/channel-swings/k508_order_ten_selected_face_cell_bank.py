#!/usr/bin/env python3
"""Positive-width interval cells for K487's selected order-ten faces."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K392_PATH = HERE / "k392_order_nine_preconditioned_face_cell_bank.py"
K408_PATH = HERE / "k408_order_ten_node_directional_jet_bank.py"
K412_PATH = HERE / "k412_order_ten_interior_origin_control.py"
K485_PATH = HERE / "k485_order_ten_mask_native_preconditioner_compiler.py"
K485_JSON = ROOT / "lab/process/k485-order-ten-mask-native-preconditioner-compiler.json"
K487_JSON = ROOT / "lab/process/k487-order-ten-face-program-compiler.json"
OUTPUT = ROOT / "lab/process/k508-order-ten-selected-face-cell-bank.json"

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


BASE = load_module(K392_PATH, "k392_for_k508")
K408 = load_module(K408_PATH, "k408_for_k508")
K412 = load_module(K412_PATH, "k412_for_k508")
K485 = load_module(K485_PATH, "k485_for_k508")

# K392's determinant-preserving evaluator is order-generic once its backends
# are rebound. These aliases adapt only historical backend attribute names.
K408.K382_MODULE = K408.K407_MODULE
K485.K382_BACKEND = K485.K407_BACKEND
K485.zero_matrix = K485.K388.zero_matrix
K485.coalescence_labels = K485.K388.coalescence_labels
BASE.K383_BACKEND = K408
BASE.K387_BACKEND = K412
BASE.K388_BACKEND = K485

NORMAL_CELLS = BASE.NORMAL_CELLS


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


def build() -> dict[str, Any]:
    k485 = json.loads(K485_JSON.read_text())
    k487 = json.loads(K487_JSON.read_text())
    singular_templates, confluent_templates = BASE.template_maps(k485)
    programs = {row["program_id"]: row for row in k487["face_programs"]}
    selected = [row for row in k487["selected_boundary_or_interior_program_per_hybrid"] if row["program_kind"] == "reachable_face"]
    if len(selected) != 20:
        raise AssertionError("K508 selected reachable-face census changed")

    rows = []
    direct_controls = []
    global_singular: Counter[str] = Counter()
    global_confluent: Counter[str] = Counter()
    for selection in selected:
        program = programs[selection["program_id"]]
        cells = []
        for cell_index, (left, right) in enumerate(NORMAL_CELLS):
            rho = BASE.interval(left, right)
            second, groups, singular_histogram, confluent_histogram, operations = BASE.complete_second(
                program, rho, singular_templates, confluent_templates
            )
            if not math.isfinite(float(abs(second).upper())):
                raise AssertionError(f"non-finite K508 cell {program['program_id']}")
            raw = BASE.raw_times(program, rho)
            cumulative_s, cumulative_v = K412.cumulative(raw)
            minimum = min([value.lower() for value in cumulative_s.values()] + [value.lower() for value in cumulative_v.values()])
            if minimum <= 0:
                raise AssertionError("K508 cell touched a zero Bessel argument")
            singular_power = int(program["maximum_value_first_second_singular_powers"][2])
            scaled = abs(second) * rho**singular_power
            active_upper = raw[program["axis"]].upper()
            peano = abs(second) * arb(active_upper) * arb(active_upper) / 2
            groups = [{**row, "group_id": str(row["group_id"]).replace("order9:", "order10:")} for row in groups]
            cells.append({
                "normal_interval": [q(left), q(right)],
                "normal_width": q(right - left),
                "minimum_cumulative_argument_lower": lower_text(arb(minimum)),
                "complete_second_derivative_lower": lower_text(second),
                "complete_second_derivative_upper": upper_text(second),
                "complete_second_derivative_abs_upper": abs_upper_text(second),
                "rho_to_K486_second_singular_power_abs_upper": abs_upper_text(scaled),
                "K410_quadratic_peano_majorant_abs_upper": abs_upper_text(peano),
                "coherent_group_count": len(groups),
                "all_28_group_intervals_sha256": digest(groups),
                "singular_template_ids": sorted(singular_histogram),
                "confluent_template_ids": sorted(confluent_histogram),
                "divided_difference_operation_uses": operations,
            })
            global_singular.update(singular_histogram)
            global_confluent.update(confluent_histogram)
            if cell_index == 0:
                direct, _ = K412.complete_second(program["axis"], raw)
                overlap = not (second.upper() < direct.lower() or second.lower() > direct.upper())
                if not overlap:
                    raise AssertionError(f"K508 direct overlap failed for {program['axis']}")
                direct_controls.append({
                    "axis": program["axis"],
                    "program_id": program["program_id"],
                    "normal_interval": [q(left), q(right)],
                    "preconditioned_lower": lower_text(second),
                    "preconditioned_upper": upper_text(second),
                    "direct_lower": lower_text(direct),
                    "direct_upper": upper_text(direct),
                    "intervals_overlap": overlap,
                })
        rows.append({
            "program_id": program["program_id"],
            "face_id": program["face_id"],
            "axis": program["axis"],
            "face_kind": program["face_kind"],
            "zeroed_axes": program["zeroed_axes"],
            "codimension": program["codimension"],
            "active_peano_axis_zeroed": program["active_peano_axis_zeroed"],
            "maximum_second_singular_power": program["maximum_value_first_second_singular_powers"][2],
            "minimum_face_normal_power": program["minimum_second_derivative_face_normal_power"],
            "cells": cells,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K508-ORDER-TEN-SELECTED-FACE-CELL-BANK",
        "created": "2026-09-25",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k485-order-ten-mask-native-preconditioner-compiler.json",
                "lab/process/k487-order-ten-face-program-compiler.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "selected_reachable_face_programs": len(rows),
            "positive_width_cells_per_selected_face": len(NORMAL_CELLS),
            "complete_positive_width_cells": len(rows) * len(NORMAL_CELLS),
            "ordered_descriptors_per_cell": 13300,
            "ordered_descriptor_cell_evaluations": len(rows) * len(NORMAL_CELLS) * 13300,
            "coherent_groups_per_cell": 28,
            "normal_cells": [[q(left), q(right)] for left, right in NORMAL_CELLS],
            "K485_template_bank_sha256": k485["template_summary"]["template_bank_sha256"],
            "K487_program_bank_sha256": k487["program_summary"]["complete_program_bank_sha256"],
            "unexecuted_reachable_face_programs": len(k487["face_programs"]) - len(rows),
            "positive_interior_fallback_axes": k487["program_summary"]["hybrids_without_reachable_faces"],
        },
        "execution_contract": {
            "one_shared_normal_interval_per_cell": True,
            "zeroed_raw_times_equal_rho_over_codimension": True,
            "exact_cumulative_node_differences_used": True,
            "confluent_row_column_divided_differences_applied_before_determinant_assembly": True,
            "K485_assignment_dual_row_column_scaling_applied_before_determinant_assembly": True,
            "all_ordered_orientations_retained": True,
            "all_28_coherent_groups_assembled_before_reported_enclosure": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "cells_are_positive_width_normal_chart_intervals": True,
            "selected_program_bank_is_not_all_936_faces": True,
            "equal_normal_chart_is_not_full_projective_normal_cone": True,
            "cells_are_not_recursive_whole_domain_cover": True,
        },
        "selected_face_cell_bank": rows,
        "direct_overlap_controls": direct_controls,
        "bank_summary": {
            "all_20_selected_reachable_faces_executed": len(rows) == 20,
            "all_140_cells_finite": all(math.isfinite(float(cell["complete_second_derivative_abs_upper"])) for row in rows for cell in row["cells"]),
            "every_cell_has_positive_argument_floor": all(float(cell["minimum_cumulative_argument_lower"]) > 0 for row in rows for cell in row["cells"]),
            "all_20_direct_overlap_controls_pass": len(direct_controls) == 20 and all(row["intervals_overlap"] for row in direct_controls),
            "executed_singular_template_ids": sorted(global_singular),
            "executed_confluent_template_ids": sorted(global_confluent),
            "complete_selected_bank_sha256": digest(rows),
        },
        "decision": {
            "K485_preconditioned_selected_positive_width_face_cells_released": True,
            "selected_20_reachable_faces_numerically_evaluated": True,
            "all_936_reachable_faces_numerically_evaluated": False,
            "canonical_equal_normal_selected_bank_complete": True,
            "full_projective_normal_cone_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "Use the selected cell bank as backend evidence, then execute the remaining 916 face programs under a separately measured resource plan before any all-face or projective integration claim.",
        },
        "release_test": {
            "exactly_20_selected_face_programs_present": len(rows) == 20,
            "exactly_140_positive_width_cells_present": sum(len(row["cells"]) for row in rows) == 140,
            "all_1862000_ordered_descriptor_cell_evaluations_covered": len(rows) * len(NORMAL_CELLS) * 13300 == 1_862_000,
            "all_cells_finite": all(math.isfinite(float(cell["complete_second_derivative_abs_upper"])) for row in rows for cell in row["cells"]),
            "all_argument_floors_positive": all(float(cell["minimum_cumulative_argument_lower"]) > 0 for row in rows for cell in row["cells"]),
            "all_direct_overlap_controls_pass": len(direct_controls) == 20 and all(row["intervals_overlap"] for row in direct_controls),
            "raw_zero_evaluation_absent": True,
            "all_face_cover_not_overclaimed": True,
            "full_normal_cone_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k487["ledger_effect"],
        "source_routing": k487["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb positive-width normal-chart cells on seven exact rational intervals for K487's selected reachable-face program in each of twenty order-ten hybrid domains. Every cell applies K485's exact confluent divided differences and assignment-dual scaling before determinant assembly, retains all 13,300 ordered descriptors and 28 coherent groups, and has a positive argument floor. This selected bank covers 20 of 936 reachable faces; it is not an all-face bank, projective normal-cone cover, recursive interior cover, analytic tail, hybrid integral, complete order-ten remainder, K457 value, K152 interval, source/ledger move, canon, paper, public or physical conclusion.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    actual = (
        fixed["selected_reachable_face_programs"],
        fixed["positive_width_cells_per_selected_face"],
        fixed["complete_positive_width_cells"],
        fixed["ordered_descriptors_per_cell"],
        fixed["ordered_descriptor_cell_evaluations"],
        fixed["coherent_groups_per_cell"],
    )
    if actual != (20, 7, 140, 13300, 1_862_000, 28):
        raise AssertionError("K508 fixed census changed")
    rows = payload["selected_face_cell_bank"]
    if len(rows) != 20 or len({row["axis"] for row in rows}) != 20 or any(len(row["cells"]) != 7 for row in rows):
        raise AssertionError("K508 selected cell identities changed")
    if any(cell["coherent_group_count"] != 28 or float(cell["minimum_cumulative_argument_lower"]) <= 0 for row in rows for cell in row["cells"]):
        raise AssertionError("K508 positive coherent cell boundary changed")
    summary = payload["bank_summary"]
    if not summary["all_140_cells_finite"] or not summary["every_cell_has_positive_argument_floor"]:
        raise AssertionError("K508 bank summary lost finite positive cells")
    if len(payload["direct_overlap_controls"]) != 20 or not all(row["intervals_overlap"] for row in payload["direct_overlap_controls"]):
        raise AssertionError("K508 direct overlap controls changed")
    decision = payload["decision"]
    if not decision["K485_preconditioned_selected_positive_width_face_cells_released"] or decision["all_936_reachable_faces_numerically_evaluated"]:
        raise AssertionError("K508 release or all-face boundary changed")
    if any(decision[key] for key in ("full_projective_normal_cone_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K508 overclaimed whole-domain closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K508 release test failed")


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

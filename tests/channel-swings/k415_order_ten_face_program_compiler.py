#!/usr/bin/env python3
"""Compile every K411 face into a replayable K413/K414 approach program.

The output is an exact execution schedule, not a numerical cover.  Each face
records the determinant singular and confluent templates used by all 13,300
ordered descriptors, the face-normal power from K414, and a deterministic
positive approach chart for later Arb evaluation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K413_MODULE = HERE / "k413_order_ten_mask_native_preconditioner_compiler.py"
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
K413 = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"
K414 = ROOT / "lab/process/k414-order-ten-face-normal-integrability-atlas.json"
OUTPUT = ROOT / "lab/process/k415-order-ten-face-program-compiler.json"

NORMAL_LEVELS = ("1/1024", "1/2048", "1/4096")
TANGENTIAL_RAW_TIME = "1/256"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K413_BACKEND = load_module(K413_MODULE, "k413_for_k415")


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def singular_key(matrix: list[list[int]] | tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(value) for value in row) for row in matrix)


def confluent_key(rank: int, rows: list[int] | tuple[int, ...], columns: list[int] | tuple[int, ...]) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    return int(rank), tuple(int(value) for value in rows), tuple(int(value) for value in columns)


def face_id(axis: str, kind: str, zeroed_axes: list[str]) -> str:
    return f"{axis}:{kind}:{','.join(zeroed_axes)}"


def build() -> dict[str, Any]:
    k411 = json.loads(K411.read_text())
    k413 = json.loads(K413.read_text())
    k414 = json.loads(K414.read_text())
    descriptors = K413_BACKEND.ordered_descriptors()
    if len(descriptors) != 13300:
        raise AssertionError("K415 ordered descriptor census changed")

    singular_templates = {
        singular_key(row["zero_entry_matrix"]): f"S{index:02d}"
        for index, row in enumerate(k413["preconditioner_templates"])
    }
    confluent_rows = k413["confluent_divided_difference_contract"]["templates"]
    confluent_templates = {
        confluent_key(row["rank"], row["row_cluster_labels"], row["column_cluster_labels"]): f"C{index:02d}"
        for index, row in enumerate(confluent_rows)
    }
    if len(singular_templates) != 60 or len(confluent_templates) != 75:
        raise AssertionError("K413 template bank changed")

    power_rows = {
        (row["axis"], row["face_kind"], tuple(row["zeroed_axes"])): row
        for row in k414["face_normal_atlas"]
    }
    programs = []
    global_singular = Counter()
    global_confluent = Counter()
    matrix_uses = 0
    descriptor_programs = 0
    for hybrid in k411["hybrid_face_atlas"]:
        axis = hybrid["axis"]
        fixed = hybrid["preceding_axes_fixed_at_node"]
        moving = hybrid["moving_axes"]
        for kind, faces in hybrid["faces"].items():
            for face in faces:
                zeroed = face["zeroed_axes"]
                mask = set(zeroed)
                if mask.intersection(fixed):
                    raise AssertionError("reachable face intersects a fixed node axis")
                singular_histogram = Counter()
                confluent_histogram = Counter()
                descriptor_signatures = []
                for descriptor in descriptors:
                    singular_ids = []
                    confluent_ids = []
                    for matrix in descriptor["species_matrices"]:
                        zero_pattern = K413_BACKEND.zero_matrix(matrix, mask)
                        singular_id = singular_templates.get(zero_pattern)
                        row_labels = K413_BACKEND.coalescence_labels(matrix["row_positions"], "s", mask)
                        column_labels = K413_BACKEND.coalescence_labels(matrix["column_positions"], "v", mask)
                        confluent_id = confluent_templates.get(confluent_key(matrix["rank"], row_labels, column_labels))
                        if singular_id is None or confluent_id is None:
                            raise AssertionError("face matrix did not resolve to K413 template banks")
                        singular_ids.append(singular_id)
                        confluent_ids.append(confluent_id)
                        singular_histogram[singular_id] += 1
                        confluent_histogram[confluent_id] += 1
                        global_singular[singular_id] += 1
                        global_confluent[confluent_id] += 1
                        matrix_uses += 1
                    descriptor_signatures.append({
                        "group_id": descriptor["group_id"],
                        "left": descriptor["left"],
                        "right": descriptor["right"],
                        "singular_templates": singular_ids,
                        "confluent_templates": confluent_ids,
                    })
                    descriptor_programs += 1

                power = power_rows.get((axis, kind, tuple(zeroed)))
                if power is None:
                    raise AssertionError("K414 face-normal row missing")
                programs.append({
                    "program_id": face_id(axis, kind, zeroed),
                    "face_id": face_id(axis, kind, zeroed),
                    "axis": axis,
                    "face_kind": kind,
                    "zeroed_axes": zeroed,
                    "codimension": len(zeroed),
                    "preceding_axes_fixed_at_node": fixed,
                    "moving_axes": moving,
                    "active_peano_axis_zeroed": axis in mask,
                    "normal_levels": list(NORMAL_LEVELS),
                    "normal_allocation": "each zeroed raw time equals rho/codimension",
                    "positive_tangential_raw_time": TANGENTIAL_RAW_TIME,
                    "maximum_value_first_second_singular_powers": power["maximum_value_first_second_singular_powers"],
                    "minimum_second_derivative_face_normal_power": power["minimum_second_derivative_face_normal_power"],
                    "singular_template_histogram": dict(sorted(singular_histogram.items())),
                    "confluent_template_histogram": dict(sorted(confluent_histogram.items())),
                    "descriptor_program_sha256": digest(descriptor_signatures),
                    "ordered_descriptor_programs": len(descriptor_signatures),
                    "determinant_matrix_programs": sum(singular_histogram.values()),
                })

    selected_programs = []
    interior_fallbacks = []
    hybrid_by_axis = {row["axis"]: row for row in k411["hybrid_face_atlas"]}
    for axis in k411["fixed_control"]["native_axes"]:
        candidates = [row for row in programs if row["axis"] == axis]
        if candidates:
            selected = min(
                candidates,
                key=lambda row: (
                    row["minimum_second_derivative_face_normal_power"],
                    -row["maximum_value_first_second_singular_powers"][2],
                    -row["codimension"],
                    row["face_id"],
                ),
            )
            selected_programs.append({
                "axis": axis,
                "program_id": selected["program_id"],
                "program_kind": "reachable_face",
                "selection_basis": "minimum K414 normal exponent, then largest second-order singular power, codimension and lexical identity",
            })
        else:
            hybrid = hybrid_by_axis[axis]
            fallback = {
                "program_id": f"{axis}:positive_interior",
                "face_id": None,
                "axis": axis,
                "face_kind": "positive_interior_fallback",
                "zeroed_axes": [],
                "codimension": 0,
                "preceding_axes_fixed_at_node": hybrid["preceding_axes_fixed_at_node"],
                "moving_axes": hybrid["moving_axes"],
                "active_peano_axis_zeroed": False,
                "normal_levels": list(NORMAL_LEVELS),
                "normal_allocation": "rho is shared equally by all moving positive raw times",
                "positive_tangential_raw_time": TANGENTIAL_RAW_TIME,
                "maximum_value_first_second_singular_powers": [0, 0, 0],
                "minimum_second_derivative_face_normal_power": None,
                "singular_template_histogram": {},
                "confluent_template_histogram": {},
                "descriptor_program_sha256": None,
                "ordered_descriptor_programs": 13300,
                "determinant_matrix_programs": 0,
            }
            interior_fallbacks.append(fallback)
            selected_programs.append({
                "axis": axis,
                "program_id": fallback["program_id"],
                "program_kind": "positive_interior_fallback",
                "selection_basis": "K411 proves no reachable zero/coalescence face for this hybrid; retain a positive-interior radial control",
            })

    return {
        "schema_version": "1.0",
        "result_id": "K415-ORDER-TEN-FACE-PROGRAM-COMPILER",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k411-order-ten-hybrid-face-atlas.json",
                "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json",
                "lab/process/k414-order-ten-face-normal-integrability-atlas.json",
            ],
            "native_axes": k411["fixed_control"]["native_axes"],
            "hybrid_terms": 22,
            "ordered_descriptors_per_face": len(descriptors),
            "reachable_face_instances": len(programs),
            "descriptor_face_programs": descriptor_programs,
            "determinant_matrix_face_programs": matrix_uses,
            "singular_template_count": len(singular_templates),
            "confluent_template_count": len(confluent_templates),
            "K413_template_bank_sha256": k413["template_summary"]["template_bank_sha256"],
            "K414_face_atlas_sha256": k414["atlas_summary"]["complete_atlas_sha256"],
        },
        "approach_chart_contract": {
            "normal_coordinate": "rho is divided equally among exactly the zeroed raw-time axes",
            "fixed_preceding_axes": TANGENTIAL_RAW_TIME,
            "positive_moving_tangential_axes": TANGENTIAL_RAW_TIME,
            "normal_levels": list(NORMAL_LEVELS),
            "determinant_singular_scaling": "resolve every matrix to its exact K413 row/column assignment-dual template before interval substitution",
            "determinant_confluence": "resolve every repeated-node cluster to its exact K413 divided-difference template before interval substitution",
            "complete_coherent_assembly_required": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "approach_program_is_not_a_face_interval": True,
            "approach_program_is_not_a_recursive_cover": True,
        },
        "face_programs": programs,
        "positive_interior_fallback_programs": interior_fallbacks,
        "selected_boundary_or_interior_program_per_hybrid": selected_programs,
        "program_summary": {
            "all_936_faces_compiled": len(programs) == 936,
            "all_12448800_descriptor_face_programs_compiled": descriptor_programs == 12_448_800,
            "all_49544352_matrix_face_programs_resolved": matrix_uses == 49_544_352,
            "all_faces_have_three_positive_normal_levels": all(row["normal_levels"] == list(NORMAL_LEVELS) for row in programs),
            "all_faces_replay_K414_integrability": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in programs),
            "hybrids_with_reachable_faces": 20,
            "hybrids_without_reachable_faces": ["v10", "v11"],
            "global_singular_template_histogram": dict(sorted(global_singular.items())),
            "global_confluent_template_histogram": dict(sorted(global_confluent.items())),
            "complete_program_bank_sha256": digest(programs),
        },
        "decision": {
            "complete_face_program_bank_compiled": True,
            "all_K413_template_uses_resolved": True,
            "hardest_boundary_or_interior_program_per_hybrid_released_for_arb_control": True,
            "preconditioned_interval_face_evaluator_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "execute complete coherent Arb approach controls on the hardest compiled face in every hybrid; then implement row/column-scaled interval cells and recursive whole-domain coverage",
        },
        "release_test": {
            "twenty_two_hybrid_control_programs_present": len(selected_programs) == 22,
            "exactly_two_positive_interior_fallbacks_present": len(interior_fallbacks) == 2,
            "all_936_face_instances_present": len(programs) == 936,
            "all_12448800_descriptor_programs_present": descriptor_programs == 12_448_800,
            "all_49544352_matrix_programs_present": matrix_uses == 49_544_352,
            "all_60_singular_templates_resolved": set(global_singular) == set(singular_templates.values()),
            "all_75_confluent_templates_resolved": set(global_confluent) == set(confluent_templates.values()),
            "all_normal_exponents_integrable": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in programs),
            "raw_zero_evaluation_absent": True,
            "complete_numerical_cover_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k414["ledger_effect"],
        "source_routing": k414["source_routing"],
        "claim_ceiling": "Exact executable approach-program compiler for all 936 K411 reachable face instances and all 12,448,800 ordered descriptor-face programs. Every determinant matrix use resolves to K413's singular and confluent template banks, while K414 supplies the face-normal exponent and the chart fixes three positive approach levels. Twenty hybrids have reachable faces; K411 proves that v10 and v11 do not, so their selected controls remain positive-interior fallbacks. This is a program map, not a preconditioned face interval, recursive cover, analytic tail, Peano integral, complete order-ten remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    expected = (22, 13300, 936, 12_448_800, 49_544_352, 60, 75)
    actual = (
        fixed["hybrid_terms"], fixed["ordered_descriptors_per_face"], fixed["reachable_face_instances"],
        fixed["descriptor_face_programs"], fixed["determinant_matrix_face_programs"],
        fixed["singular_template_count"], fixed["confluent_template_count"],
    )
    if actual != expected:
        raise AssertionError("K415 fixed census changed")
    programs = payload["face_programs"]
    if len(programs) != 936 or len({row["face_id"] for row in programs}) != 936:
        raise AssertionError("K415 face identities changed")
    if len(payload["selected_boundary_or_interior_program_per_hybrid"]) != 22 or len(payload["positive_interior_fallback_programs"]) != 2:
        raise AssertionError("K415 selected control-program bank changed")
    if any(row["ordered_descriptor_programs"] != 13300 or row["minimum_second_derivative_face_normal_power"] <= -1 for row in programs):
        raise AssertionError("K415 face program boundary changed")
    contract = payload["approach_chart_contract"]
    if (not contract["complete_coherent_assembly_required"] or contract["raw_Bessel_evaluation_at_zero_used"]
            or not contract["approach_program_is_not_a_face_interval"] or not contract["approach_program_is_not_a_recursive_cover"]):
        raise AssertionError("K415 approach contract changed")
    decision = payload["decision"]
    if not decision["complete_face_program_bank_compiled"] or not decision["all_K413_template_uses_resolved"]:
        raise AssertionError("K415 compiler release lost")
    if any(decision[key] for key in ("preconditioned_interval_face_evaluator_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K415 overclaimed numerical closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K415 release test failed")


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

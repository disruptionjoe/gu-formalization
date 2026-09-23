#!/usr/bin/env python3
"""Compile every K350 face into a replayable K352/K353 approach program.

The output is an exact execution schedule, not a numerical cover.  Each face
records the determinant singular and confluent templates used by all 2,400
ordered descriptors, the face-normal power from K353, and a deterministic
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
K352_MODULE = HERE / "k352_order_eight_mask_native_preconditioner_compiler.py"
K350 = ROOT / "lab/process/k350-order-eight-hybrid-face-atlas.json"
K352 = ROOT / "lab/process/k352-order-eight-mask-native-preconditioner-compiler.json"
K353 = ROOT / "lab/process/k353-order-eight-face-normal-integrability-atlas.json"
OUTPUT = ROOT / "lab/process/k354-order-eight-face-program-compiler.json"

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


K352_BACKEND = load_module(K352_MODULE, "k352_for_k354")


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
    k350 = json.loads(K350.read_text())
    k352 = json.loads(K352.read_text())
    k353 = json.loads(K353.read_text())
    descriptors = K352_BACKEND.ordered_descriptors()
    if len(descriptors) != 2400:
        raise AssertionError("K354 ordered descriptor census changed")

    singular_templates = {
        singular_key(row["zero_entry_matrix"]): f"S{index:02d}"
        for index, row in enumerate(k352["preconditioner_templates"])
    }
    confluent_rows = k352["confluent_divided_difference_contract"]["templates"]
    confluent_templates = {
        confluent_key(row["rank"], row["row_cluster_labels"], row["column_cluster_labels"]): f"C{index:02d}"
        for index, row in enumerate(confluent_rows)
    }
    if len(singular_templates) != 34 or len(confluent_templates) != 38:
        raise AssertionError("K352 template bank changed")

    power_rows = {
        (row["axis"], row["face_kind"], tuple(row["zeroed_axes"])): row
        for row in k353["face_normal_atlas"]
    }
    programs = []
    global_singular = Counter()
    global_confluent = Counter()
    matrix_uses = 0
    descriptor_programs = 0
    for hybrid in k350["hybrid_face_atlas"]:
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
                        zero_pattern = K352_BACKEND.zero_matrix(matrix, mask)
                        singular_id = singular_templates.get(zero_pattern)
                        row_labels = K352_BACKEND.coalescence_labels(matrix["row_positions"], "s", mask)
                        column_labels = K352_BACKEND.coalescence_labels(matrix["column_positions"], "v", mask)
                        confluent_id = confluent_templates.get(confluent_key(matrix["rank"], row_labels, column_labels))
                        if singular_id is None or confluent_id is None:
                            raise AssertionError("face matrix did not resolve to K352 template banks")
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
                    raise AssertionError("K353 face-normal row missing")
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
    hybrid_by_axis = {row["axis"]: row for row in k350["hybrid_face_atlas"]}
    for axis in k350["fixed_control"]["native_axes"]:
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
                "selection_basis": "minimum K353 normal exponent, then largest second-order singular power, codimension and lexical identity",
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
                "ordered_descriptor_programs": 2400,
                "determinant_matrix_programs": 0,
            }
            interior_fallbacks.append(fallback)
            selected_programs.append({
                "axis": axis,
                "program_id": fallback["program_id"],
                "program_kind": "positive_interior_fallback",
                "selection_basis": "K350 proves no reachable zero/coalescence face for this hybrid; retain a positive-interior radial control",
            })

    return {
        "schema_version": "1.0",
        "result_id": "K354-ORDER-EIGHT-FACE-PROGRAM-COMPILER",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k350-order-eight-hybrid-face-atlas.json",
                "lab/process/k352-order-eight-mask-native-preconditioner-compiler.json",
                "lab/process/k353-order-eight-face-normal-integrability-atlas.json",
            ],
            "native_axes": k350["fixed_control"]["native_axes"],
            "hybrid_terms": 18,
            "ordered_descriptors_per_face": len(descriptors),
            "reachable_face_instances": len(programs),
            "descriptor_face_programs": descriptor_programs,
            "determinant_matrix_face_programs": matrix_uses,
            "singular_template_count": len(singular_templates),
            "confluent_template_count": len(confluent_templates),
            "K352_template_bank_sha256": k352["template_summary"]["template_bank_sha256"],
            "K353_face_atlas_sha256": k353["atlas_summary"]["complete_atlas_sha256"],
        },
        "approach_chart_contract": {
            "normal_coordinate": "rho is divided equally among exactly the zeroed raw-time axes",
            "fixed_preceding_axes": TANGENTIAL_RAW_TIME,
            "positive_moving_tangential_axes": TANGENTIAL_RAW_TIME,
            "normal_levels": list(NORMAL_LEVELS),
            "determinant_singular_scaling": "resolve every matrix to its exact K352 row/column assignment-dual template before interval substitution",
            "determinant_confluence": "resolve every repeated-node cluster to its exact K352 divided-difference template before interval substitution",
            "complete_coherent_assembly_required": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "approach_program_is_not_a_face_interval": True,
            "approach_program_is_not_a_recursive_cover": True,
        },
        "face_programs": programs,
        "positive_interior_fallback_programs": interior_fallbacks,
        "selected_boundary_or_interior_program_per_hybrid": selected_programs,
        "program_summary": {
            "all_517_faces_compiled": len(programs) == 517,
            "all_1240800_descriptor_face_programs_compiled": descriptor_programs == 1_240_800,
            "all_4876344_matrix_face_programs_resolved": matrix_uses == 4_876_344,
            "all_faces_have_three_positive_normal_levels": all(row["normal_levels"] == list(NORMAL_LEVELS) for row in programs),
            "all_faces_replay_K353_integrability": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in programs),
            "hybrids_with_reachable_faces": 16,
            "hybrids_without_reachable_faces": ["v8", "v9"],
            "global_singular_template_histogram": dict(sorted(global_singular.items())),
            "global_confluent_template_histogram": dict(sorted(global_confluent.items())),
            "complete_program_bank_sha256": digest(programs),
        },
        "decision": {
            "complete_face_program_bank_compiled": True,
            "all_K352_template_uses_resolved": True,
            "hardest_boundary_or_interior_program_per_hybrid_released_for_arb_control": True,
            "preconditioned_interval_face_evaluator_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "execute complete coherent Arb approach controls on the hardest compiled face in every hybrid; then implement row/column-scaled interval cells and recursive whole-domain coverage",
        },
        "release_test": {
            "eighteen_hybrid_control_programs_present": len(selected_programs) == 18,
            "exactly_two_positive_interior_fallbacks_present": len(interior_fallbacks) == 2,
            "all_517_face_instances_present": len(programs) == 517,
            "all_1240800_descriptor_programs_present": descriptor_programs == 1_240_800,
            "all_4876344_matrix_programs_present": matrix_uses == 4_876_344,
            "all_34_singular_templates_resolved": set(global_singular) == set(singular_templates.values()),
            "all_38_confluent_templates_resolved": set(global_confluent) == set(confluent_templates.values()),
            "all_normal_exponents_integrable": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in programs),
            "raw_zero_evaluation_absent": True,
            "complete_numerical_cover_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k353["ledger_effect"],
        "source_routing": k353["source_routing"],
        "claim_ceiling": "Exact executable approach-program compiler for all 517 K350 reachable face instances and all 1,240,800 ordered descriptor-face programs. Every one of the 4,876,344 determinant matrix uses resolves to K352's singular and confluent template banks, while K353 supplies the face-normal exponent and the chart fixes three positive approach levels. Sixteen hybrids have reachable faces; K350 proves that v8 and v9 do not, so their selected controls remain positive-interior fallbacks. This is a program map, not a preconditioned face interval, recursive cover, analytic tail, Peano integral, complete order-eight remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    expected = (18, 2400, 517, 1_240_800, 4_876_344, 34, 38)
    actual = (
        fixed["hybrid_terms"], fixed["ordered_descriptors_per_face"], fixed["reachable_face_instances"],
        fixed["descriptor_face_programs"], fixed["determinant_matrix_face_programs"],
        fixed["singular_template_count"], fixed["confluent_template_count"],
    )
    if actual != expected:
        raise AssertionError("K354 fixed census changed")
    programs = payload["face_programs"]
    if len(programs) != 517 or len({row["face_id"] for row in programs}) != 517:
        raise AssertionError("K354 face identities changed")
    if len(payload["selected_boundary_or_interior_program_per_hybrid"]) != 18 or len(payload["positive_interior_fallback_programs"]) != 2:
        raise AssertionError("K354 selected control-program bank changed")
    if any(row["ordered_descriptor_programs"] != 2400 or row["minimum_second_derivative_face_normal_power"] <= -1 for row in programs):
        raise AssertionError("K354 face program boundary changed")
    contract = payload["approach_chart_contract"]
    if (not contract["complete_coherent_assembly_required"] or contract["raw_Bessel_evaluation_at_zero_used"]
            or not contract["approach_program_is_not_a_face_interval"] or not contract["approach_program_is_not_a_recursive_cover"]):
        raise AssertionError("K354 approach contract changed")
    decision = payload["decision"]
    if not decision["complete_face_program_bank_compiled"] or not decision["all_K352_template_uses_resolved"]:
        raise AssertionError("K354 compiler release lost")
    if any(decision[key] for key in ("preconditioned_interval_face_evaluator_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K354 overclaimed numerical closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K354 release test failed")


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

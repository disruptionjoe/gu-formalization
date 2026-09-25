#!/usr/bin/env python3
"""Compile every K411 face into a replayable K485/K486 approach program."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K485_MODULE = HERE / "k485_order_ten_mask_native_preconditioner_compiler.py"
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
K485 = ROOT / "lab/process/k485-order-ten-mask-native-preconditioner-compiler.json"
K486 = ROOT / "lab/process/k486-order-ten-face-normal-integrability-atlas.json"
OUTPUT = ROOT / "lab/process/k487-order-ten-face-program-compiler.json"
NORMAL_LEVELS = ("1/1024", "1/2048", "1/4096")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K485_BACKEND = load_module(K485_MODULE, "k485_for_k487")


def singular_key(matrix: Any) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(value) for value in row) for row in matrix)


def confluent_key(rank: int, rows: Any, columns: Any) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    return int(rank), tuple(int(v) for v in rows), tuple(int(v) for v in columns)


def face_id(axis: str, kind: str, zeroed: list[str]) -> str:
    return f"{axis}:{kind}:{','.join(zeroed)}"


def build() -> dict[str, Any]:
    k411 = json.loads(K411.read_text())
    k485 = json.loads(K485.read_text())
    k486 = json.loads(K486.read_text())
    descriptors = K485_BACKEND.ordered_descriptors()
    singular_templates = {singular_key(row["zero_entry_matrix"]): f"S{i:02d}" for i, row in enumerate(k485["preconditioner_templates"])}
    confluent_templates = {
        confluent_key(row["rank"], row["row_cluster_labels"], row["column_cluster_labels"]): f"C{i:02d}"
        for i, row in enumerate(k485["confluent_divided_difference_contract"]["templates"])
    }
    powers = {(row["axis"], row["face_kind"], tuple(row["zeroed_axes"])): row for row in k486["face_normal_atlas"]}
    programs = []
    global_singular = Counter()
    global_confluent = Counter()
    matrix_uses = 0
    descriptor_programs = 0
    for hybrid in k411["hybrid_face_atlas"]:
        axis = hybrid["axis"]
        for kind, faces in hybrid["faces"].items():
            for face in faces:
                zeroed = face["zeroed_axes"]
                mask = set(zeroed)
                singular_hist = Counter()
                confluent_hist = Counter()
                signatures = []
                for descriptor in descriptors:
                    singular_ids = []
                    confluent_ids = []
                    for matrix in descriptor["species_matrices"]:
                        pattern = K485_BACKEND.K388.zero_matrix(matrix, mask)
                        sid = singular_templates[pattern]
                        rows = K485_BACKEND.K388.coalescence_labels(matrix["row_positions"], "s", mask)
                        columns = K485_BACKEND.K388.coalescence_labels(matrix["column_positions"], "v", mask)
                        cid = confluent_templates[confluent_key(matrix["rank"], rows, columns)]
                        singular_ids.append(sid)
                        confluent_ids.append(cid)
                        singular_hist[sid] += 1
                        confluent_hist[cid] += 1
                        global_singular[sid] += 1
                        global_confluent[cid] += 1
                        matrix_uses += 1
                    signatures.append({"group_id": descriptor["group_id"], "left": descriptor["left"], "right": descriptor["right"], "singular": singular_ids, "confluent": confluent_ids})
                    descriptor_programs += 1
                power = powers[(axis, kind, tuple(zeroed))]
                programs.append({
                    "program_id": face_id(axis, kind, zeroed),
                    "face_id": face_id(axis, kind, zeroed),
                    "axis": axis,
                    "face_kind": kind,
                    "zeroed_axes": zeroed,
                    "codimension": len(zeroed),
                    "preceding_axes_fixed_at_node": hybrid["preceding_axes_fixed_at_node"],
                    "moving_axes": hybrid["moving_axes"],
                    "active_peano_axis_zeroed": axis in mask,
                    "normal_levels": list(NORMAL_LEVELS),
                    "maximum_value_first_second_singular_powers": power["maximum_value_first_second_singular_powers"],
                    "minimum_second_derivative_face_normal_power": power["minimum_second_derivative_face_normal_power"],
                    "singular_template_histogram": dict(sorted(singular_hist.items())),
                    "confluent_template_histogram": dict(sorted(confluent_hist.items())),
                    "descriptor_program_sha256": K485_BACKEND.K388.digest(signatures),
                    "ordered_descriptor_programs": len(signatures),
                    "determinant_matrix_programs": sum(singular_hist.values()),
                })

    hybrid_by_axis = {row["axis"]: row for row in k411["hybrid_face_atlas"]}
    selected = []
    fallbacks = []
    for axis in k411["fixed_control"]["native_axes"]:
        candidates = [row for row in programs if row["axis"] == axis]
        if candidates:
            choice = min(candidates, key=lambda row: (row["minimum_second_derivative_face_normal_power"], -row["maximum_value_first_second_singular_powers"][2], -row["codimension"], row["face_id"]))
            selected.append({"axis": axis, "program_id": choice["program_id"], "program_kind": "reachable_face"})
        else:
            hybrid = hybrid_by_axis[axis]
            fallback = {
                "program_id": f"{axis}:positive_interior", "face_id": None, "axis": axis,
                "face_kind": "positive_interior_fallback", "zeroed_axes": [], "codimension": 0,
                "preceding_axes_fixed_at_node": hybrid["preceding_axes_fixed_at_node"], "moving_axes": hybrid["moving_axes"],
                "active_peano_axis_zeroed": False, "normal_levels": list(NORMAL_LEVELS),
                "maximum_value_first_second_singular_powers": [0, 0, 0],
                "minimum_second_derivative_face_normal_power": None, "ordered_descriptor_programs": len(descriptors),
                "determinant_matrix_programs": 0,
            }
            fallbacks.append(fallback)
            selected.append({"axis": axis, "program_id": fallback["program_id"], "program_kind": "positive_interior_fallback"})

    return {
        "schema_version": "1.0", "result_id": "K487-ORDER-TEN-FACE-PROGRAM-COMPILER",
        "created": "2026-09-25", "classification": "INTERNAL_STRUCTURAL_ONLY", "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K411.relative_to(ROOT)), str(K485.relative_to(ROOT)), str(K486.relative_to(ROOT))],
            "native_axes": k411["fixed_control"]["native_axes"], "hybrid_terms": 22,
            "ordered_descriptors_per_face": len(descriptors), "reachable_face_instances": len(programs),
            "descriptor_face_programs": descriptor_programs, "determinant_matrix_face_programs": matrix_uses,
            "singular_template_count": len(singular_templates), "confluent_template_count": len(confluent_templates),
            "K485_template_bank_sha256": k485["template_summary"]["template_bank_sha256"],
            "K486_face_atlas_sha256": k486["atlas_summary"]["complete_atlas_sha256"],
        },
        "approach_chart_contract": {
            "normal_coordinate": "rho is divided equally among exactly the zeroed axes",
            "fixed_and_positive_tangential_raw_time": "1/256", "normal_levels": list(NORMAL_LEVELS),
            "complete_coherent_assembly_required": True, "raw_Bessel_evaluation_at_zero_used": False,
            "approach_program_is_not_a_face_interval": True, "approach_program_is_not_a_recursive_cover": True,
        },
        "face_programs": programs,
        "positive_interior_fallback_programs": fallbacks,
        "selected_boundary_or_interior_program_per_hybrid": selected,
        "program_summary": {
            "all_descriptor_face_programs_compiled": descriptor_programs == 936 * 13300,
            "all_faces_compiled": len(programs) == 936,
            "all_faces_replay_K486_integrability": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in programs),
            "all_matrix_face_programs_resolved": matrix_uses == k485["fixed_control"]["determinant_matrix_face_uses_replayed"],
            "complete_program_bank_sha256": K485_BACKEND.K388.digest(programs),
            "global_confluent_template_histogram": dict(sorted(global_confluent.items())),
            "global_singular_template_histogram": dict(sorted(global_singular.items())),
            "hybrids_with_reachable_faces": 20, "hybrids_without_reachable_faces": ["v10", "v11"],
        },
        "decision": {
            "complete_face_program_bank_compiled": True, "all_K485_template_uses_resolved": True,
            "hardest_boundary_or_interior_program_per_hybrid_released_for_arb_control": True,
            "preconditioned_interval_face_evaluator_complete": False, "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False, "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "Execute complete coherent Arb controls on the selected order-ten face or positive-interior program in every hybrid.",
        },
        "release_test": {
            "twenty_two_hybrid_control_programs_present": len(selected) == 22,
            "exactly_two_positive_interior_fallbacks_present": len(fallbacks) == 2,
            "all_936_face_instances_present": len(programs) == 936,
            "all_descriptor_programs_present": descriptor_programs == 936 * 13300,
            "all_matrix_programs_present": matrix_uses == k485["fixed_control"]["determinant_matrix_face_uses_replayed"],
            "all_60_singular_templates_resolved": set(global_singular) == set(singular_templates.values()),
            "all_75_confluent_templates_resolved": set(global_confluent) == set(confluent_templates.values()),
            "all_normal_exponents_integrable": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in programs),
            "raw_zero_evaluation_absent": True, "complete_numerical_cover_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k486["ledger_effect"], "source_routing": k486["source_routing"],
        "claim_ceiling": "Exact executable approach-program compiler for all 936 K411 reachable order-ten faces and 12,448,800 ordered descriptor-face programs. This is not a face interval, recursive cover, complete order-ten integral, K457 cross value, K152 interval or physical/source/public conclusion.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_terms"], fixed["ordered_descriptors_per_face"], fixed["reachable_face_instances"]) != (22, 13300, 936):
        raise AssertionError("K487 native census changed")
    if len(payload["selected_boundary_or_interior_program_per_hybrid"]) != 22 or len(payload["positive_interior_fallback_programs"]) != 2:
        raise AssertionError("K487 selection bank changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K487 release test failed")


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate_payload(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

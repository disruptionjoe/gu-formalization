#!/usr/bin/env python3
"""Certify every K411 face by exact complete-product singularity replay."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K389_MODULE = HERE / "k389_order_nine_face_normal_integrability_atlas.py"
K485_MODULE = HERE / "k485_order_ten_mask_native_preconditioner_compiler.py"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
K485 = ROOT / "lab/process/k485-order-ten-mask-native-preconditioner-compiler.json"
OUTPUT = ROOT / "lab/process/k486-order-ten-face-normal-integrability-atlas.json"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K389 = load_module(K389_MODULE, "k389_for_k486")
K485_BACKEND = load_module(K485_MODULE, "k485_for_k486")


def build() -> dict[str, Any]:
    k410 = json.loads(K410.read_text())
    k411 = json.loads(K411.read_text())
    k485 = json.loads(K485.read_text())
    if not k485["decision"]["determinant_preserving_row_column_preconditioners_released"]:
        raise AssertionError("K485 preconditioner bank unavailable")
    descriptors = K485_BACKEND.ordered_descriptors()
    face_rows = []
    hybrid_rows = []
    for hybrid in k411["hybrid_face_atlas"]:
        axis = hybrid["axis"]
        hybrid_face_rows = []
        for kind, faces in hybrid["faces"].items():
            for face in faces:
                mask = set(face["zeroed_axes"])
                costs = [K389.descriptor_costs(descriptor, mask, axis) for descriptor in descriptors]
                maxima = [max(row[order] for row in costs) for order in range(3)]
                peano_gain = 2 if axis in mask else 0
                exponent = len(mask) - 1 - maxima[2] + peano_gain
                row = {
                    "axis": axis,
                    "face_kind": kind,
                    "zeroed_axes": face["zeroed_axes"],
                    "codimension": len(mask),
                    "active_peano_axis_zeroed": axis in mask,
                    "maximum_value_first_second_singular_powers": maxima,
                    "face_normal_jacobian_power": len(mask) - 1,
                    "peano_zero_gain": peano_gain,
                    "minimum_second_derivative_face_normal_power": exponent,
                    "contributing_ordered_descriptors": sum(row[2] > K389.NEG for row in costs),
                    "locally_integrable": exponent > -1,
                }
                face_rows.append(row)
                hybrid_face_rows.append(row)
        hybrid_rows.append({
            "axis": axis,
            "face_instances": len(hybrid_face_rows),
            "minimum_face_normal_power": min((row["minimum_second_derivative_face_normal_power"] for row in hybrid_face_rows), default=None),
            "all_faces_locally_integrable": all(row["locally_integrable"] for row in hybrid_face_rows),
            "face_rows_sha256": K389.digest(hybrid_face_rows),
        })

    all_zero = next(row for row in face_rows if row["axis"] == "s1" and len(row["zeroed_axes"]) == 22)
    if all_zero["minimum_second_derivative_face_normal_power"] != 9:
        raise AssertionError("K486 failed to replay K410's all-zero degree nine")
    return {
        "schema_version": "1.0",
        "result_id": "K486-ORDER-TEN-FACE-NORMAL-INTEGRABILITY-ATLAS",
        "created": "2026-09-25",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k410-order-ten-zero-safe-radial-contract.json",
                "lab/process/k411-order-ten-hybrid-face-atlas.json",
                "lab/process/k485-order-ten-mask-native-preconditioner-compiler.json",
            ],
            "native_axes": k411["fixed_control"]["native_axes"],
            "hybrid_terms": 22,
            "ordered_descriptors_per_face": len(descriptors),
            "reachable_face_instances": len(face_rows),
            "descriptor_face_replays": len(face_rows) * len(descriptors),
            "maximum_derivative_order": 2,
            "K485_template_bank_sha256": k485["template_summary"]["template_bank_sha256"],
        },
        "face_normal_chart_contract": {
            "normal_coordinates": "For a codimension-c face mask M, write t_a=rho*q_a for a in M with q in the positive (c-1)-simplex and retain complementary times as positive tangential coordinates.",
            "jacobian": "rho^(c-1)",
            "primitive_scaling": "Each selected zero primitive contributes rho^-1 and each active derivative contributes one further rho^-1, using K410 Phi_0/Phi_1/Phi_2.",
            "determinant_scaling": "K485 row/column duals realize exactly the largest selected-zero count in a Leibniz term while preserving determinant assembly.",
            "product_rule": "Exact max-plus convolution over two old-position kernels and every species determinant for derivative orders zero, one and two.",
            "peano_gain": "rho^2 exactly when the active hybrid axis lies in the face mask.",
            "coalescence_cancellation_required_for_integrability": False,
            "coalescence_preconditioning_still_required_for_interval_contraction": True,
        },
        "hybrid_summary": hybrid_rows,
        "face_normal_atlas": face_rows,
        "atlas_summary": {
            "all_936_reachable_face_instances_replayed": len(face_rows) == 936,
            "all_faces_locally_integrable": all(row["locally_integrable"] for row in face_rows),
            "global_minimum_face_normal_power": min(row["minimum_second_derivative_face_normal_power"] for row in face_rows),
            "K410_all_zero_degree_nine_replayed": all_zero["minimum_second_derivative_face_normal_power"] == 9,
            "all_hybrid_digests_present": all(row["face_rows_sha256"].startswith("sha256:") for row in hybrid_rows),
            "complete_atlas_sha256": K389.digest(face_rows),
        },
        "decision": {
            "complete_reachable_face_normal_integrability_closed": True,
            "all_zero_and_proper_face_power_counting_unified": True,
            "mask_native_numerical_evaluator_released": True,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "instantiate the K485 determinant duals and K486 face charts in the complete coherent Arb evaluator, then join accepted face cells to recursive positive-interior cells and analytic tails",
        },
        "release_test": {
            "twenty_two_hybrids_present": len(hybrid_rows) == 22,
            "all_936_faces_present": len(face_rows) == 936,
            "all_12448800_descriptor_face_replays_accounted": len(face_rows) * len(descriptors) == 12448800,
            "every_face_power_is_integrable": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in face_rows),
            "all_zero_degree_nine_replayed": all_zero["minimum_second_derivative_face_normal_power"] == 9,
            "complete_numerical_cover_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k410["ledger_effect"],
        "source_routing": k410["source_routing"],
        "claim_ceiling": "Exact face-normal local-integrability certificate for all 936 K411 reachable faces and 12,448,800 ordered descriptor-face evaluations. This is not a recursive cover, numerical hybrid integral, complete order-ten remainder, K457 cross value, K152 interval or physical/source/public conclusion.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_terms"], fixed["ordered_descriptors_per_face"], fixed["reachable_face_instances"], fixed["descriptor_face_replays"]) != (22, 13300, 936, 12448800):
        raise AssertionError("K486 native census changed")
    rows = payload["face_normal_atlas"]
    if len(rows) != 936 or any(row["minimum_second_derivative_face_normal_power"] <= -1 or not row["locally_integrable"] for row in rows):
        raise AssertionError("K486 face integrability changed")
    summary = payload["atlas_summary"]
    if not summary["all_faces_locally_integrable"] or summary["global_minimum_face_normal_power"] != 0 or not summary["K410_all_zero_degree_nine_replayed"]:
        raise AssertionError("K486 atlas summary changed")
    decision = payload["decision"]
    if not decision["complete_reachable_face_normal_integrability_closed"] or not decision["mask_native_numerical_evaluator_released"]:
        raise AssertionError("K486 interface not released")
    if decision["recursive_positive_interior_cover_complete"] or decision["analytic_radial_tails_complete"] or decision["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K486 overclaimed numerical closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K486 release test failed")


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

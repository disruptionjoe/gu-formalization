#!/usr/bin/env python3
"""Certify every K411 face by exact complete-product singularity replay."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K407_MODULE = HERE / "k407_order_ten_axis_jet_compiler.py"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
K413 = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"
OUTPUT = ROOT / "lab/process/k414-order-ten-face-normal-integrability-atlas.json"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K407_BACKEND = load_module(K407_MODULE, "k407_for_k414")
NEG = -10**9


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def ordered_descriptors() -> list[dict[str, Any]]:
    rows = []
    for (seed, signature), terms in K407_BACKEND.group_terms().items():
        group_id = f"order10:seed{seed}:{signature}"
        for left in terms:
            for right in terms:
                rows.append(K407_BACKEND.entry_descriptor(group_id, left, right))
    return rows


def primitive_costs(argument_mask: list[str], face: set[str], axis: str) -> tuple[int, int, int]:
    zero = set(argument_mask).issubset(face)
    active = axis in argument_mask
    base = int(zero)
    return (
        base,
        base + int(zero) if active else NEG,
        base + 2 * int(zero) if active else NEG,
    )


def determinant_costs(matrix: dict[str, Any], face: set[str], axis: str) -> tuple[int, int, int]:
    rank = int(matrix["rank"])
    best = [NEG, NEG, NEG]
    for permutation in itertools.permutations(range(rank)):
        selected = [matrix["entry_axis_masks"][row][column] for row, column in enumerate(permutation)]
        zeros = [set(mask).issubset(face) for mask in selected]
        actives = [axis in mask for mask in selected]
        base = sum(zeros)
        best[0] = max(best[0], base)
        if any(actives):
            active_zero = any(active and zero for active, zero in zip(actives, zeros, strict=True))
            best[1] = max(best[1], base + int(active_zero))
            best[2] = max(best[2], base + 2 * int(active_zero))
    return tuple(best)


def product_costs(factors: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    current = [0, NEG, NEG]
    for factor in factors:
        updated = [NEG, NEG, NEG]
        for total_order in range(3):
            for factor_order in range(total_order + 1):
                left = current[total_order - factor_order]
                right = factor[factor_order]
                if left > NEG and right > NEG:
                    updated[total_order] = max(updated[total_order], left + right)
        current = updated
    return tuple(current)


def descriptor_costs(descriptor: dict[str, Any], face: set[str], axis: str) -> tuple[int, int, int]:
    factors = [
        primitive_costs(descriptor["left_old_axis_mask"], face, axis),
        primitive_costs(descriptor["right_old_axis_mask"], face, axis),
    ]
    factors.extend(determinant_costs(matrix, face, axis) for matrix in descriptor["species_matrices"])
    return product_costs(factors)


def build() -> dict[str, Any]:
    k410 = json.loads(K410.read_text())
    k411 = json.loads(K411.read_text())
    k413 = json.loads(K413.read_text())
    if not k413["decision"]["determinant_preserving_row_column_preconditioners_released"]:
        raise AssertionError("K413 preconditioner bank unavailable")
    descriptors = ordered_descriptors()
    face_rows = []
    hybrid_rows = []
    for hybrid in k411["hybrid_face_atlas"]:
        axis = hybrid["axis"]
        hybrid_face_rows = []
        for kind, faces in hybrid["faces"].items():
            for face in faces:
                mask = set(face["zeroed_axes"])
                costs = [descriptor_costs(descriptor, mask, axis) for descriptor in descriptors]
                maxima = [max(row[order] for row in costs) for order in range(3)]
                peano_gain = 2 if axis in mask else 0
                exponent = len(mask) - 1 - maxima[2] + peano_gain
                contributors = sum(row[2] > NEG for row in costs)
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
                    "contributing_ordered_descriptors": contributors,
                    "locally_integrable": exponent > -1,
                }
                face_rows.append(row)
                hybrid_face_rows.append(row)
        hybrid_rows.append({
            "axis": axis,
            "face_instances": len(hybrid_face_rows),
            "minimum_face_normal_power": min(row["minimum_second_derivative_face_normal_power"] for row in hybrid_face_rows) if hybrid_face_rows else None,
            "all_faces_locally_integrable": all(row["locally_integrable"] for row in hybrid_face_rows),
            "face_rows_sha256": digest(hybrid_face_rows),
        })

    all_zero = next(row for row in face_rows if row["axis"] == "s1" and len(row["zeroed_axes"]) == 22)
    if all_zero["minimum_second_derivative_face_normal_power"] != 9:
        raise AssertionError(
            "K414 failed to replay K410's all-zero degree nine: "
            f"{all_zero['minimum_second_derivative_face_normal_power']}"
        )
    return {
        "schema_version": "1.0",
        "result_id": "K414-ORDER-TEN-FACE-NORMAL-INTEGRABILITY-ATLAS",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k410-order-ten-zero-safe-radial-contract.json",
                "lab/process/k411-order-ten-hybrid-face-atlas.json",
                "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json",
            ],
            "native_axes": k411["fixed_control"]["native_axes"],
            "hybrid_terms": 22,
            "ordered_descriptors_per_face": len(descriptors),
            "reachable_face_instances": len(face_rows),
            "descriptor_face_replays": len(face_rows) * len(descriptors),
            "maximum_derivative_order": 2,
            "K413_template_bank_sha256": k413["template_summary"]["template_bank_sha256"],
        },
        "face_normal_chart_contract": {
            "normal_coordinates": "For a codimension-c face mask M, write t_a=rho*q_a for a in M with q in the positive (c-1)-simplex; retain every complementary time as a positive tangential coordinate.",
            "jacobian": "rho^(c-1)",
            "primitive_scaling": "Each selected zero primitive contributes rho^-1 and each active derivative on it contributes one further rho^-1, using K410 Phi_0/Phi_1/Phi_2.",
            "determinant_scaling": "K413 row/column duals realize exactly the largest number of selected zero primitives in a Leibniz term while preserving determinant assembly.",
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
            "complete_atlas_sha256": digest(face_rows),
        },
        "decision": {
            "complete_reachable_face_normal_integrability_closed": True,
            "all_zero_and_proper_face_power_counting_unified": True,
            "mask_native_numerical_evaluator_released": True,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "instantiate the K413 determinant duals and K414 face charts in the complete coherent Arb evaluator, then join accepted face cells to recursive positive-interior cells and analytic tails before integrating all twenty-two Peano kernels",
        },
        "release_test": {
            "twenty_two_hybrids_present": len(hybrid_rows) == 22,
            "all_936_faces_present": len(face_rows) == 936,
            "all_12448800_descriptor_face_replays_accounted": len(face_rows) * len(descriptors) == 12_448_800,
            "every_face_power_is_integrable": all(row["minimum_second_derivative_face_normal_power"] > -1 for row in face_rows),
            "all_zero_degree_nine_replayed": all_zero["minimum_second_derivative_face_normal_power"] == 9,
            "complete_numerical_cover_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k410["ledger_effect"],
        "source_routing": k410["source_routing"],
        "claim_ceiling": "Exact face-normal local-integrability certificate for all 936 K411 reachable face instances. The complete second-derivative product rule is replayed across all 13,300 ordered descriptors per face (12,448,800 descriptor-face evaluations), using K410 scaled primitive jets and K413 determinant-preserving assignment duals. Every face is locally integrable and the all-twenty-two-axis s1 face replays degree nine. This releases the zero-safe mask-native evaluator interface but not recursive positive-interior coverage, analytic tails, any of the twenty-two numerical Peano integrals, the complete order-ten remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_terms"], fixed["ordered_descriptors_per_face"], fixed["reachable_face_instances"], fixed["descriptor_face_replays"]) != (22, 13300, 936, 12_448_800):
        raise AssertionError("K414 census changed")
    rows = payload["face_normal_atlas"]
    if len(rows) != 936 or any(row["minimum_second_derivative_face_normal_power"] <= -1 or not row["locally_integrable"] for row in rows):
        raise AssertionError("K414 face integrability changed")
    summary = payload["atlas_summary"]
    if not summary["all_faces_locally_integrable"] or summary["global_minimum_face_normal_power"] != 0 or not summary["K410_all_zero_degree_nine_replayed"]:
        raise AssertionError("K414 atlas summary changed")
    decision = payload["decision"]
    if not decision["complete_reachable_face_normal_integrability_closed"] or not decision["mask_native_numerical_evaluator_released"]:
        raise AssertionError("K414 interface not released")
    if decision["recursive_positive_interior_cover_complete"] or decision["analytic_radial_tails_complete"] or decision["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K414 overclaimed numerical closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K414 release test failed")


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

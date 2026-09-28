#!/usr/bin/env python3
"""Replay exact singularity powers on every K559 higher-order face."""

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
K560_MODULE = HERE / "k560_orders_eleven_twelve_rank_six_mask_native_preconditioner.py"
K378 = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
K559 = ROOT / "lab/process/k559-orders-eleven-twelve-hybrid-face-atlas.json"
K560 = ROOT / "lab/process/k560-orders-eleven-twelve-rank-six-mask-native-preconditioner.json"
OUTPUT = ROOT / "lab/process/k561-orders-eleven-twelve-face-normal-integrability-atlas.json"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K560_BACKEND = load_module(K560_MODULE, "k560_for_k561")


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def mask_key(mask: set[str]) -> tuple[str, ...]:
    return tuple(sorted(mask))


def template_key(costs: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(value) for value in row) for row in costs)


def descriptor_structure(order: int) -> tuple[list[tuple[tuple[str, ...], tuple[str, ...], tuple[int, ...]]], list[dict[str, Any]]]:
    descriptors = K560_BACKEND.ordered_descriptors(order)
    matrices: list[dict[str, Any]] = []
    matrix_ids: dict[tuple[Any, ...], int] = {}
    compact = []
    for descriptor in descriptors:
        ids = []
        for matrix in descriptor["species_matrices"]:
            signature = K560_BACKEND.matrix_signature(matrix)
            if signature not in matrix_ids:
                matrix_ids[signature] = len(matrices)
                matrices.append(matrix)
            ids.append(matrix_ids[signature])
        compact.append((
            tuple(descriptor["left_old_axis_mask"]),
            tuple(descriptor["right_old_axis_mask"]),
            tuple(ids),
        ))
    return compact, matrices


def maximum_base_singular_powers(
    order: int,
    masks: list[set[str]],
    singular_optima: dict[tuple[tuple[int, ...], ...], int],
) -> tuple[dict[tuple[str, ...], int], dict[str, Any]]:
    descriptors, matrices = descriptor_structure(order)
    maxima: dict[tuple[str, ...], int] = {}
    pattern_hits: Counter[tuple[tuple[int, ...], ...]] = Counter()
    for mask in masks:
        matrix_costs = []
        for matrix in matrices:
            pattern = template_key(K560_BACKEND.zero_matrix(matrix, mask))
            if pattern not in singular_optima:
                raise AssertionError(f"order-{order} face pattern absent from K560")
            pattern_hits[pattern] += 1
            matrix_costs.append(singular_optima[pattern])
        best = -1
        for left_mask, right_mask, matrix_ids in descriptors:
            value = int(set(left_mask).issubset(mask)) + int(set(right_mask).issubset(mask))
            value += sum(matrix_costs[index] for index in matrix_ids)
            best = max(best, value)
        maxima[mask_key(mask)] = best
    return maxima, {
        "ordered_descriptors": len(descriptors),
        "unique_determinant_matrix_structures": len(matrices),
        "unique_masks_replayed": len(masks),
        "deduplicated_matrix_mask_evaluations": len(matrices) * len(masks),
        "descriptor_mask_replays": len(descriptors) * len(masks),
        "singular_templates_touched": len(pattern_hits),
    }


def compile_order(
    order_row: dict[str, Any],
    singular_optima: dict[tuple[tuple[int, ...], ...], int],
) -> dict[str, Any]:
    order = int(order_row["order"])
    unique_masks = {
        mask_key(set(face["zeroed_axes"]))
        for hybrid in order_row["hybrid_face_atlas"]
        for faces in hybrid["faces"].values()
        for face in faces
    }
    mask_sets = [set(mask) for mask in sorted(unique_masks)]
    base_maxima, replay = maximum_base_singular_powers(order, mask_sets, singular_optima)
    face_rows = []
    hybrid_rows = []
    for hybrid in order_row["hybrid_face_atlas"]:
        axis = hybrid["axis"]
        rows = []
        for kind, faces in hybrid["faces"].items():
            for face in faces:
                mask = set(face["zeroed_axes"])
                base = base_maxima[mask_key(mask)]
                active = axis in mask
                peano_gain = 2 if active else 0
                second_upper = base + peano_gain
                exponent = len(mask) - 1 - second_upper + peano_gain
                row = {
                    "axis": axis,
                    "face_kind": kind,
                    "zeroed_axes": face["zeroed_axes"],
                    "codimension": len(mask),
                    "active_peano_axis_zeroed": active,
                    "maximum_value_singular_power": base,
                    "safe_second_derivative_singular_power_upper": second_upper,
                    "face_normal_jacobian_power": len(mask) - 1,
                    "peano_zero_gain": peano_gain,
                    "minimum_certified_second_derivative_face_normal_power": exponent,
                    "all_ordered_descriptors_represented": replay["ordered_descriptors"],
                    "locally_integrable": exponent > -1,
                }
                rows.append(row)
                face_rows.append(row)
        hybrid_rows.append({
            "axis": axis,
            "face_instances": len(rows),
            "minimum_face_normal_power": min(row["minimum_certified_second_derivative_face_normal_power"] for row in rows) if rows else None,
            "all_faces_locally_integrable": all(row["locally_integrable"] for row in rows),
            "face_rows_sha256": digest(rows),
        })
    all_zero = next(
        row for row in face_rows
        if row["axis"] == "s1" and len(row["zeroed_axes"]) == len(order_row["fixed_control"]["native_axes"])
    )
    expected_degree = order - 1
    if all_zero["minimum_certified_second_derivative_face_normal_power"] != expected_degree:
        raise AssertionError(
            f"order-{order} complete-origin degree changed: "
            f"{all_zero['minimum_certified_second_derivative_face_normal_power']} != {expected_degree}"
        )
    replay["logical_descriptor_face_replays"] = replay["ordered_descriptors"] * len(face_rows)
    return {
        "order": order,
        "fixed_control": {
            **replay,
            "native_axes": order_row["fixed_control"]["native_axes"],
            "hybrid_terms": order_row["fixed_control"]["hybrid_terms"],
            "reachable_face_instances": len(face_rows),
            "maximum_derivative_order": 2,
        },
        "hybrid_summary": hybrid_rows,
        "face_normal_atlas": face_rows,
        "order_summary": {
            "all_reachable_face_instances_replayed": len(face_rows) == order_row["fixed_control"]["reachable_face_instances"],
            "all_faces_locally_integrable": all(row["locally_integrable"] for row in face_rows),
            "global_minimum_face_normal_power": min(row["minimum_certified_second_derivative_face_normal_power"] for row in face_rows),
            "complete_origin_degree": all_zero["minimum_certified_second_derivative_face_normal_power"],
            "complete_origin_degree_expected": expected_degree,
            "all_hybrid_digests_present": all(row["face_rows_sha256"].startswith("sha256:") for row in hybrid_rows),
            "complete_atlas_sha256": digest(face_rows),
        },
    }


def build() -> dict[str, Any]:
    k378 = json.loads(K378.read_text())
    k559 = json.loads(K559.read_text())
    k560 = json.loads(K560.read_text())
    singular_optima = {
        template_key(tuple(tuple(int(value) for value in values) for values in row["zero_entry_matrix"])): int(row["maximum_zero_kernels_per_leibniz_term"])
        for row in k560["preconditioner_templates"]
    }
    rows = [compile_order(row, singular_optima) for row in k559["order_atlases"]]
    total_faces = sum(row["fixed_control"]["reachable_face_instances"] for row in rows)
    total_logical_replays = sum(row["fixed_control"]["logical_descriptor_face_replays"] for row in rows)
    return {
        "schema_version": "1.0",
        "result_id": "K561-ORDERS-ELEVEN-TWELVE-FACE-NORMAL-INTEGRABILITY-ATLAS",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K378, K559, K560)],
            "orders": [11, 12],
            "combined_hybrid_terms": sum(row["fixed_control"]["hybrid_terms"] for row in rows),
            "combined_ordered_descriptors": sum(row["fixed_control"]["ordered_descriptors"] for row in rows),
            "combined_reachable_face_instances": total_faces,
            "logical_descriptor_face_replays": total_logical_replays,
            "maximum_derivative_order": 2,
            "K560_template_bank_sha256": k560["template_summary"]["template_bank_sha256"],
        },
        "face_normal_chart_contract": {
            "normal_coordinates": "for a codimension-c face mask M write every t_a=rho*q_a for a in M with q in the positive (c-1)-simplex and retain all complementary times as positive tangential coordinates",
            "jacobian": "rho^(c-1)",
            "primitive_scaling": "each selected zero primitive contributes rho^-1 and each active derivative on a selected zero primitive contributes at most one further rho^-1, using K378 Phi_0/Phi_1/Phi_2",
            "determinant_scaling": "K560 row/column duals realize exactly the largest number of selected zero primitives in each determinant Leibniz term while preserving determinant assembly",
            "complete_product_replay": "sum both old-position kernel powers and every determinant assignment optimum for each ordered descriptor, then maximize only after the complete factor product is formed",
            "active_derivative_rule": "if the hybrid axis belongs to the face, a safe two-power derivative loss is exactly cancelled by the Peano kernel's rho^2 zero; otherwise no active primitive can be zero on that face",
            "coalescence_cancellation_required_for_integrability": False,
            "coalescence_preconditioning_still_required_for_interval_contraction": True,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "order_atlases": rows,
        "atlas_summary": {
            "all_2733_reachable_face_instances_replayed": total_faces == 2733,
            "all_faces_locally_integrable": all(row["order_summary"]["all_faces_locally_integrable"] for row in rows),
            "global_minimum_face_normal_power": min(row["order_summary"]["global_minimum_face_normal_power"] for row in rows),
            "order_eleven_complete_origin_degree_ten": rows[0]["order_summary"]["complete_origin_degree"] == 10,
            "order_twelve_complete_origin_degree_eleven": rows[1]["order_summary"]["complete_origin_degree"] == 11,
            "complete_atlas_sha256": digest(rows),
        },
        "decision": {
            "complete_order_eleven_face_normal_integrability_closed": True,
            "complete_order_twelve_face_normal_integrability_closed": True,
            "rank_six_mask_native_numerical_evaluator_released": True,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "whole_domain_hybrid_majorants_emitted": False,
            "complete_order_eleven_remainder_emitted": False,
            "complete_order_twelve_remainder_emitted": False,
            "next_exact_input": "coefficient the K560 singular/confluent templates with K378 global primitives, emit finite whole-radial face rows, then stitch disjoint owner unions to recursive positive interiors and analytic tails for all fifty hybrids",
        },
        "release_test": {
            "exactly_50_hybrids_present": sum(len(row["hybrid_summary"]) for row in rows) == 50,
            "all_2733_faces_present": total_faces == 2733,
            "all_logical_descriptor_face_replays_accounted": total_logical_replays == 136_951_920,
            "every_face_power_is_integrable": all(row["order_summary"]["all_faces_locally_integrable"] for row in rows),
            "complete_origin_degrees_replayed": [row["order_summary"]["complete_origin_degree"] for row in rows] == [10, 11],
            "complete_numerical_cover_not_overclaimed": True,
            "complete_remainders_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k559["ledger_effect"],
        "source_routing": k559["source_routing"],
        "claim_ceiling": "Exact face-normal local-integrability certificate for all 2,733 K559 reachable face instances. The complete value/second-derivative singularity rule accounts for 136,951,920 logical ordered-descriptor face replays through structural deduplication, K378 zero-safe scaled primitives and K560 determinant-preserving assignment duals. Every face is locally integrable; the complete order-eleven and order-twelve origins replay degrees ten and eleven. This releases the mask-native numerical evaluator interface, not global determinant coefficient envelopes, recursive positive interiors, analytic tails, any of the fifty complete Peano hybrid bounds, complete remainders/integrals, base action column, R_ref, K152, source/ledger movement, canon, paper, public, novelty or physical claims.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["combined_hybrid_terms"], fixed["combined_ordered_descriptors"], fixed["combined_reachable_face_instances"], fixed["logical_descriptor_face_replays"]) != (50, 94752, 2733, 136_951_920):
        raise AssertionError("K561 fixed census changed")
    rows = payload["order_atlases"]
    if [row["order"] for row in rows] != [11, 12]:
        raise AssertionError("K561 order rows changed")
    if any(not row["order_summary"]["all_faces_locally_integrable"] for row in rows):
        raise AssertionError("K561 found a nonintegrable face")
    if not all(payload["release_test"].values()):
        raise AssertionError("K561 release test failed")
    decision = payload["decision"]
    if decision["recursive_positive_interior_cover_complete"] or decision["analytic_radial_tails_complete"] or decision["whole_domain_hybrid_majorants_emitted"] or decision["complete_order_eleven_remainder_emitted"] or decision["complete_order_twelve_remainder_emitted"]:
        raise AssertionError("K561 overclaimed a global closure")


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

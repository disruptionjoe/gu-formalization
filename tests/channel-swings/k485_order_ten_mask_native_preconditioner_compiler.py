#!/usr/bin/env python3
"""Compile exact determinant-preserving preconditioners for K411 faces."""

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
K388_MODULE = HERE / "k388_order_nine_mask_native_preconditioner_compiler.py"
K407_MODULE = HERE / "k407_order_ten_axis_jet_compiler.py"
K407 = ROOT / "lab/process/k407-order-ten-axis-jet-compiler.json"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
OUTPUT = ROOT / "lab/process/k485-order-ten-mask-native-preconditioner-compiler.json"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K388 = load_module(K388_MODULE, "k388_for_k485")
K407_BACKEND = load_module(K407_MODULE, "k407_for_k485")


def ordered_descriptors() -> list[dict[str, Any]]:
    rows = []
    for (seed, signature), terms in K407_BACKEND.group_terms().items():
        group_id = f"order10:seed{seed}:{signature}"
        for left in terms:
            for right in terms:
                rows.append(K407_BACKEND.entry_descriptor(group_id, left, right))
    return rows


def build() -> dict[str, Any]:
    k407 = json.loads(K407.read_text())
    k410 = json.loads(K410.read_text())
    k411 = json.loads(K411.read_text())
    descriptors = ordered_descriptors()
    if len(descriptors) != 13300:
        raise AssertionError("K407 ordered descriptor census changed")
    if not k410["decision"]["zero_safe_scaled_derivative_bank_emitted"]:
        raise AssertionError("K410 scaled primitive bank unavailable")

    patterns = set()
    confluent_patterns = set()
    matrix_uses = 0
    face_instances = 0
    for hybrid in k411["hybrid_face_atlas"]:
        for faces in hybrid["faces"].values():
            for face in faces:
                face_instances += 1
                mask = set(face["zeroed_axes"])
                for descriptor in descriptors:
                    for matrix in descriptor["species_matrices"]:
                        patterns.add(K388.zero_matrix(matrix, mask))
                        confluent_patterns.add((
                            int(matrix["rank"]),
                            K388.coalescence_labels(matrix["row_positions"], "s", mask),
                            K388.coalescence_labels(matrix["column_positions"], "v", mask),
                        ))
                        matrix_uses += 1

    templates = [K388.template(costs) for costs in sorted(patterns, key=lambda item: (len(item), item))]
    confluent_templates = [K388.confluent_template(*pattern) for pattern in sorted(confluent_patterns)]
    rank_histogram = Counter(row["rank"] for row in templates)
    payload = {
        "schema_version": "1.0",
        "result_id": "K485-ORDER-TEN-MASK-NATIVE-PRECONDITIONER-COMPILER",
        "created": "2026-09-25",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k407-order-ten-axis-jet-compiler.json",
                "lab/process/k410-order-ten-zero-safe-radial-contract.json",
                "lab/process/k411-order-ten-hybrid-face-atlas.json",
            ],
            "ordered_descriptors": len(descriptors),
            "reachable_face_instances": face_instances,
            "determinant_matrix_face_uses_replayed": matrix_uses,
            "unique_preconditioner_templates": len(templates),
            "unique_confluent_templates": len(confluent_templates),
            "maximum_species_determinant_rank": 5,
            "K407_compiled_entry_interface_sha256": k407["compiled_entry_interface"]["sha256"],
            "K411_face_atlas_sha256": K388.digest(k411["hybrid_face_atlas"]),
        },
        "primitive_scaling_contract": {
            "definition": "Phi_d(w)=w^(d+1)*abs((2*K1)^(d)(w)) for d=0,1,2",
            "zero_limits": k410["scaled_bessel_bank"]["continuous_zero_limits"],
            "exact_rational_envelopes_ref": "lab/process/k410-order-ten-zero-safe-radial-contract.json#scaled_bessel_bank",
            "active_derivative_extra_face_power": "d powers beyond the base w^-1 singularity",
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "determinant_scaling_contract": {
            "rule": "Mark an entry one exactly when its cumulative-time argument mask is contained in the face. The assignment optimum is realized by exact binary row/column dual powers before interval determinant assembly.",
            "determinant_assembled_after_row_column_scaling": True,
            "permutationwise_absolute_enclosure_used_for_numerical_value": False,
            "assignment_duality_is_exact": True,
            "all_ordered_orientations_retained": True,
        },
        "preconditioner_templates": templates,
        "confluent_divided_difference_contract": {
            "rule": "Rows coalesce exactly when every intervening s-axis vanishes, and columns likewise for v; replace each repeated-node cluster by confluent divided differences before interval substitution.",
            "vandermonde_factors_extracted_before_interval_substitution": True,
            "templates": confluent_templates,
            "template_count": len(confluent_templates),
            "maximum_row_divided_difference_order": max(row["maximum_row_divided_difference_order"] for row in confluent_templates),
            "maximum_column_divided_difference_order": max(row["maximum_column_divided_difference_order"] for row in confluent_templates),
            "template_bank_sha256": K388.digest(confluent_templates),
        },
        "template_summary": {
            "rank_histogram": {str(rank): rank_histogram[rank] for rank in sorted(rank_histogram)},
            "maximum_determinant_rank": max(rank_histogram),
            "all_strong_duality_checks_pass": all(row["strong_duality_verified"] for row in templates),
            "all_uses_reduce_to_finite_template_bank": matrix_uses > 0 and len(templates) == 60,
            "template_bank_sha256": K388.digest({"singular": templates, "confluent": confluent_templates}),
        },
        "decision": {
            "all_reachable_proper_face_matrix_patterns_compiled": True,
            "determinant_preserving_row_column_preconditioners_released": True,
            "complete_face_normal_integrability_emitted": False,
            "recursive_numerical_cover_complete": False,
            "next_exact_input": "replay the complete second-derivative product rule across all 13,300 ordered descriptors on every K411 face using these determinant duals and K410 primitive jets",
        },
        "release_test": {
            "all_60_singular_templates_present": len(templates) == 60,
            "ranks_one_through_five_present": sorted(rank_histogram) == [1, 2, 3, 4, 5],
            "all_75_confluent_templates_present": len(confluent_templates) == 75,
            "all_duals_match_primal_assignments": all(row["dual_sum"] == row["maximum_zero_kernels_per_leibniz_term"] for row in templates),
            "all_13300_ordered_descriptors_replayed": len(descriptors) == 13300,
            "all_936_reachable_faces_replayed": face_instances == 936,
            "raw_zero_bessel_calls_absent": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k411["ledger_effect"],
        "source_routing": k411["source_routing"],
        "claim_ceiling": "Exact finite compiler for all determinant zero and coalescence patterns induced by K411's 936 reachable order-ten faces across 13,300 ordered descriptors. This is not a face integrability result, recursive cover, complete order-ten integral, K457 cross value, K152 interval or physical/source/public conclusion.",
    }
    return payload


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    actual = (
        fixed["ordered_descriptors"], fixed["reachable_face_instances"],
        fixed["unique_preconditioner_templates"], fixed["unique_confluent_templates"],
    )
    if actual != (13300, 936, 60, 75):
        raise AssertionError("K485 native census changed")
    if not payload["template_summary"]["all_strong_duality_checks_pass"]:
        raise AssertionError("K485 assignment duality failed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K485 release test failed")
    if payload["decision"]["complete_face_normal_integrability_emitted"] or payload["decision"]["recursive_numerical_cover_complete"]:
        raise AssertionError("K485 overclaimed downstream closure")


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

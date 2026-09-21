#!/usr/bin/env python3
"""Independent replay and hostile controls for K281."""

from __future__ import annotations

import copy
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k281_order_seven_size_four_outward_calculus.py")
MANIFEST = ROOT / "lab/process/k281-order-seven-size-four-outward-calculus.json"
ARTIFACT = ROOT / "explorations/conditional-build/k281-order-seven-size-four-outward-calculus-2026-09-21.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k281_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K281 = load_solver()


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    total = Fraction(0)
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(len(matrix))
            for j in range(i + 1, len(matrix))
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


EXPECTED_JETS = {
    "a0": ("1*1", "0"),
    "a1": ("0", "-s"),
    "a2": ("s", "-s"),
    "a3": ("s", "-s^2"),
    "a4": ("s^2 - s", "-2*s^2"),
    "a5": ("2*s^2 + 2*s", "-s^3 + s^2"),
    "a6": ("s^3 - 3*s^2 - 6*s", "-3*s^3 - 3*s^2"),
}


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    theorem = data.get("exact_scaled_jet_theorem", {})
    spine = data.get("arb_coalescent_certificate", {})
    outward = data.get("outward_gap_stratified_certificate", {})
    faces = data.get("size_four_noncoalescent_face_atlas", {})
    decision = data.get("decision", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if (
        fixed.get("patterns"), fixed.get("patterns_by_size"),
        fixed.get("nontrivial_occurrences"), fixed.get("gram_entries"), fixed.get("groups")
    ) != (98, {"2": 72, "3": 25, "4": 1}, 996, 408, 16):
        failures.append("source_census")
    observed_jets = {
        key: (row.get("q_coefficient"), row.get("K0_coefficient"))
        for key, row in theorem.get("jet_polynomials", {}).items()
    }
    if observed_jets != EXPECTED_JETS or theorem.get("maximum_derivative_order") != 6:
        failures.append("jet_recurrence")
    if spine.get("tested_radii") != 199 or len(spine.get("dyadic_rows", [])) != 199:
        failures.append("dyadic_count")
    if spine.get("all_scaled_R4_balls_strictly_positive") is not True:
        failures.append("coalescent_positivity")
    if spine.get("all_raw_hankel_balls_overlap_scaled_balls") is not True:
        failures.append("raw_scaled_overlap")
    masks = faces.get("masks", [])
    observed_masks = {tuple(row.get("active", [])) for row in masks}
    labels = ("r0", "r1", "r2", "c0", "c1", "c2")
    expected_masks = {
        tuple(labels[index] for index in range(6) if mask & (1 << index))
        for mask in range(1, 64)
    }
    if faces.get("face_mask_count") != 63 or observed_masks != expected_masks:
        failures.append("face_masks")
    controls = faces.get("exact_controls", {})
    if controls.get("interiorized_exact_controls_passed") != 63:
        failures.append("face_controls")
    if outward.get("size_four_positive_union_certified") is not False:
        failures.append("failed_transfer_ceiling")
    for stratum in (outward.get("low_radial", {}), outward.get("high_radial", {})):
        if stratum.get("gap_radius") is not None or stratum.get("cell_count") != 0:
            failures.append("invented_stratum")
    required_true = (
        "exact_R4_scaled_jet_normal_form_banked",
        "directed_arb_dyadic_coalescent_spine_banked",
        "size_four_63_mask_face_atlas_serialized",
    )
    required_false = (
        "gap_stratified_R4_value_interval_serialized",
        "all_98_patterns_propagated_on_certified_union",
        "all_996_occurrences_propagated_on_certified_union",
        "arbitrary_gap_ratio_domain_covered",
        "mixed_Duffy_derivative_envelopes_serialized",
        "determinant_preserving_Jacobi_error_serialized",
        "complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true):
        failures.append("release_true")
    if any(release.get(key) is not False for key in required_false):
        failures.append("release_false")
    if decision.get("size_four_gap_stratified_positive_union_banked") is not False:
        failures.append("decision_ceiling")
    if data.get("physical_or_source_selection") is not False:
        failures.append("physical_selection")
    if data.get("Born_prediction_or_confirmation_credit") is not False:
        failures.append("prediction_credit")
    if data.get("canon_paper_release_or_public_posture_move") is not False:
        failures.append("public_posture")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()):
        failures.append("ledger")
    return failures


def hostile_controls(data: dict[str, Any]) -> dict[str, bool]:
    mutations = (
        ("drop_radius", lambda d: d["arb_coalescent_certificate"]["dyadic_rows"].pop()),
        ("break_jet", lambda d: d["exact_scaled_jet_theorem"]["jet_polynomials"]["a6"].__setitem__("q_coefficient", "0")),
        ("drop_face", lambda d: d["size_four_noncoalescent_face_atlas"]["masks"].pop()),
        ("break_face_count", lambda d: d["size_four_noncoalescent_face_atlas"].__setitem__("face_mask_count", 62)),
        ("invent_union", lambda d: d["outward_gap_stratified_certificate"].__setitem__("size_four_positive_union_certified", True)),
        ("invent_interval", lambda d: d["release_test"].__setitem__("gap_stratified_R4_value_interval_serialized", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("complete_base_action_column_evaluated", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
    )
    results = {}
    for name, mutate in mutations:
        broken = copy.deepcopy(data)
        mutate(broken)
        results[name] = bool(manifest_failures(broken))
    return results


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    pascal = [
        [Fraction((-1) ** (row + column) * K281.math.comb(row + column, row)) for column in range(4)]
        for row in range(4)
    ]
    failures = manifest_failures(data)
    hostile = hostile_controls(data)
    checks = {
        "manifest_replay": not failures,
        "deterministic_producer_replay": K281.build() == data,
        "independent_pascal_limit": determinant(pascal) == 1,
        "dyadic_rows_serialized": len(data["arb_coalescent_certificate"]["dyadic_rows"]) == 199,
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "method_failure_not_theorem": "method failure" in text and "not a theorem of nonpositivity" in text,
        "claim_ceiling_preserved": "no action-column value" in text and "native K152 interval" in text,
        "all_hostile_mutations_rejected": all(hostile.values()),
    }
    payload = {
        "schema_version": "1.0",
        "producer_result_id": data.get("result_id"),
        "checks": checks,
        "manifest_failures": failures,
        "hostile_controls": hostile,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())

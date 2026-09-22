#!/usr/bin/env python3
"""Independent replay and hostile controls for K282."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k282_order_seven_shifted_face_center_calculus.py")
MANIFEST = ROOT / "lab/process/k282-order-seven-shifted-face-center-calculus.json"
ARTIFACT = ROOT / "explorations/conditional-build/k282-order-seven-shifted-face-center-calculus-2026-09-21.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k282_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K282 = load_solver()


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    operator = data.get("shifted_operator", {})
    charts = data.get("size_four_outward_face_charts", {})
    family = data.get("order_seven_family_propagation", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if fixed.get("patterns_by_size") != {"2": 72, "3": 25, "4": 1}:
        failures.append("pattern_census")
    if fixed.get("occurrences_by_size") != {"2": 720, "3": 252, "4": 24}:
        failures.append("occurrence_census")
    if fixed.get("nontrivial_patterns") != 98 or fixed.get("nontrivial_occurrences") != 996:
        failures.append("family_totals")
    translation = operator.get("exact_translation_checks", {})
    if translation.get("matrix_entries_checked") != 272 or translation.get("all_exact") is not True:
        failures.append("translation")
    rows = charts.get("charts", [])
    active_masks = {tuple(row.get("active", [])) for row in rows}
    labels = ("r0", "r1", "r2", "c0", "c1", "c2")
    expected = {
        tuple(labels[index] for index in range(6) if mask & (1 << index))
        for mask in range(1, 64)
    }
    if charts.get("face_mask_count") != 63 or active_masks != expected:
        failures.append("face_masks")
    if not rows or any(row.get("strictly_positive") is not True for row in rows):
        failures.append("chart_positivity")
    if any(row.get("radial_tiling_contiguous") is not True for row in rows):
        failures.append("radial_tiling")
    if family.get("all_98_patterns_bound_to_a_size_specific_shifted_operator") is not True:
        failures.append("pattern_binding")
    if family.get("all_996_nontrivial_occurrences_bound_to_a_size_specific_shifted_operator") is not True:
        failures.append("occurrence_binding")
    required_true = (
        "shifted_hermite_genocchi_entry_tail_serialized_through_size_four",
        "shared_face_center_dependencies_serialized",
        "complete_determinant_cauchy_correlation_serialized",
        "all_63_size_four_face_centers_outwardly_certified",
        "all_98_patterns_bound_to_size_specific_operator",
        "all_996_occurrences_bound_to_size_specific_operator",
    )
    required_false = (
        "arbitrary_gap_ratio_domain_covered",
        "mixed_duffy_derivative_envelopes_serialized",
        "determinant_preserving_jacobi_error_serialized",
        "complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true):
        failures.append("release_true")
    if any(release.get(key) is not False for key in required_false):
        failures.append("release_false")
    if data.get("physical_or_source_selection") is not False:
        failures.append("physical_selection")
    if data.get("canon_paper_release_or_public_posture_move") is not False:
        failures.append("public_posture")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()):
        failures.append("ledger")
    return failures


def hostile_controls(data: dict[str, Any]) -> dict[str, bool]:
    mutations = (
        ("drop_face", lambda d: d["size_four_outward_face_charts"]["charts"].pop()),
        ("break_count", lambda d: d["size_four_outward_face_charts"].__setitem__("face_mask_count", 62)),
        ("break_translation", lambda d: d["shifted_operator"]["exact_translation_checks"].__setitem__("matrix_entries_checked", 271)),
        ("invent_gap_domain", lambda d: d["release_test"].__setitem__("arbitrary_gap_ratio_domain_covered", True)),
        ("invent_duffy", lambda d: d["release_test"].__setitem__("mixed_duffy_derivative_envelopes_serialized", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("complete_base_action_column_evaluated", True)),
        ("drop_occurrences", lambda d: d["fixed_control"]["occurrences_by_size"].__setitem__("4", 23)),
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
    failures = manifest_failures(data)
    hostile = hostile_controls(data)
    rebuilt = K282.build()
    fully_active = data["size_four_outward_face_charts"]["fully_active_chart"]
    checks = {
        "manifest_replay": not failures,
        "deterministic_producer_replay": rebuilt == data,
        "all_face_masks_unique": len({tuple(row["active"]) for row in data["size_four_outward_face_charts"]["charts"]}) == 63,
        "fully_active_chart_positive": fully_active["minimum_R_lower"] > 0,
        "independent_control_contained": data["independent_controls"]["fully_active_face_center"]["contained"] is True,
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "local_not_global_ceiling": "local outward" in text and "no arbitrary-gap coverage" in text,
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

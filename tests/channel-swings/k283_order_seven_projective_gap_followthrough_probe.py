#!/usr/bin/env python3
"""Independent replay and hostile controls for K283."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k283_order_seven_projective_gap_followthrough.py")
MANIFEST = ROOT / "lab/process/k283-order-seven-projective-gap-followthrough.json"
ARTIFACT = ROOT / "explorations/conditional-build/k283-order-seven-projective-gap-followthrough-2026-09-21.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k283_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K283 = load_solver()


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    spine = data.get("correlated_projective_spine", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if fixed.get("projective_scale_range") != "1/1<=t<=5/4": failures.append("scale_range")
    if spine.get("total_cells") != 1536 or len(spine.get("cells", [])) != 32: failures.append("cell_count")
    if spine.get("all_cells_strictly_positive") is not True: failures.append("positivity")
    if spine.get("scale_interval_contiguous") is not True or spine.get("radial_interval_contiguous") is not True: failures.append("continuity")
    if spine.get("k282_fully_active_face_center_join", {}).get("join_proved") is not True: failures.append("join")
    required_true = (
        "shifted_hermite_genocchi_entry_tail_retained",
        "all_entries_use_one_shared_projective_scale_cell_before_complete_determinant_enclosure",
        "size_four_projective_t1_t5_over_4_spine_outwardly_certified",
        "k282_face_center_join_proved",
    )
    required_false = (
        "transverse_arbitrary_gap_ratio_domain_covered",
        "mixed_duffy_derivative_envelopes_serialized",
        "determinant_preserving_jacobi_error_serialized",
        "complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true): failures.append("release_true")
    if any(release.get(key) is not False for key in required_false): failures.append("release_false")
    if data.get("physical_or_source_selection") is not False: failures.append("physical_selection")
    if data.get("canon_paper_release_or_public_posture_move") is not False: failures.append("public_posture")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()): failures.append("ledger")
    return failures


def hostile_controls(data: dict[str, Any]) -> dict[str, bool]:
    mutations = (
        ("drop_cell", lambda d: d["correlated_projective_spine"]["cells"].pop()),
        ("break_count", lambda d: d["correlated_projective_spine"].__setitem__("total_cells", 1535)),
        ("break_join", lambda d: d["correlated_projective_spine"]["k282_fully_active_face_center_join"].__setitem__("join_proved", False)),
        ("invent_transverse", lambda d: d["release_test"].__setitem__("transverse_arbitrary_gap_ratio_domain_covered", True)),
        ("invent_duffy", lambda d: d["release_test"].__setitem__("mixed_duffy_derivative_envelopes_serialized", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("complete_base_action_column_evaluated", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
    )
    results = {}
    for name, mutate in mutations:
        broken = copy.deepcopy(data); mutate(broken)
        results[name] = bool(manifest_failures(broken))
    return results


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    hostile = hostile_controls(data)
    checks = {
        "manifest_replay": not failures,
        "deterministic_producer_replay": K283.build() == data,
        "positive_global_lower": data["correlated_projective_spine"]["minimum_R_lower"] > 0,
        "independent_points_contained": data["independent_controls"]["all_contained"] is True,
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "one_dimensional_ceiling": "one-dimensional" in text and "no transverse arbitrary-gap atlas" in text,
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

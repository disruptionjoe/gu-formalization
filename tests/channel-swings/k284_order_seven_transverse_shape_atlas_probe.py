#!/usr/bin/env python3
"""Independent replay and hostile controls for K284."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k284_order_seven_transverse_shape_atlas.py")
MANIFEST = ROOT / "lab/process/k284-order-seven-transverse-shape-atlas.json"
ARTIFACT = ROOT / "explorations/conditional-build/k284-order-seven-transverse-shape-atlas-2026-09-21.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k284_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K284 = load_solver()


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    atlas = data.get("transverse_shape_atlas", {})
    overlap = data.get("predecessor_overlap", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if fixed.get("transverse_shape_radius") != "1/32768": failures.append("shape_radius")
    if atlas.get("shape_dimension") != 6 or atlas.get("total_cells") != 2048: failures.append("cell_count")
    cells = atlas.get("cells", [])
    if len(cells) != atlas.get("scale_cells") or sum(cell.get("radial_subcells", 0) for cell in cells) != atlas.get("total_cells"):
        failures.append("cell_payload")
    if atlas.get("all_cells_strictly_positive") is not True: failures.append("positivity")
    if data.get("ordering_certificate", {}).get("all_strictly_positive") is not True: failures.append("ordering")
    if overlap.get("both_predecessor_overlaps_proved") is not True: failures.append("overlap")
    required_true = (
        "shifted_hermite_genocchi_entry_tail_retained",
        "all_six_shape_coordinates_share_one_complete_determinant_chart",
        "strict_gap_order_preserved",
        "k282_and_k283_overlap_proved",
        "transverse_ordered_shape_tube_covered",
    )
    required_false = (
        "complete_arbitrary_gap_ratio_domain_covered",
        "mixed_duffy_derivative_envelopes_serialized",
        "determinant_preserving_jacobi_error_serialized",
        "complete_base_action_column_evaluated",
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
        ("drop_cell", lambda d: d["transverse_shape_atlas"]["cells"].pop()),
        ("break_count", lambda d: d["transverse_shape_atlas"].__setitem__("total_cells", 2047)),
        ("break_order", lambda d: d["ordering_certificate"].__setitem__("all_strictly_positive", False)),
        ("break_overlap", lambda d: d["predecessor_overlap"].__setitem__("both_predecessor_overlaps_proved", False)),
        ("invent_simplex", lambda d: d["release_test"].__setitem__("complete_arbitrary_gap_ratio_domain_covered", True)),
        ("invent_duffy", lambda d: d["release_test"].__setitem__("mixed_duffy_derivative_envelopes_serialized", True)),
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
    failures = manifest_failures(data)
    hostile = hostile_controls(data)
    checks = {
        "manifest_replay": not failures,
        "deterministic_producer_replay": K284.build() == data,
        "positive_global_lower": data["transverse_shape_atlas"]["minimum_R_lower"] > 0,
        "independent_points_contained": data["independent_controls"]["all_contained"] is True,
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "tube_ceiling": (
            "ordered tube" in text
            and "arbitrary-gap simplex" in text
            and "no complete arbitrary-gap simplex" in data.get("claim_ceiling", "")
        ),
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

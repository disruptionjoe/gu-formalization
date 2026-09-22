#!/usr/bin/env python3
"""Independent replay and hostile controls for K285."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k285_order_seven_mixed_shape_derivative_packet.py")
MANIFEST = ROOT / "lab/process/k285-order-seven-mixed-shape-derivative-packet.json"
ARTIFACT = ROOT / "explorations/conditional-build/k285-order-seven-mixed-shape-derivative-packet-2026-09-21.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k285_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K285 = load_solver()


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    packet = data.get("first_shape_gradient_packet", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if packet.get("coordinate_count") != 6 or packet.get("total_cells") != 2048: failures.append("cell_count")
    cells = packet.get("cells", [])
    if len(cells) != packet.get("scale_cells") or sum(cell.get("radial_subcells", 0) for cell in cells) != packet.get("total_cells"):
        failures.append("cell_payload")
    if packet.get("all_bounds_finite_positive") is not True: failures.append("finite_bounds")
    if set(packet.get("global_coordinate_derivative_abs_upper", {})) != {"r0", "r1", "r2", "c0", "c1", "c2"}: failures.append("coordinates")
    required_true = (
        "k284_transverse_ordered_shape_tube_retained",
        "all_six_first_shape_derivative_envelopes_serialized",
        "complete_signed_cofactor_structure_retained_before_absolute_bound",
    )
    required_false = (
        "higher_mixed_duffy_derivative_envelopes_serialized",
        "determinant_preserving_jacobi_error_serialized",
        "complete_arbitrary_gap_ratio_domain_covered",
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
        ("drop_cell", lambda d: d["first_shape_gradient_packet"]["cells"].pop()),
        ("break_count", lambda d: d["first_shape_gradient_packet"].__setitem__("total_cells", 2047)),
        ("break_finite", lambda d: d["first_shape_gradient_packet"].__setitem__("all_bounds_finite_positive", False)),
        ("drop_coordinate", lambda d: d["first_shape_gradient_packet"]["global_coordinate_derivative_abs_upper"].pop("c2")),
        ("invent_mixed", lambda d: d["release_test"].__setitem__("higher_mixed_duffy_derivative_envelopes_serialized", True)),
        ("invent_jacobi", lambda d: d["release_test"].__setitem__("determinant_preserving_jacobi_error_serialized", True)),
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
        "deterministic_producer_replay": K285.build() == data,
        "finite_difference_controls_contained": data["independent_controls"]["all_contained"] is True,
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "first_derivative_ceiling": "first-derivative" in text and "no higher mixed-Duffy derivative bank" in text,
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

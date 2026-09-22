#!/usr/bin/env python3
"""Independent replay and hostile controls for K286."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k286_order_seven_mixed_shape_derivative_bank.py")
MANIFEST = ROOT / "lab/process/k286-order-seven-mixed-shape-derivative-bank.json"
ARTIFACT = ROOT / "explorations/conditional-build/k286-order-seven-mixed-shape-derivative-bank-2026-09-21.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k286_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K286 = load_solver()


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    bank = data.get("mixed_shape_derivative_bank", {})
    release = data.get("release_test", {})
    bounds = bank.get("global_componentwise_mixed_derivative_abs_upper", {})
    operator = bank.get("global_euclidean_operator_norm_upper", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if bank.get("total_cells") != 2048 or len(bank.get("cells", [])) != 32: failures.append("cell_count")
    expected_orders = {"1", "2", "3", "4"}
    complete_orders = set(bounds) == expected_orders and set(operator) == expected_orders
    if bank.get("maximum_derivative_order") != 4 or not complete_orders: failures.append("orders")
    if bank.get("all_bounds_finite_positive") is not True: failures.append("finite_bounds")
    if complete_orders and any(
        float(operator[str(order)]) < float(bounds[str(order)])
        for order in range(1, 5)
    ):
        failures.append("operator_domination")
    required_true = (
        "k284_transverse_ordered_shape_tube_retained",
        "all_mixed_shape_derivative_components_through_order_four_bounded",
        "complete_determinant_leibniz_assignments_retained",
        "complete_normalization_product_rule_retained",
    )
    required_false = (
        "tensor_jacobi_remainder_serialized",
        "native_K179_occurrence_measure_serialized",
        "complete_arbitrary_gap_ratio_domain_covered",
        "complete_base_action_column_evaluated",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true): failures.append("release_true")
    if any(release.get(key) is not False for key in required_false): failures.append("release_false")
    if data.get("physical_or_source_selection") is not False: failures.append("physical_selection")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()): failures.append("ledger")
    return failures


def hostile_controls(data: dict[str, Any]) -> dict[str, bool]:
    mutations = (
        ("drop_scale_row", lambda d: d["mixed_shape_derivative_bank"]["cells"].pop()),
        ("break_cell_count", lambda d: d["mixed_shape_derivative_bank"].__setitem__("total_cells", 2047)),
        ("drop_fourth_order", lambda d: d["mixed_shape_derivative_bank"]["global_componentwise_mixed_derivative_abs_upper"].pop("4")),
        ("break_operator", lambda d: d["mixed_shape_derivative_bank"]["global_euclidean_operator_norm_upper"].__setitem__("4", 0)),
        ("invent_jacobi", lambda d: d["release_test"].__setitem__("tensor_jacobi_remainder_serialized", True)),
        ("invent_measure", lambda d: d["release_test"].__setitem__("native_K179_occurrence_measure_serialized", True)),
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
        "deterministic_producer_replay": K286.build() == data,
        "mixed_difference_controls_contained": data["independent_controls"]["all_contained"] is True,
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "componentwise_ceiling": "componentwise" in text and "native K179 occurrence measure" in text,
        "all_hostile_mutations_rejected": all(hostile.values()),
    }
    print(json.dumps({
        "schema_version": "1.0",
        "producer_result_id": data.get("result_id"),
        "checks": checks,
        "manifest_failures": failures,
        "hostile_controls": hostile,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
    }, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())

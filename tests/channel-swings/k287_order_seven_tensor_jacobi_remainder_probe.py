#!/usr/bin/env python3
"""Independent formula replay and hostile controls for K287."""

from __future__ import annotations

import copy
import importlib.util
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k287_order_seven_tensor_jacobi_remainder.py")
MANIFEST = ROOT / "lab/process/k287-order-seven-tensor-jacobi-remainder.json"
ARTIFACT = ROOT / "explorations/conditional-build/k287-order-seven-tensor-jacobi-remainder-2026-09-21.md"
getcontext().prec = 100


def load_solver():
    spec = importlib.util.spec_from_file_location("k287_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K287 = load_solver()


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    release = data.get("release_test", {})
    remainder = data.get("remainder", {})
    radius = Fraction(fixed.get("transverse_shape_radius", "0"))
    h = Decimal(radius.numerator) / Decimal(radius.denominator)
    fourth = Decimal(remainder.get("global_componentwise_fourth_derivative_abs_upper", "NaN"))
    expected = Decimal(6) * h ** 4 * fourth / Decimal(270)
    actual = Decimal(remainder.get("six_axis_normalized_tube_average_abs_upper", "NaN"))
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if fixed.get("shape_coordinate_count") != 6 or fixed.get("tensor_node_count") != 64: failures.append("rule_size")
    if fixed.get("jacobi_alpha") != "0" or fixed.get("jacobi_beta") != "0": failures.append("jacobi_parameters")
    if expected != actual: failures.append("remainder_formula")
    required_true = (
        "k286_fourth_derivative_bank_consumed",
        "determinant_preserving_tensor_jacobi_remainder_serialized",
        "normalized_uniform_tube_measure_only",
    )
    required_false = (
        "native_K179_occurrence_measure_serialized",
        "complete_arbitrary_gap_ratio_domain_covered",
        "complete_base_action_column_evaluated",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true): failures.append("release_true")
    if any(release.get(key) is not False for key in required_false): failures.append("release_false")
    if data.get("decision", {}).get("domain_widening_authorized") is not False: failures.append("domain_widening")
    if data.get("physical_or_source_selection") is not False: failures.append("physical_selection")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()): failures.append("ledger")
    return failures


def hostile_controls(data: dict[str, Any]) -> dict[str, bool]:
    mutations = (
        ("wrong_constant", lambda d: d["remainder"].__setitem__("six_axis_normalized_tube_average_abs_upper", "0")),
        ("wrong_nodes", lambda d: d["fixed_control"].__setitem__("tensor_node_count", 63)),
        ("wrong_jacobi", lambda d: d["fixed_control"].__setitem__("jacobi_alpha", "1")),
        ("invent_measure", lambda d: d["release_test"].__setitem__("native_K179_occurrence_measure_serialized", True)),
        ("invent_domain", lambda d: d["release_test"].__setitem__("complete_arbitrary_gap_ratio_domain_covered", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("complete_base_action_column_evaluated", True)),
        ("authorize_widening", lambda d: d["decision"].__setitem__("domain_widening_authorized", True)),
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
        "deterministic_producer_replay": K287.build() == data,
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "measure_ceiling": "normalized uniform" in text and "not the native K179 occurrence measure" in text,
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

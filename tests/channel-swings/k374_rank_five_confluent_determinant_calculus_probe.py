#!/usr/bin/env python3
"""Replay K374 and reject confluence mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k374_rank_five_confluent_determinant_calculus.py"
PUBLISHED = ROOT / "lab/process/k374-rank-five-confluent-determinant-calculus.json"
spec = importlib.util.spec_from_file_location("k374_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K374 producer")
backend = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = backend
spec.loader.exec_module(backend)


def rejected(payload: dict) -> bool:
    try:
        backend.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    rebuilt = backend.build()
    published = json.loads(PUBLISHED.read_text())
    controls = [
        rebuilt == published,
        rebuilt["fixed_control"]["maximum_rank"] == 5,
        rebuilt["fixed_control"]["maximum_kernel_derivative_order"] == 10,
        all(row["exact_equality"] for row in rebuilt["gap_free_tensor_divided_difference"]["polynomial_controls"]),
        len(rebuilt["gap_free_tensor_divided_difference"]["all_zero_controls"]) == 25,
        all(row["exact_replay"] and row["exact_normalization"] for row in rebuilt["determinant_calculus"]["exact_controls"]),
        not rebuilt["determinant_calculus"]["entrywise_cofactor_absolutization_permitted"],
        not rebuilt["decision"]["zero_safe_global_primitive_bank_through_order_ten_emitted"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("maximum_rank", 4),
        lambda p: p["fixed_control"].__setitem__("maximum_kernel_derivative_order", 9),
        lambda p: p["fixed_control"].__setitem__("polynomial_identity_checks", 54),
        lambda p: p["gap_free_tensor_divided_difference"].__setitem__("explicit_gap_denominators_after_extension", True),
        lambda p: p["gap_free_tensor_divided_difference"]["polynomial_controls"][0].__setitem__("exact_equality", False),
        lambda p: p["determinant_calculus"]["exact_controls"][4].__setitem__("exact_normalization", False),
        lambda p: p["determinant_calculus"].__setitem__("complete_determinant_assembled_before_absolute_enclosure", False),
        lambda p: p["determinant_calculus"].__setitem__("entrywise_cofactor_absolutization_permitted", True),
        lambda p: p["decision"].__setitem__("zero_safe_global_primitive_bank_through_order_ten_emitted", True),
        lambda p: p["decision"].__setitem__("numerical_order_nine_integral_emitted", True),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K374 probe failed")
    print(f"K374 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

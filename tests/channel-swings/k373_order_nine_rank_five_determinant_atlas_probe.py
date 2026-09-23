#!/usr/bin/env python3
"""Replay K373 and reject factor-atlas mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k373_order_nine_rank_five_determinant_atlas.py"
PUBLISHED = ROOT / "lab/process/k373-order-nine-rank-five-determinant-atlas.json"
spec = importlib.util.spec_from_file_location("k373_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K373 producer")
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
    inv = rebuilt["complete_factorization_inventory"]
    controls = [
        rebuilt == published,
        rebuilt["fixed_control"]["paths"] == 256,
        rebuilt["fixed_control"]["upper_triangle_gram_entries"] == 2368,
        rebuilt["fixed_control"]["ordered_quadratic_terms"] == 4480,
        inv["rank_five_patterns"] > 0,
        inv["rank_five_occurrences"] > 0,
        all(row["exact_equality"] for row in rebuilt["exact_cauchy_controls"]),
        rebuilt["confluence_demand"]["maximum_kernel_derivative_order_required"] == 10,
        not rebuilt["decision"]["numerical_order_nine_integral_emitted"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("paths", 255),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 19),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 2367),
        lambda p: p["fixed_control"].__setitem__("ordered_quadratic_terms", 4479),
        lambda p: p["fixed_control"].__setitem__("maximum_species_determinant_rank", 4),
        lambda p: p["complete_factorization_inventory"].__setitem__("rank_five_patterns", 0),
        lambda p: p["complete_factorization_inventory"].__setitem__("complete_group_assembly_precedes_absolute_enclosure", False),
        lambda p: p["exact_cauchy_controls"][4].__setitem__("exact_equality", False),
        lambda p: p["confluence_demand"].__setitem__("maximum_kernel_derivative_order_required", 9),
        lambda p: p["decision"].__setitem__("rank_five_confluent_calculus_emitted", True),
        lambda p: p["decision"].__setitem__("numerical_order_nine_integral_emitted", True),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K373 probe failed")
    print(f"K373 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

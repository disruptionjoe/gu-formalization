#!/usr/bin/env python3
"""Replay K376 and reject rank-five transfer mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k376_orders_nine_ten_rank_five_transfer.py"
PUBLISHED = ROOT / "lab/process/k376-orders-nine-ten-rank-five-transfer.json"
spec = importlib.util.spec_from_file_location("k376_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K376 producer")
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
        rebuilt["fixed_control"]["paths"] == 736,
        rebuilt["fixed_control"]["upper_triangle_gram_entries"] == 9258,
        [row["order"] for row in rebuilt["order_interfaces"]] == [9, 10],
        all(row["maximum_rank"] == 5 for row in rebuilt["order_interfaces"]),
        rebuilt["calculus_binding"]["every_required_primitive_order_present"],
        not rebuilt["calculus_binding"]["order_eight_node_or_face_atlas_reused"],
        rebuilt["decision"]["rank_six_orders_eleven_twelve_released"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("paths", 735),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 47),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 9257),
        lambda p: p["fixed_control"].__setitem__("maximum_rank", 4),
        lambda p: p["order_interfaces"][1].__setitem__("maximum_rank", 6),
        lambda p: p["calculus_binding"].__setitem__("rank_five_gap_free_confluence", False),
        lambda p: p["calculus_binding"].__setitem__("every_required_primitive_order_present", False),
        lambda p: p["calculus_binding"].__setitem__("order_eight_node_or_face_atlas_reused", True),
        lambda p: p["decision"].__setitem__("numerical_order_nine_integral_emitted", True),
        lambda p: p["decision"].__setitem__("numerical_order_ten_integral_emitted", True),
        lambda p: p["decision"].__setitem__("rank_six_orders_eleven_twelve_released", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K376 probe failed")
    print(f"K376 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

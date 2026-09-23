#!/usr/bin/env python3
"""Replay K379 and reject final higher-rank transfer mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k379_orders_eleven_twelve_rank_six_transfer.py"
PUBLISHED = ROOT / "lab/process/k379-orders-eleven-twelve-rank-six-transfer.json"
spec = importlib.util.spec_from_file_location("k379_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K379 producer")
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
        rebuilt["fixed_control"]["paths"] == 1792,
        rebuilt["fixed_control"]["upper_triangle_gram_entries"] == 48272,
        [row["positive_time_variables"] for row in rebuilt["order_interfaces"]] == [24, 26],
        all(row["rank_six_patterns"] for row in rebuilt["order_interfaces"]),
        rebuilt["complete_higher_rank_calculus"]["all_orders_eight_through_twelve_structurally_typed"],
        not rebuilt["complete_higher_rank_calculus"]["occurrencewise_absolute_value_permitted"],
        rebuilt["decision"]["higher_rank_determinant_confluence_derivative_obstruction_closed"],
        not rebuilt["decision"]["complete_base_action_column_emitted"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("paths", 1791),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 56),
        lambda p: p["fixed_control"].__setitem__("maximum_rank", 5),
        lambda p: p["order_interfaces"][0].__setitem__("positive_time_variables", 22),
        lambda p: p["order_interfaces"][1].__setitem__("rank_six_patterns", []),
        lambda p: p["complete_higher_rank_calculus"].__setitem__("gap_free_confluence_through_rank_six", False),
        lambda p: p["complete_higher_rank_calculus"].__setitem__("occurrencewise_absolute_value_permitted", True),
        lambda p: p["complete_higher_rank_calculus"].__setitem__("order_eight_node_or_face_atlas_reused", True),
        lambda p: p["decision"].__setitem__("numerical_orders_nine_through_twelve_integrals_emitted", True),
        lambda p: p["decision"].__setitem__("complete_base_action_column_emitted", True),
        lambda p: p["decision"].__setitem__("complete_R_ref_residual_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K379 probe failed")
    print(f"K379 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

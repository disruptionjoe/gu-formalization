#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K394."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k394_order_nine_normal_projective_atlas.py"
STORED = ROOT / "lab/process/k394-order-nine-normal-projective-atlas.json"
spec = importlib.util.spec_from_file_location("k394_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K394 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        len(stored["mask_atlas"]) == 98,
        len(stored["program_chart_map"]) == 695,
        sum(row["chart_count"] for row in stored["mask_atlas"]) == 758,
        sum(len(row["chart_ids"]) for row in stored["program_chart_map"]) == 4320,
        all(row["agrees"] for row in stored["jacobian_controls"]),
        all(row["reconstructed_exactly"] for row in stored["exact_controls"]),
        stored["coordinate_contract"]["closed_chart_union_covers_complete_projective_simplex"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K394 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("unique_zero_masks", 97),
        lambda p: p["fixed_control"].__setitem__("unique_maximum_charts", 757),
        lambda p: p["mask_atlas"].pop(), lambda p: p["program_chart_map"].pop(),
        lambda p: p["mask_atlas"][0].__setitem__("chart_count", 1),
        lambda p: p["jacobian_controls"][0].__setitem__("agrees", False),
        lambda p: p["exact_controls"][0].__setitem__("reconstructed_exactly", False),
        lambda p: p["coordinate_contract"].__setitem__("closed_chart_union_covers_complete_projective_simplex", False),
        lambda p: p["decision"].__setitem__("positive_width_projective_cells_evaluated", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored); mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K394 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K394 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K361."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k361_order_eight_positive_width_projective_cells.py"
STORED = ROOT / "lab/process/k361-order-eight-positive-width-projective-cells.json"
spec = importlib.util.spec_from_file_location("k361_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K361 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    module.validate_payload(stored)
    rebuilt = module.build()
    checks = [
        stored == rebuilt,
        len(stored["chart_cell_bank"]) == 578,
        stored["fixed_control"]["program_chart_cell_uses"] == 2998,
        len(stored["executed_cell_bank"]) == 13,
        all(row["positive_width_in_every_ratio"] for row in stored["chart_cell_bank"]),
        all(row["midpoint_direct_interval_contained"] for row in stored["executed_cell_bank"]),
        all(row["coherent_group_count"] == 23 for row in stored["executed_cell_bank"]),
        stored["projective_cell_contract"]["cells_are_pilots_not_a_chart_cover"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K361 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("unique_maximum_charts", 577),
        lambda p: p["fixed_control"].__setitem__("program_chart_cell_uses", 2997),
        lambda p: p["chart_cell_bank"].pop(),
        lambda p: p["chart_cell_bank"][0].__setitem__("positive_width_in_every_ratio", False),
        lambda p: p["executed_cell_bank"].pop(),
        lambda p: p["executed_cell_bank"][0].__setitem__("minimum_cumulative_argument_lower", "0"),
        lambda p: p["executed_cell_bank"][0].__setitem__("midpoint_direct_interval_contained", False),
        lambda p: p["executed_cell_bank"][0].__setitem__("coherent_group_count", 22),
        lambda p: p["projective_cell_contract"].__setitem__("cells_are_pilots_not_a_chart_cover", False),
        lambda p: p["decision"].__setitem__("complete_projective_chart_cover_emitted", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K361 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K361 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

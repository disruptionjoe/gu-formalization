#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K359."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k359_order_eight_projective_measure_and_boundary_routing.py"
STORED = ROOT / "lab/process/k359-order-eight-projective-measure-and-boundary-routing.json"
spec = importlib.util.spec_from_file_location("k359_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K359 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        len(stored["codimension_measure_bank"]) == 13,
        stored["fixed_control"]["unique_oriented_coordinate_boundaries"] == 9940,
        stored["fixed_control"]["program_oriented_coordinate_boundary_uses"] == 41588,
        stored["fixed_control"]["compactly_represented_nonempty_lower_strata"] == 4_740_626,
        all(row["chart_sum_replays_simplex_mass"] for row in stored["codimension_measure_bank"]),
        stored["boundary_routing_contract"]["zero_routing_terminates"],
        stored["boundary_routing_contract"]["interval_closures_still_require_one_sided_zero_safe_majorants"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K359 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("unique_oriented_coordinate_boundaries", 9939),
        lambda p: p["fixed_control"].__setitem__("program_oriented_coordinate_boundary_uses", 41587),
        lambda p: p["fixed_control"].__setitem__("compactly_represented_nonempty_lower_strata", 4_740_625),
        lambda p: p["codimension_measure_bank"][0].__setitem__("chart_sum_replays_simplex_mass", False),
        lambda p: p["measure_contract"].__setitem__("angular_mass_must_not_be_applied_to_K357_equal_line_values", False),
        lambda p: p["boundary_routing_contract"].__setitem__("zero_routing_terminates", False),
        lambda p: p["boundary_routing_contract"].__setitem__("interval_closures_still_require_one_sided_zero_safe_majorants", False),
        lambda p: p["decision"].__setitem__("positive_width_projective_cells_evaluated", True),
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
        raise AssertionError(f"K359 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K359 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

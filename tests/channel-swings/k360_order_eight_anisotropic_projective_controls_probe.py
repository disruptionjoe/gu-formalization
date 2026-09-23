#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K360."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k360_order_eight_anisotropic_projective_controls.py"
STORED = ROOT / "lab/process/k360-order-eight-anisotropic-projective-controls.json"
spec = importlib.util.spec_from_file_location("k360_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K360 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    module.validate_payload(stored)
    rebuilt = module.build()
    checks = [
        stored == rebuilt,
        len(stored["anisotropic_control_bank"]) == 13,
        stored["fixed_control"]["ordered_descriptor_control_evaluations"] == 31_200,
        all(row["direction_is_not_equal_normal"] for row in stored["anisotropic_control_bank"]),
        all(row["preconditioned_direct_intervals_overlap"] for row in stored["anisotropic_control_bank"]),
        all(row["coherent_group_count"] == 23 for row in stored["anisotropic_control_bank"]),
        not stored["execution_contract"]["raw_Bessel_evaluation_at_zero_used"],
        stored["execution_contract"]["point_controls_are_not_positive_width_projective_cells"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K360 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("selected_controls", 12),
        lambda p: p["fixed_control"].__setitem__("ordered_descriptor_control_evaluations", 28_800),
        lambda p: p["anisotropic_control_bank"].pop(),
        lambda p: p["anisotropic_control_bank"][0].__setitem__("direction_is_not_equal_normal", False),
        lambda p: p["anisotropic_control_bank"][0].__setitem__("minimum_cumulative_argument_lower", "0"),
        lambda p: p["anisotropic_control_bank"][0].__setitem__("preconditioned_direct_intervals_overlap", False),
        lambda p: p["anisotropic_control_bank"][0].__setitem__("coherent_group_count", 22),
        lambda p: p["execution_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["execution_contract"].__setitem__("point_controls_are_not_positive_width_projective_cells", False),
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
        raise AssertionError(f"K360 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K360 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Independent hostile probe for K573."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k573", HERE / "k573_k152_residual_accuracy_targets.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


payload = module.build()
module.validate(payload)
checks = [
    payload["inputs"]["K169_best_admissible_relative_gap"] == "5/2",
    payload["inputs"]["upper_is_not_actual_residual_lower"] is True,
    payload["ground_deficit_targets"][0]["best_gap_residual_square_budget"] == "7/2",
    payload["ground_deficit_targets"][1]["best_gap_residual_square_budget"] == "3/2",
    payload["ground_deficit_targets"][2]["best_gap_residual_square_budget"] == "13/50",
    payload["projection_targets"][0]["best_gap_residual_square_budget"] == "25/9",
    payload["projection_targets"][1]["best_gap_residual_square_budget"] == "225/256",
    payload["projection_targets"][2]["best_gap_residual_square_budget"] == "625/9801",
    payload["controls"]["all_current_targets_fail"] is True,
    payload["controls"]["budgets_tighten_with_accuracy"] is True,
    payload["decision"]["native_K152_interval_emitted"] is False,
]
mutations = [
    lambda d: d["inputs"].__setitem__("upper_is_not_actual_residual_lower", False),
    lambda d: d["controls"].__setitem__("all_current_targets_fail", False),
    lambda d: d["controls"].__setitem__("budgets_tighten_with_accuracy", False),
    lambda d: d["decision"].__setitem__("quantitative_K466_shift_is_priority_for_residual_accuracy", True),
    lambda d: d["decision"].__setitem__("complete_floor_alone_can_rescue_current_K570_upper", True),
    lambda d: d["decision"].__setitem__("residual_or_flux_accuracy_must_move_by_over_10_to_2346", False),
    lambda d: d["decision"].__setitem__("native_K152_interval_emitted", True),
]
rejected = 0
for mutate in mutations:
    hostile = copy.deepcopy(payload)
    mutate(hostile)
    try:
        module.validate(hostile)
    except AssertionError:
        rejected += 1
if not all(checks) or rejected != len(mutations):
    raise SystemExit("K573 hostile probe failed")
print(f"K573 PROBE: {sum(checks)}/{len(checks)} controls pass; {rejected}/{len(mutations)} hostile mutations rejected")

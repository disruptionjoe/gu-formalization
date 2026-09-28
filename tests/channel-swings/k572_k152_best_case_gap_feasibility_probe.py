#!/usr/bin/env python3
"""Independent hostile probe for K572."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k572", HERE / "k572_k152_best_case_gap_feasibility.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


payload = module.build()
module.validate(payload)
checks = [
    payload["composition"]["K169_relative_gap_cap"] == "5/2",
    payload["composition"]["K169_cap_is_complete_floor"] is False,
    payload["best_case_tests"]["ground_deficit_at_most_1"]["maximum_allowed_residual_square"] == "7/2",
    payload["best_case_tests"]["ground_deficit_at_most_gap_cap"]["maximum_allowed_residual_square"] == "25/2",
    payload["best_case_tests"]["projection_sine_at_most_1_over_2"]["maximum_allowed_residual_square"] == "25/9",
    payload["decision"]["failure_is_certificate_insufficiency_not_actual_residual_lower"] is True,
    payload["decision"]["complete_complement_floor_still_required"] is True,
    payload["decision"]["native_K152_interval_emitted"] is False,
    payload["sharp_control"]["both_equalities_hold"] is True,
    "failure of the current upper certificate" in payload["claim_ceiling"],
]
mutations = [
    lambda d: d["composition"].__setitem__("K169_cap_is_complete_floor", True),
    lambda d: d["best_case_tests"]["ground_deficit_at_most_1"].__setitem__("current_upper_passes", True),
    lambda d: d["decision"].__setitem__("current_upper_certifies_ground_deficit_within_gap_cap", True),
    lambda d: d["decision"].__setitem__("failure_is_certificate_insufficiency_not_actual_residual_lower", False),
    lambda d: d["decision"].__setitem__("native_K152_interval_emitted", True),
    lambda d: d["sharp_control"].__setitem__("both_equalities_hold", False),
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
    raise SystemExit("K572 hostile probe failed")
print(f"K572 PROBE: {sum(checks)}/{len(checks)} controls pass; {rejected}/{len(mutations)} hostile mutations rejected")

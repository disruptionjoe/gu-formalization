#!/usr/bin/env python3
"""Independent hostile probe for K571."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k571", HERE / "k571_k152_shifted_coercivity_dominance.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


payload = module.build()
module.validate(payload)
checks = [
    payload["theorem"]["variational_ceiling"] == "c<=a",
    payload["theorem"]["shift_can_rescue_coarse_M_dual_upper"] is False,
    payload["theorem"]["actual_shifted_dual_may_be_smaller_than_bridge_upper"] is True,
    payload["sharp_control"]["all_equal"] is True,
    payload["sharp_control"]["K466_residual_energy_upper"] == "5",
    payload["decision"]["K469_direct_M_dual_consumer_is_weakly_dominant"] is True,
    payload["decision"]["K466_remains_valid_for_shifted_form_typing"] is True,
    payload["decision"]["native_K152_interval_emitted"] is False,
    payload["source_and_ledger_context"]["ledger_effect"] == "none",
    "cannot beat K469" in payload["claim_ceiling"],
]
mutations = [
    lambda d: d["theorem"].__setitem__("variational_ceiling", "c>=a"),
    lambda d: d["theorem"].__setitem__("shift_can_rescue_coarse_M_dual_upper", True),
    lambda d: d["sharp_control"].__setitem__("all_equal", False),
    lambda d: d["decision"].__setitem__("K469_direct_M_dual_consumer_is_weakly_dominant", False),
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
    raise SystemExit("K571 hostile probe failed")
print(f"K571 PROBE: {sum(checks)}/{len(checks)} controls pass; {rejected}/{len(mutations)} hostile mutations rejected")

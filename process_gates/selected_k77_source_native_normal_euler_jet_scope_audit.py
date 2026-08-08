#!/usr/bin/env python3
"""Fail closed if the normal-Euler result outruns its exact grade."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-source-native-normal-euler-jet-2026-08-08.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-source-native-normal-euler-jet.json").read_text())

assert "mixed action Hessian" in report
assert "coefficientwise full K77 specialization" in report
assert "not a second observation field" in report
assert "no new field, coefficient, selector or external datum" in report
assert "normal jets differ" in report
assert "Antisymmetrization may begin" not in report
assert registry["free_object_delta"] == 0
assert registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED"
assert len(registry["normal_owner_classes"]) == 7
assert all(registry["open"].values())
assert registry["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
print("PASS selected K77 source-native normal Euler-jet scope audit")

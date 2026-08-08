#!/usr/bin/env python3
"""Scope audit for the K77 epsilon endpoint direct-sum gate."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-epsilon-endpoint-direct-sum-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-epsilon-endpoint-direct-sum-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-epsilon-endpoint-direct-sum.json").read_text())

for phrase in (
    "full v0.70 result",
    "presymplectic rank: 40",
    "local quotient dimension/rank: 40/40",
    "i_n(E_B-E_T)",
    "p=KT",
    "does **not yet own**",
    "P1/P2/P3 consumed: 0",
):
    assert phrase in report, phrase

assert registry["exact_result"]["local_collar_endpoint_trace_rank"] == 2
assert registry["exact_result"]["all_ten_quotient_rank"] == 40
assert registry["exact_result"]["action_weld_proved"] is False
assert registry["construction_disposition"]["single_holonomy_full_v070_bridge"] == "REMAINS_KILLED"
assert registry["construction_disposition"]["v070_boundary_coordinate_cost_retyped_as_existing_epsilon"] == "NOT_YET"
assert registry["external_datum"] == {
    "P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED", "free_object_delta": 0
}
assert registry["program_fences"]["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["program_fences"]["third_lane"] == "NOT_PROMOTED"
assert "PASS_WITH_MATERIAL_SCOPE_REPAIR" in review
assert "summary outran the artifact" in review
assert "Symplectic disposition" in review
print("PASS selected K77 epsilon endpoint direct-sum scope audit")

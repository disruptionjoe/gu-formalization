#!/usr/bin/env python3
"""Scope and provenance audit for the K77 two-endpoint edge-dressing gate."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-two-endpoint-edge-dressing-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-two-endpoint-edge-dressing-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-two-endpoint-edge-dressing.json").read_text())

required = [
    "single-holonomy candidate is killed",
    "40/40",
    "20/20",
    "p_0=p_2=-P",
    "SOURCE-SILENT__EPSILON_BOUNDARY_BFV_OWNERSHIP",
    "No K95 quaternionic",
    "P1/P2/P3 consumed: 0",
]
for phrase in required:
    assert phrase in report, phrase

assert registry["exact_result"]["kernel_equals_gauge_orbit"] is True
assert registry["exact_result"]["full_v070_recovery"] is False
assert registry["construction_disposition"]["two_continuum_endpoint_evaluation_map"] == "OPEN"
assert registry["external_datum"] == {
    "P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED", "free_object_delta": 0
}
assert registry["program_fences"]["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["program_fences"]["third_lane"] == "NOT_PROMOTED"
assert "PASS_WITH_MATERIAL_NEGATIVE_RESULT_RETAINED" in review
assert "positive energy" in review
assert "physical BFV phase" in report
print("PASS selected K77 two-endpoint edge-dressing scope audit")

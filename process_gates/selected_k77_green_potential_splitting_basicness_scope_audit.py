#!/usr/bin/env python3
"""Fail closed if the K77 splitting/basicness result outruns cotangent grade."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-green-potential-splitting-basicness-2026-08-08.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-green-potential-splitting-basicness.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.68.json").read_text())

assert "complete boundary" in report
assert "cotangent lift" in report
assert "pointwise field-frame" in report
assert "derivative-dependent/contact" in report
assert "Physical" in report and "gauge basicness" in report
assert "SOURCE-SILENT" in report
assert "does not license importing" in report
assert "P1/P2/P3" in report
assert registry["status"].startswith("SPLITTING_BASIC_EXACT_AT_COTANGENT_GRADE")
assert registry["exact_result"]["k77_live_normal_momentum_shifts"] == 10
assert registry["construction_disposition"]["vertical_B_T_lift_for_point_trivialization_descent"] == "NOT_REQUIRED"
assert registry["construction_disposition"]["derivative_dependent_B_LC_soldering_observation_contact_terms"] == "OPEN"
assert registry["construction_disposition"]["physical_gauge_contraction_and_lie_derivative_basicness"] == "OPEN"
assert registry["external_datum"]["free_object_delta"] == 0
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["quotients_ranked"] == 4
assert "contact terms" in ledger["next_work_queue"][0]["why"]
print("PASS selected K77 Green-potential splitting/basicness scope audit")

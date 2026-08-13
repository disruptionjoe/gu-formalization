#!/usr/bin/env python3
"""Fail closed if the group-edge result outruns its universal pure-gauge gate."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-group-edge-dressing-maurer-cartan-bridge-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-group-edge-dressing-maurer-cartan-bridge-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-group-edge-dressing-maurer-cartan-bridge.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.72.json").read_text())

assert "GROUP_EDGE_DRESSING_AND_PRESYMPLECTIC_BASICNESS_EXACT" in report
assert "kernel equals gauge orbit: yes" in report
assert "recovering the v0.70 minus sign" in report
assert "flat/pure-gauge" in report
assert "It is not an arbitrary olive/varpi connection" in report
assert "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report
assert "P1/P2/P3 consumed: 0" in report
assert "Symplectic-geometry lens" in review
assert "summary outrun" in review
assert "superseded or mistyped object" in review
assert registry["exact_result"]["kernel_equals_gauge_orbit"] is True
assert registry["exact_result"]["pulled_back_twoform_rank"] == 8
assert registry["exact_result"]["characteristic_kernel_dimension"] == 4
assert registry["exact_result"]["v070_minus_sign_recovered"] is True
assert registry["exact_result"]["maurer_cartan_curvature"] == "ZERO"
assert registry["exact_result"]["arbitrary_nonflat_varpi_covered"] is False
assert registry["construction_disposition"]["actual_k77_h_representation"] == "OPEN"
assert registry["construction_disposition"]["physical_bfv_phase_space"] == "OPEN"
assert registry["external_datum"]["free_object_delta"] == 0
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 5
assert "actual K77 H-representation" in ledger["next_work_queue"][0]["why"]
print("PASS selected K77 group-edge dressing Maurer-Cartan bridge scope audit")

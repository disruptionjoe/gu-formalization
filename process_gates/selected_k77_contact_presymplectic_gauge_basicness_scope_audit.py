#!/usr/bin/env python3
"""Fail closed if the K77 contact result outruns local small-gauge grade."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-contact-presymplectic-gauge-basicness-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-contact-presymplectic-gauge-basicness-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-contact-presymplectic-gauge-basicness.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.69.json").read_text())

assert "SMALL_GAUGE_BASIC__BOUNDARY_CHARGE_LIVE" in report
assert "invariance versus horizontality" in report
assert "A-B_LC(g)" in report
assert "SOURCE-SILENT" in report
assert "all ten k77" in report.lower()
assert "full nonlinear ambient" in report
assert "P1/P2/P3" in report
assert "Symplectic-geometry lens" in review
assert "not the same thing as a vanishing" in review
assert registry["status"] == "SMALL_GAUGE_BASIC__BOUNDARY_CHARGE_LIVE"
assert registry["exact_result"]["spin_levi_civita_symbol_rank"] == 10
assert registry["exact_result"]["small_gauge_contraction"] == "ZERO"
assert registry["exact_result"]["k77_normal_boundary_charges_nonzero"] == 10
assert registry["construction_disposition"]["physical_boundary_condition_or_edge_mode_extension"] == "OPEN"
assert registry["construction_disposition"]["full_nonlinear_ambient_y14_contact_coefficients"] == "OPEN"
assert registry["external_datum"]["free_object_delta"] == 0
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["quotients_ranked"] == 4
assert "edge-mode" in ledger["next_work_queue"][0]["why"]
print("PASS selected K77 contact-presymplectic gauge-basicness scope audit")

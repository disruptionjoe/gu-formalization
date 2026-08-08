#!/usr/bin/env python3
"""Fail closed if the K77 edge result outruns its finite local quotient."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-minimal-edge-mode-reduction-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-minimal-edge-mode-reduction-review.md").read_text()
review_flat = " ".join(review.split())
registry = json.loads((ROOT / "lab/process/selected-k77-minimal-edge-mode-reduction.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.70.json").read_text())

assert "MINIMAL_EDGE_EXTENSION_EXACT__SOURCE_SELECTION_OPEN" in report
assert "delta^2B=0" in report
assert "coefficient-unique" in report
assert "SOURCE-SILENT" in report
assert "all-ten" in report.lower()
assert "global labelled `Y14` edge bundle" in report
assert "new boundary-coordinate dimension: 20" in report
assert "P1/P2/P3 consumed: 0" in report
assert "Symplectic-geometry lens" in review
assert "kernel is exactly the gauge span" in review_flat
assert "summary outrun" in review
assert "superseded or mistyped object" in review
assert registry["status"] == "MINIMAL_EDGE_EXTENSION_EXACT__SOURCE_SELECTION_OPEN"
assert registry["exact_result"]["ordinary_counterterm_delta_omega"] == "ZERO"
assert registry["exact_result"]["edge_coefficients"] == {"c0": -1, "c3": 1}
assert registry["exact_result"]["all_ten_extended_dimension"] == 60
assert registry["exact_result"]["all_ten_form_rank"] == 40
assert registry["exact_result"]["all_ten_gauge_kernel_dimension"] == 20
assert registry["exact_result"]["all_ten_quotient_dimension"] == 40
assert registry["exact_result"]["all_ten_quotient_rank"] == 40
assert registry["construction_disposition"]["global_labelled_y14_edge_bundle"] == "OPEN"
assert registry["construction_disposition"]["physical_bfv_phase_space"] == "OPEN"
assert registry["external_datum"]["free_object_delta"] == 0
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 5
assert "labelled Y14" in ledger["next_work_queue"][0]["why"]
print("PASS selected K77 minimal edge-mode reduction scope audit")

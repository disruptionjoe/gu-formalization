#!/usr/bin/env python3
"""Scope audit for the selected K77 action/contact Legendre-owner correction."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-action-contact-legendre-owner-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-action-contact-legendre-owner-review.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.75.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-action-contact-legendre-owner.json").read_text())

for phrase in (
    "universal\ncontact theorem",
    "not an action-derived GU coefficient",
    "45",
    "36",
    "E_B-E_T",
    "P1/P2/P3 remain unused",
):
    assert phrase in report, phrase

assert registry["exact"]["different_KT_momenta"] is True
assert registry["exact"]["selected_action_cubic_live"] is True
assert registry["exact"]["E_B_minus_E_T_at_T_zero_nonzero"] is True
assert registry["exact"]["fixed_linear_KT_global_identity"] is False
assert registry["preserved"]["direct_sum_local_quotient"] == "40_OF_40"
assert registry["preserved"]["single_holonomy_compression_no_go"] == "20_OF_40_ONLY"
assert registry["program_fences"]["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["program_fences"]["third_lane"] == "NOT_PROMOTED"
assert all(value == "UNUSED" for value in registry["external_datum"].values())
assert ledger["schema_version"] == "0.75"
assert "GENERIC_CONTACT_THEOREM_ONLY" in registry["status"]
assert "Symplectic" in review
assert "PASS_WITH_MATERIAL_OWNERSHIP_CORRECTION" in review
print("PASS selected K77 action/contact Legendre-owner scope audit")

#!/usr/bin/env python3
"""Scope, Layer-0, source and hostile-review audit for the K77 split."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-physical-diffeomorphism-split-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-physical-diffeomorphism-split-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-physical-diffeomorphism-split-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.88.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-physical-diffeomorphism-split.json").read_text())

for phrase in (
    "The fourth physical diffeomorphism direction was not missing",
    "symmetric longitudinal complement",
    "This is a local kinematic naturality theorem",
    "P1/P2/P3 are unchanged and unused",
):
    assert phrase in report, phrase

assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "Mandatory symplectic-geometry lens" in review
assert "summary could outrun" in review.lower()
assert "superseded object" in review.lower()
assert "degree two is sampled" in review
assert registry["status"] == "PHYSICAL_SPLIT_CLOSES_LOCAL_PACKET__LOCAL_NATURALITY_ONLY"
assert registry["exact_split"]["physical_family_rank"] == 4
assert registry["exact_split"]["metric_skew_kosmann_rank"] == 3
assert registry["exact_split"]["longitudinal_response"] == "ZERO_SKEW__NONZERO_SYMMETRIC"
assert registry["constraint_accounting"] == {
    "continuous_parameters_selected": 0,
    "discrete_choices_selected": 0,
    "function_slots_selected": 0,
    "quotients_added": 0,
}
assert ledger["schema_version"] == "0.88"
assert ledger["source_return"] == "SOURCE-CONFIRMS"
assert ledger["frontier_delta"]["conditions_closed"] == 4
assert registry["scope_boundary"]["expanded_nonhomogeneous_selected_action_frechet"] == "OPEN"
assert registry["scope_boundary"]["symplectic_BFV_common_domain"] == "OPEN"
assert registry["scope_boundary"]["signature_ambient_horn"].startswith("OPEN_")
assert registry["scope_boundary"]["canon_status_public_posture"] == "UNCHANGED"

print("PASS selected K77 physical diffeomorphism split audit")

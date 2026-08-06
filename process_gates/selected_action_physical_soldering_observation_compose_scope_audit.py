#!/usr/bin/env python3
"""Fail-closed scope audit for local physical soldering/observation closure."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/selected-action-physical-soldering-observation-compose.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.28.json")
report = (ROOT / "explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-physical-soldering-observation-compose-review.md").read_text()

assert registry["status"].startswith("LOCAL_PRINCIPAL_PHYSICAL")
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["source"]["exact_composition_attribution"] == "REPOSITORY_DERIVED"
assert registry["exact_result"]["levi_civita_null_symbol_rank"] == 10
assert registry["exact_result"]["formal_adjoint_metric_receiver_rank"] == 10
assert registry["exact_result"]["observed_soldering_rank"] == 10
assert registry["exact_result"]["lifted_observed_soldering_equals_original"] is True
assert registry["exact_result"]["moving_section_response_nonzero"] is True
assert registry["exact_result"]["unrestricted_preboundary_nonzero"] is True
assert registry["exact_result"]["full_nonlinear_euler"] == "OPEN_SECOND_JETS"
assert registry["exact_result"]["odd_bv"] == "OPEN"
assert registry["exact_result"]["bfv"] == "OPEN"
assert registry["free_object_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "local principal first-order variational chain" in report
assert "summary outruns" in review
assert "superseded or mistyped object" in review
assert "Symplectic-geometry review" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_PHYSICAL_SOLDERING_OBSERVATION_COMPOSE_SCOPE_AUDIT_PASS")

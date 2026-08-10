#!/usr/bin/env python3
"""Audit the v0.130 moving-parent bundle disposition."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = json.loads((ROOT / "lab/process/selected-k77-moving-parent-bundle-observation-reduction.json").read_text())
LEDGER = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.130.json").read_text())

checks = {
    "moving rank split": RESULT["moving_projector"]["skew_rank"] + RESULT["moving_projector"]["complement_rank"] == 16384,
    "moving Euler wholesale": RESULT["moving_projector"]["moving_euler_covariance"] == "EXACT_PASS_ALL_16384",
    "carrier totals": RESULT["global_carriers"]["moving_spin_total"] == 113893 and RESULT["global_carriers"]["full_u_total"] == 229477,
    "two-half split": RESULT["two_half_reduction"]["block_connection_directions"] == RESULT["two_half_reduction"]["bifundamental_coset_directions"] == 8192,
    "skew crosses halves": RESULT["two_half_reduction"]["spin_skew_block_intersection"] + RESULT["two_half_reduction"]["spin_skew_coset_intersection"] == 8128,
    "observation counts": RESULT["observation_value_pullback"]["moving_spin_total"] == 32613 and RESULT["observation_value_pullback"]["full_u_total"] == 65637,
    "observation no selection": RESULT["observation_value_pullback"]["internal_parent_selected"] is False,
    "source return": RESULT["source_return"].startswith("SOURCE_CONFIRMS_FULL_U6464"),
    "validation": RESULT["validation"] == {"primary": "39/39_PASS", "independent_sage": "15/15_PASS"},
    "ledger version": LEDGER["schema_version"] == "0.130",
    "migrations": len(LEDGER["migrations"]) == 639,
    "frontier": LEDGER["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 0, "remaining_named_conditions": 1},
    "accounting fixed": RESULT["accounting"] == {"new_coefficients": 0, "new_quotients": 0, "new_external_datum": 0, "P1_P2_P3": "UNCHANGED_UNUSED"},
    "no verdict inflation": RESULT["claim_status_change"] == RESULT["canon_verdict_change"] == RESULT["public_posture_change"] == "none",
}

for label, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'} {label}")
if not all(checks.values()):
    raise SystemExit(1)
print(f"PASS {len(checks)}/{len(checks)}")

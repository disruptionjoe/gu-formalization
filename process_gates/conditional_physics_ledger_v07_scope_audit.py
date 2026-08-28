#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.7."""

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative

    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.7.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
registry = strict("lab/process/k77-global-chimeric-spin-reduction-and-support-normalization.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.7.md").read_text()
report = (ROOT / "explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-k77-global-chimeric-spin-reduction-review.md").read_text()

rows = {row["id"]: row for row in ledger["rows"]}
active = [row for row in rows.values() if row.get("row_status") != "SUPERSEDED"]

assert ledger["schema_version"] == "0.7"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.6.json")
assert len(active) == 82 and len(rows) == 83
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 83
assert ledger["residue"]["continuous_real_upper_if_lambda_def_independent"] == 84
assert ledger["residue"]["open_discrete_forks"] == 11
assert ledger["residue"]["quotients_ranked"] == 1
assert "conditional local" in ledger["residue"]["quotients_ranked_scope"]
assert rows["LT-GR2c"]["verdict"] == "NEEDS"
assert rows["LT-GR2c"]["reason_kind"] == "MISSING_CONSTRUCTION"
assert "GLOBAL_GAMMA_EPSILON_EXACT" in rows["LT-GR2c"]["mapping_grade"]
assert "PRIMARY_SUPPORT_WITHOUT_PROFILE_SELECTED" in rows["LT-GR2c"]["mapping_grade"]
assert "LAMBDA_DEF_ALIAS" in rows["LT-GR2c"]["mapping_grade"]

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.7.json"
)

assert registry["global_full_reduction"]["global"] is True
assert registry["global_full_reduction"]["labelled_rank"] == 14
assert registry["global_full_reduction"]["new_field_count"] == 0
assert registry["receiver_inheritance"]["receiver_rank"] == 10
assert registry["support_horns"]["primary"]["id"] == "BULK_PLUS_INDEPENDENT_X"
assert registry["support_horns"]["primary"]["transverse_profile_required"] is False
assert registry["normalization"]["new_continuous_parameter_added"] == "NOT_BOOKED_PENDING_ALIAS_ADJUDICATION"
assert registry["source_return"] == "SOURCE-CORRECTS"
assert registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED"

assert "SOURCE-CORRECTS" in report
assert "summary outruns the artifact" in review
assert "superseded or mistyped object" in review
assert "alias" in review.lower()
assert "82/82" in view and "global full gamma_epsilon" in view

print("PASS: v0.7 wires the source-owned global K77 full Clifford frame and profile-free independent-X support horn to the lambda_def/BV/null-Green gate without booking physical recovery")

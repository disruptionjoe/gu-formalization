#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.4."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative

    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.4.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
registry = strict("lab/process/source-native-curvature-vev-euler-rank.json")
lanes = (ROOT / "LANES.yaml").read_text()
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.4.md").read_text()
report = (ROOT / "explorations/conditional-build/source-native-curvature-vev-euler-rank-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-source-native-curvature-vev-euler-rank-review.md").read_text()

rows = {row["id"]: row for row in ledger["rows"]}
active = [row for row in rows.values() if row.get("row_status") != "SUPERSEDED"]
directive = contract["active_scientific_directives"][0]

assert ledger["schema_version"] == "0.4"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.3.json")
assert len(active) == 82 and len(rows) == 83
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 83
assert ledger["residue"]["quotients_ranked"] == 0
assert rows["LT-GR2b"]["verdict"] == "SAME"
assert "RANK_105_EXACT" in rows["LT-GR2c"]["mapping_grade"]
assert rows["LT-GR2d"]["reason_kind"] == "PROVEN_UNABLE_BY_CURRENT_ACTION"

assert contract["standing_ledger"]["ref"].endswith("v0.5.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.5.md")
assert "conditional-physics-ledger-v0.5.json" in lanes
assert directive["source_return"] == "SOURCE-SILENT"
assert "EPSILON_IG_GRAVITATIONAL_SOLDERING" in directive["next_gate"]

assert registry["exact_results"]["ambient_curvature_covariation_rank"] == 105
assert registry["exact_results"]["total_homogeneous_T_Euler_rank_fixed_nonzero_gain"] == 196
assert registry["exact_results"]["T_only_row_count"] == 91
assert registry["exact_results"]["native_BV_quotient_rank"] == "UNDEFINED"
assert registry["exact_results"]["vacuum_shift"] == "TRACKED_INTO_T__NOT_SCREENED"

assert "circular to demand" in report
assert "Lambda g` spans only the one-dimensional" in report
assert "summary outruns the artifact" in review
assert "superseded or mistyped object" in review
assert "82/82" in view and "Quotients ranked: 0" in view
assert all(token in report for token in ("P1/P2/P3", "canon", "public posture"))

print("PASS: historical v0.4 ambient curvature/VEV action-rank result remains intact beneath current v0.5 soldering/weld/null-domain wiring")

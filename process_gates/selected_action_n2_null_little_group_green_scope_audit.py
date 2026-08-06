#!/usr/bin/env python3
"""Fail-closed scope audit for N2 little-group and Green-flux typing."""

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


registry = strict(ROOT / "lab/process/selected-action-n2-null-little-group-green.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.37.json")
report = (ROOT / "explorations/conditional-build/selected-action-n2-null-little-group-green-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-n2-null-little-group-green-review.md").read_text()

assert registry["status"].startswith("EXACT_N2_COMPACT_NULL_LITTLE_GROUP_HELICITY_ONE")
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
exact = registry["exact_result"]
assert exact["kernel_dimension"] == 6 and exact["gauge_dimension"] == 4
assert exact["extra_mode_dimension"] == 2
rotation = exact["compact_null_rotation"]
assert rotation["quotient_generator"] == [[0, -1], [1, 0]]
assert rotation["characteristic_polynomial"] == "x^2+1"
assert rotation["spin_two_target_polynomial"] == "x^2+4"
assert rotation["disposition"] == "WRONG_HELICITY_FOR_GRAVITON"
green = exact["principal_green_flux"]
assert green["rank_on_two_mode_quotient"] == 2
assert green["gauge_cross_rank"] == 0
assert green["global_domain"].startswith("OPEN")
assert registry["disposition"]["fired"] == "N2_WRONG_HELICITY"
assert "completed first-layer grade-one bank" in registry["disposition"]["scope"]
assert "every possible source-action completion" in registry["disposition"]["not_killed"]
assert registry["ledger_effect"]["verdict_change"] == "NONE"
assert registry["free_object_delta"] == registry["quotient_count_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}

assert ledger["schema_version"] == "0.37"
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert "LT-GR3" in ledger["next_work_queue"][0]["rows"]
assert "I2B" in ledger["next_work_queue"][0]["why"]
assert "helicity-one" in ledger["next_work_queue"][0]["why"]

assert "helicity-`\u00b11`" in report
assert "helicity-two" in report
assert "A live flux cannot repair wrong helicity" in report
assert "scoped route kill" in report.lower()
assert "Symplectic-geometry lens (mandatory)" in review
assert "summary outrun" in review.lower()
assert "superseded or mistyped object" in review
assert "local principal Green flux" in review

assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_N2_NULL_LITTLE_GROUP_GREEN_SCOPE_AUDIT_PASS")

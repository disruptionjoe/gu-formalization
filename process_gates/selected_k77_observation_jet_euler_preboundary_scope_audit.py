#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.62 K77 observation-jet gate."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/selected-k77-observation-jet-euler-preboundary-sufficiency.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.62.json")
report = (ROOT / "explorations/conditional-build/selected-k77-observation-jet-euler-preboundary-sufficiency-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-k77-observation-jet-euler-preboundary-review.md").read_text(encoding="utf-8")

assert registry["null_response"]["rank"] == 1470
assert registry["null_response"]["nullity"] == 0
assert registry["null_response"]["independent_sage_flint_qq_rank"] == 1470
assert registry["principal_symbol"]["rank"] == 650
assert registry["principal_symbol"]["nullity"] == 820
assert registry["boundary"]["green_owner_required"] is True
assert registry["boundary"]["invariant_action_pairing_built"] is False
assert registry["boundary"]["reduced_presymplectic_class_built"] is False
assert registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED"
assert ledger["schema_version"] == "0.62"
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert ledger["residue"]["continuous_real"] == 84
assert "not an Euler covector" in review
assert "paired first variation" in report
for forbidden in ("Einstein equation recovered", "BFV phase space constructed", "P1 consumed"):
    assert forbidden not in report

print("PASS selected K77 observation-jet Euler/preboundary scope audit")

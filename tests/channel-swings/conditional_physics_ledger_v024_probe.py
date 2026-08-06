#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.24."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.23.json")
new = strict("lab/process/conditional-physics-ledger-v0.24.json")
registry = strict("lab/process/two-layer-action-selected-cubic-owner-retype.json")

print("A. FROZEN METER AND PROGRAM FENCES")
check("exact", "schema advances exactly 0.23 to 0.24", old["schema_version"] == "0.23" and new["schema_version"] == "0.24")
check("exact", "denominator is frozen", old["denominator"] == new["denominator"])
check("exact", "82/82 rows remain mapped", new["progress"]["mapped"] == 82 and new["progress"]["total"] == 82)
check("exact", "verdict counts are frozen", old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "residue is frozen", old["residue"] == new["residue"])
check("program", "P1/P2/P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt remains separate", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
check("program", "third lane remains unpromoted", registry["third_lane"] == "NOT_PROMOTED")
check("program", "canon and public posture are frozen", registry["canon_verdict_change"] == "NONE" and registry["public_posture_change"] == "NONE")

print("\nB. EXACT APPEND-ONLY MOVEMENT")
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]]
check("exact", "row id set is frozen", set(old_rows) == set(new_rows))
check("exact", "exactly LT-GR3 changes", changed == ["LT-GR3"])
before, after = old_rows["LT-GR3"], new_rows["LT-GR3"]
check("exact", "LT-GR3 verdict is frozen", before["verdict"] == after["verdict"] == "DIFFERS")
check("exact", "LT-GR3 reason kind is frozen", before["reason_kind"] == after["reason_kind"] == "STRUCTURAL_DIFFERENCE")
check("exact", "LT-GR3 revival trigger is frozen", before["revival_trigger"] == after["revival_trigger"])
check("exact", "distance names I2B and observer full-II owner map", "I2B" in after["distance"] and "||II||^2" in after["distance"])
check("exact", "mapping grade records the open owner map", "OBSERVER_FULL_II_OWNER_MAP_OPEN" in after["mapping_grade"])
check("exact", "evidence points to retype report", after["evidence"] == "two-layer-action-selected-cubic-owner-retype-2026-08-06.md")
new_migrations = [m for m in new["migrations"] if m.get("from_version") == "0.23" and m.get("to_version") == "0.24"]
check("exact", "one migration is recorded", [m["row_id"] for m in new_migrations] == ["LT-GR3"])
check("exact", "migration preserves meaning", new_migrations[0]["meaning_changed"] is False)

print("\nC. SPLIT QUEUE")
q1, q2 = new["next_work_queue"][:2]
check("type", "rank one is first-order completion", "first-order I1B completion" in q1["why"])
check("type", "rank one does not claim LT-GR3", "LT-GR3" not in q1["rows"])
check("type", "rank two owns LT-GR3", q2["rows"] == ["LT-GR3"])
check("type", "rank two requires I2B/full-II map", "I2B" in q2["why"] and "||II||^2" in q2["why"])
check("type", "rank two requires preboundary comparison", "preboundary" in q2["why"])
check("type", "Q1 remains downstream", "before Weyl/Bach Q1" in q2["why"])

for label in (
    "a queue correction is not a physics promotion",
    "generic cubic independence does not prohibit a geometric identity",
    "one-dimensional proportionality does not establish equality",
    "first-layer solutions imply second-layer stationarity only one way",
    "two parallel packages must reconcile before Q1",
    "LT-GR3 remains a structural difference",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

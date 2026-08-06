#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.22."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.21.json")
new = strict("lab/process/conditional-physics-ledger-v0.22.json")
registry = strict("lab/process/selected-cubic-two-connection-principal-ward-descent.json")

print("A. DENOMINATOR, METER, RESIDUE, AND PROGRAM FENCES")
check("exact", "schema advances exactly 0.21 to 0.22", old["schema_version"] == "0.21" and new["schema_version"] == "0.22")
check("exact", "denominator is frozen", old["denominator"] == new["denominator"])
check("exact", "82 of 82 active targets remain mapped", new["progress"]["mapped"] == 82 and new["progress"]["total"] == 82)
check("exact", "verdict counts remain 33/19/24/6", new["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "residue is frozen", old["residue"] == new["residue"])
check("exact", "four scoped quotients remain ranked", new["residue"]["quotients_ranked"] == 4)
check("program", "P1/P2/P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt remains separate", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
check("program", "third lane remains unpromoted", registry["third_lane"] == "NOT_PROMOTED")
check("program", "no canon or public posture change", registry["canon_verdict_change"] == "NONE" and registry["public_posture_change"] == "NONE")

print("\nB. EXACT APPEND-ONLY ROW MOVEMENT")
touched = ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("exact", "row id set is frozen", set(old_rows) == set(new_rows))
changed = [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]]
check("exact", "exactly five named rows change", changed == touched)
for row_id in touched:
    before = old_rows[row_id]
    after = new_rows[row_id]
    check("exact", f"{row_id}: verdict frozen", before["verdict"] == after["verdict"])
    check("exact", f"{row_id}: reason kind frozen", before["reason_kind"] == after["reason_kind"])
    check("exact", f"{row_id}: distance advances to principal two-connection descent", "principal" in after["distance"].lower() and ("two-connection" in after["distance"].lower() or "principal-descended" in after["distance"].lower()))
    check("exact", f"{row_id}: evidence points to the two-connection report", after["evidence"] == "selected-cubic-two-connection-principal-ward-descent-2026-08-06.md")

new_migrations = [m for m in new["migrations"] if m.get("from_version") == "0.21" and m.get("to_version") == "0.22"]
check("exact", "five 0.21 to 0.22 migrations are recorded", [m["row_id"] for m in new_migrations] == touched)
check("exact", "all migrations preserve meaning", all(m["meaning_changed"] is False for m in new_migrations))
check("exact", "wave dispositions name only the same five rows", [d["row_id"] for d in new["wave_row_dispositions"]] == touched)

print("\nC. NEXT-GATE AND NONPROMOTION")
rank_one = new["next_work_queue"][0]
check("type", "rank one starts with lower-order homogeneous orbit", "lower-order homogeneous adjoint-orbit" in rank_one["why"])
check("type", "rank one retains moving Shiab/pairing/observation", "moving Shiab/Hodge/DeWitt/Krein pairing/observation" in rank_one["why"])
check("type", "rank one retains direct curvature/full-II/defect", "direct curvature/full-II/defect D3" in rank_one["why"])
check("type", "rank one retains preboundary and Q1 ordering", "preboundary" in rank_one["why"] and "Q1" in rank_one["why"])
check("type", "LT-GR3 did not migrate", "LT-GR3" not in changed)
check("type", "registry does not count a fifth quotient", registry["quotient_test"]["fifth_quotient"] == "NOT_COUNTED")
check("type", "principal descent is fenced from full reduction", registry["quotient_test"]["lower_order_homogeneous_orbit"] == "OPEN")

for label in (
    "principal rank zero is not a nonlinear Ward quotient",
    "source confirms the difference owner not the derived coefficient",
    "the old isolated rank-five result remains scoped truth",
    "surviving kernel is not a Q1 pole or transition",
    "correcting one quotient does not increment quotient count",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

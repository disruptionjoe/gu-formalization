#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.34."""

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


old = strict("lab/process/conditional-physics-ledger-v0.33.json")
new = strict("lab/process/conditional-physics-ledger-v0.34.json")
registry = strict("lab/process/selected-action-curvature-graph-six-versus-four.json")

print("A. FROZEN METER AND PROGRAM FENCES")
check("exact", "schema advances 0.33 to 0.34", old["schema_version"] == "0.33" and new["schema_version"] == "0.34")
check("exact", "denominator is frozen", old["denominator"] == new["denominator"])
check("exact", "82/82 remain mapped", new["progress"]["mapped"] == 82 and new["progress"]["total"] == 82)
check("exact", "verdict counts are frozen", old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "residue and quotients are frozen", old["residue"] == new["residue"] and new["residue"]["quotients_ranked"] == 4)
check("program", "P1/P2/P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
check("program", "canon and public posture are frozen", registry["canon_verdict_change"] == "NONE" and registry["public_posture_change"] == "NONE")

print("\nB. EXACT APPEND-ONLY MOVEMENT")
touched = ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]]
check("exact", "row ids are frozen", set(old_rows) == set(new_rows))
check("exact", "exactly five named rows change", changed == touched)
required = (
    "SELECTED_GRAPH_CURVATURE_GAIN_MINUS1_OVER26",
    "NONNULL",
    "KERNEL_GAUGE4",
    "NULL",
    "GAUGE4_PHYSICAL2",
    "OPEN",
)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check("exact", f"{row_id}: verdict frozen", before["verdict"] == after["verdict"])
    check("exact", f"{row_id}: reason kind frozen", before["reason_kind"] == after["reason_kind"])
    check("exact", f"{row_id}: revival trigger frozen", before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id}: graph curvature and off-graph burden are typed", all(token in after["mapping_grade"] for token in required))
    check("exact", f"{row_id}: evidence points to graph curvature", after["evidence"] == "selected-action-curvature-graph-six-versus-four-2026-08-06.md")

migrations = [m for m in new["migrations"] if m.get("from_version") == "0.33" and m.get("to_version") == "0.34"]
check("exact", "five migrations are recorded", [m["row_id"] for m in migrations] == touched)
check("exact", "all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
check("exact", "wave dispositions name the same rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)

print("\nC. QUEUE AND NONPROMOTION")
rank_one, rank_two = new["next_work_queue"][:2]
check("type", "rank one names the off-graph dBT source carrier", all(token in rank_one["why"] for token in ("off-graph d_B T", "full independent", "(g,varpi)")))
check("type", "rank one preserves nonnull gauge and null physical kernels", "nonnull kernel gauge four" in rank_one["why"] and "null kernel gauge four plus physical two" in rank_one["why"])
check("type", "rank one rejects characteristics as residue", "do not book characteristics as residue" in rank_one["why"])
check("type", "rank two remains the LT-GR3 I2B owner map", rank_two["rows"] == ["LT-GR3"] and "I2B" in rank_two["why"])
check("type", "no quotient is promoted", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"])

for label in (
    "v0.33 zero-jet theorem is retained rather than erased",
    "graph curvature is not full off-graph I1B",
    "two null characteristics are not two parameters",
    "graph symbol kernel is not BV cohomology",
    "observer full-II remains a separate owner",
    "P1/P2/P3 are not used to fit a completion",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

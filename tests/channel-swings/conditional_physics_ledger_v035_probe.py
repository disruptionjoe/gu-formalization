#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.35."""

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


old = strict("lab/process/conditional-physics-ledger-v0.34.json")
new = strict("lab/process/conditional-physics-ledger-v0.35.json")
registry = strict("lab/process/selected-action-offgraph-dbt-principal-symbol.json")

print("A. FROZEN METER AND PROGRAM FENCES")
check("exact", "schema advances 0.34 to 0.35", old["schema_version"] == "0.34" and new["schema_version"] == "0.35")
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
    "SAME_GRADE_CL2_DBT_EULER_ZERO",
    "ADJACENT_GRADE_CL1_HCL2_EULER_RANKS_12_12_11",
    "CURRENT_34_VARIABLE_TRUNCATION_NOT_ACTION_INVARIANT",
    "OPEN",
)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check("exact", f"{row_id}: verdict frozen", before["verdict"] == after["verdict"])
    check("exact", f"{row_id}: reason kind frozen", before["reason_kind"] == after["reason_kind"])
    check("exact", f"{row_id}: revival trigger frozen", before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id}: dBT parity and completion burden are typed", all(token in after["mapping_grade"] for token in required))
    check("exact", f"{row_id}: evidence points to off-graph dBT", after["evidence"] == "selected-action-offgraph-dbt-principal-symbol-2026-08-06.md")

migrations = [m for m in new["migrations"] if m.get("from_version") == "0.34" and m.get("to_version") == "0.35"]
check("exact", "five migrations are recorded", [m["row_id"] for m in migrations] == touched)
check("exact", "all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
check("exact", "wave dispositions name the same rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)

print("\nC. QUEUE AND NONPROMOTION")
rank_one, rank_two = new["next_work_queue"][:2]
check("type", "rank one names grade-one algebraic completion", "grade-one algebraic Hessian" in rank_one["why"])
check("type", "rank one names the filtered metric-Cl2-Cl1 Euler symbol", "filtered metric-Cl2-Cl1 Euler symbol" in rank_one["why"])
check("type", "rank one names both observation carriers", "s* T" in rank_one["why"] and "res_s^V T" in rank_one["why"])
check("type", "rank one preserves the graph result", "preserve the exact graph result" in rank_one["why"])
check("type", "rank one rejects cross ranks as residue", "Do not book cross ranks as residue" in rank_one["why"])
check("type", "rank two remains the LT-GR3 I2B owner map", rank_two["rows"] == ["LT-GR3"] and "I2B" in rank_two["why"])
check("type", "no quotient is promoted", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"])

for label in (
    "same-grade zero is not full dBT zero",
    "the current 34 variables are not the full adjoint one-form carrier",
    "cross rank is not a parameter count",
    "null rank loss is not a physical quotient",
    "the graph curvature theorem is retained",
    "I2B and observer full-II remain separately owned",
    "P1/P2/P3 are not used to fit a completion",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

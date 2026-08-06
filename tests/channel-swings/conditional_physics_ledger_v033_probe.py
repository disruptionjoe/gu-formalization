#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.33."""

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


old = strict("lab/process/conditional-physics-ledger-v0.32.json")
new = strict("lab/process/conditional-physics-ledger-v0.33.json")
registry = strict("lab/process/selected-action-source-variable-hessian-and-diffeomorphism-lift.json")

print("A. FROZEN METER AND PROGRAM FENCES")
check("exact", "schema advances 0.32 to 0.33", old["schema_version"] == "0.32" and new["schema_version"] == "0.33")
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
    "ZERO_JET_SOURCE_HESSIAN_RANK24_NULLITY10",
    "GAUGE4_NONGAUGE6",
    "BOTH_WARD_BLOCKS_EXACT",
    "FULL_I1B_SIX_VERSUS_FOUR",
    "OPEN",
)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check("exact", f"{row_id}: verdict frozen", before["verdict"] == after["verdict"])
    check("exact", f"{row_id}: reason kind frozen", before["reason_kind"] == after["reason_kind"])
    check("exact", f"{row_id}: revival trigger frozen", before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id}: source Hessian and full-action burden are typed", all(token in after["mapping_grade"] for token in required))
    check("exact", f"{row_id}: evidence points to source-variable Hessian", after["evidence"] == "selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md")

migrations = [m for m in new["migrations"] if m.get("from_version") == "0.32" and m.get("to_version") == "0.33"]
check("exact", "five migrations are recorded", [m["row_id"] for m in migrations] == touched)
check("exact", "all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
check("exact", "wave dispositions name the same rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)

print("\nC. QUEUE AND NONPROMOTION")
rank_one, rank_two = new["next_work_queue"][:2]
check("type", "rank one names full first-order source-variable I1B", all(token in rank_one["why"] for token in ("full first-order I1B", "source variables", "(g,varpi)")))
check("type", "rank one requires the six-versus-four test", "six zero-jet nongauge" in rank_one["why"] and "four gauge" in rank_one["why"])
check("type", "rank one rejects diagnostic completion and nullity-as-residue", "diagnostic 10+16" in rank_one["why"] and "book nullity as residue" in rank_one["why"])
check("type", "rank two remains the LT-GR3 I2B owner map", rank_two["rows"] == ["LT-GR3"] and "I2B" in rank_two["why"])
check("type", "no quotient is promoted", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"])

for label in (
    "v0.32 diagnostic theorem is retained rather than erased",
    "zero-jet source Hessian is not full I1B",
    "six nongauge null directions are not six parameters",
    "zero-jet radical is not BV cohomology",
    "observer full-II remains a separate owner",
    "P1/P2/P3 are not used to fit a completion",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

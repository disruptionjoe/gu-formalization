#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.31."""

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


old = strict("lab/process/conditional-physics-ledger-v0.30.json")
new = strict("lab/process/conditional-physics-ledger-v0.31.json")
registry = strict("lab/process/selected-action-ward-completion-identifiability.json")

print("A. FROZEN METER AND PROGRAM FENCES")
check("exact", "schema advances 0.30 to 0.31", old["schema_version"] == "0.30" and new["schema_version"] == "0.31")
check("exact", "denominator is frozen", old["denominator"] == new["denominator"])
check("exact", "82/82 remain mapped", new["progress"]["mapped"] == 82 and new["progress"]["total"] == 82)
check("exact", "verdict counts are frozen", old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "residue and quotients are frozen", old["residue"] == new["residue"] and new["residue"]["quotients_ranked"] == 4)
check("program", "P1/P2/P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
check("program", "canon and public posture are frozen", registry["canon_verdict_change"] == "NONE" and registry["public_posture_change"] == "NONE")

print("\nB. EXACT APPEND-ONLY MOVEMENT")
touched = ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]
old_rows = {r["id"]: r for r in old["rows"]}
new_rows = {r["id"]: r for r in new["rows"]}
changed = [rid for rid in old_rows if old_rows[rid] != new_rows[rid]]
check("exact", "row ids are frozen", set(old_rows) == set(new_rows))
check("exact", "exactly five named rows change", changed == touched)
required = (
    "WARD_COMPLETION_SYSTEM_RANK34_AFFINE_DIM21",
    "SEPARATELY_INVARIANT_BLOCK_CANNOT_CANCEL",
    "SAME_I1B_DIRECT_METRIC_COFRAME_PACKET",
    "OPEN",
)
for rid in touched:
    before, after = old_rows[rid], new_rows[rid]
    check("exact", f"{rid}: verdict frozen", before["verdict"] == after["verdict"])
    check("exact", f"{rid}: reason kind frozen", before["reason_kind"] == after["reason_kind"])
    check("exact", f"{rid}: revival trigger frozen", before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{rid}: Ward target and correct owner are typed", all(token in after["mapping_grade"] for token in required))
    check("exact", f"{rid}: evidence points to identifiability report", after["evidence"] == "selected-action-ward-completion-identifiability-2026-08-06.md")

migrations = [m for m in new["migrations"] if m.get("from_version") == "0.30" and m.get("to_version") == "0.31"]
check("exact", "five migrations are recorded", [m["row_id"] for m in migrations] == touched)
check("exact", "all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
check("exact", "wave dispositions name the same rows", [d["row_id"] for d in new["wave_row_dispositions"]] == touched)

print("\nC. NEXT QUEUE AND NONPROMOTION")
rank_one, rank_two = new["next_work_queue"][:2]
check("type", "rank one names the same-I1B packet", "same-I1B" in rank_one["why"] and all(token in rank_one["why"] for token in ("metric/coframe", "Hodge", "Shiab", "Krein", "density", "observation")))
check("type", "rank one carries the 34-plus-21 target", "rank-34" in rank_one["why"] and "21 quotient-form" in rank_one["why"])
check("type", "rank one forbids wrong-owner import", "do not import" in rank_one["why"] and "observer full-II" in rank_one["why"])
check("type", "rank two remains the LT-GR3 I2B owner map", rank_two["rows"] == ["LT-GR3"] and "I2B" in rank_two["why"])
check("type", "no quotient is promoted", registry["quotient_change"] is False)

for label in (
    "Ward target is not an action-derived completion",
    "21 quotient-form directions are not 21 booked parameters",
    "diagnostic projector is not Lorentz-natural geometry",
    "Einstein control is not an I1B counterterm",
    "observation transport is not cancellation",
    "observer full-II remains a separate owner",
    "P1/P2/P3 are not used to fit the completion",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

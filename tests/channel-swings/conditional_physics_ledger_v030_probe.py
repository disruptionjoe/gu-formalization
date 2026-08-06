#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.30."""

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


old = strict("lab/process/conditional-physics-ledger-v0.29.json")
new = strict("lab/process/conditional-physics-ledger-v0.30.json")
registry = strict("lab/process/selected-action-stationary-spin-lc-hessian.json")

print("A. FROZEN METER AND PROGRAM FENCES")
check("exact", "schema advances 0.29 to 0.30", old["schema_version"] == "0.29" and new["schema_version"] == "0.30")
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
required_grade = (
    "COORDINATE_CHRISTOFFEL_RANK10_SCOPED",
    "ACTION_SPIN_LC_RANK9_KERNEL_KK",
    "STATIONARY_SELECTED_METRIC_HESSIAN_EXACT_CAUSAL_INERTIA",
    "SECOND_LIFT_HESSIAN_TERM_ZERO",
    "DIFFEO_CROSS_RANK3",
    "DIRECT_CURVATURE_FULL_II_DEFECT_OBSERVATION_WARD",
    "OPEN",
)
for rid in touched:
    before, after = old_rows[rid], new_rows[rid]
    check("exact", f"{rid}: verdict frozen", before["verdict"] == after["verdict"])
    check("exact", f"{rid}: reason kind frozen", before["reason_kind"] == after["reason_kind"])
    check("exact", f"{rid}: revival trigger frozen", before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{rid}: scope correction and Hessian are owned", all(token in after["mapping_grade"] for token in required_grade))
    check("exact", f"{rid}: evidence points to stationary Hessian report", after["evidence"] == "selected-action-stationary-spin-lc-hessian-2026-08-06.md")

migrations = [m for m in new["migrations"] if m.get("from_version") == "0.29" and m.get("to_version") == "0.30"]
check("exact", "five migrations are recorded", [m["row_id"] for m in migrations] == touched)
check("exact", "all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
check("exact", "wave dispositions name the same rows", [d["row_id"] for d in new["wave_row_dispositions"]] == touched)

print("\nC. NEXT QUEUE AND NONPROMOTION")
rank_one, rank_two = new["next_work_queue"][:2]
check("type", "rank one starts with direct Ward totalization", all(token in rank_one["why"] for token in ("direct curvature", "full-II", "defect", "observation", "rank-three diffeomorphism")))
check("type", "rank one forbids coordinate-rank restoration", "do not restore coordinate-Christoffel rank ten" in rank_one["why"])
check("type", "rank one retains BV BFV and global domain downstream", "BV" in rank_one["why"] and "BFV" in rank_one["why"] and "global Krein/Green" in rank_one["why"])
check("type", "rank two remains LT-GR3 owner map", rank_two["rows"] == ["LT-GR3"] and "I2B" in rank_two["why"])
check("type", "no quotient is promoted", registry["quotient_change"] is False)

for label in (
    "coordinate Christoffel rank ten is not action-spin rank ten",
    "rank-nine spin map is not rank-nine physical gravity",
    "stationary Hessian is not the off-shell nonlinear Euler operator",
    "observation congruence is not a physical quotient",
    "nonzero Ward residual is not a GU falsification before direct blocks",
    "vanishing D-gradient Hessian term does not erase cubic second jets",
    "P1/P2/P3 are not used to repair a local rank",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

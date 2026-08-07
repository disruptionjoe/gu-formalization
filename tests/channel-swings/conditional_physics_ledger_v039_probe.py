#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.39."""

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


old = strict("lab/process/conditional-physics-ledger-v0.38.json")
new = strict("lab/process/conditional-physics-ledger-v0.39.json")
registry = strict("lab/process/selected-second-layer-full-cl2-residual-pullback.json")

print("A. METER AND PROGRAM FENCES")
check("exact", "schema advances 0.38 to 0.39", old["schema_version"] == "0.38" and new["schema_version"] == "0.39")
check("exact", "denominator verdicts and coverage are frozen",
      old["denominator"] == new["denominator"]
      and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6}
      and new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("exact", "residue and four scoped quotients are frozen", old["residue"] == new["residue"] and new["residue"]["quotients_ranked"] == 4)
check("program", "P1 P2 P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
check("program", "canon claim and public posture remain unchanged", registry["canon_verdict_change"] == registry["claim_status_change"] == registry["public_posture_change"] == "NONE")

print("\nB. APPEND-ONLY ROW MOVEMENT")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]]
check("exact", "row identities are frozen", set(old_rows) == set(new_rows))
check("exact", "exactly five named rows change", changed == touched)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check("exact", f"{row_id}: verdict reason summary and revival trigger are frozen",
          before["verdict"] == after["verdict"] and before["reason_kind"] == after["reason_kind"]
          and before["summary"] == after["summary"] and before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id}: evidence points to full Cl2 result", after["evidence"] == "selected-second-layer-full-cl2-residual-pullback-2026-08-07.md")
    check("exact", f"{row_id}: mapping records selected Cl2 and remaining total residual", "CL2" in after["mapping_grade"] and "TOTAL_RESIDUAL_OTHER_GRADES" in after["mapping_grade"])

migrations = [item for item in new["migrations"] if item.get("from_version") == "0.38" and item.get("to_version") == "0.39"]
check("exact", "five migrations are recorded in row order", [item["row_id"] for item in migrations] == touched)
check("exact", "all migrations preserve row meanings", all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name the same five rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)
check("exact", "all row moves are distance or priority only", all("VERDICT" not in item["change"] for item in new["wave_row_dispositions"]))

print("\nC. EXACT CONSTRUCTION DISPOSITION")
exact = registry["exact_result"]
check("exact", "target shape rank and sparsity are exact", exact["target_shape"] == [1274, 100] and exact["target_rank"] == 100 and exact["nonzero_entries"] == 640)
check("exact", "full Cl2 coefficients replace the projected trace coefficient", exact["full_ii_coefficient"] == "15376/13689" and exact["trace_square_coefficient"] == "-340/4563" and exact["orthogonal_leakage_trace_increment"] == "4/169")
check("type", "rank one now targets total-residual other-grade support", "total bosonic-plus-fermionic residual" in new["next_work_queue"][0]["why"] and "other-grade" in new["next_work_queue"][0]["why"])
check("type", "selected Cl2 is closed while total residual stays open", registry["disposition"]["closed"] == "SELECTED_CL2_COMPLETENESS" and registry["disposition"]["open"] == "TOTAL_RESIDUAL_OTHER_CLIFFORD_GRADE_SUPPORT")

for label in (
    "selected Cl2 is not the total residual",
    "full rank is not helicity two",
    "native inertia is not positive physical energy",
    "stationary quadratic equality is not Euler or preboundary equivalence",
    "source silence is not a construction failure",
    "no coefficient residue quotient or external datum is booked",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

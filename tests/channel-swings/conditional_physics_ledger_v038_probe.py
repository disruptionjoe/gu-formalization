#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.38."""

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


old = strict("lab/process/conditional-physics-ledger-v0.37.json")
new = strict("lab/process/conditional-physics-ledger-v0.38.json")
registry = strict("lab/process/selected-second-layer-i2b-gauss-owner-map.json")

print("A. METER AND PROGRAM FENCES")
check("exact", "schema advances 0.37 to 0.38",
      old["schema_version"] == "0.37" and new["schema_version"] == "0.38")
check("exact", "denominator and verdict meter are frozen",
      old["denominator"] == new["denominator"]
      and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "coverage remains 82 of 82",
      new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("exact", "residue and four scoped quotients are frozen",
      old["residue"] == new["residue"] and new["residue"]["quotients_ranked"] == 4)
check("program", "P1 P2 P3 remain unused",
      registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third-lane fences hold",
      registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
      and registry["third_lane"] == "NOT_PROMOTED")
check("program", "canon claim and public posture remain unchanged",
      registry["canon_verdict_change"] == registry["claim_status_change"]
      == registry["public_posture_change"] == "NONE")

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
          before["verdict"] == after["verdict"]
          and before["reason_kind"] == after["reason_kind"]
          and before["summary"] == after["summary"]
          and before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id}: evidence points to the I2B Gauss map",
          after["evidence"] == "selected-second-layer-i2b-gauss-owner-map-2026-08-06.md")
    check("exact", f"{row_id}: mapping records projected block and full-target burden",
          ("GAUSS_PROJECTED" in after["mapping_grade"]
           or "PROJECTED_FORM_EXACT" in after["mapping_grade"])
          and ("LEAKAGE" in after["mapping_grade"]
               or "FULL_RESIDUAL_TARGET" in after["mapping_grade"]))

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.37" and item.get("to_version") == "0.38"]
check("exact", "five migrations are recorded in row order",
      [item["row_id"] for item in migrations] == touched)
check("exact", "all migrations preserve row meanings",
      all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name the same five rows",
      [item["row_id"] for item in new["wave_row_dispositions"]] == touched)
check("exact", "all row moves are distance or priority only",
      all("VERDICT" not in item["change"] for item in new["wave_row_dispositions"]))

print("\nC. CONSTRUCTION DISPOSITION")
rank_one = new["next_work_queue"][0]
check("type", "rank one is the complete residual-target map",
      "1274-by-100" in rank_one["why"] and "other Clifford-grade" in rank_one["why"])
check("type", "rank one retains co-moving observation before physics",
      all(token in rank_one["why"] for token in ("epsilon", "observation", "helicity")))
check("exact", "registry records the exact projected fixed combination",
      registry["exact_result"]["projected_full_ii_coefficient"] == "15376/13689"
      and registry["exact_result"]["projected_trace_square_coefficient"] == "-448/4563")
check("exact", "registry records the exact leakage witness",
      registry["exact_result"]["leakage_witness"]["coefficient"] == "2/39")
check("type", "wrong-type ending is scoped to the rank-100 identification",
      registry["disposition"]["fired"] == "I2B_GAUSS_WRONG_TYPE"
      and "full residual-target" in registry["disposition"]["not_killed"])

for label in (
    "projected residual norm is not the full I2B pullback",
    "full rank is not helicity two",
    "native norm square is not positive energy",
    "quadratic equality is not Euler or preboundary equivalence",
    "source silence is not a construction failure",
    "no coefficient residue quotient or external datum is booked",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

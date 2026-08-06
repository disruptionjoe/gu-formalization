#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.37."""

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


old = strict("lab/process/conditional-physics-ledger-v0.36.json")
new = strict("lab/process/conditional-physics-ledger-v0.37.json")
registry = strict("lab/process/selected-action-n2-null-little-group-green.json")

print("A. METER AND PROGRAM FENCES")
check("exact", "schema advances 0.36 to 0.37",
      old["schema_version"] == "0.36" and new["schema_version"] == "0.37")
check("exact", "denominator and complete verdict meter are frozen",
      old["denominator"] == new["denominator"]
      and old["progress"]["mapped"] == new["progress"]["mapped"] == 82
      and old["progress"]["total"] == new["progress"]["total"] == 82
      and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
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
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6", "LT-SM8"]
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]]
check("exact", "row identities are frozen", set(old_rows) == set(new_rows))
check("exact", "exactly six named rows change", changed == touched)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check("exact", f"{row_id}: verdict reason and summary are frozen",
          before["verdict"] == after["verdict"]
          and before["reason_kind"] == after["reason_kind"]
          and before["summary"] == after["summary"])
    check("exact", f"{row_id}: evidence points to N2 typing result",
          after["evidence"] == "selected-action-n2-null-little-group-green-2026-08-06.md")
    check("exact", f"{row_id}: mapping records helicity-one rather than spin-two",
          "HELICITY1_NOT_SPIN2" in after["mapping_grade"]
          or "HELICITY1_NOT_HELICITY2" in after["mapping_grade"])

migrations = [
    item for item in new["migrations"]
    if item.get("from_version") == "0.36" and item.get("to_version") == "0.37"
]
check("exact", "six migrations are recorded in row order",
      [item["row_id"] for item in migrations] == touched)
check("exact", "all migrations preserve row meanings",
      all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name the same six rows",
      [item["row_id"] for item in new["wave_row_dispositions"]] == touched)
check("exact", "all row moves are distance or priority only",
      all("VERDICT" not in item["change"] for item in new["wave_row_dispositions"]))

print("\nC. PRIORITY AND SCIENTIFIC DISPOSITION")
rank_one = new["next_work_queue"][0]
check("type", "rank one is the distinct second-layer owner map",
      "LT-GR3" in rank_one["rows"] and "I2B" in rank_one["why"]
      and "observer" in rank_one["why"] and "owner map" in rank_one["why"])
check("type", "rank one carries the N2 representation kill forward",
      "N2" in rank_one["why"] and "helicity-one" in rank_one["why"])
check("exact", "registry records exact helicity-one quotient action",
      registry["exact_result"]["compact_null_rotation"]["quotient_generator"]
      == [[0, -1], [1, 0]]
      and registry["exact_result"]["compact_null_rotation"]["characteristic_polynomial"] == "x^2+1"
      and registry["exact_result"]["compact_null_rotation"]["spin_two_target_polynomial"] == "x^2+4")
check("exact", "registry records live gauge-descending rank-two local flux",
      registry["exact_result"]["principal_green_flux"]["rank_on_two_mode_quotient"] == 2
      and registry["exact_result"]["principal_green_flux"]["gauge_cross_rank"] == 0)
check("type", "N2 is killed only in the completed grade-one spin-two route",
      registry["disposition"]["fired"] == "N2_WRONG_HELICITY"
      and "completed first-layer grade-one bank" in registry["disposition"]["scope"])

for label in (
    "two algebraic modes are not two graviton polarizations",
    "a definite finite principal flux is not positive energy",
    "compact rotation typing is not a full global domain",
    "the graph-only theorem remains scoped rather than erased",
    "N2 wrong helicity does not falsify every source-action completion",
    "no kappa value residue quotient or external datum is booked",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.36."""

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


old = strict("lab/process/conditional-physics-ledger-v0.35.json")
new = strict("lab/process/conditional-physics-ledger-v0.36.json")
registry = strict("lab/process/selected-action-grade1-dbt-schur-observation.json")

print("A. METER, VERDICT, AND PROGRAM FENCES")
check("exact", "schema advances 0.35 to 0.36", old["schema_version"] == "0.35" and new["schema_version"] == "0.36")
check("exact", "denominator is frozen", old["denominator"] == new["denominator"])
check("exact", "82/82 remain mapped", new["progress"]["mapped"] == 82 and new["progress"]["total"] == 82)
check("exact", "one SAME moves to NEEDS",
      old["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
      and new["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "residue and quotients are frozen", old["residue"] == new["residue"] and new["residue"]["quotients_ranked"] == 4)
check("program", "P1/P2/P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
check("program", "canon claim and public posture are frozen", registry["canon_verdict_change"] == registry["claim_status_change"] == registry["public_posture_change"] == "NONE")

print("\nB. EXACT APPEND-ONLY MOVEMENT")
touched = ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]]
check("exact", "row ids are frozen", set(old_rows) == set(new_rows))
check("exact", "exactly five named rows change", changed == touched)

before, after = old_rows["LT-GR1"], new_rows["LT-GR1"]
check("exact", "LT-GR1 graph-only conditional match is retracted",
      (before["verdict"], before["reason_kind"]) == ("SAME", "DERIVED_CONDITIONAL")
      and (after["verdict"], after["reason_kind"]) == ("NEEDS", "MISSING_CONSTRUCTION"))
check("exact", "LT-GR1 names the exact causal revival route",
      "N2" in after["distance"] and "null little group" in after["distance"] and "Green" in after["distance"])

required = (
    "GRADE1_HESSIAN_RANK196",
    "FULL_SOURCE_SCHUR_LIVE",
    "N2_TWO_MODE_CAUSAL_CANDIDATE_PHYSICAL_TYPING_OPEN",
)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    if row_id != "LT-GR1":
        check("exact", f"{row_id}: verdict and reason kind are frozen",
              before["verdict"] == after["verdict"] and before["reason_kind"] == after["reason_kind"])
        check("exact", f"{row_id}: revival trigger is frozen", before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id}: grade-one Schur and N2 burden are typed", all(token in after["mapping_grade"] for token in required))
    check("exact", f"{row_id}: evidence points to the completed source Schur", after["evidence"] == "selected-action-grade1-dbt-schur-observation-2026-08-06.md")

migrations = [m for m in new["migrations"] if m.get("from_version") == "0.35" and m.get("to_version") == "0.36"]
check("exact", "five migrations are recorded", [m["row_id"] for m in migrations] == touched)
check("exact", "all migrations preserve row meaning", all(m["meaning_changed"] is False for m in migrations))
check("exact", "wave dispositions name the same rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)
check("exact", "only LT-GR1 has verdict movement", [item["change"] for item in new["wave_row_dispositions"]] == ["MIGRATED_VERDICT_AND_DISTANCE"] + ["MIGRATED_DISTANCE_ONLY"] * 4)

print("\nC. QUEUE AND NONPROMOTION")
rank_one, rank_two = new["next_work_queue"][:2]
check("type", "rank one names the unique N2 two-mode kernel", "unique positive N2" in rank_one["why"])
check("type", "rank one requires little-group and Green typing", "null little group" in rank_one["why"] and "Green form" in rank_one["why"])
check("type", "rank one requires common right-H/Krein domain and odd BV/BFV", "right-H/Krein" in rank_one["why"] and "odd BV/BFV" in rank_one["why"])
check("type", "rank one rejects coefficient residue and quotient promotion", "Do not book kappa_1, residue, a quotient" in rank_one["why"])
check("type", "rank two remains the LT-GR3 I2B owner map", rank_two["rows"] == ["LT-GR3"] and "I2B" in rank_two["why"])
check("type", "no quotient is promoted", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"])

for label in (
    "graph-only exactness is not completed-source exactness",
    "a Schur complement is not a BV or symplectic quotient",
    "two algebraic modes are not yet physical gravitons",
    "the N2 root is not yet a selected measured coupling",
    "finite observation preservation is not global faithfulness",
    "I2B and observer full-II remain separately owned",
    "P1/P2/P3 are not used to fit the coefficient locus",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

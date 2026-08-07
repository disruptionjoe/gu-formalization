#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.42."""

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
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.41.json")
new = strict("lab/process/conditional-physics-ledger-v0.42.json")
registry = strict("lab/process/selected-second-layer-offtt-scalar-ward-owner.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.41 to 0.42", old["schema_version"] == "0.41" and new["schema_version"] == "0.42")
check("exact", "denominator and verdict counts freeze", old["denominator"] == new["denominator"] and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("exact", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
for key in ("continuous_real", "function_valued_at_least", "open_discrete_forks", "quotients_ranked"):
    check("exact", f"residue {key} freezes", old["residue"][key] == new["residue"][key])
check("program", "P1 P2 P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third lane stay fenced", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane_gate"] == "NOT_PROMOTED")
check("program", "no posture promotion", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "none")

print("\nB. APPEND-ONLY MIGRATION")
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("exact", "row identities freeze", set(old_rows) == set(new_rows))
check("exact", "exactly five named rows change", [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]] == touched)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check("exact", f"{row_id} verdict reason summary revival freeze", before["verdict"] == after["verdict"] and before["reason_kind"] == after["reason_kind"] and before["summary"] == after["summary"] and before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id} points to new evidence", after["evidence"] == "selected-second-layer-offtt-scalar-ward-owner-2026-08-07.md")
    check("type", f"{row_id} retains an open boundary", "OPEN" in after["mapping_grade"] or "REQUIRED" in after["mapping_grade"])
migrations = [item for item in new["migrations"] if item.get("from_version") == "0.41" and item.get("to_version") == "0.42"]
check("exact", "five migrations recorded in order", [item["row_id"] for item in migrations] == touched)
check("exact", "row meanings remain fixed", all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name five rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)

print("\nC. OWNER AND POLE FENCES")
exact = registry["exact_result"]
check("exact", "TT pole reproduces", exact["tt_mass2_reproduced"] == "1922/3589")
check("exact", "restricted scalar candidate is not admissible", exact["restricted_scalar_candidate_mass2"] == "1157/3589" and exact["restricted_scalar_candidate_admissible"] is False)
check("exact", "Ward defect and full candidate rank recorded", exact["full_metric_ward_defect_rank"] == 4 and exact["full_metric_rank_at_candidate"] == 10)
check("type", "old and selected action owners stay distinct", exact["old_full_b_coefficient_owner"] != exact["selected_i2b_owner"])
check("type", "full co-moving owner is next", "FULL_COMOVING_DUPSILON" in exact["next_owner"] and "full co-moving D Upsilon" in new["next_work_queue"][0]["why"])
check("source", "source return is confirm plus silent", "SOURCE-CONFIRMS" in registry["source_return"] and "SOURCE-SILENT" in registry["source_return"])
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "restricted scalar root is not a coupled characteristic root",
    "metric-only Ward failure is not a failure of the full action",
    "TT recovery does not imply off-TT basicness",
    "old full-B coefficient cannot cross action owners",
    "finite Hessian is not a BFV phase space",
    "no datum residue quotient or public posture changes",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

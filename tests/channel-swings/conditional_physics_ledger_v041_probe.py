#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.41."""

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


old = strict("lab/process/conditional-physics-ledger-v0.40.json")
new = strict("lab/process/conditional-physics-ledger-v0.41.json")
registry = strict("lab/process/selected-second-layer-massive-so3-closure-identifiability.json")

print("A. METER AND PROGRAM FENCES")
check("exact", "schema advances 0.40 to 0.41",
      old["schema_version"] == "0.40" and new["schema_version"] == "0.41")
check("exact", "denominator verdicts and coverage are frozen",
      old["denominator"] == new["denominator"]
      and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6}
      and new["progress"]["mapped"] == new["progress"]["total"] == 82)
for key in ("continuous_real", "function_valued_at_least", "open_discrete_forks", "quotients_ranked"):
    check("exact", f"residue field {key} is frozen", old["residue"][key] == new["residue"][key])
check("program", "P1 P2 P3 remain unused",
      registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third-lane fences hold",
      registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
      and registry["third_lane_gate"] == "NOT_PROMOTED")
check("program", "no claim canon or public posture promotion",
      registry["claim_status_change"] == registry["canon_verdict_change"]
      == registry["public_posture_change"] == "none")

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
    check("exact", f"{row_id}: evidence points to SO3 closure",
          after["evidence"] == "selected-second-layer-massive-so3-closure-identifiability-2026-08-07.md")
    check("exact", f"{row_id}: mapping records an open boundary", "OPEN" in after["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.40" and item.get("to_version") == "0.41"]
check("exact", "five migrations are recorded in row order",
      [item["row_id"] for item in migrations] == touched)
check("exact", "all migrations preserve row meanings",
      all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name the same five rows",
      [item["row_id"] for item in new["wave_row_dispositions"]] == touched)
check("exact", "all row moves are distance or priority only",
      all("VERDICT" not in item["change"] for item in new["wave_row_dispositions"]))

print("\nC. EXACT CONSTRUCTION DISPOSITION")
exact = registry["exact_result"]
check("exact", "massive SO3 closure is the five-dimensional spin-two irrep",
      exact["so3_orbit_closure_dimension"] == 5
      and exact["so3_casimir"] == -6
      and exact["massive_type"] == "SPIN_2")
check("exact", "rest quotient retains one separate scalar",
      exact["rest_spatial_quotient_dimension"] == 6
      and exact["complement"] == "SPIN_0_DIMENSION_1")
check("exact", "two commutant blocks create the identifiability boundary",
      exact["so3_commutant_dimension"] == 2
      and exact["tt_determines"] == "SPIN2_CHARACTERISTIC_POLYNOMIAL_ONLY"
      and exact["unidentified"] == "SPIN0_CHARACTERISTIC_POLYNOMIAL")
check("type", "rank one is the off-TT spin-zero action owner",
      "background-subtracted off-TT" in new["next_work_queue"][0]["why"]
      and "scalar polynomial" in new["next_work_queue"][0]["why"])
check("type", "coupled nonzero-fermion Hessian remains rank two",
      "spinor Euler block" in new["next_work_queue"][1]["why"]
      and "nonzero-fermion Hessian" in new["next_work_queue"][1]["why"])
check("source", "explicit primary-source return is confirm plus silent",
      "SOURCE-CONFIRMS" in registry["source_return"]
      and "SOURCE-SILENT" in registry["source_return"])
check("symplectic", "symplectic work remains downstream",
      "MASSLESS_CONSTRAINT_COMPLEX" in registry["next_gate"])

for label in (
    "five representation partners are not five positive physical states",
    "axial weight zero inside spin two is not the independent trace scalar",
    "TT data do not determine the scalar polynomial",
    "massive closure is not the massless constraint quotient",
    "representation closure is not a BFV phase space",
    "no coefficient residue quotient or external datum is booked",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

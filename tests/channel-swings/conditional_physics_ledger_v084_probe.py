#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.84."""

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=pairs)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


current = strict(ROOT / "lab/process/conditional-physics-ledger-v0.84.json")
previous = strict(ROOT / "lab/process/conditional-physics-ledger-v0.83.json")
registry = strict(ROOT / "lab/process/selected-k77-gamma-soldered-epsilon-dupsilon-orbit.json")

check("schema", "ledger advances once", current["schema_version"] == "0.84")
check("schema", "predecessor is immutable v0.83",
      current["predecessor"].endswith("conditional-physics-ledger-v0.83.json"))
check("meter", "coverage remains 82 of 82",
      current["progress"]["mapped"] == current["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen",
      current["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen", current["residue"] == previous["residue"])
check("meter", "five scoped quotients remain", current["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is explicit",
      current["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 4,
                                    "conditions_opened": 0, "remaining_named_conditions": 2})
check("source", "source return confirms carriers while preserving soldering silence",
      "EPSILON_GAMMA_FRAME" in current["source_return"]
      and "SOURCE-SILENT" in current["source_return"])

old_rows = {row["id"]: row for row in previous["rows"]}
new_rows = {row["id"]: row for row in current["rows"]}
changed = {row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
check("rows", "exactly five named rows migrate", changed == expected)

for row_id in sorted(expected):
    old = old_rows[row_id]
    new = new_rows[row_id]
    check("rows", f"{row_id} verdict remains frozen", new["verdict"] == old["verdict"])
    check("rows", f"{row_id} reason kind remains frozen", new["reason_kind"] == old["reason_kind"])
    check("rows", f"{row_id} points to v0.84 evidence",
          new["evidence"] == "selected-k77-gamma-soldered-epsilon-dupsilon-orbit-2026-08-08.md")
    check("rows", f"{row_id} retains the exact source-varpi predecessor",
          "VARPI" in new["mapping_grade"] and "DUPSILON" in new["mapping_grade"])
    check("rows", f"{row_id} records the gamma-epsilon successor",
          "GAMMA_EPSILON" in new["mapping_grade"])

migrations = [m for m in current["migrations"] if m["from_version"] == "0.83"
              and m["to_version"] == "0.84"]
check("migration", "five append-only migration edges exist",
      {m["row_id"] for m in migrations} == expected and len(migrations) == 5)
objects = set(current["layer0_objects_compared"])
check("layer0", "source epsilon and dependent gamma frame remain distinct",
      {"SOURCE_EPSILON_H_VALUED_FIELD", "DEPENDENT_GLOBAL_GAMMA_EPSILON_FRAME"} <= objects)
check("layer0", "Kosmann and gamma-soldered tangents remain distinct",
      {"KOSMANN_GRADE2_COMPENSATOR", "GAMMA_EPSILON_GRADE1_SOLDERED_TANGENT"} <= objects)
check("layer0", "principal epsilon orbit and full physical identity remain distinct",
      {"PRINCIPAL_INTERNAL_GAUGE_ORBIT_DEPSILON_UPSILON",
       "FULL_PHYSICAL_DIFFEO_SOLDERING_IDENTITY"} <= objects)
check("queue", "rank one names transverse metric full Frechet and Green owners",
      "six transverse physical" in current["next_work_queue"][0]["why"]
      and "full Frechet J-R identity" in current["next_work_queue"][0]["why"]
      and "Green concomitant" in current["next_work_queue"][0]["why"])

check("theorem", "all causal Kosmann compensators remain rank three",
      {value["kosmann_rank"] for value in registry["causal_orbits"].values()} == {3})
check("theorem", "all causal gamma-epsilon residual blocks have rank four",
      {value["gamma_residual_rank"] for value in registry["causal_orbits"].values()} == {4})
check("theorem", "all common-field principal orbit responses have rank four",
      {value["combined_orbit_rank"] for value in registry["causal_orbits"].values()} == {4})
check("surplus", "gamma construction adds no field coefficient or datum",
      registry["constraint_surplus"]["new_fields"] == 0
      and registry["constraint_surplus"]["new_continuous_coefficients"] == 0
      and registry["constraint_surplus"]["new_discrete_datum"] == 0)
check("scope", "old metric diagnostic is revived only for recheck",
      registry["old_metric_diagnostic"]["disposition"] == "REVIVED_FOR_RECHECK__NOT_PROMOTED")
check("krein", "pairing adjoint Green and Gram remain open",
      set(registry["held_open"].values()) == {"OPEN", "OPEN__SIX_TRANSVERSE_COLUMNS"})
check("scope", "P1 P2 P3 remain unused and no quotient moves",
      registry["constraint_fence"] == {"P1_P2_P3": "UNUSED", "new_scoped_quotients": 0})
check("scope", "Curt and third-lane fences remain",
      registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
      and registry["third_lane"] == "NOT_PROMOTED")
check("scope", "canon claim and public posture do not move",
      registry["claim_status_change"] == registry["canon_verdict_change"]
      == registry["public_posture_change"] == "NONE")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

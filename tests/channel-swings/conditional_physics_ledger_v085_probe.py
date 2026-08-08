#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.85."""

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


current = strict(ROOT / "lab/process/conditional-physics-ledger-v0.85.json")
previous = strict(ROOT / "lab/process/conditional-physics-ledger-v0.84.json")
registry = strict(ROOT / "lab/process/selected-k77-metric-transverse-augmented-torsion-block.json")

check("schema", "ledger advances once", current["schema_version"] == "0.85")
check("schema", "predecessor is immutable v0.84",
      current["predecessor"].endswith("conditional-physics-ledger-v0.84.json"))
check("meter", "coverage remains 82 of 82",
      current["progress"]["mapped"] == current["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen",
      current["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen", current["residue"] == previous["residue"])
check("meter", "five scoped quotients remain", current["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is explicit",
      current["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                    "conditions_opened": 0, "remaining_named_conditions": 2})
check("source", "source return confirms augmented torsion while preserving operator silence",
      "T_EQUALS_VARPI_MINUS_ROTATED_BLC" in current["source_return"]
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
    check("rows", f"{row_id} points to v0.85 evidence",
          new["evidence"] == "selected-k77-metric-transverse-augmented-torsion-block-2026-08-08.md")
    check("rows", f"{row_id} retains the gamma-epsilon predecessor",
          "GAMMA_EPSILON" in new["mapping_grade"])
    check("rows", f"{row_id} records the transverse torsion successor",
          "TRANSVERSE" in new["mapping_grade"] and "TORSION" in new["mapping_grade"])

migrations = [m for m in current["migrations"] if m["from_version"] == "0.84"
              and m["to_version"] == "0.85"]
check("migration", "five append-only migration edges exist",
      {m["row_id"] for m in migrations} == expected and len(migrations) == 5)
objects = set(current["layer0_objects_compared"])
check("layer0", "metric value and first jet remain distinct",
      {"TEN_METRIC_VALUE_DIRECTIONS_SYM2_TSTAR_X", "METRIC_FIRST_JET_Q_TENSOR_H"} <= objects)
check("layer0", "orbit and transverse metric directions remain distinct",
      {"RANK4_METRIC_DIFFEO_ORBIT_IM_DQ", "RANK6_TRANSVERSE_METRIC_PROJECTOR"} <= objects)
check("layer0", "direct torsion and complete moving operator remain distinct",
      {"DIRECT_PRINCIPAL_AUGMENTED_TORSION_RESIDUAL_BLOCK",
       "MOVING_SHIAB_HODGE_CURVATURE_DENSITY_OBSERVATION_OPERATOR_PACKET"} <= objects)
check("queue", "rank one names operator packet full Ward and Green owners",
      "rank-four moving Shiab/Hodge" in current["next_work_queue"][0]["why"]
      and "full Frechet J-R zero" in current["next_work_queue"][0]["why"]
      and "Green concomitant" in current["next_work_queue"][0]["why"])

check("theorem", "all causal Levi-Civita symbols have rank nine",
      {value["levi_civita_rank"] for value in registry["causal_blocks"].values()} == {9})
check("theorem", "all causal transverse torsion residual blocks have rank six",
      {value["transverse_torsion_residual_rank"] for value in registry["causal_blocks"].values()} == {6})
check("theorem", "all causal partial Ward defects have rank four",
      {value["partial_ward_defect_rank"] for value in registry["causal_blocks"].values()} == {4})
check("surplus", "transverse block adds no field coefficient or datum",
      registry["constraint_surplus"]["new_fields"] == 0
      and registry["constraint_surplus"]["new_continuous_coefficients"] == 0
      and registry["constraint_surplus"]["new_discrete_datum"] == 0)
check("scope", "moving operator pairing adjoint Green and Gram remain open",
      registry["held_open"]["moving_shiab_hodge_curvature_density_observation_orbit_packet"].startswith("OPEN")
      and registry["held_open"]["residual_K_star"] == "OPEN"
      and registry["held_open"]["green_concomitant"] == "OPEN")
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

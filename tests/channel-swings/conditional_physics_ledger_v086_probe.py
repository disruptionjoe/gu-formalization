#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.86."""

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
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


current = strict(ROOT / "lab/process/conditional-physics-ledger-v0.86.json")
previous = strict(ROOT / "lab/process/conditional-physics-ledger-v0.85.json")
registry = strict(ROOT / "lab/process/selected-k77-principal-ward-gamma-epsilon-reconciliation.json")

check("schema", "ledger advances once", current["schema_version"] == "0.86")
check("schema", "predecessor is immutable v0.85",
      current["predecessor"].endswith("conditional-physics-ledger-v0.85.json"))
check("meter", "coverage remains 82 of 82",
      current["progress"]["mapped"] == current["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen",
      current["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen", current["residue"] == previous["residue"])
check("meter", "five scoped quotients remain", current["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is explicit",
      current["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                    "conditions_opened": 0, "remaining_named_conditions": 2})
check("source", "decisive source return is SOURCE-CORRECTS",
      current["source_return"] == registry["source_return"] == "SOURCE-CORRECTS")

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
    check("rows", f"{row_id} points to v0.86 evidence",
          new["evidence"] == "selected-k77-principal-ward-gamma-epsilon-reconciliation-2026-08-08.md")
    check("rows", f"{row_id} carries the v0.86 rank-three/gamma-conditional mapping grade",
          "RANK3" in new["mapping_grade"] and "GAMMA" in new["mapping_grade"])
    check("rows", f"{row_id} distance no longer demands a sourced rank-four packet",
          "source-minimal rank-three" in new["distance"])

migrations = [m for m in current["migrations"] if m["from_version"] == "0.85"
              and m["to_version"] == "0.86"]
check("migration", "five append-only migration edges exist",
      {m["row_id"] for m in migrations} == expected and len(migrations) == 5)
objects = set(current["layer0_objects_compared"])
check("layer0", "source epsilon and conditional gamma lift remain distinct",
      {"SOURCE_EPSILON_H_GAUGE_VARIABLE", "CONDITIONAL_GAMMA_EPSILON_GRADE1_LIFT"} <= objects)
check("layer0", "direct torsion and full raw residual remain distinct",
      "DIRECT_TORSION_RESPONSE_VERSUS_FULL_RAW_UPSILON_RESPONSE" in objects)
check("layer0", "rank-three source and rank-four conditional packets remain distinct",
      {"RANK3_SOURCE_CURVATURE_PACKET", "RANK4_CONDITIONAL_GAMMA_EXTENDED_PACKET"} <= objects)
check("queue", "rank one names corrected source packet full Ward and Green owners",
      "rank-three moving Shiab/Hodge" in current["next_work_queue"][0]["why"]
      and "full Frechet J-R zero" in current["next_work_queue"][0]["why"]
      and "Green concomitant" in current["next_work_queue"][0]["why"])

check("theorem", "all sourced principal packets have rank three",
      {value["source_variable_curvature_packet_rank"]
       for value in registry["causal_reconciliations"].values()} == {3})
check("theorem", "all conditional gamma extensions have rank four",
      {value["conditional_gamma_extended_packet_rank"]
       for value in registry["causal_reconciliations"].values()} == {4})
check("theorem", "all direct torsion orbits cancel",
      {value["direct_torsion_cancellation_rank"]
       for value in registry["causal_reconciliations"].values()} == {0})
check("theorem", "all gamma extensions are nonzero on the sourced kernel",
      all(value["conditional_gamma_kernel_response_nonzero"]
          and value["source_longitudinal_response_zero"]
          for value in registry["causal_reconciliations"].values()))
check("scope", "moving operator is narrowed rather than eliminated",
      registry["reconciliation"]["moving_operator"] == "NARROWED_FROM_RANK4_TO_RANK3__NOT_ELIMINATED")
check("scope", "gamma construction remains live but conditional",
      registry["reconciliation"]["gamma_epsilon"].startswith("PRESERVED_AS_INTERNAL_GAUGE"))
check("scope", "full Frechet and symplectic reductions remain open",
      registry["full_frechet_ward"] == registry["reduced_symplectic_class"] == "OPEN")
check("scope", "P1 P2 P3 remain unused",
      set(registry["external_datum"].values()) == {"UNUSED"})
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

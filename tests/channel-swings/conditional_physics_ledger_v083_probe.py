#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.83."""

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


current = strict(ROOT / "lab/process/conditional-physics-ledger-v0.83.json")
previous = strict(ROOT / "lab/process/conditional-physics-ledger-v0.82.json")
registry = strict(ROOT / "lab/process/selected-k77-common-field-dupsilon-varpi-block.json")

check("schema", "ledger advances once", current["schema_version"] == "0.83")
check("schema", "predecessor is immutable v0.82",
      current["predecessor"].endswith("conditional-physics-ledger-v0.82.json"))
check("meter", "coverage remains 82 of 82",
      current["progress"]["mapped"] == current["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen",
      current["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen", current["residue"] == previous["residue"])
check("meter", "five scoped quotients remain", current["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is explicit",
      current["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                    "conditions_opened": 0, "remaining_named_conditions": 2})
check("source", "source return confirms varpi and epsilon while preserving silence",
      "VARPI_DIRECTION_AND_EPSILON_FIELD" in current["source_return"]
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
    check("rows", f"{row_id} points to v0.83 evidence",
          new["evidence"] == "selected-k77-common-field-dupsilon-varpi-block-2026-08-08.md")
    check("rows", f"{row_id} retains the stationary first-derivative reduction",
          "STATIONARY_H2_FIRST_DERIVATIVE_REDUCTION" in new["mapping_grade"])
    check("rows", f"{row_id} records the exact varpi block",
          "VARPI" in new["mapping_grade"] and "DUPSILON" in new["mapping_grade"])

migrations = [m for m in current["migrations"] if m["from_version"] == "0.82"
              and m["to_version"] == "0.83"]
check("migration", "five append-only migration edges exist",
      {m["row_id"] for m in migrations} == expected and len(migrations) == 5)
objects = set(current["layer0_objects_compared"])
check("layer0", "D-omega and D-epsilon Upsilon remain distinct",
      {"SOURCE_D_OMEGA_UPSILON_EXTERIOR_PROLONGATION",
       "SOURCE_D_EPSILON_UPSILON_FRECHET_BLOCK"} <= objects)
check("layer0", "fixed-epsilon horn and rank-four import are explicit",
      {"FIXED_EPSILON_G_VARPI_COMMON_FIELD_HORN",
       "OLD_RANK4_METRIC_DIAGNOSTIC_IMPORT"} <= objects)
check("queue", "rank one names physical metric epsilon J-R and Green owners",
      "source-epsilon Frechet block" in current["next_work_queue"][0]["why"]
      and "J-R identity" in current["next_work_queue"][0]["why"]
      and "Green concomitant" in current["next_work_queue"][0]["why"])

check("theorem", "registry records exact horizontal varpi response",
      registry["varpi_block"]["domain_dimension"] == registry["varpi_block"]["rank"] == 24
      and registry["varpi_block"]["output_support"] == 56)
check("theorem", "all causal varpi residual orbits have rank three",
      {value["residual_rank"] for value in registry["causal_orbits"].values()} == {3})
check("theorem", "fixed-epsilon rank-four metric import is rejected",
      registry["fixed_epsilon_fork"]["old_metric_ward_load_rank"] == 4
      and registry["fixed_epsilon_fork"]["fixed_epsilon_common_field_gram_metric_load_rank_upper_bound"] == 3
      and registry["fixed_epsilon_fork"]["old_metric_diagnostic_import"].startswith("REJECTED"))
check("scope", "source epsilon remains an open revival rather than a fit",
      registry["fixed_epsilon_fork"]["source_epsilon_revival"].startswith("OPEN"))
check("krein", "residual pairing and physical Gram operator remain open",
      registry["residual_pairing"]["K_star"] == "OPEN"
      and registry["residual_pairing"]["stationary_gram_hessian"] == "OPEN")
check("scope", "no constraint-accounting movement",
      registry["constraint_fence"]["new_scoped_quotients"] == 0
      and registry["constraint_fence"]["new_external_datum"] == 0)
check("scope", "P1 P2 P3 remain unused",
      registry["constraint_fence"]["P1_P2_P3"] == "UNUSED")
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

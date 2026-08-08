#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.82."""

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


current = strict(ROOT / "lab/process/conditional-physics-ledger-v0.82.json")
previous = strict(ROOT / "lab/process/conditional-physics-ledger-v0.81.json")
registry = strict(ROOT / "lab/process/selected-k77-stationary-two-layer-hessian-factorization.json")

check("schema", "ledger advances once", current["schema_version"] == "0.82")
check("schema", "predecessor is immutable v0.81",
      current["predecessor"].endswith("conditional-physics-ledger-v0.81.json"))
check("meter", "coverage remains 82 of 82",
      current["progress"]["mapped"] == current["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen",
      current["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen", current["residue"] == previous["residue"])
check("meter", "five scoped quotients remain", current["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is explicit",
      current["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 4,
                                    "conditions_opened": 0, "remaining_named_conditions": 3})
check("source", "source return confirms residual norm square and preserves silence",
      "RESIDUAL_NORM_SQUARE" in current["source_return"]
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
    check("rows", f"{row_id} points to v0.82 evidence",
          new["evidence"] == "selected-k77-stationary-two-layer-hessian-factorization-2026-08-08.md")
    check("rows", f"{row_id} preserves the full coupled Hessian burden",
          "FULL_COUPLED_TWO_LAYER_HESSIAN_REQUIRED" in new["mapping_grade"])
    check("rows", f"{row_id} records the stationary first-derivative reduction",
          "STATIONARY_H2_FIRST_DERIVATIVE_REDUCTION" in new["mapping_grade"])
    check("rows", f"{row_id} names common-field D Upsilon and K as open",
          "COMMON_FIELD_DUPSILON_K_OPEN" in new["mapping_grade"])

migrations = [m for m in current["migrations"] if m["from_version"] == "0.81"
              and m["to_version"] == "0.82"]
check("migration", "five append-only migration edges exist",
      {m["row_id"] for m in migrations} == expected and len(migrations) == 5)
objects = set(current["layer0_objects_compared"])
check("layer0", "first Hessian, raw Jacobian and second Hessian remain distinct",
      {"FIRST_LAYER_34_VARIABLE_WARD_BASIC_SCHUR_SYMBOL",
       "RAW_COMMON_FIELD_DUPSILON_JACOBIAN",
       "SECOND_LAYER_STATIONARY_GRAM_HESSIAN"} <= objects)
check("layer0", "physical operator movement and dependent observation are explicit",
      {"INDEPENDENT_PHYSICAL_DSHIAB_FA_STAR_AND_DHODGE_T_STAR",
       "DEPENDENT_OBSERVATION_RECEIVER_CHAIN_RULE"} <= objects)
check("analytic", "complex contour and path-integral measure remain separate",
      "COMPLEX_CONTOUR_AND_PATH_INTEGRAL_MEASURE" in objects)
check("queue", "rank one names D Upsilon, K and Ward",
      "D-Upsilon block matrix" in current["next_work_queue"][0]["why"]
      and "J-R equals zero" in current["next_work_queue"][0]["why"])

check("theorem", "registry records exact stationary factorization",
      registry["result"] == "AT_UPSILON_ZERO__H2_EQUALS_DUPSILON_ADJOINT_K_DUPSILON")
check("theorem", "registry preserves physical operator movement",
      "PHYSICAL_DSHIAB_ON_FA_STAR" in registry["stationary_factorization"]["retained"]
      and "PHYSICAL_DHODGE_ON_KAPPA_T_STAR" in registry["stationary_factorization"]["retained"])
check("krein", "registry refuses a physical kernel or energy conclusion",
      registry["krein_control"]["injective_J_can_have_null_gram_form"] is True
      and registry["krein_control"]["physical_kernel_or_energy_derived"] is False)
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

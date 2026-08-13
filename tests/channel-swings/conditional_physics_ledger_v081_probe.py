#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.81."""

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


current = strict(ROOT / "lab/process/conditional-physics-ledger-v0.81.json")
previous = strict(ROOT / "lab/process/conditional-physics-ledger-v0.80.json")
registry = strict(ROOT / "lab/process/selected-k77-coupled-euler-complex-scope.json")

check("schema", "ledger advances once", current["schema_version"] == "0.81")
check("schema", "predecessor is immutable v0.80",
      current["predecessor"].endswith("conditional-physics-ledger-v0.80.json"))
check("meter", "coverage remains 82 of 82",
      current["progress"]["mapped"] == current["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen",
      current["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen", current["residue"] == previous["residue"])
check("meter", "five scoped quotients remain", current["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is explicit",
      current["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 4,
                                    "conditions_opened": 1, "remaining_named_conditions": 3})
check("source", "source return confirms two layers and preserves silence",
      "TWO_LAYER_FULL_VARIABLE_ACTION_GRAMMAR" in current["source_return"]
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
    check("rows", f"{row_id} points to v0.81 evidence",
          new["evidence"] == "selected-k77-coupled-euler-complex-scope-2026-08-08.md")
    check("rows", f"{row_id} retains the ten metric equations",
          "TEN_METRIC_SECTION_EQUATIONS_RETAINED" in new["mapping_grade"])
    check("rows", f"{row_id} records vertical-only mistyping",
          "VERTICAL_ONLY_COMPLEX_MISTYPED" in new["mapping_grade"])
    check("rows", f"{row_id} records first-layer generic cohomology zero",
          "FIRST_LAYER_COUPLED_WARD_EXACT_GENERIC_COHOMOLOGY0" in new["mapping_grade"])
    check("rows", f"{row_id} records second-layer Ward defect",
          "SECOND_LAYER_FULL_METRIC_WARD_DEFECT4" in new["mapping_grade"])
    check("rows", f"{row_id} names the coupled two-layer owner",
          "FULL_COUPLED_TWO_LAYER_HESSIAN_REQUIRED" in new["mapping_grade"])

migrations = [m for m in current["migrations"] if m["from_version"] == "0.80"
              and m["to_version"] == "0.81"]
check("migration", "five append-only migration edges exist",
      {m["row_id"] for m in migrations} == expected and len(migrations) == 5)
check("layer0", "retained coordinates and closed subsystem are distinct",
      {"RETAINED_TEN_METRIC_EULER_COORDINATES", "CLOSED_TEN_VARIABLE_ACTION_SUBSYSTEM"}
      <= set(current["layer0_objects_compared"]))
check("layer0", "first and second action blocks are distinct",
      {"FIRST_LAYER_34_VARIABLE_WARD_BASIC_SCHUR_SYMBOL",
       "SECOND_LAYER_TEN_BY_TEN_METRIC_DIAGNOSTIC"}
      <= set(current["layer0_objects_compared"]))
check("layer0", "formal and action-derived completions are distinct",
      {"FORMAL_21_PARAMETER_WARD_COMPLETION", "ACTION_DERIVED_COUPLED_WARD_COMPLETION"}
      <= set(current["layer0_objects_compared"]))
check("analytic", "symbol cohomology and hyperbolicity/domain are distinct",
      {"PRINCIPAL_SYMBOL_COHOMOLOGY", "STRONG_HYPERBOLICITY_AND_COMMON_GREEN_KREIN_DOMAIN"}
      <= set(current["layer0_objects_compared"]))
check("queue", "rank one names the full selected two-layer Hessian",
      "both selected action layers" in current["next_work_queue"][0]["why"]
      and "common field/jet" in current["next_work_queue"][0]["why"])

check("exact", "registry records generic first-layer cohomology zero",
      set(registry["first_layer"]["generic_physical_symbol_cohomology"].values()) == {0})
check("representation", "registry records exceptional helicity one versus target two",
      registry["first_layer"]["exceptional_N2"]["helicity_absolute_value"] == 1
      and registry["first_layer"]["exceptional_N2"]["einstein_target_polynomial"] == "x^2+4")
check("exact", "registry records second-layer Ward defect four",
      registry["second_layer_metric_block"]["ward_defect_rank"] == 4)
check("exact", "registry records naive sum defect four",
      registry["composition"]["naive_first_plus_metric_second_ward_defect_rank"] == 4)
check("surplus", "registry rejects the 21-dimensional formal fit",
      registry["composition"]["formal_symmetric_completion"]["affine_solution_dimension"] == 21
      and registry["composition"]["formal_symmetric_completion"]["disposition"]
      == "UNINFORMATIVE_WITHOUT_ACTION_SELECTION")
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

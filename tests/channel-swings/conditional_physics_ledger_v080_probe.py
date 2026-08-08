#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.80."""

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


current = strict(ROOT / "lab/process/conditional-physics-ledger-v0.80.json")
previous = strict(ROOT / "lab/process/conditional-physics-ledger-v0.79.json")
registry = strict(ROOT / "lab/process/selected-k77-metric-section-bianchi-typing.json")

check("schema", "ledger advances once", current["schema_version"] == "0.80")
check("schema", "predecessor is immutable v0.79",
      current["predecessor"].endswith("conditional-physics-ledger-v0.79.json"))
check("meter", "coverage remains 82 of 82",
      current["progress"]["mapped"] == current["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen",
      current["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen",
      current["residue"] == previous["residue"])
check("meter", "five scoped quotients remain", current["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta remains explicit",
      current["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                    "conditions_opened": 1, "remaining_named_conditions": 2})
check("source", "source return confirms target and preserves silence",
      "METRIC_SECTION_RANK10" in current["source_return"]
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
    check("rows", f"{row_id} points to v0.80 evidence",
          new["evidence"] == "selected-k77-metric-section-bianchi-typing-2026-08-08.md")
    check("rows", f"{row_id} retains the v0.79 faithfulness fence",
          "ORDINARY_PULLBACK_ACTION_FAITHFULNESS_KILLED" in new["mapping_grade"])
    check("rows", f"{row_id} retains the ten metric equations",
          "TEN_METRIC_SECTION_EQUATIONS_RETAINED" in new["mapping_grade"])
    check("rows", f"{row_id} rejects full-conormal BV erasure",
          "FULL_CONORMAL_BV_ERASURE_REJECTED" in new["mapping_grade"])
    check("rows", f"{row_id} records the exact Einstein comparator",
          "EINSTEIN_COMPARATOR_NONCHAR_EXACT_NULL_HELICITY2" in new["mapping_grade"])
    check("rows", f"{row_id} keeps the selected K77 Euler complex open",
          "SELECTED_K77_EULER_WARD_COMPLEX_OPEN" in new["mapping_grade"])

migrations = [m for m in current["migrations"] if m["from_version"] == "0.79"
              and m["to_version"] == "0.80"]
check("migration", "five append-only migration edges exist",
      {m["row_id"] for m in migrations} == expected and len(migrations) == 5)
check("layer0", "base and metric-section variations are separate",
      {"BASE_GRAPH_REPARAMETRIZATION_DELTA_X",
       "INDEPENDENT_METRIC_SECTION_VARIATION_DELTA_G"}
      <= set(current["layer0_objects_compared"]))
check("layer0", "field gauge and equation identity are separate",
      {"RANK_FOUR_DIFFEO_FIELD_SYMBOL_D_K", "RANK_FOUR_BIANCHI_EQUATION_SYMBOL_W_K"}
      <= set(current["layer0_objects_compared"]))
check("layer0", "Einstein comparator and selected K77 operator are separate",
      {"STANDARD_LINEARIZED_EINSTEIN_COMPARATOR_G_K", "SELECTED_K77_VERTICAL_EULER_OPERATOR"}
      <= set(current["layer0_objects_compared"]))
check("queue", "rank one names the selected K77 Euler Ward comparison",
      "selected K77 ten-dimensional vertical Euler" in current["next_work_queue"][0]["why"])

check("exact", "registry retypes conormal as metric equations",
      registry["complete_receiver"]["conormal_retyped_as_metric_equations"] is True)
check("exact", "registry preserves ten metric equations",
      registry["construction_disposition"]["retain_metric_equations"] is True)
check("exact", "registry records noncharacteristic exactness",
      registry["einstein_comparator"]["noncharacteristic_exact"] is True)
check("exact", "registry records two null cohomology dimensions",
      registry["einstein_comparator"]["null_field_cohomology_dimension"] == 2
      and registry["einstein_comparator"]["null_equation_cohomology_dimension"] == 2)
check("exact", "selected K77 operator remains unidentified",
      registry["einstein_comparator"]["selected_k77_operator_identified"] is False)
check("scope", "no constraint-accounting movement",
      registry["constraint_fence"]["new_scoped_quotients"] == 0
      and registry["constraint_fence"]["new_external_datum"] == 0)
check("scope", "P1 P2 P3 remain unused",
      registry["constraint_fence"]["P1_P2_P3"] == "UNUSED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.68."""

from collections import Counter
import json
from pathlib import Path


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


old = strict("lab/process/conditional-physics-ledger-v0.67.json")
new = strict("lab/process/conditional-physics-ledger-v0.68.json")
registry = strict("lab/process/selected-k77-green-potential-splitting-basicness.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.67" and new["schema_version"] == "0.68")
check("schema", "predecessor points to v0.67", new["predecessor"].endswith("v0.67.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen", new["residue"] == old["residue"])
check("frontier", "two conditions close", new["frontier_delta"]["conditions_closed"] == 2)
check("frontier", "one contact condition opens", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check("source", "source return separates silence from repo-derived cotangent basicness",
      "SOURCE-SILENT" in new["source_return"] and "REPO-DERIVES" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.68 evidence", new_rows[rid]["evidence"] == "selected-k77-green-potential-splitting-basicness-2026-08-08.md")
    check("rows", f"{rid} records point-splitting basicness", "POINT_SPLITTING_BASIC" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.67" and item.get("to_version") == "0.68"]
check("migration", "five append-only migration edges exist",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "complete Green one-form transport is exact",
      registry["exact_result"]["complete_green_oneform_transport"] == "EXACT")
check("registry", "presymplectic two-form transport is exact",
      registry["exact_result"]["presymplectic_twoform_transport"] == "EXACT")
check("registry", "all ten K77 normal momentum shifts are live",
      registry["exact_result"]["k77_live_normal_momentum_shifts"] == 10)
check("registry", "partial field-sector defect remains live",
      registry["exact_result"]["partial_field_sector_defect"] == "NONZERO")
check("registry", "vertical lift is not required only for point descent",
      registry["construction_disposition"]["vertical_B_T_lift_for_point_trivialization_descent"] == "NOT_REQUIRED")
check("queue", "rank one is selected-action contact and gauge-basicness assembly",
      "contact terms" in new["next_work_queue"][0]["why"]
      and "physical gauge" in new["next_work_queue"][0]["why"])
check("scope", "contact transformations remain open",
      registry["construction_disposition"]["derivative_dependent_B_LC_soldering_observation_contact_terms"] == "OPEN")
check("scope", "physical gauge basicness remains open",
      registry["construction_disposition"]["physical_gauge_contraction_and_lie_derivative_basicness"] == "OPEN")
check("scope", "no new free object is introduced", registry["external_datum"]["free_object_delta"] == 0)
check("scope", "P1 P2 P3 remain unused", set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"})
check("scope", "no quotient is added", new["residue"]["quotients_ranked"] == 4)
check("scope", "no third lane is promoted", "THIRD_LANE" not in new["status"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.73."""

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


old = strict("lab/process/conditional-physics-ledger-v0.72.json")
new = strict("lab/process/conditional-physics-ledger-v0.73.json")
registry = strict("lab/process/selected-k77-two-endpoint-edge-dressing.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.72" and new["schema_version"] == "0.73")
check("schema", "predecessor points to v0.72", new["predecessor"].endswith("v0.72.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "continuous function and fork residue remain frozen",
      new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84
      and new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "scoped quotient count remains five",
      old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"] == 5)
check("frontier", "two conditions close", new["frontier_delta"]["conditions_closed"] == 2)
check("frontier", "one continuum-owner condition opens", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check("frontier", "headline remains unchanged", new["frontier_delta"]["headline_delta"] == "NONE")
check("source", "source return separates confirmation from silence",
      "SOURCE-CONFIRMS" in new["source_return"] and "SOURCE-SILENT" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.73 evidence",
          new_rows[rid]["evidence"] == "selected-k77-two-endpoint-edge-dressing-2026-08-08.md")
    check("rows", f"{rid} records exact K77 P_H owner", "K77_P_H_OWNER_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records exact two-endpoint kernel equality",
          "TWO_ENDPOINT_COTANGENT_KERNEL_EQUALS_GAUGE_ORBIT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records the holonomy compression fence",
          "DIM20" in new_rows[rid]["mapping_grade"] or "40_TO_20" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.72" and item.get("to_version") == "0.73"]
check("migration", "five append-only migration edges exist",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "dressed map and pulled-back form have rank eight",
      registry["exact_result"]["dressed_map_rank"] == 8
      and registry["exact_result"]["pulled_back_twoform_rank"] == 8)
check("registry", "kernel equals the rank-eight endpoint gauge orbit",
      registry["exact_result"]["characteristic_kernel_dimension"] == 8
      and registry["exact_result"]["source_target_gauge_orbit_rank"] == 8
      and registry["exact_result"]["kernel_equals_gauge_orbit"] is True)
check("registry", "single holonomy retains only 20 of the v0.70 rank 40",
      registry["exact_result"]["v070_ten_normal_dimension_rank"] == "40_40"
      and registry["exact_result"]["single_holonomy_ten_normal_dimension_rank"] == "20_20"
      and registry["exact_result"]["full_v070_recovery"] is False)
check("registry", "K77 owner is exact without K95 import",
      registry["construction_disposition"]["k77_principal_group_owner"].startswith("EXACT")
      and registry["layer0"]["k95_sp32_32_h"].startswith("INCOMPATIBLE"))
check("queue", "rank one requires two continuum endpoint action owners",
      "two continuum endpoint evaluation maps" in new["next_work_queue"][0]["why"]
      and "without compressing" in new["next_work_queue"][0]["why"])
check("scope", "no new quotient or selected boundary field is introduced",
      registry["constraint_accounting"]["new_scoped_quotients"] == 0
      and registry["constraint_accounting"]["new_boundary_fields_selected"] == 0)
check("scope", "continuum endpoint and epsilon owners remain open",
      registry["construction_disposition"]["two_continuum_endpoint_evaluation_map"] == "OPEN"
      and registry["construction_disposition"]["primitive_epsilon_preboundary_owner"] == "OPEN")
check("scope", "P1 P2 P3 remain unused",
      set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"})
check("scope", "no third lane is promoted", registry["program_fences"]["third_lane"] == "NOT_PROMOTED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

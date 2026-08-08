#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.74."""

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


old = strict("lab/process/conditional-physics-ledger-v0.73.json")
new = strict("lab/process/conditional-physics-ledger-v0.74.json")
registry = strict("lab/process/selected-k77-epsilon-endpoint-direct-sum.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.73" and new["schema_version"] == "0.74")
check("schema", "predecessor points to v0.73", new["predecessor"].endswith("v0.73.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "continuous function and fork residue remain frozen",
      new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84
      and new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "scoped quotient count remains five",
      old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"] == 5)
check("frontier", "two conditions close", new["frontier_delta"]["conditions_closed"] == 2)
check("frontier", "the action weld opens as the narrowed condition", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check("frontier", "headline remains unchanged", new["frontier_delta"]["headline_delta"] == "NONE")
check("source", "source return separates confirmation silence and repo derivation",
      all(marker in new["source_return"] for marker in ("SOURCE-CONFIRMS", "SOURCE-SILENT", "REPO-DERIVES")))

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.74 evidence",
          new_rows[rid]["evidence"] == "selected-k77-epsilon-endpoint-direct-sum-2026-08-08.md")
    check("rows", f"{rid} records the exact endpoint trace", "EPSILON_ENDPOINT_TRACE_RANK2" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records full direct-sum forty recovery", "DIRECT_SUM" in new_rows[rid]["mapping_grade"] and "FULL40" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} keeps the action momentum weld open", "ACTION_MOMENTUM" in new_rows[rid]["mapping_grade"] and "OPEN" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.73" and item.get("to_version") == "0.74"]
check("migration", "five append-only migration edges exist",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "local endpoint trace has rank two", registry["exact_result"]["local_collar_endpoint_trace_rank"] == 2)
check("registry", "matrix direct sum has rank sixteen and exact gauge kernel",
      registry["exact_result"]["matrix_direct_sum_twoform_rank"] == 16
      and registry["exact_result"]["matrix_direct_sum_kernel_dimension"] == 8
      and registry["exact_result"]["matrix_direct_sum_endpoint_gauge_rank"] == 8
      and registry["exact_result"]["matrix_direct_sum_kernel_equals_gauge_orbit"] is True)
check("registry", "all-ten direct sum recovers full forty quotient",
      registry["exact_result"]["all_ten_extended_dimension"] == 60
      and registry["exact_result"]["all_ten_twoform_rank"] == 40
      and registry["exact_result"]["all_ten_kernel_dimension"] == 20
      and registry["exact_result"]["all_ten_quotient_dimension"] == 40
      and registry["exact_result"]["all_ten_quotient_rank"] == 40)
check("registry", "action weld condition is explicit and unproved",
      registry["exact_result"]["action_weld_condition"] == "E0_EQUALS_P0__E2_EQUALS_P2"
      and registry["exact_result"]["action_weld_proved"] is False)
check("registry", "single-holonomy no-go is retained",
      registry["construction_disposition"]["single_holonomy_full_v070_bridge"] == "REMAINS_KILLED")
check("registry", "boundary-coordinate cost is not prematurely retyped",
      registry["construction_disposition"]["v070_boundary_coordinate_cost_retyped_as_existing_epsilon"] == "NOT_YET")
check("queue", "rank one is the coefficientwise action weld",
      "i_n(E_B-E_T)=p_KT" in new["next_work_queue"][0]["why"])
check("scope", "no new quotient field datum or coefficient is introduced",
      registry["constraint_accounting"]["new_scoped_quotients"] == 0
      and registry["constraint_accounting"]["new_bulk_fields"] == 0
      and registry["constraint_accounting"]["new_external_datum"] == 0
      and registry["constraint_accounting"]["new_continuous_coefficients"] == 0)
check("scope", "global tau and BFV remain open",
      registry["construction_disposition"]["full_tau_a0_overlap_and_global_epsilon_extension"] == "OPEN"
      and registry["construction_disposition"]["physical_bfv_charge_algebra_polarization_common_domain"] == "OPEN")
check("scope", "P1 P2 P3 remain unused",
      set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"})
check("scope", "no third lane is promoted", registry["program_fences"]["third_lane"] == "NOT_PROMOTED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

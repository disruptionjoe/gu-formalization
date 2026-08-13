#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.70."""

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


old = strict("lab/process/conditional-physics-ledger-v0.69.json")
new = strict("lab/process/conditional-physics-ledger-v0.70.json")
registry = strict("lab/process/selected-k77-minimal-edge-mode-reduction.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.69" and new["schema_version"] == "0.70")
check("schema", "predecessor points to v0.69", new["predecessor"].endswith("v0.69.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "global continuous residue remains frozen", new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84)
check("meter", "function and fork residue remain frozen",
      new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "one scoped quotient is added",
      old["residue"]["quotients_ranked"] == 4 and new["residue"]["quotients_ranked"] == 5)
check("frontier", "three conditions close", new["frontier_delta"]["conditions_closed"] == 3)
check("frontier", "one global edge condition opens", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check("frontier", "headline records the scoped quotient", new["frontier_delta"]["headline_delta"] == "SCOPED_QUOTIENT_PLUS_ONE")
check("source", "source return separates silence from repo construction",
      "SOURCE-SILENT" in new["source_return"]
      and "REPO-CONSTRUCTS" in new["source_return"]
      and "EDGE_EXTENSION" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.70 evidence", new_rows[rid]["evidence"] == "selected-k77-minimal-edge-mode-reduction-2026-08-08.md")
    check("rows", f"{rid} records the exact edge extension", "EDGE_EXTENSION_UNIQUE" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records the conditional rank-40 quotient", "CONDITIONAL_QUOTIENT_DIM40" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} keeps the global boundary problem open", "GLOBAL" in new_rows[rid]["mapping_grade"])

migrations = [
    item for item in new["migrations"]
    if item.get("from_version") == "0.69" and item.get("to_version") == "0.70"
]
check("migration", "five append-only migration edges exist",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "ordinary scalar counterterm leaves Omega unchanged",
      registry["exact_result"]["ordinary_counterterm_delta_omega"] == "ZERO")
check("registry", "edge coefficients are unique and signed",
      registry["exact_result"]["edge_coefficients"] == {"c0": -1, "c3": 1}
      and registry["exact_result"]["edge_coefficient_solution_dimension"] == 0)
check("registry", "all-ten extended dimension is sixty", registry["exact_result"]["all_ten_extended_dimension"] == 60)
check("registry", "all-ten form rank is forty", registry["exact_result"]["all_ten_form_rank"] == 40)
check("registry", "all-ten gauge kernel is twenty", registry["exact_result"]["all_ten_gauge_kernel_dimension"] == 20)
check("registry", "all-ten quotient is nondegenerate rank forty",
      registry["exact_result"]["all_ten_quotient_dimension"] == 40
      and registry["exact_result"]["all_ten_quotient_rank"] == 40)
check("queue", "rank one is global edge lift or source-selected domain",
      "labelled Y14" in new["next_work_queue"][0]["why"]
      and "source/action-select" in new["next_work_queue"][0]["why"])
check("scope", "boundary coordinate cost is twenty",
      registry["constraint_accounting"]["new_boundary_coordinate_dimension"] == 20)
check("scope", "no new coefficient freedom is introduced",
      registry["constraint_accounting"]["new_continuous_coefficients"] == 0)
check("scope", "physical boundary condition remains unselected",
      not registry["constraint_accounting"]["boundary_condition_selected"])
check("scope", "global edge bundle remains unconstructed",
      not registry["constraint_accounting"]["global_edge_bundle_constructed"])
check("scope", "P1 P2 P3 remain unused",
      set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"})
check("scope", "no third lane is promoted", registry["program_fences"]["third_lane"] == "NOT_PROMOTED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

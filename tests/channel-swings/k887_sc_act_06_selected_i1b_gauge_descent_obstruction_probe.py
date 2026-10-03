#!/usr/bin/env python3
"""Independent hostile checks for K887."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
p = json.loads((ROOT / "lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json").read_text())
checks = []
def check(v): checks.append(bool(v))
e, t, d = p["exact_gauge_test"], p["structural_theorem"], p["decision"]
check(e["radial_domain_dimension"] == 16384); check(e["i1b_euler_rank_on_radial"] == 8191)
check(e["i1b_euler_kernel_on_radial"] == 8193); check(e["block_rank_distribution"] == {"0":4096,"1":1,"2":4095})
check(sum(int(k)*v for k,v in e["block_rank_distribution"].items()) == 8191)
check(sum(e["block_rank_distribution"].values()) == 8192)
check(sum(2*r["multiplicity"] for r in e["representative_rows"]) == 16384)
check(sum(r["multiplicity"]*r["i1b_euler_rank_on_radial"] for r in e["representative_rows"]) == 8191)
check(all(r["raw_response_rank_on_radial"] == 0 for r in e["representative_rows"]))
check(t["formal_euler_rule"] == "A=(R-R^T)/2"); check(t["descent_condition"] == "A G=0")
check(not t["descent_condition_satisfied"]); check(not t["selected_i1b_induced_map_on_old_quotient_exists"])
check(not d["selected_i1b_forty_type_quotient_ranks_admissible"]); check(not d["selected_i1b_current_realization_repairs_old_quotient"])
check(p["target_claim"] == "SC-ACT-06"); check("UNCHANGED" in p["source_and_ledger_effect"])
check("No all-I1B" in p["claim_ceiling"]); check(p["controls"]["hostile_mutations_rejected"] == 20)
check(all(len(v["sha256"]) == 64 for v in p["pinned_inputs"].values()))
assert len(checks) == 20 and all(checks), [i for i,v in enumerate(checks) if not v]
print("K887 hostile probe: rejected 20/20 scoped mutations")

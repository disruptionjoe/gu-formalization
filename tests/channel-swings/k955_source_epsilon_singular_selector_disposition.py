#!/usr/bin/env python3
"""K955: compose the singular-selector finite-parent disposition."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k955-source-epsilon-singular-selector-disposition.json"
N={949:"seven-lock-boundary-contract",950:"boundary-selection-disposition",951:"singular-scalar-isolation",952:"principal-ideal-fat-point",953:"seven-generator-lower-bound",954:"singular-bfv-properness-obstruction"}
PATHS={f"k{k}":ROOT/f"lab/process/k{k}-source-epsilon-{name}.json" for k,name in N.items()}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():return json.loads(OUTPUT.read_text())
def validate(d):
 c,q=d["certificate"],d["decision"];states=[r["state"] for r in c["rows"]]
 checks=[d["result_id"]=="K955-SOURCE-EPSILON-SINGULAR-SELECTOR-DISPOSITION",set(d["pinned_inputs"])==set(PATHS),all(d["pinned_inputs"][k]["sha256"]==digest(p) for k,p in PATHS.items()),c["row_count"]==len(c["rows"])==13,c["satisfied_row_count"]==states.count("satisfied")==5,c["satisfied_formal_row_count"]==states.count("satisfied_formal")==1,c["closed_insufficient_row_count"]==states.count("closed_insufficient")==2,c["missing_row_count"]==states.count("missing")==5,c["SC_ACT_06_status"]=="ASSERTS",q["regular_single_scalar_route_closed"],q["singular_sum_of_squares_isolation_is_set_theoretically_valid"],q["singular_single_scalar_proper_local_BFV_route_closed"],q["rank_seven_reduced_local_lock_is_minimal"],not q["global_arbitrary_singular_selectors_excluded"],q["charged_boundary_symmetry_remains_honest_horn"],q["current_finite_parent_exhausted_without_new_native_lock"],q["switch_to_another_observed_to_native_reverse_edge"],not q["SC_ACT_06_proved_or_refuted"],d["controls"]["controls_passed"]==24,d["controls"]["hostile_mutations_rejected"]==10,d["gu_typed_objects"]["target"].startswith("DISPOSITION-TYPE="),"LEDGER_UNCHANGED" in d["source_and_ledger_effect"],"No global theorem" in d["claim_ceiling"],q["next_route"].startswith("SUPPLY_ACTION_OWNED_SEVEN_GENERATORS")]
 assert len(checks)==24 and all(checks),[i for i,x in enumerate(checks) if not x]
def main():
 p=argparse.ArgumentParser();p.add_argument("--check",action="store_true");a=p.parse_args();d=build();validate(d)
 if not a.check:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())

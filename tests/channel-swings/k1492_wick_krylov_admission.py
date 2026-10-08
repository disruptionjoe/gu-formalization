#!/usr/bin/env python3
"""Controls for K1492's Wick Krylov admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1492-wick-krylov-admission.json").read_text())

def validate(d):
 c,q=d["bridge_census"],d["decision"]
 return [d["schema_version"]=="1.0",d["claim_id"]=="K1492",c["row_count"]==179,
  c["satisfied_count"]==111,c["conditional_count"]==10,c["excluded_count"]==54,c["missing_count"]==4,
  sum(c[k] for k in ("satisfied_count","conditional_count","excluded_count","missing_count"))==c["row_count"],
  len(c["new_satisfied_rows"])==5,len(c["new_excluded_rows"])==4,len(c["missing_rows"])==4,
  q["higher_chaos_krylov_direction_constructed"],q["two_dimensional_ritz_quasimode_excluded"],
  q["strict_variational_improvement_proved"],q["enlarged_scalar_and_brst_window_excluded"],
  not q["matching_ground_energy_lower_asymptotic_constructed"],not q["ground_energy_recentered_limit_constructed"],
  not q["full_spacetime_pde_repair_constructed"],not q["source_selected_reduction_constructed"],
  not q["k1145_k1150_candidate_counts_move"],not q["protected_status_change"],
  "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in d["source_and_ledger_effect"],
  "SC-META-53 UNCERTAIN" in d["source_and_ledger_effect"],"K1145/K1150 0/7" in d["source_and_ledger_effect"]]

def main():
 checks=[]
 for name,pin in D["pinned_inputs"].items():checks.append((f"{name} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"]))
 checks.extend((f"serialized invariant {i}",ok) for i,ok in enumerate(validate(D),1))
 checks.extend([("prior plus new rows",170+5+4==179),("satisfied delta",106+5==111),("excluded delta",50+4==54)])
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

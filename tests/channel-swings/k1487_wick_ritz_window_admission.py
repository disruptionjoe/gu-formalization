#!/usr/bin/env python3
"""Controls for K1487's admission census and protected ceilings."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/"lab/process/k1487-wick-ritz-window-admission.json").read_text())


def validate(d):
 c,q=d["bridge_census"],d["decision"]
 return [d["claim_id"]=="K1487",c["row_count"]==170,c["satisfied_count"]==106,c["conditional_count"]==10,c["excluded_count"]==50,c["missing_count"]==4,sum(c[k] for k in ("satisfied_count","conditional_count","excluded_count","missing_count"))==c["row_count"],len(c["new_satisfied_rows"])==5,len(c["new_excluded_rows"])==3,len(c["missing_rows"])==4,q["wick_third_moment_triangle_bound_proved"],q["ritz_leading_upper_correction_proved"],q["subleading_scalar_recenter_window_excluded"],q["brst_recenter_window_excluded"],not q["matching_ground_energy_lower_asymptotic_constructed"],not q["ground_energy_recentered_limit_constructed"],not q["full_spacetime_pde_repair_constructed"],not q["source_selected_reduction_constructed"],not q["k1145_k1150_candidate_counts_move"],not q["protected_status_change"],"33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in d["source_and_ledger_effect"],"K1145/K1150 0/7" in d["source_and_ledger_effect"]]


def main():
 checks=[]
 for name,pin in D["pinned_inputs"].items():checks.append((f"{name} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"]))
 checks.extend((f"serialized invariant {i}",ok) for i,ok in enumerate(validate(D),1))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

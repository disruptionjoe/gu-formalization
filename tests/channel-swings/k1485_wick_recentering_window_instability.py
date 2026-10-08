#!/usr/bin/env python3
"""Controls for K1485's scalar-recentering instability window."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1485-wick-recentering-window-instability.json").read_text())


def validate(d):
 a,q=d["recentering_window"],d["decision"]
 return [d["claim_id"]=="K1485","a_N<=6gC_N^2-g sigma_N+O(N)" in a["necessary_upper_location"],"a_N>=6gC_N^2-(g-epsilon)sigma_N" in a["excluded_window"],"nonzero vacuum vector" in a["weak_trial"],"contradicting weak Mosco liminf" in a["mosco_failure"],"recovers less than g sigma_N" in a["projective_case"],q["uniform_semiboundedness_requires_subleading_negative_shift"],q["necessary_negative_shift_leading_size"]=="g sigma_N",q["fixed_fraction_under_recentered_window_excluded"],not q["excluded_window_mosco_liminf_holds"],not q["ground_energy_recentered_mosco_limit_excluded"],not q["boundary_window_is_two_sided_ground_energy_asymptotic"],not q["protected_status_change"]]


def main():
 checks=[]
 for name,pin in D["pinned_inputs"].items(): checks.append((f"{name} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"]))
 checks.extend((f"serialized invariant {i}",ok) for i,ok in enumerate(validate(D),1))
 g=.4; eps=.1
 values=[]
 for n in (16,32,64,128,256):
  sigma=n**2.5; ritz=-g*sigma+3*n; shift_correction=-(g-eps)*sigma
  recentered=ritz-shift_correction; values.append(recentered)
  checks.append((f"excluded-window value eventually negative N={n}",recentered<0))
 checks.append(("excluded-window values diverge down",all(x>y for x,y in zip(values,values[1:]))))
 checks.append(("N term is lower order than sigma",256/(256**2.5)<.001))
 for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__": main()

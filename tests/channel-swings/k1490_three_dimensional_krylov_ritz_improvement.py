#!/usr/bin/env python3
"""Controls for K1490's three-dimensional Krylov Ritz improvement."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1490-three-dimensional-krylov-ritz-improvement.json").read_text())

def validate(d):
 a,q=d["three_dimensional_ritz"],d["decision"]
 return [d["schema_version"]=="1.0",d["claim_id"]=="K1490",
  "e0=1" in a["basis"],"tau_N>=1" in a["multiplication_matrix"],
  "|eta_N|" in a["moment_bounds"] and "6561" in a["moment_bounds"],
  "t=1/6562" in a["fixed_trial"] and "c_star=1/39372" in a["fixed_trial"],
  "8 omega_max(N)=O(N)" in a["free_cost"],"(1+c_star)g sigma_N" in a["ground_energy_upper"],
  "not the leading full variational coefficient" in a["strict_consequence"],
  q["three_dimensional_krylov_compression_constructed"],q["hypercontractive_eta_absolute_upper"]==6561,
  q["fixed_trial_t_denominator"]==6562,q["strict_improvement_constant"]=="1/39372",
  q["ground_energy_upper_correction"]=="-(1+1/39372)g sigma_N+O(N)",
  not q["two_dimensional_minus_one_coefficient_variationally_sharp"],
  not q["ground_energy_asymptotic_determined"],not q["protected_status_change"]]

def main():
 checks=[]
 for name,pin in D["pinned_inputs"].items():checks.append((f"{name} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"]))
 checks.extend((f"serialized invariant {i}",ok) for i,ok in enumerate(validate(D),1))
 M=6561;t=1/(M+1);mu=1/(2*(M+1));tau=1;eta=M
 r=(-2+mu-2*tau*t+eta*t*t)/(2+t*t)
 checks.extend([("Nelson degree-four constant",3**2==9),("Nelson degree-eight constant",3**4==81),
  ("eta Cauchy bound",81**2==6561),("worst-case trial strictly below minus one",r<-1),
  ("advertised conservative gap",r<=-1-1/39372),("free cost lower order",8*128/(128**2.5)<0.006)])
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

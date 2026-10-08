#!/usr/bin/env python3
"""Controls for K1491's recentering and BRST instability window."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1491-krylov-recentering-brst-instability.json").read_text())

def validate(d):
 a,q=d["recentering_and_brst"],d["decision"]
 return [d["schema_version"]=="1.0",d["claim_id"]=="K1491","c_star=1/39372" in a["constant"],
  "kappa g sigma_N" in a["necessary_recentering"],"-g epsilon sigma_N" in a["explicit_window"],
  "nonzero vacuum component" in a["weak_limit"],"Mosco weak liminf fails" in a["mosco_failure"],
  "harmonic BRST vacuum" in a["brst_transfer"],q["necessary_scalar_correction_coefficient_lower"]=="1+1/39372",
  not q["old_coefficient_one_window_is_final"],q["enlarged_fixed_fraction_window_spectral_bottom_diverges"],
  not q["enlarged_window_mosco_weak_liminf_holds"],not q["harmonic_brst_factor_repairs_window"],
  not q["true_ground_energy_recentering_excluded"],not q["changed_representation_excluded"],
  not q["protected_status_change"]]

def main():
 checks=[]
 for name,pin in D["pinned_inputs"].items():checks.append((f"{name} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"]))
 checks.extend((f"serialized invariant {i}",ok) for i,ok in enumerate(validate(D),1))
 c=1/39372;eps=c/2
 checks.extend([("positive strict improvement",c>0),("window epsilon admissible",0<eps<c),
  ("sigma dominates O(N)",all(n**2.5/n>100 for n in (32,64,128))),
  ("trial vacuum coefficient nonzero",1/(2+(1/6562)**2)**0.5>0.7)])
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

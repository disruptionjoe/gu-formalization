#!/usr/bin/env python3
"""Independent-order and multistart tangent-regression control for K1739."""
import importlib.util,json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
SPEC=importlib.util.spec_from_file_location("k1733",ROOT/"tests/channel-swings/k1733_finite_strength_four_point_benchmark.py")
K=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(K)
TARGET=(-0.10375807269568682,-0.12852500388603265)
def intercepts(qs,sols):
 s=np.sqrt(np.array(qs));p=np.array([x[1] for x in sols]);a=np.array([x[2] for x in sols])
 return (np.polyfit(s,(p-K.P0)/s,2)[2],np.polyfit(s,(a-K.A0)/s,2)[2])
def main():
 d=json.loads((ROOT/"lab/process/k1739-finite-channel-tangent-regression.json").read_text());r=d["regression"];z=d["decision"]
 qs=r["q_grid"];s120=[];s180=[];spreads=[];checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1739"),("grade",d["grade"]=="reproducible_numerical_regression_not_interval_certification")]
 records={x["q"]:x for x in r["order_180_minimizers"]}
 for q in qs:
  a,sa=K.solve(q,120);b,sb=K.solve(q,180);s120.append(a);s180.append(b);spreads.append(max(sa,sb));rec=records[q]
  checks += [(f"orders objective {q}",abs(a[0]-b[0])<6e-21),(f"starts {q}",max(sa,sb)<8e-21),
   (f"record j {q}",abs(b[0]-rec["j"])<2e-20),(f"record p {q}",abs(b[1]-rec["p"])<2e-12),(f"record a {q}",abs(b[2]-rec["a"])<2e-12)]
 i120=intercepts(qs,s120);i180=intercepts(qs,s180)
 checks += [("120 P",abs(i120[0]-TARGET[0])<.0023),("120 A",abs(i120[1]-TARGET[1])<.0023),
  ("180 P",abs(i180[0]-TARGET[0])<.0023),("180 A",abs(i180[1]-TARGET[1])<.0023),
  ("record 120","-0.1023667741" in r["quadratic_ratio_extrapolation"]),("record 180","-0.1040829661" in r["quadratic_ratio_extrapolation"]),
  ("conditioning caveat","conditioning caveat" in r["controls"]),("supported",z["analytic_tangent_numerically_supported"]),
  ("not proof",not z["analytic_tangent_proved_by_regression"]),("branch open",not z["complete_branch_certified"]),
  ("global open",not z["global_two_radius_optimizer_proved"]),("interval guard","not an interval proof" in d["scope_guard"])]
 assert len(checks)==30
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

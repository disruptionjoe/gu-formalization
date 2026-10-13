#!/usr/bin/env python3
"""Protected-state and frontier controls for K1755."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1755-two-radius-rectangular-admission.json"
def validate(d):
 c=d["bridge_census"];p=d["protected_state"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1755"),
  ("total",c["total"]==455),("partition",c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]==c["total"]),
  ("new rows",c["new_satisfied_rows"]==["K1751","K1752","K1753","K1754","K1755"]),
  ("protected unchanged",all(not p[k] for k in p if k.endswith("_changed"))),
  ("scores",p["k1145_score"]==p["k1150_score"]=="0/7"),
  ("chart admitted",z["rectangular_chart_and_boundaries_admitted"]),("improvement",z["named_rational_improvement_admitted"]),
  ("not whole",not z["whole_chart_optimizer_admitted"]),("not physical",not z["all_seed_or_physical_result_admitted"]),
  ("incumbent","collar" in d["next_frontier"]["incumbent"]),("haar alt","Haar" in d["next_frontier"]["strongest_alternative"]),
  ("tensor outlier","correlated" in d["next_frontier"]["high_confidence_outlier"]),
  ("lower seam","sixth-moment" in d["next_frontier"]["lower_principle_boundary"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

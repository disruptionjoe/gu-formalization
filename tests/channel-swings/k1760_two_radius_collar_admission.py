#!/usr/bin/env python3
"""Protected integration audit for K1760."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1760-two-radius-collar-admission.json"
def validate(d):
 r=d["residual_domain"];c=d["bridge_census"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1760"),("inputs",len(d["inputs"])==7),
  ("q",r["q"]=="1/1024"),("closed rectangle",r["rectangle"]=="0<=c<=2-1/961 and 10^-34<=z<=1"),
  ("regularity","at least 1/32" in r["regularity"]),("remaining BnB","every box" in r["remaining_method"]),
  ("census sum",c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]==c["total"]),("census",c=={"total":460,"satisfied":381,"conditional":10,"excluded":65,"missing":4}),
  ("zero",z["zero_noise_collar_completed"]),("joint",z["joint_rare_zero_corner_completed"]),("rare",z["quantitative_rare_atom_collar_completed"]),
  ("residual",z["compact_residual_rectangle_frozen"]),("BnB open",not z["compact_core_branch_and_bound_completed"]),
  ("stationarity fenced",not z["stationarity_or_uniqueness_proved"]),("global fenced",not z["global_optimizer_proved"]),
  ("protected",not z["source_ledger_canon_paper_prediction_confirmation_or_public_status_changed"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

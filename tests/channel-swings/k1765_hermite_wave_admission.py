#!/usr/bin/env python3
"""Protected integration controls for K1765."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1765-hermite-wave-admission.json"
def validate(d):
 c=d["bridge_census"];p=d["protected_state"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1765"),("inputs",d["inputs"]==["K1760","K1761","K1762","K1763","K1764"]),("census",c=={"total":465,"satisfied":386,"conditional":10,"excluded":65,"missing":4}),("partition",c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]==c["total"]),("protected",all(not p[k] for k in p if k.endswith("_changed"))),("scores",p["k1145_score"]==p["k1150_score"]=="0/7"),("hierarchy",z["finite_hermite_lower_hierarchy_admitted"]),("upper",z["candidate_absolute_arb_upper_admitted"]),("pilot fenced",not z["naive_interval_cover_admitted_as_global_certificate"]),("global fenced",not z["global_two_radius_optimizer_admitted"]),("physical fenced",not z["all_seed_or_physical_result_admitted"]),("next gate","c=2-q/t^2" in d["next_gate"] and "replayable exact partition" in d["next_gate"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

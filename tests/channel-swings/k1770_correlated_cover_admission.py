#!/usr/bin/env python3
"""Protected integration controls for K1770."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1770-correlated-cover-admission.json"
def validate(d):
 c=d["bridge_census"];p=d["protected_state"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1770"),("inputs",d["inputs"]==["K1765","K1766","K1767","K1768","K1769"]),("census",c=={"total":470,"satisfied":391,"conditional":10,"excluded":65,"missing":4}),("partition",sum(c[k] for k in ("satisfied","conditional","excluded","missing"))==c["total"]),("protected",all(v is False for k,v in p.items() if k.endswith("_changed"))),("scores",p["k1145_score"]==p["k1150_score"]=="0/7"),("engine",z["correlation_preserving_engine_admitted"]),("partition admitted",z["zero_unresolved_partition_admitted"]),("cover admitted",z["sixty_cell_degree_seven_outer_cover_admitted"]),("Fisher fenced",not z["full_fisher_stationarity_or_uniqueness_admitted"]),("global fenced",not z["global_two_radius_optimizer_admitted"]),("physical fenced",not z["all_seed_or_physical_result_admitted"]),("next gate","Full-Fisher interval Newton" in d["next_gate"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

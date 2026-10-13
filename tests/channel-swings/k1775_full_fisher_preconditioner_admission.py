#!/usr/bin/env python3
"""Protected integration controls for K1775."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1775-full-fisher-preconditioner-admission.json"
def validate(d):
 c=d["bridge_census"];p=d["protected_state"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1775"),("inputs",d["inputs"]==["K1770","K1771","K1772","K1773","K1774"]),("census",c=={"total":475,"satisfied":396,"conditional":10,"excluded":65,"missing":4}),("partition",sum(c[k] for k in ("satisfied","conditional","excluded","missing"))==c["total"]),("protected",all(v is False for k,v in p.items() if k.endswith("_changed"))),("geometry",z["five_piece_geometric_preconditioner_admitted"]),("contract",z["full_fisher_variational_contract_admitted"]),("no exclusion",not z["boundary_strip_exclusion_admitted"]),("no Newton",not z["full_fisher_interval_newton_admitted"]),("no optimizer",not z["global_two_radius_optimizer_admitted"]),("physical fenced",not z["all_seed_or_physical_result_admitted"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

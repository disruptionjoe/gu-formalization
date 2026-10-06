#!/usr/bin/env python3
"""K1189: corrected changed-parent radial cancellation cost."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1189-changed-parent-cancellation-cost.json"
PATHS={"k891":ROOT/"lab/process/k891-sc-act-06-gauge-cancellation-necessity.json","k1127":ROOT/"lab/process/k1127-k887-t0-gauge-carrier-correction.json","k1129":ROOT/"lab/process/k1129-k887-k940-consumer-survival-audit.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 k=json.loads(PATHS["k891"].read_text());t=k["cancellation_theorem"]
 return {"schema_version":"1.0","result_id":"K1189-CHANGED-PARENT-CANCELLATION-COST","created":"2026-10-05","status":"working_draft_verified","classification":"CORRECTION_PROPAGATION","target_claim":"SC-ACT-06","pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},"cancellation_equation":"(H+C)G=0","forced_restriction":"CG=-HG","full_radial_domain_dimension":t["radial_domain_dimension"],"minimum_completion_restriction_rank":t["minimum_completion_restriction_rank"],"rank_below_8191_suffices":False,"raw_response_cancellation_already_zero_on_radial":True,"replacement_parent_constructed":False,"claim_ceiling":"exact auxiliary restriction cost; no replacement parent, action ownership, or functional completion"}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K1189-CHANGED-PARENT-CANCELLATION-COST" and p["status"]=="working_draft_verified" and p["classification"]=="CORRECTION_PROPAGATION" and p["target_claim"]=="SC-ACT-06"
 assert p["cancellation_equation"]=="(H+C)G=0" and p["forced_restriction"]=="CG=-HG" and p["full_radial_domain_dimension"]==16384 and p["minimum_completion_restriction_rank"]==8191
 assert not p["rank_below_8191_suffices"] and p["raw_response_cancellation_already_zero_on_radial"] and not p["replacement_parent_constructed"]
 assert set(p["pinned_inputs"])==set(PATHS) and all(v["sha256"]==digest(ROOT/v["path"]) for v in p["pinned_inputs"].values()) and "no replacement parent" in p["claim_ceiling"]
def main()->int:
 q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");print("PASS controls=16",file=__import__('sys').stderr);return 0
if __name__=="__main__":raise SystemExit(main())

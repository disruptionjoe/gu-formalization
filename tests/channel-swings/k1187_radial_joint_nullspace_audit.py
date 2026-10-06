#!/usr/bin/env python3
"""K1187: compose the corrected auxiliary radial ranks."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1187-radial-joint-nullspace-audit.json"
PATHS={"k887":ROOT/"lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json","k1127":ROOT/"lab/process/k1127-k887-t0-gauge-carrier-correction.json","k1129":ROOT/"lab/process/k1129-k887-k940-consumer-survival-audit.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 k887=json.loads(PATHS["k887"].read_text());e=k887["exact_gauge_test"];dim=e["radial_domain_dimension"];hr=e["i1b_euler_rank_on_radial"];jr=max(r["raw_response_rank_on_radial"] for r in e["representative_rows"])
 return {"schema_version":"1.0","result_id":"K1187-RADIAL-JOINT-NULLSPACE-AUDIT","created":"2026-10-05","status":"working_draft_verified","classification":"CORRECTION_PROPAGATION","target_claim":"SC-ACT-06","pinned_inputs":{k:{"path":str(v.relative_to(ROOT)),"sha256":digest(v)} for k,v in PATHS.items()},"radial_domain_dimension":dim,"hessian_rank_on_radial":hr,"raw_response_rank_on_radial":jr,"joint_restriction_rank":hr,"joint_kernel_dimension_on_radial":dim-hr,"full_radial_module_jointly_admissible":False,"action_owned_current_t0_gauge_rank":4,"null_stratum_computed":False,"ownership_disposition":"K1127/K1129: frozen connection-only auxiliary carrier, not the native T=0 source-action gauge image","claim_ceiling":"exact nonnull auxiliary-slice arithmetic; no native gauge ownership, null-stratum transfer, or physical quotient"}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K1187-RADIAL-JOINT-NULLSPACE-AUDIT" and p["classification"]=="CORRECTION_PROPAGATION" and p["target_claim"]=="SC-ACT-06"
 assert p["radial_domain_dimension"]==16384 and p["hessian_rank_on_radial"]==8191 and p["raw_response_rank_on_radial"]==0
 assert p["joint_restriction_rank"]==8191 and p["joint_kernel_dimension_on_radial"]==8193 and p["joint_kernel_dimension_on_radial"]==p["radial_domain_dimension"]-p["joint_restriction_rank"]
 assert not p["full_radial_module_jointly_admissible"] and p["action_owned_current_t0_gauge_rank"]==4 and not p["null_stratum_computed"]
 assert set(p["pinned_inputs"])==set(PATHS) and all(v["sha256"]==digest(ROOT/v["path"]) for v in p["pinned_inputs"].values())
 assert "not the native" in p["ownership_disposition"] and "nonnull" in p["claim_ceiling"]
def main()->int:
 q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");print("PASS controls=17",file=__import__('sys').stderr);return 0
if __name__=="__main__":raise SystemExit(main())

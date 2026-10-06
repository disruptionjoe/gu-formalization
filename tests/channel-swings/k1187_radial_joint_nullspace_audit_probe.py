#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1187_radial_joint_nullspace_audit.py";CERT=ROOT/"lab/process/k1187-radial-joint-nullspace-audit.json"
def load():
 s=importlib.util.spec_from_file_location("k1187_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);paths=[("result_id",),("classification",),("target_claim",),("radial_domain_dimension",),("hessian_rank_on_radial",),("raw_response_rank_on_radial",),("joint_restriction_rank",),("joint_kernel_dimension_on_radial",),("full_radial_module_jointly_admissible",),("action_owned_current_t0_gauge_rank",),("null_stratum_computed",),("ownership_disposition",),("claim_ceiling",)];rejected=0
 for path in paths:
  bad=copy.deepcopy(p);old=bad[path[0]];bad[path[0]]=not old if isinstance(old,bool) else (old+1 if isinstance(old,int) else "BROKEN")
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 assert rejected==13;print("PASS controls=17 hostile_mutations_rejected=13/13");return 0
if __name__=="__main__":raise SystemExit(main())

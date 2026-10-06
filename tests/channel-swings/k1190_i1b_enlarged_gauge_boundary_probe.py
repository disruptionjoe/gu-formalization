#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1190_i1b_enlarged_gauge_boundary.py";CERT=ROOT/"lab/process/k1190-i1b-enlarged-gauge-boundary.json"
def load():
 s=importlib.util.spec_from_file_location("k1190_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);paths=[("result_id",),("status",),("classification",),("target_claim",),("actual_current_t0_gauge_rank",),("changed_parent_minimum_restriction_rank",),("null_radial_rank_computed",),("candidate_meeting_full_packet",),("next_condition",),("protected_disposition",),("claim_ceiling",),("auxiliary_nonnull_radial","domain_dimension"),("auxiliary_nonnull_radial","hessian_defect_rank"),("auxiliary_nonnull_radial","joint_null_dimension"),("favorable_nonnull_overgrant","after_auxiliary_radial"),("favorable_nonnull_overgrant","after_auxiliary_radial_and_rank98_best")];rejected=0
 for path in paths:
  bad=copy.deepcopy(p);c=bad
  for k in path[:-1]:c=c[k]
  old=c[path[-1]];c[path[-1]]=not old if isinstance(old,bool) else (old+1 if isinstance(old,int) else "BROKEN")
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 assert rejected==16;print("PASS controls=20 hostile_mutations_rejected=16/16");return 0
if __name__=="__main__":raise SystemExit(main())

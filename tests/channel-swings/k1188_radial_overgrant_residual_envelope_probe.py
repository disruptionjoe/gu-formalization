#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1188_radial_overgrant_residual_envelope.py";CERT=ROOT/"lab/process/k1188-radial-overgrant-residual-envelope.json"
def load():
 s=importlib.util.spec_from_file_location("k1188_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);paths=[("result_id",),("classification",),("target_claim",),("current_nonnull_residual_after_h_j_and_actual_gauge",),("actual_current_gauge_rank",),("auxiliary_radial_joint_null_grant",),("residual_after_radial_overgrant",),("rank98_grant",),("nonnull_only",),("full_packet_candidate_after_overgrant",),("claim_ceiling",),("residual_after_radial_plus_rank98","best_independent_placement"),("residual_after_radial_plus_rank98","worst_complete_overlap"),("ownership","radial_joint_nullspace")];rejected=0
 for path in paths:
  bad=copy.deepcopy(p);c=bad
  for k in path[:-1]:c=c[k]
  old=c[path[-1]];c[path[-1]]=not old if isinstance(old,bool) else (old+1 if isinstance(old,int) else "BROKEN")
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 assert rejected==14;print("PASS controls=18 hostile_mutations_rejected=14/14");return 0
if __name__=="__main__":raise SystemExit(main())

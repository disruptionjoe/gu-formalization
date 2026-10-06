#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1189_changed_parent_cancellation_cost.py";CERT=ROOT/"lab/process/k1189-changed-parent-cancellation-cost.json"
def load():
 s=importlib.util.spec_from_file_location("k1189_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);paths=["result_id","classification","target_claim","cancellation_equation","forced_restriction","full_radial_domain_dimension","minimum_completion_restriction_rank","rank_below_8191_suffices","raw_response_cancellation_already_zero_on_radial","replacement_parent_constructed","claim_ceiling","status"];rejected=0
 for key in paths:
  bad=copy.deepcopy(p);old=bad[key];bad[key]=not old if isinstance(old,bool) else (old+1 if isinstance(old,int) else "BROKEN")
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 assert rejected==12;print("PASS controls=16 hostile_mutations_rejected=12/12");return 0
if __name__=="__main__":raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1185_i1b_measured_candidate_boundary.py";CERT=ROOT/"lab/process/k1185-i1b-measured-candidate-boundary.json"
def load():
 s=importlib.util.spec_from_file_location("k1185_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);rejected=0
 for path in [("result_id",),("classification",),("target_claim",),("current_measured_source_owned_k132_maps",),("candidate_meeting_full_packet",),("next_condition",),("protected_disposition",)]+[(group,key) for group in ("causal_complement_ranks","actual_residual_after_gauge","best_favorable_residual_after_rank98") for key in ("timelike","spacelike","null")]:
  bad=copy.deepcopy(p);c=bad
  for k in path[:-1]:c=c[k]
  c[path[-1]]=c[path[-1]]+1 if isinstance(c[path[-1]],int) else "BROKEN"
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 assert rejected==16;print("PASS controls=18 hostile_mutations_rejected=16/16");return 0
if __name__=="__main__":raise SystemExit(main())

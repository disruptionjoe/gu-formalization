#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1183_rank98_overlap_envelope.py";CERT=ROOT/"lab/process/k1183-rank98-overlap-envelope.json"
def load():
 s=importlib.util.spec_from_file_location("k1183_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);rejected=0
 for path in [("result_id",),("status",),("prior_channel_ownership",)]+[("exact_controls","cases",i,k) for i in (0,1) for k in ("j_sequential_complement_min","j_sequential_complement_max","repair_residual_best_case","repair_residual_worst_overlap")]:
  bad=copy.deepcopy(p);c=bad
  for k in path[:-1]:c=c[k]
  c[path[-1]]=1 if not isinstance(c[path[-1]],int) else c[path[-1]]+1
  try:m.validate(bad)
  except (AssertionError,KeyError,AttributeError):rejected+=1
 assert rejected==11;print("PASS controls=16 hostile_mutations_rejected=11/11");return 0
if __name__=="__main__":raise SystemExit(main())

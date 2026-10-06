#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1186_joint_gauge_admissibility_theorem.py";CERT=ROOT/"lab/process/k1186-joint-gauge-admissibility-theorem.json"
def load():
 s=importlib.util.spec_from_file_location("k1186_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);paths=[("result_id",),("status",),("classification",),("necessary_equations",),("equivalent_condition",),("dimension_ceiling",),("sharp",),("claim_ceiling",)]+[("controls",i,"admissible") for i in range(4)];rejected=0
 for path in paths:
  bad=copy.deepcopy(p);c=bad
  for k in path[:-1]:c=c[k]
  old=c[path[-1]];c[path[-1]]=not old if isinstance(old,bool) else (["BROKEN"] if isinstance(old,list) else "BROKEN")
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 assert rejected==12;print("PASS controls=16 hostile_mutations_rejected=12/12");return 0
if __name__=="__main__":raise SystemExit(main())

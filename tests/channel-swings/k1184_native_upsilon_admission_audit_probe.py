#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k1184_native_upsilon_admission_audit.py";CERT=ROOT/"lab/process/k1184-native-upsilon-admission-audit.json"
def load():
 s=importlib.util.spec_from_file_location("k1184_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();p=json.loads(CERT.read_text());m.validate(p);rejected=0
 muts=[("result_id","BROKEN"),("classification","COMPARATOR"),("target_claim","NONE"),("protected_disposition","MOVED")]
 for k,v in muts:
  bad=copy.deepcopy(p);bad[k]=v
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 for k in ("pass","fail","open"):
  bad=copy.deepcopy(p);bad["summary"][k]+=1
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 for k in ("candidate_sufficient","failure_precedes_functional_promotion"):
  bad=copy.deepcopy(p);bad["summary"][k]=not bad["summary"][k]
  try:m.validate(bad)
  except (AssertionError,KeyError):rejected+=1
 bad=copy.deepcopy(p);bad["gate_rows"][3]["evidence"]="none"
 try:m.validate(bad)
 except (AssertionError,KeyError):rejected+=1
 assert rejected==10;print("PASS controls=15 hostile_mutations_rejected=10/10");return 0
if __name__=="__main__":raise SystemExit(main())

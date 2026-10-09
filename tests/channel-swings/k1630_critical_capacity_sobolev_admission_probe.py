#!/usr/bin/env python3
"""Hostile mutations for K1630's protected boundaries."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 c=d["census"];p=d["protected_boundaries"]
 return (c["rows"]==345 and c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]==345 and c["physics_ledger"]=={"SAME":33,"DIFFERS":22,"NEEDS":31,"OVER_DETERMINED":2} and all(v is False for v in p.values()))
def main():
 d=json.loads((ROOT/"lab/process/k1630-critical-capacity-sobolev-admission.json").read_text());checks=[("baseline",reject(d))]
 for key in d["protected_boundaries"]:
  m=deepcopy(d);m["protected_boundaries"][key]=True;checks.append((key,not reject(m)))
 for key in ["rows","satisfied","conditional","excluded","missing"]:
  m=deepcopy(d);m["census"][key]+=1;checks.append((f"census {key}",not reject(m)))
 m=deepcopy(d);m["census"]["physics_ledger"]["SAME"]+=1;checks.append(("ledger mutation",not reject(m)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

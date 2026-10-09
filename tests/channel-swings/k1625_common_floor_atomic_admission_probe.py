#!/usr/bin/env python3
"""Hostile mutations for K1625's protected census."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 c,p=d["census"],d["protected_boundaries"]
 return (c["rows"]==340 and c["satisfied"]+c["conditional"]+c["excluded"]+c["missing"]==340
  and sum(c["physics_ledger"].values())==88 and c["k1145_k1150_scorable_rows"]=="0/7"
  and all(v is False for v in p.values()) and len(d["next_wakes"])==3)
def main():
 d=json.loads((ROOT/"lab/process/k1625-common-floor-atomic-admission.json").read_text());checks=[("baseline",reject(d))]
 for key in ("rows","satisfied","conditional","excluded","missing"):
  m=deepcopy(d);m["census"][key]+=1;checks.append((f"mutate {key}",not reject(m)))
 for key in d["protected_boundaries"]:
  m=deepcopy(d);m["protected_boundaries"][key]=True;checks.append((f"flip {key}",not reject(m)))
 m=deepcopy(d);m["census"]["physics_ledger"]["SAME"]+=1;checks.append(("mutate ledger",not reject(m)))
 m=deepcopy(d);m["next_wakes"].pop();checks.append(("drop wake",not reject(m)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

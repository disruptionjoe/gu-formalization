#!/usr/bin/env python3
"""Hostile mutations for K1623's sufficient covariance tests."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d["effective_rank_tests"],d["decision"]
 return ("not necessary thresholds" in q["scope_guard"] and z["trace_test_sufficient"] and z["rank_norm_test_sufficient"]
  and z["vanishing_relative_excess_sufficient"] and z["subextensive_effective_rank_sufficient"]
  and not z["critical_capacity_resolved"] and not z["protected_status_change"])
def main():
 d=json.loads((ROOT/"lab/process/k1623-effective-rank-covariance-rigidity.json").read_text());checks=[("baseline",reject(d))]
 m=deepcopy(d);m["effective_rank_tests"]["scope_guard"]=m["effective_rank_tests"]["scope_guard"].replace("not necessary thresholds","the exact necessary thresholds");checks.append(("promote threshold",not reject(m)))
 for key in ("trace_test_sufficient","rank_norm_test_sufficient","vanishing_relative_excess_sufficient","subextensive_effective_rank_sufficient","critical_capacity_resolved","protected_status_change"):
  m=deepcopy(d);m["decision"][key]=not m["decision"][key];checks.append((f"flip {key}",not reject(m)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()

#!/usr/bin/env python3
"""Exact controls for K1300's functional-lift admission boundary."""
import hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1300-functional-lift-admission-boundary.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
R=D["k1150_control_replay"]; counts=Counter(row["state"] for row in R["rows"])
check("K1150 satisfied",counts["satisfied"]==R["mathematical_rows_satisfied"]==4)
check("K1150 conditional",counts["conditional"]==R["mathematical_rows_conditional"]==1)
check("K1150 missing",counts["missing"]==R["mathematical_rows_missing"]==2)
check("native K1150 zero",R["native_candidate_pass_count"]==0)
I=D["integrated_k1295_boundary"]
check("integrated total",I["satisfied_count"]+I["excluded_count"]+I["conditional_count"]+I["missing_count"]==35)
check("three rows conditional",len(I["moved_to_conditional"])==3)
check("three ownership rows missing",len(I["still_missing"])==3)
check("source packet absent",not D["decision"]["source_selected_functional_packet_constructed"])
check("protected unchanged",not D["decision"]["protected_status_change"])
assert n==16
print("RESULT: PASS 16/16")

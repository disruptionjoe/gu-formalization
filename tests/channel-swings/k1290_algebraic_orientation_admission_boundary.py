#!/usr/bin/env python3
"""Exact controls for K1290's integrated admission."""
import hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1290-algebraic-orientation-admission-boundary.json").read_text())
n=0
def c(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
def digest(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

c("id",D["result_id"]=="K1290-ALGEBRAIC-ORIENTATION-ADMISSION-BOUNDARY")
for key in ("k1285","k1286","k1287","k1288","k1289"):
    c(f"{key} pin",digest(D["pinned_inputs"][key]["path"])==D["pinned_inputs"][key]["sha256"])
counts=Counter(r["state"] for r in D["certificate"]["rows"])
c("satisfied count",counts["satisfied"]==D["certificate"]["satisfied_count"]==15)
c("excluded count",counts["excluded"]==D["certificate"]["excluded_count"]==6)
c("conditional count",counts["conditional"]==D["certificate"]["conditional_count"]==5)
c("missing count",counts["missing"]==D["certificate"]["missing_count"]==6)
c("K1145 zero",D["certificate"]["k1145_pass_count"]==0)
c("K1150 zero",D["certificate"]["k1150_pass_count"]==0)
c("protected unchanged",D["decision"]["protected_status_change"] is False)
assert n==13
print("RESULT: PASS 13/13")

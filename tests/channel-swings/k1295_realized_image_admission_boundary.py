#!/usr/bin/env python3
"""Exact controls for K1295's integrated admission boundary."""
import hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1295-realized-image-admission-boundary.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
def digest(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
check("id",D["result_id"]=="K1295-REALIZED-IMAGE-ADMISSION-BOUNDARY")
for key in ("k1290","k1291","k1292","k1293","k1294"):
    check(f"{key} pin",digest(D["pinned_inputs"][key]["path"])==D["pinned_inputs"][key]["sha256"])
counts=Counter(row["state"] for row in D["certificate"]["rows"])
check("satisfied count",counts["satisfied"]==D["certificate"]["satisfied_count"]==19)
check("excluded count",counts["excluded"]==D["certificate"]["excluded_count"]==6)
check("conditional count",counts["conditional"]==D["certificate"]["conditional_count"]==4)
check("missing count",counts["missing"]==D["certificate"]["missing_count"]==6)
check("K1145 zero",D["certificate"]["k1145_pass_count"]==0)
check("K1150 zero",D["certificate"]["k1150_pass_count"]==0)
check("source owner absent",not D["decision"]["source_selector_owned"])
check("sign not a component label",not D["decision"]["p_sign_is_a_connected_component_label"])
check("protected unchanged",not D["decision"]["protected_status_change"])
assert n==15
print("RESULT: PASS 15/15")

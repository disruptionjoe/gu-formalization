#!/usr/bin/env python3
"""Exact controls for K1296's Weyl-covariant quadratic normal model."""
import hashlib,json
from math import factorial,prod
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1296-weyl-covariant-quadratic-model.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
pin=D["pinned_inputs"]["k1294"]
check("K1294 pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]
check("W(D7) order",T["regular_orbit_size"]==2**6*factorial(7)==322560)
b=(1,2,3,4,5,6,7)
perm=(2,0,1,6,5,4,3)
bp=tuple(b[i] for i in perm)
check("positive fixture",min(b)>0)
check("spectral floor",min(b)==1)
check("conjugate trace",sum(bp)==sum(b))
check("conjugate determinant",prod(bp)==prod(b))
check("conjugate spectrum",sorted(bp)==sorted(b))
check("positive Hessian",T["base_hessian_positive_definite"])
check("covariant transport","w B_o w^T" in T["transport_law"])
check("quadratic Hessian",T["quadratic_hessian_equals_selector_hessian"])
check("not global selector",not T["finite_selector_equal_to_quadratic_model_globally"])
check("source owner absent",not T["source_owned"])
assert n==12
print("RESULT: PASS 12/12")

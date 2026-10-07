#!/usr/bin/env python3
"""Exact controls for K1287's normalized threshold."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1287-algebraic-orientation-threshold.json").read_text())
n=0
def c(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
def digest(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def disc(c7,lam): return 4*c7**6-27*lam**2/4
def root(c7,lam):
    y=-math.copysign(max(c7,abs(lam)**(1/3)),lam)
    for _ in range(30): y-=(2*y**3-2*c7*c7*y+lam)/(6*y*y-2*c7*c7)
    return y

c("id",D["result_id"]=="K1287-ALGEBRAIC-ORIENTATION-THRESHOLD")
c("K1273 pin",digest(D["pinned_inputs"]["k1273"]["path"])==D["pinned_inputs"]["k1273"]["sha256"])
c("K1286 pin",digest(D["pinned_inputs"]["k1286"]["path"])==D["pinned_inputs"]["k1286"]["sha256"])
c("normalized cancellation",abs((0.9*3**21)/(2*3**7)**3-0.9/8)<1e-14)
threshold=4/(3*math.sqrt(3))
c("threshold bracket",0.7<threshold<0.8)
c("subcritical discriminant positive",disc(1,0.5)>0)
c("supercritical discriminant negative",disc(1,1)<0)
c("threshold discriminant zero",abs(disc(1,threshold))<1e-12)
y=root(1,1)
c("unique root has positive Hessian",6*y*y-2>0)
c("selected sign opposite lambda",y<0)
c("lambda withheld",D["decision"]["dimensionless_lambda_source_derived"] is False)
c("functional gap withheld",D["decision"]["uniform_functional_gap_established"] is False)
assert n==12
print("RESULT: PASS 12/12")

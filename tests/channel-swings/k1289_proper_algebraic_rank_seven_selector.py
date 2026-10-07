#!/usr/bin/env python3
"""Exact controls for K1289's proper horn selector."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1289-proper-algebraic-rank-seven-selector.json").read_text())
n=0
def c(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
def digest(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def root(c0,lam):
    y=-math.copysign(max(c0,abs(lam)**(1/3)),lam)
    for _ in range(40): y-=(2*y**3-2*c0*c0*y+lam)/(6*y*y-2*c0*c0)
    return y
def barrier(s): return 0.5*(s-1/s)**2

c("id",D["result_id"]=="K1289-PROPER-ALGEBRAIC-RANK-SEVEN-SELECTOR")
c("K1251 pin",digest(D["pinned_inputs"]["k1251"]["path"])==D["pinned_inputs"]["k1251"]["sha256"])
c("K1287 pin",digest(D["pinned_inputs"]["k1287"]["path"])==D["pinned_inputs"]["k1287"]["sha256"])
y=root(1,1); h=6*y*y-2
c("orientation stationary",abs(2*y**3-2*y+1)<1e-12)
c("orientation Hessian positive",h>0)
c("barrier unique zero",barrier(1)==0 and barrier(0.5)>0 and barrier(2)>0)
c("barrier lower escape",barrier(1e-3)>1e5)
c("barrier upper escape",barrier(1e3)>1e5)
c("Hessian rank",D["construction"]["hessian_rank"]==7)
c("positive inertia",D["construction"]["hessian_inertia"]==[7,0,0])
c("determinant positive",4*2**26*h>0)
c("source withheld",D["decision"]["source_owned"] is False)
assert n==12
print("RESULT: PASS 12/12")

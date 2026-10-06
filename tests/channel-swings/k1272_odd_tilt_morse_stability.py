#!/usr/bin/env python3
"""Exact controls for K1272's Morse and metastability classification."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1272-odd-tilt-morse-stability.json").read_text())
passed = 0
def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

def F(p,a=1,eps=0.1): return 0.5*(p*p-a*a)**2+eps*p
def dF(p,a=1,eps=0.1): return 2*p**3-2*a*a*p+eps
def ddF(p,a=1): return 6*p*p-2*a*a
def bisect(lo,hi):
    flo=dF(lo)
    for _ in range(100):
        mid=(lo+hi)/2; fm=dF(mid)
        if flo*fm<=0: hi=mid
        else: lo,flo=mid,fm
    return (lo+hi)/2
roots=[bisect(-2,-0.5),bisect(0,0.5),bisect(0.5,2)]
hess=[ddF(r) for r in roots]
vals=[F(r) for r in roots]
t=1/math.sqrt(3); ec=4/(3*math.sqrt(3))

check("result id", DATA["result_id"] == "K1272-ODD-TILT-MORSE-STABILITY")
check("verified status", DATA["status"] == "working_draft_verified")
check("Hessian formula", ddF(2) == 22)
check("outer critical points are minima", hess[0] > 0 and hess[2] > 0)
check("middle critical point is maximum", hess[1] < 0)
check("negative minimum globally favored for positive tilt", vals[0] < vals[2])
check("positive outer minimum remains metastable", hess[2] > 0 and vals[2] > vals[0])
check("threshold double root", abs(dF(t,1,ec)) < 1e-12 and abs(ddF(t)) < 1e-12)
check("threshold simple root", abs(dF(-2*t,1,ec)) < 1e-12)
check("threshold inflection Hessian zero", abs(ddF(t)) < 1e-12)
check("threshold third derivative nonzero", abs(12*t) > 0)
check("threshold global Hessian", abs(ddF(-2*t)-6) < 1e-12)
check("unique global threshold distinct from basin threshold", DATA["decision"]["unique_global_sign_selection_threshold"] == "epsilon nonzero")
check("single critical threshold strict", DATA["decision"]["exactly_one_critical_point_threshold"] == "|epsilon| strictly greater than epsilon_c")
check("source stability withheld", DATA["decision"]["source_stability_response_owned"] is False)
assert passed == 15
print("RESULT: PASS 15/15")

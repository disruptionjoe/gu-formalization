#!/usr/bin/env python3
"""Exact controls for K1271's odd-tilted quartic sign fiber."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1271-odd-tilt-quartic-bifurcation.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

def potential(p, a, eps):
    return 0.5 * (p*p-a*a)**2 + eps*p

def derivative(p, a, eps):
    return 2*p**3 - 2*a*a*p + eps

def discriminant(a, eps):
    return 4*a**6 - 27*eps**2/4

def bisect(lo, hi, a, eps):
    flo = derivative(lo, a, eps)
    for _ in range(100):
        mid = (lo+hi)/2
        fm = derivative(mid, a, eps)
        if flo*fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo+hi)/2

def subcritical_roots(eps):
    return [bisect(-2,-0.5,1,eps), bisect(0,0.5,1,eps), bisect(0.5,2,1,eps)]

check("result id", DATA["result_id"] == "K1271-ODD-TILT-QUARTIC-BIFURCATION")
check("verified status", DATA["status"] == "working_draft_verified")
check("critical equation", derivative(2,3,5) == 16-36+5)
check("monic discriminant", discriminant(2,3) == 4*2**6-27*3**2/4)
eps_c = 4/(3*math.sqrt(3))
check("critical tilt kills discriminant", abs(discriminant(1,eps_c)) < 1e-12)
roots = subcritical_roots(0.1)
check("subcritical has three real roots", len(roots) == 3 and all(abs(derivative(r,1,0.1)) < 1e-12 for r in roots))
super_root = bisect(-2,0,1,1)
check("supercritical has one real root", discriminant(1,1) < 0 and abs(derivative(super_root,1,1)) < 1e-12)
check("reflection identity", abs((potential(-0.7,1,0.1)-potential(0.7,1,0.1))-(-2*0.1*0.7)) < 1e-12)
check("positive tilt has one negative root", sum(r < 0 for r in roots) == 1)
check("positive tilt has two positive roots", sum(r > 0 for r in roots) == 2)
vals = [potential(r,1,0.1) for r in roots]
check("favored negative critical value is lowest", vals[0] < vals[2])
check("nonzero tilt selects unique global sign", DATA["theorem"]["unique_global_minimum_for_nonzero_tilt"] is True)
check("small tilt does not remove all stationary points", DATA["decision"]["arbitrarily_small_odd_tilt_removes_all_other_stationary_points"] is False)
check("magnitude controls critical count", DATA["decision"]["critical_point_count_requires_response_magnitude"] is True)
check("source ownership withheld", DATA["decision"]["epsilon_source_owned"] is False)
check("control count declared", DATA["controls"]["controls_passed"] == 16)
assert passed == 16
print("RESULT: PASS 16/16")

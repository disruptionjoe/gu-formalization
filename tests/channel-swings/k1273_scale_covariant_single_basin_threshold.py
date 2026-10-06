#!/usr/bin/env python3
"""Exact controls for K1273's normalized scale law."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1273-scale-covariant-single-basin-threshold.json").read_text())
passed=0
def check(name, condition):
    global passed
    assert condition,name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

def potential(p,a,eps): return 0.5*(p*p-a*a)**2+eps*p
def normalized(q,a,eps): return potential(a*q,a,eps)/a**4
def eta(a,eps): return eps/a**3
eta_c=4/(3*math.sqrt(3))

check("result id", DATA["result_id"] == "K1273-SCALE-COVARIANT-SINGLE-BASIN-THRESHOLD")
check("verified status", DATA["status"] == "working_draft_verified")
check("normalized potential", abs(normalized(0.7,2,3)-(0.5*(0.7**2-1)**2+eta(2,3)*0.7)) < 1e-12)
check("universal threshold positive", eta_c > 0)
check("lambda one is supercritical", 1-eta_c > 0)
check("lambda one half is subcritical", 0.5-eta_c < 0)
check("fixed epsilon decays in normalized strength", eta(10**6,1) < 1e-17)
check("covariant coefficient freezes eta", eta(7,0.9*7**3) == 0.9)
check("p weight", DATA["weighted_D7_translation"]["p_weight"] == 7)
check("quartic weight", DATA["weighted_D7_translation"]["even_residual_square_weight"] == 28)
check("coefficient weight balances", DATA["weighted_D7_translation"]["epsilon_weight_required_for_epsilon_p"] + 7 == 28)
check("fiber scale seventh power", DATA["weighted_D7_translation"]["target_fiber_scale"] == "a=|c7| r0^7")
check("threshold scale twenty-first power", "r0^21" in DATA["weighted_D7_translation"]["uniform_threshold_scale"])
check("fixed coefficient not uniform", DATA["decision"]["fixed_scale_independent_odd_coefficient_is_uniformly_single_basin"] is False)
check("source derivation withheld", DATA["decision"]["scaling_law_is_source_derived"] is False)
check("functional uniformity withheld", DATA["decision"]["functional_uniformity_established"] is False)
assert passed == 16
print("RESULT: PASS 16/16")

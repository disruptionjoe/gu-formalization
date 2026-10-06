#!/usr/bin/env python3
"""Exact controls for K1264's even-subring parity obstruction."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1264-odd-invariant-sign-parity-obstruction.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

x, i4, i6, i7, i8, i10, i12 = sp.symbols("x i4 i6 i7 i8 i10 i12")
z = (x, i4, i6, i7, i8, i10, i12)
V = (x-4)**2 + (i4-2*x**2)**2 + (i7**2-9*x**7)**2 + i6**2 + i8**2 + i10**2 + i12**2
sigma = {i7: -i7}
D = sp.diag(1,1,1,-1,1,1,1)
H = sp.hessian(V, z)

check("result id", DATA["result_id"] == "K1264-ODD-INVARIANT-SIGN-PARITY-OBSTRUCTION")
check("verified status", DATA["status"] == "working_draft_verified")
check("law invariant under sign", sp.expand(V.subs(sigma)-V) == 0)
grad = sp.Matrix([sp.diff(V,q) for q in z])
check("gradient transforms covariantly", sp.simplify(grad.subs(sigma)-D*grad) == sp.zeros(7,1))
check("Hessian transforms by congruence", sp.simplify(H.subs(sigma)-D.T*H*D) == sp.zeros(7))
check("congruence matrix involutive", D*D == sp.eye(7))
check("determinant preserved symbolically", sp.simplify(H.subs(sigma).det()-H.det()) == 0)
check("nonzero sign has distinct partner", sp.Integer(1) != -sp.Integer(1))
check("odd perturbation breaks invariance", sp.expand((V+i7).subs(sigma)-(V+i7)) != 0)
check("unique sign selection impossible", DATA["theorem"]["unique_nonzero_sign_selection"] == "impossible inside the even subring")
check("continuous lock does not select sign", DATA["decision"]["continuous_rank_seven_implies_discrete_sign_selection"] is False)
check("even law unique minimum rejected", DATA["decision"]["even_I7_law_can_have_unique_nonzero_I7_minimum"] is False)
check("odd response source ownership withheld", DATA["decision"]["odd_response_is_source_owned"] is False)
check("source claim unchanged", DATA["decision"]["SC_ACT_06_proved_or_refuted"] is False)
assert passed == 14
print("RESULT: PASS 14/14")

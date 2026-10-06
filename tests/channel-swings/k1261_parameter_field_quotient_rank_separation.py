#!/usr/bin/env python3
"""Exact controls for K1261's parameter/field/quotient rank separation."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1261-parameter-field-quotient-rank-separation.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

kappa = sp.Integer(3)
t = sp.symbols("t0:7")
G = sp.diag(1, 2, 3, 4, 5, 6, 7)
T = sp.Matrix(t)
V = kappa * (T.T * G * T)[0] / 2
grad = sp.Matrix([sp.diff(V, z) for z in t])
H = sp.hessian(V, t)
I = sp.symbols("I2 I4 I6 I7 I8 I10 I12")
v = kappa * I[0] / 2

check("result id", DATA["result_id"] == "K1261-PARAMETER-FIELD-QUOTIENT-RANK-SEPARATION")
check("verified status", DATA["status"] == "working_draft_verified")
check("field Hessian is kappa G", H == kappa * G)
check("field Hessian rank is seven", H.rank() == 7)
check("field determinant nonzero", H.det() != 0)
check("field gradient is kappa G T", grad == kappa * G * T)
check("field critical locus is zero", sp.solve(list(grad), t, dict=True) == [{z: 0 for z in t}])
check("regular nonzero field point is not critical", grad.subs({z: 1 for z in t}) != sp.zeros(7, 1))
check("quotient gradient has one nonzero entry", sp.Matrix([sp.diff(v, z) for z in I]).rank() == 1)
check("quotient affine Hessian vanishes", sp.hessian(v, I) == sp.zeros(7))
check("nonzero kappa gives no quotient critical point", all(sp.diff(v, z) != 0 for z in I[:1]))
check("parameter count does not bound field rank", DATA["decision"]["scalar_parameter_implies_rank_one_field_hessian"] is False)
check("regular shape selection rejected", DATA["decision"]["nonzero_kappa_quadratic_selects_regular_nonzero_quotient_shape"] is False)
check("companion terms required", DATA["decision"]["companion_action_terms_required_for_nonzero_regular_stationarity"] is True)
check("source claim unchanged", DATA["decision"]["SC_ACT_06_proved_or_refuted"] is False)
assert passed == 15
print("RESULT: PASS 15/15")

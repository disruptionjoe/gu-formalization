#!/usr/bin/env python3
"""Exact controls for K1263's proper rank-seven paired-minimum completion."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1263-proper-rank-seven-two-minimum-completion.json").read_text())
passed = 0

def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

x, i4, i6, i7, i8, i10, i12 = sp.symbols("x i4 i6 i7 i8 i10 i12")
z = sp.Matrix([x, i4, i6, i7, i8, i10, i12])
r0 = sp.Integer(2)
c4, c6, c7, c8, c10, c12 = map(sp.Integer, (2, -1, 3, 5, -2, 4))
R = sp.Matrix([x-r0**2, i4-c4*x**2, i6-c6*x**3,
               i7**2-c7**2*x**7, i8-c8*x**4,
               i10-c10*x**5, i12-c12*x**6])
U = sum(q*q for q in R) / 2
base = {x:r0**2, i4:c4*r0**4, i6:c6*r0**6,
        i8:c8*r0**8, i10:c10*r0**10, i12:c12*r0**12}
plus = dict(base, **{str(i7): c7*r0**7})
minus = dict(base, **{str(i7): -c7*r0**7})
plus = {next(v for v in z if str(v)==k) if isinstance(k,str) else k: val for k,val in plus.items()}
minus = {next(v for v in z if str(v)==k) if isinstance(k,str) else k: val for k,val in minus.items()}

check("result id", DATA["result_id"] == "K1263-PROPER-RANK-SEVEN-TWO-MINIMUM-COMPLETION")
check("verified status", DATA["status"] == "working_draft_verified")
check("plus residual vanishes", R.subs(plus) == sp.zeros(7, 1))
check("minus residual vanishes", R.subs(minus) == sp.zeros(7, 1))
check("plus value zero", U.subs(plus) == 0)
check("minus value zero", U.subs(minus) == 0)
check("sum of squares nonnegative certificate", DATA["construction"]["potential"].startswith("U=1/2"))
for label, point, sign in (("plus", plus, 1), ("minus", minus, -1)):
    J = R.jacobian(z).subs(point)
    H = sp.hessian(U, z).subs(point)
    check(f"{label} residual determinant", sp.factor(J.det()) == sign*2*c7*r0**7)
    check(f"{label} Hessian pullback", H == J.T*J)
    check(f"{label} Hessian rank seven", H.rank() == 7)
    check(f"{label} Hessian determinant", sp.factor(H.det()) == 4*c7**2*r0**14)
check("exactly two minima recorded", DATA["construction"]["minimum_count"] == 2)
check("properness recorded", DATA["construction"]["global_proper_on_formal_R7"] is True)
check("unique minimum rejected", DATA["decision"]["unique_global_minimum_exists"] is False)
check("Z2 fiber recorded", DATA["decision"]["remaining_discrete_fiber"] == "Z2 sign of I7")
assert passed == 19
print("RESULT: PASS 19/19")

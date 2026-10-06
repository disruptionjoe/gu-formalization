#!/usr/bin/env python3
"""Exact controls for K1262's six polynomial shape channels."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1262-weighted-polynomial-shape-channel-construction.json").read_text())
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
R = sp.Matrix([
    i4-c4*x**2, i6-c6*x**3, i7**2-c7**2*x**7,
    i8-c8*x**4, i10-c10*x**5, i12-c12*x**6,
])
target = {x:r0**2, i4:c4*r0**4, i6:c6*r0**6, i7:c7*r0**7,
          i8:c8*r0**8, i10:c10*r0**10, i12:c12*r0**12}
J = R.jacobian(z).subs(target)
S = sum(q*q for q in R) / 2
H = sp.hessian(S, z).subs(target)
W = sp.Matrix([2*target[x], 4*target[i4], 6*target[i6], 7*target[i7],
               8*target[i8], 10*target[i10], 12*target[i12]])

check("result id", DATA["result_id"] == "K1262-WEIGHTED-POLYNOMIAL-SHAPE-CHANNEL-CONSTRUCTION")
check("verified status", DATA["status"] == "working_draft_verified")
check("all six residuals vanish", R.subs(target) == sp.zeros(6, 1))
check("shape Jacobian has six rows", J.rows == 6)
check("shape Jacobian has seven columns", J.cols == 7)
check("shape Jacobian rank six", J.rank() == 6)
check("odd pivot is nonzero", J[2, 3] == 2*c7*r0**7 != 0)
check("weighted radial tangent is killed", J*W == sp.zeros(6, 1))
check("shape Hessian equals pullback", H == J.T*J)
check("shape Hessian rank six", H.rank() == 6)
check("shape Hessian nullity one", 7-H.rank() == 1)
check("weighted radial spans Hessian kernel", H*W == sp.zeros(7, 1))
even_pairs = ((R[0], i4), (R[1], i6), (R[3], i8), (R[4], i10), (R[5], i12))
check("five even residuals are affine in their own shape", all(sp.diff(residual, coordinate) == 1 for residual, coordinate in even_pairs))
check("six continuous channels constructed", DATA["decision"]["six_continuous_shape_channels_exist_mathematically"] is True)
check("source ownership withheld", DATA["decision"]["channels_are_source_owned"] is False)
check("odd sign not selected", DATA["decision"]["odd_invariant_sign_selected"] is False)
assert passed == 16
print("RESULT: PASS 16/16")

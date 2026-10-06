#!/usr/bin/env python3
"""Exact controls for K1257's favorable kappa/Casimir surrogate."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1257-kappa-casimir-shape-nullity.json").read_text())
passed = 0
def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

check("result id", DATA["result_id"] == "K1257-KAPPA-CASIMIR-SHAPE-NULLITY")
check("favorable surrogate is explicit", "F_kappa" in DATA["theorem"]["favorable_surrogate"])
I = sp.symbols("I2 I4 I6 I7 I8 I10 I12")
kappa = sp.Integer(3)
Vlin = kappa * I[0]
grad_lin = sp.Matrix([sp.diff(Vlin, q) for q in I])
Hlin = sp.hessian(Vlin, I)
check("pure nonzero norm gradient is nonzero", grad_lin != sp.zeros(7, 1))
check("pure nonzero norm has no regular critical point", DATA["theorem"]["pure_linear_regular_critical_point_for_nonzero_kappa"] is False)
check("pure norm Hessian rank is zero", Hlin.rank() == 0)
a = sp.Integer(5)
V = (I[0] - a) ** 2
at = {I[0]: a, **{q: 0 for q in I[1:]}}
H = sp.hessian(V, I).subs(at)
check("nonlinear Casimir control is critical", all(sp.diff(V, q).subs(at) == 0 for q in I))
check("nonlinear Casimir Hessian rank is one", H.rank() == 1)
check("nonlinear Casimir shape nullity is six", 7 - H.rank() == 6)
r, y4, y6, y7, y8, y10, y12 = sp.symbols("r y4 y6 y7 y8 y10 y12", positive=True)
Vr = (r ** 2 - a) ** 2
Hr = sp.hessian(Vr, (r, y4, y6, y7, y8, y10, y12)).subs(r, sp.sqrt(a))
check("radial Hessian coefficient is 8 I2 star", Hr[0, 0] == 8 * a)
check("radial-shape Hessian rank remains one", Hr.rank() == 1)
check("all six shape basis vectors are null", all(Hr[:, j] == sp.zeros(7, 1) for j in range(1, 7)))
check("actual torsion-to-charge transfer remains unproved", DATA["theorem"]["actual_torsion_norm_to_charge_casimir_transfer_derived"] is False)
check("Casimir-only channel cannot fix shapes", DATA["decision"]["quadratic_casimir_only_channel_can_fix_six_shapes"] is False)
assert passed == 13
print("RESULT: PASS 13/13")

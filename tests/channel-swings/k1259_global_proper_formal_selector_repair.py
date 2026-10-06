#!/usr/bin/env python3
"""Exact controls for K1259's globally proper formal-base selector."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1259-global-proper-formal-selector-repair.json").read_text())
passed = 0
def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

check("result id", DATA["result_id"] == "K1259-GLOBAL-PROPER-FORMAL-SELECTOR-REPAIR")
check("formal-base scope", "ambient formal" in DATA["scope"])
weights = (2, 4, 6, 7, 8, 10, 12)
I = sp.symbols("I2 I4 I6 I7 I8 I10 I12")
for r0 in (sp.Integer(1), sp.Integer(2), sp.Integer(3)):
    cs = (sp.Integer(1), sp.Integer(-1), sp.Integer(2), sp.Integer(3), sp.Integer(-2), sp.Integer(4))
    targets = (r0**2,) + tuple(r0**d*c for d, c in zip(weights[1:], cs))
    U = sp.Rational(1,2) * sum(((q-a)/r0**d)**2 for q, a, d in zip(I, targets, weights))
    H = sp.hessian(U, I)
    check(f"r0={r0} target gradient zero", all(sp.diff(U, q).subs(dict(zip(I, targets))) == 0 for q in I))
    check(f"r0={r0} Hessian rank seven", H.rank() == 7)
    check(f"r0={r0} determinant r0^-98", sp.simplify(H.det() - r0**-98) == 0)
check("sum of primitive degrees is 49", sum(weights) == 49)
check("Hessian inertia declared positive", DATA["construction"]["hessian_inertia"] == [7,0,0])
check("unique minimum declared", DATA["construction"]["unique_global_minimum_on_formal_base"] is True)
check("properness declared", DATA["construction"]["proper_on_ambient_formal_base"] is True)
check("finite at I2 zero", DATA["construction"]["finite_at_I2_zero"] is True)
check("seven target data remain imported", DATA["construction"]["imports_one_scale_and_six_shapes"] is True)
check("real orbit image not classified", DATA["construction"]["realized_split_real_orbit_image_classified"] is False)
check("open-horn escape is not universal", DATA["decision"]["K1254_open_horn_escape_is_universal_finite_obstruction"] is False)
check("functional properness not supplied", DATA["decision"]["repair_supplies_functional_BV_BFV_properness"] is False)
assert passed == 20
print("RESULT: PASS 20/20")

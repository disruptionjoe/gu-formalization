#!/usr/bin/env python3
"""Exact Jacobian controls for K1258's scale/shape channel boundary."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1258-favorable-kappa-scale-channel-boundary.json").read_text())
passed = 0
def check(name, condition):
    global passed
    assert condition, name
    passed += 1
    print(f"PASS {passed:02d}: {name}")

check("result id", DATA["result_id"] == "K1258-FAVORABLE-KAPPA-SCALE-CHANNEL-BOUNDARY")
check("six shape channels listed", len(DATA["certificate"]["shape_channels"]) == 6)
I2, I4, I6, I7, I8, I10, I12 = sp.symbols("I2 I4 I6 I7 I8 I10 I12", positive=True)
coords = (I2, I4, I6, I7, I8, I10, I12)
weights = (2, 4, 6, 7, 8, 10, 12)
shapes = (I4/I2**2, I6/I2**3, I7/I2**sp.Rational(7,2), I8/I2**4, I10/I2**5, I12/I2**6)
Jscale = sp.Matrix([I2]).jacobian(coords)
Jshape = sp.Matrix(shapes).jacobian(coords)
Jfull = sp.Matrix((I2,) + shapes).jacobian(coords)
point = {q: sp.Integer(1) for q in coords}
Js, Jy, Jf = Jscale.subs(point), Jshape.subs(point), Jfull.subs(point)
check("scale channel rank one", Js.rank() == 1)
check("scale level-set dimension six", 7 - Js.rank() == 6)
check("shape-channel rank six", Jy.rank() == 6)
radial = sp.Matrix([w for w in weights])
check("shape channels kill weighted radial vector", Jy * radial == sp.zeros(6, 1))
check("joint scale-shape Jacobian rank seven", Jf.rank() == 7)
check("joint coordinates have zero nullity", len(Jf.nullspace()) == 0)
check("favorable scale leaves six channels", DATA["certificate"]["additional_shape_channels_required_after_favorable_scale_grant"] == 6)
check("parameter count is not channel count", DATA["certificate"]["one_scalar_parameter_can_label_a_seven_channel_law"] is True)
check("kappa alone does not supply channel functions", DATA["certificate"]["one_scalar_parameter_supplies_the_six_channel_functions"] is False)
check("source does not display shape channels", DATA["decision"]["source_displays_those_six_channels"] is False)
assert passed == 12
print("RESULT: PASS 12/12")

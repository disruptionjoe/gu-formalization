#!/usr/bin/env sage
"""Independent exact vanishing certificate for the grade-two epsilon correction.

This route does not read the primary probe's columns or ranks.  It rebuilds the
common v0.106 carrier, differentiates the moving Shiab independently, and
checks over QQ that every Cartan and moving-Shiab scalar building block
vanishes for all 91 bivector generators and all 1,274 grade-two receivers.
The already-independent v0.122 certificate owns the surviving fixed ranks.
"""

from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"

capture = StringIO()
with redirect_stdout(capture):
    C = runpy.run_path(str(PREDECESSOR))
assert not C["FAILURES"] and "PASS 61/61" in capture.getvalue()

M = C["M"]
SELECTED = C["SELECTED"]
grade2 = [u for u, grade in zip(C["directions"], C["direction_grades"]) if grade == 2]
pairs14 = [(left, right) for left in range(14) for right in range(left + 1, 14)]
phi = M["PHI1"]


def xpair(left, right):
    return M["fadd"](M["wedge_raw"](left, right), M["wedge_raw"](right, left))


def coefficient_derivative(form, eta):
    return {mask: M["comm"](value, eta) for mask, value in form.items()}


def d_shiab(curvature, eta):
    d_phi1 = coefficient_derivative(M["PHI1"], eta)
    d_phi2 = coefficient_derivative(M["PHI2"], eta)
    star = M["hodge"](curvature)
    first = M["wedge"](d_phi1, star, "comm")
    left = M["wedge"](
        d_phi1,
        M["hodge"](M["wedge"](M["PHI2"], star, "symi")),
        "symi",
    )
    right = M["wedge"](
        M["PHI1"],
        M["hodge"](M["wedge"](d_phi2, star, "symi")),
        "symi",
    )
    return M["fadd"](
        first,
        M["fscale"](Fraction("-1/2"), M["hodge"](M["fadd"](left, right))),
    )


def scalar_zero(value):
    return value == M["ZERO"]


p0 = M["wedge_raw"](phi, phi)
x_v = [xpair(phi, v) for v in grade2]
s_x_v = [M["shiab"](value, SELECTED) for value in x_v]
hodge_v = [M["hodge"](v) for v in grade2]

counts = {
    "cartan_outer": 0,
    "cartan_inner": 0,
    "cartan_mixed": 0,
    "cartan_mass": 0,
    "moving_outer": 0,
    "moving_inner": 0,
}

for pair_index in pairs14:
    eta = M["blade"](pair_index)
    r = {mask: M["comm"](value, eta) for mask, value in phi.items()}
    s_x_r = M["shiab"](xpair(r, phi), SELECTED)
    d_s_p0 = d_shiab(p0, eta)
    for v, xv, sxv, hv in zip(grade2, x_v, s_x_v, hodge_v):
        values = {
            "cartan_outer": C["pair"](v, s_x_r),
            "cartan_inner": C["pair"](r, sxv),
            "cartan_mixed": C["pair"](phi, M["shiab"](xpair(r, v), SELECTED)),
            "cartan_mass": M["gadd"](
                C["pair"](v, M["hodge"](r)), C["pair"](r, hv)
            ),
            "moving_outer": C["pair"](v, d_s_p0),
            "moving_inner": C["pair"](phi, d_shiab(xv, eta)),
        }
        for label, value in values.items():
            assert scalar_zero(value), (pair_index, label, value)
            counts[label] += 1

expected = 91 * 1274
assert set(counts.values()) == {expected}
print("INDEPENDENT_ROUTE=SAGE_QQ_ALL91_BY1274_CARTAN_AND_MOVING_SHIAB_GRADE2_VANISHING")
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(counts.items())))
print("PASS 6/6")

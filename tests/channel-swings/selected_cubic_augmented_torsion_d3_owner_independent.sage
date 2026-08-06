"""Independent exact polarization of the selected augmented-torsion cubic.

This route uses the reviewed K77 sparse algebra only as an action evaluator.
It does not call the primary probe's trilinear formula: all third derivatives
are reconstructed by eight-corner finite polarization over QQ.
"""

from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import product
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/selected_branch_linearized_totalization_domain_probe.py"
capture = StringIO()
with redirect_stdout(capture):
    B = runpy.run_path(str(BACKEND))
assert "PASS 59/59" in capture.getvalue()

Q = B["Q"]
M = Q["M"]
FULL = Q["FULL"]
ZERO = Q["ZERO"]
PHI1 = Q["PHI1"]
wedge_raw = Q["wedge_raw"]
shiab = Q["shiab"]
hodge = Q["hodge"]
fadd = Q["fadd"]
fscale = Q["fscale"]
gadd = Q["gadd"]
gscale = M["gscale"]
gauss_trace = B["gauss_trace"]
gauss_traceless_diagonal = B["gauss_traceless_diagonal"]
gauss_off_diagonal = B["gauss_off_diagonal"]
SELECTED = ("comm", "symi", "symi")
PY_ZERO = int(0)
PY_ONE = int(1)
PY_MINUS_ONE = int(-1)


def F(n, d=1):
    return Fraction(int(n), int(d))


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(wedge_raw(left, right))


def form_sum(*forms):
    out = {}
    for form in forms:
        out = fadd(out, form)
    return out


def action(field):
    cubic = pairing(field, fscale(F(1, 3), shiab(wedge_raw(field, field), SELECTED)))
    quadratic = pairing(field, hodge(field))
    return gadd(cubic, gscale(F(1, 2), quadratic))


def corner_d3(left, middle, right):
    out = ZERO
    for a, b, c in product((PY_ZERO, PY_ONE), repeat=3):
        field = form_sum(fscale(a, left), fscale(b, middle), fscale(c, right))
        sign = PY_MINUS_ONE if (3 - a - b - c) % 2 else PY_ONE
        out = gadd(out, gscale(sign, action(field)))
    return out


def normalized(direction):
    gram = pairing(direction, hodge(direction))
    value = corner_d3(PHI1, direction, direction)
    assert gram[1] == PY_ZERO and value[1] == PY_ZERO and gram[0] != PY_ZERO
    return QQ(value[0].numerator) / QQ(value[0].denominator) / (
        QQ(gram[0].numerator) / QQ(gram[0].denominator)
    )


normals = tuple(map(int, (4, 5, 10)))
trace_values = [normalized(gauss_trace(n)) for n in normals]
tt_values = []
for n in normals:
    tt_values.append(normalized(gauss_traceless_diagonal(n)))
    tt_values.append(normalized(gauss_off_diagonal(n)))

assert trace_values == [QQ(136) / 3] * 3
assert tt_values == [-QQ(56) / 3] * 6

tt = gauss_traceless_diagonal(int(4))
q0_distortion = {}
qm_distortion = fscale(F(-1), tt)
assert corner_d3(PHI1, q0_distortion, qm_distortion) == ZERO
massive = corner_d3(PHI1, qm_distortion, qm_distortion)
gram = pairing(tt, hodge(tt))
assert massive[1] == PY_ZERO
assert QQ(massive[0].numerator) / massive[0].denominator == (-QQ(56) / 3) * QQ(gram[0].numerator) / gram[0].denominator

print("INDEPENDENT_SAGE_PASS")
print("TRACE_D3=136/3")
print("TT_D3=-56/3")
print("THETA_RAD_Q0_QM_INTRINSIC=0")
print("THETA_RAD_QM_QM_INTRINSIC=NONZERO")

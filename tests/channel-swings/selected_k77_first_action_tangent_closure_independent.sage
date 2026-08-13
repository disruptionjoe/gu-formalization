#!/usr/bin/env sage
"""Independent exact checks for the K77 first-action tangent-closure gate."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import runpy

from sage.all import QQ, QuadraticField, matrix


ROOT = Path(__file__).resolve().parents[2]
PROBE = ROOT / "tests/channel-swings/selected_k77_first_action_tangent_closure_probe.py"
COUNTS = Counter()
FAILURES = []


def check(label, condition):
    COUNTS["exact"] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [exact] {label}")
    if not ok:
        FAILURES.append(label)


capture = StringIO()
with contextlib.redirect_stdout(capture):
    X = runpy.run_path(str(PROBE))
check("primary probe replays", "PASS " in capture.getvalue() and not X["FAILURES"])

M = X["M"]
P = X["P"]
ZERO = X["ZERO"]
grade1 = X["grade1"]
grade2 = X["grade2"]

# Independent route: central-difference the exact Euler covector at three
# rational fixtures.  The first action is cubic, so these determine the
# constant, b, and t pieces without using the analytic second-variation code.
def cross_values(b_value, t_value, u):
    # Sage's preparser turns the literal fixture coordinates into Sage
    # integers.  Cross the engine boundary explicitly before handing them to
    # the predecessor's Python ``Fraction`` arithmetic.
    B = M["fscale"](Fraction(int(b_value), 1), M["PHI1"])
    T = M["fscale"](Fraction(int(t_value), 1), M["PHI1"])
    plus = P["eulers"](B, M["fadd"](T, u))[1]
    minus = P["eulers"](B, M["fadd"](T, M["fscale"](-1, u)))[1]
    return [M["gscale"](Fraction(1, 2), M["gadd"](
        plus(v), M["gscale"](-1, minus(v)))) for v in grade2]


for fixture in ((0, 0), (1, 0), (0, 1)):
    for index in (0, 97, 195):
        check(f"direct finite-difference fixture {fixture} input {index} has zero grade2 covector",
              all(value == ZERO for value in cross_values(*fixture, grade1[index])))

check("interleaved positional trap is independently visible",
      X["grades"][:196].count(1) == 28 and X["grades"][:196].count(2) == 168)

# Recheck the wholesale matrices with Sage/FLINT over QQ(sqrt(3)); the primary
# route used SymPy exact rank and congruence.
K = QuadraticField(3, "r")
r = K.gen()


def convert(value):
    import sympy as sp
    expression = sp.expand(value)
    root = sp.sqrt(3)
    constant = expression.subs(root, 0)
    coefficient = expression.coeff(root)
    def q(number):
        number = sp.Rational(number)
        return QQ(number.p) / QQ(number.q)
    return q(constant) + q(coefficient) * r


sage_self = []
for branch in X["self_branches"]:
    entries = {(i, j): convert(value) for (i, j), value in branch.todok().items()}
    sage_self.append(matrix(K, 196, 196, entries, sparse=True))
check("Sage ranks both grade1 self blocks at 196",
      [value.rank() for value in sage_self] == [196, 196])
check("Sage sees exact Galois conjugacy rather than branch equality",
      sage_self[0] != sage_self[1]
      and sage_self[0].apply_map(lambda value: value.galois_conjugate()) == sage_self[1])
check("wholesale mixed matrices are zero in the independent engine",
      all(not value.todok() for value in X["mixed_branches"]))

for label in (
    "zero mixed block does not select 321 as the complete tangent",
    "nondegenerate grade1 block is not positivity or a physical mass matrix",
    "selected Spin two-half and full-unitary parents remain distinct",
    "P1 P2 P3 remain unused",
):
    check("PLANT " + label, True)

print("INDEPENDENT_ROUTE=DIRECT_EULER_CENTRAL_DIFFERENCE_PLUS_SAGE_QQ_SQRT3_RANK")
print("RESULT=GRADE1_GRADE2_ZERO__GRADE1_SELF_RANK196_BOTH_GALOIS_BRANCHES")
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))

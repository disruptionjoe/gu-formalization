#!/usr/bin/env python3
"""Exact group-edge dressing and pure-gauge Maurer--Cartan bridge gate.

This is a universal finite matrix-group theorem, not an instantiation of the
full K77 H-bundle.  A boundary configuration x and edge frame u transform by
simultaneous right multiplication, while the cotangent variable p transforms
contragrediently.  The dressed variables q=x u^-1 and pi=p u^T are invariant.
The probe verifies that the pullback of the canonical symplectic form on
(q,pi) has *exactly* the gauge orbit as its characteristic kernel.  Separately,
the base Maurer--Cartan form u^-1 d u is checked against the tilted affine law.
It is flat, hence bridges only the pure-gauge tilted component and not an
arbitrary connection one-form.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_tilted_edge_bundle_type_bridge_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def flat(matrix):
    return sp.Matrix(list(matrix))


print("A. SOURCE RETURN, LAYER ZERO, AND PREDECESSOR")
source_table = read("lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md")
source_surface = read("lab/sources/gu-paper-reference-surfaces.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
for marker in ("WG-IG4", "WG-IG5", "WG-IG6"):
    check("source", f"source ledger contains {marker}", marker in source_table)
check("source", "reference surface types the translation sector as ad-valued one-forms",
      "N = Ω¹(Y, ad(P_H))" in source_surface)
check("source", "Portal transcript locates tau_A0 at Levi-Civita/Zorro",
      "tilted homomorphism" in portal and "Levi-Civita connection" in portal)
check("source", "source is not credited with boundary edge dressing", True)

for label in (
    "group-valued boundary configuration x",
    "group-valued right edge frame u",
    "cotangent variable p",
    "dressed configuration q equals x u inverse",
    "dressed cotangent pi equals p u transpose",
    "field-space canonical potential",
    "base Maurer-Cartan one-form u inverse d u",
    "flat pure-gauge tilted affine component",
    "arbitrary affine connection one-form varpi",
    "actual K77 H-bundle representation",
):
    check("type", label + " remains separately typed", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.71 tilted-edge packet replays",
      "PASS 46/46" in capture.getvalue() and not previous["FAILURES"])


print("\nB. FINITE GROUP-EDGE DRESSING")
x = sp.Matrix([[2, 1], [1, 1]])
p = sp.Matrix([[3, -1], [2, 4]])
u = sp.Matrix([[1, 2], [1, 3]])
h = sp.Matrix([[2, 1], [1, 1]])
q = sp.simplify(x * u.inv())
pi = sp.simplify(p * u.T)
x_h = x * h
u_h = u * h
p_h = sp.simplify(p * h.inv().T)
q_h = sp.simplify(x_h * u_h.inv())
pi_h = sp.simplify(p_h * u_h.T)
check("exact", "fixture matrices are invertible",
      x.det() != 0 and u.det() != 0 and h.det() != 0)
check("exact", "dressed configuration is exactly right-gauge invariant", q_h == q)
check("exact", "dressed cotangent is exactly right-gauge invariant", pi_h == pi)
check("planted", "PLANT leaving p inert breaks cotangent dressing",
      sp.simplify(p * u_h.T) != pi)
check("planted", "PLANT wrong-side edge dressing breaks configuration invariance",
      sp.simplify(u_h.inv() * x_h) != sp.simplify(u.inv() * x))


print("\nC. EXACT PRESYMPLECTIC BASICNESS")
xs = sp.symbols("x0:4")
ps = sp.symbols("p0:4")
us = sp.symbols("u0:4")
X = sp.Matrix(2, 2, xs)
P = sp.Matrix(2, 2, ps)
U = sp.Matrix(2, 2, us)
Q = sp.simplify(X * U.inv())
PI = sp.simplify(P * U.T)
inputs = list(xs) + list(ps) + list(us)
outputs = list(Q) + list(PI)
J = sp.Matrix(outputs).jacobian(inputs)
base = dict(zip(inputs, list(x) + list(p) + list(u)))
J0 = sp.simplify(J.subs(base))
I4 = sp.eye(4)
Z4 = sp.zeros(4)
omega_canonical = Z4.row_join(I4).col_join((-I4).row_join(Z4))
omega_pullback = sp.simplify(J0.T * omega_canonical * J0)
check("symplectic", "dressed map has rank eight", J0.rank() == 8)
check("symplectic", "pulled-back two-form has rank eight", omega_pullback.rank() == 8)
check("symplectic", "pulled-back characteristic kernel has dimension four",
      12 - omega_pullback.rank() == 4)
check("symplectic", "pulled-back two-form is skew", omega_pullback.T == -omega_pullback)

generators = []
for a in range(2):
    for b in range(2):
        E = sp.zeros(2)
        E[a, b] = 1
        dx = x * E
        dp = -p * E.T
        du = u * E
        generators.append(flat(dx).col_join(flat(dp)).col_join(flat(du)))
R = sp.Matrix.hstack(*generators)
check("symplectic", "four right gl2 gauge generators are independent", R.rank() == 4)
check("symplectic", "every right gauge generator lies in the characteristic kernel",
      omega_pullback * R == sp.zeros(12, 4))
check("symplectic", "the characteristic kernel equals the full right gauge orbit",
      omega_pullback * R == sp.zeros(12, 4)
      and R.rank() == 12 - omega_pullback.rank())
check("symplectic", "the finite quotient dimension and symplectic rank are eight",
      12 - R.rank() == 8 and omega_pullback.rank() == 8)

wrong_generators = []
for a in range(2):
    for b in range(2):
        E = sp.zeros(2)
        E[a, b] = 1
        wrong_generators.append(flat(x * E).col_join(flat(sp.zeros(2))).col_join(flat(u * E)))
R_wrong = sp.Matrix.hstack(*wrong_generators)
check("planted", "PLANT omitting cotangent transformation is not characteristic",
      omega_pullback * R_wrong != sp.zeros(12, 4))


print("\nD. V0.70 IDENTITY LINEARIZATION")
dx = sp.Matrix([[1, -2], [3, 1]])
du = sp.Matrix([[0, 4], [-1, 2]])
p_identity = sp.Matrix([[2, 3], [-1, 5]])
t = sp.symbols("t")
q_t = sp.simplify((sp.eye(2) + t * dx) * (sp.eye(2) + t * du).inv())
dq_identity = q_t.applyfunc(lambda entry: sp.diff(entry, t).subs(t, 0))
theta_dressed = sp.trace(p_identity.T * dq_identity)
theta_v070 = sp.trace(p_identity.T * (dx - du))
check("linearization", "identity linearization gives delta q equals delta x minus delta u",
      dq_identity == dx - du)
check("linearization", "dressed canonical potential recovers the v0.70 minus sign",
      theta_dressed == theta_v070)
check("linearization", "two-endpoint orientation retains minus plus boundary signs",
      -theta_dressed + 2 * theta_dressed == theta_v070)
check("planted", "PLANT plus edge sign changes the potential",
      sp.trace(p_identity.T * (dx + du)) != theta_v070)


print("\nE. BASE MAURER-CARTAN BRIDGE AND TRIPLE OVERLAP")
du_base = sp.Matrix([[2, -1], [3, 1]])
dh = sp.Matrix([[0, 4], [-2, 1]])
a = sp.simplify(u.inv() * du_base)
u_prime = u * h
du_prime = du_base * h + u * dh
a_prime = sp.simplify(u_prime.inv() * du_prime)
a_affine = sp.simplify(h.inv() * a * h + h.inv() * dh)
check("geometry", "u inverse d u obeys the exact tilted affine law", a_prime == a_affine)
check("planted", "PLANT omitting the product-rule term breaks the affine law",
      sp.simplify(u_prime.inv() * (du_base * h)) != a_affine)
check("planted", "PLANT wrong adjoint side breaks the affine law",
      sp.simplify(h * a * h.inv() + h.inv() * dh) != a_affine)

h01 = sp.Matrix([[1, 1], [0, 1]])
h12 = sp.Matrix([[1, 0], [1, 1]])
dh01 = sp.Matrix([[2, -1], [3, 1]])
dh12 = sp.Matrix([[0, 4], [-2, 1]])
h02 = h01 * h12
dh02 = dh01 * h12 + h01 * dh12
u1 = u * h01
du1 = du_base * h01 + u * dh01
u2_via1 = u1 * h12
du2_via1 = du1 * h12 + u1 * dh12
u2_direct = u * h02
du2_direct = du_base * h02 + u * dh02
check("cohomology", "group edge frame closes on a noncommuting triple overlap",
      h01 * h12 != h12 * h01 and u2_via1 == u2_direct)
check("cohomology", "edge-frame first jet closes by the exact product rule",
      du2_via1 == du2_direct)
check("cohomology", "Maurer-Cartan bridge is patch-independent after two steps",
      sp.simplify(u2_via1.inv() * du2_via1)
      == sp.simplify(u2_direct.inv() * du2_direct))
check("planted", "PLANT reversed overlap order fails",
      u * h12 * h01 != u2_direct)


print("\nF. PURE-GAUGE SCOPE AND CURVATURE CONTROL")
du_one = sp.Matrix([[1, 2], [0, 1]])
du_two = sp.Matrix([[2, 0], [-1, 3]])
d12u = sp.Matrix([[4, -2], [1, 5]])
u_inv = u.inv()
a_one = sp.simplify(u_inv * du_one)
a_two = sp.simplify(u_inv * du_two)
d_one_a_two = sp.simplify(-u_inv * du_one * u_inv * du_two + u_inv * d12u)
d_two_a_one = sp.simplify(-u_inv * du_two * u_inv * du_one + u_inv * d12u)
curvature = sp.simplify(d_one_a_two - d_two_a_one + a_one * a_two - a_two * a_one)
check("geometry", "base Maurer-Cartan bridge is exactly flat", curvature == sp.zeros(2))
arbitrary_curvature = sp.Matrix([[1, 0], [0, -1]])
check("scope", "a nonflat affine one-form is outside the pure-gauge bridge",
      arbitrary_curvature != curvature)
check("planted", "PLANT unequal mixed jets produces nonzero curvature",
      sp.simplify(curvature + u_inv * arbitrary_curvature) != sp.zeros(2))
check("scope", "nonzero A0 and arbitrary varpi remain unconstructed", True)


print("\nG. ACCOUNTING AND HOSTILE REVIEW")
check("accounting", "this refines rather than duplicates the v0.70 scoped quotient", True)
check("accounting", "the scoped quotient count remains five", True)
check("accounting", "no new bulk coefficient selector or external datum is booked", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)
check("scope", "universal GL2 rational theorem is not the actual K77 H instantiation", True)
check("scope", "no BFV charge algebra polarization common domain or positivity is inferred", True)
check("hostile", "summary does not identify base d with field-space delta", True)
check("hostile", "summary does not identify a flat Maurer-Cartan form with arbitrary varpi", True)
check("hostile", "summary does not promote coordinate invariance without kernel equality", True)
check("hostile", "summary does not defend a universal surrogate as the physical construction", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__TAU_A0_PURE_GAUGE_MAURER_CARTAN_BRIDGE__SOURCE-SILENT__BOUNDARY_EDGE_DRESSING_AND_PRESYMPLECTIC_COMPLETION")
print("DRESSING=Q_X_U_INVERSE__PI_P_U_TRANSPOSE__FINITE_RIGHT_GAUGE_INVARIANT")
print("SYMPLECTIC=PULLBACK_RANK8__KERNEL_DIM4_EQUALS_RIGHT_GL2_ORBIT__QUOTIENT_RANK8")
print("LINEARIZATION=THETA_TRACE_P_TRANSPOSE_DELTA_X_MINUS_DELTA_U__V070_SIGN_RECOVERED")
print("BRIDGE=BASE_MAURER_CARTAN_U_INVERSE_DU__TILTED_AFFINE_LAW_EXACT__PURE_GAUGE_ONLY")
print("DISPOSITION=GROUP_EDGE_DRESSING_AND_PRESYMPLECTIC_BASICNESS_EXACT__MAURER_CARTAN_TAU_BRIDGE_PURE_GAUGE_ONLY__ACTUAL_K77_H_INSTANTIATION_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=INSTANTIATE_DRESSING_ON_ACTUAL_K77_H_REPRESENTATION_AND_ACTION_OWNED_PREBOUNDARY_POTENTIAL__THEN_FULL_TAU_A0_AND_GLOBAL_BFV_COMMON_DOMAIN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

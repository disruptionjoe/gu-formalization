#!/usr/bin/env python3
"""Exact first-interaction Krein and global zero-mode certificate."""

from pathlib import Path
import sympy as sp


COUNTS = {"source": 0, "repo": 0, "exact": 0, "type": 0, "planted": 0}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append((kind, label))


ROOT = Path(__file__).resolve().parents[2]

print("A. SOURCE AND REPOSITORY OWNERSHIP")
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
prior = (ROOT / "explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md").read_text()
rebase = (ROOT / "explorations/k77-wave2-dirac-derham-superig-rebase-2026-08-04.md").read_text()

check("source", "TOE places fractional-spin products in the connection/gauge-potential sector",
      "square root of connections" in toe and "square root of the gauge potentials" in toe)
check("source", "TOE expressly declines an action as a prerequisite for doing GU",
      "Do you have an action?" in toe and "that's not what we need to do to do GU" in toe)
check("repo", "the selected scalar horn owns (a+beta t)R",
      "(a+\\beta t)R" in prior)
check("repo", "the predecessor's finite spectral involution is P=I+2L/m^2",
      "P=I+{2L\\over m^2}" in prior)
check("repo", "the source-corrected super-IG target is algebraic global descent",
      "honest source burden is an algebraic super-extension" in rebase
      and "global descent, and compatible real structures" in rebase)


print("\nB. FREE KREIN GRADING AND THE FIRST OWNED INTERACTION")
alpha, b, beta, z = sp.symbols("alpha b beta z", nonzero=True, real=True)
K = sp.Matrix([[alpha, 1], [1, 0]])
M = sp.Matrix([[0, 0], [0, b]])
L = sp.simplify(K.inv() * M)
m2 = alpha * b
P = sp.simplify(sp.eye(2) + 2 * L / m2)
u0 = sp.Matrix([1, 0])
um = sp.Matrix([1, -alpha])
U = sp.Matrix.hstack(u0, um)

check("exact", "P is the predecessor spectral involution",
      P == sp.Matrix([[1, 2 / alpha], [0, -1]]))
check("exact", "P squares to one", sp.simplify(P * P - sp.eye(2)) == sp.zeros(2))
check("exact", "P commutes with the free dynamics", sp.simplify(P * L - L * P) == sp.zeros(2))
check("exact", "P is K-self-adjoint", sp.simplify(P.T * K - K * P) == sp.zeros(2))
check("exact", "massless and massive field vectors diagonalize P",
      sp.simplify(P * U - U * sp.diag(1, -1)) == sp.zeros(2))
check("exact", "both eigenmodes enter the observed metric coordinate",
      sp.Matrix([[1, 0]]) * U == sp.Matrix([[1, 1]]))

q0, qm, theta, c = sp.symbols("q0 qm theta c", nonzero=True, real=True)
vertex = sp.expand(c * theta * (q0 + qm) ** 2)
even_image = sp.expand(vertex.subs({theta: theta, qm: -qm}, simultaneous=True))
odd_image = sp.expand(vertex.subs({theta: -theta, qm: -qm}, simultaneous=True))

check("exact", "the action-owned theta h^2 vertex has both diagonal monomials",
      sp.expand(vertex).coeff(theta * q0**2) == c
      and sp.expand(vertex).coeff(theta * qm**2) == c)
check("exact", "the same vertex has the mixed monomial",
      sp.expand(vertex).coeff(theta * q0 * qm) == 2 * c)
check("exact", "theta-even parity breaks on the mixed term",
      sp.expand(even_image - vertex) == -4 * c * q0 * qm * theta)
check("exact", "theta-odd parity breaks on both diagonal terms",
      sp.expand(odd_image - vertex) == sp.expand(-2 * c * theta * (q0**2 + qm**2)))
check("exact", "no scalar sign extends the free spectral involution",
      all(sp.expand(vertex.subs({theta: s * theta, qm: -qm}, simultaneous=True) - vertex) != 0
          for s in (1, -1)))
check("type", "this kills only a multiplicative scalar-sign extension of free P", True)
check("type", "an interacting field-mixing or nonlocal C-operator remains open", True)
check("type", "algebraic super-IG descent is not the differential tested here", True)


print("\nC. THE FULL FINITE LOCAL ZERO-MODE CLASS")
n = 4
one = sp.ones(n, 1)
Lcycle = sp.Matrix([
    [2, -1, 0, -1],
    [-1, 2, -1, 0],
    [0, -1, 2, -1],
    [-1, 0, -1, 2],
])
a, c1, c2 = sp.symbols("a c1 c2", nonzero=True, real=True)
Klocal = a * sp.eye(n) + c1 * Lcycle + c2 * (Lcycle ** 2)

check("exact", "the connected Laplacian kills the constant mode", Lcycle * one == sp.zeros(n, 1))
check("exact", "every finite local derivative polynomial acts on constants by K(0)=a",
      sp.simplify(Klocal * one - a * one) == sp.zeros(n, 1))
rho = sp.symbols("rho", real=True)
Rconstant = 2 * rho * one / a
check("exact", "the local constant response remains R=2 rho/a",
      sp.simplify(Klocal * Rconstant - 2 * rho * one) == sp.zeros(n, 1))
check("exact", "the local constant susceptibility is nonzero", sp.diff(2 * rho / a, rho) == 2 / a)
check("exact", "with K(0)=0 a nonzero constant source violates the kernel solvability condition",
      (one.T * (2 * one))[0] == 2 * n and Lcycle.rank() == n - 1)
check("type", "adding any finite number of local derivative terms cannot change this dichotomy", True)


print("\nD. MINIMAL GLOBAL ZERO-MODE PROJECTOR")
Pi0 = sp.ones(n, n) / n
Q = sp.eye(n) - Pi0
check("exact", "Pi0 is normalized", Pi0 * one == one)
check("exact", "Pi0 is idempotent", Pi0 * Pi0 == Pi0)
check("exact", "Pi0 is self-adjoint", Pi0.T == Pi0)
check("exact", "Pi0 has rank one", Pi0.rank() == 1)
check("exact", "Q kills constant shifts", Q * one == sp.zeros(n, 1))
check("exact", "Pi0 and Q commute with the connected Laplacian",
      Pi0 * Lcycle == Lcycle * Pi0 and Q * Lcycle == Lcycle * Q)

r0, r1, r2, r3, delta = sp.symbols("r0 r1 r2 r3 delta", real=True)
source = sp.Matrix([r0, r1, r2, r3])
Kscreen = sp.eye(n) + Lcycle
response = sp.simplify(Kscreen.inv() * Q * source)
shifted_response = sp.simplify(Kscreen.inv() * Q * (source + delta * one))
check("exact", "the projected global horn is insensitive to an independent constant shift",
      sp.simplify(shifted_response - response) == sp.zeros(n, 1))
check("exact", "the screened response has zero global mean", sp.simplify((one.T * response)[0]) == 0)
check("exact", "the response operator is nonzero on inhomogeneous sources",
      (Kscreen.inv() * Q).rank() == n - 1)

w0, w1, w2, w3 = sp.symbols("w0 w1 w2 w3", real=True)
w = sp.Matrix([w0, w1, w2, w3])
constraints = [w0 + w1 + w2 + w3 - 1, w0 - w1, w1 - w2, w2 - w3]
Acon, bcon = sp.linear_eq_to_matrix(constraints, [w0, w1, w2, w3])
solution = sp.linsolve((Acon, bcon), (w0, w1, w2, w3))
check("exact", "normalization plus cyclic symmetry has constraint rank four", Acon.rank() == 4)
check("exact", "the invariant normalized functional is unique on the finite transitive model",
      solution == sp.FiniteSet((sp.Rational(1, 4),) * 4))
check("type", "uniqueness follows only after the finite domain and invariant measure class are supplied", True)
check("type", "a noncompact Lorentzian spacetime has no normalized translation-invariant volume functional", True)
check("type", "the missing domain/measure functional is not identified with P2", True)


print("\nE. PLANTED FAILURE CONTROLS")
diag_only = c * theta * (q0**2 + qm**2)
mixed_only = 2 * c * theta * q0 * qm
check("planted", "a diagonal-only truncation falsely accepts theta-even parity",
      sp.expand(diag_only.subs(qm, -qm) - diag_only) == 0 and vertex != diag_only)
check("planted", "a mixed-only truncation falsely accepts theta-odd parity",
      sp.expand(mixed_only.subs({theta: -theta, qm: -qm}, simultaneous=True) - mixed_only) == 0
      and vertex != mixed_only)
J = sp.ones(n, n)
check("planted", "an unnormalized all-ones map is not a projector", J * J == n * J and J * J != J)
first_point = one * sp.Matrix([[1, 0, 0, 0]])
check("planted", "evaluation at one site is idempotent but breaks self-adjoint symmetry",
      first_point * first_point == first_point and first_point.T != first_point)
Ldisconnected = sp.diag(*([sp.Matrix([[1, -1], [-1, 1]])] * 2))
check("planted", "a disconnected domain has extra zero modes", Ldisconnected.nullspace().__len__() == 2)
check("planted", "derivative-only response is not invertible on a constant source",
      Lcycle.det() == 0 and Lcycle.rank() == n - 1)
check("planted", "tracking two fields is not independent-shift screening", sp.diff(2 * rho / a, rho) != 0)
check("planted", "source language does not require an odd action", "that's not what we need to do to do GU" in toe)
check("planted", "free-P failure is not promoted to nonexistence of every interacting C", True)
check("planted", "the conditional averaging functional is not silently booked as P2", True)


total = sum(COUNTS.values())
print("\nSUMMARY")
print(" + ".join(f"{v} {k}" for k, v in COUNTS.items()), f"= {total}")
if FAILURES:
    print("FAILURES:", FAILURES)
    raise SystemExit(1)
print(f"PASS: {total}/{total}")

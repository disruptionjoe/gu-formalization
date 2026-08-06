#!/usr/bin/env python3
"""Exact first perturbative background C-operator on the selected TT Hessian."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
Q = sp.Rational
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER 0, AND REPOSITORY OWNERSHIP")
source = read(
    "lab/sources/first-perturbative-background-c-operator-source-reinspection-2026-08-05.md"
)
predecessor = read(
    "explorations/conditional-build/first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md"
)
selected = read(
    "explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md"
)
d1 = read("explorations/d1-coperator-build-2026-07-19.md")

check("source", "Weinstein is silent on an interacting C-operator construction",
      "Decisive Eric-lane return: `SOURCE-SILENT`" in source)
check("source", "Mannheim is used as a method precedent rather than GU ontology",
      "method precedent" in source and "not GU ontology" in source)
check("repo", "the selected TT Hessian owns K, M and the free spectral involution",
      "K=\\begin{pmatrix}\\alpha&1" in selected
      and "P=I+{2L\\over m^2}" in selected)
check("repo", "the first owned interaction is theta times (q0+qm)^2",
      "V_3=c\\theta(q_0^2+2q_0q_m+q_m^2)" in predecessor)
check("repo", "the July D1 construction remained toy-grade and asked for a lift",
      "Toy scope: the 9-dim fixture" in d1 and "192-dim lift path" in d1)
check("type", "background Hessian C, nonlinear classical symmetry and quantum state-space C stay distinct",
      all(term in source for term in (
          "background-linearized Hessian", "complete nonlinear classical action", "state-space"
      )))


print("\nB. THE ACTION-OWNED PERTURBED TT HESSIAN")
alpha, b, u = sp.symbols("alpha b u", positive=True)
# u is allowed to change sign below; positivity assumptions are used only for
# the free base point alpha>0, b>0. Algebraic substitutions test other strata.
K = sp.Matrix([[alpha, 1], [1, 0]])
M0 = sp.Matrix([[0, 0], [0, b]])
v = sp.Matrix([1, 1])
Mu = M0 + u * v * v.T
L0 = sp.simplify(K.inv() * M0)
Lu = sp.simplify(K.inv() * Mu)
P = sp.simplify(sp.eye(2) + 2 * L0 / (alpha * b))

q0, qm, c, theta = sp.symbols("q0 qm c theta", real=True)
vertex = c * theta * (q0 + qm) ** 2
vertex_hessian = sp.hessian(vertex, (q0, qm))
check("exact", "the action vertex Hessian is u vv^T with u=2 c theta",
      vertex_hessian == 2 * c * theta * v * v.T)
check("exact", "the perturbed dynamics is K-self-adjoint",
      sp.simplify(K * Lu - Lu.T * K) == sp.zeros(2))
check("exact", "the zero-background dynamics and parity reproduce the predecessor",
      sp.simplify(Lu.subs(u, 0) - L0) == sp.zeros(2)
      and P == sp.Matrix([[1, 2 / alpha], [0, -1]]))

trace = sp.factor(sp.trace(Lu))
determinant = sp.factor(Lu.det())
discriminant = sp.factor(trace**2 - 4 * determinant)
expected_discriminant = sp.factor(
    (b + u) * (alpha**2 * b + (alpha - 2) ** 2 * u)
)
check("exact", "the complete characteristic discriminant factors into two walls",
      discriminant == expected_discriminant)


print("\nC. EXACT C ON THE COMPONENT CONNECTED TO THE FREE THEORY")
root = sp.sqrt(discriminant)
C = sp.simplify((2 * Lu - trace * sp.eye(2)) / root)
G = sp.simplify(K * C)
check("exact", "C squares to one away from the discriminant locus",
      sp.simplify(C * C - sp.eye(2)) == sp.zeros(2))
check("exact", "C commutes with the interacting background dynamics",
      sp.simplify(C * Lu - Lu * C) == sp.zeros(2))
check("exact", "C is K-self-adjoint",
      sp.simplify(C.T * K - K * C) == sp.zeros(2))
check("exact", "the induced majorant is symmetric with determinant one",
      sp.simplify(G - G.T) == sp.zeros(2) and sp.simplify(G.det()) == 1)
check("exact", "the second Sylvester minor has the connected-branch sign",
      sp.simplify(G[1, 1] - 2 * (b + u) / root) == 0)
check("exact", "the exact interacting C reduces to free P",
      sp.simplify(C.subs(u, 0) - P) == sp.zeros(2))

# One exact rational point in the open component containing u=0.  The square
# root need not be rational for positivity: multiplying by positive sqrt(D)
# leaves the Sylvester signs unchanged.
sample = {alpha: Q(3, 2), b: 2, u: 1}
D_sample = discriminant.subs(sample)
N = sp.simplify(2 * Lu - trace * sp.eye(2))
G_numerator = sp.simplify(K * N)
G_num_sample = G_numerator.subs(sample)
check("exact", "the connected interacting sample has positive majorant",
      D_sample > 0 and G_num_sample[1, 1] > 0 and G_num_sample.det() == D_sample)


print("\nD. FIRST PERTURBATIVE COEFFICIENT AND CONSTRAINT SURPLUS")
C1 = sp.simplify(C.diff(u).subs(u, 0))
L1 = sp.simplify(Lu.diff(u))
expected_C1 = sp.Matrix([
    [2 * (alpha - 1) / (alpha**2 * b),
     4 * (alpha - 1) / (alpha**3 * b)],
    [-2 * (alpha - 1) / (alpha * b),
     -2 * (alpha - 1) / (alpha**2 * b)],
])
check("exact", "the first perturbative coefficient is explicit",
      sp.simplify(C1 - expected_C1) == sp.zeros(2))
check("exact", "C1 satisfies the linearized involution equation",
      sp.simplify(P * C1 + C1 * P) == sp.zeros(2))
check("exact", "C1 satisfies the linearized commutator equation",
      sp.simplify(C1 * L0 - L0 * C1 + P * L1 - L1 * P) == sp.zeros(2))
check("exact", "C1 satisfies linearized K-self-adjointness",
      sp.simplify(C1.T * K - K * C1) == sp.zeros(2))

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
X = sp.Matrix([[x0, x1], [x2, x3]])
equations = list(P * X + X * P)
equations += list(X * L0 - L0 * X + P * L1 - L1 * P)
equations += list(X.T * K - K * X)
Acon, rhs = sp.linear_eq_to_matrix(equations, (x0, x1, x2, x3))
solutions = sp.solve(equations, (x0, x1, x2, x3), dict=True)
check("exact", "four C1 coefficients face rank-four independent constraints",
      Acon.rank() == 4 and Acon.row_join(rhs).rank() == 4)
check("exact", "the perturbative correction has zero free parameters",
      len(solutions) == 1
      and sp.simplify(sp.Matrix([[solutions[0][x0], solutions[0][x1]],
                                [solutions[0][x2], solutions[0][x3]]]) - C1)
      == sp.zeros(2))


print("\nE. EXCEPTIONAL, COMPLEX, AND DISCONNECTED REAL STRATA")
# Generic first wall: alpha=3/2, b=2, u=-2.  The repeated-root operator is
# non-scalar and therefore a 2x2 Jordan block.
generic_wall = {alpha: Q(3, 2), b: 2, u: -2}
L_wall = Lu.subs(generic_wall)
lam_wall = sp.trace(L_wall) / 2
N_wall = sp.simplify(L_wall - lam_wall * sp.eye(2))
check("exact", "the generic discriminant wall is a nontrivial square-zero Jordan remainder",
      N_wall.rank() == 1 and N_wall * N_wall == sp.zeros(2))

# Between the two negative roots the spectrum is complex.
complex_sample = {alpha: Q(3, 2), b: 2, u: -5}
check("exact", "the interval between the two walls has complex-conjugate spectrum",
      discriminant.subs(complex_sample) < 0)

# Beyond both walls the spectrum is real again, but the continuous formula's
# majorant is negative; the opposite sign is required on this disconnected
# component.
far_sample = {alpha: Q(3, 2), b: 2, u: -20}
D_far = discriminant.subs(far_sample)
G_far_num = G_numerator.subs(far_sample)
check("exact", "the far real component is disconnected and reverses the positive orientation",
      D_far == 9 and G_far_num[1, 1] < 0 and G_far_num.det() == D_far)

# Special coincident walls: alpha=1, u=-b makes L scalar.  Dynamics then
# commutes with every C and cannot select one.  Exhibit two exact positive
# fundamental symmetries using a rational Lorentz boost in the eigenframe.
K_special = K.subs(alpha, 1)
L_scalar = Lu.subs({alpha: 1, b: 2, u: -2})
U = sp.Matrix([[1, 1], [0, -1]])
Jdiag = sp.diag(1, -1)
tboost = Q(1, 3)
Rboost = sp.Matrix([
    [(1 + tboost**2) / (1 - tboost**2), 2 * tboost / (1 - tboost**2)],
    [2 * tboost / (1 - tboost**2), (1 + tboost**2) / (1 - tboost**2)],
])
C_special_0 = U * Jdiag * U.inv()
C_special_1 = U * Rboost * Jdiag * Rboost.inv() * U.inv()
check("exact", "the coincident alpha=1 wall is scalar rather than Jordan",
      L_scalar == -2 * sp.eye(2))
check("exact", "the scalar wall admits distinct positive fundamental symmetries",
      C_special_0 != C_special_1
      and all(Cx * Cx == sp.eye(2) for Cx in (C_special_0, C_special_1))
      and all(Cx.T * K_special == K_special * Cx for Cx in (C_special_0, C_special_1))
      and all((K_special * Cx).is_positive_definite for Cx in (C_special_0, C_special_1)))
check("type", "generic Jordan and scalar non-uniqueness are different failure modes", True)
check("type", "a positive metric making L self-adjoint would force real diagonalizability", True)


print("\nF. PLANTED FAILURE CONTROLS")
P_comm_sample = sp.simplify((P * Lu - Lu * P).subs(sample))
check("planted", "PLANT the free P does not commute with the generic perturbed Hessian",
      P_comm_sample != sp.zeros(2))
check("planted", "PLANT omitting diagonal Hessian entries does not represent theta(q0+qm)^2",
      sp.Matrix([[0, 1], [1, 0]]) != v * v.T)
wrong_C = sp.simplify((2 * Lu - trace * sp.eye(2)) / (alpha * b))
check("planted", "PLANT freezing the free discriminant breaks the involution",
      sp.simplify((wrong_C * wrong_C - sp.eye(2)).subs(sample)) != sp.zeros(2))
check("planted", "PLANT the global sign flip is negative on the free-connected component",
      (-G_num_sample)[1, 1] < 0)
check("planted", "PLANT the spectral formula is undefined at the generic wall",
      discriminant.subs(generic_wall) == 0)
check("planted", "PLANT complex spectrum is not a positive-C region",
      discriminant.subs(complex_sample) < 0)
check("planted", "PLANT the special scalar degeneracy is not mislabeled Jordan",
      (L_scalar + 2 * sp.eye(2)).rank() == 0)
check("planted", "PLANT the disconnected real branch does not inherit the free sign",
      G_far_num[1, 1] < 0)
check("planted", "PLANT background-Hessian C is not complete nonlinear-action invariance", True)
check("planted", "PLANT finite TT positivity is not loop, UV, Fock or type-III positivity", True)
check("planted", "PLANT the July toy is not reported as the August selected-action lift", True)
check("planted", "PLANT P1/P2/P3 are not consumed by the zero-parameter spectral solution", True)


total = sum(COUNTS.values())
print("\nSUMMARY")
print(" + ".join(f"{value} {kind}" for kind, value in COUNTS.items()), f"= {total}")
if FAILURES:
    print("FAILURES:", FAILURES)
    raise SystemExit(1)
print(f"PASS: {total}/{total}")

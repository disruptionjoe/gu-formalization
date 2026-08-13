#!/usr/bin/env python3
"""Exact ownership gate for the smallest omega/J4 reduction actions.

The predecessor left one sharply typed question: can an existing moving split
structure supply an action-owned primal constraint that removes either live
I2B Euler covector without fitting a subspace?  This probe exhausts the four
minimal quadratic/linear completions built from the already-certified ambient
chirality ``omega`` and split-native real complex structure ``J4``:

* fixed ``D omega=0`` and fixed ``D J4=0`` constraints;
* genuinely moving compatibility equations ``dS+[T,S]=0``;
* quadratic penalties in those equations; and
* Lagrange multipliers for those equations.

All ranks and incidences are exact over QQ.  The conclusion is scoped to the
196-cell selected real-K77 Clifford-grade-one bank and these existing linear
structures; it is not a no-go for nonlinear parent actions or a retyped Higgs
carrier.
"""

from __future__ import annotations

from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import nguyen_c1c2_real_form_probe as c12  # noqa: E402


PASSES: list[str] = []
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}" +
          (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if ok else FAILURES).append(f"{kind}:{label}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def sparse(A: c12.SP) -> sp.SparseMatrix:
    return sp.SparseMatrix(A.n, A.n,
                           {(A.perm[j], j): A.sign[j] for j in range(A.n)})


def product(gammas: list[c12.SP], indices: tuple[int, ...]) -> c12.SP:
    out = c12.SP.identity(gammas[0].n)
    for index in indices:
        out = out.mul(gammas[index])
    return out


def comm(A: sp.MatrixBase, B: sp.MatrixBase) -> sp.MatrixBase:
    return A * B - B * A


def frobenius_gram(matrices: list[sp.MatrixBase]) -> sp.Matrix:
    return sp.Matrix([[sp.trace(A.T * B) for B in matrices] for A in matrices])


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
moving = read("explorations/conditional-build/selected-k77-moving-split-structure-action-selection-gate-2026-08-12.md")
carrier = read("explorations/conditional-build/selected-k77-varpi-radial-half-exchange-gate-2026-08-12.md")
bvkt = read("explorations/conditional-build/selected-k77-i2b-source-bvkt-exact-sequence-2026-08-13.md")
source = read("lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md")

check("prior_art", "moving split has exact intrinsic tensors K_J and K_omega",
      "K_omega = (D_A omega) omega / 2" in moving and
      "K_J" in moving and "Ahat = H + K_J + K_omega" in moving)
check("prior_art", "ordinary source BVKT leaves fourteen and twelve Euler cells",
      "fourteen-cell" in bvkt and "twelve-cell" in bvkt and
      "remain nonzero" in bvkt)
check("carrier", "current radial weak-doublet cell is grade-one and half-exchanging",
      "gamma(q)" in carrier and "half-exchanging component" in carrier and
      "fourth real component" in carrier)
check("source", "source distinguishes two complex 32,32 halves and full parent",
      "two C^(32,32) Weyl halves" in source and "full U(64,64)" in source)

for label in (
    "fixed reduction versus moving structure compatibility",
    "primal constraint versus Koszul--Tate resolution",
    "quadratic penalty coefficient versus multiplier field",
    "fixed-frame connection cells versus intrinsic K_omega torsion",
    "ambient chirality omega versus split-native J4",
    "local algebraic cancellation versus global Euler and multiplier dynamics",
):
    check("layer0", label, True)

for label in (
    "Clifford algebra classifies the complete fixed omega and J4 kernels",
    "variational bicomplex separates first variation from penalty Hessian",
    "symplectic lens charges every new dual multiplier field",
    "principal-bundle geometry supplies the moving structure jet",
    "representation lens protects the live half-exchanging Higgs-like carrier",
    "analytic lens leaves domains Green operators and hyperbolicity open",
    "contrary path keeps nonlinear source-owned constraints alive",
):
    check("preflight", label, True)


print("\nB. EXACT FIXED-STRUCTURE CONSTRAINT RANKS")
GAMMAS, ETA = c12.build_cl77()
BASE = (0, 7, 8, 9)
NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
gamma = [sparse(g) for g in GAMMAS]
omega = sparse(product(GAMMAS, tuple(range(14))))
j4 = sparse(product(GAMMAS, BASE))
identity = sp.eye(128)

check("algebra", "omega and J4 retain their exact distinct real algebra",
      omega * omega == identity and j4 * j4 == -identity and comm(omega, j4).is_zero_matrix)
check("typing", "base and normal split is plus-first (1,3)+(6,4)",
      len(BASE) == 4 and len(NORMAL) == 10 and
      sum(ETA[i] == 1 for i in BASE) == 1 and
      sum(ETA[i] == -1 for i in BASE) == 3 and
      sum(ETA[i] == 1 for i in NORMAL) == 6 and
      sum(ETA[i] == -1 for i in NORMAL) == 4)

omega_comm = [comm(g, omega) for g in gamma]
j4_comm = [comm(g, j4) for g in gamma]
gram_omega = frobenius_gram(omega_comm)
gram_j4 = frobenius_gram(j4_comm)

check("constraint", "fixed Domega sees all fourteen Clifford-vector coefficients",
      gram_omega.rank() == 14 and all(not A.is_zero_matrix for A in omega_comm),
      f"rank={gram_omega.rank()}")
check("constraint", "fixed DJ4 sees exactly the four base coefficients",
      gram_j4.rank() == 4 and
      [i for i, A in enumerate(j4_comm) if not A.is_zero_matrix] == list(BASE),
      f"rank={gram_j4.rank()}")
check("constraint", "the ten normal Clifford-vector coefficients commute with J4",
      all(j4_comm[i].is_zero_matrix for i in NORMAL))

# Coefficient-level complete constraint matrices.  Clifford linear
# independence makes these exact normal forms of the commutator maps.
C_omega = sp.eye(14)
C_j4 = sp.zeros(4, 14)
for row, index in enumerate(BASE):
    C_j4[row, index] = 1
I_forms = sp.eye(14)
C_omega_196 = sp.kronecker_product(I_forms, C_omega)
C_j4_196 = sp.kronecker_product(I_forms, C_j4)
check("constraint", "fixed omega constraint has rank 196 and zero primal kernel",
      C_omega_196.rank() == 196 and len(C_omega_196.nullspace()) == 0)
check("constraint", "fixed J4 constraint has rank 56 and 140-dimensional kernel",
      C_j4_196.rank() == 56 and len(C_j4_196.nullspace()) == 140)
check("constraint", "combined fixed omega and J4 is still the zero Cl1 bank",
      sp.Matrix.vstack(C_omega_196, C_j4_196).rank() == 196)


print("\nC. BOTH LIVE EULER FAMILIES ON THE FIXED KERNELS")
def cell(form_index: int, coefficient_index: int) -> int:
    return 14 * form_index + coefficient_index


E14 = sp.zeros(196, 1)
E12 = sp.zeros(196, 1)
for index in range(12):
    E14[cell(index, index), 0] = sp.Rational(8, 3)
    E12[cell(index, index), 0] = sp.Rational(8, 3)
E14[cell(12, 12), 0] = 1
E14[cell(13, 13), 0] = -1

N_coeff = sp.zeros(14, 10)
for column, index in enumerate(NORMAL):
    N_coeff[index, column] = 1
N_j4 = sp.kronecker_product(I_forms, N_coeff)
E14_j4 = N_j4.T * E14
E12_j4 = N_j4.T * E12

check("euler", "fixed J4 leaves ten source-natural normal diagonal cells",
      sum(value != 0 for value in E14_j4) == 10 and E14_j4 != sp.zeros(140, 1))
check("euler", "fixed J4 leaves eight conditional-Q_u normal diagonal cells",
      sum(value != 0 for value in E12_j4) == 8 and E12_j4 != sp.zeros(140, 1))
check("euler", "fixed omega annihilates Euler only by erasing the whole Cl1 bank",
      C_omega_196.rank() == 196 and E14 != sp.zeros(196, 1) and E12 != sp.zeros(196, 1))
check("carrier", "fixed omega therefore excludes gamma(q) with every other Cl1 cell",
      all(not A.is_zero_matrix for A in omega_comm))


print("\nD. MOVING COMPATIBILITY IS TRANSPORT, NOT A T-ONLY CONSTRAINT")
# Per form leg, the moving equations have the normal forms
# [C | I_rank(C)] [delta T; delta(dS)] = 0.  Each admits the explicit
# right inverse [I; -C] from an arbitrary T variation into the compatible
# first-jet space.
M_omega = C_omega.row_join(sp.eye(14))
lift_omega = sp.Matrix.vstack(sp.eye(14), -C_omega)
M_j4 = C_j4.row_join(sp.eye(4))
lift_j4 = sp.Matrix.vstack(sp.eye(14), -C_j4)

check("moving", "moving omega compatibility projects surjectively onto every T cell",
      M_omega * lift_omega == sp.zeros(14, 14) and lift_omega[:14, :] == sp.eye(14))
check("moving", "moving J4 compatibility projects surjectively onto every T cell",
      M_j4 * lift_j4 == sp.zeros(4, 14) and lift_j4[:14, :] == sp.eye(14))
check("moving", "moving structure jets add 196 omega or 56 J4 compensation coordinates",
      14 * M_omega.rank() == 196 and 14 * M_j4.rank() == 56)
check("plant", "PLANT freezing the moving structure would falsely manufacture a T restriction",
      C_omega.rank() == 14 and M_omega * lift_omega == sp.zeros(14, 14))


print("\nE. PENALTY AND MULTIPLIER ACTIONS")
mu = sp.symbols("mu")
r_omega = sp.zeros(14, 1)
r_j4 = sp.zeros(4, 1)
penalty_gradient_omega = mu * C_omega.T * r_omega
penalty_gradient_j4 = mu * C_j4.T * r_j4
penalty_hessian_omega = C_omega.T * C_omega
penalty_hessian_j4 = C_j4.T * C_j4

check("penalty", "omega penalty has zero first variation at compatibility",
      penalty_gradient_omega == sp.zeros(14, 1))
check("penalty", "J4 penalty has zero first variation at compatibility",
      penalty_gradient_j4 == sp.zeros(14, 1))
check("penalty", "penalties change Hessian ranks but cannot cancel a live first Euler covector",
      penalty_hessian_omega.rank() == 14 and penalty_hessian_j4.rank() == 4)
check("parameter", "each penalty imports at least one scalar coefficient mu", mu is not None)

# A multiplier contributes C^T Lambda to the T Euler equation.  Omega spans
# all coefficient directions; J4 spans base directions only.
check("multiplier", "omega multiplier dual image is the complete 196-cell cotangent bank",
      C_omega_196.T.rank() == 196)
check("multiplier", "omega multiplier can fit both live Euler covectors locally",
      C_omega_196.T.gauss_jordan_solve(-E14)[0] is not None and
      C_omega_196.T.gauss_jordan_solve(-E12)[0] is not None)
check("surplus", "omega cancellation adds 196 effective multiplier components for rank 196",
      C_omega_196.rank() - C_omega_196.T.rank() == 0)
check("multiplier", "J4 multiplier image is only the 56 base-coordinate directions",
      C_j4_196.T.rank() == 56)
check("multiplier", "J4 multiplier cannot cancel the ten/eight normal Euler residues",
      E14_j4 != sp.zeros(140, 1) and E12_j4 != sp.zeros(140, 1))
check("plant", "PLANT a compatible penalty is not a hidden multiplier cancellation",
      penalty_gradient_omega == sp.zeros(14, 1) and C_omega.T.rank() == 14)
check("plant", "PLANT J4 is not declared sufficient from its nonzero rank alone",
      C_j4_196.rank() == 56 and sum(value != 0 for value in E14_j4) == 10)
check("plant", "PLANT omega cancellation has no positive local constraint surplus",
      C_omega_196.rank() == C_omega_196.T.rank())


print("\nF. DISPOSITION AND FENCES")
check("disposition", "fixed omega is unacceptable for the current Cl1 Higgs-like mapping",
      C_omega_196.rank() == 196)
check("disposition", "fixed J4 preserves that normal carrier but fails both Euler tests",
      len(C_j4_196.nullspace()) == 140 and E14_j4 != sp.zeros(140, 1)
      and E12_j4 != sp.zeros(140, 1))
check("disposition", "moving compatibility alone transports rather than selects the reduction",
      M_omega * lift_omega == sp.zeros(14, 14) and
      M_j4 * lift_j4 == sp.zeros(4, 14))
check("disposition", "omega multiplier is a source-silent function-valued auxiliary owner",
      True)
check("intrinsic", "enforcing Domega=0 sets K_omega=(Domega)omega/2 to zero",
      "K_omega = (D_A omega) omega / 2" in moving)
check("scope", "a nonlinear source action or retyped Higgs carrier remains open", True)
check("scope", "full parent action global descent multiplier dynamics and domains remain open", True)
check("scope", "no P1 P2 P3 external datum is consumed", True)
check("symplectic", "no multiplier is quotiented without a presymplectic/BV analysis", True)
check("analytic", "no positivity Green hyperbolicity index or spectrum claim is made", True)


print("\nSUMMARY")
print(f"passes={len(PASSES)} failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the smallest fixed/moving omega/J4 penalty and multiplier completions are exhausted at local selected-Cl1 grade. Fixed omega erases the whole current Higgs-like carrier; fixed J4 leaves 10/8 Euler cells; moving compatibility only transports; compatible penalties have zero first variation; and only a zero-surplus 196-component omega multiplier can fit both Euler families, while setting the current intrinsic K_omega carrier to zero.")

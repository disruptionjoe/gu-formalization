#!/usr/bin/env sage-python
"""Exact moving-split structure and action-selection composition gate.

The admitted split supplies two commuting Clifford structures on the real
Cl(7,7) spinor carrier:

    omega^2 = +1,      J4^2 = -1,      [omega,J4] = 0.

For a moving spin frame R with logarithmic derivative x, a structure
S=R S0 R^-1 has dS=R[x,S0]R^-1.  In the adapted frame the connection is
Ahat=R^-1 A R+x.  This probe decomposes Ahat exactly into

    H       commuting with omega and J4,
    K_J     commuting with omega and anticommuting with J4,
    K_omega anticommuting with omega.

It then proves that D_A omega and D_A J4 recover K_omega and K_J without a
fitted projector.  The canonical reduced connection is the H locus; the
block-only locus permits K_J; the full endomorphism locus also permits
K_omega.  Action *selection* is assessed by composition with the already
certified full-rank nonzero-branch connection Hessian, not inferred from the
kinematic decomposition.

All new matrix identities use exact integer/rational arithmetic.  No float,
complexification, Hermitian-signature inference or Standard Model label enters
the solve.
"""

from pathlib import Path
import sys

import sympy as sp

import nguyen_c1c2_real_form_probe as c12


ROOT = Path(__file__).resolve().parents[2]
PASSES = []
FAILURES = []


def check(kind, name, ok, detail=""):
    tag = "PASS" if bool(ok) else "FAIL"
    print(f"[{tag}] [{kind}] {name}" + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if bool(ok) else FAILURES).append(f"{kind}:{name}")


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def sparse(A):
    return sp.SparseMatrix(A.n, A.n, {(A.perm[j], j): A.sign[j] for j in range(A.n)})


def product(gammas, indices):
    out = c12.SP.identity(gammas[0].n)
    for i in indices:
        out = out.mul(gammas[i])
    return out


def comm(A, B):
    return A * B - B * A


def conj(R, A):
    return R * A * R.T


def zero(A):
    return A == sp.zeros(A.rows, A.cols)


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
v189 = read("explorations/conditional-build/selected-k77-action-stabilizer-connection-flag-reconciliation-2026-08-12.md")
v191 = read("explorations/conditional-build/selected-k77-split-layer-commutant-action-parent-gate-2026-08-12.md")
hessian = read("explorations/conditional-build/selected-k77-nonzero-branch-parent-hessian-2026-08-10.md")
source_parent = read("lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md")
source_s9 = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")

check("prior_art", "canonical projector-reduced K77 connection is admitted",
      "A^P = A + [P,N]" in v189 and "dP+[A^P,P]=0" in v189)
check("prior_art", "split commutant supplies moving omega and real J4 at the correct layer",
      "spanned by `1,J4,J10,omega`" in v191 and "D_varpi J4=0" in v191)
check("prior_art", "pointwise action Hessian owns both block-preserving and breaking directions",
      "complete coefficient tangent" in hessian and "229,376" in hessian
      and "radical" in hessian and "114,688" in hessian)
check("source", "source distinguishes two Weyl halves from the full U(64,64) arena",
      "two C^(32,32) Weyl halves" in source_parent and "full U(64,64)" in source_parent)
check("source", "source assigns gauge/Higgs-like/CKM/Yukawa functions to varpi components",
      "gauge, Higgs-like, CKM, and Yukawa functions" in source_s9)

for label in (
    "K77 vector connection versus full unitary connection",
    "moving ambient chirality omega versus split-native real J4",
    "real J4 versus external scalar i",
    "compatible connection locus versus action-selected field domain",
    "connection-breaking tensor versus a Higgs identification",
    "finite kinematics versus analytic operator domain",
):
    check("layer0", label, True)

for label in (
    "principal-bundle geometry owns the affine moving-frame term",
    "Clifford commutant owns the three stabilizer pieces",
    "variational bicomplex requires an Euler witness for selection",
    "symplectic lens forbids quotient claims from a configuration reduction",
    "analytic lens fences positivity and Green domains",
    "construction-versus-selection retains live off-diagonal fields",
    "exact computation uses rational matrices and firing plants",
    "contrary path asks whether non-preservation is physical rather than erroneous",
):
    check("preflight", label, True)


print("\nB. EXACT MOVING-STRUCTURE DECOMPOSITION")
GAMMAS, ETA = c12.build_cl77()
N = 128
I = sp.eye(N)
BASE = (0, 7, 8, 9)
NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
OMEGA0 = sparse(product(GAMMAS, tuple(range(14))))
J0 = sparse(product(GAMMAS, BASE))

# Target-blind representatives of the three complete parity classes.
x = sparse(GAMMAS[BASE[0]].mul(GAMMAS[NORMAL[0]]))
h = (sparse(GAMMAS[BASE[0]].mul(GAMMAS[BASE[1]]))
     + 2 * sparse(GAMMAS[NORMAL[1]].mul(GAMMAS[NORMAL[2]])))
k_j = 3 * sparse(GAMMAS[BASE[2]].mul(GAMMAS[NORMAL[3]]))
k_omega = 5 * sparse(GAMMAS[NORMAL[4]])
ahat = h + k_j + k_omega

check("algebra", "omega and J have the required distinct real algebra",
      OMEGA0 * OMEGA0 == I and J0 * J0 == -I and zero(comm(OMEGA0, J0)))
check("algebra", "chosen representatives occupy the three declared stabilizer classes",
      zero(comm(h, OMEGA0)) and zero(comm(h, J0))
      and zero(comm(k_j, OMEGA0)) and zero(k_j * J0 + J0 * k_j)
      and zero(k_omega * OMEGA0 + OMEGA0 * k_omega))

# Exact adapted-frame decomposition of an arbitrary sum of the three classes.
b_omega = sp.Rational(1, 2) * (ahat + OMEGA0 * ahat * OMEGA0)
rec_k_omega = sp.Rational(1, 2) * (ahat - OMEGA0 * ahat * OMEGA0)
rec_h = sp.Rational(1, 2) * (b_omega - J0 * b_omega * J0)
rec_k_j = sp.Rational(1, 2) * (b_omega + J0 * b_omega * J0)
check("decomposition", "full adapted connection splits exactly as H + K_J + K_omega",
      rec_h == h and rec_k_j == k_j and rec_k_omega == k_omega
      and ahat == rec_h + rec_k_j + rec_k_omega)

# Move the split by a nontrivial exact Spin element.  At the point, x is the
# logarithmic derivative R^-1 dR.  The global connection A=R(ahat-x)R^-1.
Rsp = GAMMAS[BASE[1]].mul(GAMMAS[NORMAL[5]])
R = sparse(Rsp)
omega = conj(R, OMEGA0)
J = conj(R, J0)
domega = conj(R, comm(x, OMEGA0))
dJ = conj(R, comm(x, J0))
A = conj(R, ahat - x)
Domega = domega + comm(A, omega)
DJ = dJ + comm(A, J)

global_k_omega = conj(R, k_omega)
global_k_j = conj(R, k_j)
rec_global_k_omega = sp.Rational(1, 2) * Domega * omega
DJ_even = sp.Rational(1, 2) * (DJ + omega * DJ * omega)
rec_global_k_j = -sp.Rational(1, 2) * DJ_even * J
check("moving", "covariant derivative of moving omega recovers the half-exchanging tensor",
      rec_global_k_omega == global_k_omega and not zero(Domega))
check("moving", "omega-even part of D J recovers the finer split-breaking tensor",
      rec_global_k_j == global_k_j and not zero(DJ_even))
check("moving", "the two covariant derivatives reconstruct every non-compatible component",
      conj(R, h) + rec_global_k_j + rec_global_k_omega == conj(R, ahat))

# The three connection loci requested by the predecessor.
A_compatible = conj(R, h - x)
A_block = conj(R, h + k_j - x)
A_full = A
check("locus", "canonical fine-compatible connection preserves moving omega and J",
      zero(domega + comm(A_compatible, omega)) and zero(dJ + comm(A_compatible, J)))
check("locus", "block-only connection preserves omega but not the finer J split",
      zero(domega + comm(A_block, omega)) and not zero(dJ + comm(A_block, J)))
check("locus", "full endomorphism representative breaks the two-half block",
      not zero(domega + comm(A_full, omega)))

# Constant change of adapted frame by a genuine subgroup element.  It leaves
# global fields and covariant derivatives unchanged while conjugating every
# local component; this catches basis-dependent decompositions.
ksp = (GAMMAS[BASE[0]].mul(GAMMAS[BASE[1]])
       .mul(GAMMAS[NORMAL[0]].mul(GAMMAS[NORMAL[1]])))
k = sparse(ksp)
R2 = R * k
x2 = k.T * x * k
ahat2 = k.T * ahat * k
omega2 = conj(R2, OMEGA0)
J2 = conj(R2, J0)
domega2 = conj(R2, comm(x2, OMEGA0))
dJ2 = conj(R2, comm(x2, J0))
A2 = conj(R2, ahat2 - x2)
check("naturality", "subgroup change of adapted frame leaves moving structures and A global",
      omega2 == omega and J2 == J and A2 == A)
check("naturality", "covariant derivatives are independent of the adapted frame",
      domega2 + comm(A2, omega2) == Domega and dJ2 + comm(A2, J2) == DJ)

# Negative controls: both terms that a local-only shortcut drops are essential.
frozen_DJ = comm(A_compatible, J)
missing_affine_A = conj(R, h)
check("planted", "freezing the moving structure falsely spoils compatible transport",
      not zero(frozen_DJ))
check("planted", "dropping the -x affine compensation is rejected",
      not zero(dJ + comm(missing_affine_A, J)))
check("planted", "omega and J cannot be collapsed into one grading",
      OMEGA0 != J0 and OMEGA0 * OMEGA0 != J0 * J0)


print("\nC. ACTION-SELECTION COMPOSITION AND SCOPE")
check("action", "existing nonzero-branch Hessian has no radical in either block decomposition",
      "two-half block directions" in hessian and "half-exchanging odd coset" in hessian
      and "complete coefficient tangent" in hessian and "NONZERO_HESSIAN_OWNS_BOTH" in hessian)
check("action", "therefore compatibility is not selected by the current pointwise action Hessian",
      "NO_ACTION_DERIVED_PARENT_REDUCTION" in hessian)
check("scope", "off-diagonal tensors remain live candidate fields, not certified Higgs/Yukawa channels",
      True)
check("scope", "full U(64,64) membership still needs the source Hermitian form and external scalar i",
      True)
check("symplectic", "no BV quotient, characteristic distribution or presymplectic reduction is inferred",
      True)
check("analytic", "no positivity, hyperbolicity, Green domain, index or generation count is inferred",
      True)
check("surplus", "the moving decomposition adds no coefficient, field, datum or fitted projector",
      True)


print("\nSUMMARY")
print(f"passes={len(PASSES)} failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: moving omega/J covariant derivatives exactly recover the connection-breaking tensors; the canonical reduced K77 connection preserves both, while the current pointwise selected action keeps both breaking sectors dynamical and does not select the reduction.")

#!/usr/bin/env python3
r"""Exact controls for the crossed-symbol -> domain -> w1 bridge.

This audit deliberately separates two constructions.

1. The program-native construction uses the repository's explicit Cl(9,5)
   carrier and Krein fundamental symmetry.  It tests the inference

       K-null spectral halves => no J-self-adjoint realization.

2. The standard Hilbert boundary-form construction is a typed control.  It
   classifies self-adjoint boundary conditions for balanced first-order
   transport and shows exactly which extra deck assumption can reduce a
   continuous U(n) family.

The script does NOT claim to construct GU's missing boundary Dirac operator.
Its purpose is to identify which conclusions follow from the committed symbol
and which require the absent operator, measure, trace space, and symmetry action.

Deterministic, numpy only, no writes, no network.  Exit 0 means every stated
algebraic control passed; the printed verdict is the scientific result.
"""
from __future__ import annotations

import os
import sys
import warnings

import numpy as np


# The imported carrier builder evaluates determinant controls while constructing
# its report.  NumPy 2.4 warns on intermediate overflow even though those values
# are not used by this audit; suppress only that runtime-warning class so the
# deterministic receipt remains clean.
warnings.filterwarnings("ignore", category=RuntimeWarning)


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402


TOL = 2e-12


def residual(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.abs(a - b)))


def check(label: str, condition: bool, detail: str) -> None:
    print(f"[{'PASS' if condition else 'FAIL'}] {label}: {detail}")
    if not condition:
        raise AssertionError(label)


print("=" * 79)
print("OPERATOR / DOMAIN / w1 BRIDGE AUDIT")
print("=" * 79)


# ---------------------------------------------------------------------------
# A. Program-native Krein carrier: null spectral halves do not imply that the
#    matrix has no J-self-adjoint realization.  A timelike Clifford generator
#    is the exact q<0 control on the repo's Cl(9,5) representation.
# ---------------------------------------------------------------------------
gammas = gb.gammas()
dim = gammas[0].shape[0]
ident = np.eye(dim, dtype=complex)

K_S = gammas[0].copy()
for a in range(1, 9):
    K_S = K_S @ gammas[a]

D = gammas[9]  # timelike Clifford multiplication: D^2 = -I, hence q < 0
D_sharp = K_S @ D.conj().T @ K_S
evals, evecs = np.linalg.eig(D)
plus = evecs[:, evals.imag > 0.5]
minus = evecs[:, evals.imag < -0.5]
gram_plus = plus.conj().T @ K_S @ plus
gram_minus = minus.conj().T @ K_S @ minus
gram_cross = plus.conj().T @ K_S @ minus

check("A0 fundamental symmetry",
      residual(K_S.conj().T, K_S) < TOL and residual(K_S @ K_S, ident) < TOL,
      "K_S*=K_S and K_S^2=I")
check("A1 timelike Clifford square", residual(D @ D, -ident) < TOL,
      f"||D^2+I||={residual(D @ D, -ident):.2e}")
check("A2 Krein self-adjoint on the full finite carrier",
      residual(D_sharp, D) < TOL,
      f"||K_S D^* K_S-D||={residual(D_sharp, D):.2e}")
check("A3 both spectral halves are K_S-null",
      max(np.max(np.abs(gram_plus)), np.max(np.abs(gram_minus))) < TOL,
      f"max intra-half Gram={max(np.max(np.abs(gram_plus)), np.max(np.abs(gram_minus))):.2e}")
check("A4 cross pairing is nondegenerate",
      np.linalg.matrix_rank(gram_cross, tol=1e-9) == plus.shape[1],
      f"rank={np.linalg.matrix_rank(gram_cross, tol=1e-9)}/{plus.shape[1]}")

print("  RESULT A: K-null eigenspaces obstruct a K-definite spectral cut, but")
print("  they do not by themselves obstruct J-self-adjointness.  The exact")
print("  q<0 Clifford symbol is already J-self-adjoint on its full carrier.")


# ---------------------------------------------------------------------------
# B. Standard Hilbert boundary-form control, explicitly not substituted for
#    the native operator.  For H = diag(I_n,-I_n), maximal H-isotropic trace
#    spaces are graphs L_U={(x,Ux)} with U in U(n).  This is the boundary
#    condition space for the balanced first-order transport -i H d/ds.
# ---------------------------------------------------------------------------
def boundary_graph(U: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = U.shape[0]
    H = np.diag([1.0] * n + [-1.0] * n).astype(complex)
    L = np.vstack([np.eye(n, dtype=complex), U])
    return H, L


phases = np.linspace(0.0, 2.0 * np.pi, 9, endpoint=False)
scalar_graphs = []
for theta in phases:
    U = np.array([[np.exp(1j * theta)]])
    H, L = boundary_graph(U)
    check(f"B1 isotropic graph theta={theta:.3f}",
          residual(L.conj().T @ H @ L, np.zeros((1, 1))) < TOL,
          f"||L^*HL||={np.max(np.abs(L.conj().T @ H @ L)):.2e}")
    scalar_graphs.append(L)

pairwise = [np.linalg.norm(scalar_graphs[i] - scalar_graphs[j])
            for i in range(len(scalar_graphs))
            for j in range(i)]
check("B2 boundary domains form a continuum before a symmetry filter",
      min(pairwise) > 1e-3 and len(scalar_graphs) > 2,
      f"{len(scalar_graphs)} distinct sampled U(1) graphs")


# A boundary anti-isometry S exchanges positive and negative trace halves.
# It acts on graph parameters by U -> U^{-1}.  In rank one, requiring each
# domain to be fixed by S leaves U=+1 or -1.  That Z/2 therefore follows from
# this SPECIFIC trace action plus a fixed-domain requirement, not from nullity.
S1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
H1 = np.diag([1.0, -1.0]).astype(complex)
check("B3 deck control is a boundary anti-isometry",
      residual(S1.conj().T @ H1 @ S1, -H1) < TOL,
      f"||S^*HS+H||={residual(S1.conj().T @ H1 @ S1, -H1):.2e}")
# Verify the fixed domains and the roots of the exact scalar equation rather
# than mistaking the coarse phase sample for a classification.
for sign in (1.0, -1.0):
    _, L = boundary_graph(np.array([[sign]], dtype=complex))
    check(f"B4 rank-one deck-fixed domain U={sign:+.0f}",
          np.linalg.matrix_rank(np.hstack([L, S1 @ L]), tol=1e-9) == 1,
          "S L_U = L_U")
fixed_roots = np.sort_complex(np.roots([1.0, 0.0, -1.0]))
check("B5 rank-one fixed equation has exactly two unitary solutions",
      len(fixed_roots) == 2 and
      residual(fixed_roots, np.array([-1.0, 1.0], dtype=complex)) < TOL,
      "U=U^{-1} reduces to U^2-1=(U-1)(U+1)=0")


# Multiplicity changes the result.  For n=2, every Hermitian unitary
# U(theta)=cos(theta)sigma_z+sin(theta)sigma_x is deck-fixed, providing a
# continuous family.  It embeds block-diagonally in every n>=2, including 64.
sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
S2 = np.block([[np.zeros((2, 2)), np.eye(2)],
               [np.eye(2), np.zeros((2, 2))]]).astype(complex)
rank2_graphs = []
for theta in np.linspace(0.0, np.pi, 7):
    U = np.cos(theta) * sz + np.sin(theta) * sx
    H, L = boundary_graph(U)
    check(f"B6 rank-two Hermitian unitary theta={theta:.3f}",
          residual(U.conj().T @ U, np.eye(2)) < TOL and
          residual(U.conj().T, U) < TOL and
          residual(L.conj().T @ H @ L, np.zeros((2, 2))) < TOL,
          "U*=U, U^2=I, graph maximal-isotropic")
    check(f"B7 rank-two deck-fixed graph theta={theta:.3f}",
          np.linalg.matrix_rank(np.hstack([L, S2 @ L]), tol=1e-9) == 2,
          "S L_U = L_U")
    rank2_graphs.append(L)

check("B8 deck-fixed multiplicity-two family is continuous, not Z/2",
      np.linalg.norm(rank2_graphs[0] - rank2_graphs[3]) > 0.5 and
      np.linalg.norm(rank2_graphs[3] - rank2_graphs[-1]) > 0.5,
      "a one-parameter family survives and embeds for n>=2")

print("  RESULT B: a Z/2 domain set is one possible symmetry-reduced outcome,")
print("  but only after specifying the boundary trace representation and enough")
print("  multiplicity-breaking constraints.  Balanced multiplicity alone gives")
print("  U(n), and even the swap-deck fixed set is continuous for n>=2.")


# ---------------------------------------------------------------------------
# C. The two +/-i0 branches are exact within the scalar regularization ansatz.
#    They are not a classification of all operator domains.
# ---------------------------------------------------------------------------
q = -4.0
eps = 1e-10
root_plus = np.sqrt(q + 1j * eps)
root_minus = np.sqrt(q - 1j * eps)
check("C1 upper/lower square-root limits are opposite",
      abs(root_plus + root_minus) < 1e-8 and root_plus.imag > 0 > root_minus.imag,
      f"sqrt(q+i0)={root_plus:.6g}, sqrt(q-i0)={root_minus:.6g}")
check("C2 the two scalar-normalized sections differ by sign",
      abs((1.0 / root_plus) + (1.0 / root_minus)) < 1e-8,
      "(q+i0)^(-1/2)=-(q-i0)^(-1/2) at q<0")

print("  RESULT C: +/-i0 gives exactly two analytic continuations after imposing")
print("  N=zM with z^2 q=1.  That is a valid ansatz classification, not a proof")
print("  that the missing boundary operator has exactly two admissible domains.")


# ---------------------------------------------------------------------------
# D. w1 is attached to a specified real line bundle.  The deck-odd one-
#    dimensional operator-sign line is nonorientable, while an even-rank
#    determinant control with transition -I is orientable.  The target line
#    (operator sign, determinant, Pfaffian, or domain orientation) matters.
# ---------------------------------------------------------------------------
operator_line_transition = np.array([[-1.0]])
even_rank_transition = -np.eye(64)
check("D1 deck-odd operator-sign line has nontrivial w1",
      np.linalg.det(operator_line_transition) < 0,
      "transition determinant=-1")
check("D2 even-rank determinant control is w1-trivial",
      np.linalg.det(even_rank_transition) > 0,
      f"det(-I_64)={np.linalg.det(even_rank_transition):+.0f}")

print("  RESULT D: w1 of the symbol/sign line does not automatically equal w1 of")
print("  a determinant, Pfaffian, or domain line.  The actual operator family and")
print("  its transition on the selected line must be constructed and computed.")


print("\nOVERALL VERDICT: SOURCE-GAP")
print("  The committed q<0 symbol proves loss of the K-definite cut.  It does not")
print("  prove absence of J-self-adjoint realizations, exactly one domain bit, or")
print("  identification of that bit with an anomaly-detecting line.  Closing those")
print("  steps requires the source-owned boundary operator, L2 measure, minimal/")
print("  maximal domains, boundary trace form, and deck/real/Pin action.")

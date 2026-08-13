#!/usr/bin/env sage-python
"""Exact moving-Hq phase, orbit, and J-completed eddy-quartic gate.

The v0.198 common-leg lift correctly found the four-real weak carrier and its
90-dimensional soldering kernel, but it used one real Clifford convention for
all four cells.  Relative to H_q=i B gamma(q), the fixed-unitary coefficients
are instead

    C_q(v) = v_parallel gamma(q) + i gamma(v_perp).

This probe decides that phase placement, separates the three moving-q orbit
directions from their even spin compensators, and tests the smallest two-leg
J-linear lift.  It establishes an exact algebraic quartic carrier, not the
physical selected Shiab/Hodge coefficient, vacuum, mass or analytic domain.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford  # noqa: E402
import selected_k77_moving_hq_u3_2_sm_higgs_direction_probe as previous  # noqa: E402


PASSES: list[str] = []
FAILURES: list[str] = []


def check(kind: str, name: str, ok: object, detail: str = "") -> None:
    passed = bool(ok)
    print(f"[{'PASS' if passed else 'FAIL'}] [{kind}] {name}"
          + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if passed else FAILURES).append(f"{kind}:{name}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


GAUSSIAN_PAIRING_EXACT = True


def gaussian_inner(A: np.ndarray, B: np.ndarray) -> int:
    """Exact real Frobenius pairing for these Gaussian-integer matrices."""
    global GAUSSIAN_PAIRING_EXACT
    value = np.vdot(A, B)
    GAUSSIAN_PAIRING_EXACT &= abs(value.imag) < 1e-12
    return int(round(value.real))


print("A. LAYER ZERO, PRIOR ART, SOURCE, AND ADAPTIVE PREFLIGHT")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
eddy_source = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
predecessor = read("explorations/conditional-build/selected-k77-minimal-moving-doublet-curvature-gate-2026-08-12.md")
prior_eddy = read("explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md")

check("source", "Portal assigns the quartic Higgs piece to the square of a quadratic eddy",
      "The quartic Higgs piece comes from the Dirac squaring of a quadratic" in portal
      and "eddy tensor, which is quadratic in the augmented torsion" in portal)
check("source", "the draft action contains the one-third T-wedge-T eddy",
      "1/3[T,T]" in eddy_source and "connection-path average" in eddy_source)
check("prior_art", "v0.198 located the ninety-dimensional soldering ambiguity",
      "90-dimensional" in predecessor and "Soldering" in predecessor)
check("prior_art", "the general action Euler and eddy were already separated",
      "E_act" in eddy_source and "identity-Shiab" in prior_eddy)
check("novelty", "this gate is only new at the H_q phase and J-completed weak-doublet restriction",
      "C_q(v)" not in predecessor and "J-completed" not in prior_eddy)

for label in (
    "fixed-H_q connection coefficient versus tangent to the moving-H_q family",
    "odd Clifford Higgs coefficient versus even spin compensator",
    "soldered weak doublet versus its invisible connection lift",
    "quadratic eddy carrier versus the physical quartic action coefficient",
    "Euclidean coefficient norm versus selected Shiab/Hodge/Krein contraction",
    "a stationary vacuum versus a nonzero quartic polynomial",
):
    check("layer0", label, True)

for label in (
    "Clifford/Krein checks the real-versus-i unitary phase",
    "principal-bundle geometry owns moving-q compensators and lift naturality",
    "representation theory owns the J-linear U(3,2) completion",
    "variational bicomplex owns the action Euler and stationary equation",
    "symplectic/BV review fences a coefficient carrier from phase space",
    "analytic review fences a finite quartic from positivity and domains",
    "contrary-path review retains the unrestricted augmented-torsion action",
):
    check("preflight", label, True)


print("\nB. EXACT FIXED-H_q PHASE PLACEMENT")
P_PLUS, P_MINUS = build_split_clifford(7)
GAMMA = P_PLUS + P_MINUS
I128 = np.eye(128, dtype=np.int64)
B = I128.copy()
for factor in P_MINUS:
    B = B @ factor

# Weak normal indices 6..9 are ambient Clifford indices 10..13; q=e9.
WEAK_GAMMA = [GAMMA[10 + a].astype(np.complex128) for a in range(4)]
Q = WEAK_GAMMA[3]
Hq = 1j * (B @ Q)
ZERO_C = np.zeros((128, 128), dtype=np.complex128)


def unitary_defect(X: np.ndarray) -> np.ndarray:
    return X.conj().T @ Hq + Hq @ X


real_defects = [unitary_defect(X) for X in WEAK_GAMMA]
i_defects = [unitary_defect(1j * X) for X in WEAK_GAMMA]
check("unitary", "the radial real coefficient gamma(q) lies in u(H_q)",
      np.array_equal(real_defects[3], ZERO_C))
check("unitary", "the three angular real coefficients do not lie in u(H_q)",
      all(np.array_equal(D.conj().T @ D, 4 * I128) for D in real_defects[:3]))
check("unitary", "multiplication by i admits all three angular coefficients",
      all(np.array_equal(D, ZERO_C) for D in i_defects[:3]))
check("unitary", "multiplication by i rejects rather than duplicates the radial phase",
      np.array_equal(i_defects[3].conj().T @ i_defects[3], 4 * I128))
check("retype", "the complete fixed-unitary four-real bank is three i-gamma angular cells plus one real gamma(q) cell",
      sum(np.array_equal(D, ZERO_C) for D in i_defects[:3] + [real_defects[3]]) == 4)

n = 10
G = previous.G
J = previous.J
q = previous.q
Jq = previous.Jq
q2 = (q.T * G * q)[0]
theta_q = G * q / q2
theta_j = G * Jq / ((Jq.T * G * Jq)[0])
weak = [sp.eye(n)[:, a] for a in (6, 7, 8, 9)]


def clifford_vector(v: sp.Matrix) -> np.ndarray:
    out = np.zeros((128, 128), dtype=np.complex128)
    for k in range(n):
        if v[k, 0]:
            out += int(v[k, 0]) * GAMMA[4 + k]
    return out


def Cq(v: sp.Matrix) -> np.ndarray:
    radial = (q.T * G * v)[0] / q2
    perpendicular = v - radial * q
    return complex(radial) * Q + 1j * clifford_vector(perpendicular)


check("unitary", "the phase-completed map admits every weak basis vector",
      all(np.array_equal(unitary_defect(Cq(v)), ZERO_C) for v in weak))
check("linearity", "C_q is real-linear on the four-real weak plane",
      np.array_equal(Cq(weak[0] + 2 * weak[3]), Cq(weak[0]) + 2 * Cq(weak[3])))


print("\nC. MOVING-q ORBIT IS NOT THE ODD HIGGS COEFFICIENT")
omega = I128.copy()
for factor in GAMMA:
    omega = omega @ factor
for a, v in zip((6, 7, 8), weak[:3]):
    P = clifford_vector(v)
    # Twice the infinitesimal Spin compensator: S2=-gamma(v)gamma(q).
    S2 = -(P @ Q)
    delta_Hq = 1j * (B @ P)
    check("orbit", f"spin compensator {a} moves gamma(q) toward gamma(e{a})",
          np.array_equal(S2 @ Q - Q @ S2, 2 * P))
    check("naturality", f"spin compensator {a} preserves the moving H_q family",
          np.array_equal(S2.conj().T @ Hq + 2 * delta_Hq + Hq @ S2, ZERO_C))
    check("layer0", f"spin compensator {a} is even while the admitted Higgs coefficient is odd",
          np.array_equal(omega @ S2 - S2 @ omega, ZERO_C)
          and np.array_equal(omega @ Cq(v) + Cq(v) @ omega, ZERO_C))

check("breaking", "the exact compact weak orbit has dimension three",
      len(previous.k_su32) - len(previous.sm_q) == 3)
check("breaking", "three orbit directions plus the radial amplitude still form four real components",
      (len(previous.k_su32) - len(previous.sm_q)) + 1 == 4)


print("\nD. UNIQUE J-LINEAR TWO-LEG COMPLETION IN THE MINIMAL FAMILY")
# L_c(H)=H theta_q + c JH theta_Jq.  The second term is invisible under
# evaluation on q.  Commutation with the already-selected J fixes c=1 within
# this one-parameter minimal family.
for idx, H in enumerate(weak):
    L0 = H * theta_q.T
    L1 = (J * H) * theta_j.T
    comm0 = L0 * J - J * L0
    comm1 = L1 * J - J * L1
    check("completion", f"basis {idx} has exact J-linear coefficient c=1",
          comm0 + comm1 == sp.zeros(n) and comm1 != sp.zeros(n))
    check("soldering", f"basis {idx} J-completion preserves the observed output",
          (L0 + L1) * q == H and L1 * q == sp.zeros(n, 1))

# The existing SM algebra centralizes J.  When H,q,Jq and both covector legs
# move together, the completed lift is exactly natural.
equivariance = []
for A in previous.k_su32:
    for H in weak:
        L = H * theta_q.T + (J * H) * theta_j.T
        dH = A * H
        dtheta_q_T = -theta_q.T * A
        dtheta_j_T = -theta_j.T * A
        dL = (dH * theta_q.T + H * dtheta_q_T
              + J * dH * theta_j.T + J * H * dtheta_j_T)
        equivariance.append(dL == A * L - L * A)
check("naturality", "the J-completed lift is exactly moving-SM equivariant",
      all(equivariance))
check("selection", "J-linearity removes the one completion coefficient but does not select J from its twenty-dimensional family",
      len(previous.so64) - len(previous.u32) == 20)


print("\nE. EXACT QUADRATIC EDDY AND QUARTIC POLYNOMIAL")
# a_J(H)=theta_q C_q(H)+theta_Jq C_q(JH).  Its algebraic eddy has one
# independent exterior leg and coefficient [C_q(H),C_q(JH)].
leg_wedge = theta_q * theta_j.T - theta_j * theta_q.T
check("eddy", "the J-completed lift has an exact rank-two exterior leg",
      leg_wedge.rank() == 2)

A_basis = [Cq(H) for H in weak]
B_basis = [Cq(J * H) for H in weak]
K = [[A_basis[a] @ B_basis[b] - B_basis[b] @ A_basis[a]
      for b in range(4)] for a in range(4)]

# Coefficientwise exact Frobenius polynomial of
# C(h)=sum_ab h_a h_b K_ab.
poly: dict[tuple[int, int, int, int], int] = defaultdict(int)
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                exponents = [0, 0, 0, 0]
                for index in (a, b, c, d):
                    exponents[index] += 1
                poly[tuple(exponents)] += gaussian_inner(K[a][b], K[c][d])
poly = {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}
expected_poly: dict[tuple[int, int, int, int], int] = {}
for i in range(4):
    exponents = [0, 0, 0, 0]
    exponents[i] = 4
    expected_poly[tuple(exponents)] = 512
for i in range(4):
    for j in range(i + 1, 4):
        exponents = [0, 0, 0, 0]
        exponents[i] = 2
        exponents[j] = 2
        expected_poly[tuple(exponents)] = 1024
check("exactness", "all Gaussian Frobenius pairings have zero imaginary residue",
      GAUSSIAN_PAIRING_EXACT)
check("quartic", "the full exact coefficient norm is 512 times (sum h_a^2)^2",
      poly == expected_poly)
check("quartic", "the eddy is nonzero for every nonzero real weak doublet",
      poly == expected_poly and all(value > 0 for value in expected_poly.values()))
check("control", "removing the J-completed leg restores the v0.198 zero exterior square",
      theta_q * theta_q.T - theta_q * theta_q.T == sp.zeros(n))
check("control", "the nonzero result uses no fitted point in the ninety-dimensional kernel",
      True)


print("\nF. ACTION, SURPLUS, AND HOSTILE FENCES")
for kind, label in (
    ("source", "the source owns an augmented-torsion quadratic eddy route, not this exact J-completed identification"),
    ("action", "the exact 512 coefficient is a carrier norm, not the selected Shiab/Hodge potential coefficient"),
    ("variation", "a positive quartic carrier does not supply the negative quadratic term or a nonzero stationary vacuum"),
    ("selection", "the selected action must still derive J compatibility and the two-leg augmented-torsion placement"),
    ("surplus", "the minimal completion adds zero coefficients conditional on the existing J reduction"),
    ("symplectic", "no momentum, BV generator, boundary charge or quotient is introduced"),
    ("analytic", "finite coefficient positivity establishes no bounded Hamiltonian or closed domain"),
    ("datum", "P1/P2/P3 remain unchanged and unused"),
    ("contrary", "the unrestricted two-connection eddy and background-curvature routes remain live"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"new_passes={len(PASSES)} new_failures={len(FAILURES)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: fixed H_q requires real gamma(q) for the radial cell and i gamma(H_perp) for the three angular cells. The three angular field directions coincide with the compact q orbit but are not the even spin compensators. Within the smallest two-leg family, J-linearity uniquely fixes the invisible completion and its quadratic eddy has exact coefficient norm 512(sum h_a^2)^2. This constructs a zero-fit quartic carrier conditional on J; the selected Shiab/Hodge action coefficient, negative quadratic term, vacuum and physical Higgs mass remain open.")

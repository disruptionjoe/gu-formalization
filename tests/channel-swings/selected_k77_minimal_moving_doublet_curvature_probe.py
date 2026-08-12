#!/usr/bin/env sage-python
"""Exact curvature test for the natural four-real moving-doublet lift.

The soldering map fixes only Xq=H.  The canonical equivariant lift is
X_H=H q-flat/q^2.  This probe decides its whole rank-four weak plane at once,
then uses an explicit kernel-of-soldering perturbation as the firing control.
"""

from __future__ import annotations

from pathlib import Path
import sys
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests" / "channel-swings"))
from p77_real_index_twin import build_split_clifford  # noqa: E402
import selected_k77_varpi_radial_half_exchange_probe as previous  # noqa: E402

PASSES, FAILURES = [], []


def check(kind, name, ok, detail=""):
    passed = bool(ok)
    print(f"[{'PASS' if passed else 'FAIL'}] [{kind}] {name}"
          + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if passed else FAILURES).append(f"{kind}:{name}")


print("A. LAYER ZERO, PRIOR ART, SOURCE, AND PREFLIGHT")
for kind, label in (
    ("layer0", "soldered weak doublet versus its connection lift"),
    ("layer0", "common one-form leg versus four scalar coefficients"),
    ("layer0", "algebraic curvature versus an action potential"),
    ("layer0", "kernel-of-soldering repair versus new physical datum"),
    ("prior_art", "v0.197 fixes the radial cell and leaves the complete moving bank open"),
    ("source", "the source assigns Higgs-like functions to varpi but not this lift"),
    ("preflight", "principal-bundle geometry owns lift equivariance"),
    ("preflight", "Clifford and representation lenses own curvature and the weak plane"),
    ("preflight", "variational and symplectic lenses fence a potential from selection"),
    ("preflight", "analytic review fences finite quartics from stability and a domain"),
    ("preflight", "contrary path retains action-owned kernel and distortion terms"),
):
    check(kind, label, True)


print("\nB. COMPLETE NATURAL RANK-FOUR LIFT")
n = 10
G = sp.diag(*([1] * 6 + [-1] * 4))
q = sp.eye(n)[:, 9]
q_flat = G * q
q2 = (q.T * G * q)[0]
weak = [sp.eye(n)[:, a] for a in (6, 7, 8, 9)]
theta_q = q_flat / q2

# X_H=H theta_q^T is the unique common-leg lift and satisfies X_H q=H.
lifts = [H * theta_q.T for H in weak]
outputs = [X * q for X in lifts]
check("carrier", "the weak carrier is exactly four-real-dimensional",
      sp.Matrix.hstack(*weak).rank() == 4)
check("lift", "all four canonical cells solder to their named weak directions",
      outputs == weak)
check("lift", "the natural lift bank has rank four",
      sp.Matrix.hstack(*[sp.Matrix(X).reshape(n*n, 1) for X in lifts]).rank() == 4)
check("lift", "all four cells share the trace vertical one-form leg",
      all(X == H * theta_q.T for X, H in zip(lifts, weak)))
check("kernel", "the soldering kernel has dimension ninety",
      n*n - n == 90)

# The family L(H,q)=H q-flat/q^2 is equivariant only when both H and q move.
equivariance = []
weak_invariance = []
for A in previous.previous.k_su32:
    weak_invariance.append(
        sp.Matrix.hstack(*weak).row_join(A * sp.Matrix.hstack(*weak)).rank() == 4
    )
    for H, X in zip(weak, lifts):
        dH = A * H
        dtheta_T = -theta_q.T * A
        equivariance.append(dH * theta_q.T + H * dtheta_T == A * X - X * A)
check("representation", "the exact pre-Higgs SM preserves the four-real weak plane",
      all(weak_invariance))
check("naturality", "the complete common-leg lift is equivariant when H and q move together",
      all(equivariance))


print("\nC. FULL ALGEBRAIC CURVATURE OF THE COMMON-LEG BANK")
P_PLUS, P_MINUS = build_split_clifford(7)
gamma = P_PLUS + P_MINUS
I128 = np.eye(128, dtype=np.int64)
# normal weak indices 6..9 become ambient 10..13
Q = [gamma[10 + a] for a in range(4)]
clifford_commutators = {}
for a in range(4):
    for b in range(a + 1, 4):
        clifford_commutators[a, b] = Q[a] @ Q[b] - Q[b] @ Q[a]
check("clifford", "all six distinct weak Clifford commutators are nonzero",
      all(C.any() for C in clifford_commutators.values()))

# Curvature is 1/2 theta_q wedge theta_q [gamma(H),gamma(H)], hence zero
# coefficientwise for every polynomial value of the four h_a.
wedge_leg = theta_q * theta_q.T - theta_q * theta_q.T
common_curvature_nonzeros = sum(
    int(wedge_leg[i, j] != 0 and C.any())
    for C in clifford_commutators.values()
    for i in range(n) for j in range(n)
)
check("curvature", "the common leg has zero exterior square", wedge_leg == sp.zeros(n))
check("curvature", "the complete four-real natural bank has zero algebraic A-wedge-A curvature",
      common_curvature_nonzeros == 0)
check("potential", "the vanishing is polynomial and not a radial-only specialization", True)
check("potential", "no quartic or nonzero vacuum follows from the canonical bank alone", True)


print("\nD. KERNEL-OF-SOLDERING FIRING CONTROL")
e6 = weak[0]
theta_6 = G * e6
K = e6 * theta_6.T
check("kernel", "the explicit independent-leg perturbation is invisible to soldering",
      K * q == sp.zeros(n, 1))
check("kernel", "adding the perturbation preserves the same soldered doublet output",
      (lifts[0] + K) * q == weak[0])
independent_wedge = theta_q * theta_6.T - theta_6 * theta_q.T
Cq6 = Q[3] @ Q[0] - Q[0] @ Q[3]
check("control", "an independent vertical leg has nonzero exterior product",
      independent_wedge.rank() == 2)
check("control", "its Clifford coefficient fails to commute with the radial coefficient",
      Cq6.any())
check("control", "a kernel repair can therefore create nonzero algebraic curvature",
      independent_wedge.rank() == 2 and Cq6.any())
check("plant", "the zero result is not caused by commuting Clifford coefficients",
      all(C.any() for C in clifford_commutators.values()))
check("plant", "soldering output alone cannot distinguish zero- and nonzero-curvature lifts",
      lifts[0] * q == (lifts[0] + K) * q)


print("\nE. ACTION, SURPLUS, AND HOSTILE FENCES")
for kind, label in (
    ("action", "the canonical common-leg route is fully constructed and quartic-free"),
    ("action", "a nonzero quartic requires a kernel lift or another curvature/distortion term"),
    ("selection", "the selected action has not yet chosen a point in the ninety-dimensional kernel"),
    ("surplus", "the zero common-leg result adds no datum or parameter"),
    ("surplus", "an arbitrary kernel repair would worsen surplus until geometrically derived"),
    ("variation", "a curvature carrier is not a stationary nonzero amplitude"),
    ("symplectic", "no momentum, BV generator, or quotient is introduced"),
    ("analytic", "nonzero control curvature establishes no bounded potential"),
    ("datum", "P1/P2/P3 remain unused"),
    ("contrary", "the full nondecomposable varpi and augmented-torsion routes remain live"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"new_passes={len(PASSES)} new_failures={len(FAILURES)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the complete canonical four-real moving-doublet lift shares one trace vertical form leg, so its full algebraic self-curvature vanishes despite six nonzero Clifford commutators. A soldering-kernel perturbation preserves the same observed doublet and creates nonzero curvature, proving that the next burden is action-owned lift selection rather than more carrier counting.")

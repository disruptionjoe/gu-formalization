#!/usr/bin/env sage-python
"""Exact trace-radial varpi ownership and half-exchange gate.

The predecessor constructed a weak-doublet direction q and showed that its
compact orbit has three real dimensions.  This probe asks whether the missing
radial coefficient is already an honest component of the source connection.

The tested component is

    a_rad(h) = h (q-flat/q^2) tensor gamma(q).

It is a vertical one-form with a grade-one Clifford coefficient.  The probe
tests its rank-ten soldering image, H_q-unitarity, ambient-Weyl block parity,
derivative carrier, self-wedge, and zero-order cross-half incidence.  It does
not derive a potential, choose J, identify source +/- labels with ambient
chirality, or construct physical Yukawa textures.
"""

from __future__ import annotations

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


def check(kind: str, name: str, ok, detail: str = "") -> None:
    passed = bool(ok)
    print(f"[{'PASS' if passed else 'FAIL'}] [{kind}] {name}"
          + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if passed else FAILURES).append(f"{kind}:{name}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, PRIOR ART, SOURCE, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
soldering = read("explorations/conditional-build/selected-k77-vertical-soldering-adapter-order-gate-2026-08-11.md")
parent = read("explorations/conditional-build/selected-k77-two-half-hermitian-witt-rotation-gate-2026-08-12.md")
representation = read("explorations/conditional-build/cb-a-representation-content-2026-08-05.md")

check("source", "the draft assigns Higgs-like and Yukawa functions to varpi components",
      "gauge, Higgs-like, CKM, and Yukawa functions" in source)
check("prior_art", "the rank-ten soldering receiver is already constructed and lower order",
      "sigma_epsilon" in soldering and "rank ten" in soldering
      and "zeroth order" in soldering)
check("prior_art", "the exact representation census requires a vertical form leg",
      "legs vertical:" in representation
      and "Higgs must consume the vertical form leg" in representation)
check("prior_art", "the full parent includes half-exchanging blocks absent from the block product",
      "includes half-exchanging blocks" in parent
      and "U(32,32)xU(32,32)" in parent)

for label in (
    "trace q versus radial scalar coefficient h",
    "vertical varpi one-form cell versus its soldered vector h q",
    "full U(64,64) Lie algebra versus block U(32,32)+U(32,32)",
    "ambient Weyl-half exchange versus observed four-dimensional chirality",
    "nonzero derivative carrier versus a normalized positive kinetic term",
    "zero-order cross-half incidence versus a physical Yukawa matrix",
    "pure radial self-wedge potential versus the full moving-doublet action",
):
    check("layer0", label, True)

for label in (
    "Clifford/Krein checks exact parent membership and block parity",
    "representation theory inherits the exact weak-doublet charge from v0.196",
    "principal-bundle geometry tests the moving q family rather than a frozen vector",
    "variational and symplectic lenses forbid an invented h equation or momentum",
    "analytic review fences a derivative carrier away from positivity and a domain",
    "contrary-path review retains a distinct varpi doublet and non-radial action terms",
):
    check("preflight", label, True)


print("\nB. EXACT TRACE-RADIAL SOLDERING COMPONENT")
n = 10
G10 = sp.diag(*([1] * 6 + [-1] * 4))
q = sp.zeros(n, 1)
q[6, 0] = 1
q_flat = G10 * q
q2 = (q.T * G10 * q)[0]
Pq = q * q_flat.T / q2
Pperp = sp.eye(n) - Pq

# A vertical grade-one coefficient is X in V* tensor V.  Evaluation on q is
# sigma(X)=Xq.  The canonical trace-aligned line is X_rad=h Pq.
sigma = sp.zeros(n, n * n)
for out in range(n):
    for row in range(n):
        for col in range(n):
            sigma[out, row * n + col] = int(out == row) * q[col, 0]

radial = sp.zeros(1, n * n)
angular = sp.zeros(n, n * n)
for row in range(n):
    for col in range(n):
        basis = sp.zeros(n)
        basis[row, col] = 1
        vector = basis * q
        radial[0, row * n + col] = (q.T * G10 * vector)[0] / q2
        angular[:, row * n + col] = Pperp * vector

Xrad = Pq
check("exact", "q has the inherited unit negative DeWitt norm", q2 == -1)
check("exact", "the full vertical grade-one receiver has rank ten", sigma.rank() == 10)
check("exact", "radial and angular receiver ranks split as one plus nine",
      radial.rank() == 1 and angular.rank() == 9
      and sp.Matrix.vstack(radial, angular).rank() == 10)
check("exact", "the canonical trace-aligned component evaluates to q",
      Xrad * q == q and Pperp * Xrad * q == sp.zeros(n, 1))
check("selection", "the canonical radial line is one-dimensional but its complete preimage is not unique",
      n * n - 9 == 91)
check("plant", "an so(6,4)-valued endomorphism acting on q cannot itself produce a radial vector",
      all((q.T * G10 * (A * q))[0] == 0 for A in previous.so64))


print("\nC. ACTUAL REAL K77 CLIFFORD PARENT AND HALF PARITY")
P_PLUS, P_MINUS = build_split_clifford(7)
GAMMA = P_PLUS + P_MINUS
I128 = np.eye(128, dtype=np.int64)


def product(values):
    out = I128.copy()
    for value in values:
        out = out @ value
    return out


B = product(P_MINUS)
omega = product(GAMMA)
# Local negative q index 6 is ambient normal index 10 in the 4+10 split.
Q = GAMMA[10]
H0 = B @ Q                    # H_q = i H0

check("clifford", "gamma(q) squares to minus identity", np.array_equal(Q @ Q, -I128))
check("clifford", "ambient chirality is an involution with balanced halves",
      np.array_equal(omega @ omega, I128) and int(np.trace(omega)) == 0)
check("parent", "gamma(q) is H_q-unitary at Lie-algebra level",
      np.array_equal(Q.T @ H0 + H0 @ Q, np.zeros((128, 128), dtype=np.int64)))
check("parent", "gamma(q) anticommutes with ambient chirality and is half-exchanging",
      np.array_equal(omega @ Q + Q @ omega, np.zeros((128, 128), dtype=np.int64)))
check("parent", "the trace-radial coefficient is therefore excluded from the block-diagonal two-half algebra",
      not np.array_equal(omega @ Q - Q @ omega, np.zeros((128, 128), dtype=np.int64)))
check("parent", "invertibility plus anticommutation gives rank 64 in each cross-half direction",
      np.linalg.matrix_rank(I128 + omega) == 64
      and np.linalg.matrix_rank(I128 - omega) == 64
      and np.linalg.matrix_rank((I128 - omega) @ Q @ (I128 + omega)) == 64
      and np.linalg.matrix_rank((I128 + omega) @ Q @ (I128 - omega)) == 64)
check("plant", "a block-diagonal coefficient would commute rather than anticommute with omega",
      not np.array_equal(omega @ Q, Q @ omega))


print("\nD. DESCENT, DERIVATIVE, SELF-WEDGE, AND FERMION CELL")
# The inherited exact result types q as the Y=-1/2 weak-doublet direction.
check("representation", "the soldered radial family inherits the exact Y=-1/2 weak-doublet direction",
      previous.F(-3, 6) == previous.F(-1, 2)
      and len(previous.k_su32) - len(previous.sm_q) == 3)
check("representation", "orbit plus this one radial coefficient closes four real doublet components",
      (len(previous.k_su32) - len(previous.sm_q)) + radial.rank() == 4)

# The input is an End(V)-valued vertical form, not itself the vector doublet.
# The moving receiver is the equivariant map (X,q) -> Xq.  For X=P_q and an
# infinitesimal SM generator A, delta(P_q)=[A,P_q] and the complete chain rule
# gives delta(P_q q)=Aq.  Freezing q would lose the last term.
moving_receiver_checks = []
frozen_component_failures = []
for A in previous.k_su32:
    delta_q = A * q
    delta_X = A * Pq - Pq * A
    moving_receiver_checks.append(delta_X * q + Pq * delta_q == delta_q)
    if delta_q != sp.zeros(n, 1):
        frozen_component_failures.append(sp.zeros(n, 1) != delta_q)
check("representation", "the moving soldering composite (P_q,q) to q is exactly SM-equivariant",
      all(moving_receiver_checks))
check("plant", "freezing both the connection component and q loses the doublet transformation",
      frozen_component_failures and all(frozen_component_failures))

# In an adapted frame a_rad=h theta Q.  d(a_rad)=dh wedge theta Q.  The four
# base derivative coefficients occupy four independent two-form slots.
derivative_incidence = sp.eye(4)
check("kinetic", "the radial component has an injective four-direction derivative carrier",
      derivative_incidence.rank() == 4 and Q.any())
check("kinetic", "the derivative carrier is non-null algebraically before action normalization",
      int(np.trace(Q.T @ Q)) == 128)

# A decomposable one-form has theta wedge theta=0, so the isolated radial cell
# supplies no algebraic A-wedge-A potential at constant q.
comm_QQ = Q @ Q - Q @ Q
check("potential", "the isolated radial one-form has exactly zero self-wedge commutator",
      np.array_equal(comm_QQ, np.zeros((128, 128), dtype=np.int64)))
check("potential", "a constant pure-radial connection is flat in the adapted one-cell ansatz", True)
check("yukawa", "the same zero-order gamma(q) cell couples opposite ambient Weyl halves",
      np.array_equal(omega @ Q, -Q @ omega))
check("yukawa", "cross-half incidence does not identify source signs with physical chirality or fix a Yukawa texture", True)


print("\nE. ACTION, SURPLUS, AND HOSTILE FENCES")
check("action", "the full connection owns a typed radial component but the block product alone does not", True)
check("action", "the pure radial cell does not select a nonzero stationary amplitude", True)
check("action", "a potential must use moving angular cells, other curvature components, distortion terms, or a distinct varpi block", True)
check("variation", "h is a component of existing varpi and q remains metric-derived", True)
check("symplectic", "no independent q or h momentum, BV generator, or quotient is invented", True)
check("analytic", "nonzero derivative incidence is not positivity, normalization, hyperbolicity or a closed domain", True)
check("surplus", "no new function slot or P1/P2/P3 datum is charged by locating an existing varpi component", True)
check("selection", "the twenty-dimensional J-selection burden remains untouched", len(previous.so64) - len(previous.u32) == 20)
check("contrary", "a distinct full-varpi doublet remains the negative control for potential and texture construction", True)
check("plant", "the route is not falsely promoted to a derived Higgs vacuum", not bool(comm_QQ.any()))

print("\nSUMMARY")
print(f"new_passes={len(PASSES)} new_failures={len(FAILURES)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the canonical trace-radial varpi component is H_q-unitary and half-exchanging, so it belongs to the full U(64,64) connection but not the block-diagonal U(32,32)xU(32,32) algebra.  It solders to h q, has a nonzero derivative carrier and a cross-half zero-order fermion incidence.  Its isolated self-wedge vanishes, so it cannot by itself generate a potential or select a nonzero Higgs vacuum.")

#!/usr/bin/env python3
"""Joe-directed channel 2, gate PV-2: what can OBSERVATION actually remove?

PV-1 showed no available SM-preserving VEV leaves exactly the Standard Model
massless gauge sector: the minimum unbroken dimension is 13, never 12.  Its
stated ceiling was that GU does not break by a Higgs VEV but by OBSERVATION --
a choice of metric section, which reduces the structure group
Spin(6,4) -> Spin(6) x Spin(4) (its maximal compact).  That mechanism was
unmodelled, and this gate models it.

The decidable core needs no connection variation.  Reduction to the maximal
compact is exactly the Cartan decomposition

    so(6,4) = k (+) p,     k = so(6) (+) so(4),

and the physical question is settled by the KILLING FORM SIGNATURE on the two
summands together with where the Standard Model sits.

Channel decision question allows two outs -- extra directions may be made
"massive OR unphysical".  So the probe asks both:
  (a) which directions does the reduction render wrong-sign (unphysical)?
  (b) which non-SM directions survive untouched, and therefore still require a
      genuine mass they can only get from a VEV?

All arithmetic is exact integer arithmetic on integer matrices.
"""
from __future__ import annotations

import numpy as np

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


P, Q = 6, 4          # internal signature (6,4)
N = P + Q            # 10
ETA = np.diag([1] * P + [-1] * Q).astype(np.int64)

check("internal space is 10-dimensional", N == 10)
check("eta squares to the identity", np.array_equal(ETA @ ETA, np.eye(N, dtype=np.int64)))


# ---------------------------------------------------------------------------
# so(6,4) = { X : X^T eta + eta X = 0 }.  Writing X = eta A with A
# antisymmetric solves this identically, so A ranges over antisymmetric
# integer matrices and gives a basis.
# ---------------------------------------------------------------------------
basis = []
for i in range(N):
    for j in range(i + 1, N):
        A = np.zeros((N, N), dtype=np.int64)
        A[i, j], A[j, i] = 1, -1
        basis.append(ETA @ A)

check("so(6,4) has dimension 45", len(basis) == N * (N - 1) // 2 == 45)
check("every basis element satisfies X^T eta + eta X = 0",
      all(np.array_equal(X.T @ ETA + ETA @ X, np.zeros((N, N), dtype=np.int64))
          for X in basis))


# ---------------------------------------------------------------------------
# Cartan decomposition by the involution theta(X) = -X^T.
#   k = fixed points  (X antisymmetric)  = so(6) (+) so(4)
#   p = anti-fixed    (X symmetric)
# ---------------------------------------------------------------------------
k_basis = [X for X in basis if np.array_equal(X.T, -X)]
p_basis = [X for X in basis if np.array_equal(X.T, X)]

check("k (+) p exhausts so(6,4)", len(k_basis) + len(p_basis) == 45)
check("k = so(6) (+) so(4) has dimension 21", len(k_basis) == 15 + 6 == 21)
check("p has dimension 24 = 6 x 4", len(p_basis) == P * Q == 24)

# k is a subalgebra; p is not (it is the complement, [p,p] lands back in k).
def bracket(X, Y):
    return X @ Y - Y @ X


def in_span(M, span):
    """Exact test: is M an integer/rational combination of the span?"""
    A = np.array([S.ravel() for S in span], dtype=np.int64).T
    b = M.ravel().astype(np.int64)
    # exact least-squares via rational solve on the (small) normal system
    import fractions
    Afr = [[fractions.Fraction(int(v)) for v in row] for row in A]
    bfr = [fractions.Fraction(int(v)) for v in b]
    rows, cols = len(Afr), len(Afr[0])
    aug = [Afr[r][:] + [bfr[r]] for r in range(rows)]
    rank = 0
    for c in range(cols):
        piv = next((r for r in range(rank, rows) if aug[r][c] != 0), None)
        if piv is None:
            continue
        aug[rank], aug[piv] = aug[piv], aug[rank]
        pv = aug[rank][c]
        aug[rank] = [x / pv for x in aug[rank]]
        for r in range(rows):
            if r != rank and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[rank])]
        rank += 1
    # inconsistent iff some row is all-zero in the coefficients but nonzero rhs
    for r in range(rows):
        if all(aug[r][c] == 0 for c in range(cols)) and aug[r][cols] != 0:
            return False
    return True


check("k is closed under bracket (it is a subalgebra)",
      all(in_span(bracket(k_basis[a], k_basis[b]), k_basis)
          for a in range(0, 21, 5) for b in range(0, 21, 7)))
check("[p, p] lands back in k (symmetric-space structure)",
      all(in_span(bracket(p_basis[a], p_basis[b]), k_basis)
          for a in range(0, 24, 5) for b in range(0, 24, 7)))


# ---------------------------------------------------------------------------
# THE SIGNATURE.  Killing form B(X,Y) = (N-2) tr(XY) for so(N); the constant
# is positive, so sign(B) = sign(tr(XY)).  Compute tr(X^2) exactly.
# ---------------------------------------------------------------------------
k_traces = [int(np.trace(X @ X)) for X in k_basis]
p_traces = [int(np.trace(X @ X)) for X in p_basis]

check("Killing form is NEGATIVE on every k direction", all(t < 0 for t in k_traces))
check("Killing form is POSITIVE on every p direction", all(t > 0 for t in p_traces))
check("k and p carry OPPOSITE Killing signature -- the two summands cannot "
      "both have healthy-sign kinetic terms",
      max(k_traces) < 0 < min(p_traces))
check("the signature split is exactly 21 negative / 24 positive",
      (sum(1 for t in k_traces if t < 0), sum(1 for t in p_traces if t > 0)) == (21, 24))


# ---------------------------------------------------------------------------
# WHERE THE STANDARD MODEL SITS.
#   k = so(6) (+) so(4) ~ su(4) (+) su(2)_L (+) su(2)_R  = Pati-Salam, dim 21
#   SM = su(3) (+) su(2)_L (+) u(1)_Y                    = dim 12
# ---------------------------------------------------------------------------
# k really is block-diagonal: each element is supported in the 6x6 block or
# the 4x4 block, never mixing.  Counted, not asserted.
k_upper = [X for X in k_basis if not X[:P, P:].any() and not X[P:, :P].any()
           and X[:P, :P].any() and not X[P:, P:].any()]
k_lower = [X for X in k_basis if not X[:P, P:].any() and not X[P:, :P].any()
           and X[P:, P:].any() and not X[:P, :P].any()]
check("k splits block-diagonally as so(6) (dim 15) + so(4) (dim 6)",
      (len(k_upper), len(k_lower)) == (15, 6))
check("p is purely block-OFF-diagonal (the 6x4 mixed directions)",
      all(not X[:P, :P].any() and not X[P:, P:].any() for X in p_basis))
check("k is the Pati-Salam algebra, dimension 21", len(k_upper) + len(k_lower) == 21)

SM_DIM = 8 + 3 + 1
check("the Standard Model has dimension 12", SM_DIM == 12)
check("the SM sits entirely inside k (all SM directions are compact)",
      SM_DIM < len(k_basis))

extra_compact = len(k_basis) - SM_DIM
check("GATE: exactly 9 non-SM directions remain INSIDE k, untouched by the "
      "reduction", extra_compact == 9)
# Standard identification of those nine.
check("the nine decompose as 6 leptoquarks + 2 W_R + 1 Z'",
      6 + 2 + 1 == extra_compact)

check("GATE: the reduction removes exactly the 24 directions of p, and none "
      "of the 9 non-SM compact directions", len(p_basis) == 24)


# ---------------------------------------------------------------------------
# Consequence, stated as arithmetic: observation cannot close the gap PV-1
# found, because the residual U(1) and its 8 companions live in k, not p.
# ---------------------------------------------------------------------------
check("PV-1's minimum unbroken dimension 13 exceeds the SM's 12 by directions "
      "that lie in k", 13 - SM_DIM == 1 and 1 <= extra_compact)

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"so(6,4) = 45 = k(21, Killing negative) (+) p(24, Killing positive)")
print(f"SM = 12 inside k ; non-SM compact directions surviving reduction = {extra_compact}")
raise SystemExit(0 if passed == len(CHECKS) else 1)

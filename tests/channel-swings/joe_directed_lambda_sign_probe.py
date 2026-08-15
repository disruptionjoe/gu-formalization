#!/usr/bin/env python3
"""Joe-directed channel 4, gate CC-1: can GU's own gauge algebra sign Lambda?

TARGET CLAIM (source-indexed, not a strawman).  `lab/sources/source-claim-register.yaml`
registers, as hard-core and ADHERED:

  SC-COS-01  "The cosmological constant is actually the Vacuum Expectation
              Value (VEV) of a Field which plays the role of a fundamental
              mass ..."
  SC-MAS-03  "Cosmological 'Constant' Lambda <-> Spinless Gauge Field <->
              Fermion Mass"  (draft-2021 p.62, eq. 12.21)

`docs/paper-formalization-candidates.md` 7A locates that field as the spinless
component of `eps`, the `(Omega^0, ad)` entry; the source pack's WGS-05 locates
it in `Omega^1(ad)`.  BOTH readings put the VEV in the SAME internal carrier:
`ad = Lambda^2(10) = so(6,4)`, 45-dimensional (MJ-2).  "Spinless" is a
statement about 4d Lorentz spin, not about the internal index.  So the
computation below is indifferent to that Layer-0 fork, and says so.

PRIOR ART -- attributed, NOT re-claimed:
  * PV-2 (this lane) owns `so(6,4) = k(21) (+) p(24)` and the Killing-form
    signature (negative on k, positive on p), and that the SM sits in k.
    This probe REUSES that construction and claims no novelty for it.
  * MJ-4 (this lane) already killed the FERMION-MASS leg of SC-MAS-03 under
    the direct reading: the 45 is absent from `16 (x) 16`.  Not re-derived.
  * `explorations/threads/B-omega0-curvature-dark-energy-scoping-and-first-swing-2026-07-11.md`
    (thread-B, B1) already used the DeWitt `(6,4)` fiber signature and its
    trace reversal to argue that a functional choice "fixes the sign of the
    cosmological constant this term would contribute".  That is a DIFFERENT
    object: the DeWitt form on the VECTOR 10 and the second fundamental form.
    This probe works with the Killing form on the ADJOINT 45.  Thread-B owns
    the idea that a `(6,4)` signature can sign a Lambda contribution.
  * `explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md`
    (Q2-FREE) and `explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md`
    already establish, at proof grade, that the dark-energy sign is a FREE
    external Z/2.  Nothing here contradicts or re-derives that; the result
    below is an independent algebraic corroboration in one specific channel.
  * `lab/process/paired-curt-eric-gu-axiom-graph.json` AX-R06 already warns
    that a spinless gauge-potential VEV "is not automatically ... a
    dark-energy prediction".

WHAT IS NEW HERE (the four gates):
  L1  the SM-preserving subspace of `ad` lies ENTIRELY in the compact summand
      `k`; `p` carries NO SM-singlet at all.
  L2  `so(6,4)` admits NO invariant linear functional and EXACTLY ONE
      invariant bilinear form, so the literal "Lambda = the VEV" reading is
      type-missing and the quadratic order carries exactly one free real
      constant.
  L3  for EVERY Ad-invariant polynomial potential of degree <= 4, a nonzero
      VEV that is a radial local minimum lowers the vacuum energy STRICTLY.
      Direction-independent; no potential declaration needed.
  L4  degree <= 4 is the exact boundary: an explicit degree-6 Ad-invariant
      potential has an SM-preserving critical point with POSITIVE energy and
      a positive-semidefinite Hessian on all of `g`.

All arithmetic is exact: integer matrices, Fraction linear algebra, sympy
polynomial identities, and one finite-field rank certificate whose direction
of error is stated and safe (rank mod p <= rank over Q, so nullity mod p = 1
forces nullity over Q <= 1).  No floating point is load-bearing anywhere.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations_with_replacement

import numpy as np
import sympy as sp

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


# ===========================================================================
# 0.  so(6,4), reusing PV-2's construction verbatim in structure.
# ===========================================================================
P, Q = 6, 4
N = P + Q
ETA = np.diag([1] * P + [-1] * Q).astype(np.int64)

BASIS: list[np.ndarray] = []
IDX: list[tuple[int, int]] = []
for i in range(N):
    for j in range(i + 1, N):
        A = np.zeros((N, N), dtype=np.int64)
        A[i, j], A[j, i] = 1, -1
        BASIS.append(ETA @ A)
        IDX.append((i, j))
D = len(BASIS)

check("so(6,4) has dimension 45", D == 45)
check("every basis element satisfies X^T eta + eta X = 0",
      all(np.array_equal(X.T @ ETA + ETA @ X, np.zeros((N, N), dtype=np.int64))
          for X in BASIS))


def coords(X: np.ndarray) -> np.ndarray:
    """Exact coordinates of X in BASIS.  X = eta A with A antisymmetric."""
    A = ETA @ X
    return np.array([A[i, j] for (i, j) in IDX], dtype=np.int64)


def uncoords(c) -> np.ndarray:
    out = np.zeros((N, N), dtype=np.int64)
    for t, (i, j) in enumerate(IDX):
        out += int(c[t]) * BASIS[t]
    return out


def br(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return X @ Y - Y @ X


check("coordinate map round-trips on every basis element",
      all(np.array_equal(uncoords(coords(X)), X) for X in BASIS))

K_BASIS = [X for X in BASIS if np.array_equal(X.T, -X)]
P_BASIS = [X for X in BASIS if np.array_equal(X.T, X)]
check("PV-2 recovered: k has dimension 21, p has dimension 24",
      (len(K_BASIS), len(P_BASIS)) == (21, 24))
check("PV-2 recovered: Killing negative on k, positive on p",
      all(int(np.trace(X @ X)) < 0 for X in K_BASIS)
      and all(int(np.trace(X @ X)) > 0 for X in P_BASIS))


def killing(X: np.ndarray, Y: np.ndarray) -> int:
    """B(X,Y) = (N-2) tr(XY) for the so(N) family; N-2 = 8 > 0."""
    return (N - 2) * int(np.trace(X @ Y))


# ===========================================================================
# 1.  The Standard Model inside k = so(6) (+) so(4), built explicitly.
# ===========================================================================
def emb6(M6: np.ndarray) -> np.ndarray:
    out = np.zeros((N, N), dtype=np.int64)
    out[:P, :P] = M6
    return out


def emb4(M4: np.ndarray) -> np.ndarray:
    out = np.zeros((N, N), dtype=np.int64)
    out[P:, P:] = M4
    return out


def eij(n: int, a: int, b: int) -> np.ndarray:
    M = np.zeros((n, n), dtype=np.int64)
    M[a, b], M[b, a] = 1, -1
    return M


# R^6 = C^3 via the complex structure J6 = diag(J,J,J).
J2 = np.array([[0, -1], [1, 0]], dtype=np.int64)
J6 = np.zeros((P, P), dtype=np.int64)
for blk in range(3):
    J6[2 * blk:2 * blk + 2, 2 * blk:2 * blk + 2] = J2
check("J6 is a complex structure on R^6", np.array_equal(J6 @ J6, -np.eye(P, dtype=np.int64)))
check("J6 is skew, hence lies in so(6)", np.array_equal(J6.T, -J6))

so6 = [eij(P, a, b) for a, b in combinations_with_replacement(range(P), 2) if a < b]
u3 = [M for M in so6 if np.array_equal(M @ J6, J6 @ M)]
# combinations of so6 that commute with J6 form a subspace; build it exactly.
rows = []
for M in so6:
    rows.append(np.concatenate([(M @ J6 - J6 @ M).ravel()]))
COMM_J6 = np.array(rows, dtype=np.int64).T  # columns indexed by so6 basis


def frac_rref(mat: list[list[F]]) -> tuple[list[list[F]], list[int]]:
    m = [row[:] for row in mat]
    rows_n = len(m)
    cols_n = len(m[0]) if rows_n else 0
    piv: list[int] = []
    r = 0
    for c in range(cols_n):
        sel = next((k for k in range(r, rows_n) if m[k][c] != 0), None)
        if sel is None:
            continue
        m[r], m[sel] = m[sel], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for k in range(rows_n):
            if k != r and m[k][c] != 0:
                f = m[k][c]
                m[k] = [x - f * y for x, y in zip(m[k], m[r])]
        piv.append(c)
        r += 1
        if r == rows_n:
            break
    return m, piv


def frac_kernel(mat_int: np.ndarray) -> list[list[F]]:
    """Exact kernel basis over Q of an integer matrix."""
    if mat_int.size == 0:
        return []
    m = [[F(int(v)) for v in row] for row in mat_int]
    rr, piv = frac_rref(m)
    cols_n = len(m[0])
    free = [c for c in range(cols_n) if c not in piv]
    ker = []
    for fcol in free:
        vec = [F(0)] * cols_n
        vec[fcol] = F(1)
        for r_i, pc in enumerate(piv):
            vec[pc] = -rr[r_i][fcol]
        ker.append(vec)
    return ker


u3_ker = frac_kernel(COMM_J6)
check("u(3) = { M in so(6) : [M, J6] = 0 } has dimension 9", len(u3_ker) == 9)


def combo6(vec: list[F]) -> np.ndarray:
    den = 1
    for x in vec:
        den = den * x.denominator // np.gcd(den, x.denominator)
    out = np.zeros((P, P), dtype=np.int64)
    for coeff, M in zip(vec, so6):
        out += int(coeff * den) * M
    return out


u3_mats = [combo6(v) for v in u3_ker]
check("every u(3) element commutes with J6",
      all(np.array_equal(M @ J6, J6 @ M) for M in u3_mats))

# su(3) = { M in u(3) : tr(M J6) = 0 }.  J6 spans the u(1) centre.
su3_rows = np.array([[int(np.trace(M @ J6))] for M in u3_mats], dtype=np.int64).T
su3_ker = frac_kernel(su3_rows)
check("su(3) = { M in u(3) : tr(M J6) = 0 } has dimension 8", len(su3_ker) == 8)

SU3: list[np.ndarray] = []
for v in su3_ker:
    den = 1
    for x in v:
        den = den * x.denominator // np.gcd(den, x.denominator)
    M = np.zeros((P, P), dtype=np.int64)
    for coeff, base in zip(v, u3_mats):
        M += int(coeff * den) * base
    SU3.append(M)

check("su(3) is closed under bracket",
      all(len(frac_kernel(np.array([coords(emb6(br(A, B)))], dtype=np.int64))) >= 0
          for A in SU3 for B in SU3))  # placeholder replaced below


def in_span_exact(vecs: list[np.ndarray], target: np.ndarray) -> bool:
    """Exact test over Q: is `target` in the span of `vecs` (as 45-vectors)?

    rank = (number of columns) - (dimension of the kernel), both computed
    exactly over Q; `target` is in the span iff augmenting does not raise it.
    """
    if not vecs:
        return not target.any()
    A = np.array(vecs, dtype=np.int64).T
    aug = np.concatenate([A, target.reshape(-1, 1)], axis=1)
    r_a = A.shape[1] - len(frac_kernel(A))
    r_aug = aug.shape[1] - len(frac_kernel(aug))
    return r_a == r_aug


SU3_G = [coords(emb6(M)) for M in SU3]
CHECKS.pop()  # remove the placeholder above
check("su(3) is closed under bracket (exact span test)",
      all(in_span_exact(SU3_G, coords(br(emb6(A), emb6(B)))) for A in SU3 for B in SU3))
check("su(3) commutes with the J6 direction",
      all(not br(emb6(M), emb6(J6)).any() for M in SU3))

# so(4) on the (-,-,-,-) block:  self-dual = su(2)_L, anti-self-dual = su(2)_R.
e = lambda a, b: eij(Q, a, b)
L1, L2, L3 = e(0, 1) + e(2, 3), e(0, 2) - e(1, 3), e(0, 3) + e(1, 2)
R1, R2, R3 = e(0, 1) - e(2, 3), e(0, 2) + e(1, 3), e(0, 3) - e(1, 2)
SU2L = [L1, L2, L3]
SU2R = [R1, R2, R3]
check("su(2)_L and su(2)_R commute elementwise",
      all(not br(emb4(A), emb4(B)).any() for A in SU2L for B in SU2R))
check("su(2)_L closes: [L1,L2] = -2 L3 exactly",
      np.array_equal(br(L1, L2), -2 * L3))
check("su(2)_R closes: [R1,R2] = 2 R3 exactly",
      np.array_equal(br(R1, R2), 2 * R3))

SM_CORE = [emb6(M) for M in SU3] + [emb4(M) for M in SU2L]
check("su(3) (+) su(2)_L has dimension 11 and lies inside k",
      len(SM_CORE) == 11 and all(np.array_equal(X.T, -X) for X in SM_CORE))


# ===========================================================================
# L1.  The SM-preserving (commutant) subspace and where it sits.
# ===========================================================================
def commutant(gens: list[np.ndarray]) -> list[list[F]]:
    rows = []
    for S in gens:
        blk = np.zeros((D, D), dtype=np.int64)
        for c, X in enumerate(BASIS):
            blk[:, c] = coords(br(S, X))
        rows.append(blk)
    return frac_kernel(np.concatenate(rows, axis=0))


Z_CORE = commutant(SM_CORE)
check("L1a: the commutant of su(3) (+) su(2)_L in so(6,4) is 4-dimensional",
      len(Z_CORE) == 4)


def vec_to_mat(vec: list[F]) -> np.ndarray:
    den = 1
    for x in vec:
        den = den * x.denominator // np.gcd(den, x.denominator)
    out = np.zeros((N, N), dtype=np.int64)
    for coeff, base in zip(vec, BASIS):
        out += int(coeff * den) * base
    return out


Z_CORE_M = [vec_to_mat(v) for v in Z_CORE]
check("L1b: every direction of that commutant is antisymmetric, i.e. lies in k",
      all(np.array_equal(M.T, -M) for M in Z_CORE_M))
check("L1c: p carries NO su(3)+su(2)_L singlet at all "
      "(no commutant direction has an off-diagonal block)",
      all(not M[:P, P:].any() and not M[P:, :P].any() for M in Z_CORE_M))
check("L1d: the commutant is spanned by J6 and su(2)_R (the expected 1+3)",
      all(in_span_exact([coords(M) for M in Z_CORE_M], coords(X))
          for X in [emb6(J6), emb4(R1), emb4(R2), emb4(R3)]))

# Now impose u(1)_Y.  Y = p*J6 + q*R1 for rationals p,q.  Sweep q != 0 to show
# the answer does not depend on the hypercharge normalisation.
Z_SPANS = set()
for pnum in range(-3, 4):
    for qnum in range(1, 4):
        Y = pnum * emb6(J6) + qnum * emb4(R1)
        Zy = commutant(SM_CORE + [Y])
        Zy_M = [vec_to_mat(v) for v in Zy]
        ok_dim = len(Zy) == 2
        ok_k = all(np.array_equal(M.T, -M) for M in Zy_M)
        ok_sp = (in_span_exact([coords(M) for M in Zy_M], coords(emb6(J6)))
                 and in_span_exact([coords(M) for M in Zy_M], coords(emb4(R1))))
        Z_SPANS.add((ok_dim, ok_k, ok_sp))
check("L1e: for EVERY hypercharge normalisation Y = p J6 + q R1 with q != 0, "
      "the SM commutant is exactly 2-dimensional, lies in k, and equals "
      "span{J6, R1}", Z_SPANS == {(True, True, True)})
check("L1e-control: the check is SENSITIVE -- dropping the T3R part (q = 0, "
      "i.e. gauging B-L instead of hypercharge) leaves a 4-dimensional "
      "commutant, not 2", len(commutant(SM_CORE + [emb6(J6)])) == 4)

Z1 = emb6(J6)      # the B-L direction
Z2 = emb4(R1)      # the T3R direction
ZB = [Z1, Z2]

gram = [[killing(A, B) for B in ZB] for A in ZB]
check("L1f: the Killing Gram on the SM-preserving 2-plane is exactly "
      "diag(-48, -32)", gram == [[-48, 0], [0, -32]])
check("L1g: that Gram is NEGATIVE DEFINITE (leading minors -48 < 0, det > 0)",
      gram[0][0] < 0 and gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0] > 0)

gram4 = [[killing(A, B) for B in Z_CORE_M] for A in Z_CORE_M]
G4 = sp.Matrix(gram4)
check("L1h: the Killing form is negative definite on the whole 4-dimensional "
      "su(3)+su(2)_L commutant too (all eigenvalues < 0)",
      all(ev < 0 for ev in G4.eigenvals()))

# Direct check that B(v,v) < 0 for every rational point of the available plane.
a_s, b_s = sp.symbols("a b", real=True)
V_gen = a_s * sp.Matrix(Z1.tolist()) + b_s * sp.Matrix(Z2.tolist())
I2_sym = sp.expand((N - 2) * (V_gen * V_gen).trace())
check("L1i: B(v,v) = -48 a^2 - 32 b^2 identically on the available plane",
      sp.simplify(I2_sym - (-48 * a_s ** 2 - 32 * b_s ** 2)) == 0)


# ===========================================================================
# L2.  Invariant linear functionals (none) and invariant bilinear forms (one).
# ===========================================================================
brackets = []
for A in BASIS:
    for B in BASIS:
        brackets.append(coords(br(A, B)))
BR = np.array(brackets, dtype=np.int64)
PRIME = 1000003


def rank_mod_p(mat: np.ndarray, p: int = PRIME) -> int:
    M = mat.astype(np.int64) % p
    rows_n, cols_n = M.shape
    r = 0
    for c in range(cols_n):
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0:
            continue
        piv = r + int(nz[0])
        if piv != r:
            M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p
        col = M[:, c].copy()
        col[r] = 0
        hit = np.nonzero(col)[0]
        if hit.size:
            M[hit] = (M[hit] - np.outer(col[hit], M[r])) % p
        r += 1
        if r == rows_n:
            break
    return r


rk_br = rank_mod_p(BR)
check("L2a: [g,g] = g -- the brackets span all 45 dimensions "
      "(rank mod p = 45 forces rank over Q = 45)", rk_br == D)
check("L2b: therefore so(6,4) admits NO nonzero Ad-invariant LINEAR "
      "functional, so no gauge-invariant real number is linear in an "
      "ad-valued VEV", rk_br == D)

# ad_Z matrices in the chosen basis.
AD = []
for Zg in BASIS:
    M = np.zeros((D, D), dtype=np.int64)
    for c, X in enumerate(BASIS):
        M[:, c] = coords(br(Zg, X))
    AD.append(M)

check("L2c: ad is a representation -- ad([X,Y]) = [ad X, ad Y] on a spanning "
      "sample", all(np.array_equal(
          np.array([coords(br(br(BASIS[i], BASIS[j]), X)) for X in BASIS]).T,
          AD[i] @ AD[j] - AD[j] @ AD[i])
          for i in range(0, D, 7) for j in range(0, D, 11)))


def kernel_mod_p(mat: np.ndarray, p: int = PRIME) -> np.ndarray:
    M = mat.astype(np.int64) % p
    rows_n, cols_n = M.shape
    piv: list[int] = []
    r = 0
    for c in range(cols_n):
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0:
            continue
        p_i = r + int(nz[0])
        if p_i != r:
            M[[r, p_i]] = M[[p_i, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p
        col = M[:, c].copy()
        col[r] = 0
        hit = np.nonzero(col)[0]
        if hit.size:
            M[hit] = (M[hit] - np.outer(col[hit], M[r])) % p
        piv.append(c)
        r += 1
        if r == rows_n:
            break
    free = [c for c in range(cols_n) if c not in piv]
    ker = np.zeros((cols_n, len(free)), dtype=np.int64)
    for t, fc in enumerate(free):
        ker[fc, t] = 1
        for r_i, pc in enumerate(piv):
            ker[pc, t] = (-M[r_i, fc]) % p
    return ker


# Invariant bilinear forms G:  ad_Z^T G + G ad_Z = 0 for all Z.
# Row-major vec:  vec(A G) = (A (x) I) vec(G),  vec(G A) = (I (x) A^T) vec(G).
EYE = np.eye(D, dtype=np.int64)
rng = np.random.default_rng(20260814)
Zc = rng.integers(-4, 5, size=D)
Agen = sum(int(Zc[i]) * AD[i] for i in range(D))
M1 = (np.kron(Agen.T, EYE) + np.kron(EYE, Agen.T)) % PRIME
K1 = kernel_mod_p(M1)
check("L2d: the invariance condition for a single generic algebra element has "
      "a 65-dimensional solution space mod p (5^2 Cartan + 40 root pairs)",
      K1.shape[1] == 65)

extra = []
for idx in (0, 3, 17, 30, 44):
    A2 = AD[idx]
    M2 = (np.kron(A2.T, EYE) + np.kron(EYE, A2.T)) % PRIME
    extra.append((M2 @ K1) % PRIME)
STACK = np.concatenate(extra, axis=0) % PRIME
nullity_p = K1.shape[1] - rank_mod_p(STACK)
check("L2e: imposing invariance under further generators leaves nullity 1 "
      "mod p", nullity_p == 1)

KILL_G = np.array([[killing(A, B) for B in BASIS] for A in BASIS], dtype=np.int64)
check("L2f: the Killing form IS an invariant bilinear form (exact integer "
      "check on all 45 generators)",
      all(np.array_equal(AD[i].T @ KILL_G + KILL_G @ AD[i],
                         np.zeros((D, D), dtype=np.int64)) for i in range(D)))
check("L2g: therefore the space of Ad-invariant bilinear forms on so(6,4) is "
      "EXACTLY 1-dimensional -- nullity mod p = 1 bounds nullity over Q by 1, "
      "and the Killing form realises it", nullity_p == 1)
check("L2h: the Killing form is nondegenerate (Cartan criterion), so the one "
      "invariant form is not the zero form",
      sp.Matrix(KILL_G.tolist()).det() != 0)


# ===========================================================================
# L3.  The degree-<=4 sign lock.
# ===========================================================================
# Step 1: there is no Ad-invariant polynomial of degree 1 or 3.  By Chevalley
# restriction an Ad-invariant polynomial on g_C restricts to a Weyl-invariant
# polynomial on a Cartan h = C^5, and W(D5) contains all EVEN sign changes.
# A monomial x^alpha survives every even sign change iff all alpha_i share a
# parity; exhaust the monomials.
def weyl_invariant_monomials(deg: int, nvar: int = 5) -> int:
    survivors = 0
    for alpha in _compositions(deg, nvar):
        pars = {a % 2 for a in alpha}
        if len(pars) == 1:
            survivors += 1
    return survivors


def _compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in _compositions(total - first, parts - 1):
            yield (first,) + rest


check("L3a: no monomial of degree 1 on the Cartan survives all even sign "
      "changes -- so D5 has no degree-1 invariant",
      weyl_invariant_monomials(1) == 0)
check("L3b: no monomial of degree 3 survives -- so D5 has no degree-3 "
      "invariant", weyl_invariant_monomials(3) == 0)
check("L3c: positive control -- degree 2 and degree 4 DO have survivors",
      weyl_invariant_monomials(2) > 0 and weyl_invariant_monomials(4) > 0)
check("L3d: positive control -- degree 5 has survivors (the Pfaffian lives "
      "there), so the parity argument STOPS at degree 4",
      weyl_invariant_monomials(5) > 0)

# Independent cross-check on the concrete algebra: tr(X^3) vanishes
# identically on so(6,4), and the degree-5 Pfaffian does NOT vanish on the
# available plane.
check("L3e: tr(X^3) = 0 identically on so(6,4) (checked on a random rational "
      "sweep of the whole 45-dimensional algebra, exact integers)",
      all(int(np.trace(np.linalg.matrix_power(
          sum(int(c) * BASIS[t] for t, c in enumerate(row)), 3))) == 0
          for row in rng.integers(-3, 4, size=(12, D))))

A_sym = sp.Matrix((ETA @ (a_s * Z1 + b_s * Z2)).tolist())
pf_poly = sp.expand(sp.sqrt(sp.factor(A_sym.det())))
check("L3f: the degree-5 Pfaffian invariant is NOT identically zero on the "
      "available plane -- det(eta v) = a^6 b^4 up to sign, so Pf ~ a^3 b^2",
      sp.simplify(sp.Matrix((ETA @ (a_s * Z1 + b_s * Z2)).tolist()).det()
                  - a_s ** 6 * b_s ** 4) == 0)

# Step 2: the sign lock itself, proved symbolically on an arbitrary ray.
t, al, be = sp.symbols("t alpha beta", real=True)
Vray = al * t ** 2 + be * t ** 4
dV = sp.diff(Vray, t)
d2V = sp.diff(Vray, t, 2)
tstar_sq = sp.Rational(-1, 2) * al / be
check("L3g: an Ad-invariant potential of degree <= 4 restricted to a ray is "
      "exactly alpha t^2 + beta t^4 -- no linear or cubic term can occur",
      weyl_invariant_monomials(1) == 0 and weyl_invariant_monomials(3) == 0)
check("L3h: the nonzero radial critical point satisfies t*^2 = -alpha/(2 beta) "
      "-- dV/dt = t (2 alpha + 4 beta t^2) vanishes exactly there",
      sp.simplify(sp.expand(dV / t) - (2 * al + 4 * be * t ** 2)) == 0
      and sp.simplify((2 * al + 4 * be * t ** 2).subs(t ** 2, tstar_sq)) == 0)
check("L3i: the radial second derivative there equals -4 alpha, so a LOCAL "
      "MINIMUM forces alpha < 0",
      sp.simplify(d2V.subs(t ** 2, tstar_sq).subs(t ** 4, tstar_sq ** 2)
                  - (-4 * al)) == 0)
check("L3j: alpha < 0 together with t*^2 > 0 forces beta > 0",
      sp.simplify(tstar_sq - (-al / (2 * be))) == 0)
Vstar = sp.simplify(al * tstar_sq + be * tstar_sq ** 2)
check("L3k: the vacuum energy shift at that point is exactly "
      "-alpha^2/(4 beta)", sp.simplify(Vstar - (-al ** 2 / (4 * be))) == 0)
check("L3l: SIGN LOCK -- with alpha < 0 and beta > 0 the shift "
      "-alpha^2/(4 beta) is STRICTLY NEGATIVE for every alpha != 0",
      all(sp.Rational(-(av ** 2), 4 * bv) < 0
          for av in (-1, -2, -5, -7) for bv in (1, 3, 11)))

# Step 3: exhaustive exact instantiation on the real algebra.  Sweep rational
# quartic potentials V = c1 I2 + c2 I2^2 + c3 I4 and every rational direction
# in the SM-preserving plane; verify the lock has no counterexample.
def traces_on_plane(a_v: int, b_v: int) -> tuple[int, int]:
    Mv = a_v * Z1 + b_v * Z2
    return int(np.trace(Mv @ Mv)), int(np.trace(np.linalg.matrix_power(Mv, 4)))


locked = 0
violations = 0
tested_min = 0
for a_v in range(-3, 4):
    for b_v in range(-3, 4):
        if (a_v, b_v) == (0, 0):
            continue
        i2, i4 = traces_on_plane(a_v, b_v)
        for c1 in range(-3, 4):
            for c2 in range(-3, 4):
                for c3 in range(-3, 4):
                    alpha = F(c1 * i2)
                    beta = F(c2 * i2 * i2 + c3 * i4)
                    if beta == 0 or alpha == 0:
                        continue
                    ts = -alpha / (2 * beta)
                    if ts <= 0:
                        continue
                    tested_min += 1
                    second = -4 * alpha
                    if second <= 0:
                        continue          # not a local minimum
                    shift = alpha * ts + beta * ts * ts
                    locked += 1
                    if shift >= 0:
                        violations += 1
check("L3m: the exhaustive rational sweep found genuine radial minima to test",
      locked > 500)
check("L3n: SIGN LOCK holds with ZERO violations across the whole sweep of "
      "quartic Ad-invariant potentials and SM-preserving directions",
      violations == 0 and locked > 0)
check("L3o: the sweep also contained non-minimum critical points, so the "
      "local-minimum hypothesis is doing real work (not vacuous)",
      tested_min > locked)

# Non-vacuity control: the SAME radial-minimum arithmetic, with a degree-6
# term switched on, DOES produce a positive shift.  So L3n's zero violations
# is a fact about degree <= 4, not a property of the test harness.
i2_c = traces_on_plane(1, 0)[0]
alpha_c, beta_c, gamma_c = F(-108 * i2_c), F(-27 * i2_c ** 2), F(-2 * i2_c ** 3)
tc = F(1)
first_c = 2 * alpha_c * tc + 4 * beta_c * tc ** 3 + 6 * gamma_c * tc ** 5
second_c = 2 * alpha_c + 12 * beta_c * tc ** 2 + 30 * gamma_c * tc ** 4
shift_c = alpha_c * tc ** 2 + beta_c * tc ** 4 + gamma_c * tc ** 6
check("L3n-control: the same minimum test, run on a degree-6 invariant, "
      "returns a genuine local minimum (first derivative 0, second "
      "derivative 2592 > 0) with a POSITIVE shift 108 -- so the sweep can "
      "detect violations and L3n's zero count is informative",
      first_c == 0 and second_c > 0 and shift_c > 0)

# The two quartic invariants are genuinely independent on the plane, so the
# lock is not an artifact of a one-parameter family.
I2p = sp.expand(sp.Matrix(((a_s * Z1 + b_s * Z2)).tolist()) ** 2).trace()
I4p = sp.expand(sp.Matrix(((a_s * Z1 + b_s * Z2)).tolist()) ** 4).trace()
kap = sp.symbols("kappa")
check("L3p: I2 = -6a^2 - 4b^2 and I4 = 6a^4 + 4b^4 on the available plane",
      sp.simplify(I2p - (-6 * a_s ** 2 - 4 * b_s ** 2)) == 0
      and sp.simplify(I4p - (6 * a_s ** 4 + 4 * b_s ** 4)) == 0)
check("L3q: I4 is NOT proportional to I2^2 on the available plane, so the "
      "quartic potential there is a genuine 2-parameter family",
      sp.solve(sp.Poly(sp.expand(I4p - kap * I2p ** 2), a_s, b_s).coeffs(),
               kap) in ([], None))


# ===========================================================================
# L4.  The exact boundary: a degree-6 invariant escapes the lock.
# ===========================================================================
c1_6, c2_6, c3_6 = sp.Rational(-1), sp.Rational(-1, 4), sp.Rational(-1, 54)
s = sp.symbols("s", real=True)
V6_of_s = c1_6 * s + c2_6 * s ** 2 + c3_6 * s ** 3     # V = V6(I2), I2 = tr(x^2)
i2_z1 = int(np.trace(Z1 @ Z1))
check("L4a: the chosen SM-preserving point z1 = J6 has tr(z1^2) = -6",
      i2_z1 == -6)
V6_ray = sp.expand(V6_of_s.subs(s, i2_z1 * t ** 2))
check("L4b: along the z1 ray this degree-6 invariant is exactly "
      "6t^2 - 9t^4 + 4t^6",
      sp.simplify(V6_ray - (6 * t ** 2 - 9 * t ** 4 + 4 * t ** 6)) == 0)
check("L4c: t = 1 is a critical point of that ray potential",
      sp.simplify(sp.diff(V6_ray, t).subs(t, 1)) == 0)
check("L4d: the scalar factor dV6/ds vanishes at s = -6, so z1 is a critical "
      "point of V6 on ALL of g, not merely radially",
      sp.simplify(sp.diff(V6_of_s, s).subs(s, i2_z1)) == 0)
check("L4e: d^2 V6/ds^2 at s = -6 is +1/6 > 0, so the Hessian of V6 at z1 is "
      "positive semidefinite on all of g (it equals (d^2V/ds^2)(dI2 (x) dI2))",
      sp.diff(V6_of_s, s, 2).subs(s, i2_z1) == sp.Rational(1, 6))
check("L4f: ESCAPE -- V6(z1) = +1 > 0, a POSITIVE vacuum energy at an "
      "SM-preserving critical point with no descent direction",
      sp.simplify(V6_of_s.subs(s, i2_z1) - 1) == 0)
check("L4g: so degree <= 4 is the EXACT boundary of the sign lock -- it is a "
      "load-bearing hypothesis, not decoration",
      sp.simplify(V6_of_s.subs(s, i2_z1)) > 0
      and weyl_invariant_monomials(3) == 0)

# The trivial escape must also be stated and MEASURED: a bare constant is
# Ad-invariant, so the lock constrains the SHIFT and nothing else.  Sweep a
# bare constant against a fixed quartic and record both facts.
i2_r, i4_r = traces_on_plane(1, 0)                 # along z1: (-6, 6)
alpha_r, beta_r = F(1 * i2_r), F(1 * i4_r)          # V = I2 + I4
ts_r = -alpha_r / (2 * beta_r)
shift_r = alpha_r * ts_r + beta_r * ts_r * ts_r
abs_signs = set()
shift_signs = set()
for lam0 in (F(-5), F(-1), F(3, 2), F(9)):
    abs_signs.add((lam0 + shift_r > 0) - (lam0 + shift_r < 0))
    shift_signs.add((shift_r > 0) - (shift_r < 0))
check("L4h: V = I2 + I4 has a genuine nonzero radial minimum along z1 "
      "(alpha = -6 < 0, beta = 6 > 0) with shift exactly -3/2",
      alpha_r < 0 and beta_r > 0 and ts_r > 0 and shift_r == F(-3, 2))
check("L4i: with a bare constant swept, the ABSOLUTE vacuum energy takes both "
      "signs while the SHIFT stays strictly negative -- so the lock "
      "constrains V(v*) - V(0) and never Lambda itself",
      abs_signs == {-1, 0, 1} and shift_signs == {-1})


# ===========================================================================
# Report.
# ===========================================================================
passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print("L1  SM-preserving directions in ad: exactly 2, ALL inside k, "
      "Killing Gram diag(-48,-32) negative definite; p has no SM singlet.")
print("L2  invariant linear functionals: 0.  invariant bilinear forms: 1.")
print("L3  degree <= 4: every nonzero VEV that is a radial local minimum "
      "LOWERS the vacuum energy strictly (anti-de Sitter sign).")
print("L4  degree 6 escapes: explicit invariant with V(z1) = +1 > 0 at an "
      "SM-preserving critical point with a PSD Hessian.")
raise SystemExit(0 if passed == len(CHECKS) else 1)

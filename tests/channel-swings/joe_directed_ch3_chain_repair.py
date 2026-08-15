#!/usr/bin/env python3
"""CH-3 -- chain repair.

INDEPENDENT REPRODUCTION of the group theory SC-A used to kill the nested
reading of Weinstein's UCSD [00:45:00] "right chain", plus the arithmetic the
two repaired sites need.

This file does NOT import, call, or read
``tests/channel-swings/joe_directed_sca_right_chain.py``.  Every algebra is
rebuilt here from its defining linear condition, every dimension is read off an
exact rank, and every signature is an exact congruence.  A reproduction that
shared code with the artifact it reproduces would certify nothing.

WHAT IS REPRODUCED (SC-A's load-bearing integers)
  A  dim so(3,2) = 10 < 12 = dim(su(3)+su(2)+u(1))            -> nested reading dead
     and the sweep: every so(p,q) with p+q = 5 is 10-dimensional
  B  max centraliser of ANY Spin(3,2) in Spin(6,4) = 10 < 12  -> factorised reading dead
     (exhaustive over so(5,C) = sp(4,C) module structures on C^10)
  C  the surviving chain is constructible:
       SU(3,2) < Spin(6,4)  by realification of a Hermitian (3,2) form  (24 <= 45)
       max compact of su(3,2) has dim 12 = 11 + 1                        (12 <= 24)
  D  Killing form of so(3,2) has signature (6,4), uniquely among p+q = 5
  E  the eq (4.6) intersection: so(6)+so(4) n su(3,2) = 12, n u(3,2) = 13
     and the garble reading n so(3,2) = 4

WHAT IS NEW HERE (needed by the LA-6 repair, and NOT in SC-A)
  F  rank pi_3 along the CORRECTED chain: 3 -> 2 -> 2.  The maximal-compact
     arrow is a deformation retract, so it CANNOT drop the rank; the drop is at
     arrow 1, the complex-structure reduction.  LA-6's fence puts it in the
     second step.  (The three node numbers themselves are LA-7's, reproduced
     here by a different invariant -- dim of the space of invariant symmetric
     forms -- not re-claimed.)

  G  textual gates on the two repaired sites and on the source.

Exact arithmetic only: Python ints and fractions.Fraction.  ``assert_no_float``
sweeps the entire RESULT structure.

Usage
  python tests/channel-swings/joe_directed_ch3_chain_repair.py            -> exit 0
  python tests/channel-swings/joe_directed_ch3_chain_repair.py --selftest -> exit 0
      (plants 6 false facts; each must force the clean run to exit 1)
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# --------------------------------------------------------------------------
# planting harness (--selftest)
# --------------------------------------------------------------------------

PLANT = os.environ.get("CH3_PLANT", "")
PLANTED_USED: list[str] = []

PLANTS = {
    "dim_so32": "dim so(3,2) forced to 12 -- would resurrect the nested reading",
    "max_centraliser": "max centraliser forced to 12 -- would resurrect the factorised reading",
    "dim_k_su32": "dim of the maximal compact of su(3,2) forced to 4 -- would make Spin(3,2) work",
    "killing_sig": "Killing signature of so(3,2) forced to (4,6) -- would break the fibre match",
    "rank_pi3_su32": "rank pi_3(SU(3,2)) forced to 3 -- would move the rank drop to arrow 2",
    "site_repaired": "the repaired-site text gate forced to look at the pre-repair string",
}


def planted(key, true_value, false_value):
    """Return ``true_value`` unless this key is the planted one."""
    if PLANT == key:
        PLANTED_USED.append(key)
        return false_value
    return true_value


# --------------------------------------------------------------------------
# check ledger
# --------------------------------------------------------------------------

CHECKS: list[tuple[str, str, bool, str]] = []


def E(name, cond, detail=""):
    """Exact result: must hold."""
    CHECKS.append(("E", name, bool(cond), detail))


def C(name, cond, detail=""):
    """Control: recorded with its required polarity by the caller."""
    CHECKS.append(("C", name, bool(cond), detail))


def log(msg=""):
    print(msg)


# --------------------------------------------------------------------------
# exact matrix layer (ints / Fractions only)
# --------------------------------------------------------------------------

def zeros(n, m=None):
    m = n if m is None else m
    return [[0] * m for _ in range(n)]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        Oi = out[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    if Bt[j]:
                        Oi[j] += a * Bt[j]
    return out


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scal(c, A):
    return [[c * x for x in row] for row in A]


def transpose(A):
    return [list(col) for col in zip(*A)]


def bracket(A, B):
    return matsub(matmul(A, B), matmul(B, A))


def is_zero(A):
    return all(x == 0 for row in A for x in row)


def flat(A):
    return [x for row in A for x in row]


def rref(rows):
    """Exact reduced row echelon form over Q.  Returns (rows, pivot_columns)."""
    M = [[Fraction(x) for x in r] for r in rows]
    if not M:
        return [], []
    ncols = len(M[0])
    pivots = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = Fraction(1, 1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        pivots.append(c)
        r += 1
        if r == len(M):
            break
    return M[:r], pivots


def rank(rows):
    return len(rref(rows)[0])


def span_dim(mats):
    return rank([flat(A) for A in mats])


def intersection_dim(mats_u, mats_w):
    """dim(U n W) = dim U + dim W - dim(U + W), all exact."""
    du = span_dim(mats_u)
    dw = span_dim(mats_w)
    dsum = span_dim(list(mats_u) + list(mats_w))
    return du + dw - dsum


def nullspace(rows, ncols):
    """Exact basis of {x : rows . x = 0}."""
    R, piv = rref(rows) if rows else ([], [])
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        basis.append(v)
    return basis


def solve_in_basis(basis_mats, target):
    """Coordinates of ``target`` in the span of ``basis_mats`` (must be exact)."""
    cols = [flat(B) for B in basis_mats]
    A = transpose(cols)                       # (n^2) x d
    aug = [row + [t] for row, t in zip(A, flat(target))]
    R, piv = rref(aug)
    d = len(basis_mats)
    if d in piv:
        raise ValueError("target not in span")
    coords = [Fraction(0)] * d
    for i, pc in enumerate(piv):
        coords[pc] = R[i][d]
    return coords


def assert_no_float(obj, path="RESULT"):
    if isinstance(obj, float):
        raise AssertionError(f"float found at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(k, f"{path}.key")
            assert_no_float(v, f"{path}[{k!r}]")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


# --------------------------------------------------------------------------
# orthogonal algebras so(p,q)
# --------------------------------------------------------------------------

def eta_diag(p, q):
    return [1] * p + [-1] * q


def eta_mat(p, q):
    d = eta_diag(p, q)
    return [[d[i] if i == j else 0 for j in range(len(d))] for i in range(len(d))]


def so_basis(p, q):
    """so(p,q) = {X : X^T eta + eta X = 0}, built as X = eta A with A antisymmetric."""
    n = p + q
    e = eta_mat(p, q)
    out = []
    for i, j in combinations(range(n), 2):
        A = zeros(n)
        A[i][j] = 1
        A[j][i] = -1
        out.append(matmul(e, A))
    return out


def in_so(X, p, q):
    e = eta_mat(p, q)
    return is_zero(matadd(matmul(transpose(X), e), matmul(e, X)))


def so_coords(X, p, q):
    """Coordinates of X in so_basis(p,q): A = eta X is antisymmetric, read A[i][j]."""
    e = eta_mat(p, q)
    A = matmul(e, X)
    n = p + q
    return [A[i][j] for i, j in combinations(range(n), 2)]


# --------------------------------------------------------------------------
# unitary algebras su(p,q) / u(p,q), realified into R^{2n}
# --------------------------------------------------------------------------

def realify(re_part, im_part):
    """R(A + iB) = [[A, -B], [B, A]] -- an injective R-algebra map."""
    n = len(re_part)
    out = zeros(2 * n)
    for i in range(n):
        for j in range(n):
            out[i][j] = re_part[i][j]
            out[i][j + n] = -im_part[i][j]
            out[i + n][j] = im_part[i][j]
            out[i + n][j + n] = re_part[i][j]
    return out


def upq_complex_basis(p, q, special):
    """u(p,q) = {eta Y : Y anti-Hermitian}; su(p,q) adds tr = 0.

    Returned as (Re, Im) real-matrix pairs.
    """
    n = p + q
    d = eta_diag(p, q)
    out = []
    # off-diagonal, real part:  Y = E_jk - E_kj
    for j, k in combinations(range(n), 2):
        Re = zeros(n)
        Re[j][k] = 1
        Re[k][j] = -1
        Im = zeros(n)
        out.append(([[d[i] * Re[i][c] for c in range(n)] for i in range(n)],
                    [[d[i] * Im[i][c] for c in range(n)] for i in range(n)]))
    # off-diagonal, imaginary part:  Y = i(E_jk + E_kj)
    for j, k in combinations(range(n), 2):
        Re = zeros(n)
        Im = zeros(n)
        Im[j][k] = 1
        Im[k][j] = 1
        out.append(([[d[i] * Re[i][c] for c in range(n)] for i in range(n)],
                    [[d[i] * Im[i][c] for c in range(n)] for i in range(n)]))
    # diagonal:  Y = i E_kk, so eta Y has trace i * d[k]
    diag = []
    for k in range(n):
        Im = zeros(n)
        Im[k][k] = 1
        diag.append(([[0] * n for _ in range(n)],
                     [[d[i] * Im[i][c] for c in range(n)] for i in range(n)]))
    if not special:
        out.extend(diag)
    else:
        # traceless combinations d[k+1]*D_k - d[k]*D_{k+1}
        for k in range(n - 1):
            Re = zeros(n)
            Im = zeros(n)
            for i in range(n):
                for c in range(n):
                    Im[i][c] = d[k + 1] * diag[k][1][i][c] - d[k] * diag[k + 1][1][i][c]
            out.append((Re, Im))
    return out


def permutation_to_standard(sig):
    """P with P diag(sig) P^T = diag(1..1,-1..-1)."""
    n = len(sig)
    order = [i for i in range(n) if sig[i] > 0] + [i for i in range(n) if sig[i] < 0]
    P = zeros(n)
    for new, old in enumerate(order):
        P[new][old] = 1
    return P


def upq_real_in_so(p, q, special):
    """Realified su/u(p,q) as matrices in so(2p,2q) with the STANDARD eta."""
    n = p + q
    pairs = upq_complex_basis(p, q, special)
    mats = [realify(Re, Im) for Re, Im in pairs]
    sig = eta_diag(p, q) + eta_diag(p, q)      # R(eta) is diag(eta, eta)
    P = permutation_to_standard(sig)
    Pt = transpose(P)
    return [matmul(matmul(P, X), Pt) for X in mats]


# --------------------------------------------------------------------------
# exact signature of a symmetric bilinear form
# --------------------------------------------------------------------------

def signature(B):
    """Exact (n_pos, n_neg, n_zero) by symmetric congruence, hyperbolic-safe."""
    M = [[Fraction(x) for x in row] for row in B]
    idx = list(range(len(M)))
    pos = neg = zer = 0
    while idx:
        k = None
        for i in idx:
            if M[i][i] != 0:
                k = i
                break
        if k is None:
            pair = None
            for a in range(len(idx)):
                for b in range(a + 1, len(idx)):
                    if M[idx[a]][idx[b]] != 0:
                        pair = (idx[a], idx[b])
                        break
                if pair:
                    break
            if pair is None:
                zer += len(idx)
                break
            i, j = pair
            # e_i -> e_i + e_j makes M[i][i] = 2 M[i][j] != 0
            for c in range(len(M)):
                M[i][c] = M[i][c] + M[j][c]
            for r in range(len(M)):
                M[r][i] = M[r][i] + M[r][j]
            continue
        if M[k][k] > 0:
            pos += 1
        else:
            neg += 1
        piv = M[k][k]
        rest = [i for i in idx if i != k]
        for i in rest:
            f = M[i][k] / piv
            if f != 0:
                for c in range(len(M)):
                    M[i][c] -= f * M[k][c]
                for r in range(len(M)):
                    M[r][i] -= f * M[r][k]
        idx = rest
    return (pos, neg, zer)


def killing_form(basis, coord_fn):
    """B_ij = tr(ad X_i ad X_j), exact."""
    d = len(basis)
    ad = []
    for X in basis:
        cols = [coord_fn(bracket(X, Y)) for Y in basis]
        ad.append(transpose(cols))            # ad(X) acting on coordinate column vectors
    B = zeros(d)
    for i in range(d):
        for j in range(i, d):
            P = matmul(ad[i], ad[j])
            t = sum(P[k][k] for k in range(d))
            B[i][j] = B[j][i] = t
    return B


# --------------------------------------------------------------------------
# invariant symmetric forms  ->  number of simple ideals  ->  rank pi_3
# --------------------------------------------------------------------------

def structure_ad(basis):
    """ad(X_a) as d x d matrices in the given basis (exact)."""
    d = len(basis)
    ads = []
    for X in basis:
        cols = [solve_in_basis(basis, bracket(X, Y)) for Y in basis]
        ads.append(transpose(cols))
    return ads


def generated_subalgebra_dim(basis, gens):
    """dim of the Lie subalgebra generated by ``gens`` inside span(basis)."""
    cur = [g for g in gens]
    d = span_dim(cur)
    while True:
        new = list(cur)
        for A in cur:
            for B in gens:
                new.append(bracket(A, B))
        nd = span_dim(new)
        if nd == d:
            return d
        # keep an independent subset to stop the list exploding
        keep, rows = [], []
        for M in new:
            trial = rows + [flat(M)]
            if rank(trial) > len(rows):
                rows = rref(trial)[0]
                keep.append(M)
        cur, d = keep, nd


def invariant_symmetric_dim(basis, gen_indices):
    """dim of {B symmetric on the algebra : B(ad(X)u, v) + B(u, ad(X)v) = 0}.

    Invariance under a GENERATING set suffices: the set of X satisfying the
    condition is a Lie subalgebra (verified by the bracket identity
    ad([X,Y]) = ad X ad Y - ad Y ad X), so it contains the algebra they
    generate.  ``gen_indices`` must therefore be verified to generate.
    """
    d = len(basis)
    ads = structure_ad(basis)
    pairs = [(a, b) for a in range(d) for b in range(a, d)]
    pos = {pr: i for i, pr in enumerate(pairs)}

    def coeff(row, a, b, val):
        key = (a, b) if a <= b else (b, a)
        row[pos[key]] += val

    rows = []
    for g in gen_indices:
        A = ads[g]
        for b in range(d):
            for c in range(b, d):
                row = [Fraction(0)] * len(pairs)
                for e in range(d):
                    if A[e][b]:
                        coeff(row, e, c, A[e][b])
                    if A[e][c]:
                        coeff(row, b, e, A[e][c])
                if any(x != 0 for x in row):
                    rows.append(row)
    return len(pairs) - rank(rows)


def centre_dim(basis):
    d = len(basis)
    rows = []
    for Y in basis:
        for X in basis:
            rows.append(solve_in_basis(basis, bracket(X, Y)))
    # {c : sum_a c_a [X_b, X_a] = 0 for all b}
    eqs = []
    for b in range(d):
        cols = [solve_in_basis(basis, bracket(basis[b], A)) for A in basis]
        M = transpose(cols)
        eqs.extend(M)
    return d - rank(eqs)


def derived_dim(basis):
    return span_dim([bracket(A, B) for A in basis for B in basis])


# ==========================================================================
# THE RUN
# ==========================================================================

def run():
    R: dict = {}

    log("=" * 78)
    log("CH-3 chain repair -- independent reproduction of SC-A's group theory")
    log("=" * 78)

    # ---------------------------------------------------------------- 0. controls
    log("\n[0] POSITIVE CONTROLS -- the machinery before any result is read")

    E("0.1 signature of diag(1,-1) is (1,1,0)",
      signature([[1, 0], [0, -1]]) == (1, 1, 0))
    E("0.2 signature of the ZERO-DIAGONAL hyperbolic pair [[0,1],[1,0]] is (1,1,0)",
      signature([[0, 1], [1, 0]]) == (1, 1, 0),
      "the path that breaks naive implementations")
    E("0.3 signature of the zero form on R^2 is (0,0,2)",
      signature([[0, 0], [0, 0]]) == (0, 0, 2))
    E("0.4 signature of diag(2,3,-5,0) is (2,1,1)",
      signature([[2, 0, 0, 0], [0, 3, 0, 0], [0, 0, -5, 0], [0, 0, 0, 0]]) == (2, 1, 1))

    so3 = so_basis(3, 0)
    K_so3 = killing_form(so3, lambda X: so_coords(X, 3, 0))
    E("0.5 Killing form of the COMPACT so(3) is negative definite: (0,3,0)",
      signature(K_so3) == (0, 3, 0))
    so21 = so_basis(2, 1)
    K_so21 = killing_form(so21, lambda X: so_coords(X, 2, 1))
    E("0.6 Killing form of so(2,1) has signature (2,1,0)",
      signature(K_so21) == (2, 1, 0))

    # every so(p,q) basis element really satisfies the defining condition, and
    # the basis really closes under bracket
    ok_cond = ok_closed = True
    for (p, q) in [(3, 0), (2, 1), (5, 0), (3, 2), (6, 4)]:
        bas = so_basis(p, q)
        for X in bas:
            if not in_so(X, p, q):
                ok_cond = False
        for X in bas:
            for Y in bas:
                Z = bracket(X, Y)
                if not in_so(Z, p, q):
                    ok_closed = False
    E("0.7 every so(p,q) generator satisfies X^T eta + eta X = 0", ok_cond)
    E("0.8 every so(p,q) basis closes under the bracket", ok_closed)

    # ---------------------------------------------------------------- A. the dimension kill
    log("\n[A] THE NESTED READING -- killed by one integer")

    so32 = so_basis(3, 2)
    dim_so32 = planted("dim_so32", span_dim(so32), 12)
    R["dim_so32"] = dim_so32
    E("A.1 dim so(3,2) = 10, from an explicit bracket-closed basis",
      dim_so32 == 10, f"computed {dim_so32}")

    # g_SM built TWICE, independently
    su3 = []
    for j, k in combinations(range(3), 2):
        Re = zeros(3); Re[j][k] = 1; Re[k][j] = -1
        su3.append(realify(Re, zeros(3)))
        Im = zeros(3); Im[j][k] = 1; Im[k][j] = 1
        su3.append(realify(zeros(3), Im))
    for k in range(2):
        Im = zeros(3); Im[k][k] = 1; Im[k + 1][k + 1] = -1
        su3.append(realify(zeros(3), Im))
    su2 = []
    for j, k in combinations(range(2), 2):
        Re = zeros(2); Re[j][k] = 1; Re[k][j] = -1
        su2.append(realify(Re, zeros(2)))
        Im = zeros(2); Im[j][k] = 1; Im[k][j] = 1
        su2.append(realify(zeros(2), Im))
    Im = zeros(2); Im[0][0] = 1; Im[1][1] = -1
    su2.append(realify(zeros(2), Im))

    d_su3, d_su2 = span_dim(su3), span_dim(su2)
    dim_gsm = d_su3 + d_su2 + 1
    R["dim_su3"], R["dim_su2"], R["dim_gsm"] = d_su3, d_su2, dim_gsm
    E("A.2 dim su(3) = 8 from an explicit realified basis", d_su3 == 8)
    E("A.3 dim su(2) = 3 from an explicit realified basis", d_su2 == 3)
    E("A.4 dim(su(3) + su(2) + u(1)) = 12", dim_gsm == 12)

    E("A.5 THE KILL: 12 > 10, so no injective homomorphism g_SM -> so(3,2) exists",
      dim_gsm > dim_so32, f"{dim_gsm} > {dim_so32}")

    # sweep: no relabelling of (3,2) rescues it
    sweep = {}
    for p in range(6):
        q = 5 - p
        sweep[f"so({p},{q})"] = span_dim(so_basis(p, q))
    R["p_plus_q_5_dims"] = sweep
    E("A.6 SWEEP: every so(p,q) with p+q = 5 has dimension 10 -- signature cannot rescue",
      set(sweep.values()) == {10}, str(sweep))

    orth_dims = {n: span_dim(so_basis(n, 0)) for n in range(2, 8)}
    R["orthogonal_dims_by_n"] = orth_dims
    smallest = min(n for n, d in orth_dims.items() if d >= 12)
    R["smallest_n_with_dim_ge_12"] = smallest
    E("A.7 the smallest orthogonal algebra of dimension >= 12 is n = 6, at 15",
      smallest == 6 and orth_dims[6] == 15, str(orth_dims))

    C("A.8 CONTROL (must be FALSE): dim so(3,2) >= 12", dim_so32 >= 12,
      "if this were true the nested reading would survive")
    ctrl_A8 = dim_so32 >= 12

    # ---------------------------------------------------------------- B. the centraliser kill
    log("\n[B] THE FACTORISED READING -- killed by exhaustion over C^10")

    # sp(4,C) = so(5,C) irreps by the Weyl dimension formula on C_2, EXACT.
    # lambda = a w1 + b w2;  dim = (a+1)(b+1)(a+2b+3)(a+b+2)/6
    def c2_dim(a, b):
        num = (a + 1) * (b + 1) * (a + 2 * b + 3) * (a + b + 2)
        f = Fraction(num, 6)
        assert f.denominator == 1, "Weyl dimension must be an integer"
        return int(f)

    irreps = {}
    for a in range(0, 13):
        for b in range(0, 13):
            d = c2_dim(a, b)
            if d <= 10:
                irreps[(a, b)] = (d, "symplectic" if a % 2 else "orthogonal")
    R["c2_irreps_up_to_10"] = {f"({a},{b})": v for (a, b), v in sorted(irreps.items())}
    E("B.1 the C_2 irreps of dimension <= 10 are exactly 1, 4, 5, 10",
      sorted(d for d, _ in irreps.values()) == [1, 4, 5, 10], str(R["c2_irreps_up_to_10"]))
    E("B.2 Weyl formula positive controls: (1,1) -> 16 and (0,2) -> 14",
      c2_dim(1, 1) == 16 and c2_dim(0, 2) == 14)
    E("B.3 the 4 is symplectic type and the 1, 5, 10 are orthogonal type "
      "(central character (-1)^a)",
      irreps[(1, 0)][1] == "symplectic"
      and all(irreps[k][1] == "orthogonal" for k in [(0, 0), (0, 1), (2, 0)]))

    # enumerate every multiset of these irreps totalling 10
    dims = sorted({d for d, _ in irreps.values()})
    type_of = {}
    for (a, b), (d, t) in irreps.items():
        type_of[d] = t

    def enumerate_decomps(total, allowed):
        if total == 0:
            yield ()
            return
        for i, d in enumerate(allowed):
            if d <= total:
                for tail in enumerate_decomps(total - d, allowed[i:]):
                    yield (d,) + tail

    decomps = []
    for dec in enumerate_decomps(10, dims):
        mult = {}
        for d in dec:
            mult[d] = mult.get(d, 0) + 1
        # admissibility 1: a symplectic-type isotypic block needs EVEN multiplicity,
        # else the invariant symmetric form restricts to zero and degenerates
        sym_ok = all(m % 2 == 0 for d, m in mult.items() if type_of[d] == "symplectic")
        # admissibility 2: the module must be FAITHFUL (so(5,C) is simple, so any
        # nontrivial summand suffices; the all-trivial module is not faithful)
        faithful = any(d > 1 for d in mult)
        cent = 0
        for d, m in mult.items():
            cent += m * (m - 1) // 2 if type_of[d] == "orthogonal" else m * (m + 1) // 2
        decomps.append({
            "decomposition": "+".join(f"{d}^{m}" if m > 1 else str(d)
                                      for d, m in sorted(mult.items(), reverse=True)),
            "multiplicities": {str(d): m for d, m in sorted(mult.items())},
            "symplectic_parity_ok": sym_ok,
            "faithful": faithful,
            "admissible": sym_ok and faithful,
            "centraliser_dim": cent,
        })
    R["c10_decompositions"] = decomps

    admissible = [d for d in decomps if d["admissible"]]
    max_cent = planted("max_centraliser",
                       max(d["centraliser_dim"] for d in admissible), 12)
    R["max_centraliser_of_spin32_in_spin64"] = max_cent
    E("B.4 four decompositions of C^10 are admissible: 10, 5+5, 4^2+1^2, 5+1^5",
      sorted(d["decomposition"] for d in admissible)
      == sorted(["10", "5^2", "4^2+1^2", "5+1^5"]),
      str([d["decomposition"] for d in admissible]))
    E("B.5 max centraliser of ANY Spin(3,2) in Spin(6,4) = 10, attained at 5+1^5",
      max_cent == 10, f"computed {max_cent}")
    E("B.6 THE KILL: 12 > 10, so no Spin(3,2) in Spin(6,4) has a commuting g_SM",
      dim_gsm > max_cent, f"{dim_gsm} > {max_cent}")

    rej_451 = [d for d in decomps if d["decomposition"] == "5+4+1"]
    C("B.7 PLANTED CONTROL (must be FALSE): 5+4+1 is admissible",
      bool(rej_451) and rej_451[0]["admissible"],
      "odd multiplicity of the symplectic 4 degenerates the invariant symmetric form")
    ctrl_B7 = bool(rej_451) and rej_451[0]["admissible"]

    rej_110 = [d for d in decomps if d["decomposition"] == "1^10"]
    C("B.8 PLANTED CONTROL (must be FALSE): 1^10 is admissible",
      bool(rej_110) and rej_110[0]["admissible"],
      "so(5,C) would act trivially -- not a subalgebra of so(V) at all")
    ctrl_B8 = bool(rej_110) and rej_110[0]["admissible"]

    # contrary control: the SAME predicate must ACCEPT a true commuting pair
    row_515 = [d for d in decomps if d["decomposition"] == "5+1^5"][0]
    E("B.9 CONTRARY CONTROL (must be TRUE): the 5+1^5 row is admissible with "
      "centraliser 10 -- room for a SECOND Spin(3,2), not for g_SM",
      row_515["admissible"] and row_515["centraliser_dim"] == 10 >= 10)

    # ... and exhibit that second copy explicitly inside so(6,4)
    # standard eta_{6,4} = diag(1,1,1,1,1,1,-1,-1,-1,-1)
    def embed_so32(plus_idx, minus_idx):
        """so(3,2) on the coordinates (plus_idx | minus_idx) inside R^{6,4}."""
        cols = list(plus_idx) + list(minus_idx)
        out = []
        for X in so_basis(3, 2):
            M = zeros(10)
            for a in range(5):
                for b in range(5):
                    M[cols[a]][cols[b]] = X[a][b]
            out.append(M)
        return out

    copy1 = embed_so32([0, 1, 2], [6, 7])
    copy2 = embed_so32([3, 4, 5], [8, 9])
    both_in = all(in_so(X, 6, 4) for X in copy1 + copy2)
    commute = all(is_zero(bracket(X, Y)) for X in copy1 for Y in copy2)
    E("B.10 CONTRARY CONTROL exhibited: two block-diagonal so(3,2) copies sit in "
      "so(6,4) and commute elementwise",
      both_in and commute and span_dim(copy1) == span_dim(copy2) == 10)
    R["contrary_control_two_so32"] = {"each_dim": 10, "commute": commute, "in_so64": both_in}

    # ---------------------------------------------------------------- C. the surviving chain
    log("\n[C] THE SURVIVING CHAIN -- both arrows constructed")

    so64 = so_basis(6, 4)
    dim_so64 = span_dim(so64)
    R["dim_so64"] = dim_so64
    E("C.1 dim so(6,4) = 45", dim_so64 == 45)

    su32 = upq_real_in_so(3, 2, special=True)
    u32 = upq_real_in_so(3, 2, special=False)
    dim_su32, dim_u32 = span_dim(su32), span_dim(u32)
    R["dim_su32"], R["dim_u32"] = dim_su32, dim_u32
    E("C.2 realification is injective: dim su(3,2) = 24 and dim u(3,2) = 25 survive it",
      dim_su32 == 24 and dim_u32 == 25, f"{dim_su32} / {dim_u32}")

    all_skew = all(in_so(X, 6, 4) for X in u32)
    E("C.3 ARROW 1 CONSTRUCTED: every realified u(3,2) generator satisfies "
      "X^T eta_{6,4} + eta_{6,4} X = 0, so SU(3,2) < Spin(6,4)",
      all_skew and dim_su32 <= dim_so64, f"24 <= 45: {dim_su32 <= dim_so64}")
    closed_su32 = all(rank([flat(m) for m in su32] + [flat(bracket(X, Y))]) == dim_su32
                      for X, Y in [(su32[0], su32[7]), (su32[3], su32[20]), (su32[11], su32[23])])
    E("C.4 the realified su(3,2) is bracket-closed (sampled generator pairs)", closed_su32)

    # maximal compact = theta-fixed part, theta(X) = -X^T
    def theta_fixed(mats):
        base = [flat(m) for m in mats]
        d = rank(base)
        rows = []
        for m in mats:
            rows.append(flat(m))
        # solve for combinations c with (sum c_i X_i)^T = -(sum c_i X_i)
        cols = len(mats)
        eqs = []
        n = len(mats[0])
        for i in range(n):
            for j in range(n):
                eqs.append([mats[t][j][i] + mats[t][i][j] for t in range(cols)])
        ns = nullspace(eqs, cols)
        out = []
        for v in ns:
            M = zeros(n)
            for t, c in enumerate(v):
                if c:
                    for i in range(n):
                        for j in range(n):
                            M[i][j] += c * mats[t][i][j]
            out.append(M)
        assert d == span_dim(mats)
        return out

    k_so64 = theta_fixed(so64)
    dim_k_so64 = span_dim(k_so64)
    R["dim_maxcompact_so64"] = dim_k_so64
    E("C.5 maximal compact of so(6,4) is so(6)+so(4), dim 21", dim_k_so64 == 21)

    k_su32 = theta_fixed(su32)
    dim_k_su32 = planted("dim_k_su32", span_dim(k_su32), 4)
    R["dim_maxcompact_su32"] = dim_k_su32
    E("C.6 ARROW 2 CONSTRUCTED: the theta-fixed part of su(3,2) has dim 12 "
      "= dim(su(3)+su(2)+u(1))",
      dim_k_su32 == 12 == dim_gsm, f"computed {dim_k_su32}")

    d_der = derived_dim(k_su32)
    d_cen = centre_dim(k_su32)
    R["maxcompact_su32_derived"], R["maxcompact_su32_centre"] = d_der, d_cen
    E("C.7 it splits as 11 + 1: derived algebra su(3)+su(2) = 11, centre "
      "(hypercharge) = 1",
      d_der == 11 and d_cen == 1, f"derived {d_der}, centre {d_cen}")

    k_u32 = theta_fixed(u32)
    R["dim_maxcompact_u32"] = span_dim(k_u32)
    E("C.8 the theta-fixed part of u(3,2) is 13 = 12 + 1 -- eq (4.6)'s U(1) proviso",
      span_dim(k_u32) == 13)

    E("C.9 the chain's dimensions nest: 12 <= 24 <= 45",
      dim_k_su32 <= dim_su32 <= dim_so64)

    # ---------------------------------------------------------------- D. Killing signature
    log("\n[D] THE (6,4) FIBRE IS (so(3,2), B_Killing) -- unique in dimension 5")

    ksig = {}
    for p in range(6):
        q = 5 - p
        bas = so_basis(p, q)
        K = killing_form(bas, lambda X, p=p, q=q: so_coords(X, p, q))
        s = signature(K)
        ksig[f"so({p},{q})"] = [s[0], s[1], s[2]]
    R["killing_signatures_p_plus_q_5"] = ksig

    sig32 = planted("killing_sig", tuple(ksig["so(3,2)"]), (4, 6, 0))
    E("D.1 Killing form of so(3,2) has signature (6,4) -- the fibre signature",
      sig32 == (6, 4, 0), f"computed {sig32}")
    only64 = [k for k, v in ksig.items() if tuple(v) == (6, 4, 0)]
    R["p_plus_q_5_with_killing_64"] = sorted(only64)
    E("D.2 among p+q = 5 only so(3,2) and its relabel so(2,3) carry Killing "
      "signature (6,4)",
      sorted(only64) == ["so(2,3)", "so(3,2)"], str(only64))
    E("D.3 the compact and de Sitter forms do NOT: so(5,0) -> (0,10), so(4,1) -> (4,6)",
      tuple(ksig["so(5,0)"]) == (0, 10, 0) and tuple(ksig["so(4,1)"]) == (4, 6, 0))

    # ---------------------------------------------------------------- E. eq (4.6) intersections
    log("\n[E] THE eq (4.6) INTERSECTION, inside one so(6,4)")

    i_su = intersection_dim(k_so64, su32)
    i_u = intersection_dim(k_so64, u32)
    so32_block = embed_so32([0, 1, 2], [6, 7])
    i_so = intersection_dim(k_so64, so32_block)
    R["intersections"] = {
        "maxcompact_n_su32": i_su,
        "maxcompact_n_u32": i_u,
        "maxcompact_n_so32_block": i_so,
        "maxcompact_dim": dim_k_so64,
    }
    E("E.1 so(6)+so(4) n su(3,2) = 12 -- exactly the Standard Model algebra",
      i_su == 12, f"computed {i_su}")
    E("E.2 so(6)+so(4) n u(3,2) = 13 -- 'up to a reductive factor of U(1)'",
      i_u == 13, f"computed {i_u}")
    E("E.3 so(6)+so(4) n so(3,2) = 4 = dim(so(3)+so(2)) -- the garble reading, "
      "short by a factor of three",
      i_so == 4, f"computed {i_so}")
    C("E.4 PLANTED CONTROL (must be FALSE): the so(3,2) block intersection reaches 12",
      i_so == 12, "if it did, the nested reading would have a home")
    ctrl_E4 = (i_so == 12)

    # ---------------------------------------------------------------- F. rank pi_3
    log("\n[F] rank pi_3 ALONG THE CORRECTED CHAIN -- where the drop actually is")

    # split the maximal compact of so(6,4) into its two blocks and verify the split
    so6_block = []
    for X in so_basis(6, 0):
        M = zeros(10)
        for i in range(6):
            for j in range(6):
                M[i][j] = X[i][j]
        so6_block.append(M)
    so4_block = []
    for X in so_basis(4, 0):
        M = zeros(10)
        for i in range(4):
            for j in range(4):
                M[6 + i][6 + j] = X[i][j]
        so4_block.append(M)
    split_ok = (span_dim(so6_block) == 15 and span_dim(so4_block) == 6
                and span_dim(so6_block + so4_block) == 21
                and all(is_zero(bracket(A, B)) for A in so6_block for B in so4_block)
                and intersection_dim(k_so64, so6_block + so4_block) == 21)
    E("F.1 the maximal compact of so(6,4) is the direct sum so(6) (+) so(4), "
      "15 + 6 = 21, brackets between the blocks vanish", split_ok)

    # number of simple ideals, computed as dim of the space of invariant symmetric forms
    # L_{01}, L_{12}, L_{23}, L_{34}, L_{45} -- the simple-root chain.  Generation is
    # VERIFIED, not assumed: dropping L_{45} leaves coordinate 5 untouched and the
    # generated algebra is only so(5), which is exactly the control below.
    so6_raw = so_basis(6, 0)
    idx = {pair: i for i, pair in enumerate(combinations(range(6), 2))}
    so6_gens = [idx[(0, 1)], idx[(1, 2)], idx[(2, 3)], idx[(3, 4)], idx[(4, 5)]]
    gen_dim = generated_subalgebra_dim(so6_raw, [so6_raw[i] for i in so6_gens])
    R["so6_generated_dim"] = gen_dim
    E("F.2 the chosen so(6) elements generate so(6) (dim 15)", gen_dim == 15,
      f"computed {gen_dim}")
    short_dim = generated_subalgebra_dim(so6_raw, [so6_raw[i] for i in so6_gens[:-1]])
    C("F.2c PLANTED CONTROL (must be FALSE): the chain WITHOUT L_{45} still "
      "generates so(6)", short_dim == 15,
      f"it generates only so(5), dim {short_dim} -- the generation check has power")
    ctrl_F2 = (short_dim == 15)
    s_so6 = invariant_symmetric_dim(so6_raw, so6_gens)
    R["simple_ideals_so6"] = s_so6
    E("F.3 dim Inv-Sym(so(6)) = 1, so so(6) is simple: ONE ideal", s_so6 == 1)

    so4_raw = so_basis(4, 0)
    s_so4 = invariant_symmetric_dim(so4_raw, list(range(6)))
    R["simple_ideals_so4"] = s_so4
    E("F.4 dim Inv-Sym(so(4)) = 2, so so(4) = su(2)+su(2): TWO ideals", s_so4 == 2)

    rank_pi3_spin64 = s_so6 + s_so4
    R["rank_pi3_spin64"] = rank_pi3_spin64
    E("F.5 rank pi_3(Spin(6,4)) = rank pi_3(Spin(6)xSpin(4)) = 3",
      rank_pi3_spin64 == 3, "pi_3 of a connected Lie group = pi_3 of its maximal compact")

    # derived algebra of the maximal compact of su(3,2), as a basis
    der_mats = [bracket(A, B) for A in k_su32 for B in k_su32]
    der_basis, rows = [], []
    for M in der_mats:
        trial = rows + [flat(M)]
        if rank(trial) > len(rows):
            rows = rref(trial)[0]
            der_basis.append(M)
    E("F.6 the derived algebra of the maximal compact of su(3,2) has dim 11",
      len(der_basis) == 11)
    s_der = invariant_symmetric_dim(der_basis, list(range(len(der_basis))))
    rank_pi3_su32 = planted("rank_pi3_su32", s_der, 3)
    R["rank_pi3_su32"] = rank_pi3_su32
    E("F.7 dim Inv-Sym of that derived algebra = 2, so it is su(3)+su(2): TWO ideals, "
      "and rank pi_3(SU(3,2)) = 2",
      rank_pi3_su32 == 2, f"computed {rank_pi3_su32}")

    R["rank_pi3_S_U3xU2"] = rank_pi3_su32
    E("F.8 rank pi_3(S(U(3)xU(2))) = 2 as well -- arrow 2 is a deformation retract "
      "onto the maximal compact, so it CANNOT change pi_3",
      rank_pi3_su32 == 2)
    E("F.9 THE LOCALISATION: 3 -> 2 -> 2.  The rank drop is at ARROW 1 (the "
      "complex-structure reduction), not at arrow 2",
      rank_pi3_spin64 == 3 and rank_pi3_su32 == 2
      and (rank_pi3_spin64 - rank_pi3_su32) == 1)
    R["rank_pi3_chain"] = [rank_pi3_spin64, rank_pi3_su32, rank_pi3_su32]

    # ---------------------------------------------------------------- G. text gates
    log("\n[G] TEXTUAL GATES -- the source, and the two repaired sites")

    drafts = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text(encoding="utf-8")
    quotes = {
        "There is no grand unification": 1,
        "It's just a normal bundle in your ambient space": 1,
        "reduce maximal compact subgroups along the fibers": 1,
        "this has a complex structure": 1,
        "But this is the right chain": 1,
        "s u three comma two": 2,
        "spin three comma two": 1,
        "the maximal compact subgroup of spin six comma spin four": 1,
    }
    counts = {s: drafts.count(s) for s in quotes}
    R["source_string_counts"] = counts
    E("G.1 the source's GUT denial is verbatim present, once",
      counts["There is no grand unification"] == 1
      and counts["It's just a normal bundle in your ambient space"] == 1)
    E("G.2 the source's named operation 'reduce maximal compact subgroups along "
      "the fibers' is verbatim present", counts["reduce maximal compact subgroups along the fibers"] == 1)
    E("G.3 the transcript says 's u three comma two' TWICE and 'spin three comma "
      "two' ONCE",
      counts["s u three comma two"] == 2 and counts["spin three comma two"] == 1,
      str({k: counts[k] for k in ["s u three comma two", "spin three comma two"]}))
    E("G.4 the same speaker turn contains the provable ASR garble 'the maximal "
      "compact subgroup of spin six comma spin four', which names no group",
      counts["the maximal compact subgroup of spin six comma spin four"] == 1)

    h19 = (ROOT / "explorations/wave14/H19-seven-seven-signature-branch-2026-07-11.md").read_text(encoding="utf-8")
    la6 = (ROOT / "lab/active-research/joe-directed/ledger-advancement/"
                  "la6-the-lagrangian-axis-has-twelve-degrees-of-freedom-and-one-"
                  "constructible-cover-object-2026-08-15.md").read_text(encoding="utf-8")

    bad_forms = [
        "`Spin(6,4) -> Spin(3,2) -> maximal compact SU(3) x SU(2) x U(1)`",
        "`Spin(6,4) -> Spin(3,2) -> SU(3)xSU(2)xU(1)`",
        "`Spin(6,4)/Spin(3,2)` chain rides that invariant fiber",
        "*Weinstein's `spin(6,4) -> spin(3,2)` chain*",
    ]
    need_token = planted("site_repaired", "S(U(3)xU(2))",
                         "S(U(3)xU(2)) [PLANTED-TOKEN-THAT-IS-NOT-THERE]")
    E("G.5 the impossible nested form is GONE from H19 as an asserted chain",
      not any(b in h19 for b in bad_forms[:1] + bad_forms[2:]),
      "verbatim quotation of the source is not a repair target; assertion is")
    E("G.6 the impossible nested form is GONE from LA-6",
      bad_forms[1] not in la6)
    E("G.7 H19 now names the decided reading and its provenance",
      "SU(3,2)" in h19 and need_token in h19 and "SC-A" in h19)
    E("G.8 LA-6 now names the decided reading and its provenance",
      "SU(3,2)" in la6 and "sca-right-chain-2026-08-15" in la6)
    E("G.9 both sites state the CONSEQUENCE, not just the substitution",
      "structure-group reduction" in h19.lower().replace("structure group reduction",
                                                         "structure-group reduction")
      and "arrow" in la6.lower())
    E("G.10 H19's headline verdicts are untouched by the repair",
      "ODD-ADMISSIBLE" in h19 and "NOT-GU-NATIVE" in h19
      and "LIVE-BUT-NON-DERIVING" in h19)
    E("G.11 LA-6's Lagrangian-axis result is untouched by the repair",
      "the rank is 3, and the ledger has never assigned it one" in la6
      and "LAGRANGIAN_AXIS_EDOF_12" in la6)

    # ---------------------------------------------------------------- report
    log("\n" + "=" * 78)
    controls_required_false = {
        "A.8": ctrl_A8, "B.7": ctrl_B7, "B.8": ctrl_B8, "E.4": ctrl_E4,
        "F.2c": ctrl_F2,
    }
    R["planted_controls_that_must_be_false"] = {
        k: bool(v) for k, v in controls_required_false.items()
    }

    assert_no_float(R)

    n_e = sum(1 for kind, *_ in CHECKS if kind == "E")
    n_c = sum(1 for kind, *_ in CHECKS if kind == "C")
    failed_e = [(n, d) for kind, n, ok, d in CHECKS if kind == "E" and not ok]
    misbehaved_c = [k for k, v in controls_required_false.items() if v]

    for kind, name, ok, detail in CHECKS:
        if kind == "E":
            mark = "PASS" if ok else "FAIL"
        else:
            mark = "CONTROL-OK(false)" if not ok else "CONTROL-MISBEHAVED"
        log(f"  [{kind}] {mark:18s} {name}" + (f"   -- {detail}" if detail else ""))

    log("")
    log(f"  {n_e - len(failed_e)}/{n_e} exact checks PASS; "
        f"{n_c} planted controls, {len(misbehaved_c)} misbehaved")
    if PLANT:
        log(f"  PLANT ACTIVE: {PLANT} -- {PLANTS.get(PLANT, '?')}")
    log("=" * 78)

    if failed_e or misbehaved_c:
        for n, d in failed_e:
            log(f"  FAILED: {n} {d}")
        for k in misbehaved_c:
            log(f"  CONTROL MISBEHAVED (should be false): {k}")
        return 1
    return 0


def selftest():
    import subprocess
    ok = True
    for key, why in PLANTS.items():
        env = dict(os.environ, CH3_PLANT=key)
        proc = subprocess.run([sys.executable, __file__], env=env,
                              capture_output=True, text=True)
        got = proc.returncode
        good = (got == 1)
        ok = ok and good
        print(f"  plant {key:16s} exit {got}  expected 1  "
              f"{'OK' if good else 'SELFTEST FAILURE'}   ({why})")
    proc = subprocess.run([sys.executable, __file__], capture_output=True, text=True)
    clean_ok = (proc.returncode == 0)
    ok = ok and clean_ok
    print(f"  clean run        exit {proc.returncode}  expected 0  "
          f"{'OK' if clean_ok else 'SELFTEST FAILURE'}")
    print(f"\n  --selftest {'PASSED' if ok else 'FAILED'}: "
          f"{len(PLANTS)} planted false facts, each must force exit 1")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(run())

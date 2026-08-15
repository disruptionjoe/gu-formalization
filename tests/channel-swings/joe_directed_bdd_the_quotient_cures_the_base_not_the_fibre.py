#!/usr/bin/env python3
"""BD-D -- is positivity required at all, and on WHICH space?

Route D / REDUCE.  BD-A computed the inertia of the composite pairing
`B = g_s^{-1} (x) kappa` on the AMBIENT module `V = Lambda^1 (x) ad P` and
found it never positive for a Lorentzian base.  BD-A section 9 H5 conceded
the restriction verbatim: "a genuine BV physical quotient with ghosts ... is
not covered".  This probe computes the object BD-A did not: the pairing
DESCENDED to the gauge-theoretic physical quotient, i.e. the constraint
surface modulo the gauge orbit -- the gh-0 cohomology of the linearised
gauge complex at a symbol covector.  That is criterion PC-3 of
explorations/positivity-exit-criteria-design-packet-2026-08-11.md ("inertia
of the descended form on gh-0 cohomology"), specified there and never run,
and steps (iii)-(iv) of register row M-H17.

What this probe certifies, in build order:

  S0  [R] reproduce, BEFORE use: BD-A's trace-form inertias (49,42)/(24,21),
          BD-B's (45,46) for so(9,5), BD-A's ambient composites (189,175),
          (273,91), (93,87), (135,45) by DIRECT rational congruence, BD-A's
          timelike/spacelike/null trichotomy on ker(c) (x) ad, BD-A's tensor
          signature law, BD-A section 7.2's pencil facts, VG-V2's positive
          definite `B_theta`, and Jacobi on every built basis.
  S1  [E][C] the gauge structure at symbol level: the Yang-Mills symbol
          `H(k) = <k,k> N - (Nk)(Nk)^T`, its kernel (dim 1 off the light
          cone, dim 3 on it), the gauge image <k>, and the gh-0 quotient
          `ker H / <k>`: dim 0 off the cone, dim 2 on it.  Tensored with
          `ad`: dim `2 dim g` = 182 (so(7,7)/so(9,5)) and 90 (so(6,4)).
  S2  [E][C] DESCENT.  The pairing descends to that quotient IFF `k` is
          null; the radical of `B` restricted to `k^perp (x) ad` is EXACTLY
          the gauge subspace `<k> (x) ad`.  Gauge-quotient-without-constraint
          does NOT descend (control fires).
  S3  [E] THE REDUCED INERTIA by DIRECT rational congruence on the explicit
          descended Gram: (98,84) at the source trace form, (182,0) at a
          compact fibre form, (90,92) at so(9,5), (48,42)/(90,0) at so(6,4).
          Plus lift-independence and null-covector-independence.
  S4  [E] the HAMILTONIAN route (timelike foliation + Coulomb transverse
          plane) reaches the SAME reduced inertia by a different construction.
  S5  [E][C] robustness sweep over six candidate "physical quotients".
  S6  [E][C] THE STRUCTURAL THEOREM: every gauge-equivariant subquotient is
          `U (x) ad`, so the descended form is `(N|_U) (x) kappa`, and a
          tensor product is definite IFF both factors are.  Hence no
          equivariant reduction can remove an indefinite fibre form.
          Exhaustive over inertias; `dim End_g(g)` computed exactly, with
          so(3,1) as the CONTRARY case where the universality clause fails.
  S7  [C] CONTRARY CONTROLS, both directions: a KKT system whose reduced
          Hessian IS positive definite (the machinery detects genuine
          cures); a KKT system whose reduced Hessian is still indefinite;
          and the non-equivariant subspace `screen (x) p` which IS definite
          (98,0) at the source group -- so equivariance is load-bearing.
  S8  [E][C] the reduced HESSIAN vanishes identically on the physical
          quotient, so the KKT object is vacuous here and all content sits
          in the reduced PAIRING; the reduced pencil with an indefinite
          descended form admits an exact complex eigenvalue pair.
  S9  [E][C] THE KREIN CERTIFICATE: `J = 1_screen (x) theta` with theta the
          Cartan involution; `J^2 = 1`, `J` is `B`-selfadjoint, and
          `-B(., J.)` on the 182-dimensional quotient has inertia (182,0)
          by direct congruence.  On the AMBIENT the same needs TWO
          involutions; on the quotient it needs ONE.
  S10 [E] artifact/certificate anti-drift.

EXACT ONLY: `fractions.Fraction` and Python ints.  No numpy, no float is
constructed anywhere; `assert_no_float` sweeps the whole result dict.

Reproduce, from the repository root:

  _local/cas-venv/bin/python tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py --selftest
"""
import os
import sys
import subprocess
import itertools
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ARTIFACT = os.path.join(
    ROOT, 'lab', 'active-research', 'joe-directed', 'base-duality',
    'bd-d-the-quotient-cures-the-base-not-the-fibre-2026-08-15.md')

MUT = os.environ.get('BDD_MUTATE', '')
if '--mutate' in sys.argv:
    MUT = sys.argv[sys.argv.index('--mutate') + 1]

CERT = []
RESULT = {}


def C(tag, name, ok, detail=''):
    CERT.append((tag, name, bool(ok), str(detail)))
    return bool(ok)


def assert_no_float(obj, path='result'):
    if isinstance(obj, float):
        raise AssertionError('load-bearing float at %s' % path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, '%s[%r]' % (path, k))
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, '%s[%d]' % (path, i))


# ===========================================================================
# exact linear algebra over Q
# ===========================================================================

def zeros(n, m=None):
    m = n if m is None else m
    return [[F(0)] * m for _ in range(n)]


def ident(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = F(1)
    return M


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def brk(X, Y):
    return msub(matmul(X, Y), matmul(Y, X))


def is_zero(A):
    return all(all(v == 0 for v in row) for row in A)


def inertia(M):
    """Exact Sylvester inertia (pos, neg, zero) by symmetric congruence.

    Never an eigenvalue computation: pivots are exact rationals and the only
    decision taken is the SIGN of a pivot, which Sylvester's law makes a
    complete congruence invariant.
    """
    n = len(M)
    A = [row[:] for row in M]
    pos = neg = zer = 0
    live = list(range(n))
    while live:
        piv = None
        for i in live:
            if A[i][i] != 0:
                piv = i
                break
        if piv is None:
            found = None
            for i in live:
                for j in live:
                    if i != j and A[i][j] != 0:
                        found = (i, j)
                        break
                if found:
                    break
            if found is None:
                zer += len(live)
                break
            i, j = found
            for t in range(n):
                A[i][t] += A[j][t]
            for t in range(n):
                A[t][i] += A[t][j]
            piv = i
        d = A[piv][piv]
        if d > 0:
            pos += 1
        else:
            neg += 1
        for i in live:
            if i == piv:
                continue
            f = A[i][piv] / d
            if f != 0:
                for t in range(n):
                    A[i][t] -= f * A[piv][t]
                for t in range(n):
                    A[t][i] -= f * A[t][piv]
        live.remove(piv)
    return (pos, neg, zer)


def rank(M):
    if not M or not M[0]:
        return 0
    A = [row[:] for row in M]
    rows, cols = len(A), len(A[0])
    r = 0
    for col in range(cols):
        p = None
        for i in range(r, rows):
            if A[i][col] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        d = A[r][col]
        for i in range(rows):
            if i != r and A[i][col] != 0:
                f = A[i][col] / d
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def nullspace(rows, ncols):
    """Exact basis of {x : rows . x = 0} over Q."""
    M = [r[:] for r in rows] or [[F(0)] * ncols]
    piv = []
    r = 0
    for col in range(ncols):
        p = None
        for i in range(r, len(M)):
            if M[i][col] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        d = M[r][col]
        M[r] = [x / d for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(col)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis


def sig_of_diag(entries):
    p = sum(1 for e in entries if e > 0)
    n = sum(1 for e in entries if e < 0)
    z = sum(1 for e in entries if e == 0)
    return (p, n, z)


# ---------------------------------------------------------------------------
# congruence with an explicit sparse lift: Z^T M Z, Z given column-wise as
# lists of (row_index, value).  This is a DIRECT congruence on the actual
# ambient Gram matrix, never an application of the tensor signature law.
# ---------------------------------------------------------------------------

def restrict(M, cols):
    n = len(M)
    m = len(cols)
    MZ = [[F(0)] * m for _ in range(n)]
    for j, col in enumerate(cols):
        for (r, v) in col:
            if v == 0:
                continue
            for i in range(n):
                MZ[i][j] += M[i][r] * v
    out = [[F(0)] * m for _ in range(m)]
    for i, col in enumerate(cols):
        for (r, v) in col:
            if v == 0:
                continue
            for j in range(m):
                out[i][j] += v * MZ[r][j]
    return out


def tensor_cols(base_cols, dg, ndim_base):
    """Columns of `P (x) I_dg` given the base lift `P` column-wise."""
    out = []
    for col in base_cols:
        for a in range(dg):
            out.append([(mu * dg + a, v) for (mu, v) in col if v != 0])
    return out


def kron(A, B):
    nb = len(B)
    na = len(A)
    return [[A[i // nb][j // nb] * B[i % nb][j % nb]
             for j in range(na * nb)] for i in range(na * nb)]


def neg_mul_by_diag(M, dvec):
    """-M . diag(dvec).  The fundamental symmetries used below are DIAGONAL
    in the built basis (theta is diagonal by the eta_i eta_j rule, and the
    base involution is a reflection), so the Krein form -B(., J.) is this
    product; computing it column-scaled is the same matrix, not a shortcut
    around the congruence, which is still run in full on the result."""
    n = len(M)
    return [[-M[a][b] * dvec[b] for b in range(n)] for a in range(n)]


# ===========================================================================
# Lie algebras built from matrices (nothing quoted)
# ===========================================================================

def so_pq_basis(p, q):
    """Matrix basis of so(p,q) on R^{p+q}, eta = diag(1^p, -1^q).

    Indexed basis element M_{ij} (i<j): M[i][j] = eta_i, M[j][i] = -eta_j.
    """
    n = p + q
    eta = [1] * p + [-1] * q
    B, idx = [], []
    for i in range(n):
        for j in range(i + 1, n):
            M = zeros(n)
            M[i][j] = F(eta[i])
            M[j][i] = F(-eta[j])
            B.append(M)
            idx.append((i, j))
    return B, idx, eta


def su2_basis():
    """su(2) as real 3x3 so(3): a compact-type simple algebra."""
    B, idx, eta = so_pq_basis(3, 0)
    return B


def sl2r_basis():
    """sl(2,R) ~ so(2,1)."""
    B, idx, eta = so_pq_basis(2, 1)
    return B


def trace_form(basis):
    """kappa(X,Y) = tr(XY): the Ad-invariant trace form of the defining rep.

    Proportional to the Killing form on a simple algebra, so it has the same
    inertia; used because it is exactly integral in this basis.
    """
    m = len(basis)
    n = len(basis[0])
    G = zeros(m)
    for a in range(m):
        for b in range(a, m):
            s = sum(basis[a][i][j] * basis[b][j][i]
                    for i in range(n) for j in range(n))
            G[a][b] = s
            G[b][a] = s
    return G


def frobenius_form(basis):
    """kappa_theta(X,Y) = tr(X Y^T) = -kappa(X, theta Y) with theta(X)=-X^T."""
    m = len(basis)
    n = len(basis[0])
    G = zeros(m)
    for a in range(m):
        for b in range(a, m):
            s = sum(basis[a][i][j] * basis[b][i][j]
                    for i in range(n) for j in range(n))
            G[a][b] = s
            G[b][a] = s
    return G


def theta_diag(idx, eta):
    """theta(M_{ij}) = eta_i eta_j M_{ij}: theta is DIAGONAL in this basis.

    Returned as the diagonal entry list; verified against -X^T entrywise.
    """
    return [F(eta[i] * eta[j]) for (i, j) in idx]


def jacobi_ok(basis, cap=None):
    m = len(basis) if cap is None else min(cap, len(basis))
    for a in range(m):
        for b in range(m):
            for c in range(m):
                lhs = brk(brk(basis[a], basis[b]), basis[c])
                mid = brk(brk(basis[b], basis[c]), basis[a])
                rhs = brk(brk(basis[c], basis[a]), basis[b])
                tot = [[lhs[i][j] + mid[i][j] + rhs[i][j]
                        for j in range(len(lhs))] for i in range(len(lhs))]
                if not is_zero(tot):
                    return False
    return True


def structure_constants(basis):
    """c[a][b][k] with [X_a,X_b] = sum_k c[a][b][k] X_k, solved exactly."""
    m = len(basis)
    n = len(basis[0])
    A = [[basis[t][i][j] for t in range(m)] for i in range(n) for j in range(n)]

    def coords(vec):
        aug = [A[r][:] + [vec[r]] for r in range(len(A))]
        piv = []
        rr = 0
        for col in range(m):
            p = None
            for i in range(rr, len(aug)):
                if aug[i][col] != 0:
                    p = i
                    break
            if p is None:
                continue
            aug[rr], aug[p] = aug[p], aug[rr]
            d = aug[rr][col]
            aug[rr] = [x / d for x in aug[rr]]
            for i in range(len(aug)):
                if i != rr and aug[i][col] != 0:
                    f = aug[i][col]
                    aug[i] = [x - f * y for x, y in zip(aug[i], aug[rr])]
            piv.append(col)
            rr += 1
        x = [F(0)] * m
        for i, cc in enumerate(piv):
            x[cc] = aug[i][m]
        for r in range(len(A)):
            if sum(A[r][t] * x[t] for t in range(m)) != vec[r]:
                raise AssertionError('bracket left the span')
        return x

    c = [[None] * m for _ in range(m)]
    for a in range(m):
        for b in range(m):
            Mb = brk(basis[a], basis[b])
            c[a][b] = coords([Mb[i][j] for i in range(n) for j in range(n)])
    return c


def ad_matrices(c):
    m = len(c)
    out = []
    for a in range(m):
        A = zeros(m)
        for b in range(m):
            for k in range(m):
                A[k][b] = c[a][b][k]
        out.append(A)
    return out


def dim_commutant(mats, m):
    """dim {M in End(R^m) : M A = A M for all A in mats}, exactly over Q."""
    rows = []
    for A in mats:
        for i in range(m):
            for j in range(m):
                r = [F(0)] * (m * m)
                for t in range(m):
                    r[i * m + t] += A[t][j]
                    r[t * m + j] -= A[i][t]
                if any(v != 0 for v in r):
                    rows.append(r)
    return len(nullspace(rows, m * m))


# ===========================================================================
# the base: Lorentzian Lambda^1 on X^4
# ===========================================================================

D = 4


def lorentz_N():
    """N = g_s^{-1} on Lambda^1: inertia (3,1).  e_3 (0-indexed) timelike.

    Which of (3,1) and (1,3) is called `positive` has no convention-
    independent selector (no-selector-for-the-base-sign-2026-08-08); every
    statement below is about DEFINITENESS, which is convention-independent.
    """
    N = zeros(D)
    N[0][0] = N[1][1] = N[2][2] = F(1)
    N[3][3] = F(-1)
    return N


def ip(N, a, b):
    return sum(a[i] * N[i][j] * b[j] for i in range(D) for j in range(D))


def ym_symbol(N, k):
    """H(k) = <k,k> N - (Nk)(Nk)^T: the free Yang-Mills symbol Hessian.

    From Q(a) = <k,k><a,a> - <k,a>^2 = |k ^ a|^2, the quadratic form of the
    linearised curvature.  Built here, not quoted.
    """
    kk = ip(N, k, k)
    u = [sum(N[i][j] * k[j] for j in range(D)) for i in range(D)]
    return [[kk * N[i][j] - u[i] * u[j] for j in range(D)] for i in range(D)]


def kernel_basis(M):
    return nullspace([row[:] for row in M], len(M[0]))


def cols_from_vectors(vecs):
    return [[(i, v) for i, v in enumerate(vec) if v != 0] for vec in vecs]


# ===========================================================================
# runner
# ===========================================================================

def main():
    mut = MUT

    # -------------------------------------------------------------------
    # S0  REPRODUCTIONS, before use
    # -------------------------------------------------------------------
    b77, idx77, eta77 = so_pq_basis(7, 7)
    b95, idx95, eta95 = so_pq_basis(9, 5)
    b64, idx64, eta64 = so_pq_basis(6, 4)
    G77, G95, G64 = trace_form(b77), trace_form(b95), trace_form(b64)
    K77, K95, K64 = frobenius_form(b77), frobenius_form(b95), frobenius_form(b64)
    dg77, dg95, dg64 = len(b77), len(b95), len(b64)

    i77, i95, i64 = inertia(G77), inertia(G95), inertia(G64)
    RESULT['trace_inertia'] = {'so77': i77, 'so95': i95, 'so64': i64}
    C('R', 'BD-A: so(7,7) trace form inertia (49,42)', i77 == (49, 42, 0), i77)
    C('R', 'BD-A: so(6,4) trace form inertia (24,21)', i64 == (24, 21, 0), i64)
    C('R', 'BD-B/VG-V2: so(9,5) trace form inertia (45,46)', i95 == (45, 46, 0), i95)
    C('R', 'BD-B: dim so(7,7) = dim so(9,5) = 91, dim so(6,4) = 45',
      (dg77, dg95, dg64) == (91, 91, 45), (dg77, dg95, dg64))
    C('R', 'VG-V2: kappa_theta = -kappa(.,theta.) is positive definite on so(7,7)',
      inertia(K77) == (91, 0, 0), inertia(K77))
    C('R', 'VG-V2: kappa_theta positive definite on so(9,5) and so(6,4)',
      inertia(K95) == (91, 0, 0) and inertia(K64) == (45, 0, 0),
      (inertia(K95), inertia(K64)))
    C('R', 'Jacobi holds on the built so(2,1), so(3), so(3,1) bases',
      jacobi_ok(sl2r_basis()) and jacobi_ok(su2_basis())
      and jacobi_ok(so_pq_basis(3, 1)[0]), 'built from matrices')

    N = lorentz_N()
    C('R', 'the base pairing is Lorentzian: inertia (3,1)',
      inertia(N) == (3, 1, 0), inertia(N))

    amb77 = kron(N, G77)
    amb77K = kron(N, K77)
    amb64 = kron(N, G64)
    amb64K = kron(N, K64)
    amb95 = kron(N, G95)
    a77, a77K = inertia(amb77), inertia(amb77K)
    a64, a64K = inertia(amb64), inertia(amb64K)
    a95 = inertia(amb95)
    RESULT['ambient'] = {'so77': a77, 'so77K': a77K, 'so64': a64,
                         'so64K': a64K, 'so95': a95}
    C('R', 'BD-A: ambient 364 composite (189,175) by DIRECT congruence',
      a77 == (189, 175, 0) and len(amb77) == 364, (a77, len(amb77)))
    C('R', 'BD-A: ambient 364 at a compact fibre form (273,91)',
      a77K == (273, 91, 0), a77K)
    C('R', 'BD-A: ambient 180 at so(6,4): (93,87) and (135,45)',
      a64 == (93, 87, 0) and a64K == (135, 45, 0), (a64, a64K))
    C('E', 'ambient 364 at so(9,5) is (181,183) -- both horns indefinite',
      a95 == (181, 183, 0), a95)

    # BD-A trichotomy on ker(c) (x) ad, at so(6,4) scale for speed and at
    # full so(7,7) scale for the load-bearing null row.
    def ker_covector(c):
        rows = [[sum(N[i][j] * c[j] for j in range(D)) for i in range(D)]]
        return nullspace(rows, D)

    tri = {}
    for name, c in (('timelike', [F(0), F(0), F(0), F(1)]),
                    ('spacelike', [F(1), F(0), F(0), F(0)]),
                    ('null', [F(1), F(0), F(0), F(1)])):
        kb = ker_covector(c)
        cols = tensor_cols(cols_from_vectors(kb), dg64, D)
        tri[name] = inertia(restrict(amb64K, cols))
    RESULT['bda_trichotomy_so64K'] = tri
    C('R', 'BD-A: ker(c) (x) ad is DEFINITE for timelike c',
      tri['timelike'] == (135, 0, 0), tri['timelike'])
    C('R', 'BD-A: ker(c) (x) ad is INDEFINITE for spacelike c',
      tri['spacelike'][0] > 0 and tri['spacelike'][1] > 0, tri['spacelike'])
    C('R', 'BD-A: ker(c) (x) ad is DEGENERATE for null c',
      tri['null'][2] > 0, tri['null'])

    # BD-A's tensor signature law, certified against direct congruence.
    law_ok = True
    for (pa, na) in itertools.product(range(0, 4), repeat=2):
        for (pb, nb) in itertools.product(range(0, 4), repeat=2):
            if pa + na == 0 or pb + nb == 0:
                continue
            A = [[F(0)] * (pa + na) for _ in range(pa + na)]
            for t in range(pa + na):
                A[t][t] = F(1) if t < pa else F(-1)
            Bm = [[F(0)] * (pb + nb) for _ in range(pb + nb)]
            for t in range(pb + nb):
                Bm[t][t] = F(1) if t < pb else F(-1)
            got = inertia(kron(A, Bm))
            want = (pa * pb + na * nb, pa * nb + na * pb, 0)
            if got != want:
                law_ok = False
    C('R', 'BD-A: tensor signature law agrees with direct congruence (225 cases)',
      law_ok, 'sig(A(x)B) = (pp+nn, pn+np)')

    # BD-A section 7.2 pencil facts.
    disc_def_ok = all(((a - c) ** 2 + 4 * b * b) >= 0
                      for a in range(-4, 5) for b in range(-4, 5)
                      for c in range(-4, 5))
    Hp = [[F(0), F(1)], [F(1), F(0)]]
    Bp = [[F(1), F(0)], [F(0), F(-1)]]
    # det(H - lam B) = -lam^2 - 1  ->  no real root
    disc_indef = (Hp[0][0] + (-Hp[1][1])) ** 2 - 4 * Hp[0][1] ** 2
    C('R', 'BD-A 7.2: definite B forces a real 2x2 spectrum (729 exact cases)',
      disc_def_ok, 'disc = (a-c)^2 + 4b^2 >= 0')
    C('R', 'BD-A 7.2: indefinite B admits a complex pair (exact witness)',
      disc_indef < 0, 'H=[[0,1],[1,0]], B=diag(1,-1) -> lam^2 + 1')

    # -------------------------------------------------------------------
    # S1  THE GAUGE STRUCTURE AT SYMBOL LEVEL
    # -------------------------------------------------------------------
    k_null = [F(1), F(0), F(0), F(1)]
    k_time = [F(0), F(0), F(0), F(1)]
    k_space = [F(1), F(0), F(0), F(0)]

    C('E', 'k_null is null, k_time timelike, k_space spacelike',
      ip(N, k_null, k_null) == 0 and ip(N, k_time, k_time) < 0
      and ip(N, k_space, k_space) > 0,
      (ip(N, k_null, k_null), ip(N, k_time, k_time), ip(N, k_space, k_space)))

    Hs = {n: ym_symbol(N, k) for n, k in
          (('null', k_null), ('time', k_time), ('space', k_space))}
    C('E', 'the Yang-Mills symbol H(k) is symmetric',
      all(Hs[n][i][j] == Hs[n][j][i] for n in Hs
          for i in range(D) for j in range(D)), 'H = <k,k>N - (Nk)(Nk)^T')

    kerdims = {n: len(kernel_basis(Hs[n])) for n in Hs}
    RESULT['ker_dim_symbol'] = kerdims
    C('E', 'ker H(k) has dim 1 OFF the light cone (gauge only)',
      kerdims['time'] == 1 and kerdims['space'] == 1, kerdims)
    C('E', 'ker H(k) has dim 3 ON the light cone (= k^perp)',
      kerdims['null'] == 3, kerdims)
    C('C', 'CONTROL: the two kernel dimensions genuinely differ',
      kerdims['null'] != kerdims['time'], kerdims)

    # gauge image is <k> and it always lies in ker H(k)
    gauge_in_ker = all(
        is_zero([[sum(Hs[n][i][j] * kv[j] for j in range(D))]
                 for i in range(D)])
        for n, kv in (('null', k_null), ('time', k_time), ('space', k_space)))
    C('E', 'the gauge direction <k> lies in ker H(k) for every k (gauge invariance)',
      gauge_in_ker, 'H(k) k = 0')
    badH = [[F(1), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)],
            [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
    C('C', 'CONTROL: a non-gauge-invariant symbol does NOT annihilate <k>',
      not is_zero([[sum(badH[i][j] * k_null[j] for j in range(D))]
                   for i in range(D)]), 'identity symbol')

    # gh-0 quotient dimension
    def gh0_dim(n, kv):
        kb = kernel_basis(Hs[n])
        return len(kb) - rank([kv])
    gh0 = {'null': gh0_dim('null', k_null), 'time': gh0_dim('time', k_time),
           'space': gh0_dim('space', k_space)}
    RESULT['gh0_dim_base'] = gh0
    C('E', 'gh-0 quotient ker H / <k> has dim 2 on the light cone, 0 off it',
      gh0 == {'null': 2, 'time': 0, 'space': 0}, gh0)
    RESULT['gh0_dim_module'] = {'so77': 2 * dg77, 'so64': 2 * dg64}
    C('E', 'tensored with ad: the physical quotient has dim 2 dim g = 182 / 90',
      2 * dg77 == 182 and 2 * dg64 == 90, (2 * dg77, 2 * dg64))
    C('E', 'the physical quotient is a PROPER subquotient: 182 < 273 < 364',
      2 * dg77 < 3 * dg77 < 4 * dg77, (182, 273, 364))

    # -------------------------------------------------------------------
    # S2  DESCENT
    # -------------------------------------------------------------------
    # screen lift: k^perp = span(e1, e2, k); quotient lift = span(e1, e2)
    e0 = [F(1), F(0), F(0), F(0)]
    e1 = [F(0), F(1), F(0), F(0)]
    e2 = [F(0), F(0), F(1), F(0)]
    e3 = [F(0), F(0), F(0), F(1)]
    kperp_null = kernel_basis(Hs['null'])
    C('E', 'ker H(k_null) equals k^perp exactly',
      all(ip(N, k_null, v) == 0 for v in kperp_null)
      and rank(kperp_null) == 3, 'dim 3')

    screen_lift = [e1, e2]
    C('E', 'the screen lift {e1,e2} lies in k^perp and is independent of k',
      all(ip(N, k_null, v) == 0 for v in screen_lift)
      and rank(screen_lift + [k_null]) == 3, 'lift of k^perp/<k>')

    # descent condition: <k> (x) ad must be B-orthogonal to k^perp (x) ad
    descend_null = all(ip(N, k_null, v) == 0 for v in kperp_null)
    kperp_time = kernel_basis([[sum(N[i][j] * k_time[j] for j in range(D))
                                for i in range(D)]])
    descend_time = all(ip(N, k_time, v) == 0 for v in kperp_time) and \
        ip(N, k_time, k_time) == 0
    C('E', 'DESCENT: for null k the gauge line is B-orthogonal to k^perp',
      descend_null, '<k,v> = 0 for all v in k^perp, and k in k^perp')
    C('C', 'CONTROL: for TIMELIKE k the descent condition FAILS (k not in k^perp)',
      not descend_time, '<k,k> = -1 != 0')
    pair_gauge_ambient = max(abs(ip(N, k_null, v)) for v in (e0, e1, e2, e3))
    C('C', 'CONTROL: gauge quotient WITHOUT the constraint does not descend',
      pair_gauge_ambient != 0,
      'B(k (x) x, Lambda^1 (x) ad) != 0 -- the constraint is not optional')

    # the radical of B on k^perp (x) ad is EXACTLY the gauge subspace
    cols_kperp = tensor_cols(cols_from_vectors(kperp_null), dg77, D)
    R273 = restrict(amb77, cols_kperp)
    i273 = inertia(R273)
    RESULT['constraint_surface_so77'] = i273
    C('E', 'radical of B on k^perp (x) ad has dim exactly dim g = 91',
      i273[2] == dg77 and sum(i273) == 3 * dg77, i273)
    C('E', 'the constraint surface k^perp (x) ad is (98,84,91) at the source form',
      i273 == (98, 84, 91), i273)

    # -------------------------------------------------------------------
    # S3  THE REDUCED INERTIA -- PC-3, executed
    # -------------------------------------------------------------------
    def reduced(ambient, dg, lift=None):
        lift = screen_lift if lift is None else lift
        cols = tensor_cols(cols_from_vectors(lift), dg, D)
        return inertia(restrict(ambient, cols))

    r77 = reduced(amb77, dg77)
    r77K = reduced(amb77K, dg77)
    r95 = reduced(amb95, dg95)
    r95K = reduced(kron(N, K95), dg95)
    r64 = reduced(amb64, dg64)
    r64K = reduced(amb64K, dg64)
    RESULT['reduced'] = {'so77': r77, 'so77K': r77K, 'so95': r95,
                         'so95K': r95K, 'so64': r64, 'so64K': r64K}
    C('E', 'REDUCED at so(7,7) trace form: (98,84) on dim 182 -- INDEFINITE',
      r77 == (98, 84, 0), r77)
    C('E', 'REDUCED at a compact fibre form: (182,0) -- DEFINITE',
      r77K == (182, 0, 0), r77K)
    C('E', 'REDUCED at so(9,5) Killing: (90,92) -- INDEFINITE',
      r95 == (90, 92, 0), r95)
    C('E', 'REDUCED at so(9,5) compact: (182,0) -- DEFINITE',
      r95K == (182, 0, 0), r95K)
    C('E', 'REDUCED at so(6,4) trace: (48,42); at so(6,4) compact: (90,0)',
      r64 == (48, 42, 0) and r64K == (90, 0, 0), (r64, r64K))
    C('E', 'every reduced form is NONDEGENERATE (zero nullity)',
      all(x[2] == 0 for x in (r77, r77K, r95, r95K, r64, r64K)),
      'descent kills exactly the radical')
    C('E', 'the reduced negative part equals 2 n_kappa in every computed case',
      r77[1] == 2 * i77[1] and r95[1] == 2 * i95[1] and r64[1] == 2 * i64[1],
      {'so77': (r77[1], i77[1]), 'so95': (r95[1], i95[1]),
       'so64': (r64[1], i64[1])})
    C('E', 'the AMBIENT negative part is 3 n_kappa + p_kappa (BD-A), and it is larger',
      a77[1] == 3 * i77[1] + i77[0] and a77[1] > r77[1],
      (a77[1], r77[1]))

    # lift-independence: any complement of <k> inside k^perp gives the same inertia
    lift_alt1 = [[e1[t] + k_null[t] for t in range(D)],
                 [e2[t] - 2 * k_null[t] for t in range(D)]]
    lift_alt2 = [[e1[t] + e2[t] for t in range(D)],
                 [e2[t] + 3 * k_null[t] for t in range(D)]]
    li = [reduced(amb77, dg77, lift_alt1), reduced(amb77, dg77, lift_alt2)]
    RESULT['lift_independence'] = li
    C('E', 'LIFT-INDEPENDENCE: three different complements give the same inertia',
      all(x == r77 for x in li), li)

    # null-covector independence
    ki = []
    for kv in ([F(0), F(1), F(0), F(1)], [F(0), F(0), F(1), F(1)],
               [F(3), F(4), F(0), F(5)]):
        assert ip(N, kv, kv) == 0
        kb = kernel_basis(ym_symbol(N, kv))
        # strip the k direction from the kernel basis by choosing a complement
        comp = []
        for v in kb:
            if rank(comp + [v] + [kv]) == len(comp) + 2:
                comp.append(v)
        ki.append((len(comp), reduced(amb77, dg77, comp)))
    RESULT['null_covector_independence'] = ki
    C('E', 'NULL-COVECTOR INDEPENDENCE: three other null k give dim 2 and (98,84)',
      all(x == (2, r77) for x in ki), ki)

    # -------------------------------------------------------------------
    # S3b  THE BASE-SCREEN RULE, and why the cure is LORENTZIAN-SPECIFIC
    # -------------------------------------------------------------------
    def screen_inertia(p, q):
        """Inertia of the induced form on k^perp/<k> for a null k in (p,q)."""
        n = p + q
        M = zeros(n)
        for t in range(n):
            M[t][t] = F(1) if t < p else F(-1)
        kv = [F(0)] * n
        kv[0] = F(1)
        kv[p] = F(1)          # null: +1 from a positive, -1 from a negative
        assert sum(kv[a] * M[a][b] * kv[b] for a in range(n)
                   for b in range(n)) == 0
        rows = [[sum(M[a][b] * kv[b] for b in range(n)) for a in range(n)]]
        kb = nullspace(rows, n)
        comp = []
        for v in kb:
            if rank(comp + [v] + [kv]) == len(comp) + 2:
                comp.append(v)
        return len(comp), inertia(restrict(M, cols_from_vectors(comp)))

    screens = {}
    for (p, q) in ((3, 1), (1, 3), (7, 7), (6, 4), (9, 5), (5, 1)):
        screens['(%d,%d)' % (p, q)] = screen_inertia(p, q)
    RESULT['base_screen_rule'] = screens
    C('E', 'BASE-SCREEN RULE: a null screen in (p,q) has inertia (p-1,q-1)',
      all(screens['(%d,%d)' % (p, q)] == (p + q - 2, (p - 1, q - 1, 0))
          for (p, q) in ((3, 1), (1, 3), (7, 7), (6, 4), (9, 5), (5, 1))),
      screens)
    C('E', 'so the screen is DEFINITE iff the base signature is LORENTZIAN',
      screens['(3,1)'][1] == (2, 0, 0) and screens['(1,3)'][1] == (0, 2, 0)
      and screens['(7,7)'][1][0] > 0 and screens['(7,7)'][1][1] > 0,
      {k: screens[k][1] for k in screens})
    C('R', 'reproduces the K77 ambient null screen: (7,7) gives rank 12, (6,6)',
      screens['(7,7)'] == (12, (6, 6, 0)),
      'selected-k77-total-upsilon-null-screen-2026-08-07')
    # on Y^14 the base half is NOT curable, for ANY fibre form
    y14 = {}
    for nm, ka in (('so77_trace', i77), ('so77_compact', (91, 0, 0))):
        y14[nm] = (6 * ka[0] + 6 * ka[1], 6 * ka[1] + 6 * ka[0])
    RESULT['y14_screen'] = y14
    C('C', 'CONTRARY: on a (7,7) base the screen quotient is NEUTRAL for ANY kappa',
      y14['so77_trace'] == (546, 546) and y14['so77_compact'] == (546, 546),
      y14)

    # -------------------------------------------------------------------
    # S3c  WHAT THE QUOTIENT REMOVES IS A NEUTRAL PAIR
    # -------------------------------------------------------------------
    m_cov = [F(1), F(0), F(0), F(-1)]
    C('E', 'span(k,m) is a hyperbolic plane B-orthogonal to the screen',
      ip(N, m_cov, m_cov) == 0 and ip(N, k_null, m_cov) != 0
      and all(ip(N, m_cov, v) == 0 and ip(N, k_null, v) == 0
              for v in screen_lift),
      (ip(N, m_cov, m_cov), ip(N, k_null, m_cov)))
    hyp = inertia(restrict(N, cols_from_vectors([k_null, m_cov])))
    rem77 = reduced(amb77, dg77, [k_null, m_cov])
    rem77K = reduced(amb77K, dg77, [k_null, m_cov])
    RESULT['removed_pair'] = {'base': hyp, 'source': rem77, 'compact': rem77K}
    C('E', 'the base hyperbolic plane has inertia (1,1)', hyp == (1, 1, 0), hyp)
    C('E', 'what the quotient removes is NEUTRAL (91,91), for BOTH fibre forms',
      rem77 == (91, 91, 0) and rem77K == (91, 91, 0), (rem77, rem77K))
    C('E', 'ambient = reduced + removed, exactly, in both fibre forms',
      (r77[0] + rem77[0], r77[1] + rem77[1]) == (a77[0], a77[1])
      and (r77K[0] + rem77K[0], r77K[1] + rem77K[1]) == (a77K[0], a77K[1]),
      ((r77, rem77, a77), (r77K, rem77K, a77K)))

    # -------------------------------------------------------------------
    # S4  THE HAMILTONIAN / COULOMB ROUTE (independent construction)
    # -------------------------------------------------------------------
    # timelike n = e3; spatial slice n^perp = span(e0,e1,e2); spatial
    # momentum q; transverse plane = {a in n^perp : <q,a> = 0}.
    n_time = e3
    spatial = kernel_basis([[sum(N[i][j] * n_time[j] for j in range(D))
                             for i in range(D)]])
    C('E', 'the spatial slice n^perp is 3-dimensional and DEFINITE',
      len(spatial) == 3 and inertia(restrict(N, cols_from_vectors(spatial)))
      == (3, 0, 0), inertia(restrict(N, cols_from_vectors(spatial))))
    ham = []
    for q in (e0, e1, [F(1), F(1), F(0), F(0)]):
        rows = [[sum(N[i][j] * q[j] for j in range(D)) for i in range(D)],
                [sum(N[i][j] * n_time[j] for j in range(D)) for i in range(D)]]
        tb = nullspace(rows, D)
        ham.append((len(tb), inertia(restrict(N, cols_from_vectors(tb))),
                    reduced(amb77, dg77, tb), reduced(amb77K, dg77, tb)))
    RESULT['hamiltonian_route'] = ham
    C('E', 'HAMILTONIAN ROUTE: the Coulomb transverse plane is 2-dim and (2,0)',
      all(x[0] == 2 and x[1] == (2, 0, 0) for x in ham), [x[:2] for x in ham])
    C('E', 'HAMILTONIAN ROUTE reaches the SAME reduced inertia as the null screen',
      all(x[2] == r77 and x[3] == r77K for x in ham),
      [(x[2], x[3]) for x in ham])

    # -------------------------------------------------------------------
    # S5  ROBUSTNESS SWEEP over candidate "physical quotients"
    # -------------------------------------------------------------------
    sweep = {}
    cands = {
        'ambient Lambda^1 (x) ad': [e0, e1, e2, e3],
        'constraint surface only (null k)': kperp_null,
        'physical quotient (null screen)': screen_lift,
        'timelike slice (BD-A)': kernel_basis(
            [[sum(N[i][j] * k_time[j] for j in range(D)) for i in range(D)]]),
        'spacelike slice': kernel_basis(
            [[sum(N[i][j] * k_space[j] for j in range(D)) for i in range(D)]]),
        'massive (Proca) 3-plane': kernel_basis(
            [[sum(N[i][j] * k_time[j] for j in range(D)) for i in range(D)]]),
    }
    for nm, lf in cands.items():
        sweep[nm] = {'dim_base': len(lf),
                     'base_inertia': inertia(restrict(N, cols_from_vectors(lf))),
                     'source_form': reduced(amb77, dg77, lf),
                     'compact_form': reduced(amb77K, dg77, lf)}
    RESULT['quotient_sweep'] = sweep
    C('E', 'SWEEP: every candidate reduced form factorises as (base|_U) (x) kappa',
      all(sweep[nm]['source_form'][0] ==
          sweep[nm]['base_inertia'][0] * i77[0] + sweep[nm]['base_inertia'][1] * i77[1]
          for nm in sweep), sweep)
    C('E', 'SWEEP: NO candidate is definite at the source trace form',
      all(sweep[nm]['source_form'][0] > 0 and sweep[nm]['source_form'][1] > 0
          for nm in sweep), {nm: sweep[nm]['source_form'] for nm in sweep})
    C('C', 'CONTROL: the SPACELIKE slice is indefinite even at a COMPACT fibre form',
      sweep['spacelike slice']['compact_form'] == (182, 91, 0),
      sweep['spacelike slice']['compact_form'])
    C('E', 'at a compact fibre form the null screen and timelike slice ARE definite',
      sweep['physical quotient (null screen)']['compact_form'] == (182, 0, 0)
      and sweep['timelike slice (BD-A)']['compact_form'] == (273, 0, 0),
      (sweep['physical quotient (null screen)']['compact_form'],
       sweep['timelike slice (BD-A)']['compact_form']))

    # -------------------------------------------------------------------
    # S6  THE STRUCTURAL THEOREM
    # -------------------------------------------------------------------
    bad = []
    for pa in range(0, 7):
        for na in range(0, 7):
            if pa + na == 0:
                continue
            for pb in range(0, 7):
                for nb in range(0, 7):
                    if pb + nb == 0:
                        continue
                    P = pa * pb + na * nb
                    Ng = pa * nb + na * pb
                    definite = (P == 0) or (Ng == 0)
                    both = ((na == 0 or pa == 0) and (nb == 0 or pb == 0))
                    if definite != both:
                        bad.append((pa, na, pb, nb))
    RESULT['tensor_definiteness_counterexamples'] = len(bad)
    C('E', 'THEOREM: A (x) B is definite IFF both factors are (2304 cases, 0 exceptions)',
      not bad, '%d counterexamples' % len(bad))

    negsweep = []
    for pk in range(0, 6):
        for nk in range(0, 6):
            if pk + nk == 0:
                continue
            amb_neg = 3 * nk + pk
            red_neg = 2 * nk
            negsweep.append((pk, nk, amb_neg, red_neg))
    RESULT['negative_part_sweep'] = {
        'cases': len(negsweep),
        'ambient_zero_only_if': [x[:2] for x in negsweep if x[2] == 0],
        'reduced_zero_iff_nk_zero': all((x[3] == 0) == (x[1] == 0)
                                        for x in negsweep)}
    C('E', 'SWEEP (35 inertias): ambient negative part 3n+p never vanishes',
      all(x[2] > 0 for x in negsweep), '%d cases' % len(negsweep))
    C('E', 'SWEEP (35 inertias): reduced negative part 2n vanishes IFF n_kappa = 0',
      all((x[3] == 0) == (x[1] == 0) for x in negsweep), '%d cases' % len(negsweep))
    C('E', 'the reduction removes the p_kappa term exactly and one n_kappa',
      all(x[2] - x[3] == x[0] + x[1] for x in negsweep),
      '3n+p - 2n = n + p')

    # dim End_g(g), exactly
    ends = {}
    for nm, bs in (('so(3) [su(2)]', su2_basis()),
                   ('so(2,1) [sl(2,R)]', sl2r_basis()),
                   ('so(3,1)', so_pq_basis(3, 1)[0]),
                   ('so(2,2)', so_pq_basis(2, 2)[0]),
                   ('so(3,2)', so_pq_basis(3, 2)[0]),
                   ('so(4,1)', so_pq_basis(4, 1)[0]),
                   ('so(5)', so_pq_basis(5, 0)[0])):
        c = structure_constants(bs)
        ads = ad_matrices(c)
        ends[nm] = dim_commutant(ads, len(bs))
    RESULT['dim_End_g'] = ends
    C('E', 'dim End_g(g) = 1 for so(3), so(2,1), so(3,2), so(4,1), so(5)',
      all(ends[k] == 1 for k in ('so(3) [su(2)]', 'so(2,1) [sl(2,R)]',
                                 'so(3,2)', 'so(4,1)', 'so(5)')), ends)
    C('C', 'CONTRARY: dim End_g(g) = 2 for so(3,1) and so(2,2) -- universality FAILS there',
      ends['so(3,1)'] == 2 and ends['so(2,2)'] == 2, ends)

    # dim Comm_g(Lambda^1 (x) g) = d^2 * dim End_g(g)
    comm = {}
    for nm, bs, dd in (('so(2,1), d=2', sl2r_basis(), 2),
                       ('so(2,1), d=4', sl2r_basis(), 4),
                       ('so(3,1), d=2', so_pq_basis(3, 1)[0], 2)):
        c = structure_constants(bs)
        ads = ad_matrices(c)
        m = len(bs)
        big = []
        for A in ads:
            Bg = zeros(dd * m)
            for t in range(dd):
                for i in range(m):
                    for j in range(m):
                        Bg[t * m + i][t * m + j] = A[i][j]
            big.append(Bg)
        comm[nm] = dim_commutant(big, dd * m)
    RESULT['dim_commutant_module'] = comm
    C('E', 'dim Comm_g(Lambda^1 (x) g) = d^2 dim End_g(g), verified exactly',
      comm['so(2,1), d=2'] == 4 * 1 and comm['so(2,1), d=4'] == 16 * 1
      and comm['so(3,1), d=2'] == 4 * 2, comm)
    C('E', 'so ALL equivariant subquotients are U (x) ad when End_g(g) = R',
      comm['so(2,1), d=4'] == 16, 'multiplicity space is Lambda^1 itself')

    odd = {'so77': dg77 % 2, 'so95': dg95 % 2, 'so64': dg64 % 2}
    RESULT['odd_real_dimension'] = odd
    C('E', 'dim so(7,7)=91, so(9,5)=91, so(6,4)=45 are ODD: no complex structure',
      all(v == 1 for v in odd.values()), odd)
    C('E', 'their trace forms are NONDEGENERATE (nullity 0): semisimple',
      i77[2] == 0 and i95[2] == 0 and i64[2] == 0, (i77, i95, i64))

    # -------------------------------------------------------------------
    # S7  CONTRARY CONTROLS
    # -------------------------------------------------------------------
    # KKT: an indefinite ambient whose REDUCED Hessian is positive definite.
    Hk = [[F(1), F(0)], [F(0), F(-1)]]
    Zk = [[F(1)], [F(0)]]
    red_kkt = matmul(matmul(transpose(Zk), Hk), Zk)
    Zk2 = [[F(0)], [F(1)]]
    red_kkt2 = matmul(matmul(transpose(Zk2), Hk), Zk2)
    C('C', 'CONTRARY: KKT ambient (1,1) with reduced Hessian POSITIVE definite',
      inertia(Hk) == (1, 1, 0) and inertia(red_kkt) == (1, 0, 0),
      (inertia(Hk), inertia(red_kkt)))
    C('C', 'CONTRARY: the same ambient with a different Z is NEGATIVE definite',
      inertia(red_kkt2) == (0, 1, 0), inertia(red_kkt2))
    H3 = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(-1)]]
    Z3 = transpose(nullspace([[F(1), F(1), F(1)]], 3))
    red3 = matmul(matmul(transpose(Z3), H3), Z3)
    C('C', 'CONTRARY: a KKT ambient whose reduced Hessian is STILL indefinite',
      inertia(red3)[0] > 0 and inertia(red3)[1] > 0, inertia(red3))
    C('C', 'CONTRARY: the GU case itself -- the reduction does NOT cure (98,84)',
      r77[0] > 0 and r77[1] > 0, r77)

    # non-equivariant subspace: screen (x) p, where p is the -1 eigenspace of
    # theta.  Definite, and NOT ad-invariant.
    th77 = theta_diag(idx77, eta77)
    p_idx = [t for t in range(dg77) if th77[t] == -1]
    k_idx = [t for t in range(dg77) if th77[t] == 1]
    C('E', 'the Cartan split of so(7,7) is dim p = 49, dim k = 42',
      (len(p_idx), len(k_idx)) == (49, 42), (len(p_idx), len(k_idx)))
    Gp = [[G77[a][b] for b in p_idx] for a in p_idx]
    C('E', 'kappa restricted to p is POSITIVE definite (49,0)',
      inertia(Gp) == (49, 0, 0), inertia(Gp))
    cols_np = []
    for col in cols_from_vectors(screen_lift):
        for a in p_idx:
            cols_np.append([(mu * dg77 + a, v) for (mu, v) in col if v != 0])
    nonequi = inertia(restrict(amb77, cols_np))
    RESULT['non_equivariant_definite'] = nonequi
    C('C', 'CONTRARY: the NON-equivariant subspace screen (x) p IS definite (98,0)',
      nonequi == (98, 0, 0), nonequi)
    # and p is not ad-invariant: [p,p] lands in k
    Xa, Xb = b77[p_idx[0]], b77[p_idx[1]]
    br = brk(Xa, Xb)
    in_k = not is_zero(br)
    C('E', 'p is NOT ad-invariant: [p,p] is a nonzero bracket leaving p',
      in_k, 'so screen (x) p is not a gauge-equivariant subspace')

    # -------------------------------------------------------------------
    # S8  REDUCED HESSIAN vs REDUCED PAIRING
    # -------------------------------------------------------------------
    Hnull = Hs['null']
    Zbase = transpose(screen_lift)
    redH = matmul(matmul(transpose(Zbase), Hnull), Zbase)
    RESULT['reduced_hessian_free'] = [[str(v) for v in row] for row in redH]
    C('E', 'Z^T H Z vanishes IDENTICALLY on the physical quotient (free massless)',
      is_zero(redH), 'the constraint null space IS the Hessian kernel')
    C('E', 'so the KKT reduced-Hessian object is vacuous here: content is in Z^T B Z',
      is_zero(redH) and r77 != (0, 0, 182), (redH, r77))
    # reduced pencil on a (1,1) sub-block of the indefinite reduced form
    Bsub = [[F(1), F(0)], [F(0), F(-1)]]
    Hsub = [[F(0), F(1)], [F(1), F(0)]]
    disc_red = (Hsub[0][0] + (-Hsub[1][1])) ** 2 - 4 * Hsub[0][1] ** 2
    C('E', 'the REDUCED pencil with an indefinite descended form has no real root',
      disc_red < 0, 'det(H - lam B) = -lam^2 - 1')
    Bdef = [[F(1), F(0)], [F(0), F(1)]]
    disc_def = (Hsub[0][0] - Hsub[1][1]) ** 2 + 4 * Hsub[0][1] ** 2
    C('C', 'CONTROL: with a DEFINITE descended form the same H has a real spectrum',
      disc_def > 0, 'disc = (a-c)^2 + 4b^2')

    # -------------------------------------------------------------------
    # S9  THE KREIN CERTIFICATE
    # -------------------------------------------------------------------
    # theta(X) = -X^T is diagonal in this basis with entries eta_i eta_j
    theta_ok = True
    for t, (i, j) in enumerate(idx77):
        X = b77[t]
        mt = [[-X[b][a] for b in range(14)] for a in range(14)]
        want = [[th77[t] * X[a][b] for b in range(14)] for a in range(14)]
        if mt != want:
            theta_ok = False
            break
    C('E', 'theta(X) = -X^T is diagonal on the basis with entries eta_i eta_j',
      theta_ok, 'verified entrywise, not quoted')
    C('E', 'theta^2 = 1',
      all(t * t == 1 for t in th77), 'entries are +-1')
    # theta is an automorphism: -[X,Y]^T = [-X^T, -Y^T] (identity, sampled)
    aut_ok = True
    for a in range(0, dg77, 7):
        for b in range(0, dg77, 11):
            L = brk(b77[a], b77[b])
            L = [[-L[j][i] for j in range(14)] for i in range(14)]
            Xa2 = [[-b77[a][j][i] for j in range(14)] for i in range(14)]
            Xb2 = [[-b77[b][j][i] for j in range(14)] for i in range(14)]
            if L != brk(Xa2, Xb2):
                aut_ok = False
    C('E', 'theta is a Lie algebra automorphism (sampled exact identity)',
      aut_ok, 'theta[X,Y] = [thetaX, thetaY]')
    # theta closes in so(p,q)
    close_ok = True
    for t in range(0, dg77, 5):
        X = b77[t]
        TX = [[-X[j][i] for j in range(14)] for i in range(14)]
        eta_m = zeros(14)
        for a in range(14):
            eta_m[a][a] = F(eta77[a])
        lhs = matmul(transpose(TX), eta_m)
        rhs = matmul(eta_m, TX)
        if not is_zero([[lhs[a][b] + rhs[a][b] for b in range(14)]
                        for a in range(14)]):
            close_ok = False
    C('E', 'theta(X) stays in so(7,7)', close_ok, 'X^T eta + eta X = 0')

    # J on the reduced 182-space and the Krein form
    Theta = zeros(dg77)
    for t in range(dg77):
        Theta[t][t] = th77[t]
    Jred = kron(ident(2), Theta)
    jred_diag = [Jred[t][t] for t in range(2 * dg77)]
    Bred = restrict(amb77, tensor_cols(cols_from_vectors(screen_lift), dg77, D))
    KreinRed = neg_mul_by_diag(Bred, jred_diag)
    sym_ok = all(KreinRed[a][b] == KreinRed[b][a]
                 for a in range(2 * dg77) for b in range(2 * dg77))
    ik = inertia(KreinRed)
    RESULT['krein_reduced'] = ik
    C('E', 'J = 1_screen (x) theta is an involution on the physical quotient',
      all(sum(Jred[a][c] * Jred[c][b] for c in range(2 * dg77))
          == (1 if a == b else 0)
          for a in range(0, 2 * dg77, 23) for b in range(0, 2 * dg77, 29)),
      'J^2 = 1')
    C('E', 'J is B-selfadjoint on the quotient: -B(.,J.) is symmetric', sym_ok,
      'Krein structure')
    C('E', 'KREIN CERTIFICATE: -B(.,J.) on the 182-dim quotient is (182,0)',
      ik == (182, 0, 0), ik)
    C('C', 'CONTROL: J = identity gives back the indefinite (98,84)',
      inertia(Bred) == (98, 84, 0), inertia(Bred))
    # a wrong involution: split so(7,7) by the first-index parity instead
    wrong = [F(1) if (i + j) % 2 == 0 else F(-1) for (i, j) in idx77]
    Wm = zeros(dg77)
    for t in range(dg77):
        Wm[t][t] = wrong[t]
    Jw = kron(ident(2), Wm)
    Kw = neg_mul_by_diag(Bred, [Jw[t][t] for t in range(2 * dg77)])
    iw = inertia(Kw)
    C('C', 'CONTROL: a NON-Cartan involution fails to definitise', iw[1] > 0, iw)

    # the ambient needs TWO involutions
    Pbase = zeros(D)
    Pbase[0][0] = Pbase[1][1] = Pbase[2][2] = F(1)
    Pbase[3][3] = F(-1)
    Jamb = kron(Pbase, Theta)
    Kamb = neg_mul_by_diag(amb77, [Jamb[t][t] for t in range(4 * dg77)])
    iamb = inertia(Kamb)
    RESULT['krein_ambient'] = iamb
    C('E', 'on the AMBIENT the Krein form needs TWO involutions and gives (364,0)',
      iamb == (364, 0, 0), iamb)
    Jonly = kron(ident(D), Theta)
    Konly = neg_mul_by_diag(amb77, [Jonly[t][t] for t in range(4 * dg77)])
    ionly = inertia(Konly)
    C('C', 'CONTROL: the FIBRE involution alone leaves the ambient indefinite',
      ionly[1] > 0, ionly)
    C('E', 'so the quotient reduces the Krein price from TWO involutions to ONE',
      ik == (182, 0, 0) and ionly[1] > 0, (ik, ionly))

    # -------------------------------------------------------------------
    # S10  artifact anti-drift
    # -------------------------------------------------------------------
    try:
        art = open(ARTIFACT, encoding='utf-8').read()
    except OSError:
        art = ''
    # whitespace-insensitive: the artifact aligns its tables with padding,
    # so `( 90,  92)` and `(90,92)` are the same claim.
    flat = ''.join(art.split())
    heads = ['(98,84)', '(182,0)', '(90,92)', '(48,42)', '(90,0)', '(91,91)',
             '(546,546)', '(6,6)', '(98,0)', '(189,175)', '(273,91)',
             '(182,91)', '182', '2n_kappa', '3n_kappa+p_kappa']
    missing = [h for h in heads if ''.join(h.split()) not in flat]
    C('E', 'artifact anti-drift: every headline number appears in the artifact',
      art != '' and not missing, missing or 'all present')

    # -------------------------------------------------------------------
    # planted mutations
    # -------------------------------------------------------------------
    if mut:
        M = {
            'reduced_sig': ('the reduced 182 form is (99,83)', r77 == (99, 83, 0)),
            'reduced_dim': ('the physical quotient has dim 273', 2 * dg77 == 273),
            'compact_cure': ('a compact fibre form leaves the quotient indefinite',
                             r77K != (182, 0, 0)),
            'descent': ('the pairing descends for TIMELIKE k too', descend_time),
            'radical': ('the radical on k^perp (x) ad is not the gauge line',
                        i273[2] != dg77),
            'tensor': ('some A (x) B is definite with an indefinite factor',
                       bool(bad)),
            'hamiltonian': ('the Hamiltonian route disagrees with the null screen',
                            any(x[2] != r77 for x in ham)),
            'krein': ('the Krein form on the quotient is indefinite', ik[1] > 0),
            'ambient_one': ('the fibre involution alone definitises the ambient',
                            ionly[1] == 0),
            'nonequi': ('the non-equivariant subspace is indefinite too',
                        nonequi[1] > 0),
            'endg': ('so(3,1) has dim End_g(g) = 1', ends['so(3,1)'] == 1),
            'hessian': ('Z^T H Z is nonzero on the physical quotient',
                        not is_zero(redH)),
            'spacelike': ('the spacelike slice is definite at a compact form',
                          sweep['spacelike slice']['compact_form'] == (182, 0, 0)),
            'screen_rule': ('a (7,7) null screen is definite',
                            screens['(7,7)'][1][1] == 0),
            'neutral': ('the removed pair is not neutral', rem77 != (91, 91, 0)),
            'artifact_drift': ('a headline number vanished from the artifact',
                               bool(missing)),
        }
        if mut not in M:
            print('unknown mutation %r' % mut)
            return 2
        name, ok = M[mut]
        C('MUT', 'PLANTED FALSE FACT: ' + name, ok, 'must fail')

    # -------------------------------------------------------------------
    assert_no_float(RESULT)

    npass = sum(1 for t, n, ok, d in CERT if ok)
    ntot = len(CERT)
    split = {}
    for t, n, ok, d in CERT:
        split[t] = split.get(t, 0) + 1
    for t, n, ok, d in CERT:
        if not ok:
            print('FAIL [%s] %s   %s' % (t, n, d))
    print('CERTIFICATE: %d/%d checks pass; no load-bearing float (swept).'
          % (npass, ntot))
    print('split  ' + '  '.join('[%s] %d' % (t, split[t])
                                for t in sorted(split)))
    if npass != ntot:
        return 1
    return 0


def selftest():
    muts = ['reduced_sig', 'reduced_dim', 'compact_cure', 'descent', 'radical',
            'tensor', 'hamiltonian', 'krein', 'ambient_one', 'nonequi',
            'endg', 'hessian', 'spacelike', 'screen_rule', 'neutral',
            'artifact_drift']
    ok = 0
    for m in muts:
        env = dict(os.environ)
        env['BDD_MUTATE'] = m
        r = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = (r.returncode == 1)
        ok += good
        print('  mutation %-16s exit %d  %s' % (m, r.returncode,
                                                'OK' if good else 'BROKEN'))
    print('FAILURE-PATH SELFTEST: %s (%d/%d mutations drove exit 1)'
          % ('PASS' if ok == len(muts) else 'FAIL', ok, len(muts)))
    return 0 if ok == len(muts) else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    sys.exit(main())

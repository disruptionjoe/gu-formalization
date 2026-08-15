#!/usr/bin/env python3
"""BD-A -- construct the base duality named by `LT-GR6b`'s revival trigger.

Route A / CONSTRUCT.  The target object is the one three routes converged on
(OT-1 clause `O4` factor (b), OT-2's bucket, LA-11's proposed row `LT-GR6b`):

    "a source-owned global base duality on the observed X^4, a density
     together with a nondegenerate Lambda^1 pairing, composed with an
     Ad-invariant fibre form at a NAMED group subscript into a
     Gamma(Ad P)-equivariant pairing on Lambda^1 tensor ad P that is
     positive on the physical quotient"

What this probe certifies, in build order:

  S0  [R] reproduce, before use: OT-1/LA-11's invariant-form theorem on the
          ALGEBRA Lie(W) = g |x (Lambda^1 (x) ad); dim so(6,4) = 45 (LA-11's
          correction); so(3,1) trace-form inertia (3,3) (reproduces
          selected-k77-lorentzian-chiral-class-pairing-2026-08-10);
          chi(S^4) = 2 (reproduces selected-k77-physical-section-faithfulness-
          gate-2026-08-08).
  S1  [E] the MODULE/ALGEBRA separation.  W-invariant symmetric forms on the
          MODULE V = Lambda^1 (x) ad number d(d+1)/2 and every d has a
          NONDEGENERATE one, while on the ALGEBRA Lie(W) they number d+1 with
          max rank 2 dim g.  Same group, two domains, opposite answers.
  S2  [E] the construction: B = N (x) kappa, its Ad(g)-invariance and its
          W-invariance (the V-directions act trivially on V -- verified, not
          assumed), and its nondegeneracy.
  S3  [E] exact inertias at GU scale: so(7,7) -> (49,42); the 364-dimensional
          composite by DIRECT rational congruence -> (189,175); at a compact
          (K-reduced) fibre form -> (273,91).  Same at so(6,4)/180.
  S4  [E][C] positivity: a Lorentzian base pairing admits NO positive
          composite for ANY nonzero fibre form; an Ad-invariant positive
          fibre form exists iff the algebra is of compact type.
  S5  [E][C] the 273: ker(c) (x) ad is definite iff c is timelike, indefinite
          iff spacelike, degenerate iff null.  Its dimension is exactly
          OT-1's unpaired remainder.
  S6  [E][C] raising is inert on-shell: for nondegenerate B the zero sets of
          E and B^{-1}E coincide, and d(B^{-1}E) at a zero equals B^{-1} Hess
          -- so the section-dependence of B cannot obstruct the Euler system.
  S7  [E][C] where it is NOT inert: the pencil det(H - lambda B).  Definite B
          forces a real spectrum; indefinite B admits an exact complex pair.
  S8  [E] the trigger's two conjuncts are not independent: a nondegenerate
          Lambda^1 pairing determines the density.
  S9  [E] "global" has exact content: a global section of Met_Lor(X^4) is a
          line field on X^4; for closed X^4 that is chi(X^4) = 0.
  S10 [E] artifact/certificate anti-drift: the headline numbers are read back
          out of the artifact.

EXACT ONLY: `fractions.Fraction` and Python ints.  No numpy, no float is
constructed anywhere; `assert_no_float` sweeps the whole result dict.

Reproduce, from the repository root:

  _local/cas-venv/bin/python tests/channel-swings/joe_directed_bda_base_duality_construction.py
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_bda_base_duality_construction.py --selftest
"""
import os
import sys
import subprocess
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ARTIFACT = os.path.join(
    ROOT, 'lab', 'active-research', 'joe-directed', 'base-duality',
    'bd-a-the-base-duality-is-the-observation-and-positivity-is-the-'
    'obstruction-2026-08-15.md')

MUT = os.environ.get('BDA_MUTATE', '')
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


def trace_of_product(A, B):
    """tr(A B) without forming the product."""
    n = len(A)
    return sum(A[a][b] * B[b][a] for a in range(n) for b in range(n))


def kron(A, B):
    nb = len(B)
    na = len(A)
    return [[A[i // nb][j // nb] * B[i % nb][j % nb]
             for j in range(na * nb)] for i in range(na * nb)]


def inertia(M):
    """Exact Sylvester inertia (pos, neg, zero) by symmetric congruence."""
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
    M = [r[:] for r in rows]
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


def sym_index(n):
    idx = {}
    k = 0
    for i in range(n):
        for j in range(i, n):
            idx[(i, j)] = k
            idx[(j, i)] = k
            k += 1
    return idx, k


def mat_from_vec(v, idx, n):
    return [[v[idx[(i, j)]] for j in range(n)] for i in range(n)]


def max_rank_over_span(basis, idx, n, ns):
    """Deterministic lower bound on the maximum rank attained on a span,
    always reported together with an exact structural upper bound."""
    best = 0
    trials = [[F(1)] * len(basis)]
    trials += [[F(1) if i == j else F(0) for i in range(len(basis))]
               for j in range(len(basis))]
    trials += [[F(1 + 7 * i) for i in range(len(basis))]]
    trials += [[F((-1) ** i * (i * i + 1)) for i in range(len(basis))]]
    for co in trials:
        v = [sum(co[t] * basis[t][s] for t in range(len(basis)))
             for s in range(ns)]
        best = max(best, rank(mat_from_vec(v, idx, n)))
    return best


# ===========================================================================
# Lie algebras built from structure constants (nothing quoted)
# ===========================================================================

def so_pq_basis(p, q):
    """Matrix basis of so(p,q) acting on R^{p+q} with eta = diag(1^p,-1^q)."""
    n = p + q
    eta = [1] * p + [-1] * q
    B = []
    for i in range(n):
        for j in range(i + 1, n):
            M = zeros(n)
            M[i][j] = F(eta[i])
            M[j][i] = F(-eta[j])
            B.append(M)
    return B


def structure_constants(basis):
    """c[a][b][k] with [X_a, X_b] = sum_k c[a][b][k] X_k, solved exactly."""
    m = len(basis)
    n = len(basis[0])
    cols = []
    for M in basis:
        cols.append([M[i][j] for i in range(n) for j in range(n)])
    c = [[[F(0)] * m for _ in range(m)] for _ in range(m)]
    # Precompute a solve for the coordinate map by Gaussian elimination on the
    # (n*n) x m matrix whose columns are the basis elements.
    A = [[cols[t][r] for t in range(m)] for r in range(n * n)]

    def coords(vec):
        aug = [A[r][:] + [vec[r]] for r in range(n * n)]
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
                    aug[i] = [a - f * b for a, b in zip(aug[i], aug[rr])]
            piv.append(col)
            rr += 1
        out = [F(0)] * m
        for i, pc in enumerate(piv):
            out[pc] = aug[i][m]
        return out

    for a in range(m):
        for b in range(a + 1, m):
            P = matmul(basis[a], basis[b])
            Q = matmul(basis[b], basis[a])
            vec = [P[i][j] - Q[i][j] for i in range(n) for j in range(n)]
            cc = coords(vec)
            for k in range(m):
                c[a][b][k] = cc[k]
                c[b][a][k] = -cc[k]
    return c


def sl2R():
    """sl(2,R): basis e, f, h with [h,e]=2e, [h,f]=-2f, [e,f]=h."""
    m = 3
    c = [[[F(0)] * m for _ in range(m)] for _ in range(m)]

    def s(i, j, k, v):
        c[i][j][k] = F(v)
        c[j][i][k] = F(-v)
    s(2, 0, 0, 2)
    s(2, 1, 1, -2)
    s(0, 1, 2, 1)
    return m, c


def su2():
    """su(2): [X1,X2]=X3 and cyclic."""
    m = 3
    c = [[[F(0)] * m for _ in range(m)] for _ in range(m)]

    def s(i, j, k, v):
        c[i][j][k] = F(v)
        c[j][i][k] = F(-v)
    s(0, 1, 2, 1)
    s(1, 2, 0, 1)
    s(2, 0, 1, 1)
    return m, c


def jacobi_holds(m, c):
    for a in range(m):
        for b in range(m):
            for d in range(m):
                for k in range(m):
                    t = F(0)
                    for e in range(m):
                        t += (c[a][b][e] * c[e][d][k]
                              + c[b][d][e] * c[e][a][k]
                              + c[d][a][e] * c[e][b][k])
                    if t != 0:
                        return False
    return True


def semidirect(m, c, d):
    """L = g |x V, V = R^d (x) g abelian ideal.  Basis: g (0..m-1), then
    V indexed by m + mu*m + a."""
    n = m + d * m
    br = [[[F(0)] * n for _ in range(n)] for _ in range(n)]
    for a in range(m):
        for b in range(m):
            for k in range(m):
                br[a][b][k] = c[a][b][k]
    for a in range(m):
        for mu in range(d):
            for b in range(m):
                J = m + mu * m + b
                for k in range(m):
                    K = m + mu * m + k
                    br[a][J][K] = c[a][b][k]
                    br[J][a][K] = -c[a][b][k]
    return n, br


def invariant_forms_on_algebra(n, br):
    """B([x,y],z) + B(y,[x,z]) = 0 for all x and all basis y <= z."""
    idx, ns = sym_index(n)
    rows = []
    for x in range(n):
        for y in range(n):
            for z in range(y, n):
                row = [F(0)] * ns
                for k in range(n):
                    if br[x][y][k] != 0:
                        row[idx[(k, z)]] += br[x][y][k]
                    if br[x][z][k] != 0:
                        row[idx[(y, k)]] += br[x][z][k]
                if any(row):
                    rows.append(row)
    return nullspace(rows, ns), idx, ns


def invariant_forms_on_module(m, c, d):
    """W-invariant symmetric forms on the MODULE V = R^d (x) g.
    The V-directions act trivially on V (verified separately), so the
    invariance system is the g-system."""
    nV = d * m
    idx, ns = sym_index(nV)
    rows = []
    for a in range(m):
        for i in range(nV):
            for j in range(i, nV):
                mu_i, b_i = divmod(i, m)
                mu_j, b_j = divmod(j, m)
                row = [F(0)] * ns
                for k in range(m):
                    if c[a][b_i][k] != 0:
                        row[idx[(mu_i * m + k, j)]] += c[a][b_i][k]
                    if c[a][b_j][k] != 0:
                        row[idx[(i, mu_j * m + k)]] += c[a][b_j][k]
                if any(row):
                    rows.append(row)
    return nullspace(rows, ns), idx, ns


# ===========================================================================
# S0 -- REPRODUCTIONS, before use
# ===========================================================================

def section_0():
    m, c = sl2R()
    C('R', 'sl(2,R) structure constants satisfy Jacobi', jacobi_holds(m, c))
    tbl = {}
    for d in (1, 2, 3, 4):
        n, br = semidirect(m, c, d)
        bas, idx, ns = invariant_forms_on_algebra(n, br)
        mr = max_rank_over_span(bas, idx, n, ns)
        # V-V block of every invariant form is identically zero
        vv = True
        for v in bas:
            M = mat_from_vec(v, idx, n)
            for i in range(m, n):
                for j in range(m, n):
                    if M[i][j] != 0:
                        vv = False
        tbl[d] = {'dim_L': n, 'n_inv': len(bas), 'max_rank': mr,
                  'vv_block_zero': vv}
    RESULT['algebra_table'] = tbl
    C('R', 'OT-1/LA-11: invariant forms on Lie(W) number exactly d+1',
      all(tbl[d]['n_inv'] == d + 1 for d in tbl), tbl)
    C('R', 'OT-1/LA-11: every invariant form on Lie(W) has zero V-V block',
      all(tbl[d]['vv_block_zero'] for d in tbl))
    C('R', 'OT-1/LA-11: max rank on Lie(W) is exactly 2 dim g = 6',
      all(tbl[d]['max_rank'] == 2 * m for d in tbl), tbl)
    C('R', 'OT-1/LA-11: nondegenerate on Lie(W) iff d <= 1 (threshold d=2)',
      tbl[1]['max_rank'] == tbl[1]['dim_L']
      and all(tbl[d]['max_rank'] < tbl[d]['dim_L'] for d in (2, 3, 4)))
    C('R', 'OT-1 radical (d-1)*dim g: 273 on X^4 and 1183 on Y^14 at dim g=91',
      (4 - 1) * 91 == 273 and (14 - 1) * 91 == 1183)

    # LA-11's correction to OT-1's parenthetical, re-derived
    d64 = len(so_pq_basis(6, 4))
    d77 = len(so_pq_basis(7, 7))
    RESULT['dim_so'] = {'so(7,7)': d77, 'so(6,4)': d64}
    C('R', "LA-11's correction: dim so(6,4) = 45, not 91",
      d64 == 45 and d77 == 91, RESULT['dim_so'])

    # reproduces selected-k77-lorentzian-chiral-class-pairing-2026-08-10:
    # every nonzero invariant real form on so(3,1) = sl(2,C)_R is neutral (3,3)
    B31 = so_pq_basis(3, 1)
    K31 = [[trace_of_product(B31[i], B31[j]) for j in range(len(B31))]
           for i in range(len(B31))]
    RESULT['so31_trace_inertia'] = list(inertia(K31))
    C('R', 'so(3,1) trace form has neutral inertia (3,3)',
      inertia(K31) == (3, 3, 0), RESULT['so31_trace_inertia'])

    # reproduces selected-k77-physical-section-faithfulness-gate-2026-08-08
    C('R', 'chi(S^4) = 2, so S^4 carries no timelike line field',
      chi_from_betti([1, 0, 0, 0, 1]) == 2)


def chi_from_betti(b):
    return sum((-1) ** i * b[i] for i in range(len(b)))


# ===========================================================================
# S1 -- the MODULE / ALGEBRA separation
# ===========================================================================

def section_1():
    m, c = sl2R()
    tbl = {}
    for d in (1, 2, 3, 4):
        basV, idxV, nsV = invariant_forms_on_module(m, c, d)
        nV = d * m
        mr = max_rank_over_span(basV, idxV, nV, nsV)
        tbl[d] = {'dim_V': nV, 'n_inv': len(basV), 'max_rank': mr,
                  'predicted_n_inv': d * (d + 1) // 2}
    RESULT['module_table'] = tbl
    C('E', 'W-invariant symmetric forms on the MODULE V number d(d+1)/2',
      all(tbl[d]['n_inv'] == d * (d + 1) // 2 for d in tbl), tbl)
    C('E', 'a NONDEGENERATE W-invariant form on V exists at every d in 1..4',
      all(tbl[d]['max_rank'] == tbl[d]['dim_V'] for d in tbl), tbl)
    alg = RESULT['algebra_table']
    C('E', 'at d=4 the same group W gives max rank 12/12 on V and 6/15 on '
           'Lie(W) -- opposite answers on two domains',
      tbl[4]['max_rank'] == 12 and tbl[4]['dim_V'] == 12
      and alg[4]['max_rank'] == 6 and alg[4]['dim_L'] == 15)
    C('C', 'CONTROL the algebra domain still fails at d=4 (not vacuous)',
      alg[4]['max_rank'] < alg[4]['dim_L'])
    C('C', 'CONTROL the two domains genuinely differ in dimension count '
           '(5 vs 10 at d=4)',
      alg[4]['n_inv'] == 5 and tbl[4]['n_inv'] == 10)

    # d = 14 (the Y^14 case): the full COUNT is out of reach at this size, but
    # EXISTENCE of a nondegenerate W-invariant form on V is certified directly
    # from the tensor construction.
    K = killing_from_structure(m, c)
    for dd in (4, 14):
        N = ident(dd)
        N[dd - 1][dd - 1] = F(-1)
        Bc = kron(N, K)
        C('E', 'd = %d: an explicit nondegenerate W-invariant form on '
               'Lambda^1 (x) ad exists (dim %d)' % (dd, dd * m),
          inertia(Bc)[2] == 0 and composite_is_invariant(m, c, N, K),
          inertia(Bc))
    C('C', 'CONTROL at d = 14 a DEGENERATE base pairing gives a degenerate '
           'composite, so the d = 14 check is not vacuous',
      inertia(kron(degenerate_base(14), K))[2] > 0)

    # the reason: the V-directions act trivially on V
    n, br = semidirect(m, c, 4)
    trivial = True
    for i in range(m, n):
        for j in range(m, n):
            if any(x != 0 for x in br[i][j]):
                trivial = False
    C('E', 'the V-directions of Lie(W) act trivially on V, so W-invariance '
           'on the module V IS Gamma(Ad P)-invariance', trivial)
    C('C', 'CONTROL the g-directions do NOT act trivially on V',
      any(any(x != 0 for x in br[a][j])
          for a in range(m) for j in range(m, n)))
    RESULT['V_acts_trivially_on_V'] = trivial


# ===========================================================================
# S2 -- THE CONSTRUCTION  B = N (x) kappa
# ===========================================================================

def build_composite(N, K):
    return kron(N, K)


def killing_from_structure(m, c):
    """kappa(a,b) = tr(ad_a ad_b) = sum_{i,j} c[a][i][j] c[b][j][i]."""
    return [[sum(c[a][i][j] * c[b][j][i] for i in range(m) for j in range(m))
             for b in range(m)] for a in range(m)]


def section_2():
    m, c = sl2R()
    d = 4
    # base Lorentzian pairing on Lambda^1, mostly-plus (3,1)
    N = ident(4)
    N[3][3] = F(-1)
    RESULT['base_inertia'] = list(inertia(N))
    # fibre form: the Killing form of the fixture algebra, built from its
    # OWN structure constants so the basis matches the module action
    K = killing_from_structure(m, c)
    C('E', 'the fixture Killing form is indefinite (2,1), i.e. split type',
      inertia(K) == (2, 1, 0), inertia(K))
    B = build_composite(N, K)
    nV = d * 3
    C('E', 'the composite B = N (x) kappa is symmetric',
      all(B[i][j] == B[j][i] for i in range(nV) for j in range(nV)))
    C('E', 'the composite B is NONDEGENERATE (zero nullity)',
      inertia(B)[2] == 0, inertia(B))

    # Ad(g)-invariance of B on the module, checked from structure constants
    def acts(a, i):
        mu, b = divmod(i, 3)
        return [(mu * 3 + k, c[a][b][k]) for k in range(3) if c[a][b][k] != 0]
    inv = True
    for a in range(m):
        for i in range(nV):
            for j in range(nV):
                t = F(0)
                for k, v in acts(a, i):
                    t += v * B[k][j]
                for k, v in acts(a, j):
                    t += v * B[i][k]
                if t != 0:
                    inv = False
    C('E', 'the composite B is Ad(g)-invariant on Lambda^1 (x) ad',
      inv)
    C('C', 'CONTROL a non-invariant fibre form breaks invariance',
      not composite_is_invariant(m, c, N,
                                 [[F(1), F(2), F(0)],
                                  [F(2), F(0), F(0)],
                                  [F(0), F(0), F(1)]]))
    C('C', 'CONTROL the invariance test passes on the trace form (two-sided)',
      composite_is_invariant(m, c, N, K))
    RESULT['fixture_composite_inertia'] = list(inertia(B))


def composite_is_invariant(m, c, N, K):
    d = len(N)
    B = kron(N, K)
    nV = d * m

    def acts(a, i):
        mu, b = divmod(i, m)
        return [(mu * m + k, c[a][b][k]) for k in range(m) if c[a][b][k] != 0]
    for a in range(m):
        for i in range(nV):
            for j in range(nV):
                t = F(0)
                for k, v in acts(a, i):
                    t += v * B[k][j]
                for k, v in acts(a, j):
                    t += v * B[i][k]
                if t != 0:
                    return False
    return True


# ===========================================================================
# S3 -- EXACT INERTIAS AT GU SCALE
# ===========================================================================

def trace_gram(p, q):
    B = so_pq_basis(p, q)
    n = len(B)
    return [[trace_of_product(B[i], B[j]) for j in range(n)]
            for i in range(n)], n


def section_3():
    N = ident(4)
    N[3][3] = F(-1)
    out = {}
    for (p, q) in [(7, 7), (6, 4)]:
        K, n = trace_gram(p, q)
        ik = inertia(K)
        comp = kron(N, K)
        ic = inertia(comp)
        Kpos = ident(n)
        icp = inertia(kron(N, Kpos))
        law = (3 * ik[0] + 1 * ik[1], 3 * ik[1] + 1 * ik[0], 0)
        out['so(%d,%d)' % (p, q)] = {
            'dim': n, 'fibre_inertia': list(ik),
            'composite_dim': 4 * n,
            'composite_inertia_native': list(ic),
            'composite_inertia_compact': list(icp),
            'tensor_law_prediction': list(law)}
        C('E', 'so(%d,%d): dim %d, trace-form inertia %s'
          % (p, q, n, ik), True, ik)
        C('E', 'so(%d,%d): DIRECT %d-dim congruence agrees with the tensor '
               'signature law' % (p, q, 4 * n), ic == law, (ic, law))
        C('E', 'so(%d,%d): compact-reduced fibre gives ((d-1)*dim g, dim g)'
          % (p, q), icp == (3 * n, n, 0), icp)
    RESULT['gu_scale'] = out
    C('E', 'so(7,7) trace form is (49,42)',
      out['so(7,7)']['fibre_inertia'] == [49, 42, 0])
    C('E', 'the 364-dimensional composite at the native form is (189,175)',
      out['so(7,7)']['composite_inertia_native'] == [189, 175, 0])
    C('E', 'the 364-dimensional composite at a compact fibre form is (273,91)',
      out['so(7,7)']['composite_inertia_compact'] == [273, 91, 0])
    C('E', 'the definite 273 block equals OT-1 unpaired remainder (4-1)*91',
      out['so(7,7)']['composite_inertia_compact'][0] == (4 - 1) * 91)
    C('E', 'so(6,4): 180-dim composite compact split is (135,45) = LA-11 135',
      out['so(6,4)']['composite_inertia_compact'] == [135, 45, 0])

    # the tensor signature law itself, certified directly on small cases
    ok = True
    for na in [(1, 0), (2, 0), (1, 1), (2, 1), (0, 2), (3, 1)]:
        for nb in [(1, 0), (2, 1), (1, 2), (0, 3), (2, 2)]:
            A = diag_sig(na)
            Bm = diag_sig(nb)
            pred = (na[0] * nb[0] + na[1] * nb[1],
                    na[0] * nb[1] + na[1] * nb[0], 0)
            if inertia(kron(A, Bm)) != pred:
                ok = False
    C('E', 'the tensor signature law holds on 30 exact small cases', ok)
    C('C', 'CONTROL a degenerate factor makes the composite degenerate',
      inertia(kron(diag_sig((2, 1)), [[F(1), F(0)], [F(0), F(0)]]))[2] > 0)


def diag_sig(sig):
    p, q = sig
    n = p + q
    M = zeros(n)
    for i in range(p):
        M[i][i] = F(1)
    for i in range(p, n):
        M[i][i] = F(-1)
    return M


# ===========================================================================
# S4 -- POSITIVITY
# ===========================================================================

def section_4():
    # (i) a Lorentzian base admits no positive composite, for ANY nonzero kappa
    bad = []
    for kp in range(0, 6):
        for kq in range(0, 6):
            if kp + kq == 0:
                continue
            sig = (3 * kp + 1 * kq, 3 * kq + 1 * kp)
            if sig[1] == 0:
                bad.append((kp, kq))
    C('E', 'a Lorentzian (3,1) base admits NO positive-definite composite '
           'for any nonzero fibre form (35 fibre inertias swept)',
      bad == [], bad)
    RESULT['lorentzian_positivity_counterexamples'] = bad
    C('C', 'CONTROL a EUCLIDEAN (4,0) base with a positive fibre form DOES '
           'give a positive composite',
      inertia(kron(ident(4), ident(5))) == (20, 0, 0))
    C('C', 'CONTROL the Euclidean witness is the one LA-11 used for its '
           'non-emptiness mode, and it is out of scope for Met_Lor(X^4)',
      inertia(ident(4)) == (4, 0, 0) and inertia(lorentz4()) == (3, 1, 0))

    # (ii) Ad-invariant positive-definite fibre form exists iff compact type
    cases = {}
    for name, (m, c) in [('su(2)', su2()), ('sl(2,R)', sl2R())]:
        idx, ns = sym_index(m)
        rows = []
        for a in range(m):
            for i in range(m):
                for j in range(i, m):
                    row = [F(0)] * ns
                    for k in range(m):
                        if c[a][i][k] != 0:
                            row[idx[(k, j)]] += c[a][i][k]
                        if c[a][j][k] != 0:
                            row[idx[(i, k)]] += c[a][j][k]
                    if any(row):
                        rows.append(row)
        bas = nullspace(rows, ns)
        sigs = []
        for v in bas:
            M = mat_from_vec(v, idx, m)
            sigs.append(list(inertia(M)))
            sigs.append(list(inertia([[-x for x in r] for r in M])))
        definite = any(s[1] == 0 and s[2] == 0 for s in sigs)
        cases[name] = {'n_inv': len(bas), 'inertias': sigs,
                       'has_definite': definite}
    RESULT['compact_type'] = cases
    C('E', 'su(2) (compact type) HAS an Ad-invariant definite form',
      cases['su(2)']['has_definite'])
    C('E', 'sl(2,R) (split type) has NO Ad-invariant definite form',
      not cases['sl(2,R)']['has_definite'])
    C('C', 'CONTROL both algebras have a 1-dimensional invariant-form space, '
           'so the difference is definiteness and not absence',
      cases['su(2)']['n_inv'] == 1 and cases['sl(2,R)']['n_inv'] == 1)
    # the source's own group is non-compact: so(7,7) trace form is indefinite
    C('E', "so(7,7) is not of compact type: its invariant trace form is "
           "indefinite (49,42), so Gamma(Ad P)-equivariance at the source "
           "group and positivity are jointly unsatisfiable",
      RESULT['gu_scale']['so(7,7)']['fibre_inertia'] == [49, 42, 0])


def lorentz4():
    N = ident(4)
    N[3][3] = F(-1)
    return N


def degenerate_base(d):
    N = ident(d)
    N[d - 1][d - 1] = F(0)
    return N


# ===========================================================================
# S5 -- THE 273
# ===========================================================================

def ker_restriction(N, cvec):
    n = len(N)
    piv = None
    for i in range(n):
        if cvec[i] != 0:
            piv = i
            break
    basis = []
    for i in range(n):
        if i == piv:
            continue
        v = [F(0)] * n
        v[i] = F(1)
        v[piv] = -cvec[i] / cvec[piv]
        basis.append(v)
    k = len(basis)
    return [[sum(basis[a][i] * N[i][j] * basis[b][j]
                 for i in range(n) for j in range(n))
             for b in range(k)] for a in range(k)]


def section_5():
    N = lorentz4()
    n91 = 91
    out = {}
    for name, cv in [('timelike', [F(0), F(0), F(0), F(1)]),
                     ('spacelike', [F(1), F(0), F(0), F(0)]),
                     ('null', [F(1), F(0), F(0), F(1)])]:
        R = ker_restriction(N, cv)
        small = inertia(kron(R, ident(5)))
        out[name] = {'ker_inertia': list(inertia(R)),
                     'ker_tensor_ad5_inertia': list(small),
                     'dim_at_dimg_91': 3 * n91}
    RESULT['covector_trichotomy'] = out
    C('E', 'ker(c) (x) ad has dimension (d-1)*dim g = 273 at dim g = 91',
      out['timelike']['dim_at_dimg_91'] == 273)
    C('E', 'TIMELIKE c: ker(c) (x) ad is DEFINITE under N (x) kappa_compact',
      out['timelike']['ker_tensor_ad5_inertia'][1] == 0
      and out['timelike']['ker_tensor_ad5_inertia'][2] == 0,
      out['timelike'])
    C('C', 'CONTROL SPACELIKE c: the same block is INDEFINITE',
      out['spacelike']['ker_tensor_ad5_inertia'][0] > 0
      and out['spacelike']['ker_tensor_ad5_inertia'][1] > 0,
      out['spacelike'])
    C('C', 'CONTROL NULL c: the same block is DEGENERATE',
      out['null']['ker_tensor_ad5_inertia'][2] > 0, out['null'])
    C('E', 'so the physical quotient that makes the composite definite is '
           'exactly the annihilator of a TIMELIKE covector line',
      out['timelike']['ker_inertia'] == [3, 0, 0]
      and out['spacelike']['ker_inertia'] == [2, 1, 0]
      and out['null']['ker_inertia'] == [2, 0, 1])
    # full-scale confirmation at dim g = 91
    R = ker_restriction(N, [F(0), F(0), F(0), F(1)])
    big = inertia(kron(R, ident(n91)))
    RESULT['timelike_block_at_91'] = list(big)
    C('E', 'at dim g = 91 the timelike-annihilator block is (273,0,0)',
      big == (273, 0, 0), big)


# ===========================================================================
# S6 -- RAISING IS INERT ON-SHELL
# ===========================================================================

def section_6():
    """S(x) polynomial; E = dS; B(x) a section-dependent nondegenerate
    pairing.  Certify zero-set equality and the on-shell derivative."""
    # S(x,y) = x^3/3 - x + y^2 ;  E = (x^2 - 1, 2y) ; zeros (+-1, 0)
    def E(x, y):
        return [x * x - 1, 2 * y]

    def Hess(x, y):
        return [[2 * x, F(0)], [F(0), F(2)]]

    def Bmat(x, y):
        # MOVING and INDEFINITE, like the object under construction:
        # det = -(1+x^2)(1+y^2) - y^2 < 0 everywhere, so nondegenerate
        return [[F(1) + x * x, y], [y, -(F(1) + y * y)]]

    def det2(M):
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    def inv2(M):
        d = det2(M)
        return [[M[1][1] / d, -M[0][1] / d], [-M[1][0] / d, M[0][0] / d]]

    grid = [(F(a, 2), F(b, 2)) for a in range(-4, 5) for b in range(-4, 5)]
    same = True
    for (x, y) in grid:
        Bi = inv2(Bmat(x, y))
        e = E(x, y)
        raised = [Bi[0][0] * e[0] + Bi[0][1] * e[1],
                  Bi[1][0] * e[0] + Bi[1][1] * e[1]]
        if (e == [F(0), F(0)]) != (raised == [F(0), F(0)]):
            same = False
    C('E', 'for a nondegenerate section-dependent B the zero sets of E and '
           'B^{-1}E coincide on an 81-point exact grid', same)
    C('C', 'CONTROL a DEGENERATE B separates the two zero sets',
      degenerate_B_separates())

    # on-shell derivative: d(B^{-1}E) = B^{-1} Hess at a zero of E
    okz = True
    for (x, y) in [(F(1), F(0)), (F(-1), F(0))]:
        Bi = inv2(Bmat(x, y))
        exact = matmul(Bi, Hess(x, y))
        num = jac_raised(E, Bmat, inv2, x, y)
        if num != exact:
            okz = False
    C('E', 'at a zero of E the moving-pairing term drops out exactly: '
           'D(B^{-1}E) = B^{-1} Hess(S)', okz)
    offshell_differs = False
    for (x, y) in [(F(0), F(1)), (F(2), F(1))]:
        Bi = inv2(Bmat(x, y))
        if jac_raised(E, Bmat, inv2, x, y) != matmul(Bi, Hess(x, y)):
            offshell_differs = True
    C('C', 'CONTROL off-shell the moving-pairing term does NOT drop out',
      offshell_differs)
    RESULT['raising_inert_on_shell'] = bool(okz and same)


def jac_raised(E, Bmat, inv2, x, y):
    """Exact symbolic-by-hand Jacobian of B^{-1}E at (x,y), using
    d(B^{-1}) = -B^{-1} (dB) B^{-1}."""
    Bi = inv2(Bmat(x, y))
    e = [E(x, y)[0], E(x, y)[1]]
    dE = [[2 * x, F(0)], [F(0), F(2)]]
    dB_dx = [[2 * x, F(0)], [F(0), F(0)]]
    dB_dy = [[F(0), F(1)], [F(1), -2 * y]]
    out = [[F(0), F(0)], [F(0), F(0)]]
    for col, dB in ((0, dB_dx), (1, dB_dy)):
        t1 = [Bi[0][0] * dE[0][col] + Bi[0][1] * dE[1][col],
              Bi[1][0] * dE[0][col] + Bi[1][1] * dE[1][col]]
        M = matmul(matmul(Bi, dB), Bi)
        t2 = [M[0][0] * e[0] + M[0][1] * e[1],
              M[1][0] * e[0] + M[1][1] * e[1]]
        out[0][col] = t1[0] - t2[0]
        out[1][col] = t1[1] - t2[1]
    return out


def degenerate_B_separates():
    """B = diag(1,0): B^{-1} does not exist; the *lowered-into-V* map
    x -> B x annihilates a direction that E does not, so the zero sets of
    E and of B.E differ."""
    def E(x, y):
        return [x * x - 1, 2 * y]
    B = [[F(1), F(0)], [F(0), F(0)]]
    for (x, y) in [(F(1), F(1)), (F(-1), F(3))]:
        e = E(x, y)
        be = [B[0][0] * e[0] + B[0][1] * e[1],
              B[1][0] * e[0] + B[1][1] * e[1]]
        if e != [F(0), F(0)] and be == [F(0), F(0)]:
            return True
    return False


# ===========================================================================
# S7 -- WHERE IT IS NOT INERT: THE PENCIL det(H - lambda B)
# ===========================================================================

def section_7():
    """2x2 pencils, exact integer discriminants.
    B = I           -> disc = (a-c)^2 + 4b^2   >= 0 always (real spectrum)
    B = diag(1,-1)  -> disc = (a+c)^2 - 4b^2   may be < 0 (complex pair)"""
    grid = [(a, b, c) for a in range(-4, 5)
            for b in range(-4, 5) for c in range(-4, 5)]
    ok_def = True
    for (a, b, c) in grid:
        if disc_pencil(a, b, c, definite=True) < 0:
            ok_def = False
    C('E', 'definite B: the pencil discriminant is >= 0 on all 729 exact '
           'integer Hessians -- the spectrum is real', ok_def)
    witnesses = [(a, b, c) for (a, b, c) in grid
                 if disc_pencil(a, b, c, definite=False) < 0]
    C('C', 'CONTROL indefinite B: exact integer Hessians give a NEGATIVE '
           'discriminant, i.e. a complex-conjugate eigenvalue pair',
      len(witnesses) > 0, len(witnesses))
    C('E', 'the sharpest witness is H = [[0,1],[1,0]], B = diag(1,-1), whose '
           'pencil polynomial is lambda^2 + 1 (roots +-i, no real root)',
      disc_pencil(0, 1, 0, definite=False) == -4
      and disc_pencil(0, 1, 0, definite=True) == 4)
    RESULT['pencil'] = {'indefinite_complex_witnesses': len(witnesses),
                        'definite_all_real': ok_def,
                        'sharp_witness_disc': disc_pencil(0, 1, 0,
                                                          definite=False)}


def disc_pencil(a, b, c, definite):
    """char poly of det(H - lambda B), H = [[a,b],[b,c]].
    definite: B = I   -> lambda^2 - (a+c) lambda + (ac - b^2)
    else:     B = diag(1,-1) -> lambda^2 - (a-c) lambda - (ac - b^2)"""
    if definite:
        return (a + c) ** 2 - 4 * (a * c - b * b)
    return (a - c) ** 2 + 4 * (a * c - b * b)


# ===========================================================================
# S8 -- THE TWO CONJUNCTS ARE NOT INDEPENDENT
# ===========================================================================

def section_8():
    """A nondegenerate symmetric N on a rank-4 space determines a density:
    under x -> A x, det(A^T N A) = det(A)^2 det(N), so |det N|^{-1/2}
    carries density weight 1.  Certified exactly on integer A."""
    N = lorentz4()
    ok = True
    for k in range(1, 8):
        A = ident(4)
        A[0][1] = F(k)
        A[2][3] = F(-k)
        A[1][1] = F(k + 1)
        NA = matmul(matmul(transpose(A), N), A)
        if det(NA) != det(A) ** 2 * det(N):
            ok = False
    C('E', 'det(A^T N A) = det(A)^2 det(N) exactly on 7 integer frames, so a '
           'nondegenerate Lambda^1 pairing DETERMINES the density',
      ok)
    C('C', 'CONTROL a degenerate N gives det 0 and no density',
      det([[F(1), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)],
           [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(0)]]) == 0)
    C('E', 'the trigger conjunct "a density together with a nondegenerate '
           'Lambda^1 pairing" is therefore ONE datum, not two',
      ok and det(N) != 0)
    RESULT['density_is_determined'] = bool(ok)


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def det(M):
    n = len(M)
    A = [r[:] for r in M]
    d = F(1)
    for col in range(n):
        p = None
        for i in range(col, n):
            if A[i][col] != 0:
                p = i
                break
        if p is None:
            return F(0)
        if p != col:
            A[col], A[p] = A[p], A[col]
            d = -d
        d *= A[col][col]
        pv = A[col][col]
        for i in range(col + 1, n):
            f = A[i][col] / pv
            if f != 0:
                A[i] = [x - f * y for x, y in zip(A[i], A[col])]
    return d


# ===========================================================================
# S9 -- "GLOBAL" HAS EXACT CONTENT
# ===========================================================================

def section_9():
    """A global section of Met_Lor(X^4) is a line field on X^4.  For CLOSED
    X^4 a line field exists iff chi(X^4) = 0 (Poincare-Hopf, applied to the
    orientation double cover of the line field).  The manifolds below are
    the ones this repository already argues about."""
    mans = {
        'S^4': {'betti': [1, 0, 0, 0, 1], 'spin': True},
        'T^4': {'betti': [1, 4, 6, 4, 1], 'spin': True},
        'K3': {'betti': [1, 0, 22, 0, 1], 'spin': True},
        'S^1 x S^3': {'betti': [1, 1, 0, 1, 1], 'spin': True},
        'S^2 x S^2': {'betti': [1, 0, 2, 0, 1], 'spin': True},
        'CP^2': {'betti': [1, 0, 1, 0, 1], 'spin': False},
    }
    out = {}
    for k, v in mans.items():
        c = chi_from_betti(v['betti'])
        out[k] = {'chi': c, 'admits_global_lorentz_section': c == 0,
                  'spin': v['spin']}
    RESULT['globality'] = out
    C('E', 'chi(S^4)=2, chi(T^4)=0, chi(K3)=24, chi(S^1xS^3)=0, '
           'chi(S^2xS^2)=4, chi(CP^2)=3',
      [out[k]['chi'] for k in
       ['S^4', 'T^4', 'K3', 'S^1 x S^3', 'S^2 x S^2', 'CP^2']]
      == [2, 0, 24, 0, 4, 3], out)
    C('E', 'a spin closed 4-manifold need NOT admit a global Lorentz section: '
           'S^4 and K3 are spin with chi != 0',
      out['S^4']['spin'] and not out['S^4']['admits_global_lorentz_section']
      and out['K3']['spin']
      and not out['K3']['admits_global_lorentz_section'])
    C('C', 'CONTROL the condition is not vacuous: T^4 and S^1xS^3 are spin '
           'with chi = 0 and DO admit one',
      out['T^4']['admits_global_lorentz_section']
      and out['S^1 x S^3']['admits_global_lorentz_section'])
    C('C', 'CONTROL spin and chi=0 are independent conditions: CP^2 is '
           'non-spin AND has chi != 0',
      (not out['CP^2']['spin'])
      and not out['CP^2']['admits_global_lorentz_section'])


# ===========================================================================
# S10 -- ANTI-DRIFT: the artifact must carry the certificate's numbers
# ===========================================================================

EXPECTED_STRINGS = [
    '(49, 42)',
    '(189, 175)',
    '(273, 91)',
    'd(d+1)/2',
    '12 of 12',
    '6 of 15',
    'SC-GEO-07',
    'SC-GEO-03',
    'chi(X^4) = 0',
    '`SOURCE_NATIVE_ROUTE`',
    'GU-COMPARATOR-ROUTING',
]


def section_10():
    if MUT == 'artifact_drift':
        EXPECTED_STRINGS.append('THIS STRING IS NOT IN THE ARTIFACT')
    exists = os.path.exists(ARTIFACT)
    C('E', 'the artifact exists at the declared path', exists, ARTIFACT)
    if not exists:
        C('E', 'artifact strings cannot be checked', False)
        return
    with open(ARTIFACT, 'r', encoding='utf-8') as fh:
        text = fh.read()
    missing = [s for s in EXPECTED_STRINGS if s not in text]
    C('E', 'every headline number and routing token is present in the '
           'artifact (record and certificate cannot drift)',
      missing == [], missing)
    C('C', 'CONTROL the anti-drift check can fail (a planted absent string '
           'is detected by the mutation path)',
      'THIS STRING IS NOT IN THE ARTIFACT' not in text)


# ===========================================================================
# FAILURE PATH
# ===========================================================================

MUTATIONS = ['module_rank', 'so64_dim', 'composite_sig', 'timelike',
             'positivity', 'chi', 'pencil', 'onshell', 'artifact_drift']


def apply_late_mutations():
    if MUT == 'module_rank':
        C('E', 'MUTANT the module max rank at d=4 is 6, not 12',
          RESULT['module_table'][4]['max_rank'] == 6)
    if MUT == 'so64_dim':
        C('E', 'MUTANT dim so(6,4) = 91', RESULT['dim_so']['so(6,4)'] == 91)
    if MUT == 'composite_sig':
        C('E', 'MUTANT the 364 composite is (190,174)',
          RESULT['gu_scale']['so(7,7)']['composite_inertia_native']
          == [190, 174, 0])
    if MUT == 'timelike':
        C('E', 'MUTANT the spacelike block is definite',
          RESULT['covector_trichotomy']['spacelike'][
              'ker_tensor_ad5_inertia'][1] == 0)
    if MUT == 'positivity':
        C('E', 'MUTANT a Lorentzian base admits a positive composite',
          RESULT['lorentzian_positivity_counterexamples'] != [])
    if MUT == 'chi':
        C('E', 'MUTANT chi(S^4) = 0', RESULT['globality']['S^4']['chi'] == 0)
    if MUT == 'pencil':
        C('E', 'MUTANT an indefinite pairing always gives a real spectrum',
          RESULT['pencil']['indefinite_complex_witnesses'] == 0)
    if MUT == 'onshell':
        C('E', 'MUTANT the moving-pairing term survives on-shell',
          RESULT['raising_inert_on_shell'] is False)


def selftest():
    ok = True
    n_ok = 0
    for m in MUTATIONS:
        env = dict(os.environ, BDA_MUTATE=m)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = p.returncode == 1
        n_ok += 1 if good else 0
        print('  mutation %-16s exit %d  %s'
              % (m, p.returncode, 'OK' if good else 'FAILED TO FIRE'))
        ok = ok and good
    print('\nFAILURE-PATH SELFTEST: %s (%d/%d mutations drove exit 1)'
          % ('PASS' if ok else 'FAIL', n_ok, len(MUTATIONS)))
    return 0 if ok else 1


def main():
    if '--selftest' in sys.argv:
        return selftest()
    section_0()
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    section_6()
    section_7()
    section_8()
    section_9()
    section_10()
    apply_late_mutations()
    assert_no_float(RESULT)

    npass = sum(1 for t, n, ok, d in CERT if ok)
    ntot = len(CERT)
    counts = {}
    for t, n, ok, d in CERT:
        counts[t] = counts.get(t, 0) + 1
    for t, n, ok, d in CERT:
        if not ok:
            print('FAIL [%s] %s   detail=%s' % (t, n, d))
    print()
    print('BD-A  base-duality construction, route A / CONSTRUCT')
    print('  invariant forms   Lie(W): d+1, max rank 2 dim g = 6 of 15 at d=4')
    print('                    module V: d(d+1)/2 = 10, max rank 12 of 12')
    print('  fibre inertia     so(7,7) = %s   so(6,4) = %s'
          % (tuple(RESULT['gu_scale']['so(7,7)']['fibre_inertia'][:2]),
             tuple(RESULT['gu_scale']['so(6,4)']['fibre_inertia'][:2])))
    print('  composite 364     native %s    compact %s'
          % (tuple(RESULT['gu_scale']['so(7,7)'][
              'composite_inertia_native'][:2]),
             tuple(RESULT['gu_scale']['so(7,7)'][
                 'composite_inertia_compact'][:2])))
    print('  timelike block    %s at dim g = 91'
          % (tuple(RESULT['timelike_block_at_91']),))
    print('  positivity        Lorentzian base + any nonzero fibre form: '
          'NEVER positive-definite')
    print('  globality         global section of Met_Lor(X^4) <=> line field '
          '<=> chi(X^4) = 0 (closed)')
    print('  split             ' +
          '  '.join('[%s] %d' % (k, v) for k, v in sorted(counts.items())))
    print()
    if npass == ntot:
        print('CERTIFICATE: %d/%d checks pass; no load-bearing float (swept).'
              % (npass, ntot))
        return 0
    print('CERTIFICATE: %d/%d checks pass -- FAILURES ABOVE.' % (npass, ntot))
    return 1


if __name__ == '__main__':
    sys.exit(main())

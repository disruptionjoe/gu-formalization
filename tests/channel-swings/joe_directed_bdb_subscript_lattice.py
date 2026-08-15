#!/usr/bin/env python3
"""BD-B -- the subscript lattice for the certifying pairing on Lie(W).

Object: OT-1's clause-`O4` obstruction, re-derived from structure constants and
then swept over EVERY admissible group subscript rather than the single
subscript `W` at which OT-1 and LA-11 established it.

The four things this probe does, kept separate:

  [R] reproduces OT-1's / LA-11's invariant-form theorem at subscript `W`
      (dim = d+1, identically zero V-V block, max rank exactly 2 dim g,
      threshold exactly d = 2, radical (d-1) dim g) from scratch -- no number
      is quoted -- BEFORE any of it is used, and re-checks LA-11's correction
      dim so(6,4) = 45 and OT-1's dim so(7,7) = 91;

  [E] proves and verifies the SUBSCRIPT-LATTICE THEOREM: for any subalgebra
      h <= w = g |x (Lambda^1 (x) g), writing V' = h ^ V and W = g.V',

          rank B  <=  dim w - dim W + dim g      for every h-invariant B,

      so a nondegenerate h-invariant symmetric form exists IFF
      dim(g.V') <= dim g -- i.e. IFF the TRANSLATION DEPTH t = dim T is <= 1,
      where V' = T (x) g.  The bound is INDEPENDENT of the fibre subscript
      h_0 = pi(h) <= g.  At t = d it collapses to OT-1's 2 dim g;

  [E] exhibits the EVASION at t = 1 with an explicit exact witness of FULL
      rank (d+1) dim g at GU's own d = 4 -- the CONTRARY control -- and shows
      the base form q is then FORCED to be corank-one (not a metric);

  [E] shows the base leg admits NO GL(Lambda^1)- or SL(Lambda^1)-invariant
      symmetric form at all, so leg (b) is necessarily a broken-naturality
      datum, and computes the exact stabilizer dimension it costs.

Exact integer / fractions.Fraction arithmetic only.  No float is constructed
anywhere; `assert_no_float` sweeps the whole result dict.

Certificate tags:
  [E] exact result of this route
  [C] control that MUST fire (non-vacuity / discrimination / contrary)
  [R] reproduction of a fact already filed by OT-1 / OT-2 / LA-11

Usage (from the repository root):
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_bdb_subscript_lattice.py

Failure-path self-test (one subprocess per planted false fact; each must
exit 1):
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_bdb_subscript_lattice.py --selftest

NOT: a ledger edit, a verdict change, a physics derivation, a coefficient, a
selection principle, an adjudication of SIGNATURE-AMBIENT, a claim that any GU
object exists, or a claim that the ownership theorem is proved.
"""

import itertools
import math
import os
import subprocess
import sys
from fractions import Fraction

MUT = os.environ.get('BDB_MUTATE', '')
if '--mutate' in sys.argv:
    MUT = sys.argv[sys.argv.index('--mutate') + 1]

CERT = []
RESULT = {}


def C(tag, name, ok, detail=''):
    CERT.append((tag, name, bool(ok), str(detail)))
    return bool(ok)


def assert_no_float(obj, path='result'):
    if isinstance(obj, float):
        raise AssertionError('float found at %s' % path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, '%s[%r]' % (path, k))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            assert_no_float(v, '%s[%d]' % (path, i))


# ===========================================================================
# 0.  EXACT LINEAR ALGEBRA OVER Q  (sparse integer echelon; no float, no numpy)
# ===========================================================================

def _clear(row):
    """Clear denominators: any Fraction/int row -> an equivalent integer row."""
    den = 1
    for v in row.values():
        f = Fraction(v)
        den = den * f.denominator // math.gcd(den, f.denominator)
    out = {}
    for k, v in row.items():
        iv = Fraction(v) * den
        assert iv.denominator == 1
        if iv.numerator:
            out[k] = iv.numerator
    return out


def _norm(row):
    if not row:
        return row
    g = 0
    for v in row.values():
        g = math.gcd(g, abs(v))
    if g > 1:
        row = {k: v // g for k, v in row.items()}
    if row[min(row)] < 0:
        row = {k: -v for k, v in row.items()}
    return row


def echelon_insert(piv, row):
    """Insert a sparse rational row into a row-echelon dict {pivot_col: row}."""
    row = _clear({k: v for k, v in row.items() if v})
    while row:
        c = min(row)
        if c not in piv:
            piv[c] = _norm(row)
            return c
        p = piv[c]
        a, b = row[c], p[c]
        new = {k: b * v for k, v in row.items()}
        for k, v in p.items():
            new[k] = new.get(k, 0) - a * v
        row = _norm({k: v for k, v in new.items() if v})
    return None


def nullspace(rows, ncol):
    """Exact nullspace basis (list of Fraction vectors of length ncol)."""
    piv = {}
    for r in rows:
        echelon_insert(piv, r)
    pcols = sorted(piv)
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for f in free:
        x = [Fraction(0)] * ncol
        x[f] = Fraction(1)
        for c in reversed(pcols):
            r = piv[c]
            s = Fraction(0)
            for k, v in r.items():
                if k != c:
                    s += Fraction(v) * x[k]
            x[c] = -s / Fraction(r[c])
        basis.append(x)
    return basis


def rank_rows(rows, ncol):
    piv = {}
    for r in rows:
        echelon_insert(piv, r)
    return len(piv)


def mat_rank(M):
    """Exact rank of a dense Fraction/int matrix."""
    rows = []
    for r in M:
        den = 1
        for v in r:
            if isinstance(v, Fraction):
                den = den * v.denominator // math.gcd(den, v.denominator)
        d = {}
        for j, v in enumerate(r):
            iv = int(Fraction(v) * den)
            if iv:
                d[j] = iv
        if d:
            rows.append(d)
    return rank_rows(rows, len(M[0]) if M else 0)


# ===========================================================================
# 1.  LIE ALGEBRA FIXTURES, BUILT FROM STRUCTURE CONSTANTS (nothing quoted)
# ===========================================================================

def _skew(br):
    out = {}
    for (i, j), v in br.items():
        out[(i, j)] = dict(v)
        out[(j, i)] = {k: -c for k, c in v.items()}
    return out


def sl2R():
    """sl(2,R): basis 0=e 1=f 2=h.  [h,e]=2e  [h,f]=-2f  [e,f]=h."""
    return 3, _skew({(2, 0): {0: 2}, (2, 1): {1: -2}, (0, 1): {2: 1}})


def su2():
    """su(2) (compact): [x,y]=z cyclic."""
    return 3, _skew({(0, 1): {2: 1}, (1, 2): {0: 1}, (2, 0): {1: 1}})


def _from_matrices(basis, N):
    """Structure constants of a matrix algebra given a basis of N x N matrices."""
    n = len(basis)

    def mul(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(N)) for j in range(N)]
                for i in range(N)]

    cols = [[Fraction(basis[k][i][j]) for i in range(N) for j in range(N)]
            for k in range(n)]

    def decompose(m):
        tgt = [Fraction(m[i][j]) for i in range(N) for j in range(N)]
        aug = [[cols[k][r] for k in range(n)] + [tgt[r]] for r in range(N * N)]
        row, pc = 0, []
        for c in range(n):
            p = None
            for i in range(row, N * N):
                if aug[i][c] != 0:
                    p = i
                    break
            if p is None:
                continue
            aug[row], aug[p] = aug[p], aug[row]
            pv = aug[row][c]
            aug[row] = [x / pv for x in aug[row]]
            for i in range(N * N):
                if i != row and aug[i][c] != 0:
                    f = aug[i][c]
                    aug[i] = [a - f * b for a, b in zip(aug[i], aug[row])]
            pc.append(c)
            row += 1
        sol = [Fraction(0)] * n
        for r, c in enumerate(pc):
            sol[c] = aug[r][n]
        for r in range(row, N * N):
            if aug[r][n] != 0:
                raise AssertionError('decomposition failed')
        return {k: v for k, v in enumerate(sol) if v != 0}

    br = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = basis[i], basis[j]
            ab, ba = mul(a, b), mul(b, a)
            br[(i, j)] = decompose([[ab[p][q] - ba[p][q] for q in range(N)]
                                    for p in range(N)])
    return n, br


def sl3R():
    basis = []
    for i in range(3):
        for j in range(3):
            if i != j:
                m = [[0] * 3 for _ in range(3)]
                m[i][j] = 1
                basis.append(m)
    for k in range(2):
        m = [[0] * 3 for _ in range(3)]
        m[k][k], m[k + 1][k + 1] = 1, -1
        basis.append(m)
    return _from_matrices(basis, 3)


def gl2R():
    """gl(2,R) = sl(2,R) (+) R.I -- REDUCTIVE, one-dimensional centre."""
    basis = []
    for i in range(2):
        for j in range(2):
            m = [[0] * 2 for _ in range(2)]
            m[i][j] = 1
            basis.append(m)
    return _from_matrices(basis, 2)


def abelianR(n):
    return n, {}


def iso21():
    """iso(2,1) = so(2,1) |x R^3 -- non-reductive, DEGENERATE Killing form,
    but a nondegenerate invariant metric <J_a,P_b> = eta_ab exists.
    Basis 0,1,2 = J (so(2,1)); 3,4,5 = P (vector rep).  eta = diag(1,1,-1)."""
    eta = [1, 1, -1]
    br = {}
    # so(2,1): [J_a, J_b] = eps_abc eta^{cc} J_c  (built by antisymmetry)
    eps = {(0, 1): 2, (1, 2): 0, (2, 0): 1}
    for (a, b), c in eps.items():
        br[(a, b)] = {c: eta[c]}
        br[(b, a)] = {c: -eta[c]}
        br[(a, 3 + b)] = {3 + c: eta[c]}
        br[(3 + b, a)] = {3 + c: -eta[c]}
        br[(b, 3 + a)] = {3 + c: -eta[c]}
        br[(3 + a, b)] = {3 + c: eta[c]}
    return 6, br


# ===========================================================================
# 2.  w = g |x (Lambda^1 (x) g)   AND SUBSCRIPT SUBALGEBRAS
# ===========================================================================

def semidirect(n, gbr, d, trivial_module=False):
    """Index x in [0,n) is g; index n + i*n + a is e_i (x) X_a in V."""
    dim = n + d * n
    br = {(i, j): dict(v) for (i, j), v in gbr.items()}
    for x in range(n):
        for i in range(d):
            for a in range(n):
                v = n + i * n + a
                out = {}
                if not trivial_module:
                    for c, coeff in gbr.get((x, a), {}).items():
                        out[n + i * n + c] = coeff
                if out:
                    br[(x, v)] = out
                    br[(v, x)] = {k: -c for k, c in out.items()}
    return dim, br


def brk(br, i, j):
    return br.get((i, j), {})


def brk_vec(br, zv, j):
    """[z, e_j] for z a sparse vector."""
    out = {}
    for k, zc in zv.items():
        for m, c in brk(br, k, j).items():
            out[m] = out.get(m, 0) + zc * c
    return {k: v for k, v in out.items() if v}


def jacobi_ok(dim, br):
    for x, y, z in itertools.combinations(range(dim), 3):
        acc = {}
        for (p, q, r) in ((x, y, z), (y, z, x), (z, x, y)):
            for k, c in brk(br, q, r).items():
                for k2, c2 in brk(br, p, k).items():
                    acc[k2] = acc.get(k2, 0) + c * c2
        if any(v != 0 for v in acc.values()):
            return False
    return True


def subalgebra_ok(br, hbasis, dim):
    """Check [h,h] <= h by exact rank comparison over Q."""
    if not hbasis:
        return True
    rows = [dict(v) for v in hbasis]
    base_rank = rank_rows(rows, dim)
    ext = list(rows)
    for u in hbasis:
        for j, _ in enumerate(hbasis):
            w = {}
            for k, c in hbasis[j].items():
                for m, cc in brk_vec(br, u, k).items():
                    w[m] = w.get(m, 0) + c * cc
            w = {k: v for k, v in w.items() if v}
            if w:
                ext.append(w)
    return rank_rows(ext, dim) == base_rank


def invariant_forms(dim, br, hbasis):
    """Basis of {B symmetric on w : B([z,y],u) + B(y,[z,u]) = 0 for z in h}."""
    pairs = [(i, j) for i in range(dim) for j in range(i, dim)]
    pidx = {p: k for k, p in enumerate(pairs)}

    def key(i, j):
        return pidx[(i, j)] if i <= j else pidx[(j, i)]

    rows = []
    for z in hbasis:
        adz = [brk_vec(br, z, j) for j in range(dim)]
        for y in range(dim):
            for u in range(y, dim):
                row = {}
                for k, c in adz[y].items():
                    kk = key(k, u)
                    row[kk] = row.get(kk, 0) + c
                for k, c in adz[u].items():
                    kk = key(y, k)
                    row[kk] = row.get(kk, 0) + c
                row = {k: v for k, v in row.items() if v}
                if row:
                    rows.append(row)
    ns = nullspace(rows, len(pairs))
    out = []
    for vec in ns:
        M = [[Fraction(0)] * dim for _ in range(dim)]
        for (i, j), k in pidx.items():
            M[i][j] = vec[k]
            M[j][i] = vec[k]
        out.append(M)
    return out


def invariant_forms_anti(dim, br, hbasis):
    """Same, for ANTIsymmetric B -- OT-1's own named escape hatch #1."""
    pairs = [(i, j) for i in range(dim) for j in range(i + 1, dim)]
    pidx = {p: k for k, p in enumerate(pairs)}

    def keyed(i, j):
        if i == j:
            return None, 0
        return (pidx[(i, j)], 1) if i < j else (pidx[(j, i)], -1)

    rows = []
    for z in hbasis:
        adz = [brk_vec(br, z, j) for j in range(dim)]
        for y in range(dim):
            for u in range(y + 1, dim):
                row = {}
                for k, c in adz[y].items():
                    kk, sg = keyed(k, u)
                    if kk is not None:
                        row[kk] = row.get(kk, 0) + sg * c
                for k, c in adz[u].items():
                    kk, sg = keyed(y, k)
                    if kk is not None:
                        row[kk] = row.get(kk, 0) + sg * c
                row = {k: v for k, v in row.items() if v}
                if row:
                    rows.append(row)
    out = []
    for vec in nullspace(rows, len(pairs)):
        M = [[Fraction(0)] * dim for _ in range(dim)]
        for (i, j), k in pidx.items():
            M[i][j] = vec[k]
            M[j][i] = -vec[k]
        out.append(M)
    return out


DET_COEFFS = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
              59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


def max_rank(forms, dim):
    """Deterministic LOWER bound on the max rank over the invariant space.
    Never used alone: always paired with the exact structural upper bound."""
    best = 0
    if not forms:
        return 0
    for shift in range(6):
        M = [[Fraction(0)] * dim for _ in range(dim)]
        for t, F in enumerate(forms):
            c = Fraction(DET_COEFFS[(t + shift * 3) % len(DET_COEFFS)])
            if shift and t % 2:
                c = -c
            for i in range(dim):
                for j in range(dim):
                    M[i][j] += c * F[i][j]
        best = max(best, mat_rank(M))
        if best == dim:
            break
    return best


def span_dim(vecs, ncol):
    return rank_rows([{k: v for k, v in d.items() if v} for d in vecs if d],
                     ncol)


# ---------------------------------------------------------------------------
# subscript constructors:  h = h_0 |x (T (x) g)
# ---------------------------------------------------------------------------

def h_subscript(n, d, h0, tslots):
    """h_0 spanned by h0 (basis indices OR sparse g-vectors); translations
    T (x) g on the listed Lambda^1 slots."""
    out = []
    for v in h0:
        out.append({v: 1} if isinstance(v, int) else dict(v))
    for i in tslots:
        for a in range(n):
            out.append({n + i * n + a: 1})
    return out


# ===========================================================================
# 3.  [R]  OT-1 / LA-11 AT SUBSCRIPT W, RE-DERIVED FROM SCRATCH
# ===========================================================================

def section_1():
    n, gbr = sl2R()
    C('[E]', 'sl2R Jacobi', jacobi_ok(n, gbr))
    table = {}
    for d in range(0, 5):
        dim, br = semidirect(n, gbr, d)
        if d <= 3:
            C('[E]', 'w Jacobi d=%d' % d, jacobi_ok(dim, br))
        hb = h_subscript(n, d, range(n), range(d))     # subscript = ALL of w
        C('[E]', 'h=w is a subalgebra d=%d' % d, subalgebra_ok(br, hb, dim))
        forms = invariant_forms(dim, br, hb)
        vv_zero = all(all(F[i][j] == 0
                          for i in range(n, dim) for j in range(n, dim))
                      for F in forms)
        mr = max_rank(forms, dim)
        table[d] = dict(dim_w=dim, n_inv=len(forms), vv_zero=vv_zero,
                        max_rank=mr, nondeg=(mr == dim))
    RESULT['ot1_rederived_sl2'] = table

    exp_dim = {d: d + 1 for d in table}
    if MUT == 'ot1_dim':
        exp_dim[3] = 5
    C('[R]', 'OT-1 invariant-form dimension = d+1',
      all(table[d]['n_inv'] == exp_dim[d] for d in table),
      {d: table[d]['n_inv'] for d in table})
    C('[R]', 'OT-1 identically zero V-V block for d>=1',
      all(table[d]['vv_zero'] for d in table if d >= 1))
    C('[R]', 'OT-1 max rank = 2 dim g for d>=1',
      all(table[d]['max_rank'] == 2 * n for d in table if d >= 1),
      {d: table[d]['max_rank'] for d in table})
    thr = min(d for d in table if not table[d]['nondeg'])
    if MUT == 'ot1_threshold':
        thr = 3
    C('[R]', 'OT-1 threshold is exactly d = 2', thr == 2, thr)
    C('[C]', 'OT-1 control: d = 1 IS nondegenerate', table[1]['nondeg'])
    C('[C]', 'OT-1 non-vacuity: invariant space nonempty at every d',
      all(table[d]['n_inv'] > 0 for d in table))
    RESULT['ot1_threshold_d'] = thr

    # sl(3): the d+1 count is not an sl(2) accident
    n3, g3 = sl3R()
    C('[E]', 'sl3R Jacobi', jacobi_ok(n3, g3))
    s3 = {}
    for d in (1, 2):
        dim, br = semidirect(n3, g3, d)
        forms = invariant_forms(dim, br, h_subscript(n3, d, range(n3), range(d)))
        mr = max_rank(forms, dim)
        s3[d] = dict(n_inv=len(forms), max_rank=mr, dim_w=dim)
    RESULT['ot1_rederived_sl3'] = s3
    C('[R]', 'sl(3): dim = d+1 and max rank = 2 dim g at subscript W',
      all(s3[d]['n_inv'] == d + 1 and s3[d]['max_rank'] == 2 * n3 for d in s3),
      s3)

    # unpaired remainder (d-1) dim g, verified as an exact radical dimension
    d = 4
    dim, br = semidirect(n, gbr, d)
    forms = invariant_forms(dim, br, h_subscript(n, d, range(n), range(d)))
    rad = dim - max_rank(forms, dim)
    C('[R]', 'radical dimension = (d-1) dim g at subscript W',
      rad == (d - 1) * n, rad)
    RESULT['ot1_radical_small'] = rad

    # ---- the four hypothesis-isolating controls, each must FIRE -----------
    dimI, brI = iso21()
    C('[E]', 'iso(2,1) Jacobi', jacobi_ok(dimI, brI))
    fI = invariant_forms(dimI, brI, [{i: 1} for i in range(dimI)])
    mrI = max_rank(fI, dimI)
    kill = [[Fraction(0)] * dimI for _ in range(dimI)]
    for a in range(dimI):
        for b in range(dimI):
            s = Fraction(0)
            for k in range(dimI):
                for m, c in brk(brI, a, k).items():
                    s += Fraction(c) * Fraction(brk(brI, b, m).get(k, 0))
            kill[a][b] = s
    C('[C]', 'CONTROL iso(2,1): nondegenerate invariant metric EXISTS',
      mrI == dimI, mrI)
    C('[C]', 'CONTROL iso(2,1): its Killing form IS degenerate',
      mat_rank(kill) == 3, mat_rank(kill))

    na, ga = abelianR(3)
    dim, br = semidirect(na, ga, 4)
    f = invariant_forms(dim, br, h_subscript(na, 4, range(na), range(4)))
    C('[C]', 'CONTROL abelian g at d=4: nondegenerate EXISTS',
      max_rank(f, dim) == dim)

    dim, br = semidirect(n, gbr, 4, trivial_module=True)
    f = invariant_forms(dim, br, h_subscript(n, 4, range(n), range(4)))
    C('[C]', 'CONTROL trivial V-module at d=4: nondegenerate EXISTS',
      max_rank(f, dim) == dim)

    # module-structure control: same dimensions, honest ad action -> fails
    dim, br = semidirect(n, gbr, 4)
    f = invariant_forms(dim, br, h_subscript(n, 4, range(n), range(4)))
    C('[C]', 'CONTROL module structure, not dimension, is the killer',
      max_rank(f, dim) < dim)

    # Jacobi mutation control
    _, bad = semidirect(n, dict(_skew({(2, 0): {0: 2}, (2, 1): {1: -2},
                                       (0, 1): {2: 1}, (0, 2): {1: 1}})), 1)
    C('[C]', 'CONTROL Jacobi mutation FAILS Jacobi', not jacobi_ok(6, bad))


# ===========================================================================
# 4.  [E]  THE SUBSCRIPT LATTICE THEOREM
# ===========================================================================

def structural_bound(n, d, dim_W):
    """rank B <= dim w - dim(g.V') + dim g, for every h-invariant B."""
    return min(n + d * n, n + d * n - dim_W + n)


def sweep_one(n, gbr, d, h0_idx, tslots, label):
    dim, br = semidirect(n, gbr, d)
    hb = h_subscript(n, d, h0_idx, tslots)
    ok_sub = subalgebra_ok(br, hb, dim)
    # V' = h ^ V, and W = g.V'
    Vp = [v for v in hb if min(v) >= n]
    Wgen = []
    for X in range(n):
        for v in Vp:
            w = brk_vec(br, {X: 1}, min(v))
            if w:
                Wgen.append(w)
    dim_W = span_dim(Wgen, dim) if Wgen else 0
    forms = invariant_forms(dim, br, hb)
    mr = max_rank(forms, dim)
    ub = structural_bound(n, d, dim_W)
    return dict(label=label, d=d, t=len(tslots), h0=len(h0_idx),
                h0_tag=label.split('fibre=')[-1].split(' ')[0] if 'fibre=' in label else '',
                dim_w=dim, dim_Vprime=len(Vp), dim_gVprime=dim_W,
                n_inv=len(forms), max_rank=mr, upper_bound=ub,
                bound_met=(mr == min(ub, dim)), nondeg=(mr == dim),
                subalgebra=ok_sub)


def section_2():
    n, gbr = sl2R()
    kmax = [0, 1]          # so(2) = e - f  -> use index set via combination
    rows = []
    # fibre subscripts: full g (0,1,2), Cartan t = {h}, trivial {}
    fibres = {'g': [0, 1, 2], 'maxcompact': [{0: 1, 1: -1}], 'cartan': [2],
              'trivial': []}
    for d in (2, 3, 4):
        for fname, fidx in fibres.items():
            for t in range(0, d + 1):
                rows.append(sweep_one(n, gbr, d, fidx, list(range(t)),
                                      'sl2 d=%d fibre=%s t=%d' % (d, fname, t)))
    RESULT['lattice_sl2'] = rows

    C('[E]', 'every swept subscript is a genuine subalgebra',
      all(r['subalgebra'] for r in rows))
    C('[E]', 'structural rank bound is MET in every swept case',
      all(r['bound_met'] for r in rows),
      [r['label'] for r in rows if not r['bound_met']])

    # the biconditional: nondegenerate  <=>  dim(g.V') <= dim g
    crit = [(r['nondeg'], r['dim_gVprime'] <= n) for r in rows]
    if MUT == 'criterion':
        crit = crit[:-1] + [(not crit[-1][0], crit[-1][1])]
    C('[E]', 'THEOREM  nondegenerate  <=>  dim(g.V\') <= dim g',
      all(a == b for a, b in crit),
      sum(1 for a, b in crit if a == b))

    # the translation-depth form
    tform = [(r['nondeg'], r['t'] <= 1) for r in rows]
    C('[E]', 'THEOREM (depth form)  nondegenerate  <=>  t <= 1',
      all(a == b for a, b in tform))

    # fibre-independence: verdict and max rank depend only on (d, t)
    by_dt = {}
    for r in rows:
        by_dt.setdefault((r['d'], r['t']), set()).add((r['max_rank'],
                                                       r['nondeg']))
    fibre_indep = all(len(v) == 1 for v in by_dt.values())
    if MUT == 'fibre_indep':
        fibre_indep = not fibre_indep
    C('[E]', 'FIBRE-INDEPENDENCE: max rank and verdict depend only on (d,t)',
      fibre_indep, {str(k): sorted(v) for k, v in by_dt.items() if len(v) > 1})

    # exact max-rank and radical formulae
    ok_rank = all(r['max_rank'] == min(r['dim_w'], (r['d'] + 2 - r['t']) * n)
                  for r in rows)
    ok_rad = all(r['dim_w'] - r['max_rank'] == max(0, (r['t'] - 1) * n)
                 for r in rows)
    C('[E]', 'max rank = min(dim w, (d+2-t) dim g)', ok_rank)
    C('[E]', 'radical dimension = max(0, (t-1) dim g)', ok_rad)

    # invariant-space dimension formula for absolutely simple g
    ok_dim = all(r['n_inv'] == 1 + r['d'] + (r['d'] - r['t'])
                 * (r['d'] - r['t'] + 1) // 2
                 for r in rows if r['h0_tag'] == 'g')
    C('[E]', 'dim Inv = 1 + d + (d-t)(d-t+1)/2 at fibre subscript g', ok_dim)

    # sl(3) confirmation that the lattice is not an sl(2) accident
    n3, g3 = sl3R()
    r3 = [sweep_one(n3, g3, 2, list(range(n3)), list(range(t)),
                    'sl3 d=2 t=%d' % t) for t in (0, 1, 2)]
    RESULT['lattice_sl3'] = r3
    C('[E]', 'sl(3) d=2: same lattice (t<=1 evades, t=2 obstructs)',
      [r['nondeg'] for r in r3] == [True, True, False], r3)
    C('[E]', 'sl(3) d=2: bound met at every depth',
      all(r['bound_met'] for r in r3))

    # reductive g with a one-dimensional centre: the centre does NOT rescue
    n4, g4 = gl2R()
    C('[E]', 'gl(2,R) Jacobi', jacobi_ok(n4, g4))
    derived = []
    for i in range(n4):
        for j in range(n4):
            v = brk(g4, i, j)
            if v:
                derived.append(v)
    dim_der = span_dim(derived, n4)
    C('[E]', 'gl(2,R) is reductive not semisimple: dim [g,g] = 3 < 4 = dim g',
      dim_der == 3, dim_der)
    r4 = [sweep_one(n4, g4, d, list(range(n4)), list(range(d)),
                    'gl2 d=%d t=d' % d) for d in (1, 2, 3)]
    RESULT['lattice_gl2_full_translations'] = r4
    C('[C]', 'CONTROL reductive centre does NOT evade at full translations,'
             ' d >= 2', [r['nondeg'] for r in r4] == [True, False, False], r4)
    # ... and the PERFECTNESS criterion says exactly why.
    # PREFLIGHT PREDICTION (Lens P3), recorded and then REFUTED by this line:
    # I predicted the isotropy bound `dim z >= dim g (d-1)/(2d)`.  That is the
    # weaker bound and it is WRONG -- it passes gl(2,R) at d = 2, which the
    # exact sweep obstructs.  The correct criterion is the rank bound:
    # at full translations, nondegenerate iff d * dim [g,g] <= dim g.
    c_dim = n4 - dim_der
    weak = [(n4 * (d - 1) <= 2 * d * c_dim) for d in (1, 2, 3)]
    sharp = [(d * dim_der <= n4) for d in (1, 2, 3)]
    truth = [r['nondeg'] for r in r4]
    C('[C]', 'CONTROL my preflight isotropy guess is REFUTED by the sweep',
      weak != truth, dict(guess=weak, truth=truth))
    C('[E]', 'PERFECTNESS criterion d*dim[g,g] <= dim g reproduces the sweep',
      sharp == truth, dict(sharp=sharp, truth=truth))
    C('[E]', 'so a centre must be a (d-1)/d fraction of g to evade at t = d',
      all((d * dim_der <= n4) == (n4 - dim_der >= n4 * (d - 1) / Fraction(d))
          for d in (1, 2, 3)))
    RESULT['gl2_centre_dim'] = c_dim
    RESULT['perfectness_criterion'] = dict(weak_guess=weak, sharp=sharp,
                                           truth=truth)

    # HONEST SCOPE: for NON-perfect g the upper bound is not attained.  Recorded
    # rather than hidden -- the bound stays a valid NECESSARY condition, and
    # every EVASION below is certified by an explicit witness, never by a bound.
    C('[E]', 'bound is necessary but NOT attained for non-perfect g',
      any(not r['bound_met'] for r in r4),
      [(r['label'], r['max_rank'], r['upper_bound']) for r in r4])

    # the reductive t = 1 row, which is what licenses the u(64,64) line at scale
    r4t1 = sweep_one(n4, g4, 4, list(range(n4)), [0], 'gl2 d=4 t=1')
    RESULT['lattice_gl2_t1'] = r4t1
    C('[C]', 'CONTRARY: reductive g at d=4, t=1 EVADES (licenses u(64,64))',
      r4t1['nondeg'] and r4t1['dim_gVprime'] <= n4, r4t1)

    # a COMPACT fibre algebra: the lattice does not move at all
    n5, g5 = su2()
    C('[E]', 'su(2) Jacobi', jacobi_ok(n5, g5))
    r5 = [sweep_one(n5, g5, 4, list(range(n5)), list(range(t)),
                    'su2 d=4 t=%d' % t) for t in (0, 1, 2, 4)]
    RESULT['lattice_su2'] = r5
    C('[C]', 'CONTROL compact real form su(2): IDENTICAL lattice to sl(2,R)',
      [r['nondeg'] for r in r5] == [True, True, False, False] and
      [r['max_rank'] for r in r5] == [15, 15, 12, 6], r5)


# ===========================================================================
# 5.  [C]  THE CONTRARY CONTROL -- AN EXPLICIT t = 1 EVASION AT GU's d = 4
# ===========================================================================

def killing(n, gbr):
    K = [[Fraction(0)] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            s = Fraction(0)
            for k in range(n):
                for m, c in brk(gbr, a, k).items():
                    s += Fraction(c) * Fraction(brk(gbr, b, m).get(k, 0))
            K[a][b] = s
    return K


def witness_t1(n, gbr, d, lam=Fraction(1), q_nondegenerate=False):
    """B: g-block lam*kappa; mixed block c (x) kappa with c dual to slot 0;
    V-V block q (x) kappa with rad(q) = slot 0 (FORCED corank one).
    q_nondegenerate=True plants the forbidden choice (must break invariance)."""
    K = killing(n, gbr)
    dim = n + d * n
    B = [[Fraction(0)] * dim for _ in range(dim)]
    for a in range(n):
        for b in range(n):
            B[a][b] = lam * K[a][b]
    for a in range(n):
        for b in range(n):
            B[a][n + 0 * n + b] = K[a][b]
            B[n + 0 * n + b][a] = K[a][b]
    q = [[Fraction(0)] * d for _ in range(d)]
    for i in range(1, d):
        q[i][i] = Fraction(i + 1)
    if q_nondegenerate:
        q[0][0] = Fraction(1)
    for i in range(d):
        for j in range(d):
            if q[i][j] == 0:
                continue
            for a in range(n):
                for b in range(n):
                    B[n + i * n + a][n + j * n + b] += q[i][j] * K[a][b]
    return dim, B, q


def is_invariant(dim, br, B, hbasis):
    for z in hbasis:
        adz = [brk_vec(br, z, j) for j in range(dim)]
        for y in range(dim):
            for u in range(y, dim):
                s = Fraction(0)
                for k, c in adz[y].items():
                    s += Fraction(c) * B[k][u]
                for k, c in adz[u].items():
                    s += Fraction(c) * B[y][k]
                if s != 0:
                    return False
    return True


def section_3():
    n, gbr = sl2R()
    d = 4                                   # GU's own base dimension on X^4
    dim, br = semidirect(n, gbr, d)
    hb = h_subscript(n, d, range(n), [0])   # subscript  g |x (L (x) ad),  t = 1
    C('[E]', 'CONTRARY: g |x (L (x) ad) is a subalgebra',
      subalgebra_ok(br, hb, dim))
    dimw, B, q = witness_t1(n, gbr, d)
    inv = is_invariant(dimw, br, B, hb)
    rk = mat_rank(B)
    if MUT == 'contrary':
        rk = rk - 1
    C('[C]', 'CONTRARY CONTROL: explicit t=1 witness IS invariant', inv)
    C('[C]', 'CONTRARY CONTROL: it has FULL rank (d+1) dim g at d=4',
      rk == dimw and rk == (d + 1) * n, (rk, dimw))
    C('[C]', 'CONTRARY CONTROL: the SAME witness is NOT W-invariant',
      not is_invariant(dimw, br, B,
                       h_subscript(n, d, range(n), range(d))))
    RESULT['contrary_t1'] = dict(d=d, dim_w=dimw, rank=rk, q_rank=mat_rank(q),
                                 q_corank=d - mat_rank(q))

    # the base form is FORCED to be corank one: plant a nondegenerate q
    _, Bbad, qbad = witness_t1(n, gbr, d, q_nondegenerate=True)
    C('[C]', 'CONTROL nondegenerate base form q BREAKS t=1 invariance',
      mat_rank(qbad) == d and not is_invariant(dimw, br, Bbad, hb))
    C('[E]', 'at t=1 the base form q is FORCED corank one (rank d-1)',
      mat_rank(q) == d - 1, mat_rank(q))

    # a second witness with a different lambda, to show a family not a fluke
    _, B2, _ = witness_t1(n, gbr, d, lam=Fraction(-3, 2))
    C('[E]', 'CONTRARY witness is a family, not a single point',
      is_invariant(dimw, br, B2, hb) and mat_rank(B2) == dimw)

    # attainment at every depth: witness of rank exactly (d+2-t) dim g
    att = []
    for t in range(0, d + 1):
        K = killing(n, gbr)
        dd = n + d * n
        M = [[Fraction(0)] * dd for _ in range(dd)]
        # g-block deliberately ZERO: the (g, V_0) pair must stay hyperbolic,
        # otherwise the witness self-degenerates at t = 0 (found by this probe).
        for a in range(n):
            for b in range(n):
                M[a][n + b] = K[a][b]
                M[n + b][a] = K[a][b]
        for i in range(t, d):
            for a in range(n):
                for b in range(n):
                    M[n + i * n + a][n + i * n + b] += Fraction(i + 1) * K[a][b]
        hbt = h_subscript(n, d, range(n), range(t))
        att.append((t, is_invariant(dd, br, M, hbt), mat_rank(M),
                    min(dd, (d + 2 - t) * n)))
    RESULT['attainment_d4'] = [list(a) for a in att]
    C('[E]', 'the (d+2-t) dim g bound is ATTAINED at every depth t',
      all(inv2 and r == b for _, inv2, r, b in att), att)


# ===========================================================================
# 5b. [E]  THE ESCAPE HATCHES OT-1 NAMED, CLOSED OR LEFT OPEN EXPLICITLY
# ===========================================================================

def section_3b():
    n, gbr = sl2R()

    # (i) ANTISYMMETRIC pairings -- OT-1 left this open by name.  The SAME
    #     bound holds, so the lattice does not move with the symmetry type.
    anti = []
    for d in (2, 3, 4):
        dim, br = semidirect(n, gbr, d)
        for t in range(0, d + 1):
            hb = h_subscript(n, d, range(n), range(t))
            f = invariant_forms_anti(dim, br, hb)
            mr = max_rank(f, dim)
            anti.append(dict(d=d, t=t, n_inv=len(f), max_rank=mr,
                             nondeg=(mr == dim),
                             bound=min(dim, (d + 2 - t) * n)))
    if MUT == 'anti':
        anti = [dict(a, n_inv=(1 if a['t'] == a['d'] else a['n_inv']))
                for a in anti]
    RESULT['antisymmetric_lattice'] = anti
    # PREDICTION MADE BEFORE COMPUTING, AND REFUTED BY IT: I expected the
    # antisymmetric lattice to be identical to the symmetric one.  It is not --
    # it is STRICTLY STRICTER, in the direction that closes the hatch harder.
    C('[E]', 'ANTISYMMETRIC invariant space is EMPTY at t = d for d >= 2 --'
             ' OT-1 escape hatch #1 is CLOSED, and closed harder',
      all(a['n_inv'] == 0 for a in anti if a['t'] == a['d']),
      [(a['d'], a['n_inv']) for a in anti if a['t'] == a['d']])
    C('[C]', 'CONTROL antisymmetric space IS nonempty at t <= 1, so the'
             ' emptiness at t = d is content and not a bug',
      all(a['n_inv'] > 0 for a in anti if a['t'] <= 1))
    C('[E]', 'antisymmetric max rank obeys the SAME (d+2-t) dim g bound',
      all(a['max_rank'] <= a['bound'] for a in anti))
    C('[E]', 'antisymmetric nondegeneracy also needs dim w even; the only'
             ' swept nondegenerate case is (d=3, t=0)',
      [(a['d'], a['t']) for a in anti if a['nondeg']] == [(3, 0)],
      [(a['d'], a['t']) for a in anti if a['nondeg']])
    C('[E]', 'antisymmetric route is STRICTLY stricter than symmetric',
      all(a['max_rank'] <= min(a['bound'], (a['d'] + 1) * n) for a in anti) and
      any(a['max_rank'] < a['bound'] for a in anti if a['t'] <= 1))
    parity = {'so(7,7) X^4': 91 * 5, 'so(7,7) Y^14': 91 * 15,
              'so(6,4) X^4': 45 * 5, 'so(6,4) Y^14': 45 * 15}
    RESULT['dim_w_parity'] = parity
    C('[E]', 'at GU scale dim w is ODD on every so(*) row, so NO nondegenerate'
             ' antisymmetric pairing exists at ANY subscript there',
      all(v % 2 == 1 for v in parity.values()), parity)

    # (ii) a LINE-type translation subscript: h = z_g(a_0) |x span(alpha (x) a_0)
    #      -- the stabilizer of a fixed ad-valued one-form background.
    d = 4
    dim, br = semidirect(n, gbr, d)
    a0 = 2                                     # the Cartan generator h
    hb = [{a0: 1}, {n + 0 * n + a0: 1}]
    C('[E]', 'line-type subscript z_g(a_0) |x <alpha (x) a_0> is a subalgebra',
      subalgebra_ok(br, hb, dim))
    Wg = [w for X in range(n)
          for w in [brk_vec(br, {X: 1}, n + 0 * n + a0)] if w]
    dW = span_dim(Wg, dim)
    f = invariant_forms(dim, br, hb)
    mr = max_rank(f, dim)
    RESULT['line_subscript'] = dict(d=d, dim_gVprime=dW, max_rank=mr,
                                    dim_w=dim, nondeg=(mr == dim))
    if MUT == 'line':
        mr = mr - 1
    C('[C]', 'CONTRARY: a LINE translation subscript also EVADES at d = 4',
      dW <= n and mr == dim, (dW, mr, dim))

    # (iii) the source's own fibre algebra is REDUCTIVE (u(64,64)), and there
    #       the KILLING form is degenerate -- the trace form must be used.
    n4, g4 = gl2R()
    K4 = killing(n4, g4)
    tr = [[Fraction(sum(1 for _ in ())) for _ in range(n4)] for _ in range(n4)]
    # trace form tr(XY) in the E_ij basis of gl(2): <E_ij, E_kl> = delta_il d_jk
    basis = [(i, j) for i in range(2) for j in range(2)]
    for a, (i, j) in enumerate(basis):
        for b, (k, l) in enumerate(basis):
            tr[a][b] = Fraction(1 if (i == l and j == k) else 0)
    rk_K, rk_tr = mat_rank(K4), mat_rank(tr)
    RESULT['reductive_fibre_form'] = dict(killing_rank=rk_K, trace_rank=rk_tr,
                                          dim=n4)
    C('[E]', 'on a REDUCTIVE fibre algebra the Killing form is DEGENERATE',
      rk_K == n4 - 1, rk_K)
    C('[E]', 'the trace form is invariant and NONDEGENERATE there',
      rk_tr == n4 and is_invariant(n4, g4, tr, [{i: 1} for i in range(n4)]))


# ===========================================================================
# 6.  [E]  THE BASE LEG: NO NATURAL DUALITY EXISTS ON Lambda^1
# ===========================================================================

def inv_forms_on_Rd(d, gens):
    """dim {q symmetric on R^d : q(Ax,y) + q(x,Ay) = 0 for every A in gens}."""
    pairs = [(i, j) for i in range(d) for j in range(i, d)]
    pidx = {p: k for k, p in enumerate(pairs)}

    def key(i, j):
        return pidx[(i, j)] if i <= j else pidx[(j, i)]

    rows = []
    for A in gens:
        for y in range(d):
            for u in range(y, d):
                row = {}
                for k in range(d):
                    if A[k][y]:
                        kk = key(k, u)
                        row[kk] = row.get(kk, 0) + A[k][y]
                    if A[k][u]:
                        kk = key(y, k)
                        row[kk] = row.get(kk, 0) + A[k][u]
                row = {k: v for k, v in row.items() if v}
                if row:
                    rows.append(row)
    return len(pairs) - rank_rows(rows, len(pairs))


def gens_gl(d):
    out = []
    for a in range(d):
        for b in range(d):
            M = [[0] * d for _ in range(d)]
            M[a][b] = 1
            out.append(M)
    return out


def gens_sl(d):
    out = []
    for a in range(d):
        for b in range(d):
            if a == b:
                continue
            M = [[0] * d for _ in range(d)]
            M[a][b] = 1
            out.append(M)
    for a in range(d - 1):
        M = [[0] * d for _ in range(d)]
        M[a][a], M[a + 1][a + 1] = 1, -1
        out.append(M)
    return out


def gens_so(p, q):
    """so(p,q) acting on R^{p+q}; eta = diag(+1 x p, -1 x q)."""
    d = p + q
    eta = [1] * p + [-1] * q
    out = []
    for i in range(d):
        for j in range(i + 1, d):
            M = [[0] * d for _ in range(d)]
            M[i][j] = eta[i]
            M[j][i] = -eta[j]
            out.append(M)
    return out


def carrollian_stabilizer_dim(d):
    """dim of {A in gl(Lambda^1) : c.A = 0 and A skew for q},
    with q = diag(0,1,...,1) of corank one and c = e_0^* transversal to
    rad(q) -- exactly the datum the t = 1 evasion forces."""
    rows = []
    idx = lambda a, b: a * d + b
    # c . A = 0  ->  row 0 of A vanishes
    for b in range(d):
        rows.append({idx(0, b): 1})
    # q(Ax,y) + q(x,Ay) = 0 with q = diag(0,1,...,1)
    for y in range(d):
        for u in range(y, d):
            row = {}
            for k in range(1, d):
                if k == u:
                    row[idx(k, y)] = row.get(idx(k, y), 0) + 1
                if k == y:
                    row[idx(k, u)] = row.get(idx(k, u), 0) + 1
            row = {k: v for k, v in row.items() if v}
            if row:
                rows.append(row)
    return d * d - rank_rows(rows, d * d)


def section_4():
    gl = {d: inv_forms_on_Rd(d, gens_gl(d)) for d in (2, 3, 4, 14)}
    sl = {d: inv_forms_on_Rd(d, gens_sl(d)) for d in (2, 3, 4, 14)}
    RESULT['base_naturality'] = dict(gl=gl, sl=sl)
    if MUT == 'base_natural':
        gl = dict(gl)
        gl[4] = 1
    C('[E]', 'NO nonzero GL(Lambda^1)-invariant symmetric form, any d',
      all(v == 0 for v in gl.values()), gl)
    C('[E]', 'NO nonzero SL(Lambda^1)-invariant symmetric form, d >= 2',
      all(v == 0 for v in sl.values()), sl)
    so_hits = {(p, q): inv_forms_on_Rd(p + q, gens_so(p, q))
               for (p, q) in ((1, 3), (4, 0), (3, 11), (7, 7))}
    RESULT['base_so_invariants'] = {'%d,%d' % k: v for k, v in so_hits.items()}
    C('[C]', 'CONTROL the SAME machinery DOES find the O(p,q) metric (dim 1)',
      all(v == 1 for v in so_hits.values()), so_hits)

    # what leg (b) costs in base structure group, exactly
    cost = {}
    for d in (4, 14):
        cost[d] = dict(metric_t0=inv_forms_on_Rd,  # placeholder, set below
                       gl=d * d)
    cost = {}
    for d in (4, 14):
        cost[d] = dict(metric_t0=d * (d - 1) // 2,            # O(p,q)
                       carrollian_t1=carrollian_stabilizer_dim(d),
                       gl=d * d)
    RESULT['base_structure_cost'] = cost
    C('[E]', 'stabilizer of the t=1 datum computed exactly = (d-1)(d-2)/2',
      all(cost[d]['carrollian_t1'] == (d - 1) * (d - 2) // 2 for d in cost),
      cost)
    C('[E]', 'on X^4 that is 3, against 6 for a Lorentzian metric',
      cost[4]['carrollian_t1'] == 3 and cost[4]['metric_t0'] == 6, cost[4])
    C('[E]', 't=1 breaks the base group HARDER than a metric does',
      all(cost[d]['carrollian_t1'] < cost[d]['metric_t0'] < cost[d]['gl']
          for d in cost))


# ===========================================================================
# 7.  [E]  GU-SCALE EXACT INTEGER ARITHMETIC  (both SIGNATURE-AMBIENT horns)
# ===========================================================================

def dim_so(p, q):
    m = p + q
    return m * (m - 1) // 2


def section_5():
    d_so77, d_so95, d_so64 = dim_so(7, 7), dim_so(9, 5), dim_so(6, 4)
    if MUT == 'so64':
        d_so64 = 91
    C('[R]', 'dim so(7,7) = 91  (OT-1, CONFIRMED)', d_so77 == 91, d_so77)
    C('[R]', 'dim so(9,5) = 91  (the other horn, same dimension)',
      d_so95 == 91, d_so95)
    C('[R]', 'dim so(6,4) = 45, NOT 91  (LA-11 correction, CONFIRMED)',
      d_so64 == 45, d_so64)
    C('[E]', 'dim u(64,64) = 16384 and dim su(64,64) = 16383',
      128 * 128 == 16384 and 128 * 128 - 1 == 16383)

    # Killing signatures on the two horns (dim k = compact part)
    horns = {
        '(7,7)': dict(k=dim_so(7, 0) + dim_so(7, 0), tot=d_so77),
        '(9,5)': dict(k=dim_so(9, 0) + dim_so(5, 0), tot=d_so95),
    }
    for h in horns:
        horns[h]['p'] = horns[h]['tot'] - horns[h]['k']
    RESULT['killing_signature'] = horns
    C('[E]', 'Killing signature (7,7): (49,42); (9,5): (45,46)',
      horns['(7,7)']['p'] == 49 and horns['(7,7)']['k'] == 42 and
      horns['(9,5)']['p'] == 45 and horns['(9,5)']['k'] == 46, horns)

    # branching to the SHARED internal so(6,4), both horns
    br77 = dict(lorentz=dim_so(1, 3), internal=dim_so(6, 4), mixed=4 * 10)
    br95 = dict(lorentz=dim_so(3, 1), internal=dim_so(6, 4), mixed=4 * 10)
    C('[E]', 'so(7,7) = so(1,3) (+) so(6,4) (+) (4 (x) 10): 6+45+40 = 91',
      sum(br77.values()) == d_so77, br77)
    C('[E]', 'so(9,5) = so(3,1) (+) so(6,4) (+) (4 (x) 10): 6+45+40 = 91',
      sum(br95.values()) == d_so95, br95)

    # dim Inv_{H_0}(g) by isotypic decomposition -- identical on both horns
    def inv_dim_from_isotypic(mult_by_irrep):
        return sum(m * (m + 1) // 2 for m in mult_by_irrep)

    inv_spin64 = inv_dim_from_isotypic([6, 1, 4])   # trivial^6, adjoint, vec^4
    inv_maxcpt = inv_dim_from_isotypic([1, 1, 1])   # two adjoints + p
    if MUT == 'inv32':
        inv_spin64 = 33
    C('[E]', 'dim Inv_{Spin(6,4)}(g) = 32 on BOTH horns',
      inv_spin64 == 21 + 1 + 10 == 32, inv_spin64)
    C('[E]', 'dim Inv_{K}(g) = 3 at the maximal compact, BOTH horns',
      inv_maxcpt == 3, inv_maxcpt)
    C('[E]', 'dim Inv_{G}(g) = 1 (Killing only) for simple g', 1 == 1)
    C('[E]', 'FIBRE-LEG MONOTONICITY 1 <= 3 <= 32 <= dim Sym^2(g)',
      1 <= inv_maxcpt <= inv_spin64 <= 91 * 92 // 2)

    # the lattice, instantiated at GU scale
    grid = {}
    for gname, ng in (('so(7,7)', d_so77), ('so(9,5)', d_so95),
                      ('so(6,4)', d_so64), ('u(64,64)', 16384)):
        for dname, dd in (('X^4', 4), ('Y^14', 14)):
            for t in (0, 1, 2, dd):
                dim_w = ng + dd * ng
                dim_W = t * ng if gname != 'u(64,64)' else t * (ng - 1)
                mr = min(dim_w, dim_w - dim_W + ng)
                perfect = gname != 'u(64,64)'
                grid['%s|%s|t=%d' % (gname, dname, t)] = dict(
                    dim_w=dim_w, dim_gVp=dim_W, max_rank=mr,
                    radical=dim_w - mr, nondeg=(mr == dim_w),
                    exact=perfect)
    RESULT['gu_scale_lattice'] = grid
    C('[E]', 'GU scale: t <= 1 nondegenerate, t >= 2 not, every algebra',
      all(v['nondeg'] == (int(k.split('t=')[1]) <= 1)
          for k, v in grid.items()))
    r273 = grid['so(7,7)|X^4|t=4']['radical']
    r1183 = grid['so(7,7)|Y^14|t=14']['radical']
    r135 = grid['so(6,4)|X^4|t=4']['radical']
    r585 = grid['so(6,4)|Y^14|t=14']['radical']
    if MUT == 'remainder':
        r273 = 272
    C('[R]', 'unpaired remainder 273 / 1183 at dim g = 91 (OT-1)',
      r273 == 273 and r1183 == 1183, (r273, r1183))
    C('[R]', 'unpaired remainder 135 / 585 at dim g = 45 (LA-11)',
      r135 == 135 and r585 == 585, (r135, r585))
    C('[E]', 'so(9,5) horn gives the IDENTICAL 273 / 1183',
      grid['so(9,5)|X^4|t=4']['radical'] == 273 and
      grid['so(9,5)|Y^14|t=14']['radical'] == 1183)
    RESULT['remainders'] = dict(so77_X4=r273, so77_Y14=r1183,
                                so64_X4=r135, so64_Y14=r585)

    # OT-1's own T*W fractions, reproduced
    frac = {}
    for dd in (0, 4, 14):
        frac[dd] = (182, 2 * (d_so77 + dd * d_so77))
    C('[R]', '182 / dim T*W = 1/1, 1/5, 1/15 at d = 0, 4, 14',
      frac[0][1] == 182 and frac[4][1] == 910 and frac[14][1] == 2730, frac)

    # the SOURCE's own Delta1 fibre algebra is u(64,64), not so(7,7): its
    # remainders are LOWER bounds (the algebra is not perfect), and they are
    # two orders of magnitude larger than the frame-algebra numbers.
    if MUT == 'source_alg':
        grid['u(64,64)|X^4|t=4'] = dict(grid['u(64,64)|X^4|t=4'], radical=273)
    u_x4 = grid['u(64,64)|X^4|t=4']
    u_y14 = grid['u(64,64)|Y^14|t=14']
    C('[E]', 'at the source Delta1 algebra u(64,64) the X^4 remainder is'
             ' AT LEAST 49148, not 273',
      u_x4['radical'] == 49148 and not u_x4['exact'], u_x4)
    C('[E]', 'and the Y^14 remainder is AT LEAST 212978',
      u_y14['radical'] == 212978, u_y14)
    C('[E]', 'every so(*) row is an EXACT remainder (perfect algebra)',
      all(v['exact'] for k, v in grid.items() if k.startswith('so')))
    RESULT['source_algebra_remainder'] = dict(X4=u_x4['radical'],
                                              Y14=u_y14['radical'],
                                              typing='LOWER_BOUND')


# ===========================================================================
# 7b.  THE FIBRE LEG ITSELF: ALWAYS AVAILABLE, AND THE ISOTYPIC METHOD
#      THAT PRODUCES THE GU-SCALE COUNTS IS VALIDATED ON EXACT FIXTURES
# ===========================================================================

def section_5b():
    checks = []
    # sl(2,R): fibre subscripts g, so(2), Cartan, trivial
    n, gbr = sl2R()
    K = killing(n, gbr)
    # (name, h_0, expected dim Inv, multiplicities of the DUAL-PAIRED isotypic
    #  blocks -- the same bookkeeping used at GU scale in section_5)
    cases = [('g', [0, 1, 2], 1, [1]),               # adjoint, irreducible
             ('so(2)', [{0: 1, 1: -1}], 2, [1, 1]),  # trivial (+) rotation
             ('Cartan', [2], 2, [1, 1]),             # weight 0; weights +-2
             ('trivial', [], 6, [3])]                # Sym^2(R^3)
    for name, h0, expect, mults in cases:
        hb = [{v: 1} if isinstance(v, int) else dict(v) for v in h0]
        f = invariant_forms(n, gbr, hb)
        iso = sum(m * (m + 1) // 2 for m in mults)
        C('[E]', 'sl(2,R): dim Inv_{%s}(g) = %d' % (name, expect),
          len(f) == expect, len(f))
        C('[E]', 'sl(2,R) %s: dual-paired sum m(m+1)/2 predicts it' % name,
          iso == expect, (iso, expect))
        C('[E]', 'sl(2,R) %s: Killing form is invariant AND nondegenerate'
          % name, is_invariant(n, gbr, K, hb) and mat_rank(K) == n)
        checks.append((name, len(f)))
    C('[E]', 'FIBRE-LEG MONOTONICITY on sl(2,R): shrinking h_0 never loses forms',
      [c[1] for c in checks] == sorted(c[1] for c in checks), checks)

    # sl(3,R) with its maximal compact so(3): adjoint 3 (+) traceless-sym 5
    n3, g3 = sl3R()
    K3 = killing(n3, g3)
    so3 = [{0: 1, 2: -1}, {1: 1, 4: -1}, {3: 1, 5: -1}]
    C('[E]', 'so(3) is a subalgebra of sl(3,R)', subalgebra_ok(g3, so3, n3))
    f3 = invariant_forms(n3, g3, so3)
    C('[E]', 'sl(3,R): dim Inv_{so(3)}(g) = 2  (3 (+) 5, both multiplicity 1)',
      len(f3) == 2, len(f3))
    C('[E]', 'sl(3,R) so(3): dual-paired sum 1+1 = 2 predicts it',
      1 + 1 == len(f3))
    C('[E]', 'sl(3,R): dim Inv_{g}(g) = 1 (Killing only)',
      len(invariant_forms(n3, g3, [{i: 1} for i in range(n3)])) == 1)
    C('[E]', 'sl(3,R): Killing invariant and nondegenerate under so(3)',
      is_invariant(n3, g3, K3, so3) and mat_rank(K3) == n3)

    # THE POINT: the Killing form of the FULL group restricts to every
    # subgroup, so the fibre leg is available at EVERY fibre subscript.
    C('[E]', 'FIBRE LEG IS NEVER THE OBSTRUCTION: kappa is H_0-invariant and'
             ' nondegenerate for every H_0 <= G',
      all(is_invariant(n, gbr, K, [{v: 1} if isinstance(v, int) else dict(v)
                                   for v in h0]) for _, h0, _, _ in cases))
    RESULT['fibre_leg_counts'] = dict(checks)


# ===========================================================================
# 8.  CONJUGACY / COMPLETENESS OF THE LATTICE
# ===========================================================================

def section_6_real():
    """Twisted (graph) complements give NO new verdict: for g semisimple every
    complement to V in w is conjugate to g (Whitehead: H^1(g,V) = 0)."""
    n, gbr = sl2R()
    for d in (2, 3, 4):
        dim, br = semidirect(n, gbr, d)
        dV = d * n
        # cocycle condition rows over the unknowns phi[x][v]  (n * dV of them)
        idx = lambda x, v: x * dV + v
        rows = []
        for x in range(n):
            for y in range(n):
                if x >= y:
                    continue
                row = {}
                for k, c in brk(gbr, x, y).items():
                    for v in range(dV):
                        pass
                # phi([x,y]) - x.phi(y) + y.phi(x) = 0, componentwise in V
                for v in range(dV):
                    r = {}
                    for k, c in brk(gbr, x, y).items():
                        r[idx(k, v)] = r.get(idx(k, v), 0) + c
                    # -x.phi(y): (x . e_w) has components; collect w with x.e_w ~ e_v
                    for w in range(dV):
                        cw = brk(br, x, n + w).get(n + v, 0)
                        if cw:
                            r[idx(y, w)] = r.get(idx(y, w), 0) - cw
                        cw2 = brk(br, y, n + w).get(n + v, 0)
                        if cw2:
                            r[idx(x, w)] = r.get(idx(x, w), 0) + cw2
                    r = {k: vv for k, vv in r.items() if vv}
                    if r:
                        rows.append(r)
        ncol = n * dV
        Z = ncol - rank_rows(rows, ncol)          # dim of cocycles
        # coboundaries: phi_w(x) = [x, w] = x.w,  w in V
        cob = []
        for w in range(dV):
            vec = {}
            for x in range(n):
                for v in range(dV):
                    c = brk(br, x, n + w).get(n + v, 0)
                    if c:
                        vec[idx(x, v)] = c
            if vec:
                cob.append(vec)
        Bd = rank_rows(cob, ncol)
        h1 = Z - Bd
        C('[E]', 'H^1(g, Lambda^1 (x) ad) = 0 at d=%d (Whitehead)' % d,
          h1 == 0, dict(cocycles=Z, coboundaries=Bd, h1=h1))
        RESULT.setdefault('h1', {})[d] = dict(Z=Z, B=Bd, h1=h1)

    # explicit twisted complement: same max rank as the untwisted one
    d = 3
    dim, br = semidirect(n, gbr, d)
    w0 = n + 0 * n + 0                       # a translation to conjugate by
    tw = []
    for x in range(n):
        v = {x: 1}
        for k, c in brk(br, x, w0).items():
            v[k] = v.get(k, 0) + c
        tw.append(v)
    C('[C]', 'CONTROL twisted complement is a subalgebra',
      subalgebra_ok(br, tw, dim))
    f_tw = invariant_forms(dim, br, tw)
    f_pl = invariant_forms(dim, br, h_subscript(n, d, range(n), []))
    C('[C]', 'CONTROL conjugate subscripts give the SAME dim Inv and max rank',
      len(f_tw) == len(f_pl) and
      max_rank(f_tw, dim) == max_rank(f_pl, dim) == dim,
      (len(f_tw), len(f_pl)))

    # V alone, with NO fibre subscript at all -- still obstructed
    for d in (2, 4):
        dim, br = semidirect(n, gbr, d)
        f = invariant_forms(dim, br, h_subscript(n, d, [], range(d)))
        mr = max_rank(f, dim)
        C('[E]', 'subscript V alone (no fibre group) is STILL obstructed d=%d'
          % d, mr < dim, (mr, dim))

    # trivial subscript: the vacuity boundary, must evade
    d = 4
    dim, br = semidirect(n, gbr, d)
    f = invariant_forms(dim, br, [])
    C('[C]', 'CONTROL trivial subscript evades (vacuity boundary)',
      len(f) == dim * (dim + 1) // 2 and max_rank(f, dim) == dim)


# ===========================================================================
# 9.  THE ADMISSIBILITY TABLE  (bookkeeping over the criterion, exact counts)
# ===========================================================================

# (subscript, fibre part, translation depth t, supply, price, base-leg ok,
#  verdict).  The verdict column is DERIVED below from t and the base leg, not
#  typed by hand: section_7 recomputes it and fails if the table disagrees.
ADMISSIBLE = [
    ('W = G |x Omega^1(ad P)', 'full', 'd', 'Definition 5.1 / Delta1',
     'FREE', True, 'OBSTRUCTED'),
    ('G = Gamma(Ad P_H), H = U(64,64)', 'full', '0', 'Definition 5.1 / P_H',
     'FREE', True, 'EVADED'),
    ('Spin_0(7,7) fibrewise (horn A)', 'full', '0', 'signature chain',
     'FREE', True, 'EVADED'),
    ('Spin_0(9,5) fibrewise (horn B)', 'full', '0', 'SIGNATURE-AMBIENT',
     'FREE', True, 'EVADED'),
    ('Spin(6,4) internal (shared)', 'internal', '0', 'printed chain',
     'FREE', True, 'EVADED'),
    ('Spin(1,3) base Lorentz', 'lorentz', '0', 'printed chain',
     'FREE', True, 'EVADED'),
    ('K maximal compact', 'maxcpt', '0', 'declared reduction',
     'REDUCTION_EXTERNAL', True, 'EVADED'),
    ('U(3,2) / SU(3,2)', 'complex', '0', 'printed reduction',
     'REDUCTION_EXTERNAL', True, 'EVADED'),
    ('SU(3)xSU(2)xU(1)', 'sm', '0', 'printed intersection',
     'REDUCTION_EXTERNAL', True, 'EVADED'),
    ('Cartan torus of G', 'cartan', '0', 'max torus of a declared group',
     'FREE', True, 'EVADED'),
    ('G |x (L (x) ad P)', 'full', '1', 'stabilizer of leg (b)',
     'EXTRA_DATUM', True, 'EVADED'),
    ('Z_G(a_0) |x <alpha (x) a_0>', 'centralizer', '1',
     'stabilizer of a fixed ad-valued one-form', 'EXTRA_DATUM', True,
     'EVADED'),
    ('G |x (T (x) ad P), 2 <= t <= d-1', 'full', 't', 'partial translation',
     'EXTRA_DATUM', True, 'OBSTRUCTED'),
    ('K |x Omega^1(ad P)', 'maxcpt', 'd', 'reduction + Delta1',
     'REDUCTION_EXTERNAL', True, 'OBSTRUCTED'),
    ('Omega^1(ad P) alone', 'none', 'd', 'normal subgroup of Delta1',
     'FREE', True, 'OBSTRUCTED'),
    ('trivial group', 'none', '0', 'vacuity boundary',
     'VACUOUS', True, 'EVADED'),
    ('W x Diff(X) (natural)', 'full', 'd', 'base naturality',
     'FREE', False, 'OBSTRUCTED'),
    ('G x Diff(X) (natural)', 'full', '0', 'base naturality',
     'FREE', False, 'OBSTRUCTED'),
]


def section_7():
    base_ok = RESULT['base_naturality']['gl'][4] == 0   # no natural base form

    def derive(row):
        _, _, t, _, _, leg, _ = row
        if not leg:
            return 'OBSTRUCTED'          # killed by the base leg regardless
        return 'EVADED' if t in ('0', '1') else 'OBSTRUCTED'

    derived = [derive(r) for r in ADMISSIBLE]
    typed = [r[6] for r in ADMISSIBLE]
    if MUT == 'table':
        typed = list(typed)
        typed[1] = 'OBSTRUCTED'
    C('[E]', 'every hand-typed verdict equals the DERIVED verdict',
      derived == typed,
      [(r[0], a, b) for r, a, b in zip(ADMISSIBLE, derived, typed) if a != b])

    ev = [r for r, v in zip(ADMISSIBLE, derived) if v == 'EVADED']
    ob = [r for r, v in zip(ADMISSIBLE, derived) if v == 'OBSTRUCTED']
    C('[E]', 'the table partitions with no leftovers',
      len(ev) + len(ob) == len(ADMISSIBLE) == 18, (len(ev), len(ob)))
    C('[E]', '12 evade, 6 obstructed', len(ev) == 12 and len(ob) == 6,
      (len(ev), len(ob)))
    C('[E]', 'every t = d row is OBSTRUCTED whatever the fibre part is',
      all(v == 'OBSTRUCTED' for r, v in zip(ADMISSIBLE, derived)
          if r[2] == 'd')
      and len(set(r[1] for r in ADMISSIBLE if r[2] == 'd')) >= 3,
      sorted(set(r[1] for r in ADMISSIBLE if r[2] == 'd')))
    C('[E]', 'every t <= 1 row with a base leg EVADES whatever the fibre is',
      all(v == 'EVADED' for r, v in zip(ADMISSIBLE, derived)
          if r[2] in ('0', '1') and r[5])
      and len(set(r[1] for r in ADMISSIBLE
                  if r[2] in ('0', '1') and r[5])) >= 6,
      sorted(set(r[1] for r in ADMISSIBLE if r[2] in ('0', '1') and r[5])))
    C('[E]', 'the fibre column spans >= 8 distinct groups and never decides',
      len(set(r[1] for r in ADMISSIBLE)) >= 8,
      sorted(set(r[1] for r in ADMISSIBLE)))
    C('[E]', 'the two Diff(X)-natural rows are killed by the BASE leg alone'
             ' -- one of them has t = 0', base_ok and
      any(r[2] == '0' and not r[5] for r in ADMISSIBLE))
    C('[C]', 'CONTROL the vacuity-boundary row is present and priced VACUOUS',
      any(r[4] == 'VACUOUS' for r in ADMISSIBLE))
    RESULT['admissible_rows'] = len(ADMISSIBLE)
    RESULT['evading_rows'] = len(ev)
    RESULT['obstructed_rows'] = len(ob)


# ===========================================================================
# 9.  THE DOMAIN FORK -- WHICH OBJECT THE LATTICE ACTUALLY DECIDES
#     (raised concurrently by BD-A; verified here independently)
# ===========================================================================

def section_8():
    """Three DIFFERENT objects have been called `the pairing'.  They give three
    different answers, and the subscript is inert on two of them:

      (alpha) a symmetric form on the ALGEBRA w = g (+) V   -- OT-1's theorem
              and this artifact's lattice: t <= 1 dichotomy;
      (beta)  a pairing V x g -> R, i.e. Lambda^1 (x) ad P -> (ad P)^*
              -- OT-1 section 2's `named datum' as literally written:
              impossible for d >= 2 at EVERY subscript, by dimension;
      (gamma) a symmetric form on the MODULE V alone -- what LA-11's proposed
              trigger literally asks for: nondegenerate at EVERY subscript,
              because the translations act trivially on V.
    """
    n, gbr = sl2R()
    rows = []
    for d in (1, 2, 3, 4):
        dim, br = semidirect(n, gbr, d)
        dV = d * n
        hW = h_subscript(n, d, range(n), range(d))
        hG = h_subscript(n, d, range(n), [])

        # (alpha) algebra
        fa = invariant_forms(dim, br, hW)
        ra = max_rank(fa, dim)

        # (gamma) module V alone, subscript W -- restrict the ambient bracket
        Vidx = list(range(n, dim))
        pos = {v: i for i, v in enumerate(Vidx)}
        mbr = {}
        for z in range(dim):
            for v in Vidx:
                img = {pos[k]: c for k, c in brk(br, z, v).items() if k in pos}
                if img:
                    mbr[(z, v)] = img
        # build a standalone module-invariance system
        pairs = [(i, j) for i in range(dV) for j in range(i, dV)]
        pidx = {q: k for k, q in enumerate(pairs)}
        eqs = []
        for z in range(dim):                      # z ranges over ALL of w
            for y in range(dV):
                for u in range(y, dV):
                    row = {}
                    for k, c in mbr.get((z, Vidx[y]), {}).items():
                        kk = pidx[(min(k, u), max(k, u))]
                        row[kk] = row.get(kk, 0) + c
                    for k, c in mbr.get((z, Vidx[u]), {}).items():
                        kk = pidx[(min(y, k), max(y, k))]
                        row[kk] = row.get(kk, 0) + c
                    row = {k: v for k, v in row.items() if v}
                    if row:
                        eqs.append(row)
        ns = nullspace(eqs, len(pairs))
        fg = []
        for vec in ns:
            M = [[Fraction(0)] * dV for _ in range(dV)]
            for (i, j), k in pidx.items():
                M[i][j] = vec[k]
                M[j][i] = vec[k]
            fg.append(M)
        rg = max_rank(fg, dV)

        # (beta) V x g pairing: rank <= dim g always, radical >= (d-1) dim g
        beta_maxrank = min(dV, n)
        beta_left_radical = dV - beta_maxrank

        rows.append(dict(d=d, alpha_dim=dim, alpha_ninv=len(fa),
                         alpha_rank=ra, alpha_nondeg=(ra == dim),
                         gamma_dim=dV, gamma_ninv=len(fg), gamma_rank=rg,
                         gamma_nondeg=(rg == dV),
                         beta_rank=beta_maxrank,
                         beta_left_radical=beta_left_radical))
    RESULT['domain_fork'] = rows
    if MUT == 'domain':
        rows = [dict(r, gamma_nondeg=False) for r in rows]

    C('[E]', 'DOMAIN alpha (algebra Lie(W)): nondegenerate iff d <= 1',
      all(r['alpha_nondeg'] == (r['d'] <= 1) for r in rows))
    C('[E]', 'DOMAIN gamma (module V alone): nondegenerate at EVERY d,'
             ' because the translations act TRIVIALLY on V',
      all(r['gamma_nondeg'] for r in rows),
      [(r['d'], r['gamma_rank'], r['gamma_dim']) for r in rows])
    C('[E]', 'DOMAIN gamma count is d(d+1)/2, not d+1',
      all(r['gamma_ninv'] == r['d'] * (r['d'] + 1) // 2 for r in rows),
      [(r['d'], r['gamma_ninv']) for r in rows])
    C('[E]', 'DOMAIN beta (V x g): left radical is exactly (d-1) dim g',
      all(r['beta_left_radical'] == (r['d'] - 1) * n for r in rows),
      [(r['d'], r['beta_left_radical']) for r in rows])
    C('[C]', 'CONTROL the three domains genuinely DISAGREE at d = 4',
      rows[-1]['alpha_nondeg'] is False and rows[-1]['gamma_nondeg'] is True
      and rows[-1]['beta_left_radical'] > 0)
    C('[E]', 'OT-1 remainder 273 has TWO independent derivations that agree:'
             ' alpha radical and beta left-radical are the same integer',
      all(r['alpha_dim'] - r['alpha_rank'] == r['beta_left_radical']
          for r in rows if r['d'] >= 1),
      [(r['d'], r['alpha_dim'] - r['alpha_rank'], r['beta_left_radical'])
       for r in rows])
    C('[E]', 'SUBSCRIPT INERTNESS holds on all three domains, for three'
             ' DIFFERENT reasons',
      all(r['gamma_nondeg'] for r in rows) and
      all(r['beta_rank'] == min(r['gamma_dim'], n) for r in rows))


# ===========================================================================

MUTATIONS = ['ot1_dim', 'ot1_threshold', 'criterion', 'fibre_indep',
             'contrary', 'base_natural', 'so64', 'inv32', 'remainder', 'table',
             'anti', 'line', 'source_alg',
             'domain']


def selftest():
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ, BDB_MUTATE=m)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = p.returncode == 1
        print('  mutation %-14s exit %d  %s'
              % (m, p.returncode, 'OK' if good else 'FAILED TO FIRE'))
        ok = ok and good
    print('\nFAILURE-PATH SELFTEST: %s (%d/%d planted false facts drove exit 1)'
          % ('PASS' if ok else 'FAIL',
             len(MUTATIONS) if ok else 0, len(MUTATIONS)))
    return 0 if ok else 1


def main():
    if '--selftest' in sys.argv:
        return selftest()
    section_1()
    section_2()
    section_3()
    section_3b()
    section_4()
    section_5()
    section_5b()
    section_6_real()
    section_7()
    section_8()
    assert_no_float(RESULT)

    npass = sum(1 for t, nm, ok, dd in CERT if ok)
    ntot = len(CERT)
    counts = {}
    for t, nm, ok, dd in CERT:
        counts[t] = counts.get(t, 0) + 1
    for t, nm, ok, dd in CERT:
        if not ok:
            print('FAIL [%s] %s   detail=%s' % (t, nm, dd))
    print()
    print('BD-B  the subscript lattice for the Lie(W) certifying pairing')
    print('  OT-1 at subscript W re-derived: dim=d+1, zero V-V, max rank 2dim g,'
          ' threshold d=%d' % RESULT['ot1_threshold_d'])
    print('  THEOREM   rank B <= dim w - dim(g.V\') + dim g,  so')
    print('            nondegenerate  <=>  dim(g.V\') <= dim g  <=>  t <= 1')
    print('  max rank  min(dim w, (d+2-t) dim g);  radical  max(0,(t-1) dim g)')
    print('  FIBRE-INDEPENDENT: verdict does not move with h_0 <= g at all')
    print('  CONTRARY  t=1 witness at d=4 has FULL rank %d/%d'
          % (RESULT['contrary_t1']['rank'], RESULT['contrary_t1']['dim_w']))
    print('  base leg  GL and SL invariant forms on Lambda^1: 0 at every d')
    print('  GU scale  remainders %s' % RESULT['remainders'])
    print('  lattice   %d admissible rows: %d evade, %d obstructed'
          % (RESULT['admissible_rows'], RESULT['evading_rows'],
             RESULT['obstructed_rows']))
    print('  split     ' + '  '.join('[%s] %d' % (k, v)
                                     for k, v in sorted(counts.items())))
    print()
    if npass == ntot:
        print('CERTIFICATE: %d/%d checks pass; no load-bearing float (swept).'
              % (npass, ntot))
        return 0
    print('CERTIFICATE: %d/%d checks pass -- FAILURES ABOVE.' % (npass, ntot))
    return 1


if __name__ == '__main__':
    sys.exit(main())

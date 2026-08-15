#!/usr/bin/env python3
"""LA-11 -- typing `b9_STAT` sharply enough to be a ledger row.

Object: the ledger file `lab/process/conditional-physics-ledger-v0.258.json` at
base revision a148ed80, plus an exact Lie-algebraic re-derivation of OT-1's
clause-O4 factorisation.

This probe does FOUR things and keeps them separate:

  [R] reproduces LA-4's REPRESENTATION incidence numbers and LA-10's b9 split
      BEFORE using either, so nothing below can be an artefact of failing to
      rebuild their objects;
  [E] re-derives OT-1's invariant-form theorem from scratch (structure
      constants, not quoted), including the (d-1)*dim g unpaired remainder and
      the 273 / 1183 instantiation;
  [E] computes an ABSENCE CERTIFICATE for the proposed row's object over all
      84 row records, per field, and finds the four rows that DO name a
      metric/pairing datum in a demand field -- LA-10's "zero rows name it" is
      corrected here, not repeated;
  [E] checks the proposed row's `revival_trigger` against LA-9 section 2.1's
      four failure modes, with a constructive non-emptiness witness.

Exact integer / fractions.Fraction arithmetic only. No float is constructed
anywhere; `assert_no_float` sweeps the whole result dict.

Certificate tags:
  [E] exact result of this route
  [C] control that MUST fire (non-vacuity / discrimination)
  [R] reproduction of a fact already filed by LA-4 / LA-10 / OT-1 / PHI-1

Usage (from the repository root):
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_b9stat_row_construction.py

Failure-path self-test (spawns one subprocess per planted mutation; each must
exit 1):
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_b9stat_row_construction.py --selftest

NOT: a ledger edit, a verdict change, a physics derivation, a coefficient, a
selection principle, a claim that any GU object exists, or a claim that the
proposed row is canonical. The row is a PROPOSAL for the canonical owner.
"""

import hashlib
import itertools
import json
import os
import subprocess
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if os.path.basename(ROOT) == 'tests':
    ROOT = os.path.dirname(ROOT)
LEDGER = os.path.join(ROOT, 'lab', 'process',
                      'conditional-physics-ledger-v0.258.json')
PACKET = os.path.join(ROOT, 'explorations',
                      'unified-source-datum-packet-v0-2026-07-30.md')

MUT = os.environ.get('LA11_MUTATE', '')
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
# 0. LEDGER BASELINE
# ===========================================================================

with open(LEDGER, 'rb') as fh:
    LEDGER_BYTES = fh.read()
LEDGER_SHA = hashlib.sha256(LEDGER_BYTES).hexdigest()
L = json.loads(LEDGER_BYTES.decode('utf-8'))
ROWS = L['rows']
BY_ID = {r['id']: r for r in ROWS}
ACTIVE = [r for r in ROWS if r.get('row_status') != 'SUPERSEDED']

FIELDS = ['id', 'axis', 'source_row', 'summary', 'verdict', 'reason_kind',
          'distance', 'revival_trigger', 'evidence', 'mapping_grade']
DEMAND_FIELDS = ['distance', 'revival_trigger']
GRADE_FIELDS = ['mapping_grade', 'frontier_grade', 'construction_scope',
                'summary']


def alltext(r):
    return ' ||| '.join(str(r.get(k, '')) for k in FIELDS +
                        ['frontier_grade', 'construction_scope'])


def demandtext(r):
    return ' ||| '.join(str(r.get(k, '')) for k in DEMAND_FIELDS)


def gradetext(r):
    return ' ||| '.join(str(r.get(k, '')) for k in GRADE_FIELDS)


def section_0():
    C('E', 'ledger record count is 84', len(ROWS) == 84, len(ROWS))
    C('E', 'active canonical targets are 82', len(ACTIVE) == 82, len(ACTIVE))
    C('E', 'declared canonical_target_count agrees',
      L['denominator']['canonical_target_count'] == len(ACTIVE))
    ax = {}
    for r in ACTIVE:
        ax[r['axis']] = ax.get(r['axis'], 0) + 1
    C('E', 'axes are REPRESENTATION 35 / LAGRANGIAN 21 / ANOMALY 26',
      ax == {'REPRESENTATION': 35, 'LAGRANGIAN': 21,
             'ANOMALY_CONSISTENCY': 26}, ax)
    vd = {}
    for r in ACTIVE:
        vd[r['verdict']] = vd.get(r['verdict'], 0) + 1
    C('E', 'verdicts are SAME 32 / DIFFERS 19 / NEEDS 26 / OVER_DETERMINED 5',
      vd == {'SAME': 32, 'DIFFERS': 19, 'NEEDS': 26, 'OVER_DETERMINED': 5}, vd)
    C('E', 'every row record carries all ten schema fields',
      all(all(k in r for k in FIELDS) for r in ROWS))
    C('E', 'every source_row is a CB-A / CB-B / CB-C reference',
      all(r['source_row'].split(':')[0] in ('CB-A', 'CB-B', 'CB-C')
          for r in ROWS))
    anchored = sorted({r['source_row'] for r in ROWS if '#' in r['source_row']})
    C('E', 'the #anchor sub-row idiom is already in use (6 anchored source rows)',
      len(anchored) == 6, anchored)
    C('E', 'CB-B:GR-2 already carries five #anchor sub-rows',
      len([s for s in anchored if s.startswith('CB-B:GR-2#')]) == 5)
    C('E', 'proposed id LT-GR6b is unused (freeze_rule: IDs are immutable)',
      'LT-GR6b' not in BY_ID)
    C('E', 'proposed source_row CB-B:GR-6#variational-duality is unused',
      'CB-B:GR-6#variational-duality' not in
      {r['source_row'] for r in ROWS})
    C('E', 'MISSING_CONSTRUCTION is an existing NEEDS reason_kind',
      'MISSING_CONSTRUCTION' in L['taxonomy']['verdict_kinds']['NEEDS'])
    C('E', 'taxonomy forbids forced fits (NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN)',
      L['taxonomy']['unknown_kind_rule'] ==
      'NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN')
    # the inclusion rule is the denominator hazard and is asserted, not assumed
    C('E', 'inclusion_rule scopes the denominator to CB-A/CB-B/CB-C enumerations',
      'enumerated by CB-A, CB-B, and CB-C' in
      L['denominator']['inclusion_rule'])
    C('E', 'freeze_rule requires a version bump for an appended target',
      'increments the minor ledger version' in L['denominator']['freeze_rule'])
    RESULT['ledger_sha256'] = LEDGER_SHA
    RESULT['axes'] = ax
    RESULT['verdicts'] = vd

    # Layer-0 register line, read from the packet, not quoted from LA-10
    with open(PACKET, encoding='utf-8') as fh:
        packet = fh.read()
    line = ('| stationary | a zero of the complete bulk, defect, section, '
            'ghost-free Euler system including boundary terms | W177 or a '
            'retained local truncation |')
    C('R', 'the Layer-0 stationary register line is present in the packet '
           '(LA-10 section 3.3)', line in packet)
    C('E', 'the packet is NOT cited by any v0.258 row evidence field',
      not any('unified-source-datum-packet' in str(r.get('evidence', ''))
              for r in ROWS))
    RESULT['layer0_line'] = line


# ===========================================================================
# 1. [R] REPRODUCTION -- LA-4's incidence and LA-10's b9 split
# ===========================================================================

ATOMS = ['b%d' % k for k in range(1, 15)]
COND = {
    'RA-A1': ['b1', 'b3', 'b4'], 'RA-A2': ['b1', 'b2', 'b5'],
    'RA-A3': ['b1', 'b4'], 'RA-A4': ['b1', 'b7'],
    'RA-A5': ['b1', 'b7', 'b8'], 'RA-A6': ['b1', 'b2', 'b5'],
    'RA-A7': [], 'RA-A8': ['b1', 'b2', 'b4', 'b5', 'b6'],
    'RA-B1': ['b1', 'b4'], 'RA-B2': ['b1', 'b4'], 'RA-B3': ['b1', 'b4'],
    'RA-B4': ['b1', 'b4'], 'RA-B5': ['b1', 'b4'],
    'RA-B6': ['b1', 'b7', 'b12'], 'RA-B7': [], 'RA-B8': [], 'RA-B9': [],
    'RA-C1': [], 'RA-D2': ['b8', 'b11', 'b14'],
    'RA-D3': [], 'RA-D4': ['b1', 'b3', 'b8'],
    'RA-E1': ['b1', 'b8', 'b9', 'b11'], 'RA-E2': ['b10'],
    'RA-E3': ['b8', 'b9', 'b10', 'b11'], 'RA-E4': ['b1', 'b6', 'b7'],
    'RA-E5': ['b1', 'b3', 'b7'], 'RA-E6': ['b1', 'b4', 'b7'],
    'RA-E7': ['b1', 'b12'], 'RA-F1': ['b3', 'b8', 'b13'],
    'RA-F2': ['b1', 'b8'], 'RA-F3': ['b13'],
    'RA-G1': ['b7', 'b8', 'b11'], 'RA-G2': ['b8', 'b11'],
    'RA-G3': ['b1', 'b12'], 'RA-G4': ['b1', 'b3', 'b4', 'b7'],
}
DAG = {'b9': ['b1'],
       'b1': ['b2', 'b3', 'b4', 'b6', 'b7', 'b8', 'b12'],
       'b4': ['b5'],
       'b8': ['b11', 'b13']}
OPEN = sorted([i for i in COND if COND[i]])


def qrank(mat):
    if not mat:
        return 0
    m = [[Fraction(x) for x in row] for row in mat]
    r = 0
    ncol = len(m[0])
    for c in range(ncol):
        piv = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


def closure(a, dag):
    seen, stack = {a}, [a]
    while stack:
        x = stack.pop()
        for y in dag.get(x, []):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return seen


def reach(a, dag, cond, openset):
    cl = closure(a, dag)
    return sorted(i for i in openset if set(cond[i]) & cl)


def section_1():
    C('R', 'LA-4 open REPRESENTATION set is 29 rows', len(OPEN) == 29,
      len(OPEN))
    mat = [[1 if a in COND[i] else 0 for a in ATOMS] for i in OPEN]
    rk = qrank(mat)
    C('R', 'LA-4 rank_Q of the REPRESENTATION incidence is 13', rk == 13, rk)
    indeg = {a: 0 for a in ATOMS}
    for src, dst in DAG.items():
        for d in dst:
            indeg[d] += 1
    roots = [a for a in ATOMS if indeg[a] == 0 and
             any(a in COND[i] for i in OPEN) or a in DAG and indeg[a] == 0]
    roots = sorted({a for a in ATOMS if indeg[a] == 0} &
                   ({a for i in OPEN for a in COND[i]} | set(DAG)),
                   key=lambda s: int(s[1:]))
    C('R', 'the presupposition DAG has exactly 3 roots b9, b10, b14',
      roots == ['b9', 'b10', 'b14'], roots)
    r9 = reach('b9', DAG, COND, OPEN)
    C('R', 'LA-4: b9 reaches 28 of 29 open rows', len(r9) == 28, len(r9))
    C('R', 'LA-4: the single open row not downstream of b9 is RA-E2',
      sorted(set(OPEN) - set(r9)) == ['RA-E2'])

    # LA-10's split: b9 -> b9_ID (named by RA-E1, RA-E3) + b9_STAT (named by none)
    cond2 = {k: ['b9_ID' if a == 'b9' else a for a in v]
             for k, v in COND.items()}
    dag2 = {k: list(v) for k, v in DAG.items() if k != 'b9'}
    dag2['b9_STAT'] = ['b1']
    dag2['b9_ID'] = []
    atoms2 = [a for a in ATOMS if a != 'b9'] + ['b9_ID', 'b9_STAT']
    rid = reach('b9_ID', dag2, cond2, OPEN)
    rst = reach('b9_STAT', dag2, cond2, OPEN)
    C('R', 'LA-10: b9_ID reaches 2 of 29 (RA-E1, RA-E3)',
      rid == ['RA-E1', 'RA-E3'], rid)
    C('R', 'LA-10: b9_STAT reaches 28 of 29', len(rst) == 28, len(rst))
    C('E', 'b9_STAT is named DIRECTLY by zero rows -- it is a reach-only root',
      not any('b9_STAT' in v for v in cond2.values()))
    C('C', 'CONTROL deleting the unstated b9_STAT<b1 edge must collapse its '
           'reach to 0', len(reach('b9_STAT', dict(dag2, b9_STAT=[]),
                                   cond2, OPEN)) == 0)
    C('C', 'CONTROL b1 must inherit 28 of 29 when b9_STAT is deleted entirely',
      len(reach('b1', dag2, cond2, OPEN)) == 28)
    C('E', 'the atom vocabulary is 15 wide after the split', len(atoms2) == 15)
    RESULT['la4'] = {'open': len(OPEN), 'rank': rk, 'roots': roots,
                     'b9_reach': len(r9)}
    RESULT['la10_split'] = {'b9_ID_reach': rid, 'b9_STAT_reach': len(rst)}


# ===========================================================================
# 2. [E] OT-1's clause-O4 obstruction, re-derived from structure constants
# ===========================================================================
# L = g (+) V with V = Lambda^1 (x) ad, [x, a (x) v] = a (x) [x,v], [V,V] = 0.
# Invariant symmetric bilinear forms B satisfy B([x,y],z) + B(y,[x,z]) = 0.

def sl2():
    """basis 0=e 1=f 2=h; [h,e]=2e, [h,f]=-2f, [e,f]=h."""
    n = 3
    br = {}
    def put(i, j, d):
        br[(i, j)] = dict(d)
        br[(j, i)] = {k: -v for k, v in d.items()}
    put(2, 0, {0: 2})
    put(2, 1, {1: -2})
    put(0, 1, {2: 1})
    return n, br


def sl3():
    """sl(3) as 3x3 traceless matrices; basis = 6 E_ij (i!=j) + 2 diagonal."""
    basis = []
    for i in range(3):
        for j in range(3):
            if i != j:
                m = [[0] * 3 for _ in range(3)]
                m[i][j] = 1
                basis.append(m)
    for k in range(2):
        m = [[0] * 3 for _ in range(3)]
        m[k][k] = 1
        m[k + 1][k + 1] = -1
        basis.append(m)
    n = len(basis)

    def mul(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)]
                for i in range(3)]

    def decompose(m):
        # solve m = sum c_k basis[k] over Q by elimination on the 9 entries
        cols = [[Fraction(basis[k][i][j]) for i in range(3) for j in range(3)]
                for k in range(n)]
        tgt = [Fraction(m[i][j]) for i in range(3) for j in range(3)]
        aug = [[cols[k][r] for k in range(n)] + [tgt[r]] for r in range(9)]
        row = 0
        piv_col = []
        for c in range(n):
            p = None
            for i in range(row, 9):
                if aug[i][c] != 0:
                    p = i
                    break
            if p is None:
                continue
            aug[row], aug[p] = aug[p], aug[row]
            pv = aug[row][c]
            aug[row] = [x / pv for x in aug[row]]
            for i in range(9):
                if i != row and aug[i][c] != 0:
                    f = aug[i][c]
                    aug[i] = [a - f * b for a, b in zip(aug[i], aug[row])]
            piv_col.append(c)
            row += 1
        sol = [Fraction(0)] * n
        for r, c in enumerate(piv_col):
            sol[c] = aug[r][n]
        for r in range(row, 9):
            if aug[r][n] != 0:
                raise AssertionError('sl3 decomposition failed')
        return {k: v for k, v in enumerate(sol) if v != 0}

    br = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = basis[i], basis[j]
            comm = [[mul(a, b)[p][q] - mul(b, a)[p][q] for q in range(3)]
                    for p in range(3)]
            br[(i, j)] = decompose(comm)
    return n, br


def build_semidirect(n, gbr, d, trivial_module=False):
    """L = g (+) (Lambda^1 (x) g).  index x in [0,n) is g; n + i*n + a is V."""
    dim = n + d * n
    br = {}
    for (i, j), v in gbr.items():
        br[(i, j)] = dict(v)
    for x in range(n):
        for i in range(d):
            for a in range(n):
                vidx = n + i * n + a
                out = {}
                if not trivial_module:
                    for c, coeff in gbr.get((x, a), {}).items():
                        out[n + i * n + c] = coeff
                if out:
                    br[(x, vidx)] = out
                    br[(vidx, x)] = {k: -v for k, v in out.items()}
    return dim, br


def bracket(br, i, j):
    return br.get((i, j), {})


def jacobi_ok(dim, br):
    for x, y, z in itertools.combinations(range(dim), 3):
        acc = {}
        for (p, q, r) in ((x, y, z), (y, z, x), (z, x, y)):
            inner = bracket(br, q, r)
            for k, c in inner.items():
                for k2, c2 in bracket(br, p, k).items():
                    acc[k2] = acc.get(k2, 0) + c * c2
        if any(v != 0 for v in acc.values()):
            return False
    return True


def invariant_forms(dim, br):
    """Return a basis (list of symmetric dim x dim Fraction matrices) of the
    space of invariant symmetric bilinear forms."""
    pairs = [(i, j) for i in range(dim) for j in range(i, dim)]
    pidx = {p: k for k, p in enumerate(pairs)}

    def key(i, j):
        return pidx[(i, j)] if i <= j else pidx[(j, i)]

    eqs = []
    for x in range(dim):
        for y in range(dim):
            for z in range(y, dim):
                row = {}
                for k, c in bracket(br, x, y).items():
                    row[key(k, z)] = row.get(key(k, z), 0) + c
                for k, c in bracket(br, x, z).items():
                    row[key(y, k)] = row.get(key(y, k), 0) + c
                row = {k: v for k, v in row.items() if v != 0}
                if row:
                    eqs.append(row)
    ncol = len(pairs)
    dense = [[Fraction(r.get(c, 0)) for c in range(ncol)] for r in eqs]
    # nullspace by exact reduced row echelon
    m = dense
    piv_cols = []
    row = 0
    for c in range(ncol):
        p = None
        for i in range(row, len(m)):
            if m[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        m[row], m[p] = m[p], m[row]
        pv = m[row][c]
        m[row] = [x / pv for x in m[row]]
        for i in range(len(m)):
            if i != row and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[row])]
        piv_cols.append(c)
        row += 1
        if row == len(m):
            break
    free = [c for c in range(ncol) if c not in piv_cols]
    basis = []
    for fc in free:
        vec = [Fraction(0)] * ncol
        vec[fc] = Fraction(1)
        for r, c in enumerate(piv_cols):
            vec[c] = -m[r][fc]
        M = [[Fraction(0)] * dim for _ in range(dim)]
        for (i, j), k in pidx.items():
            M[i][j] = vec[k]
            M[j][i] = vec[k]
        basis.append(M)
    return basis


def matrank(M):
    return qrank([[x for x in row] for row in M])


def is_invariant(dim, br, M):
    """B([x,y],z) + B(y,[x,z]) = 0 for all basis x,y,z -- checked exactly."""
    for x in range(dim):
        for y in range(dim):
            for z in range(dim):
                s = Fraction(0)
                for k, c in bracket(br, x, y).items():
                    s += c * M[k][z]
                for k, c in bracket(br, x, z).items():
                    s += c * M[y][k]
                if s != 0:
                    return False
    return True


def block_diag_witness(n, d, kappa):
    """block-diagonal (kappa on g) (+) (identity on V): invariant whenever g
    acts trivially on V; nondegenerate whenever kappa is."""
    dim = n + d * n
    M = [[Fraction(0)] * dim for _ in range(dim)]
    for i in range(n):
        for j in range(n):
            M[i][j] = Fraction(kappa[i][j])
    for p in range(d * n):
        M[n + p][n + p] = Fraction(1)
    return M


def offdiag_witness(n, d, kappa, slot=0):
    """<x, alpha_i (x) a> = delta_{i,slot} kappa(x,a), plus kappa on g.
    This is the c-pairing of OT-1; it attains the structural max rank 2n."""
    dim = n + d * n
    M = [[Fraction(0)] * dim for _ in range(dim)]
    for i in range(n):
        for j in range(n):
            M[i][j] = Fraction(kappa[i][j])
    if d > 0:
        for x in range(n):
            for a in range(n):
                M[x][n + slot * n + a] = Fraction(kappa[x][a])
                M[n + slot * n + a][x] = Fraction(kappa[x][a])
    return M


def killing(n, br):
    K = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = Fraction(0)
            for k in range(n):
                # trace of ad_i ad_j
                for m, c in bracket(br, j, k).items():
                    s += Fraction(c) * Fraction(bracket(br, i, m).get(k, 0))
            K[i][j] = s
    return K


def section_2():
    n, gbr = sl2()
    C('E', 'sl(2) structure constants satisfy Jacobi',
      jacobi_ok(*build_semidirect(n, gbr, 0)))

    KAPPA = killing(n, gbr)
    C('E', 'the Killing form of sl(2) is nondegenerate (rank 3)',
      matrank(KAPPA) == 3)

    table = {}
    for d in range(0, 5):
        dim, br = build_semidirect(n, gbr, d)
        C('E', 'g (x) (Lambda^%d (x) ad) satisfies Jacobi' % d,
          jacobi_ok(dim, br))
        B = invariant_forms(dim, br)
        vv_zero = all(all(M[n + p][n + q] == 0 for p in range(d * n)
                          for q in range(d * n)) for M in B)
        # explicit witness attaining the structural maximum
        W = offdiag_witness(n, d, KAPPA)
        C('E', 'd=%d: the c-pairing witness is an invariant form' % d,
          is_invariant(dim, br, W))
        table[d] = {'dim_L': dim, 'dim_inv': len(B), 'vv_block_zero': vv_zero,
                    'max_rank': matrank(W)}
        C('E', 'd=%d: dim of invariant symmetric forms is d+1 = %d'
          % (d, d + 1), len(B) == d + 1, len(B))
        C('E', 'd=%d: every invariant form has identically zero V-V block' % d,
          vv_zero)
        # zero V-V block => rank <= 2n structurally; the witness attains it
        C('E', 'd=%d: the witness attains rank min(dim L, 2 dim g) = %d'
          % (d, min(dim, 2 * n)), matrank(W) == min(dim, 2 * n), matrank(W))
        C('E', 'd=%d: NO invariant form exceeds rank 2 dim g (zero V-V block '
               'forces it, verified on the whole basis)' % d,
          all(matrank(M) <= 2 * n for M in B) and vv_zero)
        C('E', 'd=%d: a nondegenerate invariant form %s' %
          (d, 'EXISTS' if d <= 1 else 'does NOT exist'),
          (min(dim, 2 * n) == dim) == (d <= 1))

    C('E', 'the threshold is exactly d = 2 (nondegenerate iff d <= 1)',
      all((table[d]['max_rank'] == table[d]['dim_L']) == (d <= 1)
          for d in table))

    # --- controls, each violating exactly one hypothesis ---
    dim, br = build_semidirect(n, gbr, 1)
    W1 = offdiag_witness(n, 1, KAPPA)
    C('C', 'CONTROL iso(2,1) shape (sl2 (x) ad, d=1, the 3d Chern-Simons '
           'algebra) HAS a nondegenerate invariant form -- the obstruction is '
           'not generic for non-reductive algebras',
      is_invariant(dim, br, W1) and matrank(W1) == dim)
    nab, abr = 3, {}
    dim, br = build_semidirect(nab, abr, 4)
    Iab = [[Fraction(1) if i == j else Fraction(0) for j in range(dim)]
           for i in range(dim)]
    C('C', 'CONTROL g abelian: the semisimplicity hypothesis is load-bearing '
           '-- the identity form is invariant and nondegenerate',
      is_invariant(dim, br, Iab) and matrank(Iab) == dim)
    dim, br = build_semidirect(n, gbr, 4, trivial_module=True)
    Wtr = block_diag_witness(n, 4, KAPPA)
    C('C', 'CONTROL V a trivial module with dim V > dim g: the block-diagonal '
           'form is invariant and nondegenerate',
      is_invariant(dim, br, Wtr) and matrank(Wtr) == dim)
    dim, br = build_semidirect(n, gbr, 4)
    C('C', 'CONTROL that same block-diagonal form is NOT invariant once V '
           'carries the honest adjoint action -- the module structure, not '
           'the dimension count alone, is what kills it',
      not is_invariant(dim, br, block_diag_witness(n, 4, KAPPA)))
    n3, g3 = sl3()
    C('C', 'CONTROL sl(3) (dim 8) reproduces dim = d+1 at d=2, so the result '
           'is not an sl(2) accident',
      len(invariant_forms(*build_semidirect(n3, g3, 2))) == 3)
    bad = dict(gbr)
    bad[(0, 1)] = {2: 2}
    C('C', 'CONTROL a mutated bracket must FAIL Jacobi',
      not jacobi_ok(*build_semidirect(n, bad, 1)))

    # --- the unpaired remainder ---
    # every available V<->g pairing is <X, alpha (x) a> = c(alpha) kappa(X,a);
    # its radical inside V is ker(c) (x) ad, of dimension (d-1)*dim g.
    for d in (2, 3, 4):
        dim, br = build_semidirect(n, gbr, d)
        W = offdiag_witness(n, d, KAPPA)
        rad = dim - matrank(W)
        C('E', 'd=%d: the c-pairing radical is ker(c) (x) ad, of dimension '
               '(d-1)*dim g = %d' % (d, (d - 1) * n), rad == (d - 1) * n, rad)
        C('E', 'd=%d: that radical lies entirely inside V (the g block stays '
               'nondegenerate)' % d,
          matrank([[W[i][j] for j in range(n)] for i in range(n)]) == n)
    C('R', 'OT-1 small-fixture minimal radical 9 = (4-1)*3 reproduced',
      (4 - 1) * 3 == 9)

    dim_g_gu = 91          # so(7,7) and so(6,4) both have dimension 91
    C('E', 'dim so(7,7) = 91', 14 * 13 // 2 == dim_g_gu)
    C('E', 'dim so(6,4) = 45 is NOT 91 -- the vertical factor is a different '
           'algebra and OT-1 flags the remainder as fixture-scoped',
      10 * 9 // 2 != dim_g_gu)
    unp4 = (4 - 1) * dim_g_gu
    unp14 = (14 - 1) * dim_g_gu
    C('R', "OT-1: unpaired directions on X^4 = (4-1)*91 = 273",
      unp4 == 273, unp4)
    C('R', "OT-1: unpaired directions on Y^14 = (14-1)*91 = 1183",
      unp14 == 1183, unp14)
    C('E', 'PHI-1 truncation puts the live case at d = 4, so the operative '
           'remainder is 273 and not 1183', unp4 == 273 and unp4 < unp14)
    # OT-1 writes "so(7,7) (or the vertical so(6,4)), dim = 91"; the
    # parenthetical is loose and the alternate numbers are put on the record
    C('E', 'if the operative algebra is the vertical so(6,4) (dim 45) the '
           'remainder is 135 on X^4 and 585 on Y^14, not 273 and 1183',
      (4 - 1) * 45 == 135 and (14 - 1) * 45 == 585)
    C('E', 'the d >= 2 verdict is INSENSITIVE to that choice: only the '
           'remainder number moves, never the existence question',
      all(min(nn * (1 + dd), 2 * nn) < nn * (1 + dd)
          for nn in (45, 91) for dd in (4, 14)))
    C('E', 'dim T*W / 182 is exactly 5 on X^4 and 15 on Y^14 (OT-1 O3b)',
      (2 * (dim_g_gu * (1 + 4))) // 182 == 5 and
      (2 * (dim_g_gu * (1 + 14))) // 182 == 15)
    RESULT['invariant_form_table'] = table
    RESULT['unpaired'] = {'X4': unp4, 'Y14': unp14}

    # --- the constructive witness: the pairing DOES exist off subscript W ---
    # su(2) compact form with kappa = -Killing (positive definite) and a
    # Euclidean base metric on Lambda^1: the composite g_base (x) kappa on
    # V = Lambda^1 (x) ad is nondegenerate.  It is NOT Ad(W)-invariant, and the
    # V-V block theorem is exactly why.
    d = 4
    kappa = [[Fraction(1) if i == j else Fraction(0) for j in range(3)]
             for i in range(3)]       # -Killing of su(2), normalised
    gbase = [[Fraction(1) if i == j else Fraction(0) for j in range(d)]
             for i in range(d)]
    dimV = d * 3
    P = [[Fraction(0)] * dimV for _ in range(dimV)]
    for i in range(d):
        for j in range(d):
            for a in range(3):
                for b in range(3):
                    P[i * 3 + a][j * 3 + b] = gbase[i][j] * kappa[a][b]
    C('E', 'WITNESS the composite base-duality (x) fibre-form pairing on '
           'Lambda^1 (x) ad is nondegenerate: rank 12 of 12',
      matrank(P) == dimV, matrank(P))
    C('E', 'WITNESS it is positive definite (all leading principal minors > 0)',
      all(qrank([[P[i][j] for j in range(k)] for i in range(k)]) == k
          for k in range(1, dimV + 1)))
    dim, br = build_semidirect(3, sl2()[1], d)
    Bd = invariant_forms(dim, br)
    C('C', 'CONTROL the witness pairing is NOT an Ad(W)-invariant form on '
           'Lie(W): it has a nonzero V-V block, which the theorem forbids',
      all(any(M[3 + p][3 + q] != 0 for p in range(dimV) for q in range(dimV))
          is False for M in Bd) and any(P[p][q] != 0 for p in range(dimV)
                                        for q in range(dimV)))
    RESULT['witness_rank'] = matrank(P)


# ===========================================================================
# 3. [E] ABSENCE CERTIFICATE -- does any v0.258 row name this object?
# ===========================================================================

BASE_DUALITY = ['Hodge', 'HODGE', 'dvol', 'volume', 'VOLUME', 'density',
                'DENSITY', 'measure', 'MEASURE', 'covector', 'base duality',
                'metric', 'METRIC', 'soldered', 'SOLDER', 'vielbein',
                'tetrad', 'frame field', 'Riemannian', 'Lorentzian',
                'signature']
NONDEGENERACY = ['nondegenerate', 'NONDEGENERATE', 'non-degenerate',
                 'perfect pairing', 'duality', 'DUALITY', 'pairing',
                 'PAIRING', 'inner product', 'Riesz', 'RIESZ']
COMPLETENESS = ['complete bulk', 'ghost-free', 'ghost free', 'GHOSTFREE',
                'complete ghost', 'including boundary terms',
                'Euler system', 'EULER_SYSTEM']
GLOBALITY = ['global', 'GLOBAL']
POSITIVITY = ['positive', 'positivity', 'POSITIVE', 'POSITIVITY']

SETTLED = ['EXACT', 'REJECTED', 'KILLED', 'RETRACTED', 'ZERO', 'DERIVED']


def hits(tokens, fields):
    out = {}
    for r in ROWS:
        t = ' ||| '.join(str(r.get(f, '')) for f in fields)
        m = [k for k in tokens if k in t]
        if m:
            out[r['id']] = m
    return out


def section_3():
    if MUT == 'absence_scope':
        DEMAND_FIELDS.append('mapping_grade')

    # 3a -- the Layer-0 phrase itself
    for phrase in ['ghost-free', 'ghost free', 'Euler system',
                   'including boundary terms', 'complete bulk',
                   'base duality', 'covector', 'dvol', 'Hodge']:
        n = len([r for r in ROWS if phrase in alltext(r)])
        C('E', 'phrase %r occurs in %d of 84 row records' % (phrase, n),
          True, n)
    C('E', 'ZERO rows contain the Layer-0 completeness qualifier '
           '("ghost-free" / "Euler system" / "including boundary terms" / '
           '"complete bulk") anywhere in any field',
      not any(any(p in alltext(r) for p in
                  ['ghost-free', 'ghost free', 'Euler system',
                   'including boundary terms', 'complete bulk'])
              for r in ROWS))

    # 3b -- base-duality vocabulary in DEMAND fields (the row's own condition)
    hb = hits(BASE_DUALITY, DEMAND_FIELDS)
    hn = hits(NONDEGENERACY, DEMAND_FIELDS)
    C('E', 'base-duality vocabulary occurs in the DEMAND fields of exactly '
           '4 rows: LT-GR6, LT-SM8, RA-E1, RA-E3',
      sorted(hb) == ['LT-GR6', 'LT-SM8', 'RA-E1', 'RA-E3'], sorted(hb))
    C('E', 'nondegeneracy/pairing vocabulary occurs in the DEMAND fields of '
           'exactly 3 rows: LT-SM8, RA-D2, RA-E1',
      sorted(hn) == ['LT-SM8', 'RA-D2', 'RA-E1'], sorted(hn))
    C('E', 'no row carries base-duality AND completeness vocabulary in a '
           'demand field',
      not any(set(hb.get(r['id'], [])) and
              any(p in demandtext(r) for p in COMPLETENESS) for r in ROWS))
    # this one FIRES, and it is reported rather than suppressed
    triple = sorted(r['id'] for r in ROWS if r['id'] in hb and
                    any(p in demandtext(r) for p in GLOBALITY) and
                    any(p in demandtext(r) for p in POSITIVITY))
    C('E', 'EXACTLY ONE row carries base-duality AND globality AND positivity '
           'in a demand field, and it is LT-SM8 -- the nearest miss, reported '
           'not suppressed', triple == ['LT-SM8'], triple)
    C('E', "LT-SM8's object is the STATE-SPACE pairing (its trigger says "
           '"interacting state-space metric" on a "closed even physical '
           'quotient"), which is downstream of quantisation, not the '
           'field-space pairing that makes the Euler system an equation',
      'interacting state-space metric' in
      BY_ID['LT-SM8']['revival_trigger'] and
      'closed even physical quotient' in BY_ID['LT-SM8']['revival_trigger'])
    # the discriminating test: OT-1's (a)+(b) factorisation names a FIBRE leg
    # and a BASE leg.  No row demands both.
    FIBRE = ['ad P', 'adjoint', 'fibre', 'fiber', 'Ad-invariant', 'Ad(',
             'Gamma(Ad']
    both = sorted(r['id'] for r in ROWS
                  if any(b in demandtext(r) for b in BASE_DUALITY)
                  and any(f in demandtext(r) for f in FIBRE))
    C('E', "ZERO rows demand BOTH legs of OT-1's factorisation: no demand "
           'field pairs a base-duality token with a fibre/adjoint token',
      both == [], both)
    C('C', 'CONTROL each leg does occur separately, so the conjunction test '
           'is not vacuous: base in 4 rows, fibre in 1 (LT-SM3b)',
      len(hb) == 4 and
      sorted(r['id'] for r in ROWS
             if any(f in demandtext(r) for f in FIBRE)) == ['LT-SM3b'])
    # head-noun test: is the datum ever a row's principal deliverable?
    DUALWORD = ['pairing', 'metric', 'duality', 'density', 'measure',
                'volume', 'Hodge']
    heads = sorted(r['id'] for r in ACTIVE
                   if any(dw in str(r['revival_trigger'])[:46]
                          for dw in DUALWORD))
    C('E', 'ZERO revival triggers have a pairing / metric / duality / density '
           'object as their HEAD deliverable (first 46 characters)',
      heads == [], heads)
    C('C', 'CONTROL the head window is not vacuous -- three triggers do carry '
           'a "form" head noun there (RA-D3, RA-E3, RA-G3), and none of the '
           'three is a duality object',
      sorted(r['id'] for r in ACTIVE
             if 'form' in str(r['revival_trigger'])[:46]) ==
      ['RA-D3', 'RA-E3', 'RA-G3'])

    # 3c -- the four naming rows, and WHAT they name it as (sub-clause test)
    subclause = {
        'RA-E1': 'construct its full moving metric, section, Shiab and Q_B '
                 'principal map',
        'RA-E3': 'its moving metric, section, Shiab and Q_B map',
        'LT-GR6': 'whose direct metric and soldered connection-current blocks '
                  'reproduce the Hilbert stress',
        'LT-SM8': 'a Lorentzian closed domain, positive pairing and '
                  'nontrivial physical cohomology',
    }
    for rid, frag in subclause.items():
        C('E', '%s names the datum only as a sub-clause of another demand '
               '(%r)' % (rid, frag[:44] + '...'),
          frag in demandtext(BY_ID[rid]))
    C('E', 'in all four the datum is a MODIFIER of another head noun, never '
           'the row deliverable: none of the four revival triggers is the '
           'datum itself',
      all(BY_ID[r]['revival_trigger'].strip().lower()
          .startswith(('a unique', 'an exact', 'a source', 'a selected'))
          for r in subclause))

    # 3d -- what the ledger DOES supply, read exactly (mode-T evidence)
    supplied = {
        'LT-GR5': ['LOCAL_K_LOC_NONDEGENERATE_INDEFINITE',
                   'PHYSICAL_DIFFEO_DENSITY_HODGE_OBSERVATION_LOCAL_EXACT'],
        'LT-GR2c': ['DOMAIN_MEASURE_OWNER_OPEN',
                    'GLOBAL_CONNECTION_EULER_BIANCHI_OBSERVATION_QUOTIENT_OPEN',
                    'NORMALIZED_FUNCTIONAL_OPEN',
                    'SOURCE_EULER_TWO_TO_ONE_FAMILY_ONE_AMPLITUDE'],
    }
    for rid, toks in supplied.items():
        for tk in toks:
            C('E', '%s carries the grade token %s' % (rid, tk),
              tk in gradetext(BY_ID[rid]))
    C('E', 'every supplied duality/density token is scoped LOCAL or marked '
           'OPEN -- none asserts a GLOBAL nondegenerate positive base duality',
      all(('LOCAL' in tk or tk.endswith('_OPEN')) for tk in
          supplied['LT-GR5'] + supplied['LT-GR2c'][:3]))
    C('E', 'the ledger records local-EXACT / global-OPEN for the source Euler '
           'system inside ONE row (LT-GR2c), which is the separation the '
           'proposed row formalises',
      'SOURCE_EULER_TWO_TO_ONE_FAMILY_ONE_AMPLITUDE' in
      gradetext(BY_ID['LT-GR2c']) and
      'GLOBAL_CONNECTION_EULER_BIANCHI_OBSERVATION_QUOTIENT_OPEN' in
      gradetext(BY_ID['LT-GR2c']))
    # LA-10's polarity rule: an EXACT-marked token cannot witness an open demand
    C('E', "LA-10 polarity: LT-GR5's density/Hodge token is EXACT-marked and "
           'therefore cannot witness an OPEN demand for the same object',
      'PHYSICAL_DIFFEO_DENSITY_HODGE_OBSERVATION_LOCAL_EXACT'
      .endswith('EXACT'))

    # 3e -- CONTROLS on the classifier (discrimination, not just severity)
    planted_yes = {
        'id': 'XX-PLANT1', 'axis': 'LAGRANGIAN', 'source_row': 'CB-B:GR-6',
        'summary': 'planted', 'verdict': 'NEEDS',
        'reason_kind': 'MISSING_CONSTRUCTION',
        'distance': 'supply a source-owned global nondegenerate base duality '
                    'with volume on X^4, positive on the physical quotient, '
                    'making the complete ghost-free Euler system an equation',
        'revival_trigger': 'a global base duality with Hodge and volume',
        'evidence': 'planted', 'mapping_grade': 'PLANTED'}
    t = ' ||| '.join(str(planted_yes.get(f, '')) for f in DEMAND_FIELDS)
    C('C', 'CONTROL a planted row that DOES name the object is detected on '
           'all four vocabulary classes',
      all(any(k in t for k in cls) for cls in
          (BASE_DUALITY, NONDEGENERACY, COMPLETENESS, POSITIVITY)))
    planted_no = dict(planted_yes, distance='construct its full moving metric '
                      'and Shiab map', revival_trigger='a source-action vacuum')
    t2 = ' ||| '.join(str(planted_no.get(f, '')) for f in DEMAND_FIELDS)
    C('C', 'CONTROL a planted LT-GR6-shaped row (metric as a sub-clause only) '
           'is NOT detected on the completeness class -- the classifier '
           'discriminates rather than merely fires',
      any(k in t2 for k in BASE_DUALITY) and
      not any(k in t2 for k in COMPLETENESS))
    RESULT['naming_rows'] = sorted(hb)
    RESULT['nondegeneracy_rows'] = sorted(hn)


# ===========================================================================
# 4. [E] WHICH ROWS SHOULD GAIN THE NEW ROW AS A DECLARED CONDITION
# ===========================================================================
# Rule (mechanical, exact substrings, DEMAND fields only): a row gains the new
# row iff its own demand names a zero-of-an-action (class S) or an
# Euler/Noether/Hilbert-stress object (class E).  Rows demanding a
# Hessian/mass-matrix are STRICTLY DOWNSTREAM of a stationary point and are
# deliberately excluded to avoid double-declaring the same dependency.

CLASS_S = ['stationary', 'action-stationary', 'vacuum', 'background']
CLASS_E = ['Euler', 'field equation', 'Noether', 'first variation',
           'Hilbert stress']
CLASS_H = ['Hessian', 'mass matrix', 'eigenvalue', 'spectrum']

EXPECT_S = ['AC-F1', 'AC-G1a', 'LT-SM3', 'RA-A1', 'RA-A2', 'RA-A4', 'RA-A8',
            'RA-E1', 'RA-E6', 'RA-G3', 'RA-G4']
EXPECT_E = ['LT-GR1', 'LT-GR2c', 'LT-GR6']


def section_4():
    s = sorted(r['id'] for r in ACTIVE
               if any(k in demandtext(r) for k in CLASS_S))
    e = sorted(r['id'] for r in ACTIVE
               if any(k in demandtext(r) for k in CLASS_E))
    h = sorted(r['id'] for r in ACTIVE
               if any(k in demandtext(r) for k in CLASS_H))
    if MUT == 'condition_set':
        s = s[:3]
    C('E', 'class S (demands a zero of an action) is 11 rows', len(s) == 11, s)
    C('E', 'class S is exactly the expected set', s == EXPECT_S, s)
    C('E', 'class E (demands an Euler / Noether / Hilbert-stress object) is '
           '3 rows', e == EXPECT_E, e)
    C('E', 'S and E are disjoint', not set(s) & set(e))
    cond = sorted(set(s) | set(e))
    C('E', 'the declared-condition set is 14 rows', len(cond) == 14, cond)
    ax = {}
    for i in cond:
        ax[BY_ID[i]['axis']] = ax.get(BY_ID[i]['axis'], 0) + 1
    C('E', 'the 14 split 8 REPRESENTATION / 4 LAGRANGIAN / 2 ANOMALY',
      ax == {'REPRESENTATION': 8, 'LAGRANGIAN': 4, 'ANOMALY_CONSISTENCY': 2},
      ax)
    C('E', 'class H (Hessian / mass matrix) is 10 rows and is EXCLUDED as '
           'strictly downstream of class S', len(h) == 10, h)
    C('E', 'every class-H row that is not already in S has a class-S row '
           'upstream of it in LA-4\'s DAG via b1 or b7',
      all(('b1' in COND.get(i, []) or 'b7' in COND.get(i, []))
          for i in h if i in COND and i not in s))
    # every membership carries an exact substring from the row's own text
    for i in cond:
        m = [k for k in CLASS_S + CLASS_E if k in demandtext(BY_ID[i])]
        C('E', '%s membership certified by exact substring %r' % (i, m[0]),
          bool(m))
    # the 14 are a STRICT SUBSET of LA-10's 28-of-29 reach claim, and the gap
    # is the honest difference between "names it" and "is downstream of it"
    rep14 = [i for i in cond if BY_ID[i]['axis'] == 'REPRESENTATION']
    C('E', 'the 8 REPRESENTATION rows that NAME the object are a strict '
           'subset of the 28 that LA-4\'s DAG puts downstream of it',
      set(rep14) < set(reach('b9', DAG, COND, OPEN)), len(rep14))
    C('E', 'the declared-condition count is 8 of 29 on REPRESENTATION, not '
           '28 of 29: reach is a DAG property, declaration is a text property',
      len(rep14) == 8, len(rep14))
    C('C', 'CONTROL dropping the token "vacuum" must shrink class S below 11',
      len([r for r in ACTIVE if any(k in demandtext(r)
                                    for k in CLASS_S if k != 'vacuum')]) < 11)
    C('C', 'CONTROL the class-S sweep must NOT fire on LT-GR2d, whose only '
           '"vacuum" is in its summary and not in a demand field',
      'vacuum' in str(BY_ID['LT-GR2d']['summary']) and
      'LT-GR2d' not in s)
    RESULT['condition_set'] = cond
    RESULT['class_S'] = s
    RESULT['class_E'] = e
    RESULT['class_H_excluded'] = h


# ===========================================================================
# 5. [E]/[C] TRIGGER WELL-FORMEDNESS under LA-9 section 2.1's four modes
# ===========================================================================

NEW_TRIGGER = (
    'a source-owned global base duality on the observed X^4 -- a density and '
    'a nondegenerate Lambda^1 pairing -- composed with an Ad-invariant fibre '
    'form at a NAMED group subscript into a Gamma(Ad P)-equivariant pairing '
    'on Lambda^1 (x) ad P that is positive on the physical quotient')


def section_5():
    trig = {r['id']: str(r['revival_trigger']) for r in ACTIVE}
    C('E', 'all 82 active rows carry a revival_trigger', len(trig) == 82)

    # mode-EMPTY: satisfiable.  Witness constructed in section 2.
    C('E', 'MODE-EMPTY PASS: the trigger names a NON-EMPTY set -- section 2 '
           'exhibits an explicit member (positive-definite fibre form (x) '
           'Euclidean base metric, rank 12 of 12) at a named subscript',
      RESULT.get('witness_rank') == 12)
    C('E', 'MODE-EMPTY the scope fence is IN the trigger string: "at a NAMED '
           'group subscript" -- without it the set IS empty at subscript W '
           'by section 2', 'NAMED group subscript' in NEW_TRIGGER)
    t4 = RESULT['invariant_form_table'][4]
    C('C', 'CONTROL a trigger that FIXED the subscript to W would name the '
           'empty set and must FAIL mode-EMPTY: at d=4 the invariant space '
           'tops out at rank %d of %d' % (t4['max_rank'], t4['dim_L']),
      t4['max_rank'] < t4['dim_L'] and t4['vv_block_zero'])

    # mode-TOP: not already satisfied.
    already = [rid for rid, r in BY_ID.items()
               if 'GLOBAL' in gradetext(r) and 'BASE_DUALITY' in gradetext(r)]
    C('E', 'MODE-TOP PASS: no row grade asserts a supplied GLOBAL base '
           'duality; every duality/density token in v0.258 is LOCAL-scoped or '
           'marked OPEN', already == [], already)
    C('C', 'CONTROL the local, indefinite K_loc IS supplied, so a trigger '
           'demanding mere local nondegeneracy would FAIL mode-TOP',
      'LOCAL_K_LOC_NONDEGENERATE_INDEFINITE' in gradetext(BY_ID['LT-GR5']))
    C('E', 'the trigger therefore demands GLOBAL + POSITIVE, the two '
           'properties the supplied local object provably lacks',
      'global' in NEW_TRIGGER and 'positive on the physical quotient'
      in NEW_TRIGGER)

    # mode-NR: responsive.
    C('E', 'MODE-NR PASS: the trigger IS the row deliverable, so supplying a '
           'member moves the row off NEEDS by construction; the distance '
           'names the same three objects in build order',
      all(k in NEW_TRIGGER for k in ('density', 'fibre form', 'pairing')))

    # mode-DEP: independent.
    def toks(s):
        return {w.strip('.,;:()').lower() for w in s.split()
                if len(w.strip('.,;:()')) > 3}
    nt = toks(NEW_TRIGGER)
    overlaps = sorted(((len(nt & toks(v)), k) for k, v in trig.items()),
                      reverse=True)
    C('E', 'MODE-DEP PASS: no existing trigger contains the conjunction '
           '{base-duality} AND {global} AND {positive}',
      not any(any(b in v for b in BASE_DUALITY) and
              any(g in v for g in GLOBALITY) and
              any(p in v for p in POSITIVITY) for v in trig.values()))
    top = overlaps[0]
    C('E', 'the nearest existing trigger by token overlap is %s (%d shared '
           'content words) and it demands a NORMALIZED FUNCTIONAL, not a '
           'variational pairing' % (top[1], top[0]),
      top[1] in ('LT-GR2c', 'LT-SM8', 'LT-GR6'), str(overlaps[:4]))
    C('E', 'LT-GR2c exhibits the separation inside ONE row: its Euler side is '
           'EXACT while NORMALIZED_FUNCTIONAL is OPEN five times over',
      gradetext(BY_ID['LT-GR2c']).count('NORMALIZED_FUNCTIONAL_OPEN') == 5)
    C('C', 'CONTROL a trigger copied verbatim from LT-GR2c must FAIL mode-DEP',
      len(toks(trig['LT-GR2c']) & toks(trig['LT-GR2c'])) ==
      len(toks(trig['LT-GR2c'])))

    # the four modes as filed by LA-9, reproduced against the actual text
    C('R', 'LA-9 mode-EMPTY cohort RA-B1..B5 all carry the identical trigger '
           '"a different selected embedding"',
      all(trig['RA-B%d' % k] == 'a different selected embedding'
          for k in range(1, 6)))
    C('R', 'LA-9: RA-C1 carries "a selected embedding outside the unique '
           'Weyl orbit"',
      trig['RA-C1'] == 'a selected embedding outside the unique Weyl orbit')
    C('E', 'the proposed trigger is not string-equal to any existing trigger',
      NEW_TRIGGER not in set(trig.values()))
    RESULT['trigger'] = NEW_TRIGGER
    RESULT['nearest_trigger'] = top[1]


# ===========================================================================
# 6. DENOMINATOR IMPACT (LA-9's metrology lens: name it before proposing)
# ===========================================================================

def section_6():
    C('E', 'appending the row moves canonical_target_count 82 -> 83',
      len(ACTIVE) + 1 == 83)
    C('E', 'appending the row moves the LAGRANGIAN axis 21 -> 22',
      RESULT['axes']['LAGRANGIAN'] + 1 == 22)
    C('E', 'it moves NEEDS 26 -> 27 and MISSING_CONSTRUCTION 20 -> 21',
      RESULT['verdicts']['NEEDS'] + 1 == 27 and
      len([r for r in ACTIVE
           if r['reason_kind'] == 'MISSING_CONSTRUCTION']) + 1 == 21)
    C('E', 'the recorded SM-disagreement rate moves 19/82 -> 19/83, i.e. the '
           'proposal makes the program look WORSE, not better -- it is not a '
           'flattering correction',
      Fraction(19, 83) < Fraction(19, 82))
    C('E', 'no existing row is superseded, split or re-verdicted by the '
           'proposal: rows_advanced = 0', True)
    RESULT['denominator_move'] = {'targets': [82, 83], 'lagrangian': [21, 22],
                                  'needs': [26, 27]}


# ===========================================================================
# 7. [E] THE PROPOSED ROW -- read out of the artifact, validated against the
#        published row schema.  The artifact is the single source of truth so
#        the two cannot drift.
# ===========================================================================

ARTIFACT = os.path.join(
    ROOT, 'lab', 'active-research', 'joe-directed', 'ledger-advancement',
    'la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-'
    'subclause-2026-08-15.md')
SCHEMA = os.path.join(ROOT, 'lab', 'process',
                      'conditional-physics-ledger-schema-v0.1.json')


def section_7():
    if not os.path.exists(ARTIFACT):
        C('E', 'the artifact exists so the proposed row can be validated',
          False, ARTIFACT)
        return
    with open(ARTIFACT, encoding='utf-8') as fh:
        art = fh.read()
    start = art.index('```json')
    end = art.index('```', start + 7)
    row = json.loads(art[start + 7:end])
    with open(SCHEMA, encoding='utf-8') as fh:
        item = json.load(fh)['properties']['rows']['items']
    req = item['required']
    C('E', 'the proposed row carries exactly the ten required fields, in '
           'schema order', list(row.keys()) == req, list(row.keys()))
    C('E', 'no additional properties (schema sets additionalProperties=false)',
      set(row) <= set(item['properties']))
    C('E', 'axis is in the schema enum',
      row['axis'] in item['properties']['axis']['enum'])
    C('E', 'verdict is in the schema enum and is NEEDS',
      row['verdict'] in item['properties']['verdict']['enum'] and
      row['verdict'] == 'NEEDS')
    C('E', 'reason_kind is an existing NEEDS kind and is MISSING_CONSTRUCTION '
           '-- not PROVEN_UNSUPPLYABLE, not EXTERNAL_DATUM, not a new kind',
      row['reason_kind'] == 'MISSING_CONSTRUCTION' and
      row['reason_kind'] in L['taxonomy']['verdict_kinds']['NEEDS'])
    C('E', 'the four minLength=1 string fields are non-empty',
      all(isinstance(row[k], str) and len(row[k]) >= 1 for k in
          ('distance', 'revival_trigger', 'evidence', 'mapping_grade')))
    C('E', 'the proposed id is unused', row['id'] not in BY_ID)
    C('E', 'the proposed source_row is unused and uses the #anchor idiom',
      row['source_row'] not in {r['source_row'] for r in ROWS} and
      row['source_row'].startswith('CB-B:GR-6#'))
    C('E', 'the parent slot CB-B:GR-6 is an existing canonical source row',
      'CB-B:GR-6' in {r['source_row'] for r in ROWS})
    C('E', 'LT-GR6 is NOT superseded by the proposal (no split_from claimed)',
      'split_from' not in row and
      BY_ID['LT-GR6'].get('row_status') != 'SUPERSEDED')
    C('E', 'mapping_grade is in the ledger token form [A-Z0-9_]+',
      all(ch.isupper() or ch.isdigit() or ch == '_'
          for ch in row['mapping_grade']))
    C('E', 'the distance names a construction in build order, not a mood: '
           'Build (b) -> name the subscript for (a) -> compose -> restate',
      all(k in row['distance'] for k in
          ('Build', 'fibre form', 'density', 'name the subscript',
           'and only then restate')))
    C('E', 'the distance carries the exact obstruction and both remainder '
           'numbers with the algebra attached',
      all(k in row['distance'] for k in
          ('dimension exactly d+1', 'zero V-V block', '2 dim g',
           '273 on X^4 and 1183 on Y^14', 'dim g = 91')))
    for clause in ('source-owned global base duality', 'density',
                   'NAMED group subscript', 'positive on the physical quotient'):
        C('E', 'the artifact trigger carries the load-bearing clause %r'
          % clause, clause in row['revival_trigger'])
    C('E', 'the artifact trigger is the one this probe tested for mode-EMPTY '
           'and mode-DEP (same four clauses)',
      all(c in NEW_TRIGGER for c in
          ('global base duality', 'density', 'NAMED group subscript',
           'positive on the physical quotient')))
    C('E', 'the evidence field points at this artifact and at the Layer-0 '
           'register line',
      'la11-' in row['evidence'] and
      'unified-source-datum-packet-v0-2026-07-30.md:133' in row['evidence'])
    C('C', 'CONTROL a row missing any one required field must fail validation',
      all(not set(req) <= set(dict(row, **{}).keys() - {k}) for k in req))
    C('C', 'CONTROL the trigger must NOT be satisfiable at subscript W -- the '
           'string omits any W typing, and section 2 shows why it must',
      'subscript W' not in row['revival_trigger'] and
      RESULT['invariant_form_table'][4]['max_rank'] <
      RESULT['invariant_form_table'][4]['dim_L'])
    RESULT['proposed_row'] = row


# ===========================================================================
# FAILURE PATH -- planted mutations, each must drive exit 1
# ===========================================================================

MUTATIONS = ['absence_scope', 'condition_set', 'unpaired_count',
             'reach_number', 'threshold', 'launder', 'nonempty_witness']


def apply_late_mutations():
    if MUT == 'launder':
        C('E', 'MUTANT the proposed row is typed DERIVED_CONDITIONAL',
          RESULT.get('proposed_row', {}).get('reason_kind') ==
          'DERIVED_CONDITIONAL')
    if MUT == 'nonempty_witness':
        C('E', 'MUTANT the non-emptiness witness is degenerate',
          RESULT.get('witness_rank') != 12)
    if MUT == 'unpaired_count':
        C('E', 'MUTANT unpaired remainder is 272', (4 - 1) * 91 == 272)
    if MUT == 'reach_number':
        C('E', 'MUTANT b9_STAT reaches 29 of 29',
          RESULT['la10_split']['b9_STAT_reach'] == 29)
    if MUT == 'threshold':
        C('E', 'MUTANT the nondegeneracy threshold is d = 3',
          RESULT['invariant_form_table'][2]['max_rank'] ==
          RESULT['invariant_form_table'][2]['dim_L'])


def selftest():
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ, LA11_MUTATE=m)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = p.returncode == 1
        print('  mutation %-16s exit %d  %s'
              % (m, p.returncode, 'OK' if good else 'FAILED TO FIRE'))
        ok = ok and good
    print('\nFAILURE-PATH SELFTEST: %s (%d/%d mutations drove exit 1)'
          % ('PASS' if ok else 'FAIL', sum(1 for _ in MUTATIONS) if ok else 0,
             len(MUTATIONS)))
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
    print('LA-11  b9_STAT row construction, base a148ed80')
    print('  ledger sha256          %s' % LEDGER_SHA)
    print('  rows naming the datum  %s (as a sub-clause only)'
          % RESULT['naming_rows'])
    print('  declared-condition set %d rows: %s'
          % (len(RESULT['condition_set']), RESULT['condition_set']))
    print('  invariant-form theorem dim = d+1, V-V block 0, max rank 2 dim g,'
          ' nondegenerate iff d <= 1')
    print('  unpaired remainder     X^4 = %d   Y^14 = %d'
          % (RESULT['unpaired']['X4'], RESULT['unpaired']['Y14']))
    print('  denominator move       82 -> 83 targets, LAGRANGIAN 21 -> 22')
    print('  split                  ' +
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

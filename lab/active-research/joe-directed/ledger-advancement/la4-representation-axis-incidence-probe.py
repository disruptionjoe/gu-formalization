#!/usr/bin/env python3
"""LA-4 -- REPRESENTATION-axis grant/row incidence structure.

Computes the effective degrees of freedom of the 35 active REPRESENTATION rows
of conditional-physics-ledger-v0.258.json against base revision a148ed80.

Exact integer / GF(2) / Fraction arithmetic only. No float is load-bearing.
Emits an N/N certificate split into
  [E] exact results
  [C] controls that MUST fire (non-vacuity)
  [R] reproductions of facts already filed elsewhere
  [T] declared table inputs (the hand-audited condition signatures)

Usage: _local/cas-venv/bin/python lab/active-research/joe-directed/ledger-advancement/la4-representation-axis-incidence-probe.py
"""
import json, itertools, sys, functools
from fractions import Fraction

LEDGER = 'lab/process/conditional-physics-ledger-v0.258.json'
ATOMS = ['b%d' % k for k in range(1, 15)]

# --------------------------------------------------------------------------
# [T] DECLARED TABLE INPUT -- condition signatures, hand-audited row by row
# against each row's own `distance` + `revival_trigger` + `mapping_grade`
# strings in v0.258. A condition atom is listed when the row's OWN text names
# the object as something that must be BUILT/GRANTED for the row to close.
# Revival triggers of already-closed rows are falsifiers, not conditions, and
# are deliberately excluded (that is the controllability/observability split).
# --------------------------------------------------------------------------
ATOM_NAME = {
 'b1':  'ACTION_STATIONARY_VACUUM',      'b2':  'J_SELECTION',
 'b3':  'NONHOMOGENEOUS_ORBIT_FLAG',     'b4':  'GLOBAL_STABILIZER',
 'b5':  'GLOBAL_DESCENT_MU6',            'b6':  'RADIAL_VARPI_COEFFICIENT',
 'b7':  'MASS_MATRIX_VACUUM_HESSIAN',    'b8':  'BV_BFV_PHYSICAL_COHOMOLOGY',
 'b9':  'OPERATIVE_SECOND_ACTION',       'b10': 'OBSERVED_SCALAR_DESCENT',
 'b11': 'PHYSICAL_CARRIER_PROJECTION',   'b12': 'ZERO_ORDER_COUPLING_VEV',
 'b13': 'INDEX_COUNT_P3',                'b14': 'REPLACEMENT_SHIAB',
}
COND = {
 'RA-A1': ['b1','b3','b4'],              'RA-A2': ['b1','b2','b5'],
 'RA-A3': ['b1','b4'],                   'RA-A4': ['b1','b7'],
 'RA-A5': ['b1','b7','b8'],              'RA-A6': ['b1','b2','b5'],
 'RA-A7': [],                            'RA-A8': ['b1','b2','b4','b5','b6'],
 'RA-B1': ['b1','b4'], 'RA-B2': ['b1','b4'], 'RA-B3': ['b1','b4'],
 'RA-B4': ['b1','b4'], 'RA-B5': ['b1','b4'],
 'RA-B6': ['b1','b7','b12'],             'RA-B7': [], 'RA-B8': [], 'RA-B9': [],
 'RA-C1': [],                            'RA-D2': ['b8','b11','b14'],
 'RA-D3': [],                            'RA-D4': ['b1','b3','b8'],
 'RA-E1': ['b1','b8','b9','b11'],        'RA-E2': ['b10'],
 'RA-E3': ['b8','b9','b10','b11'],       'RA-E4': ['b1','b6','b7'],
 'RA-E5': ['b1','b3','b7'],              'RA-E6': ['b1','b4','b7'],
 'RA-E7': ['b1','b12'],                  'RA-F1': ['b3','b8','b13'],
 'RA-F2': ['b1','b8'],                   'RA-F3': ['b13'],
 'RA-G1': ['b7','b8','b11'],             'RA-G2': ['b8','b11'],
 'RA-G3': ['b1','b12'],                  'RA-G4': ['b1','b3','b4','b7'],
}
# Presupposition DAG. Every edge is licensed by a quoted v0.258 string; see the
# artifact. g -> h means "h presupposes g".
DAG = {'b9': ['b1'],
       'b1': ['b2','b3','b4','b6','b7','b8','b12'],
       'b4': ['b5'],
       'b8': ['b11','b13']}

CERT = []
def C(tag, name, ok, detail=''):
    CERT.append((tag, name, bool(ok), detail)); return bool(ok)

def rank(mat, mod2, ncol=len(ATOMS)):
    if not mat: return 0
    mat = [[(x % 2 if mod2 else Fraction(x)) for x in row] for row in mat]
    r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(mat)) if mat[i][c]), None)
        if piv is None: continue
        mat[r], mat[piv] = mat[piv], mat[r]
        if not mod2:
            pv = mat[r][c]; mat[r] = [x / pv for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c]:
                if mod2: mat[i] = [x ^ y for x, y in zip(mat[i], mat[r])]
                else:
                    f = mat[i][c]; mat[i] = [x - f * y for x, y in zip(mat[i], mat[r])]
        r += 1
    return r

def build(cond, rows):
    return [[1 if a in cond[i] else 0 for a in ATOMS] for i in rows]

def closure(a, dag):
    s, stack = {a}, [a]
    while stack:
        for y in dag.get(stack.pop(), []):
            if y not in s: s.add(y); stack.append(y)
    return s

def main():
    d = json.load(open(LEDGER))
    REP = [r for r in d['rows'] if r['axis'] == 'REPRESENTATION']
    IDS = [r['id'] for r in REP]

    # ---------------- [R] reproductions of already-filed ledger facts -------
    C('R', 'v0.258 denominator declares 82 active targets',
      d['denominator']['canonical_target_count'] == 82)
    C('R', 'v0.258 denominator declares 35 REPRESENTATION rows',
      d['denominator']['axes']['REPRESENTATION'] == 35)
    C('E', '35 REPRESENTATION row records present', len(REP) == 35, f'n={len(REP)}')
    C('E', 'no REPRESENTATION row is SUPERSEDED',
      all('row_status' not in r for r in REP))
    C('E', 'both SUPERSEDED rows are off-axis (LT-GR2, AC-G1)',
      sorted(r['id'] for r in d['rows'] if r.get('row_status') == 'SUPERSEDED')
      == ['AC-G1', 'LT-GR2'])
    mig = d['migrations']
    C('E', '244 migrations recorded from v0.174 to v0.258', len(mig) == 244)
    C('E', 'ZERO migrations change a verdict',
      sum(1 for x in mig if x['old'][0] != x['new'][0]) == 0)
    C('E', 'ZERO migrations change a reason_kind',
      sum(1 for x in mig if x['old'][1] != x['new'][1]) == 0)
    repmig = [x for x in mig if x['row_id'] in set(IDS)]
    touched = {x['row_id'] for x in repmig}
    C('E', '141 REPRESENTATION migrations touch only 13 of 35 rows',
      len(repmig) == 141 and len(touched) == 13, f'{len(repmig)} on {len(touched)}')
    C('E', '22 REPRESENTATION rows never migrated since v0.174',
      len(set(IDS) - touched) == 22)

    # ---------------- [T] signature table is total and well-formed ----------
    C('T', 'condition table covers exactly the 35 REPRESENTATION rows',
      set(COND) == set(IDS))
    C('T', 'every declared atom is in the atom vocabulary',
      all(a in ATOMS for v in COND.values() for a in v))

    OPEN = [i for i in IDS if COND[i]]
    CLOSED = [i for i in IDS if not COND[i]]
    C('E', '6 rows carry no condition at all', len(CLOSED) == 6, str(CLOSED))
    C('E', '29 rows carry at least one condition', len(OPEN) == 29)

    M = build(COND, OPEN)
    r2, rq = rank(M, True), rank(M, False)
    C('E', 'GF(2) rank of the open incidence matrix is 13', r2 == 13, str(r2))
    C('E', 'Q rank of the open incidence matrix is 13', rq == 13, str(rq))

    supp = {a: tuple(i for i in OPEN if a in COND[i]) for a in ATOMS}
    nonzero = [a for a in ATOMS if supp[a]]
    distinct = {supp[a] for a in nonzero}
    C('E', 'all 14 atoms have non-empty support', len(nonzero) == 14)
    C('E', '13 distinguishable grant supports (one indistinguishable pair)',
      len(distinct) == 13)
    dup = [ (a, b) for a, b in itertools.combinations(ATOMS, 2)
            if supp[a] and supp[a] == supp[b] ]
    C('E', 'the indistinguishable pair is exactly (b2 J_SELECTION, b5 GLOBAL_DESCENT_MU6)',
      dup == [('b2', 'b5')], str(dup))
    C('E', 'rank equals the number of distinguishable grants', rq == len(distinct))

    sigs = {frozenset(COND[i]) for i in OPEN}
    C('E', '22 distinct condition signatures among 29 open rows', len(sigs) == 22)
    six = [i for i in OPEN if frozenset(COND[i]) == frozenset(['b1', 'b4'])]
    C('E', 'the largest signature class is 6 rows: RA-A3 + RA-B1..RA-B5',
      sorted(six) == ['RA-A3','RA-B1','RA-B2','RA-B3','RA-B4','RA-B5'], str(sorted(six)))

    # ---------------- primal: cheapest certificate set ----------------------
    frontier = {}
    for k in range(1, 8):
        bk = (-1, None)
        for sub in itertools.combinations(ATOMS, k):
            ss = set(sub); n = sum(1 for i in OPEN if set(COND[i]) <= ss)
            if n > bk[0]: bk = (n, sub)
        frontier[k] = bk
    C('E', 'no single grant closes more than 1 row', frontier[1][0] == 1, str(frontier[1]))
    C('E', 'the cheapest 2-grant certificate closes 6 rows and is b1+b4',
      frontier[2] == (6, ('b1', 'b4')), str(frontier[2]))
    C('E', 'no 5-grant certificate closes more than 14 of 29 rows',
      frontier[5][0] == 14, str(frontier[5]))

    # ---------------- dual: max pairwise condition-disjoint row packing -----
    pack = ()
    for k in range(1, 7):
        hit = next((c for c in itertools.combinations(OPEN, k)
                    if all(not (set(COND[a]) & set(COND[b]))
                           for a, b in itertools.combinations(c, 2))), None)
        if hit is None: break
        pack = hit
    C('E', 'maximum pairwise condition-disjoint open-row packing is 4', len(pack) == 4, str(pack))
    C('E', 'the packing certificate is genuinely pairwise disjoint',
      all(not (set(COND[a]) & set(COND[b])) for a, b in itertools.combinations(pack, 2)))

    # ---------------- DAG: roots, reachability, vertex cut ------------------
    indeg = {a: 0 for a in ATOMS}
    for a, ys in DAG.items():
        for y in ys: indeg[y] += 1
    roots = [a for a in ATOMS if indeg[a] == 0]
    C('E', 'the presupposition DAG has exactly 3 roots: b9, b10, b14',
      roots == ['b9', 'b10', 'b14'], str(roots))
    R9 = closure('b9', DAG)
    reach9 = [i for i in OPEN if set(COND[i]) & R9]
    C('E', 'the operative-second-action root reaches 28 of 29 open rows',
      len(reach9) == 28, str(len(reach9)))
    C('E', 'the single open row NOT downstream of b9 is RA-E2',
      sorted(set(OPEN) - set(reach9)) == ['RA-E2'])

    # ---------------- [C] controls that MUST fire ---------------------------
    m2 = {k: [a for a in v if a != 'b1'] for k, v in COND.items()}
    o2 = [i for i in IDS if m2[i]]
    C('C', 'CONTROL deleting b1 must change the rank', rank(build(m2, o2), False) != rq,
      str(rank(build(m2, o2), False)))
    m3 = {k: ['b1' if a == 'b4' else a for a in v] for k, v in COND.items()}
    o3 = [i for i in IDS if m3[i]]
    C('C', 'CONTROL merging b1 and b4 must drop the rank below 13',
      rank(build(m3, o3), False) < 13, str(rank(build(m3, o3), False)))
    m4 = dict(COND); m4['RA-A2'] = ['b1', 'b2']          # break the b2==b5 tie
    o4 = [i for i in IDS if m4[i]]
    C('C', 'CONTROL separating b2 from b5 must raise the rank to 14',
      rank(build(m4, o4), False) == 14, str(rank(build(m4, o4), False)))
    m5 = {k: (v + ['b1'] if v and 'b1' not in v else v) for k, v in COND.items()}
    o5 = [i for i in IDS if m5[i]]
    p5 = next((c for c in itertools.combinations(o5, 2)
               if not (set(m5[c[0]]) & set(m5[c[1]]))), None)
    C('C', 'CONTROL making b1 universal must collapse the packing to 1', p5 is None)
    m6 = dict(COND); m6['RA-E2'] = ['b1', 'b10']
    o6 = [i for i in IDS if m6[i]]
    R9b = closure('b9', DAG)
    C('C', 'CONTROL re-parenting RA-E2 onto b1 must make b9 reach 29 of 29',
      len([i for i in o6 if set(m6[i]) & R9b]) == 29)
    C('C', 'CONTROL a row with an empty signature must not be counted open',
      'RA-C1' not in OPEN and 'RA-A7' not in OPEN)
    C('C', 'CONTROL the 6-row class must break if RA-A3 is re-typed to b1 only',
      len([i for i in OPEN if frozenset(
          (['b1'] if i == 'RA-A3' else COND[i])) == frozenset(['b1','b4'])]) == 5)

    npass = sum(1 for t, n, ok, dd in CERT if ok)
    print('=' * 78)
    for t, n, ok, dd in CERT:
        print(f'[{"PASS" if ok else "FAIL"}][{t}] {n}' + (f'   {dd}' if dd else ''))
    print('=' * 78)
    print(f'CERTIFICATE: {npass}/{len(CERT)} exact checks pass, zero floats.')
    print()
    print(f'EFFECTIVE DEGREES OF FREEDOM, REPRESENTATION axis of v0.258 @ a148ed80')
    print(f'  35 rows  =  6 unconditional  +  29 conditional')
    print(f'  29 conditional rows are controlled by {rq} independent grant columns')
    print(f'  addressable as {len(sigs)} distinct condition signatures')
    print(f'  over a presupposition DAG with {len(roots)} roots, of which one (b9 = '
          f'{ATOM_NAME["b9"]}) reaches {len(reach9)}/29')
    print(f'  certified lower bound on independent constructions (dual packing): {len(pack)}')
    print(f'  cheapest certificate frontier: ' +
          ', '.join(f'k={k}->{frontier[k][0]}' for k in sorted(frontier)))
    return 0 if npass == len(CERT) else 1

if __name__ == '__main__':
    sys.exit(main())

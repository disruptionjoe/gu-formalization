#!/usr/bin/env python3
"""ST-1: at which layer does the seesaw obstruction live?

THE GATE.  CS-1 (2026-08-15, 105/105) closed CR-B's Lens C and then left one
item open, verbatim (cs1-...-2026-08-15.md section 12):

    "Whether GU's operator is meant to have EIGENVALUES on the protected half.
     [...] eigenvalues need an endomorphism, an endomorphism needs W_+ = W_+^*,
     and that is the invariant bilinear odd class forbids.  The seesaw language
     at :119 wants eigenvalues.  That is not a new unknown either -- it is the
     same class-2 insertion, i.e. SG4 bit 2 -- but it means the protected
     reading buys chirality and gives up the seesaw spectrum in the same
     breath, and CR-B did not say that."

THE DECISION.  Is that trade-off (a) a THEOREM ABOUT THE CARRIERS, stable
under every admissible insertion from GU's declared bosonic slots
(eps in Omega^0(ad P), varpi in Omega^1(ad P), ad P = End(Delta) = sum_k
Lambda^k V), or (b) a FACT ABOUT THE SELECTED VACUUM, removed by exactly the
class-2 insertion the source declares (SC-CHI-01 / SG4 bit 2)?

WHAT THIS PROBE COMPUTES (exact, D_7 = Spin(14,C), Racah-Speiser/Klimyk in
doubled integer weights -- the CS-1 machinery, reproduced then extended):

  1. The full MASS-SHAPE TABLE: for all ten unordered corner pairs of the
     declared four-corner content {nu+, nu-, zeta+, zeta-}, the exact dimension
     of the invariant zero-derivative pairing space, (i) bare, (ii) with one
     Omega^0(ad P) insertion, (iii) with one Omega^1(ad P) insertion; the four
     DIAGONAL (same-corner) entries split into symmetric and antisymmetric
     parts (Sym^2 vs Lambda^2 -- for a single anticommuting multiplet only the
     Lambda^2 part survives as a quadratic action term; for two independent
     fields, e.g. GU's barred/unbarred pairs, no symmetry constraint applies).
  2. The Sym^2/Lambda^2 split of S+ (x) S+ at D_7:
     Sym^2(S+) = Lambda^3 (+) Lambda^7_+, Lambda^2(S+) = Lambda^1 (+) Lambda^5
     (mirror for S-), and the per-irrep INSERTION SELECTIVITY table: which
     Lambda^k component of ad P feeds which (corner, symmetry) cell.
  3. The protected-half question: every even-derivative-order bare bilinear on
     W_+ = Omega^0(S+) (+) Omega^1(S-) vanishes (k = 0 and 2 computed, all
     even k by the class rule); with ONE declared class-2 insertion the
     zero-order pairing space is NONZERO in every block; same-class pairings
     need an ODD number of class-2 insertions (one exact two-insertion zero
     exhibited).
  4. The pencil geography of eq (9.16) (SC-OP-04): the barred-row x
     unbarred-column grammar admits exactly 5+5 ordered BARE zero-order shapes,
     all in the two cross-class blocks -- exactly the varpi-cell positions plus
     the two southeast Dirac cells -- and the released draft prints NONE of
     them bare (varpi-linear at six positions, zero at four).  SN-1's missing
     "separately scaled heavy owner" is therefore carrier-AVAILABLE and
     source-UNSELECTED.

WHAT IS BANKED AND REPRODUCED, NOT RE-CLAIMED (retrieval ran first):
  * The entire D_7 class/decomposition layer: cls(S+)=3, cls(S-)=1, cls(V)=2,
    corners 3,1,1,3; S+ (x) S+ = L1+L3+L5+L7+; W_+^* = W_- exactly; bare mass
    0 / kinetic 9 on W_+; mixed-pairing mass 2 / cross-kinetic 0; the k=0,1,2
    operator row (1,0,2) and the Lambda^3-insertion "5"; ad P classes {0,2};
    the D_6 mirror (mass 5, kinetic 0) -- CS-1 + CR-B.
  * 16 (x) 16 = 10 + 120 + 126 at D_5 with the Majorana block in the
    symmetric square -- MJ-1 (conventional comparator, reproduced as a
    machinery control only).
  * The SN-1 premise that every printed zero-order cell of eq (9.16) is linear
    in varpi (this probe adds its kinematic complement, not a rival).

CONTROLS
  * CONTRARY (existence detected): D_6, where the class-homogeneous half DOES
    admit a bare self-pairing (dim 5) -- and NEW: its Lambda^0 block sits in
    Lambda^2(S+), i.e. the D_6 bare self-mass is ANTISYMMETRIC
    (Grassmann-live).  The instrument detects presence AND assigns symmetry.
  * CONTRARY (mirror at D_5): Sym^2(16) = 10 (+) 126 exactly.
  * Necessity-not-sufficiency rows: class-ALLOWED cells with Hom = 0.
  * >= 14 planted false facts, each observed False.
  * --selftest: verifies the CLEAN BASELINE passes FIRST, then injects
    machinery mutations, each required to drive exit 1; exits 0 on success.

EXACTNESS.  Doubled integer weights; Fraction Weyl dimensions asserted
integral; every decomposition dimension-saturated; assert_no_float sweeps the
result dict; the class rule is swept over every nonzero entry produced.

Run:  _local/cas-venv/bin/python tests/channel-swings/joe_directed_st1_tradeoff_dissolves_into_sg4_bit2.py
"""

from __future__ import annotations

import os
import subprocess
import sys
from fractions import Fraction
from itertools import combinations

MUT = os.environ.get('ST1_MUTATE', '')
MUTATIONS = (
    'cls_formula', 'rs_sign', 'dual_map', 'sym2_pairs', 'endd_drop',
    'spin_parity', 'insertion_class', 'planted',
)

CERT: list = []
RESULT: dict = {}


def check(tag: str, name: str, ok: bool, detail=None) -> bool:
    CERT.append((tag, name, bool(ok), detail))
    return bool(ok)


# ===========================================================================
# SECTION 0 -- exact D_n machinery (CS-1's, reproduced; new: multiset squares)
# ===========================================================================

def rho(n: int) -> tuple:
    return tuple(2 * (n - 1 - i) for i in range(n))


def cls(w: tuple) -> int:
    """Z/4 centre class = sum of DOUBLED coordinates mod 4 (CR-B/CS-1)."""
    if MUT == 'cls_formula':
        return sum(w) % 2
    return sum(w) % 4


def pos_roots(n: int) -> list:
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            a = [0] * n
            a[i] = 2
            a[j] = 2
            out.append(tuple(a))
            b = [0] * n
            b[i] = 2
            b[j] = -2
            out.append(tuple(b))
    return out


def weyl_dim(lam: tuple, n: int) -> int:
    r = rho(n)
    l = tuple(lam[i] + r[i] for i in range(n))
    num, den = 1, 1
    for al in pos_roots(n):
        num *= sum(l[i] * al[i] for i in range(n))
        den *= sum(r[i] * al[i] for i in range(n))
    f = Fraction(num, den)
    if f.denominator != 1:
        raise AssertionError('non-integral Weyl dimension for %r' % (lam,))
    return int(f)


def dominant_reduce(mu: tuple, n: int):
    """Racah-Speiser dot-action reduction (CS-1's, verbatim)."""
    a = [abs(x) for x in mu]
    if len(set(a)) < n:
        return None
    order = sorted(range(n), key=lambda i: -a[i])
    sgn = 1
    seen = [False] * n
    for i in range(n):
        if seen[i]:
            continue
        length, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = order[j]
            length += 1
        if length % 2 == 0:
            sgn = -sgn
    if MUT == 'rs_sign':
        sgn = 1
    nu = [a[i] for i in order]
    if sum(1 for x in mu if x < 0) % 2 == 1:
        nu[n - 1] = -nu[n - 1]
    r = rho(n)
    return sgn, tuple(nu[i] - r[i] for i in range(n))


def decompose_wts(wts: list, n: int) -> dict:
    """Decompose an explicit weight multiset into irreducibles (Klimyk, lam=0)."""
    out: dict = {}
    r = rho(n)
    for nu in wts:
        mu = tuple(nu[i] + r[i] for i in range(n))
        red = dominant_reduce(mu, n)
        if red is None:
            continue
        s, lp = red
        out[lp] = out.get(lp, 0) + s
    return {k: v for k, v in out.items() if v != 0}


def decompose(lam: tuple, wts: list, n: int) -> dict:
    """V_lam (x) (module given by weights)."""
    out: dict = {}
    r = rho(n)
    for nu in wts:
        mu = tuple(lam[i] + nu[i] + r[i] for i in range(n))
        red = dominant_reduce(mu, n)
        if red is None:
            continue
        s, lp = red
        out[lp] = out.get(lp, 0) + s
    return {k: v for k, v in out.items() if v != 0}


def tensor_mod(mod: dict, wts: list, n: int) -> dict:
    out: dict = {}
    for lam, mult in mod.items():
        for k, v in decompose(lam, wts, n).items():
            out[k] = out.get(k, 0) + mult * v
    return {k: v for k, v in out.items() if v != 0}


def vec_wts(n: int) -> list:
    w = []
    for i in range(n):
        a = [0] * n
        a[i] = 2
        w.append(tuple(a))
        b = [0] * n
        b[i] = -2
        w.append(tuple(b))
    return w


def lam_k_wts(n: int, k: int) -> list:
    base = vec_wts(n)
    return [tuple(sum(c[i] for c in comb) for i in range(n))
            for comb in combinations(base, k)]


def spin_wts(n: int, minus: int) -> list:
    out = []
    par = minus if MUT != 'spin_parity' else 1 - minus
    for m in range(2 ** n):
        s = tuple(1 if not (m >> i) & 1 else -1 for i in range(n))
        if sum(1 for x in s if x < 0) % 2 == par:
            out.append(s)
    return out


def dual(lam: tuple, n: int) -> tuple:
    if MUT == 'dual_map':
        return lam
    m = [-x for x in lam]
    a = sorted((abs(x) for x in m), reverse=True)
    w = list(a)
    if sum(1 for x in m if x < 0) % 2 == 1:
        w[n - 1] = -w[n - 1]
    return tuple(w)


def mod_dim(mod: dict, n: int) -> int:
    return sum(v * weyl_dim(k, n) for k, v in mod.items())


def mod_classes(mod: dict) -> set:
    return {cls(k) for k in mod}


def mod_dual(mod: dict, n: int) -> dict:
    return {dual(k, n): v for k, v in mod.items()}


def mod_add(a: dict, b: dict) -> dict:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}


def mod_sub(a: dict, b: dict) -> dict:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v != 0}


def hom_dim(a: dict, b: dict) -> int:
    return sum(a.get(k, 0) * b.get(k, 0) for k in set(a) | set(b))


def inv_dim(pair_dec: dict, t_dec: dict, n: int) -> int:
    """dim Inv(X (x) T) = sum_lam mult_X(lam^*) mult_T(lam)."""
    return hom_dim(mod_dual(pair_dec, n), t_dec)


def prod_wts(A: list, B: list, n: int) -> list:
    return [tuple(a[i] + b[i] for i in range(n)) for a in A for b in B]


def sym2_wts(A: list, n: int) -> list:
    """Weights of Sym^2 of the module with weight list A (i <= j)."""
    L = len(A)
    hi = 1 if MUT != 'sym2_pairs' else 0
    return [tuple(A[i][t] + A[j][t] for t in range(n))
            for i in range(L) for j in range(i + 1 - hi, L)]


# ===========================================================================
# SECTION 1 -- machinery certifies itself; [R] the banked D_7 layer
# ===========================================================================

def named_irreps(n=7):
    lam = {('L', k): tuple([2] * k + [0] * (n - k)) for k in range(0, n)}
    lam[('L7', '+')] = tuple([2] * n)
    lam[('L7', '-')] = tuple([2] * (n - 1) + [-2])
    return lam


def section_1(n=7):
    for m in (5, 6, 7):
        sums = {sum(a) for a in pos_roots(m)}
        check('machinery', 'D_%d roots have doubled sum in {0,+-4}' % m,
              sums <= {0, 4, -4}, sorted(sums))
    NI = named_irreps(n)
    dims = {('L', 0): 1, ('L', 1): 14, ('L', 2): 91, ('L', 3): 364,
            ('L', 4): 1001, ('L', 5): 2002, ('L', 6): 3003,
            ('L7', '+'): 1716, ('L7', '-'): 1716}
    for k, d in dims.items():
        check('machinery', 'dim Lambda^%s = %d' % (str(k), d),
              weyl_dim(NI[k], n) == d, weyl_dim(NI[k], n))
    Sp, Sm = tuple([1] * n), tuple([1] * (n - 1) + [-1])
    Hp, Hm = (3, 1, 1, 1, 1, 1, 1), (3, 1, 1, 1, 1, 1, -1)
    for nm, lam, d in (('S+', Sp, 64), ('S-', Sm, 64),
                       ('H+', Hp, 832), ('H-', Hm, 832)):
        check('machinery', 'dim %s = %d' % (nm, d), weyl_dim(lam, n) == d)
    check('machinery', 'dual(S+) = S- and dual(L7+) = L7- at D_7 (n odd)',
          dual(Sp, n) == Sm and dual(NI[('L7', '+')], n) == NI[('L7', '-')])
    check('machinery', 'L7+ and L7- are each SELF-classed 2 and dual-SWAPPED',
          cls(NI[('L7', '+')]) == 2 == cls(NI[('L7', '-')]))

    # [R] CR-B / CS-1 class table
    check('reproduce', '[R] cls(S+)=3 cls(S-)=1 cls(V)=2 cls(Lambda^2)=0',
          (cls(Sp), cls(Sm), cls(NI[('L', 1)]), cls(NI[('L', 2)])) == (3, 1, 2, 0))

    # corners
    corners = {
        'nu+': decompose_wts(spin_wts(n, 0), n),
        'nu-': decompose_wts(spin_wts(n, 1), n),
        'zeta+': decompose_wts(prod_wts(vec_wts(n), spin_wts(n, 0), n), n),
        'zeta-': decompose_wts(prod_wts(vec_wts(n), spin_wts(n, 1), n), n),
    }
    check('reproduce', '[R] nu+ = {S+}, nu- = {S-}',
          corners['nu+'] == {Sp: 1} and corners['nu-'] == {Sm: 1})
    check('reproduce', '[R] zeta+ = Omega^1(S+) = S- (+) 832_+ ; zeta- = S+ (+) 832_-',
          corners['zeta+'] == {Sm: 1, Hp: 1} and corners['zeta-'] == {Sp: 1, Hm: 1},
          (corners['zeta+'], corners['zeta-']))
    ccls = {k: sorted(mod_classes(v)) for k, v in corners.items()}
    check('reproduce', '[R] corner classes 3,1,1,3 (nu+, nu-, zeta+, zeta-)',
          ccls == {'nu+': [3], 'nu-': [1], 'zeta+': [1], 'zeta-': [3]}, ccls)

    # ad P = End(Delta) = sum_k Lambda^k V, decomposed from 128^2 weights
    dwts = spin_wts(n, 0) + spin_wts(n, 1)
    endd = decompose_wts(prod_wts(dwts, dwts, n), n)
    if MUT == 'endd_drop':
        endd = dict(endd)
        endd.pop(NI[('L7', '-')], None)
    expected_endd = {NI[('L', k)]: 2 for k in range(0, n)}
    expected_endd[NI[('L7', '+')]] = 1
    expected_endd[NI[('L7', '-')]] = 1
    check('reproduce',
          '[R] ad P = End(Delta) = 2(L0+...+L6) (+) L7+ (+) L7-  '
          '(dimension-saturated 16384)',
          endd == expected_endd and mod_dim(endd, n) == 16384,
          mod_dim(endd, n))
    check('reproduce', '[R] ad P spans classes {0,2} only',
          mod_classes(endd) == {0, 2}, sorted(mod_classes(endd)))

    RESULT['corner_classes'] = ccls
    return corners, endd, NI


# ===========================================================================
# SECTION 2 -- [R] CS-1's decision numbers, reproduced before extension
# ===========================================================================

def section_2(corners, NI, n=7):
    Sp, Sm = tuple([1] * n), tuple([1] * (n - 1) + [-1])
    Wp = mod_add(corners['nu+'], corners['zeta-'])
    Wm = mod_add(corners['nu-'], corners['zeta+'])
    Wmix = mod_add(corners['nu+'], corners['zeta+'])
    check('reproduce', '[R] W+^* = W- exactly; dim W+ = dim W- = 960',
          mod_dual(Wp, n) == Wm and mod_dim(Wp, n) == 960)

    SpSp = decompose_wts(prod_wts(spin_wts(n, 0), spin_wts(n, 0), n), n)
    check('reproduce',
          '[R] S+ (x) S+ = L1 (+) L3 (+) L5 (+) L7+, no L0 (no bare bilinear)',
          SpSp == {NI[('L', 1)]: 1, NI[('L', 3)]: 1, NI[('L', 5)]: 1,
                   NI[('L7', '+')]: 1}, SpSp)

    mass_prot = hom_dim(Wp, mod_dual(Wp, n))
    check('reproduce', '[R] bare mass on W+ = 0', mass_prot == 0, mass_prot)

    kin = hom_dim(tensor_mod(Wp, vec_wts(n), n), mod_dual(Wp, n))
    check('reproduce', '[R] first-order pairing on W+ = 9 (kinetic exists)',
          kin == 9, kin)
    mass_mixed = hom_dim(Wmix, mod_dual(Wmix, n))
    check('reproduce', '[R] class-MIXED pairing bare mass = 2', mass_mixed == 2)
    kin_mixed = hom_dim(tensor_mod(corners['nu+'], vec_wts(n), n),
                        mod_dual(corners['zeta+'], n))
    check('reproduce', '[R] class-MIXED cross kinetic = 0', kin_mixed == 0)

    # CS-1's operator row: Omega^0(S+) -> Omega^1(S-) at k=0,1,2 and with L3
    row = []
    wts_k = {0: [tuple([0] * n)], 1: vec_wts(n)}
    d0 = hom_dim(corners['nu+'], corners['zeta-'])
    d1 = hom_dim(tensor_mod(corners['nu+'], vec_wts(n), n), corners['zeta-'])
    sym2V = sym2_wts(vec_wts(n), n)
    d2 = hom_dim(tensor_mod(corners['nu+'], sym2V, n), corners['zeta-'])
    dins = hom_dim(tensor_mod(tensor_mod(corners['nu+'], vec_wts(n), n),
                              lam_k_wts(n, 3), n), corners['zeta-'])
    check('reproduce',
          '[R] CS-1 operator row Omega^0(S+) -> Omega^1(S-): k=0,1,2 = 1,0,2 '
          'and k=1 with a Lambda^3 (class-2 ad P) insertion = 5',
          (d0, d1, d2, dins) == (1, 0, 2, 5), (d0, d1, d2, dins))
    RESULT['cs1_row'] = (d0, d1, d2, dins)
    return Wp, Wm


# corner weight LISTS (explicit multisets), built once
def corner_weight_lists(n=7):
    return {
        'nu+': spin_wts(n, 0),
        'nu-': spin_wts(n, 1),
        'zeta+': prod_wts(vec_wts(n), spin_wts(n, 0), n),
        'zeta-': prod_wts(vec_wts(n), spin_wts(n, 1), n),
    }


# ===========================================================================
# SECTION 3 -- NEW: the Sym^2/Lambda^2 split and the mass-shape table
# ===========================================================================

def section_3(corners, endd, NI, n=7):
    cw = corner_weight_lists(n)
    Sp, Sm = tuple([1] * n), tuple([1] * (n - 1) + [-1])
    L = {k: NI[k] for k in NI}

    # ---- Sym^2 / Lambda^2 of the half-spinors -----------------------------
    sym_sp = decompose_wts(sym2_wts(cw['nu+'], n), n)
    lam_sp = mod_sub(decompose_wts(prod_wts(cw['nu+'], cw['nu+'], n), n), sym_sp)
    sym_sm = decompose_wts(sym2_wts(cw['nu-'], n), n)
    lam_sm = mod_sub(decompose_wts(prod_wts(cw['nu-'], cw['nu-'], n), n), sym_sm)
    check('split', 'NEW Sym^2(S+) = L3 (+) L7+  (dim 2080)',
          sym_sp == {L[('L', 3)]: 1, L[('L7', '+')]: 1}
          and mod_dim(sym_sp, n) == 2080, sym_sp)
    check('split', 'NEW Lambda^2(S+) = L1 (+) L5  (dim 2016)',
          lam_sp == {L[('L', 1)]: 1, L[('L', 5)]: 1}
          and mod_dim(lam_sp, n) == 2016, lam_sp)
    check('split', 'NEW Sym^2(S-) = L3 (+) L7-  and Lambda^2(S-) = L1 (+) L5',
          sym_sm == {L[('L', 3)]: 1, L[('L7', '-')]: 1}
          and lam_sm == {L[('L', 1)]: 1, L[('L', 5)]: 1}, (sym_sm, lam_sm))
    check('split',
          'Lambda^2(S+) and Lambda^2(S-) have IDENTICAL irrep content '
          '(both {L1, L5}): no irrep-TYPE-selective Grassmann-live diagonal '
          'mass at the 0-form corners', lam_sp == lam_sm)
    check('split',
          'Sym^2(S+) and Sym^2(S-) differ EXACTLY in the middle form '
          '(L7+ vs L7-): the chirally selective diagonal shapes are the '
          'SYMMETRIC ones', mod_sub(sym_sp, sym_sm) ==
          {L[('L7', '+')]: 1, L[('L7', '-')]: -1})

    # ---- diagonal splits for the 1-form corners ---------------------------
    diag = {'nu+': (sym_sp, lam_sp), 'nu-': (sym_sm, lam_sm)}
    for z in ('zeta+', 'zeta-'):
        sq = decompose_wts(prod_wts(cw[z], cw[z], n), n)
        sy = decompose_wts(sym2_wts(cw[z], n), n)
        la = mod_sub(sq, sy)
        Ld = len(cw[z])
        check('split', '%s: dim Sym^2 = %d and dim Lambda^2 = %d (saturated)'
              % (z, Ld * (Ld + 1) // 2, Ld * (Ld - 1) // 2),
              mod_dim(sy, n) == Ld * (Ld + 1) // 2
              and mod_dim(la, n) == Ld * (Ld - 1) // 2)
        diag[z] = (sy, la)

    # ---- insertion carriers ----------------------------------------------
    triv = {tuple([0] * n): 1}
    ad0 = endd                                     # Omega^0(ad P)
    ad1 = tensor_mod(endd, vec_wts(n), n)          # Omega^1(ad P)
    check('machinery', 'Omega^1(ad P) is dimension-saturated (14 x 16384)',
          mod_dim(ad1, n) == 14 * 16384, mod_dim(ad1, n))
    ins_cols = [('bare', triv), ('O0ad', ad0), ('O1ad', ad1)]

    # ---- the ten-pair table ----------------------------------------------
    names = ('nu+', 'nu-', 'zeta+', 'zeta-')
    pair_dec = {}
    for i, a in enumerate(names):
        for b in names[i:]:
            pair_dec[(a, b)] = decompose_wts(prod_wts(cw[a], cw[b], n), n)
    table = {}
    for (a, b), dec in pair_dec.items():
        for cn, T in ins_cols:
            table[(a, b, cn)] = inv_dim(dec, T, n)
    dtable = {}
    for c in names:
        sy, la = diag[c]
        for cn, T in ins_cols:
            dtable[(c, cn)] = (inv_dim(sy, T, n), inv_dim(la, T, n))
            check('table', '%s diagonal %s: sym+antisym = total (%d+%d=%d)'
                  % (c, cn, dtable[(c, cn)][0], dtable[(c, cn)][1],
                     table[(c, c, cn)]),
                  sum(dtable[(c, cn)]) == table[(c, c, cn)])

    # headline structural checks on the table
    check('table',
          'BARE DIAGONALS ALL ZERO: no bare same-corner self-pairing anywhere '
          '(the Majorana-shape theorem clause at the carrier layer)',
          all(table[(c, c, 'bare')] == 0 for c in names),
          {c: table[(c, c, 'bare')] for c in names})
    bare_cross = {(a, b): table[(a, b, 'bare')]
                  for (a, b) in pair_dec if a != b}
    check('table',
          'BARE CROSS SHAPES: exactly {nu+nu-:1, nu+zeta+:1, nu-zeta-:1, '
          'zeta+zeta-:2}, all cross-CLASS; the same-class cross pairs are 0',
          bare_cross == {('nu+', 'nu-'): 1, ('nu+', 'zeta+'): 1,
                         ('nu-', 'zeta-'): 1, ('zeta+', 'zeta-'): 2,
                         ('nu+', 'zeta-'): 0, ('nu-', 'zeta+'): 0},
          bare_cross)
    check('table',
          'ONE DECLARED INSERTION RESTORES EVERYTHING: with one Omega^0(ad P) '
          'insertion every one of the ten pairings is nonzero, and likewise '
          'with one Omega^1(ad P) insertion',
          all(table[(a, b, 'O0ad')] > 0 and table[(a, b, 'O1ad')] > 0
              for (a, b) in pair_dec),
          {k: v for k, v in table.items() if v == 0 and k[2] != 'bare'})
    check('table',
          'nu+ diagonal with one Omega^0(ad P) insertion: (sym, antisym) = '
          '(3, 4); nu- mirror (3, 4) -- the Grassmann-live (antisym) shapes '
          'exist with multiplicity 4 on each 0-form corner',
          dtable[('nu+', 'O0ad')] == (3, 4) == dtable[('nu-', 'O0ad')],
          (dtable[('nu+', 'O0ad')], dtable[('nu-', 'O0ad')]))

    # ---- class sweep over every nonzero entry -----------------------------
    corner_cls = {'nu+': 3, 'nu-': 1, 'zeta+': 1, 'zeta-': 3}
    ins_cls = {'bare': (0,), 'O0ad': (0, 2), 'O1ad': (0, 2)}
    if MUT == 'insertion_class':
        ins_cls = {'bare': (0,), 'O0ad': (1, 3), 'O1ad': (1, 3)}
    bad = []
    allowed_zero = 0
    for (a, b, cn), v in table.items():
        need = (-corner_cls[a] - corner_cls[b]) % 4
        if v > 0 and need not in ins_cls[cn]:
            bad.append((a, b, cn, v, need))
        if v == 0 and need in ins_cls[cn]:
            allowed_zero += 1
    check('sweep',
          'CLASS SWEEP: every nonzero mass-shape entry is class-allowed '
          '(insertion classes {0,2} only); no violation over all 30 cells',
          not bad, bad)
    check('sweep',
          'COARSE SATURATION (recorded, and itself a finding): at whole-slot '
          'granularity the declared slots feed EVERY class-allowed cell -- '
          'the class rule is exactly saturated at slot level (%d allowed-'
          'and-zero cells)' % allowed_zero, allowed_zero == 0, allowed_zero)

    RESULT['pair_table'] = {'%s|%s|%s' % k: v for k, v in table.items()}
    RESULT['diag_table'] = {'%s|%s' % k: v for k, v in dtable.items()}
    return cw, pair_dec, diag, ad0, ad1, table, dtable


# ===========================================================================
# SECTION 4 -- NEW: per-irrep insertion selectivity (which Lambda^k feeds what)
# ===========================================================================

def section_4(diag, endd, NI, n=7):
    sel = {}
    keys = [('L', 1), ('L', 3), ('L', 5), ('L7', '+'), ('L7', '-')]
    for c in ('nu+', 'nu-', 'zeta+', 'zeta-'):
        sy, la = diag[c]
        for k in keys:
            T = {NI[k]: 1}
            sel[(c, str(k))] = (inv_dim(sy, T, n), inv_dim(la, T, n))
    check('selectivity',
          'L7+ feeds ONLY Sym^2(nu-) and L7- ONLY Sym^2(nu+): the middle-form '
          'insertion is perfectly chirality-selective at the 0-form corners',
          sel[('nu-', "('L7', '+')")] == (1, 0)
          and sel[('nu+', "('L7', '+')")] == (0, 0)
          and sel[('nu+', "('L7', '-')")] == (1, 0)
          and sel[('nu-', "('L7', '-')")] == (0, 0),
          {k: v for k, v in sel.items() if 'L7' in k[1] and k[0].startswith('nu')})
    check('selectivity',
          'L1 and L5 feed Lambda^2 (Grassmann-live) of BOTH nu+ and nu- '
          'alike: the Grassmann-live directions are chirality-BLIND at the '
          '0-form corners',
          all(sel[(c, str(k))] == (0, 1) for c in ('nu+', 'nu-')
              for k in (('L', 1), ('L', 5))),
          {k: v for k, v in sel.items()
           if k[1] in ("('L', 1)", "('L', 5)") and k[0].startswith('nu')})
    check('selectivity',
          'L3 feeds Sym^2 of both nu corners (chirality-blind symmetric)',
          sel[('nu+', "('L', 3)")] == (1, 0) == sel[('nu-', "('L', 3)")])
    # the 1-form corners: does the chirality-selective middle form reach the
    # Grassmann-live column there?
    z_sel = {k: v for k, v in sel.items() if k[0].startswith('zeta')}
    l7_live_zp = sel[('zeta+', "('L7', '+')")][1] + sel[('zeta+', "('L7', '-')")][1]
    l7_live_zm = sel[('zeta-', "('L7', '+')")][1] + sel[('zeta-', "('L7', '-')")][1]
    check('selectivity',
          'AT THE 1-FORM CORNERS the middle form DOES reach the '
          'Grassmann-live column (Lambda^2(V (x) S) contains '
          'Lambda^2 V (x) Sym^2 S): L7 insertions give antisymmetric '
          'self-shapes on zeta+ and zeta- (counts recorded)',
          l7_live_zp > 0 and l7_live_zm > 0, (l7_live_zp, l7_live_zm))
    sel_asym = {
        'zeta+': (sel[('zeta+', "('L7', '+')")][1], sel[('zeta+', "('L7', '-')")][1]),
        'zeta-': (sel[('zeta-', "('L7', '+')")][1], sel[('zeta-', "('L7', '-')")][1])}
    check('selectivity',
          'THE ONE-FORM TEXTURE ROUTE, exact: L7- feeds Lambda^2(zeta+) with '
          'multiplicity 1 and Lambda^2(zeta-) with 0; L7+ the mirror; and '
          'Lambda^2(nu+-) get 0 from both.  A single L7-direction insertion '
          'therefore generates a Grassmann-live diagonal self-shape on '
          'EXACTLY ONE corner, and that corner is a 1-form corner',
          sel[('zeta+', "('L7', '-')")][1] == 1
          and sel[('zeta+', "('L7', '+')")][1] == 0
          and sel[('zeta-', "('L7', '+')")][1] == 1
          and sel[('zeta-', "('L7', '-')")][1] == 0
          and all(sel[(c, k)][1] == 0 for c in ('nu+', 'nu-')
                  for k in ("('L7', '+')", "('L7', '-')")), sel_asym)
    # necessity-not-sufficiency lives at the per-irrep level: every listed
    # irrep is class-2, every diagonal needs class 2, so ALL these cells are
    # class-ALLOWED -- and many are 0 anyway.
    allowed_zero_fine = [(c, k, part)
                         for (c, k), v in sel.items()
                         for part, val in (('sym', v[0]), ('antisym', v[1]))
                         if val == 0]
    check('sweep',
          'necessity is NOT sufficiency at the per-irrep level: %d class-'
          'ALLOWED (corner-diagonal, class-2 irrep, symmetry) cells have '
          'Hom = 0 anyway (e.g. Sym^2(nu+) (x) L7+)'
          % len(allowed_zero_fine),
          len(allowed_zero_fine) >= 8
          and ('nu+', "('L7', '+')", 'sym') in allowed_zero_fine,
          allowed_zero_fine[:6])
    RESULT['l7_zeta_live'] = sel_asym
    RESULT['selectivity'] = {'%s|%s' % k: v for k, v in sel.items()}
    return sel


# ===========================================================================
# SECTION 5 -- NEW: the protected-half pencil question, decided
# ===========================================================================

def section_5(corners, cw, pair_dec, ad0, ad1, table, NI, n=7):
    triv = {tuple([0] * n): 1}
    Wp = mod_add(corners['nu+'], corners['zeta-'])
    Wm = mod_add(corners['nu-'], corners['zeta+'])

    # (1) THE THEOREM CLAUSE.  Same-class bilinear on W+ at even orders: zero.
    def wp_bilinear_with(Twts_or_dec, is_dec):
        blocks = [('nu+', 'nu+', 1), ('nu+', 'zeta-', 2), ('zeta-', 'zeta-', 1)]
        tot = 0
        for a, b, m in blocks:
            dec = pair_dec[(a, b)] if (a, b) in pair_dec else pair_dec[(b, a)]
            T = Twts_or_dec if is_dec else decompose_wts(Twts_or_dec, n)
            tot += m * inv_dim(dec, T, n)
        return tot

    k0 = wp_bilinear_with(triv, True)
    k1 = wp_bilinear_with(vec_wts(n), False)
    k2 = wp_bilinear_with(sym2_wts(vec_wts(n), n), False)
    check('pencil',
          'THEOREM CLAUSE (bare): invariant bilinear on W+ (x) W+ with k '
          'derivatives = 0, 9, 0 for k = 0, 1, 2; every EVEN order vanishes '
          'by the class rule (6 + 2k = 0 mod 4 iff k odd), so no bare mass '
          'and no bare eigenvalue pairing at any even order',
          (k0, k1, k2) == (0, 9, 0), (k0, k1, k2))

    # (2) THE AVAILABILITY CLAUSE.  One declared insertion restores it.
    a0 = wp_bilinear_with(ad0, True)
    a1 = wp_bilinear_with(ad1, True)
    check('pencil',
          'AVAILABILITY CLAUSE: zero-order bilinear on W+ (x) W+ with ONE '
          'declared insertion: Omega^0(ad P) gives %d and Omega^1(ad P) '
          'gives %d -- both NONZERO, and blockwise additive' % (a0, a1),
          a0 > 0 and a1 > 0
          and a0 == table[('nu+', 'nu+', 'O0ad')]
          + 2 * table[('nu+', 'zeta-', 'O0ad')]
          + table[('zeta-', 'zeta-', 'O0ad')], (a0, a1))

    # class-0 content does NOT unlock the same-class bilinear
    z_l2 = wp_bilinear_with({NI[('L', 2)]: 1}, True)
    z_l0 = wp_bilinear_with({NI[('L', 0)]: 1}, True)
    check('pencil',
          'a class-0 insertion NEVER unlocks the same-class bilinear: '
          'Lambda^0 and Lambda^2 (the so(14) adjoint) give 0',
          z_l2 == 0 and z_l0 == 0, (z_l0, z_l2))

    # ODD-COUNT rule: two class-2 insertions restore the bare prohibition
    two_ins = inv_dim(pair_dec[('nu+', 'nu+')],
                      decompose_wts(prod_wts(lam_k_wts(n, 3),
                                             lam_k_wts(n, 3), n), n), n)
    check('pencil',
          'ODD-COUNT RULE witness: TWO class-2 insertions (L3 (x) L3) on the '
          'nu+ diagonal give 0 again -- same-class shapes need an ODD number '
          'of class-2 insertions', two_ins == 0, two_ins)

    # (3) THE PENCIL GEOGRAPHY.  Operator guise of the same numbers.
    op_bare_mass = hom_dim(Wp, Wm)         # W+ -> W+^* bare order 0
    op_bare_pencil = hom_dim(Wp, Wp)       # W+ -> W-^* = W+ bare order 0
    check('pencil',
          'DUALITY DISCIPLINE, both guises: bare order-0 W+ -> W+^* '
          '(same-class bilinear) = 0, while bare order-0 W+ -> W-^* = W+ '
          '(the barred-grammar pencil block) = 5',
          op_bare_mass == 0 and op_bare_pencil == 5,
          (op_bare_mass, op_bare_pencil))
    # the five, named: they are exactly the bare cross-class shapes
    five = (table[('nu+', 'nu-', 'bare')] + table[('nu+', 'zeta+', 'bare')]
            + table[('nu-', 'zeta-', 'bare')] + table[('zeta+', 'zeta-', 'bare')])
    check('pencil',
          'the 5 bare pencil shapes ARE the 5 bare cross-class mass shapes '
          '(1+1+1+2), i.e. they sit at the varpi-cell positions plus the two '
          'southeast Dirac cells of eq (9.16)', five == 5 == op_bare_pencil,
          five)

    # eq (9.16) cell geography under CS-1's unique convention (flip=True):
    # rows (bzeta-, bzeta+, bnu-, bnu+) classes (1,3,1,3);
    # cols (zeta+, zeta-, nu+, nu-) classes (3,1,3,1).
    R = (1, 3, 1, 3)
    C = (3, 1, 3, 1)
    D0_CELLS = ((0, 1), (0, 3), (1, 0), (1, 2), (2, 1), (3, 0))
    VARPI_CELLS = ((0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (3, 1))
    SE_ZERO = ((2, 2), (2, 3), (3, 2), (3, 3))
    d0_ok = all((R[i] + 2 + C[j]) % 4 == 0 for i, j in D0_CELLS)
    varpi_bare_allowed = [(i, j) for i, j in VARPI_CELLS
                          if (R[i] + C[j]) % 4 == 0]
    se_bare_allowed = [(i, j) for i, j in SE_ZERO if (R[i] + C[j]) % 4 == 0]
    se_first_allowed = [(i, j) for i, j in SE_ZERO
                        if (R[i] + 2 + C[j]) % 4 == 0]
    check('geography', '[R] the six printed d_0 cells are first-order '
          'class-consistent under the unique CS-1 convention', d0_ok)
    check('geography',
          'NEW: ALL SIX varpi cells sit at bare-order-0-ALLOWED positions '
          '(row class + col class = 0): the draft prints varpi-linear entries '
          'where varpi-INDEPENDENT bare entries are also class-allowed',
          len(varpi_bare_allowed) == 6, varpi_bare_allowed)
    check('geography',
          'NEW: of the four southeast zeros, the TWO cells NOT first-order-'
          'allowed are exactly the two ORDER-0 bare-Dirac-allowed cells '
          '(bnu- x nu+ and bnu+ x nu-, each of Hom dimension 1): all four SE '
          'zeros are class-allowed at some order <= 1, and the draft zeroes '
          'them all',
          sorted(se_bare_allowed) == [(2, 2), (3, 3)]
          and sorted(se_first_allowed) == [(2, 3), (3, 2)]
          and table[('nu+', 'nu-', 'bare')] == 1,
          (se_bare_allowed, se_first_allowed))

    # (4) ROBUSTNESS OF THE AVAILABILITY CLAUSE against the ad P seam.
    # Split ad P by block parity: even (chirality-preserving, block-diagonal)
    # part 2(L0+L2+L4+L6); odd (chirality-flipping) part 2(L1+L3+L5)+L7+ +L7-.
    ad_even = {NI[('L', k)]: 2 for k in (0, 2, 4, 6)}
    ad_odd = {NI[('L', k)]: 2 for k in (1, 3, 5)}
    ad_odd[NI[('L7', '+')]] = 1
    ad_odd[NI[('L7', '-')]] = 1
    ad1_even = tensor_mod(ad_even, vec_wts(n), n)
    ad1_odd = tensor_mod(ad_odd, vec_wts(n), n)
    names = ('nu+', 'nu-', 'zeta+', 'zeta-')
    ccls = {'nu+': 3, 'nu-': 1, 'zeta+': 1, 'zeta-': 3}
    comp_ok = True
    detail = {}
    for (a, b), dec in pair_dec.items():
        e0, o0 = inv_dim(dec, ad_even, n), inv_dim(dec, ad_odd, n)
        e1, o1 = inv_dim(dec, ad1_even, n), inv_dim(dec, ad1_odd, n)
        same = (ccls[a] + ccls[b]) % 4 == 2
        # class forcing: same-class cells use odd blocks at Omega^0 and even
        # blocks at Omega^1; cross-class cells the reverse.  EXACT
        # complementarity: the non-forced parity contributes 0.
        if same and not (e0 == 0 and o1 == 0):
            comp_ok = False
        if (not same) and not (o0 == 0 and e1 == 0):
            comp_ok = False
        detail[(a, b)] = (e0, o0, e1, o1)
    check('robustness',
          'BLOCK-PARITY COMPLEMENTARITY, exact on all 10 pairs: same-class '
          'cells are fed ONLY by odd blocks at Omega^0 and ONLY by the even '
          '(chirality-preserving) part at Omega^1; cross-class cells the '
          'reverse', comp_ok,
          {('%s|%s' % k): v for k, v in detail.items()})
    check('robustness',
          'SEAM ROBUSTNESS: every same-class cell (the cells the protected-'
          'half spectrum needs) is fed by the Omega^1 EVEN route alone -- so '
          'the availability clause survives ANY reality condition that '
          'constrains the odd blocks of End(Delta)',
          all(detail[(a, b)][2] > 0 for (a, b) in pair_dec
              if (ccls[a] + ccls[b]) % 4 == 2),
          {('%s|%s' % (a, b)): detail[(a, b)][2] for (a, b) in pair_dec
           if (ccls[a] + ccls[b]) % 4 == 2})
    # minimal-ad control: even the bare so(14) adjoint Lambda^2 alone, used
    # as the Omega^1 coefficient, feeds the protected-half mass cells.
    ad1_min = tensor_mod({NI[('L', 2)]: 1}, vec_wts(n), n)
    min_cells = {('%s|%s' % (a, b)): inv_dim(pair_dec[(a, b)], ad1_min, n)
                 for (a, b) in pair_dec if (ccls[a] + ccls[b]) % 4 == 2}
    check('robustness',
          'MINIMAL-AD CONTROL: Omega^1(Lambda^2) alone (the so(14) adjoint, '
          'the most conservative reading of the gauge content) already feeds '
          'every same-class cell', all(v > 0 for v in min_cells.values()),
          min_cells)
    RESULT['block_split'] = {('%s|%s' % k): v for k, v in detail.items()}
    RESULT['minimal_ad_cells'] = min_cells

    RESULT['pencil'] = {
        'wp_bilinear_k0_k1_k2': (k0, k1, k2),
        'wp_bilinear_O0ad': a0, 'wp_bilinear_O1ad': a1,
        'wp_bilinear_class0_L0_L2': (z_l0, z_l2),
        'wp_op_bare_mass': op_bare_mass, 'wp_op_bare_pencil': op_bare_pencil,
        'two_insertion_nu_diag': two_ins,
    }
    return Wp, Wm


# ===========================================================================
# SECTION 6 -- contrary controls: D_6 (existence + symmetry) and D_5 (mirror)
# ===========================================================================

def section_6():
    # D_6: the class-homogeneous half has a bare mass (5) -- and its Lambda^0
    # sits in the ANTISYMMETRIC square, so the detected self-pairing is
    # Grassmann-live.  The instrument sees presence and assigns symmetry.
    n = 6
    Sp6 = spin_wts(n, 0)
    Sm6 = spin_wts(n, 1)
    triv6 = tuple([0] * n)
    sq6 = decompose_wts(prod_wts(Sp6, Sp6, n), n)
    sy6 = decompose_wts(sym2_wts(Sp6, n), n)
    la6 = mod_sub(sq6, sy6)
    check('contrary-D6',
          'D_6 CONTRARY: S+ (x) S+ CONTAINS the trivial rep (bare self-'
          'pairing EXISTS: the machinery detects presence, not only absence)',
          sq6.get(triv6, 0) == 1, sq6.get(triv6, 0))
    check('contrary-D6',
          'D_6 NEW RIDER: Lambda^0 sits in Lambda^2(S+) (antisymmetric '
          'square): the 12-dimensional bare self-mass is Grassmann-LIVE',
          la6.get(triv6, 0) == 1 and sy6.get(triv6, 0) == 0,
          (sy6.get(triv6, 0), la6.get(triv6, 0)))
    Wp6 = mod_add(decompose_wts(Sp6, n),
                  decompose_wts(prod_wts(vec_wts(n), Sm6, n), n))
    mass6 = hom_dim(Wp6, mod_dual(Wp6, n))
    kin6 = hom_dim(tensor_mod(Wp6, vec_wts(n), n), mod_dual(Wp6, n))
    check('contrary-D6', '[R] D_6 mirror numbers: bare mass 5, kinetic 0 '
          '(the exact reverse of D_7)', mass6 == 5 and kin6 == 0,
          (mass6, kin6))
    RESULT['d6'] = {'mass': mass6, 'kinetic': kin6,
                    'L0_side': 'Lambda^2 (antisym)'}

    # D_5: the MJ-1 comparator mirror.  16 (x) 16 = 10 + 120 + 126 with the
    # Majorana block in the SYMMETRIC square: Sym^2(16) = 10 (+) 126.
    n = 5
    S16 = spin_wts(n, 0)
    sq5 = decompose_wts(prod_wts(S16, S16, n), n)
    sy5 = decompose_wts(sym2_wts(S16, n), n)
    la5 = mod_sub(sq5, sy5)
    L1_5 = (2, 0, 0, 0, 0)
    L3_5 = (2, 2, 2, 0, 0)
    L5p = (2, 2, 2, 2, 2)
    check('contrary-D5',
          '[R] D_5 mirror: 16 (x) 16 = 10 (+) 120 (+) 126 and the Majorana '
          'block is in the symmetric square: Sym^2(16) = 10 (+) 126 '
          '(dim 136), Lambda^2(16) = 120',
          sq5 == {L1_5: 1, L3_5: 1, L5p: 1}
          and sy5 == {L1_5: 1, L5p: 1} and la5 == {L3_5: 1}
          and mod_dim(sy5, n) == 136 and weyl_dim(L5p, n) == 126,
          (sq5, sy5, la5))
    RESULT['d5'] = {'sym': 'L1+L5p (10+126)', 'lam': 'L3 (120)'}


# ===========================================================================
# SECTION 7 -- planted false facts
# ===========================================================================

def section_7(corners, diag, table, sel, NI, n=7):
    Sp = tuple([1] * n)
    triv = tuple([0] * n)
    sq = decompose_wts(prod_wts(spin_wts(n, 0), spin_wts(n, 0), n), n)
    sym_sp, lam_sp = diag['nu+']
    p = RESULT['pencil']
    planted = [
        ('Lambda^0 appears in S+ (x) S+ at D_7', sq.get(triv, 0) > 0),
        ('Lambda^1 sits in the SYMMETRIC square of S+',
         sym_sp.get(NI[('L', 1)], 0) > 0),
        ('dual(L7+) = L7+ at D_7',
         dual(NI[('L7', '+')], n) == NI[('L7', '+')]),
        ('some corner has a bare diagonal self-pairing',
         any(table[(c, c, 'bare')] > 0
             for c in ('nu+', 'nu-', 'zeta+', 'zeta-'))),
        ('the protected half W+ has a bare mass',
         p['wp_bilinear_k0_k1_k2'][0] > 0),
        ('L7+ feeds Sym^2(nu+)', sel[('nu+', "('L7', '+')")][0] > 0),
        ('L3 feeds the Grassmann-live column of nu+',
         sel[('nu+', "('L', 3)")][1] > 0),
        ('a class-0 insertion (Lambda^0 or the so(14) adjoint Lambda^2) '
         'unlocks the W+ same-class bilinear',
         any(z > 0 for z in p['wp_bilinear_class0_L0_L2'])),
        ('two class-2 insertions unlock the nu+ diagonal',
         p['two_insertion_nu_diag'] > 0),
        ('at D_6 the bare self-pairing is symmetric (Grassmann-dead)',
         RESULT['d6']['L0_side'] != 'Lambda^2 (antisym)'),
        ('at D_5 the 126 sits in Lambda^2(16)',
         RESULT['d5']['lam'] != 'L3 (120)'),
        ('all four southeast zeros are order-0 bare-allowed',
         len([1 for i, j in ((2, 2), (2, 3), (3, 2), (3, 3))
              if ((1, 3, 1, 3)[i] + (3, 1, 3, 1)[j]) % 4 == 0]) == 4),
        ('the bare cross-class shape count differs from 5',
         p['wp_op_bare_pencil'] != 5),
        ('the Omega^1(ad P) insertion column has a zero cell',
         any(table[(a, b, 'O1ad')] == 0 for (a, b) in
             [(x, y) for x in ('nu+', 'nu-', 'zeta+', 'zeta-')
              for y in ('nu+', 'nu-', 'zeta+', 'zeta-') if x <= y])),
        ('W+ (x) W+ admits a first-order bilinear of dimension other than 9',
         p['wp_bilinear_k0_k1_k2'][1] != 9),
    ]
    if MUT == 'planted':
        planted = [(nm, not v) for nm, v in planted]
    for nm, v in planted:
        check('planted-false', 'PLANTED FALSE observed False: %s' % nm,
              v is False, v)
    RESULT['planted'] = len(planted)


# ===========================================================================

def assert_no_float(obj, path='RESULT'):
    if isinstance(obj, float):
        raise AssertionError('load-bearing float at %s' % path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, '%s[%r]' % (path, k))
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, '%s[%d]' % (path, i))


def selftest() -> int:
    print('SELFTEST: verifying the clean baseline passes BEFORE any mutation')
    env0 = dict(os.environ)
    env0.pop('ST1_MUTATE', None)
    p0 = subprocess.run([sys.executable, os.path.abspath(__file__)],
                        env=env0, capture_output=True, text=True)
    print('  clean baseline exit %d  %s'
          % (p0.returncode, 'OK' if p0.returncode == 0 else 'BROKEN BASELINE'))
    if p0.returncode != 0:
        print('FAILURE-PATH SELFTEST: FAIL (baseline does not pass)')
        return 1
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ, ST1_MUTATE=m)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = p.returncode == 1
        print('  mutation %-18s exit %d  %s'
              % (m, p.returncode, 'OK' if good else 'FAILED TO FIRE'))
        ok = ok and good
    print('\nFAILURE-PATH SELFTEST: %s (baseline clean + %d/%d mutations '
          'drove exit 1)' % ('PASS' if ok else 'FAIL',
                             len(MUTATIONS) if ok else 0, len(MUTATIONS)))
    return 0 if ok else 1


def main() -> int:
    if '--selftest' in sys.argv:
        return selftest()
    n = 7
    corners, endd, NI = section_1(n)
    Wp, Wm = section_2(corners, NI, n)
    cw, pair_dec, diag, ad0, ad1, table, dtable = section_3(corners, endd, NI, n)
    sel = section_4(diag, endd, NI, n)
    section_5(corners, cw, pair_dec, ad0, ad1, table, NI, n)
    section_6()
    section_7(corners, diag, table, sel, NI, n)
    assert_no_float(RESULT)

    npass = sum(1 for t, nm, ok, dd in CERT if ok)
    ntot = len(CERT)
    counts: dict = {}
    for t, nm, ok, dd in CERT:
        counts[t] = counts.get(t, 0) + 1
    for t, nm, ok, dd in CERT:
        if not ok:
            print('FAIL [%s] %s   detail=%s' % (t, nm, dd))

    names = ('nu+', 'nu-', 'zeta+', 'zeta-')
    print()
    print('ST-1  at which layer does the seesaw obstruction live?')
    print()
    print('  MASS-SHAPE TABLE (zero-derivative invariant pairings, exact dim)')
    print('    %-16s %-6s %-10s %-10s   diagonal (sym, antisym)'
          % ('pair', 'bare', '+O0(adP)', '+O1(adP)'))
    for i, a in enumerate(names):
        for b in names[i:]:
            row = [RESULT['pair_table']['%s|%s|%s' % (a, b, cn)]
                   for cn in ('bare', 'O0ad', 'O1ad')]
            dd = ''
            if a == b:
                dd = '   sym/antisym: bare %s  O0 %s  O1 %s' % (
                    RESULT['diag_table']['%s|bare' % a],
                    RESULT['diag_table']['%s|O0ad' % a],
                    RESULT['diag_table']['%s|O1ad' % a])
            print('    %-16s %-6d %-10d %-10d%s'
                  % ('%s x %s' % (a, b), row[0], row[1], row[2], dd))
    print()
    p = RESULT['pencil']
    print('  THE PROTECTED HALF W+ = Omega^0(S+) (+) Omega^1(S-)')
    print('    bare bilinear at k = 0,1,2 derivatives : %s  '
          '(even orders all 0: THEOREM)' % (p['wp_bilinear_k0_k1_k2'],))
    print('    zero-order bilinear, ONE declared insertion: '
          'Omega^0(ad P) -> %d, Omega^1(ad P) -> %d  (AVAILABILITY)'
          % (p['wp_bilinear_O0ad'], p['wp_bilinear_O1ad']))
    print('    bare order-0  W+ -> W+^* : %d   (same-class bilinear: the '
          'obstruction)' % p['wp_op_bare_mass'])
    print('    bare order-0  W+ -> W-^* : %d   (the pencil block eq (9.16) '
          'prints as varpi-linear/zero)' % p['wp_op_bare_pencil'])
    print('    two class-2 insertions on the nu+ diagonal: %d  (odd-count '
          'rule)' % p['two_insertion_nu_diag'])
    print()
    print('  SELECTIVITY (which ad P component feeds which diagonal cell)')
    print('    L7+ -> Sym^2(nu-) only; L7- -> Sym^2(nu+) only '
          '(chirality-selective, Grassmann-dead at 0-form corners)')
    print('    L1, L5 -> Lambda^2 of BOTH nu corners (Grassmann-live, '
          'chirality-blind)')
    print('    L7 at the 1-form corners reaches Lambda^2 (Grassmann-live): '
          'zeta+ %s, zeta- %s' % (RESULT['l7_zeta_live']['zeta+'],
                                  RESULT['l7_zeta_live']['zeta-']))
    print()
    print('  CONTROLS: D_6 mass/kinetic = (%d, %d) with Lambda^0 in the '
          'ANTISYMMETRIC square; D_5 Sym^2(16) = 10 (+) 126 [R MJ-1]; '
          'planted false facts observed False: %d'
          % (RESULT['d6']['mass'], RESULT['d6']['kinetic'], RESULT['planted']))
    print()
    print('  check split: ' + '  '.join('[%s] %d' % (k, v)
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

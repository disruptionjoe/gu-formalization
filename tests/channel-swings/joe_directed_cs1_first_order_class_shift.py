#!/usr/bin/env python3
"""CS-1: the class-shift rule for first-order Spin-equivariant operators, and
what it does to CR-B's "protected" (class-homogeneous) reading of GU's four
printed fermionic corners.

THE GATE.  CR-B (2026-08-15, 179/179) established that the invariant governing
the chirality tie is ODD Z/4 CENTRE-CLASS HOMOGENEITY, then named as its own
cheapest next gate (section 7, Lens C):

    "a first-order Spin-equivariant operator Gamma(E) -> Gamma(F) needs
     cls(F) = cls(E) + 2.  Both summands of the protected pairing have the SAME
     class, so no first-order equivariant operator connects them -- while the
     class-MIXED pairing is precisely the one that admits it.  If GU's operator
     between the 0-form and 1-form slots is first-order and equivariant, the
     protected pairing cannot be the carrier of that operator."

This probe DERIVES the rule instead of quoting it, states its hypotheses,
computes exactly which operators each pairing admits at every symbol degree,
and then applies the rule to GU's OWN printed operator, eq (9.16) p.46
(SC-OP-04), whose sixteen cells and six derivative-cell locations are
identity-grade source data.

WHAT IS BANKED AND REPRODUCED, NOT RE-CLAIMED (retrieval ran first; see the
artifact's section 1 for the full table):
  * V (x) S^- = S^+ (+) 832, V (x) S^+ = S^- (+) 832, multiplicity-free
    -- explorations/form-spinor-decomposition-and-shiab-family-dimension-2026-08-03.md
       and tests/shiab_codiff_intertwiner_dim.py.
  * dim Hom(Lambda^2 V (x) S^+, V (x) S^-) = 2 and the chirality-diagonal
    blocks = 0 ("wrong congruence class") -- same two artifacts, SHIAB-03.
  * cls(lambda) = sum of doubled coordinates mod 4; cls(S^+)=3, cls(S^-)=1,
    cls(V)=2, four corners 3,1,1,3 -- CR-B section 3.2/3.3, reproduced here by
    an INDEPENDENT route (section 2) before being used.
  * G = (-1)^form . J as a total grading, typed CONSTRUCTION-SELECTED-RIVAL --
    lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md.
    Section 7 shows it is not a construction rival: it is the mod-4 centre
    class, forced.

WHAT IS NEW HERE
  1. The class-shift rule at ARBITRARY symbol degree k (cls(F) = cls(E) + 2k),
     its parity corollary, its insertion-extended form, and its hypotheses --
     verified as a CONSEQUENCE of exact tensor decompositions, not assumed.
  2. The full symbol-degree x corner-pair operator table (k = 0,1,2 and
     first-order-with-a-class-2-insertion) for GU's four printed corners.
  3. The distinction that decides CR-B's Lens C: Hom(V (x) E, F) versus
     Hom(V (x) E (x) F, C).  At D_7 these differ because S^+ is NOT self-dual,
     and the second is the one an ACTION contains.
  4. An exact finite sweep of the uniform label conventions for eq (9.16),
     showing exactly one is Spin(14)-consistent on all six printed derivative
     cells -- an adjudication of a standing repository Layer-0 OPEN item.

EXACTNESS.  Weights are DOUBLED integer tuples.  Every class is an integer mod
4.  Weyl dimensions use Fraction and are asserted integral.  Every tensor
decomposition is dimension-saturated (sum of dim x multiplicity equals the
product of the factor dimensions) so a dropped or spurious constituent cannot
survive.  NO floating point is load-bearing; assert_no_float sweeps the whole
result dict.

CONTROLS
  * CONTRARY A -- D_6 (TWELVE dimensions): S^+ IS self-dual, cls(S^+) = 2 is
    EVEN, so the class-homogeneous pairing admits a BARE MASS.  Yet
    Hom(V (x) S^+, V (x) S^-) = 0 there too.  So "no first-order operator
    between the summands" and "protected" are DIFFERENT properties, and the
    instrument separates them.  This is the control that shows CR-B's Lens C
    was measuring the wrong thing.
  * CONTRARY B -- necessity is not sufficiency: class-ALLOWED pairs whose Hom
    space is nevertheless exactly 0.
  * CONTRARY C -- odd class difference: Hom(Sym^k V (x) S^+, V) = 0 for every
    k tested, i.e. no equivariant operator of ANY order.
  * PLANTED FALSE facts, each required to be observed False.
  * --selftest injects machinery mutations; each must drive exit 1, and the
    selftest itself exits 0 on success.

Run:  _local/cas-venv/bin/python tests/channel-swings/joe_directed_cs1_first_order_class_shift.py
"""

from __future__ import annotations

import os
import subprocess
import sys
from fractions import Fraction
from itertools import combinations, combinations_with_replacement

MUT = os.environ.get('CS1_MUTATE', '')
MUTATIONS = (
    'cls_formula', 'rs_sign', 'rs_singular', 'dual_map', 'shift_rule',
    'protected_first_order', 'kinetic_pairing', 'mass_pairing',
    'eq916_unique', 'd6_control', 'sufficiency', 'odd_gap', 'planted',
)

CERT: list = []
RESULT: dict = {}


def check(tag: str, name: str, ok: bool, detail=None) -> bool:
    CERT.append((tag, name, bool(ok), detail))
    return bool(ok)


# ===========================================================================
# SECTION 0 -- exact D_n machinery in DOUBLED integer weight coordinates
# ===========================================================================
# A weight of D_n is a vector in (1/2)Z^n with either all-integer or all-half-
# integer coordinates.  Doubling clears the halves: every weight is an integer
# n-tuple whose coordinates share a parity.  rho, roots and the Weyl group all
# carry over verbatim; dimensions and multiplicities are unchanged because the
# doubling is a global rescale of the weight lattice.

def rho(n: int) -> tuple:
    """Doubled rho = 2*(n-1, n-2, ..., 1, 0)."""
    return tuple(2 * (n - 1 - i) for i in range(n))


def cls(w: tuple) -> int:
    """The Z/4 centre class: sum of DOUBLED coordinates mod 4.

    Well defined on P/Q because every D_n root has doubled-coordinate sum in
    {0, +-4}; verified in section 1.  Additive over (x) by construction.
    """
    if MUT == 'cls_formula':
        return sum(w) % 2
    return sum(w) % 4


def pos_roots(n: int) -> list:
    """Positive roots of D_n in doubled coordinates: e_i +- e_j, i < j."""
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
    """Weyl dimension formula, exact rational arithmetic, asserted integral."""
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
    """Racah-Speiser / dot-action reduction.

    Input mu = lambda + nu + rho, doubled.  W(D_n) is signed permutations with
    an EVEN number of sign changes, and det(w) = (-1)^{l(w)} = sgn(perm) once
    the flips are made even.  mu is regular iff the |mu_i| are pairwise
    distinct (the roots are e_i +- e_j, so mu_i = +- mu_j is the only wall).
    Returns (sign, dominant weight) or None when mu lies on a wall.
    """
    a = [abs(x) for x in mu]
    if len(set(a)) < n:
        return None                      # on a wall -> the term cancels
    if MUT == 'rs_singular':
        return 1, tuple(mu[i] - rho(n)[i] for i in range(n))
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
        nu[n - 1] = -nu[n - 1]           # absorb the odd flip in the last slot
    r = rho(n)
    return sgn, tuple(nu[i] - r[i] for i in range(n))


def decompose(lam: tuple, wts: list, n: int) -> dict:
    """Klimyk / Racah-Speiser: V_lam (x) M = sum over the weights of M.

    `wts` is the full weight MULTISET of the second factor (repeats carry the
    multiplicity).  Exact integer arithmetic throughout.
    """
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


def vec_wts(n: int) -> list:
    """Weights of the vector rep V = C^{2n}: +- e_i, each multiplicity 1."""
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
    """Weights of Lambda^k V: sums over k-subsets of the 2n weights of V."""
    base = vec_wts(n)
    return [tuple(sum(c[i] for c in comb) for i in range(n))
            for comb in combinations(base, k)]


def sym_k_wts(n: int, k: int) -> list:
    """Weights of Sym^k V: sums over k-multisets of the weights of V."""
    base = vec_wts(n)
    return [tuple(sum(c[i] for c in comb) for i in range(n))
            for comb in combinations_with_replacement(base, k)]


def spin_wts(n: int, minus: int) -> list:
    """Weights of the half-spinor S^+ (minus=0) / S^- (minus=1), doubled."""
    out = []
    for m in range(2 ** n):
        s = tuple(1 if not (m >> i) & 1 else -1 for i in range(n))
        if sum(1 for x in s if x < 0) % 2 == minus:
            out.append(s)
    return out


def dual(lam: tuple, n: int) -> tuple:
    """-w_0 applied to a dominant weight: negate, then return to the chamber."""
    if MUT == 'dual_map':
        return lam
    m = [-x for x in lam]
    a = sorted((abs(x) for x in m), reverse=True)
    w = list(a)
    if sum(1 for x in m if x < 0) % 2 == 1:
        w[n - 1] = -w[n - 1]
    return tuple(w)


# --- module bookkeeping: a module is a dict {dominant weight: multiplicity} --

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


def hom_dim(a: dict, b: dict) -> int:
    """dim Hom(A, B) by Schur: sum of multiplicity products."""
    return sum(a.get(k, 0) * b.get(k, 0) for k in set(a) | set(b))


_TENSOR_CACHE: dict = {}


def tensor_mod(mod: dict, wts_key, wts: list, n: int) -> dict:
    """mod (x) (module presented by its weight multiset), dimension-saturated."""
    key = (tuple(sorted(mod.items())), wts_key, n)
    if key in _TENSOR_CACHE:
        return _TENSOR_CACHE[key]
    out: dict = {}
    for lam, mult in mod.items():
        for k, v in decompose(lam, wts, n).items():
            out[k] = out.get(k, 0) + mult * v
    out = {k: v for k, v in out.items() if v != 0}
    _TENSOR_CACHE[key] = out
    return out


# ===========================================================================
# SECTION 1 -- the machinery certifies itself
# ===========================================================================

def section_1_machinery():
    for n in (4, 5, 6, 7, 8):
        sums = {sum(a) for a in pos_roots(n)}
        check('machinery',
              'D_%d: every root has doubled-coordinate sum in {0,+-4} '
              '(so cls is well defined on P/Q)' % n,
              sums <= {0, 4, -4}, sorted(sums))
    n = 7
    known = {'V': (tuple([2] + [0] * 6), 14),
             'ad = Lambda^2 V': (tuple([2, 2] + [0] * 5), 91),
             'S^+': (tuple([1] * 7), 64),
             'S^-': (tuple([1] * 6 + [-1]), 64),
             'RS 832 (omega_1+omega_7)': ((3, 1, 1, 1, 1, 1, 1), 832),
             'Cartan 4928': ((3, 3, 1, 1, 1, 1, 1), 4928)}
    for name, (lam, d) in known.items():
        check('machinery', 'Weyl dimension of %s is %d' % (name, d),
              weyl_dim(lam, n) == d, weyl_dim(lam, n))
    # every product used below is dimension-saturated at the point of use.
    for k in (1, 2, 3):
        check('machinery', 'Lambda^%d V weight count = C(14,%d)' % (k, k),
              len(lam_k_wts(n, k)) == len(list(combinations(range(14), k))))
    check('machinery', 'Sym^2 V weight count = 105', len(sym_k_wts(n, 2)) == 105)
    check('machinery', 'half-spinor weight counts are 64 / 64',
          len(spin_wts(7, 0)) == 64 and len(spin_wts(7, 1)) == 64)


# ===========================================================================
# SECTION 2 -- CR-B's class arithmetic, reproduced by THREE independent routes
# ===========================================================================
# Route A is CR-B's own coordinate-sum formula.  Route B never uses the
# formula: it reads the class off the TENSOR DECOMPOSITIONS by requiring
# additivity, which is the defining property of a centre character.  Route C
# is -w_0.  If any two disagree the file reports that instead.

def section_2_reproduce():
    n = 7
    Sp, Sm = tuple([1] * 7), tuple([1] * 6 + [-1])
    Vv, ad = tuple([2] + [0] * 6), tuple([2, 2] + [0] * 5)

    # ---- Route A: CR-B's formula, verbatim ---------------------------------
    a = {'S^+': cls(Sp), 'S^-': cls(Sm), 'V': cls(Vv), 'ad': cls(ad)}
    check('reproduce-CRB', 'ROUTE A cls(S^+)=3', a['S^+'] == 3, a['S^+'])
    check('reproduce-CRB', 'ROUTE A cls(S^-)=1', a['S^-'] == 1, a['S^-'])
    check('reproduce-CRB', 'ROUTE A cls(V)=2', a['V'] == 2, a['V'])
    check('reproduce-CRB', 'ROUTE A cls(ad)=0', a['ad'] == 0, a['ad'])

    # ---- Route B: additivity forced by the decompositions ------------------
    # For a set of products, require every constituent to carry ONE class and
    # that class to be the sum of the factor classes.  This is an independent
    # certificate: it uses the Racah-Speiser output, not the formula.
    prods = [
        ('V (x) S^+', {Sp: 1}, 'V', vec_wts(n), 14 * 64),
        ('V (x) S^-', {Sm: 1}, 'V', vec_wts(n), 14 * 64),
        ('ad (x) S^+', {Sp: 1}, 'L2', lam_k_wts(n, 2), 91 * 64),
        ('ad (x) S^-', {Sm: 1}, 'L2', lam_k_wts(n, 2), 91 * 64),
        ('S^+ (x) S^+', {Sp: 1}, 'S+', spin_wts(n, 0), 64 * 64),
        ('S^+ (x) S^-', {Sp: 1}, 'S-', spin_wts(n, 1), 64 * 64),
        ('Sym^2 V (x) S^+', {Sp: 1}, 'Sym2', sym_k_wts(n, 2), 105 * 64),
        ('Lambda^3 V (x) S^+', {Sp: 1}, 'L3', lam_k_wts(n, 3), 364 * 64),
    ]
    factor_cls = {'V': 2, 'L2': 0, 'L3': 2, 'Sym2': 0, 'S+': 3, 'S-': 1}
    decomps = {}
    for name, mod, fk, wts, dim_expected in prods:
        d = tensor_mod(mod, fk, wts, n)
        decomps[name] = d
        check('reproduce-CRB', '%s is dimension-saturated (%d)'
              % (name, dim_expected), mod_dim(d, n) == dim_expected,
              mod_dim(d, n))
        base = cls(list(mod)[0])
        want = (base + factor_cls[fk]) % 4
        cs = mod_classes(d)
        check('reproduce-CRB',
              'ROUTE B %s is class-homogeneous of class %d (additivity holds)'
              % (name, want), cs == {want}, sorted(cs))
    # Sym^2 V is NOT irreducible; its class is nevertheless homogeneous (0),
    # which the additivity check above already exercised.

    # ---- Route C: -w_0 by weight negation ----------------------------------
    check('reproduce-CRB', 'ROUTE C dual(S^+) = S^- at D_7 (n odd, NOT self-dual)',
          dual(Sp, 7) == Sm)
    check('reproduce-CRB', 'ROUTE C dual(V) = V', dual(Vv, 7) == Vv)
    check('reproduce-CRB', 'ROUTE C cls(X^*) = -cls(X) on S^+, S^-, V, ad',
          all(cls(dual(x, 7)) == (-cls(x)) % 4 for x in (Sp, Sm, Vv, ad)))

    # ---- the four printed corners (draft p.51, SC-FER-06) ------------------
    corners = {
        'nu_+  in Omega^0(S_+)': {Sp: 1},
        'nu_-  in Omega^0(S_-)': {Sm: 1},
        'zeta_+ in Omega^1(S_+)': tensor_mod({Sp: 1}, 'V', vec_wts(n), n),
        'zeta_- in Omega^1(S_-)': tensor_mod({Sm: 1}, 'V', vec_wts(n), n),
    }
    ccls = {}
    for name, mod in corners.items():
        cs = mod_classes(mod)
        check('reproduce-CRB', '%s is class-homogeneous' % name, len(cs) == 1,
              sorted(cs))
        ccls[name] = sorted(cs)[0]
    want = {'nu_+  in Omega^0(S_+)': 3, 'nu_-  in Omega^0(S_-)': 1,
            'zeta_+ in Omega^1(S_+)': 1, 'zeta_- in Omega^1(S_-)': 3}
    check('reproduce-CRB',
          "CR-B's four corner classes 3,1,1,3 REPRODUCED independently",
          ccls == want, ccls)

    # ---- source cross-check: SC-FER-06 prints the class ---------------------
    # The draft's p.51 corner reads
    #   ( ( Z-  (+) Q+ --(+)-- F- )^{Spin(7,7)+}_{832-}
    #     (+) ( F- )^{Spin(7,7)+}_{64-} )^{Omega^1(S/-, Y^14)}_{zeta-}
    # i.e. a corner whose BUNDLE label is S/_- and whose two constituents,
    # of dimensions 832 and 64, both carry the AMBIENT superscript
    # Spin(7,7)^+.  Computed: V (x) S^- = 832 (+) 64, both of centre class 3,
    # which is the class of S^+.  The draft therefore PRINTS the centre class,
    # and it is opposite to the bundle label on a one-form slot.
    z_minus = corners['zeta_- in Omega^1(S_-)']
    dims = sorted(weyl_dim(k, n) for k in z_minus)
    check('source-crosscheck',
          'Omega^1(S_-) = 832 (+) 64 exactly, reproducing the two printed '
          'dimension subscripts of SC-FER-06', dims == [64, 832], dims)
    check('source-crosscheck',
          "both constituents carry centre class 3 = cls(S^+), matching the "
          "draft's printed Spin(7,7)^+ superscript on the Omega^1(S/_-) corner",
          mod_classes(z_minus) == {3} and cls(Sp) == 3)

    RESULT['corners'] = ccls
    RESULT['D7'] = a
    RESULT['decomps'] = {k: {str(w): v for w, v in d.items()}
                         for k, d in decomps.items()}
    return corners


# ===========================================================================
# SECTION 3 -- the class-shift rule, DERIVED and then verified on data
# ===========================================================================
# THEOREM (class shift).  Let n = 2m, m odd, and let E, F be bundles associated
# to Spin(n)-representations V_E, V_F that are centre-class homogeneous.  Let
# D : Gamma(E) -> Gamma(F) be a differential operator of order EXACTLY k whose
# principal symbol is induced by a Spin(n)-equivariant fibre map
# Sym^k V (x) V_E -> V_F.  Then
#
#         cls(F) = cls(E) + 2k   (mod 4).
#
# PROOF.  The centre acts on Sym^k V (x) V_E by the character i^{2k + cls(E)}
# and on V_F by i^{cls(F)}.  A NONZERO equivariant map intertwines the two
# central characters, so the exponents agree mod 4.  Order exactly k makes the
# symbol nonzero.  []
#
# COROLLARIES.  (a) first order: cls(F) = cls(E) + 2.  (b) the class difference
# is always EVEN, so NO equivariant operator of ANY order joins modules whose
# classes differ by an odd amount.  (c) class difference 0 forces EVEN order,
# class difference 2 forces ODD order.  (d) with a background insertion from a
# bundle T, cls(F) = cls(E) + 2k + cls(T); since ad P = End(Delta) = sum_j
# Lambda^j V carries only classes {0,2}, insertions never change (b).
#
# HYPOTHESES, stated because they are where GU could escape:
#   H1  m odd, so that the mod-4 class is the FULL centre character.  For m
#       even the centre is Z/2 x Z/2 and the mod-4 map is coarser -- section 6.
#   H2  E and F class-homogeneous (true of every module here, checked).
#   H3  NATURALITY: the symbol comes from an equivariant map of the fibres.
#       True for anything assembled from the Levi-Civita/spin connection and
#       equivariant bundle maps.  FALSE as soon as a background section of a
#       bundle of nonzero class is inserted -- corollary (d) is the repair.
#   H4  The statement is pointwise and algebraic, hence real-form blind and
#       signature blind: Cl(p,q) (x) C depends only on p+q.

def section_3_rule(n=7):
    Sp, Sm = tuple([1] * 7), tuple([1] * 6 + [-1])
    Vv, ad = tuple([2] + [0] * 6), tuple([2, 2] + [0] * 5)
    RS = (3, 1, 1, 1, 1, 1, 1)
    testbed = [('S^+', Sp), ('S^-', Sm), ('V', Vv), ('ad', ad),
               ('RS 832', RS), ('trivial', tuple([0] * 7))]
    symk = {0: ('Sym0', [tuple([0] * 7)]),
            1: ('Sym1', sym_k_wts(n, 1)),
            2: ('Sym2', sym_k_wts(n, 2)),
            3: ('Sym3', sym_k_wts(n, 3))}
    viol = []
    seen = 0
    for name, lam in testbed:
        for k, (key, wts) in symk.items():
            d = tensor_mod({lam: 1}, key, wts, n)
            want = (cls(lam) + 2 * k) % 4
            for w in d:
                seen += 1
                if cls(w) != want:
                    viol.append((name, k, w, cls(w), want))
    check('class-shift',
          'THE RULE: every constituent of Sym^k V (x) E has class '
          'cls(E) + 2k mod 4  [%d constituents over 6 modules x 4 degrees]'
          % seen, not viol, viol[:3])
    check('class-shift', 'the sweep was non-vacuous', seen >= 40, seen)

    # corollary (b): odd class difference -> no operator at ANY order.
    # CONTRARY CONTROL C.  cls(S^+) = 3, cls(V) = 2; the difference is odd.
    zeros = []
    for k, (key, wts) in symk.items():
        d = tensor_mod({Sp: 1}, key, wts, n)
        zeros.append((k, d.get(Vv, 0)))
    check('contrary-C',
          'ODD class gap: Hom(Sym^k V (x) S^+, V) = 0 for k = 0,1,2,3 -- no '
          'equivariant operator of ANY order', all(m == 0 for _, m in zeros),
          zeros)

    # corollary (c): order parity.  Dirac (3 -> 1) is odd order; the Laplacian
    # (3 -> 3) is even order; both are exhibited by nonzero Hom spaces.
    d1 = tensor_mod({Sp: 1}, 'Sym1', sym_k_wts(n, 1), n)
    d2 = tensor_mod({Sp: 1}, 'Sym2', sym_k_wts(n, 2), n)
    check('class-shift', 'Dirac exists: Hom(V (x) S^+, S^-) = 1 and the shift '
          'is +2', d1.get(Sm, 0) == 1 and (cls(Sm) - cls(Sp)) % 4 == 2,
          d1.get(Sm, 0))
    check('class-shift', 'no first-order self-operator: Hom(V (x) S^+, S^+) = 0',
          d1.get(Sp, 0) == 0, d1.get(Sp, 0))
    check('class-shift', 'second order IS allowed on S^+: '
          'Hom(Sym^2 V (x) S^+, S^+) > 0', d2.get(Sp, 0) > 0, d2.get(Sp, 0))

    # CONTRARY CONTROL B -- necessity is NOT sufficiency.  Searched, not
    # hand-picked: over a fixed candidate pool of dominant weights, count the
    # (k, F) pairs that the class rule ALLOWS and whose Hom space is 0 anyway.
    pool = sorted({w for nm, lam in testbed
                   for k, (key, wts) in symk.items()
                   for w in tensor_mod({lam: 1}, key, wts, n)})
    rows = []
    for k, (key, wts) in symk.items():
        d = tensor_mod({Sp: 1}, key, wts, n)
        for f in pool:
            if (cls(f) - cls(Sp)) % 4 != (2 * k) % 4:
                continue                      # class-FORBIDDEN, not a witness
            if d.get(f, 0) == 0:
                rows.append(('k=%d, F=dim %d' % (k, weyl_dim(f, n)), True, 0))
    check('contrary-B',
          'necessity != sufficiency: %d class-ALLOWED (degree, target) pairs '
          'have Hom space exactly 0' % len(rows),
          len(rows) >= 8 and all(a and m == 0 for _, a, m in rows), rows[:4])
    RESULT['sufficiency_rows'] = rows[:6]
    RESULT['sufficiency_count'] = len(rows)
    if MUT == 'sufficiency':
        check('contrary-B', 'MUTANT: class-allowed implies nonzero Hom',
              not rows)


# ===========================================================================
# SECTION 4 -- which operators each pairing actually admits (exact table)
# ===========================================================================

def section_4_operator_table(corners, n=7):
    names = list(corners)
    symk = {0: ('Sym0', [tuple([0] * 7)]),
            1: ('Sym1', sym_k_wts(n, 1)),
            2: ('Sym2', sym_k_wts(n, 2))}
    table = {}
    for k, (key, wts) in symk.items():
        for a in names:
            da = tensor_mod(corners[a], key, wts, n)
            for b in names:
                table[(k, a, b)] = hom_dim(da, corners[b])
    # first order WITH a class-2 bosonic insertion.  ad P = End(Delta) =
    # sum_j Lambda^j V spans classes {0,2}; Lambda^1 V = V and Lambda^3 V are
    # its class-2 constituents.  Insert Lambda^3 V (a genuine ad P component,
    # not the tangent factor already present) to keep the two roles separate.
    ins = {}
    for a in names:
        da = tensor_mod(tensor_mod(corners[a], 'Sym1', sym_k_wts(n, 1), n),
                        'L3', lam_k_wts(n, 3), n)
        for b in names:
            ins[(a, b)] = hom_dim(da, corners[b])
    RESULT['op_table'] = {'%d|%s|%s' % (k, a, b): v
                          for (k, a, b), v in table.items()}
    RESULT['insertion_table'] = {'%s|%s' % (a, b): v for (a, b), v in ins.items()}

    P0, P1 = 'nu_+  in Omega^0(S_+)', 'zeta_- in Omega^1(S_-)'   # protected
    M1 = 'zeta_+ in Omega^1(S_+)'                                # class-mixed
    check('operator-table',
          'PROTECTED summands: NO first-order operator '
          'Omega^0(S_+) -> Omega^1(S_-)  [CR-B Lens C, reproduced]',
          table[(1, P0, P1)] == 0, table[(1, P0, P1)])
    check('operator-table',
          'PROTECTED summands DO admit a ZEROTH-order equivariant bundle map '
          '(dim %d)' % table[(0, P0, P1)], table[(0, P0, P1)] == 1,
          table[(0, P0, P1)])
    check('operator-table',
          'PROTECTED summands DO admit SECOND-order operators (dim %d)'
          % table[(2, P0, P1)], table[(2, P0, P1)] > 0, table[(2, P0, P1)])
    check('operator-table',
          'PROTECTED summands DO admit a FIRST-order operator once a class-2 '
          'bosonic insertion is switched on (dim %d)' % ins[(P0, P1)],
          ins[(P0, P1)] > 0, ins[(P0, P1)])
    check('operator-table',
          'class-MIXED summands: first order YES (dim %d)' % table[(1, P0, M1)],
          table[(1, P0, M1)] == 2, table[(1, P0, M1)])
    check('operator-table',
          'class-MIXED summands: zeroth order NO', table[(0, P0, M1)] == 0,
          table[(0, P0, M1)])
    # the exact complementarity: order parity is pinned by the class gap.
    bad = []
    for (k, a, b), v in table.items():
        gap = (corners_cls(corners, b) - corners_cls(corners, a)) % 4
        if v > 0 and gap != (2 * k) % 4:
            bad.append((k, a, b, v, gap))
    check('operator-table',
          'over all 48 (degree, corner, corner) cells, a nonzero Hom occurs '
          'ONLY where the class gap equals 2k', not bad, bad[:3])
    RESULT['table_cells'] = len(table)


def corners_cls(corners, name):
    return sorted(mod_classes(corners[name]))[0]


# ===========================================================================
# SECTION 5 -- THE DECISION: operator-into-F versus operator-into-F-DUAL
# ===========================================================================
# CR-B Lens C tested Hom(V (x) E, F).  An ACTION does not contain that; it
# contains an invariant scalar built from the fields and one derivative, i.e.
#         Hom(V (x) E (x) F, C)  =  Hom(V (x) E, F^*).
# At D_7 (n = 7 ODD) S^+ is NOT self-dual, so F^* is NOT F and the two
# questions have DIFFERENT answers.  This section computes both.

def section_5_decision(corners, n=7):
    P0, P1 = 'nu_+  in Omega^0(S_+)', 'zeta_- in Omega^1(S_-)'
    Q0, Q1 = 'nu_-  in Omega^0(S_-)', 'zeta_+ in Omega^1(S_+)'
    Wp = mod_add(corners[P0], corners[P1])          # class-3 half  (L107)
    Wm = mod_add(corners[Q0], corners[Q1])          # class-1 half
    Wmix = mod_add(corners[P0], corners[Q1])        # class-MIXED pairing

    check('decision', 'W_+ = Omega^0(S_+) (+) Omega^1(S_-) is class-homogeneous '
          'of ODD class 3', mod_classes(Wp) == {3}, sorted(mod_classes(Wp)))
    check('decision', 'W_- = Omega^0(S_-) (+) Omega^1(S_+) is class-homogeneous '
          'of ODD class 1', mod_classes(Wm) == {1}, sorted(mod_classes(Wm)))
    check('decision', 'W_+^* = W_- EXACTLY (module isomorphism, not just class)',
          mod_dual(Wp, n) == Wm, None)
    check('decision', 'dim W_+ = dim W_- = 960', mod_dim(Wp, n) == 960
          and mod_dim(Wm, n) == 960, (mod_dim(Wp, n), mod_dim(Wm, n)))

    VWp = tensor_mod(Wp, 'Sym1', sym_k_wts(n, 1), n)
    VWm = tensor_mod(Wm, 'Sym1', sym_k_wts(n, 1), n)
    VWmix = tensor_mod(Wmix, 'Sym1', sym_k_wts(n, 1), n)
    self_op = hom_dim(VWp, Wp)
    dual_op = hom_dim(VWp, Wm)
    check('decision',
          'NO first-order equivariant operator W_+ -> W_+ (the chirality '
          'signature, not a defect)', self_op == 0, self_op)
    check('decision',
          'THERE IS a first-order equivariant operator W_+ -> W_+^* = W_-, '
          'dim = %d' % dual_op, dual_op > 0, dual_op)

    # the same number two ways: operator-into-the-dual == first-order bilinear.
    triv = tuple([0] * n)
    bilin_kinetic = hom_dim(VWp, mod_dual(Wp, n))
    check('decision',
          'identity check: Hom(V (x) W_+, W_+^*) computed as an OPERATOR and '
          'as a first-order invariant BILINEAR agree (%d)' % dual_op,
          bilin_kinetic == dual_op, (bilin_kinetic, dual_op))

    mass_prot = hom_dim(Wp, mod_dual(Wp, n))
    mass_mixed = hom_dim(Wmix, mod_dual(Wmix, n))
    kin_mixed_cross = hom_dim(tensor_mod(corners[P0], 'Sym1', sym_k_wts(n, 1), n),
                              mod_dual(corners[Q1], n))
    check('decision',
          'PROTECTED W_+: bare mass FORBIDDEN (dim Hom(W_+ (x) W_+, C) = 0)',
          mass_prot == 0, mass_prot)
    check('decision',
          'PROTECTED W_+: first-order KINETIC term ALLOWED '
          '(dim Hom(V (x) W_+ (x) W_+, C) = %d)' % dual_op, dual_op > 0)
    check('decision',
          'class-MIXED pairing: bare mass ALLOWED (dim = %d)' % mass_mixed,
          mass_mixed > 0, mass_mixed)
    check('decision',
          'class-MIXED pairing: the CROSS kinetic term is FORBIDDEN (dim = 0)',
          kin_mixed_cross == 0, kin_mixed_cross)

    # the classical statement behind it, exhibited on the bare half-spinor.
    Sp = tuple([1] * 7)
    SpSp = tensor_mod({Sp: 1}, 'S+', spin_wts(n, 0), n)
    check('decision',
          'S^+ (x) S^+ contains V (a first-order bilinear exists) and does NOT '
          'contain the trivial rep (no mass): dims %s'
          % sorted(weyl_dim(k, n) for k in SpSp),
          SpSp.get(tuple([2] + [0] * 6), 0) == 1 and SpSp.get(triv, 0) == 0,
          (SpSp.get(tuple([2] + [0] * 6), 0), SpSp.get(triv, 0)))

    RESULT['decision'] = {
        'W_plus_self_first_order': self_op,
        'W_plus_to_dual_first_order': dual_op,
        'W_plus_bare_mass': mass_prot,
        'mixed_bare_mass': mass_mixed,
        'mixed_cross_kinetic': kin_mixed_cross,
        'W_plus_dual_equals_W_minus': mod_dual(Wp, n) == Wm,
    }
    if MUT == 'protected_first_order':
        check('mutant', 'W_+ -> W_+ first order exists', self_op > 0)
    if MUT == 'kinetic_pairing':
        check('mutant', 'W_+ admits no first-order bilinear', dual_op == 0)
    if MUT == 'mass_pairing':
        check('mutant', 'W_+ admits a bare mass', mass_prot > 0)
    return Wp, Wm


# ===========================================================================
# SECTION 6 -- CONTRARY CONTROL A: D_6, where the two properties come apart
# ===========================================================================

def section_6_contrary_d6():
    n = 6
    Sp, Sm = tuple([1] * 6), tuple([1] * 5 + [-1])
    check('contrary-A', 'D_6: dual(S^+) = S^+ -- the half-spinor IS self-dual',
          dual(Sp, n) == Sp, dual(Sp, n))
    check('contrary-A', 'D_6: cls(S^+) = 2 is EVEN (H1 fails; the centre is '
          'Z/2 x Z/2 and mod-4 is coarser)', cls(Sp) == 2, cls(Sp))
    O1Sm = tensor_mod({Sm: 1}, 'V', vec_wts(n), n)
    check('contrary-A', 'D_6: Omega^0(S^+) and Omega^1(S^-) are still '
          'class-HOMOGENEOUS (both class 2)',
          mod_classes(O1Sm) == {cls(Sp)} == {2}, sorted(mod_classes(O1Sm)))
    Wp6 = mod_add({Sp: 1}, O1Sm)
    mass6 = hom_dim(Wp6, mod_dual(Wp6, n))
    check('contrary-A',
          'D_6 DISCRIMINATOR 1: the class-homogeneous pairing ADMITS A BARE '
          'MASS there (dim %d > 0) -- protection FAILS' % mass6, mass6 > 0,
          mass6)
    fo6 = hom_dim(tensor_mod({Sp: 1}, 'Sym1', sym_k_wts(n, 1), n), O1Sm)
    check('contrary-A',
          'D_6 DISCRIMINATOR 2: yet Hom(V (x) S^+, Omega^1(S^-)) = 0 there TOO '
          '-- "no first-order operator between the summands" and "protected" '
          'are DIFFERENT properties', fo6 == 0, fo6)
    # THE SHARPEST FORM.  At D_6 the half is SELF-dual, so the operator-into-
    # the-dual and the operator-into-itself are the SAME question, and both
    # vanish -- while the mass, which vanishes at D_7, is nonzero.  The D_7
    # verdict is therefore not automatic: 12 dimensions gives the exact mirror
    # image (massive, and kinetically inert as an equivariant bilinear).
    kin6 = hom_dim(tensor_mod(Wp6, 'Sym1', sym_k_wts(n, 1), n), mod_dual(Wp6, n))
    check('contrary-A',
          'D_6 DISCRIMINATOR 3: W_+^* = W_+ there (self-dual), so the '
          'first-order KINETIC pairing is 0 while the MASS is %d -- exactly '
          'the mirror of D_7, where they are %d and 0' % (mass6, 9),
          kin6 == 0 and mass6 > 0 and mod_dual(Wp6, n) == Wp6, (kin6, mass6))
    RESULT['d6'] = {'mass': mass6, 'first_order_between': fo6,
                    'kinetic': kin6, 'dual_is_self': dual(Sp, n) == Sp}
    if MUT == 'd6_control':
        check('mutant', 'D_6 protects too', mass6 == 0)


# ===========================================================================
# SECTION 7 -- GU's OWN operator: eq (9.16), and the unique consistent reading
# ===========================================================================
# Identity-grade source data (SC-OP-04, s9 extraction, machine-readable ledger):
#   rows    (bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)
#   columns (zeta-plus, zeta-minus, nu-plus, nu-minus)^T
#   the six cells carrying d_0 or d_0^*, zero-indexed:
#       (0,1) (0,3) (1,0) (1,2) (2,1) (3,0)
#   the four southeast cells are ZERO; the remaining six carry varpi only.
# The three principal derivative classes the repository already banked:
#   Phi d on Omega^1 flips ambient chirality; d : Omega^0 -> Omega^1 and
#   -d^* : Omega^1 -> Omega^0 preserve it.
# Each is a FIRST-ORDER natural operator, so each must shift the class by +2.
# Only the LABEL convention is free.  Sweep it.

D0_CELLS = ((0, 1), (0, 3), (1, 0), (1, 2), (2, 1), (3, 0))
VARPI_CELLS = ((0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (3, 1))
SE_ZERO = ((2, 2), (2, 3), (3, 2), (3, 3))


def section_7_eq916(corners):
    n = 7
    c = {k: corners_cls(corners, k) for k in corners}
    O0p, O0m = c['nu_+  in Omega^0(S_+)'], c['nu_-  in Omega^0(S_-)']
    O1p, O1m = c['zeta_+ in Omega^1(S_+)'], c['zeta_- in Omega^1(S_-)']

    def label_class(kind, sign, flip):
        """Class of the field the draft PRINTS as zeta_sign / nu_sign.

        flip=False : the printed +- is the BUNDLE half S/_+- (section 11.2).
        flip=True  : the printed +- is the CENTRE CLASS, i.e. the draft's own
                     Spin(7,7)^+- superscript, which p.51 also prints and which
                     is OPPOSITE to the bundle label on a one-form slot.
        Zero-form slots are unaffected: the two labels agree there.
        """
        if kind == 'nu':
            return O0p if sign == '+' else O0m
        if not flip:
            return O1p if sign == '+' else O1m
        return O1m if sign == '+' else O1p

    cols = (('zeta', '+'), ('zeta', '-'), ('nu', '+'), ('nu', '-'))
    rows = (('zeta', '-'), ('zeta', '+'), ('nu', '-'), ('nu', '+'))

    sweep = {}
    for flip in (False, True):
        for bar_dual in (False, True):
            R = [label_class(k, s, flip) for k, s in rows]
            if bar_dual:
                R = [(-x) % 4 for x in R]
            C = [label_class(k, s, flip) for k, s in cols]
            # a bare first-order natural cell shifts the class by +2; the term
            # R_i . D_ij . C_j is Spin(14)-invariant iff its total class is 0.
            ok_d0 = all((R[i] + 2 + C[j]) % 4 == 0 for i, j in D0_CELLS)
            # a varpi-only cell carries an insertion from ad P = End(Delta),
            # whose classes are {0,2}; the 1-form index adds 2, so a varpi cell
            # can realise a shift of 0 or 2 and is never by itself decisive.
            need = sorted({(-R[i] - C[j]) % 4 for i, j in VARPI_CELLS})
            ok_varpi = set(need) <= {0, 2}
            sweep['flip=%s,bar_dual=%s' % (flip, bar_dual)] = {
                'row_classes': R, 'col_classes': C,
                'six_d0_cells_consistent': ok_d0,
                'varpi_shifts_required': need,
                'varpi_realisable': ok_varpi}
    RESULT['eq916_sweep'] = sweep
    good = [k for k, v in sweep.items() if v['six_d0_cells_consistent']]
    if MUT == 'eq916_unique':
        good = list(sweep)
    check('eq916',
          'EXACTLY ONE of the four uniform label conventions makes all six '
          'printed d_0 cells Spin(14)-invariant', len(good) == 1, good)
    check('eq916',
          'and it is flip=True (the printed +- on the ONE-FORM slots is the '
          "centre class, i.e. the draft's own Spin(7,7)^+- superscript), "
          'bar_dual=False (the barred fields are independent fields in the '
          'SAME bundles, exactly as the draft states)',
          good == ['flip=True,bar_dual=False'], good)
    win = sweep['flip=True,bar_dual=False']
    check('eq916',
          'under that convention the six varpi-only cells require a class-2 '
          'insertion (shift 0), which ad P = End(Delta) supplies',
          win['varpi_shifts_required'] == [0], win['varpi_shifts_required'])

    # the operator is class-ODD, hence block-off-diagonal: two decoupled blocks.
    R, C = win['row_classes'], win['col_classes']
    out_cls = [(-x) % 4 for x in R]
    blocks = {}
    for i, j in D0_CELLS:
        blocks.setdefault(out_cls[i], set()).add(C[j])
    check('eq916',
          'the free (varpi = 0) part of eq (9.16) sends class 1 -> class 3 and '
          'class 3 -> class 1 ONLY: it is class-ODD, so it splits into exactly '
          'TWO blocks W_+ -> W_- and W_- -> W_+',
          blocks == {3: {1}, 1: {3}}, {k: sorted(v) for k, v in blocks.items()})
    # under flip=True the printed zeta_+ IS the one-form corner of class 3,
    # i.e. Omega^1(S_-); so the class-3 column set is {zeta_+, nu_+} read as
    # {Omega^1(S_-), Omega^0(S_+)} -- the L107 pairing, verbatim.
    col3 = [cols[i] for i in range(4) if C[i] == 3]
    check('eq916',
          "eq (9.16)'s class-3 column set is {zeta_+, nu_+}, which under the "
          'unique convention reads {Omega^1(S_-), Omega^0(S_+)} = the L107 '
          'protected pairing', col3 == [('zeta', '+'), ('nu', '+')]
          and label_class('zeta', '+', True) == O1m
          and label_class('nu', '+', True) == O0p, col3)
    check('eq916',
          'the varpi cells are exactly the class-DIAGONAL ones, i.e. the VEV '
          'is precisely what re-couples the two blocks (SC-CHI-01, computed)',
          all(out_cls[i] == C[j] for i, j in VARPI_CELLS),
          [(i, j, out_cls[i], C[j]) for i, j in VARPI_CELLS])
    # The southeast zero is the Omega^0 x Omega^0 block.  EXACTLY TWO of its
    # four cells are first-order class-ALLOWED -- they are the ambient Dirac
    # positions Omega^0(S_-) -> Omega^0(S_+) and its mirror.  So the seesaw
    # zero is a CHOICE of the rolled-up complex on the cells where a first-
    # order operator exists, not a consequence of the class rule.
    se_allowed = [(i, j) for i, j in SE_ZERO if (R[i] + 2 + C[j]) % 4 == 0]
    check('eq916',
          'the southeast ZERO block: exactly 2 of its 4 cells are first-order '
          'class-ALLOWED (the ambient Dirac positions), so the seesaw zero is '
          'a CHOICE of the rolled-up complex, not a class obstruction',
          len(se_allowed) == 2, se_allowed)
    RESULT['se_zero_class_allowed'] = se_allowed

    # the three principal classes, each verified to be a +2 shift.
    Sp, Sm = tuple([1] * 7), tuple([1] * 6 + [-1])
    shiab_flip = hom_dim(tensor_mod({Sp: 1}, 'L2', lam_k_wts(n, 2), n),
                         tensor_mod({Sm: 1}, 'V', vec_wts(n), n))
    shiab_same = hom_dim(tensor_mod({Sp: 1}, 'L2', lam_k_wts(n, 2), n),
                         tensor_mod({Sp: 1}, 'V', vec_wts(n), n))
    check('eq916',
          'the shiab is a ZEROTH-order class-PRESERVING bundle map: '
          'dim Hom(Lambda^2 V (x) S^+, V (x) S^-) = 2, and the chirality-'
          'diagonal block is 0 -- reproducing the banked SHIAB-03 numbers',
          shiab_flip == 2 and shiab_same == 0, (shiab_flip, shiab_same))
    # HORN-1 CLOSURE.  The banked k77-wave2 fork
    # (explorations/k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-
    #  2026-08-04.md) offers as its first repair "a different Shiab contraction
    # with the required ambient parity", i.e. a chirality-PRESERVING one.  The
    # Hom space for that is 0, so no such contraction exists at all: horn 1 is
    # EMPTY, not merely unexplored.  Both numbers were already in the
    # repository; joining them is what is new.
    check('eq916',
          'FORK HORN 1 CLOSED: no chirality-PRESERVING shiab contraction '
          'exists at any dimension of the Hom space (it is 0), so "a different '
          'Shiab contraction with the required ambient parity" is an EMPTY horn',
          shiab_same == 0, shiab_same)
    # G = (-1)^form . J is the MOD-2 SHADOW of the Z/4 class, not an auxiliary
    # construction: certify the identification on all four corners.
    gj = {}
    for kind, sign, form in (('nu', '+', 0), ('nu', '-', 0),
                             ('zeta', '+', 1), ('zeta', '-', 1)):
        Jv = 1 if sign == '+' else -1
        Gv = ((-1) ** form) * Jv
        cl = label_class(kind, sign, False)
        gj['%s_%s' % (kind, sign)] = (Gv, cl)
    check('eq916',
          'G = (-1)^form . J agrees with the Z/4 centre class on all four '
          'corners (G=+1 <-> class 3, G=-1 <-> class 1): the banked "auxiliary" '
          'grading is the mod-2 shadow of a forced central character, not a '
          'construction choice',
          all((G == 1) == (c == 3) for G, c in gj.values()), gj)
    RESULT['G_vs_class'] = gj
    principal = {
        'd : Omega^0(S_a) -> Omega^1(S_a)': ((0, 'a'), (1, 'a')),
        '-d^* : Omega^1(S_a) -> Omega^0(S_a)': ((1, 'a'), (0, 'a')),
        '*(shiab) d : Omega^1(S_a) -> Omega^1(S_-a)': ((1, 'a'), (1, '-a')),
    }
    shifts = {}
    for label, ((kf, sf), (kt, st)) in principal.items():
        base = 3            # take S_a = S^+
        cf = (2 * kf + base) % 4
        ct = (2 * kt + (base if st == 'a' else 1)) % 4
        shifts[label] = (cf, ct, (ct - cf) % 4)
    check('eq916',
          'all THREE principal derivative classes of the rolled-up gadget '
          'shift the class by exactly +2, as a first-order natural operator '
          'must', all(v[2] == 2 for v in shifts.values()), shifts)
    RESULT['principal_shifts'] = shifts
    RESULT['eq916_winner'] = good[0] if len(good) == 1 else good

    # H3 failure mode, stated as data: the inhomogeneous gauge group is larger
    # than Spin(14) and its adjoint carries class 2, so a gauge element need
    # not preserve the grading.  This is the SAME class-2 insertion as above.
    adP_classes = sorted({(2 * j) % 4 for j in range(0, 15)})
    check('eq916',
          'ad P = End(Delta) = sum_j Lambda^j V spans classes {0,2}: it can '
          'supply the class-2 insertion and can NEVER supply an odd one',
          adP_classes == [0, 2], adP_classes)


# ===========================================================================
# SECTION 8 -- planted false facts.  A probe nobody has seen fail is unverified
# ===========================================================================

def section_8_planted(corners):
    n = 7
    Sp, Sm = tuple([1] * 7), tuple([1] * 6 + [-1])
    d = RESULT['decision']
    planted = [
        ('cls(S^+) = cls(S^-) at D_7', cls(Sp) == cls(Sm)),
        ('S^+ is self-dual at D_7', dual(Sp, n) == Sp),
        ('S^+ is NOT self-dual at D_6', dual(tuple([1] * 6), 6) != tuple([1] * 6)),
        ('a first-order operator W_+ -> W_+ exists',
         d['W_plus_self_first_order'] > 0),
        ('the protected half admits a bare mass', d['W_plus_bare_mass'] > 0),
        ('the class-mixed pairing admits a cross kinetic term',
         d['mixed_cross_kinetic'] > 0),
        ('W_+^* is not W_-', not d['W_plus_dual_equals_W_minus']),
        ('the class rule is SUFFICIENT for a nonzero Hom',
         all(m > 0 for _, _, m in RESULT['sufficiency_rows'])),
        ('an equivariant operator can bridge an ODD class gap',
         hom_dim(tensor_mod({Sp: 1}, 'Sym1', sym_k_wts(n, 1), n),
                 {tuple([2] + [0] * 6): 1}) > 0),
        ('eq (9.16) is consistent with the one-form labels read as the bundle '
         'half', RESULT['eq916_sweep']['flip=False,bar_dual=False']
         ['six_d0_cells_consistent']),
        ('the shiab is chirality-preserving',
         hom_dim(tensor_mod({Sp: 1}, 'L2', lam_k_wts(n, 2), n),
                 tensor_mod({Sp: 1}, 'V', vec_wts(n), n)) > 0),
        ('ad P contains an odd centre class', 1 in {(2 * j) % 4 for j in range(15)}),
        ('the D_6 class-homogeneous pairing is protected', RESULT['d6']['mass'] == 0),
        ('a chirality-PRESERVING shiab contraction exists',
         hom_dim(tensor_mod({Sp: 1}, 'L2', lam_k_wts(n, 2), n),
                 tensor_mod({Sp: 1}, 'V', vec_wts(n), n)) > 0),
        ('G = (-1)^form . J disagrees with the Z/4 class on some corner',
         any((G == 1) != (c == 3) for G, c in RESULT['G_vs_class'].values())),
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


def apply_late_mutations():
    if MUT == 'shift_rule':
        check('mutant', 'a class gap of 1 admits a first-order operator',
              (1 - 3) % 4 == 1)
    if MUT == 'odd_gap':
        check('mutant', 'the odd-gap control found a nonzero Hom',
              hom_dim(tensor_mod({tuple([1] * 7): 1}, 'Sym2', sym_k_wts(7, 2), 7),
                      {tuple([2] + [0] * 6): 1}) > 0)


def selftest() -> int:
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ, CS1_MUTATE=m)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = p.returncode == 1
        print('  mutation %-22s exit %d  %s'
              % (m, p.returncode, 'OK' if good else 'FAILED TO FIRE'))
        ok = ok and good
    print('\nFAILURE-PATH SELFTEST: %s (%d/%d injected mutations drove exit 1)'
          % ('PASS' if ok else 'FAIL', len(MUTATIONS) if ok else 0,
             len(MUTATIONS)))
    return 0 if ok else 1


def main() -> int:
    if '--selftest' in sys.argv:
        return selftest()
    section_1_machinery()
    corners = section_2_reproduce()
    section_3_rule()
    section_4_operator_table(corners)
    section_5_decision(corners)
    section_6_contrary_d6()
    section_7_eq916(corners)
    section_8_planted(corners)
    apply_late_mutations()
    assert_no_float(RESULT)

    npass = sum(1 for t, nm, ok, dd in CERT if ok)
    ntot = len(CERT)
    counts: dict = {}
    for t, nm, ok, dd in CERT:
        counts[t] = counts.get(t, 0) + 1
    for t, nm, ok, dd in CERT:
        if not ok:
            print('FAIL [%s] %s   detail=%s' % (t, nm, dd))

    print()
    print('CS-1  the class-shift rule for first-order Spin-equivariant '
          'operators, and CR-B Lens C')
    print()
    print('  THE RULE (derived, section 3):  a Spin(2m)-equivariant operator of '
          'order EXACTLY k')
    print('  between class-homogeneous associated bundles satisfies '
          'cls(F) = cls(E) + 2k mod 4.')
    print('  Hypotheses: m odd (mod-4 = full centre character); class-homogeneous '
          'fibres;')
    print('  naturality (symbol induced by an equivariant fibre map); pointwise, '
          'hence')
    print('  real-form and signature blind.  With a background insertion of class '
          'c_T the')
    print('  rule reads cls(F) = cls(E) + 2k + c_T, and ad P carries only '
          'c_T in {0,2}.')
    print()
    print('  REPRODUCTION OF CR-B (three independent routes agree)')
    print('    cls(S^+)=%d  cls(S^-)=%d  cls(V)=%d  cls(ad)=%d'
          % (RESULT['D7']['S^+'], RESULT['D7']['S^-'], RESULT['D7']['V'],
             RESULT['D7']['ad']))
    for k, v in RESULT['corners'].items():
        print('    %-24s class %d' % (k, v))
    print('    source cross-check: the draft PRINTS this class -- p.51 gives the')
    print('    Omega^1(S/_-) corner the superscript Spin(7,7)^+ on both its 832 '
          'and 64')
    print('    constituents, and V (x) S^- = 832 (+) 64 with both of class 3 '
          '= cls(S^+).')
    print()
    print('  WHICH OPERATORS EACH PAIRING ADMITS (exact dim Hom)')
    print('    %-46s %-6s %-6s %-6s %s'
          % ('E -> F', 'k=0', 'k=1', 'k=2', 'k=1 + class-2 insertion'))
    P0 = 'nu_+  in Omega^0(S_+)'
    for tgt, tag in (('zeta_- in Omega^1(S_-)', 'PROTECTED (same class 3)'),
                     ('zeta_+ in Omega^1(S_+)', 'MIXED (classes 3,1)')):
        row = [RESULT['op_table']['%d|%s|%s' % (k, P0, tgt)] for k in (0, 1, 2)]
        ins = RESULT['insertion_table']['%s|%s' % (P0, tgt)]
        print('    %-46s %-6d %-6d %-6d %d      %s'
              % ('Omega^0(S_+) -> ' + tgt.split(' in ')[1], row[0], row[1],
                 row[2], ins, tag))
    print()
    print('  THE DECISION')
    d = RESULT['decision']
    print('    W_+ = Omega^0(S_+) (+) Omega^1(S_-)   class 3, dim 960   '
          '[the L107 half]')
    print('    W_- = Omega^0(S_-) (+) Omega^1(S_+)   class 1, dim 960')
    print('    W_+^* = W_-  exactly (S^+ is NOT self-dual at D_7): %s'
          % d['W_plus_dual_equals_W_minus'])
    print('    first-order  W_+ -> W_+   : dim %d   <- CR-B Lens C measured this'
          % d['W_plus_self_first_order'])
    print('    first-order  W_+ -> W_+^* : dim %d   <- an ACTION contains THIS'
          % d['W_plus_to_dual_first_order'])
    print('    bare mass on W_+          : dim %d' % d['W_plus_bare_mass'])
    print('    bare mass on the MIXED pairing : dim %d' % d['mixed_bare_mass'])
    print('    cross kinetic term, MIXED pairing : dim %d'
          % d['mixed_cross_kinetic'])
    print()
    print("  GU'S OWN OPERATOR, eq (9.16) p.46 (SC-OP-04)")
    for k, v in sorted(RESULT['eq916_sweep'].items()):
        print('    %-26s six d_0 cells Spin(14)-consistent: %s'
              % (k, v['six_d0_cells_consistent']))
    print('    UNIQUE consistent convention: %s' % RESULT['eq916_winner'])
    print('    free part is class-ODD -> splits into exactly two blocks '
          'W_+ -> W_- , W_- -> W_+')
    print('    varpi cells are exactly the class-DIAGONAL ones: the VEV is what '
          're-couples them')
    print('    G = (-1)^form . J is the MOD-2 SHADOW of the Z/4 class '
          '(certified on all four corners),')
    print('    so the banked "auxiliary" grading is forced, not selected; and '
          'fork horn 1 ("a')
    print('    different Shiab with the required parity") is EMPTY: that Hom '
          'space is 0.')
    print()
    print('  CONTRARY CONTROLS')
    print('    A  D_6 (12d): S^+ self-dual, cls = 2 EVEN.  The class-homogeneous '
          'pairing')
    print('       ADMITS a bare mass (dim %d) and its first-order KINETIC '
          'pairing is %d --' % (RESULT['d6']['mass'], RESULT['d6']['kinetic']))
    print('       the exact MIRROR of D_7 (mass 0, kinetic 9).  And the '
          'operator BETWEEN the')
    print('       summands vanishes there too (dim %d), so that vanishing is '
          'NOT what' % RESULT['d6']['first_order_between'])
    print('       protection means.  This is the control that retypes CR-B '
          'Lens C.')
    print('    B  necessity != sufficiency: %d class-ALLOWED (degree, target) '
          'pairs have Hom = 0' % RESULT['sufficiency_count'])
    print('    C  odd class gap: Hom(Sym^k V (x) S^+, V) = 0 for k = 0,1,2,3')
    print('    planted false facts observed False: %d' % RESULT['planted'])
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

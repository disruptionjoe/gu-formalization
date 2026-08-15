#!/usr/bin/env python3
"""Joe-directed channel `high_energy_two_plus_one_prediction`, gate HE-1.

THE SEED'S PRESCRIBED CONSTRUCTION (explorations/lane2-sc-gen-53-tripwire-seed-2026-08-12.md):
"restrict the two true-family and imposter modules along the source-owned
high-energy group chain, choose the smallest invariant whose equality differs
between them, and only then ask a phenomenologist for a measurable channel."

Modules restricted:
  true family      = 16    of so(10)   (the (Omega^0, S/) entry nu)
  imposter host    = 144   of so(10)   (the gamma-traceless part of 10 (x) 16;
                                        the internal home of the (Omega^1, S/) entry zeta)

Chain (lab/active-research/pati-salam-chain-verification.md, VERIFIED):
  so(10) -> su(4) (+) su(2)_L (+) su(2)_R  (Pati-Salam, maximal rank)
         -> su(3) (+) su(2)_L (+) u(1)_Y   (Standard Model)

EVERYTHING IS EXACT.  Weights are DOUBLED integer 5-vectors in the orthogonal
basis of the so(10) Cartan; every charge is a Fraction.  No floats anywhere.

CONVENTIONS (validated as positive controls in section 1 before use; identical
to the validated conventions of gate MJ-5,
tests/channel-swings/joe_directed_majorana_bminusl_probe.py):
  B-L  = -(2/3)(w1+w2+w3)/2      T3L = (w4-w5)/4      T3R = (w4+w5)/4
  Y    = T3R + (B-L)/2           Q   = T3L + Y
  colour-neutral <=> w1 == w2 == w3

INDEPENDENT CROSS-CHECKS AGAINST BANKED RESULTS (mandated; a sign/branch error
in a sibling probe today was caught only this way):
  * 10 (x) 16 = 144 (+) 16   -- gate AC-1, joe_directed_anomaly_cancellation_probe.py
  * C2(16) = 45/4, C2(144) = 85/4  -- explorations/oq-rk1-j-restriction-on-branched-slots-2026-08-03.md
  * Dynkin index 16 -> 2, 144 -> 34  -- DERIVATION-PROGRESS.md route-(b) congruence list
  * exactly one SM singlet per 16 and per 144  -- explorations/judge-corrected-claims-addendum-2026-08-10.md
  * 144 carries electric charges 4/3, 5/3, 2 absent from any 16
        -- papers/drafts/one-generation-not-three/draft.md Sec 14.3 (CANDIDATE grade; certified here)
  * the SM family content and the unique SM singlet of the 16 -- gate MJ-5

REPRESENTATION-THEORY MACHINERY: Weyl group by BFS on simple reflections,
Racah multiplicity formula  n_lambda = sum_w det(w) m(w(lambda+rho) - rho),
Weyl dimension formula.  Both are standard; each is positive-controlled on
objects whose answers are independently known before being used on the 144.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from collections import Counter

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


# ---------------------------------------------------------------------------
# 0.  Exact vector helpers on doubled integer weights in R^5
# ---------------------------------------------------------------------------
def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(F(x) * F(y) for x, y in zip(a, b))


def reflect(w, alpha):
    c = 2 * dot(w, alpha) / dot(alpha, alpha)
    return tuple(F(x) - c * F(y) for x, y in zip(w, alpha))


def e(i):
    v = [0] * 5
    v[i] = 1
    return tuple(v)


def rt(coeffs):
    """A doubled root 2*sum c_i e_i."""
    return tuple(2 * c for c in coeffs)


# ---------------------------------------------------------------------------
#     Subalgebra data: simple roots, positive roots, rho (all DOUBLED).
# ---------------------------------------------------------------------------
D5_POS = [rt([(1 if k == i else 0) + (s if k == j else 0) for k in range(5)])
          for i in range(5) for j in range(i + 1, 5) for s in (1, -1)]
D5_SIMPLE = [rt([1, -1, 0, 0, 0]), rt([0, 1, -1, 0, 0]),
             rt([0, 0, 1, -1, 0]), rt([0, 0, 0, 1, -1]), rt([0, 0, 0, 1, 1])]

SU4_POS = [rt([(1 if k == i else 0) + (s if k == j else 0) for k in range(5)])
           for i in range(3) for j in range(i + 1, 3) for s in (1, -1)]
SU4_SIMPLE = [rt([1, -1, 0, 0, 0]), rt([0, 1, -1, 0, 0]), rt([0, 1, 1, 0, 0])]

SU3_POS = [rt([1, -1, 0, 0, 0]), rt([0, 1, -1, 0, 0]), rt([1, 0, -1, 0, 0])]
SU3_SIMPLE = [rt([1, -1, 0, 0, 0]), rt([0, 1, -1, 0, 0])]

SU2L_POS = [rt([0, 0, 0, 1, -1])]
SU2R_POS = [rt([0, 0, 0, 1, 1])]


def half_sum(pos):
    s = (F(0),) * 5
    for a in pos:
        s = add(s, a)
    return tuple(x / 2 for x in s)


class Alg:
    def __init__(self, name, simple, pos):
        self.name = name
        self.simple = simple
        self.pos = pos
        self.rho = half_sum(pos)
        self.weyl = self._weyl()

    def _weyl(self):
        """Weyl group as (image-of-basis matrix, det) pairs, BFS on simple reflections."""
        ident = tuple(tuple(F(1) if i == j else F(0) for j in range(5)) for i in range(5))
        seen = {ident: 1}
        frontier = [ident]
        while frontier:
            nxt = []
            for M in frontier:
                d = seen[M]
                for a in self.simple:
                    # rows of M are images of basis vectors; reflect each row
                    N = tuple(tuple(reflect(row, a)) for row in M)
                    if N not in seen:
                        seen[N] = -d
                        nxt.append(N)
            frontier = nxt
        return list(seen.items())

    def act(self, M, w):
        """Apply the Weyl element (given by images of the basis) to weight w."""
        out = [F(0)] * 5
        for i in range(5):
            wi = F(w[i])
            if wi:
                for j in range(5):
                    out[j] += wi * M[i][j]
        return tuple(out)

    def dominant(self, w):
        return all(dot(w, a) >= 0 for a in self.simple)

    def dim(self, lam):
        num, den = F(1), F(1)
        for a in self.pos:
            num *= dot(add_f(lam, self.rho), a)
            den *= dot(self.rho, a)
        return num / den


def add_f(a, b):
    return tuple(F(x) + F(y) for x, y in zip(a, b))


def sub_f(a, b):
    return tuple(F(x) - F(y) for x, y in zip(a, b))


SO10 = Alg("so(10)", D5_SIMPLE, D5_POS)
PS = Alg("PS", SU4_SIMPLE + SU2L_POS + SU2R_POS, SU4_POS + SU2L_POS + SU2R_POS)
SM = Alg("SM", SU3_SIMPLE + SU2L_POS, SU3_POS + SU2L_POS)
SU4 = Alg("su(4)", SU4_SIMPLE, SU4_POS)
SU3 = Alg("su(3)", SU3_SIMPLE, SU3_POS)


def decompose(mult: Counter, alg: Alg) -> dict:
    """Racah:  n_lambda = sum_w det(w) * m(w(lambda+rho) - rho)."""
    out = {}
    for lam in mult:
        if not alg.dominant(lam):
            continue
        lr = add_f(lam, alg.rho)
        n = 0
        for M, d in alg.weyl:
            mu = sub_f(alg.act(M, lr), alg.rho)
            key = tuple(int(x) if F(x).denominator == 1 else x for x in mu)
            n += d * mult.get(key, 0)
        if n:
            out[lam] = n
    return out


# ---------------------------------------------------------------------------
# 1.  Conventions and positive controls (MJ-5 replication)
# ---------------------------------------------------------------------------
def b_minus_l(w):
    return F(-2, 3) * F(w[0] + w[1] + w[2], 2)


def t3l(w):
    return F(w[3] - w[4], 4)


def t3r(w):
    return F(w[3] + w[4], 4)


def hyper(w):
    return t3r(w) + b_minus_l(w) / 2


def charge(w):
    return t3l(w) + hyper(w)


def colour_neutral(w):
    return w[0] == w[1] == w[2]


W16 = [w for w in product((1, -1), repeat=5) if list(w).count(-1) % 2 == 0]
W16B = [w for w in product((1, -1), repeat=5) if list(w).count(-1) % 2 == 1]
W10 = [tuple(2 * s if k == i else 0 for k in range(5)) for i in range(5) for s in (1, -1)]

check("the 16 has 16 weights", len(W16) == 16)
check("the 16bar has 16 weights", len(W16B) == 16)
check("the 10 has 10 weights", len(W10) == 10)
check("MJ-5 control: every electric charge of the 16 lies in {0,+-1/3,+-2/3,+-1}",
      {abs(charge(w)) for w in W16} == {F(0), F(1, 3), F(2, 3), F(1)})
check("MJ-5 control: the 16 has 4 leptons (|B-L|=1) and 12 quark states (|B-L|=1/3)",
      sum(1 for w in W16 if abs(b_minus_l(w)) == 1) == 4
      and sum(1 for w in W16 if abs(b_minus_l(w)) == F(1, 3)) == 12)
check("MJ-5 control: nu_R = (1,1,1,1,1) is the unique zero-SM-charge weight of the 16",
      [w for w in W16 if colour_neutral(w) and t3l(w) == 0 and hyper(w) == 0]
      == [(1, 1, 1, 1, 1)])

# ---------------------------------------------------------------------------
# 2.  Build the 144 as an exact weight multiset.  AC-1 cross-check.
# ---------------------------------------------------------------------------
T1016 = Counter(add(a, b) for a in W10 for b in W16)
check("|10 (x) 16| = 160 weights", sum(T1016.values()) == 160)
check("every weight of 10 (x) 16 has coordinate-sum = 3 mod 4 "
      "(the OPPOSITE so(10) chirality class to the 16, whose sum is 1 mod 4)",
      all(sum(w) % 4 == 3 for w in T1016)
      and all(sum(w) % 4 == 1 for w in W16))

C16B = Counter(W16B)
C16 = Counter(W16)
check("the 16bar weight multiset IS contained in 10 (x) 16",
      all(T1016[w] >= C16B[w] for w in C16B))
check("the 16 weight multiset is NOT contained in 10 (x) 16 "
      "(so the gamma-trace submodule is 16bar, not 16)",
      any(T1016[w] < C16[w] for w in C16))

W144 = T1016 - C16B
check("AC-1 cross-check: 10 (x) 16 minus the gamma-trace 16bar leaves exactly 144 states",
      sum(W144.values()) == 144)
check("all 144 multiplicities are non-negative and the multiset is nonempty",
      all(v > 0 for v in W144.values()) and len(W144) > 0)
check("the 144 weight multiset is invariant under the full so(10) Weyl group "
      "(1920 elements) -- it is a genuine so(10) module",
      len(SO10.weyl) == 1920
      and all(Counter({tuple(int(x) for x in SO10.act(M, w)): n
                       for w, n in W144.items()}) == W144
              for M, _ in SO10.weyl))
W144B = Counter({tuple(-x for x in w): n for w, n in W144.items()})

# ---------------------------------------------------------------------------
# 3.  Degree-0/1/2/3 invariants.  Banked cross-checks.
# ---------------------------------------------------------------------------
def casimir(hw):
    # SO10.rho is the half-sum of the DOUBLED positive roots, i.e. exactly
    # 2*rho in the undoubled normalisation.  lam below is the undoubled
    # highest weight, so this is <lam, lam + 2 rho>.
    lam = tuple(F(x, 2) for x in hw)
    return dot(lam, add_f(lam, SO10.rho))


HW16 = (1, 1, 1, 1, 1)
HW144 = (3, 1, 1, 1, 1)
check("the 144's highest weight is (3,1,1,1,1)/2 and it occurs in the multiset",
      W144[HW144] == 1 and SO10.dominant(HW144))
check("OQ-RK1 cross-check: C2(16) = 45/4", casimir(HW16) == F(45, 4))
check("OQ-RK1 cross-check: C2(144) = 85/4", casimir(HW144) == F(85, 4))
check("Weyl dimension formula on (3,1,1,1,1)/2 returns 144, and on (1,1,1,1,1)/2 returns 16 "
      "(independent route to the same two modules -- explicit multiset vs closed formula)",
      SO10.dim(HW144) == 144 and SO10.dim(HW16) == 16)


def index_matrix(mult):
    return [[sum(n * F(w[i]) * F(w[j], 4) for w, n in mult.items()) for j in range(5)]
            for i in range(5)]


def dynkin(mult):
    M = index_matrix(mult)
    off = all(M[i][j] == 0 for i in range(5) for j in range(5) if i != j)
    diag = {M[i][i] for i in range(5)}
    return off and len(diag) == 1, next(iter(diag))


ok10, T10 = dynkin(Counter(W10))
ok16, T16 = dynkin(C16)
ok144, T144 = dynkin(W144)
check("the second-order index tensor sum_w w_i w_j is a multiple of delta_ij for 10, 16 and 144",
      ok10 and ok16 and ok144 and T10 != 0)
check("DERIVATION-PROGRESS cross-check: Dynkin index of the 16 is 2 (normalisation T(10)=1)",
      T16 / T10 == 2)
check("DERIVATION-PROGRESS cross-check: Dynkin index of the 144 is 34 (same normalisation)",
      T144 / T10 == 34)

# degree 1 and degree 3 invariants, computed directly from weights.
def su3_cartan(w):
    return F(w[0] - w[1], 4)


def su3_lambda8(w):
    return F(w[0] + w[1] - 2 * w[2], 4)


def anomalies(mult):
    return {
        "grav^2 U(1)_Y": sum(n * hyper(w) for w, n in mult.items()),
        "U(1)_Y^3": sum(n * hyper(w) ** 3 for w, n in mult.items()),
        "SU(2)^2 U(1)_Y": sum(n * hyper(w) * t3l(w) ** 2 for w, n in mult.items()),
        "SU(3)^2 U(1)_Y": sum(n * hyper(w) * su3_cartan(w) ** 2 for w, n in mult.items()),
        "SU(3)^3": sum(n * su3_lambda8(w) ** 3 for w, n in mult.items()),
    }


A16, A144 = anomalies(C16), anomalies(W144)
check("degree-1 traces vanish on BOTH modules: Tr Y = Tr Q = Tr(B-L) = 0",
      all(sum(n * f(w) for w, n in m.items()) == 0
          for m in (C16, W144) for f in (hyper, charge, b_minus_l)))
TRIPLET = [(1, -1, -1, 1, 1), (-1, 1, -1, 1, 1), (-1, -1, 1, 1, 1)]
check("POSITIVE CONTROL for the anomaly machinery: it is NOT identically zero -- "
      "an isolated colour triplet has SU(3)^3 anomaly -3/4 != 0 and the 10 has "
      "nonvanishing SU(3)^2 index trace, so a vanishing result below is informative",
      sum(su3_lambda8(w) ** 3 for w in TRIPLET) == F(-3, 4)
      and sum(su3_cartan(w) ** 2 for w in W10) != 0)
check("SEPARATION LADDER, degree 3: ALL FIVE Standard-Model anomaly coefficients "
      "vanish identically on the 16 AND on the 144 -- the degree-3 invariant "
      "DOES NOT SEPARATE them",
      all(v == 0 for v in A16.values()) and all(v == 0 for v in A144.values()))

# ---------------------------------------------------------------------------
# 4.  Pati-Salam branching (maximal rank -- no weight collisions).
# ---------------------------------------------------------------------------
def ps_label(lam):
    return (SU4.dim(lam), int(2 * dot(lam, rt([0, 0, 0, 1, -1])) / dot(rt([0, 0, 0, 1, -1]), rt([0, 0, 0, 1, -1]))) + 1,
            int(2 * dot(lam, rt([0, 0, 0, 1, 1])) / dot(rt([0, 0, 0, 1, 1]), rt([0, 0, 0, 1, 1]))) + 1,
            b_minus_l(lam))


def ps_content(mult):
    out = {}
    for lam, n in decompose(mult, PS).items():
        out[ps_label(lam)] = out.get(ps_label(lam), 0) + n
    return out


PS16 = ps_content(C16)
PS16B = ps_content(C16B)
PS144 = ps_content(W144)
check("PS decomposition of the 16 closes on dimension 16 and has exactly two blocks",
      sum(n * d * l * r for (d, l, r, _), n in PS16.items()) == 16 and len(PS16) == 2)
check("PS decomposition of the 144 closes on dimension 144",
      sum(n * d * l * r for (d, l, r, _), n in PS144.items()) == 144)
check("the 16 branches to PS as (4,2,1) + (4bar,1,2), dimensions 8 + 8",
      sorted((d, l, r, n) for (d, l, r, _), n in PS16.items())
      == [(4, 1, 2, 1), (4, 2, 1, 1)])
check("the 144 branches to PS into exactly SIX blocks of dimensions 8, 8, 24, 24, 40, 40",
      len(PS144) == 6
      and sorted(d * l * r for (d, l, r, _), n in PS144.items() for _ in range(n))
      == [8, 8, 24, 24, 40, 40])

# multiplicity of each 16bar block inside the 144
check("KEY MULTIPLICITY: each of the two PS blocks of the 16bar occurs in the 144 "
      "with multiplicity EXACTLY ONE",
      len(PS16B) == 2 and all(PS144.get(k, 0) == 1 for k in PS16B))
check("KEY MULTIPLICITY: NEITHER of the two PS blocks of the 16 occurs in the 144 "
      "(multiplicity zero) -- the family-shaped content of the 144 is a MIRROR, "
      "not a copy",
      len(PS16) == 2 and all(PS144.get(k, 0) == 0 for k in PS16))
check("NEGATIVE CONTROL on the multiplicity-1 result: before the gamma-trace is removed, "
      "10 (x) 16 contains the mirror family's PS blocks with multiplicity TWO, so the "
      "value 1 for the 144 is a property of gamma-tracelessness and not of the machinery",
      all(ps_content(T1016).get(k, 0) == 2 for k in PS16B) and len(PS16B) == 2)
REMAIN = {k: v - PS16B.get(k, 0) for k, v in PS144.items()}
check("after removing the one 16bar-shaped block pair, 128 states remain and NONE of "
      "them is a 16- or 16bar-shaped PS block",
      sum(n * d * l * r for (d, l, r, _), n in REMAIN.items()) == 128
      and all(REMAIN.get(k, 0) == 0 for k in list(PS16) + list(PS16B)))

# ---------------------------------------------------------------------------
# 5.  Standard-Model branching (rank drops by one; multiplicities aggregate over X).
# ---------------------------------------------------------------------------
def su3_dynkin(lam):
    return (int(F(lam[0] - lam[1], 2)), int(F(lam[1] - lam[2], 2)))


def sm_key(lam):
    """(su(3) Dynkin labels, 2j_L+1, Y) -- a complete SM irrep label."""
    twojl = int(2 * dot(lam, rt([0, 0, 0, 1, -1]))
                / dot(rt([0, 0, 0, 1, -1]), rt([0, 0, 0, 1, -1])))
    return (su3_dynkin(lam), twojl + 1, hyper(lam))


def sm_conj(key):
    (a, b), l, y = key
    return ((b, a), l, -y)


def sm_dim(key):
    (a, b), l, _ = key
    return F((a + 1) * (b + 1) * (a + b + 2), 2) * l


def sm_content(mult):
    out = {}
    for lam, n in decompose(mult, SM).items():
        out[sm_key(lam)] = out.get(sm_key(lam), 0) + n
    return out


SMc16 = sm_content(C16)
SMc144 = sm_content(W144)
check("SM decomposition of the 16 closes on dimension 16",
      sum(n * sm_dim(k) for k, n in SMc16.items()) == 16)
check("SM decomposition of the 144 closes on dimension 144",
      sum(n * sm_dim(k) for k, n in SMc144.items()) == 144)
# the standard SM family, CP-conjugated (this weight convention puts nu_R at
# (1,1,1,1,1) with B-L = -1, i.e. it is the anti-family labelling; MJ-5 uses the
# same convention).  Written out before the run, not read off it.
STD_FAMILY_CONJ = {
    (((0, 1), 2, F(-1, 6))): 1,   # Qbar   (3bar, 2)_{-1/6}
    (((1, 0), 1, F(2, 3))): 1,    # ubar   (3, 1)_{+2/3}
    (((1, 0), 1, F(-1, 3))): 1,   # dbar   (3, 1)_{-1/3}
    (((0, 0), 2, F(1, 2))): 1,    # Lbar   (1, 2)_{+1/2}
    (((0, 0), 1, F(-1))): 1,      # ebar   (1, 1)_{-1}
    (((0, 0), 1, F(0))): 1,       # nubar  (1, 1)_{0}
}
check("MJ-5 cross-check: the 16 branches to EXACTLY the (CP-conjugated) Standard-Model "
      "family -- (3bar,2)_-1/6 + (3,1)_2/3 + (3,1)_-1/3 + (1,2)_1/2 + (1,1)_-1 + (1,1)_0",
      SMc16 == STD_FAMILY_CONJ)

sing16 = sum(n for k, n in SMc16.items() if k == ((0, 0), 1, F(0)))
sing144 = sum(n for k, n in SMc144.items() if k == ((0, 0), 1, F(0)))
check("JUDGE-ADDENDUM cross-check: the 16 has exactly ONE Standard-Model singlet",
      sing16 == 1)
check("JUDGE-ADDENDUM cross-check: the 144 also has exactly ONE Standard-Model singlet "
      "-- the SM-singlet count DOES NOT SEPARATE them",
      sing144 == 1)

# ---------------------------------------------------------------------------
# 6.  What DOES separate.
# ---------------------------------------------------------------------------
qmax16 = max(abs(charge(w)) for w in W16)
qmax144 = max(abs(charge(w)) for w in W144)
q144 = {abs(charge(w)) for w in W144}
q16 = {abs(charge(w)) for w in W16}
check("draft Sec 14.3 CERTIFIED: max |Q| is 1 on the 16 and 2 on the 144",
      qmax16 == 1 and qmax144 == 2)
check("draft Sec 14.3 CERTIFIED: the exotic charges 4/3, 5/3 and 2 all occur in the 144 "
      "and none of them occurs in any 16",
      {F(4, 3), F(5, 3), F(2)} <= q144 and not ({F(4, 3), F(5, 3), F(2)} & q16))
def su3dim(k):
    a, b = k[0]
    return F((a + 1) * (b + 1) * (a + b + 2), 2)


check("SEPARATION: maximum weak isospin is 1/2 on the 16 and 1 on the 144",
      max(k[1] for k in SMc16) == 2 and max(k[1] for k in SMc144) == 3)
check("SEPARATION: the SU(3) content of the 16 is only {1, 3, 3bar}; the 144 also "
      "carries a colour sextet and a colour octet",
      {su3dim(k) for k in SMc16} == {1, 3}
      and {F(6), F(8)} <= {su3dim(k) for k in SMc144})
check("SEPARATION: max |B-L| is 1 on the 16 and 5/3 on the 144",
      max(abs(b_minus_l(w)) for w in W16) == 1
      and max(abs(b_minus_l(w)) for w in W144) == F(5, 3))
t3_16 = sum(n * su3_cartan(w) ** 2 for w, n in C16.items())
t3_144 = sum(n * su3_cartan(w) ** 2 for w, n in W144.items())
t2_16 = sum(n * t3l(w) ** 2 for w, n in C16.items())
t2_144 = sum(n * t3l(w) ** 2 for w, n in W144.items())
check("SEPARATION LADDER, degree 2: the SU(3) and the SU(2)_L Dynkin indices are 2 on "
      "the 16 and 34 on the 144, EXACTLY reproducing the so(10) index (embedding index 1 "
      "on both factors) -- the degree-2 invariant SEPARATES where degree 3 did not",
      t3_16 == 2 and t3_144 == 34 and t2_16 == 2 and t2_144 == 34
      and t3_144 / t3_16 == T144 / T16)

# ---------------------------------------------------------------------------
# 7.  THE MASS-CHANNEL LADDER  (the "16 x 144 mediator decomposition",
#     named as queued-not-done in papers/drafts/one-generation-not-three Sec 14.3)
# ---------------------------------------------------------------------------
def tensor(a: Counter, b: Counter) -> Counter:
    out = Counter()
    for wa, na in a.items():
        for wb, nb in b.items():
            out[add(wa, wb)] += na * nb
    return out


def invariants(mult, alg, extra_zero=()):
    """dim Inv_alg(mult); extra_zero = u(1) functionals that must also vanish."""
    tot = 0
    for lam, n in decompose(mult, alg).items():
        if any(dot(lam, a) != 0 for a in alg.simple):
            continue
        if all(f(lam) == 0 for f in extra_zero):
            tot += n
    return tot


P16_144 = tensor(C16, W144)
P16_16 = tensor(C16, C16)
check("POSITIVE CONTROL for the invariant counter: dim Inv_so(10)(16 (x) 16bar) = 1 "
      "and dim Inv_so(10)(144 (x) 144bar) = 1",
      invariants(tensor(C16, C16B), SO10) == 1
      and invariants(tensor(W144, W144B), SO10) == 1)
check("POSITIVE CONTROL: dim Inv_so(10)(16 (x) 16) = 0 -- no Spin(10)-invariant "
      "Majorana mass for a single family",
      invariants(P16_16, SO10) == 0)

inv_so10 = invariants(P16_144, SO10)
inv_ps = invariants(P16_144, PS, extra_zero=())
inv_sm = invariants(P16_144, SM, extra_zero=(hyper,))
inv_sm_1616 = invariants(P16_16, SM, extra_zero=(hyper,))
inv_ps_1616 = invariants(P16_16, PS)
check("LADDER RUNG 1: dim Inv_so(10)(16 (x) 144) = 0 -- NO Spin(10)-invariant mass "
      "channel joins a family to the imposter host",
      inv_so10 == 0)
check("LADDER RUNG 2: dim Inv_PS(16 (x) 144) = 2 -- exactly TWO Pati-Salam-invariant "
      "mass channels open once Spin(10) breaks to Pati-Salam",
      inv_ps == 2)
inv_sm_pairing = sum(n * SMc144.get(sm_conj(k), 0) for k, n in SMc16.items())
check("LADDER RUNG 3: dim Inv_SM(16 (x) 144) = 11, computed TWICE by independent routes "
      "(Racah alternating sum on the 2304-weight tensor product, and direct SM-irrep "
      "conjugate pairing) -- the two agree",
      inv_sm == 11 and inv_sm_pairing == 11)
check("of those 11 SM channels, exactly 6 -- one per SM irrep of the family -- are the "
      "ones already present at Pati-Salam level; the other 5 are SM-only coincidences "
      "that open only after Pati-Salam breaks",
      len(SMc16) == 6 and all(SMc144.get(sm_conj(k), 0) >= 1 for k in SMc16)
      and inv_sm - sum(1 for k in SMc16) == 5)
check("CONTRAST: 16 (x) 16 opens NO Pati-Salam channel but ONE Standard-Model channel "
      "(the nu_R Majorana direction of gate MJ-5)",
      inv_ps_1616 == 0 and inv_sm_1616 == 1)

# ---------------------------------------------------------------------------
# 8.  The 128-state remainder, and the 2+1 partition as a NET-CHIRALITY statement.
# ---------------------------------------------------------------------------
REM = W144 - C16B
check("the 144's weight multiset really does contain the mirror family's weights, and "
      "removing them leaves exactly 128 states with non-negative multiplicities",
      sum(REM.values()) == 128 and all(v > 0 for v in REM.values())
      and all(W144[w] > C16B[w] for w in C16B))
AREM = anomalies(REM)
check("the 128-state remainder is itself free of all five Standard-Model anomalies "
      "(it must be, since the 144 and the mirror family separately are)",
      all(v == 0 for v in AREM.values()))
SMcREM = sm_content(REM)
check("the 128-state remainder carries NO Standard-Model singlet: the 144's single "
      "SM singlet lies entirely inside its mirror-family block",
      sum(n for k, n in SMcREM.items() if k == ((0, 0), 1, F(0))) == 0
      and sum(n * sm_dim(k) for k, n in SMcREM.items()) == 128)
check("the 128-state remainder carries all of the separating structure: |Q| reaches 2, "
      "colour sextets and octets are present, and weak isospin reaches 1",
      max(abs(charge(w)) for w in REM) == 2
      and {F(6), F(8)} <= {su3dim(k) for k in SMcREM}
      and max(k[1] for k in SMcREM) == 3)
t3_rem = sum(n * su3_cartan(w) ** 2 for w, n in REM.items())
check("the remainder's SU(3) Dynkin index is 32 = 34 - 2, additively consistent with "
      "the 144 and the removed mirror family",
      t3_rem == 32 and t3_144 - t3_16 == 32)

# ---- net chirality of  n_g copies of 16  plus one 144, block by block ----------
# Conjugation is applied to the WEIGHT MULTISET (w -> -w) and the Pati-Salam
# content recomputed, so no hand-written label algebra can go wrong.
def negate(mult):
    return Counter({tuple(-x for x in w): n for w, n in mult.items()})


check("POSITIVE CONTROL for the conjugation route: the PS content of the negated 16 "
      "weight multiset equals the PS content of the 16bar, and differs from that of the 16",
      ps_content(negate(C16)) == PS16B and PS16 != PS16B)

FAMILY_LABELS = set(PS16) | set(PS16B)
EXOTIC_LABELS = set(PS144) - FAMILY_LABELS
check("the 144's six Pati-Salam blocks split as 2 family-shaped (mirror) + 4 exotic",
      len(EXOTIC_LABELS) == 4 and len(set(PS144) & FAMILY_LABELS) == 2)

for ng in (1, 2, 3, 4):
    total = Counter()
    for w, n in C16.items():
        total[w] += ng * n
    total += W144
    cont = ps_content(total)
    conj = ps_content(negate(total))
    net = {k: cont.get(k, 0) - conj.get(k, 0) for k in set(cont) | set(conj)}
    check(f"NET CHIRALITY (n_g = {ng} copies of the 16, plus one 144): each of the two "
          f"family-shaped Pati-Salam blocks has net chirality exactly {ng} - 1 = {ng - 1}, "
          f"its mirror has {1 - ng}, and each of the four exotic blocks has net chirality 1",
          all(net[k] == ng - 1 for k in PS16)
          and all(net[k] == 1 - ng for k in PS16B)
          and all(net[k] == 1 for k in EXOTIC_LABELS)
          and sum(cont[k] * k[0] * k[1] * k[2] for k in cont) == 16 * ng + 144)

check("THE 2+1 PARTITION IS FORCED, NOT CHOSEN: the drop from n_g to n_g - 1 chiral "
      "families is exactly the multiplicity 1 of the mirror blocks in the 144. There is "
      "no free parameter: a second 144 would be needed to remove a second family",
      all(PS144.get(k, 0) == 1 for k in PS16B) and len(PS16B) == 2)
check("THE PARTITION IS UNLABELLED (what this probe verifies): the two Pati-Salam mass "
      "channels are carried by two DISTINCT and independent PS blocks, so they are two "
      "separate 1 x n_g coupling rows, not one",
      inv_ps == 2 and len(PS16B) == 2 and len(set(PS16B)) == 2
      and list(PS16B)[0] != list(PS16B)[1])

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
print("PS content of the 16    (dim, 2j_L+1, 2j_R+1) x mult:")
for k, n in sorted(PS16.items()):
    print(f"    ({k[0]}, {k[1]}, {k[2]})  x{n}    B-L(hw) = {k[3]}")
print("PS content of the 144:")
for k, n in sorted(PS144.items()):
    print(f"    ({k[0]}, {k[1]}, {k[2]})  x{n}    B-L(hw) = {k[3]}   dim {k[0]*k[1]*k[2]*n}")
print("SM content of the 16    (SU(3) Dynkin, 2j_L+1, Y) x mult:")
for k, n in sorted(SMc16.items(), key=lambda t: (su3dim(t[0]), t[0][1], t[0][2])):
    print(f"    ({su3dim(k)}{'bar' if k[0][1] > k[0][0] else ''}, {k[1]})_Y={k[2]}  x{n}")
print("SM content of the 144:")
for k, n in sorted(SMc144.items(), key=lambda t: (su3dim(t[0]), t[0][1], t[0][2])):
    print(f"    ({su3dim(k)}{'bar' if k[0][1] > k[0][0] else ''}, {k[1]})_Y={k[2]}  x{n}")
print(f"\nInvariant ladder  Inv(16 (x) 144):  so(10) = {inv_so10}   PS = {inv_ps}   SM = {inv_sm}")
print(f"Invariant ladder  Inv(16 (x) 16 ):  so(10) = {invariants(P16_16, SO10)}   "
      f"PS = {inv_ps_1616}   SM = {inv_sm_1616}")
print(f"Dynkin indices (T(10)=1):  16 -> {T16/T10}   144 -> {T144/T10}")
print(f"Casimirs:  16 -> {casimir(HW16)}   144 -> {casimir(HW144)}")
print(f"|Q|max:  16 -> {qmax16}   144 -> {qmax144}      "
      f"|B-L|max:  16 -> {max(abs(b_minus_l(w)) for w in W16)}   "
      f"144 -> {max(abs(b_minus_l(w)) for w in W144)}")
print(f"SM singlets:  16 -> {sing16}   144 -> {sing144}")
print()

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)

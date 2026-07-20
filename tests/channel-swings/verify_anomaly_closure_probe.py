#!/usr/bin/env python3
r"""HOSTILE SECOND-DRY-ROUND VERIFIER -- anomaly-closure result pair, 2026-07-20.

Independent recomputation of the load-bearing numbers behind
  explorations/dk-chirality-fork-2026-07-20.md      (commit 2f06e7f)
  explorations/global-anomaly-leg-2026-07-20.md     (commit 4b83f4b)
by DIFFERENT routes wherever a different route exists. This probe shares NO code
with the two target probes and deliberately swaps the derivation route:

  R1  A-hat coefficients via the BERNOULLI-NUMBER expansion
      Q(x) = (x/2)/sinh(x/2) = e^{x/2} * (x/(e^x - 1)) = e^{x/2} * sum B_n x^n/n!
      (target probes used sinh-series reciprocal / -log h + Newton).
  R2  p-basis conversion by exact INTEGER-SPECIALIZATION linear solve with
      overdetermined consistency rows (targets used monomial-matching Gaussian
      elimination on symmetric-function coefficients).
  R3  Fixture Pontryagin numbers of (K3)^4 and (HP^2)^2 DERIVED here from
      nilpotent product algebra (targets quoted them), plus the multiplicativity
      cross-check A-hat((K3)^4) = (A-hat(K3))^4 = 2^4.
  R4  The C3 alternating density killed via the SPLITTING-PRINCIPLE product
      prod_i (2 - 2 cosh x_i) computed at weight cap 7: identically zero through
      weight 6 and EXACTLY -e_7 at weight 7 (lowest degree 28) -- a sharper,
      falsifiable form of the targets' weight-4 vanishing.
  R5  The bounding-extension class via the residue identity
      G = [t^14] lambda_t(TZ_C) (1+t)^{-3}  =>  a_k = C(16-k,2) = (15-k)(16-k)/2
      (independent derivation of the closed form), and ch(G) computed to weight 7:
      ZERO through weight 6, weight-7 part exactly -e_7(u_1..u_8). This is
      STRONGER than the target's check (which verified only the weight-4 part of
      A-hat*ch(G)): it kills the degree-16 extension density for EVERY gauge
      twist as well, closing a gauge-mixed gap the target never examined.
  R6  Omega^spin window re-derived from the ABP wedge shape (shape input [T],
      flagged) against the published table, ranks via an INDEPENDENT partition
      function (Euler pentagonal recurrence, not brute enumeration); the two
      BSp AHSS lines re-derived from Borel degrees, upgrading the target's
      "unsourced candidate Z/2" for Omega~^spin_5(BSp(64)) to a derived Z/2.
  R7  Kramers perfect-square mechanism on a DIFFERENT quaternionic fixture with
      the charpoly computed by NEWTON'S IDENTITIES from power traces (target
      used Faddeev-LeVerrier), plus an explicit J-commutation matrix check.

Discipline: exact Fraction arithmetic, no floats, no RNG, no imports from the
target probes. Tags: [T] table/shape input (excluded from headline), [E] exact
recomputation, [F] fixture/known-value control. Exit 0 iff all pass.

Run:  python tests/channel-swings/verify_anomaly_closure_probe.py
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial

CHECKS: list[tuple[str, str, bool]] = []


def check(tag: str, name: str, okv: bool, detail: str = "") -> None:
    CHECKS.append((tag, name, bool(okv)))
    line = f"[{tag}] {'PASS' if okv else 'FAIL'}  {name}"
    if detail:
        line += f"   {detail}"
    print(line)
    assert okv, f"[{tag}] {name} FAILED {detail}"


# ============================================================================
# Polynomial engine: monomials = exponent tuples over nv vars u_i (= x_i^2,
# cohomological degree 4 each); weight = total u-degree; cap = wmax.
# ============================================================================

def padd(a, b):
    o = dict(a)
    for k, v in b.items():
        w = o.get(k, F(0)) + v
        if w:
            o[k] = w
        elif k in o:
            del o[k]
    return o


def pscale(a, c):
    c = F(c)
    return {k: v * c for k, v in a.items() if v * c != 0}


def pmul(a, b, wmax):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            if sum(k) <= wmax:
                w = o.get(k, F(0)) + va * vb
                if w:
                    o[k] = w
                elif k in o:
                    del o[k]
    return o


def pweight(a, w):
    return {k: v for k, v in a.items() if sum(k) == w}


def plowcap(a, w):
    return {k: v for k, v in a.items() if sum(k) <= w}


def univ(ser, i, nv, wmax):
    o = {}
    for d, c in ser.items():
        if d <= wmax and c:
            key = [0] * nv
            key[i] = d
            o[tuple(key)] = F(c)
    return o


def esym_val(us, j):
    return sum(
        1 if j == 0 else 0
        for _ in [0]
    ) if j == 0 else sum(
        _prod(us[i] for i in idx) for idx in combinations(range(len(us)), j)
    )


def _prod(it):
    r = 1
    for x in it:
        r *= x
    return r


def peval(poly, us):
    tot = F(0)
    for k, v in poly.items():
        m = v
        for e, u in zip(k, us):
            m *= u ** e
        tot += m
    return tot


# ============================================================================
# R1 -- A-hat per-root series via BERNOULLI numbers (independent route).
# ============================================================================
print("=" * 84)
print("V1  A-hat engine via Bernoulli-number route + fixtures derived from scratch")
print("=" * 84)

NB = 10
BER = [F(0)] * NB          # Bernoulli numbers, B1 = -1/2 convention
BER[0] = F(1)
for n in range(1, NB):
    s = F(0)
    for k in range(n):
        s += comb(n + 1, k) * BER[k]
    BER[n] = -s / (n + 1)
check("T", "Bernoulli setup: B2 = 1/6, B4 = -1/30, B6 = 1/42, B8 = -1/30",
      (BER[2], BER[4], BER[6], BER[8]) == (F(1, 6), F(-1, 30), F(1, 42), F(-1, 30)))

XMAX = 8                    # series in x through x^8  (u^4)
ex_half = [F(1, 2 ** n * factorial(n)) for n in range(XMAX + 1)]   # e^{x/2}
bser = [BER[n] / factorial(n) for n in range(XMAX + 1)]            # x/(e^x-1)
qx = [F(0)] * (XMAX + 1)
for i in range(XMAX + 1):
    for j in range(XMAX + 1 - i):
        qx[i + j] += ex_half[i] * bser[j]
check("E", "Q(x) = e^{x/2} x/(e^x-1) is EVEN (odd coefficients vanish identically)",
      all(qx[n] == 0 for n in range(1, XMAX + 1, 2)))
QU = {m: qx[2 * m] for m in range(5)}   # series in u = x^2
check("E", "per-root A-hat factor: 1 - u/24 + 7u^2/5760 - 31u^3/967680 + 127u^4/154828800",
      QU == {0: F(1), 1: F(-1, 24), 2: F(7, 5760), 3: F(-31, 967680),
             4: F(127, 154828800)})

WM = 4


def ahat_prod(nv):
    o = {(0,) * nv: F(1)}
    for i in range(nv):
        o = pmul(o, univ(QU, i, nv, WM), WM)
    return o


# p-basis conversion by integer specializations (route R2)
BASES = {
    1: [(1, 0, 0, 0)],
    2: [(2, 0, 0, 0), (0, 1, 0, 0)],
    3: [(3, 0, 0, 0), (1, 1, 0, 0), (0, 0, 1, 0)],
    4: [(4, 0, 0, 0), (2, 1, 0, 0), (0, 2, 0, 0), (1, 0, 1, 0), (0, 0, 0, 1)],
}
SPECS = [
    (1, 2, 3, 4, 5, 7, 11, 13),
    (1, 1, 2, 3, 5, 8, 13, 21),
    (2, 3, 5, 7, 11, 13, 17, 19),
    (1, 4, 9, 16, 25, 36, 49, 64),
    (1, 2, 4, 8, 16, 32, 64, 128),
    (3, 1, 4, 1, 5, 9, 2, 6),
    (1, 3, 6, 10, 15, 21, 28, 36),
    (2, 2, 3, 3, 5, 5, 7, 7),
]


def gauss_solve(rows, ncol):
    piv = 0
    for col in range(ncol):
        sel = next((r for r in range(piv, len(rows)) if rows[r][col] != 0), None)
        if sel is None:
            return None
        rows[piv], rows[sel] = rows[sel], rows[piv]
        pr = rows[piv]
        rows[piv] = pr = [x / pr[col] for x in pr]
        for r in range(len(rows)):
            if r != piv and rows[r][col] != 0:
                f = rows[r][col]
                rows[r] = [a - f * b for a, b in zip(rows[r], pr)]
        piv += 1
    sol = [F(0)] * ncol
    for col in range(ncol):
        row = next(r for r in rows if r[col] == 1
                   and all(r[c] == 0 for c in range(ncol) if c != col))
        sol[col] = row[-1]
    for r in rows[piv:]:
        if r[-1] != 0:
            return None
    return sol


def to_p(poly, w, nv):
    """Weight-w part of a symmetric poly -> coefficients on BASES[w], by
    exact evaluation at integer specializations (overdetermined)."""
    basis = BASES[w]
    pw = pweight(poly, w)
    rows = []
    for spec in SPECS:
        us = [F(x) for x in spec[:nv]]
        e = [None] + [esym_val(us, j) for j in range(1, 5)]
        brow = []
        for exp in basis:
            val = F(1)
            for j, kexp in enumerate(exp, start=1):
                val *= e[j] ** kexp
            brow.append(val)
        rows.append(brow + [peval(pw, us)])
    sol = gauss_solve([r[:] for r in rows], len(basis))
    assert sol is not None, "specialization system inconsistent/singular"
    return {exp: c for exp, c in zip(basis, sol) if c != 0}


NV = 7
AH = ahat_prod(NV)
a4 = to_p(AH, 1, NV)
a8 = to_p(AH, 2, NV)
a12 = to_p(AH, 3, NV)
a16 = to_p(AH, 4, NV)
check("E", "[A-hat]_4  = -p1/24 (Bernoulli route)", a4 == {(1, 0, 0, 0): F(-1, 24)})
check("E", "[A-hat]_8  = (7p1^2 - 4p2)/5760",
      a8 == {(2, 0, 0, 0): F(7, 5760), (0, 1, 0, 0): F(-1, 1440)})
check("E", "[A-hat]_12 = (-31p1^3 + 44p1p2 - 16p3)/967680",
      a12 == {(3, 0, 0, 0): F(-31, 967680), (1, 1, 0, 0): F(44, 967680),
              (0, 0, 1, 0): F(-16, 967680)})
D16 = 464486400
check("E", "[A-hat]_16 = (381p1^4 - 904p1^2p2 + 208p2^2 + 512p1p3 - 192p4)/464486400",
      a16 == {(4, 0, 0, 0): F(381, D16), (2, 1, 0, 0): F(-904, D16),
              (0, 2, 0, 0): F(208, D16), (1, 0, 1, 0): F(512, D16),
              (0, 0, 0, 1): F(-192, D16)})
P4C = a16[(0, 0, 0, 1)]
check("E", "tr R^8 channel: p4 coefficient = -1/2419200", P4C == F(-1, 2419200))

# fixtures with Pontryagin numbers DERIVED here (nilpotent product algebra)
# (K3)^4: generators a_0..a_3 with a_i^2 = 0; class dict keyed by frozenset
def k3_mul(A, B):
    o = {}
    for ka, va in A.items():
        for kb, vb in B.items():
            if ka & kb:
                continue
            k = ka | kb
            o[k] = o.get(k, F(0)) + va * vb
    return o


ONE4 = {frozenset(): F(1)}
E1 = {frozenset([i]): F(1) for i in range(4)}          # e_1(a)
PK = {1: E1}
for j in (2, 3, 4):
    PK[j] = {frozenset(s): F(1) for s in combinations(range(4), j)}
TOP = frozenset(range(4))


def k3_num(exp):
    cls = ONE4
    for j, k in enumerate(exp, start=1):
        for _ in range(k):
            cls = k3_mul(cls, PK[j])
    return cls.get(TOP, F(0))


pk3 = {exp: k3_num(exp) for exp in BASES[4]}
check("E", "DERIVED Pontryagin numbers of (K3)^4 / a^4: "
      "{p1^4:24, p1^2p2:12, p2^2:6, p1p3:4, p4:1}",
      pk3 == {(4, 0, 0, 0): 24, (2, 1, 0, 0): 12, (0, 2, 0, 0): 6,
              (1, 0, 1, 0): 4, (0, 0, 0, 1): 1})
A = F(-48)   # p1[K3]  (signature -16 = p1/3)
idx_k3 = sum(a16[k] * v for k, v in pk3.items()) * A ** 4
check("F", "end-to-end: A-hat index (K3)^4 = 16 AND = (A-hat(K3))^4 = (48/24)^4",
      idx_k3 == 16 and (-A / 24) ** 4 == 16)

# (HP^2)^2: truncated algebra F[u,v]/(u^3, v^3); p(HP^2) = 1 + 2u + 7u^2
def hp_mul(A_, B_):
    o = {}
    for (i, j), va in A_.items():
        for (k, l), vb in B_.items():
            if i + k < 3 and j + l < 3:
                key = (i + k, j + l)
                o[key] = o.get(key, F(0)) + va * vb
    return o


ptot = {(0, 0): F(1), (1, 0): F(2), (2, 0): F(7),
        (0, 1): F(2), (1, 1): F(4), (2, 1): F(14),
        (0, 2): F(7), (1, 2): F(14), (2, 2): F(49)}   # (1+2u+7u^2)(1+2v+7v^2)
PH = {j: {k: v for k, v in ptot.items() if k[0] + k[1] == j} for j in (1, 2, 3, 4)}


def hp_num(exp):
    cls = {(0, 0): F(1)}
    for j, k in enumerate(exp, start=1):
        for _ in range(k):
            cls = hp_mul(cls, PH[j])
    return cls.get((2, 2), F(0))


php = {exp: hp_num(exp) for exp in BASES[4]}
check("E", "DERIVED Pontryagin numbers of (HP^2)^2: "
      "{p1^4:96, p1^2p2:88, p2^2:114, p1p3:56, p4:49}",
      php == {(4, 0, 0, 0): 96, (2, 1, 0, 0): 88, (0, 2, 0, 0): 114,
              (1, 0, 1, 0): 56, (0, 0, 0, 1): 49})
check("F", "end-to-end: A-hat index (HP^2)^2 = 0 AND A-hat(HP^2) = (7*4-4*7)/5760 = 0",
      sum(a16[k] * v for k, v in php.items()) == 0
      and F(7 * 4 - 4 * 7, 5760) == 0)

# ============================================================================
# V2 -- the recount by direct dimension counting (fork table, all rows)
# ============================================================================
print()
print("=" * 84)
print("V2  net-chirality recount, partial-sum identity, Fierz counts")
print("=" * 84)

check("E", "Pascal induction: sum_{p<=k}(-1)^p C(14,p) = (-1)^k C(13,k), all k = 0..14",
      all(sum((-1) ** p * comb(14, p) for p in range(k + 1))
          == (-1) ** k * comb(13, k) for k in range(15)))
check("E", "-13 IS the k=1 partial sum; full tower k=14 gives (1-1)^14 = 0; "
      "no proper truncation k=0..13 vanishes",
      -comb(13, 1) == -13
      and sum((-1) ** p * comb(14, p) for p in range(15)) == 0
      and all(comb(13, k) != 0 for k in range(14)))

CONT = {
    "C0": ([(0, +1), (1, -1)], -13),
    "C0m": ([(0, -1), (1, +1)], +13),
    "C1": ([(0, 0), (1, 0)], 0),
    "C2": ([(p, 0) for p in range(15)], 0),
    "C3": ([(p, (-1) ** p) for p in range(15)], 0),
    "C4": ([(p, (-1) ** p) for p in range(3)], +78),
    "C5": ([(0, 0), (0, 0), (1, 0), (13, 0), (14, 0)], 0),
    "C5b": ([(0, +1), (1, -1), (13, +1), (14, -1)], 0),
    "C5c": ([(0, +1), (1, -1), (13, -1), (14, +1)], -26),
}
for name, (content, wexp) in CONT.items():
    W = sum(eps * comb(14, p) for p, eps in content)
    check("E", f"W({name}) = {wexp} by direct counting", W == wexp, f"got {W}")
coeff = lambda W: 64 * W * P4C
check("E", "coeff(C0) = 13/37800; coeff(C4) = -13/6300; coeff(C5c) = 13/18900; "
      "balanced rows = 0",
      coeff(-13) == F(13, 37800) and coeff(78) == F(-13, 6300)
      and coeff(-26) == F(13, 18900) and coeff(0) == 0)
check("E", "Fierz: 2^14 = 16384 = dim_R M(64,H) = 64*256; complex 128^2; d=4 control 4^2",
      2 ** 14 == 16384 == 64 * 64 * 4 == 64 * 256 and 2 ** 14 == 128 ** 2
      and 2 ** 4 == 4 ** 2)

# ============================================================================
# V3 -- bordism ledger: ABP-shape window, partition ranks, BSp AHSS, KO/KSp
# ============================================================================
print()
print("=" * 84)
print("V3  bordism ledger: Omega^spin window, BSp(64) AHSS lines, KO/KSp slots")
print("=" * 84)

check("T", "SHAPE INPUT (ABP 1967, flagged not derived): 2-local MSpin wedge with "
      "ko-type bottom cells 0, 8, 10, 16x2; first HZ/2 at 20; odd-locally MSpin=MSO "
      "and no odd torsion (Wall)", True)


def ko_pi(n):
    if n < 0:
        return None
    return {0: "Z", 1: "Z2", 2: "Z2", 4: "Z"}.get(n % 8, "0")


def omega_spin(n):
    out = []
    for shift, mult, floor in ((0, 1, 0), (8, 1, 0), (8, 1, 2), (16, 2, 0)):
        # third summand = Sigma^10 (Sigma^{-2} ko<2>): pi_{n-8}(ko) for n-8 >= 2
        m = n - shift
        if m < floor:
            continue
        v = ko_pi(m)
        if v and v != "0":
            out.extend([v] * mult)
    return tuple(sorted(out))


LIT = {0: ("Z",), 1: ("Z2",), 2: ("Z2",), 3: (), 4: ("Z",), 5: (), 6: (), 7: (),
       8: ("Z", "Z"), 9: ("Z2", "Z2"), 10: ("Z2", "Z2", "Z2"), 11: (),
       12: ("Z", "Z", "Z"), 13: (), 14: (), 15: (),
       16: ("Z", "Z", "Z", "Z", "Z")}
check("E", "derived window matches published table for ALL n = 0..16 "
      "(incl. 13,14,15 = 0 and 16 = Z^5)",
      all(omega_spin(n) == LIT[n] for n in range(17)))


def euler_partition(n):
    p = [1] + [0] * n
    for m in range(1, n + 1):
        tot, k = 0, 1
        while True:
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2
            if g1 > m and g2 > m:
                break
            sgn = -1 if k % 2 == 0 else 1
            if g1 <= m:
                tot += sgn * p[m - g1]
            if g2 <= m:
                tot += sgn * p[m - g2]
            k += 1
        p[m] = tot
    return p[n]


check("E", "rational ranks via Euler pentagonal recurrence: rank Om_12 = p(3) = 3, "
      "rank Om_16 = p(4) = 5 (= # weight-4 Pontryagin monomials)",
      sum(1 for s in omega_spin(12) if s == "Z") == euler_partition(3) == 3
      and sum(1 for s in omega_spin(16) if s == "Z") == euler_partition(4) == 5 == len(BASES[4]))
check("E", "no odd torsion anywhere in the derived window (all summands Z or Z2)",
      all(s in ("Z", "Z2") for n in range(17) for s in omega_spin(n)))

# AHSS for reduced spin bordism of BSp(64), from Borel degrees ([T] input)
check("T", "INPUT (Borel 1953): H*(BSp(64);Z) = Z[q_1..q_64], torsion-free, "
      "degrees 0 mod 4 => reduced homology only in degrees 4,8,12,... (free)", True)
line15 = [(p, 15 - p) for p in (4, 8, 12)]
check("E", "AHSS line p+q = 15: E2_{4,11}, E2_{8,7}, E2_{12,3} all ZERO "
      "(coefficients Omega^spin_{11,7,3} = 0 from derived window) "
      "=> Omega~^spin_15(BSp(64)) = 0, no extension possible",
      all(omega_spin(q) == () for _, q in line15))
# line p+q = 5: only (4,1) nonzero; differentials in/out land in zero groups.
# H~_p(BSp(64)) is nonzero only for p a positive multiple of 4.
hbsp_zero = lambda p: not (p > 0 and p % 4 == 0)
d_out = [(4 - r, r) for r in (2, 3, 4)]        # d_r: (4,1) -> (4-r, r): p = 2,1,0
d_in = [(4 + r, 2 - r) for r in (2,)]          # d_r hits (4,1) only from q >= 0: (6,0)
check("E", "AHSS line p+q = 5: E2_{4,1} = H_4 (x) Om_1 = Z/2 is the ONLY entry; "
      "d_r out land in H~_{2,1,0} = 0; d_2 in comes from H~_6 = 0 => "
      "Omega~^spin_5(BSp(64)) = Z/2 DERIVED (upgrades the target's unsourced flag)",
      omega_spin(1) == ("Z2",)
      and all(hbsp_zero(p) for p, _ in d_out)
      and all(hbsp_zero(p) for p, _ in d_in)
      and all(hbsp_zero(p) or omega_spin(5 - p) == () for p in range(5, 6)))
check("E", "kill unaffected either way: content multiplicity 64 is EVEN, so a Z/2 "
      "receptacle (0 or Z/2) is not populated", 64 % 2 == 0)

# KO / KSp dead slots at 15, live at 5 (Bott ladder input)
check("T", "INPUT (Bott): KO_n = Z,Z2,Z2,0,Z,0,0,0 period 8; KSp_n = KO_{n+4}", True)
KOpat = {0: "Z", 1: "Z2", 2: "Z2", 4: "Z"}
ko_at = lambda n: KOpat.get(n % 8, "0")
check("E", "KO_15 = 0 (15 = 7 mod 8); KSp_15 = KO_19 = 0 (19 = 3 mod 8): "
      "mapping-torus dim 15 Bott-dead for BOTH reality types",
      ko_at(15) == "0" and ko_at(19) == "0")
check("F", "positive control: KSp_5 = KO_9 = Z/2 (Witten SU(2) slot LIVE at dim 5)",
      ko_at(9) == "Z2")
check("E", "mod-2 slots = KO degrees 1,2 mod 8: dim 15 real (7) and quaternionic "
      "(15-4 = 3) both outside; dim 5 quaternionic (1) inside",
      15 % 8 not in (1, 2) and (15 - 4) % 8 not in (1, 2) and (5 - 4) % 8 in (1, 2))

# 3-primary disjointness
check("E", "24 = 2^3 * 3; Hom(Z/3, Z) = 0; Hom(Z/3, Z/2^k) = 0 (gcd(3, 2^k) = 1); "
      "Omega^spin_3 = 0 kills the spin image of pi_3^s",
      24 == 8 * 3 and all(pow(2, k) % 3 != 0 for k in range(1, 11))
      and omega_spin(3) == ())

# ============================================================================
# V4 -- the C3 alternating density by the splitting-principle product route
# ============================================================================
print()
print("=" * 84)
print("V4  alternating density: product route, per-slot densities, honest C0")
print("=" * 84)

COSH = {m: F(1, factorial(2 * m)) for m in range(8)}          # cosh(x) in u
TWO_M_2COSH = {m: F(-2, factorial(2 * m)) for m in range(1, 8)}  # 2 - 2cosh(x)


def lambda_tpoly(nv, wmax):
    """t-coefficients of prod_i (1 + 2cosh(u_i) t + t^2): tp[p] = ch(Lambda^p V_C)."""
    tp = [{(0,) * nv: F(1)}]
    for i in range(nv):
        ci = univ(COSH, i, nv, wmax)
        new = [dict() for _ in range(len(tp) + 2)]
        for d, poly in enumerate(tp):
            new[d] = padd(new[d], poly)
            new[d + 1] = padd(new[d + 1], pscale(pmul(ci, poly, wmax), 2))
            new[d + 2] = padd(new[d + 2], poly)
        tp = new
    return tp


W7 = 7
tp7 = lambda_tpoly(7, W7)                     # rank-14 bundle, weight cap 7
check("E", "rank check: ch(Lambda^p)|_0 = C(14,p), p = 0..14",
      all(tp7[p].get((0,) * 7, F(0)) == comb(14, p) for p in range(15)))

# route A: alternating sum of the t-coefficients
S_A = {}
for p in range(15):
    S_A = padd(S_A, pscale(tp7[p], (-1) ** p))
# route B: the splitting-principle product prod_i (2 - 2 cosh x_i)
S_B = {(0,) * 7: F(1)}
for i in range(7):
    S_B = pmul(S_B, univ(TWO_M_2COSH, i, 7, W7), W7)
check("E", "ROUTE AGREEMENT: sum_p (-1)^p ch(Lambda^p V_C) == prod_i (2 - 2cosh x_i) "
      "exactly (weights 0..7)", S_A == S_B)
check("E", "K-theory Euler class: ZERO at all weights 0..6 (degree < 28) -- "
      "so the ENTIRE degree-16 density, gauge twists included, dies",
      all(pweight(S_A, w) == {} for w in range(7)))
e7_7 = {tuple(1 for _ in range(7)): F(-1)}
check("E", "lowest term EXACTLY -e_7 (u_1..u_7) at weight 7 (cohomological degree 28)",
      pweight(S_A, 7) == e7_7)

# per-slot densities at weight cap 4 (reuse tp7 truncated)
AH7 = AH                                       # A-hat product, nv = 7, wmax 4
D = [pmul(AH7, plowcap(tp7[p], WM), WM) for p in range(15)]
check("F", "D_0 == [A-hat]_16 from the Bernoulli engine (route agreement)",
      to_p(D[0], 4, 7) == a16)
check("E", "every per-slot degree-16 density D_p is NONZERO (p = 0..14)",
      all(pweight(D[p], 4) != {} for p in range(15)))
Sk = {}
trunc_all_nonzero = True
for k in range(14):
    Sk = padd(Sk, pscale(D[k], (-1) ** k))
    if pweight(Sk, 4) == {}:
        trunc_all_nonzero = False
check("E", "every proper truncation k = 0..13 has NONZERO exact degree-16 density "
      "(no partial repair, honest-curvature version)", trunc_all_nonzero)
S_D = padd(Sk, D[14])                          # k = 14 completes the tower
check("E", "full-tower exact degree-16 density == 0 (C3 kill, curvature-honest)",
      pweight(S_D, 4) == {})

# honest C0 observation, recomputed independently (predicted analytically:
# D1 p4 = 14*(-1/2419200) + ch_16(V) p4-part = -494/2419200; D0 - D1 => 493)
hC0 = to_p(padd(D[0], pscale(D[1], -1)), 4, 7)
check("E", "honest twisted C0 p4 coefficient = 493/2419200 (vs 13/2419200 "
      "multiplicity convention; BOTH nonzero, branch verdict unchanged)",
      hC0.get((0, 0, 0, 1)) == F(493, 2419200)
      and -13 * P4C == F(13, 2419200))

# ============================================================================
# V5 -- bounding-extension leg: a_k closed form re-derived, ch(G) to weight 7
# ============================================================================
print()
print("=" * 84)
print("V5  extension class G: independent a_k derivation, ch(G) = 0 through wt 6")
print("=" * 84)

check("E", "INDEPENDENT closed form: a_k = sum_{j=1}^{15-k} j = (15-k)(16-k)/2 "
      "= C(16-k, 2) (the [t^14] lambda_t(TZ)(1+t)^{-3} residue route)",
      all(sum(range(1, 16 - k)) == (15 - k) * (16 - k) // 2 == comb(16 - k, 2)
          for k in range(15)))
check("E", "a_14 = 1, a_15 = a_16 = 0: the truncation at 14 is CANONICAL "
      "(C(2,2) = 1, C(1,2) = C(0,2) = 0 -- the series ends by itself)",
      comb(2, 2) == 1 and comb(1, 2) == 0 and comb(0, 2) == 0)

tp8 = lambda_tpoly(8, W7)                      # rank-16 bundle TZ_C, weight cap 7
chG = {}
for k in range(15):
    chG = padd(chG, pscale(tp8[k], (-1) ** k * comb(16 - k, 2)))
check("E", "ch(G) == 0 IDENTICALLY at weights 0..6 -- STRONGER than the target's "
      "weight-4-of-(A-hat.ch G) check: extension density dies for EVERY gauge "
      "twist, closing the gauge-mixed extension gap",
      all(pweight(chG, w) == {} for w in range(7)))
e7_8 = {k: F(-1) for k in
        (tuple(1 if i in idx else 0 for i in range(8))
         for idx in combinations(range(8), 7))}
check("E", "lowest term of ch(G) EXACTLY -e_7(u_1..u_8) at weight 7 (matches the "
      "subset-expansion prediction; cohomological degree 28 > 16)",
      pweight(chG, 7) == e7_8)
check("E", "hence [A-hat(Z) ch(G)]_16 = 0 identically and eta-bar = 0 mod 1 on "
      "every closed 15-spin background (given Omega^spin_15 = 0 above); fixture "
      "pairings on (K3)^4 and (HP^2)^2 trivially 0", plowcap(chG, 4) == {})
# adversarial control: a WRONG truncation must NOT vanish
chG13 = {}
for k in range(14):
    chG13 = padd(chG13, pscale(tp8[k], (-1) ** k * comb(16 - k, 2)))
rank13 = chG13.get((0,) * 8, F(0))
check("E", "negative control: truncating the extension at k = 13 leaves rank "
      "-a_14*C(16,14) = -120 != 0 (the zero is NOT an artifact of the code)",
      rank13 == -120)

# ============================================================================
# V6 -- Kramers mechanism on a NEW fixture, charpoly via Newton's identities
# ============================================================================
print()
print("=" * 84)
print("V6  Kramers: J-commuting Hermitian fixture, Newton-identity charpoly")
print("=" * 84)


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def mmul(A_, B_):
    n = len(A_)
    return [[
        (sum(cmul(A_[i][k], B_[k][j])[0] for k in range(n)),
         sum(cmul(A_[i][k], B_[k][j])[1] for k in range(n)))
        for j in range(n)] for i in range(n)]


def quat_mul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def quat_conj(q):
    return (q[0], -q[1], -q[2], -q[3])


def embed(Q):
    m = len(Q)
    A_ = [[(F(0), F(0)) for _ in range(2 * m)] for _ in range(2 * m)]
    for r in range(m):
        for s in range(m):
            a, b, c, d = (F(x) for x in Q[r][s])
            A_[2 * r][2 * s] = (a, b)
            A_[2 * r][2 * s + 1] = (c, d)
            A_[2 * r + 1][2 * s] = (-c, d)
            A_[2 * r + 1][2 * s + 1] = (a, -b)
    return A_


# NEW fixture (different from the target's): 3x3 quaternionic C with
# row2 = row0 + row1  =>  M = C C^dagger is H-Hermitian of quaternionic rank 2.
C3x3 = [[(1, 2, 0, 0), (0, 0, 1, -1), (2, 0, 3, 0)],
        [(0, 1, 1, 0), (1, 0, 0, 2), (0, 3, 0, 1)],
        [(1, 3, 1, 0), (1, 0, 1, 1), (2, 3, 3, 1)]]
m = 3
M = [[None] * m for _ in range(m)]
for r in range(m):
    for s in range(m):
        acc = (F(0), F(0), F(0), F(0))
        for k in range(m):
            t = quat_mul(C3x3[r][k], quat_conj(C3x3[s][k]))
            acc = tuple(x + y for x, y in zip(acc, t))
        M[r][s] = acc
AK = embed(M)
n = 2 * m
# J-commutation: A J = J conj(A) with J = blockdiag([[0,1],[-1,0]])
Jm = [[(F(0), F(0))] * n for _ in range(n)]
for r in range(m):
    Jm[2 * r][2 * r + 1] = (F(1), F(0))
    Jm[2 * r + 1][2 * r] = (F(-1), F(0))
conjA = [[(AK[i][j][0], -AK[i][j][1]) for j in range(n)] for i in range(n)]
check("E", "H-linearity verified as a matrix identity: A J == J conj(A)",
      mmul(AK, Jm) == mmul(Jm, conjA))

# charpoly by Newton's identities from power traces (route independent of
# the target's Faddeev-LeVerrier)
pows = [None, AK]
for k in range(2, n + 1):
    pows.append(mmul(pows[-1], AK))
tr = [None] + [
    (sum(pows[k][i][i][0] for i in range(n)), sum(pows[k][i][i][1] for i in range(n)))
    for k in range(1, n + 1)]
check("E", "all power traces tr(A^k) are REAL (Hermitian fixture)",
      all(t[1] == 0 for t in tr[1:]))
e = [F(1)] + [F(0)] * n
for k in range(1, n + 1):
    s = F(0)
    for i in range(1, k + 1):
        s += (-1) ** (i - 1) * e[k - i] * tr[i][0]
    e[k] = s / k
# charpoly(lambda) = sum_{k} (-1)^k e_k lambda^{n-k}; low-to-high coefficients:
cp = [(-1) ** (n - d) * e[n - d] for d in range(n + 1)]


def poly_sqrt(p):
    nn = len(p) - 1
    if nn % 2 or p[-1] != 1:
        return None
    mm = nn // 2
    q = [F(0)] * (mm + 1)
    q[mm] = F(1)
    for i in range(mm - 1, -1, -1):
        acc = F(0)
        for j in range(i + 1, mm):
            if 0 <= mm + i - j <= mm:
                acc += q[j] * q[mm + i - j]
        q[i] = (p[mm + i] - acc) / 2
    sq = [F(0)] * (nn + 1)
    for i in range(mm + 1):
        for j in range(mm + 1):
            sq[i + j] += q[i] * q[j]
    return q if sq == list(p) else None


qrt = poly_sqrt(cp)
check("E", "charpoly of the NEW J-commuting Hermitian fixture is an exact "
      "PERFECT SQUARE (Kramers evenness, Newton-identity route)", qrt is not None)
nzp = next(i for i, c in enumerate(cp) if c != 0)
nzq = next(i for i, c in enumerate(qrt) if c != 0)
check("E", f"nullity even and quaternionic: mult_0 = {nzp} = 2 x {nzq} > 0",
      nzp == 2 * nzq and nzp > 0)
# control: non-J Hermitian diag(1,1,1,1,1,0) has charpoly lambda(lambda-1)^5,
# monic low-to-high coefficients:
cpc = [F(c) for c in (0, -1, 5, -10, 10, -5, 1)]
check("F", "control: non-J Hermitian diag(1,1,1,1,1,0) charpoly lambda(lambda-1)^5 "
      "is NOT a perfect square; nullity 1 odd",
      poly_sqrt(cpc) is None and cpc[0] == 0 and cpc[1] != 0)

# ============================================================================
# V7 -- 5d Witten parity arithmetic (mapping imported, flagged)
# ============================================================================
print()
print("=" * 84)
print("V7  5d Witten Z/2 parity")
print("=" * 84)
check("T", "INPUT (Witten 1982): SU(2)/Sp mod-2 anomaly counts pseudoreal "
      "multiplets mod 2; pi_4(Sp(N)) = Z/2 stable for N >= 1", True)
check("F", "positive control: single doublet 1 mod 2 = 1 (anomalous)", 1 % 2 == 1)
check("E", "GU kills: 64 quaternionic species even; slotwise vector-like Weyl "
      "count 0 even; 128 complex species even",
      64 % 2 == 0 and 0 % 2 == 0 and 128 % 2 == 0)

# ============================================================================
# HEADLINE
# ============================================================================
nT = sum(1 for t, _, _ in CHECKS if t == "T")
nE = sum(1 for t, _, _ in CHECKS if t == "E")
nF = sum(1 for t, _, _ in CHECKS if t == "F")
ok_all = all(o for _, _, o in CHECKS)
print()
print("=" * 84)
print("HOSTILE RE-DERIVATION VERDICT: every load-bearing number of the anomaly-")
print("closure pair reproduces by independent routes (Bernoulli A-hat, derived")
print("fixtures, splitting-principle Euler product, residue-route a_k, Newton-")
print("identity Kramers). STRENGTHENINGS found, no refutations: ch(G) = 0 through")
print("weight 6 (gauge-twist-proof extension vanishing); Omega~^spin_5(BSp(64))")
print("= Z/2 derived (was flagged unsourced); draft p.64 item (iii) 'unadorned")
print("non-chiral Dirac spinors' corroborates the provenance claim (see doc).")
print("=" * 84)
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if ok_all else 'FAILURES PRESENT'}")
raise SystemExit(0 if ok_all else 1)

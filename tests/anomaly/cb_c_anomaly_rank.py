#!/usr/bin/env python3
r"""CB-C conditional build: the 14D local anomaly system, carried SYMBOLICALLY in the
unknown fermion content U1.

UNKNOWN U1: the source action's chiral fermion content on Y^14, written in GU's own
native arena Omega^p(Y, /S), p = 0..14, as a virtual (signed-multiplicity) vector
    x = (x_0, ..., x_14) in Z^15,
x_p = (# of +chirality copies) - (# of -chirality copies) of Omega^p (x) S.

CONDITION (local 14D anomaly cancellation, Alvarez-Gaume-Witten / Green-Schwarz):
    I_16(x) := sum_p x_p * [A-hat(TY) ch(Lambda^p T_C) ch(S_gauge)]_16
must vanish AS A POLYNOMIAL IDENTITY in the characteristic classes (p_1..p_4 and the
gauge Casimir), i.e. every degree-16 monomial coefficient must vanish separately.

That is a LINEAR SYSTEM M x = 0. This script computes M exactly and returns its RANK
and KERNEL DIMENSION -- the PRE-2 "compute the dimension and exclude wholesale" move.

Exact rational arithmetic throughout (fractions.Fraction). No floats anywhere.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial, comb
from itertools import product

WMAX = 4  # weight 4 == form degree 16

# ----------------------------------------------------------------------------
# graded polynomial ring: variables P1,P2,P3,P4 (power sums of x_i^2) and Y (=y^2,
# the Sp(1) Cartan square). weights: P_k -> k, Y -> 1. truncate at total weight 4.
# monomial key = (e1, e2, e3, e4, eY)
# ----------------------------------------------------------------------------
def wt(k): return k[0] + 2*k[1] + 3*k[2] + 4*k[3] + k[4]
ONE = {(0,0,0,0,0): F(1)}
ZERO = {}

def padd(a, b):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, F(0)) + v
    return {k: v for k, v in o.items() if v != 0}

def pscale(a, c):
    return {k: v*c for k, v in a.items() if v*c != 0}

def pmul(a, b):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(ka[i] + kb[i] for i in range(5))
            if wt(k) <= WMAX:
                o[k] = o.get(k, F(0)) + va*vb
    return {k: v for k, v in o.items() if v != 0}

def pexp(a):
    """exp of a graded quantity with zero constant term, truncated at weight WMAX."""
    assert a.get((0,0,0,0,0), F(0)) == 0
    acc, term = dict(ONE), dict(ONE)
    for n in range(1, WMAX+1):
        term = pmul(term, a)
        acc = padd(acc, pscale(term, F(1, factorial(n))))
    return acc

# ----------------------------------------------------------------------------
# t-series: dict from t-power -> graded polynomial, truncated at t^14
# ----------------------------------------------------------------------------
TMAX = 14
def tmul(A, B):
    o = {}
    for i, a in A.items():
        for j, b in B.items():
            if i + j <= TMAX:
                o[i+j] = padd(o.get(i+j, {}), pmul(a, b))
    return {k: v for k, v in o.items() if v}

def tadd(A, B):
    o = dict(A)
    for k, v in B.items():
        o[k] = padd(o.get(k, {}), v)
    return {k: v for k, v in o.items() if v}

def tscale(A, c):
    return {k: pscale(v, c) for k, v in A.items() if pscale(v, c)}

def texp(A):
    """exp of a t-series whose t^0 term has zero constant part."""
    acc = {0: dict(ONE)}
    term = {0: dict(ONE)}
    # nilpotency: every term of A has weight >= 1, and weight is capped at WMAX,
    # so A^n = 0 for n > WMAX.
    for n in range(1, WMAX+1):
        term = tmul(term, A)
        acc = tadd(acc, tscale(term, F(1, factorial(n))))
    return acc

# ----------------------------------------------------------------------------
# 1. log A-hat = sum_k g_k P_k     (A-hat char series (x/2)/sinh(x/2))
# ----------------------------------------------------------------------------
def ahat_g():
    h = [F(1, 4**m * factorial(2*m+1)) for m in range(WMAX+1)]  # sinh(x/2)/(x/2)
    w = [F(0)] + h[1:]
    def smul(a, b):
        r = [F(0)]*(WMAX+1)
        for i in range(WMAX+1):
            if a[i] == 0: continue
            for j in range(WMAX+1-i): r[i+j] += a[i]*b[j]
        return r
    logh = [F(0)]*(WMAX+1); wn = [F(1)]+[F(0)]*WMAX
    for n in range(1, WMAX+1):
        wn = smul(wn, w); c = F((-1)**(n+1), n)
        for i in range(WMAX+1): logh[i] += c*wn[i]
    return [F(0)] + [-logh[k] for k in range(1, WMAX+1)]

G = ahat_g()
def Pvar(k):
    e = [0,0,0,0,0]; e[k-1] = 1
    return {tuple(e): F(1)}
LOG_AHAT = {}
for k in range(1, WMAX+1):
    LOG_AHAT = padd(LOG_AHAT, pscale(Pvar(k), G[k]))

# ----------------------------------------------------------------------------
# 2. sum_i log(1 + u*c(x_i)),  c(x) = cosh(x) - 1 = sum_{m>=1} x^{2m}/(2m)!
#    sum_i c(x_i)^n = sum_{M>=n} C[n][M] * P_M ,
#    C[n][M] = sum over compositions m_1+..+m_n = M, m_j>=1 of 1/prod (2 m_j)!
# ----------------------------------------------------------------------------
def C_nM(n, M):
    tot = F(0)
    def rec(j, rem, acc):
        nonlocal tot
        if j == n:
            if rem == 0:
                tot += acc
            return
        for m in range(1, rem - (n-1-j) + 1):
            rec(j+1, rem-m, acc * F(1, factorial(2*m)))
    rec(0, M, F(1))
    return tot

# u = 2t/(1+t)^2 as a t-series (scalar coefficients, weight 0)
def u_series():
    o = {}
    for j in range(0, TMAX):
        p = j+1
        if p <= TMAX:
            o[p] = {(0,0,0,0,0): F(2 * (-1)**j * (j+1))}
    return o

U = u_series()
def tpow(A, n):
    r = {0: dict(ONE)}
    for _ in range(n): r = tmul(r, A)
    return r

LOG_GEN = {}   # sum_i log(1 + u c(x_i)) as a t-series of graded polys
Upow = {0: dict(ONE)}
for n in range(1, WMAX+1):
    Upow = tmul(Upow, U)
    inner = {}
    for M in range(n, WMAX+1):
        c = C_nM(n, M)
        if c:
            inner = padd(inner, pscale(Pvar(M), c))
    if inner:
        LOG_GEN = tadd(LOG_GEN, tscale(tmul(Upow, {0: inner}), F((-1)**(n+1), n)))

# ----------------------------------------------------------------------------
# 3. A-hat * sum_p t^p ch(Lambda^p T_C)  =  (1+t)^14 * exp( log A-hat + LOG_GEN )
# ----------------------------------------------------------------------------
EXPPART = texp(tadd({0: LOG_AHAT}, LOG_GEN))
ONEPLUST14 = {p: {(0,0,0,0,0): F(comb(14, p))} for p in range(0, 15)}
AHAT_LAMBDA = tmul(ONEPLUST14, EXPPART)   # t^p coefficient = [A-hat ch(Lambda^p T_C)]

# ----------------------------------------------------------------------------
# 4. gauge factor ch(S) under the Sp(1)=right-H commutant reading:
#    S = H^64 = 64 copies of the 2-dim fundamental, weights {+-y}
#    ch(S) = 64 (e^y + e^-y) = 128 cosh(y) = 128 sum_m Y^m/(2m)! , Y := y^2 (weight 1)
# ----------------------------------------------------------------------------
def Yvar(m):
    return {(0,0,0,0,m): F(1)}
CH_S = {}
for m in range(0, WMAX+1):
    CH_S = padd(CH_S, pscale(Yvar(m), F(128, factorial(2*m))))

# ----------------------------------------------------------------------------
# 5. P-monomials -> p-monomials (Newton), then restrict to weight exactly 4
# ----------------------------------------------------------------------------
# p_j == e_j(x_i^2) ; power sums P_k in terms of p_j:
NEWTON = {
    1: {(1,0,0,0): F(1)},
    2: {(2,0,0,0): F(1), (0,1,0,0): F(-2)},
    3: {(3,0,0,0): F(1), (1,1,0,0): F(-3), (0,0,1,0): F(3)},
    4: {(4,0,0,0): F(1), (2,1,0,0): F(-4), (1,0,1,0): F(4), (0,2,0,0): F(2), (0,0,0,1): F(-4)},
}
def pwt(k): return k[0] + 2*k[1] + 3*k[2] + 4*k[3]
def qmul(a, b):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(ka[i]+kb[i] for i in range(4))
            if pwt(k) <= WMAX:
                o[k] = o.get(k, F(0)) + va*vb
    return {k: v for k, v in o.items() if v != 0}

def to_p_basis(poly):
    """graded poly in (P1..P4, Y) -> dict from (p-monomial, Ypower) -> Fraction,
    keeping only total weight exactly 4."""
    out = {}
    for key, val in poly.items():
        if wt(key) != WMAX:
            continue
        e1, e2, e3, e4, eY = key
        acc = {(0,0,0,0): F(1)}
        for k, e in ((1,e1),(2,e2),(3,e3),(4,e4)):
            for _ in range(e):
                acc = qmul(acc, NEWTON[k])
        for pk, pv in acc.items():
            kk = (pk, eY)
            out[kk] = out.get(kk, F(0)) + pv*val
    return {k: v for k, v in out.items() if v != 0}

PMON = {(4,0,0,0): "p1^4", (2,1,0,0): "p1^2 p2", (0,2,0,0): "p2^2",
        (1,0,1,0): "p1 p3", (0,0,0,1): "p4"}

# ----------------------------------------------------------------------------
# exact rank / kernel over Q
# ----------------------------------------------------------------------------
def rref(M):
    M = [row[:] for row in M]
    rows, cols = len(M), (len(M[0]) if M else 0)
    piv = []; r = 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][c]; M[r] = [v/pv for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [M[i][j] - f*M[r][j] for j in range(cols)]
        piv.append(c); r += 1
        if r == rows: break
    return M, piv

def kernel_basis(M, ncols):
    R, piv = rref(M)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)]*ncols; v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        basis.append(v)
    return basis, piv, free


def main():
    print("="*78)
    print("CB-C : the 14D local anomaly system as a LINEAR SYSTEM in the unknown U1")
    print("="*78)

    # ---- per-slot GRAVITY-ONLY densities D_p = [A-hat ch(Lambda^p T_C)]_16 -----
    Dgrav = {}
    for p in range(0, 15):
        Dgrav[p] = to_p_basis(AHAT_LAMBDA.get(p, {}))

    # VALIDATION 1: D_0 == [A-hat]_16 == AGW table over 464486400
    D = 464486400
    agw = {(4,0,0,0): 381, (2,1,0,0): -904, (0,2,0,0): 208, (1,0,1,0): 512, (0,0,0,1): -192}
    print("\n[V1] D_0 = [A-hat(TY14)]_16 vs Alvarez-Gaume-Witten table (num over %d):" % D)
    ok = True
    for mk, name in PMON.items():
        got = Dgrav[0].get((mk, 0), F(0))*D
        assert got.denominator == 1
        m = (int(got) == agw[mk]); ok = ok and m
        print(f"     {name:9s} computed {int(got):+6d}   AGW {agw[mk]:+6d}   {'OK' if m else 'MISMATCH'}")
    assert ok, "A-hat degree-16 mismatch"

    # VALIDATION 2: alternating sum over the FULL tower is identically zero
    alt = {}
    for p in range(0, 15):
        for k, v in Dgrav[p].items():
            alt[k] = alt.get(k, F(0)) + ((-1)**p)*v
    alt = {k: v for k, v in alt.items() if v != 0}
    print(f"\n[V2] alternating sum sum_p (-1)^p D_p over the FULL tower = "
          f"{'IDENTICALLY ZERO' if not alt else alt}")
    assert not alt, "the C3 identity failed"

    # VALIDATION 3: the honest C0 p4 coefficient (repo: 493/2419200 honest vs
    # 13/2419200 multiplicity-convention).  C0 = Omega^0 (x) S^+ + Omega^1 (x) S^-
    c0_p4 = Dgrav[0].get(((0,0,0,1), 0), F(0)) - Dgrav[1].get(((0,0,0,1), 0), F(0))
    print(f"\n[V3] honest C0 p4 coefficient (grav-only, per unit dim S) = {c0_p4}")
    print(f"     repo record (global-anomaly-leg): honest 493/2419200 vs convention 13/2419200")
    print(f"     computed * (-1) = {-c0_p4}   ; 493/2419200 = {F(493,2419200)}")

    # ---- MATRIX A : gravity-only, 5 rows x 15 cols ---------------------------
    rowsA = sorted(PMON.keys(), key=lambda k: (-k[0], -k[1]))
    MA = [[Dgrav[p].get((mk, 0), F(0)) for p in range(15)] for mk in rowsA]
    RA, pivA = rref(MA)
    kerA, _, freeA = kernel_basis(MA, 15)
    print("\n" + "-"*78)
    print("MATRIX A -- gravitational channel only (5 conditions, 15 unknowns)")
    print("-"*78)
    print(f"  rank = {len(pivA)}    kernel dim = {15 - len(pivA)}")
    print(f"  pivot slots p = {pivA}   free slots p = {freeA}")

    # ---- MATRIX B : gravity + Sp(1) gauge, 12 rows x 15 cols -----------------
    Dfull = {}
    for p in range(0, 15):
        Dfull[p] = to_p_basis(pmul(AHAT_LAMBDA.get(p, {}), CH_S)) if AHAT_LAMBDA.get(p) else {}
    keys = sorted({k for p in range(15) for k in Dfull[p]},
                  key=lambda k: (k[1], -k[0][0], -k[0][1]))
    MB = [[Dfull[p].get(k, F(0)) for p in range(15)] for k in keys]
    RB, pivB = rref(MB)
    kerB, _, freeB = kernel_basis(MB, 15)
    print("\n" + "-"*78)
    print("MATRIX B -- gravity + Sp(1)=right-H gauge channel (%d conditions, 15 unknowns)" % len(keys))
    print("-"*78)
    print("  degree-16 monomial basis (p-monomial , power of Y=y^2):")
    for k in keys:
        print(f"     {PMON.get(k[0], str(k[0])):9s} * Y^{k[1]}")
    print(f"\n  rank = {len(pivB)}    kernel dim = {15 - len(pivB)}")
    print(f"  pivot slots p = {pivB}   free slots p = {freeB}")

    # ---- the kernel, spelled out --------------------------------------------
    # net chirality in the repo's (MOVE-1) sense: W = sum_p x_p * rank(Lambda^p) = sum_p x_p C(14,p)
    def Wof(x): return sum(F(c)*comb(14, p) for p, c in enumerate(x))

    print("\n  KERNEL BASIS (anomaly-free contents, as integer vectors x_0..x_14):")
    import math
    ker_int = []
    for v in kerB:
        den = 1
        for c in v:
            den = den*c.denominator//math.gcd(den, c.denominator)
        w = [int(c*den) for c in v]
        g = 0
        for c in w: g = math.gcd(g, abs(c))
        if g: w = [c//g for c in w]
        ker_int.append(w)
        print("     " + str(w) + f"   W = sum_p x_p C(14,p) = {Wof(w)}")

    # ---- is W = sum_p x_p C(14,p) forced to zero on the kernel? --------------
    print("\n  Is the repo's net chirality W forced to 0 by the anomaly system?")
    Ws = [Wof(v) for v in ker_int]
    forced = all(w == 0 for w in Ws)
    print(f"     ==> W identically zero on the whole anomaly-free kernel? {forced}")
    if not forced:
        print("     ==> NO: W is a NONTRIVIAL linear functional on the 15-dim content space")
        print("         that is NOT in the row space of the anomaly system.")
        # is W in the row space? test by appending W as a row and seeing if rank grows
        Wrow = [F(comb(14, p)) for p in range(15)]
        MB2 = MB + [Wrow]
        _, piv2 = rref(MB2)
        print(f"         rank(anomaly rows) = {len(pivB)} ; rank(anomaly rows + W row) = {len(piv2)}")
        print(f"         ==> W {'IS' if len(piv2)==len(pivB) else 'IS NOT'} implied by anomaly cancellation.")

    # ---- named GU contents, checked against the system ----------------------
    print("\n" + "-"*78)
    print("NAMED GU CONTENTS evaluated against MATRIX B")
    print("-"*78)
    named = {
        "C0  Om^0(x)S^+ + Om^1(x)S^-  (chiral truncation, IMPORT)": [1,-1]+[0]*13,
        "C0m mirror                                              ": [-1,1]+[0]*13,
        "C1  draft-literal Sec 9.3 full /S (nu, zeta)             ": [0]*15,
        "C3  alternating full DK tower Om^p (x) S^{(-1)^p}        ": [(-1)**p for p in range(15)],
        "C4  Bianconi-style 0+1+2 alternating                     ": [1,-1,1]+[0]*12,
        "C5c chiral 4-slot Hodge-paired (+,-,-,+) on 0,1,13,14    ": [1,-1]+[0]*11+[-1,1],
        "kerGamma-refined C0: Om^0(x)S^+ + (Om^1 - Om^0)(x)S^-    ": [2,-1]+[0]*13,
    }
    for name, x in named.items():
        res = {}
        for i, k in enumerate(keys):
            val = sum(MB[i][p]*x[p] for p in range(15))
            if val: res[k] = val
        p4only = res.get(((0,0,0,1), 0), F(0))
        status = "CANCELS (all 12 coefficients zero)" if not res else \
                 f"SURVIVES ({len(res)} of {len(keys)} coefficients nonzero)"
        print(f"  {name}")
        print(f"      W = {int(Wof(x)):+5d}   pure-grav p4 coeff = {p4only}   -> {status}")

    # ---- structural facts about the system ----------------------------------
    print("\n" + "-"*78)
    print("STRUCTURE OF THE SYSTEM")
    print("-"*78)

    # Hodge symmetry D_p == D_{14-p}
    hodge = all(Dfull[p] == Dfull[14-p] for p in range(15))
    print(f"  Hodge symmetry  D_p == D_(14-p)  for all p:  {hodge}")

    # rank restricted to the Hodge-symmetric sector (8 combinations)
    sym_cols = [[Dfull[p].get(k, F(0)) * (1 if p == 7 else 1) for k in keys] for p in range(8)]
    MS = [[sym_cols[p][i] for p in range(8)] for i in range(len(keys))]
    _, pivS = rref(MS)
    print(f"  rank on the 8 Hodge-symmetric combinations s_p = x_p + x_(14-p): {len(pivS)}")
    print(f"     => 7 antisymmetric free directions + ({8} - {len(pivS)}) symmetric = "
          f"{7 + 8 - len(pivS)} total kernel dim (cross-check {15-len(pivB)})")

    # W in the row space?
    Wrow = [F(comb(14, p)) for p in range(15)]
    _, pivW = rref(MB + [Wrow])
    print(f"\n  rank(anomaly rows) = {len(pivB)};  rank(anomaly rows + W-row) = {len(pivW)}")
    print(f"  ==> the net-chirality functional W = sum_p x_p C(14,p) "
          f"{'IS' if len(pivW) == len(pivB) else 'IS NOT'} in the row space,")
    print(f"      i.e. W = 0 is {'DERIVED FROM' if len(pivW)==len(pivB) else 'INDEPENDENT OF'} "
          f"local anomaly cancellation.")

    # necessity-not-sufficiency witness: a W = 0 content that is still anomalous
    print("\n  NECESSITY-NOT-SUFFICIENCY WITNESS (a content with W = 0 that is still anomalous):")
    wit = [0]*15
    wit[0] = comb(14, 2); wit[2] = -1        # W = C(14,2)*1 + (-1)*C(14,2) = 0
    resid = {k: sum(MB[i][p]*wit[p] for p in range(15)) for i, k in enumerate(keys)}
    resid = {k: v for k, v in resid.items() if v != 0}
    print(f"     x = 91*[Om^0 (x) S^+] - 1*[Om^2 (x) S^+]   ->  W = {Wof(wit)}")
    print(f"     nonzero degree-16 coefficients: {len(resid)} of {len(keys)}  "
          f"(pure-grav p4 = {resid.get(((0,0,0,1),0), F(0))})")
    print(f"     ==> W = 0 is NECESSARY but NOT SUFFICIENT: {len(resid) > 0}")

    # positive control: a single chiral slot must be anomalous
    for pc in (0, 7):
        v = [0]*15; v[pc] = 1
        r = sum(1 for i in range(len(keys)) if sum(MB[i][p]*v[p] for p in range(15)) != 0)
        print(f"  [PC] single chiral slot Om^{pc} (x) S^+ : {r}/{len(keys)} coefficients nonzero "
              f"(must be > 0): {'OK' if r > 0 else 'FAIL'}")

    # gauge channel adds nothing beyond gravity
    print(f"\n  rank(gravity only) = {len(pivA)} ; rank(gravity + Sp(1) gauge) = {len(pivB)}")
    print(f"  ==> the Sp(1)=right-H gauge channel contributes "
          f"{len(pivB)-len(pivA)} independent condition(s) beyond gravity.")

    print("\n" + "="*78)
    print("DONE (exact rational arithmetic; no floats)")
    print("="*78)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
r"""MOVE-1 terminal recheck: pure-grav [A-hat(TY14)]_16 + Sp(2n) octic factorizability
under the Sp(64) reading vs the Sp(1)=right-H commutant reading.

STANDALONE. Exact rational arithmetic (fractions.Fraction) for every load-bearing
number. numpy used ONLY for the Jacobian-rank independence test (a rank of a real
matrix), never for a claimed coefficient.

WHAT THIS DECIDES
-----------------
The repo's tests/sp64_octic_trace_i16.py concluded the LOCAL 14D anomaly does NOT
Green-Schwarz factorize, driven by (a) an irreducible Sp(64) octic Casimir
tr_S F^8|prim and (b) the pure-gravitational tr R^8 (p4 of [A-hat]_16). The triage
(lab/roadmap/triage-pass-...-2026-06-30.md, MOVE-1) flags that the repo's OWN
commutant note (tests/shiab_selector_sp64.py L38-43) says the genuine Clifford
commutant gauge group is Sp(1)=right-H, NOT Sp(64). Under Sp(1) the module
S = H^64 is 64 copies of the 2-dim fundamental of Sp(1) (rank 1), so its octic
CANNOT contain an independent order-8 Casimir. Question: does the gauge octic
irreducibility -- and the headline non-factorizability -- FLIP under Sp(1)?

We recompute the octic decomposition under BOTH readings and emit the two booleans.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial, comb
import numpy as np

# ============================================================================
# PART A. [A-hat(TY14)]_16 exact, cross-checked vs the Alvarez-Gaume-Witten table.
#   A-hat has char. series Q(x)=(x/2)/sinh(x/2). log A-hat = sum_k g_k P_k with
#   P_k = sum_i (x_i^2)^k the power sums; Newton -> Pontryagin p_j = e_j(x_i^2).
# ============================================================================
WMAX = 4
KEY0 = (0, 0, 0, 0)
def wt(k): return k[0] + 2*k[1] + 3*k[2] + 4*k[3]
def padd(a, b):
    o = dict(a)
    for k, v in b.items(): o[k] = o.get(k, F(0)) + v
    return {k: v for k, v in o.items() if v != 0}
def pscale(a, c): return {k: v*c for k, v in a.items() if v*c != 0}
def pmul(a, b):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = (ka[0]+kb[0], ka[1]+kb[1], ka[2]+kb[2], ka[3]+kb[3])
            if wt(k) <= WMAX: o[k] = o.get(k, F(0)) + va*vb
    return {k: v for k, v in o.items() if v != 0}
# Newton: power sums of x_i^2 in terms of p_j = e_j(x_i^2)
P = {1: {(1,0,0,0): F(1)},
     2: {(2,0,0,0): F(1), (0,1,0,0): F(-2)},
     3: {(3,0,0,0): F(1), (1,1,0,0): F(-3), (0,0,1,0): F(3)},
     4: {(4,0,0,0): F(1), (2,1,0,0): F(-4), (1,0,1,0): F(4), (0,2,0,0): F(2), (0,0,0,1): F(-4)}}
def g_coeffs():
    h = [F(1, 4**m * factorial(2*m+1)) for m in range(WMAX+1)]   # sinh(x/2)/(x/2) series
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
def ahat_graded():
    g = g_coeffs(); L = {}
    for k in range(1, WMAX+1): L = padd(L, pscale(P[k], g[k]))
    acc = {KEY0: F(1)}; Lp = {KEY0: F(1)}
    for n in range(1, WMAX+1):
        Lp = pmul(Lp, L); acc = padd(acc, pscale(Lp, F(1, factorial(n))))
    graded = {w: {} for w in range(WMAX+1)}
    for k, v in acc.items(): graded[wt(k)][k] = v
    return graded

def part_A():
    print("="*80)
    print("PART A  [A-hat(TY14)]_16 exact  (cross-check vs Alvarez-Gaume-Witten table)")
    print("="*80)
    G = ahat_graded()
    a4, a8, a12, a16 = G[1], G[2], G[3], G[4]
    # lower canonical coefficients
    assert a4 == {(1,0,0,0): F(-1,24)}, a4
    assert a8 == {(2,0,0,0): F(7,5760), (0,1,0,0): F(-4,5760)}, a8
    assert a12 == {(3,0,0,0): F(-31,967680), (1,1,0,0): F(44,967680), (0,0,1,0): F(-16,967680)}, a12
    print("  lower coeffs OK: [A-hat]_4=-p1/24, [A-hat]_8=(7p1^2-4p2)/5760,")
    print("                   [A-hat]_12=(-31p1^3+44p1p2-16p3)/967680")
    # the 5 degree-16 coefficients over the AGW common denominator 464486400
    D = 464486400
    mono = {(4,0,0,0): "p1^4", (2,1,0,0): "p1^2 p2", (0,2,0,0): "p2^2",
            (1,0,1,0): "p1 p3", (0,0,0,1): "p4"}
    agw = {(4,0,0,0): 381, (2,1,0,0): -904, (0,2,0,0): 208, (1,0,1,0): 512, (0,0,0,1): -192}
    print(f"  [A-hat]_16 numerators over {D} (computed vs AGW literature):")
    ok16 = True
    for k in mono:
        num = a16.get(k, F(0)) * D
        assert num.denominator == 1
        match = (int(num) == agw[k]); ok16 = ok16 and match
        print(f"     {mono[k]:9s}: computed {int(num):+5d}   AGW {agw[k]:+5d}   {'OK' if match else 'MISMATCH'}")
    assert ok16, "degree-16 A-hat coefficients disagree with AGW"
    # independent end-to-end index checks
    A = -48
    pontK3 = {(4,0,0,0):24,(2,1,0,0):12,(0,2,0,0):6,(1,0,1,0):4,(0,0,0,1):1}
    idxK3 = sum(a16.get(k,F(0))*m for k,m in pontK3.items())*(A**4)
    pontHP = {(4,0,0,0):96,(2,1,0,0):88,(0,2,0,0):114,(1,0,1,0):56,(0,0,0,1):49}
    idxHP = sum(a16.get(k,F(0))*m for k,m in pontHP.items())
    assert idxK3 == 16, idxK3
    assert idxHP == 0, idxHP
    print(f"  end-to-end indices: A-hat[(K3)^4]={idxK3} (=2^4=16 OK), A-hat[(HP^2)^2]={idxHP} (=0 OK)")
    p4_grav = a16[(0,0,0,1)]
    print(f"  ==> gravitational irreducible p4 (~tr R^8) coeff = {p4_grav}  (!= 0)")
    return p4_grav

# ============================================================================
# PART B. Octic trace decomposition for the module S = H^64 under two readings.
#   General fact: for a weight system {w_a}, Str_S F^{2m} = sum_a w_a^{2m}.
#   We decompose the octic (m=4) into the primitive power-sum basis of the
#   relevant Cartan and split {independent order-8 Casimir} vs {products}.
# ============================================================================
def partitions_weight(m, kmax):
    res = []
    def rec(k, rem, acc):
        if k > kmax:
            if rem == 0: res.append(tuple(acc))
            return
        for e in range(rem//k + 1): rec(k+1, rem-k*e, acc+[e])
    rec(1, m, []); return res
def Pmono(expo, xs):
    v = F(1)
    for k, e in enumerate(expo, 1):
        if e:
            Pk = sum((x**(2*k) for x in xs), F(0)); v *= Pk**e
    return v
def solve_exact(Arows, b):
    m = len(Arows); n = len(Arows[0])
    M = [[F(Arows[i][j]) for j in range(n)]+[F(b[i])] for i in range(m)]
    piv = []; col = 0; r = 0
    while r < m and col < n:
        pr = next((i for i in range(r, m) if M[i][col] != 0), None)
        if pr is None: col += 1; continue
        M[r], M[pr] = M[pr], M[r]; pv = M[r][col]; M[r] = [v/pv for v in M[r]]
        for i in range(m):
            if i != r and M[i][col] != 0:
                f = M[i][col]; M[i] = [M[i][j]-f*M[r][j] for j in range(n+1)]
        piv.append(col); r += 1; col += 1
    x = [F(0)]*n
    for i, c in enumerate(piv): x[c] = M[i][n]
    for i in range(m):
        if sum(Arows[i][j]*x[j] for j in range(n)) != b[i]:
            raise ValueError("trace not a polynomial in P_1..P_kmax")
    return x
def decompose_octic(trace_at, nvars, seed=12345):
    """Express the degree-8 (m=4) symmetric trace exactly in the power-sum monomial
    basis of weight 4 over 'nvars' Cartan variables."""
    monos = partitions_weight(4, 4)
    rng = np.random.RandomState(seed)
    rows, rhs = [], []
    for _ in range(len(monos)+4):
        xs = [F(int(rng.randint(1,50)), int(rng.randint(1,7))) for _ in range(nvars)]
        rows.append([Pmono(e, xs) for e in monos]); rhs.append(trace_at(xs))
    coeffs = solve_exact(rows, rhs)
    return {monos[i]: coeffs[i] for i in range(len(monos)) if coeffs[i] != 0}
def fmt(coeffs):
    nm = {1:"P1",2:"P2",3:"P3",4:"P4"}
    def m(e):
        p = [nm[k] if v==1 else f"{nm[k]}^{v}" for k,v in enumerate(e,1) if v]
        return "*".join(p) if p else "1"
    return "  ".join(f"({c}){m(e)}" for e,c in sorted(coeffs.items()))
def primitive_octic(coeffs):
    """Coeff of the lone P4 monomial (0,0,0,1) = the independent order-8 Casimir."""
    return coeffs.get((0,0,0,1), F(0))
def jac_rank(vars_vals):
    """Rank of the Jacobian of (P1,P2,P3,P4) wrt the Cartan variables. Rank 4 <=>
    P4 functionally independent <=> a genuine order-8 Casimir exists."""
    x = np.array(vars_vals, float); J = np.zeros((4, len(x)))
    for k in range(1,5): J[k-1,:] = 2*k*x**(2*k-1)
    return int(np.linalg.matrix_rank(J, tol=1e-9))

def part_B():
    print("\n" + "="*80)
    print("PART B  octic decomposition of S = H^64 under the two gauge-group readings")
    print("="*80)

    # ---- Reading 1: Sp(64) = U(64,H) fundamental. Weights {+-x_1,...,+-x_32}. rank 32.
    nSp = 32
    tr64 = lambda xs: 2*sum((x**8 for x in xs), F(0))   # Str_S F^8 = sum_{+-x} (+-x)^8 = 2 sum x^8
    oc64 = decompose_octic(tr64, nSp)
    prim64 = primitive_octic(oc64)
    red64 = {e:c for e,c in oc64.items() if e != (0,0,0,1)}
    rk64 = jac_rank(list(range(1, nSp+1)))
    ctrl = jac_rank([1,2,3])            # Sp(6) rank-3 control: P4 must be dependent -> rank 3
    irr64 = (prim64 != 0) and (rk64 == 4)
    print("\n  [Reading 1: Sp(64)=U(64,H), S=fundamental H^64, rank 32]")
    print(f"     Str_S F^8 = {fmt(oc64)}   (power-sum basis)")
    print(f"     primitive order-8 Casimir (P4) coeff = {prim64}")
    print(f"     reducible/product part               = {fmt(red64) if red64 else '0 (pure primitive)'}")
    print(f"     Jacobian rank(P1..P4) at rank 32     = {rk64}  (control Sp(6) rank-3 -> {ctrl})")
    assert ctrl == 3 and rk64 == 4, "irreducibility self-check failed"
    print(f"     ==> gauge octic IRREDUCIBLE (independent order-8 Casimir present)? {irr64}")

    # ---- Reading 2: Sp(1)=right-H commutant. S=H^64 = 64 copies of the 2-dim fund. rank 1.
    #      Weights {+-y} each with multiplicity 64. Cartan has ONE variable.
    tr1 = lambda xs: 64*(2*sum((x**8 for x in xs), F(0)))   # 64 copies, weights {+-y}
    oc1 = decompose_octic(tr1, 1)       # nvars=1
    prim1 = primitive_octic(oc1)
    red1 = {e:c for e,c in oc1.items() if e != (0,0,0,1)}
    rk1 = jac_rank([1.0])               # rank-1 Cartan: only P1 independent
    irr1 = (rk1 == 4)                    # independence is decided by the Jacobian rank ONLY
    print("\n  [Reading 2: Sp(1)=right-H commutant, S=H^64=64x(2-dim fund), rank 1]")
    print(f"     Str_S F^8 (as a function of the single Cartan var y) = 128*y^8 = 128*(y^2)^4")
    print(f"     NOTE: at rank 1 the power-sum basis {{P4,P1^4,P1^2P2,...}} is DEGENERATE")
    print(f"           (all equal y^8), so the formal solver attribution ({fmt(oc1)}) is")
    print(f"           basis-arbitrary and NOT a real independent Casimir.")
    print(f"     Jacobian rank(P1..P4) at rank 1      = {rk1}  (P4=(P1)^4 => NOT independent)")
    assert rk1 == 1, "rank-1 self-check failed"
    print(f"     ==> gauge octic IRREDUCIBLE? {irr1}   (octic = pure product of quadratics)")

    # normalize the primitive coeff to textbook C_8 = tr_v F^8 = 2 P4 units for the assembly.
    # Only meaningful when the octic is actually irreducible; else there is NO gauge octic term.
    prim64_C8 = prim64/2 if irr64 else F(0)     # = 1
    prim1_C8  = F(0)                              # Sp(1) octic reducible -> no irreducible term
    return irr64, irr1, prim64_C8, prim1_C8

# ============================================================================
# PART C. Total local I_16 factorizability under both readings.
#   Assumed GU content Omega^0(x)S^+ + Omega^1(x)S^-  (repo canon).
#   gauge irreducible octic coeff (x (2pi)^-8) = (n_+ - n_-)/8! * prim_C8
#   grav irreducible tr R^8 coeff             = dim(S)*(n_+ - n_-) * p4_grav
#   Total local anomaly GS-factorizes  <=>  BOTH irreducible coeffs vanish.
# ============================================================================
def part_C(p4_grav, prim64_C8, prim1_C8):
    print("\n" + "="*80)
    print("PART C  total local I_16 Green-Schwarz factorizability (both readings)")
    print("="*80)
    rank0, rank1 = comb(14,0), comb(14,1)     # Omega^0 -> 1, Omega^1 -> 14
    W = (+1)*rank0 + (-1)*rank1                # net chiral weight n_+ - n_- = -13
    dimS = 64                                   # dim of S as H^64 (reading-independent vector space)
    Ngrav = dimS*W                              # = -832
    grav_irr = F(Ngrav)*p4_grav                 # reading-INDEPENDENT
    print(f"  assumed content Omega^0(x)S^+ (rank {rank0}) + Omega^1(x)S^- (rank {rank1}); "
          f"n_+ - n_- = {W}")
    print(f"  gravitational tr R^8 coeff = dim(S)*(n_+-n_-)*p4 = {Ngrav}*{p4_grav} = {grav_irr}  "
          f"(reading-INDEPENDENT)")
    out = {}
    for tag, primC8 in (("Sp(64)", prim64_C8), ("Sp(1)=right-H", prim1_C8)):
        gauge_irr = F(W)*F(1, factorial(8))*primC8
        gauge_block = (gauge_irr != 0)
        grav_block  = (grav_irr != 0)
        factorizable = (not gauge_block) and (not grav_block)
        out[tag] = dict(gauge_irr=gauge_irr, gauge_block=gauge_block,
                        grav_block=grav_block, factorizable=factorizable)
        print(f"\n  reading = {tag}:")
        print(f"     gauge  tr_S F^8|prim coeff = (n_+-n_-)/8! * {primC8} = {gauge_irr}"
              f"   -> gauge block? {gauge_block}")
        print(f"     grav   tr R^8       coeff = {grav_irr}                 -> grav  block? {grav_block}")
        print(f"     ==> total local GS-factorizable? {factorizable}")
    return out

def main():
    p4_grav = part_A()
    irr64, irr1, prim64_C8, prim1_C8 = part_B()
    tot = part_C(p4_grav, prim64_C8, prim1_C8)

    print("\n" + "="*80)
    print("TERMINAL SELF-CHECK + VERDICT")
    print("="*80)
    print(f"  GAUGE-OCTIC-IRREDUCIBLE booleans:")
    print(f"     Sp(64) reading      : {irr64}")
    print(f"     Sp(1)=right-H reading: {irr1}")
    gauge_flips = (irr64 != irr1)
    print(f"     gauge octic irreducibility FLIPS between readings? {gauge_flips}")
    print(f"  TOTAL-LOCAL-FACTORIZABLE booleans:")
    print(f"     Sp(64) reading      : {tot['Sp(64)']['factorizable']}")
    print(f"     Sp(1)=right-H reading: {tot['Sp(1)=right-H']['factorizable']}")
    headline_flips = (tot['Sp(64)']['factorizable'] != tot['Sp(1)=right-H']['factorizable'])
    print(f"     total non-factorizability HEADLINE flips? {headline_flips}")
    # assertions pinning the terminal claims
    assert irr64 is True and irr1 is False, "gauge octic should flip True->False"
    assert tot['Sp(64)']['factorizable'] is False
    assert tot['Sp(1)=right-H']['factorizable'] is False   # grav channel keeps it False
    assert gauge_flips is True and headline_flips is False
    print("\n  VERDICT (PARTIAL):")
    print("   * The Sp(64) GAUGE octic red flag IS an artifact of the gauge-group reading:")
    print("     under the genuine Sp(1)=right-H commutant it becomes 128*(y^2)^4 -- a pure")
    print("     product of quadratics, GS-reducible, NO independent order-8 Casimir. FLIPS.")
    print("   * BUT the pure-gravitational tr R^8 (p4) irreducible is READING-INDEPENDENT")
    print("     and nonzero for the assumed net chiral count (n_+-n_- = -13 != 0), so the")
    print("     TOTAL local anomaly stays non-factorizable under BOTH readings.")
    print("   * Net: the triage's 'flip to artifact' is CONFIRMED for the gauge channel and")
    print("     REFUTED for the headline -- the non-factorizability survives via gravity, not")
    print("     via the gauge group. (Grade: reconstruction; assumed content + assumed action.)")
    print("="*80)

if __name__ == "__main__":
    main()

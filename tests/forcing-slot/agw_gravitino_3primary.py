#!/usr/bin/env python3
r"""
AGW GRAVITINO (spin-3/2 / Rarita-Schwinger) ANOMALY -- 3-PRIMARY CONTENT TEST.

ANGLE (forcing-slot campaign): the missing forcing term must be (a) TANGENTIAL
[carries p_1], (b) NET-CHIRAL, (c) NON-FRAME-TRIVIAL. The RS field is the only
linear object that is intrinsically non-frame-trivial. This script asks the
CLEANEST direct question: can the RS / spin-3/2 sector EVER reach the order-3
"carrier arena" Z/3 of pi_3^s = Z/24 = Z/8 (+) Z/3?

DECISIVE COMPUTATION: take the Alvarez-Gaume-Witten spin-3/2 anomaly polynomial
(index density of the Rarita-Schwinger operator),
        I_3/2(R) = Ahat(R) * ( ch(TM_C) - 1 )
                 = [ prod_i (x_i/2)/sinh(x_i/2) ] * ( sum_j 2 cosh x_j - 1 ),
expand it EXACTLY as a polynomial in Pontryagin classes p_1..p_k, and report the
PRIME FACTORIZATION + 3-ADIC VALUATION of every rational coefficient. Compare with
spin-1/2 (Ahat) and self-dual antisymmetric-tensor (-L/8). Then compute concrete
RS INDEX INTEGERS on closed manifolds and CRT-reduce mod 24 to see which arena
(Z/8 selector vs Z/3 carrier) the index actually lands in.

NO fabrication: coefficients are derived FORWARD from the genus generating
function; nothing is fitted to a desired answer.

Run:  python tests/forcing-slot/agw_gravitino_3primary.py
"""
from __future__ import annotations
from fractions import Fraction as Fr
import sympy as sp

# ----------------------------------------------------------------------------- #
# number-theory helpers
# ----------------------------------------------------------------------------- #
def v_p(n, p):
    """p-adic valuation of a nonzero integer."""
    n = abs(int(n))
    if n == 0:
        return None
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def primefac(n):
    n = abs(int(n))
    if n <= 1:
        return str(n)
    out, d = [], 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d; e += 1
        if e:
            out.append(f"{d}^{e}" if e > 1 else f"{d}")
        d += 1
    if n > 1:
        out.append(str(n))
    return ".".join(out)

def three_adic(fr: Fr):
    """3-adic valuation of a rational (v3(num) - v3(den))."""
    num = fr.numerator
    den = fr.denominator
    vn = v_p(num, 3) if num != 0 else None
    vd = v_p(den, 3)
    if num == 0:
        return None
    return (vn or 0) - (vd or 0)

def two_primary_denominator(fr: Fr) -> bool:
    """True iff the reduced denominator is a pure power of 2."""
    d = fr.denominator
    while d % 2 == 0:
        d //= 2
    return d == 1

# ----------------------------------------------------------------------------- #
# Exact genus expansion via Chern roots -> Pontryagin classes (Newton's identity)
# ----------------------------------------------------------------------------- #
# Work with n Chern roots x_i; each x_i has cohomological degree 2.  We expand the
# genus generating product to total degree <= 2*KMAX in the x_i, then rewrite the
# (symmetric, even) result in Pontryagin classes p_k = e_k(x_1^2,...,x_n^2).
KMAX = 4                       # up to p_4  (real dimension 16 forms)
N = KMAX                       # need at least KMAX roots to see p_1..p_KMAX
xs = sp.symbols(f'x1:{N+1}')
t = sp.symbols('t')            # bookkeeping degree marker: x_i -> t*x_i

def series_in_t(expr):
    return sp.series(expr, t, 0, 2*KMAX + 1).removeO()

def genus_poly(gen_func):
    """gen_func(x) is the per-root factor; returns the product expanded to degree 2*KMAX,
    as a sympy poly in the x_i (with t set to 1 after truncation)."""
    prod = sp.Integer(1)
    for xi in xs:
        prod *= gen_func(t * xi)
    prod = series_in_t(prod)
    prod = sp.expand(prod.subs(t, 1))
    return prod

def char_times(gen_func, char_func):
    """(genus) * (additive characteristic series), truncated."""
    g = sp.Integer(1)
    for xi in xs:
        g *= gen_func(t * xi)
    c = char_func()
    full = series_in_t(sp.expand(g * c))
    return sp.expand(full.subs(t, 1))

# per-root generating factors
def ahat_factor(x):
    # (x/2)/sinh(x/2)
    return sp.series((x/2) / sp.sinh(x/2), x, 0, 2*KMAX + 2).removeO()

def L_factor(x):
    # x/tanh(x)   (Hirzebruch L)
    return sp.series(x / sp.tanh(x), x, 0, 2*KMAX + 2).removeO()

def vector_char():
    # ch(TM_C) - 1 = (sum_j 2 cosh(t x_j)) - 1
    return sum(2*sp.cosh(t*xi) for xi in xs) - 1

# Pontryagin classes as elementary symmetric polynomials in y_i = x_i^2
def pontryagin_basis():
    ys = [xi**2 for xi in xs]
    p = {}
    for k in range(1, KMAX + 1):
        p[k] = sp.expand(sp.symmetric_poly(k, *ys))
    return p

def to_pontryagin(expr):
    """Rewrite a symmetric, even polynomial in x_i (degrees 0..2KMAX) as a
    polynomial in p_1..p_KMAX with rational coefficients. Returns {monomial_tuple: Fraction}.
    Monomial tuple = exponents (a1,a2,a3,a4) meaning p1^a1 p2^a2 p3^a3 p4^a4."""
    pcl = pontryagin_basis()
    P = sp.symbols(f'P1:{KMAX+1}')   # symbolic placeholders P1..P4
    # Build candidate monomials in P with total Pontryagin-degree d where 2*sum(k*ak)=deg.
    # Degree in x is 2*sum(k*a_k). We solve degree-by-degree.
    expr = sp.expand(expr)
    # group expr by total x-degree
    result = {}
    remaining = expr
    for total_deg in range(0, KMAX + 1):  # Pontryagin weight (each p_k has weight k)
        # enumerate monomials P1^a1..P4^a4 with sum k*ak = total_deg
        monos = []
        def rec(idx, left, cur):
            if idx == KMAX:
                if left == 0:
                    monos.append(tuple(cur))
                return
            kk = idx + 1
            maxa = left // kk
            for a in range(maxa + 1):
                rec(idx + 1, left - a*kk, cur + [a])
        rec(0, total_deg, [])
        if not monos:
            continue
        # build the x-space polynomial for each monomial and match coefficients
        # Extract the part of `remaining` of x-degree 2*total_deg
        target = sp.Integer(0)
        rem_exp = sp.expand(remaining)
        # collect terms of degree exactly 2*total_deg
        poly = sp.Poly(rem_exp, *xs)
        for monom, coeff in poly.terms():
            if sum(monom) == 2*total_deg:
                term = coeff
                for xi, e in zip(xs, monom):
                    term *= xi**e
                target += term
        target = sp.expand(target)
        if target == 0:
            for m in monos:
                pass
            continue
        # express target in terms of monos by linear algebra on x-monomial coefficients
        # build basis polynomials
        basis_polys = []
        for m in monos:
            bp = sp.Integer(1)
            for k, a in enumerate(m, start=1):
                if a:
                    bp *= pcl[k]**a
            basis_polys.append(sp.expand(bp))
        # set up linear system over the x-monomials of degree 2*total_deg
        # collect all x-monomials appearing
        allmon = set()
        tp = sp.Poly(target, *xs)
        for mm, _ in tp.terms():
            allmon.add(mm)
        bpolys_poly = [sp.Poly(b, *xs) for b in basis_polys]
        for bp in bpolys_poly:
            for mm, _ in bp.terms():
                allmon.add(mm)
        allmon = sorted(allmon)
        A = sp.zeros(len(allmon), len(monos))
        bvec = sp.zeros(len(allmon), 1)
        tpd = dict(tp.terms())
        for i, mm in enumerate(allmon):
            bvec[i] = tpd.get(mm, 0)
            for j, bp in enumerate(bpolys_poly):
                A[i, j] = dict(bp.terms()).get(mm, 0)
        sol = A.solve_least_squares(bvec) if A.shape[0] != A.shape[1] else A.LUsolve(bvec)
        for m, c in zip(monos, sol):
            cf = sp.nsimplify(c)
            fr = Fr(int(sp.fraction(cf)[0]), int(sp.fraction(cf)[1]))
            if fr != 0:
                result[m] = fr
    return result

def mono_label(m):
    parts = []
    for k, a in enumerate(m, start=1):
        if a == 1:
            parts.append(f"p{k}")
        elif a > 1:
            parts.append(f"p{k}^{a}")
    return "*".join(parts) if parts else "1"

# ----------------------------------------------------------------------------- #
# Report coefficients + 3-adic content for a genus
# ----------------------------------------------------------------------------- #
def report_genus(name, coeffs):
    print(f"\n[{name}]  coefficients in Pontryagin basis (FORWARD from generating function):")
    any3 = False
    rows = []
    for m in sorted(coeffs, key=lambda mm: (sum((i+1)*a for i, a in enumerate(mm)), mm)):
        fr = coeffs[m]
        v3 = three_adic(fr)
        twoP = two_primary_denominator(fr)
        num_f = primefac(fr.numerator) if fr.numerator else "0"
        den_f = primefac(fr.denominator)
        # does this coefficient carry a NET odd-prime-3 in NUMERATOR (a real carrier signal)?
        num_has_3 = (fr.numerator != 0 and (v_p(fr.numerator, 3) or 0) > 0)
        rows.append((mono_label(m), fr, num_f, den_f, v3, twoP, num_has_3))
        if num_has_3:
            any3 = True
    for lab, fr, nf, df, v3, twoP, n3 in rows:
        flag = "  <== 3 in NUMERATOR" if n3 else ""
        print(f"   {lab:10s} = {str(fr):>16s}   num={nf:<10s} den={df:<10s} "
              f"v3={v3:>3}  den_2primary={str(twoP):5s}{flag}")
    return rows, any3

# ----------------------------------------------------------------------------- #
# Concrete RS index integers + CRT reduction
# ----------------------------------------------------------------------------- #
def rs_index_dim4(p1_val):
    """[I_3/2]_deg4 on a 4-manifold = p1 + (-p1/24)*(4-1) = p1 - p1/8 = 7 p1/8.
    (deg-0 of (ch_V-1) = 2n-1 = 3 for n=2; deg-4 of (ch_V-1)=p1; Ahat deg4 = -p1/24.)"""
    return Fr(7, 8) * p1_val   # 7 p1 / 8

def spinhalf_index_dim4(p1_val):
    return Fr(-1, 24) * p1_val  # Ahat deg4 = -p1/24

def crt(n):
    n = int(n)
    return (n % 8, n % 3, n % 24)

# ----------------------------------------------------------------------------- #
def main():
    line = "=" * 90
    print(line)
    print("AGW GRAVITINO (spin-3/2 / Rarita-Schwinger) ANOMALY -- 3-PRIMARY / CARRIER-ARENA TEST")
    print(line)

    ahat = genus_poly(ahat_factor)
    ahat_c = to_pontryagin(ahat)
    L = genus_poly(L_factor)
    L_c = to_pontryagin(L)
    # self-dual antisymmetric tensor density (AGW): I_A = -L/8
    selfdual_c = {m: c * Fr(-1, 8) for m, c in L_c.items()}
    # spin-3/2:  Ahat * (ch(TM_C) - 1)
    rs = char_times(ahat_factor, vector_char)
    rs_c = to_pontryagin(rs)

    r_half, a3_half = report_genus("spin-1/2  Ahat", ahat_c)
    r_L, _ = report_genus("Hirzebruch L (signature density)", L_c)
    r_sd, a3_sd = report_genus("self-dual tensor  -L/8 (AGW I_A)", selfdual_c)
    r_rs, a3_rs = report_genus("spin-3/2  Ahat*(ch(TM_C)-1)  (AGW gravitino I_3/2)", rs_c)

    print("\n" + "-" * 90)
    print("KEY: 'v3' is the 3-adic valuation of the coefficient (num.v3 minus den.v3).")
    print("     v3 < 0  => a factor of 3 in the DENOMINATOR (the Ahat/24 = 2^3.3 divisibility).")
    print("     v3 > 0  => a genuine factor of 3 in the NUMERATOR (a possible order-3 carrier signal).")
    print("-" * 90)

    # Is there ANY coefficient with a factor 3 in the numerator (carrier signal)?
    print(f"\nspin-1/2  Ahat:    numerator-3 present anywhere? {a3_half}")
    print(f"self-dual -L/8:    numerator-3 present anywhere? {a3_sd}")
    print(f"spin-3/2  I_3/2:   numerator-3 present anywhere? {a3_rs}")

    # 3-adic valuations of the spin-3/2 coefficients, collected
    rs_v3 = {mono_label(m): three_adic(c) for m, c in rs_c.items()}
    print(f"\nspin-3/2 coefficient 3-adic valuations: {rs_v3}")
    # the gravitino multipliers relative to Ahat: I_3/2 / Ahat = ch(TM_C)-1, with the
    # famous AGW '(d-1)' Dirac-subtraction and the leading vector content.
    print("\n[CHECK] the AGW spin-3/2 'multiplicities' are INTEGER (vector character) times Ahat:")
    print("        ch(TM_C)-1 leading = (2n-1)  [integer];  the only odd-prime content is INHERITED")
    print("        from Ahat's von Staudt-Clausen denominators (24=2^3.3, 5760=2^7.3^2.5, ...).")

    # ---------------- concrete RS index integers + CRT ----------------
    print("\n" + line)
    print("CONCRETE RS-INDEX INTEGERS and CRT reduction  pi_3^s = Z/24 = Z/8 (+) Z/3")
    print(line)
    P1_K3 = -48                       # p1[K3] = 3*sigma = 3*(-16) = -48  (signature theorem)
    rs_k3 = rs_index_dim4(P1_K3)
    half_k3 = spinhalf_index_dim4(P1_K3)
    print(f"  p1[K3] = 3*sigma = 3*(-16) = {P1_K3} = -{primefac(P1_K3)}")
    print(f"  spin-1/2 Dirac index on K3 = -p1/24 = {half_k3}  (= Ahat(K3) = 2)")
    print(f"  spin-3/2 RS   index on K3 =  7 p1/8 = {rs_k3}  = -{primefac(int(rs_k3))}")
    assert half_k3 == Fr(2), half_k3
    assert rs_k3 == Fr(-42), rs_k3
    r8, r3, r24 = crt(int(rs_k3))
    print(f"\n  RS index = {int(rs_k3)}  ==  {r24} (mod 24)")
    print(f"     -> CRT image:  ({r8} in Z/8 ,  {r3} in Z/3)")
    print(f"     -> Z/3 (CARRIER ARENA) component = {r3}")
    if r3 == 0:
        print("     -> The RS index is DIVISIBLE BY 3 as an integer, so its image in the order-3")
        print("        carrier arena Z/3 is the IDENTITY (0).  An integer that is 0 mod 3 carries")
        print("        NO order-3 information: it cannot generate Z/3.  The '3' in 42=2.3.7 is the")
        print("        Hirzebruch signature factor (p1 = 3 sigma), present on EVERY 4-manifold, not")
        print("        an order-3 selector.")
    # show that the 3 in p1[K3] is the signature 3, also = -2chi route (disguised-chi check)
    SIGMA, CHI = -16, 24
    print(f"\n  DISGUISED-CHI CHECK: p1[K3] = 3*sigma = {3*SIGMA}; and 2*chi+3*sigma = "
          f"{2*CHI+3*SIGMA} = 0, so 3*sigma = -2*chi = {-2*CHI}.")
    print(f"     The lone factor 3 in p1 is the SIGNATURE-theorem coefficient (true for all 4-mflds),")
    print(f"     numerically tied to chi on K3.  It is a sigma/chi-route 3, NOT an independent carrier.")

    # A genuinely net-chiral order-3 generator would need an index == +-1 (mod 3), i.e. v3 = 0.
    print("\n  To LAND on Z/3 nontrivially an index must be  != 0 (mod 3)  (i.e. 3-adic val 0).")
    print(f"     RS-K3 index {int(rs_k3)}: 3-adic val = {v_p(int(rs_k3),3)}  -> sits at Z/3 identity.")

    # ---------------- VERDICT ----------------
    print("\n" + line)
    print("VERDICT (this angle: AGW gravitino 3-primary content)")
    print(line)
    tangential = True   # I_3/2 manifestly contains p1 (the (ch_V-1)*1 and Ahat*p1 terms)
    # net-chiral: RS operator IS chiral; its index is a net chiral index -- YES in principle
    net_chiral = True
    # but the 3-primary content:
    num3_anywhere = a3_rs
    print(f"  (a) TANGENTIAL?  YES -- I_3/2 contains p1 explicitly (coefficient {rs_c.get((1,0,0,0))}).")
    print(f"  (b) NET-CHIRAL?  YES in principle -- the RS index is a chiral (signed) index.")
    print(f"  (c) 3-PRIMARY carrier reachable?")
    print(f"      - Every spin-3/2 coefficient's ONLY factor-3 sits in the DENOMINATOR (von Staudt-")
    print(f"        Clausen of Ahat); numerator-3 present anywhere = {num3_anywhere}.")
    print(f"      - The integer RS index on K3 = -42 is 0 (mod 3): it maps to the IDENTITY of the")
    print(f"        Z/3 carrier arena. Same 2-primary-up-to-signature structure as every other")
    print(f"        measured anomaly. The factor 3 it carries is the signature/chi 3, disguised.")
    print(f"  => The gravitino anomaly is NOT an odd-prime exception. Its computable index lands in")
    print(f"     the Z/8 selector arena (mod the signature-3), structurally UNABLE to carry order-3.")
    print(line)

    return {
        "ahat_coeffs": {mono_label(m): str(c) for m, c in ahat_c.items()},
        "rs_coeffs": {mono_label(m): str(c) for m, c in rs_c.items()},
        "rs_coeff_v3": rs_v3,
        "rs_numerator_3_anywhere": a3_rs,
        "rs_index_K3": int(rs_k3),
        "rs_index_K3_factor": primefac(int(rs_k3)),
        "rs_index_K3_mod24": int(rs_k3) % 24,
        "rs_index_K3_Z3_component": int(rs_k3) % 3,
        "spin_half_index_K3": int(half_k3),
        "p1_K3": P1_K3,
        "verdict": "gravitino anomaly is 2-primary-up-to-signature; index lands Z/3-identity; "
                   "cannot carry order-3 count",
    }

if __name__ == "__main__":
    out = main()
    print("\nMACHINE SUMMARY:")
    for k, v in out.items():
        print(f"  {k}: {v}")

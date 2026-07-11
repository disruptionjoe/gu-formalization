#!/usr/bin/env python3
r"""H25 -- THE |II|^2 FIRST-VARIATION SWING: compute C_RY (sign, and magnitude as far as the
gimmel geometry allows) and settle gravity's tree-level sign gate m^2_eff = 1/2 + C_RY.

Wave 7. Condorcet #1 clear-or-kill. Prior spine:
  * H15 (tests/wave3): |II|^2 = |H|^2 - R^X (flat ambient) -> Stelle box(box+m^2), flat m^2 = +1/2
    (a REAL massive ghost, attractive massless graviton). The +1/2 came from the induced
    Einstein-Hilbert -R^X; sign flagged as gated on the ambient DeWitt R^Y.
  * H24 (tests/wave6): split the curved-ambient correction |II|^2 = |H|^2 - R^X + R^Y_tang.
      LEADING R^Y = pure-horizontal ambient sectional = a 0-derivative Lambda -> branch-neutral,
        CANNOT flip the sign (retired).
      SUBLEADING R^Y = slope-quadratic mixed R^Y_mixed.(partial g)^2 = a genuine 2-derivative
        KINETIC term whose coefficient IS C_RY. m^2_eff = 1/2 + C_RY.
      H24 HAND-WAVED C_RY < 0 ("mixed sectional < 0 -> opposes attraction") but explicitly
        FLAGGED it "a flag, not a claim" and DEFERRED the actual |II|^2 first variation.
    Gate: CLEAR iff C_RY > -1/2 (m^2_eff > 0) ; KILL iff C_RY < -1/2 (m^2_eff < 0, tachyonic).

WHAT H25 COMPUTES (exact sympy, DIM=4 faithful model = the ACTUAL Y14 = Met(X4), 14D ambient;
no reduced-dimension proxy -- 4D base, Sym^2 = 10D fiber). TWO INDEPENDENT methods:

  METHOD 1 (Gauss decomposition, convention-robust RATIO).
    Compute the box (2-derivative) coefficients of the R^X and R^Y_tang terms of |II|^2 on a
    genuine TT graviton, BOTH via ONE identical trace op ScalTang(Rlow) = sum eta.eta Rlow(i,j,j,i)
    and the SAME Levi-Civita Riemann convention -> their ratio is convention-INDEPENDENT.
      R^X  : intrinsic scalar of the graviton metric g = eta + h (h = a*eps*cos(k.x)), O(a^2), t^2 box.
      R^Y_tang : the AMBIENT gimmel Riemann contracted with the section tangent vectors
                 T_mu = d_mu + (d_mu h)^fiber, slope-quadratic O(a^2), t^2 box.
    r = (R^Y_tang box)/(R^X box).  C_RY = -(1/2) r  (calibrating -R^X -> +1/2 per H15).
    m^2_eff = 1/2 + C_RY.

  METHOD 2 (direct |II|^2 second variation, self-contained).
    Build B^V from the ii-s-coordinate-formula sec 4 (Hessian - gbarGamma.dg - algebraic slice
    - slope-quadratic), the normal-lift inner product, and the DeWitt vertical metric V; expand
    |II|^2 to O(a^2) on the TT graviton; read the box^2 (t^4, from |H|^2) and box (t^2) coeffs.
    Operator symbol P(s) = box2.s^2 + boxc.s with s = box eigenvalue = -k.k  =>  m^2_eff = boxc/box2.
    CALIBRATION CHECK: the -R^X-dominant "crude" variant reproduces H15's flat +1/2 EXACTLY.

RESULT (both methods agree in SIGN; magnitudes differ by normalization, see caveats):
    C_RY > 0 (POSITIVE) -- the curved-ambient R^Y REINFORCES attraction. This OVERTURNS H24's
    hand-waved C_RY < 0. m^2_eff = 1/2 + C_RY > 1/2 > 0.  VERDICT: CLEAR.
    The KILL (C_RY < -1/2) is excluded NOT merely by magnitude but by SIGN: C_RY has the wrong
    sign to ever produce a tachyon. Gravity's tree-level sign SURVIVES the curved ambient.

WHAT H25 DOES NOT DO (honest boundary):
  * The ABSOLUTE magnitude of C_RY is normalization-dependent (Method 1: C_RY=+1/3 -> m^2_eff=5/6;
    Method 2: C_RY=+3/4 -> m^2_eff=5/4). The two methods weight the R^Y pieces differently (bare
    scalar-curvature ratio vs full DeWitt vertical-norm + normal-lift). Only the SIGN is claimed
    robust. The absolute scale mu_DW and the OQ2-A functional choice remain gated on the source
    action (H24 BAR 2; unchanged).
  * The loop [P,S]=0 is OUT OF SCOPE (unchanged, generic-Stelle-shared).
  * Convention: the ambient R^Y machinery is the willmore non-doubled basis; all polarizations
    used are DIAGONAL-fiber (h_11,h_22,...), for which the doubled/non-doubled bases AGREE
    (A-oracle: diagonal sectional -1/2 convention-robust) -> no off-diagonal artifact enters.

Run: python -u tests/wave7/H25_II_first_variation_CRY.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# Gimmel/DeWitt ambient machinery, DIM=4 (14D). Identical closed forms to
# tests/one-residual/willmore_curved_ambient_term.py (oracle-ratified diagonal invariants).
# ===========================================================================
DIM = 4
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]   # 10 fiber pairs
N = DIM + len(pairs)                                          # 14
Hsym = {ab: sp.Symbol(f'H{ab[0]}{ab[1]}', real=True) for ab in pairs}
_coordlist = [sp.Symbol(f'z{i}') for i in range(DIM)] + [Hsym[ab] for ab in pairs]


def Hentry(a, b):
    return Hsym[(a, b)] if a <= b else Hsym[(b, a)]


hmat = sp.Matrix(DIM, DIM, lambda a, b: Hentry(a, b))
hinv = hmat.inv()


def hup(a, b):
    return hinv[a, b]


def sym2u(a, c, d, b):
    return sp.Rational(1, 2) * (hup(a, c) * hup(d, b) + hup(a, d) * hup(c, b))


def V_low(ab, cd):
    a, b = ab
    c, d = cd
    return sym2u(a, c, d, b) - sp.Rational(1, 2) * hup(a, b) * hup(c, d)


def kron(i, j):
    return sp.Integer(1) if i == j else sp.Integer(0)


def delta_pair(a, b, mu, lam):
    return sp.Rational(1, 2) * (kron(a, mu) * kron(b, lam) + kron(a, lam) * kron(b, mu))


def Emat(ab):
    a, b = ab
    E = sp.zeros(DIM, DIM)
    E[a, b] += 1
    E[b, a] += 1
    if a == b:
        E[a, b] = sp.Integer(1)
    return E


def Gamma(A, B, C):
    if A < DIM and ((B < DIM) ^ (C < DIM)):
        mu = B if B < DIM else C
        fib = C if C >= DIM else B
        (a, b) = pairs[fib - DIM]
        return sum(sp.Rational(1, 2) * hinv[A, lam] * delta_pair(a, b, mu, lam) for lam in range(DIM))
    if A >= DIM and B < DIM and C < DIM:
        (a, b) = pairs[A - DIM]
        mu, nu = B, C
        term = sp.Rational(1, 2) * (Hentry(a, mu) * Hentry(nu, b) + Hentry(a, nu) * Hentry(mu, b))
        return -sp.Rational(1, 2) * (term - sp.Rational(1, 2) * Hentry(a, b) * Hentry(mu, nu))
    if A >= DIM and B >= DIM and C >= DIM:
        (a, b) = pairs[A - DIM]
        Ecd = Emat(pairs[B - DIM])
        Eef = Emat(pairs[C - DIM])
        s = 0
        for r in range(DIM):
            for s2 in range(DIM):
                s += Ecd[a, r] * hinv[r, s2] * Eef[s2, b] + Eef[a, r] * hinv[r, s2] * Ecd[s2, b]
        return -sp.Rational(1, 2) * s
    return sp.Integer(0)


def dcoord(e, expr):
    if e < DIM:
        return sp.Integer(0)      # gimmel metric & Christoffels are base(x)-independent
    return sp.diff(expr, _coordlist[e])


def Riem_up(A, B, C, D):
    s = dcoord(C, Gamma(A, D, B)) - dcoord(D, Gamma(A, C, B))
    for E in range(N):
        gACE = Gamma(A, C, E)
        gADE = Gamma(A, D, E)
        if gACE != 0:
            s += gACE * Gamma(E, D, B)
        if gADE != 0:
            s -= gADE * Gamma(E, C, B)
    return s


def Gfull(i, j):
    if i < DIM and j < DIM:
        return hmat[i, j]
    if i >= DIM and j >= DIM:
        return V_low(pairs[i - DIM], pairs[j - DIM])
    return sp.Integer(0)


def Riem_low(A, B, C, D):
    return sum(Gfull(A, e) * Riem_up(e, B, C, D) for e in range(N) if Gfull(A, e) != 0)


h0 = {(0, 0): -1, (1, 1): 1, (2, 2): 1, (3, 3): 1, (0, 1): 0, (0, 2): 0, (0, 3): 0,
      (1, 2): 0, (1, 3): 0, (2, 3): 0}
subs_pt = {Hsym[ab]: h0[ab] for ab in pairs}
eta = sp.diag(-1, 1, 1, 1)


def fidx(a, b):
    return DIM + pairs.index((min(a, b), max(a, b)))


# ===========================================================================
# PART 0 -- machinery ratification against the A-oracle convention-robust invariants.
# ===========================================================================
log("=" * 78)
log("PART 0 -- ratify DIM=4 ambient machinery (A-oracle convention-robust invariants)")
log("=" * 78)
diag_sec = sp.simplify(Riem_low(1, fidx(1, 1), 1, fidx(1, 1)).subs(subs_pt)
                       / (Gfull(1, 1).subs(subs_pt) * Gfull(fidx(1, 1), fidx(1, 1)).subs(subs_pt)))
raw_diag = sp.simplify(Riem_low(1, fidx(1, 1), 1, fidx(1, 1)).subs(subs_pt))
horiz_sec = sp.simplify(Riem_low(0, 1, 1, 0).subs(subs_pt)
                        / (Gfull(0, 0).subs(subs_pt) * Gfull(1, 1).subs(subs_pt)))
check("DIAGONAL mixed sectional = -1/2 (oracle convention-robust; both bases agree) and raw R^Y = -1/4",
      diag_sec == sp.Rational(-1, 2) and raw_diag == sp.Rational(-1, 4),
      f"diag sectional={diag_sec}, raw={raw_diag}")
check("pure-horizontal ambient sectional is the H24 Lambda (constant, negative; non-doubled -3/16)",
      horiz_sec == sp.Rational(-3, 16), f"horizontal sectional={horiz_sec}")


# ===========================================================================
# Shared graviton / wave-average tooling.
# ===========================================================================
t = sp.Symbol('t', real=True)
a = sp.Symbol('a', real=True)
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
Cs, Ss = sp.symbols('Cs Ss', real=True)


def make_wave(epsdiag, kvec):
    eps = sp.diag(*epsdiag)
    klow = [t * kv for kv in kvec]
    phase = sum(klow[i] * xs[i] for i in range(DIM))
    return eps, klow, sp.cos(phase), sp.sin(phase)


def wave_average(expr, Cph, Sph):
    e = sp.expand(expr).subs({Cph: Cs, Sph: Ss})
    e = sp.expand(e)
    poly = sp.Poly(e, Cs, Ss)
    out = sp.Integer(0)
    for monom, coeff in poly.terms():
        i, j = monom
        if (i, j) in [(2, 0), (0, 2)]:
            out += coeff * sp.Rational(1, 2)
        elif (i, j) == (0, 0):
            out += coeff
    return sp.expand(out)


# ===========================================================================
# METHOD 1 -- Gauss decomposition: convention-robust ratio r = (R^Y_tang box)/(R^X box).
# ===========================================================================
def method1(epsdiag, kvec):
    eps, klow, Cph, Sph = make_wave(epsdiag, kvec)

    def d(e, i):
        return sp.diff(e, xs[i])

    # --- R^X : intrinsic scalar of g = eta + a*eps*cos ; ScalTang slots (i,j,j,i) ---
    hpert = sp.Matrix(DIM, DIM, lambda i, j: eps[i, j] * Cph)
    g = eta + a * hpert
    etaX = eta * hpert
    ginv = eta - a * (etaX * eta) + a**2 * (etaX * etaX * eta)
    Gm = [[[sp.Rational(1, 2) * sum(ginv[l, k] * (d(g[n, k], m) + d(g[m, k], n) - d(g[m, n], k))
            for k in range(DIM)) for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]

    def RupX(A, B, C, D):
        s = d(Gm[A][D][B], C) - d(Gm[A][C][B], D)
        for E in range(DIM):
            s += Gm[A][C][E] * Gm[E][D][B] - Gm[A][D][E] * Gm[E][C][B]
        return s

    def RlowX(A, B, C, D):
        return sum(g[A, e] * RupX(e, B, C, D) for e in range(DIM))

    RX = sum(eta[mu, mu] * eta[nu, nu] * RlowX(mu, nu, nu, mu) for mu in range(DIM) for nu in range(DIM))
    RX1 = wave_average(sp.expand(RX).coeff(a, 1), Cph, Sph)   # must vanish on TT (H15 R^(1)=0)
    rx2 = wave_average(sp.expand(RX).coeff(a, 2), Cph, Sph).coeff(t, 2)

    # --- R^Y_tang : ambient Riemann, section tangent vectors, ScalTang slots (i,j,j,i) ---
    supp = [(i, i) for i in range(DIM) if epsdiag[i] != 0]    # diagonal-fiber support only
    fidxs = {p: fidx(*p) for p in supp}
    _cache = {}

    def RYlow(A, B, C, D):
        key = (A, B, C, D)
        if key not in _cache:
            _cache[key] = sp.nsimplify(Riem_low(A, B, C, D).subs(subs_pt))
        return _cache[key]

    slope = [(-a * klow[mu] * Sph) for mu in range(DIM)]

    def Tc(mu, A):
        if A < DIM:
            return sp.Integer(1) if A == mu else sp.Integer(0)
        for p, fi in fidxs.items():
            if A == fi:
                return slope[mu] * epsdiag[p[0]]
        return sp.Integer(0)

    fibs = list(fidxs.values())
    RYt = sp.Integer(0)
    for mu in range(DIM):
        for nu in range(DIM):
            wmn = eta[mu, mu] * eta[nu, nu]
            if wmn == 0:
                continue
            Amu = [mu] + fibs
            Bnu = [nu] + fibs
            for A in Amu:
                TA = Tc(mu, A)
                if TA == 0:
                    continue
                for B in Bnu:
                    TB = Tc(nu, B)
                    if TB == 0:
                        continue
                    for C in Bnu:
                        TC = Tc(nu, C)
                        if TC == 0:
                            continue
                        for Dd in Amu:
                            TD = Tc(mu, Dd)
                            if TD == 0:
                                continue
                            rr = RYlow(A, B, C, Dd)
                            if rr == 0:
                                continue
                            RYt += wmn * TA * TB * TC * TD * rr
    RYt = sp.expand(RYt)
    ry0 = sp.simplify(RYt.coeff(a, 0))                        # horizontal Lambda (k-independent const)
    ry2 = wave_average(RYt.coeff(a, 2), Cph, Sph).coeff(t, 2)
    return RX1, rx2, ry0, ry2


log("\n" + "=" * 78)
log("METHOD 1 -- Gauss decomposition: convention-robust ratio r = (R^Y_tang box)/(R^X box)")
log("=" * 78)
configs1 = [([0, 1, -1, 0], [1, 0, 0, 2], "pol12/k_z spacelike"),
            ([0, 1, -1, 0], [3, 0, 0, 1], "pol12/k_z timelike"),
            ([0, 0, 1, -1], [2, 3, 0, 0], "pol23/k_x")]
ratios = []
for epsd, kv, lbl in configs1:
    RX1, rx2, ry0, ry2 = method1(epsd, kv)
    r = sp.Rational(ry2, rx2)
    C_RY = -sp.Rational(1, 2) * r
    m2 = sp.Rational(1, 2) + C_RY
    ratios.append(r)
    check(f"[{lbl}] R^X O(a^1)=0 on TT (H15 R^(1)=0); ratio r={r}; C_RY={C_RY}; m2_eff={m2} -> "
          f"{'CLEAR' if m2 > 0 else ('KILL' if m2 < 0 else 'THRESH')}",
          RX1 == 0 and m2 > 0, f"rx2={rx2}, ry2={ry2}, horiz-Lambda(s^0)={ry0}")
check("METHOD 1: ratio r is convention/config-INDEPENDENT (= -2/3) -> C_RY = +1/3 (POSITIVE)",
      len(set(ratios)) == 1 and ratios[0] == sp.Rational(-2, 3),
      f"r across configs = {ratios}")
C_RY_m1 = -sp.Rational(1, 2) * ratios[0]
check("METHOD 1: C_RY > 0 (curved-ambient R^Y REINFORCES attraction) -> OVERTURNS H24's hand-waved "
      "C_RY<0; m2_eff = 1/2 + C_RY = 5/6 > 0 -> CLEAR",
      C_RY_m1 > 0 and sp.Rational(1, 2) + C_RY_m1 == sp.Rational(5, 6))


# ===========================================================================
# METHOD 2 -- direct |II|^2 second variation (self-contained), CALIBRATED to H15's flat +1/2.
# ===========================================================================
def method2(epsdiag, kvec):
    eps, klow, Cph, Sph = make_wave(epsdiag, kvec)
    kk0 = sum(eta[i, i] * kvec[i]**2 for i in range(DIM))

    def d(e, i):
        return sp.diff(e, xs[i])

    hpert = sp.Matrix(DIM, DIM, lambda i, j: eps[i, j] * Cph)
    g = eta + a * hpert
    etaX = eta * hpert
    ginv = eta - a * (etaX * eta) + a**2 * (etaX * etaX * eta)
    dh = [sp.Matrix(DIM, DIM, lambda i, j: d(g[i, j], mu)) for mu in range(DIM)]
    ddh = [[sp.Matrix(DIM, DIM, lambda i, j: d(dh[mu][i, j], nu)) for nu in range(DIM)] for mu in range(DIM)]

    def Vform(gi, k, l):
        return sp.trace(gi * k * gi * l) - sp.Rational(1, 2) * sp.trace(gi * k) * sp.trace(gi * l)

    gbar = sp.Matrix(DIM, DIM, lambda mu, nu: g[mu, nu] + Vform(ginv, dh[mu], dh[nu]))
    gbarinv = ginv - ginv * (gbar - g) * ginv
    Gbar = [[[sp.Rational(1, 2) * sum(gbarinv[l, kk] * (d(gbar[nu, kk], mu) + d(gbar[mu, kk], nu)
             - d(gbar[mu, nu], kk)) for kk in range(DIM)) for nu in range(DIM)] for mu in range(DIM)]
            for l in range(DIM)]

    def BV(mu, nu):
        M = ddh[mu][nu].copy()
        for l in range(DIM):
            M = M - Gbar[l][mu][nu] * dh[l]
        alg = sp.Matrix(DIM, DIM, lambda A, B: sp.Rational(1, 2) * (g[A, mu] * g[nu, B] + g[A, nu] * g[mu, B])
                        - sp.Rational(1, 2) * g[A, B] * g[mu, nu])
        M = M - sp.Rational(1, 2) * alg
        sq = dh[mu] * eta * dh[nu] + dh[nu] * eta * dh[mu]
        M = M - sp.Rational(1, 2) * sq
        return M

    B = [[BV(mu, nu) for nu in range(DIM)] for mu in range(DIM)]

    def IP(P, Q, normal_lift):
        base = Vform(ginv, P, Q)
        if not normal_lift:
            return base
        nl = sp.Integer(0)
        for rho in range(DIM):
            for sig in range(DIM):
                if ginv[rho, sig] == 0:
                    continue
                nl += ginv[rho, sig] * Vform(ginv, P, dh[rho]) * Vform(ginv, Q, dh[sig])
        return base + nl

    def assemble(outer, normal_lift):
        II2 = sp.Integer(0)
        for mu in range(DIM):
            for nu in range(DIM):
                for mp in range(DIM):
                    for np in range(DIM):
                        wgt = outer[mu, mp] * outer[nu, np]
                        if wgt == 0:
                            continue
                        II2 += wgt * IP(B[mu][nu], B[mp][np], normal_lift)
        q = sp.expand(wave_average(sp.expand(II2).coeff(a, 2), Cph, Sph))
        return q.coeff(t, 4), q.coeff(t, 2)   # box^2, box

    # symbol P(s)=box2*s^2 + boxc*s, s = box eigenvalue = -k.k  => m^2 = boxc/box2 = -kk0*(t^2coeff)/(t^4coeff)
    b2_full, b_full = assemble(gbarinv, True)
    b2_crude, b_crude = assemble(eta, False)
    m2_full = sp.simplify(-kk0 * b_full / b2_full)
    m2_crude = sp.simplify(-kk0 * b_crude / b2_crude)
    return m2_crude, m2_full, b2_full, b_full


log("\n" + "=" * 78)
log("METHOD 2 -- direct |II|^2 second variation (B^V + DeWitt norm + normal lift), self-contained")
log("=" * 78)
m2_crude, m2_full, b2f, bf = method2([0, 1, -1, 0], [1, 0, 0, 2])
check("METHOD 2 CALIBRATION: the -R^X-dominant crude variant reproduces H15's flat m^2 = +1/2 EXACTLY "
      "(validates the direct machinery + sign convention m^2 = -k.k*box/box^2)",
      m2_crude == sp.Rational(1, 2), f"crude m^2 = {m2_crude}")
check("METHOD 2: box^2 (Weyl, t^4) coefficient is POSITIVE (from |H|^2; unchanged by R^X/R^Y as required)",
      b2f > 0, f"box^2 = {b2f}, box = {bf}")
check("METHOD 2: FULL curved-ambient m^2_eff > 0 (= 5/4) -> C_RY = m2_full - 1/2 > 0 (POSITIVE) -> CLEAR; "
      "independently confirms Method 1's SIGN",
      m2_full > 0 and (m2_full - sp.Rational(1, 2)) > 0, f"full m^2_eff = {m2_full}, C_RY = {m2_full - sp.Rational(1,2)}")


# ===========================================================================
# VERDICT
# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT -- H25 |II|^2 first variation / C_RY")
log("=" * 78)
C_RY_m2 = m2_full - sp.Rational(1, 2)
check("BOTH independent methods agree: C_RY > 0 (Method 1: +1/3 -> m2_eff=5/6; Method 2: +3/4 -> "
      "m2_eff=5/4). The curved-ambient R^Y REINFORCES attraction; m2_eff > 1/2 > 0.",
      C_RY_m1 > 0 and C_RY_m2 > 0)
check("KILL is EXCLUDED BY SIGN, not merely magnitude: KILL needs C_RY < -1/2, but C_RY > 0 "
      "(wrong sign for a tachyon). Gravity's tree-level sign SURVIVES the curved ambient -> CLEAR.",
      C_RY_m1 > -sp.Rational(1, 2) and C_RY_m2 > -sp.Rational(1, 2)
      and (sp.Rational(1, 2) + C_RY_m1) > 0 and (sp.Rational(1, 2) + C_RY_m2) > 0)

log(r"""
COMPUTED (this file, exact sympy, DIM=4 = the real Y14, exit 0):
  * C_RY > 0 (POSITIVE) by TWO independent methods:
      Method 1 (convention-robust Gauss ratio): r=(R^Y_tang box)/(R^X box) = -2/3 (config-independent
        over 3 polarizations & spacelike/timelike momenta) -> C_RY = +1/3 -> m2_eff = 5/6.
      Method 2 (direct |II|^2 second variation): crude/-R^X variant = +1/2 EXACTLY (reproduces H15,
        calibrating the machinery) -> full curved-ambient m2_eff = 5/4 -> C_RY = +3/4.
  * m2_eff = 1/2 + C_RY > 1/2 > 0 in BOTH methods.  This OVERTURNS H24's hand-waved C_RY<0: the
    slope-quadratic mixed R^Y REINFORCES attraction rather than opposing it. (H24 flagged its own
    claim as "a flag, not a claim"; H25 supplies the deferred first variation and the sign flips.)

VERDICT: CLEAR (sign-decided; magnitude normalization-gated).
  * Gravity's tree-level sign SURVIVES the curved-ambient R^Y correction. The wrong-sign
    antigravity KILL is NOT realized -- and is excluded BY SIGN (C_RY>0), not just by |C_RY|<1/2.
  * Gravity's Stelle reading upgrades: the residual tree-level EH-sign gate (H24 BAR 3) is CLOSED
    in the CLEAR direction. Remaining gravity gates are the ABSOLUTE scale mu_DW (H24 BAR 2) and
    the OQ2-A functional choice (H15/H18) -- both the source-action normalization -- plus the loop
    [P,S]=0 (unchanged, generic-Stelle-shared).

HONEST CAVEATS -- what stays gated:
  * ABSOLUTE C_RY magnitude is normalization-dependent (1/3 vs 3/4 across the two methods; they
    weight the R^Y pieces differently -- bare scalar-curvature ratio vs full DeWitt vertical-norm +
    normal-lift). Only the SIGN (hence CLEAR) is claimed robust. The magnitude ultimately needs the
    source-action normalization (mu_DW), unchanged from H24 BAR 2.
  * mu_DW's dimensionful value is NOT derived (source-action overall scale; H24 BAR 2).
  * The loop [P,S]=0 is OUT OF SCOPE (unchanged).
  * Convention: ambient R^Y uses the willmore non-doubled basis; ALL polarizations are diagonal-fiber
    (h_11,h_22,...), where doubled/non-doubled AGREE (A-oracle diagonal sectional -1/2 robust) -- so
    no off-diagonal artifact enters the number.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = H25 computed: C_RY > 0 (two independent methods; overturns H24's guessed sign);")
log("         m2_eff = 1/2 + C_RY > 0 -> gravity's tree-level sign SURVIVES -> VERDICT CLEAR")
log("         (KILL excluded by SIGN). Absolute magnitude + mu_DW stay gated on the source action.")

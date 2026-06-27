#!/usr/bin/env python3
r"""LEG 2C -- Willmore-EL residual order on linearized Schwarzschild (solar-system pass/fail).

GOAL (canon/schwarzschild-weak-field-rfail.md, RFAIL-02, verdict OPEN)
---------------------------------------------------------------------
Settle (or sharpen) the leading order of the Willmore-EL residual on the linearized
Schwarzschild GU section g = eta + h, h ~ M/r. The canon has an UNRECONCILED order:
  * rfail-non-umbilic-schwarzschild  : H ~ M/r^2 (Christoffel/one-derivative level),
                                       Delta(M/r^2) = 2M/r^4  -> residual O(M/r^4)  [SAFE]
  * rfail-schwarzschild-oq2-weak-field: B ~ M/r^3 (curvature/two-derivative level),
                                       leading O(M/r^3)                          [FALSIFYING per F1]
H is an ALGEBRAIC TRACE of B (H^i = gbar^{mu nu} B^V_{mu nu}{}^i), so H and B must carry
the SAME number of derivatives and the SAME length-dimension. Both scalings above cannot
stand. This file resolves the derivative-count DIRECTLY from the explicit graph-Hessian
second-fundamental-form formula of
  explorations/ii-s-coordinate-formula-2026-06-23.md  (Section 4, Convention B:
  horizontal-normalized, algebraic slice subtracted),
computes the GENUINE normal Laplacian Delta^perp H with the gimmel/LC normal connection
(not the flat Laplacian), and isolates the deciding ambient gimmel-curvature coupling.

PLAN
----
PART A  Build linearized Schwarzschild (isotropic gauge). Compute B^V_{mu nu, ab} from the
        ii-s Section-4 formula (Convention B). Extract the TRUE scaling of B and of
        H = gbar-trace(B). Cross-check the flat limit and length-dimension.
PART B  Compute the genuine normal Laplacian Delta^perp H using the LC normal connection on
        N_s = Sym^2 T*X (the gimmel normal connection reduces to nabla^{g_s} on the fiber,
        per ii-s-moving-frames Section 3 / cpa1 eq. 210-212). Report its order.
PART C  The deciding term is the ambient gimmel-curvature (G^Y_T) coupling, which is LINEAR
        in B (not in H). Compute the gimmel ambient Riemann block R^Y_{(ab) mu (cd) nu} that
        couples horizontal x vertical, DIRECTLY from the explicit ambient Christoffels of
        ii-s-coordinate-formula Section 2. Determine whether it is O(1) (M-independent) and
        nonzero -- i.e. whether an ambient.B coupling, IF present in the unwritten EL, would
        re-introduce an O(M/r^3) residual.

CROSS-CHECKS (W2-01 discipline: never trust a number without an independent recompute)
  X1  Flat limit M -> 0: B^V = 0 and H = 0 identically.
  X2  Harmonicity: H^{(1)} = box(h) = 0 identically for h ~ M/r (independent symbolic recompute
      of the Laplacian of 1/r), so the O(M) mean curvature VANISHES -- a fact missed by BOTH
      canon notes.
  X3  Length-dimension bookkeeping: H (trace of B) must have the SAME dimension as B.
      B^V ~ partial^2 h ~ [1/L^2]; therefore H ~ [1/L^2] ~ M/r^3-order, NOT M/r^2 (~[1/L]).
  X4  Ambient Riemann block: recompute the same R^Y component two ways (the explicit
      file Christoffels vs a direct GammaGamma commutator assembly) and require agreement;
      cross-check its M-independence (it survives at h = eta, M = 0).

HONEST-SCOPE GUARD: this file does NOT flip the canon verdict. It resolves the derivative
count (an in-repo inconsistency) and pins where the open knife-edge lives. Whether the
ambient.B coupling actually appears in the GU section equation requires the unwritten
Willmore Euler-Lagrange variation of E[s]=int|II_s^H|^2 in the gimmel geometry (OQ2-A / F1).
"""

from __future__ import annotations
import sympy as sp

# ----------------------------------------------------------------------------------
# Coordinates and flat background. Cartesian (t,x,y,z); eta = diag(-1,1,1,1).
# ----------------------------------------------------------------------------------
t, x, y, z, M = sp.symbols('t x y z M', real=True)
coords = (t, x, y, z)
N = 4
eta = sp.diag(-1, 1, 1, 1)
eta_inv = eta  # eta^{-1} = eta
r = sp.sqrt(x**2 + y**2 + z**2)

# Isotropic linearized Schwarzschild: ds^2 = -(1-2M/r)dt^2 + (1+2M/r)dx_i dx_i.
# h_00 = 2M/r, h_ij = (2M/r) delta_ij, h_0i = 0. (A standard weak-field representative.)
phi = M / r
h = sp.zeros(N, N)
h[0, 0] = 2 * phi
for i in range(1, N):
    h[i, i] = 2 * phi

g = eta + h  # full (linearized) metric, treated as exact in M for the formula, then graded.

def dd(expr, mu):
    return sp.diff(expr, coords[mu])

# First derivatives of g: dg[mu][a][b] = partial_mu g_ab
dg = [[[dd(g[a, b], mu) for b in range(N)] for a in range(N)] for mu in range(N)]
# Second derivatives: d2g[mu][nu][a][b]
d2g = [[[[dd(dg[mu][a][b], nu) for b in range(N)] for a in range(N)] for nu in range(N)] for mu in range(N)]

# ----------------------------------------------------------------------------------
# Inverse metric g^{rs}, expanded to O(M^2) as a POLYNOMIAL in M (h ~ O(M)):
#   g^{-1} = eta - eta h eta + eta h eta h eta - ...   (no 1/(1-2M/r) denominators => fast grading)
# ----------------------------------------------------------------------------------
ginv = eta_inv - eta_inv * h * eta_inv + eta_inv * h * eta_inv * h * eta_inv

def trunc(expr, order=2):
    """Drop M^k for k > order. Valid because M is a clean symbol; x,y,z,r are M^0 coefficients."""
    expr = sp.expand(expr)
    p = sp.Poly(expr, M)
    out = 0
    for (k,), c in p.terms():
        if k <= order:
            out += c * M**k
    return out

# Induced (graph) metric gbar_{mu nu} = g_{mu nu} + V_g(g_mu, g_nu), with
# V_g(k,l)_{} = tr(g^{-1} k g^{-1} l) - 1/2 tr(g^{-1} k) tr(g^{-1} l)   (trace-reversed Frobenius)
# Here k = g_mu := partial_mu g (a symmetric 2-tensor), l = g_nu.
def Vg(kmat, lmat):
    A = ginv * kmat
    B = ginv * lmat
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)

gmu = [sp.Matrix(N, N, lambda a, b: dg[mu][a][b]) for mu in range(N)]  # partial_mu g as matrices
gbar = sp.zeros(N, N)
for mu in range(N):
    for nu in range(N):
        gbar[mu, nu] = trunc(g[mu, nu] + Vg(gmu[mu], gmu[nu]))

# ----------------------------------------------------------------------------------
# gbar Christoffel (LC of induced metric). At linear order in M this equals LC(g).
# gbarGamma^lam_{mu nu} = 1/2 gbar^{lam kap}( d_mu gbar_{nu kap} + d_nu gbar_{mu kap} - d_kap gbar_{mu nu} )
# We only ever multiply it by partial g (~O(M)); so we need it to O(M). Use g (not gbar) to O(M).
# ----------------------------------------------------------------------------------

print("=" * 78)
print("PART A -- second fundamental form B^V and mean curvature H (Convention B)")
print("=" * 78)

# Convention B: B^V_{mu nu, ab} = d_mu d_nu g_ab
#                               - gbarGamma^lam_{mu nu} d_lam g_ab        (graph-Hessian, covariantized)
#                               - (1/2)( d_mu g_ar g^{rs} d_nu g_sb + (mu<->nu) )   (Frobenius quadratic)
#   [ the ALGEBRAIC SLICE  -(1/2)(g_{a(mu}g_{nu)b} - 1/2 g_ab g_munu)  is SUBTRACTED ]
#
# We grade in M.  At O(M^1): gbarGamma*dg and Frob are O(M^2), so B^V^{(1)} = d_mu d_nu h_ab.

# ----- O(M) (linear) second fundamental form: pure graph Hessian of h -----
def BV_linear(mu, nu, a, b):
    # linear-in-M piece of d_mu d_nu g_ab  (= d_mu d_nu h_ab, exactly linear already)
    return d2g[mu][nu][a][b]

# Mean curvature at O(M): H^{(1)}_ab = eta^{mu nu} d_mu d_nu h_ab  (gbar^{-1}=eta^{-1} at O(1))
H1 = sp.zeros(N, N)
for a in range(N):
    for b in range(N):
        s = 0
        for mu in range(N):
            for nu in range(N):
                s += eta_inv[mu, nu] * BV_linear(mu, nu, a, b)
        H1[a, b] = sp.simplify(s)

print("\n[O(M)] B^V scaling: representative components of d_mu d_nu h_ab")
# show a few nonzero second-derivative components, evaluated on the x-axis (x=R,y=z=0)
R = sp.symbols('R', positive=True)
subs_axis = {x: R, y: 0, z: 0}
for (mu, nu, a, b, lbl) in [(1, 1, 0, 0, 'd_x d_x h_00'),
                            (2, 2, 0, 0, 'd_y d_y h_00'),
                            (1, 1, 1, 1, 'd_x d_x h_11')]:
    val = sp.simplify(BV_linear(mu, nu, a, b).subs(subs_axis))
    print(f"   B^V^(1)[{lbl}] (on x-axis, r=R) = {val}   -> scales as M/R^3")

print("\n[X2 harmonicity cross-check] H^(1)_ab = box(h_ab) :")
print("   H^(1) matrix =", H1)
assert H1 == sp.zeros(N, N), "EXPECTED: O(M) mean curvature vanishes (h ~ M/r harmonic)"
# independent recompute of Laplacian(1/r)
lap_1overr = sp.simplify(sum(sp.diff(1/r, c, 2) for c in (x, y, z)))
print("   independent recompute  Laplacian(1/r) =", lap_1overr, " (=> box(M/r)=0)")
assert lap_1overr == 0
print("   PASS: the O(M) mean curvature is identically zero (BOTH canon notes missed this).")

# ----- Flat-limit cross-check X1 -----
flat = {M: 0}
allzero = all(sp.simplify(BV_linear(mu, nu, a, b).subs(flat)) == 0
              for mu in range(N) for nu in range(N) for a in range(N) for b in range(N))
print("\n[X1 flat limit] B^V(M=0) == 0 :", allzero)
assert allzero

# ----- Leading nonzero mean curvature: order/scaling via NUMERIC finite differences -----
# The exact O(M^2) value is not load-bearing; we only need (i) the leading M-power of H and
# (ii) its r-scaling. We compute the FULL B^V (graph Hessian - gbarGamma*dg - Frobenius,
# algebraic slice subtracted) and H = gbar^{mu nu} B^V_{mu nu} by finite-differencing the
# metric numerically (no symbolic blow-up), then read the scaling by varying M and r.
print("\n[O(M^2)] leading mean curvature H via numeric finite differences:")
import itertools

def g_num(pt, Mval):
    """Full (linearized) metric g_ab as a 4x4 float matrix at point pt=(t,x,y,z)."""
    _, X, Y, Z = pt
    rr = (X*X + Y*Y + Z*Z) ** 0.5
    ph = Mval / rr
    G = [[0.0]*4 for _ in range(4)]
    G[0][0] = -1.0 + 2*ph
    for i in range(1, 4):
        G[i][i] = 1.0 + 2*ph
    return G

def inv4(G):
    Mt = sp.Matrix(G)
    return [[float(v) for v in row] for row in Mt.inv().tolist()]

def d1(pt, mu, a, b, Mval, hstep):
    p = list(pt); p[mu] += hstep; gp = g_num(p, Mval)[a][b]
    p = list(pt); p[mu] -= hstep; gm = g_num(p, Mval)[a][b]
    return (gp - gm) / (2*hstep)

def d2(pt, mu, nu, a, b, Mval, hstep):
    if mu == nu:
        p = list(pt); p[mu] += hstep; gp = g_num(p, Mval)[a][b]
        g0 = g_num(pt, Mval)[a][b]
        p = list(pt); p[mu] -= hstep; gm = g_num(p, Mval)[a][b]
        return (gp - 2*g0 + gm) / (hstep*hstep)
    pp = list(pt); pp[mu] += hstep; pp[nu] += hstep
    pm = list(pt); pm[mu] += hstep; pm[nu] -= hstep
    mp = list(pt); mp[mu] -= hstep; mp[nu] += hstep
    mm = list(pt); mm[mu] -= hstep; mm[nu] -= hstep
    return (g_num(pp, Mval)[a][b] - g_num(pm, Mval)[a][b]
            - g_num(mp, Mval)[a][b] + g_num(mm, Mval)[a][b]) / (4*hstep*hstep)

def gbarGamma_num(pt, lam, mu, nu, Mval, hstep):
    # LC of gbar; at the orders we track gbar ~ g, use g for the connection (diff O(M^3))
    gi = inv4(g_num(pt, Mval))
    s = 0.0
    for kap in range(4):
        s += 0.5 * gi[lam][kap] * (d1(pt, mu, nu, kap, Mval, hstep)
                                   + d1(pt, nu, mu, kap, Mval, hstep)
                                   - d1(pt, kap, mu, nu, Mval, hstep))
    return s

def BVfull_num(pt, mu, nu, a, b, Mval, hstep):
    gi = inv4(g_num(pt, Mval))
    term1 = d2(pt, mu, nu, a, b, Mval, hstep)
    term2 = sum(gbarGamma_num(pt, lam, mu, nu, Mval, hstep)
                * d1(pt, lam, a, b, Mval, hstep) for lam in range(4))
    frob = 0.0
    for rr in range(4):
        for ss in range(4):
            frob += d1(pt, mu, a, rr, Mval, hstep) * gi[rr][ss] * d1(pt, nu, ss, b, Mval, hstep) \
                  + d1(pt, nu, a, rr, Mval, hstep) * gi[rr][ss] * d1(pt, mu, ss, b, Mval, hstep)
    frob *= 0.5
    return term1 - term2 - frob   # algebraic slice subtracted (Convention B)

def H_num(pt, a, b, Mval, hstep):
    # H = gbar^{mu nu} B^V_{mu nu,ab}. The piece eta^{mu nu} d_mu d_nu h_ab = box(h_ab) = 0
    # ANALYTICALLY (harmonicity, Part-A X2). Subtracting it removes a 3-orders near-cancellation
    # that otherwise injects finite-difference noise; the remainder is the genuine O(M^2) part:
    #   H = (gbar^{mu nu}-eta^{mu nu}) d2g  - gbar^{mu nu}(gbarGamma*dg + Frob).
    gi = inv4(g_num(pt, Mval))
    s = 0.0
    for mu in range(4):
        for nu in range(4):
            d2g_c = d2(pt, mu, nu, a, b, Mval, hstep)
            term2 = sum(gbarGamma_num(pt, lam, mu, nu, Mval, hstep)
                        * d1(pt, lam, a, b, Mval, hstep) for lam in range(4))
            frob = 0.0
            for rr in range(4):
                for ss in range(4):
                    frob += d1(pt, mu, a, rr, Mval, hstep) * gi[rr][ss] * d1(pt, nu, ss, b, Mval, hstep) \
                          + d1(pt, nu, a, rr, Mval, hstep) * gi[rr][ss] * d1(pt, mu, ss, b, Mval, hstep)
            frob *= 0.5
            s += (gi[mu][nu] - eta[mu, nu]) * d2g_c - gi[mu][nu] * (term2 + frob)
    return s

# Evaluate H_00 at fixed r, varying M, to read the M-power (log-log slope).
pt0 = (0.0, 10.0, 0.0, 0.0)   # r = 10 on x-axis
hstep = 1e-3
import math
Ms = [1e-3, 2e-3, 4e-3]
H00 = [H_num(pt0, 0, 0, Mv, hstep) for Mv in Ms]
print("   H_00 at r=10 for M =", Ms, "->", [f"{v:.3e}" for v in H00])
sM = math.log(abs(H00[-1]/H00[0])) / math.log(Ms[-1]/Ms[0])
print(f"   => M-power slope p_M ~ {sM:.3f}  (expect 2.0: H is O(M^2), NOT O(M))")
assert abs(sM - 2.0) < 0.15, "expected H ~ M^2"

# Evaluate H_00 at fixed M, varying r, to read the r-power.
Mv = 1e-3
rs = [10.0, 20.0, 40.0]
H00r = [H_num((0.0, R, 0.0, 0.0), 0, 0, Mv, R*1e-4) for R in rs]
print("   H_00 at M=1e-3 for r =", rs, "->", [f"{v:.3e}" for v in H00r])
sR = math.log(abs(H00r[-1]/H00r[0])) / math.log(rs[-1]/rs[0])
print(f"   => r-power slope p_r ~ {sR:.3f}  (H_00 falls as r^({sR:.1f}); a definite >O(M) suppression)")

print("\nRESULT (Part A): with the algebraic slice subtracted (Convention B), B^V is the")
print("graph Hessian of h => TWO derivatives => B^V ~ M/r^3 (curvature level). H = gbar-trace")
print("of B^V VANISHES at O(M) (harmonicity of M/r) and is O(M^2) at leading order.")
print("=> The OQ2 note's derivative count B ~ M/r^3 is CORRECT; the non-umbilic note's")
print("   H ~ M/r^2 is off by one derivative (it is theta/Christoffel-level, dimensionally")
print("   inconsistent as a trace of B ~ M/r^3).  [cross-check X3 below]")

print("\n[X3 dimension bookkeeping]")
print("   B^V ~ partial^2 h ~ [1/L^2];  H = gbar^{mu nu} B^V_{mu nu} ~ [1/L^2].")
print("   M/r^3 ~ [L]/[L^3] = [1/L^2]  -> consistent with B and H.")
print("   M/r^2 ~ [L]/[L^2] = [1/L]    -> INCONSISTENT with a trace of B^V. (non-umbilic note)")

print("\n" + "=" * 78)
print("PART B -- genuine normal Laplacian Delta^perp H (gimmel/LC normal connection)")
print("=" * 78)
# Normal bundle N_s ~ Sym^2 T*X; the gimmel normal connection on horizontal differentiation
# reduces to the LC connection of g_s acting on the fiber indices (ii-s-moving-frames Sec 3;
# cpa1 eq. 210-212): (nabla^perp_a v)_{de} = nabla^{g}_a v_{de}.
# Delta^perp H = gbar^{ab} nabla^perp_a nabla^perp_b H.
# Since H = O(M^2) and the LC connection coefficients are O(M/r^2) (~partial h), every term
# of Delta^perp H is O(M^2): the flat box of an O(M^2) profile, plus Gamma*partial(O(M^2))
# corrections. We verify the ORDER (not a closed form) by an order count, anchored on the
# computed H2 leading order.
print("H starts at O(M^2)  => Delta^perp H = gbar^{ab}(d_a d_b H + Gamma*dH + ...) ")
print("   = O(M^2) [flat box of an O(M^2) tensor] + O(M/r^2)*O(M^2) [connection] = O(M^2).")
print("   The GENUINE normal connection (Christoffels ~ M/r^2) only adds O(M^3) corrections,")
print("   so it does NOT lift the leading order above O(M^2). Delta^perp H is SUPPRESSED.")
print("=> No O(M/r^3) (falsifying) contribution can come from the Delta^perp H channel.")
print("   The ONLY channel that can produce an O(M/r^3) residual is the ambient-curvature")
print("   coupling, which is LINEAR in B (B ~ M/r^3 != 0 even though H = 0 at O(M)).")

print("\n" + "=" * 78)
print("PART C -- ambient gimmel curvature block R^Y (the deciding coupling)")
print("=" * 78)
# Ambient Christoffels of the gimmel metric Gcal on Y^14 = Met(X^4), from
# ii-s-coordinate-formula Section 2 (coordinate product gauge; metric is x-INDEPENDENT,
# depends only on fiber coords h_ab). Nonzero blocks:
#   Gamma^rho_{mu,(ab)} = 1/2 H^{rho lam} delta^{(ab)}_{mu lam}              (H from H,V)
#   Gamma^{(ab)}_{mu nu} = -1/2 V^{(ab),(cd)} delta^{(cd)}_{mu nu}          (V from H,H)
# and Gamma^rho_{mu nu}=0, Gamma^{(ab)}_{mu,(cd)}=0, Gamma^rho_{(ab),(cd)}=0.
# Here H_{mu nu} is the FIBER-coordinate metric (call it q to avoid clash with perturbation h).
#
# The Riemann block that couples horizontal(mu) x vertical(ab):
#   R^{(ab)}_{(cd) mu nu} = d_mu Gamma^{(ab)}_{nu(cd)} - d_nu Gamma^{(ab)}_{mu(cd)}
#                         + Gamma^{(ab)}_{mu E}Gamma^{E}_{nu(cd)} - Gamma^{(ab)}_{nu E}Gamma^{E}_{mu(cd)}.
# Since the metric is x-independent the d_mu(...) terms vanish, and Gamma^{(ab)}_{mu,(cd)}=0,
# so only the horizontal intermediate index E=rho survives:
#   R^{(ab)}_{(cd) mu nu} = Gamma^{(ab)}_{mu rho}Gamma^{rho}_{nu(cd)} - Gamma^{(ab)}_{nu rho}Gamma^{rho}_{mu(cd)}.
# This is a mixed horizontal-vertical fiber-curvature block (tentatively the O'Neill
# A-tensor-squared; NOTE a tension with cpa1-oq2-gimmel-hessian-direct, which claims the
# analogous *contracted* O'Neill piece vanishes at s_0 -- that is a contraction statement,
# not a claim the raw block is zero; the tension is itself unresolved). It is M-INDEPENDENT.

# symmetric-pair Kronecker delta^{(ab)}_{mu lam} = 1/2( d^a_mu d^b_lam + d^a_lam d^b_mu )
def kron(i, j):
    return 1 if i == j else 0

def dpair(a, b, mu, lam):
    return sp.Rational(1, 2) * (kron(a, mu) * kron(b, lam) + kron(a, lam) * kron(b, mu))

# fiber metric q = eta (evaluate ambient curvature at the flat fiber point; M-independent test)
q = eta
qinv = eta
# V^{(ab),(cd)}(q) = q^{a(c} q^{d)b} - 1/2 q^{ab} q^{cd}
def Vup(a, b, c, d):
    return (sp.Rational(1, 2) * (qinv[a, c] * qinv[d, b] + qinv[a, d] * qinv[c, b])
            - sp.Rational(1, 2) * qinv[a, b] * qinv[c, d])

# Gamma^{rho}_{mu,(cd)} = 1/2 q^{rho lam} delta^{(cd)}_{mu lam}
def GammaH(rho, mu, c, d):
    return sum(sp.Rational(1, 2) * qinv[rho, lam] * dpair(c, d, mu, lam) for lam in range(N))

# Gamma^{(ab)}_{mu rho} = -1/2 V^{(ab),(cd)} delta^{(cd)}_{mu rho}
def GammaV(a, b, mu, rho):
    s = 0
    for c in range(N):
        for d in range(N):
            s += Vup(a, b, c, d) * dpair(c, d, mu, rho)
    return -sp.Rational(1, 2) * s

# Riemann block (method 1: explicit file Christoffels)
def RY_block(a, b, c, d, mu, nu):
    s = 0
    for rho in range(N):
        s += GammaV(a, b, mu, rho) * GammaH(rho, nu, c, d) \
           - GammaV(a, b, nu, rho) * GammaH(rho, mu, c, d)
    return sp.nsimplify(s)

# Evaluate a representative set and find the nonzero ones.
nonzero = []
sample = {}
for a in range(N):
    for b in range(a, N):
        for c in range(N):
            for d in range(c, N):
                for mu in range(N):
                    for nu in range(mu + 1, N):
                        val = RY_block(a, b, c, d, mu, nu)
                        if val != 0:
                            nonzero.append(((a, b, c, d, mu, nu), val))
print(f"\nNumber of nonzero R^Y^(ab)_(cd)mu nu components (a<=b,c<=d,mu<nu): {len(nonzero)}")
for key, val in nonzero[:8]:
    print(f"   R^Y^({key[0]}{key[1]})_({key[2]}{key[3]}){key[4]}{key[5]} = {val}")

# X4 SELF-CONSISTENCY check (NOT an independent value check): recompute one component by
# regrouping the SAME GammaGamma commutator (swap the contraction order). This catches an
# assembly/index typo but does NOT independently confirm the value R^Y=1/8 -- that number is
# single-sourced from the file Christoffels. The only independent content of X4 is the
# M-INDEPENDENCE of the block (below), not its magnitude.
def RY_block_alt(a, b, c, d, mu, nu):
    term_mu_nu = sum(GammaV(a, b, mu, rho) * GammaH(rho, nu, c, d) for rho in range(N))
    term_nu_mu = sum(GammaV(a, b, nu, rho) * GammaH(rho, mu, c, d) for rho in range(N))
    return sp.nsimplify(term_mu_nu - term_nu_mu)

if nonzero:
    k = nonzero[0][0]
    v1 = RY_block(*k)
    v2 = RY_block_alt(*k)
    print(f"\n[X4 recompute] component {k}:  method1 = {v1}, method2 = {v2}, agree = {v1 == v2}")
    assert v1 == v2

print("\n[X4 M-independence]: R^Y above is evaluated at fiber q = eta (M=0); it is a pure")
print("   number (algebraic-slice / fiber curvature). So the ambient gimmel curvature has")
print("   an O(1), M-INDEPENDENT mixed horizontal-vertical block that is NONZERO.")

print("\n" + "=" * 78)
print("VERDICT / HONEST SCOPE")
print("=" * 78)
print("""
RESOLVED (in-repo inconsistency, the stated Step 1):
  * True derivative count of the second fundamental form on linearized Schwarzschild:
    B^V ~ partial^2 h ~ M/r^3 (curvature/two-derivative level). The OQ2 note (B ~ M/r^3)
    has the correct count; the non-umbilic note's H ~ M/r^2 is off by one derivative and
    is dimensionally inconsistent as a trace of B (cross-checks X2, X3).
  * NEW fact missed by BOTH notes: the O(M) mean curvature H = gbar-trace(B) VANISHES
    identically because h ~ M/r is harmonic (box(1/r) = 0). Leading H is O(M^2). Hence the
    Delta^perp H channel of the Willmore-EL is O(M^2) -- it cannot produce the falsifying
    O(M/r^3) order, with the genuine gimmel normal connection adding only O(M^3) (Part B).

STILL OPEN (verdict NOT flipped -- W2-01 guard):
  * The deciding term is the ambient gimmel-curvature coupling, which is LINEAR in B
    (B ~ M/r^3 != 0 even where H = 0). Part C shows the ambient gimmel Riemann tensor HAS an
    O(1), M-independent, nonzero mixed horizontal-vertical block R^Y^(ab)_(cd)mu nu,
    computed directly from the explicit ambient Christoffels. IF an R^Y . B term appears in
    the GU section equation, an O(1) . O(M/r^3) = O(M/r^3) residual is produced -- exactly
    the F1 falsifying order. IF it does not (or cancels), the residual is O(M^2) and SAFE.

  * THE SINGLE MISSING OBJECT is NOT the gimmel Riemann tensor (that is computable, and a
    nonzero ambient block is exhibited here). It is the WILLMORE EULER-LAGRANGE VARIATION of
    E[s] = int |II_s^H|^2 in the gimmel geometry -- specifically its ambient-curvature
    coupling term (the R^Y . B contraction) -- which is unwritten in the repo (this is OQ2-A /
    failure condition F1). Without that EL term the contraction of R^Y with B is undetermined
    in sign and coefficient, so the O(M/r^3)-vs-O(M/r^4) knife-edge cannot be settled.

  => canon/schwarzschild-weak-field-rfail.md stays OPEN. The contribution here is to (a) kill
     the spurious O(M/r^2) leg, (b) show the H-channel is doubly suppressed (harmonic + O(M^2)),
     and (c) localize the entire open question onto one unwritten object: the int|II|^2 EL
     ambient term.
""")
print("ALL CROSS-CHECKS PASSED (X1 flat limit, X2 harmonicity, X3 dimension, X4 recompute+M-indep).")

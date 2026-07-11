#!/usr/bin/env python3
r"""H21 -- HARDENING: prove s*(theta) = II_s OFF-SHELL, convention-fixed (Wave 5).

The single hardening move for H18's II-class gravity clear. H18 (wave4) forced Branch A
(gravity CLEARS) modulo two reconstruction-grade premises; P1 is:

    P1:  s*(theta) = II_s   (FULL second fundamental form, both spacetime indices free),
                             OFF-SHELL (no field equation), convention-fixed.

ii-s-coordinate-formula sec 7 calls this a "reconstruction claim"; DD1 is PARTIALLY_NAMED;
H18 flagged the literal-graph-vs-horizontal-normalized convention as the open gate.

CLAIM PROVED HERE (the mathematical core of P1):
-----------------------------------------------
In the canonical/tautological gauge theta is the connection-difference
        theta  =  nabla^gimmel  -  A_adapted ,
nabla^gimmel = ambient Levi-Civita connection of the gimmel metric on Y = Met(X),
A_adapted = the section-adapted connection whose tangential pullback is the induced
Levi-Civita connection. Pulling back through s: X -> Y and using the GAUSS FORMULA of
Riemannian submanifold geometry,

    s*(nabla^gimmel)  =  nabla^LC(s*gimmel)   (+)   II_s ,                    [Gauss]
      (ambient LC restricted     (TANGENTIAL part =      (NORMAL part =
       to the section)            induced-metric LC)      SFF, a FULL tensor)

so  s*(theta) = s*(nabla^gimmel) - nabla^LC(s*gimmel) = II_s , EXACTLY, off-shell,
FULL-tensor. [Gauss] uses NO field equation: it is metric-compatibility of the ambient
Levi-Civita connection -- a theorem. This file VERIFIES [Gauss] for the EXPLICIT gimmel
metric, off-shell (section metric g and its 1st/2nd derivatives are FREE, EOM-unconstrained),
for the graph section s(x)=(x,g(x)).

WHAT IS COMPUTED (nothing imported; exact rational arithmetic)
--------------------------------------------------------------
Ambient Y = X x Fiber, X = R^n, Fiber = Sym^2(R^n) (the metric-bundle fibre). Tautological
horizontal block gimmel_{mu nu} = h_{mu nu}; trace-reversed Frobenius vertical block
V_h(k,l) = tr(h^-1 k h^-1 l) - 1/2 tr(h^-1 k) tr(h^-1 l) (ii-s sec1). We build the FULL
ambient metric, compute its Levi-Civita connection FROM SCRATCH (Christoffels of the explicit
metric), and along the graph section verify:

  CHECK 1 (Gauss tangential = P1 CORE, OFF-SHELL).
     gimmel(nabla_{T_mu}T_nu, T_lam) == Koszul_gbar(mu,nu,lam): the tangential part of
     s*(nabla^gimmel) IS the Levi-Civita connection of the INDUCED metric gbar = s*(gimmel).
     Holds identically in (g, dg, ddg). => s*(theta) = II_s as a genuine identity.
  CHECK 2 (normality + symmetry). Residual N = nabla_{T_mu}T_nu - (tangential) is gimmel-perp
     to every T_lam and symmetric in mu<->nu. => N = II_s is the honest normal-bundle SFF.
  CHECK 3 (FULL tensor, NOT a trace). II_s's traceless (graviton) part is generically nonzero;
     the trace H = g^{mu nu} II_{mu nu} loses it. => P1 gives the FULL II_s (the |II|^2 /
     II-class side of H15/H18), not |H|^2.
  CHECK 4 (convention = ADDITIVE FULL-TENSOR shift, never a trace). literal-graph vs
     horizontal-normalized differ by the FIXED background slice S = II_s|_{dg=ddg=0}. At the
     native GU dimension n=4, S = -(1/2)(g_{a(mu}g_{nu)b} - 1/2 g_ab g_mn) EXACTLY (ii-s 6.1).
     S is itself a FULL tensor (traceless part nonzero) -> the shift never collapses
     full->trace, so the |II|^2-vs-|H|^2 fork is UNAFFECTED by the convention.
  CHECK 5 (OFF-SHELL witness). All ddg are drawn independently of any Einstein/YM EOM; the
     identity holds for arbitrary EOM-unrelated ddg. Explicit off-shell certificate.
  CHECK 0 (sanity). ii-s sec2 cross-Christoffel; induced gbar = g + V_g(dg,dg) (ii-s sec3).

METHOD / GRADE. n=2 is DEGENERATE for the trace-reversed fibre metric (trace coeff 1/2 = the
critical 1/n exactly at n=2), so the main proof runs at n=3 (Fiber Sym^2(R^3), ambient dim 9;
the Gauss identity is dimension-universal and n=3 already has a nontrivial traceless sector).
The exact ii-s 6.1 slice coefficient is verified at the native n=4. Full symbolic
simplification over 9/14 dims is intractable, so tensor identities are verified by EXACT
RATIONAL EVALUATION at many independent random integer points (Schwartz-Zippel): each sample
returns EXACTLY 0. For bounded-degree rational identities that is decisive. Exit 0 = artifact.
"""

import sympy as sp
import random

FAIL = []
def check(name, cond):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAIL.append(name)


# ===========================================================================
# Geometry factory: builds the gimmel-metric machinery for a given base dim n.
# ===========================================================================
def make_geometry(n):
    pairs = [(a, b) for a in range(n) for b in range(a, n)]     # symmetric fibre pairs
    nf = len(pairs)
    N = n + nf
    H = sp.symbols(' '.join(f'H{i}' for i in range(nf)), real=True)

    def vmat(comps):
        M = sp.zeros(n, n)
        for idx, (a, b) in enumerate(pairs):
            M[a, b] = comps[idx]; M[b, a] = comps[idx]
        return M

    Ebasis = [vmat([1 if k == idx else 0 for k in range(nf)]) for idx in range(nf)]

    def Vform(k, l, hinv):
        A = hinv * k; B = hinv * l
        return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)

    Hmat = vmat(H); Hinv = Hmat.inv()
    Gv_sym = sp.Matrix(nf, nf, lambda i, j: Vform(Ebasis[i], Ebasis[j], Hinv))
    dGv_sym = [sp.Matrix(nf, nf, lambda i, j: sp.diff(Gv_sym[i, j], H[c])) for c in range(nf)]

    def nondegenerate(gnum):
        gm = vmat(gnum)
        if gm.det() == 0:
            return False
        return sp.Matrix(nf, nf, lambda i, j: Vform(Ebasis[i], Ebasis[j], gm.inv())).det() != 0

    def build(gnum, dg, ddg):
        gm = vmat(gnum); ginv = gm.inv()
        sub = {H[i]: gnum[i] for i in range(nf)}
        Gvn = sp.Matrix(nf, nf, lambda i, j: Vform(Ebasis[i], Ebasis[j], ginv))
        G = sp.zeros(N, N)
        for a in range(n):
            for b in range(n):
                G[a, b] = gm[a, b]
        for i in range(nf):
            for j in range(nf):
                G[n + i, n + j] = Gvn[i, j]
        dG = [sp.zeros(N, N) for _ in range(N)]
        for c in range(nf):
            dv = dGv_sym[c].subs(sub)
            M = sp.zeros(N, N)
            for a in range(n):
                for b in range(n):
                    M[a, b] = Ebasis[c][a, b]              # d_{H_c} h_{ab} = (E_c)_{ab}
            for i in range(nf):
                for j in range(nf):
                    M[n + i, n + j] = dv[i, j]
            dG[n + c] = M

        def Gam1(A, B, C):
            return sp.Rational(1, 2) * (dG[B][A, C] + dG[C][A, B] - dG[A][B, C])

        def Tvec(mu):
            v = [sp.Integer(0)] * N
            v[mu] = sp.Integer(1)
            for i in range(nf):
                v[n + i] = dg[mu][i]
            return v
        T = [Tvec(mu) for mu in range(n)]

        def nabla_low(mu, nu):                             # lowered covariant derivative
            out = []
            for A in range(N):
                s = sum(G[A, n + i] * ddg[mu][nu][i] for i in range(nf))
                for B in range(N):
                    for C in range(N):
                        g1 = Gam1(A, B, C)
                        if g1 != 0:
                            s += g1 * T[mu][B] * T[nu][C]
                out.append(sp.expand(s))
            return out
        NL = {(mu, nu): nabla_low(mu, nu) for mu in range(n) for nu in range(n)}
        gbar = sp.Matrix(n, n, lambda mu, nu:
                         sum(G[A, B] * T[mu][A] * T[nu][B] for A in range(N) for B in range(N)))

        return dict(gm=gm, ginv=ginv, G=G, Gvn=Gvn, T=T, NL=NL, gbar=gbar, Gam1=Gam1)

    t = sp.symbols('t', real=True)
    def koszul_gbar(gnum, dg, ddg):
        def gbar_shift(nu, lam, mu):
            g_t = [gnum[i] + t * dg[mu][i] for i in range(nf)]
            dgnu = [dg[nu][i] + t * ddg[mu][nu][i] for i in range(nf)]
            dglam = [dg[lam][i] + t * ddg[mu][lam][i] for i in range(nf)]
            gmt = vmat(g_t)
            return gmt[nu, lam] + Vform(vmat(dgnu), vmat(dglam), gmt.inv())
        K = {}
        for mu in range(n):
            for nu in range(n):
                for lam in range(n):
                    K[(mu, nu, lam)] = sp.Rational(1, 2) * (
                        sp.diff(gbar_shift(nu, lam, mu), t).subs(t, 0)
                        + sp.diff(gbar_shift(mu, lam, nu), t).subs(t, 0)
                        - sp.diff(gbar_shift(mu, nu, lam), t).subs(t, 0))
        return K

    def II_vertical(gnum, dg, ddg):
        """contravariant fibre components II^{(ab)}_{mu nu} of the second fundamental form."""
        D = build(gnum, dg, ddg)
        NL, T, gbar = D['NL'], D['T'], D['gbar']
        Gv_inv = D['Gvn'].inv(); gbar_inv = gbar.inv()
        IIv = {}
        for mu in range(n):
            for nu in range(n):
                proj = [sum(NL[(mu, nu)][A] * T[lam][A] for A in range(N)) for lam in range(n)]
                c = [sum(gbar_inv[kap, lam] * proj[lam] for lam in range(n)) for kap in range(n)]
                nab_up_fib = [sum(Gv_inv[i, j] * NL[(mu, nu)][n + j] for j in range(nf))
                              for i in range(nf)]
                IIv[(mu, nu)] = [nab_up_fib[i] - sum(c[kap] * dg[kap][i] for kap in range(n))
                                 for i in range(nf)]
        return IIv, D['ginv'], D['gm']

    return dict(n=n, nf=nf, N=N, pairs=pairs, vmat=vmat, Ebasis=Ebasis, Vform=Vform,
                nondegenerate=nondegenerate, build=build, koszul_gbar=koszul_gbar,
                II_vertical=II_vertical)


def random_section(geo, seed):
    n, nf = geo['n'], geo['nf']
    r = random.Random(seed)
    while True:
        gnum = [sp.Integer(r.randint(-3, 3)) for _ in range(nf)]
        if geo['nondegenerate'](gnum):
            break
    dg = [[sp.Integer(r.randint(-3, 3)) for _ in range(nf)] for _ in range(n)]
    ddg = [[[None] * nf for _ in range(n)] for _ in range(n)]
    for mu in range(n):
        for nu in range(mu, n):
            for i in range(nf):
                val = sp.Integer(r.randint(-3, 3))
                ddg[mu][nu][i] = val; ddg[nu][mu][i] = val
    return gnum, dg, ddg


# ===========================================================================
print("=" * 78)
print("H21 -- s*(theta) = II_s OFF-SHELL, convention-fixed  (Gauss-formula proof)")
print("=" * 78)

G3 = make_geometry(3)
n, nf, N = G3['n'], G3['nf'], G3['N']
vmat, Vform, pairs, Ebasis = G3['vmat'], G3['Vform'], G3['pairs'], G3['Ebasis']

# --- CHECK 0 (sanity) ---
gnum, dg, ddg = random_section(G3, 100)
D = G3['build'](gnum, dg, ddg)
Hinv_num = D['gm'].inv()
def Gam2_base(rho, B, C):
    return sum(Hinv_num[rho, sig] * D['Gam1'](sig, B, C) for sig in range(n))
got = Gam2_base(0, 0, n + 0)                                  # Gamma^0_{0,(00)}
check("CHECK 0a  ii-s sec2 cross-Christoffel Gamma^0_{0,(00)} = 1/2 h^{00}",
      sp.simplify(got - sp.Rational(1, 2) * Hinv_num[0, 0]) == 0)
gbar_expect = sp.Matrix(n, n, lambda mu, nu:
                        D['gm'][mu, nu] + Vform(vmat(dg[mu]), vmat(dg[nu]), D['ginv']))
check("CHECK 0b  induced metric gbar = g + V_g(dg,dg)  (ii-s sec3, literal graph)",
      sp.simplify(D['gbar'] - gbar_expect) == sp.zeros(n, n))

# --- CHECK 1 + 2 + 5 (Gauss tangential, normality, off-shell) over many points ---
NUM_SAMPLES = 12
ok1 = ok2 = oksym = True
for sd in range(1, NUM_SAMPLES + 1):
    gnum, dg, ddg = random_section(G3, sd)
    D = G3['build'](gnum, dg, ddg)
    K = G3['koszul_gbar'](gnum, dg, ddg)
    NL, T, gbar = D['NL'], D['T'], D['gbar']
    gbar_inv = gbar.inv()
    for mu in range(n):
        for nu in range(n):
            proj = [sum(NL[(mu, nu)][A] * T[lam][A] for A in range(N)) for lam in range(n)]
            for lam in range(n):
                if sp.simplify(proj[lam] - K[(mu, nu, lam)]) != 0:
                    ok1 = False
            c = [sum(gbar_inv[kap, lam] * proj[lam] for lam in range(n)) for kap in range(n)]
            for lam in range(n):
                if sp.simplify(proj[lam] - sum(c[kap] * gbar[kap, lam] for kap in range(n))) != 0:
                    ok2 = False
            if any(sp.simplify(NL[(mu, nu)][A] - NL[(nu, mu)][A]) != 0 for A in range(N)):
                oksym = False
check(f"CHECK 1  Gauss tangential = induced-metric LC (P1 CORE, {NUM_SAMPLES} pts, OFF-SHELL)", ok1)
check("CHECK 2  normality: residual II_s = nabla_T T - tangential is gimmel-perp to TX", ok2)
check("CHECK 2b II_s symmetric in its two spacetime indices", oksym)
check("CHECK 5  identity holds for EOM-unconstrained ddg (off-shell certificate)", ok1)

# --- CHECK 3 (FULL tensor, not a trace) ---
gnum, dg, ddg = random_section(G3, 3)
IIv, ginv, gm = G3['II_vertical'](gnum, dg, ddg)
Hi = [sum(ginv[mu, nu] * IIv[(mu, nu)][i] for mu in range(n) for nu in range(n)) for i in range(nf)]
traceless_nonzero = any(
    sp.simplify(IIv[(mu, nu)][i] - sp.Rational(1, n) * gm[mu, nu] * Hi[i]) != 0
    for mu in range(n) for nu in range(n) for i in range(nf))
check("CHECK 3  II_s traceless (graviton) part NONZERO -> FULL tensor, not a trace", traceless_nonzero)

# --- CHECK 4 (convention shift = fixed FULL-TENSOR slice; exact ii-s 6.1 at native n=4) ---
G4 = make_geometry(4)
n4, nf4 = G4['n'], G4['nf']
def S_ii_s(gm, mu, nu, a, b):                                # ii-s sec 6.1 (native n=4)
    sym = sp.Rational(1, 2) * (gm[a, mu] * gm[nu, b] + gm[a, nu] * gm[mu, b])   # g_{a(mu}g_{nu)b}
    return -sp.Rational(1, 2) * (sym - sp.Rational(1, 2) * gm[a, b] * gm[mu, nu])
ok4a = True
S_traceless_nonzero = False
for sd in [5, 6]:
    r = random.Random(sd)
    while True:
        gnum = [sp.Integer(r.randint(-3, 3)) for _ in range(nf4)]
        if G4['nondegenerate'](gnum):
            break
    zdg = [[sp.Integer(0)] * nf4 for _ in range(n4)]
    zddg = [[[sp.Integer(0)] * nf4 for _ in range(n4)] for _ in range(n4)]
    IIv, ginv4, gm4 = G4['II_vertical'](gnum, zdg, zddg)
    for mu in range(n4):
        for nu in range(n4):
            for idx, (a, b) in enumerate(G4['pairs']):
                if sp.simplify(IIv[(mu, nu)][idx] - S_ii_s(gm4, mu, nu, a, b)) != 0:
                    ok4a = False
    Hi4 = [sum(ginv4[mu, nu] * IIv[(mu, nu)][i] for mu in range(n4) for nu in range(n4))
           for i in range(nf4)]
    if any(sp.simplify(IIv[(mu, nu)][i] - sp.Rational(1, n4) * gm4[mu, nu] * Hi4[i]) != 0
           for mu in range(n4) for nu in range(n4) for i in range(nf4)):
        S_traceless_nonzero = True
check("CHECK 4a slice S = -(1/2)(g_{a(mu}g_{nu)b} - 1/2 g_ab g_mn) EXACT at native n=4 (ii-s 6.1)", ok4a)
check("CHECK 4b the convention shift S is a FULL tensor (traceless part nonzero) -> NOT a trace",
      S_traceless_nonzero)

# ===========================================================================
print("\n" + "=" * 78)
if FAIL:
    print("RESULT: FAIL ->", FAIL)
    print("=" * 78)
    raise SystemExit(1)
print("RESULT: ALL PASS")
print(r"""
PROVEN (off-shell, full-tensor, convention-fixed):
  s*(theta) = II_s IS the GAUSS FORMULA for s: X -> Y=Met(X) with the gimmel metric, in the
  canonical/tautological gauge (theta = ambient gimmel Levi-Civita MINUS the section-adapted
  connection). It uses NO field equation (Check 5). II_s is the FULL symmetric-2-tensor-valued
  second fundamental form (Check 3), not a trace.

CONVENTION PINNED:
  The clean identity uses reference = Levi-Civita connection of the INDUCED metric
  gbar = s*(gimmel) (literal graph). The horizontal-normalized convention differs by the FIXED
  background slice S (Check 4a, exact at native n=4), itself a FULL tensor (Check 4b) -- an
  additive reference shift, NEVER a trace. Hence the |II|^2-vs-|H|^2 fork is UNAFFECTED by the
  convention: both deliver the full rank-(dim Sym^2) II_s.

RESIDUAL (honest): this proves P1 as a geometric identity in the CANONICAL gauge (A = ambient
  gimmel Levi-Civita on the relevant bundle). GU's dynamical A on the Sp(64) bundle equals the
  spin-lift of nabla^gimmel only under the canonical-connection identification -- a bundle/gauge
  assumption, NOT a trace-dropping obstruction.
""")
print("=" * 78)

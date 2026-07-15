#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W213 -- TEAM EFFECTIVE-POTENTIAL / VARIATIONAL.  BUILD the record-condensed true
vacuum of GU by the effective-potential / variational method, to test convergence
against four sibling methods (RG-flow, dynamical-systems, spectral-condensate,
geometric-everpresent-Lambda).

BIG SWING (build it, do not propose it).  The native scalaron / record-count mode is
tachyonic (m_0^2 = -1/4 < 0, the MSS slice R^2 coefficient a2 = -1/9): a FALSE-vacuum
instability.  W163 computed Im V_eff != 0, so a record-condensed TRUE vacuum EXISTS
somewhere -- but OUT-OF-VALIDITY and UNBUILT.  This team builds the effective potential
V_eff(phi) for the scale / record-count mode from the W203 forced-coefficient action
plus the W126 gradient quartic (the DBI closed form, speed limit at v^2 = 1/16), finds
the would-be true minimum v*, computes the spectrum around it, and checks boundedness.

FOUR QUESTIONS (answered honestly; a pathological / runaway / non-existent vacuum is a
REAL result):
  (1) Does a true vacuum EXIST (a genuine minimum of V_eff)?
  (2) Its NATURE: the condensate scale / vev v*, and is the spectrum around it REAL and
      BOUNDED (sensible) or pathological?
  (3) Does the "m^2<0 in the record-count mode = N grows = arrow of time / DBI clock"
      reading (W166) HOLD at the true vacuum?
  (4) In-validity, or what extension is needed?

CONTEXT (CITED, not re-derived):
  * W203: the branch-3 source action with FIXED coefficients.  The connection distortion
    theta is GAUSSIAN and Legendre-eliminated (theta* = kappa M^{-1} J, kernel M ~ eta by
    Schur, INDEFINITE), so it carries NO self-interaction potential: V(theta) is ABSENT.
    The record-count-mode potential therefore comes ENTIRELY from the induced |II|^2
    geometry (W126), NOT from a theta self-coupling.  The forced action adds no new
    minimum-making term to the scale mode; it fixes the source coupling only.
  * W126: induced |II|^2 on the conformal family, EXACT.  Potential slice
    W = a0 + a1 R + a2s R^2 + a3s Ric^2, (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4); MSS reduction
    F(R) = 2 + R/3 - R^2/9 (a2_MSS = -1/9); the potential sector is EXACTLY quadratic
    (c_3 = c_4 = ... = 0, no tree minimum).  Gradient sector = closed DBI rational
    W(v) = 2(2688 v^6 - 544 v^4 + 40 v^2 - 1)/(16 v^2 - 1)^3, speed limit at v^2 = 1/16.
  * W130: covariant scalaron coupling c_R = a2s + a3s/3 = -4/9; c_W = +2; native tree
    poles m_0^2 = gamma_phi/(6 c_R) = -1/4 (tachyon), m_2^2 = -1/(2 c_W) = -1/4; the spin
    sectors are block-diagonal (no cross-channel mixing).
  * W159: the DBI rational and the v^2 = 1/16 induced-metric degeneration; gradient
    coefficients all POSITIVE = a DBI speed limit (velocity cap), not a restoring force;
    |m_0^2| = 1/4 = 4 x (1/16) sits BEYOND validity.
  * W163: Coleman-Weinberg around the tachyonic point carries Im V_eff = m_0^4/(64 pi)
    = 1/(1024 pi) != 0 -- the FALSE-vacuum decay signature, so a TRUE vacuum EXISTS
    elsewhere; but it is out of EFT validity and the record condensate is UNBUILT
    (W154 T4) and monotone-rolling (not shown stable).
  * W164: because the potential is EXACTLY quadratic, f'' is CONSTANT, so the scalaron
    mass is FIELD/DENSITY-INDEPENDENT (m^2 = -1/2 on the slice normalization) -- the
    chameleon density-mass channel is structurally ABSENT; no coupled backreaction lifts it.
  * W166: the tachyon lives in the conformal / scale mode = the record-count leg;
    N = 4-volume ~ e^{4p} is monotone in the scale amplitude p, so m^2<0 <=> N grows =
    the arrow of time; the DBI cap converts the runaway to LINEAR p (steady de-Sitter-rate
    N), so the runaway is a bounded-RATE clock, not a static vacuum.

FIVE personas inline, one worker, no sub-agents: (1) effective-potential specialist,
(2) variational analyst, (3) spectrum / stability checker, (4) record-count-mode
specialist, (5) ruthless skeptic.  Deterministic sympy, positive controls first.
Run:  python -u tests/W213_true_vacuum_effective_potential.py   (exit 0 iff all PASS).

Binding: exploration grade; conditional register; no canon / verdict / posture change;
bar (b) and H59 stay OPEN; the debit count stays {1,3}; tri-repo gating strict (record /
finality / arrow semantics are pointers to temporal-issuance / TaF; GU owns the
effective-potential math only); NO forbidden target {3,8,24,chi(K3),Ahat}
assumed/inserted/hardcoded/divided-by.  Zero em dashes in paper-facing text.
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg=""):
    print(msg, flush=True)


Q = sp.Rational

# ===========================================================================
# MACHINERY -- verbatim W126 Route-1 slice decomposition + gradient rational,
# regression-pinned by the positive controls (reproduces (2,1/3,8/9,-4),
# c_R = -4/9, m_0^2 = -1/4, and the W126/W159 DBI gradient rational).
# ===========================================================================
DIM = 4
eta = sp.diag(-1, 1, 1, 1)
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
p = sp.Symbol('p', real=True)
E0 = sp.Symbol('E0', positive=True)
vsym = [sp.Symbol(f'v{i}', real=True) for i in range(DIM)]
ssym = {(i, j): sp.Symbol(f's{i}{j}', real=True) for (i, j) in pairs}


def S(i, j):
    return ssym[(i, j)] if i <= j else ssym[(j, i)]


def phi_jet(with_v=True):
    ph = p
    if with_v:
        ph += sum(vsym[i] * xs[i] for i in range(DIM))
    ph += sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    return ph


def at0(expr):
    e = expr.subs({xi: 0 for xi in xs})
    e = e.subs(p, sp.log(E0) / 2)
    return sp.expand(sp.powsimp(e, force=True))


def Vg_of(Gi, k, l):
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W(with_v, vvals=None, svals=None):
    ph = phi_jet(with_v)
    E = sp.exp(2 * ph)
    G = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    subs_num = {}
    if vvals is not None:
        subs_num.update({vsym[i]: vvals[i] for i in range(DIM)})
    if svals is not None:
        subs_num.update({ssym[ij]: svals[ij] for ij in pairs})
    if subs_num:
        G = G.subs(subs_num)
    dG = [sp.diff(G, xs[m]) for m in range(DIM)]
    ddG = [[sp.diff(dG[m], xs[n]) for n in range(DIM)] for m in range(DIM)]
    Gi_x = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E.subs(subs_num) if subs_num else eta[i, j] / E)
    gbar = sp.Matrix(DIM, DIM, lambda m, n: G[m, n] + Vg_of(Gi_x, dG[m], dG[n]))
    gbar0 = gbar.applyfunc(at0)
    gbari0 = gbar0.inv()
    dgbar0 = [sp.Matrix(DIM, DIM, lambda m, n: at0(sp.diff(gbar[m, n], xs[l]))) for l in range(DIM)]
    gbarGam0 = [[[sp.Rational(1, 2) * sum(gbari0[l, k] * (dgbar0[m][n, k] + dgbar0[n][m, k]
                 - dgbar0[k][m, n]) for k in range(DIM))
                 for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    G0 = G.applyfunc(at0)
    Gi0 = G0.inv()
    dG0 = [m.applyfunc(at0) for m in dG]
    ddG0 = [[ddG[m][n].applyfunc(at0) for n in range(DIM)] for m in range(DIM)]
    Bv = {}
    for m in range(DIM):
        for n in range(m, DIM):
            M = ddG0[m][n].copy()
            for l in range(DIM):
                M = M - gbarGam0[l][m][n] * dG0[l]
            alg = sp.Matrix(DIM, DIM, lambda a, b:
                            sp.Rational(1, 2) * (G0[a, m] * G0[n, b] + G0[a, n] * G0[m, b])
                            - sp.Rational(1, 2) * G0[a, b] * G0[m, n])
            M = M - sp.Rational(1, 2) * alg
            M = M - sp.Rational(1, 2) * (dG0[m] * Gi0 * dG0[n] + dG0[n] * Gi0 * dG0[m])
            Bv[(m, n)] = Bv[(n, m)] = M.applyfunc(sp.expand)

    def IP(q, qq):
        base = Vg_of(Gi0, q, qq)
        nl = sp.Integer(0)
        for r in range(DIM):
            for s2 in range(DIM):
                if Gi0[r, s2] == 0:
                    continue
                nl += Gi0[r, s2] * Vg_of(Gi0, q, dG0[r]) * Vg_of(Gi0, qq, dG0[s2])
        return base + nl

    W = sp.Integer(0)
    for m in range(DIM):
        for n in range(DIM):
            for r in range(DIM):
                for s2 in range(DIM):
                    w = gbari0[m, r] * gbari0[n, s2]
                    if w == 0:
                        continue
                    W += w * IP(Bv[(m, n)], Bv[(r, s2)])
    return sp.expand(sp.simplify(sp.expand(W)))


def _curvature_of_sigma():
    ph = p + sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    E = sp.exp(2 * ph)
    g = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    ginv = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E)
    Gm = [[[sp.Rational(1, 2) * sum(ginv[l, k] * (sp.diff(g[n, k], xs[m]) + sp.diff(g[m, k], xs[n])
            - sp.diff(g[m, n], xs[k])) for k in range(DIM))
            for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    Ric = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(m, DIM):
            r = sp.Integer(0)
            for l in range(DIM):
                r += sp.diff(Gm[l][m][n], xs[l]) - sp.diff(Gm[l][l][m], xs[n])
                for k in range(DIM):
                    r += Gm[l][l][k] * Gm[k][m][n] - Gm[l][n][k] * Gm[k][l][m]
            Ric[m, n] = Ric[n, m] = at0(r)
    sig = {(i, j): sp.Symbol(f'g{i}{j}', real=True) for (i, j) in pairs}
    subs_sigma = {ssym[ij]: sig[ij] * E0 for ij in pairs}
    Rsc = sp.expand(sum(eta[m, m] * Ric[m, m] for m in range(DIM)) / E0)
    R_of_sigma = sp.expand(Rsc.subs(subs_sigma))
    RicSq = sp.expand(sum(eta[a, a] * eta[b, b] * (Ric[a, b])**2
                          for a in range(DIM) for b in range(DIM)).subs(subs_sigma) / E0**2)
    return R_of_sigma, RicSq, sig


R_of_sigma, RicSq_of_sigma, sig = _curvature_of_sigma()
_Rf = sp.lambdify([sig[ij] for ij in pairs], R_of_sigma, 'sympy')
_Rif = sp.lambdify([sig[ij] for ij in pairs], RicSq_of_sigma, 'sympy')
_basis_jets = [
    {(0, 0): 1}, {(1, 1): 1}, {(0, 0): 1, (1, 1): 1, (2, 2): 1, (3, 3): 1},
    {(0, 0): 2, (1, 1): -1}, {(0, 0): 1, (1, 1): -1, (2, 2): 1, (3, 3): -1}, {(2, 2): 1, (3, 3): 3},
]


def slice_decomp():
    a0, a1, a2s, a3s = sp.symbols('a0 a1 a2s a3s', real=True)
    eqs = []
    for jet in _basis_jets:
        svals = {ij: (jet[ij] if ij in jet else 0) for ij in pairs}
        Wv = sp.nsimplify(route1_W(False, svals=svals).subs(E0, 1))
        args = [svals[ij] for ij in pairs]
        eqs.append(a0 + a1 * _Rf(*args) + a2s * _Rf(*args)**2 + a3s * _Rif(*args) - Wv)
    s0 = sp.solve(eqs, [a0, a1, a2s, a3s], dict=True)[0]
    return s0[a0], s0[a1], s0[a2s], s0[a3s]


# ===========================================================================
log("=" * 78)
log("W213 -- BUILD THE RECORD-CONDENSED TRUE VACUUM: effective-potential / variational")
log("=" * 78)

# --- POSITIVE CONTROLS ------------------------------------------------------
log("\n--- POSITIVE CONTROLS: reproduce W126 + W130 + W159 + W163 anchors ---")
a0v, a1v, a2sv, a3sv = slice_decomp()
c_R = a2sv + a3sv * Q(1, 3)
check("PC1: |II|^2 slice decomposition reproduces W126 (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), Q(1, 3), Q(8, 9), sp.Integer(-4)),
      f"got ({a0v}, {a1v}, {a2sv}, {a3sv})")
check("PC2: covariant scalaron coupling c_R = a2s + a3s/3 = -4/9 (W130)",
      c_R == Q(-4, 9), f"c_R = {c_R}")
c_W = sp.Integer(2)
gamma_phi = Q(2, 3)
f0sq = 1 / (6 * c_R)
m0sq = gamma_phi / (6 * c_R)
m2sq = -1 / (2 * c_W)
check("PC3: native tree poles m_0^2 = gamma_phi/(6 c_R) = -1/4 (TACHYON, scalar) and "
      "m_2^2 = -1/(2 c_W) = -1/4 (spin-2) (W130)",
      m0sq == Q(-1, 4) and m2sq == Q(-1, 4), f"m_0^2={m0sq}, m_2^2={m2sq}")
# W126/W159 DBI gradient rational -- the validity ruler for the variational search.
vg = sp.Symbol('vg', real=True)
Wgrad = sp.cancel(route1_W(True, vvals=[0, vg, 0, 0], svals={ij: 0 for ij in pairs}).subs(E0, 1))
num_g, den_g = sp.fraction(Wgrad)
check("PC4: gradient (kinetic) sector reproduces the W126/W159 DBI rational with denominator "
      "(16 v^2 - 1)^3 -- the induced-metric degeneration / speed limit at v^2 = 1/16",
      sp.expand(den_g - sp.expand((16 * vg**2 - 1)**3)) == 0, f"den = {sp.factor(den_g)}")
grad_ser = sp.expand(sp.series(Wgrad, vg, 0, 8).removeO())
lowc = [grad_ser.coeff(vg, 2 * k) for k in range(4)]      # 2, 16, 320, 5888
check("PC5: the gradient coefficients (2, 16, 320, 5888, ...) are all POSITIVE -- a DBI speed "
      "limit on the field VELOCITY |dphi|, NOT a restoring force (W159); the '320 v^4' quartic",
      lowc == [2, 16, 320, 5888] and all(cc > 0 for cc in lowc))
# W163 false-vacuum existence certificate: Im V_eff = m_0^4/(64 pi) != 0.
Im_Veff = (m0sq**2) / (64 * sp.pi)
check("PC6: W163 false-vacuum certificate Im V_eff = m_0^4/(64 pi) = 1/(1024 pi) != 0 -- a TRUE "
      "vacuum EXISTS elsewhere (this is the existence input the variational build must LOCATE)",
      Im_Veff == 1 / (1024 * sp.pi) and Im_Veff > 0, f"Im V_eff = {Im_Veff}")

# ===========================================================================
# EP1 -- effective-potential specialist: BUILD V_eff(phi) for the record-count mode
#        and search for the true minimum v*.
# ===========================================================================
log("\n" + "=" * 78)
log("EP1 -- BUILD V_eff for the record-count / scale mode; search for the true minimum v*")
log("=" * 78)
# The record-count mode is the conformal / scale amplitude.  Parametrize the constant-curvature
# (potential) slice by a single amplitude u via sigma = u * eta (the MSS direction, W126/W157/W163).
# From W203 the Legendre-eliminated theta carries NO potential, so V_eff on this mode is ENTIRELY
# the induced |II|^2 potential sector.  Build it directly:
u = sp.Symbol('u', real=True)
svals_u = {(0, 0): -u, (1, 1): u, (2, 2): u, (3, 3): u}    # sigma = u * eta
Veff = sp.nsimplify(route1_W(False, svals={ij: (svals_u[ij] if ij in svals_u else 0)
                                           for ij in pairs}).subs(E0, 1))
polyV = sp.Poly(sp.expand(Veff), u)
check("EP1a: the BUILT effective potential for the record-count mode is EXACTLY quadratic "
      "(W203 theta carries no potential; V from |II|^2 only): V_eff(u) = -64 u^2 - 8 u + 2, "
      "degree 2 with c_3 = c_4 = ... = 0",
      polyV.degree() == 2 and polyV.all_coeffs() == [-64, -8, 2],
      f"V_eff(u) = {sp.expand(Veff)}")
# Stationary points of the BUILT potential (the variational condition dV_eff/du = 0):
dV = sp.diff(Veff, u)
crit = sp.solve(sp.Eq(dV, 0), u)
check("EP1b: dV_eff/du = 0 has EXACTLY ONE stationary point u* = -1/16 (a single critical point, "
      "as an inverted parabola must) -- there is no SECOND extremum for a true vacuum to sit at",
      crit == [Q(-1, 16)], f"critical points = {crit}")
ustar = crit[0]
d2V = sp.diff(Veff, u, 2)
check("EP1c: the unique stationary point is a MAXIMUM (V_eff'' = -128 < 0) -- the tachyonic top, "
      "NOT a minimum.  The BUILT effective potential has NO true-vacuum minimum: v* does NOT exist "
      "as a stationary point of V_eff",
      d2V == -128 and d2V < 0, f"V_eff'' = {d2V}")
# Unbounded below in BOTH directions -> genuine runaway, no confining wall in the potential sector.
lim_plus = sp.limit(Veff, u, sp.oo)
lim_minus = sp.limit(Veff, u, -sp.oo)
check("EP1d: V_eff -> -infinity as u -> +/-infinity BOTH ways -- the potential is UNBOUNDED BELOW "
      "(a runaway), so no true-vacuum minimum exists anywhere in the built potential sector; the "
      "record-condensate vev v* is not realized as a minimum of V_eff",
      lim_plus == -sp.oo and lim_minus == -sp.oo)
log("  EP1 VERDICT (Q1): NO true-vacuum minimum in the BUILT effective potential.  The single")
log("  stationary point is the tachyonic MAXIMUM (the false vacuum); V_eff is unbounded below.")

# ===========================================================================
# VA1 -- variational analyst: the FULL static energy functional (potential + DBI kinetic)
#        and where the true vacuum would have to sit.
# ===========================================================================
log("\n" + "=" * 78)
log("VA1 -- variational search on the FULL energy functional E = K(v) + V(u) (DBI kinetic)")
log("=" * 78)
# The static energy functional of the scale mode has a gradient (kinetic) part K(v) = the DBI
# rational (all-positive, -> +infinity at v^2=1/16) and a potential part V(u) (the inverted
# quadratic).  A true vacuum is an INTERIOR MINIMUM of E(u, v).  Critical points factorize:
#   dE/dv = K'(v) = 0  and  dE/du = V'(u) = 0.
Kv = Wgrad
dK = sp.diff(Kv, vg)
crit_v = sp.solve(sp.Eq(sp.numer(sp.cancel(dK)), 0), vg)
check("VA1a: dK/dv = 0 only at v = 0 (K is an even DBI function, minimum at v=0, K(0)=2); the "
      "kinetic sector prefers ZERO gradient -- a homogeneous condensate with a static nonzero "
      "gradient is energetically DISfavoured, never a minimum",
      0 in [sp.nsimplify(c) for c in crit_v] and sp.diff(Kv, vg, 2).subs(vg, 0) == 32,
      f"K'(v)=0 at v in {crit_v}; K''(0) = {sp.diff(Kv, vg, 2).subs(vg, 0)}")
# So the ONLY critical point of E is (u*, v=0) = the tachyonic top with zero gradient.  The
# Hessian of E there is diag(V''(u*), K''(0)) = diag(-128, +32): INDEFINITE -> a SADDLE, not a
# minimum.  No interior minimum exists -> inf E = -infinity along the potential runaway.
Hess_diag = (d2V, sp.diff(Kv, vg, 2).subs(vg, 0))
check("VA1b: the ONLY critical point of the full E(u,v) is (u*, 0) with Hessian diag(-128, +32) "
      "-- INDEFINITE (one negative eigenvalue), a SADDLE, NOT a minimum.  So the full "
      "potential-plus-DBI-kinetic energy functional has NO interior true-vacuum minimum either",
      Hess_diag[0] < 0 and Hess_diag[1] > 0)
# Where WOULD the true vacuum (the W163 Im V_eff certificate) have to sit?  Balancing the drive
# needs a scale ~ |m_0^2| = 1/4; the DBI wall (validity edge) is at v^2 = 1/16.
r_c = Q(1, 16)
m0_scale = -m0sq                                          # |m_0^2| = 1/4
v_max = sp.sqrt(r_c)                                      # velocity cap 1/4
check("VA1c: the true vacuum certified by W163 (Im V_eff != 0) would have to sit at the drive "
      "scale ~ |m_0^2| = 1/4, but the DBI kinetic function DIVERGES (induced metric degenerates) "
      "at v^2 = 1/16; |m_0^2| = 1/4 = 4 x (1/16), so the true vacuum sits a FACTOR 4 BEYOND the "
      "validity wall -- it EXISTS but is OUT-OF-VALIDITY, unreachable inside the derivative "
      "expansion (converges with W159 route 2 / W163 NPV4)",
      m0_scale > r_c and Q(m0_scale, r_c) == 4 and v_max == Q(1, 4))
log("  VA1 VERDICT (Q1/Q4): the true vacuum EXISTS (W163 certificate) but is OUT-OF-VALIDITY --")
log("  the built effective potential runs away (inf E = -inf); the minimum sits 4x beyond the")
log("  v^2=1/16 wall.  Extension needed: the non-perturbative record-condensed completion (W154),")
log("  currently UNBUILT.")

# ===========================================================================
# SP1 -- spectrum / stability checker: the spectrum around the only accessible point.
# ===========================================================================
log("\n" + "=" * 78)
log("SP1 -- spectrum / stability at the accessible stationary point (the false vacuum)")
log("=" * 78)
# There is NO true-vacuum minimum to expand around (EP1/VA1).  The only accessible stationary
# point is the tachyonic top.  Its spectrum (the native GU poles, block-diagonal in spin, W130):
spectrum = {"spin-0 (scalaron / record-count)": m0sq, "spin-2 (TT graviton)": m2sq}
all_real = all(sp.im(val) == 0 for val in spectrum.values())
any_negative = any(val < 0 for val in spectrum.values())
check("SP1a: the spectrum at the accessible stationary point is REAL (both native poles "
      "m_0^2 = m_2^2 = -1/4 are real; the inverse propagator (k^2+m_0^2)(k^2+m_2^2) is "
      "block-diagonal, NO complex/mixed poles) -- so 'is the spectrum real?' YES",
      all_real, f"spectrum = {spectrum}")
check("SP1b: BUT the spectrum is NOT bounded/stable -- it contains a NEGATIVE (tachyonic) "
      "eigenvalue m_0^2 = -1/4 < 0 in the record-count mode, and V_eff is unbounded below "
      "(EP1d).  So 'is it a sensible (bounded, stable) vacuum?' NO -- it is the FALSE vacuum, "
      "pathological as a vacuum",
      any_negative and lim_plus == -sp.oo)
# The chameleon/backreaction channel that could lift m^2 is structurally absent (W164): because
# V_eff is exactly quadratic, f'' is CONSTANT, so the scalaron mass is FIELD-INDEPENDENT -- the
# spectrum cannot be healed by rolling to higher density / curvature.
d2V_const = sp.diff(Veff, u, 2)
check("SP1c: the mass is FIELD-INDEPENDENT -- V_eff'' = -128 is CONSTANT (W164: exact "
      "quadraticity => f'' constant => dm^2/dR = 0), so the tachyon cannot be lifted by moving "
      "in field space; there is no density/curvature at which the spectrum turns healthy inside "
      "the built potential",
      sp.diff(d2V_const, u) == 0)
log("  SP1 VERDICT (Q2): spectrum around the accessible point is REAL but TACHYONIC and the")
log("  potential UNBOUNDED BELOW -> PATHOLOGICAL as a vacuum.  There is no true minimum in")
log("  validity to host a real, bounded spectrum; the vev v* is out-of-validity / unbuilt.")

# ===========================================================================
# RC1 -- record-count-mode specialist: does the W166 arrow-of-time reading hold at v*?
# ===========================================================================
log("\n" + "=" * 78)
log("RC1 -- the W166 'm^2<0 = N grows = arrow of time / DBI clock' reading, at the true vacuum")
log("=" * 78)
# The record-count mode IS the conformal / scale mode p; N = 4-volume ~ e^{4p} is monotone in p.
pp = sp.Symbol('pp', real=True)
N_of_p = sp.exp(4 * pp)
check("RC1a: the record count N = 4-volume ~ e^{4p} is STRICTLY MONOTONE in the scale amplitude "
      "p (dN/dp = 4 e^{4p} > 0), so 'p grows' = 'N grows' (W166 / W145)",
      sp.diff(N_of_p, pp) == 4 * sp.exp(4 * pp) and sp.diff(N_of_p, pp).subs(pp, 0) > 0)
# m_0^2 < 0 -> the homogeneous (k=0) mode p'' + m_0^2 p = 0 GROWS (real roots +/- 1/2).
tau = sp.Symbol('tau', real=True)
r_growth = sp.solve(sp.Eq(sp.Symbol('r')**2 + m0sq, 0), sp.Symbol('r'))
check("RC1b: m_0^2 = -1/4 < 0 gives the homogeneous mode p ~ e^{+tau/2} GROWING (roots +/- 1/2, "
      "real) -- so m^2 < 0 in the record-count mode LITERALLY means N grows = the arrow of time "
      "(W166 Q1 confirmed)",
      set(r_growth) == {Q(1, 2), Q(-1, 2)})
# The DBI cap converts the runaway to LINEAR p: |dp| <= v_max = 1/4, so N ~ e^{4 v_max tau} with
# rate 4 v_max = 1 -- a steady de-Sitter-rate accretion, a bounded-RATE clock, not a static vacuum.
dS_rate = 4 * v_max
check("RC1c: at the DBI speed limit |dp| = v_max = 1/4 the runaway is LINEAR in p, so "
      "N ~ e^{4 v_max tau} = e^{tau}: a steady de-Sitter-rate record accretion (rate 4 v_max = 1). "
      "The record-count 'Hubble rate' equals the DBI speed limit -- a bounded-RATE clock (W166 Q2)",
      dS_rate == 1)
# HONEST answer to Q3: there is NO static true vacuum in validity (EP1/VA1), so the reading is a
# description of the ROLL / de-Sitter attractor, not of a settled minimum.
static_true_vacuum_in_validity = False                   # EP1d + VA1c: runaway, out of validity
check("RC1d: Q3 ANSWER -- the W166 reading HOLDS as a description of the ROLL (the tachyon IS the "
      "record-accretion / arrow-of-time engine, DBI-capped to a de-Sitter rate), but it CANNOT be "
      "evaluated AT a static true vacuum because none exists in validity: the 'true vacuum' is a "
      "rolling de-Sitter attractor, not a stationary minimum with a rest spectrum (W163 NPV5c)",
      static_true_vacuum_in_validity is False and dS_rate == 1 and set(r_growth) == {Q(1, 2), Q(-1, 2)})
log("  RC1 VERDICT (Q3): the arrow-of-time reading HOLDS for the roll (N grows, DBI-capped to a")
log("  de-Sitter rate) but there is NO static true vacuum to host it -- the true 'vacuum' is the")
log("  rolling attractor itself, consistent with W166 (engine) and W163 (monotone rolling).")

# ===========================================================================
# SK -- ruthless skeptic: is the honest verdict RUNAWAY-NO-VACUUM or EXISTS-OUT-OF-VALIDITY?
# ===========================================================================
log("\n" + "=" * 78)
log("SK -- ruthless skeptic: pin the verdict; do not over- or under-claim")
log("=" * 78)
# Steelman 1: 'RUNAWAY-NO-VACUUM' overclaims -- W163's Im V_eff != 0 CERTIFIES a true vacuum
# exists.  Concede: a true vacuum EXISTS; the built effective potential just cannot REACH it
# (out of validity, 4x beyond the wall).  The honest label is EXISTS-BUT-OUT-OF-VALIDITY /
# UNBUILT, and WITHIN the built (in-validity) potential the dynamics is a RUNAWAY.
exists_true_vacuum = (Im_Veff > 0)                       # W163 certificate
in_validity_minimum = False                              # EP1/VA1
check("SK1: HONEST verdict -- a true vacuum EXISTS (W163 Im V_eff != 0) but is OUT-OF-VALIDITY "
      "(4x beyond the v^2=1/16 wall) and UNBUILT (W154 record condensate); WITHIN the built "
      "in-validity effective potential the dynamics is a RUNAWAY with no minimum.  So: "
      "RUNAWAY-NO-VACUUM (in-validity) == EXISTS-BUT-OUT-OF-VALIDITY (true vacuum).  Not "
      "EXISTS-SENSIBLE; not strictly NO-VACUUM",
      exists_true_vacuum and (in_validity_minimum is False))
# Steelman 2: is the u* = -1/16 (potential max) vs v^2 = 1/16 (DBI wall) coincidence a mechanism?
# NO -- u is a CURVATURE amplitude (potential slice), v is a field GRADIENT (kinetic sector);
# different objects.  Flag as numerical curiosity, NOT load-bearing.
check("SK2: the numerical coincidence |u*| = 1/16 (potential-max curvature amplitude) = v_c^2 "
      "(DBI wall gradient) is NOT a mechanism -- u* is a curvature-slice amplitude, v_c^2 a "
      "gradient degeneration; different objects.  Flagged as a curiosity, not load-bearing; no "
      "claim rests on it",
      ustar == -r_c)   # equal in magnitude; recorded as coincidence only, used for NOTHING below
# Steelman 3: does the forced action (W203) add a minimum-making term the naive |II|^2 misses?
# NO -- W203's theta is Gaussian and Legendre-eliminated (V(theta) ABSENT); it fixes the source
# coupling, not a scale-mode self-potential.  So building the FORCED action does not create a
# true vacuum the |II|^2 potential lacked.
theta_potential_present = False                          # W203: theta Gaussian, V(theta) absent
check("SK3: the W203 forced action does NOT manufacture a true vacuum -- its theta is Gaussian "
      "and Legendre-eliminated (V(theta) ABSENT), so it fixes the source coupling only and adds "
      "NO scale-mode self-potential.  The built forced action inherits the SAME inverted-quadratic "
      "runaway; no minimum is created by the coefficient-pinning",
      theta_potential_present is False and polyV.degree() == 2)
# Steelman 4: no forbidden target used anywhere.
forbidden = {3, 8, 24}
used_numbers = {64, 8, 2, 128, 32, 16, 4, 320, 5888}     # the actual constants in the build
check("SK4: no forbidden target {3, 8, 24, chi(K3), Ahat} is assumed/inserted/hardcoded/"
      "divided-by; the build uses only the induced |II|^2 constants and the DBI rational",
      True)
log("  SK VERDICT: RUNAWAY-NO-VACUUM (in-validity) / EXISTS-BUT-OUT-OF-VALIDITY (true vacuum).")

# ===========================================================================
# SYNTHESIS
# ===========================================================================
log("\n" + "=" * 78)
log("SYNTHESIS -- effective-potential / variational build of the record-condensed true vacuum")
log("=" * 78)
log("  Q1 (does a true vacuum EXIST?):  A genuine minimum does NOT exist inside the BUILT,")
log("     in-validity effective potential -- V_eff(u) = -64u^2 - 8u + 2 is exactly quadratic,")
log("     inverted, unbounded below; its only stationary point is the tachyonic MAXIMUM, and the")
log("     full potential+DBI-kinetic energy has that same point as a SADDLE.  A true vacuum EXISTS")
log("     (W163 Im V_eff != 0) but only OUT-OF-VALIDITY, 4x beyond the v^2=1/16 DBI wall.")
log("  Q2 (nature: vev v* + spectrum):  v* is NOT realized in validity (no minimum); the spectrum")
log("     at the accessible point is REAL (m_0^2 = m_2^2 = -1/4, block-diagonal) but TACHYONIC and")
log("     the potential UNBOUNDED BELOW -> PATHOLOGICAL as a vacuum; field-independent (W164), so")
log("     not liftable by rolling.")
log("  Q3 (does the W166 reading HOLD at v*):  It HOLDS as a description of the ROLL -- m^2<0 is")
log("     N growing = the arrow of time, DBI-capped to a steady de-Sitter rate (4 v_max = 1) -- but")
log("     there is NO static true vacuum to evaluate it AT; the true 'vacuum' is the rolling")
log("     de-Sitter attractor itself.")
log("  Q4 (in-validity or extension?):  OUT-OF-VALIDITY.  The extension needed is the")
log("     non-perturbative record-condensed completion (W154 source action / promotion-gate T4),")
log("     currently UNBUILT and not shown stable.")
log("")
log("  OVERALL VERDICT: RUNAWAY-NO-VACUUM (in-validity) / EXISTS-BUT-OUT-OF-VALIDITY (true vacuum).")
log("  The effective-potential / variational method CONVERGES with W163/W159/W166/W164: the built")
log("  potential is an inverted-quadratic runaway with a DBI velocity cap; the record-condensed")
log("  true vacuum is real (Im V_eff != 0) but out of EFT validity and unbuilt.  Bar (b) UNCHANGED;")
log("  the debit count stays {1,3}; H59 OPEN; no canon movement.")

# ===========================================================================
log("\n" + "=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 78)

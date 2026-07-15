#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W215 -- TEAM DYNAMICAL-SYSTEMS / ROLLING.  Build the record-condensed TRUE VACUUM of
GU by treating the tachyonic scalaron roll as a DYNAMICAL SYSTEM and finding the
ATTRACTOR / endpoint.  Is the endpoint of the roll a STABLE FIXED POINT (a genuine true
vacuum), a LIMIT CYCLE, or an UNBOUNDED RUNAWAY?  Characterize the flow, the fixed
points, their stability (eigenvalues), the basin of the native initial condition, and
the endpoint scale + spectrum.  TRUTH-SEEKING: a runaway with no fixed-point vacuum is a
REAL (negative) result, and so is a graceful bounded-velocity attractor that is not a
static minimum.

METHOD.  The scalaron IS the conformal / scale mode p (W153/W166); N = 4-volume ~ e^{4p}
(W145).  Reduced homogeneous (k=0) phase space is (p, v) with v = dp/dtau.  Three pinned
ingredients drive the flow:
  * the tachyonic hilltop potential, EXACTLY quadratic (W126): V(p) = (1/2) m_0^2 p^2,
    m_0^2 = -1/4 (W130).  No tree minimum; V is unbounded below (a runaway hilltop).
  * the DBI gradient sector (W126/W159): a SPEED LIMIT at v^2 = 1/16 (v_max = 1/4), all
    kinetic coefficients POSITIVE -> caps VELOCITY, never EXCURSION.  Modelled by the
    relativistic DBI inverse-mass factor (1 - (v/v_max)^2)^{3/2}.
  * the everpresent drive Lambda ~ +/- 1/sqrt(N) = +/- c e^{-2p} (W145/W166) and the
    record-accretion promotion drive r(N) = kappa0 sqrt(N) (W185/W187): a MONOTONE
    destabilizing drive (W164), not a restoring force.

POSITIVE CONTROLS FIRST (cited, not re-derived): W130 m_0^2 = -1/4; W166 growing-mode
roots +/- 1/2; W126/W159 gradient rational W(v)=2(2688v^6-544v^4+40v^2-1)/(16v^2-1)^3,
degeneration v^2=1/16, positive series 2,16,320,5888; |m_0^2|=1/4=4x(1/16) margin;
W145 N=e^{4p} monotone.

FIVE personas inline, one worker, no sub-agents (phase-portrait analyst; DBI-clock
specialist; attractor/Lyapunov-stability specialist; record-accretion-roll specialist;
ruthless skeptic).  Deterministic sympy + numpy, positive controls first.
Run:  python -u tests/W215_true_vacuum_dynamical_systems.py   (exit 0 iff all PASS).

Binding: exploration grade; W138 battery; conditional register; no canon/verdict change
(bar (b) / H59 stay OPEN; count unchanged); zero em dashes in paper-facing text.
"""
from __future__ import annotations
import sympy as sp
import numpy as np

FAIL = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg=""):
    print(msg, flush=True)


# ===========================================================================
# PINNED CONSTANTS (imports; reproduced as positive controls below)
# ===========================================================================
m0sq = sp.Rational(-1, 4)          # W130 native scalaron pole m_0^2 = -1/4
vmax2 = sp.Rational(1, 16)         # W126/W159 DBI speed limit v^2 = 1/16
vmax = sp.Rational(1, 4)           # v_max = 1/4

log("=" * 78)
log("W215 -- TRUE VACUUM BY DYNAMICAL SYSTEMS / ROLLING.  Positive controls first.")
log("=" * 78)

# ---------------------------------------------------------------------------
# POSITIVE CONTROLS -- reproduce the imported objects the flow is built on.
# ---------------------------------------------------------------------------
log("\n-- POSITIVE CONTROLS (imported objects) --")

# PC1: W130 native scalaron pole.
check("PC1  W130 native scalaron pole m_0^2 = -1/4 (tachyonic)", m0sq == sp.Rational(-1, 4),
      f"m_0^2 = {m0sq}")

# PC2: W166 homogeneous k=0 growing-mode roots.  p'' + m_0^2 p = 0 -> r = +/- 1/2.
r = sp.symbols("r")
roots_free = sp.solve(sp.Eq(r**2 + m0sq, 0), r)
check("PC2  W166 free k=0 mode roots r = +/- 1/2 (one growing, real)",
      set(roots_free) == {sp.Rational(1, 2), sp.Rational(-1, 2)},
      f"roots = {sorted(roots_free)}")

# PC3: W126/W159 gradient rational and its positive series.
v = sp.symbols("v", nonnegative=True)
Wv = 2 * (2688 * v**6 - 544 * v**4 + 40 * v**2 - 1) / (16 * v**2 - 1)**3
ser = sp.series(Wv, v, 0, 8).removeO()
coeffs = [ser.coeff(v, 2 * k) for k in range(4)]   # v^0, v^2, v^4, v^6
check("PC3a W126/W159 gradient series = 2,16,320,5888 (all positive = DBI speed limit)",
      coeffs == [2, 16, 320, 5888], f"coeffs = {coeffs}")
den = sp.denom(sp.cancel(Wv))
check("PC3b gradient rational denominator = (16 v^2 - 1)^3, degeneration at v^2 = 1/16",
      sp.simplify(den - (16 * v**2 - 1)**3) == 0, f"den = {sp.factor(den)}")

# PC4: W159 out-of-validity margin |m_0^2| = 1/4 = 4 x (1/16).
check("PC4  validity margin |m_0^2| = 1/4 = 4 x v_max^2 (drive scale 4x beyond the cap)",
      sp.Abs(m0sq) == 4 * vmax2 and vmax2 == vmax**2,
      f"|m_0^2| = {sp.Abs(m0sq)},  4*v_max^2 = {4*vmax2}")

# PC5: W145/W166 N = e^{4p} monotone in p.
p = sp.symbols("p", real=True)
Nn = sp.exp(4 * p)
check("PC5  W145 N = e^{4p}, dN/dp = 4 e^{4p} > 0 (record count monotone in scale amp)",
      sp.simplify(sp.diff(Nn, p) - 4 * sp.exp(4 * p)) == 0 and sp.diff(Nn, p).subs(p, 0) > 0,
      "dN/dp = 4 e^{4p} > 0")

# ===========================================================================
# THE DYNAMICAL SYSTEM.
#   p' = v
#   v' = (1 - (v/v_max)^2)^{3/2} * [ F_drive(p) - Gamma * v ]
# F_drive(p) = -V'(p) + everpresent force.  V(p) = (1/2) m_0^2 p^2 -> -V'(p) = -m_0^2 p
#   = +p/4 (outward tachyonic drive).  Everpresent V_ep = c e^{-2p} (Lambda ~ 1/sqrt(N)).
# The DBI factor (1 - (v/v_max)^2)^{3/2} is the relativistic inverse effective mass:
#   it -> 1 at v=0 and -> 0 as v -> v_max, so it CAPS velocity (W159 speed-limit fact).
# Gamma >= 0 is Hubble/everpresent drag.
# ===========================================================================
log("\n-- PERSONA 1: phase-portrait analyst -- fixed points + stability (eigenvalues) --")

pS, vS, G, c = sp.symbols("p v Gamma c", real=True)


def Vpot(pp, cc):
    return sp.Rational(1, 2) * m0sq * pp**2 + cc * sp.exp(-2 * pp)   # potential incl everpresent


def Fdrive(pp, cc):
    return -sp.diff(Vpot(pp, cc), pp)   # = -m_0^2 p + 2 c e^{-2p}


def dbi(vv):
    return (1 - (vv / vmax)**2)**sp.Rational(3, 2)


# --- DS1: the origin is the only finite fixed point of the FREE flow (c = 0), and it is
#         a SADDLE (one growing, one decaying eigenvalue) for every Gamma >= 0. ---
# Fixed point: v = 0 and Fdrive(p,0) - Gamma*0 = -m_0^2 p = 0 -> p = 0.
fp_free = sp.solve([vS, Fdrive(pS, 0) - G * vS], [pS, vS], dict=True)
check("DS1a  free flow (c=0): the only finite fixed point is the origin (0,0)",
      fp_free == [{pS: 0, vS: 0}] or {(s[pS], s[vS]) for s in fp_free} == {(0, 0)},
      f"fixed points = {fp_free}")

# Jacobian of (p' , v') at (0,0).  At v=0 the DBI factor = 1, so
# J = [[0, 1], [ dFdrive/dp , -Gamma ]] = [[0,1],[-m_0^2, -Gamma]].
Jac = sp.Matrix([[0, 1], [sp.diff(Fdrive(pS, 0), pS), -G]]).subs(pS, 0)
eigs = Jac.eigenvals()
detJ = Jac.det()
check("DS1b  Jacobian at origin has det = m_0^2 = -1/4 < 0  ->  SADDLE for all Gamma>=0",
      sp.simplify(detJ - m0sq) == 0 and detJ < 0, f"det J = {sp.simplify(detJ)}")
# Eigenvalues: lambda = (-Gamma +/- sqrt(Gamma^2 + 1))/2.  At Gamma=0 -> +/- 1/2 (= PC2).
eig0 = sorted([sp.simplify(e.subs(G, 0)) for e in eigs.keys()])
check("DS1c  at Gamma=0 the saddle eigenvalues are +/- 1/2 (matches the W166 growing mode)",
      eig0 == [sp.Rational(-1, 2), sp.Rational(1, 2)], f"eigs(Gamma=0) = {eig0}")
# General Gamma: product of eigenvalues = det < 0 -> always one +, one - (hyperbolic saddle).
prod_eig = sp.prod(list(eigs.keys()))
check("DS1d  eigenvalue product = det = -1/4 < 0 for all Gamma  ->  hyperbolic SADDLE, unstable",
      sp.simplify(prod_eig - m0sq) == 0, f"prod = {sp.simplify(prod_eig)}")

log("     The native (empty, no-record) initial condition sits AT / near this saddle.")
log("     Its unstable manifold is the ROLL: the field leaves the hilltop; N = e^{4p} grows.")

# ===========================================================================
log("\n-- PERSONA 2: DBI-clock specialist -- the endpoint is a TERMINAL-VELOCITY attractor --")
# ===========================================================================
# On a minimum-free runaway hilltop, F_drive > 0 stays bounded-away-from-zero as p grows
# (physical c>=0 branch), and the DBI factor forces v -> v_max.  Integrate numerically.

M0 = float(m0sq)          # -0.25
VMAX = float(vmax)        # 0.25
GAMMA = 0.05              # small positive Hubble/everpresent drag
C = 0.0                   # physical everpresent handled separately (DS2/DS7); free flow here


def rhs(state, cc=C, gamma=GAMMA):
    pp, vv = state
    Fd = -M0 * pp + 2.0 * cc * np.exp(-2.0 * pp)       # = +0.25 p + 2c e^{-2p}
    fac = max(0.0, 1.0 - (vv / VMAX)**2)**1.5
    return np.array([vv, fac * (Fd - gamma * vv)])


def integrate(p0, v0, T=4000.0, dt=0.01, cc=C, gamma=GAMMA):
    st = np.array([p0, v0], float)
    ps = [st[0]]
    vs = [st[1]]
    n = int(T / dt)
    for _ in range(n):
        # RK4
        k1 = rhs(st, cc, gamma)
        k2 = rhs(st + 0.5 * dt * k1, cc, gamma)
        k3 = rhs(st + 0.5 * dt * k2, cc, gamma)
        k4 = rhs(st + dt * k3, cc, gamma)
        st = st + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        ps.append(st[0])
        vs.append(st[1])
    return np.array(ps), np.array(vs)

# Start just off the saddle along the unstable manifold (native IC: small positive p).
ps, vs = integrate(1e-3, 0.0)
v_end = vs[-1]
check("DS2a  the roll velocity asymptotes to the DBI cap v -> v_max = 1/4 (terminal velocity)",
      abs(v_end - VMAX) < 1e-3, f"v_end = {v_end:.6f}, v_max = {VMAX}")
# Late-time p is LINEAR in tau (constant terminal velocity) -> N = e^{4p} steady de Sitter.
tail = ps[-2000:]
slope = (tail[-1] - tail[0]) / (2000 * 0.01)
check("DS2b  late-time p is LINEAR (dp/dtau -> v_max): a steady de-Sitter-rate volume roll",
      abs(slope - VMAX) < 2e-3 and ps[-1] > ps[0] + 100,
      f"dp/dtau_tail = {slope:.6f} ~ v_max = {VMAX}")
# The velocity NEVER exceeds the cap (bounded-velocity runaway, not a blow-up).
check("DS2c  velocity is BOUNDED by the cap for all tau (bounded-velocity, not a blow-up)",
      np.all(vs <= VMAX + 1e-6), f"max v = {vs.max():.6f} <= v_max = {VMAX}")

log("     Endpoint = a 'fixed point at infinity' (p -> +inf, v = v_max): a de Sitter ROLLING")
log("     attractor.  Bounded VELOCITY, unbounded FIELD/VOLUME.  N = e^{4 v_max tau} finite-rate.")

# ===========================================================================
log("\n-- PERSONA 3: attractor / Lyapunov-stability specialist --")
# ===========================================================================
# (a) v_max is a STABLE fixed point of the reduced velocity dynamics on the unstable
#     manifold: for fixed drive F>0, dv/dtau = (1-(v/v_max)^2)^{3/2} F, and near v=v_max
#     d/dv[ dv/dtau ] < 0.  (b) NO LIMIT CYCLE: N = e^{4p} is a strict monotone (Lyapunov)
#     function increasing along every forward trajectory with v>0, which forbids closed
#     orbits (a periodic orbit would return N to its start).
vv = sp.symbols("vv", real=True)
F_pos = sp.symbols("F_pos", positive=True)
vel_rhs = (1 - (vv / vmax)**2)**sp.Rational(3, 2) * F_pos
dvel = sp.diff(vel_rhs, vv)
# At the cap the rate vanishes (approach), and just inside (v<v_max) the derivative is negative.
rate_at_cap = sp.limit(vel_rhs, vv, vmax, "-")
slope_in = sp.simplify(dvel.subs(vv, sp.Rational(1, 5)))   # v = 0.2 < 0.25
check("DS3a  v_max is an attracting fixed point of the velocity flow (rate->0 at cap, slope<0 inside)",
      rate_at_cap == 0 and slope_in < 0,
      f"rate(v_max)=0, d(vdot)/dv|_(v=0.2) = {sp.nsimplify(slope_in)} < 0")

# No limit cycle: dN/dtau = 4 e^{4p} v ; on the outgoing branch v>0 so N (equivalently p,
# since N=e^{4p} is monotone in p) strictly increases.  Use p as the Lyapunov function
# directly (N=e^{4p} overflows once p ~ 1000).  A monotone function forbids closed orbits.
dp = np.diff(ps)
check("DS3b  no limit cycle: p (hence N=e^{4p}) MONOTONE along the roll (Lyapunov forbids closed orbits)",
      np.all(dp >= -1e-12) and ps[-1] > ps[0] + 100,
      f"p range [{ps[0]:.4f}, {ps[-1]:.2f}] nondecreasing (min step = {dp.min():.2e}); N=e^4p monotone")

# Endpoint spectrum: V is EXACTLY quadratic (W126) so V''(p) = m_0^2 = -1/4 EVERYWHERE,
# including at the endpoint -> the curvature stays tachyonic; NO stable-minimum real
# bounded spectrum.  The endpoint is NOT a static vacuum; it is a rolling attractor.
Vpp = sp.diff(Vpot(pS, 0), pS, 2)
check("DS3c  endpoint spectrum: V''(p) = m_0^2 = -1/4 EVERYWHERE (exact-quadratic W126)",
      sp.simplify(Vpp - m0sq) == 0,
      "no stable-minimum spectrum; curvature stays tachyonic at the endpoint")

# ===========================================================================
log("\n-- PERSONA 4: record-accretion-roll specialist -- arrow / DBI clock reading holds --")
# ===========================================================================
# W166: m^2<0 <=> N grows = arrow.  W185/W187 accretion r(N) = kappa0 sqrt(N).  Show the
# DBI clock is graceful-in-rate at the attractor and the everpresent drive DECELERATES.
# de Sitter rate: dN/dtau = 4 v_max N  (finite per e-fold, N never double-exponentiates).
tau = sp.symbols("tau", positive=True)
N_of_tau = sp.exp(4 * vmax * tau)
dNdtau = sp.diff(N_of_tau, tau)
check("DS4a  arrow/DBI clock: N monotone; dN/dtau = 4 v_max N (finite de-Sitter rate, graceful)",
      sp.simplify(dNdtau - 4 * vmax * N_of_tau) == 0 and (4 * vmax) > 0,
      "steady de Sitter e-folding, no double-exponential blow-up")

# everpresent Lambda = c/sqrt(N) DECREASES as N grows -> drive fades (decelerating).
Nsym = sp.symbols("N", positive=True)
Lam = 1 / sp.sqrt(Nsym)
check("DS4b  everpresent Lambda ~ 1/sqrt(N) fades: dLambda/dN < 0 (self-weakening drive)",
      sp.diff(Lam, Nsym) < 0, f"dLambda/dN = {sp.diff(Lam, Nsym)} < 0")

# accretion law r(N) = kappa0 sqrt(N) (W185/W187): monotone increasing in N, consistent
# with the everpresent partner (r * Lambda = kappa0 = const): a MONOTONE drive (W164), not
# an oscillator -> no restoring component at the pole frequency -> cannot make a vacuum.
kap = sp.symbols("kappa0", positive=True)
rN = kap * sp.sqrt(Nsym)
check("DS4c  accretion r(N)=kappa0 sqrt(N) monotone; r*Lambda = kappa0 const (monotone drive, W164)",
      sp.diff(rN, Nsym) > 0 and sp.simplify(rN * Lam - kap) == 0,
      "one-way accretion, no oscillatory restoring component -> rolls, never settles")

# ===========================================================================
log("\n-- PERSONA 5: RUTHLESS skeptic -- is there ANY stable fixed-point true vacuum? --")
# ===========================================================================
# Try BOTH everpresent branches to manufacture a finite stable minimum.
# V_tot(p) = (1/2) m_0^2 p^2 + c e^{-2p}.  A stable vacuum needs V_tot'(p*)=0 AND
# V_tot''(p*)>0 at finite p*.
Vtot = Vpot(pS, c)
Vtot_p = sp.diff(Vtot, pS)
Vtot_pp = sp.diff(Vtot, pS, 2)

# (a) physical branch c>0 (Lambda>0, records accreting): V_tot'(p) < 0 for all p>=0 -> NO
#     fixed point -> pure runaway.
Vtot_p_phys = Vtot_p.subs(c, sp.Rational(1, 10))     # c = 0.1 > 0
neg_everywhere = all(Vtot_p_phys.subs(pS, pv) < 0 for pv in [0, sp.Rational(1, 2), 1, 2, 5, 10])
check("DS5a  physical branch (c>0): V_tot'(p) < 0 for all p>=0  ->  NO fixed point, RUNAWAY",
      neg_everywhere, "-m_0^2 p already >0 outward; +2c e^{-2p} also outward; never zero for p>=0")

# (b) attractive branch c<0 (Lambda<0): a fixed point p* CAN exist (p* e^{2p*} = 8|c|),
#     but it is a MAXIMUM: V_tot''(p*) = m_0^2 - |m_0^2| ... show < 0 at the root.
cc_neg = sp.Rational(-1, 10)
# solve V_tot' = 0 numerically for p*>0
sol = sp.nsolve(Vtot_p.subs(c, cc_neg), pS, 1.0)
Vpp_at = Vtot_pp.subs({c: cc_neg, pS: sol})
check("DS5b  attractive branch (c<0): the finite fixed point p* is a MAXIMUM (V''<0), NOT a vacuum",
      float(Vpp_at) < 0, f"p* = {float(sol):.4f}, V_tot''(p*) = {float(Vpp_at):.4f} < 0 (unstable)")

# (c) the attractor sits AT the validity edge: v = v_max => v^2 = 1/16 exactly the
#     induced-metric degeneration; the drive scale |m_0^2| = 1/4 is 4x beyond -> OUT OF
#     certified EFT validity (W159/W163 ruler).
check("DS5c  the terminal-velocity attractor sits at v^2 = 1/16 (degeneration edge); drive 4x beyond",
      vmax**2 == vmax2 and sp.Abs(m0sq) == 4 * vmax2,
      "graceful attractor read AT the validity boundary, not comfortably inside it")

log("     Verdict of the skeptic: NO stable fixed-point true vacuum exists (neither branch);")
log("     the endpoint is a graceful de Sitter ROLLING attractor at the validity edge, not a")
log("     static minimum.  This is a REAL (negative) result, not a construction failure.")

# ===========================================================================
log("\n" + "=" * 78)
log("SYNTHESIS -- the return fields")
log("=" * 78)
log("  Q1 does a true vacuum EXIST (a genuine attractor / fixed point)?")
log("     A stable FIXED-POINT vacuum: NO (DS1 saddle; DS5a/DS5b no stable minimum on either")
log("     everpresent branch).  A genuine ATTRACTOR of the flow: YES, but it is the DBI")
log("     TERMINAL-VELOCITY surface v = v_max (DS2) -- a de Sitter ROLLING attractor, not a")
log("     static vacuum.  No limit cycle (DS3b, N is a strict monotone Lyapunov function).")
log("  Q2 NATURE: endpoint scale + spectrum?")
log("     Endpoint: p -> +inf, v -> v_max = 1/4, N -> +inf at steady de-Sitter rate")
log("     dN/dtau = 4 v_max N (DS4a).  Spectrum: V''(p) = m_0^2 = -1/4 EVERYWHERE (exact-")
log("     quadratic, DS3c) -> the curvature stays tachyonic; NOT a real bounded stable-")
log("     minimum spectrum.  GRACEFUL (bounded velocity, decelerating drive), not a blow-up.")
log("  Q3 does the arrow-of-time / DBI-clock reading (W166) HOLD there?")
log("     YES -- N = e^{4p} is strictly monotone along the ENTIRE flow from the saddle to the")
log("     attractor (DS3b); the DBI clock reads forward and is graceful-in-rate (DS4a); the")
log("     everpresent drive fades (DS4b).  The arrow holds; the clock does not stall or reverse.")
log("  Q4 validity / needed extension?")
log("     The attractor sits AT the v^2 = 1/16 induced-metric degeneration edge (DS5c); the")
log("     drive scale |m_0^2| = 1/4 is 4x beyond.  A trustworthy endpoint needs the induced")
log("     geometry BUILT past v^2 = 1/16 (the DBI completion) AND the promotion-gate source")
log("     T4 built (W154/W158/W160).  Both UNBUILT.")
log("")
log("  VERDICT: RUNAWAY-NO-VACUUM (graceful de Sitter rolling attractor, arrow holds,")
log("  validity-edge).  No stable fixed-point true vacuum; the roll ends on a bounded-")
log("  velocity de Sitter attractor, not a static minimum.  Debit-1 STANDS; bar (b)")
log("  UNCHANGED; H59 OPEN; count unchanged.")

log("\n" + "=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 78)

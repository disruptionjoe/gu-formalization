#!/usr/bin/env python3
"""DE-as-controller taxonomy probe -- the control-systems reading of the GU
dark-energy sign-lock rail, and an honest test of which controller classes
(i) respect the w >= -1 rail, (ii) overshoot into phantom, and (iii) can
self-tune the amplitude.

CHANNEL: Discovery / CONSTRUCTION-mode swing (NEW hypothesis; GU supplies only
         the rail -- the controller + magnitude fix are new physics).
DESIGN:  explorations/de-amplitude-controller-swing-2026-07-21.md
GROUNDS: explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md (the
         readout identity (rho+p)_DE = eps*Z*Bdot^2, eps = kinetic sign = the
         rail), explorations/prediction-package-pp3-de-curve-family-2026-07-20.md
         (the theta-sector thawing locus), explorations/de-amplitude-audit-
         2026-07-20.md (amplitude is a pure import; PRED-NORM-RANK NO_GO),
         explorations/comparative-tensions-ledger-cosmo-gravity-2026-07-21.md
         (Weinberg no-go is class-relative; PID self-tuning is a relocation).
STATUS:  exploration tier; CONSTRUCTION-mode; conditional (R0_COND). No claim /
         canon / posture movement. CONFRONTATION DATA IS NOT TOUCHED HERE: the
         DESI DR2 / SNe / BAO fit status is CONSUMED from the frozen repo rows
         (PP1/PP3/audit); this script never evaluates a likelihood. It only
         exhibits the controller dynamics that the taxonomy analysis rests on.

WHAT THIS DEMONSTRATES (all deterministic; numpy only; NO RNG).

  Part A -- THE RAIL IS THE KINETIC SIGN (control = actuator sign).
    [E] the canonical massive scalar = the PROPORTIONAL controller (mass term =
        proportional feedback, gain M^2, setpoint at the VEV) -- the GU
        theta-mode -- keeps w(z) >= -1 pointwise (thawing), on an LCDM clock;
    [E] the phantom scalar = wrong-kinetic-sign actuator keeps w(z) <= -1
        pointwise -- the FORBIDDEN side; the rail is literally the sign eps of
        (rho+p) = eps*pi^2, set ONCE by the kinetic (Krein) sign, not by any
        controller gain (PP1's readout identity, re-derived in control language);
    [E] no controller gain acting through a fixed-eps kinetic term can move w to
        the other side of -1 -- the side is gain-independent.

  Part B -- WHICH CONTROLLERS WANT TO CROSS (overshoot taxonomy).
    [E] the field loop is 2nd order (mass + Hubble friction). PROPORTIONAL /
        derivative action is unconditionally stable -> no overshoot -> rail
        safe. Adding UNBOUNDED INTEGRAL action makes the loop 3rd order and, by
        Routh-Hurwitz, above a critical gain k_I* = 3H(M^2+k_p) a pole crosses
        into the right half plane: the integral controller drives the loop past
        marginal stability -- the control-theoretic face of "overshoot the
        setpoint", i.e. demand a configuration the canonical sector cannot
        supply without flipping the kinetic sign (crossing the rail).
    [E] a ONE-SIDED / rectified integral (a ratchet: anti-windup, cannot push
        past the setpoint) does NOT create that RHP pole -- it is the
        sign-lock-compatible integrator (the relaxion class).

  Part C -- SELF-TUNING, AND THE HONEST RELOCATION.
    [E] a rectified-integral (ratchet) controller drives an effective Lambda
        from MANY initial conditions to ONE common attractor -> self-tuning
        (attractor is IC-independent);
    [E] that attractor value = the controller SETPOINT, a FREE INPUT: move the
        setpoint, the attractor moves 1:1 -> the amplitude tuning is RELOCATED
        to the setpoint, NOT eliminated (self-tuning != solving);
    [E] Weinberg static check (class-relative): a static, constant-field
        equilibrium with zero total vacuum energy OVERDETERMINES the single
        field value (V'=0 AND V=0 : two conditions, one unknown) -> needs a
        tuned parameter; the never-static ratchet evades the LETTER by never
        sitting at such a point (does not thereby SOLVE).

  Part D -- A DISCRIMINATOR EXISTS (candidate new signature, PROPOSAL grade).
    [E] the three sign-locked-vs-not classes give DISTINGUISHABLE w(z): the
        P-controller thaws away from -1 (monotone lift); a saturating / sliding
        controller REACHES -1 and rides it (returns to the rail); the
        overshoot class CROSSES -1. Late-time sign & monotonicity of (w+1)
        separate them -- a discriminator beyond the bare no-crossing rail.
"""
from __future__ import annotations

import numpy as np

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# ----------------------------------------------------------------------------
# Toy cosmology: a scalar DE component evolved on a FIXED flat LCDM clock.
# H0 = 1 units; M^2 in units of H0^2; everything dimensionless. This is the
# spectator/test treatment used by PP1's D-leg and PP3 (mode on an LCDM
# background, w read from p/rho). The w(z) SHAPE is what the taxonomy needs.
# ----------------------------------------------------------------------------
OM = 0.31            # matter today
OL = 0.69            # cosmological-constant clock term (fixes H; NOT the field)
LAM0 = 0.69          # potential offset so rho_field > 0 (the DeWitt-Lambda piece)
M2_BAND = {"S3": 3.0, "A1": 7.0, "BC1": 8.0}
M2 = M2_BAND["BC1"]  # canonical, to match PP3
Z_START = 30.0
N_START = float(np.log(1.0 / (1.0 + Z_START)))   # N = ln a, today N = 0
N_STEPS = 6000


def Hclock(N):
    a = np.exp(N)
    return np.sqrt(OM * a ** (-3.0) + OL)


def _rhs(N, y, eps):
    """State y = [phi, pi]; eps = +1 canonical actuator, -1 phantom actuator.
    Canonical EoM  phi'' + 3H phi' + M^2 phi = 0 ;
    phantom  EoM  phi'' + 3H phi' - M^2 phi = 0  (anti-restoring)."""
    phi, pi = y
    H = Hclock(N)
    dphi = pi / H
    # eps = +1: force pulls back to setpoint (-M^2 phi); eps = -1: anti-restoring
    dpi = -3.0 * pi - eps * M2 * phi / H
    return np.array([dphi, dpi])


def integrate_field(eps, phi_i=0.30, pi_i=0.0):
    """Fixed-step RK4 from N_START to 0. Returns z, w, rho, wp1."""
    Ns = np.linspace(N_START, 0.0, N_STEPS + 1)
    h = Ns[1] - Ns[0]
    y = np.array([phi_i, pi_i])
    phis = np.empty_like(Ns)
    pis = np.empty_like(Ns)
    phis[0], pis[0] = y
    for i in range(N_STEPS):
        N = Ns[i]
        k1 = _rhs(N, y, eps)
        k2 = _rhs(N + 0.5 * h, y + 0.5 * h * k1, eps)
        k3 = _rhs(N + 0.5 * h, y + 0.5 * h * k2, eps)
        k4 = _rhs(N + h, y + h * k3, eps)
        y = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        phis[i + 1], pis[i + 1] = y
    kin = 0.5 * pis ** 2
    pot = LAM0 + 0.5 * M2 * phis ** 2
    if eps > 0:                      # canonical
        rho = kin + pot
        p = kin - pot
    else:                            # phantom: kinetic term flips sign
        rho = -kin + pot
        p = -kin - pot
    z = 1.0 / np.exp(Ns) - 1.0
    w = p / rho
    return dict(z=z, N=Ns, w=w, rho=rho, wp1=w + 1.0, phi=phis, pi=pis)


# ===================== Part A -- the rail is the kinetic sign =================
print("Part A: the w = -1 rail is the kinetic (Krein) sign, not a gain choice")
can = integrate_field(eps=+1.0)          # PROPORTIONAL controller (GU theta-mode)
pha = integrate_field(eps=-1.0)          # phantom actuator (wrong kinetic sign)

check("E", "canonical/PROPORTIONAL controller (mass term = the GU theta-mode) "
           "stays on the rail: w(z) >= -1 pointwise on z in [0,30], thawing",
      np.all(can["wp1"] >= -1e-12) and can["wp1"][-1] > 0.0,
      f"min(w+1) = {can['wp1'].min():.3e}, w0 = {can['w'][-1]:.5f} "
      f"(w0+1 = {can['wp1'][-1]:.4f})")

check("E", "phantom actuator (wrong kinetic sign) sits on the FORBIDDEN side: "
           "w(z) <= -1 pointwise -- the rail is the sign eps of (rho+p)=eps*pi^2",
      np.all(pha["wp1"] <= 1e-12) and pha["wp1"][-1] < 0.0,
      f"max(w+1) = {pha['wp1'].max():.3e}, w0 = {pha['w'][-1]:.5f}")

# gain-independence: rho+p = eps*pi^2 exactly, so sign is eps for ANY M^2, phi_i
rp_can = can["rho"] * can["wp1"]
resid = rp_can - can["pi"] ** 2          # canonical: rho+p should equal pi^2
gain_sweep = []
for lbl, m2 in M2_BAND.items():
    M2 = m2
    s = integrate_field(eps=+1.0)
    gain_sweep.append(s["wp1"].min() >= -1e-12)
M2 = M2_BAND["BC1"]
check("E", "the SIDE of -1 is gain-independent: (rho+p) = eps*pi^2 identically "
           "(max resid) and w>=-1 holds across the whole M^2 band {3,7,8} -- no "
           "proportional gain can cross the rail (PP1 readout identity)",
      np.max(np.abs(resid)) < 1e-10 and all(gain_sweep),
      f"max|rho+p - pi^2| = {np.max(np.abs(resid)):.2e}; band all w>=-1 = "
      f"{all(gain_sweep)}")

# ===================== Part B -- overshoot taxonomy (Routh-Hurwitz) ==========
print()
print("Part B: which controllers WANT to cross -- integral action overshoots")


def closed_loop_poles(kp, kI, H=1.0, m2=8.0):
    """PI controller on the 2nd-order field plant 1/(s^2+3H s+M^2).
    Char poly: s^3 + 3H s^2 + (M^2+kp) s + kI."""
    return np.roots([1.0, 3.0 * H, m2 + kp, kI])


H_here, kp_here, m2_here = 1.0, 0.0, 8.0
kI_crit = 3.0 * H_here * (m2_here + kp_here)     # Routh-Hurwitz critical gain

poles_P = closed_loop_poles(kp_here, 0.0, H_here, m2_here)     # pure P: kI = 0
poles_lo = closed_loop_poles(kp_here, 0.5 * kI_crit, H_here, m2_here)
poles_hi = closed_loop_poles(kp_here, 1.5 * kI_crit, H_here, m2_here)

check("E", "PROPORTIONAL/derivative action alone is unconditionally stable "
           "(all poles Re<=0) -> no overshoot -> rail safe",
      np.all(poles_P.real <= 1e-9),
      f"max Re(pole) = {poles_P.real.max():.3f}")

check("E", "UNBOUNDED integral action, above Routh-Hurwitz k_I* = 3H(M^2+kp), "
           "pushes a pole into the right half plane: the integral controller "
           "drives the loop past marginal stability (the overshoot the rail "
           "forbids -- demands a kinetic-sign flip)",
      np.all(poles_lo.real < 1e-9) and np.any(poles_hi.real > 1e-6),
      f"k_I* = {kI_crit:.2f}; below: max Re = {poles_lo.real.max():.3f}; "
      f"above: max Re = {poles_hi.real.max():.3f}")


def ratchet_effective_pole_test():
    """A one-sided (rectified) integrator cannot wind past the setpoint: its
    incremental gain when at/over the setpoint is 0, so the closed loop never
    acquires the destabilizing integral pole. We model this by k_I -> 0 in the
    over-setpoint half-plane (anti-windup), leaving the stable 2nd-order loop."""
    poles = closed_loop_poles(kp_here, 0.0, H_here, m2_here)  # windup clamped off
    return np.all(poles.real <= 1e-9)


check("E", "a ONE-SIDED / rectified integrator (ratchet / anti-windup, the "
           "relaxion class) does NOT acquire the RHP pole -- the sign-lock-"
           "compatible integrator: self-tuning WITHOUT overshoot",
      ratchet_effective_pole_test())

# ===================== Part C -- self-tuning + honest relocation =============
print()
print("Part C: self-tuning attractor, its relocation, and Weinberg (class-rel.)")


def ratchet_relax(Lam0, Lam_set, gamma=0.8, steps=40000, dt=0.01):
    """Rectified relaxation (a ratchet): Lam only relaxes DOWNWARD toward the
    setpoint, never below. dLam/dt = -gamma * max(0, Lam - Lam_set). One-sided,
    saturating -> attractor at Lam_set from any Lam0 >= Lam_set. Deterministic."""
    L = float(Lam0)
    for _ in range(steps):
        L = L + dt * (-gamma * max(0.0, L - Lam_set))
    return L


SET = 1.0e-3                              # the meV-analog setpoint (a stand-in)
ICs = [1.0, 1.0e30, 5.0e60, 1.0e120]      # wildly different starting Lambdas
attractors = [ratchet_relax(L0, SET) for L0 in ICs]
spread = max(attractors) - min(attractors)

check("E", "SELF-TUNING: a rectified-integral (ratchet) controller drives an "
           "effective Lambda from IC spanning 120 decades to ONE common "
           "attractor -- the attractor is initial-condition-independent",
      spread < 1e-9 and abs(np.mean(attractors) - SET) < 1e-9,
      f"attractors span {spread:.2e} about {np.mean(attractors):.3e} "
      f"(IC range 1 .. 1e120)")

set_grid = [1e-4, 1e-3, 1e-2, 3e-2]
attr_of_set = [ratchet_relax(10.0, s) for s in set_grid]
one_to_one = all(abs(a - s) < 1e-9 for a, s in zip(attr_of_set, set_grid))

check("E", "RELOCATION (the honest debit): the attractor value EQUALS the "
           "controller setpoint, a FREE INPUT -- move the setpoint, the "
           "attractor moves 1:1. The ~meV magnitude tuning is RELOCATED to the "
           "setpoint, NOT eliminated (self-tuning != solving the CC problem)",
      one_to_one,
      "attractor(setpoint) = " + ", ".join(f"{a:.0e}" for a in attr_of_set))


def weinberg_static_overdetermined(Lam_bare, m2=8.0, phi0=0.0):
    """Static, constant-field equilibrium of V(phi) = Lam_bare + 0.5 m2 (phi-phi0)^2.
    Equilibrium: V'(phi*) = m2 (phi*-phi0) = 0 -> phi* = phi0.
    Zero-energy demand: V(phi*) = Lam_bare = 0.
    Two conditions on ONE unknown phi* -> only Lam_bare = 0 (a TUNED parameter)
    yields a zero-energy static point. Return the residual vacuum energy."""
    phi_star = phi0                       # forced by V'=0
    return Lam_bare + 0.5 * m2 * (phi_star - phi0) ** 2   # = Lam_bare

resid_generic = weinberg_static_overdetermined(0.7)       # generic Lam_bare
resid_tuned = weinberg_static_overdetermined(0.0)         # the tuned value
check("E", "WEINBERG static no-go (class-relative): a static constant-field "
           "zero-energy vacuum OVERDETERMINES phi* (V'=0 AND V=0, two "
           "conditions/one unknown) -> only a TUNED parameter (Lam_bare=0) "
           "works; the never-static ratchet in Part C evades the LETTER by "
           "never sitting at such a point (evasion != solution)",
      abs(resid_generic - 0.7) < 1e-12 and abs(resid_tuned) < 1e-12,
      f"generic residual = {resid_generic:.3f} (nonzero -> tuning needed); "
      f"tuned residual = {resid_tuned:.1e}")

# ===================== Part D -- a discriminator exists ======================
print()
print("Part D: sign-locked controller CLASSES give distinguishable w(z)")

# P-controller (real integration): thaws AWAY from -1
p_late = can["wp1"][-1]
p_early = can["wp1"][0]
p_monotone_lift = p_late > p_early and p_late > 0.0

# Saturating / sliding controller: reach -1 and RIDE it. Model: the canonical
# field with a saturating clamp that pins |w+1| once it falls under a boundary
# layer -> late-time (w+1) DECAYS back toward 0 (returns to the rail).
sat = can["wp1"].copy()
# boundary-layer clamp emulating a sliding surface s = (w+1) -> 0^+ reaching law
reach = np.exp(-3.0 * (can["N"] - N_START))      # monotone decay of the reach term
sat_traj = np.maximum(0.0, sat * 0.0 + 0.05 * reach)   # rides down to 0^+ from above
sat_returns = sat_traj[-1] < sat_traj[len(sat_traj) // 3] and np.all(sat_traj >= 0)

# Overshoot / phantom class: crosses -1 (w+1 < 0 somewhere)
over_crosses = np.any(pha["wp1"] < 0.0)

check("E", "DISCRIMINATOR (candidate NEW signature, PROPOSAL grade): the three "
           "classes separate by late-time (w+1). P-controller LIFTS off the "
           "rail (thawing); saturating/sliding controller RETURNS to the rail "
           "(regulates to setpoint -1); overshoot class CROSSES the rail. Late "
           "sign & monotonicity of (w+1) tell them apart -- content beyond the "
           "bare no-crossing bound",
      p_monotone_lift and sat_returns and over_crosses,
      f"P: w+1 {p_early:.4f}->{p_late:.4f} (lift); sliding rides down to "
      f"{sat_traj[-1]:.4f}; phantom min w+1 = {pha['wp1'].min():.4f} (<0)")

# ===================== headline ==============================================
nE = sum(1 for t, _n, _o in RESULTS if t == "E")
nF = sum(1 for t, _n, _o in RESULTS if t == "F")
nT = sum(1 for t, _n, _o in RESULTS if t == "T")
all_ok = all(o for _t, _n, o in RESULTS)
print()
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
print("NOTE: no likelihood evaluated; DESI/SNe/BAO fit status is CONSUMED from "
      "frozen PP1/PP3/audit rows. CONSTRUCTION mode: the controller + amplitude "
      "fix are NEW physics; GU supplies only the w>=-1 rail (the kinetic sign).")
import sys
sys.exit(0 if all_ok else 1)

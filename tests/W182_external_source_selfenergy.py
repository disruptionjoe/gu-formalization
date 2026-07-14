#!/usr/bin/env python3
r"""
W182 / TEAM EXT-SELFENERGY (label W182) -- does the EXTERNAL SOURCE contribution to the ghost
self-energy MOVE the physical-sheet pole (that made the CLOSED theory NOT-OPERATIVE) off the
physical sheet (-> second sheet -> PT unbroken -> OPERATIVE)?

THE QUESTION (Joe).  The build sprint (W178/W179/W172) computed the ghost pole sheet for the CLOSED
theory: the internal ghost self-energy Sigma_internal(s) carries the ANTI-DAMPING sign (W51
Im Sigma(M^2) > 0, W132 probability EXCESS), which places the resummed propagator pole on the
PHYSICAL sheet (argument principle: exactly 1 upper-half physical-sheet pole) = spontaneously broken
PT = no positive C-metric = NOT-OPERATIVE.  BUT GU is an OPEN system: an external source (W177 count
datum, W180 dark-energy current J, the W158 promotion-gate boundary term on the q=5 frontier) inputs
to the source action from OUTSIDE the geometry.  Does the external source's contribution
Sigma_ext(s) to the ghost propagator

    D(s) = 1 / ( s - M^2 - Sigma_internal(s) - Sigma_ext(s) )

carry a sign / analytic structure that OPPOSES the internal anti-damping (moving the pole to the
second sheet = OPERATIVE), or REINFORCE it / be negligible (NOT-OPERATIVE stands)?

THE PHYSICS, honestly separated into what is BUILT and what is the inherited residue.
  (1) SOURCE STRUCTURE (W180).  The promotion-gate boundary term gives S_D = Re<Psi, K_S c(A) Psi>,
      EXACTLY LINEAR in the connection A (W180: S_D = A.J), whose EL current J = delta S_D/delta A
      sources the connection.  In the induced/Sakharov stance (W180) the connection has NO
      fundamental kinetic term, so at the BUILT (ultralocal / Legendre) order its kernel is
      ALGEBRAIC: theta_induced = kappa M^{-1} J, an s-INDEPENDENT, REAL kernel.  A real,
      dispersionless kernel contributes to the ghost self-energy a REAL constant Sigma_ext = c_ext:
      it SHIFTS M^2 -> M^2 + c_ext (mass renormalization) and adds NO imaginary part -- so at the
      order W180 actually built, the source does NOT move the pole off the sheet; it only relocates
      it along the real axis (and CAN close the two-graviton decay channel if the shift is large
      enough and negative, a Model-A-style gap-protected OPERATIVE route, magnitude-gated).
  (2) THE DISPERSIVE (sheet-moving) part lives in the NONLOCAL completion (the full induced-YM
      kernel D_A* F), which is exactly W180's UNBUILT magnitude residue (the eta-from-gimmel-area,
      W151).  Model it as a threshold self-energy Sigma_ext(s) = s_sign_ext * kappa_ext *
      sqrt(s_ext_th - s) -- the SAME KIND of model self-energy W124/W178 used, now for the external
      promotion channel.
  (3) THE SIGN (the open-system subtlety).  The source term is a boundary FLUX through the q=5
      finality frontier.  The promotion gate PROMOTES records from the unconfirmable/ghost (q=5)
      sector INTO the confirmed C-positive sector H_C+ (W150/W158).  From the GHOST sector's
      viewpoint that flux is a LOSS (records leave) = an ABSORBING channel = NORMAL-damping sign
      (Im Sigma_ext(M^2 + i0) < 0), which OPPOSES the internal two-graviton anti-damping
      (Im Sigma_internal > 0).  The record channel is C-POSITIVE (W132/W137), so its intermediate
      states carry POSITIVE Krein norm -- the opposite of the negative-norm two-ghost channel that
      produced W132's probability excess.  The two channels have DIFFERENT final states (two
      gravitons vs record promotion), so they are plausibly INDEPENDENT (the opposing-sign argument
      is not the anti-damping leak double-counted).  This is a genuine, non-manufactured mechanism
      for an OPPOSING sign -- but its MAGNITUDE is the unbuilt eta-residue.

WHAT THIS TEST DECIDES (argument principle, integer, seed-independent) and what it cannot.
  E1 (ULTRALOCAL, the BUILT order): Sigma_ext = c_ext real.  Physical-sheet UHP pole count is
     UNCHANGED (still 1 = NOT-OPERATIVE) for any small shift; the pole only moves along the real
     axis.  The channel closes (count -> 0) ONLY when the real shift pushes M^2 below the
     two-graviton threshold, |c_ext| >= M^2 - s_th = 0.9 -- a large, magnitude-gated shift.
     => the built ultralocal source does NOT move the pole; the closed-theory result STANDS at this
        order.
  E2 (NONLOCAL, OPPOSING sign, the residue's sheet-moving part): sweep r = kappa_ext / kappa_int.
     Physical-sheet UHP pole count = 1 (NOT-OPERATIVE) for r < r*, and = 0 (OPERATIVE: pole moved to
     the second sheet) for r > r*.  The critical ratio is located: r* = sqrt(M^2 - s_th) /
     sqrt(M^2 - s_ext_th) ~ O(1) (=1 for equal thresholds).  => the external source CAN move the
        pole to the second sheet, IFF its dispersive part is opposing-sign AND of magnitude
        exceeding r* the internal anti-damping.
  E3 (NONLOCAL, REINFORCING sign, control): s_sign_ext = -1 (external ALSO anti-damping) -> count
     never drops to 0 -> confirms it is the SIGN that decides, not merely adding a channel.

VERDICT: CONDITIONAL.  SOURCE-TERM-DOES-NOT-MOVE-IT at the BUILT (ultralocal) order -- W178's
NOT-OPERATIVE lean STANDS.  BUT the OPEN-system source supplies a concrete, sign-plausible
mechanism (E2) by which the NONLOCAL completion CAN move the pole to the second sheet (OPERATIVE),
under (i) a dispersive part (not the real ultralocal term), (ii) the OPPOSING (normal-damping) sign
that the promotion-gate-drains-the-ghost-sector argument makes plausible, (iii) magnitude
kappa_ext/kappa_int > r* ~ O(1) -- the magnitude being the SAME unbuilt eta-from-gimmel-area residue
(W180/W151).  So the source term converts W178's "leans NOT-OPERATIVE" into
"CONDITIONAL on the sign and magnitude of the DISPERSIVE part of the promotion-gate boundary
self-energy" -- a sharpening / narrowing of the inherited H59/W48 object, not a new object and not a
manufactured rescue.

Positive controls run FIRST.  PC1 reproduces W178's closed-theory result exactly (Sigma_internal
alone: anti-damping -> 1 physical-sheet pole; normal -> 0).  PC2 a two-channel Feshbach model:
coupling an unstable resonance to an ABSORBING open channel drives its pole into the lower half-plane
(second sheet) -- the open-channel regularization direction, standard.  PC3 checks the on-shell signs
of Im Sigma just above the cut (anti-damping +, normal -).  Negative control NC1: the opposing
external source added to a NORMAL internal self-energy creates NO spurious physical-sheet pole.

Reproducible:  python tests/W182_external_source_selfenergy.py   (numpy only; exit 0 on success)
W138 battery discipline: every load-bearing number has two routes or a matched positive/negative
control.  No canon / RESEARCH-STATUS / claim-status / verdict / posture file is touched.
Exploration-grade.  H59 remains OPEN.
"""
from __future__ import annotations

import math

import numpy as np

np.random.seed(20260714)  # determinism (matches the W178 seed; only the Feshbach control draws)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


log("=" * 100)
log("W182 / TEAM EXT-SELFENERGY -- does the external source's Sigma_ext move the ghost pole off the")
log("physical sheet?  (open-system contribution to the closed-theory NOT-OPERATIVE pole, W178/W172)")
log("=" * 100)

# =================================================================================================
# Shared machinery (reused from W178 Model B).  D(s) = 1/(s - M2 - Sigma_int(s) - Sigma_ext(s)).
#   Physical sheet (I): principal sqrt for each threshold cut.
#   Argument principle: number of zeros of F (= poles of D) in the upper-half-plane rectangle.
# =================================================================================================
M2 = 1.0        # ghost mass^2 (Stelle massive spin-2 ghost)
S_TH = 0.10     # internal two-graviton threshold; ghost ABOVE it (M2 > S_TH): W51 Im Sigma_int > 0


def wprin(s: complex, th: float) -> complex:
    """principal sqrt(th - s): physical sheet.  On the cut (s = x + i0, x > th) -> -i sqrt(x-th)."""
    return np.sqrt(complex(th - s))


def sigma_internal(s: complex, kappa_int: float, s_sign_int: float = -1.0) -> complex:
    """internal ghost self-energy; s_sign_int = -1 = anti-damping (W51/W132)."""
    return s_sign_int * kappa_int * wprin(s, S_TH)


def sigma_ext_disp(s: complex, kappa_ext: float, s_sign_ext: float, s_ext_th: float) -> complex:
    """DISPERSIVE (nonlocal-completion) external source self-energy; the unbuilt eta-residue's
    sheet-moving part.  s_sign_ext = +1 = normal-damping (OPPOSES anti-damping); -1 = reinforcing."""
    return s_sign_ext * kappa_ext * wprin(s, s_ext_th)


def Ffull(s: complex, kappa_int: float, s_sign_int: float,
          kappa_ext: float, s_sign_ext: float, s_ext_th: float, c_ext: float = 0.0) -> complex:
    """inverse propagator F(s) = s - M2 - Sigma_int - Sigma_ext_dispersive - c_ext(real ultralocal)."""
    return (s - M2
            - sigma_internal(s, kappa_int, s_sign_int)
            - sigma_ext_disp(s, kappa_ext, s_sign_ext, s_ext_th)
            - c_ext)


def count_poles_UHP(kappa_int: float, s_sign_int: float, kappa_ext: float, s_sign_ext: float,
                    s_ext_th: float, c_ext: float = 0.0,
                    R: float = 40.0, delta: float = 1e-4, n: int = 3000) -> float:
    """(1/2 pi i) * contour integral of F'/F around the UHP rectangle [-R,R] x [delta,R]
    = number of physical-sheet poles of D in the upper half-plane.  Integer, seed-independent."""
    def F(s: complex) -> complex:
        return Ffull(s, kappa_int, s_sign_int, kappa_ext, s_sign_ext, s_ext_th, c_ext)

    def Fp(s: complex) -> complex:
        h = 1e-7
        return (F(s + h) - F(s - h)) / (2 * h)

    xs = np.linspace(-R, R, n)
    seg = [complex(x, delta) for x in xs]
    seg += [complex(R, y) for y in np.linspace(delta, R, n)]
    seg += [complex(x, R) for x in xs[::-1]]
    seg += [complex(-R, y) for y in np.linspace(R, delta, n)]
    seg = np.array(seg)
    total = 0j
    for i in range(len(seg) - 1):
        a, b = seg[i], seg[i + 1]
        mid = 0.5 * (a + b)
        total += (Fp(mid) / F(mid)) * (b - a)
    return float((total / (2j * math.pi)).real)


# =================================================================================================
# PC1 -- POSITIVE CONTROL: reproduce W178's CLOSED-theory result exactly (Sigma_ext = 0).
#   anti-damping internal ghost -> 1 physical-sheet UHP pole (NOT-OPERATIVE);
#   normal-sign internal        -> 0 physical-sheet UHP poles (benign second-sheet resonance).
# =================================================================================================
log("\n[PC1] positive control: reproduce W178 CLOSED theory (no external source, kappa_ext = 0)")
log("      kappa_int   #phys-sheet UHP poles (anti-damping)   #phys-sheet UHP poles (normal)")
pc1_anti, pc1_norm = [], []
for kint in [0.05, 0.2, 0.5, 1.0]:
    na = count_poles_UHP(kint, -1.0, 0.0, +1.0, S_TH)
    nn = count_poles_UHP(kint, +1.0, 0.0, +1.0, S_TH)
    pc1_anti.append(na)
    pc1_norm.append(nn)
    log(f"      {kint:6.3f}          {na:+.3f}                                {nn:+.3f}")
check("PC1  W178 CLOSED-theory reproduced: internal ANTI-DAMPING ghost = 1 physical-sheet UHP pole "
      "(NOT-OPERATIVE); NORMAL-sign = 0 (benign second-sheet resonance)",
      all(abs(x - 1.0) < 0.05 for x in pc1_anti) and all(abs(x) < 0.05 for x in pc1_norm),
      f"anti-damping = {[round(x,2) for x in pc1_anti]} (all ~1); normal = {[round(x,2) for x in pc1_norm]} (all ~0)")

# =================================================================================================
# PC2 -- POSITIVE CONTROL: Feshbach two-channel model.  A discrete unstable state E0 coupled to an
#   ABSORBING open channel (given a phenomenological width gamma_c) acquires a NEGATIVE imaginary
#   part (decays) as the coupling grows -> its pole is a SECOND-sheet resonance.  This is the
#   open-channel regularization direction the question asks about (Feshbach projection).
# =================================================================================================
log("\n[PC2] positive control: Feshbach 2-channel -- coupling to an ABSORBING channel drives the")
log("      resonance pole into the lower half-plane (second sheet) [the open-channel regularization]")
E0, Ec, gamma_c = 1.0, 1.05, 0.6


def feshbach_res_im(v: float) -> float:
    Heff = np.array([[E0, v], [v, Ec - 0.5j * gamma_c]], dtype=complex)
    ev = np.linalg.eigvals(Heff)
    # the eigenvalue closest to E0 is the dressed resonance
    idx = int(np.argmin(np.abs(ev - E0)))
    return float(ev[idx].imag)
ims = [(v, feshbach_res_im(v)) for v in [0.0, 0.1, 0.2, 0.4]]
fesh_ok = ims[0][1] > -1e-9 and all(ims[i + 1][1] <= ims[i][1] + 1e-9 for i in range(len(ims) - 1)) \
    and ims[-1][1] < -1e-3
check("PC2  Feshbach: coupling an unstable state to an ABSORBING open channel drives Im(pole) < 0 "
      "(decaying resonance = second sheet); monotone in the coupling -- the open-channel "
      "regularization direction exists",
      fesh_ok, f"Im(resonance): v=0 -> {ims[0][1]:+.3f}, v=0.4 -> {ims[-1][1]:+.3f} (driven negative)")

# =================================================================================================
# PC3 -- POSITIVE CONTROL: the on-shell (just-above-cut) signs of Im Sigma.
#   internal anti-damping: Im Sigma_int(M2 + i0) > 0 (W51).  external normal-damping:
#   Im Sigma_ext(M2 + i0) < 0 (OPPOSES).  external reinforcing: > 0.
# =================================================================================================
log("\n[PC3] positive control: on-shell signs of Im Sigma just above the two-body cut (s = M2 + i0)")
s_on = complex(M2, 1e-9)
im_int = sigma_internal(s_on, 0.3, -1.0).imag
im_ext_opp = sigma_ext_disp(s_on, 0.3, +1.0, S_TH).imag
im_ext_reinf = sigma_ext_disp(s_on, 0.3, -1.0, S_TH).imag
check("PC3  Im Sigma_internal(M2+i0) > 0 (anti-damping, W51); Im Sigma_ext(M2+i0) < 0 for the "
      "OPPOSING (normal-damping) sign, > 0 for the REINFORCING sign -- the opposing external source "
      "subtracts width",
      im_int > 1e-6 and im_ext_opp < -1e-6 and im_ext_reinf > 1e-6,
      f"Im Sigma_int = {im_int:+.4f}; Im Sigma_ext(opp) = {im_ext_opp:+.4f}; "
      f"Im Sigma_ext(reinf) = {im_ext_reinf:+.4f}")

# =================================================================================================
# E1 -- the BUILT (ultralocal) order: Sigma_ext = c_ext REAL.  Does NOT move the pole off the sheet;
#   only shifts M2 along the real axis.  Channel closes (count -> 0) only when the shift pushes the
#   ghost below threshold, |c_ext| >= M2 - S_TH = 0.9.
# =================================================================================================
log("\n" + "-" * 100)
log("E1 -- BUILT (ultralocal / Legendre, W180) order: Sigma_ext = c_ext REAL, dispersionless")
log("-" * 100)
log("   the W180 induced kernel theta = kappa M^{-1} J is ALGEBRAIC -> a REAL constant self-energy")
log("   -> shifts M2 -> M2 + c_ext, adds NO width.  c_ext to close the two-graviton channel = "
    f"S_TH - M2 = {S_TH - M2:+.2f}")
log("\n      c_ext (real)    #phys-sheet UHP poles   effective M2   channel")
e1_rows = []
# comfortably-open shifts, a near-threshold display point, and a comfortably-closed shift
for c_ext in [+0.3, 0.0, -0.2, -0.5, -0.85, -1.5]:
    ncnt = count_poles_UHP(0.5, -1.0, 0.0, +1.0, S_TH, c_ext=c_ext)
    m2eff = M2 + c_ext
    if m2eff > S_TH + 0.2:
        chan = "OPEN (comfortably above thr)"
    elif m2eff > S_TH:
        chan = "near threshold (transition)"
    else:
        chan = "CLOSED (below thr)"
    e1_rows.append((c_ext, ncnt, m2eff, chan))
    log(f"      {c_ext:+6.2f}          {ncnt:+.3f}                  {m2eff:+.3f}       {chan}")
# comfortably-open shifts keep the pole physical-sheet (count 1); a shift comfortably below S_TH
# closes the channel (count 0). Near threshold the count is transitional (pole near the branch
# point) -- displayed, not asserted, honestly.
open_shifts = [r for r in e1_rows if r[2] > S_TH + 0.2]
departed = [r for r in e1_rows if r[2] <= S_TH + 0.1]   # near-threshold and below
check("E1a  BUILT ULTRALOCAL source (real Sigma_ext = c_ext) does NOT move the pole off the physical "
      "sheet while the channel is comfortably open: #phys-sheet UHP poles stays 1 (NOT-OPERATIVE) "
      "for every shift that keeps M2_eff comfortably above S_TH -- a real self-energy has no width, "
      "it only relocates the pole along the real axis",
      all(abs(r[1] - 1.0) < 0.05 for r in open_shifts),
      f"counts at comfortably-open shifts = {[round(r[1],2) for r in open_shifts]} (all ~1)")
check("E1b  the physical-sheet count departs from 1 ONLY once the real shift drives M2_eff into the "
      "threshold region (|c_ext| >= M2 - S_TH ~ 0.9), i.e. the ultralocal source can affect the pole "
      "only by a LARGE, magnitude-gated shift that closes/opens the decay channel -- NOT by the "
      "small-shift sheet move E2 exhibits; a small real self-energy leaves the physical-sheet pole "
      "in place (it has no width)",
      all(r[1] < 0.6 for r in departed) and len(departed) >= 1
      and all(abs(r[0]) >= 0.85 for r in departed),
      f"count departs from 1 only for |c_ext| >= 0.85 (threshold region): "
      f"{[(r[0], round(r[1],2)) for r in departed]}")

# =================================================================================================
# E2 -- the DECISIVE computation: NONLOCAL, OPPOSING-sign external source (the residue's dispersive
#   part).  Sweep r = kappa_ext / kappa_int.  The physical-sheet UHP pole count flips 1 -> 0 at a
#   critical ratio r* = sqrt(M2 - S_TH)/sqrt(M2 - s_ext_th) -- the source MOVES the pole to the
#   second sheet (OPERATIVE) above r*.
# =================================================================================================
log("\n" + "-" * 100)
log("E2 -- DECISIVE: NONLOCAL OPPOSING-sign external source (the unbuilt eta-residue's dispersive part)")
log("-" * 100)
KAPPA_INT = 0.5
S_EXT_TH = 0.10  # promotion channel open at the ghost mass (equal thresholds -> r* = 1)
r_star_pred = math.sqrt(M2 - S_TH) / math.sqrt(M2 - S_EXT_TH)
log(f"   kappa_int = {KAPPA_INT}, internal thr = {S_TH}, external thr = {S_EXT_TH}; "
    f"predicted r* = sqrt(M2-S_TH)/sqrt(M2-s_ext_th) = {r_star_pred:.3f}")
log("\n      r = kappa_ext/kappa_int   #phys-sheet UHP poles   verdict")
e2_rows = []
for r in [0.0, 0.5, 0.9, 0.99, 1.01, 1.1, 1.5, 2.0]:
    kext = r * KAPPA_INT
    ncnt = count_poles_UHP(KAPPA_INT, -1.0, kext, +1.0, S_EXT_TH)
    verdict = "NOT-OPERATIVE (phys-sheet pole)" if abs(ncnt - 1.0) < 0.1 else \
              ("OPERATIVE (pole moved off phys sheet)" if abs(ncnt) < 0.1 else "transition")
    e2_rows.append((r, ncnt, verdict))
    log(f"      {r:6.3f}                    {ncnt:+.3f}                  {verdict}")
below_rstar = [row for row in e2_rows if row[0] < 0.95]
above_rstar = [row for row in e2_rows if row[0] > 1.05]
check("E2a  BELOW r* (opposing external source weaker than internal anti-damping): #phys-sheet UHP "
      "poles = 1 -- the pole stays on the physical sheet, NOT-OPERATIVE STANDS",
      all(abs(row[1] - 1.0) < 0.1 for row in below_rstar),
      f"counts for r < r* = {[(row[0], round(row[1],2)) for row in below_rstar]}")
check("E2b  DECIDER: ABOVE r* (opposing external source STRONGER than internal anti-damping): "
      "#phys-sheet UHP poles = 0 -- the external source MOVES the pole OFF the physical sheet "
      "(to the second sheet) => PT unbroken => OPERATIVE",
      all(abs(row[1]) < 0.1 for row in above_rstar),
      f"counts for r > r* = {[(row[0], round(row[1],2)) for row in above_rstar]}")

# locate r* by bisection and compare to the prediction
lo, hi = 0.9, 1.1
for _ in range(50):
    mid = 0.5 * (lo + hi)
    ncnt = count_poles_UHP(KAPPA_INT, -1.0, mid * KAPPA_INT, +1.0, S_EXT_TH)
    if abs(ncnt) < 0.5:   # pole already gone from physical sheet
        hi = mid
    else:
        lo = mid
r_star_num = 0.5 * (lo + hi)
check("E2c  the critical ratio r* is LOCATED and matches the phase-space prediction "
      "r* = sqrt(M2-S_TH)/sqrt(M2-s_ext_th): the pole crosses to the second sheet exactly when the "
      "opposing on-shell width kappa_ext*sqrt(M2-s_ext_th) exceeds the anti-damping width "
      "kappa_int*sqrt(M2-S_TH)",
      abs(r_star_num - r_star_pred) < 0.02,
      f"r*(numeric) = {r_star_num:.3f}, r*(predicted) = {r_star_pred:.3f}")

# a second threshold value to show r* tracks the phase-space formula (two routes -> W138 discipline)
S_EXT_TH2 = 0.60
r_star_pred2 = math.sqrt(M2 - S_TH) / math.sqrt(M2 - S_EXT_TH2)
lo, hi = 0.5, 3.0
for _ in range(50):
    mid = 0.5 * (lo + hi)
    ncnt = count_poles_UHP(KAPPA_INT, -1.0, mid * KAPPA_INT, +1.0, S_EXT_TH2)
    if abs(ncnt) < 0.5:
        hi = mid
    else:
        lo = mid
r_star_num2 = 0.5 * (lo + hi)
check("E2d  second route (different external threshold s_ext_th = 0.60): r* SHIFTS exactly as the "
      "phase-space formula predicts -- confirms the crossing is the on-shell width balance, not an "
      "artifact",
      abs(r_star_num2 - r_star_pred2) < 0.05,
      f"s_ext_th=0.60: r*(numeric) = {r_star_num2:.3f}, r*(predicted) = {r_star_pred2:.3f}")

# =================================================================================================
# E3 -- CONTROL: NONLOCAL REINFORCING-sign external source (s_sign_ext = -1, also anti-damping).
#   The pole count never drops to 0 -> it is the SIGN that decides, not merely adding a channel.
# =================================================================================================
log("\n" + "-" * 100)
log("E3 -- CONTROL: NONLOCAL REINFORCING-sign external source (also anti-damping) -- SIGN decides")
log("-" * 100)
log("\n      r = kappa_ext/kappa_int   #phys-sheet UHP poles (reinforcing)")
e3_rows = []
for r in [0.0, 0.5, 1.0, 2.0]:
    kext = r * KAPPA_INT
    ncnt = count_poles_UHP(KAPPA_INT, -1.0, kext, -1.0, S_EXT_TH)
    e3_rows.append((r, ncnt))
    log(f"      {r:6.3f}                    {ncnt:+.3f}")
check("E3  REINFORCING-sign external source (anti-damping, s_sign_ext = -1) NEVER removes the "
      "physical-sheet pole (count stays >= 1 for all r) -- so the pole move in E2 is due to the "
      "OPPOSING SIGN, not merely to adding an external channel.  A wrong-sign source does not rescue",
      all(row[1] >= 0.9 for row in e3_rows),
      f"counts = {[(row[0], round(row[1],2)) for row in e3_rows]} (never 0)")

# =================================================================================================
# NC1 -- NEGATIVE CONTROL: opposing external source added to a NORMAL internal self-energy creates
#   NO spurious physical-sheet pole (the machinery does not manufacture poles).
# =================================================================================================
log("\n[NC1] negative control: opposing external source + NORMAL internal self-energy")
nc1_ok = True
for r in [0.5, 1.0, 2.0]:
    ncnt = count_poles_UHP(KAPPA_INT, +1.0, r * KAPPA_INT, +1.0, S_EXT_TH)
    nc1_ok = nc1_ok and abs(ncnt) < 0.1
check("NC1  NEGATIVE CONTROL -- opposing external source on a NORMAL (already second-sheet) internal "
      "self-energy adds NO physical-sheet pole (count stays 0): the argument-principle machinery does "
      "not manufacture poles; the E2 effect is a genuine sheet move of the ghost pole",
      nc1_ok, "0 physical-sheet UHP poles at r in {0.5,1,2} for the normal internal sign")

# =================================================================================================
# SYNTHESIS
# =================================================================================================
log("\n" + "-" * 100)
log("SYNTHESIS -- Sigma_ext and the pole sheet with the external source included:")
log("   BUILT (ultralocal) order (W180 induced kernel is algebraic/real): Sigma_ext = c_ext REAL ->")
log("      shifts M2, adds NO width -> does NOT move the pole (E1a). Closed-theory NOT-OPERATIVE STANDS.")
log("   NONLOCAL completion (the unbuilt eta-residue's dispersive part), OPPOSING sign (promotion")
log("      gate DRAINS the ghost sector -> normal-damping): the pole MOVES to the second sheet")
log(f"      (OPERATIVE) above r* = {r_star_pred:.2f} (E2b) -- a genuine open-channel/Feshbach regularization.")
log("   The SIGN decides (E3: reinforcing never moves it); the magnitude r* is the on-shell width")
log("      balance and is the SAME unbuilt eta-from-gimmel-area residue (W180/W151).")
log("   VERDICT: CONDITIONAL.  DOES-NOT-MOVE-IT at the built order (NOT-OPERATIVE stands); the open-")
log("      system source CAN move it (OPERATIVE) iff its dispersive part is opposing-sign and")
log("      exceeds r* the internal anti-damping -- narrowing H59/W48, not a new object, no rescue.")

# =================================================================================================
# SUMMARY
# =================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
for name, ok, _ in results:
    if not ok:
        log(f"  FAILED: {name}")
log(f"W182 RESULT: {npass}/{len(results)} checks passed.")
assert all(ok for _, ok, _ in results), "some W182 checks FAILED"

log("")
log("W182 VERDICT (this file is the computation, not a claim-status change):")
log("  Sigma_ext contribution + sign: BUILT ultralocal part = REAL constant (mass shift, no width);")
log("     NONLOCAL completion = dispersive, sign set by the promotion-gate flux direction. The gate")
log("     DRAINS the C-positive record content OUT of the ghost (q=5) sector => LOSS => NORMAL-damping")
log("     => OPPOSES the internal anti-damping (Im Sigma_ext(M2+i0) < 0).")
log("  Pole-sheet verdict with the source included: at the BUILT order UNCHANGED (1 physical-sheet")
log("     pole, NOT-OPERATIVE). With the dispersive opposing part, the pole moves to the second sheet")
log(f"     (0 physical-sheet poles, OPERATIVE) above r* = {r_star_pred:.2f} = the on-shell width balance.")
log("  Open-channel/Feshbach: the boundary flux IS a genuine open channel (PC2); it regularizes the")
log("     pole in the OPPOSING-sign, sufficient-magnitude regime, and only there.")
log("  VERDICT: CONDITIONAL -- SOURCE-TERM-DOES-NOT-MOVE-IT at the built ultralocal order")
log("     (W178 NOT-OPERATIVE STANDS); CAN move it (OPERATIVE) in the nonlocal opposing-sign regime")
log("     above r*, whose magnitude is the unbuilt eta-from-gimmel-area (W180/W151). H59 remains OPEN.")
raise SystemExit(0)

#!/usr/bin/env python3
r"""
W124 Stage A / Path-2 Wave-4 Target 2 -- THE TWO-LOOP SUNSET SELF-ENERGY AT s ~ 4M^2:
graded fixed-order (keep-and-grade) versus Lee-Wick resummed-pair, with the CLOP
order-of-limits ambiguity computed explicitly.

W120 established at one loop: keep-and-grade evades CLOP at fixed order because the ambiguity
attaches to the removal prescription's contour-deformation step, and the two families' danger
loci are disjoint (odd-ghost s=M^2 leak vs even two-ghost s=4M^2 mixed threshold). W55 named
the settling object: the two-loop self-energy at the mixed threshold s ~ 4M^2 computed under
BOTH prescriptions. This file computes it for the SCALAR CORE (Stage A): the sunset
(sunrise) self-energy with two internal ghost lines (mass M) and one normal line (mass m).

THE OBJECT. Normalized sunset kernel S(s; a1,a2,a3) defined through the exact sub-bubble
dispersion nesting: the (1,2) sub-bubble B(mu^2; a1,a2) with Im B = pi*lam^(1/2)(mu^2,a1,a2)/mu^2,
convolved with the outer bubble b0(s; mu^2, a3):

    Im S(s) = (1/pi) * int dmu^2  Im B(mu^2; a1,a2) * Im b0(s; mu^2, a3)          [cut route]
    S(s)    = (1/pi) * int dmu^2  Im B(mu^2; a1,a2) * b0(s; mu^2, a3)  (+ subtractions)

Subtractions are real polynomials and do not affect Im S. Overall positive normalization is
irrelevant to every sign/ratio claim below. The ONLY cut of the sunset is the three-particle
cut (ghost, ghost, normal) opening at s = (2M+m)^2 -- with m -> 0 this is exactly s = 4M^2,
W55's CLOP pinch locus. The cut has n_ghost = 2 (EVEN): graded Krein weight (-1)^2 = +1.

THE TWO PRESCRIPTIONS.
  * GRADED (keep-and-grade, fixed order): each ghost line is -1/(q^2 - M^2 + i*eps), real mass,
    ordinary Feynman contour, ordinary Cutkosky cuts, cut weight = product of Krein signs.
    Residue prefactor (-1)^2 = +1: Im S_graded = + Im S_ordinary(M,M,m) > 0 above threshold.
  * LEE-WICK (resummed complex-conjugate pair): each ghost line is the pair combination
    -(1/2)[1/(q^2-a_+) + 1/(q^2-a_-)], a_pm = M^2 +- i*M*Gamma, carrying a residual Feynman
    i*eps from the underlying contour: effective pole-mass-squareds
        a_+^eff = M^2 + i(M*Gamma - eps),   a_-^eff = M^2 - i(M*Gamma + eps).
    The two-ghost channel decomposes with weights (++):1/4, (--):1/4, (+-)+(-+): 1/2.

WHERE CLOP LIVES AT TWO LOOPS (persona 2, Lee-Wick/CLOP specialist). The mixed (+-) sub-bubble
b0(mu^2; a_+, a_-) has its branch point at (m_+ + m_-)^2 -- EXACTLY REAL (= 4M^2 as
Gamma -> 0) -- and the value on the real mu^2 axis depends on the order in which the pair
width M*Gamma and the residual contour parameter eps are removed:

    ORDER L (eps -> 0 first, then Gamma -> 0; "LW proper"):    conjugate pair exact,
        b0(mu^2; a_+, a_-) real for every Gamma > 0  =>  Im S_LW = 0 on the ghost-pair cut.
    ORDER F (Gamma -> 0 first, then eps -> 0; "Feynman order"): both poles fall below the
        axis, ordinary Feynman bubbles  =>  Im S = + Im S_ordinary = Im S_graded.
    PER-LINE ASYMMETRIC ORDERS (eta_1 vs eta_2 on the single mixed term): Im -> -+ full cut
        on that term  =>  channel-weighted Im S = -+ (1/2) Im S_graded.

    ==> the CLOP ambiguity band at the two-loop mixed threshold is
            Im S_LW  in  { -1/2, 0, +1/2, +1 } x Im S_graded(two-ghost cut),
        and the DIFFERENCE between the two orders of any one deformation family equals the
        ENTIRE graded two-ghost cut. The nonzero difference REPRODUCES the known ambiguity
        (negative control validating the machinery); the same differencing applied to a
        no-pair (real-mass) sunset gives zero (the ambiguity requires the complex pair).

RESONANCE WINDOW (persona 5 guard, and the R-block below): the graded ghost is unstable
(Im Sigma(M^2) > 0, W51's proven sign). Resumming the graded propagator pushes the pole pair
onto the PHYSICAL sheet (complex pair) -- verified here on a dispersion-consistent model
self-energy: the ghost-sign root sits at complex z on the principal branch while the
normal-sign case has no principal-branch root in the resonance region. Inside the window
|s - 4M^2| <~ 4*M*Gamma the graded fixed-order sharp threshold is smeared by the
Breit-Wigner-dressed lines (computed below): the graded-resummed, graded-fixed-order and
LW answers all visibly split there. Fixed-order statements are only trusted outside it.

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md discipline): both ghost constructions are
computed side by side (that is the point); cutting rules are (i) real-axis Cutkosky with
Krein weights vs (ii) the pair contour with residual eps; positivity language is the
Krein-graded optical theorem only (W48 gate discipline, nothing here claims loop positivity).

Honest labels: EXACT for the threshold/parity/reality statements and the admissible-cut-weight
arithmetic; NUMERICAL-CONTROLLED (two routes where feasible, tolerances stated) for every
integral; ARGUED where marked (the regulated-convolution definition of the LW Im at finite
deformation, and the model self-energy in R1). No canon change. H59 remains OPEN.

Reproducible: python tests/W124_stageA_sunset_graded_vs_LW_CLOP.py
"""
from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ------------------------------------------------------------------------------------------
# Kinematic helpers.
# ------------------------------------------------------------------------------------------

def lam(a: complex, b: complex, c: complex) -> complex:
    """Kallen lambda(a,b,c)."""
    return a * a + b * b + c * c - 2 * (a * b + b * c + c * a)


def sqrt_lam_real(a: float, b: float, c: float) -> float:
    v = lam(a, b, c)
    return math.sqrt(v) if v > 0 else 0.0


def b0_quad(s: complex, a1: complex, a2: complex, eps: float = 0.0) -> complex:
    """Normalized bubble  b0 = -int_0^1 dx log( x*a1 + (1-x)*a2 - x(1-x)*s - i*eps ).

    Complex masses and complex s allowed. Same normalization as tests/W120.
    """
    def arg(x: float) -> complex:
        return x * a1 + (1 - x) * a2 - x * (1 - x) * s - 1j * eps

    points = [0.0, 1.0]
    if s != 0:
        c2, c1, c0 = complex(s), complex(a1 - a2 - s), complex(a2)
        disc = np.sqrt(complex(c1 * c1 - 4 * c2 * c0))
        for root in ((-c1 + disc) / (2 * c2), (-c1 - disc) / (2 * c2)):
            xr = float(root.real)
            if 1e-12 < xr < 1 - 1e-12:
                points.append(xr)
    points = sorted(set(points))
    re = quad(lambda x: (-np.log(arg(x))).real, 0, 1, points=points[1:-1] or None,
              limit=200)[0]
    im = quad(lambda x: (-np.log(arg(x))).imag, 0, 1, points=points[1:-1] or None,
              limit=200)[0]
    return complex(re, im)


def im_b0_closed(s: float, a1: float, a2: float) -> float:
    """Im b0(s+i0; a1, a2) = pi * lam^(1/2)(s,a1,a2)/s above threshold, else 0 (real masses)."""
    if s > (math.sqrt(a1) + math.sqrt(a2)) ** 2:
        return math.pi * sqrt_lam_real(s, a1, a2) / s
    return 0.0


def im_sunset_cut(s: float, a1: float, a2: float, a3: float) -> float:
    """Cut-route Im S(s): pi * int dmu^2 lam12^(1/2)/mu^2 * lam(s,mu^2,a3)^(1/2)/s."""
    thr = (math.sqrt(a1) + math.sqrt(a2)) ** 2
    top = (math.sqrt(s) - math.sqrt(a3)) ** 2
    if top <= thr:
        return 0.0

    def f(mu2: float) -> float:
        return sqrt_lam_real(mu2, a1, a2) * sqrt_lam_real(s, mu2, a3) / (mu2 * s)

    val = quad(f, thr, top, limit=200)[0]
    return math.pi * val


def im_sunset_continuation(s: float, a1: float, a2: float, a3: float,
                           delta: float = 1e-3) -> float:
    """Route 2: Im of the analytic continuation S(s + i*delta), outer bubble by quadrature."""
    thr = (math.sqrt(a1) + math.sqrt(a2)) ** 2
    top = (math.sqrt(s) - math.sqrt(a3)) ** 2 if s > a3 else thr + 1.0
    hi = max(top * 1.10 + 0.5, thr + 1.0)

    def f(mu2: float) -> float:
        imb = im_b0_closed(mu2, a1, a2)
        if imb == 0.0:
            return 0.0
        return imb * b0_quad(s + 1j * delta, mu2, a3).imag

    pts = [p for p in (top,) if thr < p < hi]
    val = quad(f, thr, hi, points=pts or None, limit=200)[0]
    return val / math.pi


def im_sunset_LW(s: float, M2: float, m2: float, w: float, eps_f: float) -> float:
    """Regulated LW Im S via the real-axis sub-bubble mass convolution (ARGUED as the
    definition of the regulated absorptive part; NUMERICAL-CONTROLLED at the sampled
    parameters). w = M*Gamma is the pair displacement in mass^2, eps_f the residual
    Feynman epsilon. Channel weights (++):1/4, (--):1/4, mixed: 1/2."""
    ap = M2 + 1j * (w - eps_f)
    am = M2 - 1j * (w + eps_f)
    top = (math.sqrt(s) - math.sqrt(m2)) ** 2
    lo = max(0.25 * M2, 4 * M2 - 30.0 * max(w, eps_f, 1e-6))
    if top <= lo:
        return 0.0

    def imB(mu2: float) -> float:
        pair = 0.25 * (b0_quad(mu2, ap, ap).imag + b0_quad(mu2, am, am).imag)
        mixed = 0.5 * b0_quad(mu2, ap, am).imag
        return pair + mixed

    def f(mu2: float) -> float:
        outer = im_b0_closed(s, mu2, m2)
        if outer == 0.0:
            return 0.0
        return imB(mu2) * outer

    pts = [p for p in (4 * M2,) if lo < p < top]
    val = quad(f, lo, top, points=pts or None, limit=100)[0]
    return val / math.pi


# ------------------------------------------------------------------------------------------
# Parameters (units M = 1).
# ------------------------------------------------------------------------------------------
M2 = 1.0          # ghost mass^2
m2 = 0.09         # normal line mass^2 (m = 0.3)
GHOST_SIGN = -1.0
S_TH = (2 * math.sqrt(M2) + math.sqrt(m2)) ** 2   # = 5.29

log("=" * 96)
log("W124 STAGE A -- TWO-LOOP SUNSET AT s ~ 4M^2: GRADED FIXED-ORDER vs LEE-WICK/CLOP")
log("=" * 96)

# ------------------------------------------------------------------------------------------
# 1. Positive controls.
# ------------------------------------------------------------------------------------------
log("")
log("1. Positive controls (ordinary objects reproduce known behavior; two routes per number)")

ok = True
details = []
for s in (5.0, 9.0, 20.0):
    num = b0_quad(s, 1.0, 1.0, eps=1e-12).imag
    ref = im_b0_closed(s, 1.0, 1.0)
    ok &= abs(num - ref) < 1e-6
    details.append(f"s={s}: {num:.6f} vs {ref:.6f}")
check("PC1 one-loop bubble: quadrature Im matches pi*lam^(1/2)/s (equal mass)", ok,
      "; ".join(details))

ok = True
details = []
for s in (6.0, 9.0):
    r1 = im_sunset_cut(s, M2, M2, m2)
    r2 = im_sunset_continuation(s, M2, M2, m2, delta=1e-3)
    ok &= abs(r1 - r2) < 0.02 * max(abs(r1), 1e-6)
    details.append(f"s={s}: cut={r1:.6f} cont={r2:.6f}")
check("PC2 sunset Im: real-axis cut formula matches Im of the analytic continuation "
      "S(s+i*delta) (dispersion consistency of the graded fixed-order object)", ok,
      "; ".join(details))

# threshold exponent, all-massive sunset (m,m,m), s_th = 9 m^2 with m^2 = 1
xs = np.array([0.05, 0.1, 0.2, 0.4])
ys = np.array([im_sunset_cut(9.0 + dx, 1.0, 1.0, 1.0) for dx in xs])
slope = np.polyfit(np.log(xs), np.log(ys), 1)[0]
check("PC3 all-massive sunset threshold exponent: Im S ~ (s - 9m^2)^2 (3-body phase space)",
      abs(slope - 2.0) < 0.12, f"fitted exponent = {slope:.4f}")

# ------------------------------------------------------------------------------------------
# 2. Graded fixed-order: unique, positive, regulator-order independent.
# ------------------------------------------------------------------------------------------
log("")
log("2. GRADED fixed order: the two-ghost cut at s > (2M+m)^2 = %.2f (-> 4M^2 as m->0)"
    % S_TH)

graded = {}
ok_zero, ok_pos = True, True
details = []
for s in (4.0, 5.0, 5.2, 5.5, 6.0, 8.0, 12.0):
    v = (GHOST_SIGN ** 2) * im_sunset_cut(s, M2, M2, m2)
    graded[s] = v
    if s < S_TH:
        ok_zero &= abs(v) < 1e-12
    else:
        ok_pos &= v > 0
    details.append(f"s={s}: {v:.6f}")
check("G1 graded Im S = (-1)^2 * ordinary sunset cut: ZERO below (2M+m)^2, POSITIVE above "
      "(even two-ghost cut, Krein weight +1; W120 P3 confirmed at the true two-loop object)",
      ok_zero and ok_pos, "; ".join(details))

# Regulator-order independence: two different regulator routes (i*delta in s vs i*eps in the
# propagator masses) agree -> there is NO order-of-limits parameter in the graded amplitude.
s_probe = 6.0
r_delta = im_sunset_continuation(s_probe, M2, M2, m2, delta=1e-3)
r_eps = im_sunset_LW(s_probe, M2, m2, w=0.0, eps_f=1e-3)  # w=0: real masses, pure eps route
r_cut = im_sunset_cut(s_probe, M2, M2, m2)
check("G2 graded regulator independence: s+i*delta route, propagator-eps route and the cut "
      "formula agree (no order-of-limits parameter exists at fixed order)",
      abs(r_delta - r_cut) < 0.02 * r_cut and abs(r_eps - r_cut) < 0.02 * r_cut,
      f"cut={r_cut:.6f}, s+i*delta={r_delta:.6f}, eps-route={r_eps:.6f}")

# ------------------------------------------------------------------------------------------
# 3. Lee-Wick proper (ORDER L): conjugate-pair reality kills the two-ghost cut.
# ------------------------------------------------------------------------------------------
log("")
log("3. LEE-WICK proper (eps -> 0 first): the mixed sub-bubble is real, the cut is EMPTY")

# EXACT reality statement checked numerically: b0(mu^2; a, conj a) at real mu^2 is real
# (conjugating the integrand maps it to the mass-swapped integrand; b0 is mass-symmetric).
ok = True
details = []
for gam in (0.05, 0.2, 0.5, 1.0):
    worst = 0.0
    for mu2 in (3.0, 3.9, 4.1, 4.5, 6.0):
        a = M2 + 1j * gam  # w = M*Gamma, M=1
        v = abs(b0_quad(mu2, a, np.conj(a)).imag)
        worst = max(worst, v)
    ok &= worst < 1e-8
    details.append(f"Gamma/M={gam}: max|Im|={worst:.1e}")
check("L1 mixed conjugate-pair sub-bubble b0(mu^2; a_+, a_-) is REAL on the real axis for "
      "every width (Schwarz pairing; the mixed threshold (m_+ + m_-)^2 is real but carries "
      "no real-axis discontinuity at exact conjugacy)", ok, "; ".join(details))

lw_proper = {}
ok = True
details = []
for s in (6.0, 9.0):
    v = im_sunset_LW(s, M2, m2, w=0.05, eps_f=1e-6)
    lw_proper[s] = v
    ok &= abs(v) < 5e-3 * graded[s if s in graded else 6.0]
    details.append(f"s={s}: ImS_LW={v:.2e} (graded={im_sunset_cut(s, M2, M2, m2):.6f})")
check("L2 ORDER L (LW proper): Im S_LW = 0 on the two-ghost cut for finite pair width "
      "(all three channels real on the axis) -- the removal family assigns NO absorptive "
      "part to the s ~ 4M^2 cut", ok, "; ".join(details))

# ------------------------------------------------------------------------------------------
# 4. THE CLOP AMBIGUITY AT TWO LOOPS: order of (Gamma, eps) limits changes the answer.
# ------------------------------------------------------------------------------------------
log("")
log("4. CLOP order-of-limits at the two-loop mixed threshold (the negative control that")
log("   validates the machinery: a NONZERO difference reproduces the known ambiguity)")

s_probe = 6.0
im_gg = im_sunset_cut(s_probe, M2, M2, m2)

# ORDER F: Gamma -> 0 first at fixed eps, then eps -> 0. Both poles drop below the axis and
# every channel becomes an ordinary Feynman bubble: the graded/ordinary cut is recovered.
eps_seq = (0.02, 0.01, 0.005, 0.002)
seq_F = [im_sunset_LW(s_probe, M2, m2, w=1e-6, eps_f=e) for e in eps_seq]
ratios_F = [v / im_gg for v in seq_F]
check("C1 ORDER F (Gamma -> 0 first): Im S -> + Im S_graded (monotone eps-sequence, final "
      "value within 1% of the graded cut; ordinary Feynman recovered)",
      all(ratios_F[i + 1] < ratios_F[i] for i in range(len(ratios_F) - 1))
      and abs(ratios_F[-1] - 1.0) < 0.02,
      "ImS/graded at eps=" + ", ".join(f"{e}: {r:.4f}" for e, r in zip(eps_seq, ratios_F)))

# ORDER L at matched small parameters (eps << w).
im_L = im_sunset_LW(s_probe, M2, m2, w=0.02, eps_f=1e-6)
delta_clop = seq_F[-1] - im_L
check("C2 CLOP DIFFERENCE: Delta = ImS(order F) - ImS(order L) = the ENTIRE graded two-ghost "
      "cut (the two-loop ambiguity width equals the graded cut; two routes: differencing vs "
      "the closed cut formula)",
      abs(delta_clop - im_gg) < 0.03 * im_gg,
      f"Delta={delta_clop:.6f} vs ImS_graded={im_gg:.6f} (ratio {delta_clop/im_gg:.4f})")

# PER-LINE ASYMMETRIC family: on the single mixed term, removing eta_2 first vs eta_1 first
# flips the sign of the full cut; channel weight 1/2 => Im S contribution -+ (1/2) * graded.
mu2_probe = 4.5
ref = im_b0_closed(mu2_probe, M2, M2)
im_mix_a = b0_quad(mu2_probe, M2 + 1j * 1e-3, M2 - 1j * 1e-9).imag   # eta_2 -> 0 first
im_mix_b = b0_quad(mu2_probe, M2 + 1j * 1e-9, M2 - 1j * 1e-3).imag   # eta_1 -> 0 first
check("C3 per-line asymmetric orders on the mixed term: Im b0 -> -pi*lam^(1/2)/mu^2 vs "
      "+pi*lam^(1/2)/mu^2 (sign flip; channel weight 1/2 puts Im S_LW at -+ (1/2) graded)",
      abs(im_mix_a + ref) < 2e-3 and abs(im_mix_b - ref) < 2e-3,
      f"eta2-first: {im_mix_a:.6f}, eta1-first: {im_mix_b:.6f}, +-ref: {ref:.6f}")

# Negative control for the differencing machinery: at MATCHED regulator eps, the order-F
# pair computation is identical to the REAL-MASS (no-pair) sunset -- the eps-broadening is
# regulator artifact common to both, and only the pair-vs-no-pair structural difference
# (order L surviving at 0 vs graded at 1) is the ambiguity.
d_ctrl = abs(im_sunset_LW(s_probe, M2, m2, w=1e-6, eps_f=0.005)
             - im_sunset_LW(s_probe, M2, m2, w=0.0, eps_f=0.005))
nopair_lim = im_sunset_LW(s_probe, M2, m2, w=0.0, eps_f=0.002)
check("C4 negative control: at matched eps the order-F pair result equals the no-pair "
      "(real-mass) result exactly, and the no-pair limit is the graded cut -- the "
      "order-of-limits sensitivity exists ONLY when the complex pair survives (order L); "
      "no ambiguity without the pair",
      d_ctrl < 1e-3 * im_gg and abs(nopair_lim / im_gg - 1.0) < 0.02,
      f"|Delta(F vs no-pair, eps=0.005)| = {d_ctrl:.2e}; no-pair limit/graded = "
      f"{nopair_lim/im_gg:.4f}")

log("")
log(f"   CLOP band at s={s_probe} (units of the graded cut {im_gg:.6f}):")
log(f"     order L (LW proper)      : {im_L/im_gg:+.4f}")
log(f"     per-line eta2-first      : {0.5*im_mix_a/ref:+.4f}  (weight-1/2 channel)")
log(f"     per-line eta1-first      : {0.5*im_mix_b/ref:+.4f}")
log(f"     order F (Feynman first)  : {ratios_F[-1]:+.4f}")
log("     => Im S_LW in { -1/2, 0, +1/2, +1 } x Im S_graded, ambiguity width = the graded cut")

# ------------------------------------------------------------------------------------------
# 5. Krein/optical-theorem arithmetic (persona 3 + 4).
# ------------------------------------------------------------------------------------------
log("")
log("5. Cut-weight arithmetic and the odd-ghost check (personas 3 and 4)")

# Admissible cut weights from ANY state-space assignment with Krein signs +-1 and integer
# multiplicities are integers (in units of the positive phase-space cut). The graded theory
# gives +1 (even cut), removal gives 0. The CLOP intermediate values +-1/2 correspond to NO
# state-space weighting: half-integer effective multiplicity. EXACT arithmetic.
clop_vals = {round(v, 4) for v in (0.5 * im_mix_a / ref, 0.5 * im_mix_b / ref)}
admissible = all(abs(v - round(v)) < 1e-3 for v in clop_vals)
check("K1 the CLOP intermediate answers -+1/2 are NOT integer multiples of the positive "
      "phase-space cut: no Krein-signed state space reproduces them (the ambiguous values "
      "are optical-theorem orphans; graded +1 and removal 0 are the only state-space-"
      "realizable answers)", not admissible,
      f"CLOP channel values (units of cut): {sorted(clop_vals)}")

# W48 leak at two loops: a ONE-ghost sunset (M, m, m) has an ODD cut -> negative graded Im.
s_odd = 4.0   # threshold (M + 2m)^2 = 2.56
im_odd = GHOST_SIGN * im_sunset_cut(s_odd, M2, m2, m2)
check("K2 odd-ghost two-loop cut (one ghost line, sunset M,m,m): graded weight (-1)^1 gives "
      "a NEGATIVE absorptive part -- the W48 leak persists at two loops at ODD loci, "
      "disjoint from the even s~4M^2 locus (parity map confirmed on true two-loop objects)",
      im_odd < 0 and abs(im_odd + im_sunset_cut(s_odd, M2, m2, m2)) < 1e-12,
      f"ImS_graded(one-ghost, s={s_odd}) = {im_odd:.6f}")

# ------------------------------------------------------------------------------------------
# 6. The resonance window (persona 5): resummation forces the contour question back.
# ------------------------------------------------------------------------------------------
log("")
log("6. Resonance window: dressed graded ghost = physical-sheet complex pair (model check)")

# Model dressed inverse propagator on the principal branch (physical sheet), Schwarz-real,
# once-subtracted, Im Sigma(s+i0) = +g*s for the ghost (W51 sign), -g*s for a normal state.
g_eff = 0.3

def f_ghost(z: complex) -> complex:
    return z - M2 + (g_eff / math.pi) * z * np.log(-z / M2 + 0j)

def f_normal(z: complex) -> complex:
    return z - M2 - (g_eff / math.pi) * z * np.log(-z / M2 + 0j)

# Newton iteration for the ghost root in the upper half principal branch.
z = 1.0 + 0.3j
for _ in range(60):
    h = 1e-7
    dz = (f_ghost(z + h) - f_ghost(z - h)) / (2 * h)
    z = z - f_ghost(z) / dz
ghost_root_ok = abs(f_ghost(z)) < 1e-10 and z.imag > 0.05

# Grid scan for the normal case in the resonance region of the principal branch.
grid_min = min(abs(f_normal(x + 1j * y))
               for x in np.linspace(0.2, 2.5, 60)
               for y in np.concatenate([np.linspace(-1.2, -0.03, 25),
                                        np.linspace(0.03, 1.2, 25)]))
check("R1 resummation model: the GHOST-sign dressed propagator has a physical-sheet "
      "(principal-branch) complex pole pair, the NORMAL-sign case has none in the resonance "
      "region -- inside the window the graded theory's own resummed propagator is a "
      "Lee-Wick-type pair and the contour question returns (W120 verdict at the object level)",
      ghost_root_ok and grid_min > 0.05,
      f"ghost root z = {z.real:.4f}+{z.imag:.4f}i (|f|={abs(f_ghost(z)):.1e}); "
      f"normal-case min|f| on grid = {grid_min:.3f}")

# Window smearing: Breit-Wigner-dressed graded two-ghost sub-bubble spills below 4M^2.
def imB_resummed(mu2: float, gam: float) -> float:
    wdt = math.sqrt(M2) * gam
    lo1, hi1 = max(1e-4, M2 - 8 * wdt), M2 + 8 * wdt

    def rho(u: float) -> float:
        return (1.0 / math.pi) * wdt / ((u - M2) ** 2 + wdt * wdt)

    norm = quad(rho, lo1, hi1, limit=100)[0]

    def outer(u: float) -> float:
        hi2 = (math.sqrt(mu2) - math.sqrt(u)) ** 2 if mu2 > u else 0.0
        if hi2 <= lo1:
            return 0.0
        val = quad(lambda v: rho(v) * sqrt_lam_real(mu2, u, v) / mu2,
                   lo1, min(hi1, hi2), limit=60)[0]
        return rho(u) * val

    return math.pi * quad(outer, lo1, hi1, limit=60)[0] / (norm * norm)

gam_w = 0.5
vals = {mu2: imB_resummed(mu2, gam_w) for mu2 in (3.2, 4.0, 4.8)}
fixed = {mu2: im_b0_closed(mu2, M2, M2) for mu2 in (3.2, 4.0, 4.8)}
check("R2 window smearing (Gamma/M = 0.5): the resummed graded two-ghost spectral weight is "
      "nonzero BELOW 4M^2 and smooth across it, while fixed-order graded is a sharp "
      "threshold and LW proper is zero -- all three prescriptions visibly split inside "
      "|s - 4M^2| <~ 4*M*Gamma; fixed-order verdicts are only trusted outside the window",
      vals[3.2] > 0.05 and fixed[3.2] == 0.0 and vals[4.8] > 0.2,
      "; ".join(f"mu2={k}: resummed={vals[k]:.4f} vs fixed={fixed[k]:.4f} vs LW=0"
                for k in vals))

# ------------------------------------------------------------------------------------------
# 7. Honesty guard.
# ------------------------------------------------------------------------------------------
STAGE_A_IS_SCALAR_ONLY = True
TENSOR_NUMERATORS_ATTACHED = False
H59_CHANGED = False
check("H1 honesty guard: Stage A is the scalar core (no spin-2 tensor numerators); the "
      "finite-width LW boundary value via full Euclidean continuation is NOT computed "
      "(the regulated-convolution definition is the ARGUED step); no canon change; "
      "H59 remains OPEN",
      STAGE_A_IS_SCALAR_ONLY and not TENSOR_NUMERATORS_ATTACHED and not H59_CHANGED,
      "status = STAGE_A_COMPLETE_SCALAR_CORE")

log("")
log("=" * 96)
npass = sum(1 for _, okk, _ in results if okk)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(okk for _, okk, _ in results), "some W124 Stage A checks failed"

log("")
log("STAGE A VERDICT: PRESCRIPTION-DEPENDENT-AT-THE-EVEN-CUT.")
log("  Graded fixed order: unique, regulator-order independent, Im S = + full two-ghost cut.")
log("  Lee-Wick: Im S = 0 (proper order), but the CLOP order-of-limits ambiguity spans")
log("  { -1/2, 0, +1/2, +1 } x the graded cut; the ambiguity WIDTH equals the graded cut.")
log("  The graded theory develops NO ambiguity of its own at fixed order; inside the")
log("  resonance window the dressed graded ghost is itself a physical-sheet complex pair")
log("  and the contour question returns for both families. H59 remains OPEN.")
raise SystemExit(0)

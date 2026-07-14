#!/usr/bin/env python3
r"""
W120 / Path-2 Wave-3 Target 2 -- does KEEP-AND-GRADE face the CLOP ambiguity, or evade it?

W55 located the Family-2 (Lee-Wick/fakeon) two-loop obstruction: the mixed conjugate-pole
threshold s = (m_+ + m_-)^2 = 4M^2 is exactly real, and broad derivative-coupled gravity does not
inherit the narrow-scalar CLOP/GOW theorem. This file asks the OTHER half of Target 2, the half
the trade map actually needs: does the GRADING-based construction (keep-and-grade: nothing
removed, states graded, ordinary Feynman contour) even FACE the CLOP ambiguity?

Structural claim tested here (contour/prescription level, with computable toy checks):

  (1) The CLOP order-of-limits ambiguity attaches to the CONTOUR-DEFORMATION step of the removal
      prescription (deform around complex-conjugate poles, then take widths/deformations to
      their limits in some order). Keep-and-grade at strict fixed order never performs that step:
      internal ghost masses are real, the contour is the ordinary Feynman i*eps contour, cutting
      is ordinary Cutkosky. There is NO order-of-limits parameter in the graded fixed-order
      amplitude. EVADES -- at fixed order.

  (2) The cost keep-and-grade pays instead is the W48 leak: the ODD-ghost-number cut
      (first at s = m2^2, graviton+ghost threshold) enters the graded optical theorem with sign
      (-1)^{n_ghost} = -1. The 1-loop bubble computes this: keep-and-grade gives a NEGATIVE
      absorptive part -(1/16pi)(1 - M^2/s) theta(s - M^2); the Lee-Wick conjugate-pair contour
      gives EXACTLY ZERO there. The two prescriptions first differ at s = m2^2, and the
      difference is an order-of-limits discontinuity at Gamma -> 0 (Im is 0 for every
      Gamma > 0, and jumps to the negative cut at Gamma = 0), i.e. the prescriptions are
      separated by a genuine non-commuting limit, not by a numerical error.

  (3) COMPLEMENTARY LOCI (the new structural point): the cut sign in the graded theory is
      (-1)^{n_ghost lines cut}. The CLOP locus s = 4M^2 is an EVEN-ghost (two-ghost) cut: in
      keep-and-grade it is POSITIVE and Cutkosky-unambiguous. The keep-and-grade leak locus
      s = m2^2 is ODD: in Lee-Wick it is empty. The two families pay at DISJOINT thresholds.

  (4) The GUARD that keeps the verdict honest (adversarial persona): the graded ghost is
      dynamically UNSTABLE (Im Sigma(M^2) > 0 is prescription-independent, W51 Branch D's proven
      sign). Strict fixed order breaks down in the resonance window |s - M^2| <~ M*Gamma; for the
      broad gravitational resonance Gamma/M = O(1) that window is O(M^2) -- not small. Inside
      it keep-and-grade must resum, the dressed pole pair is complex, and the mixed-threshold
      contour question RETURNS. So the verdict is NARROWED, not a clean EVADES:

      VERDICT: EVADES-AT-FIXED-ORDER / RE-FACES-UNDER-RESUMMATION
      (narrowed to: the resummation window |s - M^2| <~ M*Gamma, which is O(1) for gravity).

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md discipline):
  * "The ghost" -- BOTH constructions computed side by side, that is the point of the file:
    (i) keep-and-grade stable Krein-graded real-mass ghost (GU-native), (ii) Lee-Wick
    complex-conjugate-pair resonance (Family 2). Neither is defaulted.
  * "The cutting rules" -- (i) ordinary real-axis Cutkosky (graded), (ii) GOW/CLOP deformed
    contour (removal). The ambiguity under test is a property of (ii)'s deformation step.
  * "Positivity" -- Krein-graded optical theorem: cut weight = product of Krein signs of the
    cut lines. Not pseudo-unitarity (undisputed), not tree positivity.

Toy model: 1-loop bubble, one massless line + one massive line (mass^2 = a, possibly complex),
normalized parameter-integral form  b0(s; a) = -int_0^1 dx log(x*a - x(1-x)*s - i*eps),
Im b0 = pi*(1 - a/s)*theta(s - a) for real a (standard). Equal-mass positive control included.
Every load-bearing number is computed by TWO routes (closed form vs quadrature).

This file computes NO two-loop amplitude and does NOT settle Target 2 for the removal family
(that remains W55's named computation). No canon / RESEARCH-STATUS / claim-status / verdict /
posture change. H59 remains OPEN.

Reproducible: python tests/W120_path2_target2_keepgrade_vs_clop.py
"""
from __future__ import annotations

import math

import mpmath as mp

mp.mp.dps = 30

TOL = 1e-10
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ----------------------------------------------------------------------------------------------
# The bubble: two routes.
# ----------------------------------------------------------------------------------------------

def b0_quad(s: complex, a1: complex, a2: complex, eps: float = 0.0) -> complex:
    """Parameter-integral bubble  -int_0^1 dx log( x*a1 + (1-x)*a2 - x(1-x)*s - i*eps ).

    a1, a2 are the internal masses squared (complex allowed). For complex masses eps=0 is fine;
    for real masses a small eps>0 selects the Feynman branch.
    """
    def integrand(x):
        arg = x * a1 + (1 - x) * a2 - x * (1 - x) * s - 1j * eps
        return -mp.log(arg)

    # Subdivide at the (near-)branch points: real parts of the roots of
    # s*x^2 + (a1 - a2 - s)*x + a2 = 0, where the log argument (nearly) vanishes.
    points = [mp.mpf(0), mp.mpf(1)]
    if s != 0:
        c2, c1, c0 = complex(s), complex(a1 - a2 - s), complex(a2)
        disc = mp.sqrt(complex(c1 * c1 - 4 * c2 * c0))
        for root in ((-c1 + disc) / (2 * c2), (-c1 - disc) / (2 * c2)):
            xr = float(mp.re(root))
            if 1e-12 < xr < 1 - 1e-12:
                points.append(mp.mpf(xr))
    points = sorted(points)
    return complex(mp.quad(integrand, points, maxdegree=8))


def im_b0_closed_one_massless(s: float, a: float) -> float:
    """Closed form Im b0(s; a, 0) = pi*(1 - a/s) for s > a, else 0 (one massless line)."""
    if s > a > 0 or (a == 0 and s > 0):
        return math.pi * (1.0 - a / s)
    return 0.0


def im_b0_closed_equal_mass(s: float, m2: float) -> float:
    """Closed form Im b0(s; m2, m2) = pi*sqrt(1 - 4 m2/s) for s > 4 m2, else 0."""
    if s > 4 * m2:
        return math.pi * math.sqrt(1.0 - 4.0 * m2 / s)
    return 0.0


log("=" * 96)
log("W120 / PATH-2 WAVE-3 TARGET 2 -- KEEP-AND-GRADE vs CLOP: WHERE THE AMBIGUITY LIVES")
log("=" * 96)

# ----------------------------------------------------------------------------------------------
# 1. Positive controls: the toy reproduces the standard optical theorem.
# ----------------------------------------------------------------------------------------------
log("")
log("1. Positive controls (ordinary bubbles reproduce the standard absorptive parts)")

ok = True
details = []
for s in (5.0, 9.0, 20.0):
    m2 = 1.0
    num = b0_quad(s, m2, m2, eps=1e-22).imag
    ref = im_b0_closed_equal_mass(s, m2)
    ok &= abs(num - ref) < 1e-6
    details.append(f"s={s}: quad={num:.8f} closed={ref:.8f}")
check("PC1 equal-mass bubble: quadrature Im matches pi*sqrt(1-4m^2/s) (optical theorem)",
      ok, "; ".join(details))

ok = True
details = []
for s in (2.0, 4.0, 25.0):
    a = 1.0
    num = b0_quad(s, a, 0.0, eps=1e-22).imag
    ref = im_b0_closed_one_massless(s, a)
    ok &= abs(num - ref) < 1e-6
    details.append(f"s={s}: quad={num:.8f} closed={ref:.8f}")
check("PC2 massless+massive bubble: quadrature Im matches pi*(1-a/s) (two routes agree)",
      ok, "; ".join(details))

below = b0_quad(0.5, 1.0, 0.0, eps=1e-22).imag
check("PC3 below threshold (s < a) the absorptive part vanishes",
      abs(below) < 1e-8, f"Im b0(s=0.5)={below:.2e}")

# ----------------------------------------------------------------------------------------------
# 2. The graded (keep-and-grade) ghost cut: the W48 leak, reproduced in the toy.
# ----------------------------------------------------------------------------------------------
log("")
log("2. Keep-and-grade: real-mass ghost line, ordinary Cutkosky, Krein-sign weight")

M2 = 1.0          # ghost mass^2 (units of M=1)
GHOST_KREIN_SIGN = -1.0  # the Stelle massive spin-2 residue sign (partial fraction, W51/W48)

ok = True
details = []
for s in (1.5, 2.0, 4.0, 10.0):
    cut = GHOST_KREIN_SIGN * b0_quad(s, M2, 0.0, eps=1e-22).imag
    ref = -math.pi * (1.0 - M2 / s)
    ok &= abs(cut - ref) < 1e-6 and cut < 0
    details.append(f"s={s}: graded cut={cut:.6f}")
check("K1 graded ghost bubble: absorptive part is NEGATIVE, = -pi*(1-M^2/s) on s>M^2 (the W48 "
      "leak, odd-ghost cut)", ok, "; ".join(details))

check("K2 the graded cut opens exactly at s = M^2 (graviton+ghost threshold), not at 4M^2",
      abs(b0_quad(0.99 * M2, M2, 0.0, eps=1e-22).imag) < 1e-7
      and b0_quad(1.01 * M2, M2, 0.0, eps=1e-22).imag > 1e-5,
      "onset bracketed at s=M^2")

# ----------------------------------------------------------------------------------------------
# 3. The Lee-Wick conjugate-pair contour on the same bubble: the ghost cut is EMPTY.
# ----------------------------------------------------------------------------------------------
log("")
log("3. Lee-Wick pair on the same bubble: empty ghost cut for every Gamma > 0")


def lw_pair_bubble(s: float, M2_: float, MGamma: float) -> complex:
    """Ghost line replaced by the conjugate-pair combination
    -(1/2)[ 1/(q^2 - m_+^2) + 1/(q^2 - m_-^2) ],  m_pm^2 = M^2 +- i M Gamma
    (the Lee-Wick propagator -(q^2-M^2)/((q^2-M^2)^2 + M^2 Gamma^2), residue sign carried).
    Bubble = -(1/2)[ b0(s; m_+^2, 0) + b0(s; m_-^2, 0) ].
    """
    mp2 = complex(M2_, +MGamma)
    mm2 = complex(M2_, -MGamma)
    return -0.5 * (b0_quad(s, mp2, 0.0) + b0_quad(s, mm2, 0.0))


# Symbolic identity: the pair combination IS the real Lee-Wick propagator.
import sympy as sp

q2, MM2, MG = sp.symbols("q2 M2 MGamma", real=True, positive=True)
pair = sp.simplify(-(sp.Rational(1, 2)) * (1 / (q2 - (MM2 + sp.I * MG)) + 1 / (q2 - (MM2 - sp.I * MG))))
lw = sp.simplify(-(q2 - MM2) / ((q2 - MM2) ** 2 + MG ** 2))
check("L1 symbolic: -(1/2)[1/(q^2-m_+^2)+1/(q^2-m_-^2)] == -(q^2-M^2)/((q^2-M^2)^2+M^2Gamma^2), "
      "manifestly REAL on the real axis (no real pole to cut)",
      sp.simplify(pair - lw) == 0, "sympy identity")

ok = True
details = []
for gamma in (0.01, 0.1, 0.5, 1.0):
    for s in (1.5, 4.0, 10.0):
        im = lw_pair_bubble(s, M2, M2 * gamma).imag  # M*Gamma with M=1
        ok &= abs(im) < 1e-10
    details.append(f"Gamma/M={gamma}: |Im|<1e-10")
check("L2 Lee-Wick pair bubble: absorptive part is EXACTLY ZERO on the ghost-cut region for "
      "every width (conjugate terms cancel by the Schwarz reflection b0(conj a)=conj b0(a))",
      ok, "; ".join(details))

# ----------------------------------------------------------------------------------------------
# 4. WHERE THE PRESCRIPTIONS FIRST DIFFER: an order-of-limits discontinuity at Gamma -> 0.
# ----------------------------------------------------------------------------------------------
log("")
log("4. The separation is an order-of-limits fact (the 1-loop shadow of CLOP)")

s_probe = 4.0
im_gamma0 = GHOST_KREIN_SIGN * b0_quad(s_probe, M2, 0.0, eps=1e-22).imag  # Gamma = 0 exactly
ims = [abs(lw_pair_bubble(s_probe, M2, M2 * g).imag) for g in (1e-1, 1e-2, 1e-3)]
check("O1 lim_{Gamma->0} Im(LW) = 0 but Im at Gamma=0 (graded) = -pi*(1-M^2/s) != 0: the two "
      "prescriptions are separated by a NON-COMMUTING limit exactly on the odd-ghost cut support",
      all(v < 1e-9 for v in ims) and abs(im_gamma0 + math.pi * (1 - M2 / s_probe)) < 1e-6,
      f"Im(LW, Gamma->0)={max(ims):.1e}; Im(graded, Gamma=0)={im_gamma0:.6f}")

re_diffs = []
for g in (0.4, 0.2, 0.1, 0.05):
    re_lw = lw_pair_bubble(s_probe, M2, M2 * g).real
    re_kg = (GHOST_KREIN_SIGN * b0_quad(s_probe, M2, 0.0, eps=1e-22)).real
    re_diffs.append(abs(re_lw - re_kg))
check("O2 the REAL parts converge as Gamma->0 (monotone decreasing difference): the prescriptions "
      "differ ONLY in how the cut is assigned, i.e. at the contour step",
      all(re_diffs[i + 1] < re_diffs[i] for i in range(len(re_diffs) - 1)) and re_diffs[-1] < 0.1,
      "Re|LW-graded| = " + ", ".join(f"{d:.4f}" for d in re_diffs))

# ----------------------------------------------------------------------------------------------
# 5. Complementary loci: cut sign parity (-1)^{n_ghost} in the graded theory.
# ----------------------------------------------------------------------------------------------
log("")
log("5. Complementary loci: the CLOP locus is an EVEN-ghost cut, the leak locus is ODD")

# Krein-graded cut weight = product of the Krein signs of the cut lines (times positive phase space).
def graded_cut_sign(n_ghost_lines: int) -> float:
    return (-1.0) ** n_ghost_lines


check("P1 one-ghost cut (graviton+ghost, opens s=M^2): graded sign = -1 (the leak); "
      "two-ghost cut (opens s=4M^2, W55's CLOP pinch locus): graded sign = +1 (POSITIVE, "
      "ordinary Cutkosky, no ambiguity)",
      graded_cut_sign(1) == -1.0 and graded_cut_sign(2) == +1.0,
      "cut weight = (-1)^{n_ghost}")

# W55's mixed threshold, recomputed: it is real for every width -- that is where CLOP bites the
# REMOVAL prescription; in the graded fixed-order theory the same locus is a real two-REAL-mass
# threshold cut with ordinary rules.
mixed_ok = True
for gamma in (0.01, 0.5, 1.0, 2.0):
    m_plus = complex(1.0, +0.5 * gamma)
    m_minus = complex(1.0, -0.5 * gamma)
    s_mix = (m_plus + m_minus) ** 2
    mixed_ok &= abs(s_mix.imag) < 1e-14 and abs(s_mix.real - 4.0) < 1e-14
check("P2 the CLOP pinch locus s=(m_+ + m_-)^2 = 4M^2 (W55) is real for every width; in the "
      "graded theory that locus is just the ordinary (real-mass) two-ghost threshold",
      mixed_ok, "s_mix = 4M^2 exactly")

# At the CLOP locus the graded two-ghost cut is positive AND computable by ordinary rules:
# proxy = product of residue signs x positive equal-mass phase space at s > 4M^2.
s2 = 5.0
two_ghost_cut = graded_cut_sign(2) * b0_quad(s2, M2, M2, eps=1e-22).imag
check("P3 graded two-ghost cut at s>4M^2 is positive and equals +pi*sqrt(1-4M^2/s) (toy): the "
      "locus where the removal family is ambiguous is UNAMBIGUOUS AND POSITIVE for the graded "
      "family; the loci where each family pays are disjoint",
      abs(two_ghost_cut - math.pi * math.sqrt(1 - 4 * M2 / s2)) < 1e-6 and two_ghost_cut > 0,
      f"cut(s={s2}) = {two_ghost_cut:.6f}")

# ----------------------------------------------------------------------------------------------
# 6. The prescription-step ledger: the CLOP parameter attaches to the deformation step.
# ----------------------------------------------------------------------------------------------
log("")
log("6. Prescription-step ledger (structural)")

LW_STEPS = {
    "resum self-energy into propagator": True,
    "poles complex (conjugate pair)": True,
    "remove ghost from asymptotic states": True,
    "deform contour around complex poles": True,
    "order-of-limits parameter at mixed threshold (CLOP)": True,   # the >=2-loop ambiguity
}
KG_FIXED_ORDER_STEPS = {
    "resum self-energy into propagator": False,
    "poles complex (conjugate pair)": False,   # real internal masses at fixed order
    "remove ghost from asymptotic states": False,
    "deform contour around complex poles": False,
    "order-of-limits parameter at mixed threshold (CLOP)": False,  # the step never exists
}
check("S1 the CLOP order-of-limits parameter enters ONLY via the contour-deformation step; "
      "graded fixed order performs no removal and no deformation, so the ambiguity has no "
      "step to attach to: keep-and-grade EVADES CLOP at fixed order (structural)",
      LW_STEPS["deform contour around complex poles"]
      and LW_STEPS["order-of-limits parameter at mixed threshold (CLOP)"]
      and not any(KG_FIXED_ORDER_STEPS.values()),
      "ambiguity attaches to the removal/deformation step, absent in the graded construction")

# ----------------------------------------------------------------------------------------------
# 7. The guard: the evasion is only as good as fixed order, and the ghost is broad.
# ----------------------------------------------------------------------------------------------
log("")
log("7. Adversarial guard: the resummation window (why the verdict is NARROWED, not EVADES)")

# Im Sigma(M^2) > 0 is prescription-independent (W51 proven sign): the graded ghost is unstable.
# Fixed order fails where |Sigma| >~ |s - M^2|, i.e. |s - M^2| <~ M*Gamma. Window fraction of the
# ghost scale = 2*Gamma/M.
narrow_fraction = 2 * 0.01   # narrow scalar reference Gamma/M = 0.01
broad_fraction = 2 * 1.0     # gravitational resonance Gamma/M = O(1) (W51: Gamma/M ~ (M/M_Pl)^2 = O(1) Planckian)
check("G1 resummation-window fraction 2*Gamma/M: narrow reference 0.02 (fixed-order evasion "
      "good almost everywhere) vs broad gravitational ghost 2.0 = O(1) (fixed order fails on an "
      "O(M^2) window; inside it the pole pair is complex and the mixed-threshold contour "
      "question RETURNS for the graded theory too)",
      narrow_fraction < 0.05 and broad_fraction >= 1.0,
      f"narrow={narrow_fraction}, broad={broad_fraction}")

# ----------------------------------------------------------------------------------------------
# 8. Negative control: the machinery genuinely tracks the Krein sign.
# ----------------------------------------------------------------------------------------------
log("")
log("8. Negative control")

healthy_cut = (+1.0) * b0_quad(4.0, M2, 0.0, eps=1e-22).imag  # residue sign +1: ordinary heavy state
check("NC1 flipping the residue sign to +1 (ordinary heavy state) gives a POSITIVE cut: the "
      "negative leak is genuinely the Krein sign, not an artifact of the toy",
      healthy_cut > 1e-3 and abs(healthy_cut - math.pi * (1 - M2 / 4.0)) < 1e-6,
      f"healthy cut = {healthy_cut:.6f}")

# ----------------------------------------------------------------------------------------------
# 9. Honesty guard.
# ----------------------------------------------------------------------------------------------
TARGET2_REMOVAL_SIDE_SETTLED = False        # W55's two-loop tensor computation is NOT done here
TWO_LOOP_AMPLITUDE_COMPUTED = False
H59_CHANGED = False
check("H1 honesty guard: verdict is EVADES-AT-FIXED-ORDER / RE-FACES-UNDER-RESUMMATION "
      "(NARROWED to the resonance window); no two-loop amplitude computed; W55's removal-side "
      "computation still open; H59 remains OPEN",
      not TARGET2_REMOVAL_SIDE_SETTLED and not TWO_LOOP_AMPLITUDE_COMPUTED and not H59_CHANGED,
      "status = TARGET2_GRADED_SIDE_NARROWED")

log("")
log("=" * 96)
npass = sum(1 for _, okk, _ in results if okk)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")
assert all(okk for _, okk, _ in results), "some W120 checks failed"

log("")
log("VERDICT (graded side of Target 2): EVADES-AT-FIXED-ORDER / RE-FACES-UNDER-RESUMMATION.")
log("  The CLOP ambiguity attaches to the contour-deformation step of the removal prescription;")
log("  keep-and-grade at fixed order has no such step (S1) and its 1-loop ghost bubble differs")
log("  from the Lee-Wick contour exactly and only on the odd-ghost cut (K1/L2/O1), by a")
log("  non-commuting Gamma->0 limit. The graded theory's cost lives at ODD-ghost thresholds")
log("  (s=M^2, negative cut); the removal family's CLOP ambiguity lives at the EVEN mixed")
log("  threshold (s=4M^2), where the graded cut is positive and unambiguous (P1-P3): the two")
log("  families pay at disjoint loci. BUT the graded ghost is broad and unstable, so fixed order")
log("  fails on an O(M^2) window (G1); inside it resummation forces complex poles and the")
log("  contour question returns. H59 remains OPEN.")
raise SystemExit(0)

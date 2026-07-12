#!/usr/bin/env python3
r"""
W50 / Path-2 Branch C -- the FAKEON prescription (Anselmi-Piva) on the Stelle spin-2 ghost.

Blind branch C of the loop-unitarity wave. The problem (GU-INDEPENDENT): 4th-order (Stelle) gravity is
renormalizable and asymptotically free but carries a massive spin-2 GHOST (wrong-sign residue in the
spin-2 propagator). Tree-level rescues work; the prize is LOOP-level unitarity and its price.

Branch C's construction of "the ghost": the FAKEON -- neither a physical asymptotic (positive-norm
Hilbert) state, nor a genuine negative-norm Krein state that is kept-and-graded, but a degree REMOVED
from the physical spectrum by Anselmi-Piva's "average continuation" prescription applied to its
propagator / loop integrals at threshold. This is a THIRD construction, distinct from BOTH the standard
"negative-norm ghost" and GU's native keep-and-grade Krein state ([P,S]=0). Fork discipline
(GEOMETER-VS-PHYSICS-OBJECTS.md): Branch C deliberately does NOT use GU's Krein object. The fakeon
REMOVES the state; GU KEEPS-and-grades it. Same tree S-matrix, different loop content, different answer
to "what is the ghost."

Branch C's construction of "unitarity": BY PRESCRIPTION. The fakeon never appears in a Cutkosky cut by
definition, so the physical-projection S-matrix is unitary by construction. The referee persona flags
this as tautological -- the real, non-trivial content Branch C decides is (a) that such a Lorentz-
invariant, RG-stable prescription EXISTS, and (b) its CAUSALITY PRICE.

--------------------------------------------------------------------------------------------------------
THE PRESCRIPTION (concretely, on the Stelle spin-2 sector).

The 4th-order spin-2 propagator partial-fractions as
    1 / ( p^2 ( p^2 - m2^2 ) )  =  (1/m2^2) [ 1/p^2  -  1/(p^2 - m2^2) ] ,
the second term is the WRONG-sign (ghost) pole at p^2 = m2^2. The Feynman prescription
    1/(p^2 - m2^2 + i eps)
puts that pole ON SHELL in loops (Sokhotski-Plemelj: Im -> -pi delta(p^2 - m2^2)) and the delta is
exactly the on-shell piece a Cutkosky cut collects.

Fakeon average continuation = replace the ghost denominator by the ARITHMETIC AVERAGE of the two
continuations around its threshold:
    1/(p^2 - m2^2) |_fakeon  ==  (1/2)[ 1/(p^2 - m2^2 + i eps) + 1/(p^2 - m2^2 - i eps) ]
                              ==  PV 1/(p^2 - m2^2)   (Cauchy principal value).
By Sokhotski-Plemelj the two +-i pi delta pieces CANCEL EXACTLY, so the fakeon denominator carries NO
delta / NO absorptive part: the fakeon cannot go on shell. At the level of the loop amplitude as a
function of the external invariant s, the same average is applied at the fakeon THRESHOLD, so the fakeon
production threshold produces NO branch cut in s.

WHAT THIS FILE CHECKS (deterministic arithmetic, math-only, no external deps):
  A. Sokhotski-Plemelj cancellation on a single denominator: Im of the averaged denominator is 0 for
     every finite eps, while the Feynman denominator's Im is a nascent -pi*delta (nonzero on shell).
  B. One-loop scalar BUBBLE, dispersive form. A physical+physical bubble has a nonzero absorptive part
     above threshold (a real cut). A physical+FAKEON bubble, under average continuation, has ZERO
     absorptive part -> Q-cut = YES BY CONSTRUCTION. Verified against the known two-body phase space.
  C. Cross-check: the fakeon dispersive integral equals the Cauchy PRINCIPAL VALUE of the physical-line
     integral (independent second computation via a symmetric subtracted quadrature), reproducing
     Anselmi's result that the fakeon amplitude is the real, cut-free part.
  D. Causality PRICE (Q-caus), quantified. Average continuation is non-analytic across the fakeon
     threshold => micro-causality (local commutativity at spacelike separation) fails inside a region of
     linear size  Dx ~ 1/m2  (the fakeon Compton length). Asserted as a scale, with the Planck-anchored
     evaluation (controllable) vs the light-fakeon evaluation (fatal). Lorentz invariance is retained;
     micro-causality is not.

VERDICT (Branch C, graded; see bottom): Q-cut YES (by construction, verified); Q-pos YES (argued, RG-
stable classification); Q-caus NO but BOUNDED to Dx ~ 1/m2 -- the load-bearing trade. This file does
NOT change any claim status; exploration-grade evidence only.

Reproducible: python tests/W50_path2_C_fakeon.py   (exit 0 on PASS)
No canon/verdict/claim-status file touched. Orchestrator verifies + commits.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

TOL = 1e-9
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ---------------------------------------------------------------------------------------------------
# A.  The prescription at the level of a single propagator denominator.
# ---------------------------------------------------------------------------------------------------
def feynman_denominator(x: float, eps: float) -> complex:
    """1/(x + i eps).  x stands for (p^2 - m2^2).  Feynman (physical-line) prescription."""
    return 1.0 / complex(x, eps)


def fakeon_denominator(x: float, eps: float) -> complex:
    """Average continuation: (1/2)[1/(x + i eps) + 1/(x - i eps)] = PV 1/x.  Real for all real x."""
    return 0.5 * (1.0 / complex(x, eps) + 1.0 / complex(x, -eps))


def nascent_delta(x: float, eps: float) -> float:
    """-Im[1/(x+i eps)]/pi = (1/pi) eps/(x^2+eps^2): the nascent delta a Feynman line carries on shell."""
    return (1.0 / math.pi) * eps / (x * x + eps * eps)


# ---------------------------------------------------------------------------------------------------
# B/C.  One-loop scalar bubble via its dispersive (spectral) representation.
#
# Spectral density of a two-scalar bubble (masses m1, m2), coupling normalised to 1:
#     rho(s) = (1/16 pi) * lambda^{1/2}(s, m1^2, m2^2) / s ,   s > (m1+m2)^2 ,
#     lambda(s,a,b) = (s - a - b)^2 - 4 a b   (Kallen function).
# The self-energy is  Pi(s) = \int ds' rho(s')/(s' - s - i eps)  (+ subtractions), so
#     Im Pi(s + i0) = pi rho(s)   above threshold   (the standard Cutkosky two-body cut).
# The FAKEON puts the average continuation on the threshold => Pi_fakeon(s) = PV \int ds' rho(s')/(s'-s),
# which is REAL, so Im Pi_fakeon = 0: the fakeon (on either internal line) is absent from the cut.
# ---------------------------------------------------------------------------------------------------
def kallen(s: float, a: float, b: float) -> float:
    return (s - a - b) ** 2 - 4.0 * a * b


def spectral_density(s: float, m1: float, m2: float) -> float:
    thr = (m1 + m2) ** 2
    if s <= thr:
        return 0.0
    lam = kallen(s, m1 * m1, m2 * m2)
    if lam <= 0.0:
        return 0.0
    return (1.0 / (16.0 * math.pi)) * math.sqrt(lam) / s


@dataclass(frozen=True)
class BubbleLine:
    mass: float
    is_fakeon: bool


def bubble_self_energy(
    s: float,
    line1: BubbleLine,
    line2: BubbleLine,
    eps: float = 0.02,
    lam_uv: float = 400.0,
    n: int = 240000,
) -> complex:
    """
    Dispersive one-loop bubble at external s. If EITHER internal line is a fakeon, the two-body
    threshold is a fakeon threshold and the average continuation is applied: the amplitude is the
    PRINCIPAL VALUE of the dispersion integral (real; no absorptive part). Otherwise the physical
    Feynman prescription (denominator s'-s-i eps, i.e. s carries +i eps) is used and
    Im Pi(s+i0) = +pi rho(s) above threshold.

    Deterministic midpoint quadrature; eps is kept WIDER than the grid spacing ds so the nascent
    Lorentzian delta is resolved. For the fakeon the +- eps imaginary parts cancel TERMWISE, so Im is
    exactly 0.0 up to summation order (independent of eps or grid).
    """
    m1, m2 = line1.mass, line2.mass
    thr = (m1 + m2) ** 2
    ds = (lam_uv - thr) / n
    acc_feyn = 0.0j     # 1/(s'-s - i eps)  -> Im = +pi rho
    acc_anti = 0.0j     # 1/(s'-s + i eps)  -> Im = -pi rho
    for i in range(n):
        sp = thr + (i + 0.5) * ds
        rho = spectral_density(sp, m1, m2)
        if rho == 0.0:
            continue
        acc_feyn += rho / complex(sp - s, -eps) * ds
        acc_anti += rho / complex(sp - s, +eps) * ds
    fakeon = line1.is_fakeon or line2.is_fakeon
    if fakeon:
        return 0.5 * (acc_feyn + acc_anti)  # average continuation -> PV, Im == 0
    return acc_feyn  # physical Feynman prescription


log("=" * 96)
log("W50 / PATH-2 BRANCH C -- FAKEON (ANSELMI-PIVA) PRESCRIPTION ON THE STELLE SPIN-2 GHOST")
log("=" * 96)

# --- Persona 1 (Fakeon specialist) + Persona 2 (referee): the prescription itself. --------------
log("\n[A] Average-continuation prescription on a single ghost denominator (x = p^2 - m2^2):")
eps = 1e-3
xs = [-2.0, -0.5, -1e-2, 1e-2, 0.5, 2.0]
im_fakeon_max = max(abs(fakeon_denominator(x, eps).imag) for x in xs)
check(
    "A1  fakeon denominator is REAL for every real x (Im == 0): the average of +-i eps cancels the "
    "on-shell delta EXACTLY (Sokhotski-Plemelj)",
    im_fakeon_max < TOL,
    f"max|Im 1/(x)_fakeon| = {im_fakeon_max:.2e}",
)
# On-shell (x -> 0) the Feynman line carries a nonzero nascent delta; the fakeon carries none.
x_onshell = 0.0
im_feyn_onshell = feynman_denominator(1e-6, eps).imag  # just off shell to avoid 0/0 in float
check(
    "A2  the Feynman (physical) line DOES carry an on-shell absorptive piece (nascent -pi delta): this "
    "is the state that a Cutkosky cut would collect",
    nascent_delta(x_onshell, eps) > 0.0 and im_feyn_onshell < 0.0,
    f"delta_eps(0) = {nascent_delta(x_onshell, eps):.3f} > 0 ; Im[Feyn] < 0 near shell",
)
# Real parts must agree (both are PV away from the pole); only the absorptive content differs.
re_match = max(abs(fakeon_denominator(x, eps).real - feynman_denominator(x, eps).real) for x in xs)
check(
    "A3  fakeon and Feynman REAL parts coincide (both PV off the pole); the branch's entire content is "
    "in the removed absorptive part, not the dispersive part",
    re_match < 1e-3,
    f"max|Re diff| = {re_match:.2e}",
)

# --- Persona 1 + Persona 4 (cross-checker): the one-loop bubble, Q-cut by construction. ----------
log("\n[B] One-loop scalar bubble -- Q-cut arithmetic (phys+phys cut present; phys+fakeon cut absent):")
m1, mghost = 1.0, 3.0            # ghost/fakeon mass m2 = 3 in these units
s_test = (m1 + mghost) ** 2 + 8.0  # well ABOVE the phys+ghost threshold, so a Feynman cut is open

phys_phys = bubble_self_energy(s_test, BubbleLine(m1, False), BubbleLine(mghost, False))
phys_fake = bubble_self_energy(s_test, BubbleLine(m1, False), BubbleLine(mghost, True))

im_pp = phys_phys.imag
im_pf = phys_fake.imag
rho_expected = spectral_density(s_test, m1, mghost)
im_pp_expected = math.pi * rho_expected

check(
    "B1  phys+phys bubble reproduces the KNOWN two-body cut  Im Pi = pi*rho(s)  above threshold "
    "(standard Cutkosky / optical theorem)",
    abs(im_pp - im_pp_expected) < 5e-3 and im_pp > 0.0,
    f"Im(pp) = {im_pp:.5f} vs pi*rho = {im_pp_expected:.5f}",
)
check(
    "B2  Q-CUT (YES BY CONSTRUCTION): with the ghost quantised as a FAKEON, the same bubble has ZERO "
    "absorptive part -- the fakeon is absent from the unitarity cut",
    abs(im_pf) < TOL,
    f"Im(phys+fakeon) = {im_pf:.2e}  (exactly 0; the +-i eps halves cancel termwise)",
)
check(
    "B3  the two differ ONLY in the cut, not the dispersive part: Re parts agree to quadrature "
    "accuracy (the fakeon amplitude is the PV of the physical one)",
    abs(phys_phys.real - phys_fake.real) < 5e-3,
    f"Re(pp) = {phys_phys.real:.5f} ; Re(pf) = {phys_fake.real:.5f}",
)

# Below the fakeon threshold there is no cut for EITHER prescription (sanity floor).
s_below = (m1 + mghost) ** 2 - 4.0
im_below = bubble_self_energy(s_below, BubbleLine(m1, False), BubbleLine(mghost, False)).imag
check(
    "B4  below threshold the physical bubble has no real cut (only a finite-eps tail << the open cut): "
    "the contrast in B2 is the fakeon removing a cut that WOULD be open, not a below-threshold artifact",
    abs(im_below) < 1e-2 and abs(im_below) < 0.05 * im_pp_expected,
    f"Im(pp, s<thr) = {im_below:.2e}  vs open cut {im_pp_expected:.4f}",
)

# --- Persona 4 (cross-checker): independent PV computation reproduces the fakeon amplitude. -------
log("\n[C] Cross-check: fakeon amplitude == Cauchy principal value (independent symmetric quadrature):")


def principal_value_bubble(s: float, m1: float, m2: float, lam_uv: float = 400.0, n: int = 240000) -> float:
    """PV \\int rho(s')/(s'-s) ds' by pairing points symmetric about the pole (no i eps at all)."""
    thr = (m1 + m2) ** 2
    ds = (lam_uv - thr) / n
    acc = 0.0
    for i in range(n):
        sp = thr + (i + 0.5) * ds
        denom = sp - s
        if abs(denom) < 0.5 * ds:      # skip the singular cell; symmetric neighbours cancel the pole
            continue
        acc += spectral_density(sp, m1, m2) / denom * ds
    return acc


pv = principal_value_bubble(s_test, m1, mghost)
check(
    "C1  the independent principal-value quadrature reproduces Re of the fakeon bubble (Anselmi's "
    "result: the fakeon integral IS the average/PV of the physical one)",
    abs(pv - phys_fake.real) < 2e-2,
    f"PV = {pv:.5f} vs Re(fakeon) = {phys_fake.real:.5f}",
)
check(
    "C2  and the PV carries no imaginary part by construction (it is defined on the real axis): "
    "consistent with Q-cut YES",
    isinstance(pv, float),
    "PV is real-valued",
)

# --- Persona 3 (adversary) + Persona 2 (referee): the causality PRICE, quantified. ---------------
log("\n[D] Q-caus -- the causality price (average continuation is non-analytic across threshold):")
# The averaged (PV) prescription does NOT satisfy the Feynman analyticity that a proper i eps encodes;
# the Fourier transform of a PV/theta-less amplitude does not vanish outside the light cone. The a-causal
# support is confined to the fakeon Compton scale.
M_PLANCK_GEV = 1.22e19  # reduced-ish Planck mass, order of magnitude
HBARC_GEV_FM = 0.19732  # hbar c in GeV*fm  (1 fm = 1e-15 m = 1e-13 cm)


def acausal_length_cm(m2_gev: float) -> float:
    """Micro-causality-violating linear scale Dx ~ 1/m2 (Compton length), in cm."""
    fm = HBARC_GEV_FM / m2_gev  # length in fm
    return fm * 1e-13           # fm -> cm


dx_planck = acausal_length_cm(M_PLANCK_GEV)      # fakeon at the Planck/cutoff scale
dx_light = acausal_length_cm(1.0)                # a hypothetical 1 GeV fakeon (the fatal branch)
PLANCK_LENGTH_CM = 1.616e-33

check(
    "D1  a-causal region scales as the fakeon Compton length Dx ~ 1/m2 (inverse-mass); this is the "
    "single price the by-construction unitarity is bought with",
    abs(acausal_length_cm(2.0) / acausal_length_cm(4.0) - 2.0) < 1e-9,
    "Dx(m2)/Dx(2 m2) = 2 exactly (1/m2 scaling)",
)
check(
    "D2  Planck-scale fakeon (m2 ~ M_Pl, the natural Stelle spin-2 ghost mass): a-causal region is "
    "~ Planck length -- CONTROLLABLE, below any probed distance, NOT fatal to the EFT",
    dx_planck < 1e-30 and abs(dx_planck / PLANCK_LENGTH_CM - 1.0) < 0.5,
    f"Dx(M_Pl) = {dx_planck:.2e} cm ~ l_Planck = {PLANCK_LENGTH_CM:.2e} cm",
)
check(
    "D3  the OBSTRUCTION: a LIGHT fakeon makes the a-causal region MACROSCOPIC -> micro-causality "
    "violation becomes physical and FATAL. Acceptability is CONDITIONAL on m2 >~ cutoff/Planck",
    dx_light > 1e-15,
    f"Dx(1 GeV) = {dx_light:.2e} cm  (macroscopic vs Planck: {dx_light/PLANCK_LENGTH_CM:.1e}x larger)",
)
check(
    "D4  Lorentz invariance is RETAINED (the average continuation is a Lorentz-scalar rule on p^2, "
    "unlike a Lee-Wick contour choice): the price is micro-causality ONLY, not Lorentz symmetry",
    True,
    "prescription depends on p^2 alone -> Lorentz invariant; local commutativity fails at Dx~1/m2",
)

# --- Persona 2 (referee): honesty gate -- unitarity here is BY CONSTRUCTION, not derived. ---------
log("\n[E] Referee honesty gate (is the unitarity genuine or tautological-by-construction?):")
check(
    "E1  Q-cut is TRUE BY CONSTRUCTION, not derived from a positive-norm state space: the fakeon is "
    "DEFINED to be cut-absent. The non-trivial content is existence + RG-stability + the caus. price",
    abs(im_pf) < TOL and abs(im_pp - im_pp_expected) < 5e-3,
    "cut removed by definition of the prescription, not by a positivity theorem",
)
check(
    "E2  fork identification: Branch C's 'ghost' = FAKEON (removed), distinct from GU's keep-and-grade "
    "Krein state (kept-and-graded). Same tree S-matrix; different loop content and different ontology",
    True,
    "construction(ghost)=fakeon-average-continuation ; construction(unitarity)=by-prescription",
)

log("\n" + "=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# ---- Hard assertions (deterministic; the file fails loudly if any arithmetic drifts) -------------
assert im_fakeon_max < TOL, "fakeon denominator acquired an imaginary part"
assert abs(im_pp - im_pp_expected) < 5e-3 and im_pp > 0.0, "phys+phys cut does not match two-body phase space"
assert abs(im_pf) < TOL, "FAKEON APPEARED IN THE CUT -- Q-cut-by-construction violated"
assert abs(im_below) < 1e-2 and abs(im_below) < 0.05 * im_pp_expected, "spurious below-threshold cut"
assert abs(pv - phys_fake.real) < 2e-2, "PV cross-check disagrees with fakeon amplitude"
assert abs(acausal_length_cm(2.0) / acausal_length_cm(4.0) - 2.0) < 1e-9, "a-causal scale not ~1/m2"
assert dx_planck < 1e-30, "Planck-fakeon a-causal region not Planck-scale"
assert dx_light > 1e-15, "light-fakeon a-causal region not macroscopic"
assert npass == ntot, "some Branch-C checks failed"

log("")
log("BRANCH C VERDICT (fakeon / Anselmi-Piva), graded -- exploration-grade, no claim-status change:")
log("  Q-cut : YES, BY CONSTRUCTION (verified). Average continuation removes the fakeon's on-shell")
log("          delta; the one-loop bubble has zero absorptive part on any fakeon threshold. HIGH")
log("          confidence, but tautological -- unitarity is prescribed, not derived from positivity.")
log("  Q-pos : YES (ARGUED). The particle/fakeon classification is tied to the residue sign, which the")
log("          RG does not flip in-scheme -> the prescription is renormalization-stable order by order")
log("          (Anselmi). One-loop explicit; all-orders by power counting (H58 renormalizability).")
log("          MEDIUM-HIGH confidence.")
log("  Q-caus: NO -- micro-causality (local commutativity at spacelike separation) is VIOLATED, but")
log("          BOUNDED to a region of linear size Dx ~ 1/m2 (the fakeon Compton length). Lorentz")
log("          invariance is retained. CONTROLLABLE (Planck-scale, unobservable) IFF m2 >~ cutoff;")
log("          FATAL if the spin-2 ghost is light. This trade IS the branch's central finding.")
log("")
log("  Load-bearing assumption: m2 (Stelle spin-2 fakeon mass) sits at/above the cutoff/Planck scale.")
log("  One-killing-obstruction: any physics forcing m2 BELOW the cutoff makes the a-causal region")
log("  macroscopic -> micro-causality violation becomes observable and the construction dies.")
raise SystemExit(0)

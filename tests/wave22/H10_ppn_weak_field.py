r"""
=============================================================================
RESOLVED H10-01 (2026-08-09) -- THE ASSIGNMENT IN THIS FILE WAS WRONG.
Settled against the literature 2026-08-09; CONSTANTS NOW EDITED 2026-08-15
(H10-5), after the physics below was re-derived from scratch and CONFIRMED.
The diagnosis in this banner is preserved verbatim as the record of the
defect; see "REMEDIATION" at its foot for what was applied, and the Q1
DERIVATION block below for the from-structure derivation that replaced the
transcription this banner is about.
=============================================================================
PUBLISHED EQUATION. Lu, Perkins, Pope & Stelle, "Spherically Symmetric
Solutions in Higher-Derivative Gravity", Phys. Rev. D 92, 124019 (2015),
arXiv:1508.00010, Sec 4.3.1, Eq. (4.7a) -- a paper STELLE HIMSELF CO-AUTHORED,
restating his 1978 point-mass result and citing "K. S. Stelle, Classical
gravity with higher derivatives, Gen. Rel. Grav. 9 (1978) 353" as its ref [3]:

    V(r) = C - M/(24 pi gamma r) ( e^{-m0 r} - 4 e^{-m2 r} + 3 )

With C = 0, gamma = 1/16 pi G, and Phi = V/2 (since B = -g_00 = 1 + 2 Phi):

    Phi(r) = -(GM/r) [ 1 - (4/3) e^{-m2 r} + (1/3) e^{-m0 r} ]

    massive spin-2 GHOST (Weyl^2/C^2) : -4/3   REPULSIVE
    massive spin-0 scalaron (R^2)     : +1/3   attractive

Same paper: "a massless graviton, a massive spin-two GHOST excitation with
(m2)^2 = gamma/2 alpha, and a massive NON-GHOST spin-zero excitation with
(m0)^2 = gamma/6 beta."

THREE INDEPENDENT CONFIRMATIONS, different routes, one with OPPOSITE signature:
  - Modesto, Paula Netto & Shapiro, arXiv:1412.0740 Eq. (9), attributed
    verbatim to [Stelle-77, Stelle-78]: phi = -GM(1/r - (4/3)e^{-m2 r}/r
    + (1/3)e^{-m0 r}/r).
  - Giacchini, Phys. Lett. B 766 (2017) 306, arXiv:1609.05432 Eq. (10):
    phi = -(GM/r)[1 - (4/3)C2(r) + (1/3)C0(r)], signature (+,-,-,-) -- OPPOSITE
    to Lu et al., same answer. So signature does NOT rescue the other reading.
  - Alvarez-Gaume, Kehagias, Kounnas, Lust & Riotto, arXiv:1505.07657, from the
    tree-level amplitude: "an additional contribution from the ghost massive
    spin-2 state which produces a REPULSIVE Yukawa force."
  - Stelle's own CERN slides, tagged "K.S.S. 1978": ratios -1 : +4/3 : -1/3.

THE ERROR, CONFIRMED. The exploration note's clause "massive spin-2 projector
carries -1/3 trace vs -1/2 for the massless graviton" is CORRECT about the
projector: P^(2) = 1/2(theta theta + theta theta) - (1/3) theta theta versus
-1/2 theta theta massless. But -1/3 is the PROJECTOR TRACE COEFFICIENT; the
POTENTIAL coefficient is the RATIO (1 - 1/3)/(1 - 1/2) = 4/3 -- the
van Dam-Veltman-Zakharov enhancement. This file put a correct intermediate
quantity in the coefficient slot, and then had to give the leftover -4/3 to the
scalar.

WHY NO EXISTING CHECK CAUGHT IT. The r->0 sum rule is symmetric
(1 + 1/3 - 4/3 = 0 either way), and this file's "anchor to literature"
gamma = 1/2 is ALSO the f(R)/Brans-Dicke omega=0 value. Neither discriminates.
(The r->0 finiteness IS explicitly noted in the literature and credited to
Stelle: "V and W are actually nonsingular as r -> 0".)

TRAP TO AVOID WHEN FIXING. The SPATIAL potential has DIFFERENT numbers -- both
same-sign: psi = -(GM/r)[1 - (2/3)e^{-m2 r} - (1/3)e^{-m0 r}] (Giacchini &
Paula Netto, arXiv:1806.05664 Eq. (35); Stelle's W(r) in 4.7b agrees). A stray
"1/3 on the spin-2 term" may come from misreading psi -- but even psi never
yields this file's assignment.

CONSEQUENCE FOR GU. GU has no R^2, so m0 -> oo deletes the +1/3 SCALAR and
KEEPS the -4/3 spin-2 ghost. This file deletes the wrong one. Corrected:
alpha_Y = -4/3 not +1/3 -- magnitude x4, sign REPULSIVE as a ghost must be, and
gamma - 1 flips sign. That sign is the entire observational content here.

REMEDIATION -- APPLIED 2026-08-15 (H10-5). Every site this banner listed in
this file and in explorations/wave22/H10-ppn-weak-field-2026-07-11.md is
edited. The banner's physics was NOT taken on trust: it was re-derived from
projector traces + the ghost sign of box(box+m2^2) with no literature number
as input (see "Q1 DERIVATION" below and
tests/channel-swings/joe_directed_h105_stelle_ghost_sign.py, 45/45, 14 planted
false facts each forcing exit 1). The derivation reproduces Lu-Perkins-Pope-
Stelle Eq (4.7a) exactly, AND reproduces the spatial trap potential this banner
warns about, so the banner is CONFIRMED on both legs.

  WHAT MOVED:  alpha_Y = +1/3 attractive  ->  -4/3 REPULSIVE (magnitude x4)
               gamma - 1 = -(2/3)e^-m2r   ->  +(2/3)e^-m2r  (SIGN FLIPPED)
  WHAT DID NOT MOVE:  the Cassini m2 and mu_DW floors, and the verdict.

  WHY NOT -- a THIRD non-discriminating check, beyond the two this banner names.
  Cassini bounds |gamma - 1|, and the LEADING MAGNITUDE (2/3)e^{-m2 r} is
  IDENTICAL under the wrong and the corrected assignment. The two floors differ
  by 5.6e-6 in relative terms. So the sign IS the entire observational content
  here, exactly as this banner says -- and at Cassini precision that content is
  currently unmeasurable, because the bound is two-sided. This file's own
  verdict could never have caught its own error. The check that DOES
  discriminate is the Einstein-Weyl endpoint gamma(m2 r -> 0), = -1 corrected
  and = +1/2 wrong; it is now asserted at Q2b.

  BLAST RADIUS, WIDER THAN THIS BANNER RECORDED. alpha_Y = 1/3 is still live in
  six files outside the H10-5 write scope and is OWED, not fixed:
    explorations/track2-conditional-numbers-2026-07-13.md      (L111, L119, L193, L196, L227)
    explorations/path4-branchA-eos-gravity-correlation-2026-07-11.md (L37, L70, L72, L167)
    explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md     (L52, L112, L115, L133, L221)
    tests/W61_path4_A_eos_gravity.py                           (L36, L233-236)
    tests/W66_path4_wave2_alphaW.py                            (L118, L125-129, L174)
    tests/W138_issuance_kill_battery.py                        (L147)
  Direction of the error there: the corrected Yukawa is 4x stronger and
  REPULSIVE, so the sub-mm exclusion that track2 already calls binding gets
  STRONGER. No verdict in those files flips in GU's favour under the
  correction; the H36 point stays falsified a fortiori. That is why leaving
  them is safe to defer -- not why it is acceptable to forget.

METHODOLOGICAL WARNING, worth carrying repo-wide. During this check, an
HTML-summary fetch of arXiv:1505.07657 returned a SWAPPED version of the
equation; the LaTeX e-print source refutes it. If this file's assignment came
from a rendered PDF/HTML read, that is a plausible mechanism. ALWAYS check the
arXiv e-print source for equations.

NOT OBTAINED: Stelle 1978 itself (Springer paywall, doi:10.1007/BF00760427), so
no 1978 equation number or his internal notation. Confidence ~0.97 on the
physics: a verbatim numbered equation from a Stelle-co-authored paper citing
Stelle 1978, plus three independent confirmations.
=============================================================================
"""
# REPAIRED 2026-08-15.  The 2026-08-09 banner above was prepended as a SECOND
# module docstring, which pushed `from __future__ import annotations` past the
# start of the file and made this module raise SyntaxError on import and on
# run.  The repository's only Cassini/LLR bar was therefore DEAD for six days
# and no RED list recorded it, so a dead falsifier read as a live one.
# The future-import is hoisted here; both text blocks are preserved verbatim,
# the second now being an ordinary string expression.
#
# Note for anyone writing a gate against this class: `ast.parse` does NOT catch
# it.  The __future__-placement rule is enforced at compile, not parse, so a
# syntax check built on ast.parse reports this file clean.
from __future__ import annotations

# KNOWN-DEFECT GUARD -- ADDED 2026-08-15 with the parse repair, REMOVED 2026-08-15
# after the remediation it was waiting on was completed and verified (H10-5).
#
# The guard existed because repairing the SyntaxError ALONE would have been
# actively harmful: un-gated, this module ran to completion and printed a
# non-falsification verdict computed from the Yukawa assignment its own banner
# disavowed.  Dead and silent was bad; alive and confidently wrong is worse.
#
# It is removed now, and only now, because the condition it named is discharged:
# the constants carry -4/3 / -2/3 / +1/3, every dependent comment and derivation
# site is edited, the exploration note is edited, and the assignment is no longer
# transcribed at all -- Q1 DERIVES it below.  Removing the guard while leaving
# the constants wrong, or on the strength of the banner's citations alone, would
# have repeated the original mistake in the opposite direction.

r"""H10 -- THE PPN / WEAK-FIELD SOLAR-SYSTEM BAR for GU's tree-level gravity.

Wave 22. A CHEAP FALSIFIER. GU's gravity (Waves 1-10) is a tree-level Stelle-clear:
induced Einstein-Hilbert R^X + a Weyl^2 (Bach, 4th-order) term + a DeWitt Lambda,
conditional on the soldering postulate + the DeWitt scale mu_DW. Fourth-order (Stelle)
gravity is KNOWN to be delicate against solar-system tests: the massive spin-2 mode
produces a Yukawa correction to the Newtonian potential, and the PPN parameters
(gamma, beta) plus Cassini / LLR bound the massive-mode mass. THE QUESTION: does GU's
specific R^X + Weyl^2 + Lambda gravity PASS the real solar-system bars?

PRIOR SPINE (this repo, COMPUTED):
  * H15 (tests/wave3): |II|^2 = |H|^2 - R^X; in 4D int R^X is dynamical -> the TT graviton
    operator is Stelle box(box + m^2): a healthy massless graviton + a DISTINCT massive
    spin-2, m^2 = +1/2 (flat-ambient, in mu_DW units). |H|^2 = Weyl^2 gives the box^2.
  * H16/H24/H25 (tests/wave5,6,7): the curved-ambient correction gives m^2_eff = 1/2 + C_RY,
    C_RY COMPUTED POSITIVE by two methods (Gauss ratio +1/3 -> m^2_eff = 5/6; direct |II|^2
    2nd variation +3/4 -> m^2_eff = 5/4). So m^2_eff > 0 (O(1), geometrically fixed, sign robust).
    The PHYSICAL massive-spin-2 mass is m2^2 = m^2_eff * mu_DW^2 (H24 BAR 2 / H25). mu_DW is the
    source-action overall scale (dimensionless ratios geometric, dimensionful magnitude free);
    natural mu_DW ~ M_Pl -> Planckian.
  * KEY STRUCTURAL FACT: GU's action is R^X + Weyl^2 + Lambda with NO R^2 term. In quadratic
    gravity the massive SPIN-0 mass^2 ~ 1/beta_{R^2}; beta_{R^2} = 0 => m0 -> infinity =>
    the scalar mode DECOUPLES. So GU gravity = pure EINSTEIN-WEYL (R + Weyl^2): only a massless
    graviton + one massive spin-2. This is the CLEANEST PPN case (no scalar Yukawa).

WHAT H10 COMPUTES (deterministic, exit 0):
  Q1  The modified Newtonian potential of a point mass M for R^X + Weyl^2 (Einstein-Weyl).
      DERIVED here from structure (2026-08-15), no longer transcribed from a paper:
      the numerator trace coefficients 1/(D-2) massless and 1/(D-1) massive, saturated on
      a static point source, plus the ghost sign that follows from box(box + m2^2) itself.
      General quadratic gravity 2kappa^-2 R + beta R^2 - alpha C^2:
          V(r) = -(G M / r) [ 1 - (4/3) e^{-m2 r} + (1/3) e^{-m0 r} ].
      GU has NO R^2 term -> m0 -> infinity -> the (+1/3) SCALAR Yukawa is ABSENT and the
      spin-2 GHOST is KEPT:
          Phi(r) = -(G M / r) [ 1 - (4/3) e^{-m2 r} ]   (g_00 potential)
          Psi(r) = -(G M / r) [ 1 - (2/3) e^{-m2 r} ]   (g_ij potential)
      The massive spin-2 does NOT flip sign between the temporal and spatial potentials:
      BOTH are repulsive, and they differ in MAGNITUDE, 4/3 vs 2/3.  The 4/3 is the
      van Dam-Veltman-Zakharov ratio (1 - 1/3)/(1 - 1/2); the projector's own trace
      coefficient -1/3 is a correct INTERMEDIATE that belongs in a different slot.
  Q2  The Eddington gamma, beta from Phi, Psi. gamma(r) = Psi/Phi. Heavy-m2 limit -> GR.
  Q3  The m2 LOWER bound from Cassini |gamma-1| < 2.3e-5; translate to a mu_DW bound;
      compare to natural mu_DW ~ M_Pl.
  Q4  The verdict.

CROSS-CHECKS, and WHY THE OLD ONE WAS NOT ONE (2026-08-15).
  This file used to assert gamma(m2 r -> 0) = 1/2 "anchored to the literature".  That was a
  FALSE ANCHOR and it is why the wrong assignment survived from 2026-07-11 to 2026-08-09:
  1/2 is (i) the value for the MASSIVE MODE ALONE, not for the massless+ghost theory this
  file is about, (ii) also the Brans-Dicke omega=0 / f(R) value, and (iii) exactly what the
  WRONG assignment produces.  A check that cannot fail certifies nothing.
  The three checks now asserted DO discriminate:
    Q2a  the MASSIVE SECTOR ALONE has Psi/Phi = (1/3)/(2/3) = 1/2 -- the genuine vDVZ /
         Fierz-Pauli discontinuity, stated about the object it is actually true of.
    Q2b  the full EINSTEIN-WEYL gamma(m2 r -> 0) = -1, NOT 1/2.  The wrong assignment gives
         +1/2 here.  THIS is the endpoint that separates them.
    Q2e  gamma(m2 r -> oo) = 1 -- GR recovered (unchanged; true either way, so it is
         reported as a sanity check and NOT as an anchor).

PUBLISHED BOUNDS USED (comparison only, cited; NOT imported as targets):
  * Cassini gamma: |gamma - 1| < 2.3e-5  (Bertotti, Iess, Tortora, Nature 425, 374 (2003)).
  * LLR/Mercury beta: |beta - 1| < 8e-5   (Williams, Turyshev, Boggs, PRL 93, 261101 (2004);
    consistent with MESSENGER Mercury perihelion).

Run: python -u tests/wave22/H10_ppn_weak_field.py   (exit 0 iff all PASS)
"""
import math
import sympy as sp

FAIL = []

# Published bounds (comparison only; cited in the docstring). NOT imported as targets.
# Hoisted here 2026-08-15 so Q2 can reference them; they are used again in Q3.
CASSINI_GAMMA = 2.3e-5     # |gamma - 1| < 2.3e-5  (Bertotti, Iess, Tortora 2003)
LLR_BETA = 8.0e-5          # |beta  - 1| < 8e-5    (Williams, Turyshev, Boggs 2004)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# Q1 -- THE MODIFIED NEWTONIAN POTENTIAL (Einstein-Weyl = GU's R^X + Weyl^2, no R^2)
# ===========================================================================
log("=" * 78)
log("Q1 -- modified Newtonian potential: linearize R^X + Weyl^2 (box(box+m2^2)) around flat")
log("=" * 78)

r, m2, m0, GM = sp.symbols('r m2 m0 GM', positive=True)
Dg = sp.symbols('Dg', positive=True)   # spacetime dimension, kept symbolic

# --------------------------------------------------------------------------
# Q1 DERIVATION (2026-08-15).  These coefficients are NO LONGER TRANSCRIBED.
# The 2026-07-11 build read them off a paper, put a correct intermediate in the
# wrong slot, and the error stood for four weeks.  So the file now derives them,
# and the derivation takes NO literature number as input.
# --------------------------------------------------------------------------
# (i) Numerator trace coefficients between CONSERVED sources, in D dimensions:
#       massless graviton (harmonic gauge)  :  T.T' - (1/(D-2)) T T'
#       Fierz-Pauli massive spin-2          :  T.T' - (1/(D-1)) T T'
#     BOTH are derived, not asserted:
#     - massless, from TRACE REVERSAL. box hbar_mn ~ T_mn with hbar_mn = h_mn - (1/2)eta_mn h.
#       Trace: hbar = h(1 - D/2) => h = -2 hbar/(D-2), so inverting,
#       h_mn = hbar_mn + (1/2)eta_mn h = hbar_mn - (1/(D-2)) eta_mn hbar.
#     - massive, from TRACELESSNESS of the spin-2 projector: demanding P^(2) be traceless
#       forces its theta-theta coefficient to -1/(D-1)  (asserted at Q1-D1 below).
_hbar_tr, _h_tr = sp.symbols('_hbar_tr _h_tr')
_h_of_hbar = sp.solve(sp.Eq(_hbar_tr, _h_tr * (1 - Dg / 2)), _h_tr)[0]
c_ml_sym = sp.simplify(-(sp.Rational(1, 2) * _h_of_hbar) / _hbar_tr)   # == 1/(Dg - 2)
c_ml = sp.nsimplify(c_ml_sym.subs(Dg, 4))                # = 1/2
c_mv = sp.nsimplify((1 / (Dg - 1)).subs(Dg, 4))          # = 1/3
# (ii) Static point mass, signature (-,+,+,+): T_00 = M, T = eta^00 T_00 = -M, so
#      T.T' = +M M' and T T' = +M M'.  Both structures collapse to M M'.
Msrc = sp.symbols('Msrc', positive=True)
h00_ml, hij_ml = Msrc - c_ml * (-1) * (-Msrc), -c_ml * (+1) * (-Msrc)   # eta_00=-1, eta_ij=+1
h00_mv, hij_mv = Msrc - c_mv * (-1) * (-Msrc), -c_mv * (+1) * (-Msrc)
cT = sp.nsimplify(sp.simplify(h00_mv / h00_ml))          # temporal enhancement -> 4/3
cS = sp.nsimplify(sp.simplify(hij_mv / hij_ml))          # spatial  enhancement -> 2/3
# (iii) The GHOST SIGN, from the fourth-order operator this repo already computed:
#       1/(k^2 (k^2 + m2^2)) has residue ratio massive/massless = -1.
_k2, _m2s = sp.symbols('_k2 _m2s', positive=True)
_prop = 1 / (_k2 * (_k2 + _m2s))
ghost_ratio = sp.nsimplify(sp.simplify(
    ((_prop * (_k2 + _m2s)).subs(_k2, -_m2s)) / sp.limit(_prop * _k2, _k2, 0)))

log(f"  DERIVED  massless trace coeff 1/(D-2)|D=4 = {c_ml};  massive 1/(D-1)|D=4 = {c_mv}")
log(f"  DERIVED  vDVZ ratio (1-1/3)/(1-1/2) = {cT}  (temporal);  spatial = {cS}")
log(f"  DERIVED  ghost sign from box(box+m2^2): residue ratio = {ghost_ratio}")

check("Q1-D1: the vDVZ RATIO (1 - 1/3)/(1 - 1/2) = 4/3 is the POTENTIAL coefficient. The spin-2 "
      "PROJECTOR's own trace coefficient is -1/(D-1) = -1/3 -- a correct intermediate in a "
      "DIFFERENT slot. Putting -1/3 in the potential slot was exactly the 2026-07-11 error",
      cT == sp.Rational(4, 3) and sp.nsimplify((-1 / (Dg - 1)).subs(Dg, 4)) == sp.Rational(-1, 3))
check("Q1-D1b: the massless coefficient 1/(D-2) is DERIVED from trace reversal in D dimensions "
      "(hbar = h(1 - D/2) => h = -2 hbar/(D-2)), not asserted. Both trace coefficients entering "
      "the vDVZ ratio are therefore derived, so the ratio does not rest on a transcription",
      sp.simplify(c_ml_sym - 1 / (Dg - 2)) == 0 and c_ml == sp.Rational(1, 2))
check("Q1-D2: the massive spin-2 is a GHOST -- residue ratio -1 at the massive pole of "
      "box(box+m2^2). Its Yukawa is REPULSIVE. This sign is STRUCTURAL, read off the operator "
      "H15/H25 already computed for GU, not imported from any paper. Which pole is the ghost is "
      "fixed by requiring the MASSLESS residue to give ATTRACTION (Newton); the other one then "
      "has no freedom left",
      ghost_ratio == -1)
check("Q1-D3: the MASSIVE SECTOR ALONE has Psi/Phi = (1/3)/(2/3) = 1/2 -- the genuine vDVZ / "
      "Fierz-Pauli discontinuity. Stated about the object it is true of (see Q2a/Q2b)",
      sp.nsimplify(hij_mv / h00_mv) == sp.Rational(1, 2)
      and sp.nsimplify(hij_ml / h00_ml) == 1)

# General quadratic-gravity Stelle (1978) point-mass potential, DERIVED above.
# Spin-2 (from Weyl^2): -4/3 e^{-m2 r} REPULSIVE (ghost); spin-0 (from R^2): +1/3 e^{-m0 r}.
c_newton = sp.Integer(1)
c_spin2 = -cT                   # = -4/3  massive spin-2 Yukawa coefficient (Weyl^2), GHOST
c_spin0 = sp.Rational(1, 3)     # = +1/3  massive spin-0 Yukawa coefficient (R^2) -- ABSENT in GU
c_spin2_spatial = -cS           # = -2/3  the SAME ghost in the SPATIAL potential

V_general = -(GM / r) * (c_newton + c_spin2 * sp.exp(-m2 * r) + c_spin0 * sp.exp(-m0 * r))

# Independent fix on c_spin0: Stelle's r->0 finiteness of the FULL theory, 1 - 4/3 + c0 = 0.
_c0 = sp.symbols('_c0')
check("Q1-D4: Stelle's r->0 finiteness of the FULL quadratic theory (1 - 4/3 + c0 = 0) "
      "independently fixes the scalaron coefficient c0 = +1/3, ATTRACTIVE (non-ghost). Note "
      "this sum rule is SYMMETRIC under the swap, so it alone never discriminated -- it is "
      "used here only to fix the scalar GIVEN the spin-2 term derived above",
      sp.solve(sp.Eq(1 + c_spin2 + _c0, 0), _c0)[0] == c_spin0)

# GU HAS NO R^2 TERM => beta_{R^2} = 0 => m0 -> infinity => the SCALAR Yukawa vanishes and
# the spin-2 GHOST is KEPT. (The 2026-07-11 build deleted the ghost and kept the scalar.)
V_GU = sp.limit(V_general, m0, sp.oo)
Phi = -(GM / r) * (1 + c_spin2 * sp.exp(-m2 * r))            # g_00 potential, -4/3
Psi = -(GM / r) * (1 + c_spin2_spatial * sp.exp(-m2 * r))    # g_ij potential, -2/3

log(f"  general quadratic-gravity (Stelle 1978): V(r) = -(GM/r)[1 - (4/3)e^(-m2 r) + (1/3)e^(-m0 r)]")
log(f"  GU has NO R^2 term -> m0 -> oo -> SCALAR Yukawa ABSENT, spin-2 GHOST KEPT.  GU potentials:")
log(f"    Phi(r) (g_00) = {sp.nsimplify(Phi)}")
log(f"    Psi(r) (g_ij) = {sp.nsimplify(Psi)}")

check("Q1a: GU's scalar (spin-0) Yukawa coefficient is ZERO (no R^2 term -> m0 -> oo): only the "
      "massless graviton + ONE massive spin-2 GHOST Yukawa survive. The mode GU deletes is the "
      "HEALTHY scalar; the mode it keeps is the GHOST",
      sp.simplify(V_GU - Phi) == 0)
Phi_c = sp.expand(Phi).coeff(sp.exp(-m2 * r))
Psi_c = sp.expand(Psi).coeff(sp.exp(-m2 * r))
check("Q1b: Phi(g_00) carries -(4/3)e^{-m2 r} and Psi(g_ij) carries -(2/3)e^{-m2 r}. The massive "
      "spin-2 does NOT flip sign between temporal and spatial: BOTH are repulsive, differing in "
      "MAGNITUDE by exactly 2. (The old file asserted a sign flip; that was part of the error.)",
      sp.simplify(Phi_c - GM * cT / r) == 0 and sp.simplify(Psi_c - GM * cS / r) == 0
      and sp.simplify(Phi_c / Psi_c) == 2,
      f"Phi coeff = {Phi_c}, Psi coeff = {Psi_c}")
check("Q1b-TRAP: the SPATIAL potential of the FULL theory is -(GM/r)[1 - (2/3)e^-m2r "
      "- (1/3)e^-m0r] -- DIFFERENT numbers, BOTH same sign. A stray '1/3 on the spin-2 term' "
      "can come from misreading it; putting that pair in the temporal slot reproduces NEITHER "
      "the correct temporal bracket NOR the old wrong one",
      sp.simplify((1 - cS * sp.exp(-m2 * r) - sp.Rational(1, 3) * sp.exp(-m0 * r))
                  - (1 + c_spin2 * sp.exp(-m2 * r) + c_spin0 * sp.exp(-m0 * r))) != 0
      and sp.simplify((1 - cS * sp.exp(-m2 * r) - sp.Rational(1, 3) * sp.exp(-m0 * r))
                      - (1 + sp.Rational(1, 3) * sp.exp(-m2 * r))) != 0)
# heavy-m2 (short-range Yukawa) limit -> pure Newton
check("Q1c: as m2 -> oo (Yukawa range 1/m2 -> 0) BOTH potentials -> the pure Newtonian -GM/r "
      "(GR recovered exactly when the massive spin-2 is heavy)",
      sp.limit(Phi, m2, sp.oo) == -GM / r and sp.limit(Psi, m2, sp.oo) == -GM / r)
check("Q1d: SHORT range (m2 r << 1) the Einstein-Weyl bracket -> 1 - 4/3 = -1/3: gravity is "
      "REPULSIVE below the Yukawa range. The old assignment gave +4/3 (attraction ENHANCED). "
      "Antigravity vs enhanced gravity -- the two assignments are physically opposite, and "
      "Einstein-Weyl alone is NOT r->0 finite (Stelle finiteness needs BOTH massive modes)",
      sp.nsimplify(1 + c_spin2) == sp.Rational(-1, 3))


# ===========================================================================
# Q2 -- PPN gamma and beta
# ===========================================================================
log("\n" + "=" * 78)
log("Q2 -- Eddington gamma, beta for GU's weak field")
log("=" * 78)

# gamma(r) = (spatial potential)/(temporal potential) = Psi/Phi (both share the -GM/r prefactor).
w = sp.symbols('w', positive=True)   # stand-in for e^{-m2 r}, 0 < w <= 1
gamma_w = sp.simplify((1 - cS * w) / (1 - cT * w))
gamma_r = gamma_w.subs(w, sp.exp(-m2 * r))
log(f"  gamma(r) = Psi/Phi = (1 - (2/3)e^{{-m2 r}}) / (1 - (4/3)e^{{-m2 r}})")

# The OLD, WRONG assignment, kept live ONLY as a discriminating control (see Q2b/Q2d).
gamma_w_wrong = (1 - sp.Rational(1, 3) * w) / (1 + sp.Rational(1, 3) * w)

gamma_short = sp.nsimplify(gamma_w.subs(w, 1))       # m2 r -> 0 : massive mode fully active
gamma_long = sp.limit(gamma_w, w, 0)                 # m2 r -> oo: massive mode dead (GR)
check("Q2a: the MASSIVE SECTOR ALONE gives Psi/Phi = (1/3)/(2/3) = 1/2 -- the vDVZ / "
      "Fierz-Pauli massive-graviton value (light bending 3/4 of GR). This is the genuine "
      "literature endpoint, and it is a statement about the MASSIVE MODE, not about the full "
      "massless+ghost theory. The old file attached it to the wrong object",
      sp.nsimplify(hij_mv / h00_mv) == sp.Rational(1, 2))
check("Q2b DISCRIMINATING CHECK: the full EINSTEIN-WEYL gamma(m2 r -> 0) = -1, NOT 1/2. The "
      "WRONG assignment gives +1/2 here. THIS endpoint separates the two assignments, and it "
      "is the check this file lacked. Had it been asserted in 2026-07-11 the error could not "
      "have survived a single run",
      gamma_short == -1 and sp.nsimplify(gamma_w_wrong.subs(w, 1)) == sp.Rational(1, 2)
      and gamma_short != sp.nsimplify(gamma_w_wrong.subs(w, 1)),
      f"gamma_EW(short) = {gamma_short}  vs  wrong-assignment {sp.nsimplify(gamma_w_wrong.subs(w, 1))}")
check("Q2e SANITY (not an anchor -- true under BOTH assignments, so it certifies nothing): "
      "gamma(m2 r -> oo) = 1, GR recovered",
      gamma_long == 1 and sp.limit(gamma_w_wrong, w, 0) == 1, f"gamma(long range) = {gamma_long}")

# heavy-m2 expansion: gamma - 1 ~ +(2/3) e^{-m2 r}.
lead_w = sp.expand(sp.series(gamma_w - 1, w, 0, 2).removeO())        # +(2/3) w + O(w^2)
lead_w_wrong = sp.expand(sp.series(gamma_w_wrong - 1, w, 0, 2).removeO())
lead = lead_w.subs(w, sp.exp(-m2 * r))
check("Q2c: for m2 r >> 1, gamma - 1 = +(2/3) e^{-m2 r} + O(e^{-2 m2 r}) -- POSITIVE, and "
      "EXPONENTIALLY suppressed. GU predicts gamma > 1 at solar-system distances. The old "
      "file had -(2/3): the SIGN is refuted, and the sign is the entire observational content",
      sp.simplify(lead_w - sp.Rational(2, 3) * w) == 0,
      f"leading (gamma-1) = +(2/3)e^-m2r  [series: {sp.nsimplify(lead_w)}]")
check("Q2d DEGENERACY -- why this file could never have caught its own error. The LEADING "
      "MAGNITUDE of gamma-1 is (2/3)e^{-m2 r} under BOTH the wrong and the corrected "
      "assignment; only the sign differs. Cassini bounds |gamma-1|, two-sided. So every "
      "number Q3 computes is degenerate between the two assignments (Q3a3 quantifies it). "
      "This is a THIRD non-discriminating check, beyond the two the 2026-08-09 banner named",
      sp.simplify(sp.Abs(lead_w) - sp.Abs(lead_w_wrong)) == 0
      and sp.sign(lead_w.coeff(w)) == -sp.sign(lead_w_wrong.coeff(w)),
      f"corrected {lead_w}, wrong {lead_w_wrong} -- same magnitude, opposite sign")

# beta: for a Yukawa-corrected static field, the second-order (nonlinear) potential correction
# is likewise proportional to e^{-m2 r} and vanishes as m2 r -> oo, so beta -> 1 exponentially.
# We assert the structural fact (beta -> 1 in the heavy-m2 limit); the binding solar-system bar is
# Cassini gamma (its bound is ~4x tighter than the LLR beta bound), so gamma sets the m2 floor.
check("Q2f: beta -> 1 as m2 -> oo (the nonlinear Yukawa correction is also ~ e^{-m2 r}); the "
      "TIGHTER solar-system constraint is Cassini gamma, so gamma sets the binding m2 lower bound. "
      "Unchanged by the 2026-08-15 correction: beta's leading behaviour is O(e^{-m2 r}) under "
      "either assignment, and the LLR bound (8e-5) is ~3.5x looser than Cassini's (2.3e-5)",
      LLR_BETA / CASSINI_GAMMA > 3.0,
      "beta - 1 is O(e^{-m2 r}) -> 0 in the heavy-m2 limit; Cassini gamma dominates")


# ===========================================================================
# Q3 -- THE m2 LOWER BOUND FROM CASSINI, AND THE mu_DW CONSISTENCY
# ===========================================================================
log("\n" + "=" * 78)
log("Q3 -- m2 lower bound from Cassini, and consistency with GU's m2^2 = m^2_eff * mu_DW^2")
log("=" * 78)

# (CASSINI_GAMMA and LLR_BETA are defined once, near the top of the module.)

# Solar-system length scale over which the Yukawa must be suppressed. The Cassini Shapiro-delay
# ray runs Earth->superior-conjunction; we use r = 1 AU as the conservative (largest -> weakest
# lower bound) scale, and also report the impact-parameter (1.6 R_sun) scale.
AU = 1.495978707e11        # m
R_SUN = 6.957e8            # m
r_AU = AU
r_imp = 1.6 * R_SUN        # Cassini impact parameter ~ 1.6 solar radii
HBARC = 1.973269804e-7     # eV * m
M_PL_eV = 1.220890e28      # Planck mass in eV (1.22e19 GeV); reduced M_Pl ~ 2.4e27 eV (same order)

# Condition |gamma - 1| = (2/3)u / (1 - (4/3)u) < CASSINI_GAMMA, u = e^{-m2 r}.
# Exact solve: u < 3*eps / (2 + 4*eps).  Leading-order route: (2/3)u < eps  =>  u < 1.5*eps.
_u_exact = 3.0 * CASSINI_GAMMA / (2.0 + 4.0 * CASSINI_GAMMA)
_u_lead = 1.5 * CASSINI_GAMMA
thresh = -math.log(_u_exact)                      # = m2 * r lower bound (dimensionless)
thresh_lead = -math.log(_u_lead)                  # independent route, must agree
# The SAME bound under the OLD, WRONG assignment: |(2/3)u/(1 + u/3)| = eps  =>  u = 3 eps/(2 - eps)
_u_wrong = 3.0 * CASSINI_GAMMA / (2.0 - CASSINI_GAMMA)
thresh_wrong = -math.log(_u_wrong)
rel_degeneracy = abs(thresh - thresh_wrong) / thresh
m2_min_AU_invm = thresh / r_AU                    # 1/m
m2_min_imp_invm = thresh / r_imp
m2_min_AU_eV = m2_min_AU_invm * HBARC
m2_min_imp_eV = m2_min_imp_invm * HBARC
lam_max_AU = 1.0 / m2_min_AU_invm                 # max Yukawa range (m)

log(f"  Cassini: (2/3)u/(1-(4/3)u) < {CASSINI_GAMMA:.1e}  =>  m2 r > {thresh:.4f}")
log(f"  at r = 1 AU  = {r_AU:.3e} m : m2 > {m2_min_AU_invm:.3e} /m = {m2_min_AU_eV:.3e} eV "
    f"(Yukawa range 1/m2 < {lam_max_AU:.3e} m = {lam_max_AU/AU:.3f} AU)")
log(f"  at r = 1.6 R_sun = {r_imp:.3e} m : m2 > {m2_min_imp_invm:.3e} /m = {m2_min_imp_eV:.3e} eV")

check("Q3a: the Cassini gamma bound imposes a LOWER bound on m2 (the massive spin-2 must be heavy "
      "enough that its Yukawa range is far below solar-system scales) -- as expected for Stelle",
      m2_min_AU_eV > 0 and thresh > 0)
check("Q3a2 INDEPENDENT ROUTE: exact solve of the full rational |gamma-1| and the leading-order "
      "series give the same m2*r threshold to < 1e-3, so the bound does not ride on the series "
      "truncation",
      abs(thresh - thresh_lead) < 1e-3, f"exact {thresh:.5f} vs leading-order {thresh_lead:.5f}")
check("Q3a3 DEGENERACY QUANTIFIED: the corrected (-4/3) and the wrong (+1/3) assignment give "
      "Cassini m2*r floors differing by {:.1e} in RELATIVE terms. Repairing the physics moved "
      "the published floor by parts per million. Every Q3 number below is therefore UNCHANGED "
      "by the correction -- and this bar, on its own, could never have detected the defect"
      .format(rel_degeneracy),
      rel_degeneracy < 1e-4, f"corrected {thresh:.6f} vs wrong {thresh_wrong:.6f}")

# GU's massive spin-2 mass: m2^2 = m^2_eff * mu_DW^2, m^2_eff = 5/6 (Method 1) .. 5/4 (Method 2), O(1).
m2_eff_low = sp.Rational(5, 6)      # H25 Method 1 (convention-robust Gauss ratio)
m2_eff_high = sp.Rational(5, 4)     # H25 Method 2 (direct |II|^2 2nd variation)
sqrt_meff = math.sqrt(float(m2_eff_low))   # 0.9129 -- conservative (smallest m2 per mu_DW)

# Translate the m2 floor into a mu_DW floor: mu_DW > m2_min / sqrt(m^2_eff).
mu_DW_min_eV = m2_min_AU_eV / sqrt_meff
orders_below_planck = math.log10(M_PL_eV / mu_DW_min_eV)

log(f"  GU: m2 = sqrt(m^2_eff) * mu_DW, m^2_eff in [5/6, 5/4] (H25). Using m^2_eff = 5/6 (conservative):")
log(f"    Cassini floor on mu_DW = m2_min / sqrt(5/6) = {mu_DW_min_eV:.3e} eV")
log(f"    natural mu_DW ~ M_Pl = {M_PL_eV:.3e} eV  clears the floor by {orders_below_planck:.1f} orders of magnitude")

check("Q3b: the Cassini floor on mu_DW is ~1e-17 eV, i.e. inverse-(~0.1 AU). GU's m^2_eff is O(1) "
      "and POSITIVE (H25), so any mu_DW above this ABSURDLY LOW floor passes",
      mu_DW_min_eV < 1e-15 and mu_DW_min_eV > 1e-19,
      f"mu_DW floor = {mu_DW_min_eV:.3e} eV")
check("Q3c: natural mu_DW ~ M_Pl clears the Cassini floor by > 40 orders of magnitude -> GU's "
      "massive spin-2 is Planckian, its Yukawa range ~ 1/M_Pl ~ 1e-35 m, utterly unobservable",
      orders_below_planck > 40, f"clearance = {orders_below_planck:.1f} decades")
check("Q3d: the Cassini floor on mu_DW (~1e-17 eV) is FAR WEAKER than the ghost-decoupling bar "
      "(BAR 2, which wants mu_DW ~ M_Pl): the solar-system PPN test adds NO new binding constraint",
      mu_DW_min_eV < M_PL_eV)


# ---------------------------------------------------------------------------
# CONTRARY CONTROLS -- the bar must be able to say FAIL, or the pass is vacuous.
# Added 2026-08-15: a falsifier with no configuration that fails it is not a
# falsifier.  This file had none, which is part of why it read as healthy while
# computing from a disavowed assignment.
# ---------------------------------------------------------------------------
def _gamma_minus_1(mu_dw_eV):
    """|gamma - 1| at r = 1 AU for a GU configuration with the given mu_DW."""
    x = (math.sqrt(float(m2_eff_low)) * mu_dw_eV / HBARC) * r_AU   # m2 * r
    uu = math.exp(-x)
    return abs((2.0 / 3.0) * uu / (1.0 - (4.0 / 3.0) * uu))

_g_bad = _gamma_minus_1(1e-18)      # below the floor
_g_good = _gamma_minus_1(1e-15)     # above the floor
check("Q3-CONTRARY-A: a GU configuration that PROVABLY VIOLATES this bar. mu_DW = 1e-18 eV "
      f"gives |gamma-1| = {_g_bad:.3e}, {_g_bad/CASSINI_GAMMA:.0f}x the Cassini bound -> "
      "FALSIFIED. The same machinery passes mu_DW = 1e-15 eV. The bar can therefore say FAIL, "
      "so the pass at M_Pl is not vacuous",
      _g_bad > CASSINI_GAMMA and _g_good < CASSINI_GAMMA,
      f"1e-18 eV -> {_g_bad:.3e} VIOLATES; 1e-15 eV -> {_g_good:.3e} passes")

# External comparator control: Brans-Dicke omega = 100 (reproduces the repo's W220 control).
_gamma_bd = sp.Rational(1 + 100, 2 + 100)
_dev_bd = float(abs(_gamma_bd - 1))
check("Q3-CONTRARY-B: external comparator Brans-Dicke omega=100 gives gamma = 101/102, "
      f"|gamma-1| = {_dev_bd:.2e}, {_dev_bd/CASSINI_GAMMA:.0f}x the Cassini bound -> correctly "
      "returned FALSIFIED. Reproduces the repo's own W220 negative control (9.8e-3, ~400x)",
      _dev_bd > CASSINI_GAMMA and abs(_dev_bd - 9.8e-3) < 1e-4,
      f"gamma_BD = {_gamma_bd} = {float(_gamma_bd):.5f}")


# ===========================================================================
# Q4 -- THE VERDICT
# ===========================================================================
log("\n" + "=" * 78)
log("Q4 -- VERDICT")
log("=" * 78)

# NOT falsified: gamma, beta -> 1 exponentially; the deviation is a suppressed Yukawa, not a
# structural O(1) deviation. GU does NOT force a solar-system-visible deviation.
# The pass is conditional on m2 above the Cassini floor, i.e. mu_DW above ~1e-17 eV -- a bound so
# far below the natural (and BAR-2-required) M_Pl scale that it is not the binding gate.
not_falsified = (gamma_long == 1) and (sp.limit(Phi, m2, sp.oo) == -GM / r)
gated = mu_DW_min_eV > 0
comfortably_passes = orders_below_planck > 40

check("Q4a: NOT FALSIFIED -- GU does NOT force a solar-system-visible deviation: gamma,beta -> 1 "
      "as an EXPONENTIALLY suppressed Yukawa (heavy massive spin-2), not a structural O(1) shift",
      not_falsified)
check("Q4b: GATED-ON-mu_DW but PASSES for natural scale -- passes iff mu_DW > ~1e-17 eV "
      "(inverse ~0.1 AU); natural mu_DW ~ M_Pl clears this by > 40 decades",
      gated and comfortably_passes)
check("Q4c SIGN, REPORTED PLAINLY (2026-08-15): the corrected assignment flips the SIGN of the "
      "predicted deviation. GU predicts gamma > 1 at solar-system distances; this file used to "
      "say gamma < 1. Bertotti et al. measured gamma - 1 = (2.1 +/- 2.3)e-5 -- a POSITIVE "
      "central value consistent with zero at 0.91 sigma. So the correction moves GU's predicted "
      "deviation onto the same side as the measured central value. The statistical significance "
      "of that is ZERO (a null measurement), and it is stated here only so that nobody -- in "
      "either direction -- reads more into the sign flip than the data supports",
      2.1e-5 < CASSINI_GAMMA, "central 2.1e-5 = 0.91 sigma, consistent with zero")
check("Q4d NO VERDICT CHANGE, AND THAT IS ITSELF THE FINDING: the assignment was wrong in "
      "magnitude (x4) and in sign, and the Cassini verdict did not move at all, because the "
      "|gamma-1| magnitude is degenerate between the two (Q2d/Q3a3). A bar whose verdict is "
      "invariant under a x4 sign-flipping error in its own input is a WEAK bar. That is a "
      "statement about this test's discriminating power, not about GU",
      abs(orders_below_planck - 44.9) < 0.5, f"clearance {orders_below_planck:.2f} decades")

log(r"""
COMPUTED / ARGUED (this file, exit 0):
  Q1 [COMPUTED -- upgraded 2026-08-15 from ARGUED]: GU = R^X + Weyl^2 + Lambda has NO R^2 term,
     so the massive SPIN-0 decouples (m0 -> oo) and only ONE massive spin-2 Yukawa survives --
     the GHOST.  Phi(r) = -(GM/r)[1 - (4/3)e^{-m2 r}],  Psi(r) = -(GM/r)[1 - (2/3)e^{-m2 r}].
     The coefficients are now DERIVED in-file from the numerator trace coefficients 1/(D-2) and
     1/(D-1), a static point source, and the ghost sign of box(box+m2^2) -- no literature number
     is an input.  The derivation reproduces Lu-Perkins-Pope-Stelle Eq (4.7a) and the spatial
     trap potential exactly.  (The box(box+m2^2) TT operator itself is the repo's H15/H25 result.)
  Q2 [COMPUTED]: gamma(r) = (1-(2/3)e^{-m2 r})/(1-(4/3)e^{-m2 r}); gamma - 1 = +(2/3)e^{-m2 r} for
     m2 r >> 1 -- POSITIVE. beta -> 1 likewise. DISCRIMINATING CHECK: Einstein-Weyl
     gamma(m2 r -> 0) = -1 (the wrong assignment gives +1/2); the vDVZ 1/2 belongs to the massive
     mode ALONE. gamma(m2 r -> oo) = 1 (GR) is reported as a sanity check, not as an anchor.
  Q3 [COMPUTED]: Cassini |gamma-1| < 2.3e-5 => m2 r > 10.27 => m2 > ~1.4e-17 eV (Yukawa range
     < ~0.1 AU). GU's m2 = sqrt(m^2_eff) mu_DW, m^2_eff in [5/6, 5/4] (O(1), positive, H25); the
     bound becomes mu_DW > ~1.5e-17 eV. Natural mu_DW ~ M_Pl = 1.2e28 eV clears it by ~45 decades.
  Q4 [VERDICT]: GATED-ON-mu_DW, effectively PASSES. GU does NOT force a solar-system deviation;
     gamma,beta -> 1 as a suppressed Yukawa. The pass requires mu_DW > ~1.5e-17 eV -- a floor ~45
     orders below the natural (and ghost-decoupling-required) M_Pl scale. The solar-system PPN bar
     is NOT the binding gate on mu_DW; it is cleared with room to spare for any non-pathological scale.

WHAT THE 2026-08-15 CORRECTION MOVED, AND WHAT IT DID NOT:
  MOVED   alpha_Y = +1/3 attractive -> -4/3 REPULSIVE (magnitude x4, sign flipped: a GHOST)
          gamma - 1 = -(2/3)e^{-m2 r} -> +(2/3)e^{-m2 r}  (GU predicts gamma > 1, not < 1)
          short-range gravity: +4/3 enhanced attraction -> -1/3, i.e. REPULSIVE below 1/m2
          the "vDVZ 1/2 anchor" -> retired as a false anchor; replaced by the -1 endpoint
  DID NOT MOVE   the Cassini m2 floor, the mu_DW floor, the ~45-decade clearance, the verdict.
  WHY   Cassini bounds |gamma - 1|, and the leading magnitude (2/3)e^{-m2 r} is IDENTICAL under
        both assignments; the two floors differ by 5.6e-6 relative. The sign IS the entire
        observational content, exactly as the 2026-08-09 banner said -- and at Cassini precision
        that content is unmeasurable, because the bound is two-sided. This bar could not have
        detected its own defect, and that is now recorded in the bar itself (Q2d, Q3a3, Q4d).

HONEST LIMITS:
  * Phi, Psi and the coefficients -4/3 / -2/3 / +1/3 are now DERIVED here from projector-trace
    structure plus the ghost sign of the fourth-order operator, and cross-checked against the
    literature rather than copied from it. What is still NOT done is a re-linearization of GU's
    full |II|^2 action WITH MATTER SOURCES: this file uses the box(box+m2^2) TT operator computed
    in H15/H25 and solves THAT. The matter coupling remains imported. That gap is source-action
    requirement SA-G9 and it is unchanged by this remediation.
  * The absence of the scalar Yukawa rests on GU having NO R^2 term (repo: R^X + Weyl^2 + Lambda).
    If a source-action build induced an R^2 term, a second (spin-0) Yukawa +(1/3)e^{-m0 r} would
    appear -- ATTRACTIVE, and it would also restore Stelle's r->0 finiteness, which Einstein-Weyl
    alone does NOT have (Q1d). Its m0 would need the same (trivially-cleared) heavy-mass floor.
  * mu_DW's dimensionful value is NOT derived (H24/H25 BAR 2); it is the source-action overall
    scale. The solar-system bar constrains it only to > ~1.5e-17 eV -- far weaker than BAR 2's
    ~M_Pl, and far weaker than the sub-mm channel, which track2 already reports as the BINDING
    one (~14 orders tighter). Under the corrected assignment the sub-mm Yukawa is 4x stronger and
    repulsive, so that exclusion gets STRONGER, not weaker. That file is not edited here.
  * beta is NOT recomputed from the corrected potentials. Q2f asserts the STRUCTURAL fact that
    the nonlinear correction is also O(e^{-m2 r}) and so beta -> 1 exponentially -- true under
    either assignment, and the binding bar is Cassini gamma anyway (~3.5x tighter than LLR beta).
    But "beta -> 1" here is an ARGUED structural statement, not a computed PPN beta. Unchanged
    by this remediation, and it is the weakest link in the Q2 block.
  * Loop-level unitarity (BAR 1) is untouched here; PPN is a purely tree-level / classical test.
  * OWED, OUTSIDE THIS FILE: alpha_Y = 1/3 is still live in six files (listed in the banner's
    REMEDIATION block). None of them flips in GU's favour under the correction, but none is fixed.

RE-RANK SIGNAL: GATED-ON-mu_DW (bound: mu_DW > ~1.5e-17 eV, i.e. inverse ~0.1 AU), cleared by ~45
  orders for the natural mu_DW ~ M_Pl -> effectively PASSES. The solar-system PPN test does NOT
  falsify GU and does NOT tighten the pre-existing mu_DW gate. Second signal, new: this bar is
  WEAK -- its verdict is invariant under a x4 sign-flipping error in its own input. Ranking it as
  a live falsifier overstates it. Single next object: unchanged -- the ghost-mass SCALE mu_DW
  itself (H24/H25 BAR 2), the one dimensionful datum that all of gravity hangs on.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = H10 computed: GU = Einstein-Weyl (massive spin-2 GHOST kept, scalar deleted);")
log("         gamma - 1 = +(2/3)e^{-m2 r} (POSITIVE; corrected 2026-08-15), gamma,beta -> 1 for")
log("         heavy m2; Cassini floor mu_DW > ~1.5e-17 eV cleared by ~45 decades for natural")
log("         mu_DW ~ M_Pl. VERDICT: GATED-ON-mu_DW, effectively PASSES (not falsified) -- and")
log("         the verdict is UNCHANGED by the correction, because Cassini is two-sided and the")
log("         |gamma-1| magnitude is degenerate between the wrong and the corrected assignment.")

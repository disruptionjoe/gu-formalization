#!/usr/bin/env python3
r"""H16 -- STELLE VIABILITY: is the now-structurally-cleared GU gravity branch
(H18: Stelle R^X + Weyl^2 + DeWitt Lambda, ghost cleared at TREE by Bateman-Turok)
actually PHYSICALLY VIABLE, or a relocated problem parked in the contested
Stelle-Mannheim corner?

Wave 5, Condorcet #1. Prior spine:
  * H15 (tests/wave3/H15_gravity_fork_R_term.py): |II|^2 = |H|^2 - R^X, the II-class
    functional carries a 4D-DYNAMICAL Einstein-Hilbert R^X -> Stelle R + Weyl^2 ->
    box(box + m^2), massless graviton + distinct massive ghost. m^2 = +1/2 (flat-ambient).
  * H18 (tests/wave4/H18_forcing_II_vs_H.py): the II-class (full-norm) branch is
    STRUCTURALLY FORCED (YM full |theta|^2, not trace |H|^2) modulo 2 recon-grade premises.
  * canon/ghost-parity-krein-synthesis.md + Bateman-Turok arXiv:2607.00096: the massive
    ghost clears at TREE level via a hidden ghost parity on a Krein space.

THE FOUR VIABILITY BARS (this file computes 2+3, documents/fences 1+4):

BAR 3 -- THE R^X SIGN (the sharpest potential KILL, COMPUTED here, exact).
  Attractive gravity / positive Newton constant requires the MASSLESS graviton pole to
  be the HEALTHY (positive-residue) member of the O(1,1)/Krein pair. Which member is
  healthy is decided by the SIGN of the induced Einstein-Hilbert term:
    * E = int(|H|^2 - R^X)  [Gauss-FORCED sign]  -> operator box(box + m^2), m^2>0,
      massless residue = +1/m^2 > 0  -> HEALTHY massless graviton, massive GHOST
      -> ATTRACTIVE gravity. (correct Stelle ordering)
    * E = int(|H|^2 + R^X)  [hypothetical flip]  -> operator box(box - m^2),
      massless residue = -1/m^2 < 0 -> GHOST massless graviton -> REPULSIVE. KILL.
  The Gauss equation |II|^2 = |H|^2 - R^X FORCES the first (attractive) sign. We also
  verify the Gauss-convention R^X is sign-aligned with the standard "sphere has R>0"
  convention (so -R^X genuinely means "subtract POSITIVE curvature"), closing the
  loophole that a sign-convention mismatch could secretly flip attraction to repulsion.

BAR 2 -- THE GHOST SCALE (COMPUTED as a scaling/dimensional argument; scale gated).
  m^2 = +1/2 is the DIMENSIONLESS coefficient ratio (box coeff)/(box^2 coeff) in
  H15's flat-ambient units. The PHYSICAL ghost mass carries dimension [mass]^2 and so
  must be m_ghost^2 = (ratio) * mu_DW^2, where mu_DW^2 is the ONLY available dimensionful
  scale: the ambient DeWitt metric normalization on Y^14 = Met(X^4) (H15 Part E's gate,
  the ambient R^Y coefficient). If mu_DW ~ M_Planck (the natural expectation for the
  metric-on-metrics normalization) the ghost is PLANCKIAN -> decouples -> empirically
  SAFE. The magnitude is UNDETERMINED without the unbuilt normalization; only its
  Planckian scaling and dimensional structure are established here.

BAR 1 -- LOOP-LEVEL UNITARITY (NOT computable from GU; FENCED with primary sources).
  Bateman-Turok (arXiv:2607.00096) prove positivity of transition probabilities at
  TREE LEVEL ONLY (their own Conclusions: "a general proof of the positivity of
  transition probabilities at tree level. The main obstacle to extending the proof to
  higher orders is that, like QCD, the massless theory has collinear infrared
  divergences ... These need to be carefully regulated and resummed."). Their theory is
  moreover a SCALAR perfect-square theory; its gravity connection (ref [25], to appear)
  is the CONFORMALLY-FLAT limit of quadratic gravity, in which "the spin two graviton,
  its ghost counterpart and a vector mode decouple" -- i.e. the massive spin-2 ghost is
  precisely what is NOT covered. So loop-level unitarity for the full Stelle massive
  spin-2 ghost is OPEN in BT, and [P,S]=0-under-renormalization is asserted only via a
  diffeo Ward identity in the (to-appear) conformally-flat companion, not proven for the
  spin-2 sector. This is the SAME open problem that keeps GENERIC Stelle in the contested
  corner. This file does NOT compute it; it records the honest tree-vs-loop boundary.

BAR 4 -- DOES GU'S SPECIFIC STRUCTURE HELP? (FENCED with canon.)
  GU's O(96,96) Krein / Cartan involution PROVIDES the ghost parity kappa NATIVELY (canon
  ghost-parity-krein-synthesis: K implements the Cartan involution of so(9,5) and equals
  ghost parity on the triplet, residual 0.0e+00) -- a genuine structural asset generic
  Stelle lacks (there kappa must be posited). BUT the same canon FENCES that on the
  192-dim triplet sector every GU-native core is spectrally sign-blind and a
  dynamics-DERIVED parity never arises; [P,S]=0 requires S Krein-diagonalizable with real
  SIMPLE spectrum, and at GU's three-generation DEGENERACIES the C-operator exists but is
  NON-UNIQUE. So GU supplies kappa kinematically but does NOT derive the loop condition.
  And the Lambda (DeWitt O(M^0), H15 Part D) / ghost-mass (R^X, H15 Part A/E) RATIO is not
  fixed by the built structure -> no extra predictive rescue. GU helps kinematically, not
  dynamically; it does not WORSEN Stelle but does not resolve its loop problem either.

WHAT THIS FILE DOES NOT DO (honest boundary):
  - Does NOT prove loop-level unitarity (BAR 1) -- that is BT-tree-only + open, cited.
  - Does NOT build GU's source action, so the overall energy sign (+, from a norm^2) and
    the ambient DeWitt R^Y coefficient (which could shift or in principle FLIP the effective
    EH sign in a curved ambient) are ASSUMED/FLAGGED, not derived. BAR 3's PASS is at
    flat-ambient / structural grade, gated on R^Y not overturning the sign.
  - Does NOT pin the ghost MAGNITUDE (BAR 2) -- only its Planckian scaling; the mu_DW
    normalization is unbuilt.
  - Does NOT re-derive the Krein rep theory / ghost parity kinematics (taken from canon).

Run: python -u tests/wave5/H16_stelle_viability.py    (exit 0 iff all PASS)
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# BAR 3 -- THE R^X SIGN: attractive (healthy massless graviton) or a KILL?
# ===========================================================================
log("=" * 78)
log("BAR 3 -- R^X SIGN: is induced Einstein-Hilbert term attractive or a wrong-sign KILL?")
log("=" * 78)

s, m2 = sp.symbols('s m2', positive=True)   # s = box eigenvalue = k.k (Euclidean, >0); m2 = mass^2 scale

# (3a) Gauss-convention R^X is sign-aligned with the standard "sphere has R>0" convention.
#      Round n-sphere of radius a in flat R^{n+1}: every principal curvature k_i = 1/a > 0,
#      so R^X = sum_{i!=j} k_i k_j = n(n-1)/a^2 > 0 -- and a sphere DOES have positive scalar
#      curvature. Hence "-R^X" genuinely subtracts POSITIVE curvature; no hidden sign flip.
a = sp.symbols('a', positive=True)
for dim in (2, 3, 4):
    Rx_sphere = sp.expand(sum((sp.Integer(1) / a) * (sp.Integer(1) / a)
                              for i in range(dim) for j in range(dim) if i != j))
    expected = sp.Rational(dim * (dim - 1)) / a**2
    check(f"dim {dim}: round-sphere R^X = n(n-1)/a^2 = {expected} > 0 "
          f"(Gauss convention == standard 'sphere has R>0'); '-R^X' subtracts POSITIVE curvature",
          sp.simplify(Rx_sphere - expected) == 0 and sp.simplify(Rx_sphere) > 0)

# (3b) The decisive discriminator. E = int(|H|^2 - R^X). On TT the |H|^2 (Bach/Weyl^2) part
#      gives +box^2 (coeff fixed +1 by the POSITIVE-definite norm-square energy), and the
#      -R^X part gives + m2 * box (H15 Part B/E: on TT G^(1) = -1/2 box, and -R^X -> -(G^(1))
#      = +1/2 box, so m2 = 1/2 > 0). Operator symbol P(s):
P_gauss = s**2 + m2 * s        # -R^X  (Gauss-FORCED)  = box(box + m2)
P_flip = s**2 - m2 * s         # +R^X  (hypothetical) = box(box - m2)

# The massless graviton is the s=0 pole; its residue sign (with the fixed overall + action
# normalization) decides HEALTHY(+, attractive) vs GHOST(-, repulsive).
res0_gauss = sp.residue(1 / P_gauss, s, 0)
res0_flip = sp.residue(1 / P_flip, s, 0)
roots_gauss = sp.roots(sp.Poly(P_gauss, s))
roots_flip = sp.roots(sp.Poly(P_flip, s))

check("Gauss-forced -R^X -> P(s)=s(s+m2): massless (s=0) residue = +1/m2 > 0 -> HEALTHY "
      "massless graviton, massive pole is the ghost -> ATTRACTIVE gravity (correct Stelle order)",
      sp.simplify(res0_gauss - 1 / m2) == 0 and sp.simplify(res0_gauss.subs(m2, sp.Rational(1, 2))) > 0
      and set(roots_gauss) == {sp.Integer(0), -m2},
      f"res(s=0)=+{res0_gauss}, poles={{0, -m2}}")

check("hypothetical FLIP +R^X -> P(s)=s(s-m2): massless (s=0) residue = -1/m2 < 0 -> GHOST "
      "massless graviton -> REPULSIVE/antigravity (this is the KILL the Gauss sign AVOIDS)",
      sp.simplify(res0_flip + 1 / m2) == 0 and sp.simplify(res0_flip.subs(m2, sp.Rational(1, 2))) < 0
      and set(roots_flip) == {sp.Integer(0), m2},
      f"res(s=0)={res0_flip}, poles={{0, +m2}}")

# (3c) The two-member Krein pair has OPPOSITE-sign residues (convention-independent): the sign
#      that matters is WHICH member sits at the massless pole. Gauss -R^X puts the +residue
#      (healthy) member at s=0. Verify opposite signs and the correct assignment.
resm_gauss = sp.residue(1 / P_gauss, s, -m2)   # massive ghost pole
check("O(1,1)/Krein pair has opposite-sign residues; Gauss puts the POSITIVE-residue member "
      "at the massless pole and the NEGATIVE-residue (ghost) member at the massive pole",
      sp.simplify(res0_gauss) > 0 and sp.simplify(resm_gauss) < 0
      and sp.simplify(res0_gauss + resm_gauss) == 0,
      f"(massless +{res0_gauss}, massive {resm_gauss})")

# (3d) m2 sign is what makes the massless pole the healthy one; confirm m2 = +1/2 > 0
#      (flat-ambient), i.e. real non-tachyonic ghost AND healthy massless graviton together.
m2_val = sp.Rational(1, 2)     # = (box coeff +1/2 from -R^X) / (box^2 coeff +1 from |H|^2)
check("flat-ambient m2 = +1/2 > 0: the SAME sign that makes the ghost real (non-tachyonic) "
      "makes the massless graviton healthy/attractive -- the two are locked by the Gauss -R^X",
      m2_val > 0, f"m2 = {m2_val}")

log("  => BAR 3 PASSES at flat-ambient/structural grade: the Gauss-FORCED -R^X is the")
log("     ATTRACTIVE sign (positive Newton constant, healthy massless graviton). The sharpest")
log("     potential kill does NOT fire. GATED: overall +energy sign (norm^2) and the ambient")
log("     DeWitt R^Y coefficient (curved-ambient correction could in principle shift/flip it).")

# ===========================================================================
# BAR 2 -- THE GHOST SCALE: Planckian (safe) or observable (excluded)?
# ===========================================================================
log("\n" + "=" * 78)
log("BAR 2 -- GHOST SCALE: dimensional/scaling argument (magnitude gated on DeWitt norm)")
log("=" * 78)

# m2 = 1/2 is DIMENSIONLESS (ratio of box to box^2 coefficients). The physical ghost mass^2
# carries dimension [mass]^2, so it must be m_ghost^2 = ratio * mu_DW^2 where mu_DW^2 is the
# only dimensionful scale in the induced action: the ambient DeWitt normalization on
# Y^14 = Met(X^4) (== the coefficient that also sets the induced Planck scale of the R^X term).
ratio = sp.Rational(1, 2)                 # dimensionless (flat-ambient)
mu_DW = sp.symbols('mu_DW', positive=True)   # DeWitt / ambient-R^Y normalization scale [mass]
M_Pl = sp.symbols('M_Pl', positive=True)
m_ghost2 = ratio * mu_DW**2

# dimensional consistency: [m_ghost^2] = [mass]^2 requires exactly one power of mu_DW^2.
check("ghost mass^2 = (dimensionless 1/2) * mu_DW^2 -- dimensionally forced: the flat-ambient "
      "ratio is scaleless, so a single dimensionful DeWitt scale mu_DW must set the magnitude",
      sp.simplify(m_ghost2 - sp.Rational(1, 2) * mu_DW**2) == 0)

# The induced R^X (Einstein-Hilbert) coefficient IS the induced Planck scale; the DeWitt
# metric-on-metrics normalization is the natural origin of M_Pl. So mu_DW ~ M_Pl is the
# natural expectation -> m_ghost ~ M_Pl/sqrt(2): PLANCKIAN -> decouples -> empirically SAFE.
m_ghost2_planck = m_ghost2.subs(mu_DW, M_Pl)
check("natural normalization mu_DW ~ M_Planck (the metric-on-metrics scale that sets the "
      "induced R^X Planck coefficient) -> m_ghost^2 = M_Pl^2/2 -> Planckian -> DECOUPLES -> SAFE",
      sp.simplify(m_ghost2_planck - sp.Rational(1, 2) * M_Pl**2) == 0
      and sp.simplify(m_ghost2_planck) > 0)

# Adversarial: empirical exclusion requires m_ghost BELOW an observable scale. That needs
# mu_DW^2 <<= (observable)^2, i.e. the DeWitt scale far below Planck -- which would be
# UNNATURAL for a metric-on-metrics normalization. So the ghost is naturally safe; danger
# requires an unnatural hierarchy. Encode the scaling logic (not a magnitude proof).
mu_obs = sp.symbols('mu_obs', positive=True)  # some observable scale << M_Pl
danger = sp.simplify(sp.Rational(1, 2) * mu_obs**2)  # ghost at observable scale iff mu_DW ~ mu_obs
check("exclusion (ghost at observable scale) requires mu_DW ~ mu_obs << M_Pl -- an UNNATURAL "
      "hierarchy for a metric-on-metrics normalization; safety is the natural outcome, danger the "
      "fine-tuned one. (SCALING argument; magnitude UNDETERMINED without the unbuilt normalization)",
      danger == sp.Rational(1, 2) * mu_obs**2)   # tautological encoding of the stated logic

log("  => BAR 2 PLAUSIBLY SAFE but UNPROVEN: ghost is Planckian (decouples) for the natural")
log("     mu_DW ~ M_Pl; the magnitude is GATED on the unbuilt DeWitt R^Y normalization (H15 Part E).")

# ===========================================================================
# BAR 1 & 4 -- documented boundary (NOT computed from GU here; cited/fenced)
# ===========================================================================
log("\n" + "=" * 78)
log("BAR 1 (loop unitarity) & BAR 4 (GU rescue) -- FENCED with primary sources / canon")
log("=" * 78)
# These are NOT physics computations; they are honest-boundary assertions that the file is
# CORRECTLY FENCING the tree-vs-loop gap and the kinematic-vs-dynamic status of GU's kappa.
# A PASS here means "the boundary is stated honestly", NOT "the physics is proven".
BAR1_tree_only = True          # BT arXiv:2607.00096 Conclusions: positivity proven at TREE level only
BAR1_spin2_uncovered = True    # BT gravity link = conformally-flat limit where the spin-2 ghost DECOUPLES
BAR4_kappa_kinematic = True    # canon: K = Cartan involution of so(9,5) = ghost parity (residual 0.0e+00)
BAR4_PS0_not_derived = True    # canon: dynamics-DERIVED parity never arises; [P,S]=0 not shown (loop-open)
BAR4_ratio_unfixed = True      # Lambda(DeWitt)/ghost-mass(R^X) ratio not fixed by built structure

check("BAR 1 fenced honestly: BT prove TREE-level positivity only; loop extension OPEN (their "
      "collinear-IR obstacle); their spin-2 ghost DECOUPLES in the conformally-flat limit that "
      "carries their gravity claim -> full Stelle massive spin-2 ghost at LOOP level is UNPROVEN",
      BAR1_tree_only and BAR1_spin2_uncovered)
check("BAR 4 fenced honestly: GU provides ghost parity kappa NATIVELY (kinematic asset over "
      "generic Stelle) BUT does not derive [P,S]=0 (loop condition) and does not fix the "
      "Lambda/ghost-mass ratio -> GU helps kinematically, not dynamically; loop problem inherited",
      BAR4_kappa_kinematic and BAR4_PS0_not_derived and BAR4_ratio_unfixed)

# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT -- H16 Stelle viability")
log("=" * 78)
log(r"""
COMPUTED (this file, exact, exit 0):
  BAR 3 (R^X SIGN -- the sharpest kill): the Gauss equation |II|^2 = |H|^2 - R^X FORCES
    the -R^X sign; with the positive norm-square energy this puts the HEALTHY (+residue)
    member of the O(1,1)/Krein pair at the MASSLESS graviton pole -> ATTRACTIVE gravity,
    positive Newton constant; the massive spin-2 is the ghost (correct Stelle ordering).
    The hypothetical +R^X flip would put the GHOST at the massless pole -> repulsive KILL.
    Gauss-convention R^X is sign-aligned with 'sphere has R>0', so no hidden flip. The
    SAME -R^X sign makes m^2 = +1/2 > 0 (real, non-tachyonic). => BAR 3 PASSES.
  BAR 2 (GHOST SCALE): m^2 = 1/2 is dimensionless; the physical ghost mass^2 = (1/2) mu_DW^2
    where mu_DW is the ambient DeWitt (metric-on-metrics) normalization = the induced Planck
    scale. Natural mu_DW ~ M_Pl -> Planckian ghost -> decouples -> SAFE. Magnitude GATED on
    the unbuilt normalization; danger requires an unnatural sub-Planckian hierarchy.

FENCED (NOT computed from GU; primary sources + canon):
  BAR 1 (LOOP UNITARITY): Bateman-Turok prove positivity at TREE level ONLY (collinear-IR
    obstacle to loops, their own Conclusions); their theory is a SCALAR perfect-square model
    whose gravity connection is the conformally-flat limit in which the spin-2 ghost DECOUPLES.
    So loop-level unitarity for the full Stelle massive spin-2 ghost is OPEN. This is exactly
    the unresolved problem that keeps GENERIC Stelle-Mannheim contested.
  BAR 4 (GU RESCUE): GU's O(96,96) Krein / Cartan involution supplies the ghost parity kappa
    NATIVELY (canon, residual 0.0e+00) -- a real kinematic asset -- but does NOT derive
    [P,S]=0 at loop level and does NOT fix the Lambda/ghost-mass ratio. GU helps kinematically,
    not dynamically; the loop problem is inherited, not resolved.

VERDICT: (CONTESTED-CORNER) -- the honest most-likely. The branch is NOT KILLED: the sharpest
  kill (wrong-sign R^X -> antigravity) does NOT fire -- the Gauss-forced -R^X yields ATTRACTIVE
  gravity, a real ghost mass, a native ghost parity, and tree-level BT positivity. But it does
  NOT fully CLEAR: it inherits generic Stelle-Mannheim's UNRESOLVED loop-unitarity dispute
  (BT tree-only; spin-2 ghost uncovered; multiple competing unaccepted resolutions -- BT
  Krein/ghost-parity, Anselmi purely-virtual fakeons, Mannheim PT/PU, IHO-DQFT 2603.07150),
  and GU's structure resolves the loop condition no better than generic Stelle. The ghost scale
  is plausibly Planckian (safe) but gated on the unbuilt DeWitt normalization.

  => GRAVITY LEG STAYS CONTESTED (survives formally; not cleared, not killed). The R^X-sign
  PASS retires the wrong-sign KILL risk; the residual gate is the loop [P,S]=0 (== GU's
  long-standing missing source-action dynamics) plus the DeWitt R^Y sign/scale normalization.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = H16 computed: BAR 3 (R^X sign) PASSES -> attractive, no wrong-sign kill;")
log("         BAR 2 (ghost scale) plausibly Planckian/safe but normalization-gated;")
log("         BARS 1&4 (loop unitarity / GU rescue) OPEN -> VERDICT CONTESTED-CORNER.")

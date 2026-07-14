---
title: "W144: the DESI-fitted issuance function Q(a) and the source action it implies. Fit-first, rigor-after: FREE the issuance schedule, fit it to the repo's verified DESI DR2 BAO + theta_star machinery, then back out what the GU source action would have to supply. Deliverable is the best-fit Q(a) AND the source-action structure it forces, all at exploration grade, conditional register, hypothesis-generation not evidence."
status: exploration
grade: exploration (fit-first hypothesis generation; every number computed; nothing promoted; the DESI wiggle is FITTED, never claimed as evidence)
date: 2026-07-14
wave: W144
team: ISS-FIT (W144)
test: tests/W144_desi_fitted_issuance_function.py (28 checks, exit 0)
depends_on:
  - tests/wave29/H46_de_raw_bao_likelihood.py (raw DESI DR2 BAO likelihood, imported verbatim)
  - tests/wave46/H46C_theta_star_cmb_calibration.py (theta_star CMB calibration, imported verbatim)
  - tests/W135_issuance_structure_taxonomy.py (the source-term formulation; b2 and PID anchors)
  - explorations/W136-issuance-declaration-propagation-2026-07-14.md (beta/alpha = 2 bulk-flatness selection)
  - explorations/W138-issuance-kill-battery-2026-07-14.md (the six gates; G2 register distinction)
  - explorations/source-action-requirements-spec-2026-07-13.md (Stage B language; SA-G rows)
binding_constraints:
  - "B2 rate-identity FALSE: Q(a) is a SCHEDULE (structural function of a), never a rate identity (G4-allowed)"
  - "H36 mu_DW identification FALSIFIED: no mu_DW = DE scale identification anywhere"
  - "W138 G2: the mimic gate was derived for schedule-drift EVIDENCE claims; this wave fits the wiggle as HYPOTHESIS, never evidence"
  - "tri-repo gating: issuance = local postulate label; the issuance CONCEPT is owned by temporal-issuance; no cross-repo identity claim"
---

# W144: the DESI-fitted issuance function

## 0. Posture and scope (read first)

This wave follows Joe's explicit fit-first directive: "if we already have the DESI data,
why don't we make the function that fits the DESI data ... make it fit the DESI data and
then see what the source action would have to look like." That is deliberately bad
science stated as such: we FREE the issuance function Q(a), fit it to the data, and read
off the implied source-action structure, knowing the rigorous confrontation comes later.

Everything below is at exploration grade in the conditional register. The one hard
discipline this wave keeps, from W138: the DESI DR2 CPL wiggle is FITTED as hypothesis
generation, and is NOWHERE claimed as evidence for GU or for issuance. W138 gate G2 was
derived for schedule-drift EVIDENCE claims; the gate does not forbid fitting the wiggle
to generate a source-action target, but it does forbid promoting the fit to a truth
claim. That distinction is stated plainly and enforced: the >4 sigma preference reported
in Stage A3 is the FIT'S number under maximal freedom, not a GU prediction and not
evidence. The other branch of the fork (the pull regresses in DR3) stays fully alive and
is the W141 S1 pre-registered call; the two-bet decision table is Section 6.

Tri-repo note. "Issuance" here labels a local postulate only. The object the GU source
action would supply is the scalar Q(a) in the sourced continuity equation; no
temporal-issuance quantity is asserted to BE a GU quantity.

Five personas ran inline in one session (observational cosmologist, interacting-DE
theorist, source-action/spec specialist, numerical engineer, adversarial skeptic). The
deterministic test `tests/W144_desi_fitted_issuance_function.py` (28/28, exit 0) runs its
four positive controls first.

## 1. Persona 1, observational cosmologist: the interacting-vacuum decomposition

The repo's verified machinery (wave29 raw DESI DR2 BAO likelihood, full 13x13 covariance;
wave46 H46C theta_star calibration) is imported verbatim, exactly as W135 imported it. The
decomposition that turns a general dark-energy history into an issuance function is the
interacting-vacuum split (PORTED; see Persona 2): write dark energy as a strictly w = -1
vacuum component V exchanging energy with a reservoir,

```
rho_V' + 3 H (1 + (-1)) rho_V = Q      =>      rho_V' = Q   exactly.
```

All the w(z) structure lives in Q(a); the fluid stays a local cosmological "constant". The
effective equation of state read off the density history is

```
w_eff(a) = -1 - (1/3) d ln rho_DE / d ln a,      Q(a) = rho_DE'(a) = -3 H (1 + w_eff) rho_DE.
```

Positive controls (the test runs these before any fit):

- Q = 0 pushed through the free-Q machinery reproduces the LCDM baseline exactly
  (delta chi^2 < 0.02).
- The verbatim H46 configuration reproduces the verified LCDM row chi^2 = 30.68.
- The CPL closed form pushed through the generic solver reproduces the direct analytic
  CPL chi^2 on the same grid to < 0.01, and its w(a) reproduces the analytic CPL law to
  1.6e-6 (endpoint-accurate second-order stencil).
- The W135 b2 (stock+drip) and PID anchors are re-run and matched within the test.

## 2. Persona 2, interacting-DE theorist: the closed-form Q(a) and the phantom crossing

**PORTED, labeled.** The interacting-vacuum reading is standard-field literature (the
Wands / De-Bruck / Vacca interacting-vacuum lineage, and the broader coupled-dark-energy
program). The key ported structural result: in the interacting-vacuum decomposition the
w = -1 crossing is simply Q changing sign. There is no propagating scalar whose kinetic
term passes through zero, so the classic single-field crossing no-go (the Vikman /
gradient-instability obstruction to a single minimally coupled scalar crossing w = -1)
does not apply. The vacuum component carries no independent propagating degree of freedom;
its perturbations are slaved to the transfer Q. This wave checks the statement only at the
level of citing the known result and verifying the background solution is regular at the
crossing (below); a full perturbation computation is named, not done.

**The closed form for the DESI CPL point.** With the repo-verified digits (wave45 H46B
check A7; DESI+CMB+DESY5) w0 = -0.752, wa = -0.86, the CPL history has the exact solution

```
rho_DE(a) = rho_DE,0 * a^{-3(1 + w0 + wa)} * exp(-3 wa (1 - a)),   w(a) = w0 + wa (1 - a),
Q(a) = rho_DE'(a) = -3 H(a) (1 + w(a)) rho_DE(a).
```

**Shape and sign structure (computed):**

| quantity | value |
|---|---|
| phantom crossing w = -1 | a_x = 0.71163, z_x = 0.40523 |
| sign of Q for a < a_x (z > 0.405) | Q > 0: ISSUANCE epoch |
| sign of Q for a > a_x (z < 0.405) | Q < 0: WITHDRAWAL epoch |
| Q today | -0.248 q_B (= analytic -(1 + w0)), = -1.53 in H0^3 M_Pl,red^2 units |
| Q amplitude scale (issuance side, z <= 3 window edge) | +0.98 q_B, = +6.0 in H0^3 M_Pl,red^2 units |
| rho_DE peak (at the crossing) | 1.127 rho_L |
| past asymptotics | rho_DE ~ a^{1.836} decays into the past: no early-DE conflict |

Units: q_B = 3 H0 rho_L is the W135 bookkeeping rate; the Planck-ladder unit is
q_B / (H0^3 M_Pl,red^2) = 9 Omega_L = 6.16. So the covariant issuance rate the DESI CPL
point demands is O(1) in the natural Planck-ladder unit and changes sign once, near
z = 0.4.

**The structural advantage, stated as this writeup's sharpest point.** DESI's w0 > -1,
wa < 0 means w(z) crosses -1 from below near z = 0.4. In a single-field dark-energy model
that crossing is pathological (ghost or gradient instability). In the interacting-vacuum
reading it is nothing but Q(a) passing through zero: the vacuum stays w = -1, the sign of
the boundary supply flips from issuance to withdrawal, and there is no kinetic zero to go
unstable. The test verifies the background is regular at a_x (rho_DE > 0, E > 0, Q smooth
and finite, no divergence). This is the honest reason the issuance reading is a natural
home for a DESI-type crossing: the pathology that kills quintessence crossings is absent
by construction. Conditional register: this is an advantage OF THE READING, not evidence
the crossing is real.

## 3. Persona 1 + 4: the free fit and the four-class dAIC table

Two free parametrizations of Q(a), windowed to a >= 0.30 (the DESI window; zero supply
before, so the theta_star calibration validity guard holds, rho_DE/rho_m at z = 30 is
1e-5 to 1e-6 throughout), solved self-consistently, theta_star-calibrated and scored on
the raw BAO likelihood:

- linear Q(a) = c0 + c1 (1 - a), k = 2;
- 3-node spline at a = (0.30, 0.65, 1.0), k = 3.

**Best-fit free shapes (computed):**

- linear: (c0, c1) = (-2.66, +8.55) H0 rho_crit = (-1.29, +4.16) q_B, chi^2 = 7.70,
  dchi^2 = -22.41, dAIC = -18.41. The fitted Q crosses zero at z = 0.451 (independently
  of the CPL input, and close to the CPL crossing z = 0.405).
- 3-node: Q(0.30, 0.65, 1.0) = (+3.32, +0.51, -3.22) H0 rho_crit = (+1.61, +0.25, -1.57)
  q_B, chi^2 = 7.68, dchi^2 = -22.42, dAIC = -16.42.

Both free fits independently prefer a ZERO-CROSSING Q: positive (issuance) in the past,
negative (withdrawal) today, crossing near z ~ 0.45. The free fit does NOT prefer the
simpler one-signed constant, and it does NOT prefer LCDM. It reproduces the shape class of
the CPL closed form (issuance then withdrawal) without being told the CPL numbers.

**The four-class classification (dAIC vs LCDM, dAIC = dchi^2 + 2k):**

| class | shape | k | dchi^2 | dAIC |
|---|---|---|---|---|
| ZERO | LCDM, Q = 0 | 0 | 0.00 | 0.00 |
| ONE-SIGNED CONSTANT | b2 stock+drip, s = +0.25 | 1 | -8.44 | -6.44 |
| CONSTANT+TRANSIENT | PID, Kp = 3, eps = -0.5 | 2 | -12.57 | -8.57 |
| ZERO-CROSSING | CPL closed form | 2 | -19.96 | -15.96 |
| ZERO-CROSSING | free linear Q | 2 | -22.41 | -18.41 |
| (freest) | free 3-node Q | 3 | -22.42 | -16.42 |

**Preference ordering: ZERO-CROSSING > CONSTANT+TRANSIENT > ONE-SIGNED CONSTANT > ZERO
(LCDM).** The zero-crossing class wins decisively on this data (BAO + theta_star, SNe
unintegrated). The amplitude-freed (shape-only) rows agree: LCDM 14.38, CPL 9.46
(-4.92), fitted linear Q 6.84 (-7.54).

**SIGNIFICANCE, reported honestly and flagged (this is the finding to caveat hardest).**
The freed 2-parameter Q(a) prefers non-LCDM at dchi^2 = -22.41: about 4.7 sigma on the
1-dof scale, about 4.4 sigma as a proper k = 2 test (p = 1.4e-5). This is STRONGER than
the roughly 3.2 sigma DESI CPL point (H43/H44). That is expected and is not a GU
discovery, for three reasons stated plainly:

1. freeing the whole schedule adds fit freedom beyond CPL's two numbers (the free Q can
   put its crossing and amplitude wherever the BAO points pull hardest);
2. SNe are UNINTEGRATED here, and SNe scatter and partly pull against the BAO+theta_star
   preference; adding them would reduce this number;
3. the look-elsewhere cost of scanning shape classes is not penalized.

W138 G2 forbids reading this as EVIDENCE. This wave fits the wiggle as hypothesis
generation. The number belongs to the fit under maximal freedom, not to GU. The honest
one-line summary: if the DESI pull is taken at face value and the schedule is freed, the
data want an issuance function that issues in the past and withdraws today, crossing near
z ~ 0.45, at O(1) Planck-ladder amplitude, and they want it at 4-5 sigma-equivalent on
BAO+theta_star alone. Whether that pull is real is the DR3 question (Section 6).

## 4. Persona 3, source-action / spec specialist: Stage B, backing into the action

The transducer requirement (W135) reduced the GU-side question to one scalar: can the
source action express Q = 0 / const / feedback. The fitted shape sharpens it to: the
source action must supply a TIME-VARYING, SIGN-CHANGING boundary flux Q(a), issuance
before z ~ 0.45 and withdrawal after.

**Boundary-term structure (spec language, explorations/source-action-requirements-spec).**
In W136's boundary-flux formulation the issuance enters as a boundary energy flux whose
bulk signature is a Lambda-mimic; a constant flux gives w = -1 exactly. A time-varying Q
means the boundary supply varies with the section's evolution: the coupling that carries
the flux must depend on a cosmological clock (the section's embedding evolution, or a
horizon-structure scalar), not be a fixed number. A sign change in Q means the boundary
term switches from supplying energy to the bulk to absorbing it, near a specific epoch.

**The beta/alpha = 2 fate under time-varying Q (the key Stage-B computation).** W136's
bulk-flatness selection beta/alpha* = 2 was derived under the CONSTANT declaration, with a
pin width |x - 2| < 2.1e-60 driven by rho_DE / M_Pl^4 ~ 1e-60. The question: does a
time-varying Q break it, deform it, or leave it? Computed answer:

- The bulk-flatness selection is a statement about the BULK cosmological constant vanishing
  at the ratio beta/alpha = 2. It is set by the requirement that the bulk not add a second,
  larger Lambda to the boundary-supplied one.
- Time variation multiplies the relevant bound by the peak amplitude factor
  rho_DE,max / rho_L = 1.127, an O(1) number, NOT an exponential deformation. The pin is
  ~1e-60; multiplying by 1.13 leaves it ~1e-60.
- Verdict: the selection is LEFT INTACT at the computed level. beta/alpha = 2 survives the
  time-varying Q as an O(1) (not order-of-magnitude, not sign) deformation of the bound.
  The variation is a boundary effect that the bulk-flatness selection does not see: the
  bulk constant vanishes at beta/alpha = 2 regardless of the time profile of the boundary
  supply, because the profile is carried by the boundary term, not the bulk shape family.
  A correction of order Q'/(H Q) enters the pin width but stays sub-dominant to the 1e-60
  scale.

**Carrier separation (f0 = 0 fate).** GU's own theta-sector shape (M^2 = 8 H0^2) cannot
fit the DESI CPL point (H46C / W129, ~3.2 sigma). The whole point of freeing Q was to move
the wiggle OFF the theta sector and ONTO the boundary supply. In every fitted model here
NO theta amplitude is used: the wiggle lives entirely in Q(a). So under the fitted reading
the W136 determination (B_i, f0) = (0, 0) survives, the theta shape stays excluded as
before, and the issuance function carries the DE structure. The theta sector is not asked
to do a job it provably cannot do.

## 5. Persona 5, adversarial skeptic: THE-PULL-IS-NOISE steelman and the gate sheet

**Steelman: the fitted Q is noise.** The honest null is that the DESI DR2 evolving-DE pull
is a fluctuation plus unmodeled systematics, and the freed Q(a) is fitting it. Everything
in Stage A is consistent with that null:

- the raw significance is inflated by fit freedom (Section 3, three reasons);
- SNe are unintegrated, and the SNe datasets disagree among themselves on the strength of
  the pull;
- BAO + theta_star alone cannot separate a genuine schedule from a residual amplitude
  degeneracy (the standing DARK-ENERGY-03 caveat: raw non-CPL histories can mimic DESI
  distances along the amplitude direction);
- the crossing epoch z ~ 0.45 is exactly where the DESI LRG anticorrelated D_M / D_H
  points sit, the same points driving the headline CPL preference, so the free Q is not
  finding independent structure, it is re-fitting the same pull.

Under the noise hypothesis the correct GU-side statement is W141 S1: the theory PREDICTS
exact LCDM (Q = 0), and DR3 regressing to LCDM CONFIRMS that prediction. The fitted Q(a)
is then a hypothesis that DR3 kills.

**The W138 gate sheet applied to the fitted Q (mechanical):**

| gate | check | verdict on the fitted Q |
|---|---|---|
| G1a conservation structure | Q^i = 0 at background, ledger named | PASS: Q = q(t) u^nu, ledger = the external boundary supply (the transducer) |
| G1b locality | local enhancement over uniform 3 H rho_L | PASS: max |Q|/q_B = 1.62, O(1); margin to the 1e19 ephemeris gate is 6.2e18 |
| G2 mimic | schedule drift vs 0.3 per e-fold | OUTSIDE the band (0.744 per e-fold) BY CONSTRUCTION: the fit IS the DESI signal. Register = HYPOTHESIS, never evidence. This is the gate applied differently for a fitting exercise, exactly as the wave brief requires: not a kill, a flag |
| G3 H36 non-reimport | rho ~ c_L mu_DW^4? | PASS: no mu_DW identification anywhere; Q is a schedule in H0 rho_crit units |
| G4 B2 non-reimport | is any "rate" a structural constant? | PASS: Q(a) is a schedule (function of a), explicitly the filtration/schedule reading G4 allows; no f0/c_L/alpha_W read as a rate |
| G5 de Sitter relabeling | normalization = T_dS S_dS with no new dof? | N/A at fit level: the fit outputs a shape, not a normalization identity; the amplitude is O(1) q_B, consistent with but not derived from the de Sitter value |
| G6 record cost | required record rate above budget? | N/A: no record model invoked |

The fitted Q passes every TRUTH gate (G1, G3, G4) and is only flagged by G2, which is the
gate the brief explicitly said applies differently to a fitting exercise. The skeptic's
bottom line: nothing here is false, and nothing here is evidence. The fit is a legitimate
hypothesis-generation output whose truth is deferred to DR3.

## 6. The two-bet fork and the DR3 decision table

This exercise bets the DESI pull is REAL. The W141 S1 story bets it REGRESSES. The two
bets are complementary, both pre-registered, and DR3 (2026-27) decides.

| DR3 outcome | surviving branch | what it pins |
|---|---|---|
| pull STRENGTHENS, crossing near z ~ 0.4 confirmed jointly (BAO + SNe + CMB) | THIS branch (fitted Q real) | the source action must carry a TIME-VARYING SIGN-CHANGING boundary flux; issuance before z ~ 0.45, withdrawal after; O(1) q_B amplitude; the coupling depends on a cosmological clock, not a constant; beta/alpha = 2 survives; the crossing epoch z ~ 0.45 becomes a prediction target for any OTHER GU sector that should change character at the same z |
| pull WEAKENS toward LCDM | W141 S1 (Q = 0, exact LCDM prediction) | (B_i, f0) = (0, 0) confirmed; beta/alpha = 2 stands under the constant declaration; GU's exact-LCDM DE prediction is the win; the fitted Q(a) here is retired as a killed hypothesis |
| pull persists but as CONSTANT offset (no crossing) | ONE-SIGNED CONSTANT (W135 b2) | a constant covariant issuance rate s ~ +0.25 H0 rho_crit ~ +0.12 q_B; the source action supplies a small constant boundary flux, no clock dependence, no sign change |
| pull persists but as a decaying TRANSIENT | CONSTANT+TRANSIENT (W135 PID / EDE-like) | a setpoint with finite-gain feedback; the source action expresses a controller, not a fixed supply |

The decision is sharp because the four classes make DIFFERENT source-action demands
(constant flux vs clocked flux vs feedback vs zero), and DR3's improved BAO plus the SNe
cross-check can separate them. This wave's contribution is to have computed, ahead of DR3,
exactly what each surviving branch would pin.

## 7. The back-out ledger: what the source action must now contain

If the fitted zero-crossing Q(a) is taken as the target (this branch's bet), the source
action must have, beyond the W136 constant-declaration structure:

1. **A coupling to a cosmological clock.** A constant boundary flux gives w = -1. A
   time-varying Q requires the flux-carrying coupling to depend on the section's embedding
   evolution or a horizon-structure scalar. This is a NEW demand beyond SA-G3/G4 (which
   were fixed numbers under the constant declaration). Spec impact: SA-G3 (B_i) and SA-G4
   (f0) would move from "= 0 natural point" to "= 0 at background plus a clocked boundary
   deformation"; a new declaration row for the clock coupling would be needed.
2. **A sign-changing boundary term.** The flux must switch from supply to absorption near
   z ~ 0.45. In boundary-term language this is a boundary functional whose variation
   changes sign as the section evolves, i.e. the boundary is not a pure source but a
   two-way exchange with an epoch-dependent direction.
3. **beta/alpha = 2 UNMOVED.** The bulk-flatness selection survives (Section 4); the
   time variation is a boundary effect invisible to the bulk shape selection, up to an
   O(Q'/HQ) correction that stays far below the 1e-60 pin width. SA-G5 stays DETERMINED
   (conditional) at 2.
4. **A new testable consequence: the crossing epoch as a target.** The fitted Q's
   zero-crossing at z ~ 0.45 is a prediction target. The sharpest new question the fitted
   shape raises: is there anything ELSE in GU that should change character at the same z?
   If the boundary flux couples to the section's embedding, any other embedding-sensitive
   observable (structure-growth transitions, the theta sector's own sub-dominant evolution)
   should show a feature near z ~ 0.45. That co-incidence, if a GU mechanism predicts it,
   would be the first non-trivial cross-sector consequence of the issuance reading. It is
   named here, not computed.

Spec rows that move under this branch: SA-G3, SA-G4 (clocked deformation), plus one new
declaration row (the clock coupling). Rows that DO NOT move: SA-G5 (beta/alpha = 2 intact),
SA-G2 (mu_DW untouched, H36 still refused), the Yukawa and cure sectors (dimensionally
disjoint, W136 Personas 3-4).

## 8. Honest limits

- Everything is a FIT to the DESI wiggle, run as hypothesis generation. Nothing here is
  evidence for GU or for issuance. The >4 sigma preference is the fit's number under
  maximal freedom, not GU's, and would shrink with SNe integrated and with a look-elsewhere
  penalty applied.
- The interacting-vacuum crossing-stability result is PORTED and checked only at
  background-regularity level; a full perturbation computation is named, not done.
- SNe are unintegrated (the standing W129 / H46 residual); the pull's strength on
  BAO+theta_star alone is not the joint-probe strength.
- The source-action back-out is structural (what kind of coupling, what sign behavior),
  not a built action; H41 stays unbuilt.
- The beta/alpha = 2 survival is computed at the O(1) peak-factor level; the exact
  O(Q'/HQ) correction to the pin width is bounded, not evaluated in closed form.
- No canon, verdict, claim-status, or posture moves. The spec FIT rows do not move;
  "would move under this branch" is a property of the conditional theory, recorded here.

*Filed 2026-07-14 by Team ISS-FIT (W144). Five personas inline in one session
(observational cosmologist, interacting-DE theorist, source-action/spec specialist,
numerical engineer, adversarial skeptic). Reproducible:
`python -u tests/W144_desi_fitted_issuance_function.py` (28/28, exit 0). Exploration
grade; fit-first hypothesis generation; the DESI wiggle is fitted, never claimed as
evidence; no canon movement; H41 stays unbuilt.*

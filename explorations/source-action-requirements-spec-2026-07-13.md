---
artifact_type: exploration
status: exploration
created: 2026-07-13
hypothesis: H41
title: "THE SOURCE-ACTION REQUIREMENTS SPEC -- everything the unbuilt source action (H41, the falsifiability keystone) must supply, consolidated from every research leg, each requirement sourced to its repo artifact and test, classified FORCED / DECLARATION / FIT, and checked for mutual consistency. VERDICT of the cross-consistency pass: NO OUTRIGHT CONTRADICTION among the FORCED items (wave35's joint carve already certifies nonemptiness on carrier B with the g=1 cure; this spec adds the sector-disjointness and larger-flavor-symmetry arithmetic checks); FIVE named TENSIONS carried openly. 27 requirement rows: 8 FORCED, 9 DECLARATION, 10 FIT."
grade: "CONSOLIDATION. No new physics claims; the only new content is cross-consistency bookkeeping, and every computable piece of it is in tests/spec-consistency/source_action_requirements_consistency.py (33/33 asserts, exit 0, stdlib arithmetic reproducing numbers already computed at higher grade in the cited artifacts). Per the standing E1 rule this spec is a MAP of the requirement surface, not progress by itself. No canon movement, no verdict movement, no count movement; the count stays {1,3}; H41 stays unbuilt; H59 stays OPEN."
construction: "program-native throughout, per GEOMETER-VS-PHYSICS-OBJECTS.md; each row inherits the construction of its source artifact, and the two rows that ARE construction forks (SA-U2 ghost mass, SA-U5 guardian) are recorded as forks, not resolved."
depends_on:
  - explorations/yukawa-scoping-2026-07-13.md
  - explorations/track2-conditional-numbers-2026-07-13.md
  - explorations/h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md
  - explorations/H59-krein-loop-positivity-gate-2026-07-12.md
  - explorations/predictive-boundary-audit-2026-07-12.md
  - explorations/wave10/H27-soldering-palatini-2026-07-11.md
  - explorations/wave16/H39-sourceaction-kclass-2026-07-11.md
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md
  - explorations/wave32/H53-falsifiability-audit-2026-07-11.md
  - explorations/wave19/H42-f0-preregistration-2026-07-11.md
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
  - explorations/wave35/source-action-carve-2026-07-11.md
  - explorations/H64-mass-selection-first-swing-2026-07-11.md
  - canon/shiab-existence-cl95.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/spec-consistency/source_action_requirements_consistency.py
---

# The Source-Action Requirements Spec (H41)

**What this is.** The program's arc has collapsed onto one unbuilt object: the source action
(H41), the coherence keystone (it fixes the gauge-vacuum, soldering, count, and cure faces at
once, H40) and the falsifiability keystone (every empirical channel is gated on the free scale
it would force, H53). Each research leg has now made its demands on that object explicit. This
document consolidates all of them into one engineering-grade specification: every requirement
sourced to its repo artifact and test, classified, and checked for mutual consistency.

**What this is not.** Not a build, not new physics, not progress by itself (standing E1 rule:
a map of the requirement surface). Nothing here moves canon, the count ({1,3}), SG4, H59, or
any verdict.

**Classification legend.**

- **FORCED**: a theorem or exact computation says the source action MUST contain or satisfy
  this item; failing it is an inconsistency, not a modeling choice.
- **DECLARATION**: a choice the source action makes; the built structure provably cannot
  decide it, so an honest build either derives it by a new mechanism or carries it as a
  named postulate.
- **FIT**: a number the source action must output (or leave explicitly free); today it is
  target-fitted or free, and only a source-first emission upgrades it (Clean Prediction Rule,
  predictive-boundary-audit-2026-07-12).

Companion test: `tests/spec-consistency/source_action_requirements_consistency.py`
(deterministic, stdlib, 33/33 asserts, exit 0). It reproduces every arithmetic anchor used in
the cross-consistency pass and pins the table's class tallies to this document.

---

## 1. Persona 1 (EFT theorist): the requirements table

27 rows. Every row cites its artifact; where a machine check exists the test is named.
Composite items are split into lettered sub-rows so each row has exactly one class.

### Yukawa / matter sector (SA-Y)

| ID | Requirement | Class | Source artifact | Test |
|---|---|---|---|---|
| SA-Y1 | The Higgs carrier MUST be a form carrier Lambda^k(V14). Non-form carriers (e.g. Sym^2_0 V, dim 104) have dim Hom = 0: no Yukawa channel exists, exactly (checksum saturation of End(S) by forms). k = 0 is the unique mass-type (Dirac-Yukawa) channel, cross-chirality only; Majorana scalar on S+ x S+ is forbidden (SHIAB-05). | FORCED | explorations/yukawa-scoping-2026-07-13.md (Persona 1, channel table); canon/shiab-existence-cl95.md | tests/yukawa-scoping/yukawa_trilinear_channels.py (20/20, exit 0) |
| SA-Y2 | WHICH Lambda^k the physical Higgs sits in (k = 0 for mass generation), plus which texture fork the physical Yukawa uses (charges-add / transpose-bilinear C channel giving the 1+2 block, vs charges-subtract / Krein sesquilinear giving diagonal). | DECLARATION | yukawa-scoping-2026-07-13.md (Personas 1-2; both forks computed) | same |
| SA-Y3 | The Higgs vev (the scale multiplying the unique channel). | FIT | yukawa-scoping-2026-07-13.md ("what the source action must supply" (i)) | -- |
| SA-Y4 | The three surviving complex couplings {y00, y12, y21} (9 -> 3 by the derived Z/3; singular values exactly {\|y00\|,\|y12\|,\|y21\|}; no forced degeneracy, ordering, or ratio). Supplied as three free numbers UNLESS SA-Y5 is taken. | FIT | yukawa-scoping-2026-07-13.md (Personas 2, 4) | tests/yukawa-scoping/yukawa_trilinear_channels.py |
| SA-Y5 | The hierarchy mechanism, if hierarchy is to be mechanized rather than fitted: a flavor symmetry STRICTLY LARGER than the built Z/3 (charges valued beyond mod 3), plus a flavon and a small parameter. The built structure provably cannot do it: mod-3 FN charges are sterile for ALL 27 assignments (invariant = charge sum 0 = ungraded). Exclusive-or with SA-Y4 as the hierarchy's supply route. | DECLARATION | yukawa-scoping-2026-07-13.md (Persona 4, FN sterility) | yukawa test + spec-consistency test (block E) |
| SA-Y6 | The sector-to-flavor assignment (which Z/3 grading sector is which physical generation; identifying sector 0 with the top quark is the answer-as-premise trap, W60). | DECLARATION | yukawa-scoping-2026-07-13.md (Persona 3) | -- |
| SA-Y7a | The family-symmetry-breaking spurion's TYPE: forced to be a Z/3 DOUBLET spurion in Sym^2(Lambda^2_+) (Schur degeneracy of the collective pair; Sym^2 branching 2 singlets + 2 doublets; H64). | FORCED | explorations/H64-mass-selection-first-swing-2026-07-11.md | tests/W76_H64_mass_selection_swing.py (16/16, exit 0) |
| SA-Y7b | The spurion's VALUES: split magnitude, hierarchy direction (sign), intra-collective mixing angle. Fully free, both signs, a continuum (H64: World A does not obtain). | FIT | H64-mass-selection-first-swing-2026-07-11.md | same |
| SA-Y8 | The Majorana spurion, ONLY IF same-chirality masses are wanted: the equivariant channel is provably absent (dim Hom(S+ x S+, Lambda^0) = 0, SHIAB-05), so same-chirality mass requires an equivariance-breaking spurion the source action supplies. | DECLARATION (conditional) | canon/shiab-existence-cl95.md (SHIAB-05); yukawa-scoping-2026-07-13.md (control reproduction) | tests/yukawa-scoping/yukawa_trilinear_channels.py |

### Gravity / dark-energy sector (SA-G)

| ID | Requirement | Class | Source artifact | Test |
|---|---|---|---|---|
| SA-G1 | The soldering: theta pinned to spin-lift(grad^gimmel). Palatini variation does NOT force it (the action is a square of the distortion, not linear in curvature; H27, confidence HIGH). The source action must either force theta onto the spin-lift by a new mechanism or carry it as a declaration. Note: the soldering and the connection map are ONE datum, not two (codim-8165 in sp(64,H) is arithmetically identical to "image is a 91-dim so(9,5)"; wave34). | DECLARATION | explorations/wave10/H27-soldering-palatini-2026-07-11.md; wave34/source-action-landscape-scan-2026-07-11.md sec 1 | tests/wave10/H27_soldering_palatini.py (6/6); tests/wave34/soldering_codim_and_causal_window.py; spec-consistency block A |
| SA-G2 | mu_DW, the one free dimensionful scale (the gimmel geometry fixes ratios only, H24). The H36 identification mu_DW = DE scale is FALSIFIED (alpha = 1/3 at lambda in [60.0, 73.6] um excluded); current allowed window mu_DW >= ~3.4-4.8 meV (argued sub-mm edge), no experimental upper edge. | FIT (bounded) | explorations/track2-conditional-numbers-2026-07-13.md secs 1, 3 (S4; H36 refused); wave32/H53 (keystone status) | tests/track2/T2A_graviton_sector_numbers.py (8/8, exit 0); spec-consistency block F |
| SA-G3 | The B_i background coefficients (the theta-sector initial amplitude; the Willmore principle selects the section, not the perturbation amplitude). | FIT | explorations/wave19/H42-f0-preregistration-2026-07-11.md; track2-conditional-numbers-2026-07-13.md (gap g5) | tests/track2/T2B_dark_energy_curves.py (4/4, exit 0) |
| SA-G4 | f0 = rho_theta(0)/rho_Lambda(0), the sole data-facing DE knob: the ratio of two unbuilt amplitudes (B_i, mu_DW). Derivable only after H41 fixes the overall normalization pair; until then a FIT. | FIT (derived once SA-G2 + SA-G3 land) | wave19/H42-f0-preregistration-2026-07-11.md | tests/track2/T2B_dark_energy_curves.py |
| SA-G5 | The gravity ratio beta/alpha (\|II\|^2 vs \|II_0\|^2, the H45-vs-H48 fork): the residual shape-dimension-1 freedom of the whole allowed region. Bounded to a nonempty band by the m2_eff window + positivity; the conformal edge beta/alpha = -1/4 is excluded by the Stelle m^2 != 0 form. | FIT (bounded band) | explorations/wave35/source-action-carve-2026-07-11.md (Q3) | tests/wave35/source_action_carve.py (15/15, exit 0) |
| SA-G6 | The overall gravity coupling alpha > 0 (positivity boundary: the degenerate \|H\|^2 / alpha = 0 corner is excluded). | FIT (sign-bounded) | wave35/source-action-carve-2026-07-11.md (Q4 ablation) | tests/wave35/source_action_carve.py |
| SA-G7 | Resolution of the c_L background-vs-TT normalization band [3/8, 2] (computed value 3/8; band is the O(1) normalization ambiguity). | FIT | track2-conditional-numbers-2026-07-13.md (gap g3); wave31/H51 | tests/track2/T2A_graviton_sector_numbers.py |
| SA-G8 | Resolution of the m2_eff method band [5/6, 5/4] (normalization-gated, H25). | FIT | track2-conditional-numbers-2026-07-13.md (gap g4); wave7/H25 | tests/track2/T2A_graviton_sector_numbers.py |
| SA-G9 | A from-scratch GU linearization of the massive spin-2 sector WITH matter sources (beyond the imported Stelle 1978 solution): the action must make the matter coupling derivable, not imported. | FORCED | track2-conditional-numbers-2026-07-13.md (gap g1); wave22/H10 | tests/wave22/H10_ppn_weak_field.py |

### Count / field-space sector (SA-C)

| ID | Requirement | Class | Source artifact | Test |
|---|---|---|---|---|
| SA-C1 | The K-class field-space declaration: gamma-trace-constrained ker-Gamma field space -> carrier B (index -38, order-3 rho = (0,2,1), the unique index-changing published carrier: CAN select the count) vs full field space + BRST -> carrier A (index -42, 3-divisible: permits only, cannot select). Arithmetic provably cannot decide the bit (mutual-exclusion certificate); B-leaning lean under GU's commitments. B is FORCED CONDITIONALLY: if the source action is to count-select at all, it must name B. | DECLARATION (B forced-if-count-selecting) | explorations/wave16/H39-sourceaction-kclass-2026-07-11.md (Q1); wave17/H40 (Q1); wave35 carve (count-selection binds the bit to B) | tests/wave16/H39_sourceaction_kclass.py (14/14); tests/wave35/source_action_carve.py; spec-consistency block C |
| SA-C2 | The Porrati-Rahman causal-cure term. The built minimal operator's C2 = 155.3625 leakage is a REAL Velo-Zwanziger acausality (degree-1 homogeneous symbol norm, nonzero on any curved background): the cure is DEMANDED, not permitted; GU has the trigger, not the cure. The cure lives in a 1-real-parameter family (wedge - 6*contract, t* = -1/6, RT-TRACE-DICHOTOMY), causality fixes it to the unique point g = 1 (full ker-Gamma projection; leakage(g) = (1-g) C2), it closes on BOTH carriers (Gamma is so(9,5)-equivariant, so it does not p-hack SA-C1), and it must REVISE GU's written shiab (1,0,1,0), which is gamma-traceful. | FORCED | wave17/H40-terminal-sourceaction-2026-07-11.md (Q1 steps 1-4); wave34 landscape sec 2.2, ledger 6; wave35 carve (Q2) | tests/wave17/H40_terminal_sourceaction.py (14/14); tests/wave35/source_action_carve.py; spec-consistency blocks B, D |
| SA-C3 | The realized chiral rank: even with the cure and carrier B, the count is {1, 3}, not pinned (residue trap: a net index of exactly 3 has residue 0 mod 3, carrier A's residue, so no mod-3 datum certifies "3"). The source action must fix the realized rank. | DECLARATION | wave16/H39 (Q2); wave17/H40; RESEARCH-POSTURE.md operational frontier | tests/wave16/H39_sourceaction_kclass.py; spec-consistency block C |
| SA-C4 | Subprincipal-order causality: the 4D VZ evasion is CONDITIONALLY_RESOLVED at principal-symbol order only, and overturnable via FC-VZ-4 (the extrinsic curvature II_s sourcing spacelike characteristics; II_s is exactly the field in the action). The built cure term must survive this order. | FORCED (unbuilt check) | wave34/source-action-landscape-scan sec 2.1, sec 4.3; explorations/vz-evasion/* | -- (named unbuilt; no test exists yet) |

### UV / positivity / quantum sector (SA-U)

| ID | Requirement | Class | Source artifact | Test |
|---|---|---|---|---|
| SA-U1 | Loop-adequate dynamics: the H59 Krein loop-positivity question (does keep-and-grade [P,S]=0 make projected probabilities positive at the negative AF fixed ratio?) cannot even be POSED without the source action. The built action must supply the H59 minimum packet items it owns: renormalized [P,S]=0 (not tree-only), counterterm closure under P, an odd/internal ghost-parity loop rule, an IR regulator + inclusive observable layer, and ker-Gamma constraint closure under the loop calculation. | FORCED | explorations/H59-krein-loop-positivity-gate-2026-07-12.md (Minimum H59 Packet, items 2-8); h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md (flow-side evidence declared insufficient) | tests/W48_H59_krein_loop_positivity_gate.py (10/10); tests/W119_h59_frg_krein_negative_ratio.py (17/17) |
| SA-U2 | The ghost-mass convention fork: agravity (m2^2 rides the running coupling, Salvio-Strumia) vs GU-native fixed-scale (m2 = sqrt(m2_eff) mu_DW). A construction fork the source action would resolve; W119 computed both branches and isolated the dependence to the UV-endpoint behavior only (agravity: pinch onto the grading locus at the free endpoint; fixed-scale: stays clear, d_locus = m2_eff constant). | DECLARATION | h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md (sec 0 fork table, sec 4) | tests/W119_h59_frg_krein_negative_ratio.py |
| SA-U3 | The cure coefficient must satisfy the Krein-modified EFT positivity bound (AADNR-type convex cone, computable from the cubic vertex alone). The bound's Krein form is itself underived; but SOME sign-definite carve of the 1-parameter cure line is demanded by any causal, pseudo-unitary completion. | FORCED (bound; its precise form is a named open derivation) | wave34/source-action-landscape-scan sec 3.1, sec 5 (method 1) | -- (derivation of the Krein-modified bound is itself open) |
| SA-U4 | The RS field must be MASSIVE: Weinberg-Witten / Porrati soft theorems rule out a massless interacting spin-3/2 without a gauge (SUSY) partner; the massless branch is eliminated outright. Consistent with ledger m2 != 0. | FORCED | wave34/source-action-landscape-scan sec 3.3 | -- (literature-anchored branch elimination) |
| SA-U5 | The guardian fork: either exhibit a guardian symmetry (does Sp(32,32;H) + [P,S]=0 furnish a local-SUSY / super-IG guardian?) for a UV-complete interacting massive RS, or accept, openly, Rahman-cutoff finite-EFT status (finite content, no Regge tower: guardian-free is provably at best a finite-Lambda EFT). | DECLARATION (fork; either branch has FORCED consequences) | wave34/source-action-landscape-scan secs 2.3, 2.7, 2.8, 8; wave38/40/41 H54 guardian branches | tests/wave34/soldering_codim_and_causal_window.py (toy only) |

### Class tallies (pinned by spec-consistency block G)

- **FORCED: 8** (SA-Y1, SA-Y7a, SA-G9, SA-C2, SA-C4, SA-U1, SA-U3, SA-U4)
- **DECLARATION: 9** (SA-Y2, SA-Y5, SA-Y6, SA-Y8, SA-G1, SA-C1, SA-C3, SA-U2, SA-U5)
- **FIT: 10** (SA-Y3, SA-Y4, SA-Y7b, SA-G2, SA-G3, SA-G4, SA-G5, SA-G6, SA-G7, SA-G8)

Landscape anchor (wave35, imported not re-derived): with all ledger constraints imposed
JOINTLY, the allowed region is a FAMILY, shape-dimension 1, NOT a point and NOT empty.
Binding: causality (fixes the cure to g = 1), count-selection (fixes the bit to B),
m2_eff + positivity (bound the shape). Redundant given the rest: Krein [P,S]=0
(auto-satisfied, 2-primary sign-blind) and soldering (even-sector, orthogonal). The residual
is exactly: the gravity ratio beta/alpha (SA-G5) plus two free scales (SA-G2 mu_DW,
SA-G6 alpha).

---

## 2. Persona 2 (representation theorist): cross-consistency of the FORCED set

Question: can ONE operator simultaneously satisfy all eight FORCED items? Checked at the level
of established Hom-space and index results; anything computable is in the companion test.

**Global anchor (not new here).** Wave35's joint carve already computed that causality
(SA-C2), count-selection (SA-C1 at B), positivity (SA-G6), the m2_eff window (SA-G8's band),
Krein, and soldering are JOINTLY satisfiable: the region is NONEMPTY. EMPTY is falsified.
That is the master consistency result this spec inherits.

**Check 1: g = 1 ker-Gamma cure vs the k = 0 Yukawa channel.** No contradiction, by sector
disjointness. The cure acts on the RS carrier (spinor-valued 1-forms, dim 14 x 128 = 1792;
ker Gamma = 1664 = 1792 - 128), while the Dirac-Yukawa channel lives in
Hom(S x S, Lambda^0) over the 128-dim spinor module; these are distinct Hom spaces over
distinct carriers, and both dimension books close independently (test blocks B). The
generation triplet (192 = 3 x 64) that the reduced Yukawa texture rides sits INSIDE ker
Gamma, so restricting to carrier B's field space keeps, rather than kills, the texture
computation's home. No Hom-space clash.

**Check 2: the cure vs the carrier-B declaration.** No contradiction and no circularity:
Gamma is so(9,5)-equivariant (residual exactly 0, wave35), so the cure closes on BOTH
carriers; causality fixes g and is blind to the A/B bit. The FORCED cure therefore does not
p-hack the DECLARATION it sits next to. (This is H40's "forces the cure, not the carrier",
surviving the joint carve.)

**Check 3: FN sterility (FORCED negative inside SA-Y5) vs the larger-symmetry escape.** The
escape route is arithmetically open and compatible with the built Z/3: integer charges beyond
mod 3 that REDUCE to rho = (0,2,1) exist (e.g. (0,2,4)) and genuinely grade the cross-paired
invariant entries (integer exponent 6 -> eps^6 suppression) while the democratic entry stays
ungraded (test block E). So "the built structure cannot supply the hierarchy" and "a
source-action-imported larger symmetry can" are consistent statements, not a contradiction;
the import must merely be compatible with the derived Z/3 as its mod-3 reduction.

**Check 4: SA-U4 (massive RS) vs SA-G2 (free mu_DW) vs the refused H36.** Consistent: the
mass rides the free scale (m2 = sqrt(m2_eff) mu_DW on the GU-native branch), massiveness only
needs mu_DW != 0, and the falsified H36 point (2.94 meV) sits strictly below the allowed
floor band (3.4-4.8 meV), which is exactly why the window formulation replaced the
identification (test block F).

**Check 5: SA-C2 (g = 1 kinematic projector) vs the Porrati-Rahman template (F-analytic
vertex).** Not a contradiction, but a NAMED construction fork, already tabled in
GEOMETER-VS-PHYSICS-OBJECTS.md (row: RS cure / soldering): the geometer's equivariant
ker-Gamma projector matches de Wit-Freedman on 4/5 axes, and the differing axis is the
guardian axis, i.e. exactly SA-U5. The FORCED items coexist; the fork is carried, not hidden.

**Verdict: NO outright algebraic contradiction found among the FORCED items.** The FORCED
set is mutually consistent at the level of everything established. (A found contradiction
would have been the headline; the honest result is that wave35's nonemptiness extends to the
newly enumerated Yukawa-side FORCED items by sector disjointness.)

---

## 3. Persona 3 (higher-spin / causality specialist): the cure term in detail

What SA-C2 + SA-U3 jointly demand of the build, per the wave34 literature scan and the
wave35 carve:

1. **The family.** The constraint-preserving coupling space is NOT a free tensor space: the
   RT-TRACE-DICHOTOMY pins it to the 1-real-parameter family contract + t*wedge with
   t* = -1/6 (proportional to wedge - 6*contract). The written canon shiab (1,0,1,0) is
   gamma-traceFUL (||Gamma . shiab_contract|| = 215.85 != 0): "reconstruct GU as written" and
   "make it causal" are jointly unsatisfiable, and the build must pay that revision openly.
2. **The point.** In the minimal cure basis the leakage law is exactly
   leakage(g) = (1-g) C2, so causality has a UNIQUE solution, g = 1, the full ker-Gamma
   projection; the extended 3-basis confirms the leakage map is rank 1 (two leakage-blind
   directions are parametrization gauge, not physics). Caveat carried from wave35: the
   cure-basis SIZE is a modeling choice standing in for the unbuilt full non-minimal
   construction; "point" is robust to the two bases tested, not proven over every
   conceivable coupling.
3. **The template.** Porrati-Rahman 2009 is the existence proof that a non-minimal completion
   CAN restore constraint invertibility and causality for charged massive spin-3/2; it
   transfers in structure, not verbatim (Abelian flat background there; non-Abelian Sp on
   curved Y14 here). The GU-native realization is the equivariant projector, not the
   F-analytic vertex (the named fork, Check 5 above).
4. **What positivity carves.** An AADNR-type forward-amplitude bound computed from the cubic
   cure vertex alone turns the 1-parameter line into a sign-definite region; it is the
   cheapest discriminator on the menu. In GU it must be the KREIN-modified variant
   (pseudo-unitary, [P,S]=0-graded inner product), and deriving that modified bound is
   itself a construction-phase task; asserting the unmodified bound would silently default
   the construction fork.
5. **The price of no guardian.** Even a causal cure yields, guardian-free, at best a
   finite-cutoff EFT (Rahman helicity-1/2 strong coupling; no Regge tower in GU's finite
   content to soften it). Clean high-energy behavior wants g_gyro = 2. So the cure term's
   requirements bifurcate on SA-U5: guardian found -> gravitino-template UV story; no
   guardian -> the spec must carry "Lambda-bounded EFT" as the honest completion status,
   with mu_DW the plausible cutoff-setting scale (structural link, not yet computed).
6. **The unbuilt order.** All of the above is principal-symbol; SA-C4 (subprincipal FC-VZ-4,
   the II_s-sourced characteristics) is where the evasion is won or lost on the curved
   background, and no test for it exists yet. It is the sharpest single gap in the FORCED
   set.

---

## 4. Persona 4 (Lakatos / honesty auditor): progressive vs self-granted freedom

The E1 rule stands: this spec is a MAP. Enumerable requirements are not satisfied
requirements. Classification of the ledger's epistemic direction:

**Progressive (the object got MORE constrained; each is a theorem-grade narrowing):**

- Non-form Higgs carriers eliminated; Majorana scalar channel eliminated (SA-Y1).
- The spurion TYPE forced to a doublet (SA-Y7a).
- Mod-3 FN engines proven sterile: the built structure cannot fake a hierarchy (inside SA-Y5).
- The massless-RS branch eliminated (SA-U4).
- The cure forced to exist and pinned to a point in every basis tested (SA-C2).
- Soldering and connection map collapsed to ONE declaration (inside SA-G1).
- H36 falsified, honestly retired, replaced by a window (inside SA-G2).
- The count arena narrowed to {1,3} with the residue trap made explicit (SA-C3's frame).
- The joint region proven NONEMPTY and NOT-A-POINT: neither kill nor forcing was
  manufactured (wave35).

**Freedom the program is granting itself (degenerating pressure; each is a knob the object
must either derive or openly carry):**

- Three free complex couplings OR an imported larger flavor symmetry + flavon + small
  parameter (SA-Y4/SA-Y5): the entire fermion mass hierarchy.
- The sector-to-flavor assignment (SA-Y6) and spurion values (SA-Y7b).
- The soldering declaration (SA-G1), the A/B bit (SA-C1), the realized rank (SA-C3).
- mu_DW, B_i, f0, beta/alpha, alpha, c_L, m2_eff normalizations (SA-G2..G8): every
  data-facing number.
- The guardian fork unresolved (SA-U5) and the ghost-mass convention unresolved (SA-U2).

The honest reading: 8 FORCED items give the object a rigid shape; 9 DECLARATIONS + 10 FITs
are the freedom that keeps it, today, a framework rather than a theory
(predictive-boundary-audit: compression result, not prediction result). The spec's value is
that the freedom is now FINITE, NAMED, and CLASSIFIED; its danger is that a build could
quietly consume the declarations as fits. The Clean Prediction Rule is the guard.

---

## 5. Persona 5 (systems expositor): dependencies, tensions, acceptance

### 5.1 Dependency graph

```
SA-G1 (soldering decl) ----------------+
                                       |   (even sector; orthogonal to cure carve, wave35)
SA-C1 (A/B bit) --[B if count-selects]-+--> the field-space declaration layer
       ^                               |
       | (blind to bit)                v
SA-C2 (cure, g=1) --> SA-C4 (subprincipal survival) --> SA-U3 (Krein positivity carve)
       |                                                        |
       +--> SA-U5 (guardian fork) <-----------------------------+
                 |                                (UV status of the cured operator)
                 v
SA-U1 (H59 loop packet)  <-- SA-U2 (ghost-mass fork; UV endpoint only)
                 |
                 v
        loop-level [P,S]=0 verdict (H59, OPEN)

SA-G2 (mu_DW) --+--> SA-G4 (f0)          SA-G5 (beta/alpha) <-- SA-G8 (m2_eff band)
SA-G3 (B_i) ----+                        SA-G6 (alpha>0), SA-G7 (c_L) --> DE numbers
SA-G9 (matter coupling) --> PPN/GW channels (track2 ledger rows 1-7)

SA-Y1 (form carrier, FORCED) --> SA-Y2 (which k / which fork) --> SA-Y3 (vev)
SA-Y4 xor SA-Y5 (couplings vs mechanism) --> SA-Y6 (flavor map)
SA-Y7a (doublet type) --> SA-Y7b (values);  SA-Y8 conditional on same-chirality masses
(Yukawa sector is Hom-space disjoint from the SA-C cure sector: spec-consistency B6)
```

Reading: three near-independent supply clusters (field-space/cure, gravity scales, Yukawa),
coupled only through (i) mu_DW appearing in both the gravity FITs and the ghost-mass /
cutoff story, and (ii) the guardian fork gating the UV status of everything.

### 5.2 Open contradictions and tensions

**Contradictions found: NONE** (Section 2; wave35 nonemptiness + the new disjointness and
lift checks). **Tensions carried, five, all pre-existing and here consolidated:**

1. **Written-shiab vs causality (SA-C2):** the cure must revise the canon (1,0,1,0) formula;
   reconstruction-as-written and causality cannot both be kept (wave34 sec 4.3).
2. **Guardian-free UV boundedness (SA-U5):** finite content + Rahman cutoff means no
   guardian -> no UV-complete interacting massive RS; tension with any "complete unification"
   reading, and with the flow-side Gaussian-FP picture if the RS sector's cutoff undercuts
   the trans-Planckian flow (different truncations; flagged, not adjudicated).
3. **H45-vs-H48 (SA-G5):** full |II|^2 (beta = 0) vs conformal uniqueness pull in different
   directions inside the allowed band; the residual shape-dim-1 freedom IS this tension.
4. **Anti-gauge-fixing posture vs Stueckelberg/BRST machinery (SA-C1 side A):** cure A needs
   a local fermionic invariance GU-as-stated does not state; the Zinoviev/BKP technology
   would have to be GU-native, not imported (wave34 secs 2.5-2.6).
5. **Swampland-adjacent (SA-U5/SA-G2):** no tower + large free mu_DW excursions sit
   awkwardly with distance-conjecture expectations if GU is embedded in a QG landscape;
   speculative tier, named in wave34 sec 3.5, carried unresolved.

### 5.3 Acceptance criterion: what would count as BUILDING the source action

A build is accepted as "the source action exists" when there is an explicit action
functional on an explicitly declared field space that: (a) contains a concrete non-minimal
term realizing the g = 1 ker-Gamma cure whose VZ leakage vanishes on the actual operator AND
survives the subprincipal FC-VZ-4 check on the curved background (SA-C2, SA-C4); (b) states
every DECLARATION row either as a derived consequence of the action (with the derivation
exhibited) or as a named postulate in the action's definition, with no declaration silently
consumed (SA-Y2/Y5/Y6/Y8, SA-G1, SA-C1/C3, SA-U2/U5); (c) emits, or names as free, every
FIT row, with any emitted number produced source-first per the Clean Prediction Rule (no
target imports: no 3, 24, chi(K3), observed SM algebra, DESI values, or GR success as
inputs) and recorded before target comparison (SA-Y3/Y4/Y7b, SA-G2..G8); (d) supplies the
H59 loop packet items it owns so that loop-level [P,S]=0 becomes a computable question
rather than a slogan (SA-U1); and (e) passes, unmodified, the already-standing machine
checks this spec consolidates (the channel table, the leakage law, the carve, the window
arithmetic). Anything less is a partial fragment; anything that meets (a)-(e) but emits
zero prediction-grade numbers is a completed CONSTRUCTION whose predictive standing is then
judged separately, per the E1 rule, by whether at least one FIT row becomes a
prediction-grade emission.

---

## Honest limits

- This is consolidation: every physics claim above lives in, and at the grade of, its cited
  artifact; nothing is upgraded by appearing here.
- The requirement list is complete against the artifacts named in the frontmatter as of
  2026-07-13; a leg not yet run (e.g. a future SM vacuum-selection wave) may add rows.
- The class boundaries are judgment at the margins (e.g. SA-U3 is FORCED as a bound whose
  precise Krein form is underived; SA-C1 is a DECLARATION carrying a conditional forcing).
  The composite rows are split precisely so no single cell hides a mixed status.
- The cross-consistency verdict is bounded by what is established: "no contradiction at the
  level of established Hom-space and index results" is not "the build exists" nor "the build
  is consistent to all orders".

*Filed 2026-07-13. Five personas run inline in one session (EFT theorist, representation
theorist, higher-spin/causality specialist, Lakatos/honesty auditor, systems expositor).
Reproducible: `python tests/spec-consistency/source_action_requirements_consistency.py`
(33/33, exit 0). Exploration-grade; promotion, if any, goes through the runbook; no canon
movement here.*

---

## Status note (append-only, 2026-07-13, W125)

The first build attempt against this spec was run the same day
(explorations/W125-source-action-first-build-2026-07-13.md). One row's status moves:

- **SA-C4** (subprincipal FC-VZ-4 survival): was "FORCED (unbuilt check), no test exists".
  A test now exists: `tests/W125_sac4_subprincipal_built.py` (9/9, exit 0). For the BUILT
  g = 1 ker-Gamma candidate (constant equivariant projector, carrier B) the verdict is
  **TEST-BUILT-PASSES at principal + subprincipal symbol order** on the flat 14-dim model
  (characteristic variety exactly the eta(9,5) null cone; zeroth-order II_s inserts provably
  subprincipal because the constant projector cannot mix symbol degrees; a first-order-insert
  positive control shows the failure mode is detectable, with a finite causal window). The
  row stays FORCED; the curved-Y14 clause of acceptance leg (a) remains open; the repo-level
  VZ verdict (CONDITIONALLY_RESOLVED) is not upgraded.

No other row's class or status changes. The acceptance criterion (5.3) was attempted and is
NOT met: W125's scorecard is (a) PARTIAL, (b) PASS, (c) PASS with zero prediction-grade
emissions, (d) PARTIAL, (e) PASS -- a symbol-level construction skeleton, per the E1 rule a
construction, not progress; gated numbers unlocked: NONE.

## Status note (append-only, 2026-07-14, W131)

The covariant operator on Y14 (the single object W125 named as blocking legs (a)-full and
(d)-full, SA-G9's arena, and FC-VZ-1) was built at the frame/symbol level
(explorations/W131-covariant-operator-y14-2026-07-14.md;
`tests/W131_covariant_operator_y14.py`, 12/12, exit 0). Status movements:

- **SA-C4, curved-Y14 clause**: was "rides an argued (cited) reduction, not a bundle
  computation" (W125 scorecard leg (a)). Now MACHINE-CHECKED at symbol level on curved Y14:
  [nabla, Pi] = 0 exactly (Gamma is so(9,5)-equivariant on all 91 generators, boosts
  included, so Pi is parallel for every metric-compatible connection); the pointwise
  characteristic variety on the actual gimmel geometry (signature (9,5) verified on the
  Lorentzian locus) is the gimmel null cone; every covariantization-generated zeroth-order
  insert (curvature, II_s) is subprincipal BY so(9,5) MEMBERSHIP and Pi-commuting. The
  reopening condition is exact: a non-metric symmetric FIRST-order insert (outside the
  algebra), which the built candidate does not contain.
- **SA-U1, tree leg**: nabla K = 0 exactly (Krein parallelism, all 91 generators); the
  covariant operator including connection terms is Krein-self-adjoint. The renormalized
  [P,S] = 0 question and the loop-arena items remain open, now blocked ONLY on the analytic
  layer (propagator/Fredholm theory on non-compact Y14), no longer on the operator itself.

The row classes do not change; SA-G9 does not move; no FIT row moves; gated numbers
unlocked: NONE (per the E1 rule W131 is a construction). Preconditions inherited and named:
X4 spin (canon W2-01), gimmel nondegeneracy on the Lorentzian locus (pointwise-verified).

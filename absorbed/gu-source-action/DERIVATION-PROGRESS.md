---
title: "Source Action Construction — Derivation Progress"
started: 2026-06-27
status: in_progress
parent: ../gu-formalization
target: SPEC.md
---

# Source Action Construction — Derivation Progress

Running ledger for the construction of GU's missing RS/IG source action. Same discipline as the parent
`gu-formalization`: compute -> adversarially verify -> land only what survives; record honest negatives.

> Inherited starting state (from the parent campaign, 2026-06-24..27): the RS BV bicomplex is built and
> verified; the final obstruction C2 (= 155.36, Gamma-independent) is isolated, proven GLOBAL, and proven NOT
> an index; the three missing global objects (families pushforward, boundary holonomy/spectral section,
> BV-to-boundary-Dirac map) are named in SPEC.md section 5. The natural characteristic class is -5376, not 24.

---

### SEED — repo scaffolded (2026-06-27)

Created the construction repo as a child of gu-formalization. Wired `lib/gu_bridge.py` to the verified parent
machinery (the Cl(9,5)=M(64,H) rep, the gamma-trace constraint, C2, the bicomplex); `tests/test_bridge.py`
reproduces the anchors (bare commutator 58.72, C2 155.36). SPEC.md = the target; DEAD-ENDS.md = the killed
approaches not to re-walk. No construction attempted yet.

**Next:** the first genuine construction attempt is SPEC.md item 5(iii) — the BV-to-boundary-Dirac map —
since C2 is proven not-an-index and not-local, this is the structurally-required bridge. Any attempt must
respect the four guards and the DEAD-ENDS list, and must not import the target.

---

### LENS-01 - Cryptoeconomic security-budget source action (2026-06-27)

Added `CRYPTOECONOMIC-SOURCE-ACTION.md` as the current front-door candidate lens. The idea:

```text
source action = adversarially priced rule for finalizing admissible geometric extensions
```

This does not claim a construction. It gives the search a concrete minimax normal form:

```text
Score(phi) = GrowthValue(phi)
             - ValidationCost(phi)
             - FinalizationCost(phi)
             - WorstCaseAdversarialLoss(phi)
```

where the adversary is the space of rival GU completions, not a human attacker. Added
`lib/security_budget.py` and `tests/test_security_budget.py` as a small executable scaffold for candidate
selection surfaces. The hard next step is to replace toy loss channels with GU-native computable channels
from the parent repo objects.

---

### LENS-02 - 25-persona divergent lens vote (2026-06-27)

Added `PERSONA-LENS-VOTE-2026-06-27.md` and `tests/test_persona_lens_vote.py`. The exercise forced 25
different lenses to make independent top-3 recommendations, then used a 3/2/1 vote to prioritize the
workstreams.

Vote result:

```text
1. B - GU-native minimax loss channels        20 points
2. C - boundary spectral-section/finality     18 points
3. A - BV-to-boundary-Dirac carrier           17 points
4. I - anti-import adversarial oracle         14 points
5. D - families pushforward/cobordism index   12 points
```

The actionable consensus is a triad:

```text
source-action search = GU-native minimax loss channels
                       + boundary finality carrier
                       + adversarial anti-import oracle
```

This does not supersede `SPEC.md`; it sets the next prioritization rule for construction attempts.

---

### LENS-03 - GU-native loss-channel interface (2026-06-27)

Added `lib/loss_channels.py` and `tests/test_loss_channels.py`.

The interface enforces the rule selected by LENS-02: a loss channel must either compute from current
GU-native objects or fail loudly with a named missing carrier. The first computable channels are:

```text
L_boundary_symbol  - computes the BV-to-boundary symbol/Hessian carrier.
L_boundary_index   - computes the eta=0 APS-index obstruction for that carrier.
L_target_import    - fatal guard for known target imports.
L_acausal_trap     - fatal guard for bare-commutator/acausal decoupling traps.
```

The boundary result is intentionally double-edged: the BV-to-boundary-Dirac map exists at the
symbol/Hessian level, but the APS index route fails because the chiral grading forces eta to zero. So
`C2` is currently carried as a Hilbert-Schmidt symbol norm, not as a spectral-section index.

Missing-carrier channels now raise `MissingCarrierError` instead of pretending to compute:

```text
L_anomaly
L_RS_BRST
L_theta_source
L_weak_field
L_families_pushforward
```

---

### CONSTRUCT-01 - first 5 construction steps: the BV-to-boundary-Dirac MAP holds (M_KT = N*D_Sigma^2), but the index half is forced shut (eta=0); a new obstruction-theorem (2026-06-27)

First concrete construction work: 5 SEQUENTIAL steps on workstream A (BV-to-boundary-Dirac = SPEC item 5(iii) = persona-vote #3), each computed on the explicit Cl(9,5) rep via `lib/gu_bridge.py` and adversarially framed. (The orchestration crashed near the end but wrote all 5 step tests; re-run + verified in the main loop. Step 1's heavy 196-pair Gram loop was made exact-but-fast via the Frobenius inner product.) Genuine mixed result: half built, half forced shut, plus a sharp new theorem. Guards held throughout (bare commutator 58.72 untouched; no target import).

**ADVANCE - the bridge holds at the operator level.**
- Step 1 (`tests/step1_c2_dirac_symbol.py`): C2's escape E(xi) = sum_a xi_a E_a, E_a = (I-Pi_RS)(id_14(x)e_a)Pi_RS, is a genuine first-order symbol; its Frobenius Gram M_ab = <E_a,E_b> is EXACTLY Euclidean (kappa*I, kappa=33.96, residual 0.0 -- NOT the (9,5)-Lorentzian kappa*diag(ETA), rel resid 0.96), and C2(xi) = K*|xi| is PERFECTLY ISOTROPIC (K=21.80, 0.0% directional spread, C2(2xi)/C2(xi)=2.000000). So the boundary symbol is Euclidean-ELLIPTIC and C2 is a pure scalar-magnitude first-order symbol.
- Step 2 (`tests/step2_boundary_dirac.py`): the boundary Dirac D_Sigma is EXACTLY self-adjoint (0.0e+00), full rank 128, Euclidean-elliptic (sigma_min=0.4949 bounded from 0 over all directions), and it does NOT degenerate on the (9,5) physical light cone - it is Euclidean-elliptic, not Lorentzian-hyperbolic.
- Step 4 (`tests/step4_mkt_vs_dirac_square.py`): **M_KT = N*(D_Sigma^2)|_surface EXACTLY** (rel 8.6e-16; N=14 = Gamma Gamma^dag tight-frame constant, a-priori, not fitted), and trace(M_KT) = C2^2 => sqrt(trace) = 155.3625 = C2. So D_Sigma is the square-ROOT of the Koszul-Tate Hessian: the BV-to-boundary-Dirac MAP (SPEC 5(iii), first half) is genuinely built at the full OPERATOR level, beyond Step 1's symbol level.

**HONEST NEGATIVE - the index half is forced shut.**
- Step 3 (`tests/step3_spectral_section.py`): eta(D_Sigma) = 0, FORCED by the anticommuting chiral grading G = Pi_RS - Q ({G, D_Sigma} = 0 to 5.5e-14); spectrum mirrored about 0; eta = 0 over all 20 tested xi (12 random + 8 null-cone). The spectral section is TRIVIAL (symmetric +/-), exactly as the parent flat operator.
- Step 5 (`tests/step5_synthesis.py`): SPEC 5(iii)'s required clause "APS spectral section connects to C2 (eta != 0)" FAILS. C2 is a degree-1 SYMBOL norm (a magnitude = sqrt(trace M_KT)), living in the singular-value SCALE of D_Sigma, NOT a sign-asymmetry / index.

**NEW OBSTRUCTION-THEOREM (the genuine product).** Any boundary Dirac whose square is the (positive) Koszul-Tate Hessian inherits an anticommuting chiral grading, hence eta = 0, so C2 can NEVER be its APS index. This independently re-derives the parent's "C2 is not an index" BY CONSTRUCTION and with the MECHANISM, and converts SPEC 5(iii) from open to a precise theorem-shaped wall.

**NEXT:** break the grading - a curvature/connection term that fails to anticommute with G, or a non-self-adjoint / non-chiral boundary operator - OR abandon the index reading and pursue C2 as a genuine first-order SYMBOL invariant (its natural home per steps 1+4). The latter is workstream A converging toward C (the boundary-symbol carrier), consistent with the persona vote.

---

### CONSTRUCT-02 - the grading-break DECISION: eta=0 is NOT symmetry-protected; CONSTRUCT-01's wall is SOFT (GO) (2026-06-27)

The decisive go/no-go from the 7-lens synthesis (the single crux five lenses converged on): is CONSTRUCT-01's eta=0 a one-operator accident or symmetry-protected over the whole admissible class? Computed on the explicit Cl(9,5) rep via `lib/gu_bridge.py` (`tests/step6_grading_break_decision.py`, runs clean, all guards + symmetry assertions pass, deterministic seed). Guards held throughout (bare commutator 58.72 untouched - every perturbation is added to the boundary operator D_Sigma, M_D is never modified; all breakers a-priori; no target import).

**(A) Altland-Zirnbauer class of D_Sigma = CII (all exact).** Built the COMMUTING quaternionic structure J of M(64,H) (J antiunitary, J^2=-1, H-linear: max_a ||U conj(e_a) - e_a U|| = 4.8e-12) as the +1 eigenoperator of the Clifford-averaging superoperator. Lifting J_full = id_14 (x) J gives three exact symmetries of D_Sigma: T = J_full (TRS, T^2 = -1, [T,D] = 1.2e-11), S = G (chiral, {G,D} = 5.5e-14), C = J_full . G (PHS, C^2 = -1, {C,D} = 1.2e-11). So D_Sigma sits in class **CII**. The genuine product: it is the **particle-hole symmetry C (C^2 = -1), not the chiral grading alone, that FORCES eta = 0** - C pairs every +lambda with a -lambda. (T^2 = -1 only forces Kramers DOUBLING; every eigenvalue in this run is exactly doubly degenerate.)

**(B) THE DECISION (GO).** A grading-breaking perturbation is a G-DIAGONAL (G-commuting) Hermitian term Delta; the guard-admissible class is {a-priori, H-linear ([J_full, Delta]=0), non-equivariant, anti-trap}. Tested eta(D_Sigma + t*Delta) over t in [0,2]:
- the NATURAL breaker Delta_nat = the G-diagonal Hermitian part of M_D itself keeps **eta = 0 for ALL t** - it pushes the spectrum symmetrically AWAY from zero (nearest |lambda| ~ 6 at t=1); it is the special, non-generic case;
- GENERIC admissible breakers carry **genuine spectral flow eta = +/-4** - a fine t-scan shows a Kramers pair of eigenvalues crossing zero (e.g. -0.00055 -> +0.00033 at t~0.65) and crossing back (t~1.15), with a clean gap from the rest of the spectrum (real flow, not tol noise). eta is even throughout (quaternionic Kramers), as required.

**NEW THEOREM-SOFTENING (the genuine product).** eta = 0 is **NOT symmetry-protected**: it is forced only by the C-PHS of the BARE chiral D_Sigma, and that PHS is broken ({C, Delta} != 0) by any guard-admissible grading-breaking term lying OUTSIDE the M_D-symmetric family. So CONSTRUCT-01's "theorem-shaped wall" is **SOFT**: the index route is revived (as a spectral-flow / odd K^1 invariant, consistent with the surviving NCG proposal) the moment such a connection is supplied. This pins the entire remaining index question to ONE well-posed object: which a-priori grading-breaking connection the real **Y14 boundary holonomy (SPEC 5(ii))** supplies. GO converts the open construction of the index into a constrained, finite search instead of open invention.

**HARD BAR UNCHANGED.** Reviving the index does NOT produce a generation count: ch2(S_X)[K3] = -5376 (not 24) still stands, and the spectral flow is in the auxiliary strength t, not yet a geometric parameter (so eta is a Kramers-even / 4Z spectral-flow quantity, not yet a free integer). GO means the remaining index question is well-posed and the wall is soft - NOT "three generations."

**NEXT:** (1) replace the auxiliary t by the actual a-priori Y14 boundary connection (SPEC 5(ii)) and ask whether the geometry selects a breaker in the flowing class or the M_D-symmetric (eta=0) one - this is now the single decisive object. (2) Characterize the revived invariant properly (Kramers-even spectral flow / mod-2 vs free integer) before any count is read - feeds Tier-1 move 2 (degree-0 ratio-sector integer-freeness). (3) The hard bar -5376 is the independent second gate and is untouched by this result.

---

### CONSTRUCT-03 - the revived index is a CANONICAL integer eta_inf = sig(Delta), but CONNECTION-dependent (2026-06-27)

Follow-through on CONSTRUCT-02's GO: how strong is it - canonical net index or path-dependent fuzz? Computed on the bridge (`tests/step8_grading_flow_character.py`), guards held. **Adversarially verified** (workflow, agent ran an independent t->2000 counter-computation); the first draft mis-stated the mechanism and was corrected.

- **First-order null:** sig(P_ker Delta P_ker) = 0 for the natural AND every generic admissible breaker. D_Sigma's 1536-dim kernel splits SYMMETRICALLY to first order, so eta does not flow at small t; the flow is a finite-t level-crossing.
- **CANONICAL LIMIT (the corrected, stronger result):** eta(D + t*Delta) has a clean, numerically-stable t->infinity limit equal to **sig(Delta)** - the signature of the grading-breaking connection itself - flat from t ~ 50 (verified t = 50, 200, 1000; adversary confirmed flat to t = 2000, 11/11 breakers). The multi-crossing seen at MODERATE t is only a transient, NOT the obstruction to canonicity (the first draft wrongly called the limit "numerically delicate / limit-less"; the counter-computation refuted that).
- **Non-canonicity is PATH-DEPENDENCE, not fuzz:** sig(Delta) ranges over {0, +/-4, +/-8} across the admissible class (Kramers-even). The revived index is canonical PER CONNECTION but its VALUE is set entirely by WHICH grading-breaking connection is chosen - a datum the rep leaves free.
- **Protected exception:** the natural breaker (M_D's own G-diagonal) has sig(Delta) = 0 and keeps eta = 0 for all t (the measure-zero protected case). Flow is generic (8/8 transient over [0,6]; adversary 10/10 over [0,8]; no positive-measure non-flowing admissible set found).

**Reading:** the GO is real and SHARPER than first stated - the soft wall yields a genuine canonical integer index eta_inf = sig(Delta), not fuzz. But that integer is CONNECTION-DEPENDENT; the rep fixes no value. A generation count needs the geometry to supply a CANONICAL grading-breaking connection (a strictly stronger demand on SPEC 5(ii)'s Y14 holonomy), and even then sig(Delta) is an EVEN integer the rep's algebra never honestly pins to 3 (see CONSTRUCT-04).

---

### CONSTRUCT-04 - degree-0 integer-freeness: no honest scale-invariant Dirac integer (the unreachability leg) (2026-06-27)

Because CONSTRUCT-02 softened the eta=0 wall, the program's terminal now rests on a different question: even WITH a revived index, can an honest INTEGER - let alone 3 - be extracted from the existing bridge data without importing it? Computed on the bridge (`tests/step7_integer_freeness.py`), guards held. **Adversarially verified** (workflow, two agents ran independent counter-computations; survives both prongs; no import-target hit on {3,4,8,24} as a derived invariant).

- **PRONG 1 (rank/dimension prime spectrum):** every native Cl(9,5) dimension is {2,7,13}-smooth (128 = 2^7, 14 = 2.7, 1792 = 2^8.7, 1664 = 2^7.13, Spin(9,5) = 91 = 7.13, ...). The prime **3 is ABSENT** from the rep's dimension spectrum, so no REP-NATIVE rank/count equals 3.k. (GU GEOMETRIC quantities can carry 3 - dim SO(3,1) = 6, self-dual 2-forms = 3 - but those are external, not rep dimensions; 3 is exactly what must be imported.)
- **PRONG 2 (degree-0 ratio sector):** of the xi-independent degree-0 RATIO invariants of {Pi, Q, M_D(xi), Gamma}, every Dirac-content one is a NON-INTEGER algebraic number - a surd/rational over {2,7,13}: C2/bare = sqrt(7), bare/||E|| = sqrt(2), tr(Pi Md M Pi)/tr(M_KT) = 7/2, ... NONE equals an import target. The only integers in the ratio sector are trivial tight-frame 1's.
- **Scope/honesty (after adversarial counter-computation):** broadening to rank/signature counts DOES yield integers (rank M_D = 1792, npos(Pi M_D Pi) = 832, ...), but those are conjugation-invariant DIMENSION counts with no geometric Dirac content. The ONE genuine degree-0 Dirac-content integer is the metric signature tr(sign(e_a^2)) = 9 - 5 = **4** - flagged as a STRUCTURAL INPUT (the chosen (9,5) signature, the prong-1 analog), not derived, and it is 4 not the target 3. The prime 3 also appears in irrational DENOMINATORS of ratio-squares (sqrt(7/24)); that only makes them more irrational, never an integer.

**Combined verdict:** no honest scale-invariant INTEGER with Dirac content lives in the bridge data. So even CONSTRUCT-03's revived (soft-wall) index cannot by itself deliver "3": any honest 3 must arise as a genuine EXTERNAL topological/families index over the Y14/K3 geometry (carrying the foreign prime 3); producing it from the rep alone is a target import. EVIDENCE, not proof - bounded by this finite low-word-length catalog.

---

### SYNTHESIS (CONSTRUCT-02/03/04) - the program now bottlenecks on ONE external object

The three results converge. CONSTRUCT-02 + 03 show the eta=0 wall is SOFT and the index revives as a canonical integer eta_inf = sig(Delta), but its value is set by the (unbuilt) grading-breaking connection, not the rep. CONSTRUCT-04 shows the rep's own data contains no honest scale-invariant Dirac integer - the count's prime 3 is simply not present. So BOTH the "revive the index" route and the "read off the count" route now point at the SAME single missing object: **SPEC 5(i)+5(ii), a canonical families index / Y14 boundary holonomy over the metric fiber GL(4,R)/O(3,1)**, which must simultaneously (a) supply a canonical grading-breaking connection and (b) carry an external topological integer divisible by 3. Everything internal to the rep is now exhausted; the remaining frontier is entirely this one external geometric construction (consistent with the parent capstone's "needs new physics"). All three landed results survived adversarial counter-computation (high confidence).

---

### CONSTRUCT-05 - the decisive experiment: the natural geometric connection gives index ZERO (the escape closes) (2026-06-27)

Direct test of the synthesis frontier: does the natural EXTERNAL geometric connection actually deliver a nonzero generation index? The natural source of '3' in 4-manifold geometry is the self-dual 2-forms Lambda^2_+ = rank 3 (su(2)_+ of Spin(4)), which act asymmetrically on chirality - exactly the grading-breaking shape CONSTRUCT-03 needs. Built on the bridge (`tests/step9_selfdual_connection_index.py`), guards held; no target import (the connection is built from Clifford 2-form data, never fitted).

The geometric connection on the RS vector-spinor is the so(9,5) generator acting on BOTH indices: J_ij = M_ij (x) id_128 + id_14 (x) sigma_ij. (First draft used only the spinor part id_14 (x) sigma and was incomplete; the full vector+spinor action is the correct geometric object.)

- **Every METRIC so(9,5) connection gives index ZERO.** All 3 self-dual J+ (which carry the geometric '3' of Lambda^2_+), all 3 anti-self-dual J-, generic su(2)_+ combos, random general so(9,5) elements, AND quadratic enveloping-algebra products: **sig(Delta) = 0** in every case.
- **CONTRAST (pipeline sanity):** structureless NON-(metric-algebra) H-linear breakers DO flow (sig in {0, +/-4}); and (from adversarial verification) NON-metric gl(14) generators - which are ALSO Lie-algebra-valued - flow strongly (sig up to ~100). So the load-bearing property is being in the METRIC algebra so(9,5), NOT merely "Lie-algebra-valued"; the all-zero result is a real, sharp distinction.
- **MECHANISM (sufficient, canonical certificate):** the quaternionic structure J_quat is UNIQUE up to a U(1) phase (the complex Cl(9,5) is irreducible => commutant = scalars; verified across seeds, U_seed = lambda*U_1, |lambda|=1, resid ~6e-12), so the PHS C = J_quat . G and the test {C, Delta} are CANONICAL, not seed-dependent. **ALL 91 so(9,5) generators AND the 3 self-dual ones satisfy {C, Delta} = 0** (max ~1.2e-11, 0/91 break), and {C, Delta}=0 with C^2=-1 forces an exactly +/- symmetric spectrum, hence sig = 0. This is a SUFFICIENT (essentially-unique) certificate - sig depends only on Delta - not a proof it is the sole cause. (Adversarial check first flagged this as possibly seed-fragile by exhibiting a "second C"; that did not reproduce - phase-uniqueness shows C is canonical.)

**SCOPE (honest limit):** this is the POINTWISE index. The genuine SPEC 5(i) FAMILIES index (spectral flow / Chern classes as the connection varies over the fiber retract RP^3) is not directly computed - but every pointwise value vanishing leaves nothing for an odd/spectral-flow families invariant to integrate, and the only possible nonzero families home is H^2(RP^3) = Z2, which is 2-torsion and cannot carry the odd prime 3. So the families route is 3-free by the metric fiber's own prime spectrum {2} - the CONSTRUCT-04 prime-spectrum sieve, now at the level of the fiber.

**VERDICT (decisive):** the natural geometric '3' (Lambda^2_+) and EVERY physical (gauge/spin) connection give generation index ZERO. The soft-wall GO of CONSTRUCT-02/03 is real but INACCESSIBLE to Lie-algebra-valued connections; the index-reviving operators are structureless non-connections with no geometric meaning. **This CLOSES the most natural external escape route.** A connection outside the so(9,5) envelope (some exotic non-gauge object) remains the only conceivable opening, and none is known.

---

### SYNTHESIS v2 (CONSTRUCT-02..05) - the WALL has hardened back; the GO does not survive contact with physical connections

The picture has sharpened decisively. CONSTRUCT-02/03 opened a door (the eta=0 wall is soft; a grading-breaking connection revives a canonical integer index). CONSTRUCT-04 + 05 have now shown that door opens onto a wall:
- **No honest integer in the rep** (CONSTRUCT-04): the count's prime 3 is absent from the rep's dimension spectrum {2,7,13} and from its degree-0 Dirac invariants.
- **No index from any physical connection** (CONSTRUCT-05): every METRIC so(9,5) (gauge/spin) connection - including the natural self-dual one carrying the geometric '3' - preserves the canonical (phase-unique) PHS and gives index ZERO. Only structureless non-(metric) operators flow (incl. non-metric gl(14), which are Lie-algebra-valued but not gauge/spin connections).
- **The metric fiber is 3-free too:** RP^3's cohomology is 2-torsion (H^2 = Z2); the geometric '3' of Lambda^2_+ does not enter the families index.

So three independent routes to '3' (algebraic invariant, pointwise connection index, families index over the fiber) are now each shown 3-free or zero, each by a clean prime-spectrum/symmetry mechanism. The honest reading shifts toward **WALL-PERMANENT**: GU's existing material, even with the soft-wall index revived, contains no honest construction of '3' - the integer would have to be imported. The remaining formal opening is narrow and exotic (a non-Lie-algebra "connection", or a families invariant not killed by the {2}-spectrum of RP^3), with no known candidate. This is the sharp, mechanism-backed negative the parent campaign's central question was heading toward. All CONSTRUCT-05 sub-claims reproduce deterministically; the headline + mechanism were self-adversarially checked (spinor-only error caught and corrected; non-algebra-flows contrast confirms the pipeline).

---

### CONSTRUCT-06 - the PARITY GATE (corrected): the obstruction is UNDER-DETERMINATION, not impossibility (2026-06-27)

Capstone of the campaign, triggered by a 113-persona / 10-family Hegelian pass (over every persona in gu-formalization, gu-source-action, time-as-finality, temporal-issuance) plus three external design hypotheses (client/server, source-action-as-membrane, six-axis class-relativity). The pass collapsed the search to ONE reframed invariant - **quaternionic-linearity** (commuting with the phase-unique J_quat of M(64,H)) - and nominated a J-ANTILINEAR carrier as the only escape to an ODD index. (`tests/step10_parity_gate_quaternionic_wall.py`, guards held.)

**A first draft claimed a UNIVERSAL parity wall ("no a-priori carrier reaches an odd index"). Adversarial verification REFUTED it with a one-line counterexample, and this entry records the corrected, narrower, verified truth.** Splitting every a-priori G-diagonal Hermitian carrier by S(Delta)=J_quat.Delta.J_quat^{-1}:
- **(1) J-LINEAR carriers** (the PHYSICAL gauge/spin/metric-connection class - every connection in C-05 lives here): index forced **EVEN** by quaternionic Kramers, at ALL ranks (the J-linear projection of a rank-r object gives sig = **2r**: rank-1->2, rank-3->6, rank-5->10). The genuine wall, and exactly the physically-intended class.
- **(2) J-ANTILINEAR carriers**: index **IDENTICALLY 0**, non-vacuous (||Delta|| ~ 1180; antiunitary conjugation forces an exactly +/- symmetric spectrum). The nominated escape gives zero.
- **(3) GENERIC / LOW-RANK carriers** (no J-linearity imposed): **NO parity protection.** A rank-r positive kernel carrier gives sig = **r EXACTLY** - so rank-1->1, rank-3->**3**, rank-5->5. **ODD indices, INCLUDING 3, ARE REACHABLE.** The draft's "even only" was an artifact of sampling full-rank random carriers (signature trivially even).

**CORRECTED VERDICT.** "3" is NOT impossible: a rank-3 a-priori carrier gives index 3 directly. The genuine obstruction is **UNDER-DETERMINATION** - the rep does not FORCE the rank/index to be 3; choosing rank 3 is the forbidden import. Two real sub-walls survive (physical CONNECTIONS forced even, so the natural gauge/spin objects cannot give an odd 3; pure J-antilinear gives 0), but the index over a-priori carriers is FREE. So the campaign's honest statement is **not "GU cannot produce 3" but "GU under-determines the count; nothing internal forces 3; an honest 3 requires a CANONICAL selector (the unbuilt S_IG membrane) that pins the rank/index a-priori without choosing it."** This is WEAKER than the WALL-PERMANENT lean of C-04/C-05 and supersedes the over-strong first draft.

**RELATION TO PRIOR WALLS.** C-03 (even 4Z ladder), C-05 (physical connections -> 0/even) are now seen as the J-LINEAR-restricted face of quaternionic Kramers - real, but a property of the connection class, not of all carriers. C-04 (prime 3 absent from the dimension spectrum) still holds for rep-native dimensions. None of these forbids a rank-3 carrier; they forbid the count being FORCED by the rep.

**NEXT (the one and final frontier, unchanged):** the canonical external membrane - can a finality-pinned external structure pin the rank/index to 3 a-priori (not fitted)? This is the literal unbuilt S_IG. The honest prior is still uncertain (the rep gives no preferred rank), but the obstruction is now correctly named as under-determination, which is exactly the gap a source/membrane is meant to fill.

**PROCESS NOTE.** The adversarial-verification discipline worked: a clean-but-false "impossible" was caught pre-commit by an elementary rank-1 counterexample and corrected to a true "reachable but unforced." Recorded as a cautionary instance of full-rank-sampling overgeneralization.

---

### CONSTRUCT-07 - the GU-NATIVE PARITY THEOREM: GU's own building blocks force an EVEN index (2026-06-27)

Strengthening of C-06. C-06 showed an odd index (incl. 3) is reachable by SOME a-priori carrier (a rank-3 kernel projector gives sig=3), so the obstruction is under-determination. This step settles the sharp follow-up: is an odd carrier reachable by GU's OWN building blocks, or only by FOREIGN objects? It upgrades the numerical even-ladder findings (C-03/C-05/C-06) into a closed-form representation-theoretic theorem. (`tests/step11_gu_native_parity_theorem.py`, runs clean, guards held.)

- **(a) Every GU-native PRIMITIVE commutes with J_quat** (H-linearity defect ~1e-11): the Clifford generators e_a (incl. timelike i*G_a), spin generators sigma_ab, vector-index generators M_ij, Pi_RS, Q, M_D.
- **(b) The generated algebra is closed inside the J_quat-commutant M(14,C) (x) M(64,H)** - exactly the statement Cl(9,5)=M(64,H) (the real Clifford algebra IS the quaternionic-linear algebra). Verified: random real-coefficient products+sums stay H-linear (defect ~1e-10).
- **(c) KRAMERS:** any Hermitian operator commuting with an antiunitary J (J^2=-1) has even-dimensional eigenspaces, hence EVEN signature. Verified: GU-native carrier signatures all even.
- **(d) The odd-3 escape is FOREIGN:** the rank-3 random projector is NOT H-linear (defect ~2); the essential scalar-i needed to leave the quaternionic-linear algebra is itself J-ANTILINEAR (defect ~85). Not GU-native -> an import.

**THEOREM (the publishable structural no-go, literal-index reading where count = index):** GU's quaternionic structure forces an EVEN generation index; an ODD count such as 3 cannot arise from GU's own building blocks (the entire real Clifford algebra Cl(9,5)=M(64,H) is quaternionic-linear) - reaching an odd index requires importing a non-quaternionic (non-Clifford) object. This is closed-form representation theory, not sampling: it holds for the whole generated algebra. It is a GU-native parity no-go - the strongest, most defensible claim of the campaign.

**Under the alternative half-index reading** (count = index/2): a GU-native H-linear rank-r carrier gives index 2r, so count = r is reachable incl. 3, but the rank stays FREE - the C-06 under-determination, now pinned to a single free integer rather than a free operator.

**STANDING after C-07.** The honest, defensible result of the whole campaign: (1) GU does not close on its own (parent repo); (2) its generation count is under-determined - neither forced nor forbidden internally (C-06); (3) but GU's quaternionic structure does impose a hard PARITY constraint: GU-native operators give an even index, so under the literal-index reading an odd 3 is structurally impossible without a non-quaternionic import (C-07). The one remaining frontier is unchanged: a canonical external membrane (S_IG) that either pins the free rank (half-index reading) or supplies the non-quaternionic structure (literal-index reading) - a-priori, without import.

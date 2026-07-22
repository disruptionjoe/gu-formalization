---
title: "OPERATOR-GRADE anomaly banking swing: three SEPARATED targets, each graded independently, pre-registered kill-conditions declared before computation. T1 = the pure Pin bordism NUMBER (order of Omega^{Pin+}_14 + whether sigma's specific 14-class is nonzero and its order). T2 = the operator-grade deck action U N U^{-1} = -N (banked non-circularly, or sigma-circular?). T3 = the fiber->spacetime descent map WITH A DEFINITE SIGN (is the sign FORCED by anomaly inflow, or inserted by hand?). VERDICT: PARTIAL, leaning BLOCKED on operator-grade banking -- NONE of the three reaches operator grade this swing, and the swing's value is diagnosing WHY, precisely. T1: controls (n=0..7 incl. anchors Z/8@Pin-_2, Z/16@Pin+_4) reproduce and the instrument DISCRIMINATES (planted trivial->0, planted generators RP^2/RP^4->nonzero); the Pin+/Pin- criterion and the Pin+<->Spin(TM+3det) reduction are machine-verified; BUT the EXACT order of Omega^{Pin+}_14 is NOT certified here (needs the ko^(RP^inf-Thom) Adams chart through deg 14) -- reconstruction-grade, published tables list it nonzero, not reproduced from first principles -- AND the decisive sub-question 'is sigma's specific class nonzero' is GATED on T2 (the class = [observerse bulk, Pin+, deck structure], and the deck structure IS T2). T2: the OBSTRUCTION exists (no forced-symmetric self-adjoint completion on {q<0} ends) is established WITHOUT sigma from the machine-checked K_S-null halves -- but that is exactly the already-banked LC-SELECTOR content, not new; the OPERATOR-grade deck-ODD ACTION U N U^{-1}=-N (what upgrades 'boundary-condition ambiguity' to '(reflection) SYMMETRY anomaly') requires the self-adjoint realization of A~, which on the crossed ends requires importing sigma -- so banking sigma-as-a-protected-'t-Hooft-anomaly at OPERATOR grade via the operator-deck-action is SIGMA-CIRCULAR. The expression-grade escape (Sp(1) central -1 acting oddly on the differential-expression family N(t)) is real and sigma-free but UNDER-POWERED: a deck-odd symbol is necessary, not sufficient, for the anomaly. T3: the descent map is UNBUILT (load-bearing, non-probe-checkable); moreover the sign of an induced parity-odd (gravitational-theta / Chern-Simons) coefficient is REFLECTION-ODD, so NO parity-even committed datum can fix it -- machine-demonstrated (the coefficient sits in the -1 eigenspace of the reflection; its reflection-fixed set is {0}). The absolute sign is therefore NOT internally forced -- it IS the external bit sigma. The parity prediction consequently caps at 'parity-odd NONZERO, WITHOUT an absolute sign'; the DE-co-varying sign is the genuinely forced *relation* ONLY IF the descent map is built and the SRC-COH-1 one-bit identification holds -- both unbuilt/proposal, so the co-variance is PROPOSAL, not banked. Overall: the anomaly ID does NOT reach operator grade; it stays PROPOSAL, and this swing pins the three exact obstructions (T1 order reconstruction-grade + class T2-gated; T2 sigma-circular at operator grade; T3 sign structurally-external hence sign-free prediction)."
status: active_research
doc_type: exploration
created: 2026-07-21
outcome: "PARTIAL / leaning BLOCKED on operator-grade banking (no target reaches operator grade; three obstructions pinned)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
kill_conditions_declared_before_computation: true
directed_by: "Joe direct chat, 2026-07-21 (OPERATOR-GRADE anomaly banking; three separated targets; one synchronous pass, foreground probe)"
inputs:
  - explorations/anomaly-inflow-swing-2026-07-21.md
  - explorations/pin-bordism-cardinality-2026-07-21.md
  - explorations/lp-lc-deficiency-decisive-2026-07-21.md
  - explorations/more-predictions-hunt-2026-07-21.md
  - explorations/wave-swing1-the-lemma-2026-07-21.md
  - explorations/global-anomaly-leg-2026-07-20.md
  - canon/source-action-seiberg-witten-construction.md
  - tests/channel-swings/pin_bordism_cardinality_probe.py
probe: tests/channel-swings/operator_grade_anomaly_banking_probe.py (foreground, seed 20260721, numpy + exact mod-2 polynomial arithmetic, note exit code below)
---

# OPERATOR-GRADE anomaly banking -- three separated targets

> **CORRECTION (2026-07-22).** T1's ambient group is now closed independently:
> `Omega^{Pin+}_14 ~= Z/2` by the Smith audit and Kirby--Taylor's direct table.  T1's GU-class assignment,
> T2, and T3 remain unbuilt.  More strongly, the current operator audit retracts the inference from null
> spectral halves to absence of `J`-self-adjoint realizations: the supported result is failure of one
> `K_S`-definite cut, not a binary external-domain theorem.  See
> `explorations/operator-to-anomaly-closure-campaign-2026-07-22.md`.

Single synchronous pass, foreground, maximum honesty about grade. This session has
already caught FOUR planted-toy over-claims; the binding discipline here is that a
positive is NEVER self-banked, an operator-grade theorem is NEVER declared from a
foreground probe, and the three targets are graded SEPARATELY because they have
DIFFERENT dependency structure. Kill-conditions are declared in Section 1 BEFORE any
computation (this header and Sections 0-1 were written before the probe was run).

The whole enterprise is CONDITIONAL on the proposal-grade anomaly-inflow
identification (`anomaly-inflow-swing`, `pin-bordism-cardinality`): sigma = the w1
(orientation / time-reversal / reflection) Z/2, receptacle `Omega^{Pin+}_14`
(primary reading) / `Omega^{Pin}_15` (alt), NOT the fermionic mod-2 Dirac-index
anomaly (banked-dead by quaternionic Kramers evenness, S = H^64). Nothing here
promotes that identification; it consumes it and tests whether the two named build
gates (operator-grade anomaly; descent-map-with-a-sign) can close.

## 0. Verdict up front (per target, each graded independently)

> **OVERALL: `PARTIAL / leaning BLOCKED on operator-grade banking`.** No target reaches
> operator grade this swing. The swing's contribution is to pin the three exact
> obstructions and, in T2/T3, to show two of them are STRUCTURAL (not merely
> "more compute needed").
>
> - **T1 -- the pure bordism number: `RECONSTRUCTION-GRADE (order) + T2-GATED (class)`.**
>   The instrument is certified: the control table `n = 0..7` reproduces (incl. anchors
>   `Omega^{Pin-}_2 = Z/8`, `Omega^{Pin+}_4 = Z/16`), the Pin+/Pin- criterion from
>   Stiefel-Whitney classes is machine-computed, the `Pin+ <-> Spin(TM+3det)` /
>   `Pin- <-> Spin(TM+det)` reduction is verified, and the detector DISCRIMINATES
>   (planted trivial class -> 0; planted generators `RP^2`, `RP^4` -> nonzero). BUT the
>   **exact order of `Omega^{Pin+}_14` is NOT certified here** -- it needs the
>   `ko ^ (RP^inf Thom)` Adams chart through degree 14, a known-hard input this
>   foreground pass does not reproduce (published tables list it nonzero;
>   reconstruction-grade). AND the **decisive sub-question -- is sigma's SPECIFIC
>   14-class nonzero -- is GATED on T2**: the class is `[observerse bulk, Pin+, with the
>   deck structure]`, and the deck structure IS the T2 object. So even the
>   class-ASSIGNMENT (not just its order) needs the deck action. **T1's group-order
>   question is sigma-INDEPENDENT (pure topology, bankable in principle); T1's
>   decisive class-nonzero question is NOT.**
> - **T2 -- the operator-grade deck action: `SIGMA-CIRCULAR at operator grade (NOT banked)`.**
>   The **obstruction exists** (no forced-symmetric self-adjoint completion on the
>   `{q<0}` ends) is established WITHOUT sigma, from the machine-checked `K_S`-null
>   halves (`lp-lc`, `8.9e-16`) -- but that is exactly the already-banked **LC-SELECTOR**
>   content, not a new operator-grade result. The **operator-grade deck-ODD ACTION**
>   `U N U^{-1} = -N` -- the thing that upgrades "a boundary-condition ambiguity" to
>   "a (reflection) SYMMETRY realized anomalously" -- requires the deck operator `U` to
>   act on the REALIZED family `N`, i.e. it presupposes the self-adjoint realization of
>   `A~`, which on the crossed ends requires importing sigma. So banking
>   "sigma is a protected 't Hooft anomaly" at operator grade THROUGH the operator deck
>   action is **sigma-circular**. The expression-grade escape (the `Sp(1)` central `-1`
>   acting oddly on the differential-EXPRESSION family `N(t)`, which exists on crossed
>   ends since `P > 0`) is real and sigma-free, but UNDER-POWERED: a deck-odd SYMBOL is
>   necessary, not sufficient, for the anomaly (the anomaly is "no symmetric
>   completion," a domain-level statement).
> - **T3 -- the descent map with a sign: `SIGN NOT FORCED (structurally); prediction caps at parity-odd-nonzero`.**
>   The descent map (fiber `w1` anomaly -> spacetime gravitational-theta / Chern-Simons
>   term) is UNBUILT and is the load-bearing, non-probe-checkable step. Beyond "unbuilt,"
>   there is a STRUCTURAL obstruction to a forced sign: a parity-odd coefficient is
>   **reflection-ODD**, so no parity-EVEN committed datum can fix it -- machine-shown
>   (the coefficient sits in the `-1` eigenspace of the reflection; its reflection-fixed
>   set is `{0}`). The absolute sign is therefore **not internally forced -- it IS the
>   external bit sigma** (a parity anomaly says the symmetry is broken, not WHICH way).
>   Hence the parity prediction caps at "**parity-odd NONZERO, without an absolute
>   sign**." The DE-co-varying sign is the genuinely forced RELATION -- but only IF the
>   descent map is built AND the SRC-COH-1 one-bit identification holds; both are
>   unbuilt/proposal, so the co-variance is PROPOSAL, not banked.

Probe: `tests/channel-swings/operator_grade_anomaly_banking_probe.py` -- foreground,
numpy + exact mod-2 polynomial arithmetic, seed `20260721`. Exit code recorded in
Section 6.

## 1. Pre-declared kill-conditions (written BEFORE computation)

Three targets, SEPARATED because their dependency structure differs. For each: the
kill condition (what would break the instrument / falsify the target), the decision
rule (what counts as banked vs not), and the honest pre-declared expectation.

### T1 -- the pure bordism number

- **KILL-T1a (instrument):** if the control table `n = 0..7` does NOT reproduce the
  machine-checked Pin+/Pin- values (incl. anchors `Omega^{Pin-}_2 = Z/8`,
  `Omega^{Pin+}_4 = Z/16`), the instrument is broken -> T1 `BLOCKED`, discard.
- **KILL-T1b (planted discrimination -- anti-toy):** a KNOWN-TRIVIAL class must
  evaluate to `0` AND a KNOWN-NONTRIVIAL generator (`RP^2` generating
  `Omega^{Pin-}_2 = Z/8`; `RP^4` generating `Omega^{Pin+}_4 = Z/16`) must evaluate
  NONZERO. If the detector fails to discriminate either way -> T1 `BLOCKED`.
- **DECISION-T1 (order):** T1 counts as **"group order BANKED"** ONLY if the exact
  order of `Omega^{Pin+}_14` is reproduced from a CERTIFIED in-probe computation
  (Adams / ABP chart), not recited from a table. If only structural nonvanishing (no
  sporadic zero at 14) is certified, T1 order = **"reconstruction-grade, NOT banked."**
- **DECISION-T1 (class -- the decisive sub-question):** "is sigma's SPECIFIC 14-class
  nonzero" is BANKED only if it can be evaluated from committed structure WITHOUT the
  deck action. If the class-assignment itself needs the deck action, record
  **"sigma-class T2-GATED."**
- **Pre-declared expectation:** exact order likely NOT bankable in one foreground pass
  (needs the full `ko ^ RP-Thom` Adams chart); sigma-class nonvanishing likely
  T2-gated (the group is pure topology; the CLASS is a property of GU's construction).

### T2 -- the operator-grade deck action

- **KILL-T2a (circularity):** if the operator-grade identity `U N U^{-1} = -N`
  provably requires the self-adjoint realization of `A~`, AND that realization provably
  requires importing sigma (LC-SELECTOR: O-b does not close without sigma), then banking
  the deck action -- hence "sigma is a protected anomaly" -- at operator grade is
  **sigma-circular**; report CIRCULAR, do NOT bank.
- **DECISION-T2:** T2 = **"deck action BANKED at operator grade"** ONLY if a route to
  `U N U^{-1} = -N` as an OPERATOR identity exists that does NOT presuppose sigma. Test
  the expression-grade escape (the `Sp(1)` central `-1` acting on the differential
  expression `N(t)`, defined on crossed ends): does the expression-grade deck-oddness
  SUFFICE for the anomaly, or is it necessary-not-sufficient?
- **Pre-declared expectation:** likely sigma-circular at operator grade; the obstruction
  EXISTS non-circularly (but = the already-banked LC-SELECTOR); expression-grade
  deck-oddness bankable but under-powered.

### T3 -- the fiber->spacetime descent map with a definite sign

- **KILL-T3a (hand-inserted sign):** if the sign of the induced parity-odd coefficient
  is set by an arbitrary orientation / convention choice rather than forced by the
  anomaly inflow, the sign is NOT forced -> cap at "parity-odd nonzero, no sign."
- **KILL-T3b (structural):** a parity-odd coefficient is reflection-ODD; if NO
  parity-EVEN committed datum can fix a reflection-odd quantity (the coefficient lies in
  the `-1` eigenspace of the reflection, reflection-fixed set `{0}`), then the absolute
  sign cannot be internally forced -- it equals the external sigma. Demonstrate.
- **DECISION-T3:** T3 = **"sign FORCED"** ONLY if the descent map is constructed AND
  yields a coefficient whose sign is determined by committed (sigma-INDEPENDENT)
  structure. If the sign = sigma (external), record **"co-variance forced (proposal,
  pending built descent + one-bit ID); absolute sign NOT forced."**
- **Pre-declared expectation:** descent unbuilt; absolute sign structurally = sigma,
  not internally forced; the DE-co-variance is the forced content but proposal-grade.

<!-- RESULTS BELOW WERE WRITTEN AFTER RUNNING THE PROBE -->

## 2. T1 -- the pure bordism number

Probe run: **EXIT 0**, double-run **byte-identical**, **39/39 PASS**.

### 2a. Instrument certified (KILL-T1a, KILL-T1b both cleared)

- **Control table `n = 0..7` reproduces** (C1), including both mandated anchors
  `Omega^{Pin-}_2 = Z/8` and `Omega^{Pin+}_4 = Z/16`; all nonzero Pin groups are finite
  2-groups; the Pin+ sporadic zeros sit at `{1,5,6,7}`.
- **Pin+/Pin- criterion machine-computed** (C2) from Stiefel-Whitney classes
  (`Pin+ <=> w2 = 0`; `Pin- <=> w2 + w1^2 = 0`): `RP^2` is Pin- not Pin+ (generates the
  `Z/8`), `RP^4` is Pin+ not Pin- (generates the `Z/16`, the `T^2=(-1)^F` flavor GU
  leads with), `RP^3` is orientable (`w1(T)=0`, so `sigma` is the LINE's `w1`, matching
  the banked D2). This grounds the receptacle FLAVOR (`Omega^{Pin+}`) in a reproducible
  computation rather than an assertion.
- **The ABP reduction verified at SW-class level** (C3): `Pin+(TM) <-> Spin(TM + 3 det)`
  (the det-twist leaves `w2` unchanged) and `Pin-(TM) <-> Spin(TM + det)` (shifts `w2`
  by `w1^2`). This is the Thom-spectrum route that turns the Pin computation into a
  (twisted) `Spin = ko` computation over `RP^inf` -- the correct machine for the exact
  order, and the reason the `Z/16` at `n=4` is a KO-theoretic (`eta`/image-of-J) number.
- **Planted discrimination fires** (C4, the anti-toy): the `w1`-detector is `0` on a
  trivial input (any Spin/orientable manifold, `w1 = 0`) and `1` on the generators
  (`w1(L)^2[RP^2] = 1`, `w1(L)^4[RP^4] = 1`). The instrument SEPARATES trivial from
  nontrivial -- it is not a tautology that reads nonzero on everything.

### 2b. The exact order of `Omega^{Pin+}_14`: RECONSTRUCTION-GRADE, NOT banked (DECISION-T1 order)

`n = 14` carries no sporadic Pin+ zero (C5), and published cobordism tables list
`Omega^{Pin+}_14` as a nonzero finite 2-group. But per the pre-declared decision rule,
that is **not** "banked": the **exact order is not certified in this pass**. Certifying
it needs the `ko ^ (RP^inf Thom)` Adams `E2` chart -- `Ext_{A(1)}(H^*(MTPin+), Z/2)`
through total degree 14 plus its differentials (equivalently the ABP `ko`-module summand
structure at `n = 14`). That is a known-hard input a foreground probe does not reproduce.
**Reciting a table value would be exactly the planted-toy over-claim this session is
guarding against**, so the probe deliberately asserts only the non-implication and the
not-certified flag. **T1 order verdict: reconstruction-grade; the group is nonzero
(strongly supported), the exact order is open, and the single missing input is named.**

### 2c. The decisive sub-question -- is `sigma`'s SPECIFIC class nonzero -- is T2-GATED (DECISION-T1 class)

This is the cleanest structural finding of T1, and it answers the directed sub-question
("is the class-assignment bankable without the deck action?"):

- The **group** `Omega^{Pin+}_14` is **pure topology -- `sigma`-independent** (C6). It is
  bankable in principle with no reference to GU or the deck action.
- The **class** -- WHICH element of that group `sigma` is -- is
  `[observerse bulk, Pin+ structure, WITH the deck structure]`. The deck structure **IS
  the T2 object**. So even the class-ASSIGNMENT (not merely its order) needs the deck
  action. **`sigma`'s class-nonvanishing is T2-GATED.**

Hence "is the anomaly genuinely protected (`sigma != 0` in its receptacle)" cannot be
decided at the group level: it waits on both (i) the exact order (2b) and (ii) the
class-assignment, which is T2 -- and T2 is `sigma`-circular (Section 3). This is the
honest depth behind the prior doc's "PROTECTED (proposal grade)": the protection is not
just un-computed, its class input is entangled with the very deck action whose banking is
circular.

## 3. T2 -- the operator-grade deck action: SIGMA-CIRCULAR (KILL-T2a triggered)

The dependency analysis (encoded as a DAG in the probe, `[BOOKKEEPING]`, not as a new
theorem) resolves the directed honesty check decisively.

**The circularity (the anomaly reading, at operator grade).** The reading "`sigma` is a
protected `w1` 't Hooft anomaly" rests on the deck being realized **oddly**:
`U N U^{-1} = -N`. That is what upgrades "a self-adjoint-extension / boundary-condition
ambiguity" (a harmless `theta`-modulus) to "a reflection SYMMETRY realized with no
invariant completion" (an anomaly). But `U N U^{-1}` at operator grade requires the deck
operator `U` to act on the **realized** family `N` -- i.e. it presupposes the
self-adjoint realization of `A~`. And LC-SELECTOR is precisely that on the `{q<0}` ends
**no self-adjoint realization exists without importing `sigma`**. So the chain is

    sigma_is_protected_anomaly  ->  operator_deck_action  ->  self_adjoint_realization  ->  import_sigma

(probe: `T2-operator-grade-anomaly-requires-import_sigma`, PASS). **Banking the anomaly
through the operator-grade deck action presupposes `sigma`. It is `sigma`-circular.** The
anomaly-protection that DEFINES `sigma` would itself need `sigma` -- exactly the failure
mode the directed task flagged, and it is present. **T2 is NOT banked at operator grade.**

**The escape is real but under-powered.** There is a `sigma`-free route to deck-oddness:
the `Sp(1)` central `-1` (belt-trick `U^2 = -I`, wave-swing-1) acts oddly on the
differential-EXPRESSION family `N(t)`, which is well-defined on the crossed ends
(`P > 0` there, `lp-lc` Q2). This **expression-grade deck-oddness is `sigma`-free** (probe
PASS). But it does **not** deliver the anomaly: a deck-odd SYMBOL is **necessary, not
sufficient**. The anomaly is "no symmetric self-adjoint completion," a **domain-level**
statement the expression grade never reaches (probe:
`T2-expression-escape-does-NOT-deliver-the-anomaly`, PASS).

**What IS establishable without `sigma` is already banked as LC-SELECTOR.** The
obstruction's EXISTENCE -- that there is no forced-symmetric completion on the `{q<0}`
ends -- is proved from the machine-checked `K_S`-null halves (`8.9e-16`, `lp-lc`),
**without positing `sigma`** (probe:
`T2-obstruction-EXISTS-without-sigma-(=LC-SELECTOR-not-new)`, PASS). But that IS the
LC-SELECTOR content; it is not a NEW operator-grade result, and crucially it is the
existence of an obstruction, not the identification of it as a protected reflection
anomaly with an odd deck action. **Net T2: the obstruction exists (old, `sigma`-free);
the symmetry-anomaly upgrade is `sigma`-circular at operator grade; the expression-grade
deck-oddness is `sigma`-free but insufficient.** No non-circular operator-grade banking.

## 4. T3 -- the descent map with a sign: NOT FORCED, and structurally so (KILL-T3b triggered)

**Unbuilt.** The descent (fiber `w1` reflection anomaly -> spacetime gravitational-`theta`
/ Chern-Simons / Pontryagin term) is not constructed; it is the load-bearing,
non-probe-checkable step named in `more-predictions-hunt` gate 2. So on grounds of
"unbuilt" alone the sign is not delivered. But there is a deeper, STRUCTURAL reason the
absolute sign cannot be forced, and it is machine-shown:

**A parity-odd coefficient is reflection-ODD.** The induced grav-`theta` / CS coefficient
`c` is a pseudoscalar: under the reflection `R` (`R^2 = I`) it satisfies `R c = -c`, i.e.
`c` lives in the `-1` eigenspace of `R`, whose reflection-fixed set is `{0}` (probe:
`T3-pseudoscalar-in-minus1-eigenspace`, `T3-parity-even-data-cannot-source-c`, PASS).
Therefore **no parity-EVEN committed datum can source or fix `c`** -- any `R`-invariant
input projects to `0` on the pseudoscalar line. Both signs `+-|c|` are consistent with
all parity-even committed structure. **The absolute sign is not internally forced -- it
IS the external bit `sigma`.** This is not a gap to be closed by more computation; it is
what a parity/T anomaly IS: it says the symmetry is realized with no invariant completion
(broken), it does **not** say WHICH way. "Which way" is precisely the external reflection
bit `sigma`.

**Consequence for the parity prediction (the directed deliverable).** The prediction caps
at "**parity-odd NONZERO, without an absolute sign**" -- the weaker form the task
anticipated. What IS forced -- the genuinely testable, `LCDM`-forbidden content -- is the
**CO-VARIANCE**: if the descent map is built AND the SRC-COH-1 one-bit identification
holds (both the DE sign and the parity sign are readouts of the SAME `sigma`), the two
signs are LOCKED (probe: `T3-co-variance-locked`, both `sigma = +-1`, PASS). But both
premises are unbuilt/proposal, so **the co-variance is PROPOSAL, not banked** (probe:
`T3-co-variance-is-PROPOSAL...`, PASS). The parity leg does **not** get a definite,
DE-co-varying sign this swing; it gets "parity-odd nonzero" now, and a co-varying sign
only after the descent map and the one-bit identification are both banked.

### 4a. The one descent, four faces (reconnaissance only -- one line each, per coordinator hint)

The SAME unbuilt descent (a general grav-`theta`/CS response) would, if built, expose up
to four observable faces of the ONE `sigma` -- so they would co-vary (a 4-domain
consilience signature gated on ONE construction). Honest per-face status; **none is
computed here**, and all inherit T3's "absolute sign = external `sigma`, not forced":

| face | observable | exposed by the descent? | coefficient / sign forced? |
|---|---|---|---|
| **(A) parity** (PRIMARY) | CMB `TB/EB`, cosmic birefringence `beta`, GW handedness | **yes** -- this IS the grav-`theta`/CS face | **no** absolute sign (reflection-odd = `sigma`); co-variance forced only if descent+one-bit ID banked |
| **(G) strong-CP** | `theta_QCD` -> neutron EDM | partial -- `theta_QCD` is the same T-odd face | **no**, and it does NOT pin `theta_QCD -> 0`: an ANOMALOUS T does not enforce the T-symmetric vacuum; `theta` tracks `sigma`. needs-more |
| **(B) nu Majorana/Dirac** | `0nubb` | source-gated (physical-`nu` <-> quaternionic-carrier ID not fixed) | **reality sign runs OPPOSITE the naive guess**: Pin+ `T^2=(-1)^F` => Kramers/pseudoreal carrier => a symmetric Majorana mass is FORBIDDEN => **Dirac forced** (consistent with `S=H^64`, `J^2=-1`). Conditional on the source-gated ID. needs-more |
| **(C) protected `{q=0}` mode** | `Delta N_eff` (dark radiation) | bridge-gated (fiber-symbol mode -> spacetime massless field unowned) | **no** (magnitude unforced, bridge unowned). needs-more |

The payoff shape is therefore: **up to four un-wired predictions gated on ONE descent**,
all readouts of the same `sigma` (hence co-varying) -- but the descent is unbuilt and
`sigma`-circular to bank (T2), so at current grade the count of BANKED forced-observable
signs remains **zero**, and the honest surplus is "one construction unlocks four
co-varying faces," not "four predictions." Note (B)'s sign inverts the naive reading and
is the one face whose *reality* sign is structurally forced (by Kramers) once its
identification is fixed -- worth a dedicated future pass, but source-gated now.

## 5. Overall honest grade of the anomaly ID after this swing

**The anomaly identification does NOT reach OPERATOR grade this swing. It stays a graded
PROPOSAL, exactly where `anomaly-inflow-swing` / `pin-bordism-cardinality` left it -- and
the value delivered is diagnosing the three obstructions precisely, two of which are
STRUCTURAL (not "more compute"):**

- **T1:** the receptacle group is pure topology and bankable in principle, but its exact
  order at `n = 14` is reconstruction-grade (named missing input), and the decisive
  class-nonvanishing is T2-gated.
- **T2:** operator-grade banking of the deck action / the reflection-symmetry-anomaly is
  `sigma`-circular; only the (already-banked, `sigma`-free) obstruction-existence and an
  under-powered expression-grade deck-oddness survive.
- **T3:** the descent map is unbuilt, and the absolute parity sign is structurally
  external (`= sigma`), so the parity prediction caps at "parity-odd nonzero"; the
  DE-co-varying sign is a proposal pending the unbuilt descent + the one-bit ID.

Two would-be over-claims were available this swing and were declined: (i) "`sigma != 0`
in `Omega^{Pin+}_14`, anomaly banked" (declined -- order reconstruction-grade, class
T2-gated); (ii) "the descent forces a definite parity sign co-varying with DE" (declined
-- the sign is structurally the external `sigma`; only the co-variance is forced, and
only conditionally). Consistent with the session's four prior planted-toy catches.

## 6. Boundary

Exploration tier. Only two NEW files were written -- this document and the probe
`tests/channel-swings/operator_grade_anomaly_banking_probe.py` (foreground, seed
`20260721`, numpy + exact mod-2 polynomial arithmetic, **EXIT 0** on both of two runs,
double-run **byte-identical**, **39/39 PASS**; kill-conditions declared in Section 1
BEFORE the probe was run). GU otherwise read-only. **No commit, no push.** No edit to
LANE-STATE, research-portfolio, NEXT-STEPS, canon, PP1/PP2/PP3, the anomaly-inflow swing,
pin-bordism-cardinality, the LP-LC receipt, more-predictions-hunt, wave-swing-1/3,
Prong-0, the global-anomaly-leg pair, or any other agent's artifact, or any
claim/canon/verdict/ledger/portfolio file. No claim-status, canon-verdict, paper-status,
or public-posture change; the externality of `sigma`/`tau`, the verdicts `LC-SELECTOR`,
`CARDINALITY-1 + PROTECTED` (proposal), and the proposal-grade anomaly-inflow
identification are **consumed, not moved or promoted**. A positive here would be PROPOSAL
pending INDEPENDENT hostile-verify; nothing operator-grade is self-banked. Nothing routes
externally (Joe alone publishes).

**Contribution.** Three separated targets, graded independently: **T1** certifies the Pin
instrument (controls + anchors + Pin criterion + Pin<->Spin reduction + planted
discrimination all firm) but leaves the exact `Omega^{Pin+}_14` order reconstruction-grade
with the missing input named, and shows the decisive class-nonvanishing is T2-gated;
**T2** shows the operator-grade deck action -- hence the reflection-symmetry-anomaly
banking -- is `sigma`-circular, with only a `sigma`-free-but-insufficient expression-grade
escape; **T3** shows the descent map is unbuilt and the absolute parity sign is
structurally external (`= sigma`), so the parity prediction caps at "parity-odd nonzero"
with the DE-co-varying sign a proposal, and (reconnaissance) the one descent would expose
up to four co-varying faces (parity primary; `theta_QCD`, `nu` Majorana/Dirac with the
inverted reality sign, `Delta N_eff` -- all gated). Overall: the anomaly ID stays a graded
PROPOSAL; the swing's payoff is pinning why, and declining two available over-claims.

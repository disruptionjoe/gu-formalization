---
artifact_type: exploration
status: exploration (5-persona inline team; circularity diagnosis + partition firm-up; deterministic test)
created: 2026-07-11
hypothesis: H62
title: "H62 -- can the ARENA/VALUE split be made a PRECISE, NON-CIRCULAR partition? The bigger-story model ('the observer forces the ARENA, not the VALUE') and its payoff theorem (Lawvere no-closure, H63) rest on this split being SUBSTANTIVE, not true-by-definition. Branch E flagged the fatal risk: if 'arena' just MEANS 'the forced things' and 'value' MEANS 'the unforced things,' the meta-pattern is vacuous. VERDICT: FIRMED. The SYMMETRY characterization (c) -- arena = invariant of the unbroken observer-invariant symmetry / fixed-point data; value = requires symmetry-BREAKING (a vacuum/frame choice) to specify -- is defined WITHOUT reference to forcing and sorts ALL of the day's concrete cases correctly, INCLUDING the two discriminators that break the naive characterizations: the mass RATIOS (dimensionless-but-FREE, breaks the DIMENSIONAL characterization (a)) and f_2 (continuous-but-FORCED, breaks the DISCRETE/CONTINUOUS characterization (b)). The RG characterization (d) (fixed-point data vs relevant direction) is the RG-sector SHADOW of (c) and agrees on the overlap (f_2 vs f_0). So 'arena forced, value selected' is a SUBSTANTIVE, FALSIFIABLE claim -- an instance of Curie's principle (symmetric structure fixes invariants; breaking requires input), non-circular. Honest caveat: (c) may be GENERIC (Curie, not GU-unique) -- but generic != vacuous; the split is still non-circular and the payoff theorem rests on a REAL principle, so H61/H63 are worth mounting, scoped to symmetry-breaking language (NOT the circular forced/unforced language)."
grade: "COMPUTED / analysis. tests/W73_H62_arena_value_partition.py (deterministic, no RNG, exit 0): encodes the full test table quantity x {characterization (a)/(b)/(c)/(d) arena-or-value call} x {actual forced/free status}, asserts (c) sorts ALL decided cases correctly and (a),(b) each mismatch >=1, and asserts all four characterizations are non-circular by definition (none references 'forced'). Standard: elementary rep theory (Schur on the collective doublet, C2/W72); RG relevance (H57/H60, f_2 irrelevant vs f_0 relevant); Curie's principle. No canon / RESEARCH-STATUS / claim-status / verdict / posture movement; the arena/value split stays a MODEL of the outputs, the conjecture stays a conjecture, the count stays OPEN, GU stays framework-not-theory."
construction: "program-native throughout (GEOMETER-VS-PHYSICS-OBJECTS): the count as realized rank of a Z/3-invariant enclosure in Lambda^2_+ = 1+2 (C2); mu_DW the ratio-only free DeWitt scale (H24); the gravity coupling the induced |II|^2 -> Stelle (f_2,f_0) (H49/H57); the family symmetry the self-dual FRAME SU(2)_+ commuting with internal SM gauge (C2)."
depends_on:
  - explorations/bigger-story-persona-synthesis-2026-07-11.md
  - explorations/path5-branchE-self-dual-square-falsifier-2026-07-11.md
  - explorations/path5-branchC2-capability-enclosures-reframe-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W73_H62_arena_value_partition.py
---

# H62 -- firming the ARENA/VALUE partition (is it a substantive split or true-by-definition?)

## The gate

The day's organizing model is: **the observer / source-action FORCES the ARENA but not the VALUE.** Its payoff
theorem (the Lawvere no-closure, H63) and the whole "source action = observer" conjecture rest on this split being
**substantive**. Path-5 Branch E flagged the fatal risk (its own Persona 3, quoted verbatim):

> "the arena/value split is at some risk of being **self-sealing**. It classifies *forced* things as 'arena' and
> *unforced* things as 'value,' so any forcing can be reabsorbed as 'arena.'"

If "arena" just **means** "the forced things" and "value" **means** "the unforced things," then "the observer
forces the arena, not the value" is TRUE BY DEFINITION -- vacuous -- and any theorem built on it proves nothing.
**This note determines whether the arena/value distinction can be made PRECISE and NON-CIRCULAR** -- defined
INDEPENDENTLY of what turns out to be forced -- so that "all arena is forced, all value is free" becomes a
substantive claim one can TEST. This gates whether the Krein-TT campaign (H61) and the payoff theorem (H63) are
worth mounting.

Run as a 5-persona inline team (one worker, sequential): (1) PHILOSOPHER-OF-SCIENCE (non-circularity /
falsifiability, ruthless); (2) SYMMETRY / REP-THEORY specialist (tests (c) and the discriminators); (3) REFEREE
(grades); (4) ADVERSARY (hunts counterexamples); (5) SYNTHESIZER (verdict).

---

## Step 1 -- the current (loose) definitions, and exactly where they are circular

The loose split, as it appears across the day's files:

- **ARENA** = a forced dimensionless RATIO / a direction-up-to-scale / an operator identity / a UV-asymptotic
  limit / the discrete SET itself (Branch E dividing line; conjecture Sec 1-3).
- **VALUE** = a dimensionful/scale-carrying quantity, OR a discrete SELECTION within a forced discrete set
  (Branch E dividing line).

**Where it is circular.** The CONJECTURE's own statement of the split (Sec 1): "the source action is the object
that selects the VALUE out of the **forced** ARENA." And the meta-pattern (bigger-story Sec (a)): "GU robustly
forces the arena ... while provably **not** forcing the value." Read literally with arena := {forced things} and
value := {unforced things}, the sentence "the observer forces the arena, not the value" reduces to "the observer
forces the forced things, not the unforced things" -- a **tautology**. Branch E's dimensional/discrete dividing
line was the first attempt to break this by giving arena/value an INDEPENDENT criterion (dimension, discreteness),
but Branch E did not TEST that criterion against the free-but-dimensionless and forced-but-continuous cases -- and
those are exactly where it breaks (Step 3). So the circularity is real and un-discharged as of end-of-day.

**PHILOSOPHER-OF-SCIENCE (opening ruling).** A characterization discharges the circularity iff it is stated with
**zero reference to whether the quantity is forced**. Then "arena => forced, value => free" is a synthetic claim
with truth-makers on both sides, and it can be checked case-by-case and, crucially, could come out FALSE. Any
candidate that secretly re-imports "forced" (e.g. "arena = the structural / robust / determined part") fails on
sight. I hold all four candidates to this.

---

## Step 2 -- candidate INDEPENDENT characterizations (each defined WITHOUT reference to 'forced')

- **(a) DIMENSIONAL.** arena = dimensionless; value = dimensionful. *Non-circular?* YES -- physical dimension is
  read off the units, independent of forcing.
- **(b) DISCRETE/CONTINUOUS.** arena = discrete / topological; value = continuous. *Non-circular?* YES --
  discreteness is a property of the quantity's range, independent of forcing.
- **(c) SYMMETRY.** arena = **invariant of the unbroken observer-invariant symmetry** (fixed by the
  representation-theoretic / fixed-point structure); value = **requires symmetry-BREAKING** -- a choice of
  vacuum/frame/direction beyond the invariant structure -- to specify. *Non-circular?* YES, and this is the load-
  bearing check (Step 4): given the symmetry (the self-dual frame `SU(2)_+`, the internal SM gauge group, the
  scale/conformal symmetry, the Gaussian fixed point), whether a quantity is invariant or requires breaking is a
  GROUP-THEORETIC fact computable a priori, before asking what GU forces.
- **(d) RG.** arena = RG-invariant / fixed-point data; value = relevant-direction data. *Non-circular?* YES, but
  scope-limited to quantities that RG-run (the UV/coupling sector).

Why (c) is flagged most promising in advance: **symmetry-breaking = a vacuum SELECTION = exactly what an
observer/measurement does** (Wigner/decoherence/RQM: a measurement picks a pointer basis = breaks a symmetry). So
"value = requires breaking" and "value = observer-selected" would **coincide non-circularly** -- the bridge the
conjecture needs. (d) is the RG shadow of (c): a fixed point IS the maximally symmetric (scale/conformal-invariant)
point; a relevant direction IS a direction of symmetry breaking (flowing away breaks scale invariance). So (c) and
(d) must AGREE wherever both apply -- a cross-check, not two independent votes.

---

## Step 3 -- the full test table: quantity x characterization-call x actual forced/free status

Honest forced/free status taken from the repo (not memory): count menu `{1,3}` forced, 3-over-1 NOT forced
(path 3); replicas forced, masses free / degenerate-then-broken (C2 Schur wall); `mu_DW` structurally free (H24);
`f_2` predicted/forced by AF, `f_0` relevant/free (H57/H60); DE<->spin-2 co-presence forced, DE magnitude free
(path 4); the operator constants forced (H1/H48). `[x]` = characterization's call MATCHES the actual status;
`[MISS]` = mismatch.

| Quantity | ACTUAL | (a) dimensional | (b) discrete/cont | (c) SYMMETRY | (d) RG |
|---|---|---|---|---|---|
| count menu `{1,3}` | **forced** | dimensionless -> arena `[x]` | discrete -> arena `[x]` | invariant-subspace dims of `Lambda^2_+` under `Z/3` -> arena `[x]` | n/a |
| exact-replica structure | **forced** | dimensionless -> arena `[x]` | discrete -> arena `[x]` | unbroken SM-gauge singlet (frame `_|_` internal) -> arena `[x]` | n/a |
| **3-over-1 selection** | **free** | dimensionless -> arena `[MISS]` | discrete -> arena `[MISS]` | picks one invariant subspace; NOT fixed by the symmetry -> value `[x]` | n/a |
| generation masses | **free** | dimensionful -> value `[x]` | continuous -> value `[x]` | require family-symmetry breaking (Schur) -> value `[x]` | n/a |
| **mass RATIOS / hierarchy** | **free** | dimensionless -> arena `[MISS]` | continuous -> value `[x]` | non-degenerate ratio needs breaking (Schur: unbroken => ratio 1) -> value `[x]` | n/a |
| `mu_DW` (scale) | **free** | dimensionful -> value `[x]` | continuous -> value `[x]` | breaks scale-covariance (observer's ruler) -> value `[x]` | relevant/scale -> value `[x]` |
| **`f_2` (AF-predicted)** | **forced** | dimensionless -> arena `[x]` | continuous -> value `[MISS]` | irrelevant; fixed-point (Gaussian, scale-inv) datum -> arena `[x]` | fixed-point data -> arena `[x]` |
| `f_0` | **free** | dimensionless -> arena `[MISS]` | continuous -> value `[x]` | relevant direction (breaks scale inv) -> value `[x]` | relevant -> value `[x]` |
| DE<->spin-2 co-presence | **forced** | structural -> arena `[x]` | structural/discrete -> arena `[x]` | structural invariant of the one `|II|^2` action -> arena `[x]` | n/a |
| DE magnitude | **free** | dimensionful -> value `[x]` | continuous -> value `[x]` | requires vacuum-energy choice (breaking) -> value `[x]` | relevant -> value `[x]` |
| forced constants (`-4`, `-1/4`, wt 4) | **forced** | dimensionless -> arena `[x]` | discrete/structural -> arena `[x]` | conformal-covariance invariants -> arena `[x]` | n/a |
| loop positivity | **OPEN** | -- | -- | invariant/arena property; conjecture PREDICTS forced (the live test) | fixed-point property |

**Mismatch tally (over the DECIDED cases):**

- **(a) dimensional: 3 misses** -- `3-over-1`, `mass ratios`, `f_0` (all dimensionless-but-FREE). **FAILS.**
- **(b) discrete/continuous: 2 misses** -- `3-over-1` (discrete-but-free), `f_2` (continuous-but-forced).
  **FAILS.**
- **(c) SYMMETRY: 0 misses.** Sorts every decided case, INCLUDING all three that break (a)/(b). **SURVIVES.**
- **(d) RG: 0 misses on its domain, but n/a on 6 of 11** (count, replicas, 3-over-1, masses, mass ratios, DE
  co-presence, constants). **CORRECT-BUT-PARTIAL** -- it is (c) restricted to the RG sector.

**SYMMETRY / REP-THEORY specialist -- the two discriminators, worked explicitly:**

- **Mass RATIOS (the case that breaks (a)).** The collective generations are a **real-irreducible** doublet of the
  family symmetry (`Lambda^2_+ = 1 + 2`, C2/W72). By **Schur's lemma**, any family-symmetric mass operator is
  scalar on the doublet, so under the UNBROKEN symmetry the ratio `m_2/m_3 = 1` (degenerate). The observed ratio
  (`m_mu/m_tau ~ 1/17`) is `!= 1`, so it can only be specified by **breaking** the family symmetry. Hence the mass
  ratio -- although **dimensionless** -- is a **value** under (c). (a) miscalls it arena precisely because it is
  dimensionless; (c) gets it right because the discriminating property is "needs breaking," not "carries units."
  This is the sharp win: **(c) separates dimensionless-forced from dimensionless-free** where (a) cannot.
- **`f_2` (the case that breaks (b)).** `f_2` is a **continuous** (dimensionless) coupling, so (b) calls it a
  value -- but AF makes it **irrelevant**: it flows to the Gaussian fixed point regardless of initial data (H60,
  `beta_x = -kappa x^2 b_2`, `b_2>0` over the whole band). The Gaussian point is the **scale/conformal-invariant**
  point; being pinned there requires NO choice of vacuum -> `f_2` is fixed-point/**invariant** data -> **arena**
  under (c), matching its forced status. Contrast `f_0` (relevant, `+1` free parameter): flowing along it is set
  by `mu_DW` = a scale choice = **breaking** scale invariance -> value. So **(c) separates the two dimensionless
  couplings `f_2` (forced) and `f_0` (free) by irrelevant-vs-relevant = invariant-vs-breaking**, exactly as (d)
  does. (a) calls BOTH arena (both dimensionless) and so mis-sorts `f_0`; (b) calls BOTH value (both continuous)
  and so mis-sorts `f_2`. Only (c)/(d) split the pair correctly.

Note also that (c) sorts the **`3-over-1` selection** correctly (value: both rank-1 and rank-3 are `Z/3`-invariant
subspaces, so which is realized is NOT fixed by the symmetry -- it requires an extra selection), where BOTH (a)
and (b) miss it. That is a third independent case in (c)'s favor, and it is precisely the conjecture's
`{1,3} = {no-observer, observer}` reading, now made non-circular: the *menu* is the invariant structure (arena),
the *pick* is the vacuum selection (value).

---

## Step 4 -- non-circularity of (c), checked ruthlessly (PHILOSOPHER-OF-SCIENCE)

Does "symmetry-invariant" secretly re-import "forced"? Three probes:

1. **Order of determination.** The symmetry is fixed by GU's *structure*, independently of any forcing analysis:
   the family symmetry is the self-dual frame `SU(2)_+` (the self-dual half of `Spin(4)` in the `Spin(9,5)` rep,
   C2); the internal symmetry is the SM gauge group (a different tensor factor); the UV symmetry is the
   scale/conformal invariance of the Gaussian fixed point (H60). Given these, "is `X` invariant, or does specifying
   `X` require breaking one of them?" is answered by **rep theory / RG relevance alone** -- Schur's lemma, the
   invariant-subspace lattice, the sign of a one-loop beta -- with NO input about what GU "forces." The forcing
   question is asked *afterward and separately*. The two are logically independent, so the comparison
   "invariant => forced?" is synthetic. **Non-circular: PASSES.**
2. **The claim can be FALSE.** "Every symmetry-invariant is forced AND every symmetry-breaking-requiring quantity
   is free" is not analytic. Two concrete falsifying worlds (Step 5). A vacuous split has no such worlds; this one
   does. **PASSES.**
3. **The `structurally-free` vs `forced-but-uncomputed` guard.** (c) must not launder an epistemic gap into
   "value." Test case: `c_RS_weyl` is dimensionless and only banded `[1.02,1.82]` (H60) -- but it is a definite
   `ker-Gamma` heat-kernel number, merely uncomputed, so it is **forced-but-uncomputed = arena**, NOT structurally
   free. `mu_DW`, by contrast, is **structurally** free (H24: "scale-covariant geometry fixes only dimensionless
   ratios, overall scale structurally free" -- a symmetry statement, dilatation-covariance). (c) uses exactly this
   symmetry criterion to keep the two apart, so it does not smuggle. **PASSES.**

**One honest concession (the genericity caveat, carried, not hidden).** "Symmetric structure fixes its invariants;
specifying a symmetry-broken direction requires external input" is essentially **Curie's principle** -- it may hold
in ANY symmetry-based framework, not just GU. So satisfying (c) is **not** evidence that arena-fixing is GU's
*unique* signature (this is the bigger-story skeptic-withhold (1), "genericity"). BUT -- decisively for this gate --
**generic is not vacuous.** Vacuous = true by the definition of arena/value. Generic = true because of a real,
independently-statable theorem (Curie / Schur / RG-irrelevance) that happens to hold broadly. The latter is a
substantive, falsifiable structural fact. So the genericity caveat does **not** re-open the circularity; it
relocates the split's foundation from "a GU magic" to "a specific realization of Curie's principle in GU's arena,"
which is a legitimate -- and honestly-graded -- foundation for a theorem.

---

## Step 5 -- ADVERSARY: hunt counterexamples to (c)

The adversary's mandate: find a **forced symmetry-breaking value** or an **unforced invariant**, or a place (c)
still smuggles "forced."

- **Counterexample hunt 1 -- a forced symmetry-breaking value.** Is any board quantity requiring symmetry-breaking
  yet forced? Candidates: (i) the self-dual color-kinematics forcing of the count-carrier (Branch E Cand A) --
  would force a discrete SELECTION (breaking) -- but it **RELABELS** (`so(9,5)`-equivariant, carrier-blind; closes
  on BOTH carriers), forces nothing. (ii) A forced vacuum alignment / spurion fixing the mass ratio -- this is
  exactly the "one overturning thing" C2 hunted: a mechanism where the collective mass-splitting is FORCED *and
  ordered* by the enclosure structure. C2 found the structure predicts **degeneracy** and needs an **added,
  unordered** spurion -> the breaking is NOT forced. (iii) The source action's own non-uniqueness (shape-dim-1
  family + 2 scales, proven not forced) is precisely the statement that the vacuum-selecting data is unforced. **No
  forced symmetry-breaking value exists on the board.** (c) survives.
- **Counterexample hunt 2 -- an unforced invariant.** Is any quantity invariant under the unbroken symmetry yet
  free? The dangerous candidate is `f_0`: a dimensionless coupling sitting at the same Gaussian fixed point as
  `f_2`. But `f_0` is the **relevant** direction (H60: `f_0^2` marginally relevant), i.e. a direction of scale-
  symmetry breaking, so (c) classifies it as breaking-required = **value**, matching its free status -- it is NOT
  an invariant. The only way to get an *unforced invariant* is Hunt-2's live version: **if AF FAILED** -- if the
  Gaussian point had TWO relevant directions in the `(f_2,f_0)` plane -- then `f_2` would be fixed-point-sector data
  that is nonetheless FREE. AF (H60) is what makes `f_2` irrelevant; that is a computed fact, not a definition, so
  the "invariant => forced" edge at `f_2` is **contingent on AF**, hence falsifiable. **No unforced invariant on
  the current board.** (c) survives, contingently and honestly.
- **Smuggle check.** Does (c) ever call something "invariant" only *because* it noticed it was forced? No: every
  arena call in the table is backed by an independent symmetry witness (invariant-subspace lattice; gauge-singlet
  commutation; conformal covariance; RG-irrelevance). The adversary cannot point to an arena call whose only
  warrant is "it turned out forced." **No smuggle found.**

**Adversary verdict:** (c) has no counterexample on the current board; its two vulnerable edges (`f_2` forced,
`3-over-1`/masses free) are exactly the places where an independent computed fact (AF; Schur non-forcing of the
breaking) is doing the work -- which is what makes the claim contentful rather than definitional. The adversary
does land one lasting mark: the genericity caveat (Curie), carried above.

---

## Step 6 -- the falsifiability statement (a possible world where "arena forced, value selected" is FALSE)

The claim is falsifiable because two concrete counterfactual worlds would break it, and in the ACTUAL world both
are checked to NOT obtain:

- **World A -- a forced symmetry-breaking value.** GU's geometry forces a specific vacuum alignment / `ker-Gamma`
  spurion that fixes the collective mass ratio `m_tau/m_mu` to a definite geometric number with NO external input
  (e.g. a forced ratio of `ker-Gamma` eigenvalues that lifts the Schur degeneracy in a determined direction). Then
  a symmetry-breaking-requiring quantity would be FORCED -- arena forces a value -- and (c) is FALSE. *Actual
  world:* C2 shows the enclosure structure predicts degeneracy and supplies neither the breaking nor its ordering;
  the mass ratio is free. So (c) holds -- but the world where it fails is concrete and was actively searched.
- **World B -- an unforced invariant.** AF fails: the Gaussian fixed point has two relevant directions in the
  `(f_2,f_0)` plane, so `f_2` is fixed-point-sector (scale-invariant) data that is nonetheless a free parameter.
  Then a symmetry-invariant would be UNforced and (c) is FALSE. *Actual world:* H60 makes `f_2` marginally
  irrelevant (AF, `b_2>0` over the whole band), so `f_2` is forced. (c) holds -- contingently on the computed AF
  fact, hence falsifiable. **The LIVE version of World B is loop positivity:** positivity of the Krein form on the
  AF trajectory is an invariant/arena property the conjecture PREDICTS is forced; if the AF trajectory is loop-
  **negative**, that is an arena property that fails to close -- direct pressure on the split. This is why H62 and
  the H61 loop-positivity question are coupled.

The existence of A and B -- describable, non-trivial, and actively checked to be absent -- is exactly what a
vacuous (self-sealing) split does NOT have. **The split is falsifiable.**

---

## Step 7 -- REFEREE grades, SYNTHESIZER verdict

**REFEREE.** (a) FAILS (3 misses: dimensionless-but-free `3-over-1`, mass ratios, `f_0`). (b) FAILS (2 misses:
discrete-but-free `3-over-1`, continuous-but-forced `f_2`). (d) CORRECT-but-PARTIAL (n/a off the RG sector; is
(c)'s shadow). (c) SURVIVES: 0 misses, non-circular (three probes passed), falsifiable (two concrete worlds),
counterexample-free on the board. The one legitimate withhold is **genericity** (Curie), which weakens
"GU-unique" but NOT "substantive/non-circular." Grade of the firm-up: **COMPUTED / analysis, HIGH confidence on
the sorting and non-circularity, MEDIUM on GU-specificity (genericity open).**

**SYNTHESIZER -- VERDICT: H62 FIRMED (the arena/value split is SUBSTANTIVE, not true-by-definition).**

The surviving non-circular partition is the **SYMMETRY characterization (c):**

> **ARENA** = what is fixed by the unbroken observer-invariant symmetry (rep-theoretic invariants; fixed-point /
> RG-invariant data). **VALUE** = what requires **symmetry-BREAKING** -- a choice of vacuum / frame / direction
> beyond the invariant structure -- to specify.

It is non-circular because invariance-vs-breaking is a group-theoretic / RG fact computable BEFORE and
INDEPENDENTLY of any forcing analysis (Schur, the invariant-subspace lattice, the sign of a one-loop beta). It
sorts ALL of the day's decided cases, including the two discriminators that break the naive characterizations --
the **mass ratios** (dimensionless-but-free; (a) fails, (c) correct via Schur) and **`f_2`** (continuous-but-
forced; (b) fails, (c) correct via RG-irrelevance) -- and the **`3-over-1` selection** (both (a) and (b) fail; (c)
correct). The RG characterization (d) is its RG-sector shadow and agrees on the overlap (`f_2` vs `f_0`), a
cross-check that the same one principle (invariant vs symmetry-broken) governs both the discrete/rep-theory sector
and the continuous/RG sector.

Because symmetry-breaking = a vacuum SELECTION = exactly what an observer/measurement does, the conjecture's
identification "**value = observer-selected**" coincides with "**value = requires breaking**" -- and the coincidence
is NON-CIRCULAR (it runs through the independent notion of symmetry-breaking, not through "forced"). So
"**the observer forces the symmetry-invariant structure and selects the symmetry-broken values**" is a
substantive, falsifiable claim, not a tautology.

**Load-bearing assumption.** That the relevant symmetries (self-dual frame `SU(2)_+`; internal SM gauge; scale/
conformal invariance of the Gaussian fixed point) are the RIGHT observer-invariant symmetries and are specifiable
independently of the forcing analysis -- which they are in GU (structural: frame vs internal factorization; the
Gaussian fixed point). If a future quantity's classification required INVENTING a symmetry to fit the forced/free
status, THAT would re-introduce circularity; the discipline is: fix the symmetry from structure first, classify
second.

**What it means for H61 / H63.**
- **H61 (Krein-TT campaign): mount it.** The arena it targets (the Krein UV structure, the fixed-point data, the
  modular conjugation) is genuinely symmetry-invariant, so proving the `C`-operator = Krein modular-conjugation
  identification is proving a REAL structural fact, not a definitional one. The expensive campaign is not chasing a
  tautology.
- **H63 (payoff theorem, Lawvere no-closure): mount it, but STATE it in symmetry-breaking language, not the
  circular forced/unforced language.** The theorem "no `J`-consistent closure across the firewall without a
  residual free selection" is STRENGTHENED, not weakened, when "free selection" is read as "a symmetry-breaking
  vacuum/frame choice" -- because that is precisely, and non-circularly, what an observer contributes. The single
  scope-down demanded by this gate: **do not claim the split is GU-UNIQUE.** Claim it is a substantive instance of
  Curie's principle realized in GU's specific arena (rep theory of `Lambda^2_+`; the Gaussian fixed point). H63's
  content is then "GU's observer-invariant structure admits no closure without an added symmetry-breaking
  selection," which is exactly the observer identification, honestly scoped.

**If the split had FAILED** (no non-circular characterization survived), the honest report would have been: the
conjecture's central claim is partly definitional, the payoff theorem proves less than advertised, and H61/H63
should be deferred. That is NOT the finding. **The finding is FIRMED via (c), with the genericity caveat carried.**

---

## Honest scope (what is and isn't established)

- **Established (analysis/computed, `tests/W73_H62_arena_value_partition.py`, exit 0):** the full test table; that
  (c) sorts every decided case correctly while (a) misses 3 and (b) misses 2; that (c) correctly sorts the two
  discriminators (mass ratios, `f_2`) and the `3-over-1` selection; that all four characterizations are
  non-circular by CONSTRUCTION (none references 'forced'), so the winner (c) is non-circular AND correct.
- **NOT established:** that (c) is GU-UNIQUE rather than generic Curie's principle (open, and it does not need to
  be unique for the split to be substantive); that H63 is proved (this note firms its *premise*, not the theorem);
  that loop positivity holds (open -- the live version of falsifier World B); that 3-over-1 is forced (it is not --
  it is a value under (c), consistent with the count staying OPEN).
- **No movement:** canon, RESEARCH-STATUS, claim-status, verdicts, posture, and the generation count are all
  unchanged; the arena/value split stays a MODEL of the program's outputs; the conjecture stays a conjecture; GU
  stays framework-not-theory. Exploration/analysis grade. No git commit (orchestrator verifies).

## Not claimed

Not a proof of the payoff theorem (only that its arena/value premise is non-circular and substantive); not a claim
that arena-fixing is GU's unique signature (the genericity caveat stands); not a derivation of any value (the
values remain the symmetry-broken, observer-selected data by construction); not a canon/verdict movement. A graded,
reproducible demonstration that the arena/value split can be made a PRECISE, NON-CIRCULAR partition (the SYMMETRY
characterization (c)), so the conjecture's central claim is NOT true-by-definition and H61/H63 are worth mounting,
scoped to symmetry-breaking language.

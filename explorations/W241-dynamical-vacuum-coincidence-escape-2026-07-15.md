---
artifact_type: exploration
label: W241
created: 2026-07-15
status: exploration
posture: "adversarial, truth-seeking, native-object first; construction-fork explicit; coherence-first; conditional register; RUTHLESS skeptic; grant every unbuilt piece; only a wrong definite output or a forced inconsistency falsifies; bar(b)/H59/count stay OPEN and Joe-gated; win condition is CHARACTERIZATION of an escape route, NOT flipping the verdict"
title: "W241 (lane B) -- the coincidence-admitting SMALLER-GROUP front door: does the dynamical vacuum isotropy escape the W234/W237 no-go WITHOUT a Z2-even compactifying condensate? VERDICT: NO ESCAPE -- the vacuum is FORCED NON-COINCIDENT for the purpose of the escape, and the located flaw HARDENS. The reason is order-parameter-agnostic: the good-stable requirement is COMPACT IMAGE (Prop 1), any compact-image isotropy has every generator commuting with the Cartan involution P (= the channel-D mass VEV direction) hence ALLOWS the gen-mirror mass and KILLS chirality; preserving chirality requires an unbroken off-diagonal grading BOOST Z (non-compact) hence NO good-stable grading. Coincidences (shared isotypic type under a smaller compact subgroup) live entirely inside the block-diagonal part: they change the C-grading MODULI (0 -> positive) but never produce a mass-forbidding boost, so they cannot rescue chirality. This LIFTS W237's condensate-specific COMPACTIFY<=>Z2-ODD to the isotropy-algebra level, which is why it binds the W219/W235 dynamical-vacuum front door, not just order parameters."
grade: "STRUCTURAL / EXACT for the finite-dimensional algebra facts (machine-verified, tests/W241_dynamical_vacuum_coincidence_escape.py, 46/46, exit 0, positive controls first; pure numpy on a faithful u(2,2) model, no hardcoded verdicts): the grading boost Z has real spectrum (non-compact, unbounded exp) while the block-diagonal anti-Hermitian generators have imaginary spectrum (compact); the invariant positive-definite majorant S=I exists on the compact set and provably fails on any boost set (Prop 1 witness both directions); [X,P]!=0 forces X off-diagonal so no compact generator forbids the mass ~ P (the steelman relative-phase R=diag(iI,-iI) commutes with P); {P,Z}=0; the coincidence detector distinguishes a genuine shared-type continuum (moduli>0) from the non-coincident unique case (moduli=0, W228); the full 2x2 table with the forbidden {good-stable AND chirality} corner EMPTY; the concrete smaller-group K' delivering a non-unique good stable yet still killing chirality. STRUCTURAL (flagged, same toy status as W224/W234/W237) for the lift of the u(2,2) two-pair model to the genuine Sp(32,32;H) arena: this is a faithful finite instance of the exact structural facts (compact = centralizer of the Cartan involution; boosts anticommute with the involution; Prop 1 = invariant-majorant-iff-relatively-compact-image), not a recomputation of the full quaternionic rep. INHERITED (flagged, not re-derived): W224/HARDENING-REPORT Proposition 1; W234's operator identity tau1(null)=sigma_3(definite)=P and the Sp(32)xSp(32) centralizer arithmetic; W237's COMPACTIFY<=>Z2-ODD structural theorem and the chirality<=>grading-boost-Z-survival identification; W228's forced-unique C-grading and the coincidence/degenerate-continuum classification; W235's record bit and its kinematic-grade forcing. CONDITIONAL on the W235 record bit (this result lives on the record-conserved, chirality-relevant branch). OPEN for the interacting source action, the physical state space, and the observable algebra. No canon / RESEARCH-STATUS / claim-status / verdict / posture change; bar(b) and H59 stay OPEN; the count stays {1,3}; no forbidden target {3,8,24,chi(K3),Ahat} assumed or inserted. Zero em dashes."
construction: "Construction fork NAMED per GEOMETER-VS-PHYSICS-OBJECTS.md and load-bearing. PROGRAM-NATIVE where the objects are GU's: the dynamical vacuum isotropy as the stabilizer of the interacting vacuum + observable algebra inside the non-compact arena Sp(32,32;H) (W219/W224); the grading boost Z = tau3(null) = sigma_1(definite) and the Cartan involution / channel-D mass VEV P = tau1(null) = sigma_3(definite), related by the fixed hyperbolic rotation of the 96 null pairs of ker(Gamma) in Cl(9,5)=M(64,H) (W234/W173); the good-stable C-commutant stabilizer and its forced-unique kinematic grading (W228). STANDARD-FIELD where the machinery binds any construction and is ported/cited: Proposition 1 (invariant positive majorant exists iff relatively compact image; HARDENING-REPORT); the Krein grading-moduli classification (moduli = sum over shared isotypic types; W228); the maximal-compact = centralizer-of-Cartan-involution fact. The escape question LIVES ON BOTH sides and the characterization names which side each level lands: the ESCAPE HOPE is standard-field (a smaller compact group with a coincidence, or a non-full compactification), and the KILL is program-native + Prop-1 structural (the grading is intrinsically the boost Z, forced non-compact by {P,Z}=0, so compact image and chirality cannot coexist regardless of coincidence). The reservoir Krein sign / r* stay gated TI/TaF finality objects (one-way rule respected; no cross-repo identity asserted)."
depends_on:
  - explorations/W235-central-bit-mirror-record-vs-redundancy-2026-07-15.md
  - explorations/W237-channel-s-condensate-isotropy-2026-07-15.md
  - explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md
  - explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md
  - explorations/W231-close-a3-smg-realization-gu-mirror-2026-07-14.md
  - explorations/W228-close-a1-corrected-sign-gu-instance-2026-07-14.md
  - explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md
  - papers/drafts/structurally-forced-internally-undecidable/HARDENING-REPORT.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W241_dynamical_vacuum_coincidence_escape.py
cross_repo:
  - "time-as-finality / temporal-issuance: this result lives on the record-CONSERVED branch of the W235 central bit (the chirality-relevant reading) and does NOT touch or re-litigate the reservoir Krein sign or the Y14 spectral section. It characterizes one escape route for GU's good-stable and finds it closed; no GU claim moves, no TI/TaF claim moves, no identity asserted. One-way rule respected."
---

# W241 (lane B) -- the coincidence-admitting smaller-group front door

Test / characterization certificate: `tests/W241_dynamical_vacuum_coincidence_escape.py`
(46/46, exit 0, positive controls first). Four personas ran INLINE in one worker (Krein /
Prop-1 positive-majorant specialist; Lie-isotropy / centralizer specialist; GU-structure /
grading-boost specialist; ruthless skeptic); no sub-agents. Zero em dashes. This is lane B of
the Wave 4 escape hunt: while lane A (W240) tests whether the condensate no-go generalizes to a
structural no-go for ALL Z2-even VEVs, lane B attacks the DIFFERENT escape route flagged by
W235/W228 -- the coincidence-admitting smaller dynamical isotropy group.

## Result in one paragraph

**The coincidence escape does NOT exist; the vacuum is FORCED NON-COINCIDENT for the purpose of
the escape, and the located flaw HARDENS.** The W235/W228 flag was that the DYNAMICAL good-stable
stabilizer is unbuilt (W219), and IF it were a strictly smaller, coincidence-admitting group, a
shared `+/-` isotypic type could reappear and deliver a good grading via a mechanism OTHER than
full `Sp(32) x Sp(32)` compactification -- escaping the W234/W237 condensate no-go without a
Z2-even compactifying condensate. W241 closes that door with an order-parameter-agnostic
argument at the ISOTROPY-ALGEBRA level. The good-stable requirement is precisely **compact
image** (Proposition 1, W224/HARDENING-REPORT: an admissible positive majorant `eta.C > 0`
exists iff the isotropy has relatively compact image). Any compact-image isotropy has every
generator **block-diagonal**, hence commuting with the Cartan involution `P = diag(I_32, -I_32)`
which is exactly W234's channel-D gen-mirror mass VEV direction; so a compact-image vacuum
**allows the mass `~ P` and KILLS chirality**. Preserving chirality requires the gen-mirror mass
`~ P` to be **forbidden** as an isotropy invariant, i.e. some generator `X` with `[X, P] != 0`;
but `[X, P] != 0` forces `X` **off-diagonal = a boost**, in particular the grading boost
`Z = tau3(null) = sigma_1(definite)` (`{P, Z} = 0`), which is **non-compact**, so the isotropy
has non-compact image and by Proposition 1 admits **no** good-stable grading. The forbidden
corner `{good-stable AND chirality}` is therefore **empty for every dynamical isotropy**,
coincidence or not. Coincidences (a smaller compact subgroup under which a `+` type and a `-`
type branch to a shared irreducible) live **entirely inside the block-diagonal / compact part**:
they change the `C`-grading **moduli** (`0 ->` positive, the W228 continuum) but never produce a
mass-forbidding boost, so they cannot rescue chirality. This **lifts W237's condensate-specific
`COMPACTIFY <=> Z2-ODD` to the isotropy-algebra level**, which is exactly why it binds the
W219/W235 dynamical-vacuum front door and not merely order parameters. `bar(b)`, `H59`, and the
count stay OPEN and Joe-gated; the result is conditional on the W235 record bit.

## Construction fork (named, load-bearing)

The object "the dynamical vacuum isotropy that delivers the good stable" has a standard-field
reading and a program-native reading, and the escape hope and its kill land on opposite sides.

- **Standard-field ESCAPE HOPE.** Default to representation-theory intuition: a smaller compact
  isotropy group can have a richer isotypic decomposition, so a `+` constituent and a `-`
  constituent might branch to the same irreducible (a "coincidence"), and a coincidence yields a
  positive-dimensional family of admissible `C`-gradings (W228's degenerate case) -- so "a good
  grading exists" via a mechanism that is not the full maximal-compact reduction. Under this
  default one silently assumes that "smaller compact group with a coincidence" is a fresh way to
  reach the good stable that dodges the compactification cost.
- **Program-native KILL.** GU's grading is not a free label. The mirror grading is the boost
  `Z = tau3(null) = sigma_1(definite)`, and the compact-reduction / mass direction is the Cartan
  involution `P = tau1(null) = sigma_3(definite)`, with `{P, Z} = 0` (W234/W237). The good stable
  is an invariant positive majorant, which exists iff the isotropy has compact image
  (Proposition 1). Compact image means the isotropy is contained in a maximal compact = a
  centralizer of a Cartan involution `~ P`, hence commutes with `P`, hence allows the mass. The
  grading `Z` is intrinsically the boost; keeping it (chirality) is intrinsically non-compact.

**Which side, and why.** The answer lives on the native side and is decisive. The escape hope is
a category error: a coincidence is a statement about the isotypic decomposition of the
**block-diagonal / compact** part of the isotropy, and it can only be present once you have
**already** reduced to a compact-image group. The reduction to compact image is the step that
costs chirality (it requires breaking the grading boost `Z`), and the coincidence lives entirely
**downstream** of it. Per the fork discipline the kill is checked in the other construction: in
the standard-field reading one never notices that the grading is the boost `Z`, so one imagines a
compact "chirality charge" (the steelman relative phase `R = diag(iI, -iI)`) protecting the
generation -- but `R` commutes with `P` and so does NOT forbid the mass. The native reading
exposes that every compact generator commutes with `P`, so no compact symmetry can protect
chirality. Defaulting silently to either side is the failure mode: the native side does not get
to declare "no good stable, done" (that would flip `bar(b)`); the standard side does not get to
declare "coincidence rescues it" (it does not). The honest statement is the mutual exclusion plus
the coincidence-is-downstream fact.

## The worked characterization

### 1. Precisely what "coincidence-admitting" means here (goal 1)

W228 gave the exact classification. For a real Krein space `(V, eta)` and a compact stabilizer
`K`, the admissible good-stable gradings `{C : C^2 = I, C eta-self-adjoint, eta.C > 0}` form a
space of real dimension `sum_lambda dim_R(D_lambda) a_lambda b_lambda`, where `lambda` runs over
irreducible `K`-types, `D_lambda in {R, C, H}`, and `(a_lambda, b_lambda)` is the `+/-`
multiplicity of type `lambda`. The grading is **unique** (moduli `0`, the "canonical" case, W228)
exactly when **no type occurs on both signs** (non-coincidence). A **continuum** appears **only**
in the **degenerate** case where a `+` constituent and a `-` constituent are the same irreducible
`K`-type -- that is precisely a **coincidence**. So "coincidence-admitting smaller group" means: a
subgroup `K' subset Sp(32) x Sp(32)` under which the `+` and `-` sectors branch to share an
irreducible, giving `moduli > 0`. The escape hope reads this as "a good grading is delivered
(indeed a whole family) by `K'` without the full compactification."

The test's coincidence detector (`grading_moduli` = number of shared types) is validated both
directions (PC-3): non-coincident (max compact, disjoint types) gives `0`; a genuine shared type
gives `> 0`; a disjoint relabelling stays `0`. It has teeth exactly as the task requires: it
distinguishes a genuine shared-type coincidence from a non-coincident case.

### 2. The isotypic decomposition under a smaller dynamical isotropy (goal 2)

Model the arena faithfully as `u(2,2)` on the definite basis `(e+^1, e+^2, e-^1, e-^2)`,
`eta = diag(+1, +1, -1, -1)` (two Krein pairs; a finite instance of the exact structural facts of
`Sp(32,32;H)`). The maximal compact is `U(2)_+ x U(2)_-` = the centralizer of the Cartan
involution `P = diag(I, -I)`; the boosts are the off-diagonal block. The grading boost is
`Z = [[0,I],[I,0]] = sigma_1(definite)`, with `{P, Z} = 0` (checks PC-2).

Now take a genuinely smaller compact isotropy `K' subset U(2)_+ x U(2)_-` under which a `+` type
and a `-` type branch to a shared irreducible (a coincidence). Two facts (Section C of the test):

1. `K'` **is compact-image**, so a good-stable grading **exists** -- in fact a **continuum**
   (`moduli > 0`), the W228 degenerate case rather than the unique `C`. So the escape hope is
   partly right: a coincidence-admitting smaller group **does** admit good gradings.
2. `K'` is **still block-diagonal** (it sits inside `U(2)_+ x U(2)_-`), so **every** element of
   `K'` **commutes with `P`**. Hence the gen-mirror mass `~ P` is `K'`-invariant = **allowed**, so
   `K'` **kills chirality** exactly as the full compactification does.

The coincidence delivers a (non-unique) good stable at the **same** cost as the condensate route:
chirality lost. The escape it was hoped to provide does **not** exist (checks C1-C5).

### 3. The master exclusion (goal 3): why no coincidence can rescue chirality

The decisive, order-parameter-agnostic argument (checks A1-A8):

- **Good-stable `<=>` compact image `<=>` commutes with `P`.** By Proposition 1 the good-stable
  grading (invariant positive majorant `eta.C > 0`) exists iff the isotropy has relatively compact
  image. Compact image means the isotropy algebra contains no boost, i.e. is contained in a
  maximal compact = centralizer of a Cartan involution `~ P`, i.e. every generator commutes with
  `P`. The test witnesses both directions: the compact set admits the invariant majorant `S = I`;
  any boost set does not (PC-1).
- **Chirality `<=>` mass `~ P` forbidden `<=>` an unbroken boost.** Chirality is preserved iff the
  gen-mirror Dirac mass `~ P` is forbidden as an isotropy invariant, i.e. some generator `X` has
  `[X, P] != 0`. But `P = diag(I, -I)` is block-diagonal, so `[X, P] != 0` forces `X`
  **off-diagonal = a boost** -- in particular the grading boost `Z`. A boost is **non-compact**,
  so its presence makes the image non-compact and (Proposition 1) destroys the good stable.
- **The corner is empty.** Good-stable forces every generator to commute with `P` (mass allowed,
  chirality dead); chirality forces an unbroken boost (non-compact, no good stable). The corner
  `{good-stable AND chirality}` is **empty for every isotropy**. The steelman -- a compact
  "chirality charge" `R = diag(iI, -iI)` -- fails precisely because `R` commutes with `P`
  (checks A7-A8, PC-2): no block-diagonal (compact) generator can forbid the mass.

Coincidence is orthogonal to this. The 2x2 table (Section B) over `{coincident, non-coincident} x
{Z broken, Z kept}` shows: the `(good-stable, chirality)` verdict depends **only** on whether the
grading boost `Z` is broken, never on the coincidence; the coincidence changes only the
`C`-grading `moduli` within the compact column. The forbidden corner stays empty in all four
cells. So a coincidence-admitting smaller group cannot open it: **the vacuum is forced
non-coincident for the purpose of the escape** -- more precisely, whether or not a coincidence
exists is moot, because the escape is blocked one step earlier, at "reach compact image at all."

### 4. Why this lifts W237 to the front door

W237 proved `COMPACTIFY <=> Z2-ODD` for null-pair **bilinears** (condensate order parameters):
the unique compact-reduction direction is the Cartan involution `P`, which is Z2-odd, and every
Z2-even bilinear maps to `{singlet, boost}`. W241 shows the same content at the **isotropy-algebra
level, with no reference to an order parameter**: the good stable is compact image; compact image
means the isotropy is a centralizer of a Cartan involution `~ P`; `P` is Z2-odd (`{P, Z} = 0`);
so compact image is the "the vacuum has selected a `~ P` (Z2-odd) reduction" statement, and that
is exactly what allows the mass and kills chirality. This is why the no-go binds the **dynamical
vacuum isotropy** (the W219/W235 front door) directly, not just condensates: however the vacuum
reaches compact image -- condensate, higher-rank tensor, or an unmodelled interacting mechanism --
it has selected a `~ P` reduction and paid the chirality cost. The grading `Z` is intrinsically
the boost; there is no compact avatar of it.

## Composition with lane A (W240), and exhaustiveness

Stated explicitly, as the brief requires.

- **Lane A (W240)** attacks the order-parameter side: does the condensate no-go (W234/W237)
  generalize to a structural no-go for **all** Z2-even VEVs (bilinear through higher rank)? If yes,
  no chirality-safe **order parameter** can compactify the arena.
- **Lane B (W241, here)** attacks the front-door side: can a **smaller / coincidence-admitting
  dynamical vacuum isotropy** deliver the good stable **without** a compactifying condensate? No --
  because any compact-image isotropy already requires selecting a `~ P` (Z2-odd) reduction that
  breaks the grading boost `Z`, and coincidences live downstream of that and cannot rescue
  chirality.

**How they compose.** The two lanes attack the two hoped-for escapes from the same master fact:
the good stable **is** compact image (Proposition 1, unconditional and order-parameter-agnostic),
and reaching compact image **is** selecting a `~ P` (Z2-odd) reduction. The two escapes are
exactly (A) "make the reducing order parameter Z2-even" and (B) "avoid fully reducing / use a
coincidence instead." Lane A closes (A); lane B closes (B). **If both hold, the located flaw
HARDENS from "no native condensate delivers the good stable on the record-conserved branch"
(W237) to "no dynamical vacuum whatsoever delivers a chirality-safe good stable," modulo the one
residual below.**

**Are A + B exhaustive?** Within the standing framing "good stable = an admissible Krein positive
majorant," **yes**: every route to the good stable passes through compact image (Proposition 1),
and A + B close both ways of hoping to pass through it chirality-safely. The **only** conceivable
third route **denies Proposition 1** -- a genuinely different notion of good-stable / ghost
clearance that does not demand a relatively compact image (for example a positivity that is not an
invariant majorant at all). That is a **different object**, not a coincidence escape, and it is
out of scope here; it is the honest residual that keeps `bar(b)`/`H59` OPEN rather than falsified.
So: A + B together are exhaustive **modulo denying Proposition 1**, and that residual is named,
not hidden.

## Skeptic pass (why neither "escape found" nor "GU falsified" survives)

**Steelman "escape found."** A smaller compact `K'` with a coincidence admits good gradings (a
whole continuum), so a good stable is delivered without the full `Sp(32) x Sp(32)` reduction --
is that not the escape? **No.** `K'` is still block-diagonal, still commutes with `P`, still
allows the gen-mirror mass, still kills chirality. The coincidence buys a non-unique grading, not
a chirality-safe one. The escape needed the `{good-stable AND chirality}` corner; that corner is
empty regardless of coincidence.

**Steelman "GU falsified (no good stable exists)."** The corner is empty, so on the
record-conserved branch GU cannot have both a chirality-safe generation and a good-stable grading
from any dynamical vacuum -- is that a kill? **No.** Unbuilt `!=` false. This is a **located
flaw**, not a forced inconsistency: (i) it is conditional on the W235 record bit (the
chirality-relevant branch); (ii) it is conditional on the standing "good stable = Krein positive
majorant" framing (Proposition 1), whose denial is the named residual route; (iii) the interacting
source action, physical state space, and observable algebra are still unbuilt (W219). A precise,
hardened located gap is progress under the constructive-obstruction protocol, not a disproof.

**Is this a relabeled punt?** No. It does three things the priors did not: (a) it **lifts** W237's
condensate-specific `COMPACTIFY <=> Z2-ODD` to an **order-parameter-agnostic** statement about the
isotropy algebra, which is what makes it bind the W219/W235 dynamical-vacuum front door and not
just order parameters; (b) it **kills the specific escape** W235/W228 flagged (coincidence-
admitting smaller group) by showing coincidences are downstream of, and orthogonal to, the
chirality obstruction; (c) it **states the exhaustiveness** of the A + B pair and **names the one
residual** (denying Proposition 1), so the front door is characterized, not merely poked.

## This does NOT resolve bar(b) / H59

Explicitly, and by design. `bar(b)`, `H59`, and the generation count are the objects this escape
was hoping to move; they stay **OPEN and Joe-gated**. W241 reports a **characterization**: on the
record-conserved branch, the coincidence-admitting smaller-group front door does not deliver a
chirality-safe good stable, because the good-stable requirement is compact image and that is
mutually exclusive with keeping the grading boost `Z`, independent of any coincidence. It does not
build the dynamical stabilizer, the source action, or the observable algebra; it does not deny
Proposition 1 (the named residual); it does not decide the W235 record bit. No canon /
RESEARCH-STATUS / claim-status / verdict / posture change; the count stays `{1, 3}`; no forbidden
target `{3, 8, 24, chi(K3), Ahat}` assumed or inserted; no cross-repo identity asserted; the
reservoir Krein sign / `r*` stay gated TI/TaF finality objects.

## What this changes and what it does not

Changes (exploration-tier, no canon movement):

- Closes the **coincidence-admitting smaller-group** escape route (the W235/W228 flag): the
  vacuum is forced non-coincident for the purpose of the escape; a coincidence changes the
  `C`-grading moduli but never rescues chirality.
- **Lifts** W237's `COMPACTIFY <=> Z2-ODD` from null-pair bilinears to the **isotropy-algebra
  level** (Prop 1 compact image `<=>` commutes-with-`P` `<=>` mass allowed), so it binds the
  dynamical vacuum isotropy front door directly.
- **Hardens** the located flaw (composing with lane A): from "no native condensate delivers the
  good stable on the record-conserved branch" toward "no dynamical vacuum delivers a chirality-safe
  good stable," modulo the named Proposition-1 residual.

Does not change:

- `bar(b)`, `H59`, and the generation count remain **OPEN** and **Joe-gated**. No RESEARCH-STATUS,
  claim-status, verdict, or posture movement.
- Does not build the dynamical stabilizer, source action, physical state space, or observable
  algebra; does not deny Proposition 1; does not decide the W235 record bit.
- The finite `u(2,2)` model is a faithful toy of exact structural facts, not the full
  `Sp(32,32;H)` rep. A Lean port of the master exclusion (`{P, Z} = 0`, the boost-vs-compact
  spectrum test, and the Prop-1 majorant construction are all finite and exact) is a follow-up
  only (no Lean run here, per the machine-wide serialized-build rule; a sibling worker is
  concurrent).

## Highest-value follow-up

Attack the one **named residual**: does denying Proposition 1 open a genuinely different
good-stable? Concretely, is there a GU-native notion of ghost clearance / physical positivity that
does **not** require an invariant positive majorant (relatively compact image) -- for instance a
PT / pseudo-Hermitian positivity on a proper subspace, or a boundary/firewall positivity
(`canon/firewall-boundary-hypothesis.md`) that lives on the interface rather than the bulk arena?
If such an object exists and is chirality-compatible, it is the ONLY escape A + B leave open; if a
`{P, Z}`-type argument forbids it too, the located flaw becomes an unconditional structural no-go
(a clean, GU-independent result about Krein good-stables with an anticommuting grading boost). This
is the single computation that would move the flaw from "hardened and located" to either "escaped
by a non-majorant positivity" or "structural no-go."

**Artifacts:** this file + `tests/W241_dynamical_vacuum_coincidence_escape.py` (46/46, exit 0;
positive controls first).

*Filed 2026-07-15 by W241 (lane B of the Wave 4 escape hunt). Four personas inline in one worker
(Krein / Prop-1 positive-majorant; Lie-isotropy / centralizer; GU-structure / grading-boost;
ruthless skeptic); no sub-agents. Reproducible:
`python -u tests/W241_dynamical_vacuum_coincidence_escape.py` (46/46, exit 0). Exploration grade;
characterization not resolution; no canon movement; `bar(b)` / `H59` / the count OPEN. Zero em
dashes.*

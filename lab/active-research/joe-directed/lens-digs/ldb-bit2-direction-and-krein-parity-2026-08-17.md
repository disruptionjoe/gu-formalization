---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-17
work_item: LD-B
channel: lens-digs
wave: sg4-bit-2 lens-dig (LD-A / LD-B / LD-C / LD-D)
assigned_concerns: [3, 4, 5, 8, 9]
target_claim: "INTERNAL — canon/ghost-parity-krein-synthesis.md numbered result 3,
  verbatim: 'Restricted to the triplet sector, `K` has signature exactly
  `(+96, -96, 0)` in `(9,5)`, `(7,7)`, and `(14,0)`. Each chirality half is
  totally null; the form is purely the cross-pairing between a generation and
  its mirror.' The kill targets ONLY the scope of the second sentence at the
  THIRD enumerated signature. NO GU source claim is targeted, attacked or
  defended; the two physical horns are untouched and confirmed; the
  Turok-Bateman reading, the R3 fence on the physical horns, and the generation
  count are all unaffected."
target_claim_verdict: "NARROW KILL, ONE SIGNATURE WIDE, AND THE REPAIR IS A
  PARITY CRITERION. Confirmed on both physical horns: at `(9,5)` and `(7,7)`
  each chirality half of the 192-dim triplet is TOTALLY ISOTROPIC (signature
  `(0,0,96)`, `||K|half|| ~ 2e-14`). Refuted at the third enumerated signature:
  at `(14,0)` the halves are DEFINITE, `(+96,0,0)` and `(0,-96,0)`, with
  `||K|half|| = 9.80` — because at `q = 0` the Krein metric `beta_S` is the
  product of ALL fourteen gammas, i.e. `beta_S` IS the chirality operator, so
  `K = I_14 (x) chi`. The governing fact, never stated anywhere in the
  repository, is a PARITY criterion: the halves are totally null IFF the number
  of timelike directions `q` is ODD. Verified exactly on an eight-point sweep
  `q = 0..7` with THREE distinguishable outcomes (null at odd `q`; definite at
  `q = 0`; `(48,48)` at `q = 2,4,6`), so the instrument is not blind. Both
  SIGNATURE-AMBIENT horns have odd `q` (5 and 7), so every physical conclusion
  drawn from the sentence survives — the defect is scope, not physics. Rider:
  the R3 fencing theorem's CONCLUSION `Re tr(chi Pi_+) = 0` also fails at
  `q = 0` (value 96) and holds for every `q >= 1`, so the fence is
  horn-parity-contingent and its hypothesis `{K, chi} = 0` holds exactly at odd
  `q`. Second rider, new: at both physical horns every principal angle between
  a maximal `K`-positive subspace and each chirality half is exactly 45 degrees
  (all 96 principal cosines `= 1/sqrt(2)`), so the ghost-parity polarization and
  the chirality polarization are transverse — `dim(P ∩ chi_±) = 0` exactly."
grade: "EXACT-STRUCTURE / NUMERICAL-LINEAR-ALGEBRA. 79/79 checks, exit 0
  (~45 s). Integer-valued outputs (signatures, ranks, dimensions) computed by
  `eigvalsh`/`matrix_rank` at tolerance 1e-8 on exactly-constructed
  Jordan-Wigner Clifford generators; every asserted quantity is an integer or a
  quantity vanishing to ~1e-14 against a scale of ~9.8, so no borderline
  decision is load-bearing. Failure path: `--selftest` verifies the CLEAN
  BASELINE first (61/61, exit 0, no [FAIL] lines) and then drives 9/9
  machinery/reference mutations, EACH caught via a genuine [FAIL] line, never a
  bare nonzero exit. Non-vacuity four ways: banked canon numbers reproduced
  before extension (192-dim triplet, `(+96,-96,0)`, 96/96 halves); a contrary
  control at `q = 0` where the halves are DEFINITE and the fence FAILS, so
  presence is detectable and not just absence; an intermediate control at
  `q = 2,4,6` giving `(48,48)`, a third outcome neither null nor definite; and
  7 planted false facts each observed False plus one planted WRONG verdict card
  the coverage machinery is required to flag. NOT: an action, a vacuum, a
  scale, a spectrum, a reality map, an anomaly computation, a decoupling
  construction, a generation count, a resolution of SIGNATURE-AMBIENT, or any
  claim-status movement."
disposition: FIVE_CARDS_NO_MERGES__ITEM4_LITERAL_QUESTION_ALREADY_ANSWERED_BY_CANON_AND_THE_ANSWER_IS_NULL_NOT_POSITIVE__CANON_SCOPE_DEFECT_AT_14_0_KILLED_AND_REPAIRED_BY_A_TIMELIKE_PARITY_CRITERION__R3_FENCE_IS_HORN_PARITY_CONTINGENT__GHOST_PARITY_AND_CHIRALITY_POLARIZATIONS_ARE_EXACTLY_45_DEGREES_TRANSVERSE__BDD_NOGO_DOES_NOT_TRANSPORT_BECAUSE_SPIN_ACTS_DIAGONALLY_AND_KER_GAMMA_IS_NOT_U_TENSOR_S__ITEM3_INTRA_IRREP_DIRECTION_CHANGES_RANK_64_TO_32_ON_THE_NULL_CONE__ITEM5_FUNCTORIALITY_GENUINELY_ABSENT_AND_A_NONMONOTONICITY_WITNESS_EXISTS_UNPROPAGATED__ITEM8_MATCHING_IS_TYPED_AS_R4B_CHK2_NOT_UNTYPED_AND_IS_UNRUN__ITEM9_MISTARGETED_AT_A_SETTLED_FORK_BUT_THE_ONE_DIAL_OBLIGATION_R5_IS_REAL_AND_UNEXECUTED
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
rows_touched_structurally: []
rows_advanced: 0
rows_proposed: []
free_object_delta: 0
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - canon/escape-corners-campaign-RESULTS.md
  - tests/generation-sector/ghost_parity_krein.py
  - lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md
  - lab/active-research/joe-directed/base-duality/bd-d-the-quotient-cures-the-base-not-the-fibre-2026-08-15.md
  - lab/methods/gu-base-categories.md
  - lab/active-research/joe-directed/ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md
  - lab/active-research/joe-directed/phi-reduction/phi1-the-reduction-is-rank-one-and-the-14d-kernel-contributes-zero-bits-2026-08-15.md
  - lab/active-research/joe-directed/phi-reduction/phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md
  - explorations/decoupling-constructibility-packet-2026-08-12.md
  - lab/process/layer0-fork-registry.yaml
  - lab/sources/source-claim-register.yaml
scripts:
  - tests/channel-swings/joe_directed_ldb_bit2_direction_and_krein_parity.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders
> conventional particle-physics comparators. Cards 8 and 9 discuss 't Hooft
> anomaly matching, symmetric mass generation, and seesaw/Majorana vocabulary;
> every one of those is a fork-1 comparator object and binds only the named
> model. Card 4's BD-D leg discusses an IMPORTED free linearised Yang-Mills
> symbol quotient which is NOT GU's physical quotient (BD-D's own frontmatter:
> "GU has no derived Gauss law, interacting BRST/BV complex or physical
> quotient to which that condition can yet be transported"). It is not evidence
> for or against Weinstein's source-native mechanism without an explicit typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reusing.
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY` — §6 separates the
> source-native leg (the Krein form on GU's own declared `V (x) S` carrier at
> both SIGNATURE-AMBIENT horns; the insertion-direction rank on GU's declared
> `Ω^1(ad P)` slot) from the comparator leg (matching, SMG, seesaw taxonomy).

# LD-B — five concerns about "SG4 bit 2", one good-faith dig each

**Wave contract.** Each of the five gets its own card. No card was merged. The
dedupe test (§5) was run by quoting both one-liners in full and naming the
exact surviving nuance; every pair kept both cards with a cross-reference.

**Headline.** Digging changed three of five verdicts, and in both directions.
Item 4's literal question turned out to be **already answered in canon** — and
answered the *opposite* way from what the one-liner presupposes. Item 8's
"untyped" is **false**: the matching is typed, named, and merely unrun. Item
9 is **mis-aimed at a fork the repository settled the other way in 2026-08**.
Against that, item 5 came out **stronger** than its one-liner, and the item-4
dig turned up a genuine canon defect nobody was looking for.

---

## 1. Preflight — retrieval first, then six problem-matched lenses

Retrieval ran before any computation. Searched by object and by mechanism:
*Krein, ghost parity, (96,96), chirality half, null, isotropic, insertion, 68,
172, Grassmannian, VEV direction, functor, Layer category, Grant poset,
discharge, commute, 't Hooft, anomaly matching, spectator, imposter, third
family, spin-3/2, Rarita-Schwinger, decouple, one dial.*

**Lens 1 — Krein / indefinite-inner-product specialist.** *Route:* "does a half
sit positively" is only well-posed if the half is a NONDEGENERATE subspace. The
first thing to compute is not a signature but whether the form restricts to
zero. *Prediction:* `beta_S` is a product of `p` spacelike gammas and the
chirality operator is a product of all 14, so they commute or anticommute by
the parity of `p`; on an anticommuting horn every chirality half is totally
isotropic and the question dissolves. *Stake:* if they commute on a physical
horn, the prediction is dead and the concern is live as posed.

**Lens 2 — representation geometry / moduli.** *Route:* 68 and 172 are
dimensions of INVARIANT PAIRING spaces (coupling counts), not of the VEV space.
The moduli the concern wants is the VEV direction in `ad P` (16384-dim) modulo
gauge, times the coupling space. *Binding condition:* never write "68-dim
Grassmannian of insertions"; state which space each number counts.

**Lens 3 — category theory / functoriality.** *Route:* a commutation question
needs both structures to exist as categories first. Check whether CT-1 landed
`gu-base-categories.md`, and whether bit 2 is the arrow the concern names.
*Kill-or-switch:* if bit 2 is not the `±package → VEV-observed` arrow, the
concern's square is mis-drawn and must be redrawn before it can be answered.

**Lens 4 — anomaly / UV-IR matching specialist.** *Route:* matching is a
statement about two ENDS of a flow. PHI-1/2 compute at one scale. The
question is whether anyone has written the two-ended ledger. *Binding
condition:* distinguish "nobody computed it" from "nobody typed it" — the
one-liner asserts the latter and they are very different findings.

**Lens 5 — claim-targeting auditor (the wave's known failure mode).** *Route:*
repository memory records that GU kills routinely target claims the source or
the repository has already disavowed. Before crediting any concern, find the
register row or fork entry that owns its referent. *Stake:* item 9 names "the
third family" and "the spin-3/2 sector" in one breath; if the repository
settled those apart, the concern is mis-aimed however good its physics.

**Lens 6 — adversarial reading of my own framing.** *Route:* the wave rewards
finding live items, so the standing danger is inflating an already-covered
question into a discovery. Every card must run a grep for its own novelty
before claiming any. *Binding condition:* §7 carries both an inflation attack
and a deflation attack on every LIVE verdict.

**Cheapest kill-or-switch, recorded before computing.** If the chirality halves
turn out NONDEGENERATE on either physical horn, item 4 is live as posed and
this file leads with its signature. **Outcome: they are totally isotropic on
both horns; item 4 is not live as posed, and what IS live is a scope defect in
the sentence that already says so.**

**One credible contrary route, recorded before computing.** If the nullity were
signature-independent, there would be no parity criterion and the canon
sentence would be simply correct. **Computed: it is signature-dependent, the
discriminator is the parity of `q`, and the sentence's own enumerated scope
crosses the parity boundary.**

---

## 2. The two exact legs

Probe: `tests/channel-swings/joe_directed_ldb_bit2_direction_and_krein_parity.py`,
**79/79, exit 0**; `--selftest` baseline-first then **9/9 mutations caught via
a genuine `[FAIL]`**.

### 2.1 The parity criterion (item 4)

Objects, fixed: `V (x) S` at `D_7` (1792); the gamma-trace kernel
`ker(Gamma)` (1664); the self-dual `SU(2)+` top-Casimir stratum, the
**192-dim generation triplet**; `K = eta_V (x) beta_S` with `beta_S` the
product of the spacelike gammas; `chi` the product of all fourteen.

```
    q   sig      {K,chi}   [K,chi]    chi=+1 half     chi=-1 half     fence Re tr(chi.Pi_+)
    0  (14,0)    8.5e+01   0.0e+00   (+96, -0, 0)    (+0, -96, 0)     96.000   FAILS
    1  (13,1)    0.0e+00   8.5e+01   (0, 0, 96)      (0, 0, 96)        0.000   holds
    2  (12,2)    8.5e+01   0.0e+00   (+48, -48, 0)   (+48, -48, 0)     0.000   holds
    3  (11,3)    0.0e+00   8.5e+01   (0, 0, 96)      (0, 0, 96)        0.000   holds
    4  (10,4)    8.5e+01   0.0e+00   (+48, -48, 0)   (+48, -48, 0)     0.000   holds
    5   (9,5)    0.0e+00   8.5e+01   (0, 0, 96)      (0, 0, 96)       -0.000   holds  <- PHYSICAL
    6   (8,6)    8.5e+01   0.0e+00   (+48, -48, 0)   (+48, -48, 0)     0.000   holds
    7   (7,7)    0.0e+00   8.5e+01   (0, 0, 96)      (0, 0, 96)        0.000   holds  <- PHYSICAL
```

Readings, each machine-checked:

- **The full triplet signature is `(+96,-96,0)` at every one of the eight
  points** — the banked number is horn-blind, reproduced `[R]` before anything
  new was computed.
- **The chirality halves are totally isotropic iff `q` is ODD.** Three
  distinguishable outcomes appear, so the instrument discriminates: null at odd
  `q`, definite at `q=0`, `(48,48)` at even `q >= 2`.
- **`{K, chi} = 0` exactly at odd `q`; `[K, chi] = 0` exactly at even `q`.**
  This is the hypothesis of the R3 fencing theorem, and it is a parity fact.
- **The fence's CONCLUSION fails only at `q = 0`**, where `Re tr(chi Pi_+) = 96`.
  At even `q >= 2` it holds for a different reason (the `(48,48)` balance), so
  odd `q` is sufficient but not necessary for the fence.
- **Transversality.** At both physical horns all 96 principal cosines between a
  maximal `K`-positive subspace `P` and each chirality half equal `1/sqrt(2)`
  to nine decimals, and `dim(P ∩ chi_±) = 0`. A `K`-positive subspace contains
  no chirality eigenvector at all; the two polarizations sit at exactly 45
  degrees. (The `dim = 0` clause is a theorem for any choice of `P` — a null
  vector cannot live in a positive-definite subspace — and the 45-degree
  clause is computed for the canonical spectral `P`.)
- **Why `q = 0` is special, in one line:** at `q = 0` every direction is
  spacelike, so `beta_S` is the product of all fourteen gammas — it IS `chi`,
  and `K = I_14 (x) chi` is manifestly `±`-definite on the chirality halves.

**Rider, found by the probe's own mutation harness.** An early mutation that
dropped the gamma-trace constraint was INERT. That is a fact, not a harness
bug: the top-Casimir self-dual stratum is *automatically* gamma-traceless
(`||Gamma.Wt||/dim = 1.1e-16` computed without the projector), so `Pi` is
redundant for the triplet — though not for `ker(Gamma)` as a whole, which §2.3
uses. The mutation was replaced with an effective one; the fact is now a check.

### 2.2 The insertion direction (item 3)

Inside ONE declared insertion irrep — `Lambda^1 (subset) ad P`, a vector
`w ∈ V` — the insertion acts as `e_w : S_+ → S_-`, and the induced mass shape's
rank is `rank(e_w|_{S_+})`:

```
    (9,5):  generic w (w^2 = +4.389)  ->  rank 64      NULL w (w^2 = 0)  ->  rank 32
    (7,7):  generic w (w^2 = +0.410)  ->  rank 64      NULL w (w^2 = 0)  ->  rank 32
    (14,0): generic w                 ->  rank 64      NULL w: none exist
```

For non-null `w`, `e_w^2 = w^2 ≠ 0` so `e_w` is invertible; on the null cone
`e_w^2 = 0` and the rank halves. **Half the states that a generic direction
gives a mass shape to remain unpaired on a null direction** — and null
directions exist exactly when `q >= 1`, i.e. on both physical horns and not on
the Euclidean control. This is the INTRA-irrep stratification; ST-1 stratified
by irrep TYPE and stopped there.

### 2.3 The BD-D disanalogy (item 4, second leg)

BD-D's no-go has a hypothesis: `End_g(g) = R`, whence *"every `g`-submodule of
`Lambda^1 (x) g` is `U (x) g` for a unique `U`"*. BD-D itself records the
contrary case (`so(3,1)`, where `End_g(g) = C` and Part 1 "genuinely fails").
The fermionic module fails it far harder:

- `dim ker(Gamma) = 1664 = 13 · 128` — divisible, so dimension alone does not
  settle it;
- but `dim((v (x) S) ∩ ker Gamma) = 0` for every one of six random `v`
  (`e_v` is invertible for non-null `v`), so `ker(Gamma)` contains **no
  `v (x) S` line at all** and is not `U (x) S` for any `U`.

The structural reason: in BD-D the gauge group acts on ONE tensor factor, so
equivariant subquotients are forced to be `U (x) ad`. Here `Spin(p,q)` acts
**diagonally** on `V (x) S` and the Clifford contraction is equivariant and not
of the form `(map on V) (x) id`. **BD-D's no-go does not transport to the
fermionic Krein sector**, for a reason independent of the comparator-import
block.

---

## 3. The five cards

### CARD 3 — Representation geometry

> **One-liner, verbatim:** "ST-1's insertion spaces are 68- and
> 172-dimensional; 'bit 2 = ON' compresses a Grassmannian of *which* insertion
> to one boolean. The direction, not just the switch, decides the spectrum."

**(i) Strongest reconstruction.** ST-1 decides an EXISTENCE question — is there
any invariant zero-order pairing on the protected half — and answers it with a
boolean keyed to whether a class-2 insertion is present. But the physical
content of "the VEV is on" is a point in `ad P` (16384-dim) modulo gauge,
together with a choice of couplings; the induced mass form, its rank, and its
spectrum all vary over that space. A boolean is the right abstraction for
ST-1's question and the wrong one for any spectrum question.

**(ii) What the repo holds.** ST-1 already says this, at irrep granularity, and
says it explicitly. §4.5 is a per-irrep selectivity table ("which `ad P`
component feeds which cell"); §5 clause A2 records that *"per-irrep selectivity
(§4.5) constrains WHICH vacua can produce which textures"*; §4.5(2) states
verbatim that *"the Grassmann-live 0-form directions (`Λ^1, Λ^5`) are
chirality-blind"*, so an irrep-type choice cannot separate the two `ν` corners.
The minimal-`ad` control in §4.3 is already a direction-class witness: the bare
`so(14)` adjoint *"`Λ^2` alone as `Ω^1` coefficient feeds every same-class
cell"* but with multiplicities 2/5/13 against the full column's 14/34/90.
ST-1 §10 also disclaims *"that any specific multiplicity above is a coupling
count in the eventual action."*

**(iii) The bounded dig.** §2.2. The residual the repo does NOT hold is
stratification WITHIN one irrep. Computed exactly: a `Lambda^1` VEV direction
gives `rank(e_w|_{S_+}) = 64` generically and `32` on the null cone. The
degeneration locus is the light cone of the ambient metric, it is nonempty
exactly when `q >= 1`, and it is invisible to any irrep-type bookkeeping.

**(iv) Verdict: LIVE-MODERATE.** The concern's headline claim — direction
matters, not just the switch — is **half already-covered** (ST-1 §4.5, explicit
and machine-checked, at irrep granularity) and **half genuinely new** (the
intra-irrep null-cone stratum, computed here). It is not blocking: with no
action there is no coupling vector and hence no spectrum, so this is
Lane-1-owned downstream work, not an obstruction.

**(v) Proposed register item (PROPOSAL ONLY).** *"The insertion-direction
stratification of the declared bosonic slots is uncomputed below irrep
granularity. Known: the null cone of the ambient metric is a rank-degeneration
stratum for `Lambda^1` insertions (rank 64 → 32), nonempty iff `q >= 1`.
Unknown: the generic rank and the full stratification for the remaining
components, and whether any stratum is gauge-distinguishable. Owner: Lane 1
jointly with whoever owns the `ad P` shrinkage fork."* Not proposed for any
ledger row; no row is touched.

**(vi) Fidelity delta vs the one-liner.** **Two errors and one loss.**
(a) "ST-1's insertion spaces are 68- and 172-dimensional" mis-names the object:
68 and 172 are the dimensions of the *invariant pairing* spaces on `W_+` (ST-1
§4.3: `68  = 7 + 2·14 + 33`, `172 = 14 + 2·34 + 90`), i.e. coupling counts, NOT
the dimensions of an insertion/VEV space. (b) "a Grassmannian of *which*
insertion" is therefore the wrong moduli — the relevant space is the VEV
direction in `ad P` modulo gauge, and a Grassmannian is the wrong shape for it
(it is a cone/orbit space, and the interesting locus found here is a
quadric, not a Grassmannian stratum). (c) The compression LOST that ST-1
already answers the headline at irrep granularity — a distiller reading only
the one-liner would bank this as fully novel, which it is not.

*Cross-reference:* card 4. The null-cone stratum here and the parity criterion
there are driven by the same structure — the ambient metric's indefiniteness —
and both vanish at the Euclidean control. They are not the same claim (one is
about `ad P` insertions, one about the Krein form on the carrier), so both
cards stand.

---

### CARD 4 — Krein compatibility

> **One-liner, verbatim:** "does the selected half sit Krein-positively in the
> (96,96) pairing? The decoupling and BD-D's quotient result have never been
> checked against each other."

**(i) Strongest reconstruction.** Two independent legs. *Leg A:* SG4 bit 2
selects a chirality half; the generation sector carries an indefinite Krein
form with signature `(96,96)`; positivity of the selected half is what any
probabilistic reading needs, and it has never been checked. *Leg B:* BD-D
proved a no-go — no equivariant subquotient can cure an indefinite fibre form —
and if that transports, the decoupling cannot produce a positive sector at all.

**(ii) What the repo holds.** *Leg A is already answered, and answered NO.*
`canon/ghost-parity-krein-synthesis.md` numbered result 3 says verbatim:
*"Each chirality half is totally null; the form is purely the cross-pairing
between a generation and its mirror."* The 2026-07-06 banner adds the R3
fencing theorem: *"{K, chi} = 0 forces Re tr(chi Pi_+) = 0 for EVERY admissible
C"*, and concludes that the ghost-parity split *"is NOT a chirality selection,
and the mirror-selective datum is an import."* The same conclusion is reached
independently in `tests/anchored-leads/thooft_anomaly_matching_lever.py`: the
carrier is vectorlike `(+96/-96)`, hence carries zero 't Hooft anomaly.
*Leg B is genuinely unchecked*, and BD-D's own frontmatter pre-blocks half of
it: *"GU has no derived Gauss law, interacting BRST/BV complex or physical
quotient to which that condition can yet be transported."*

**(iii) The bounded dig.** §2.1 and §2.3 — a small computation against the
banked matrices, exactly as the brief anticipated. Three results:
1. **Confirmation on both physical horns.** The halves are totally isotropic;
   the selected half sits maximally NULL, never positively. The question's
   presupposition is false on exactly the horns GU lives on.
2. **A scope defect in the sentence that says so.** Canon's preceding sentence
   enumerates the scope as *"in `(9,5)`, `(7,7)`, and `(14,0)`"* — and at
   `(14,0)` the halves are DEFINITE, `(+96,0,0)`/`(0,-96,0)`. The repair is a
   parity criterion (null iff `q` odd), verified on eight points. Both physical
   horns have odd `q`, so no physics claim moves. The R3 fence inherits the
   same parity: its hypothesis holds exactly at odd `q`, and its conclusion
   fails exactly at `q = 0`.
3. **Leg B dissolves, twice over.** The comparator-import block is the shallow
   reason. The deep reason is that BD-D's Part-1 hypothesis has no analogue
   here: `Spin` acts diagonally on `V (x) S` and `ker(Gamma)` is not `U (x) S`
   (§2.3). BD-D's no-go does not reach the fermionic Krein sector.
4. **New corollary.** The ghost-parity polarization is exactly 45 degrees
   transverse to the chirality polarization — every `K`-positive direction is a
   50/50 chirality superposition, `dim(P ∩ chi_±) = 0`. This sharpens the
   banked "NOT a chirality selection" from a trace identity to a geometric
   statement about every admissible positive subspace.

**(iv) Verdict: ALREADY-COVERED (`canon/ghost-parity-krein-synthesis.md`
result 3 + the 2026-07-06 R3 fence banner) for Leg A as posed;
DISSOLVES for Leg B (type-blocked AND hypothesis-fails); LIVE-MODERATE for the
scope defect and the parity criterion the dig exposed.** The concern as written
would have been banked as a live gap on a question canon settled in July.

**(v) Proposed register item (PROPOSAL ONLY).** *"canon/ghost-parity-krein-
synthesis.md result 3: narrow the clause 'Each chirality half is totally null'
to odd-`q` signatures, or drop `(14,0)` from the preceding enumeration. State
the parity criterion (`{K, chi} = 0` iff `q` odd) as the governing fact, and
record that the R3 fence's conclusion fails at `q = 0`. Physical horns
unaffected — both have odd `q`. Owner: the canon file's owner; this is an
editorial narrowing with a probe attached, not a verdict change."* Also
proposed, separately: *"BD-D's no-go is scoped to modules where the group acts
on one tensor factor; it does not transport to `V (x) S`. Record the
disanalogy so the no-go is not cited against the fermionic sector."*

**(vi) Fidelity delta vs the one-liner.** **Large, and in the expensive
direction.** The one-liner presupposes the half might be Krein-positive and
that nobody checked; both are wrong, and canon's answer is the strongest
possible NO (maximally isotropic, not merely indefinite). The compression to
"has this been checked?" erased the fact that it HAS been, which is precisely
the failure mode that turns a settled result into a re-opened one. Conversely
the second clause — BD-D never cross-checked — is TRUE and productive: the
cross-check yields a real disanalogy the repo did not have. A distiller keeping
only the first clause would have banked a false gap and dropped the good half.

*Cross-reference:* cards 8 and 9. The "carrier is vectorlike ⇒ zero 't Hooft
anomaly" fact card 8 relies on IS this card's nullity, seen through a different
instrument; and this card's object (the triplet inside gamma-traceless
`V (x) S`) is card 9's spin-3/2 sector. All three stand separately: kinematic
signature (4), UV/IR consistency ledger (8), and decoupling dynamics (9) are
different questions about the same carrier.

---

### CARD 5 — Functoriality

> **One-liner, verbatim:** "bit 2 is the Layer-category arrow ±-package→
> VEV-observed. Does it commute with grant discharge (the Grant poset)? If not,
> discharge order matters and nobody has said so."

**(i) Strongest reconstruction.** If the Layer transitions form a category and
the grants form a poset with a discharge operation, then applying a layer arrow
and discharging a grant are two operations on the same state. If they do not
commute, the ORDER in which a channel discharges its grants and crosses bit 2
changes the result — and every artifact that reports a post-decoupling
conclusion under a set of grants is implicitly asserting one particular order.

**(ii) What the repo holds.** CT-1 landed `lab/methods/gu-base-categories.md`
**today**, and it is the only place either structure exists formally. The Layer
category `L` has four objects (declared-total, pullback, ±-package,
VEV-observed) and arrows LA1–LA4; the Grant poset `G` has nodes G0–G8 ordered
by inclusion of assumption sets, with discharge defined operationally as
movement along a dated `migrations[]` record. Critically, the decoupling arrow
IS already grant-indexed: it exists *"only under the `SC-CHI-01` hedge / SG4
bit 2 grant (**Grant-poset node G6**); in the `varpi → 0` phase the arrow is
absent."* And the commutation question is **absent** — no functor, no
naturality square, no open-question flag. Two facts make the absence
load-bearing rather than merely unaddressed: CT-1 explicitly denies
functoriality on the grant side (*"Movement of a ROW between nodes is not a
functor and not free"*), and the two grant nodes a square would need are held
incomparable (*"**No recorded arrow relates G3**"* — the chiral-16-shadow
selection — to G6, *"adjacent in prose ... but unidentified in the ledger"*).

**(iii) The bounded dig.** Archival, correctly — there is nothing to compute
until the square is drawn. Two findings beyond the retrieval. First, **the
one-liner mis-types the arrow.** Per CT-1 the decoupling arrow LA3 runs
`L1 → L4` (declared-total → VEV-observed), not `±package → VEV-observed`;
`L3 → L4` is not an arrow at all, and the reverse direction (`L4 → L3`,
operative-half assignment) is a NAMED NON-ARROW. Any commutation square must be
redrawn on LA3's actual domain before it can be asked. Second, **a
non-monotonicity witness already exists and was never propagated.** LA-5's
postflight records, in one sentence under a category-theory lens, that
discharging `AC-A1` is what *kills* `AC-F3`, so the grant→row map is *"not
monotone"* and the incidence matrix's all-`+1` sign structure is wrong for at
least one edge. That same document elsewhere asserts order-irrelevance for
reachability — so the order-independence argument rests on a matrix the
document itself says is mis-signed.

**(iv) Verdict: LIVE-HIGH.** Both structures now exist, the arrow is already
grant-indexed at G6, the commutation is genuinely absent, and there is a
concrete counterexample-shaped witness sitting unpropagated in a postflight.
This is the strongest of my five, and it got stronger under digging rather than
weaker.

**(v) Proposed register item (PROPOSAL ONLY).** *"Layer/Grant commutation is
undeclared. `LA3` (`L1 → L4`, the decoupling, SG4 bit 2) is indexed by Grant
node G6, but no functor `L → G`, no naturality square, and no order-sensitivity
statement exists. A known non-monotonicity (discharging `AC-A1` kills `AC-F3`,
LA-5 postflight) shows the grant→row map is not monotone, contradicting the
same document's order-irrelevance claim for reachability. Minimum ask: state
whether LA3 commutes with discharge, or declare the order-sensitivity
explicitly. Blocked upstream by G3/G6 incomparability, which CT-1 declines to
resolve. Owner: CT-1's channel jointly with the ledger-advancement channel."*

**(vi) Fidelity delta vs the one-liner.** **Two corrections, both material,
and the concern survives both.** (a) The arrow is mis-typed: LA3 is `L1 → L4`,
not `±package → L4`. (b) "nobody has said so" is *nearly* right but not
exactly: LA-5 said it once, in one sentence, about one edge, and it was never
propagated — which is a materially different (and more actionable) finding than
total silence, because it names a concrete witness. The one-liner's core
question is otherwise transmitted faithfully and is the wave's best item.

---

### CARD 8 — 't Hooft matching

> **One-liner, verbatim:** "the effective half's anomalies must match the
> total's *across* the decoupling. PHI-1/2 did comparator anomalies; the
> matching across bit 2 itself is untyped."

**(i) Strongest reconstruction.** A vectorlike UV has every 't Hooft anomaly
zero. If bit 2 produces a chiral IR, matching forces the visible sector's
anomalies to be cancelled by the mirror/dark sector for every surviving
symmetry — and a sector obliged to saturate a shared symmetry's anomaly cannot
be freely decoupled. This is the standard killer of emergent-chirality
proposals, and GU's configuration is exactly the one it targets.

**(ii) What the repo holds.** The concern is **already written down, verbatim,
and named as central**. `explorations/decoupling-constructibility-packet-
2026-08-12.md` criterion R4b is titled *"'t Hooft **anomaly matching between
the vectorlike UV** and the claimed chiral IR — the packet's central
obstruction"*, states the matching condition, invokes the SMG iff-criterion
including the mod-16 cobordism class, and types the settled-horn re-run as
`CHK-2`. The source side is typed too: `SC-CHI-50` (GU is not chiral, so the
chiral-anomaly critique misses) and `SC-CHI-51` (must produce an effectively
chiral world via a VEV in a Dirac-RS operator) are both `hard-core` /
`ADHERED`. W224 ran the ledger once and found it satisfied — but the packet
itself flags that run as *on the retired horn, with a horn-stale `SO(10)`-16
delivery, and with dynamical sufficiency GRANTED*. `thooft_anomaly_matching_
lever.py` separately shows matching is homogeneous in `n_gen` and hence vacuous
for the count.

**(iii) The bounded dig.** Archival. Confirmed: PHI-1 and PHI-2 contain **zero**
occurrences of "'t Hooft", "anomaly matching", "UV", "IR", or "decoupl" — they
compute at one scale and never invoke matching, exactly as the one-liner says.
Confirmed also: `spectator fermion` has **zero** hits repo-wide, so the
standard escape (adding spectators to saturate a ledger) has never been
proposed. But `CHK-2` — the settled-horn matching re-run — has never been
executed, and the packet that names it binds nothing (*"Design input only. This
packet binds no wave, makes no disposition, moves no verdict"*).

**(iv) Verdict: ALREADY-COVERED (`decoupling-constructibility-packet-
2026-08-12.md` R4b, typed as `CHK-2`) for the identification; LIVE-MODERATE for
the execution gap.** The concern is real and unrun. It is not untyped.

**(v) Proposed register item (PROPOSAL ONLY).** *"`CHK-2` (settled-horn 't Hooft
matching across the decoupling) is named in a non-binding packet and has never
been run; the only run (W224) is horn-stale and granted its dynamical
sufficiency. Either schedule it or record explicitly that the repository's
matching status rests on a retired-horn computation. Note the joint with the
Krein sector: 'the carrier is vectorlike, hence zero 't Hooft anomaly' and 'the
chirality halves are null Lagrangians' are the same fact through two
instruments (card 4), so the UV end of the ledger is on firmer footing than the
IR end. Owner: whoever owns the decoupling packet."*

**(vi) Fidelity delta vs the one-liner.** **One clean falsification, one
correct half.** "the matching across bit 2 itself is **untyped**" is FALSE —
it is typed, named R4b, called "the packet's central obstruction", and assigned
a check ID. The correct and useful half is the PHI-1/2 observation, which is
exactly right and which I verified independently (zero hits). The compression
turned "typed, named, and unrun" into "untyped" — and those license completely
different next actions: one is a scheduling decision, the other a typing task
that would duplicate existing work.

*Cross-reference:* card 9. R4b and R5 are adjacent criteria in the SAME packet,
and BOTH are unexecuted — only `CHK-1` (Lens 2) was ever run from it. That the
packet's two sharpest criteria are both unrun is itself a finding, and it
belongs to neither card alone.

---

### CARD 9 — The imposter under the same VEV

> **One-liner, verbatim:** "the third family only 'looks the same at low
> energy' if the *spin-3/2* sector decouples under the *same* transition. Bit
> 2's action on the RS corner specifically is unexamined."

**(i) Strongest reconstruction.** Three claims must hold together: the third
family is an imposter; it nevertheless looks like the other two at low energy;
and the mechanism is one VEV. If the spin-3/2 sector's mass rides that same
dial, then turning the dial to make the mirror heavy also moves the third
family — and "looks the same" is a constraint on the dial's action across ALL
sectors simultaneously, not a separate assertion.

**(ii) What the repo holds.** Three things, pulling in different directions.
*First, the referent was settled the other way.* `lab/process/layer0-fork-
registry.yaml` records fork `IMPOSTER-LABEL-AB` with horn *"B: the label
attaches to the RS-shaped spin-3/2 384"* and `settled_side: "A"` (the spin-1/2
128), confidence 0.90, settled 2026-08-03 by hostile field-specialist review.
HE-1's FENCE 1 excludes the RS 384 explicitly, and HE-1/2/3 contain zero RS
mentions. *Second, bit 2's action on the RS corner IS examined.* ST-1 §4.5(3)
computes exactly this and finds the **unique** one-insertion chirality-selective
Grassmann-live diagonal channel is `Λ^7_∓ → Λ²(ζ_±)` with *"multiplicity exactly
1"* — and the `ζ` corners are the one-form, Rarita-Schwinger-adjacent slots.
That is a sharp positive result about bit 2 on the RS corner. *Third, the
one-dial tension is real and only weakly closed.* `canon/escape-corners-
campaign-RESULTS.md` finds the luminous spin-3/2 has *"NO invariant mass
channel"*, so its mass is strictly VEV-borne on the one modulus whose decrease
is the generation mechanism — *"opposing demands on one dial"*, reconcilable
only by an unstated hierarchy, and **closed at author-assertion tier, no tier
higher**. The obligation is stated once, as R5: *"the wave must exhibit the
dial's action on all sectors simultaneously"*. It has never been executed.

**(iii) The bounded dig.** A table lookup in ST-1 plus a fork-registry read,
exactly as the brief anticipated — and the lookup reverses the one-liner's
second sentence. Two further notes. The settlement to Reading A was reached
partly *because* Reading B carried an unpayable bill (no known mechanism makes
a fundamental spin-3/2 family present as spin-1/2 at low energy), which means
the settlement **routes around** this concern rather than dissolving it; and
the source text the settlement had to argue past is exactly L131 (*"in g u,
there's one family of 16 flipped chiral spin three halves particles"*) and L128
(the RS product-rule term is *"where you get your third generation of matter
from"*). Separately, card 4's object — the generation triplet inside
gamma-traceless `V (x) S` — IS the spin-3/2 module, so GU's generations live in
the RS sector whichever way the label fork was settled.

**(iv) Verdict: SPLIT — three components, three different types.**
- *"Bit 2's action on the RS corner specifically is unexamined"* —
  **ALREADY-COVERED (ST-1 §4.5(3))**, and covered with a uniqueness result.
- *"the third family ... the spin-3/2 sector"* — **MIS-TARGETED**: the
  repository settled `IMPOSTER-LABEL-AB` to side A (spin-1/2 128) in 2026-08,
  so as written the concern targets a reading the repo does not hold.
- *"only 'looks the same at low energy' if the spin-3/2 sector decouples under
  the same transition"* — **LIVE-HIGH**. R5 is unexecuted, the one-dial
  conflict is closed only at author-assertion tier, and HE-1's actual computed
  effect (`n_g → n_g − 1`, the distinguished family REMOVED) points the
  opposite way from "looks the same".

**(v) Proposed register item (PROPOSAL ONLY).** *"R5 (the one-dial obligation:
exhibit the VEV dial's action on the spin-1/2 and spin-3/2 sectors
simultaneously) is stated once, in a non-binding packet, and unexecuted. The
upstream tension — spin-3/2 has no invariant mass channel and rides the same
modulus whose decrease is the generation mechanism — is closed at
author-assertion tier only. Note the targeting hazard for any future kill: the
imposter label is settled to the spin-1/2 128, so a kill aimed at 'the spin-3/2
third family' misses; the live obligation is the shared dial, not the label.
Owner: the decoupling packet jointly with the high-energy-two-plus-one
channel."*

**(vi) Fidelity delta vs the one-liner.** **The largest of the five.** The
one-liner bundles three things the repository types completely differently — a
settled label fork, an already-computed selectivity result, and a genuinely
unexecuted obligation — into a single sentence whose surface reading is "nobody
has looked at the RS corner." That reading is false twice and true once, and
the true part is not the part the sentence emphasises. Compressed further, this
item would have produced a mis-aimed kill of exactly the shape the repository's
own memory warns about.

---

## 4. Verdict summary

| # | Concern | Verdict | Changed by digging? |
|---|---|---|---|
| 3 | Representation geometry | **LIVE-MODERATE** (half covered by ST-1 §4.5; intra-irrep stratum new) | Yes — downgraded from apparent novelty |
| 4 | Krein compatibility | **ALREADY-COVERED** (canon result 3 + R3 fence) + **DISSOLVES** (BD-D leg) + **LIVE-MODERATE** (scope defect found) | Yes — reversed, then produced a new defect |
| 5 | Functoriality | **LIVE-HIGH** | Yes — strengthened; arrow re-typed |
| 8 | 't Hooft matching | **ALREADY-COVERED** (R4b/`CHK-2`) + **LIVE-MODERATE** (unrun) | Yes — "untyped" falsified |
| 9 | Imposter under the same VEV | **SPLIT**: ALREADY-COVERED + MIS-TARGETED + **LIVE-HIGH** | Yes — decomposed into three types |

---

## 5. Dedupe ledger — no merges, and why

The contract requires quoting both members of any candidate pair in full and
naming the surviving nuance. Four pairs were tested; all four kept both cards.

**3 vs 4.** *3:* "The direction, not just the switch, decides the spectrum."
*4:* "does the selected half sit Krein-positively in the (96,96) pairing?"
Shared root: both degeneracies are driven by the ambient metric's
indefiniteness and both vanish at `(14,0)`. **Surviving nuance:** card 3's
object is the VEV direction in `ad P` and its question is the RANK of an
induced map; card 4's object is the Krein form on the carrier `V (x) S` and its
question is a SIGNATURE. Different spaces, different invariants. Both stand,
cross-referenced.

**4 vs 8.** *4:* "does the selected half sit Krein-positively"; *8:* "the
effective half's anomalies must match the total's across the decoupling."
Shared root: "the carrier is vectorlike, hence zero 't Hooft anomaly" and "the
chirality halves are null Lagrangians" are the same underlying fact read
through two instruments. **Surviving nuance:** card 4 is a kinematic statement
about a form on a fixed carrier, decidable now and decided; card 8 is a
two-ended consistency ledger that requires an IR spectrum GU does not yet have,
and is therefore not decidable now. Both stand, cross-referenced.

**4 vs 9.** *4:* the `(96,96)` pairing; *9:* "the *spin-3/2* sector decouples
under the *same* transition." Shared root: the generation triplet lives inside
the gamma-traceless `V (x) S`, which IS the spin-3/2 module — card 4's object
is literally card 9's sector. **Surviving nuance:** kinematics versus dynamics.
Card 4 computes a form on a fixed carrier; card 9 asks what one VEV dial does
to two sectors at once, which no computation in this file touches. Both stand.

**8 vs 9.** *8:* R4b; *9:* R5. Shared root: adjacent criteria in the same
packet, both unexecuted, both non-binding. **Surviving nuance:** different
failure modes entirely — an anomaly ledger that must balance versus a mass dial
that must do two jobs. A single merged item would lose which check to run.
Both stand, with the shared observation (only `CHK-1` was ever run from that
packet) recorded in both.

---

## 6. Comparator routing — which route does this bind?

**Source-native half — this BINDS.** The parity criterion, the eight-point
sweep, the transversality angles, the `q = 0` contrast, the insertion-direction
rank, and the `ker(Gamma)` non-tensor fact are linear algebra on GU's own
declared carrier `V (x) S` at `D_7`, evaluated at both SIGNATURE-AMBIENT horns
and at controls. They are structural, not evaluative.

**Comparator half — this does NOT bind.** Card 8's matching, SMG, mod-16
cobordism and spectator vocabulary are fork-1 comparator objects. Card 4's
BD-D leg concerns an imported free linearised Yang-Mills symbol quotient which
is not GU's physical quotient. Card 9's "looks the same at low energy" is
source narrative, and the seesaw/Majorana words inherited from ST-1 are a
taxonomy of Hom spaces, never a mechanism.

**Forbidden summaries, named so they are not written.**
*"LD-B found the Krein positivity gap."* No — canon found it in July and the
answer is nullity; LD-B found a scope defect in the sentence recording it.
*"LD-B broke the ghost-parity synthesis."* No — both physical horns are
confirmed exactly; the kill is one signature wide and editorial.
*"LD-B showed GU's generations are ghosts."* No — nothing here touches the
physical/ghost assignment, which remains contingent on a dynamics GU does not
supply.
*"LD-B showed the spin-3/2 sector does not decouple."* No — it showed the check
was never run.
*"BD-D is wrong."* No — BD-D is correct on its own module; it simply does not
reach `V (x) S`.

---

## 7. Hostile review, inline

**Inflation attack on card 4 (the defect).** *"You found a typo in a canon
sentence and dressed it as a kill."* Partly conceded: the physics is
unaffected, both physical horns are confirmed, and I have typed the kill as one
signature wide and editorial in both `target_claim_verdict` and the proposed
register item. What resists the deflation is that the sentence's scope was
EXPLICIT — it enumerates three signatures and the third is false — and that the
governing criterion (parity of `q`) appears nowhere in the repository, so the
sentence was true by coincidence of the two horns rather than by a stated
reason. A fence whose hypothesis holds for an unstated reason is one horn
change away from being cited outside its domain.

**Deflation attack on card 4 (the parity fact).** *"`beta_S` is a product of
`p` gammas and `chi` a product of 14; they anticommute iff `p` is odd. One
line. You computed 1792-dimensional eigendecompositions to rediscover parity."*
Largely conceded — the proof IS one line, and I state it in §2.1. Three things
survive: nobody wrote that line; the naive version of it would wrongly predict
nullity at every even `q`, whereas the truth is the three-outcome structure
(definite at `q = 0`, `(48,48)` at `q = 2,4,6`); and the transversality
corollary is not a parity observation at all. Triviality of proof is not
triviality of consequence, but I am not claiming difficulty.

**Inflation attack on card 5.** *"Both structures landed today; you are
scoring a gap in a file whose ink is wet."* Conceded as a timing caveat, and it
cuts both ways — CT-1 could close it in its next pass. The item is proposed,
not filed, for exactly that reason. What makes it LIVE-HIGH rather than
premature is the LA-5 non-monotonicity witness, which predates CT-1 by two days
and sits unpropagated regardless of what CT-1 does next.

**Deflation attack on card 5.** *"CT-1 explicitly says movement between grant
nodes is not a functor, so the commutation question is already answered: no."*
Refused. That sentence denies functoriality of the row-movement map, which is a
different object from the question of whether LA3 commutes with discharge. If
anything it strengthens the concern: the absence of functoriality on one side
is precisely why a commutation square cannot be assumed on the other.

**Deflation attack on cards 8 and 9.** *"Both reduce to 'a packet named a check
and nobody ran it'. That is a scheduling note, not a finding."* Conceded for
card 8's live half. Not conceded for card 9, where the finding is a targeting
hazard — a future kill aimed at "the spin-3/2 third family" would miss a
settled fork — and that is a content fact about claim indexing, not scheduling.

**Weakest seam in this file.** The Krein computations are numerical, not exact
arithmetic: signatures come from `eigvalsh` at tolerance 1e-8. The seam is
bounded rather than hedged — every asserted quantity is an integer or vanishes
to ~1e-14 against a scale of ~9.8, a gap of fifteen orders of magnitude, and
the eight-point sweep produces three cleanly separated outcomes with no
borderline case. Still, this is `L2 COMPUTED` in `VERIFICATION.md`'s scale, not
`L1 PROVEN`, and the one-line parity proof in §2.1 is what would upgrade it.

**Second seam.** The 45-degree transversality is computed for the canonical
spectral choice of maximal positive subspace `P`. The `dim(P ∩ chi_±) = 0`
clause is choice-independent (a theorem), but the equiangularity is not proved
here for every admissible `P`. I have stated the two clauses separately in
§2.1 rather than letting the stronger one inherit the weaker one's generality.

---

## 8. Postflight — five lenses

**Lens A — claim-targeting auditor.** One card kills internal content (card 4,
canon result 3) and `target_claim` names it verbatim with its scope. No source
claim is targeted anywhere in the file. Card 9's central act is *declining* to
credit a mis-aimed concern, which is the same discipline applied in reverse.
No claim status moves; `rows_advanced: 0`, `rows_proposed: []`.

**Lens B — novelty auditor.** Every card ran a coverage grep before claiming
anything, and three of five came back covered. Card 3 is ~half reproduction
(ST-1 §4.5), card 4's leg A is fully covered by canon, card 8's identification
is fully covered by R4b, card 9's second sentence is fully covered by ST-1
§4.5(3). The genuinely new content is: the parity criterion and its sweep, the
`(14,0)` defect, the fence map, the transversality angles, the intra-irrep
rank stratum, the BD-D disanalogy, and the gamma-trace redundancy rider.

**Lens C — layer discipline.** Nothing in this file credits the total theory
with chirality or the package with an unconditional spectrum. The Krein results
are ambient-layer kinematics; the rank result is an availability statement
about an unselected direction; every "spectrum" word is VEV-conditional. The
physical/ghost assignment remains contingent on a dynamics GU does not supply,
exactly as canon's honest-boundary section says.

**Lens D — harness integrity.** The probe meets all seven `VERIFICATION.md`
rules: baseline verified before mutations (rule 1); every mutation corrupts
machinery or a reference, never a check predicate (rule 2); catches require a
genuine `[FAIL]` line, and the harness *rejected* one of my own mutations as
CRASH-NOT-DETECTION until I fixed it (rule 3); the absence claims carry a
planted-positive control (rule 4); selftest exits 0 on success (rule 5); the
selftest baseline is scoped independently of the live run (rule 6); and the
verification reads what the catches were, not the summary line (rule 7). Two
defects in my own instrument were found and fixed this way — a dict-construction
bug and an inert mutation whose inertness turned out to be a fact worth banking.

**Lens E — what did NOT move.** SG4 unchanged as decider; bit 2 unchanged as
selector. The `(96,96)` triplet signature, the 192-dim carrier, the
Turok-Bateman reading, the R3 fence on both physical horns, the generation
count, `n_g` rules, ST-1's dispositions, BD-D's verdict on its own module, the
`IMPOSTER-LABEL-AB` settlement, and SIGNATURE-AMBIENT are all untouched.
`canon_verdict_change: none`; `canonical_effect: pending_integration`.

---

## 9. Claim ceiling

- **Exact/computed, and load-bearing:** the eight-point parity sweep with its
  three outcomes; `{K,chi} = 0` iff `q` odd; the `(14,0)` definite halves and
  the fence value 96 there; the 45-degree principal angles and
  `dim(P ∩ chi_±) = 0` at both physical horns; the `Lambda^1` rank 64/32 split
  on the null cone; `dim ker(Gamma) = 1664` with no `v (x) S` line; the
  gamma-trace redundancy rider.
- **Reproduction, claimed by nobody here:** the 192-dim triplet, the
  `(+96,-96,0)` signature, the 96/96 half dimensions, ST-1's 68/172 (QUOTED,
  not re-derived — no `D_7` Hom dimension is recomputed in this file).
- **Archival, quoted with loci:** canon result 3 and the 2026-07-06 banner;
  ST-1 §4.3/§4.5; BD-D's bare-module theorem; CT-1's LA3/G6 and the
  never-launder law; LA-5's non-monotonicity sentence; R4b/R5 and the packet's
  binding disclaimer; `IMPOSTER-LABEL-AB`; `SC-CHI-01`, `SC-CHI-50`,
  `SC-CHI-51`, `SC-FER-03`, `SC-GEN-53`, `SC-GEN-57`.
- **NOT claimed:** any action, vacuum, scale, spectrum, reality map, generation
  count, anomaly coefficient, decoupling construction, or resolution of
  SIGNATURE-AMBIENT; that GU's generations are physical or ghosts; that any
  register row should move; that the `(14,0)` defect affects any physical
  conclusion; any claim-status movement.

```gu-typed-objects
result: the parity criterion for isotropy of the chirality halves of the self-dual generation triplet, and the (14,0) scope defect it exposes
carrier: the 192-dim self-dual SU(2)+ top-Casimir stratum of ker(Gamma) inside V (x) S at D_7 (LAYER=ambient, CHIRALITY=S-FULL-DIRAC)
pairing: Krein form K = eta_V (x) beta_S, beta_S the product of the spacelike gammas (ON=the 192-dim triplet, and on V (x) S ambiently)
real_structure: real form so(p,q) with p+q=14; the discriminator is the parity of q; horns (9,5) and (7,7) both odd, control (14,0) even
grading: Z/2 chirality grading by chi = the product of all fourteen gammas
action_owner: repository-construction
target: the chirality half chi=+1 (and its mirror), as a subspace of the triplet (MAP-TYPE=restriction)
```

```gu-typed-objects
result: the intra-irrep insertion-direction rank stratum -- a Lambda^1 VEV direction gives rank 64 generically and 32 on the null cone. NOTE the pairing slot below is NONE deliberately: what is computed is the rank of the INSERTION MAP e_w, not of any pairing. The induced mass shape's rank equals it only after composing with a charge conjugation C, which is NOT computed here and which the source does not supply (the reality map is source-silent, SN-1 UNDEFINED_WITHOUT_REALITY_MAP)
carrier: the ambient Dirac spinor bundle Delta = S_+ (+) S_- at D_7 (LAYER=ambient, CHIRALITY=S-FULL-DIRAC)
pairing: NONE
real_structure: real form so(p,q) with q >= 1; the null cone of the ambient metric is the degeneration locus and is empty at q = 0
grading: Z/2 chirality grading; e_w is odd, mapping S_+ to S_-
action_owner: source-action
target: S_- , via the Clifford insertion e_w for w in Lambda^1 (subset) ad P (MAP-TYPE=homomorphism)
```

---

## 10. Did digging change the verdicts? — blunt

**Yes, on three of five, and the compression lost fidelity in both
directions — which is the part worth reporting.**

The distillation's characteristic failure here was not softening. It was
**flattening typed states into a single "is this a gap?" axis.** Item 8's
matching is typed, named "the packet's central obstruction", and assigned a
check ID; the one-liner rendered that as "untyped", which points at a typing
task that would duplicate two days of existing work instead of at the
scheduling decision that is actually owed. Item 4's Krein question was settled
in canon in July with the strongest possible negative answer; the one-liner
rendered it as an open question, and banking it would have re-opened a closed
result. Item 9 fused a settled label fork, a computed uniqueness result, and a
genuinely unexecuted obligation into one sentence whose plain reading is false.

In the other direction, the compression under-sold item 5: the arrow is
mis-typed, but the underlying question is better than the one-liner suggests,
because a concrete non-monotonicity witness already exists in an LA-5
postflight and nobody propagated it.

The thing I did not expect: the most valuable output of the wave's best-covered
item was a **defect in the covering document**. Item 4's literal question was
answered, but answering it required recomputing the answer, and recomputing it
showed the canon sentence asserts its scope over three signatures when it holds
on two. That is an argument for digs on already-covered items, not against
them — the cheapest way to find a stale scope is to re-derive the result that
lives inside it.

**What I did not do:** I did not decide whether the physical/ghost assignment
is chirality-aligned (it is not, and that was already banked), did not run
`CHK-2` or R5, did not draw the Layer/Grant square, did not compute the
insertion moduli beyond one irrep, and did not move a single row. Four of my
five proposed register items are proposals to *schedule or narrow* existing
work, not to start new channels — which is the honest shape of a dig whose main
discovery is that the repository already knew most of this.

---
artifact_type: exploration
status: exploration
doc_type: representation-invariant-gate
created: 2026-08-14
work_item: HE-1
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "HE-1: the seed's prescribed construction executed exactly. Branching the 16 and the 144 along the Pati-Salam chain, the invariants that a family and the 144 SHARE are the SM-singlet count (1 = 1), every degree-1 trace (0 = 0), and ALL FIVE Standard-Model anomaly coefficients (0 = 0) -- the degree-3 invariant, the standard fingerprint of a family, is BLIND to the 144. What separates them at lowest cost is the degree-2 Dynkin index (2 vs 34) and, under the smallest possible subgroup, max|Q| (1 vs 2). Neither is family-indexed, so neither converts SC-GEN-53. The family-indexed invariant that DOES is the mass-channel ladder dim Inv_G(16 (x) 144) = 0 (Spin(10)) -> 2 (Pati-Salam) -> 11 (SM): the 144 contains the Pati-Salam content of exactly ONE family-shaped block, with multiplicity exactly one, and that block is a MIRROR, not a copy. Hence n_g chiral families plus one 144 leaves net chirality n_g - 1, with 128 exotic states unpartnered. The 2+1 partition is FORCED by a multiplicity, but it is UNLABELLED (nothing names which family) and its consequence is that the distinguished family is REMOVED, not made different-but-light. Seed does NOT graduate: invariant SUPPLIED, scale structurally located but numerically source-silent, threshold NOT SUPPLIED."
grade: "EXACT rational/integer arithmetic on doubled so(10) weight vectors; no floats anywhere; 62/62 checks, exit 0. Machinery (Weyl group by BFS, Racah alternating-sum multiplicities, Weyl dimension formula) is positive-controlled on five objects whose answers were known before the run and negative-controlled on 10 (x) 16. Cross-checked against FOUR independently banked repository numbers (C2 = 45/4 and 85/4; Dynkin 2 and 34; one SM singlet per 16 and per 144; 10 (x) 16 = 144 (+) 16) and against the MJ-5 charge conventions. STANDARD REPRESENTATION THEORY, not GU-native: every branching here is textbook so(10) technology. GU-NATIVE content is confined to which modules are selected and what the ladder is used to conclude. NOT: an index, a generation count, a physical-carrier statement, a real-form statement, a dynamical statement, a scale, or any claim-status movement."
disposition: SEED_DOES_NOT_GRADUATE__REPRESENTATION_INVARIANT_SUPPLIED_AS_A_PAIRING_LADDER__2PLUS1_FORCED_BY_MULTIPLICITY_BUT_UNLABELLED_AND_SUBTRACTIVE__ANOMALY_IS_BLIND__SCALE_AND_THRESHOLD_STILL_SOURCE_SILENT__RETURNS_TO_SOURCE_BUILD_WITH_A_STRICTLY_BETTER_HAND
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - explorations/lane2-sc-gen-53-tripwire-seed-2026-08-12.md
  - explorations/imposter-reading-adjudication-2026-08-03.md
  - explorations/judge-corrected-claims-addendum-2026-08-10.md
  - explorations/oq-rk1-j-restriction-on-branched-slots-2026-08-03.md
  - explorations/claim-indexed-verdict-doctrine-2026-08-12.md
  - papers/drafts/one-generation-not-three/draft.md
  - papers/drafts/no-go-class-relative-survey.md
  - lab/active-research/pati-salam-chain-verification.md
  - lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md
  - docs/paper-formalization-candidates.md
scripts:
  - tests/channel-swings/joe_directed_imposter_separation_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `SOURCE_NATIVE_ROUTE`.

# HE-1 — the smallest invariant that separates a family from the 144

## 0. What this file is, and the four fences it carries

The channel's own gate asks whether Weinstein's claim that **two families remain
identical up to mass at high energy while the third, representation-theoretic
imposter family, does not** (`SC-GEN-53`) can be converted into a representation
invariant, an observable, a scale, and a predeclared threshold. The seed
prescribes exactly one construction and forbids one shortcut:

> restrict the two true-family and imposter modules along the source-owned
> high-energy group chain, choose the smallest invariant whose equality differs
> between them, and only then ask a phenomenologist for a measurable channel.
> Failure to find such an invariant returns the seed to Source/Build; **it does
> not permit choosing an observable by fit.**

That construction is executed here, exactly. Four fences travel with every line
below.

**FENCE 1 — the object is WG-P03's sector, not "the imposter."** The referent
of the program's own word *imposter* was adjudicated
(`explorations/imposter-reading-adjudication-2026-08-03.md`) and **RESOLVED(A)**
(`papers/drafts/one-generation-not-three/draft.md` §11.3): the label attaches to
the `128 = S(V) (x) S(W)` block of the `Cl(9,5)` reconstruction. It does **not**
attach to the `144`. The `144` computed here is the object of source prediction
`WG-P03` — *"an additional spin-1/2 sector with a roughly 144-complex-dimensional
internal representation is predicted to combine with the third family after
Pati-Salam-like unification"* — and of the draft's §14.3 conditional (*"if the
imposter reunifies with its 144 partner"*). Nothing here renames the imposter.

**FENCE 2 — a fourth "128".** The gamma-traceless `144` minus its one
family-shaped block leaves **128 states**. This is numerically equal to, and
structurally unrelated to, all three members of the existing three-way `128`
homonym fence (adjudication §3: the `Cl(7,7)` Majorana module; the
`dim_R S± / dim_C S` conflation; the `Cl(9,5)` imposter block). No property may
be transported between them.

**FENCE 3 — multiplicity, not index.** Every number below is a multiplicity in a
branching, or a difference of two multiplicities. Per repository rule, **no count
here is a generation count.** The net-chirality result takes `n_g` as an *input*
and returns `n_g - 1`; it does not derive `n_g`. The repository count remains at
`{1, 3}` and is untouched.

**FENCE 4 — complex reps, one real form unaddressed.** All computation is on
complex `so(10)` modules. GU's internal group is `Spin(6,4)`; the signature/real-form
decision is a live repository fork. A real or quaternionic structure that pairs
`144` with `144bar` would change the net-chirality arithmetic. Declared as a
ceiling, not resolved.

---

## 1. Prior-art sweep, by mechanism — and how much was already owned

This is the most heavily worked area in the program. Swept by mechanism
(*generation, family, imposter, third family, chirality, Z/3, flavour, texture,
144, mediator, reunification, exotic charge*), not by label.

### 1.1 Already owned — cited, not re-claimed

| Result | Owner | Status before HE-1 |
|---|---|---|
| `10 (x) 16 = 144 (+) 16` for `so(10)` | gate AC-1, `tests/channel-swings/joe_directed_anomaly_cancellation_probe.py`; also `lab/process/hinge-panel-synthesis-2026-08-03.md` §2 | exact |
| `C2 = 45/4` on 16-type, `85/4` on 144-type | `explorations/oq-rk1-j-restriction-on-branched-slots-2026-08-03.md` | exact |
| Dynkin index `16 -> 2`, `144 -> 34` | `DERIVATION-PROGRESS.md` route-(b) congruence list | exact |
| Exactly one SM singlet per 16 and per 144 (`512/16 = 32`, `1152/144 = 8`) | `explorations/judge-corrected-claims-addendum-2026-08-10.md` | exact |
| **The 144 carries electric charges ±4/3, ±5/3, ±2 absent from any 16** | `papers/drafts/one-generation-not-three/draft.md` §14.3 | **CANDIDATE grade**, sourced to "seed prediction-candidates" (`references.md` §14.3 row) |
| "At whatever scale the joint constraint structure becomes visible, the third family must behave differently" | draft §14.2 | structural discriminator, candidate grade |
| Third-family-philic with **no** light-family counterpart | draft §14.4 | candidate grade |
| Imposter referent fork, **RESOLVED(A)**, confidence 0.90 | adjudication row + draft §11.3 | resolved (label attachment only) |
| `PH-K1-KINEMATIC` — the `Cl(9,5)` 128 block is kinematically vectorlike, `64+64`, both signatures | draft §9; `explorations/chirality-grading-and-77-rerun-2026-08-03.md` | CONFIRMED |
| Witten-1983 class burden on any chiral RS-derived family | `papers/drafts/no-go-class-relative-survey.md` §2.6 | binding gate |
| Reunification asymmetry; only the imposter has Lorentz-matched 144 partners; `(3,2) x 144` cells empty | draft §6; `explorations/oq-rk1-j-restriction-on-branched-slots-2026-08-03.md` | exact |
| Count at `{1,3}`; every analytic index route to 3 failed (GEN-01, GEN-03, FC4-HOLONOMY-01) | `DERIVATION-PROGRESS.md`, `NEXT-STEPS.md` | standing |
| Z/3 texture cuts `9 -> 3`; couplings free and ungraded; `rho = (0,2,1)` FN-STERILE | `explorations/yukawa-scoping-2026-07-13.md` H28 | exact |
| Carrier bit A(−42) vs B(−38), gamma-traceless carrier | `canon/carrier-bit-decision-campaign-RESULTS.md`, `canon/gamma-traceless-38-adjudication-RESULTS.md` | canon |
| `Hom(16,144)` appears in the dualized 126-type factor | `explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md` | exact, different question |
| A generation is an index, not an object; the 192-carrier identification is NON-DISCRIMINATING | `explorations/twentyfive-lens-what-is-a-generation-2026-08-09.md` + same-day deflation | standing |
| Source-side: ν and ζ are proposed as the *two true* generations, the third being the imposter | `docs/paper-formalization-candidates.md` candidate 6B (line 444) | source reading |

**Honest ratio: roughly two thirds of what this file touches was already owned.**
Everything in the table above is cited; nothing in it is re-claimed. Two entries
change grade rather than content: the exotic charges move CANDIDATE → exactly
certified, and the `16 x 144` mediator decomposition moves *queued* → done.

### 1.2 The explicit open item this swing closes

`papers/drafts/one-generation-not-three/draft.md` §14.3, verbatim:

> A 16×144 mediator decomposition would give this a mass-matrix meaning; **that
> computation is queued, not done.**

It is done below.

### 1.3 New, on a scrupulous sweep

Zero hits anywhere in the repository (`.md` and `.py`, excluding `_local/`) for a
Pati-Salam or Standard-Model branching of the `144`. Searched for the block
labels directly (`(4,3,2)`, `(20,2,1)`, `20bar`, `15bar`, `4bar,2,1`) and for
`144` co-occurring with *branch / decompose / Pati / Salam / su(3) / su(2) /
hypercharge / anomaly / Casimir / Dynkin / index*. The prior art carries the
Casimir, the Dynkin index, the SM-singlet count and the charge *values* — it does
not carry the branchings themselves, the mirror property, or the pairing ladder.

---

## 2. Preflight — six specialist lenses, each proposing a route

Written before the probe was run. Each lens proposes a route, not a comment.

**Lens 1 — representation theorist.** *Route:* the question "smallest invariant
that separates" is ill-posed on `16` vs `144` in isolation, because dimension
separates them trivially and uselessly. Pose it properly: order the
SM-restriction invariants by polynomial degree and find the first degree at
which they differ; separately, order by *subgroup* and find the smallest
subgroup of the SM under whose restriction they already differ. Compute both
ladders. *Prediction before running:* degree 3 (the anomaly) will **not**
separate them, because `so(10)` has no third-order Casimir and therefore every
`so(10)` module is anomaly-free under every subgroup — which makes the standard
"fingerprint of a family" useless here. That prediction is the lens's own
falsifiable stake.

**Lens 2 — Pati-Salam branching specialist.** *Route:* the source's own word is
*reunify* and its own scale is *after Pati-Salam-like unification* (`WG-P03`).
So branch at Pati-Salam first, not at the SM. The decisive question is whether
the `144` contains a block isomorphic to a `16`'s Pati-Salam content and with
what multiplicity — because that multiplicity, and nothing else, controls how
many families can pair off. *Prediction:* the `144` will contain family-shaped
content exactly once, and it will be the *conjugate*, since `10 (x) 16` sits in
the opposite `so(10)` chirality class.

**Lens 3 — flavour physicist.** *Route:* a representation invariant that is not
family-indexed cannot convert `SC-GEN-53`, because the claim is about **one
family among three**, and all three are the same representation. The only
family-indexed object available is the *pairing*: `dim Inv_G(16 (x) 144)` as a
function of `G` along the chain. Compute that ladder. If it is zero at
`Spin(10)` and nonzero at Pati-Salam, the source's scale statement is
structurally reproduced without being numerically supplied.

**Lens 4 — collider phenomenologist.** *Route:* do not pick a channel. Compute
the electric-charge multiset, the colour content and the weak-isospin content of
both modules first, and only afterwards read off which *class* of object could
carry the difference. Note in advance that the draft already names charge-5/3
top partners at candidate grade — so anything found here is a certification and a
sharpening of an owned claim, not a discovery.

**Lens 5 — source-fidelity reader.** *Route:* `SC-GEN-53` and `SC-GEN-57` must
not be conflated, and the imposter referent is `RESOLVED(A)` onto the `Cl(9,5)`
128 — so the `144` must be introduced under `WG-P03`'s own words, not as "the
imposter." Also check candidate 6B (`docs/paper-formalization-candidates.md`
line 444), where the source proposes ν and ζ as the **two true** generations.
If the ζ-sector's `144` turns out to be a mirror, candidate 6B's reading is
directly contradicted, and *that* is a claim-indexed finding worth more than the
invariant itself.

**Lens 6 — honesty auditor.** *Route:* the whole area is prior-art-shadowed
(draft §13 concedes the branching is standard KK-supergravity technology). Before
claiming anything, grep for the exact objects; state the owned/new ratio in the
artifact; and make the probe carry a **negative control** so that the
multiplicity-1 result cannot be an artifact of the decomposition machinery.

**Cheapest kill-or-switch condition, recorded before computing.** If the `144`
contains the Pati-Salam content of a `16` (not a `16bar`), or contains it with
multiplicity ≥ 2, the "exactly one family is distinguished" story dies on the
spot and the route switches to the SM-only charge separation, which is already
owned at candidate grade and would make this swing a certification exercise
with no new structure.

**One credible contrary route, recorded before computing.** The `2+1` could
instead be carried by the `Z/3` texture already banked in `yukawa-scoping` H28
(multiplicities `3:9:1 = {3^0, 3^1, 3^2}`, "the imposter alone carries the mod-3
multiplicity"), which is a *flavour-space* mechanism needing no `144` at all. If
that route is right, the pairing ladder is a true but idle fact. HE-1 does not
adjudicate between them; H28's couplings are free and ungraded and its `rho`
is provably FN-sterile, which is the reason it was not preferred here.

---

## 3. The swing — exact results

Probe: `tests/channel-swings/joe_directed_imposter_separation_probe.py`,
**62/62 exact checks, exit 0**, `_local/cas-venv/bin/python`. Doubled integer
weight vectors, `Fraction` charges, no floats. Charge conventions are those
validated in gate MJ-5 and are re-validated as positive controls before use.
In this convention the module written `16` is the CP-conjugated family (`ν_R` at
`(1,1,1,1,1)` with `B-L = -1`); every statement below is conjugation-symmetric.

### 3.1 Construction of the 144, and why it is the mirror side

`10 (x) 16` has 160 weights; every one has coordinate sum `≡ 3 (mod 4)`, whereas
every weight of the `16` has sum `≡ 1 (mod 4)`. So the whole of `10 (x) 16` lies
in the **opposite `so(10)` chirality class**, and the gamma-trace submodule is a
`16bar`, not a `16` — established from the weights, not assumed. Removing it
leaves exactly 144 states with non-negative multiplicities, Weyl-invariant under
all 1920 elements of `W(D5)`, highest weight `(3,1,1,1,1)/2`, and dimension 144
by the Weyl dimension formula computed independently.

### 3.2 Pati-Salam branching (both new)

Labels are `(dim SU(4), 2j_L+1, 2j_R+1)` with the `B-L` of the highest weight
appended, because the `SU(4)` type (`4` vs `4bar`, `20` vs `20bar`) is **not**
recoverable from the dimension. The probe distinguishes them by that tag, never
by dimension.

```
16    |_PS =  (4, 1, 2)[-1]   + (4, 2, 1)[-1/3]                    8 + 8 = 16
16bar |_PS =  (4, 2, 1)[-1]   + (4, 1, 2)[-1/3]

144   |_PS =  (4, 2, 1)[-1]   + (4, 1, 2)[-1/3]   <-- exactly 16bar's blocks,
                                                       multiplicity 1 each
            + (20, 2, 1)[-1]  + (20, 1, 2)[-5/3]
            + (4, 2, 3)[-1]   + (4, 3, 2)[-1/3]
              8 + 8 + 40 + 40 + 24 + 24 = 144
```

The two family-shaped blocks of the `144` are exactly the two blocks of the
`16bar` — same `SU(4)` type, same `(j_L, j_R)`, same `B-L` — and neither of the
`16`'s two blocks appears anywhere in the `144`.

Two multiplicity facts, both certified:

- each of the two Pati-Salam blocks of the `16bar` occurs in the `144` with
  multiplicity **exactly one**;
- **neither** Pati-Salam block of the `16` occurs in the `144` at all.

Negative control: before the gamma-trace is removed, `10 (x) 16` contains those
same mirror blocks with multiplicity **two**. The value 1 is therefore a property
of gamma-tracelessness, not of the decomposition machinery.

### 3.3 Standard-Model branching of the 144 (new) — 23 irreps

```
(1,1)_0     (1,1)_1     (1,2)_-3/2  (1,2)_-1/2 x2  (1,2)_1/2
(1,3)_0     (1,3)_1
(3,1)_-4/3  (3bar,1)_-2/3 x2  (3,1)_-1/3  (3bar,1)_1/3 x2
(3,2)_-5/6  (3,2)_1/6 x3      (3bar,2)_5/6      (3,2)_7/6
(3bar,3)_-2/3     (3bar,3)_1/3
(6,1)_-2/3  (6,1)_1/3   (6bar,2)_1/6
(8,1)_0     (8,1)_1     (8,2)_-1/2                    total 144
```

The mirror family sits inside as `(3,2)_1/6 + (3bar,1)_-2/3 + (3bar,1)_1/3 +
(1,2)_-1/2 + (1,1)_1 + (1,1)_0`, the exact conjugate of the `16`'s six irreps.

### 3.4 The separation table — what coincides and what separates

| Invariant | 16 | 144 | verdict |
|---|---|---|---|
| Standard-Model singlet count | **1** | **1** | **COINCIDE** (banked, judge addendum) |
| `Tr Y`, `Tr Q`, `Tr(B-L)` (degree 1) | 0 | 0 | **COINCIDE** |
| `[grav]^2 U(1)_Y` (degree 3) | 0 | 0 | **COINCIDE** |
| `[U(1)_Y]^3` (degree 3) | 0 | 0 | **COINCIDE** |
| `[SU(2)]^2 U(1)_Y` (degree 3) | 0 | 0 | **COINCIDE** |
| `[SU(3)]^2 U(1)_Y` (degree 3) | 0 | 0 | **COINCIDE** |
| `[SU(3)]^3` (degree 3) | 0 | 0 | **COINCIDE** |
| number of family-shaped PS blocks | 1 | 1 | **COINCIDE** |
| `SU(3)` Dynkin index (degree 2) | 2 | 34 | separate |
| `SU(2)_L` Dynkin index (degree 2) | 2 | 34 | separate |
| `so(10)` Casimir | 45/4 | 85/4 | separate (banked) |
| max weak isospin | 1/2 | 1 | separate |
| max `|Q|` | 1 | **2** | separate |
| max `|B-L|` | 1 | **5/3** | separate |
| `SU(3)` content | `{1, 3, 3bar}` | also `6, 6bar, 8` | separate |

The anomaly machinery is positive-controlled: an isolated colour triplet returns
`SU(3)^3 = -3/4 ≠ 0` and the `10` returns a nonvanishing `SU(3)^2` index trace,
so the row of zeros above is informative and not an artefact of a dead functional.

**Reading.** The degree-3 invariant — the standard fingerprint by which a
generation is recognised — is **completely blind** to the `144`. The reason is
structural: `so(10)` has no third-order Casimir, so *every* `so(10)` module is
anomaly-free under *every* subgroup. Anomaly cancellation, the one check that
usually certifies "this is a generation," can never distinguish a family from
this sector. The first invariant that does separate is one degree *lower*: the
Dynkin index, which is exactly the one-loop gauge beta-function coefficient.

**Smallest separating invariant, two honest senses:**

- **By polynomial degree:** the degree-2 Dynkin index, `2` vs `34` in both the
  `SU(3)` and the `SU(2)_L` channel (embedding index 1 on both factors, so these
  exactly reproduce the `so(10)` value).
- **By subgroup:** restriction to `U(1)_em` **alone** already separates, via
  `max |Q| = 1` vs `2`. No smaller subgroup exists. This is the operationally
  smallest, and it certifies the draft's §14.3 candidate exactly: `4/3`, `5/3`
  and `2` all occur in the `144` and none occurs in any `16`.

**Neither converts `SC-GEN-53`,** because neither is family-indexed. `SC-GEN-53`
says one family among three behaves differently; all three families are the same
module, so no invariant of a single module can express it.

### 3.5 The family-indexed invariant: the mass-channel ladder

The invariant that *is* family-indexed is the pairing:

```
dim Inv_G(16 (x) 144):    Spin(10)  0    Pati-Salam  2    Standard Model  11
dim Inv_G(16 (x) 16 ):    Spin(10)  0    Pati-Salam  0    Standard Model   1
```

Computed twice at the SM rung by independent routes — a Racah alternating sum
over the full 2304-weight tensor product, and direct conjugate pairing of SM
irreps — which agree at 11. The `16 (x) 16` row's SM entry of 1 is the `ν_R`
Majorana direction of gate MJ-5, reproduced here as a control.

Three consequences, all certified:

1. **No `Spin(10)`-invariant mass channel joins a family to the `144`.** The
   channel opens *only* when `Spin(10)` breaks to Pati-Salam — which is exactly,
   and independently, what `WG-P03` states: *"predicted to combine with the third
   family **after Pati-Salam-like unification**."* The source's scale statement is
   structurally reproduced, though not numerically supplied.
2. **Exactly two channels open at Pati-Salam**, one per family block, each
   carried by a distinct block of multiplicity one.
3. **Nine further channels open only at the Standard Model** (11 − 2), because
   Pati-Salam breaking creates SM-irrep coincidences between the family and the
   `144`'s exotic content that Pati-Salam forbids.

### 3.6 The 2+1 partition, as net chirality

For `n_g` chiral `16`s plus one `144`, computed by conjugating the weight
multiset and re-decomposing (no hand-written label algebra):

```
n_g = 1:  family blocks net  0    exotic blocks net 1 each (128 states)
n_g = 2:  family blocks net  1    exotic blocks net 1 each
n_g = 3:  family blocks net  2    exotic blocks net 1 each
n_g = 4:  family blocks net  3    exotic blocks net 1 each
```

**`n_g` chiral families plus one `144` leaves net chirality `n_g - 1`.** For
`n_g = 3` the partition is `2 + 1`, and it is forced by a multiplicity of one
with no free parameter: a second `144` would be needed to remove a second family.

Three properties of the 128-state remainder, all certified: it carries **no**
Standard-Model singlet (the `144`'s single singlet lies entirely inside the
mirror-family block); it is itself free of all five SM anomalies; its `SU(3)`
Dynkin index is `32 = 34 - 2`, additively consistent.

---

## 4. What this does and does not deliver against the channel's gate

| Gate item | Status |
|---|---|
| Representation invariant separating the imposter sector | **SUPPLIED** — the pairing ladder `0 -> 2 -> 11` with multiplicity-1 mirror containment; and, for the module alone, `max|Q|` and the degree-2 index |
| Energy scale where inequivalence begins | **STRUCTURALLY LOCATED, NUMERICALLY SOURCE-SILENT.** The channels open at Pati-Salam breaking and nowhere above it. `WG-P04`: *"No mass scale for the new matter is known; a mass prohibition is only conjectured."* No number is derived, and none may be assumed |
| Observable carrying the difference | **CLASS NAMED, CHANNEL NOT CHOSEN** (§5) |
| Threshold or sign frozen before looking at data | **NOT SUPPLIED** |

**The seed does not graduate to a prediction packet.** It returns to Source/Build
with a strictly better hand: the invariant it asked for exists and is exact, the
scale is structurally located, and two of the four missing items are now known to
be missing *for a structural reason* rather than for want of effort.

---

## 5. Observable class — stated only after the invariant, and not chosen by fit

Each entry below is read off an invariant computed *before* it, per the seed's
prohibition. None is selected because data exist there.

1. **From the degree-2 index (`2` vs `34`).** The Dynkin index is the one-loop
   gauge beta-function coefficient. The observable class is a **threshold in
   gauge-coupling running**. Honest limitation: this is *family-blind* — it
   counts total content and cannot say which family the extra states belong to.
   It is therefore an observable for the `144`'s existence, not for `SC-GEN-53`.
   It also overlaps the wave's gauge-coupling-unification route, so the two are
   not independent evidence.
2. **From `max|Q| = 2` and the colour sextets/octets.** The observable class is
   **exotic-charge and exotic-colour fermions**. Already owned at candidate grade
   (draft §14.3, charge-5/3 top partners); this file supplies the exact
   certification and adds that the exotics include colour sextets and octets and
   an `SU(2)_L` triplet, which the draft did not state.
3. **From the pairing ladder (the only family-indexed one).** Exactly one family
   direction acquires a Pati-Salam-scale Dirac partner. The observable class is
   **rank-one, single-family deviation** — one family's gauge couplings and
   mixing-matrix rows depart from the other two at `O(mixing^2)`, with no
   light-family counterpart. This is the same *shape* the draft already argued at
   §14.4; what is new is that the rank is now derived (from multiplicity 1) rather
   than asserted.

---

## 6. Inline hostile review

**Strongest overclaim available, and where it is refused.** "The `144` is the
imposter, and HE-1 has derived the `2+1`." Both halves fail. The imposter
referent is `RESOLVED(A)` onto the `Cl(9,5)` 128 (draft §11.3); the `144` is
`WG-P03`'s sector and the draft's §14.3 reunification partner, and Fence 1 holds
it there. And the partition is derived only *given* `n_g` as an input: the
result is `n_g -> n_g - 1`, which at the repository's own live value `n_g = 1`
gives `0 + 1` and **no `2+1` at all**. Classified: **type-missing** if the
`n_g` input is left implicit; the fence is what keeps it from being a
candidate-killing overclaim.

**Strongest contrary construction.** Real form. All arithmetic is on complex
`so(10)` modules. GU's internal group is `Spin(6,4)` and the signature decision
is an open repository fork; the `Z`-sector count `1152 = 8 x 144` already shows
the `144`-type appearing with multiplicity, and a real or quaternionic structure
pairing `144` with `144bar` would make the whole sector vectorlike and collapse
the net-chirality arithmetic to `n_g -> n_g`. Classified: **NOT-YET-FALSIFIED**,
with the real-form fork named as the single object that could falsify it.

**Second contrary construction (mistyping risk).** The `2+1` may be carried
entirely in flavour space by the banked `Z/3` texture (`yukawa-scoping` H28,
multiplicities `3:9:1`), needing no `144`. HE-1 does not adjudicate; it notes
that H28's couplings are free and ungraded and its `rho` is provably FN-sterile.
Classified: **route-alive**, not killed by anything here.

**A verdict this file DOES bank, claim-indexed.** Against
`docs/paper-formalization-candidates.md` candidate **6B**, which reports the
source as proposing that *"two true generations come from the ν- and ζ-sectors,
and the third generation is an imposter"*: the ζ-sector's gamma-traceless normal
content, computed here, supplies exactly **one** family-shaped Pati-Salam block
and that block is the **mirror** of ν's, never a copy — a fact forced by the
`(mod 4)` chirality-class computation of §3.1. So ν and the ζ-sector's
family-shaped block cannot be two same-chirality generations; at Pati-Salam they
are a **vectorlike pair**. Classified: **candidate 6B's "two true generations
from ν and ζ" is killed at the level of complex `so(10)` representation content**,
subject to Fence 4. This corroborates, on a genuinely different object, the
theme already established by `PH-K1-KINEMATIC` (draft §9) and the Witten-1983
class burden — it is a third independent arrival at the same conclusion, not a
new one.

**Weakest reproducibility seam.** The Racah/Weyl decomposition machinery is
bespoke to this probe and has no second implementation in the repository.
Mitigations actually in place: five positive controls whose answers were known
before the run (`Inv(16 x 16bar) = 1`, `Inv(144 x 144bar) = 1`,
`Inv(16 x 16) = 0` at `Spin(10)`, MJ-5's family reproduction, the Weyl dimension
formula agreeing with the explicit multiset); one negative control (`10 (x) 16`
gives multiplicity 2 where the `144` gives 1); one internal two-route agreement
(`Inv_SM = 11` twice); and four cross-checks to independently banked repository
numbers. That is strong for a single probe and still **single-implementation**.
A second implementation via an independent branching route (e.g. through `SU(5)`
rather than Pati-Salam) is the cheapest hardening available.

**Source-silent, recorded as such.** The energy scale; the threshold; the sign;
which family is the distinguished one; whether the `128` exotic remainder has a
partner. `WG-P04` explicitly leaves the mass scale unknown and the prohibition
conjectural.

**The structural problem this creates, stated plainly.** The 128-state remainder
is chiral, anomaly-free, and **unpartnered**. It carries charges up to `|Q| = 2`,
colour sextets and octets, and an `SU(2)_L` triplet, and it contains no SM
singlet, so no singlet VEV can lift it. Giving it mass requires a `144bar`, which
GU's declared field content does not obviously supply. Under Fence 4 this is
either a real defect of the construction or an artefact of computing in the
complex form — and which one it is, is exactly the real-form fork.

---

## 6b. Cross-route consequences (same-day sibling channels)

Two sibling Joe-directed channels ran the same day and interact with HE-1
directly. Recorded, not merged.

- **`CU-1`** (`lab/active-research/joe-directed/coupling-unification/`)
  independently confirms `T(144) = 34` by **three** routes (weight sums, a
  tensor-product index identity, and Freudenthal/Casimir), which is a fourth
  independent confirmation of the degree-2 number used in §3.4 and the strongest
  external check HE-1 has. `CU-1` also finds that the `144` sector's index is 34
  in all five channels, so **the `zeta` multiplicity and the carrier bit are
  exactly invisible to one-loop unification**. Consequence for HE-1's observable
  class 1: the gauge-running observable cannot see the `144`'s *identity*, only
  its total content — which downgrades that observable further than §5 already
  stated.
- **`CU-1` + `PV-2` leave Pati-Salam unbroken down to `M_Z`** in GU-as-declared.
  If that holds, the two Pati-Salam mass channels of §3.5 are open from the
  `Spin(10) -> PS` breaking scale all the way down, so the distinguished family's
  Dirac mass sits at the highest available scale and the family is **removed**,
  not made different-but-light. That sharpens §6's structural problem: on
  GU-as-declared, `n_g -> n_g - 1` is not a soft prediction, it is a subtraction
  at the unification scale.

---

## 7. Claim ceiling

- **Exact, and load-bearing:** the Pati-Salam and Standard-Model branchings of
  the `16` and the `144`; the multiplicity-1 mirror containment; the coincidence
  of the SM-singlet count, the degree-1 traces and all five SM anomaly
  coefficients; the separation by degree-2 index, `max|Q|`, `max|B-L|`, weak
  isospin and colour content; the pairing ladder `0 -> 2 -> 11`; the
  net-chirality map `n_g -> n_g - 1`; the 128-remainder facts.
- **Standard representation theory, claimed novel by nobody:** every branching
  technique used here. The draft's §13 novelty posture applies verbatim — if a
  referee produces these branchings in the Kaluza-Klein supergravity literature,
  nothing above changes.
- **GU-native only in the selection and the use:** which two modules are chosen
  (`WG-P03`, candidate 2B/6B), which chain they are restricted along
  (`pati-salam-chain-verification`), and what the ladder is used to conclude
  about `SC-GEN-53`.
- **NOT claimed:** an index; a generation count; that `n_g = 3`; a physical
  carrier (`Pi_RS^phys` still does not exist; seat4 §3(h) non-transport applies);
  a real-form statement; a dynamical or mass-matrix-eigenvalue statement; an
  energy scale; a threshold; that any experiment must see anything.
- **Claim-status movement:** none. `canon_verdict_change: none`. The count stays
  `{1,3}`. `SC-GEN-53` remains a typed seed and does **not** become a prediction
  packet.

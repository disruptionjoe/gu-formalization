---
artifact_type: exploration
status: exploration
doc_type: fork-scoping-determination
created: 2026-08-16
work_item: SA-1
channel: soldered_ad
title: "SA-1: the selector for `SOLDERED-AD` is ALREADY BUILT and is UPSTREAM of the action -- `P_H` is by definition the associated bundle of the chimeric FRAME bundle (`SC-GRP-02`, eq (3.32); manuscript 2A; K77 2026-08-05, 53/53), and the chimeric carrier `C = Sym^2(pi^* T^*X) (+) pi^* T^*X` is functorial in `T^*X`, so the `INERT-AD` horn AS TYPED -- `P_H` an independent principal bundle -- is REFUTED, not undecided. What is genuinely open is a DIFFERENT and narrower question that MD-1's horn text conflated with it: `so(7,7)` contains TWO distinct six-dimensional Lorentz subalgebras -- the endogenous/diagonal `so(1,3)_endo` induced by frame rotations of `X`, and the block `so(1,3)_H` named by the manuscript's own observation chain `Spin(7,7) -> Spin(1,3) x Spin(6,4)` -- they intersect in ZERO, they differ by an internal rotation `delta(X) in so(6,4)` lying inside the declared gauge group `H`, and on the SAME `k` they give 0 and 21. Which one labels observed 4D spin is an invariance property of the unbuilt action. Blocked there, and NOT built here."
grade: "EXACT throughout: `fractions.Fraction` and integer linear algebra over Q; signatures by Sylvester congruence, never by eigenvalues; F2 symmetric-function arithmetic for the Stiefel-Whitney block; `numpy` INTEGER matrices with entries asserted in {-1,0,1} and dtype asserted integral for the 128-dimensional Clifford block. No float is load-bearing anywhere; `assert_no_float` sweeps the result dict. 105/105, exit 0, via `tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py`. Certificate splits as 30 [S] exact source/manuscript/register substrings, 4 [B] characteristic-class reproductions, 12 [C] Clifford reproductions, 14 [D] endogenous-representation results, 24 [E] reproductions of MD-1/PV-2/LA-8, 17 [F] new two-subalgebra results and 4 [L] owner-probe re-runs, of which 6 are contrary controls that must PASS. FAILURE PATH EXERCISED: eight planted false facts (`inert-ad`, `block-is-endo`, `not-a-hom`, `lambda-blind`, `clifford-dup`, `w2`, `source`, `k-p-swap`) each run to exit 1, and the selftest verifies the CLEAN BASELINE exits 0 BEFORE any mutation is attempted, with a meta-control that poisons the baseline to prove the guard has power. NOT: a source action, a BRST/BV complex, a quotient, a spectrum, a decision of which Lorentz subalgebra is physical, a decision of `CARRIER-SPLIT`, `SIGNATURE-AMBIENT` or `VERTICAL-FROBENIUS-TRACE`, a ledger edit, a fork-registry edit, or any claim-status movement."
disposition: SELECTOR_IS_BUILT_AND_UPSTREAM_OF_THE_ACTION__INERT_AD_AS_TYPED_IS_REFUTED_BY_THE_MANUSCRIPTS_OWN_DEFINITION_OF_P_H_PLUS_A_BUILT_K77_CONSTRUCTION_PLUS_A_HARD_CORE_REGISTER_CLAIM__THE_FORK_IS_RE_TYPED_FROM_TWO_BUNDLES_TO_TWO_LORENTZ_SUBALGEBRAS_OF_ONE_SOLDERED_BUNDLE__so13_endo_AND_so13_H_INTERSECT_IN_ZERO_AND_DIFFER_BY_AN_INTERNAL_delta_IN_so64_INSIDE_THE_DECLARED_GAUGE_GROUP__SAME_k_GIVES_0_UNDER_endo_AND_21_UNDER_BLOCK__THE_RESIDUAL_SELECTOR_IS_AN_INVARIANCE_PROPERTY_OF_THE_UNBUILT_ACTION_AND_IS_AN_ALREADY_NAMED_OPEN_GATE_OWNED_BY_THE_K77_ACTION_LANE__NOT_BUILT_HERE__ZERO_ROWS_ADVANCE
target_claim: "INTERNAL. The object adjudicated is `MD-1`'s own declared fork horn `INERT-AD`, quoted verbatim: \"ad(P_H) is inert: P_H is an independent principal bundle and the ad index is an ordinary internal label, Lorentz-inert\" (`md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md`, `fork_declared`). No GU source claim is targeted, attacked or defended; the source register claims `SC-GRP-02` and `SC-GRP-06` are USED as evidence, not tested."
target_claim_verdict: "REFUTED_AS_TYPED, and the fork RE-TYPED. The horn's premise -- that `P_H` is an independent principal bundle -- contradicts the manuscript's definition (2A, eq (3.32): `P_H = P_Fr~(C^{7,7}) x_{rho_D} H`, register `SC-GRP-02`, `core: hard-core`) and a built repository construction (`k77-global-chimeric-spin-reduction-...-2026-08-05`, 53/53 plus an independent Sage certificate, `source_return: SOURCE-CORRECTS`), which names the independent-bundle reading \"the correct negative control, but ... not the source-defined GU object\". The horn's CONSEQUENCE -- that the ad index carries a Lorentz-inert internal label -- survives, but only as a statement about a DIFFERENT subalgebra (`so(1,3)_H`) of the SAME soldered bundle, and choosing between the two subalgebras requires the action. MD-1's ad-leg verdict `NOT-DETERMINED` was correct at the time and remains correct for the re-typed question."
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
rows_touched: [AC-D1, AC-D2, AC-D3, AC-D4, AC-D5]
rows_advanced: 0
grants_retyped: []
fork_assumed:
  - CARRIER-SPLIT
  - SECTION-VS-OBSERVERSE
  - VERTICAL-FROBENIUS-TRACE
fork_decided_partially:
  - id: SOLDERED-AD
    layer_decided: "ambient/bundle layer -- `P_H` is soldered; `INERT-AD` as typed is refuted"
    layer_open: "observed layer -- which of `so(1,3)_endo`, `so(1,3)_H` labels 4D spin"
    blocked_on: "invariance of the selected GU action under the block subgroup, equivalently whether the action owns `D_varpi chi_epsilon = 0` / `P_epsilon u = u` (already-named open gate, `selected-k77-moving-parent-bundle-observation-reduction-2026-08-10.md`)"
depends_on:
  - lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
  - lab/active-research/joe-directed/ledger-advancement/la8-rae2-is-refuted-at-the-settled-form-leg-and-the-open-fork-is-not-load-bearing-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md
  - lab/active-research/joe-directed/phi-reduction/phi1-the-reduction-is-rank-one-and-the-14d-kernel-contributes-zero-bits-2026-08-15.md
  - lab/active-research/joe-directed/phi-reduction/phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md
  - lab/active-research/joe-directed/archaeology/ar2-deferral-archaeology-2026-08-15.md
  - explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md
  - explorations/conditional-build/selected-k77-full-reduction-quotient-reconciliation-2026-08-07.md
  - explorations/conditional-build/selected-k77-moving-parent-bundle-observation-reduction-2026-08-10.md
  - lab/sources/k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md
  - lab/sources/source-claim-register.yaml
  - lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md
  - lab/sources/transcripts/toe-weinstein-gu-40-years.md
  - docs/paper-formalization-candidates.md
  - lab/process/path-dependencies.md
  - lab/methods/source-native-comparator-routing.md
scripts:
  - tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: **`SOURCE_NATIVE_ROUTE`.**
>
> Every computation below runs on source-native objects only: the chimeric
> bundle `C`, the principal bundle `P_H`, the observation section, and the
> Lorentz representation induced by `Y = Met(X)`. The single place this artifact
> **borders** a comparator is §7, which states what the anomaly-axis rows
> `AC-D1..D5` inherit; those rows live inside `PHI-2`'s conventional 4D
> perturbative-anomaly arena and §7 changes nothing in it. No comparator result
> is used as evidence for or against any source-native object anywhere in this
> file.
>
> **REQUIRED INTEGRATION WRITE, not performed here.** This artifact was produced
> under a write scope limited to its own two paths, on a checkout shared with a
> concurrent agent and a scheduled lane, so it does **not** edit
> `lab/process/source-native-comparator-routing-registry.json`. That registry
> needs one entry, and `process_gates/source_native_comparator_routing_audit.py`
> is red until it is added. The entry is exactly:
>
> ```json
> { "path": "lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md",
>   "classification": "SOURCE_NATIVE_ROUTE" }
> ```
>
> Adding it moves the audit from `121 derived / 111 registered / 10 unclassified`
> to `121 / 112 / 9` and the gate goes green **at the existing baseline of 9**.
> `UNCLASSIFIED_BASELINE` must **not** be raised; the gate's own comment says it
> may only ratchet down.
>
> **Gate delta, measured rather than asserted.** The full `process_gates/` suite
> was run twice — once with these two files present and once with them moved
> aside — and the failing sets were diffed. Exactly two gates change:
> `source_native_comparator_routing_audit` (the registry line above) and
> `protected_surface_diff_audit`, which is by construction red for any
> uncommitted write under `lab/active-research/` and resolves on review/commit.
> Nothing else moves in either direction. The suite's remaining red gates are a
> pre-existing condition of this checkout and are untouched by SA-1.

# SA-1 — the selector is built, it is upstream of the action, and it re-types the fork

**Blunt statement first, before any lens.** The question I was asked is whether
the selector for `SOLDERED-AD` is available from objects the repository has
already built, or requires the unbuilt GU action. **It is available, it was
built on 2026-08-05, and the answer it gives is `SOLDERED`.** `MD-1` named the
exact gate that would settle it — *"a source reinspection plus a read of
`docs/paper-formalization-candidates.md` 2A against the manuscript's definition
of `H` would settle it, and it is cheap"* — and that gate had already been
passed nine days before `MD-1` was written. Nobody composed the two.

**And the fork is not what its name says it is.** Once `P_H` is soldered, both
of `MD-1`'s "horns" still have a live representative — but they are no longer
two *bundles*. They are two distinct six-dimensional Lorentz subalgebras of the
one soldered `so(7,7)`, and choosing between them is an invariance property of
the **unbuilt action**. That is where this artifact stops. It does not build the
action, and it must not.

---

## 0. PREFLIGHT — retrieval before work, then six specialist lenses

**Retrieval ran first, and it is what produced the result.** Before computing
anything I searched for the exact objects and numbers I expected to produce:
`SOLDERED-AD` (65 hits, 13 files), `P_H` (repo-wide), `solder`, `j_s`,
`chimeric`, `U(64,64)`, `Spin(7,7) -> Spin(1,3) x Spin(6,4)`, `so(3,1)_endo`,
`endogenous Lorentz`, `two Lorentz`, `internal symmetry`. Three of those
searches returned prior art that **decides the question**, and one returned a
dated trap logged against exactly the horn under test. Reproducing that prior
art rather than re-deriving it is the whole of §2 and §3.

### Lens 1 — bundle geometer

Route: forget representation theory; ask what `P_H` *is*, as a bundle. If it is
an associated bundle of `Fr(C)`, and `C` is functorial in `T^*X`, then a frame
rotation on `X` acts on `ad(P_H)` and there is nothing left to decide at the
bundle layer. **This is the route taken.** *Cheapest kill-or-switch:* if the
manuscript or the source defines `P_H` by a structure group chosen independently
of `Fr(C)`, the soldered horn dies in one line. *Contrary route:* a bundle can be
*associated to* a frame bundle and still carry a strictly larger gauge group, in
which case the frame action is compensable — this contrary is real and it
becomes §5.

### Lens 2 — source-fidelity reader

Route: read the register and the primary transcripts for the definition of `H`,
and refuse to supply one. Found, and all three are positive statements, not
absences: `SC-GRP-02` (`core: hard-core`) prints the definition
`P_H = P_Fr~(C^{7,7}) x_{rho_D} H`; `SC-GRP-06` (`core: hard-core`) records the
assertion *"GU is asserted to have no internal symmetry groups"*, verbatim from
draft-2021 p.64 and restated p.34; Portal `01:33:22` says the gauge group is
built on *"not spinors valued in an auxiliary structure, but **intrinsic
spinors**"*. *Cheapest kill-or-switch:* a source statement declaring the
structure group of `P_H` independent of `Fr(C)` would settle it the other way.
*Contrary route:* Portal `02:41:48` says observation generates *"the sort of
illusion of internal quantum numbers"* — which is not a contrary at all once
read as a **second layer**, and §4 shows why.

### Lens 3 — representation theorist

Route: `MD-1`'s D3 is a theorem about the endogenous action. Ask whether it is a
theorem about *the* Lorentz action, or about *an* embedding. `so(7,7)` is
51-dimensional in its `so(1,3) (+) so(6,4)` block subalgebra and there is more
than one `so(1,3)` inside it. **This is the decisive route and it is where the
new content is.** *Cheapest kill-or-switch:* if the two candidate subalgebras
coincide, or if one fails to sit inside `so(7,7)`, the re-typing collapses.
*Contrary route:* only the diagonal is induced by frame rotations of `X`, so the
block factor might not be a physically available labelling at all — that is
exactly the residual question, and it needs the action.

### Lens 4 — archaeologist / process auditor

Route: `AGENTS.md` requires checking `lab/process/path-dependencies.md` before
assuming a fork horn. Run that check. Found: chain `PD-STRUCTURE-TRANSPORT`
carries a **dated trap of 2026-08-14** — the same day `MD-1` declared the fork —
reading *"A full U(64,64) frame/connection group was treated as if it supplied an
arbitrary U(64,64) bundle … The source object is instead the unitary frame
bundle of the Spin-induced spinor bundle."* That is the `INERT-AD` premise, logged
as a known mistake. *Cheapest kill-or-switch:* none needed; the trap is a
process fact, and I report it as archaeology, not as physics evidence.

### Lens 5 — honesty auditor

Route: pre-register the failure modes. Three were pre-registered before any
computation. **(a) Manufacturing a decision.** The brief warns that "blocked on
the action" is the more likely and a first-class outcome. The guard is that the
decision I reach is at the *bundle* layer only, and I must report the residue as
blocked with the same emphasis. **(b) Homonym.** `MD-1` writes `ad(P_H)` for
`Lambda^2` of the 14-dimensional carrier; the source's `ad(P_H)` is
`u(64,64)`, of dimension 16384. Treating those as one object without typing them
is exactly the failure `GEOMETER-VS-PHYSICS-OBJECTS.md` exists to prevent; §2.3
types them. **(c) False novelty.** This repository has produced eight false
novelty claims. Everything decisive in §2 and §3 is prior art; §1 attributes each
piece to its owner, and my own contribution is confined to §4.

### Lens 6 — variational geometer / action lane liaison

Route: identify precisely which sub-question terminates in the action, so that
the scheduled lane grinding that object is not duplicated. Found: the object is
already named and owned. `selected-k77-moving-parent-bundle-observation-reduction-2026-08-10`
states *"A genuine reduced connection still requires a compatibility law such as
`D_varpi chi_epsilon = 0`, or an action/BV mechanism that enforces it"* and makes
that its own next decisive gate. **That is the residual selector, and this
artifact does not touch it.**

---

## 1. PRIOR ART — every decisive input is somebody else's, and is named

| prior result | owner | relation to SA-1 |
|---|---|---|
| `SOLDERED-AD` vs `INERT-AD` declared; ad-leg verdict `NOT-DETERMINED`; the **exact** settling gate named ("a read of 2A against the manuscript's definition of `H` … it is cheap") | **`MD-1`**, 67/67 | SA-1 executes `MD-1`'s own named gate. `MD-1` gets the naming credit for the fork, for the endogenous embedding `so(3,1) -> so(6,4)`, for D3, and for stating the gate correctly |
| `P_H = P_Fr~(C^{7,7}) x_{rho_D} H`, eq (3.32), p.24; *"purely Topological as no metric has been chosen"* | **`SC-GRP-02`**, `core: hard-core`, draft-2021 | the manuscript's definition. Not re-derived; quoted and used |
| *"GU is asserted to have no internal symmetry groups"*, p.64, restated p.34 | **`SC-GRP-06`**, `core: hard-core` | the source-level statement most directly inconsistent with `INERT-AD` |
| `C = Sym^2(pi^*T^*X) (+) pi^*T^*X`; `w1(C)=0`, `w2(C)=pi^*w2(TX)`; the induced global lift `r~_C: Spin_0(1,3) -> Spin_0(7,7)`; `P_H = P_Spin(C) x_rho U(64,64)`; `gamma_0: C -> ad(P_H)`; and the explicit sentence that the independent-bundle reading is *"the correct negative control, but … not the source-defined GU object"* | **`k77-global-chimeric-spin-reduction-…-2026-08-05`**, 53/53 + independent Sage, `source_return: SOURCE-CORRECTS` | **the selector.** Built nine days before `MD-1`. Re-run clean here (L02/L04) and its numbers independently reproduced (blocks B and C) |
| *"`P_H` is the chimeric-spinor frame extension, not an independent gauge bundle"* | **`selected-k77-full-reduction-quotient-reconciliation-2026-08-07`** | the same finding, restated at the reduction-quotient locus |
| observation pullback *"retains its structure group unless a reduction section is also constructed"*; *"ordinary observation pullback does not select the action parent"*; the residual gate `D_varpi chi_epsilon = 0` / an action-BV mechanism | **`selected-k77-moving-parent-bundle-observation-reduction-2026-08-10`** | proves that candidate selector #1 (pullback) does **not** select, and names the residual selector that SA-1 hands back |
| both horns of the fork computed to numbers: sector `45` (inert) and exactly `1` (soldered); both carry **zero** doublets; `dim Inv(Sym^2)=1`, `dim Inv(traceless 9)=0`, `dim Inv(Lambda^2 V)=0`; control "with an inert ad leg the same routine returns 45" | **`LA-8`**, 78/78 | SA-1 shows LA-8's two horn-numbers are exactly the two subalgebras of §4. LA-8's own scope conclusion is untouched — see §7.2 |
| `dim k = 21`, `dim p = 24`, Killing negative on `k` and positive on `p`, the twelve inside `k` | **`PV-2`** | reproduced here (E04–E06) |
| the fork raised to verdict-load-bearing for `AC-D1..D5`, and its own limiter *"it loses `ker M`, and with it the question"* | **`PHI-2`**, 121/121 | §7 states what those rows inherit and moves none of them |
| the fork ranked the most-flagged open object, seven surfaces; the routing/promotion sequencing; the hazard check that it is source-native and not a KK revival | **`AR-2`** | SA-1 is the re-rank AR-2 asked for, executed |
| `(9,5) = (6+3, 4+1)` and `(7,7)` *"differ only in whether the horizontal Lorentz block is counted `(1,3)` or `(3,1)` — a sign"* | `AUDIT-noncompact-compact-reduction-EXTERNAL.md:117` | reproduced at F01/F02; not re-claimed |
| the manuscript's observation chain `Spin(7,7) -> Spin(1,3) x Spin(6,4)` | `docs/paper-formalization-candidates.md` 6D; `papers/drafts/no-go-class-relative-survey.md` | the source of the **block** subalgebra in §4. Not re-derived |

**What is new in SA-1, and only this:** (i) the *composition* — nobody had put
the K77 bundle construction beside the `SOLDERED-AD` fork; (ii) the observation
that `so(1,3)_endo` and `so(1,3)_H` are two **different** subalgebras of the same
`so(7,7)`, intersecting in zero, related as a graph over an internal
homomorphism `delta`; (iii) the pair of numbers `0` and `21` on the same `k`;
(iv) the resulting re-typing of the fork and the identification of the residual
selector as an action-invariance property.

---

## 2. WHAT THE FORK IS, IN TYPED TERMS

`MD-1`'s two horns, quoted verbatim from its `fork_declared` block:

> **soldered** — *"`ad(P_H)` is soldered: the chimeric carrier is built
> functorially from TX, so the physical local Lorentz group is canonically a
> subgroup of the gauge group and the ad index is NOT Lorentz-inert"*
>
> **inert** — *"`ad(P_H)` is inert: `P_H` is an independent principal bundle and
> the ad index is an ordinary internal label, Lorentz-inert"*

### 2.1 The typed content of each horn

Write `pi: Y -> X` for `Y = Met_{1,3}(X)`, `E = pi^* TX`, and

```text
C  =  Sym^2(E^*)  (+)  E^*                         rank 10 + 4 = 14
```

the chimeric bundle. Let `Fr(C) -> Y` be its (7,7)-orthonormal frame bundle and
`Fr~(C)` the double cover.

**SOLDERED, typed.** There exists a canonical bundle map
`Q~ -> Fr~(C) -> P_H` covering a nontrivial Lie group homomorphism
`Spin_0(1,3) -> Spin_0(7,7) -> H`, where `Q~ -> Y` is the pulled-back spin frame
bundle of `X`. Equivalently: `ad(P_H)` is an **associated bundle of the frame
bundle of `X`**, so a local Lorentz transformation on `X` acts on the `ad` index
by a representation whose differential is nonzero.

**INERT, typed.** `P_H` is a principal `H`-bundle over `Y` whose structure group
is chosen independently of `Fr(C)`; `ad(P_H)` carries the **trivial**
`Spin_0(1,3)` representation; Lorentz and gauge indices are independent labels.

The horns differ in exactly one testable place: **is the differential of the
Lorentz action on the `ad` index zero or not.**

### 2.2 The answer, from the definition

The manuscript defines `P_H` by (2A, §3.6, p.24, eq (3.32); register `SC-GRP-02`,
`core: hard-core`):

```text
P_H  =  P_Fr~(C^{7,7})  x_{rho_D}  H ,        H = U(64,64)
```

described in `docs/paper-formalization-candidates.md` 2A as *"an associated
bundle construction: start with the frame bundle of the chimeric bundle …, push
it forward via the Dirac representation to get a principal H-bundle."*

`C` is functorial in `T^*X`: a frame change `A` on `TX` acts by
`r_C(A) = Sym^2(A^{-T}) (+) A^{-T}`. Certified exactly (probe D08–D14): `r_C` is
a **group homomorphism** on exact rational Lorentz elements (the `(5/4, 3/4)`
boost and the `(3/5, 4/5)` rotation), it is an **isometry** of the chimeric
metric, and it is **faithful** (its `Sym^2` leg alone has kernel `{+-1}`; the
horizontal leg removes even that). At the Lie-algebra level `d rho_{Sym^2}` has
**rank 6** — not zero (D07).

Therefore the INERT horn's defining property fails, and its premise contradicts
the definition. `INERT-AD` **as typed** is refuted.

The same conclusion is reached independently, and earlier, by construction:
`k77-global-chimeric-spin-reduction-…-2026-08-05` builds
`r~_C: Spin_0(1,3) -> Spin_0(7,7)` (its eq (6)–(8)), `P_H = P_Spin(C) x_rho
U(64,64)` (eq (12)) and `gamma_0: C -> ad(P_H)` (eq (13)), and then writes, in
terms:

> *"If `(P_H)` had instead been an independent `(U(64,64))` bundle, (13) would
> require an additional isomorphism or reduction section. That is the correct
> negative control, but it is not the source-defined GU object."*

Its source return is `SOURCE-CORRECTS`, grounded on Portal `01:12:17`
(`C` = vertical 10 plus pulled-back horizontal 4), Portal `01:21:48` (*"we can
define Dirac spinors on the chimeric bundle"*), Portal `01:33:22` (*"not spinors
valued in an auxiliary structure, but intrinsic spinors"*), Portal `02:22:27`
and TOE `02:41:57`. All eleven of those substrings are checked exactly in the
probe (S05–S11, S14–S17).

### 2.3 The homonym, typed — and why it does not weaken the result

`GEOMETER-VS-PHYSICS-OBJECTS.md` rule applies and is discharged here rather than
defaulted:

| symbol | `MD-1`'s object | the source's object |
|---|---|---|
| `ad(P_H)` | `Lambda^2` of the 14-dim chimeric carrier, i.e. `so(7,7)`/`so(9,5)`, dim 91; the fork lives in its internal block `so(6,4)`, dim 45 | `u(64,64)`, dim 16384 |

They are **not** the same object. But the second contains the first: block C of
the probe reproduces `Cl(7,7) = M_128(R)` from fourteen explicit integer gamma
matrices (105 anticommutators, all squares, entries asserted in `{-1,0,1}`),
constructs the invariant form `B` with `B^2 = 1`, `tr B = 0` and
`sig B = (64,64)` by exact rank over `Q`, and certifies that **grade one and
grade two are both `B`-skew**, i.e.

```text
Lambda^2 C  =  spin(7,7)  (subset)  so(64,64)  (subset)  u(64,64)  =  ad(P_H)
```

So `MD-1`'s ad object is a Clifford-graded subbundle of the source's. Whatever
is functorial in `T^*X` for the ambient is functorial for the subbundle. The
homonym is real and it costs nothing here; it would have cost something in the
other direction, and that is why it is typed.

---

## 3. THE CANDIDATE-SELECTOR TABLE

Every candidate the brief names, plus the two the retrieval turned up.

| # | candidate selector | built? | verdict |
|---|---|---|---|
| 1 | **Observation pullback** `s^*` and the contraction identity `(s^*omega)_mu = omega_mu + omega_(ab) d_mu g_ab`, surjective onto `T*X`, a CONTRACTION not a projection | BUILT (`MD-1` E1–E3, reproduced by `PHI-1` §2.2) | **COMPATIBLE WITH BOTH.** `s^*` acts on the **form** index; it is blind to the `ad` index. Proved directly by the owner: *"Pulling back `P_H` retains its structure group unless a reduction section is also constructed"*, and *"ordinary observation pullback does not select the action parent"* (`selected-k77-moving-parent-…-2026-08-10`, S19). Pullback is not a selector |
| 2 | **The manuscript's definition of `P_H`** — 2A / `SC-GRP-02`, eq (3.32) | BUILT + source `hard-core` | **DETERMINES: SOLDERED.** `P_H` is an associated bundle of `Fr~(C)`. The INERT premise is incompatible with the definition |
| 3 | **Soldering/frame data** — the K77 induced global `Spin` lift `r~_C`, `P_H = P_Spin(C) x_rho U(64,64)`, `gamma_0: C -> ad(P_H)` | BUILT 2026-08-05, 53/53 + independent Sage, `SOURCE-CORRECTS` | **DETERMINES: SOLDERED**, and names the inert reading *"the correct negative control … not the source-defined GU object"* |
| 4 | **The tautological structure** — `Y = Met(X)`, vertical fibre `Sym^2(T^*X)`, endogenous by construction | BUILT (canon) | **DETERMINES SOLDEREDNESS OF `T^*Y` ONLY — necessary, not sufficient.** `LA-8` §3.2 is explicit and correct: *"This is fork-free. The Lorentz action on the vertical fibre is functoriality of `Met` … `SOLDERED-AD` asks whether `ad(P_H)` is soldered; it does not ask whether `T^*Y` is."* It reaches the ad leg only when composed with #2/#3 |
| 5 | **The already-built bundle map** `j_s(B_s)` in `gu-minimal-action-spec-2026-06-24` | BUILT, but as an action-spec slot ("when needed", with a normalization convention) | **COMPATIBLE WITH BOTH, AND SUBSUMED.** `j_s` presupposes a soldering rather than establishing one. `gamma_0` (#3) is the canonical version of the same map and is what `MD-1`'s next-gate question was actually about |
| 6 | **Representation-theoretic forcing** — `MD-1` D3: no nonzero Lorentz-invariant subspace of `k` | BUILT, reproduced here (E09) | **DOES NOT SELECT — it is a CONSEQUENCE of one horn, not a selector for it.** Using it as a selector is a reductio: by `MD-1` §4 it damages the SM's twelve identically. It is evidence about what a horn costs, never about which horn holds |
| 7 | **The source's own statements** — `SC-GRP-06` *"no internal symmetry groups"* (`hard-core`); Portal `01:33:22` *"not spinors valued in an auxiliary structure, but intrinsic spinors"*; Portal `02:41:48` *"generating the sort of illusion of internal quantum numbers"* | source, `hard-core` | **DETERMINES: SOLDERED at the ambient layer, and declares the inert presentation to be an OBSERVED-LAYER ILLUSION.** Two layers, not two horns — see §4.3 |
| 8 | **Which `so(1,3) (subset) so(7,7)` labels observed 4D spin** — endogenous/diagonal, or the block factor of the manuscript's own chain `Spin(7,7) -> Spin(1,3) x Spin(6,4)` | **UNBUILT** | **THE RESIDUE. REQUIRES THE ACTION.** The two subalgebras differ by `delta(X) in so(6,4)`, an element of the *declared* gauge group `H = Gamma^inf(P_H x_Ad H)`; whether that compensation is a symmetry is an invariance property of the selected action. Already a named open gate owned by the K77/action lane. **Not built here** |
| 9 | **`PHI-2`'s gauge-blindness denial** | BUILT, as a live control (121/121) | **DOES NOT SELECT.** `PHI-2` states its own limiter: *"a reduction that denies it does not get a different `phi_ext`; it loses `ker M`, and with it the question."* It raises the stakes of the fork; it cannot choose a horn |

**Reading of the table.** Three independent selectors (#2, #3, #7) agree, and
all three are upstream of the action. Two candidates (#1, #5) are compatible with
both. One (#4) is necessary but insufficient. One (#6) is a consequence
masquerading as a selector, and one (#9) is explicitly self-limiting. Exactly one
(#8) is unbuilt, and it is not the fork as named — it is what the fork becomes
once #2/#3/#7 are applied.

---

## 4. THE RE-TYPING — one soldered bundle, two Lorentz subalgebras

### 4.1 The construction

Work in the vertical fibre `V = Sym^2(T^*_x X)` with the trace-reversed DeWitt
form (inertia `(6,4)`, reproduced at E01) and the horizontal `H^* = T^*_x X`.
Two homomorphisms `so(1,3) -> so(7,7)`:

```text
rho_endo(X)  =  ( rho_{Sym^2}(X) ,  rho_{cot}(X) )        the ENDOGENOUS/diagonal
rho_block(X) =  (       0        ,  rho_{cot}(X) )        the manuscript's BLOCK factor
```

`rho_endo` is the one induced by a frame rotation of `X` — a metric `g_ab` is a
tensor on `X`, so it rotates. `rho_block` is the `Spin(1,3)` factor of the
manuscript's observation chain `Spin(7,7) -> Spin(1,3) x Spin(6,4)`, which acts
on the horizontal block and commutes with the internal `so(6,4)`.

Exactly, all checks in block F of the probe:

```text
both lie inside so(7,7)  (horizontal (1,3))                              [F01,F03]
both lie inside so(9,5)  (horizontal (3,1))                              [F02,F04]
   => the statement is independent of CARRIER-SPLIT and SIGNATURE-AMBIENT
dim so(1,3)_endo = 6 ,  dim so(1,3)_H = 6                                [F05,F06]
dim ( so(1,3)_endo + so(1,3)_H ) = 12   => they INTERSECT IN ZERO        [F07]

delta(X) := rho_endo(X) - rho_block(X)  is supported ENTIRELY in so(6,4) [F08]
delta is an injective Lie-algebra homomorphism so(1,3) -> so(6,4)        [F09,F10]
   => so(1,3)_endo is the GRAPH of delta over so(1,3)_H
delta's k-projection has rank 3 and its p-projection has rank 3          [F11]
   => the compensating internal rotation is NOT compact
```

And the pair of numbers that is the whole re-typing, on the **same** `k`, in the
**same** bundle:

```text
largest invariant subspace of k under so(1,3)_endo   =   0               [E09]
largest invariant subspace of k under so(1,3)_H      =  21               [F12,F13]
```

`0` is `MD-1`'s D3, reproduced. `21` is what the block reading gives, and it says
the `12 + 9` split **is** a covariant labelling there.

The `lambda`-independence is swept exactly: `rho_{Sym^2}` preserves the DeWitt
form `G_lambda` for every `lambda` in a seven-point exact rational sweep,
including the raw Frobenius `lambda = 0` (inertia `(7,3)`) and the trace-reversed
`lambda = 1/2` (inertia `(6,4)`) (D02–D04). So the soldering is also independent
of `VERTICAL-FROBENIUS-TRACE`.

### 4.2 What this changes about the fork

| | `MD-1`'s framing | SA-1's typing |
|---|---|---|
| the object in dispute | two candidate **bundles** for `P_H` | one **decided** bundle, two **subalgebras** of its structure algebra |
| what "inert" means | `ad` carries the trivial Lorentz rep because `P_H` is independent | `ad` carries the trivial `so(1,3)_H` action because the block factor commutes with `so(6,4)` |
| relation of the horns | mutually exclusive alternatives | related by `delta`, an element of the **declared gauge group** |
| what would select | a fact about bundle ownership | a fact about **action invariance** |
| status of the `12 + 9` labels | ill-typed on one horn | ill-typed under `so(1,3)_endo`, well-typed under `so(1,3)_H` |

`LA-8`'s two banked horn-numbers fall out of exactly this: its `45` is the block
reading of the ad leg (`1 x 45`) and its `1` is the endogenous reading, and its
control D7c — *"with an inert ad leg the same routine returns 45"* — is literally
the block computation. Reproduced at E22 and cross-checked at F15.

### 4.3 The source declares both, at different layers

This is the reading the source itself supports, and it is the same
two-layer pattern the corrected 2026-08-15 source facts already record elsewhere
(the total arena is non-chiral **and** an effective generation is a Weyl
pullback — different layers, not competing quotations).

- **Ambient layer.** *"There is no internal symmetry"* (draft-2021 p.34);
  *"no internal symmetry groups"* (p.64, `SC-GRP-06`, `hard-core`); the gauge
  group is built on *"intrinsic spinors"*, not on *"spinors valued in an
  auxiliary structure"* (Portal `01:33:22`). Soldered.
- **Observed layer.** The metric *"acts as the observer pulling back the full
  content of `Y` onto `X`, to be interpreted as if it came from `X` all along,
  **generating the sort of illusion of internal quantum numbers**"*
  (Portal `02:41:48`). Internal-looking labels are declared to be a product of
  the pullback.

So the source's position is: soldered underneath, internal-presenting after
observation. It does **not** say whether the internal presentation is *exact* —
i.e. whether `so(1,3)_H` is an honest symmetry of the observed theory or only an
approximate bookkeeping. That is #8, and the source is silent there.

---

## 5. WHERE THE SELECTOR RUNS OUT — the exact blocked object

`MD-1` already named the strongest contrary and did not defeat it:

> *"`P_H` is a principal bundle over `Y`, where 'the physical 4D Lorentz group'
> is not defined at all … observation is a gauge-fixing, so the failure of
> Lorentz-covariance of the `12+9` labels is a gauge artifact rather than a
> physical statement. This is a real defence and MD-1 does not defeat it."*

SA-1 does not defeat it either. It **types** it. The defence is now exactly the
statement that `so(1,3)_H`, not `so(1,3)_endo`, labels observed 4D spin — and
`delta` makes that a well-posed question with a named answer-object, because
`delta(so(1,3)) (subset) so(6,4) (subset) ad(P_H)` and the declared gauge group
is `H = Gamma^inf(P_H x_Ad H)` (manuscript 2C, `SC-GRP-05`), which contains it.

**The blocked condition, stated exactly.**

> Is the selected GU action invariant under the block subgroup
> `Spin(1,3)_H (subset) H` acting independently of frame rotations of `X` —
> equivalently, does the action own the reduction, in the form
> `D_varpi chi_epsilon = 0` and/or `P_epsilon u = u`, so that the
> `Spin(7,7) -> Spin(1,3) x Spin(6,4)` observation reduction is preserved by the
> dynamics rather than merely available kinematically?

- If **yes**: `so(1,3)_H` is the physical labelling, the `12 + 9` split is
  covariant, and `PV-1 / PV-2 / CU-1 / MV-1 / MV-2` stand exactly as written,
  with `MV-1`'s named assumption discharged by an action theorem rather than by a
  bundle theorem.
- If **no**: the only Lorentz action available is `so(1,3)_endo`, `MD-1`'s D3
  bites, and the whole 4D particle-label layer needs retyping — starting with the
  SM's twelve, not the nine.

**This object is already owned and is already being ground.**
`selected-k77-moving-parent-bundle-observation-reduction-2026-08-10` names it as
its own next decisive gate: *"A genuine reduced connection still requires a
compatibility law such as `D_varpi chi_epsilon = 0`, or an action/BV mechanism
that enforces it,"* and *"The next decisive gate is to derive whether the
selected source action owns `P_epsilon u=u` and/or `D_varpi chi_epsilon=0`."*
**SA-1 does not attempt it, does not sketch it, and does not price it.**
Duplicating a scheduled lane's object is waste, and the brief says so.

---

## 6. INLINE HOSTILE REVIEW

**Strongest overclaim available, and refused.** *"The `SOLDERED-AD` fork is
decided; the ad index is soldered; `MD-1`'s D3 applies; GU cannot type its own
Standard Model."* Refused on three counts. (i) D3 is a theorem about
`so(1,3)_endo`, and `so(1,3)_H` exists in the same algebra and gives 21 — F13 is
the refutation of that inference, computed rather than argued. (ii) Solderedness
is a statement about the **bundle**, and a bundle can be soldered while the
theory's observable labels are organised by a commuting subgroup of a larger
gauge group; that is ordinary in first-order gravity and it is why §5 exists.
(iii) `MD-1` §4 already shows that reading damages the twelve identically, which
is a reductio against the reading, not a result against GU. The correct headline
is the narrow one: **the horn as typed is refuted; the consequence attached to it
is not established.**

**Second overclaim, refused.** *"SA-1 discovered that `P_H` is soldered."* It did
not. `k77-global-chimeric-spin-reduction-…-2026-08-05` constructed it, with an
exact certificate and an independent Sage implementation, and its source
reinspection graded the return `SOURCE-CORRECTS` on eight dated primary loci.
`selected-k77-full-reduction-quotient-reconciliation-2026-08-07` restated it. The
manuscript prints the definition. SA-1's contribution is the **composition** and
the **re-typing**, and any citation that says otherwise is a false-novelty claim
of exactly the kind this repository has produced eight times.

**Strongest contrary construction, built as a live control.** Deny the soldering:
set `d rho_{Sym^2} = 0`, i.e. assert the `Sym^2` leg carries no Lorentz action.
That is the `inert-ad` mutation and it is run through the full harness. It
changes `Inv(Sym^2)` from `1` to `10`, `Inv(traceless 9)` from `0` to `9`,
`Inv(Lambda^2 V)` from `0` to `45`, the endogenous rank from `6` to `0`, and the
invariant part of `k` from `0` to `21` — and the harness exits `1`. So the whole
result is genuinely bought by the nonvanishing of `d rho_{Sym^2}`, and the
routines are not returning their answers by construction.

**Second contrary, built.** Deny the distinction: set
`rho_block := rho_endo` (`block-is-endo`). Then F07's 12 collapses to 6 and F12's
21 collapses to 0, and the harness exits 1. So the two subalgebras being
*different* is a computed fact, not a definition.

**Weakest seam, and it is mine.** The claim that `so(1,3)_endo` is *the*
physical local Lorentz group rests on the premise that the observed 4D spacetime
is `X` with its metric `g = s`, so that `Sym^2(T^*X)` is a tensor bundle on the
observed spacetime. `SECTION-VS-OBSERVERSE` is `status: open`, and on the
"full observerse" horn there is no `X`-frame group to be endogenous to. I have
**not** decided that fork; it is declared in `fork_assumed`. This does not touch
§2 (the bundle-layer refutation of `INERT-AD` is independent of which arena is
physical), but it does mean the §4/§5 residue is stated *relative to* the section
horn.

**Second seam.** The `(7,7)` versus `(9,5)` carrier is `CARRIER-SPLIT`, open. I
have swept it (F01–F04) and both subalgebras sit inside both real forms, so the
result is fork-independent — but the sweep covers the two *Lorentzian* horns
only, not the compact/complexified `(4,0)+(5,5)` horn the finite census uses.
Nothing here is claimed on that horn.

**Third seam, inherited and not repaired.** `SOLDERED-AD` has never been entered
in `lab/process/layer0-fork-registry.yaml` (the probe reports zero occurrences of
`SOLDERED` in that file, S30, and reports it as archaeology, not evidence). That
is a registry gap `AR-2` did not list among the seven surfaces, and it is a
plausible mechanism for why the K77 chain and the fork never met. I do **not**
edit the registry: this artifact is `pending_integration` and registry
settlements are the canonical owner's.

**On absence-based reasoning.** No step in this artifact rests on a zero-hit
search. The evidence for the horn is a set of **positive** facts — a printed
definition, a hard-core register claim, a built construction with a certificate,
and eleven exactly-matched source substrings. Where I report an absence (S30) it
is labelled non-load-bearing in the probe itself.

---

## 7. WHAT THE FIVE ANOMALY ROWS INHERIT

### 7.1 `AC-D1..D5`

`PHI-2` §7.2 made the fork verdict-load-bearing for these five rows by way of
**gauge-blindness**: `PHI-1` §2.1 established that in `M`'s own construction the
gauge Casimir `Y` occurs only in `ch(S)` and never in the form-leg factor
`A-hat(TY) ch(Lambda^p T_C)`, and `PHI-2` showed that denying that on the
spin-extended target changes the **verdict**, not merely the rank.

**What they inherit is a decided ambient horn plus a named blocked condition —
and no verdict movement.** Precisely:

1. **The promotion stands.** `PHI-2`'s finding is untouched. The fork is still
   verdict-load-bearing for these rows.
2. **Its trigger is re-typed.** The trigger is no longer "an undecided fork about
   which bundle `P_H` is". It is "an undecided **action-invariance** property
   deciding which of two subalgebras of one soldered bundle labels observed 4D
   spin". One defence of gauge-blindness is now **closed**: it can no longer be
   secured by appeal to `P_H` being an independent internal bundle, because it is
   not one.
3. **The corrected `distance` becomes horn-indexed rather than horn-free.**
   `PHI-1`/`PHI-2`'s corrected `distance` — *"none after the internal SM content
   `v` of the observed 4D spinor is fixed, and `v` is SU(5)-complete"* — is a
   result **inside** the gauge-blind arena. On the `so(1,3)_H` reading that arena
   is intact and the result stands verbatim. On the `so(1,3)_endo` reading the
   arena's defining factorisation fails, and by `PHI-2`'s own limiter the
   consequence is not a different `phi_ext` but the loss of `ker M` — i.e. the
   question the rows are answering is not posed in that arena at all.
4. **The revival trigger is unchanged.** It still fires iff `v not-in L`. What
   changes is that the trigger now carries a named enabling condition.
5. **Zero rows advance. No ledger edit. No verdict, grade, distance, priority or
   canon movement.** `AC-C2` and `AC-E1` are untouched by SA-1.

Under `GU-COMPARATOR-ROUTING`, note that `PHI-2`'s arena is a **fork-1
conventional comparator**; nothing in §7 transports a comparator conclusion onto
a source-native object, and nothing in §2–§5 depends on the comparator.

### 7.2 `LA-8`'s scope, kept separate — this is not a contradiction

`LA-8` established that the fork is **not load-bearing for `RA-E2` at the settled
form leg**, because *both* horns give zero colour-singlet weak doublets (`45 -> 0`
and `1 -> 0`). **That remains exactly correct and SA-1 does not touch it.** SA-1
decides *which horn*, not *what the count is*, and the count is zero on both. The
two scopes are:

| | `LA-8` | `SA-1` |
|---|---|---|
| scope | `RA-E2`, the form leg, doublet counting | the fork itself, the ad leg, bundle ownership |
| claim | the fork is not load-bearing **for that row** | the bundle-layer horn is decided; the observed-layer question is not |
| relation | independent | SA-1 shows LA-8's two horn-numbers are the two subalgebras |

Anyone who reads SA-1 as overturning `LA-8` has confused a scope change for a
contradiction, which is the failure mode
`explorations/claim-indexed-verdict-doctrine-2026-08-12.md` exists to prevent.

---

## 8. POSTFLIGHT — six lenses, run inline after the computation

**Bundle geometry.** The result is a statement about associated bundles and
nothing more: `P_H` is associated to `Fr~(C)`, `C` is functorial in `T^*X`, so
`ad(P_H)` is Lorentz-associated. It survives every metric-signature convention
tested and every value of the trace-reversal parameter. It does not survive a
denial of `Y = Met(X)`, which is not on offer.

**Representation theory.** The two subalgebras are the honest content. A useful
sanity statement: they are *conjugate* in `GL(14)` but **not** by an element that
fixes the `V (+) H^*` splitting, and the element relating them,
`delta`, has k-projection rank 3 and p-projection rank 3 — it is non-compact, so
it is not an SM-type internal rotation. That non-compactness is why the two
readings cannot be reconciled by a compact gauge choice, and it is what makes the
residue a genuine action question rather than a normalisation.

**Source fidelity.** Every source fact used is a positive, dated, quoted locus
with a register id where one exists. The corrected 2026-08-15 source facts are
respected: I make no positivity claim on an observed quotient, no chirality
claim, no `SU(3,2)` claim, no Kaluza-Klein claim, and I treat the observation
reduction as a contraction throughout. The `Y = Met(X)` endogeneity is used as
endogenous, not as KK.

**Adversarial red-team.** The single most damaging thing that could be true of
this artifact is that `so(1,3)_H` is not actually a subalgebra of the *reduced*
structure algebra available after observation — i.e. that the manuscript's
`Spin(7,7) -> Spin(1,3) x Spin(6,4)` chain is itself reconstruction-grade rather
than source-determined. I checked: the chain appears in
`docs/paper-formalization-candidates.md` 6D with a manuscript locus (§4.1, §11.2,
pp. 25–27, 62–63) and in `papers/drafts/no-go-class-relative-survey.md`, and
`SC-GRP-03` books the adjacent Standard-Model-inside-`Spin(6,4)` claim as
`ASSERTS`. The chain is therefore source-printed. Separately, and consistent with
my brief's correction, the `SU(3,2)` *link* in the downstream chain is
transcript-uncertain reconstruction — I use none of it; only the first arrow,
`Spin(7,7) -> Spin(1,3) x Spin(6,4)`, is load-bearing here.

**Fork hygiene.** Three open forks are declared and none is silently used:
`CARRIER-SPLIT` (swept over both Lorentzian horns; the compact horn is not
covered), `SECTION-VS-OBSERVERSE` (declared; it bounds §4/§5, not §2),
`VERTICAL-FROBENIUS-TRACE` (swept over seven exact `lambda` values). `SOLDERED-AD`
is decided only at the layer stated and is **not** marked settled anywhere — this
artifact writes to no registry.

**Process auditor.** The archaeological finding stands on its own and should be
read by whoever owns the queue: a fork was declared, ranked the most-flagged open
object in the tree across seven surfaces, routed out as expensive, then promoted
to verdict-load-bearing — while a construction that settles its bundle layer,
with an exact certificate, an independent Sage implementation and a
`SOURCE-CORRECTS` return, had been sitting in `explorations/conditional-build/`
for nine days, and while `path-dependencies.md` carried a dated trap against the
very premise, logged the same day the fork was declared. The cost of the fix was
one retrieval pass. The mechanism of the failure is the one the Layer-0 fork
registry was built to catch, and the fork was never entered in it.

---

## 9. CERTIFICATE

`tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py` — **105/105,
exit 0.**

```
   [S] 30   exact source / manuscript / register / artifact substrings
   [B]  4   Stiefel-Whitney reproductions of K77 eq (3)-(5)
   [C] 12   Clifford reproductions of K77 eq (9)-(11)
   [D] 14   endogenous-representation results (homomorphism, isometry, faithfulness, sweeps)
   [E] 24   reproductions of MD-1 / PV-2 / LA-8
   [F] 17   the two-subalgebra result
   [L]  4   owner probes re-run clean
                 of which  6  are CONTRARY CONTROLS that must PASS
```

Reproductions: `MD-1` (A2/A3 inertias `(7,3)` and `(6,4)`; B11 `Inv(Sym^2)=1`;
B12 control `=10`; C16/C17 the endogenous embedding, rank 6; C18 k- and
p-projection ranks `3` and `3`; C19; C20 control, rotations have zero p-part;
D3 `=0`; D4 `=0`; D5 control `=6`; D6 `=45`; A6/A7 total `(9,5)`).
`PV-2` (`dim k = 21`, `dim p = 24`, Killing negative on `k`, positive on `p`).
`LA-8` (B1/B2 `Inv(Sym^2)=1` on the `eta` line; B3 `=0`; B4c control `=10`;
B5c control `=2` under `so(3)` alone; D1 `=0`; D7c control `=45`; **its own probe
re-run clean under subprocess, 78/78, exit 0**).
K77 2026-08-05 (`w1(Sym^2 E)=w1(E)`, `w2(Sym^2 E)=w1(E)^2`, `w1(C)=0`,
`w2(C)=w2(E)`; `Cl(7,7)=M_128(R)` with 16384 monomials; `B^2=1`, `tr B=0`,
`sig B=(64,64)`; grade-one and grade-two `B`-skewness; **its own probe re-run
clean under subprocess, 53/53, exit 0**).

Exactness: `fractions.Fraction` and integer linear algebra over `Q`; Sylvester
congruence for every inertia, never eigenvalues; an SO(3)-adapted exact
congruence so the Cartan decomposition is the one in which the compact rotations
sit inside `k`; F2 symmetric-function arithmetic for the characteristic classes;
`numpy` integer matrices with `dtype` and entry bound `<= 1` both asserted for
the Clifford block. `assert_no_float` sweeps the result dict. No float is
load-bearing anywhere.

**Failure path exercised — eight planted false facts, each exits 1:**

| `--mutate=` | plants | what it breaks |
|---|---|---|
| `inert-ad` | `d rho_{Sym^2} = 0` (the ad index is Lorentz-inert) | the entire endogenous block; `Inv` counts flip `1->10`, `0->9`, `0->45` |
| `block-is-endo` | the two Lorentz subalgebras coincide | F07 `12->6`, F12 `21->0` |
| `not-a-hom` | `r_C` composed order-reversed | D09, the group-homomorphism certificate |
| `lambda-blind` | the DeWitt trace term carries the wrong sign | the `lambda` sweep and the `(7,3)`/`(6,4)` inertias |
| `clifford-dup` | two gamma generators identified | the `(7,7)` square count and the 91 anticommutators |
| `w2` | `w2(Sym^2 E) = w2(E)` | K77 eq (3)–(5) |
| `source` | one register substring corrupted | the `[S]` block |
| `k-p-swap` | `k` and `p` exchanged | Killing definiteness, and the `0`/`21` pair |

**Baseline discipline.** `--selftest` runs the **clean baseline first** and
aborts with exit 1 if it is not green, before attempting any mutation — the
defect that three archaeology probes shipped with on 2026-08-15. The guard is
itself controlled: `--selftest --mutate=X` poisons the baseline, and the run
prints `clean baseline does NOT pass; mutations were NOT run` and exits 1,
demonstrating that the guard has power rather than asserting it.

```
_local/cas-venv/bin/python tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py
    -> CERTIFICATE: 105/105 checks pass; no load-bearing float (swept).   exit 0

_local/cas-venv/bin/python tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py --selftest
    -> clean baseline green, 8/8 planted false facts each exit 1.          exit 0
```

---

## 10. WHAT THIS DOES NOT SUPPLY

No source action. No BRST, BV, CME or master equation. No quotient, no reduced
symplectic class, no domain, no spectrum, no propagator, no mass, no
quantization. **No attempt whatsoever at the residual selector of §5** — that
object is named, owned and already scheduled, and duplicating it is waste.
No decision of which Lorentz subalgebra labels observed 4D spin. No decision of
`CARRIER-SPLIT`, `SIGNATURE-AMBIENT`, `SECTION-VS-OBSERVERSE`,
`VERTICAL-FROBENIUS-TRACE`, the carrier bit, or the Velo–Zwanziger question. No
statement about the spinor sector, chirality, generations, positivity on an
observed quotient, or the Higgs channel. No re-decision of `RA-E2`, `RA-E1`,
`RA-E3` or `RA-E4`. No claim that the SM's twelve are or are not well-typed —
that is downstream of §5 on both readings. No ledger edit, no fork-registry edit,
no correction-registry edit, no canon movement, no current-state movement, no
priority movement, no claim-status movement, and no public-posture change. The
K77 chain, `MD-1`, `LA-8`, `PV-2`, `PHI-1`, `PHI-2` and `AR-2` are imported and
reproduced; none of them is re-claimed here.

---
artifact_type: exploration
status: exploration
doc_type: ledger-delta
created: 2026-08-15
work_item: LA-7
channel: conditional_ledger_advancement
base_revision: a148ed80
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
axis: LAGRANGIAN
delta_kind: VERSIONLESS_DELTA__NOT_A_LEDGER_EDIT
target_claim: NONE-NOT-A-KILL
canonical_effect: pending_integration
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
title: "LA-7: the LAGRANGIAN axis's one movable grade MOVES. LT-SM7 goes T0 -> T2 (+2 of 5 notches on the constrainedness ladder) at unchanged verdict and unchanged reason_kind, because the theta sector is now TYPED and one supplier class is EXCLUDED. Computed exactly, no lookups: the exceptional isomorphisms so(6) = su(4) and so(4) = su(2)+su(2) are DERIVED as Cartan-matrix isomorphisms from an e_i root realisation; rank pi_3 = number of simple ideals is read off the Dynkin graph; and rank H^4(BG;Q) = dim (Sym^2 t*)^W is solved as an exact integer null-space, not asserted. Result: the two natural theta-counting invariants DISAGREE. Under pi_3 the reconstructed subgroup sequence reads 3, 2, 2; under H^4(BG;Q) it reads 3, 3, 3. So LA-6's 'one extra angle relative to the SM' is invariant-dependent and is NOT banked here. What IS invariant-independent, and is the bankable core: over all six admissible (invariant, node) readings the sector rank lies in {2,3}, so LT-SM7's rank-1 booking is short by 1 to 2 under EVERY reading. Two further exact findings: (a) SU(3,2), not Spin(3,2), is the source-internally consistent reconstruction of the transcript's middle node -- selected by dim maxcompact(SU(3,2)) = 12 = dim SM versus dim maxcompact(Spin(3,2)) = 4, with audio confirmation still owed; (b) T_9, GU's only written topological term, is Z/2-quantized and therefore cannot supply a general point of a positive-dimensional angle torus -- the whole class of finite-order suppliers is excluded on cardinality. Secondarily the LT-SM1 split is BANKED as a delta on two independent routes (2026-08-12 surplus side, 2026-08-15 incidence side), with the honest report that the two routes DISAGREE on the second atom's reason_kind. Also computed: LT-SM7 and LT-SM1 are byte-identical across all 258 ledger versions."
grade: "EXACT integer / fractions.Fraction arithmetic throughout; Cartan matrices built from integer inner products of an explicit e_i root realisation; the exceptional isomorphisms derived by exhaustive permutation search over Cartan matrices; rank H^4(BG;Q) obtained as an exact null-space dimension over Q by Fraction elimination, cross-checked against the closed form s + m(m+1)/2 at all four nodes; assert_no_float sweeps the entire result dict and the source contains no float literal. 77/77 checks, exit 0, via tests/channel-swings/joe_directed_ledger_sm7_topological_rank.py -- 59 [E] exact results and 18 [C] planted controls that must have power, including a positive control (RA-E1) proving the freeze sweep can detect change. Every claim about a ledger row is backed by an exact substring of that row's own v0.258 text. Four standard theorems are IMPORTED and declared, not derived: Borel's H^*(BG;Q) = (Sym t*)^W, the Cartan/Iwasawa maximal-compact retraction, Bott's pi_3(compact simple) = Z, and covering-space invariance of pi_n for n >= 2. NOT: a ledger edit, a verdict change, a reason_kind change, a physics derivation, a coefficient, a theta value, a claim that any angle is physical, a computation of the reduction MAP, or any statement that a GU object exists."
disposition: LT_SM7_T0_TO_T2_PROPOSED__SECTOR_TYPED_AS_RANK_R_ANGLE_TORUS_R_BRACKETED_2_OR_3__BOOKING_RANK1_SHORT_UNDER_EVERY_READING__PI3_AND_H4BG_DISAGREE_SO_EXTRA_ANGLE_READING_NOT_BANKED__TORSION_SUPPLIER_CLASS_EXCLUDED__MIDDLE_NODE_IS_SU32_NOT_SPIN32_AND_THE_GARBLE_IS_LOAD_BEARING__T3_BLOCKED_BY_NODE_SELECTION__LT_SM1_SPLIT_BANKED_ON_TWO_ROUTES_WITH_SECOND_ATOM_KIND_CONTESTED
rows_assessed:
  migration_proposed:
    - LT-SM7
  split_proposed:
    - LT-SM1
  structural_finding:
    - LT-SM7
    - LT-SM1
  declined:
    - LT-GR7
    - LT-SM2
    - LT-SM5
    - LT-SM6
    - LT-SM3
    - LT-SM3b
    - LT-SM4
    - LT-SM8
    - LT-GR1
    - LT-GR1b
    - LT-GR2a
    - LT-GR2b
    - LT-GR2c
    - LT-GR2d
    - LT-GR2e
    - LT-GR3
    - LT-GR4
    - LT-GR5
    - LT-GR6
grants_invoked:
  - id: GRANT-LA7-DELTA5
    statement: "CG-1's GU-YM-Delta5 typing -- the internal group is the OUTPUT of a declared Cartan reduction, maximal compact of a non-compact real form -- is a correct reading of the primary source."
    provenance: IN_REPO_RESULT_REUSED__NOT_RE_DERIVED
    already_recorded_at: "lab/active-research/joe-directed/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md:244-301"
    falsifiable_by: "a source locator showing the internal group is DATA rather than the output of the declared Cartan reduction"
  - id: GRANT-LA7-STANDARD
    statement: "Four standard theorems are imported: Borel's H^*(BG;Q) = (Sym t*)^W; the Cartan/Iwasawa retraction of a connected real semisimple group onto its maximal compact; Bott's pi_3(G) = Z for G compact simple; and pi_n invariance under covering maps for n >= 2."
    provenance: STANDARD_MATHEMATICS_IMPORTED__DECLARED_NOT_DERIVED
    falsifiable_by: "n/a -- these are textbook results; the probe derives everything downstream of them"
  - id: GRANT-LA7-NONE-PHYSICS
    statement: "No physics premise is granted. No GU object is assumed to exist. No action term is assumed to be written."
    provenance: NO_GRANT_TAKEN
refusals:
  - "DERIVED_CONDITIONAL -> DERIVED is not proposed for any row. No reason_kind is proposed for upgrade toward dischargeability anywhere in this artifact."
  - "LT-SM7's verdict stays NEEDS and its reason_kind stays REAL_PARAMETER. Only mapping_grade and distance move. That is the same shape as v0.258's own migration_policy ('distances at unchanged verdict and reason kind')."
  - "LA-6's 'the Delta5 group carries one more theta angle than the Standard Model' is NOT banked. It holds under pi_3 and FAILS under H^4(BG;Q). This artifact reports the disagreement rather than picking the favourable invariant."
  - "The second reduction step is NOT computed as a map. Only the ranks AT each declared node are computed. LA-6's fence 1 is respected and restated."
  - "Physicality of any theta angle is NOT claimed. LA-6's fence 2 is respected and restated. No statement is made about theta-bar, the strong CP problem, or the measured bound."
  - "The LT-SM1 horn selection is NOT re-attacked. The 2026-08-12 attempt's SURPLUS-UNCOMPUTABLE verdict stands unchallenged; only the split it recommended is banked."
  - "LT-SM1a is NOT retyped to ONE_BIT. LA-6 4.1's fork-completeness question is live and would make the price log2(3). ONE_BIT is recorded as a CONDITIONAL successor kind behind a named gate."
depends_on:
  - lab/process/conditional-physics-ledger-v0.258.json
  - lab/process/science-council-program-efficiency-2026-08-04.md
  - lab/methods/source-native-comparator-routing.md
  - explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md
  - explorations/lt-sm1-horn-surplus-attempt-2026-08-12.md
  - lab/active-research/joe-directed/ledger-advancement/la6-the-lagrangian-axis-has-twelve-degrees-of-freedom-and-one-constructible-cover-object-2026-08-15.md
  - lab/active-research/joe-directed/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md
  - lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md
  - explorations/wave14/H19-seven-seven-signature-branch-2026-07-11.md
  - papers/drafts/Transcript into the impossible.md
  - lab/literature/weinstein-ucsd-2025-04-transcript.md
scripts:
  - tests/channel-swings/joe_directed_ledger_sm7_topological_rank.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

**Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.** The Standard Model group
appears here only as a *rank comparator* for a counting invariant. No claim is
transported across the boundary in either direction, and §5.2 records the one
place where a reader would be tempted to.

# LA-7 — `LT-SM7` moves `T0 -> T2`, and the `LT-SM1` split is banked

---

## 0. PREFLIGHT

### 0.1 Work list, re-derived from the ledger — not inherited from the brief

Re-derived by loading `lab/process/conditional-physics-ledger-v0.258.json` at
`a148ed80` and filtering, not by trusting LA-6's table.

| filter | result |
|---|---|
| `mapping_grade` beginning `T<digit>` across all 84 records | `LT-SM7` (T0), `RA-G3` (T2), `AC-B2` (T3), `LT-GR1b` (T4), `AC-F5` (T4) |
| rows at `T0` | **exactly one: `LT-SM7`** — the brief's premise confirmed mechanically |
| `reason_kind == FINITE_CHOICE` across all 84 records | **exactly one: `LT-SM1`** |
| `reason_kind == ONE_BIT` across all 84 records | **zero** |
| LAGRANGIAN rows excluding `SUPERSEDED` | 21, matching `denominator.axes.LAGRANGIAN` |
| `denominator` arithmetic | 84 records − 2 superseded = 82 canonical targets ✓ |

Both target rows are exactly as briefed. **The work list stands.**

### 0.2 What moved — and the honest answer is *nothing in the ledger, ever*

The preflight is required to report movement. It found the opposite of movement,
and it is measurable:

**`LT-SM7` and `LT-SM1` are byte-identical in all 258 ledger versions.** The
probe sweeps every `conditional-physics-ledger-v0.N.json` from `v0.1` to
`v0.258`, canonicalises each row with `json.dumps(..., sort_keys=True)`, and
finds **zero** text changes for either row across 258 files. Neither appears in
`migration_history` at all. The sweep is not blind: run on `RA-E1` as a positive
control it detects changes at `v0.190`, `v0.195`–`v0.202` and beyond.

So the two rows this brief targets are, jointly, the least-moved objects on the
axis. That is the correct frame for what follows: a `T0 -> T2` movement would be
the first change either row has ever had.

**What did move is the evidence base, all of it dated today or this week.**
`CG-1` (2026-08-14) supplied the `Delta5` typing; `LA-6` (2026-08-15) applied it
to `LT-SM7` for the first time and identified the `T0 -> T1` homotopy lookup as
the axis's only movable grade; the `LT-SM1` horn attempt (2026-08-12) is three
days old. The ledger is stationary; the reading of it is not.

**Concurrency check.** `v0.258` is the highest ledger version present; no
`la7-*` artifact and no `joe_directed_ledger_sm7_*` probe existed before this
one. No ledger, canon, or `CURRENT-STATE` file is touched.

### 0.3 Preflight lenses — five, problem-matched, inline

**Lens P1 — algebraic topologist. *Is `pi_3` the right invariant for a theta
sector at all?*** This is the lens the brief most needs run, and it changes the
result. A theta term is `theta` times a degree-4 characteristic class integrated
over spacetime. The set of independent such classes for structure group `G` is
`H^4(BG;Z)`, whose rank is `s + m(m+1)/2` for `s` simple ideals and an
`m`-dimensional central torus. `pi_3(G)` has rank `s` — it drops the torus's
`c_1^2` contribution. The two agree exactly when `m = 0`. **The `Delta5` group
has `m = 0`; the Standard Model has `m = 1`.** So the two invariants agree on the
`Delta5` node and disagree on the comparator, which is precisely the place LA-6's
headline sits. *This lens was run because "count the angles" is the kind of
question where the physics folklore answer (2 for the SM) and the topology answer
(3 for the SM) differ, and taking the folklore number silently would have made
the finding look sharper than it is.* Both are computed in §1.

**Lens P2 — textual source-critic. *Is the declared chain's middle node
`SU(3,2)` or `Spin(3,2)`?*** LA-6's fence writes `Spin(6,4) -> Spin(3,2) ->
SU(3)xSU(2)xU(1)`. The raw transcripts say **both**, in one paragraph:
`Transcript into the impossible.md:152` says *"the maximal compact subgroup of
**s u three comma two**"* and repeats it a sentence later, while `:155` says
*"this is the right chain. Spin six four, **spin three comma two**, s u three
cross s u two cross u one."* CG-1 itself warns the transcripts are *"automated
and lightly garbled."* The repo carries both readings unreconciled:
`H19-seven-seven-signature-branch-2026-07-11.md:114` and its probe encode
`Spin(3,2)`; `curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md:291`
encodes `SU(3,2)` with maximal compact `S(U(3)xU(2))`;
`transcript-concordance-derived-results-2026-07-11.md:53` carries **both in a
single sentence**. **This is decidable by integer arithmetic and §1.4 decides
it.** It is not cosmetic: §2.3 shows the answer is load-bearing for the whole
finding.

**Lens P3 — metrology / grading auditor. *What does each notch of the T-ladder
actually require, and can the ledger see a move?*** The ladder is defined once,
at `lab/process/science-council-program-efficiency-2026-08-04.md:85-91`: T0
"requirement currently met by an unexamined convention"; T1 "named, untyped"; T2
"typed, no class exclusion"; T3 "type + dimension/units fixed **and** a class of
suppliers excluded"; T4 "full type specified **and** every alternative route
exactly excluded." Two consequences, both mechanical. First, T3 has a
**conjunctive** requirement and this artifact satisfies only one conjunct, so
§2.2 stops at T2 and names the blocker. Second, the ledger's own
`residue.tightness_provisional` is `{T4: 1, T3: 3, T2: 1}` — it has **no T0 and
no T1 bucket at all**, and it does not match the row-level census
`[T0, T2, T3, T4, T4]`. It is CB-A's REPRESENTATION-axis tightness vector
(`cb-a-representation-content-2026-08-05.md:500`,
`{T4: 1, T3: 3, T2: 1, T1: 0, T0: 0}`) carried forward with the two zero buckets
dropped — so the buckets that would have registered this movement are exactly
the ones that were deleted for being empty.
**Therefore a `T0 -> T2` movement on `LT-SM7` is invisible to the ledger's own
meter.** Flagged, not fixed — this artifact may not edit the ledger.

**Lens P4 — novelty auditor. *Grep before claiming.*** Run as a repo-wide search
before any novelty word was written.

| item | prior art in repo | scope for LA-7 |
|---|---|---|
| `pi_3` of the gauge group as theta-sector rank | **LA-6 §4.4 only**, dated today | not new; LA-7 re-derives it rather than citing, and adds the second invariant |
| `pi_3^s` (stable 3-stem) | extensive — `dr2`, `dr6`, `located-not-forced` | **different object.** `pi_3^s = Z/24` is the generation-count route. Do not conflate |
| `H^4(BG;Z)` / `H^4(BSpin;Z)` | present, but only as the spin class `p_1/2` in the framing-convention work | **the theta-rank use is new**; the `(Sym^2 t*)^W` computation has no repo precedent |
| `Spin(6) x Spin(4)` as Pati-Salam maximal compact | extensive — `W221`, `papers/drafts/*`, `no-go-class-relative-survey` | not new; used as an input, and the `D_3 = A_3` / `D_2 = A_1+A_1` step is *derived* here rather than quoted |
| `SU(3,2)` vs `Spin(3,2)` | both present, **never reconciled** | **the discriminator is new**, and so is the observation that they coexist unreconciled |
| `T_9` as `Z/2`-quantized sole topological term | `cb-b-lagrangian-terms-2026-08-05.md:SM-7` | not new; **the cardinality exclusion built on it is new** |
| theta-sector supplier exclusion | none | new |

**Lens P5 — taxonomy lawyer. *Does the proposed migration launder anything, and
which fields may legally move?*** The channel has already refused
`DERIVED_CONDITIONAL -> DERIVED` once. The test: does any proposed edge move a
row **toward** dischargeability without supplying the thing? Audit of what LA-7
proposes: `LT-SM7` verdict `NEEDS -> NEEDS`, reason_kind
`REAL_PARAMETER -> REAL_PARAMETER`, only `mapping_grade` and `distance` move.
That is exactly the shape `v0.258`'s own `migration_policy` already authorises
for four other rows ("distances at unchanged verdict and reason kind"), and a
mapping-grade tightening is a statement about *how well the requirement is
specified*, not about whether it is met. For `LT-SM1`, the split's second
successor is proposed at `MISSING_CONSTRUCTION`, which is strictly **less**
dischargeable than the `REAL_PARAMETER` the other route proposes — the same
"safe direction" argument LA-6 used for `LT-GR7`. **No laundering edge exists in
this artifact.** The one place a laundering *could* have crept in — retyping
`LT-SM1a` to `ONE_BIT`, which would make it look like a 1-bit purchase away from
closure — is explicitly refused in §3.3 behind a named gate.

---

## 1. THE COMPUTATION

All of §1 is `tests/channel-swings/joe_directed_ledger_sm7_topological_rank.py`,
**77/77, exit 0**, exact integers and `fractions.Fraction` only, `assert_no_float`
sweeping the whole result structure.

### 1.1 The exceptional isomorphisms are derived, not looked up

LA-6's `pi_3` claim rests entirely on `Spin(6) ~ SU(4)` and
`Spin(4) ~ SU(2) x SU(2)`, which it asserts. Here they are derived. Simple roots
are built in an explicit `e_i` realisation — `A_n`: `alpha_i = e_i - e_{i+1}`;
`D_n`: `alpha_i = e_i - e_{i+1}` for `i < n` and `alpha_n = e_{n-1} + e_n` — and
Cartan matrices follow from integer inner products:

```text
Cartan(D_3) = [[ 2,-1,-1],[-1, 2, 0],[-1, 0, 2]]
Cartan(A_3) = [[ 2,-1, 0],[-1, 2,-1],[ 0,-1, 2]]
Cartan(D_2) = [[ 2, 0],[ 0, 2]]      (diagonal: so(4) is NOT simple)
```

An exhaustive permutation search finds a relabelling `D_3 -> A_3` and
`D_2 -> A_1 + A_1`. A planted control confirms the search is doing work: `D_3`
and `A_3` are **not** equal under the identity relabelling. Two further controls
(`D_3 = A_1+A_1+A_1`, `D_2 = A_2`) correctly fail.

### 1.2 Two invariants, both computed exactly

`rank pi_3(G)` = number of simple ideals = number of connected components of the
Dynkin graph, with `U(1)` factors contributing zero. Read off the Cartan matrix
by graph traversal.

`rank H^4(BG;Q)` = `dim (Sym^2 t*)^W`, computed as an **exact null space**: build
the simple reflections `s_i(alpha_j) = alpha_j - C[i][j] alpha_i` as integer
matrices (extended by the identity on the central torus), impose
`M^T Q M = Q` on a symmetric unknown `Q`, and solve over `Q` by Fraction
elimination. The solver is independently power-tested: it returns 1 for `U(1)^1`,
**3** for `U(1)^2`, and 1 for `A_1`; a control asserting 2 for `U(1)^2` correctly
fails. Every node's answer is then cross-checked against the closed form
`s + m(m+1)/2`.

### 1.3 The node table

| node | group | dim | simple ideals | central torus | **rank `pi_3`** | **rank `H^4(BG;Q)`** |
|---|---|---:|---:|---:|---:|---:|
| N1 | `Spin(6) x Spin(4)` — maximal compact of `Spin(6,4)`, the `Delta5` output | 21 | 3 | 0 | **3** | **3** |
| N2 | `S(U(3) x U(2))` — maximal compact of `SU(3,2)`, the source's middle node | 12 | 2 | 1 | **2** | **3** |
| N3 | `SU(3) x SU(2) x U(1)` — Standard Model comparator | 12 | 2 | 1 | **2** | **3** |
| N4 | `Spin(3) x Spin(2)` — maximal compact of `Spin(3,2)`, the garble reading | 4 | 1 | 1 | 1 | 2 |

Both invariants are insensitive to the finite central quotients that actually
occur — `(Spin(6)xSpin(4))/Z_2` for the true maximal compact of `Spin(6,4)`, and
`(SU(3)xSU(2)xU(1))/Z_6` for the true Standard Model group — because `pi_n` is a
covering invariant for `n >= 2` and `H^*(B-;Q)` depends only on the Lie algebra
and Weyl group.

**The headline of the table is the disagreement.** Under `pi_3` the chain reads
`3, 2, 2`; under `H^4(BG;Q)` it reads `3, 3, 3`.

### 1.4 `SU(3,2)` is the source-internally consistent middle-node reconstruction

The source's own sentence under test, stated twice in one paragraph, is *"the
maximal compact subgroup of X is `SU(3) x SU(2) x U(1)`."*

```text
dim( SU(3) x SU(2) x U(1) )          = 8 + 3 + 1  = 12
dim( maximal compact of SU(3,2) )    = 9 + 4 - 1  = 12   -> SATISFIABLE
dim( maximal compact of Spin(3,2) )  = 3 + 1      =  4   -> REFUTED
```

`X = SU(3,2)` makes the source's adjacent claim true; `X = Spin(3,2)` makes it
false by a factor of three in dimension. `SU(3,2) ⊂ Spin(6,4)` is also
dimensionally admissible (24 < 45). **This is a source-internal consistency
selection, not a re-transcription or source determination:** the audio was not
re-listened to. What is established is which of the two readings already present
in the repo is consistent with the source's own adjacent, twice-repeated
statement.

### 1.5 The booking, certified by the row's own text

```json
"summary":  "QCD theta and topological terms are fixed or suppressed",
"distance": "identify the QCD theta coefficient and its symmetry mechanism"
```

The `distance` contains `"the QCD theta coefficient"`, one occurrence of
`coefficient` and zero of `coefficients`: **booking rank 1**. A control confirms
the `distance` contains no `rank`, `count`, `number of` or `how many` — the row
asks for a value and never for a count. A second control confirms `LT-SM7` has
never appeared in `migration_history`.

**A defect the row carries against itself:** the `summary` says "topological
term**s**" (plural, unbounded) while the `distance` names one coefficient. The
row's own two fields disagree on the booking's cardinality. LA-6 read the
`distance`; this artifact records that the `summary` licenses a different read.

### 1.6 The deficit, minimised over every admissible reading

Six admissible readings (2 invariants × 3 nodes, N4 excluded by §1.4):

```text
pi_3      : N1 = 3, N2 = 2, N3 = 2
H^4(BG;Q) : N1 = 3, N2 = 3, N3 = 3
min = 2, max = 3, booking = 1  ->  deficit bracketed at [1, 2]
```

**Under every admissible reading the sector rank is at least 2 and the booking is
1.** Controls confirm no reading rescues the rank-1 booking, and that the
readings do not collapse to a single value.

### 1.7 The supplier exclusion

`CB-B` certifies, by exact substring, that `T_9` is *"GU's only written
topological term, and it is `Z/2`-quantized: `theta in {0, pi}`, not a continuous
angle"*, and that *"There is no `INT F ^ F` in the written candidate."*

A supplier valued in a finite group `F` determines a point of `Hom(F, U(1)^r)`, a
finite set: for `F = Z/2` and `r = 2` that is **4 points**. The sector's
parameter space is the `r`-torus `(R/2piZ)^r` with `r >= 2`, which is
uncountable. A finite set cannot exhaust it.

**Exclusion, exact:** *no finite-order topological class can supply a general
point of the sector, so `T_9` alone is excluded as a complete supplier.* Controls
confirm the exclusion is not vacuous — `T_9` is written, named, and is the only
candidate — and that it is not an artifact of a degenerate rank.

This is a **different and independent** statement from `CB-B`'s own fence, which
says no descent map from `T_9` to the 4D instanton number exists. `CB-B` says the
map is unbuilt; LA-7 says that even granting the map, the counting fails.

---

## 2. THE PROPOSED MIGRATION — `LT-SM7`

### 2.1 The transition table

| field | from | to |
|---|---|---|
| `verdict` | `NEEDS` | **`NEEDS`** (unchanged) |
| `reason_kind` | `REAL_PARAMETER` | **`REAL_PARAMETER`** (unchanged) |
| `mapping_grade` | `T0_OPEN` | `T2_SECTOR_TYPED__PI3_RANK3_AT_DELTA5_NODE__PI3_RANK2_AT_SU32_AND_SM_NODES__H4BG_RANK3_AT_ALL_NODES__BOOKING_RANK1_SHORT_BY_1_TO_2__TORSION_SUPPLIER_CLASS_EXCLUDED__NODE_SELECTION_AND_PHYSICALITY_OPEN` |
| `distance` | "identify the QCD theta coefficient and its symmetry mechanism" | "the sector is an `r`-torus of periodic dimensionless angles with `r` in `{2,3}`; pin `r` by selecting the reduction node, then supply the `r` angles and their symmetry mechanism" |
| `revival_trigger` | "a source-action topological sector with computed periodic parameter" | "a written degree-4 topological term on a selected reduction node, plus a descent map for its coefficient" *(offered; the existing trigger is not defective)* |

### 2.2 The grade movement, stated precisely

**`T0 -> T2`. Two notches on a five-notch ladder.**

- **Out of T0** ("met by an unexamined convention"). The convention is now
  examined: the term that was silently not written has a known parameter space of
  known rank, and the sole written candidate for the slot is excluded from
  supplying it.
- **Past T1** ("named, untyped"). The requirement is typed: an element of
  `Hom(pi_3(K), U(1)) ~ U(1)^r`, i.e. a point of a compact `r`-torus,
  dimensionless, periodic mod `2pi`, paired with a free abelian group of rank `r`.
- **At T2** ("typed, no class exclusion") — and in fact T2 *plus* one class
  exclusion, since §1.7 excludes all finite-order suppliers.
- **NOT T3.** T3 is conjunctive: "type + dimension/units fixed **and** a class of
  suppliers excluded." The second conjunct holds. The first does not: `r` is
  bracketed at `{2,3}`, not fixed. **The single blocker is node selection**, which
  is exactly LA-6's fence 1. This is stated as a check in the probe (`S4`), not as
  prose.

### 2.3 The dependency that makes this fragile, stated openly

**If the middle node were `Spin(3,2)`, this entire finding collapses.** Its
maximal compact has `rank pi_3 = 1`, equal to the booking, so the minimum deficit
would be **0** and `LT-SM7` would be correctly booked at the chain's end. The
probe states this as an explicit check (`S7`) rather than hiding it. The finding
therefore rests on §1.4's dimension test, and on nothing else for that step.

### 2.4 A secondary observation, offered and not asserted

`LT-SM7` bundles two obligations of different taxonomic kind: **how many** angles
(an `INTEGER_DATUM`, `r in {2,3}`, discharged by node selection) and **what
values** (a `REAL_PARAMETER`, `r` angles). This is the same pathology as
`LT-SM1`'s, on the same axis, in the same evidence document (`CB-B`). It is
recorded as `PROPOSED_NOT_ASSERTED`; the primary migration in §2.1 does not
depend on it.

---

## 3. THE `LT-SM1` SPLIT — BANKED, NOT RE-ATTACKED

### 3.1 Two independent routes to one split

| | Route A | Route B |
|---|---|---|
| artifact | `explorations/lt-sm1-horn-surplus-attempt-2026-08-12.md:460-468` | `la6-...-2026-08-15.md` §2.9 IT-2 and §3.4 |
| date | 2026-08-12 | 2026-08-15 |
| method | constraint-surplus enumeration; outcome `SURPLUS-UNCOMPUTABLE` because both sides of the subtraction are unresolved | incidence-matrix information pricing: `LT-SM1`'s atom set is `{I, A}` = one priced bit plus one unpriced construction |
| recommendation | split into `LT-SM1a` (FINITE_CHOICE, the bit) and `LT-SM1b` (**REAL_PARAMETER**, the normalization) | split into a FINITE_CHOICE bit row and a **MISSING_CONSTRUCTION** normalization row |

Both are verified by exact substring in the probe. Two independent methods
reaching the same partition of one row is the strongest thing on that row, and
banking it is the task; re-attacking the horn is not.

### 3.2 Where the two routes DISAGREE — reported, not smoothed over

They agree the row splits and agree the first atom is the `zeta_F` bit. **They
disagree on the second atom's `reason_kind`.** A planted control in the probe
asserts they agree and correctly fails.

Proposed reconciliation, offered as the least-committal reading consistent with
both: `g_A^{-2}` *would be* a `REAL_PARAMETER` once the 1-to-3 branching
construction exists; the branching does not exist; therefore the row's kind today
is `MISSING_CONSTRUCTION`, with `REAL_PARAMETER` as its successor kind. Route A
itself names the unbuilt branching alongside `g_A^{-2}`, so this is a
reconciliation rather than a choice against Route A. It also moves the row
**away** from dischargeability, which is the non-laundering direction.

### 3.3 The split, and the one retyping that is refused

| | `LT-SM1a` | `LT-SM1b` |
|---|---|---|
| `split_from` | `LT-SM1` | `LT-SM1` |
| `source_row` | `CB-B:SM-1#zeta-f-horn` | `CB-B:SM-1#relative-normalization` |
| `summary` | Yang-Mills kinetic term: fundamental versus induced (the `zeta_F` horn) | relative normalization of the Yang-Mills kinetic term (`g_A^{-2}`) and the 1-to-3 branching |
| `verdict` | `NEEDS` | `NEEDS` |
| `reason_kind` | **`FINITE_CHOICE`** (retained) | **`MISSING_CONSTRUCTION`** |
| `distance` | select the `zeta_F` horn | build the branching that makes a relative normalization computable, then supply it |
| `mapping_grade` | `FORM_EXACT_FORK_OPEN__HORN_CARDINALITY_2_CERTIFIED__THIRD_HORN_COMPLETENESS_OPEN` | `NORMALIZATION_UNBUILT__BRANCHING_1_TO_3_OPEN__GA_INVERSE_SQUARED_CHARGING_DISPUTED_IN_REPO` |
| `LT-SM1` itself | `row_status: SUPERSEDED`, `successors: [LT-SM1a, LT-SM1b]`, `superseded_reason`: "the row carried a one-bit selection and an unbuilt normalization construction under a single FINITE_CHOICE label" | |

**REFUSED: retyping `LT-SM1a` to `ONE_BIT`.** It is tempting — `ONE_BIT` is
declared in the taxonomy and used **zero** times in 84 rows, and Route A
certifies `|H| = 2`. But LA-6 §4.1 raises a live fork-completeness question: if a
third horn (the Yang-Mills-shaped term as a functional of the *difference* of two
connections, per `Delta2`) is admissible, the price is `log2(3)`, not one bit.
`ONE_BIT` is therefore recorded as a **conditional successor kind** behind the
named gate *"fork-completeness resolved to |H| = 2"*, and `FINITE_CHOICE` is
retained today. This is the one place where the artifact could have manufactured
a first-ever taxonomy use and declined to.

### 3.4 Denominator effect, computed

Under the `LT-GR2` precedent (supersede the parent, append the successors):

| field | before | after |
|---|---:|---:|
| `row_record_count` | 84 | 86 |
| `historical_superseded_count` | 2 | 3 |
| `canonical_target_count` | 82 | 83 |
| `axes.LAGRANGIAN` | 21 | 22 |

`86 - 3 = 83` closes. The split does **not** touch `residue.open_discrete_forks`
(9) or `open_fork_horn_product` (1152) — a ledger row re-partition is not a
Layer-0 fork retirement. A control asserting otherwise correctly fails.

---

## 4. POSTFLIGHT

### 4.1 Strongest overclaim available in this artifact

**"GU predicts an extra theta angle relative to the Standard Model."** That
sentence is one short step from LA-6's `3 versus 2` and it is the sentence a
reader will extract. It is **not banked here, and §1.3 is why**: under
`H^4(BG;Q)` — arguably the more apt invariant, since a theta term is a
coefficient on a degree-4 characteristic class — the counts are `3` and `3` and
the surplus is zero. The `pi_3` reading is the right one only for configurations
classified by maps to `S^4`, where the Standard Model's hypercharge `c_1^2` term
has no instanton number to multiply. **The "extra angle" is a statement about
which invariant you count with, not about GU.** A planted control (`P7`)
asserting `rank H^4(B(SM);Q) = 2` correctly fails, so the certificate cannot be
read as supporting the sharper claim.

Second overclaim guarded against: **"the sector rank is 3."** It is 3 at the
`Delta5` node only. The artifact says "bracketed at `{2,3}`" everywhere, and the
probe check `S4` exists specifically to make the non-pinning machine-visible.

### 4.2 Strongest contrary reading

**A lattice/QFT specialist would say the physical count is smaller than any
number in the table, possibly 1, possibly 0.** In the Standard Model,
`theta_weak` is removable by a `B+L` rotation because `SU(2)_L` has anomalous
fermionic zero modes, and the hypercharge angle is unobservable on `R^4`. So the
*physically observable* count is 1, not 2 and not 3. If the same reduction
applies at the `Delta5` node — and with chiral fermion content one expects some
angles to be rotatable away — the observable rank could fall to 1 and `LT-SM7`'s
booking would be exactly right after all.

**This does not overturn the finding, and the reason is precise.** The
observable-count argument requires the fermion content and the anomaly structure
of the *reduced* theory, neither of which is settled on this axis; that is
LA-6's fence 2 and this artifact holds it. What the artifact books is the
**geometric rank of the sector**, which is what a ledger row must specify before a
value can be asked for. The contrary reading is best understood as *naming the
route from T2 to T3*: settle the fermion content, settle which `U(1)` rotations
are anomalous, and the rank pins.

There is also a sharper local version worth recording: the map `pi_3(SU(3,2)) ->
pi_3(Spin(6,4))` induced by the inclusion carries **Dynkin indices**, so the
sublattice image is not simply "two of the three generators." That index is not
computed here and would be needed for any statement about *which* angle is lost.

### 4.3 Weakest seam

**The `SU(3,2)` versus `Spin(3,2)` determination.** It is the load-bearing step
(§2.3) and it is decided by a consistency argument over an automated transcript,
not by re-listening to the audio and not by a written source document. If the
speaker actually meant `Spin(3,2)` and simply mis-stated the maximal-compact
claim twice, the deficit collapses to zero. The seam is narrow — mis-stating the
same thing twice in adjacent sentences is unlikely, and the `SU(3,2)` reading is
already independently in the repo at
`curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md:291` — but it is
real, and it is where this result would break first.

**Second seam, smaller.** The T-ladder's own definitions are one table in one
council document from 2026-08-04. "Typed" and "a class of suppliers" are not
formally defined anywhere. A different reader could grade this artifact's output
at T1 (arguing that a bracketed rank is not a type) or at T3 (arguing that the
exclusion plus the bracket is enough). **T2 is defended, not proven**, and the
defence is in §2.2.

### 4.4 Postflight lenses — five, problem-matched, inline

**Lens Q1 — adversarial reviewer.** *Where is the certificate weakest?* The 77
checks split into 59 exact and 18 controls, but the exact checks are not
uniformly deep: `D1`–`D6`, `P1`–`P6`, `G1`–`G4` are genuine computations, while
`X1`, `X2`, `R1`–`R6` are substring lookups that verify *what another artifact
said*, not that it was right. The substring layer is deliberately shallow — its
job is provenance, not adjudication — but a reader should not count 77 as 77
theorems. **Stated, not hidden.**

**Lens Q2 — configuration manager.** *Is the base revision honest?* `v0.258` is
the highest ledger present; both target rows are byte-identical across all 258
versions; no `la7-*` or `joe_directed_ledger_sm7_*` artifact pre-existed. The
checkout is shared with concurrent writers, so **only** two paths are written:
this file and the probe. No git, no session-sync, no ledger, no canon, no
`CURRENT-STATE`. If a concurrent writer advances the ledger past `v0.258`, the
delta remains valid against its declared base `a148ed80` and the probe will fail
loudly on the missing file rather than silently reading a different one.

**Lens Q3 — comparator-routing officer.** *Is the Standard Model being used
illegally?* The SM appears at node N3 as a **rank comparator for a counting
invariant**, and the routing method's four recurring forks (family index /
chirality, Higgs-VEV, VEV-only breaking, Majorana-anomaly diagnostics) are all
absent — none of them is a theta-sector question. The one boundary risk is the
temptation in §4.1, which is refused there. No bridge is claimed and none is
needed, because **no failure condition is transported**: the artifact does not
say the SM's theta structure constrains GU's, only that the two groups' ranks are
different integers under one invariant and equal under another.

**Lens Q4 — FMEA / failure-mode analyst.** *Rank the ways this is wrong.*
(1) The `Spin(3,2)` reading is correct — deficit collapses to 0, finding dies.
Likelihood low, impact total. (2) `H^4(BG;Q)` is the only right invariant —
the `3 vs 3` reading wins, the chain-level surplus is 0, but **the booking is
still short by 2 under every node**, so the primary claim survives; impact
partial and already priced into the bracket. (3) The T-ladder grade is contested
down to T1 — the computation stands, only the label moves. (4) `Delta5` is a
misreading of the source and the internal group is data — kills the node table's
first row; this is `GRANT-LA7-DELTA5` with its falsifier named. **No failure mode
reaches the LT-SM1 split**, which depends on none of the topology.

**Lens Q5 — requirements engineer.** *Is the proposed `distance` actually
dischargeable, or does it presuppose its answer?* The old `distance` — "identify
the QCD theta coefficient" — presupposes there is one coefficient, which §1.6
shows is false under every reading. The new one names two ordered obligations
(pin `r`, then supply `r` angles) and the first is discharged by an object that
already exists in the source's own declaration (the reduction chain), not by an
unbuilt construction. That is a strictly better-posed requirement. It is also
still a `NEEDS`: nothing here supplies either half.

---

## 5. CLAIM CEILING AND FENCES

### 5.1 What is claimed, at what ceiling

| # | claim | ceiling |
|---|---|---|
| 1 | `rank pi_3` and `rank H^4(BG;Q)` at four declared nodes, as tabled in §1.3 | **EXACT** (77/77, integer/Fraction, controls with power) |
| 2 | `so(6) = su(4)` and `so(4) = su(2)+su(2)` as Cartan-matrix isomorphisms | **EXACT, derived here** |
| 3 | Over all six admissible readings the sector rank is in `{2,3}`, so `LT-SM7`'s rank-1 booking is short by 1 to 2 | **EXACT**, conditional on claim 4 |
| 4 | The chain's middle node is `SU(3,2)` | **SOURCE-CONSISTENCY SELECTION**, not a re-transcription |
| 5 | No finite-order topological class supplies a general point of the sector; `T_9` alone is excluded | **EXACT** (cardinality), conditional on CB-B's `Z/2` typing |
| 6 | `LT-SM7` should migrate `T0_OPEN -> T2_...` at unchanged verdict and reason_kind | **PROPOSED DELTA**, `pending_integration` |
| 7 | `LT-SM1` should split, on two independent routes | **PROPOSED DELTA**, `pending_integration`; the split is banked, the second atom's kind is contested |
| 8 | `LT-SM7`/`LT-SM1` byte-identical across 258 ledger versions; the tightness meter has no T0/T1 bucket | **EXACT** (full-corpus sweep, positive control) |

### 5.2 Every fence, restated

1. **LA-6 fence 1 — the second reduction step is not computed.** Held. Only
   ranks *at* declared nodes are computed. No statement is made about the induced
   map, its Dynkin index, which generator survives, or where in the reduction a
   rank is lost. This is precisely what blocks T3.
2. **LA-6 fence 2 — physicality is not claimed.** Held. No angle is claimed
   observable. No statement about `theta-bar`, the `10^-10` bound, strong CP, or
   axions. §4.2 records the physical-count argument as a *contrary reading* and
   explicitly declines to compute it.
3. **`CB-B`'s standing `INHERITS` posture on `theta_QCD`** — that `theta_QCD` is
   not forced in GU and the reflection-anomaly descent fix is unbuilt
   (`explorations/tension-ledger-successful-theories-2026-07-21.md:165`, quoted at
   `cb-b-lagrangian-terms-2026-08-05.md:1053`) — is **unchanged**.
   Nothing here forces a theta value in either direction.
4. **`CB-B`'s `REFEREE_CONJECTURE` on `T_9`** is neither promoted nor retired.
   §1.7 is orthogonal to it: `CB-B` says the descent map is unbuilt; LA-7 says
   the counting fails even if it is built.
5. **No laundering.** No verdict changes. No `reason_kind` moves toward
   dischargeability. The only `reason_kind` proposed anywhere (`LT-SM1b` at
   `MISSING_CONSTRUCTION`) moves away from it.
6. **No ledger edit, no canon edit, no `CURRENT-STATE` edit, no git operation.**
   Two files written: this delta and its probe.
7. **Comparator routing.** The Standard Model is a rank comparator only. No
   failure condition is transported in either direction.

### 5.3 Reproduce

```text
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ledger_sm7_topological_rank.py
# expect: CERTIFICATE: 77/77, exit 0
```

---
artifact_type: exploration
status: exploration
doc_type: gate
created: 2026-08-17
work_item: CT-4
channel: ct_hardening
route: CONSTRUCT_AN_INVARIANT_AND_MEASURE_WHETHER_IT_EARNS_THE_WORD
base_ledger: lab/process/conditional-physics-ledger-v0.259.json
ledger_edit: none -- this artifact does not touch the ledger
delta_kind: PROCESS_GATE_PLUS_MEASUREMENT__NOT_A_LEDGER_EDIT
target_claim: NONE-NOT-A-KILL
internal_target_claim: >-
  LA-CHANNEL-INDEX-2026-08-15-LEDGER-WIDE-RESULT, retired in its
  presentation-independent reading only. Operative sentence, quoted:
  "82 rows resolve to 32 formal degrees of freedom (13 + 7 + 12)"
  (lab/active-research/joe-directed/ledger-advancement/README.md,
  "Ledger-wide result"). LA-10 already WEAKENED this to vocabulary-relative;
  CT-4 shows the weakening is not repairable by moving to a graph invariant,
  because no connectivity statistic of a declared diagram is unconditionally
  refinement-invariant either. This is an INTERNAL channel claim about the
  ledger. It is not a canon claim, not a source claim, and not a GU physics
  claim; Weinstein never asserted it and nothing here bears on him.
internal_target_verdict: >-
  RETIRED IN ITS UNCONDITIONAL READING. What replaces it is not a better
  number but a number PLUS a decidable certificate: (C, beta, component
  row-size distribution) together with a NON-SEVERING certificate against a
  named refinement. Without the certificate the invariant is exactly as
  presentation-dependent as 32 was.
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
title: >-
  CT-4: the dependency-diagram invariant exists, it is CONDITIONAL, and the
  condition is the whole result. On ledger v0.259's declared edge set the
  diagram is R=84, E=136, A=35, C=35 (7 linked components with row sizes
  24/19/6/4/1/1/1 plus 28 isolated rows), b1=52 and beta = E-R+C = 87. Under
  LA-10's four-way refinement of `A_ACTION_OWNED_BACKGROUND`, completed by
  LA-10's own conservative principle, the atom count rises by 3 -- exactly the
  12->15 move that produced 32->35 -- while C, beta and the component row-size
  distribution are EQUAL, and the naive cycle rank b1 falls by exactly 3. So
  the measured 32->35 instability is worth 0 in the invariant and -3 in b1,
  which is why b1 is rejected. But there is a NO-GO: for any diagram with an
  atom of degree >= 2 a LEGAL refinement exists that raises C (demonstrated:
  35 -> 38), so no connectivity statistic is unconditionally
  refinement-invariant; the unconditional invariants are the row-side data
  (R, E, row-degree multiset) and they measure how much text there is, not how
  entangled it is. And the honest price: the declared-versus-disputed edge
  spread is C 35->24 and beta 87->122, an order of magnitude larger than the
  vocabulary instability the invariant repairs. 136 declared edges, 46
  known-disputed (20 grade-only + 26 uncited), plus LA-4's 1 uncited
  atom-atom precedence edge which moves its own reach statistic 2/29 -> 28/29
  and moves beta by 1 in 87.
grade: >-
  EXACT integer arithmetic; every quantity is a count. No float is constructed
  anywhere; assert_no_float sweeps the whole result dict. 52/52 checks, exit 0,
  via tests/channel-swings/joe_directed_ct4_dependency_diagram_invariant.py;
  66/66 well-formedness checks, exit 0, via
  process_gates/dependency_diagram_invariant_audit.py. Certificate splits as
  25 [E] exact results, 17 [C] controls that must fire, and 10 [R]
  reproductions of already-filed LA-4 / LA-5 / LA-6 / LA-10 / LA-11 facts, all
  reproduced exactly BEFORE being extended. FAILURE PATH EXERCISED: 11 probe
  mutations and 12 gate mutations, each required to drive a GENUINE [FAIL]
  line; a nonzero exit without one is rejected as CRASH-NOT-DETECTION, and
  both harnesses verify their CLEAN BASELINE before any mutation runs.
  Poison-baseline and inert-mutation controls both confirmed to exit 1. NOT:
  a ledger edit, a verdict change, a reason-kind change, a physics derivation,
  a coefficient, a selection principle, a claim-status movement, a count of
  independent problems, or any statement that a GU object exists.
disposition: >-
  INVARIANT_BUILT_AND_TYPED_CONDITIONAL__ACCEPTANCE_TEST_PASSES_ON_THE_MEASURED
  _REFINEMENT__b1_REJECTED_BY_IDENTITY__NO_GO_ON_UNCONDITIONAL_CONNECTIVITY_
  INVARIANCE__EDGE_SET_SPREAD_DOMINATES_VOCABULARY_SPREAD_BY_AN_ORDER_OF_
  MAGNITUDE__136_DECLARED_46_DISPUTED__ONE_CONTESTED_EDGE_LT_GR4_CARRIES_THE
  _ENTIRE_RESIDUAL_INSTABILITY
rows_touched_structurally: []
rows_advanced: 0
rows_escalated: []
depends_on:
  - lab/process/conditional-physics-ledger-v0.259.json
  - lab/process/conditional-physics-ledger-v0.258.json
  - lab/active-research/joe-directed/ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la6-the-lagrangian-axis-has-twelve-degrees-of-freedom-and-one-constructible-cover-object-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la10-the-cut-vertex-survives-and-is-not-the-second-action-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md
  - VERIFICATION.md
scripts:
  - tests/channel-swings/joe_directed_ct4_dependency_diagram_invariant.py
  - process_gates/dependency_diagram_invariant_audit.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact's object is
> the **ledger**, not the physics. Every number below is a property of a
> declared vocabulary over v0.259 prose plus a mechanical substring rule.
> Nothing here is evidence for or against Weinstein's source-native mechanism,
> and nothing here binds any conventional comparator. Rows that border
> comparators are touched only in their graph position; their comparator status
> is untouched. Routing method:
> `lab/methods/source-native-comparator-routing.md`.
> Classification: **`INTERNAL_STRUCTURAL_ONLY`.**

# CT-4 — the invariant is real, and it is conditional; the condition is the result

## Verdict first, unsoftened

The brief asked for a number stable under vocabulary refinement, and set the
measured 32 → 35 instability as the acceptance test. Three answers, in
descending order of comfort.

| question | answer |
|---|---|
| Does a number exist that is EQUAL under both LA-4/6's vocabulary and LA-10's split? | **Yes.** `C = 35`, `beta = 87`, component row-size distribution `(24,19,6,4,1×31)` — all equal, while the atom count rises by exactly 3, which is the `12 → 15` move that produced `32 → 35` |
| Is the obvious candidate — the cycle rank `b1` — that number? | **No, and provably not.** `b1` falls 52 → 49, by *exactly* the number of new atoms. Identity `db1 = dE − dA + dC` is checked on every variant. `b1` is as presentation-dependent as the generator count it would replace |
| Is `(C, beta, rowdist)` UNCONDITIONALLY refinement-invariant? | **No.** A LEGAL refinement of the same diagram raises `C` 35 → 38. The unconditional refinement-invariants are exactly `R`, `E` and the row-degree multiset — and those measure how much text there is, not how entangled it is |

So the deliverable is not a number. It is a **number plus a decidable
certificate**: the invariant, and a NON-SEVERING certificate naming the
refinement it is invariant *under*. That certificate is precisely what "32"
never carried, and it is the entire difference between the two.

And the honest price, quantified rather than gestured at: the **edge-set**
spread on the same diagram is `C 35 → 24` and `beta 87 → 122`. The dispute
about *which edges are real* is an order of magnitude larger than the dispute
about *what the atoms are called*, which is the one the invariant repairs.

---

## 0. PREFLIGHT — six specialist lenses, run inline

### Lens P1 — retrieval before work: does an invariant computation already exist?

**Yes, partially, and it is reproduced before being extended.** LA-6's probe
(`la6-lagrangian-effective-dof.py:311`) already computes `bipartite
components` on the LAGRANGIAN axis and reports `[(20, 13), (1, 0)]` — one
20-row component plus the zero-atom row `LT-GR2a`. That is banked and is
**not** re-presented here as new. What did not exist anywhere: a cycle rank, a
component size distribution, a whole-ledger diagram, any statement of what
survives refinement, and any certificate. LA-4 computes reach through a
declared DAG, not components. LA-5 computes rank, signature classes and a
Pareto frontier, not connectivity. LA-10 computes rank, minimum cover and a
dual witness under the split; its `components` line is LA-6's, re-run.

Ten facts are reproduced `[R]` before any extension: the v0.259 denominator,
the three axis edge counts (76 / 77 / 27), LA-10's `20 of 77` uncertified
edges, LA-10's `b9` naming rows, LA-10's 15-of-18 partial split map and its
four constituent names, LA-11's demand-field rule, and LA-4's uncited
precedence edge.

### Lens P2 — graph theory: which statistics *can* be refinement-invariant?

A refinement splits atom `a` into `a_1 … a_k`, each incidence of `a` going to
exactly one constituent. Write `R`, `A`, `E`, `C` for row-vertices,
atom-vertices, edges and components.

- `b1 = E − (R + A) + C`. Under refinement `E` and `R` are fixed and `A` rises
  by `k − 1`, so `db1 = dC − (k − 1)`.
- **`b1` is invariant iff every split totally severs.** `C` is invariant iff no
  split severs at all. **These cannot both hold for a nontrivial refinement.**
  Any brief that asks for both is asking for a contradiction, and this one did;
  the resolution is below.
- The repair is `beta := E − R + C = b1 + A`. It is the number of declared
  incidences in excess of a row-spanning forest — the **declared-demand
  redundancy** — and it is invariant exactly when `C` is.

So the candidate invariant is `(C, beta, component row-size distribution)`,
with `b1` reported and rejected.

### Lens P3 — measurement theory: what is the instrument actually measuring?

A generator count measures the *presentation*. A connectivity statistic
measures the *incidence relation*, which is one level less arbitrary — but only
one. The construct being estimated is "how coupled are these open items", and
the honest statement of construct validity is that `C` and `beta` estimate it
*up to* the non-severing class of refinements. Outside that class they do not,
and §4 exhibits the failure rather than hiding it.

### Lens P4 — evidence law: what is an edge, and who says so?

LA-11's rule, adopted verbatim and cited: a demand lives in `distance` or
`revival_trigger` — `DEMAND_FIELDS = ('distance', 'revival_trigger')`
(`tests/channel-swings/joe_directed_b9stat_row_construction.py:98`). An edge is
admitted iff its certificate substring occurs **verbatim** in the row's own
demand text in v0.259. A certificate that only occurs in `mapping_grade` /
`frontier_grade` / `summary` is a *status* token, not a demand, and is tiered
`GRADE_ONLY`. A certificate that occurs nowhere is `UNCITED`. This is the same
discipline LA-10 applied to LA-4's table, tightened from LA-10's wide text to
LA-11's demand-only text, and reported both ways.

### Lens P5 — software archaeology: the vocabularies were certified against v0.258

The brief targets v0.259. The ledger moved under the donor artifacts: `LT-SM1`
is now `SUPERSEDED` with successors `LT-SM1a`/`LT-SM1b`, `LT-GR6b` was minted
from LA-11, and `LT-SM7`'s `distance` and `revival_trigger` were both rewritten
by LA-7. Four of LA-6's inherited certificates therefore lapse. Rather than
paper over this, the extraction **inherits superseded rows' edges to their
declared successors** (via the ledger's own `split_from`) and re-certifies each
against the successor's own text. That is mechanical, and the lapses are
reported, not repaired by hand — §2.2.

### Lens P6 — gate design: what may a gate ratchet on?

Only well-formedness. A physics-adjacent number that becomes a compliance
target stops being a measurement. The gate therefore prints `C`, `beta` and the
distribution **every run and never checks them**, and ratchets only on
extraction reproducibility, tier-partition totality, the graph accounting
identities, and the honesty of each variant's declared type. There is a
unit test (`test_no_check_pins_the_invariants_value`) whose only job is to fail
if a future edit sneaks the invariant's value into the ratchet.

---

## 1. THE OBJECT

`D` = the bipartite **declared dependency diagram** over ledger v0.259:

- **row-vertices** — the 84 canonical targets (87 records minus 3 `SUPERSEDED`:
  `LT-GR2`, `AC-G1`, `LT-SM1`).
- **atom-vertices** — every open demand-object that at least one row
  *declares*. **A vocabulary term with zero declared incidences contributes no
  vertex.** This is LA-11's principle applied to the graph: reach is a DAG
  property, declaration is a text property.
- **edges** — 136 row→atom incidences admitted by the LA-11 rule above.

Three published vocabularies supply the edge assertions, inherited verbatim and
re-certified, never re-invented: LA-6's 76 LAGRANGIAN entries, LA-4's 77
REPRESENTATION entries under LA-10's per-atom token families, LA-5's 27 ANOMALY
entries under its own `BACKING` substrings. 180 assertions, 182 after successor
inheritance.

**Atom-atom precedence edges are not in `D` at all.** LA-4's DAG (`b9 ≺ b1`
etc.) is a different relation from row-atom incidence, and mixing the two in one
graph is a type error. The one edge LA-4 concedes no row states is therefore
outside the diagram *by construction*, and is priced separately in §4.4.

---

## 2. THE MEASUREMENT

### 2.1 The invariant, both edge sets

```text
                                      declared    declared+disputed
  row-vertices  R                           84            84
  edges  E                                 136           182
  atom-vertices  A                          35            36
  components  C                             35            24
    of which linked                          7             5
    of which isolated rows                  28            19
  cycle rank  b1 = E-(R+A)+C                52            86
  REDUCED CYCLE RANK  beta = E-R+C          87           122
  component row sizes (linked)  (24,19,6,4,1,1,1)   (29,21,13,1,1)
```

Two structural facts worth stating plainly:

- **No declared edge crosses an axis.** The three linked components of size
  24 / 19 / 6+4+1+1+1 are exactly REPRESENTATION / LAGRANGIAN / ANOMALY. This is
  *not* evidence that the axes are independent: it is a consequence of three
  separately declared lexicons never using a shared atom name. It is the
  strongest available statement of LA-10's §4.1 objection — `32 = 13 + 12 + 7`
  is a sum over three vocabularies whose *names* overlap while their *declared
  edges* do not touch, so the sum is licensed by a block structure that is an
  artifact of the writing, not of the ledger.
- **28 of 84 targets are isolated** in the declared diagram: their demand text
  names no atom of any of the three vocabularies. That number is exactly
  refinement-invariant (degree zero stays degree zero) and is one of the few
  honest things this diagram says without a certificate.

### 2.2 Declared versus disputed, and what lapsed

```text
  inherited edge assertions              180   (LA-6 76 + LA-4 77 + LA-5 27)
  after successor inheritance            182
    DECLARED                             136   (LT 59 · RA 55 · AC 22)
    GRADE_ONLY                            20
    UNCITED                               26
  KNOWN-DISPUTED = GRADE_ONLY + UNCITED   46
  uncited ATOM-ATOM precedence             1   (LA-4's `b9 < b1`)
```

The 20 `GRADE_ONLY` edges are certificates that live in a status field, not a
demand field. Fourteen are LAGRANGIAN, four ANOMALY, two REPRESENTATION. **Two
of LA-10's three polarity-inverted incidences are among them** — `LT-GR2b`/`A`
(`LOCAL_ACTION_OWNED_VEV_EXACT_UNREDUCED`) and `LT-GR5`/`A`
(`P_EQUALS_KT_ACTION_OWNER_REJECTED`). LA-10 rejected those on *denotation*
(an `EXACT`/`REJECTED` marker cannot witness an open demand); the LA-11 rule
rejects them on *location* (a status token is not a demand). Two independent
mechanical rules agreeing on the same two edges is a genuine convergence and is
recorded as one. **The third — `LT-GR4`/`A` — is exactly where they disagree,
and that single edge is §3.1.**

The 26 `UNCITED` edges are 20 REPRESENTATION (LA-10's finding, reproduced
exactly), 5 LAGRANGIAN and 1 ANOMALY. **The 5 LAGRANGIAN lapses are new and are
caused by the ledger's own v0.259 migration**, not by any judgement here:
`LT-SM7`'s two certificates died when LA-7 rewrote both its demand fields, and
`LT-SM1a`/`LT-SM1b` inherit certificates that no longer match their own
rewritten text. That is the version-sensitivity of substring certification,
made visible rather than smoothed away.

---

## 3. THE ACCEPTANCE TEST — the 32 → 35 instability, re-run

### 3.1 LA-10's split is PARTIAL, and a partial map is not a refinement

LA-10 assigns 15 of `A`'s 18 v0.258 incidences to four constituents and
**deletes** the other three on its polarity test. That is a refinement
*composed with* an edge deletion. Under the LA-11 demand-field rule two of the
three deleted incidences are `GRADE_ONLY` anyway (so they never enter `D`), but
one — `LT-GR4 → A`, certificate *"an exact GU-native sign opposite to the
ported negative horn"* — **is** in `LT-GR4`'s demand field and is therefore
DECLARED. It is a genuinely contested edge: contested between two mechanical
rules, LA-11's location test (admit) and LA-10's denotation test (reject).

Three total completions are computed, each typed:

```text
                                       declared edge set            decl+disputed
(a) residue -> its own atom    REFINEMENT   C 35->36  beta 87->88   C 24->24  beta 122->122
(b) residue -> A_OWN           REFINEMENT   C 35->35  beta 87->87   C 24->24  beta 122->122
(c) LA-10 as published    EDGE_SET_CHANGE   C 35->36  E 136->135    C 24->25  E 182->179
```

Completion **(b)** is LA-10's own stated principle — *"ambiguous rows are
assigned conservatively, in the direction that keeps the A-cluster largest"* —
applied to the residue instead of deleting it. It is the acceptance test.

### 3.2 The acceptance test, passed

```text
  vocabulary               LA-4/6 published        LA-10 split (completion b)
  atom-vertices  A                     35                       38   (+3)
  components  C                        35                       35   EQUAL
  beta = E - R + C                     87                       87   EQUAL
  component row sizes    (24,19,6,4,1x31)         (24,19,6,4,1x31)   EQUAL
  R, E, row-degree multiset            —                        —    EQUAL (unconditional)
  cycle rank  b1                       52                       49   MOVED (-3)
```

The `+3` in the atom count is exactly LA-10's LAGRANGIAN rank `12 → 15` and
exactly the ledger-wide `32 → 35`. **The instability the brief set as the
acceptance test is worth 0 in `(C, beta, rowdist)` and −3 in `b1`.** The same
equality holds with the disputed edges included (`C 24 = 24`, `beta 122 = 122`).

### 3.3 How conditional is that equality?

All 42 single re-assignments of a declared `A`-row to a different constituent
were swept. **39 of 42 preserve the invariant.** All three movers are the same
one: `LT-SM6` leaving `A_ID`, which strands `LT-SM1a` on `I_ZETA_F_BIT`, an atom
of degree 1. That is the general mechanism — **severing happens exactly at rows
whose remaining atoms are all private** — and the gate prints the 15
severing-vulnerable rows every run: `AC-A2, AC-A3, AC-B2, AC-F1, AC-F3, AC-F5,
LT-GR4, LT-GR7, LT-SM1a, RA-A3, RA-B6, RA-E2, RA-F2, RA-F3, RA-G2`.

---

## 4. THE CONTRARY CONTROLS, AND THE NO-GO

### 4.1 CC-B(i) — a real edge-set change moves it

The ledger's own migration, **vocabulary held fixed**:

```text
  v0.258   R 82   E 140   A 36   C 31   beta 89
  v0.259   R 84   E 136   A 35   C 35   beta 87
```

Moved. The machinery is not inert.

### 4.2 CC-B(ii) — LA-10 as published is flagged as not-a-refinement

Deleting the residue changes `E` 136 → 135 and `C` 35 → 36. The legality check
reports `is_refinement = False`. **The gate distinguishes a refinement from an
edge dispute automatically**, on the actual published object, without being told
which is which.

### 4.3 CC-B(iii) — THE NO-GO: a legal refinement that still moves it

Split `A_ACTION_OWNED_BACKGROUND` into one private constituent per incident row.
This is a *legal* refinement — total, row-injective, `E` and the row-degree
multiset preserved — and it takes `C` 35 → 38, `beta` 87 → 90. The construction
works on any atom of degree ≥ 2. Therefore:

> **No connectivity statistic of a declared dependency diagram is
> unconditionally invariant under vocabulary refinement.** The unconditional
> refinement-invariants are exactly `R`, `E` and the row-degree multiset.

The non-severing certificate correctly reports the severing here rather than
hiding it, which is the control that the certificate has power.

### 4.4 CC-B(iv) — pricing the one edge that carried LA-4's headline

LA-4's `b9 ≺ b1`, the edge no row states:

```text
  LA-4's reach statistic     2/29  ->  28/29     (the entire headline)
  components  C                35  ->  35        (unchanged)
  beta                         87  ->  88        (+1 in 87)
```

This is the strongest argument in the artifact *for* a diagram invariant over a
reach number: one uncited edge swings reach from near-nothing to near-everything
and moves the invariant by one unit in eighty-seven. It is also the strongest
argument against over-trusting the invariant, because that same edge is the
reason nobody knows what the ledger's real dependency structure is.

---

## 5. THE CAVEAT, QUANTIFIED — and it is worse than the thing it fixes

```text
  declared -> declared+disputed
    C                        35 -> 24     (-11)
    beta                     87 -> 122    (+35)
    b1                       52 -> 86     (+34)
    E                       136 -> 182    (+46)
    linked components          7 -> 5     (-2)
    largest component rows    24 -> 29    (+5)
```

Set that beside what the invariant buys: the whole `32 → 35` vocabulary
instability is 0 in `(C, beta, rowdist)`, and the presentation count's own move
was 3. **The edge-set spread is 35 in `beta` — more than ten times the
instability the invariant removes.**

The invariant answers *"how entangled is what the rows SAY"*. It does not
answer *"which edges are real"*, and on this corpus the second question is where
almost all the uncertainty lives.

---

## 6. POSTFLIGHT — five lenses, including on this gate

### Lens Q1 — the strongest overclaim available here, refused

*"CT-4 supplies the vocabulary-independent number the ledger needed; the answer
is 87."* **Refused on my own numbers.** §4.3 is a legal refinement that moves it.
`87` is invariant under a *class* of refinements, and the class membership is a
computed certificate, not a property of the number. Quoting `beta = 87` without
the certificate reproduces the exact error that made `32` quotable.

Second available inflation: *"seven linked components means seven independent
sub-programs."* Refused. Components are separated by the *absence of a shared
declared atom name*, and §2.1 shows the axis separation is a writing artifact.
Absence of a declared edge is not evidence of independence.

### Lens Q2 — the strongest contrary reading, which I cannot refute

**A reader can say the whole exercise smuggles the lexicon into the edge
extraction and calls the result an invariant.** The steelman is exact: the atom
*names* no longer matter, but the *certificate strings* do, and those strings
were chosen by LA-4, LA-5, LA-6 and LA-10 by hand. Change the certificate for
one edge and the edge changes tier; §2.2 shows the ledger did exactly that to
five edges in one version bump, without anyone deciding to. So the invariance is
invariance under *renaming the atoms*, which is a narrower freedom than
"vocabulary refinement" sounds like, and the residual freedom — which strings
count as certificates — is unbounded and unmeasured here.

I cannot refute this and will not pretend to. What I can say is that the
extraction rule is mechanical, stated, and re-verified every run, so the
residual freedom is *auditable* in a way "32" was not; and that the disputed
spread in §5 is a lower bound on how much that freedom is worth.

### Lens Q3 — the weakest seam of this gate

**The `LT-GR4 → A` edge.** One contested edge carries the entire difference
between completion (a) (severs, `C` 35 → 36) and completion (b) (`C` 35 = 35).
Two mechanical rules disagree about it — LA-11's location test admits it,
LA-10's denotation test rejects it — and I did not adjudicate between them; I
computed both and reported both. A reader who takes LA-10's rule as primary gets
`C 35 → 36` and a residual instability of 1, not 0. That is a real weakening of
the headline and it is stated as one.

Second seam: the 20 `GRADE_ONLY` REPRESENTATION-side and 26 `UNCITED` edges are
tiered but not adjudicated. The spread in §5 is a range, not an error bar; no
distribution over the disputed edges is claimed or implied.

Third seam: LA-5's ANOMALY incidence includes entries whose donor justification
is a CB-C row verdict rather than a ledger quote. Those tier as they tier; one
(`AC-A1 → U1`) is `UNCITED` on v0.259 because the row's demand text was rewritten
by LA-2's conditional settlement. I did not repair it.

### Lens Q4 — what a hostile reader should attack next

Not the graph theory — the identities are checked numerically on every variant
and the union-find is cross-checked against an independent BFS. Attack the
**certificate strings**, in groups. Specifically: take the 14 LAGRANGIAN
`GRADE_ONLY` edges and argue that a status token *is* a demand when the status is
`_OPEN`; that promotes `LT-GR1/A`, `LT-GR2c/H`, `LT-GR2d/C`, `LT-GR3/D`,
`LT-GR5/D` and `LT-SM4/H` into `D` and changes every number in §2.1. I did not run that variant
because `_OPEN`-suffix parsing is a new rule, not an inherited one, and this gate
inherits rules rather than inventing them. That is a real gap and it is the
cheapest attack available.

### Lens Q5 — decision usefulness

One concrete instruction, and it is small and cheap. `LT-GR4`'s
`A_ACTION_OWNED_BACKGROUND` incidence is the single contested edge carrying the
whole residual instability, and its certificate — *"an exact GU-native sign
opposite to the ported negative horn"* — names **no** action-family object while
sitting in a demand field. One editorial sentence in `LT-GR4`'s `distance`,
either naming the action object it waits on or dropping the clause, resolves it
in both rules at once and takes the residual vocabulary instability of this
diagram to exactly zero. That is a one-row edit with a measurable effect, which
is more than most of this channel's findings can offer.

---

## 7. WHAT MAY AND MAY NOT BE QUOTED

**The stable number is:** on ledger v0.259's DECLARED edge set, the dependency
diagram has `R = 84`, `E = 136`, `A = 35`, `C = 35` (7 linked components with
row sizes 24 / 19 / 6 / 4 / 1 / 1 / 1, plus 28 isolated rows) and
`beta = E − R + C = 87`; and `(C, beta, component row-size distribution)` is
EQUAL under LA-4/6's vocabulary and LA-10's refinement, **carrying a verified
non-severing certificate**.

**It may NOT be quoted as:**

- a count of degrees of freedom, of independent problems, of handles, or of
  anything the ledger "reduces to";
- a vocabulary-independent number full stop — §4.3 exhibits a legal refinement
  that moves it, and the certificate is not optional decoration;
- a statement that the three axes are independent, or that the ledger is or is
  not one construction;
- evidence about Geometric Unity, about Weinstein's mechanism, or about any
  comparator. Nothing here touches the physics;
- a compliance target. The gate deliberately does not check these values and
  carries a unit test whose only job is to keep it that way.

**Not laundered:** no grant becomes a derivation; no row gains or loses a
condition; zero rows advance; the sequential ledger is untouched.

```gu-typed-objects
result: the dependency-diagram invariant (C, beta = E-R+C, component row-size distribution) and its non-severing certificate, over conditional-physics-ledger v0.259
carrier: the bipartite DECLARED dependency diagram D = (84 canonical target row-vertices) union (35 declared demand-atom-vertices), 136 edges, LAYER=UNTYPED (a document-structure object over ledger prose, not a geometric stratum; no bridge to any layer is asserted or needed), CHIRALITY=N/A
# a graph carries no form: the only structure used is incidence, and no
# bilinear or sesquilinear object appears anywhere in this artifact
pairing: NONE
real_structure: N/A
grading: Z/2 bipartition grading, row-vertices versus atom-vertices; every edge is odd for this grading and no edge joins two vertices of the same parity
action_owner: repository-construction -- the edge assertions are inherited from LA-4 / LA-5 / LA-6 / LA-10 and re-certified by this gate; no source action, observer or comparator owns any object here
target: the integer triple (C, beta, row-size distribution) in Z x Z x (finite multiset of Z), MAP-TYPE=evaluation
```

---

## 8. REPRODUCE

```bash
cd /path/to/gu-formalization
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ct4_dependency_diagram_invariant.py
_local/cas-venv/bin/python process_gates/dependency_diagram_invariant_audit.py
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ct4_dependency_diagram_invariant.py --selftest
_local/cas-venv/bin/python process_gates/dependency_diagram_invariant_audit.py --selftest
```

Expected, exit 0 for each:

```text
CERTIFICATE: 52/52 checks pass; no load-bearing float (swept).
  by class: {'C': '17/17', 'E': '25/25', 'R': '10/10'}
WELL-FORMEDNESS: 66/66 checks pass; exit 0 iff all pass.
SELFTEST: 11/11 mutations produced a GENUINE failing check; crash-catches are rejected.
SELFTEST: 12/12 mutations produced a GENUINE failing check; crash-catches are rejected.
```

`--poison-baseline` on the gate's selftest corrupts the clean set and must
print `CLEAN BASELINE IS RED ... ABORT RED` and exit 1; an inert mutation must
be reported `MISSED` and exit 1. Both were confirmed at ship time.

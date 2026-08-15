---
title: "CH-3: the impossible nested chain is repaired at three sites; two conclusions never used it, one fence did and was wrong; and the correct object was already in the repository in two other notations the whole time"
created: "2026-08-15"
doc_type: attribution-correction-and-independent-reproduction
status: repaired
result: "SC-A's group theory REPRODUCES independently (58/58, exit 0, no shared code): dim so(3,2) = 10 < 12, every so(p,q) with p+q = 5 is 10-dimensional, max centraliser of any Spin(3,2) in Spin(6,4) is 10, and both arrows of Spin(6,4) > SU(3,2) > S(U(3)xU(2)) construct (24 <= 45, 12 <= 24). Three sites repaired. H19 Q3b and Q4b did NOT use the nesting -- both are load-bearing on the (6,4) fibre, and Q4b's neutrality argument comes out TIGHTER under the corrected reading. LA-6's fence (i) DID use it and was wrong in content, not only in notation: it put the rank drop in the second step, and the second arrow is a maximal-compact retract that cannot change pi_3. rank pi_3 along the chain is 3 -> 2 -> 2; the drop is at arrow 1."
target_claim: "internal: the repository-written chain `Spin(6,4) -> Spin(3,2) -> maximal compact SU(3) x SU(2) x U(1)` as ASSERTED (not as quoted) at explorations/wave14/H19-seven-seven-signature-branch-2026-07-11.md:114, :150, :157 (with the derived three-signature list at :120 and :163), and at la6-the-lagrangian-axis-...-2026-08-15.md:918"
target_claim_verdict: "KILLED AS WRITTEN and now REPAIRED IN PLACE at both files. No source claim is killed -- the source's own adjacent sentence says SU(3,2), twice. No repository RESULT is killed either: two of the three sites cite the chain in passing and their verdicts stand verbatim; the third is a fence whose content was wrong and is now corrected with its consequence named."
test: tests/channel-swings/joe_directed_ch3_chain_repair.py
certificate: "58/58 exact checks, 5 planted controls (0 misbehaved), exit 0; --selftest: 6 planted false facts each force exit 1 and the clean run exits 0"
supersedes_nothing: true
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator: the Georgi-Glashow chain
> `Spin(10) > SU(5) > G_SM` appears as the contrast class the source is
> refusing, and `SU(3)xSU(2)xU(1)` appears as a target algebra. Any result about
> those binds only the named model and is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers. Classification: `SOURCE_NATIVE_ROUTE`.

`SOURCE_NATIVE_ROUTE` is the honest value because the object under test is the
source's own sentence and the source's own reduction operation, and the
artifact's headline is that the source **refuses** the GUT comparator outright:
*"There is no grand unification. It's just a normal bundle in your ambient
space."* This artifact adjudicates a **repository attribution**, not a physics
claim, in either direction.

> [!IMPORTANT]
> **Registry consequence, measured rather than assumed.**
> `doc_type: attribution-correction-and-independent-reproduction` is honest and
> is not one of the two types (`overview`, `stewardship_record`) that leave
> `process_gates/source_native_comparator_routing_audit.py`'s derived scope, so
> this file enters that scope. I may not edit
> `lab/process/source-native-comparator-routing-registry.json`.
>
> **Measured, 2026-08-15, before and after — both runs, not one.** Before this
> file the gate was **GREEN at exactly its baseline**: 62 in derived scope, 53
> registered, 9 unclassified against `UNCLASSIFIED_BASELINE = 9`. (SC-A's own
> note recorded 10 -> 11 earlier today; the registry owner has since worked that
> backlog, so SC-A and ITC are registered and the count had returned to 9.)
> After this file: **64 in derived scope, 54 registered, 10 UNCLASSIFIED,
> `FAILED (failures=1)`.**
>
> **The two deltas are not both mine, and the difference is measurable.** Scope
> grew by 2 and the registry by 1 while this artifact was being written — the
> checkout is shared with concurrent agents — so the honest attribution is:
> **this file is +1 to the unclassified count and is the file that turns a green
> gate red**, and it is named first in the gate's own printout. The remaining 9
> are the pre-existing baseline (CG-1, CC-1, MD-1, MC-1, LA-10, LA-11, OT-1,
> OT-2, PHI-2), owned elsewhere and enumerated in the gate's own comment block.
> The fix is one row:
> `{"path": "lab/active-research/joe-directed/chain-repair/ch3-the-nested-chain-is-repaired-at-three-sites-and-the-rank-drop-moves-to-arrow-one-2026-08-15.md",
> "classification": "SOURCE_NATIVE_ROUTE"}`.
>
> That is a worse consequence than SC-A's `+1 to an already-failing gate` — that
> gate was already red; this one was green — and it is stated in that form rather
> than softened. The classification is declared in-file above, which is what the
> *method* asks for; the *gate* wants a registry row, and the row is owed.
> Declaring `stewardship_record` or `overview` would have left the audit's scope
> entirely and hidden this by lying about what this file is.

---

# CH-3 — repairing the chain, and finding out what leaned on it

Joe-directed, 2026-08-15. Downstream of `SC-A`
(`lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md`,
85/85), which decided that the source's *"right chain"* is a chain of
structure-group reductions of the rank-10 normal bundle and not a nesting of GUT
subgroups. This artifact does three things: reproduces SC-A's group theory
independently before relying on it, repairs the three repository sites that
carry the impossible nested form, and traces what depended on it.

---

## 0. PREFLIGHT

### 0.1 Retrieval, run BEFORE the work

Not before a novelty sentence — before deciding what to compute and what to
write. The brief warned that *"the chain appears in at least two notations, which
is why it was missed."* That warning turned out to understate the situation, and
finding out how changed this artifact's downstream section.

| object searched (with alternative vocabularies and notations) | verdict | where |
|---|---|---|
| `Spin(3,2)`, `spin(3,2)`, `so(3,2)`, `\mathfrak{so}(3,2)`, `spin three comma two` | **PRESENT**, 155 hits across 21 files | the two transcripts, SC-A, LA-7, CG-1, ITC, H19, LA-6, 4 probes |
| the chain as an **asserted** arrow expression `(6,4) ... (3,2)` on one line | **6 loci in 2 files**: `H19:114, :120, :150, :157, :163` and `la6:918` | the repair targets |
| the same chain in the **coset notation** `O(6,4)/U(3,2)`, `SO(6,4)/U(3,2)`, `so(6,4) > u(3,2)` | **PRESENT AND CORRECT**, ~20 files including the **live** ledger `v0.258` (3 hits), `RESEARCH-STATUS.md:399`, `NEXT-STEPS.md:1206, :1571`, `VG-V3`, `VG-SD`, `VG-V5`, `rb4` | this is **arrow 1**, already built |
| the chain's nodes in a **third**, prose notation | **PRESENT AND CORRECT**: `rb4-observer-cartan-moving-family-2026-07-30.md:382` — *"use the `Spin(6,4)`, `SU(3,2)`, and compact-subgroup chains"* | 2026-07-30 |
| `Spin(6,4)/SU(3,2)` with the **correct** middle term | **PRESENT**, `NEXT-STEPS.md:7445`, inside the `REDUCTION_EXTERNAL` audit quote | — |
| `rank pi_3` at the three nodes | **PRESENT, dated today**: LA-7 §1.4 table and `tests/channel-swings/joe_directed_ledger_sm7_topological_rank.py` P1/P2/P3 give `3`, `2`, `2` | LA-7 owns these numbers |
| the **localisation** of the rank drop to a named arrow (`first arrow`, `second arrow`, `rank drop 3 to 2`) | **ABSENT** — 0 hits; LA-6:918 is the only statement and it names the *second* step | the one new sentence here |
| anything citing `H19` **for the chain** (27 citing files swept individually) | **ABSENT** — every citer cites H19 for the `(9,5)`/`(7,7)` signature under-determination | no downstream dependency |
| anything citing `LA-6` fence (i) or the rank drop | **ABSENT** — `LT-SM7`'s citers (OT-1, OT-2, LA-10, LA-2) cite the row's ownership/typing | no downstream dependency |
| `complex-structure reduction` as a named operation | **PRESENT**, and it is SC-A's, in its probe's result dict | cited, not re-claimed |

**The finding the retrieval produced, which reframed section 3.** The
repository has carried the **correct** first arrow continuously since
2026-07-06 — five days *before* H19 was written — under the name
`O(6,4)/U(3,2)`, the homogeneous space of compatible complex structures on the
rank-10 fibre (`VG-V3`, `VG-SD`, and from there into `RESEARCH-STATUS.md`,
`NEXT-STEPS.md` and every ledger version through the live `v0.258`). It has also
carried the correct **node list** since 2026-07-30 in `rb4`. So the impossible
form was never the repository's only account of this object; it was a third,
defective transcription running in parallel with two correct ones.

**Why that is exactly why nobody caught it.** Both live notations are slashes,
and they differ by one token: `O(6,4)/U(3,2)` — correct, the complex-structure
reduction — against `Spin(6,4)/Spin(3,2)` — impossible. A reader who knew the
coset object would read the H19 string as the same thing sloppily typed. That is
a notation-collision defect, not an inattention defect, and it is the reason a
`12 > 10` obstruction sat in `explorations/` for 35 days.

**What the retrieval demoted before a line was written.** (a) The three node
numbers `3, 2, 2` are LA-7's, computed this morning; I re-derive them by a
different invariant as a control, and claim only the *localisation*. (b) The
kill itself, the frame, and the constructed arrows are SC-A's; I reproduce, I do
not co-own. (c) "SM as maximal compact rather than symmetry breaking" is July
prior art typed `REDUCTION_EXTERNAL`, and is an **input** here.

### 0.2 Specialist lenses, run inline — six, problem-matched

**Lens 1 — reproduction methodology.** *What would make a reproduction worth
anything?* Only independence. Re-running SC-A's probe would certify nothing but
that the file is deterministic. So `joe_directed_ch3_chain_repair.py` imports
nothing from `joe_directed_sca_right_chain.py`, reads none of its output, and
rebuilds every algebra from its defining linear condition: `so(p,q)` as
`{X : X^T eta + eta X = 0}` with the basis exhibited and bracket-closure checked;
`su(p,q)` as `{eta Y : Y anti-Hermitian, tr = 0}` realified through
`R(A+iB) = [[A,-B],[B,A]]`; every dimension read off an exact rank, never a
formula. A dimension that agrees with SC-A's by construction would not be a
reproduction.

**Lens 2 — Lie theory and real forms.** *Where could a signature relabelling
hide?* Nowhere, and that must be swept rather than asserted: `dim so(p,q)`
depends only on `p+q`, so all six real forms with `p+q = 5` are computed and all
six come out 10, and the orthogonal ladder is computed for `n = 2..7` to show the
first algebra of dimension `>= 12` is `n = 6` at 15. The one genuine real-form
fact is that `SU(3,2) < Spin(6,4)` is the realification `U(p,q) < SO(2p,2q)`,
which is *built* here (every generator verified skew for `eta_{6,4}` after an
explicit permutation to standard order), not cited.

**Lens 3 — exhaustiveness auditor.** *How do you kill a factorisation reading
without merely failing to find one?* By bounding the centraliser over **all**
module structures, which requires complexification (`so(3,2) (x) C = so(5,C)`,
signature-blind) and a *computed* irrep list. The `C_2` dimensions come from the
Weyl formula `(a+1)(b+1)(a+2b+3)(a+b+2)/6` evaluated over `a,b in [0,13)` with the
`Fraction` denominator asserted to be 1 before casting, and the Frobenius-Schur
types from the central character `(-1)^a`. That is the single most attackable
step in the whole chain of reasoning and it is where the controls are densest.

**Lens 4 — repair typology.** *Do all three sites need the same repair?* No, and
conflating them would be the failure mode. A site whose **conclusion** rests on
the nesting needs its consequence marked; a site that **cites** the chain in
passing needs its attribution fixed and its verdict left alone; and a site that
merely **quotes** the source verbatim needs nothing at all, because a verbatim
quote of a garbled transcript is correct data. Section 2 types each site before
touching it, and the probe's `G.5` deliberately excludes quotation from the
"impossible form is gone" gate.

**Lens 5 — topology / homotopy.** *Is the rank-drop fence even a well-posed
statement?* `pi_3` of a connected Lie group equals `pi_3` of its maximal compact
because the group deformation-retracts onto it (Cartan-Iwasawa-Malcev). That
single fact makes the fence decidable: the chain's **second** arrow *is* a
maximal-compact reduction, so it is a retract, so it cannot move `pi_3` at all.
The fence's claim was therefore not merely mis-notated — it was locating a drop
at the one arrow where a drop is impossible.

**Lens 6 — epistemics of a favourable correction.** *Which way does this
correction cut?* Toward GU, in one narrow respect: it removes an impossibility
from the repository's account of the source. That is precisely the direction in
which an attribution repair is most likely to be over-sold, and the mitigation
has to be structural rather than a disclaimer at the end. So section 4 is written
**before** the hostile review, states the two places where something genuinely
got stronger, and states in each case what did *not* get stronger.

---

## 1. DOES SC-A'S GROUP THEORY REPRODUCE?

**Yes. Every load-bearing integer, from independent constructions.**
`tests/channel-swings/joe_directed_ch3_chain_repair.py`, 58/58 exact checks,
5 planted controls, exit 0. Exact integers and `fractions.Fraction` throughout;
`assert_no_float` sweeps the entire result structure.

### 1.1 Positive controls first, so the machinery has power

The exact congruence-signature routine is power-tested on `diag(1,-1)`, on the
**zero-diagonal hyperbolic pair** `[[0,1],[1,0]]` (the path that breaks naive
implementations), on a degenerate form, on a mixed form with a kernel, and on the
Killing forms of `so(3)` → `(0,3)` and `so(2,1)` → `(2,1)`. Every `so(p,q)`
generator used anywhere is verified to satisfy `X^T eta + eta X = 0`, and every
basis is verified to close under the bracket, before any dimension is read.

### 1.2 The two kills

```text
dim so(3,2)                        = 10     (explicit basis, bracket-closed)
dim(su(3) + su(2) + u(1))          = 12     (su(3) and su(2) built independently)
12 > 10                        ->  no injective homomorphism g_SM -> so(3,2)

sweep, p+q = 5:  so(0,5) so(1,4) so(2,3) so(3,2) so(4,1) so(5,0)  ->  all 10
ladder, so(n):   n = 2..7  ->  1, 3, 6, 10, 15, 21   ->  first >= 12 is n = 6
```

```text
irreps of so(5,C) = sp(4,C) of dim <= 10, from the Weyl formula:
    (0,0) 1  orthogonal | (1,0) 4  SYMPLECTIC | (0,1) 5  orthogonal | (2,0) 10 orthogonal
admissible module structures on C^10 carrying a nondegenerate invariant symmetric form:
    10        -> centraliser  0
    5 + 5     -> centraliser  1
    4^2 + 1^2 -> centraliser  4
    5 + 1^5   -> centraliser 10    <- the maximum
max centraliser of ANY Spin(3,2) in Spin(6,4) = 10  <  12 = dim g_SM
```

Both of SC-A's kills reproduce exactly. The Weyl formula is separately controlled
on `(1,1) -> 16` and `(0,2) -> 14`, values outside the enumeration window.

### 1.3 Controls, including one that must pass

- **Planted, must fail:** `dim so(3,2) >= 12`; the decomposition `5+4+1`
  admissible (odd multiplicity of the symplectic `4` degenerates the invariant
  symmetric form); `1^10` admissible (`so(5,C)` would act trivially and is not a
  subalgebra of `so(V)` at all); the `so(3,2)` block meeting the maximal compact
  in 12; and the generation check without `L_{45}` still reaching `so(6)`.
  All five behave.
- **Contrary control, must pass:** the same predicate **accepts** the `5 + 1^5`
  row at centraliser 10, and the artifact then exhibits it — two block-diagonal
  `so(3,2)` copies inside `so(6,4)`, each of dimension 10, verified to satisfy
  `X^T eta_{6,4} + eta_{6,4} X = 0` and verified to commute elementwise. The
  machinery therefore rejects `Spin(3,2) x G_SM` and accepts
  `Spin(3,2) x Spin(3,2)`, cases differing only in the second factor.

### 1.4 The surviving chain, rebuilt

```text
dim so(6,4)                                  = 45
dim su(3,2) / u(3,2)  (realified, injective) = 24 / 25   ->  ARROW 1, all generators skew
theta-fixed part of su(3,2)                  = 12 = 11 (su(3)+su(2)) + 1 (centre)
theta-fixed part of u(3,2)                   = 13        ->  eq (4.6)'s "up to a U(1)"
so(6)+so(4)  n  su(3,2)                      = 12
so(6)+so(4)  n   u(3,2)                      = 13
so(6)+so(4)  n  so(3,2) block                =  4        ->  the garble reading, short by 3x
Killing form of so(3,2): dim 10, signature (6,4)  -- and so(5,0) -> (0,10), so(4,1) -> (4,6)
```

`12 <= 24 <= 45`. SC-A's §1.5 and §1.6 numbers reproduce. One row of SC-A's §1.5
is reproduced with a stated reading rather than blindly: SC-A's
`so(6)+so(4) n so(3,2) = 4` does not say which embedding of `so(3,2)` it uses; I
take the block-diagonal one on 3 positive and 2 negative coordinates of
`R^{6,4}`, whose `theta`-fixed part is `so(3)+so(2)`, and get 4. If SC-A meant
the adjoint copy (its R5), that row is a different computation and I have not
reproduced it — it is a planted control there, not a load-bearing result, so
nothing here depends on the difference.

**Verdict: SC-A reproduces. The repairs below rely on it.**

### 1.5 One computation that is NOT SC-A's, needed by the LA-6 site

```text
rank pi_3(Spin(6,4))      = rank pi_3(Spin(6) x Spin(4))    = 1 + 2 = 3
rank pi_3(SU(3,2))        = rank pi_3(S(U(3) x U(2)))       = 2
rank pi_3(S(U(3)xU(2)))                                     = 2
```

Computed by a **different invariant from LA-7's**: the number of simple ideals of
a compact semisimple algebra equals the dimension of its space of invariant
symmetric bilinear forms, so `dim Inv-Sym(so(6)) = 1` (simple), `= 2` for
`so(4)`, and `= 2` for the derived algebra of the maximal compact of `su(3,2)`.
The maximal compact of `so(6,4)` is verified to be the *direct sum*
`so(6) (+) so(4)` — 15 + 6 = 21, brackets between the blocks vanish — before the
counts are added. The generating set used for `so(6)` is **verified to generate**,
with a planted control showing that dropping one generator collapses it to
`so(5)`.

The three numbers are LA-7's (§1.4 and probe P1/P2/P3). What is new is one
sentence: **`3 -> 2 -> 2`, so the drop is at arrow 1**, and it cannot be at
arrow 2 because arrow 2 is a deformation retract.

---

## 2. THE THREE SITES

Each site is typed before it is touched: does its **conclusion** use the nesting,
or does it cite the chain in passing?

### 2.1 `H19:114` — Q3b, "SM embedding: survives on the common fiber"

**What it said.** *"Weinstein's own SM chain is
`Spin(6,4) -> Spin(3,2) -> maximal compact SU(3) x SU(2) x U(1)`"*, sourced to
`[00:43:47]-[00:45:00]`, with the derived claim at `:120` that *"the SM embedding
requires indefinite internal groups `(6,4),(3,2),(3,2)`."*

**Does the conclusion use the nesting? NO.** Q3b's computed content is that the
trace-reversed DeWitt fibre is `(6,4)` for **both** base orientations, because
the fibre form is quadratic in `g`. The chain is a passenger. The verdict — that
`(7,7)` costs nothing here relative to `(9,5)` — is differential and stands
verbatim.

**Repair.** The chain now reads `Spin(6,4) > SU(3,2) > S(U(3)xU(2))`; the
transcript cite is narrowed to `[00:43:47]`, where the source says *"s u three
comma two"*, rather than to the range whose far end contains the garble; the
frame is stated (*"structure-group reductions of the rank-10 vertical bundle, not
a subgroup tower"*) with the source's own denial quoted; and the three-signature
list `(6,4),(3,2),(3,2)` is corrected to **two** — the real `(6,4)` form and its
Hermitian halving `(3,2)`.

**Consequence marked, not hidden.** The bullet's own title changes: *"SM
embedding"* was the wrong phrase for this object **even with the middle term
corrected**, because the object is a reduction chain, not an embedding tower. The
repaired bullet says so, and says that the verdict never asserted GU possesses an
SM embedding — and that under the corrected reading it asserts even less, since
arrow 2 is typed `REDUCTION_EXTERNAL`.

### 2.2 `H19:150` and `:157` — Q4b, the neutrality argument

**What it said.** *"Weinstein's `Spin(6,4)/Spin(3,2)` chain rides that invariant
fiber, so it too is neutral on the total signature"*, and the bullet
*"Weinstein's `spin(6,4) -> spin(3,2)` chain — the internal/fiber chain, common
to both totals."* The summary at `:163` repeats the three-signature list.

**Does the conclusion use the nesting? NO — and this is the site the brief
flagged.** The neutrality claim needs only that the chain's nodes are structure
groups of a `g -> -g` invariant fibre. **It survives the corrected reading, and
comes out tighter.** Under the old reading it was an assertion about a chain that
could not exist. Under the decided reading it is exact: `so(6,4)` is the
structure algebra of the rank-10 fibre, `su(3,2)` is the stabiliser of a
compatible complex structure **on that same fibre** (the repository's own
`O(6,4)/U(3,2)`), and `s(u(3)+u(2))` is its maximal compact. Their common
neutrality is now a statement about **one bundle** rather than a coincidence
across three unrelated groups.

**Consequence marked.** The repaired bullet says explicitly that the correction
makes the argument stronger, and immediately says what that buys: the conclusion
being tightened is `NOT-GU-NATIVE`, a **negative** verdict, so the tightening
increases confidence that GU does not select its own signature. Q4's headline
does not move.

### 2.3 `la6:918` — fence (i) on `LT-SM7`

**What it said.** *"The source's chain has a second step,
`Spin(6,4) -> Spin(3,2) -> SU(3)xSU(2)xU(1)`; the rank drop from 3 to 2 happens
somewhere in that second step and this artifact does not compute where."*

**Does the conclusion use the nesting? The AXIS RESULT does not; the FENCE
does.** LA-6's finding — `Delta5`'s declared gauge group `Spin(6) x Spin(4)`
carries three independent topological angles, the SM carries two, `LT-SM7` books
one — is computed from the declared group alone and never touches the chain.
Every number in §4.4 stands. But **fence (i) is itself a claim about the chain,
and it was wrong in content, not only in notation**: it located the rank drop in
the *second* step. Under the decided reading the second arrow is a maximal-compact
reduction, hence a deformation retract, hence unable to change `pi_3` at all.

**Repair.** Fence (i) now reads: the chain is `Spin(6,4) > SU(3,2) >
S(U(3)xU(2))`, its arrows are structure-group reductions of the rank-10 normal
bundle, the drop from 3 to 2 is at the **first** arrow, and what this artifact
does not compute is the *index data* of that arrow — which is the residue LA-7
§4.2 already named (the map `pi_3(SU(3,2)) -> pi_3(Spin(6,4))` carries Dynkin
indices, uncomputed). A `CAUTION` block quotes the original fence verbatim,
states why it changed, and states what did not change.

**Confined as instructed.** The Lagrangian-axis result is untouched — the probe
gates on the survival of both the finding sentence and the disposition token —
and no grade, no ledger row, and no `rows_assessed` entry is altered.

### 2.4 A fourth class of site, deliberately NOT touched

`cg1-...:252, :260, :292`, `itc-...:366`, `la7-...:167-168`,
`lab/literature/weinstein-ucsd-2025-04-transcript.md:27` and
`papers/drafts/Transcript into the impossible.md:155` all contain
`spin three comma two`. **None of them is a repair target.** They quote the
source verbatim, which is exactly what they should do: a verbatim quotation of a
garbled transcript is correct data, and normalising it would destroy the evidence
that SC-A's philological argument rests on. The probe's `G.5` gate is written to
exclude quotation and fire only on assertion.

---

## 3. DOWNSTREAM — WHAT LEANED ON THE IMPOSSIBLE FORM

**Answer: nothing, and the retrieval in §0.1 explains why.** The correct object
was independently present in two other notations the whole time, so no result was
ever forced to route through the defective string.

**Swept individually, all 27 files citing `H19`.** Every one cites it for the
`(9,5)`-versus-`(7,7)` signature under-determination or the two-primary/three-primary
count split — `RESEARCH-STATUS.md:2742`, `seven-axis-count-map-L0-L7`,
`landscape-assessment-post-three-waves:58`, `eleven-lens-audit:33,132`,
`improvement-register:63`, `W202`, `H37`, `H38`, `H6`, `H20`, `H23`, `H25`,
`H27`, the `one-residual` paper candidate. **Zero cite it for the chain.** H19's
own headline verdicts (`ODD-ADMISSIBLE-BUT-NOT-3`, `NOT-GU-NATIVE`,
`LIVE-BUT-NON-DERIVING`) are computed on the reps and the fibre and are untouched;
the probe gates on their survival.

**Swept: everything citing `LA-6` or `LT-SM7`.** `OT-1`, `OT-2`, `LA-10`, `LA-2`,
`LA-9`, `AR-2` cite the row's ownership typing and its cover membership. **Zero
cite fence (i) or the rank drop.**

**Three residues I cannot repair, named rather than left.**

1. **`tests/wave14/H19_seven_seven_branch.py:49, 60, 327, 362`** still carries the
   impossible form. Out of the CH-3 write scope. **Measured, not assumed:** all
   four occurrences are in a docstring or in a `report(...)` *detail* string, never
   in a predicate — verified by reading every line containing the string — and the
   file was re-run after the repair and still reports **11/11 PASS, exit 0**. So
   the probe's certificate is unaffected and the defect there is purely textual.
   It is still owed.
2. **`explorations/transcript-concordance-derived-results-2026-07-11.md:53`**
   carries both readings in a single clause (*"spin(6,4)/spin(3,2) chain; SU(3,2)
   maximal-compact = the SM"*) and is typed `CONFIRMED (dictionary)`. Out of
   scope; SC-A already named it.
3. **`la7-...:171`** says *"`H19-...:114` and its probe encode `Spin(3,2)`"*. After
   this repair that sentence is **half stale**: the `.md` is corrected, the probe
   is not. LA-7 is not one of my three sites, so it is flagged, not edited.

**Does H19's neutrality argument survive the corrected reading?** Yes — see §2.2.
It is the one argument in the three sites that the correction improves.

---

## 4. THE TRAP, STATED BEFORE THE HOSTILE REVIEW

**The repair is more favourable to GU in exactly two narrow places, and I am
naming them rather than waiting to be caught.**

**First**, H19's Q4b neutrality argument becomes a theorem about one rank-10
bundle instead of an assertion about three groups that could not nest (§2.2).
**What that does not buy:** the conclusion being strengthened is
`NOT-GU-NATIVE` — that GU supplies no selector for its own total signature. A
tighter negative is still a negative. GU's position on the signature axis is
marginally *worse* described after this repair, not better, because the
under-determination is now established on a cleaner argument.

**Second**, the repository's account of the source no longer contains a
group-theoretic impossibility. **What that does not buy:** absolutely nothing in
physics. The impossibility was a repository transcription defect, not a GU claim;
SC-A's own register proposal keeps `spin three comma two` in the `verbatim`
field and confines the adjudication to `notes`, and the audio has still not been
checked. Removing our own error from our own account of him is hygiene, and
hygiene is not evidence.

**And the three things the correction conspicuously does not supply.**

1. **The chain being reductions rather than breakings does not supply the
   reductions.** A structure-group reduction of a bundle exists when a section of
   the associated quotient bundle exists. Arrow 1 needs a global compatible
   complex structure on the rank-10 fibre; the repository's own `VG-V3` found
   that **no** orthogonal `J` commutes with GU's own fibre data (trace split,
   `SO(3,1)` isotropy, the `SU(2)_+` family action), and reported the commutant
   scan **EMPTY**. So arrow 1 is available as an abstract group embedding — which
   is what §1.4 constructs — and is *obstructed* as a GU-native bundle reduction
   by a result already on file. Nothing in CH-3 touches that.
2. **The second arrow is external.** The non-compact-to-compact maximal-compact
   reduction is typed `REDUCTION_EXTERNAL`
   (`explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md`,
   2026-07-04): the Weyl unitarian trick, not a GU-forced selection, and GU's
   native invariant form is Krein. SC-A prices its own register row at
   `adherence: PARTIAL` for exactly this reason, and CH-3 does not move it.
3. **Localising the rank drop supplies no angle.** Knowing the drop is at arrow 1
   does not tell you *which* generator is lost (that needs the Dynkin index LA-7
   §4.2 flags as uncomputed), does not settle whether any of the three angles is
   physical (LA-6 fence (ii), untouched), and does not move `LT-SM7`'s booking
   deficit by one unit.

**Net: no claim status moves anywhere, in either direction, and this artifact
proposes none.**

---

## 5. HOSTILE REVIEW, inline

**H1 — "Your 'independent reproduction' is independent in code only. You knew the
answers."** Substantially fair, and it caps what the reproduction is worth. I knew
the target integers, which means I could not have been surprised into finding a
different one; what independence buys is that the *constructions* differ (SC-A
builds `g_SM` as the `theta`-fixed part of `su(3,2)`; I build it that way **and**
from explicit `su(3)`/`su(2)` bases and check the two agree), so a construction
bug shared with SC-A would have to be a bug in the mathematics rather than in the
code. That is a real but bounded guarantee, and I am not claiming more. The
strongest genuinely independent element is §1.5, where I compute LA-7's `3,2,2`
by a *different invariant* and get its numbers back.

**H2 — "You improved H19's argument while claiming not to strengthen GU."** Both
are true and I put them in the same paragraph rather than in different sections
(§4). The distinction that carries the weight is that the argument I tightened
concludes `NOT-GU-NATIVE`. If the tightened argument had concluded something
favourable, the honest report would have been that the repair moved GU's
standing, and I would have had to say so in the frontmatter `result`.

**H3 — "Fence (i) of LA-6 said 'this artifact does not compute where' — you
computed where. That is altering the result you were told not to alter."** The
sharpest procedural objection. My reading: the instruction fenced LA-6's
*Lagrangian-axis result* — the effective-dof count, the minimum cover, the
`LT-SM7` rank finding — and fence (i) is not that result, it is a caveat *about
the chain*, i.e. it is chain attribution, which is exactly what I was told to
repair. Correcting a wrong statement inside the attribution while leaving it
wrong would have been the worse choice. Mitigation: the computation lives in
**my** artifact and my probe; LA-6 gets the corrected sentence, a verbatim quote
of what it used to say, and a pointer. No number in LA-6 changed.

**H4 — "The `12 > 10` obstruction is not news; LA-7 decided the middle node this
morning."** Correct, and §0.1 credits it. LA-7 decided the **term** by testing the
adjacent sentence (`dim K(SU(3,2)) = 12` vs `dim K(Spin(3,2)) = 4`); SC-A decided
the **chain** and the **kind of chain**. CH-3 owns neither. It owns the repair,
the reproduction, and one sentence about which arrow drops the rank.

**H5 — "Your exhaustiveness in §1.2 inherits SC-A's assumptions about invariant
forms on isotypic blocks."** Fair — the rule *"symplectic-type isotypic blocks
need even multiplicity"* is the load-bearing representation-theoretic input, and I
implemented it rather than proved it. What defends it is that the enumeration is
controlled in both directions: `5+4+1` and `1^10` are planted and must be
rejected, and the `5+1^5` row must be **accepted** and is then exhibited as two
explicitly commuting `so(3,2)` copies inside `so(6,4)` with brackets verified
elementwise. A predicate that accepts a construction I can display and rejects
one whose obstruction is an integer is doing real work.

**H6 — "You claim nothing downstream depended on the chain. Did you check, or did
you sample?"** I swept all 27 files citing `H19` individually and all files
citing `LA-6` or `LT-SM7`, and I ran the H19 probe after the repair. The one thing
I did **not** do is sweep for downstream uses of the *coset* notation
`O(6,4)/U(3,2)`, which appears in the live ledger `v0.258` — because that
notation is **correct** and needs no repair. If it later turns out that some
result depends on the coset object being a *breaking* rather than a *reduction*,
that is a separate typing question this artifact has not opened.

**H7 — "You turned a green gate red."** Yes, by one, and §0's `IMPORTANT` block
measures it before and after rather than describing it. The alternative — a
`doc_type` outside the audit's scope — would have been the dodge the method
exists to prevent.

---

## 6. POSTFLIGHT — five lenses, inline

**Lens 1 — arithmetic discipline.** Every dimension is an exact rank over `Q`;
every signature is an exact congruence power-tested on the zero-diagonal path;
the only place a non-integer could enter (the Weyl dimension formula) returns a
`Fraction` whose denominator is asserted to be 1 before casting; `assert_no_float`
sweeps the whole `RESULT` structure. No float is load-bearing anywhere. **Clean.**

**Lens 2 — control discipline.** Six positive controls run before any result; five
planted controls that must be false (including one, `F.2c`, that gives the
*generation check* itself power); one contrary control that must be true and is
then exhibited constructively. `--selftest` plants six false facts — the two
kills, the maximal-compact dimension, the Killing signature, the `pi_3` rank, and
the repaired-site text gate — each forces exit 1, and the clean run exits 0.
**Clean.**

**Lens 3 — attribution auditor, run in both directions.** *Source → repo:* the
GUT denial, the normal-bundle sentence, the fibre-reduction operation, the
complex-structure sentence and both spoken forms of the middle term are gated by
exact substring counts in the probe (`s u three comma two` = 2,
`spin three comma two` = 1, the `spin six comma spin four` garble = 1). *Repo →
source:* nothing in either repaired site now attributes a *mechanism* to the
author; the corrected chain is stated as the repository's decided reading with
SC-A named as its owner, and the source's own words are quoted for the frame.
**Clean.**

**Lens 4 — novelty auditor.** The retrieval ran before the work and demoted three
things (§0.1): the kill, the frame and the constructed arrows are SC-A's; the
three `pi_3` numbers are LA-7's; the maximal-compact-is-the-SM result is July
prior art. The only new sentence claimed is the localisation of the rank drop to
arrow 1, and even that is a corollary of a retract argument plus LA-7's table.
§0.1 also records something the brief did not know — that the correct object was
already in the repo in two other notations — which is a *demotion* of the defect's
significance, not an inflation of it. **Clean.**

**Lens 5 — gate, convention and blast-radius auditor.** `doc_type` is honest and
deliberately inside the routing audit's scope; the `GU-COMPARATOR-ROUTING` notice
is present with the method path and a matching
``Classification: `SOURCE_NATIVE_ROUTE` `` line; `target_claim` uses the
internal-target form with `target_claim_verdict` and contains no `SC-[A-Z]+-\d+`
pattern, so `kill_target_claim_audit.py` routes it to `internal_targets` rather
than looking up a register id that does not exist. Files touched: my artifact, my
probe, and the two named sites. Nothing under `carrier/`, `carrier-notation/`,
`class-shift/`, `vz-repair/` or `wave22/` was read or written; no git command was
run. The registry row is owed and named. **Clean, with one owed registry row and
three named residues.**

---

## 7. CERTIFICATE

```text
tests/channel-swings/joe_directed_ch3_chain_repair.py
  58/58 exact checks PASS, 5 planted controls (0 misbehaved), exit 0
  --selftest: 6/6 planted false facts each force exit 1; clean run exits 0
      dim_so32         dim so(3,2) forced to 12        -> would resurrect the nesting
      max_centraliser  max centraliser forced to 12    -> would resurrect the factorisation
      dim_k_su32       max compact of su(3,2) -> 4     -> would make the Spin(3,2) reading work
      killing_sig      Killing signature -> (4,6)      -> would break the fibre match
      rank_pi3_su32    rank pi_3(SU(3,2)) forced to 3  -> would move the drop to arrow 2
      site_repaired    the repaired-site gate forced to a token that is not there

  no shared code with tests/channel-swings/joe_directed_sca_right_chain.py
  exact arithmetic only: integer matrices + fractions.Fraction
  assert_no_float sweeps the entire RESULT structure -- clean

  REPRODUCED FROM SC-A
      dim so(3,2)                             = 10
      dim(su(3) + su(2) + u(1))               = 12     -> nested reading dead
      so(p,q), p+q = 5, all six real forms    = 10     -> signature cannot rescue
      first so(n) of dim >= 12                 n = 6, dim 15
      max centraliser of so(5,C) in so(10,C)  = 10     -> factorised reading dead
      dim so(6,4) / su(3,2) / u(3,2)          = 45 / 24 / 25
      max compact of su(3,2)                  = 12 = 11 + 1
      max compact of u(3,2)                   = 13
      so(6)+so(4) n su(3,2) / u(3,2) / so(3,2)= 12 / 13 / 4
      Killing signature of so(3,2)            = (6,4), unique in dim 5 up to relabel

  NEW HERE (localisation only; the three node numbers are LA-7's)
      rank pi_3 along Spin(6,4) > SU(3,2) > S(U(3)xU(2))  =  3 -> 2 -> 2
      arrow 2 is a maximal-compact retract, so it CANNOT drop the rank
      => the drop is at ARROW 1, the complex-structure reduction

  SITES REPAIRED
      explorations/wave14/H19-seven-seven-signature-branch-2026-07-11.md
          Q3b (:114, :120)   conclusion did NOT use the nesting   -> verdict stands
          Q4b (:150, :157, :163) conclusion did NOT use the nesting -> verdict stands, tighter
      lab/active-research/joe-directed/ledger-advancement/la6-...-2026-08-15.md
          fence (i) (:918)   the FENCE used the nesting and was WRONG in content
                             -> corrected, consequence named, axis result untouched

  RESIDUES OWED, out of CH-3 scope
      tests/wave14/H19_seven_seven_branch.py:49,60,327,362  (strings only; 11/11 still passes)
      explorations/transcript-concordance-derived-results-2026-07-11.md:53
      la7-...-2026-08-15.md:171  (its pointer is now half stale)
      one routing-registry row for this file
```

*Filed 2026-08-15. Joe-directed, channel CH-3. No claim status moved; none is
proposed. No git operation was performed.*

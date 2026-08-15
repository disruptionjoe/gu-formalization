---
artifact_type: exploration
status: exploration
doc_type: ledger-delta
created: 2026-08-15
work_item: LA-2
channel: conditional_ledger_advancement
base_revision: a148ed80
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
delta_kind: VERSIONLESS_DELTA__NOT_A_LEDGER_EDIT
target_claim: NONE-NOT-A-KILL
canonical_effect: pending_integration
canon_verdict_change: none
steering_effect: unchanged
title: "LA-2: AC-A1 does not need a kernel selection and the AC-A1 -> AC-A2/AC-A3 cascade is two-thirds already banked. The briefed grant ('the source action selects a fermion content in the rank-10 kernel') is CO-EXTENSIVE with AC-A1's own claim and cannot advance it without vacuity; the grant that DOES advance it is strictly weaker and already canon-recorded -- the draft-literal Sec 9.3 full-/S content (C1), non-chiral in every form slot, which sits at the kernel's ORIGIN. Computed exactly and newly: the admissible set is an infinite family (2189 unit-height integer points, 82501 / 984169 / 6590681 at heights 2/3/4), but adding unit multiplicity plus Hodge self-conjugacy cuts it to EXACTLY THREE points {0, +DK, -DK}, and full support plus unit multiplicity to exactly TWO {+-DK}. AC-A2 and AC-A3 are shown to be STRICTLY WEAKER than AC-A1 (rank 1 and rank 4 against rank 5, with explicit witnesses satisfying each and violating AC-A1), so their filed `SAME / DERIVED` is carrying an undeclared condition. NET: one verdict advance, two grant declarations, five declines."
grade: "EXACT rational arithmetic throughout (fractions.Fraction and Python int); no float is load-bearing anywhere. 65/65, exit 0, via tests/channel-swings/joe_directed_ledger_aca1_kernel_selection.py, which IMPORTS tests/anomaly/cb_c_anomaly_rank.py rather than reimplementing it. Certificate splits as 42 [E] exact results, 15 [C] controls that must have power, 7 [R] reproductions of filed cb-c results, 1 [T] declared table input. Non-vacuity established four ways: two positive controls (single chiral slots at p=0 and p=7 read 12/12 nonzero), four named GU contents that must FAIL and do (C0 12/12, C4 12/12, C5c 12/12, kerGamma-refined 12/12), three proper truncations of the alternating tower that must fail and do, and two mutation tests (a 1/464486400 perturbation of one degree-16 entry both breaks the alternating-tower cancellation and moves the kernel dimension from 10 to 9). The discarded MOVE-1 all-proportional-to-W convention is shown to give rank 1, not 5. NOT: a source action, a chirality-production mechanism, a generation count, a selection principle, a claim-status movement, or any statement about the 2+1 construction."
disposition: ACA1_DISCHARGEABLE_WITHOUT_ANY_KERNEL_SELECTION_ON_THE_SOURCE_NATIVE_C1_CONTENT__BRIEFED_GRANT_IS_TAUTOLOGOUS__CASCADE_IS_ONE_ADVANCE_PLUS_TWO_UNDECLARED_CONDITIONS__ADMISSIBLE_SET_IS_AN_INFINITE_FAMILY_THAT_TWO_MILD_SIDE_CONDITIONS_CUT_TO_THREE_POINTS
rows_proposed:
  advanced:
    - AC-A1
  condition_declared:
    - AC-A2
    - AC-A3
  evidence_addendum:
    - AC-A7
  declined:
    - AC-A4
    - AC-A5
    - AC-A6
    - AC-F1
    - AC-B2
grants_invoked:
  - id: GRANT-ACA1-C1
    statement: "The source action's 14D fermion content is the draft-literal Sec 9.3 full-/S reading (branch C1 of the chirality fork): non-chiral in every form slot, hence x = 0 in the signed-multiplicity lattice Z^15 over Omega^p(Y^14, /S)."
    provenance: SOURCE_NATIVE__NO_IMPORT
    already_recorded_at: "CURRENT-STATE.yaml:173 (Weinstein's total theory remains explicitly non-chiral); explorations/dk-chirality-fork-2026-07-20.md:159 (C1, native, W = 0, VANISHES)"
    falsifiable_by: "the truncated content C0 of CANON.md:185, which fails 12 of 12 degree-16 coefficients"
  - id: GRANT-ACA1-KER
    statement: "The source action selects a fermion content lying in the rank-10 kernel."
    provenance: REJECTED_AS_TAUTOLOGOUS
    reason: "membership in ker M is definitionally the same statement as AC-A1's claim that I_16 vanishes; advancing the row on it is a vacuously-true assertion"
  - id: GRANT-ACA1-DK
    statement: "The source action's content is the alternating Dirac-Kahler tower x_p = (-1)^p."
    provenance: TEMPLATE_IMPORT__NOT_TAKEN
    reason: "the (-1)^p chirality grading is explicitly typed as an import not canonically supplied by the Clifford dictionary (explorations/dk-chirality-fork-2026-07-20.md:215); carried here only as a computed waypoint, never as the operative grant"
depends_on:
  - lab/process/conditional-physics-ledger-v0.258.json
  - lab/methods/source-native-comparator-routing.md
  - explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md
  - explorations/dk-chirality-fork-2026-07-20.md
  - explorations/global-anomaly-leg-2026-07-20.md
  - explorations/verify-anomaly-closure-2026-07-20.md
  - explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md
  - lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md
  - lab/active-research/anomaly/sp1-2primary-dai-freed-gate-2026-07-06.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - canon/exhaustiveness-by-type-RESULTS.md
  - CURRENT-STATE.yaml
  - CANON.md
scripts:
  - tests/channel-swings/joe_directed_ledger_aca1_kernel_selection.py
  - tests/anomaly/cb_c_anomaly_rank.py
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
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`. The form-degree slots
> `Omega^p(Y^14, /S)` are program-native (draft Sec 9.3); the *chirality grading*
> that turns them into a signed-multiplicity vector `x in Z^15` is an import. The
> whole computation therefore sits on the boundary, not inside the source-native
> route, and fork 1 of the routing method applies to every sentence below that
> mentions net chirality.

# LA-2 — AC-A1 needs no kernel selection, and the cascade is two-thirds already banked

**Versionless delta against base revision `a148ed80`.** This document is not a
ledger edit and no ledger file was touched. Every proposed transition below is a
*proposal* to the ledger keeper, stated as `row id / current cell / proposed cell /
grant carried / evidence / confidence`.

---

## 1. Preflight — specialist lenses, run inline, work list re-derived

Standing rule: N lenses means N sections written here, never N subagents. The
briefing's target was re-derived rather than inherited; what moved in the ranking is
stated in §1.8.

### 1.1 Lens — anomaly / index theorist

The object is `I_16(x) = sum_p x_p [A-hat(TY^14) . ch(Lambda^p T*Y_C) . ch(S_gauge)]_16`,
required to vanish as a polynomial identity in `p_1..p_4` and the gauge Casimir.
That is a linear system `M x = 0` on `Z^15`, already built and solved wholesale by
`cb-c` (rank 5, kernel dim 10). This lens issues one warning that decides the whole
route: **a vectorlike content zeroes the perturbative anomaly identically, and that
is a triviality rather than a cancellation mechanism.** That warning is not mine —
it is filed verbatim at `explorations/dk-chirality-fork-2026-07-20.md` in the
branch-A consequence block, dated 2026-07-20. Any advance of AC-A1 that runs through
vectorlikeness is *true* and *low-information*, and must be reported as such.

Route proposed: do not recompute the matrix; re-derive AC-A7's kernel structure to
check the briefing's premise, then spend the budget on the *implication structure*
of the cascade and on the *point count* of the admissible set, neither of which
`cb-c` computed.

### 1.2 Lens — lattice / linear-algebra and Diophantine specialist

`dim ker M = 10` over a 15-dimensional lattice is a statement about a **rank-10
sublattice of `Z^15`**, which has infinitely many integer points. So "the action
selects a content in the rank-10 kernel" is underdetermined before any physics is
consulted — that much is immediate. The non-immediate question, and the one worth
computing, is whether the underdetermination survives *minimality*: unit
multiplicity, full support, non-negativity, Hodge self-conjugacy, bounded height.
Those are cheap to count exactly, because the kernel basis turns out to be integral
with unit entries in the free slots, so `ker ∩ Z^15` is a free `Z`-module with an
explicit basis and the bounded-height count factorises into a five-fold sum of
interval-intersection lengths. Route proposed: **count, do not estimate.** This is
the cheapest decisive experiment in the whole route.

### 1.3 Lens — comparator-routing auditor

`lab/methods/source-native-comparator-routing.md` fork 1 covers ordinary family
index / net chirality versus Weinstein's `2+1`; fork 4 names "anomaly cancellation
as a family selector" as an *admissible comparator that is not automatically the
owner* of the GU mechanism. Both fire here.

Two binding consequences. **(a)** The net-chirality functional `W(x) = sum_p x_p
C(14,p)` appears below and is proved to lie inside the row space. That is a
statement about a linear system, and it is **not** a chirality no-go, **not** a
generation obstruction, and **not** evidence about the `2+1` route. **(b)** Nothing
computed here may be promoted into a *selection* claim. The row asks whether the
anomaly polynomial vanishes; it does not license the anomaly conditions to choose a
content. `AC-1` of 2026-08-14 already banked the parallel statement one dimension
down ("anomaly cancellation has exactly zero discriminating power"), at 4D and
classified `CONVENTIONAL_COMPARATOR`; that result does **not** transfer to the 14D
degree-16 row, which is a different object with a different receptacle, and it is
cited here as a lesson, never as a discharge.

### 1.4 Lens — source-fidelity reader

What do GU's own documents force? Per the GU-native geometer's pass in the chirality
fork: the documents force the 0/1-form field slots (Sec 9.3) **and nothing more**.
Eq 9.16 is explicitly full-`/S`; the fermionic action at 10.10 is author-disclaimed
("Caveat Emptor"); the draft's stated physics is "fundamentally non-chiral… would
appear chiral". So the *draft-literal* content is `C1` — full Dirac, non-chiral in
every slot, `x = 0` in signed multiplicities — and the truncation `C0` that
`CANON.md:185` carries as "the assumed truncated fermion content" is an **import**,
not a source datum.

This lens supplies the operative grant. It also supplies the falsifier: `C0` and
`C1` are different points, and only one of them satisfies AC-A1.

### 1.5 Lens — epistemics / grant-hygiene

The briefing's grant is *"the source action selects a fermion content in the rank-10
kernel."* Read literally, the antecedent is `x ∈ ker M` and the consequent is
`I_16(x) = 0`. Those are the same sentence. Advancing AC-A1 on that grant is a
vacuously-true assertion, prohibited by the channel's own exactness rule, and it is
also the purest possible instance of laundering a grant into a derivation.

The grant-hygiene lens therefore **rejects the briefed grant outright** and demands
a substitute with two properties: it must be a *named content*, and its negation
must be *live in the repo*. `GRANT-ACA1-C1` satisfies both. This is the single most
important preflight finding and it inverts the route before any computation.

### 1.6 Lens — ledger-cascade topologist

Read the cascade off the ledger rather than off the briefing. `AC-A2` and `AC-A3`
are **already** `SAME / DERIVED`. They are not `NEEDS`. The briefing's "one
selection, three rows" is false against `v0.258`: at most one row can advance a
verdict, because two of the three are banked.

But their `distance` fields read `none after AC-A1` while `AC-A1` is `NEEDS`. So
either (i) they are genuinely unconditional and the distance field is decoration, or
(ii) they are conditional on AC-A1's grant and their `DERIVED` is undeclared-
conditional. `cb-c`'s own row table settles the intent — A2 and A3 are written
"**AUTO given A1**" — but intent is not proof. Route proposed: **prove the
implication direction exactly**, in both directions, with witnesses.

### 1.7 Lens — honesty auditor / prior-art sweeper

Swept by mechanism (anomaly polynomial, index density, degree-16, kernel, content
lattice, Dirac-Kähler, truncation, vectorlike, Green-Schwarz), not by label. The
sweep found the route heavily pre-owned:

| already owned | owner | what it owns |
|---|---|---|
| the whole matrix, rank 5, kernel dim 10, `W = 0` derived, 7 + 3 split, the `91 e_0 - e_2` witness, the AGW/`493/2419200` anchors, `U5` retirement | `explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md` + `tests/anomaly/cb_c_anomaly_rank.py` | essentially the entire computational base of this route |
| the eight named contents `C0..C5c`, the `-13` as a first partial sum, `C1` native and balanced, `C3`'s `(-1)^p` typed as an import, and **the vectorlikeness-is-a-triviality warning** | `explorations/dk-chirality-fork-2026-07-20.md` | the content taxonomy and the vacuity objection |
| the 14D global leg and its adversarial re-verification | `explorations/global-anomaly-leg-2026-07-20.md`; `explorations/verify-anomaly-closure-2026-07-20.md`; `lab/active-research/anomaly/sp1-2primary-dai-freed-gate-2026-07-06.md` | everything this artifact does *not* touch |
| "anomalies cannot select", at 4D | `lab/active-research/joe-directed/anomaly-cancellation/ac1-...-2026-08-14.md` | the selector question one dimension down |
| "the decider is unique; nothing routes around SG4" | `canon/exhaustiveness-by-type-RESULTS.md`; `canon/gu-forces-field-space-declaration-RESULTS.md` | the ceiling on any content claim |

**Honest accounting: roughly 70% of this route was already owned**, which is higher
than the briefing implied. Three things were not owned, and they are the only new
content below: the exact implication structure of the cascade (§3), the exact point
count of the admissible set under minimality (§4), and the resulting re-typing of
AC-A1's `distance` field (§5).

### 1.8 Re-derived work list, and what moved in the ranking

Re-derived from `v0.258` under the channel premise (source action and external datum
assumed to exist), scanning all 26 `NEEDS` rows for those whose *only* remaining
obstacle is that assumption:

| candidate | why it looked cheap | where it ranks after preflight |
|---|---|---|
| `AC-A1` | `distance` is a pure selection | **demoted.** The stated grant is co-extensive with the claim. What advances the row is a *different, weaker, already-canon* grant, and the advance is low-information |
| `LT-SM1` | `FINITE_CHOICE` — "select the `zeta_F`/Yang-Mills horn" | **promoted to structurally cheapest pure selection on the ledger.** A finite choice is strictly cheaper than a construction. Out of this route's axis; flagged only |
| `RA-E7`, `RA-G3` | "select the hosted 10/126 channel"; "select a `Lambda5` singlet VEV" | **held.** Both sit squarely in routing forks 2 and 4; neither can move without a typed bridge, and the `majorana-126-neutrino` lane already owns the surface |
| `LT-GR7`, `LT-SM2`, `LT-SM7` | `REAL_PARAMETER` | **rejected.** The premise grants that the action *exists*, not that its numerical outputs are known. "Derive one absolute gravitational normalization" is not discharged by assuming an action |
| `RA-F1`, `AC-F5` | `EXTERNAL_DATUM`, which the premise assumes | **rejected.** Both distances contain unbuilt *constructions* ("residual flag selection, BV/KT, cohomology, domain and index"; "construct a nonzero corner/framing object"), so the datum is not the only obstacle |

**What moved:** the briefed cascade collapsed from three rows to one advance plus two
condition-declarations; `AC-A1` fell from "highest-leverage single selection" to
"cheap but low-information cell correction"; and `LT-SM1` rose above it on pure-
selection cost, though outside this route.

### 1.9 Cheapest kill-or-switch, recorded before working

**Kill:** if the seven antisymmetric directions `e_p - e_{14-p}` are *not* all in the
kernel, or the Hodge-symmetric rank is not 5, then AC-A7 is wrong, the briefing's
premise collapses, and the route stops with a defect report instead of a delta.
Cost: one import and seven residual evaluations.

**Switch:** if `x = 0` is in the kernel — which it must be — then AC-A1 is
dischargeable with *no selection at all*, and the route switches from "make the
selection" to "show the selection is not needed and re-type the row." That switch
fired immediately.

---

## 2. AC-A7 re-derived, not cited

The briefing said to verify the rank-10 lattice rather than take its word. Done, by
an independent re-derivation from the imported characteristic-class machinery
(`tests/channel-swings/joe_directed_ledger_aca1_kernel_selection.py`, §2):

- each of the seven antisymmetric directions `e_p - e_{14-p}`, `p = 0..6`, gives
  **12/12 zero** degree-16 coefficients, and the seven are independent (rank 7);
- the rank on the eight Hodge-symmetric combinations `s_p = x_p + x_{14-p}` is
  **5**, leaving **3** symmetric free directions;
- the three lifted symmetric kernel directions each verify in the kernel of the full
  12-row system, and `7 + 3` span a rank-**10** lattice;
- `7 + (8 - 5) = 10 = dim ker M`, cross-checked against the direct kernel
  computation;
- Hodge symmetry `D_p = D_{14-p}` holds for all `p`, which is what makes the split
  meaningful rather than accidental.

**AC-A7 is confirmed.** The briefing's foundation is sound. Nothing about AC-A7
moves; §6 proposes an evidence addendum only.

---

## 3. The cascade, typed exactly: AC-A1 ⟹ AC-A2 and AC-A3, and not conversely

The 12-row degree-16 system splits by gauge weight: 5 rows at gauge-weight 0 (the
gravitational conditions, AC-A1), 1 row at weight 4 (the irreducible order-8 gauge
Casimir, AC-A2), and 6 rows at weights 1–3 (the mixed gauge-gravitational terms,
AC-A3).

**Forward direction, computed.** Each of the seven gauge-carrying rows was solved
*explicitly* as an exact rational combination of the five gravitational rows — not
inferred from rank equality. All seven solve. Therefore AC-A1 entails AC-A2 and
AC-A3 exactly.

**Non-vacuity.** The order-8 row and all six mixed rows are nonzero functionals, so
the containment is not the empty statement.

**Converse, computed, and it fails.** There exists a content satisfying the order-8
gauge condition while violating AC-A1, and a content satisfying *all six* mixed
gauge-gravitational conditions while violating AC-A1. Quantitatively:

```
   rank(AC-A1's 5 gravitational rows)      = 5
   rank(AC-A2's single order-8 row alone)  = 1     -> strictly weaker
   rank(AC-A3's 6 mixed rows alone)        = 4     -> strictly weaker
```

**Consequence for the ledger.** AC-A2 and AC-A3 are true *given* AC-A1 and are not
true independently of it. A row filed as `SAME / DERIVED` whose `distance` reads
`none after AC-A1`, while AC-A1 itself is `NEEDS`, is carrying an **undeclared
condition**. Under this channel's rule that a row advances carrying its named grant
as an explicit condition or not at all, the honest cell is `DERIVED_CONDITIONAL`.

This is a *decrement in claimed strength* and an *increment in honesty*. It is
reported as such, not dressed as an advance.

---

## 4. The honest risk, decided by counting: family or point?

The briefing asked whether the rank-10 kernel admits a family or a distinguished
selection. Both halves are now exact.

**It is a family, and a large one.** `ker M ∩ Z^15` is a free `Z`-module of rank 10
with an explicit integral basis, hence infinite. Bounded-height counts, computed
exactly:

| height bound | admissible integer contents |
|---|---|
| `|x_p| <= 1` | **2189** |
| `|x_p| <= 2` | **82501** |
| `|x_p| <= 3` | **984169** |
| `|x_p| <= 4` | **6590681** |

So `GRANT-ACA1-KER` — "the action selects a content in the kernel" — does not
determine *which*, by a wide margin, even at unit multiplicity.

**But two mild side conditions collapse it almost to a point.** Also computed
exactly:

| additional constraint | admissible contents |
|---|---|
| unit multiplicity + **Hodge self-conjugacy** `x_p = x_{14-p}` | **3**: `0`, `+DK`, `-DK` |
| unit multiplicity + **full support** (every form slot occupied) | **2**: `+DK`, `-DK` |
| unit multiplicity + **non-negativity** `x_p ∈ {0,1}` | **1**: `0` alone |

where `DK` is the alternating tower `x_p = (-1)^p`. This is the sharp answer to the
briefing's question, and it is new: `cb-c` computed the kernel's *dimension*; the
*point count under minimality* is not derivable from a dimension and was not filed.

**Read it honestly in both directions.**

*In favour of specificity:* the underdetermination is not wild. Two entirely
ordinary conditions — unit multiplicities and self-conjugacy under Hodge duality —
reduce an infinite family to `{0, ±DK}`.

*Against specificity:* those two conditions are themselves **unsupplied source-action
data**. Nothing in the assumed-but-unbuilt action delivers them; assuming them is a
second grant, not a consequence of the first. And of the two survivors, `±DK` carries
the `(-1)^p` chirality grading that the 2026-07-20 fork explicitly typed as **an
import not canonically supplied by the Clifford dictionary**. So the only survivor
reachable without an import is `0`.

**Verdict on the briefing's stated risk: the risk is real but it resolves in an
unexpected place.** The grant is not specific enough — and it also is not *needed*,
because the source-native content is the origin.

---

## 5. The proposed delta

### 5.1 The grant that is taken

> **`GRANT-ACA1-C1`.** The source action's 14D fermion content is the draft-literal
> Sec 9.3 full-`/S` reading — branch `C1` of the chirality fork — non-chiral in every
> form slot, hence `x = 0` in the signed-multiplicity lattice `Z^15` over
> `Omega^p(Y^14, /S)`.

Why this grant and not the briefed one:

1. **It is not the claim.** `x = 0` is a *named content*; `I_16(0) = 0` is a
   consequence, not a restatement. `GRANT-ACA1-KER` fails this test.
2. **It is source-native.** `C1` is the draft read as written, with no completion
   and no chirality template. `GRANT-ACA1-DK` fails this test.
3. **It is already recorded.** `CURRENT-STATE.yaml:173` — "Weinstein's total theory
   remains explicitly non-chiral". The grant adds no new unowned object.
4. **Its negation is live.** `CANON.md:185` carries "the assumed truncated fermion
   content" `C0`, which fails **12 of 12** degree-16 coefficients. The grant does
   real work: it picks a side of a fork the repo has open.
5. **It is honest about its weakness.** The cancellation is by vectorlikeness, which
   the 2026-07-20 fork already typed as *"a triviality, not a cancellation
   mechanism."* This delta does not dress that up.

### 5.2 Row transitions proposed

| row | current verdict / reason_kind | proposed verdict / reason_kind | grant carried as explicit condition | evidence | confidence |
|---|---|---|---|---|---|
| **AC-A1** | `NEEDS` / `MISSING_CONSTRUCTION` | **`SAME` / `DERIVED_CONDITIONAL`** | `GRANT-ACA1-C1` | probe §4, `x = 0` in ker verified; `C0` fails 12/12 as control | **high** on the mathematics, **medium-high** on the cell |
| **AC-A2** | `SAME` / `DERIVED` | **`SAME` / `DERIVED_CONDITIONAL`** | `GRANT-ACA1-C1` (declaring the condition already implicit in `distance: none after AC-A1`) | probe §3: order-8 row is in span(grav rows); rank 1 < 5; explicit witness satisfies A2 and violates A1 | **high** |
| **AC-A3** | `SAME` / `DERIVED` | **`SAME` / `DERIVED_CONDITIONAL`** | `GRANT-ACA1-C1` (same) | probe §3: all 6 mixed rows in span(grav rows); rank 4 < 5; explicit witness satisfies A3 and violates A1 | **high** |
| **AC-A7** | `SAME` / `DERIVED` | **unchanged** — evidence addendum only | — | probe §2: 7 + 3 = 10 re-derived independently; point counts added | **high** |

Proposed `distance` for AC-A1 after transition:

> `none at local-anomaly grade for the source-native C1 content, which sits at the
> kernel origin; no selection in the rank-10 kernel is required. The open object is
> the C0-truncation-versus-C1 fork, owned by the chirality/reduction unknown U4 and
> by AC-F1, not by this row.`

Proposed `revival_trigger` for AC-A1 after transition:

> `a source action whose stabilized fermionic term forces a chiral truncation, i.e.
> selects C0 or any other content outside the rank-10 kernel.`

### 5.3 Rows explicitly declined

| row | why declined |
|---|---|
| **AC-A4** ("anomaly cancellation forces net bulk chirality zero") | re-verified exactly (`W` lies in the row space) but already `SAME / DERIVED`. Nothing to move. Per routing fork 1 this is **not** a chirality verdict. |
| **AC-A5** ("net chirality zero alone suffices") | re-verified: the `91 e_0 - e_2` witness has `W = 0` and 11/12 coefficients nonzero. Verdict `DIFFERS / PREDICTION` is correct and stands. **Seam flagged:** its `revival_trigger` is "a selected content vector in the full rank-10 kernel", and this artifact supplies such vectors at will — so the trigger now fires without changing anything. The trigger is mis-specified and should be rewritten to name a *nonlinear* or *off-kernel* condition. |
| **AC-A6** ("no Green-Schwarz repair needed or available") | only **half** re-verified. On the kernel the residual is identically zero, which is immediate. The other half — that off the kernel the obstruction is the *primitive* `p_4`, which no `Y_4 ^ Y_12` or `Y_8 ^ Y_8` product can reproduce — was **not** re-derived here and remains at `cb-c`'s grade. Declined rather than confirmed. |
| **AC-F1** ("4D chirality emerges from a balanced bulk") | untouched, and deliberately. Every minimal admissible content computed here (`0`, `±DK`) is exactly non-chiral, which is *confirmatory of GU's declared posture*, not adverse to it. Per routing fork 1, a balanced bulk is **not** a chirality no-go for a theory whose observed sectors may separate only after observation and reduction. AC-F1's burden — native background, BV/BFV, positive domain, physical cohomology — is entirely unchanged by this artifact. |
| **AC-B2** ("gauge-twisted degree-15 bordism on the settled real horn") | the global leg is a different receptacle from the local one and is not touched. The `Cl(7,7)`/`BSO(128)`-type computation `CB-C-N1` remains open with its named owner. |

**Score, stated plainly: one row advances a verdict. Two rows have a hidden
condition declared, which is a strengthening of honesty and a weakening of claim.
Five rows are declined.**

---

## 6. Postflight — specialist lenses, run inline

### 6.1 Strongest overclaim available, and why it is not made

The tempting headline is *"AC-A1 is DERIVED — the 14D local anomaly cancels."* Three
things forbid it.

First, it would drop the condition. The cancellation holds for `C1` and fails for
`C0`, and `C0` is what `CANON.md:185` currently carries. Unconditional `DERIVED` here
would be exactly the laundering this channel prohibits.

Second, it would import specificity the computation does not have. "The anomaly
cancels" invites the reading "the content is determined". It is not: the admissible
set has 2189 unit-height points and grows to 6.59 million by height 4.

Third — and this is the one that would actually mislead — it would present a
**triviality as a mechanism**. `x = 0` is anomaly-free because it is vectorlike, and
a vectorlike theory is anomaly-free in every dimension for every gauge group. The
2026-07-20 fork said so first and this artifact does not improve on it.

A second, subtler overclaim also declined: presenting the `{0, ±DK}` collapse as
*"the source action's content is essentially determined."* It is not. The two side
conditions that produce the collapse are themselves ungranted, and one of the two
non-trivial survivors rests on an imported grading.

### 6.2 Strongest contrary reading

*"AC-A1 should not move at all. It is a placeholder for the real open question —
which content the built action selects — and re-typing it to `DERIVED_CONDITIONAL`
on the trivial point buries an open fork inside a satisfied row. The ledger is
better served by a `NEEDS` row that visibly names the fork than by a `SAME` row
whose condition readers will stop reading."*

This is a serious reading and it is not refuted. The rebuttal is only that the
condition is *carried in the row*, not dropped, and that the fork it names is
already owned by `U4` / `AC-F1`, so nothing is buried — it is relocated to its
actual owner. A ledger keeper who prefers redundancy over relocation should decline
the AC-A1 transition and accept only the AC-A2/AC-A3 condition declarations. That
outcome would leave **zero** verdict advances from this route, and it would be
defensible.

### 6.3 Weakest seam

The weakest seam is the identification **"GU's total theory is non-chiral" ⟹
"`x = 0` in the signed-multiplicity lattice."** Those are close but not identical.
`x_p` is a *net* signed multiplicity per form slot; a theory could in principle be
"non-chiral" in a coarser sense (e.g. `W = 0` overall, or balanced block-by-block as
`AC-F2`'s `192+192 / 576+576 / 64+64` records) without every slot's net vanishing
separately. The computation proves `W = 0` is strictly weaker than `x = 0` — the
`91 e_0 - e_2` witness has `W = 0` and is anomalous in 11 of 12 coefficients — so the
gap between the two readings is real and load-bearing. `AC-F2`'s block balance is
the closest filed object and it is at *kinematic* grade only, with `PH-K1-KINEMATIC`
explicitly not promoted to a physical carrier.

If a ledger keeper reads "non-chiral" as `W = 0` rather than `x = 0`, **the AC-A1
transition fails outright** and the row stays `NEEDS`. That is the single hinge this
delta rests on, and it is a semantic reading of `CURRENT-STATE.yaml:173`, not a
theorem. It is flagged here rather than smoothed over.

Two lesser seams. (i) The whole computation grades slots by an *imported* chirality
assignment, so the artifact is a semantic boundary, not a source-native result;
fork 1 applies. (ii) The `Sp(1) = right-H` gauge factor used in the 12-row system is
a `Cl(9,5)` object, while the settled horn is `Cl(7,7)`; `cb-c` proves the local row
is *fork-independent* (same rank 5 either way), so this does not bite here — but the
independence is inherited from `cb-c`, not re-derived in this artifact.

### 6.4 Grant-hygiene lens, second pass

Three grants were considered and their dispositions are recorded in the frontmatter:
`GRANT-ACA1-KER` **rejected as tautologous**; `GRANT-ACA1-DK` **not taken**, carried
only as a computed waypoint because its grading is an import; `GRANT-ACA1-C1`
**taken**, and it appears as an explicit condition on all three moved rows. No row
below advances to an unconditional `DERIVED`. The channel's rule 4 holds.

### 6.5 Comparator-routing auditor, second pass

Nothing here discharges a source-native row via a comparator, and no typed bridge
was built or claimed. `AC-1`'s 4D "anomalies cannot select" result is cited as a
lesson and explicitly **not** used to discharge the 14D row. The net-chirality
functional `W` is used only as a linear functional inside a rank computation and is
nowhere read as a chirality or generation verdict. `SG4` remains the unique decider
per `canon/exhaustiveness-by-type-RESULTS.md`; nothing in this artifact routes
around it, and the content question stays open.

### 6.6 Honesty auditor, closing

Rows moved: **one** verdict advance (`AC-A1`), **two** condition declarations
(`AC-A2`, `AC-A3`), **one** evidence addendum (`AC-A7`). Rows declined: **five**.

The briefing's framing — "one selection, three rows", "the highest-leverage single
selection on the ledger" — did not survive contact with `v0.258`. Two of the three
cascade rows were already banked, and the one that could move turned out to move on
a *weaker and already-recorded* grant, for a *lower-information* reason, than the
briefing supposed. The single genuinely new computation here is the point count in
§4, and it is a sharpening of `AC-A7`, not a new claim about physics.

No canon entry, bar, count, promotion, posture or claim-status moves on this
artifact. `canonical_effect: pending_integration`.

---

## 7. Attribution

The computational base of this route is **not** new work. The matrix, its rank 5,
its kernel dimension 10, the `7 + 3` split, `W = 0` as derived rather than assumed,
the `91 e_0 - e_2` necessity-not-sufficiency witness, the AGW degree-16 anchor, the
`493/2419200` anchor and the retirement of the Green-Schwarz counterterm `U5` all
belong to `explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md` and
its script `tests/anomaly/cb_c_anomaly_rank.py`, which this artifact **imports**.

The content taxonomy `C0..C5c`, the typing of `C1` as native and balanced, the typing
of `C3`'s `(-1)^p` grading as an import, the `-13`-as-first-partial-sum observation
and — decisively for this route — **the warning that a vectorlike content zeroes the
perturbative anomaly as a triviality rather than a mechanism** belong to
`explorations/dk-chirality-fork-2026-07-20.md`, dated 2026-07-20.

The 14D global leg and its adversarial re-verification belong to
`explorations/global-anomaly-leg-2026-07-20.md`,
`explorations/verify-anomaly-closure-2026-07-20.md` and
`lab/active-research/anomaly/sp1-2primary-dai-freed-gate-2026-07-06.md`. The 4D
Standard-Model shadow belongs to
`explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md`. The 4D
selector question and the Rarita-Schwinger rescalings belong to
`lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md`.
The uniqueness of the decider belongs to
`canon/exhaustiveness-by-type-RESULTS.md` and
`canon/gu-forces-field-space-declaration-RESULTS.md`.

New here, and only this: the exact implication structure of the AC-A1 → AC-A2/AC-A3
cascade with witnesses in both directions (§3); the exact point count of the
admissible set under unit multiplicity, full support, non-negativity, Hodge
self-conjugacy and bounded height (§4); and the resulting proposal to re-type
AC-A1's `distance` field (§5).

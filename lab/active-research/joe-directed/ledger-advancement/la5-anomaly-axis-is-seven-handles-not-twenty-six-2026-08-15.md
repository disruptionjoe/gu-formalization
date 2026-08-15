---
artifact_type: exploration
status: exploration
doc_type: ledger-advancement-delta
created: 2026-08-15
work_item: LA-5
channel: conditional_ledger_advancement
base_revision: a148ed80
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
delta_kind: VERSIONLESS_DELTA__NOT_A_LEDGER_EDIT
target_claim: "NONE — no GU source claim is targeted, attacked or defended. The object measured is the DEPENDENCY STRUCTURE of the 26 active ANOMALY_CONSISTENCY rows of ledger v0.258: which grants each row's `distance` and `revival_trigger` fields actually name, and what that structure forces about how many of the 26 can move independently."
title: "LA-5: the ANOMALY_CONSISTENCY axis has SEVEN effective degrees of freedom, not twenty-six. The grant→row discharge incidence matrix has EXACT rank 7 over 9 grant atoms; 11 of 26 rows carry the EMPTY signature and can never be moved by any grant supply; the 15 live rows fall into 7 signature classes that form a depth-2 DAG with exactly ONE serialization. Over all 2^9 grant states the axis reaches only 80 distinct verdict vectors out of 2^26 — strictly between 6 and 7 bits. Two grants (U4, EMB) buy 7 of 15 live rows; the remaining seven grants buy 8. New per-row findings: AC-C2 is a STRICT COROLLARY of AC-D1..D5 on their own solution lattice (and understates by a factor of 2 — the doublet count is divisible by 4, not merely even); AC-A4's revival trigger names the Green-Schwarz counterterm AC-A6 RETIRED, so it is unfireable as filed; AC-F4's revival signature is identical to AC-F5's discharge signature, so they are one fact with two verdicts; and the 14→4 reduction, if it is to make AC-D1..D5 unconditional, must be a lattice homomorphism annihilating at least 8 of the 10 admissible 14D content directions."
grade: "EXACT integer / sympy Rational and Fraction arithmetic throughout; no float is load-bearing anywhere. 127/127 checks, exit 0, via la5-anomaly-axis-degrees-of-freedom-probe.py, which IMPORTS tests/anomaly/cb_c_anomaly_rank.py rather than reimplementing the 14D system. Certificate splits as 87 [E] exact results, 31 [C] controls that must fire, 9 [R] reproductions of filed owners (CB-C's rank 5 / kernel 10 / Hodge symmetry; LA-3's rank 4 / L / kernel dim 2). AUDITABILITY: all 27 nonzero incidence entries are machine-verified against exact substrings occurring in the row's OWN v0.258 text (summary || distance || revival_trigger || mapping_grade), with seven negative token controls asserting each distinctive token occurs in exactly its declared carrier rows and nowhere else. The Smith-form invariants are computed on PRIMITIVE integer normals so they are intrinsic rather than scaling artifacts, and the 4D Z/3 is localised by two mutation controls (invariant under Y→6Y; destroyed by LA-3's filed Y(Q): 1/6→1/3). NOT: a source action, a chirality-production mechanism, a generation count, a real-form statement, a source-native result, a bridge, or any verdict movement."
disposition: AC_AXIS_HAS_RANK_7_DISCHARGE_INCIDENCE_OVER_9_GRANT_ATOMS__11_OF_26_ROWS_ARE_PERMANENTLY_IMMOVABLE__15_LIVE_ROWS_IN_7_SIGNATURE_CLASSES__80_OF_2E26_VERDICT_STATES_REACHABLE__U4_IS_THE_SINGLE_POINT_OF_FAILURE_AT_FANOUT_8__ACC2_IS_A_STRICT_COROLLARY_OF_ACD1_TO_D5__ACA4_TRIGGER_UNFIREABLE__ACF4_AND_ACF5_ARE_ONE_FACT__PHI_MUST_KILL_8_OF_10_CONTENT_DIRECTIONS__ZERO_ROWS_ADVANCE
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
rows_touched: [AC-A1, AC-A2, AC-A3, AC-A4, AC-A5, AC-A6, AC-A7, AC-B1, AC-B2, AC-B4, AC-B5, AC-C1, AC-C2, AC-D1, AC-D2, AC-D3, AC-D4, AC-D5, AC-E1, AC-F1, AC-F2, AC-F3, AC-F4, AC-F5, AC-G1a, AC-G2]
rows_advanced: 0
rows_retyped_proposed: [AC-C2, AC-A4, AC-F4, AC-E1, AC-A5, AC-A7, AC-G2]
free_object_delta: 0
free_object_delta_note: "No new un-owned object is introduced. U5 is confirmed RETIRED (AC-A6) and is removed from the grant column set; U6 is shown NOT to be an independent column but a coordinate on U1 (CB-C sec.5), so the column count falls from a naive 8 to 9-with-U6-folded. One new REQUIRED IDENTITY CHECK is named (LA5-N1: is CB-C-N1 the same object as AC-G1a's global receptacle?) and it is assigned to the existing global-anomaly-leg custodians, so it is a task, not a free object."
residue_touched:
  - id: U4
    grade_before: T2
    grade_after: T3
    moved: true
    why: "type fixed as a lattice homomorphism phi : Z^15 -> Z^6, and a DIMENSION attached: if AC-D1..D5 are to be DERIVED rather than DERIVED_CONDITIONAL then rank(phi restricted to ker M) <= 2, so phi must annihilate at least 8 of the 10 admissible content directions and at least 5 of the 7 Hodge-antisymmetric ones. Council tightening act (i) free-parameter reduction and (iii) shape constraint."
  - id: U5
    grade_before: retired
    grade_after: retired
    moved: false
    why: "confirmed retired; additionally shown that AC-A4's revival_trigger still quantifies over it, so the ledger carries a live pointer to a retired object"
depends_on:
  - lab/process/conditional-physics-ledger-v0.258.json
  - lab/methods/source-native-comparator-routing.md
  - lab/process/science-council-program-efficiency-2026-08-04.md
  - lab/process/perspective-passes/INDEX.md
  - explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md
  - explorations/conditional-build/selected-k77-superposition-hypothesis-27-lens-council-2026-08-14.md
  - lab/active-research/joe-directed/ledger-advancement/la1-embedding-grant-is-zero-bit-and-group-a-is-already-banked-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la2-aca1-needs-no-kernel-selection-and-the-cascade-is-two-thirds-already-banked-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md
  - tests/anomaly/cb_c_anomaly_rank.py
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - CURRENT-STATE.yaml
scripts:
  - lab/active-research/joe-directed/ledger-advancement/la5-anomaly-axis-degrees-of-freedom-probe.py
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
> Classification: **`BRIDGE_OR_SEMANTIC_BOUNDARY`.**

# LA-5 — twenty-six rows, seven handles

**Headline, before anything else: zero rows advance, and no grant is taken.**
This artifact supplies no content, no reduction, no embedding and no datum. It
measures the *shape* of the axis: which of the 26 rows can move at all, which
must move together, and how many independent unknowns stand behind them. The
answer is **7**, and eleven rows cannot be moved by any grant whatsoever.

---

## 0. Prior art, swept by mechanism, and one correction to the briefing

Swept by mechanism (incidence, dependency, rank, signature, lattice, elementary
divisor, cover, poset, conditioning), not by label.

| already owned | owner | what it owns |
|---|---|---|
| the 14D system: 12×15, rank 5, kernel dim 10, `D_p = D_{14-p}`, the 7+3 split, `W = 0` derived, `U5` retired | `explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md`, `tests/anomaly/cb_c_anomaly_rank.py` | the entire 14D computational base; **imported here, never re-derived** |
| the 4D system: 5×6, rank 4, the relation `2D1 − 27D2 − 36D3 − 9D4 + 9D5 = 0`, the saturated lattice `L = Z·(15) ⊕ Z·(ν^c)`, "complete 16s" sufficient but not necessary, the chirality clause exactly inert | **LA-3** (today) | the 4D lattice; **reproduced here as an anchor, never re-claimed** |
| `AC-A1` dischargeable at `x = 0` on the source-native C1 content; the briefed kernel grant rejected as tautologous; `AC-A2`/`AC-A3` strictly weaker than `AC-A1` (rank 1 and 4 vs 5) | **LA-2** (today) | the Group-A cascade |
| the embedding grant is one object; `G-EMB` = `RA-A3`, `RA-B1..RA-B5` | **LA-1** (today) | the `EMB` atom |
| the incidence / effective-dof method itself | **LA-4** and **LA-6**, running concurrently today on `REPRESENTATION` and `LAGRANGIAN` | the method. This artifact adopts LA-6's stricter substring-backing policy rather than inventing one |
| port-Hamiltonian, PDE well-posedness, network-protocol, multi-objective-optimization, category-theoretic and quantum-information lenses | `explorations/conditional-build/selected-k77-superposition-hypothesis-27-lens-council-2026-08-14.md` | **six of the thirteen lens names the briefing called "absent from the roster"** |

> **Correction to the briefing, stated plainly.** The briefing said the 41
> perspective passes are physics/math/distributed-systems and asked for
> engineering lenses "absent from that roster." That is true of the 41 passes and
> **false of the repository.** A 27-lens council filed 2026-08-14 already carries
> *port-Hamiltonian PDE and boundary-control*, *hyperbolic/ultrahyperbolic PDE*,
> *numerical PDE and scientific computing*, *network protocol and distributed
> state*, *multi-objective optimization*, and *category theorist and
> factorization-algebra*. So **6 of the 13 lens names below are not new to the
> repository.** What *is* new for all thirteen is the **application**: the
> 27-lens council pointed its lenses at the superposition hypothesis, never at
> the ledger's dependency structure. The lens names are recycled; the target is
> not. Novelty is claimed on findings, not on lens vocabulary.

Genuinely absent from both surfaces, by name and by mechanism: **MIMO state-space
controllability/observability**, **reliability engineering / FMEA**, **queueing
theory**, **systems-engineering requirements traceability**, **order/lattice
theory (Dilworth)**, and **model theory / definability**.

---

## 1. PREFLIGHT — specialist lenses, run inline; work list re-derived

Standing rule: N lenses means N sections written here, never N subagents.

### 1.0 Re-derived pool, from `conditional-physics-ledger-v0.258.json` directly

84 row records, 82 canonical targets, 2 `SUPERSEDED`. `ANOMALY_CONSISTENCY`
holds **27 records, 26 active** — `AC-G1` is superseded with successor `AC-G1a`.
The declared `denominator.axes.ANOMALY_CONSISTENCY = 26` matches. Verified in
the probe, 7/7 checks.

By `(verdict, reason_kind)` across the 26: 11 `SAME/DERIVED`, 5
`SAME/DERIVED_CONDITIONAL`, 4 `NEEDS/MISSING_CONSTRUCTION`, 2
`DIFFERS` singletons (`PREDICTION`, `ROUTE_KILLED`), 1 each of `SAME/IMPORTED`,
`NEEDS/EXTERNAL_DATUM`, `OVER_DETERMINED/GENUINE_FALSIFICATION`,
`DIFFERS/CONVENTION_ARTIFACT`.

**One structural fact recovered from the alias table, not from the row list:**
`CB-C:B3` — the free Dai-Freed column — is **aliased into `AC-A1`** with the
reason *"explicitly the same degree-16 local polynomial, not an independent
condition."* So CB-C's 27 source rows already collapsed once, by one, before this
axis was ever written down. The axis has a **precedent for exactly the collapse
this artifact measures**, and it is the right frame: the question is not whether
collapse happens, it is how much has not yet been recorded.

### 1.1 Lens — comparator-routing auditor (fork 1 bites hardest here)

Seven of the 26 rows (`AC-C2`, `AC-D1..D5`, `AC-E1`) are **4D Standard-Model
shadow rows**. Under fork 1 their carrier is *"three repeated four-dimensional
chiral spin-1/2 families derived from an ordinary compact family index, anomaly
count or net chiral index"* — the named comparator. LA-3 already routed
`AC-D1..D5` as `CONVENTIONAL_COMPARATOR`. **The routing has not been applied to
`AC-C2` or `AC-E1`, and this preflight extends it: they carry the same carrier,
the same arena and the same grant, so the same routing applies.** That is a
finding *before* any computation: the comparator block is seven rows, not five.

Consequence, binding on everything below: no result computed on the 4D lattice
may be reported as evidence for or against Weinstein's `2+1` route. What such a
result *can* do is specify a bridge burden — and §2.9 does exactly that, for
burden item 2 (the map induced by observation/reduction), which nothing in the
repository has ever typed.

### 1.2 Lens — MIMO control engineer

Read the axis as a plant: inputs = grants supplied, state = the 26-vector of row
verdicts. Two standard questions, neither ever asked here.

- **Controllability.** `rank(B)` where `B` is the grant→row incidence. If
  `rank(B) < 26`, the state cannot be steered arbitrarily: some directions are
  structurally unreachable. Predicted before computing: rank is small, because
  the `distance` strings repeat.
- **Observability.** The dual: from the verdicts alone, can the grant state be
  inferred? Rows sharing a signature are indistinguishable sensors.

This lens **sets the route**: build `B`, compute its exact rank, and compute the
*revival* incidence separately, because a revival trigger is the axis's only
sensor channel and nobody has looked at it as one.

### 1.3 Lens — reliability engineer (FMEA)

Three FMEA questions on a 26-item system: what is the **single point of
failure** (the grant whose falsification invalidates the most rows), what is the
**common-cause failure** (rows formally independent that share a hidden cause),
and what is the **undetectable failure mode** (a failure no row would register)?
LA-3 already found one undetectable mode — the chirality clause of `G-SHADOW` is
*exactly inert*, so its falsity is invisible to `AC-D1..D5`. The lens predicts
there are more, and that they live where signatures coincide.

### 1.4 Lens — order theorist

The signatures form a poset under inclusion. Two questions decide the axis's
**schedule**: is it an antichain (fully parallel), a chain (fully serial), or
mixed? And is the family meet-closed — i.e. does every shared sub-grant get
isolated by some row? A shared sub-grant that no row isolates is a grant the
ledger can never test on its own.

### 1.5 Lens — model theorist / definability

A ledger row is a predicate. Which predicates are **definable from the others**?
LA-2 proved `AC-A2` and `AC-A3` are entailed by `AC-A1` and not conversely — that
is an explicit-definability result. The lens asks whether the same holds anywhere
else, and it flags a schema problem: the `revival_trigger` field mixes ∃-shaped
and ∀-shaped statements with no marking. LA-3 already showed one ∀ is false
(`AC-D1..D5`). This preflight promotes that to a **complete quantifier audit of
all 26 triggers** as a route.

### 1.6 Lens — honesty auditor / prior-art sweeper

Swept by mechanism. The sweep found the *method* already in flight today
(LA-4, LA-6) and **six of thirteen lens names already filed** in a council the
briefing did not name. Both are reported in §0 rather than discovered later.
It also found the 14D and 4D computational bases entirely owned. **Honest
accounting: the computational substrate of this artifact is ~80% pre-owned.**
What is not owned is the incidence structure, the row-level corollary results of
§2.5, and the `phi` typing of §2.9.

### 1.7 Ranking, what moved, and the cheapest kill-or-switch

Candidate routes, ranked by (rows whose status the result would change) ÷ cost,
tie-broken to non-substitutable and to *both outcomes informative* — the
council's Rule R.

| rank | route | why |
|---|---|---|
| 1 | build the incidence matrix and compute its exact rank | 26 rows in scope; both outcomes informative (a high rank refutes the collapse thesis); non-substitutable — no other agent holds this axis |
| 2 | test whether `AC-C2` is a corollary of `AC-D1..D5` | the filed conflict key; cheap; a negative outcome *defends* the current typing |
| 3 | type the 14→4 reduction as a lattice map and bound its rank | upgrades `U4`, the highest-fan-out atom |
| 4 | quantifier-audit the 26 revival triggers | finds mis-typed rows; mechanical |
| 5 | intrinsic Smith invariants of both condition sets | conditioning; may find nothing |

**What moved in the ranking.** The briefing framed the axis as *"the best-measured
on the ledger, so ask whether its 26 rows are really 26 facts."* Preflight
**demotes** the natural reading of that (count independent *facts*) and
**promotes** a different one (count independent *handles*). The reason is
`AC-A4`/`AC-A5`/`AC-A6`/`AC-A7`: these are theorems about the condition system
itself, already terminal, with `distance: none`. Counting them as facts is
correct; counting them as *movable* rows is not. The axis's live question is not
"how many facts" but "how many of the 26 can the program still act on." That
reframe is what produced the immovable-set result, which is the single largest
number in this artifact.

**Cheapest kill-or-switch, declared before computing.** *Kill:* if the incidence
rank equals the number of live rows (15), there is no collapse, the briefing's
premise fails for this axis, and the route stops with a negative report. *Switch:*
if the rank is small but the immovable set is empty, the story is co-movement
rather than terminality, and the artifact becomes a scheduling result rather than
a typing result. **Neither fired.** Rank came back 7 against 15 live rows, and
the immovable set came back non-empty at 11 — so both effects are present and
both are reported.

---

## 2. THE SWING

Probe: `la5-anomaly-axis-degrees-of-freedom-probe.py`, **127/127, exit 0**
(87 `[E]`, 31 `[C]`, 9 `[R]`). Exact arithmetic throughout.

### 2.0 The incidence matrix, and why it is admissible as evidence

Nine grant atoms survive, after two reductions that are themselves findings:

- **`U5` (a Green–Schwarz counterterm) is removed.** `AC-A6` retired it: on the
  admissible kernel there is nothing to cancel, and off it the obstruction is the
  primitive `p_4`, unfactorizable. A retired object is not a column.
- **`U6` (the RS-BRST ghost-subtraction datum `q`) is not an independent
  column.** CB-C §5 makes it a *coordinate on which lattice vector `U1` is*
  (`Omega^1 ⊗ S` gives `W = −13`, `ker Gamma` gives `W = −12`). It is folded into
  `U1`.

| atom | what must be supplied |
|---|---|
| `U1` | the source action's 14D fermion content `x ∈ Z^15` |
| `U2` | which group the covariant derivative gauges |
| `U3` | the tangential structure of the end/link (spin/framed/String) |
| `U4` | the 14→4 reduction plus whatever produces 4D chirality |
| `EMB` | the SM embedding / stabilizer selection (`RA-A3`, `RA-B1..RA-B5`) |
| `BV` | native action-stationary background + proper BV/BFV + domain + physical cohomology |
| `N1` | `CB-C-N1`: the `Cl(7,7)`-side gauge-twisted degree-15 reduced spin-bordism receptacle |
| `P3` | the count datum plus a nonzero framed/String corner object |
| `BR` | a non-inflow 3-primary bridge, **or** supersession of the sole-bridge canon premise |

**Auditability.** A declared typing is not evidence. All **27** nonzero entries
are backed by an exact substring occurring in that row's own v0.258 text
(`summary || distance || revival_trigger || mapping_grade`), and the probe fails
if any backing substring is absent. Seven negative token controls assert that
`BSO(128)`, `P3`, `BV`, `fermion content`, `framing`, `BSp` and `gauge-twisted`
each occur in **exactly** their declared carrier rows and nowhere else. 27/27
verified.

### 2.1 The answer: rank 7

```
  active rows                                26
  grant atoms                                 9
  nonzero incidence entries                  27
  EXACT rank of the discharge incidence       7
  rows with the EMPTY signature              11
  live rows                                  15
  distinct nonzero signature classes           7
```

**Seven.** Any combination of grants, supplied in any order, can move the
26-dimensional row-state vector only inside a **7-dimensional** subspace.
**Nineteen of the twenty-six state directions are structurally uncontrollable.**

The seven classes:

| signature | rows | count |
|---|---|---|
| `{U4, EMB}` | `AC-C2`, `AC-D1`, `AC-D2`, `AC-D3`, `AC-D4`, `AC-D5`, `AC-E1` | **7** |
| `{U1}` | `AC-A1`, `AC-A2`, `AC-A3` | 3 |
| `{U1, U2, BV}` | `AC-G1a` | 1 |
| `{U4, BV}` | `AC-F1` | 1 |
| `{U2, N1}` | `AC-B2` | 1 |
| `{U3, P3}` | `AC-F5` | 1 |
| `{BR}` | `AC-F3` | 1 |
| **∅ (immovable)** | `AC-A4`, `AC-A5`, `AC-A6`, `AC-A7`, `AC-B1`, `AC-B4`, `AC-B5`, `AC-C1`, `AC-F2`, `AC-F4`, `AC-G2` | **11** |

### 2.2 The immovable eleven — the largest single finding

**Eleven of twenty-six rows have the empty signature. No grant supply moves
them, in any order, ever.** They are already terminal: CB-C grades them `AUTO`
or `DET`, and their `distance` fields read `none`.

This is not a defect. It is the axis's banked capital, and it has never been
counted. But it forces two corrections to how the axis is read:

1. **The axis's "coverage 100%, 26/26 mapped" meter overstates live surface by a
   factor of ~1.7.** The program can act on 15 rows, not 26.
2. **Three of the eleven are not physics requirements at all.** `AC-A5` ("is
   `W = 0` the whole content of local cancellation?"), `AC-A7` ("structure of the
   admissible set"), and `AC-G2` ("is the old gauge-octic premise needed for the
   local conclusion?") are statements *about the condition system*, not
   conditions the SM imposes. Under the ledger's own `inclusion_rule` —
   *"Include every distinct representation requirement, Lagrangian/equation
   term-slot, and anomaly/consistency requirement"* — they are not
   anomaly/consistency requirements. They inflate the denominator by 3.

### 2.3 The single point of failure, and the two-grant cliff

Single-grant fan-out, exact:

```
  U4   8 rows      U2   2 rows      P3   1 row
  EMB  7 rows      BV   2 rows      BR   1 row
  U1   4 rows      U3   1 row       N1   1 row
```

**`U4` — the 14→4 reduction plus chirality production — is the axis's single
point of failure at fan-out 8**, more than half the live rows. `EMB` is second at
7. Nothing else exceeds 4.

Exact max-coverage Pareto frontier (brute force over all `2^9` subsets, so the
optimum carries a complete certificate):

| grants supplied | max live rows discharged | optimal witness |
|---:|---:|---|
| 1 | 3 | `{U1}` |
| **2** | **7** | **`{U4, EMB}`** |
| 3 | 10 | `{U1, U4, EMB}` |
| 4 | 11 | `+ BV` |
| 5 | 12 | `+ U2` |
| 6 | 13 | `+ N1` |
| 7 | 14 | `+ BR` |
| 8 | 14 | *(plateau — `U3` and `P3` only pay together)* |
| 9 | 15 | `+ P3` |

**The cheapest certificate set is `{U4, EMB}`: two grants, seven rows.** The
remaining seven grants buy the other eight rows. That is the whole cost structure
of the axis in one line — **7 of 15 for two, 8 of 15 for seven** — and it is why
`U4` and `EMB` should absorb essentially all effort.

The `k=8` plateau is a real structural fact, not an artifact: `U3` and `P3`
appear in exactly one row (`AC-F5`) and only jointly, so neither pays anything on
its own. In network-flow terms they are a **series pair**, the only one on the
axis.

### 2.4 The poset: depth 2, one serialization, six parallel workstreams

Among the seven signature classes there is **exactly one** strict comparability:

```
        {U1}  <  {U1, U2, BV}
```

i.e. **`AC-G1a` is strictly downstream of `AC-A1`/`AC-A2`/`AC-A3`.** Everything
else is incomparable. Dilworth: maximum antichain **6**, minimum chain cover
**6**. The dependency DAG has depth **2**.

Two consequences.

- **The axis is wide and shallow.** There is no long critical path to shorten and
  almost nothing to serialize. Six workstreams can run fully in parallel, and any
  sequencing effort beyond "do `AC-A1` before `AC-G1a`" is wasted.
- **Three shared sub-grants are never isolated by any row.** The meets `{BV}`,
  `{U2}` and `{U4}` are each shared by two or more classes but are not themselves
  the signature of any row. **No row on this axis tests `U4` alone.** So a `U4`
  supplied *wrongly* cannot be caught by a single row; it will present as a
  correlated failure across seven or eight. That is the axis's common-cause
  failure mode (FMEA lens), and it is undetectable by row-level inspection.

### 2.5 The three row-level corrections, computed

#### (a) `AC-C2` is a strict corollary of `AC-D1..D5` — the filed conflict resolves downward

The brief records `AC-C2`'s `SAME/DERIVED` against `AC-D1..D5`'s
`SAME/DERIVED_CONDITIONAL` on a near-identical grant as a conflict key. The
incidence confirms identical signatures. **But the relation is stronger than
"same grant": `AC-C2` is logically implied by `AC-D1..D5` on their own solution
lattice.**

Computed exactly on the 6-dimensional signed multiplicity lattice of the 16's SM
constituents. The `SU(2)_L` doublet count is `d(n) = 3 n_Q + n_L`.

- `d` is **not** in the Q-row-space of the five anomaly channels: appending it
  raises the rank from 4 to 5. So `AC-C2` is not an *equation* they imply.
- But on `L = Z·(15) ⊕ Z·(ν^c)`, `d` takes **exactly the multiples of 4**
  (verified on all 169 lattice points with coefficients in `[−6,6]`).

So on the anomaly-free set, `AC-C2`'s "even" holds automatically — and it is a
**factor-2 understatement**: the count is divisible by **4**, not merely by 2.

Controls that must fire, and do: a content with odd doublet count exists in `Z^6`
(one `L` alone, `d = 1`) and is *not* anomaly-free; a content with even doublet
count that is *still* anomalous exists (`2L`, `d = 2`). So `AC-C2` is strictly
weaker than `AC-D1..D5`, not equivalent to them.

> **Resolution of the filed conflict, and it goes downward, not upward.**
> `AC-C2` cannot be `SAME/DERIVED` while the rows that *entail* it are
> `SAME/DERIVED_CONDITIONAL`. The honest cell is `SAME/DERIVED_CONDITIONAL`,
> carrying the same declared condition. This is a decrement in claimed strength.

#### (b) `AC-A4`'s revival trigger is unfireable as filed

`AC-A4`'s trigger reads *"a counterterm changing the anomaly polynomial."* That
is `U5`. **`AC-A6` retired `U5`** — no Green–Schwarz mechanism is available or
needed. So `AC-A4`'s trigger cannot fire unless `AC-A6`'s own trigger ("a new
reducible counterterm class outside the tested factorization") fires first.

**The ledger records no dependency between them.** This is a second defect of the
same family as `AC-A5`'s (which fires at will): `AC-A5`'s trigger is *too loose*
and `AC-A4`'s is *dead*. Both are `distance: none` rows in the immovable eleven,
and both carry triggers that do not describe their actual revival condition.

#### (c) `AC-F4` and `AC-F5` are one fact with two verdicts

`AC-F4`'s **revival** signature `{U3, P3}` is **identical** to `AC-F5`'s
**discharge** signature. `AC-F4` is `DIFFERS/ROUTE_KILLED` ("spin cannot
improve"); `AC-F5` is `NEEDS/EXTERNAL_DATUM` ("construct a nonzero corner/framing
object and pair it with `P3`"). Constructing `AC-F5`'s object is *exactly* the
event that revives `AC-F4`. They are the negative and positive halves of a single
statement about where an odd count can live, filed as two rows with opposite
verdicts and no recorded edge.

A third row belongs to the same object: CB-C §4.2 names `AC-F3`'s escape horn H3
as *"use framed/String walls"* — which is `AC-F5`'s route. So **`AC-F3`, `AC-F4`
and `AC-F5` are three rows on one unknown.**

### 2.6 The revival channel is full rank; the discharge channel is not

Computed separately, over the ten columns (nine atoms plus the retired `U5`):

```
   rank(discharge incidence)  =  7   of 9 columns
   rank(revival  incidence)   = 10   of 10 columns  (FULL)
```

**The axis is fully observable and only rank-7 controllable.** Every grant atom
is individually visible through some row's revival trigger, but only seven
independent directions can be driven through discharges. Sixteen of the 26 rows
have a discharge signature different from their revival signature.

This asymmetry has a concrete reading. The ledger is a **better instrument than
it is an actuator.** If the goal is to *detect* that a grant was supplied wrongly,
the revival channel covers everything. If the goal is to *move* rows, seven
handles is the ceiling. Nothing in the ledger's schema distinguishes the two
channels, and `distance` and `revival_trigger` are currently written as if they
were the same axis of the same object. They are not.

### 2.7 Exact information content: 80 states, between 6 and 7 bits

Enumerating all `2^9 = 512` grant states and recording the induced 26-bit verdict
vector gives **80 distinct states**.

```
   2^6 = 64  <  80  <  128 = 2^7
```

**The whole `ANOMALY_CONSISTENCY` axis carries strictly between 6 and 7 bits of
grant-driven state, out of `2^26` formally expressible verdict vectors.**

And 80 < 128 = `2^7`, so the seven signature classes are not even freely
combinable: they are **logically entangled**, with an entanglement deficit of 48
states. The entanglement is forced by shared atoms — `{U1}` and `{U1,U2,BV}`
cannot be independently set, nor can `{U4,EMB}` and `{U4,BV}`.

### 2.8 Conditioning, intrinsic

Smith normal forms computed on **primitive integer normals**, so the invariants
are intrinsic to the hyperplane set rather than artifacts of a scaling choice.

| system | elementary divisors | reading |
|---|---|---|
| 4D SM, 5×6 | `[1, 1, 1, 3]` | the row lattice has index **3** in its saturation inside `Z^6` |
| 14D, 12×15 | `[1, 6, 360, 40320, 7257600]` | strongly non-unimodular |

The 4D `Z/3` is localised by two controls: it is **invariant** under the overall
rescaling `Y → 6Y` (so it is not a normalization artifact), and it is **destroyed**
by LA-3's own filed mutation `Y(Q): 1/6 → 1/3`. So it sits on the quark-doublet
hypercharge `1/6`.

> **LAYER-0 FENCE, RAISED HERE AND NOT CROSSED.** This is a **new `3`** and it is
> **not** the generation count. Its type is *the index of a rational condition
> lattice in its saturation*, on the **comparator** side of fork 1. The repo's
> 3-primary count arena is the 3-primary summand of `π_3^s = Z/24`, a stable
> homotopy object (`canon/three-generations-locate-not-force-CRT-RESULTS.md`;
> `AC-F4`). Different objects, different types, no map exhibited. Under the
> mandatory routing rule this `3` may not be reported as evidence about GU's
> generation count in either direction. It is filed as a homonym, in the same
> family as CB-C §2.4's two `13`s, and it is registered here so it is not
> re-derived and mis-read by a later wave.

Separately, an exact statement about how special the 14D result is. The locus of
`12×15` matrices of rank `≤ 5` has codimension `(12−5)(15−5) = 70` in the
180-dimensional space of such matrices; the locus of `5×6` matrices of rank `≤ 4`
has codimension `(5−4)(6−4) = 2` in 30 dimensions. **The 14D kernel-dimension-10
result is a codimension-70 coincidence of the characteristic classes; the 4D
rank-4 result is a codimension-2 one.** These are not comparable results, and the
14D one is 35× the deeper coincidence. This is the exact form of the informal
statement that the 14D freedom is fragile.

### 2.9 The reduction, typed: `U4` moves T2 → T3

The axis's highest-fan-out atom, `U4`, is graded **T2** by CB-C — typed but with
no class exclusion. It can be tightened without supplying it, and this is the
artifact's most actionable output.

Both anomaly systems are lattices. The reduction is therefore, at minimum, a
**homomorphism of lattices**

```
        phi : Z^15  ->  Z^6
```

from the 14D signed-multiplicity lattice over `Omega^p(Y^14, /S)` to the 6D
multiplicity lattice of the 16's SM constituents. Nothing in the repository has
ever written it down, and its two endpoints are both already computed.

Now the constraint, stated in the two branches that matter.

- **Weak branch (what the ledger currently claims).** Only the *supplied* content
  `x*` needs `phi(x*) ∈ L`. No rank bound follows. This is exactly
  `SAME/DERIVED_CONDITIONAL`.
- **Strong branch (what `DERIVED` would require).** For `AC-D1..D5` to be
  unconditional, every admissible 14D content must reduce to an anomaly-free 4D
  content: `phi(ker M) ⊆ L`. Then, since `rank(ker M) = 10` and `rank L = 2`:

```
        rank( phi|_{ker M} )  <=  2
        dim ker( phi|_{ker M} )  >=  10 - 2  =  8
```

> **At most 2 of the 10 admissible 14D content directions can survive to 4D. The
> reduction must annihilate at least 8 — and at least 5 of the 7 Hodge-
> antisymmetric directions `e_p − e_{14−p}` that CB-C row A7 proved are free.**

That is a **shape constraint with a dimension attached**, on the object the
program has held at T2 since 2026-08-05. Under the council's tightening taxonomy
it is act (i) — reduces the free-parameter count of a named missing object — and
act (iii) — adds a shape constraint the supplier must satisfy. **`U4`: T2 → T3.**

It is also the exact criterion the ledger is currently missing:

> `AC-D1..D5` (and `AC-C2`, and `AC-E1`) are `DERIVED` **iff** `phi(ker M) ⊆ L`,
> and `DERIVED_CONDITIONAL` otherwise. The filed `AC-C2` / `AC-D` inconsistency is
> precisely someone grading one row on the strong branch and five on the weak one.

**Routing, stated so this is not over-read.** `L` is a comparator object under
fork 1. This is therefore not a result about GU; it is a filled-in **bridge
burden item 2** — *the map induced by observation/reduction* — which LA-3 recorded
as `UNOWNED` and which the routing method requires before any comparator result
may be transported. It types the map and bounds its rank. It does not build it,
and it transports nothing.

### 2.10 The three lenses that returned nothing, stated bluntly

- **Queueing theory.** Attempted: rows as jobs, grants as servers, head-of-line
  blocking behind `U4`. The only thing it produced that the incidence matrix did
  not already give is "seven rows are blocked behind one server," which is §2.3
  restated in worse vocabulary. There is no arrival process, no service-time
  distribution and no measured throughput, so Little's law has nothing to bind.
  **Nothing banked.**
- **Systems-engineering requirements traceability.** All 26 rows have a
  `source_row` and an `evidence` pointer, and CB-C's 27 source rows reconcile
  exactly with the ledger's 27 records (27 − `B3` aliased + `G1a` split = 27).
  The traceability check **passes**, which is a clean bill of health and not a
  finding. The one thing it flagged — that 20 of 26 rows cite the same evidence
  file — is single-source concentration, but the file is CB-C, which is the
  artifact that *created* the rows, so the concentration is definitional rather
  than a defect. **Nothing banked.**
- **Optimization duality.** The intended move was an LP-dual certificate for the
  cheapest cover. It collapses: every row requires the *conjunction* of its
  grants, so the cover of all live rows is trivially all nine atoms and the dual
  is vacuous. The useful object turned out to be the max-coverage frontier
  (§2.3), which is a different problem and is certified by exhaustion, not by
  duality. **The lens named the right object and then contributed nothing to
  solving it.**

Two more that returned only a single line each, reported for completeness rather
than dressed up:

- **Port-Hamiltonian / bond-graph.** Its one contribution is the conservation
  reading: rows discharged must be *paid for* by grants supplied, and the ledger
  has **no field recording which grant paid for which row**. That is the schema
  gap this whole artifact had to reconstruct by substring matching. Real, but one
  sentence, and the 27-lens council already owns the lens name.
- **Category theory / functoriality.** Its one contribution is a genuine
  non-monotonicity: `AC-F3` is `OVER_DETERMINED` *because* local cancellation
  forces `I_16 ≡ 0`, so **discharging `AC-A1` is what kills `AC-F3`** (CB-C
  §4.2(i)). The grant→row map is therefore not monotone, and the incidence
  matrix as built — all entries `+1` — is the wrong sign structure for at least
  one edge. Also real, also one sentence.

### 2.11 The five science-council seats, applied to this axis

**Seat 2 — was the conditional pivot correct, and what has not been tried.** The
council's untried move #1 was the *deliberately-wrong complete construction*:
"stipulate any admissible choice at every open fork … **change one fork, count the
rows that move**." **That is the incidence matrix, and this artifact runs its
cheap symbolic version for one axis.** The answer is the fan-out table and the
Pareto frontier of §2.3. Seat 2's recommendation is discharged for
`ANOMALY_CONSISTENCY`; it remains untried for the program as a whole, and LA-4 and
LA-6 are running it concurrently on the other two axes.

**Seat 3 — efficiency of the mapping; the three columns.** Seat 3 asked how many
rows land in **column 3 (requires external datum N)**. This axis can now answer
exactly: **two** — `AC-F5` (`P3`) and `AC-B2` (`CB-C-N1`). Plus one column-1-by-
citation row, `AC-E1` (`CITED_NOT_REDERIVED`). So the AC axis's external-datum
residue is **2 of 26**, which is a genuinely small number and is the kind of
result Seat 3 said would be publishable either way.

**Seat 4 — the RULED syllogism, and its transferable move.** Seat 4's method is:
*two objects are described the same way; nobody has checked whether they are the
same object; the check is cheap and both outcomes are informative.* Applied here,
it finds an uncaught instance:

> **`LA5-N1` (new, unasked, cheap).** `AC-B2` needs *"the `Cl(7,7)`-appropriate
> `BSO(128)`-type receptacle"* (`CB-C-N1`). `AC-G1a` needs *"the operative
> anomaly group and global receptacle"* on the same settled `Cl(7,7)` horn. **Are
> these the same object?**
> - **Same** ⇒ the axis is double-counting one missing computation as two rows;
>   the live-row count falls to 14 and the incidence rank falls to 6.
> - **Different** ⇒ the settled horn carries **two** distinct unbuilt global
>   receptacles, not one, and `AC-G1a`'s distance understates what it needs.
>
> Cost: hours, no new geometry. Owner: the global-anomaly-leg custodians (the
> owner CB-C already named for `CB-C-N1`). Both outcomes are informative, which
> is exactly Rule R's tie-break.

Seat 4's discipline also fires a second time, and this one is answerable from
CB-C's own text: `AC-F3`'s escape horn H3 **is** `AC-F5`'s route (§2.5c). Same
object, already stated, edge not recorded.

**Seat 5 — where to point pre- and post-reviews.** PRE-1 (*what Layer-0 fork does
this assume, and what does it cost if the other branch is right?*): the AC axis
**consumes** `REAL-CLIFFORD-FORM` settled at `Cl(7,7)`, and that consumption is
exactly what produced `AC-G1 → AC-G1a`. PRE-2 (*compute the dimension of the
search space before enumerating*): **this axis is the one place PRE-2 was actually
run** — CB-C solved the whole 14D system wholesale rather than testing contents
one at a time. PRE-3 (*name any new un-owned object and its owner now*): CB-C
introduced `CB-C-N1` with an owner in the same breath. **The AC axis passes all
three PRE questions, and that is the mechanical reason it is the best-measured
axis on the ledger.**

One regression to report, bluntly. Seat 5's **POST-1** requires every wave to emit
the `residue_count` / `residue_tightness` / `free_object_delta` tuple. CB-C carries
it (`free_object_delta: 0`, a full `residue_touched` block). **LA-1, LA-2 and LA-3
— today's three artifacts on this channel — do not.** This artifact carries it.
The council installed POST-1 on 2026-08-04 and it has decayed in eleven days.

**Seat 6 — the honest ranking, under Rule R.** Candidates for the next move on
this axis, scored by (live rows whose status would change) × (probability of
landing in cost) ÷ cost, tie-broken to non-substitutable and to both-outcomes-
informative:

| # | move | rows in scope | why it ranks here |
|---|---|---|---|
| **1** | **build `phi` and decide the strong branch** (`phi(ker M) ⊆ L`?) | **7** (`AC-C2`, `AC-D1..D5`, `AC-E1`) | decides `DERIVED` vs `DERIVED_CONDITIONAL` for the whole comparator block at once; upgrades the axis's SPOF; non-substitutable; a negative outcome is as informative as a positive |
| **2** | **run `LA5-N1`** (is `CB-C-N1` = `AC-G1a`'s receptacle?) | 2 | hours, no geometry, both outcomes change the denominator |
| **3** | **re-type the immovable eleven and the three meta-rows** | 11 (+3 denominator) | mechanical, cheap, and it is the difference between a 26-row axis and a 15-row one |
| 4 | quantifier-audit the remaining revival triggers | 26 | mechanical; already found two defects here, likely more |
| 5 | supply `U1` | 3 | LA-2 showed the advance is real but low-information |

**"Keep doing what we are doing" scores below all five**, because the axis's
15 live rows are now known to sit behind 7 handles, and per-row work cannot beat
per-handle work at that ratio.

---

## 3. POSTFLIGHT — specialist lenses, run inline

### 3.1 Strongest overclaim available, and why it is refused

**"The anomaly axis is really only seven facts, so the ledger is inflated 3.7×."**

Refused on three independent grounds, each fatal alone.

1. **Rank 7 counts *handles*, not *facts*.** The eleven immovable rows are banked
   results — `Omega^spin_15 = 0`, `KO_15 = KSp_15 = 0`, `pi_4(SO(128)) = 0`, the
   `91 e_0 − e_2` witness, the `p_4` primitivity argument. They are immovable
   *because they are finished*, not because they are empty. An axis with many
   terminal rows is a **successful** axis. The correct sentence is "seven live
   handles and eleven banked results," and any compression that drops the second
   clause is a misreport.
2. **The incidence is a typing, not a theorem.** 27/27 entries are backed by exact
   ledger substrings, which makes the typing *auditable*, not *correct*. A reader
   who types `AC-E1` as `{}` rather than `{U4, EMB}` gets rank 7 still, but a
   reader who splits `EMB` into six atoms (one per `RA-B` row) gets a different
   number. The rank is exact **given the atom set**, and the atom set is a
   judgement.
3. **"Inflated" imports a standard the ledger never adopted.** The
   `inclusion_rule` counts *requirements*, not *independent requirements*. By its
   own rule the count of 26 is correct. What this artifact shows is that a second
   number — live handles — was never computed and is much smaller. Both are true.

### 3.2 Strongest contrary reading

**The best case against the central result is that `EMB` and `U4` are not one
atom each, and that the collapse is an artifact of coarse atomization.**

It has real force. `EMB` is LA-1's `G-EMB`, which spans six rows (`RA-A3`,
`RA-B1..RA-B5`) on the `REPRESENTATION` axis; LA-1 graded that grant "zero-bit,"
which supports treating it as one atom, but LA-3's mutation controls show the
embedding is *the discriminating datum* — changing one hypercharge destroys the
zeros and raises the rank. A datum that discriminating is arguably not one bit.
If `EMB` splits into two or more atoms, the `{U4, EMB}` class could split and the
rank would rise.

**Where it fails:** splitting `EMB` raises the *grant* count but does not split
the *signature class*, because all seven rows in that class name the same
embedding. Rank rises only if some row in the class depends on a strict subset of
the split atoms — and none does, by the substring backing. So the contrary reading
changes the atom count and leaves the co-movement result standing. **The seven
rows still move together.** That is the load-bearing half and it is robust.

The reading does land somewhere real, though, and it is worth banking: **the
`{U4, EMB}` class is the only place on the axis where the atomization is
genuinely contestable**, and it is also the class holding 7 of 15 live rows. So
the axis's largest structure rests on its least certain typing.

### 3.3 Weakest seam

**The `BR` atom.** Every other atom is a conjunctive requirement: supply it, and
the rows that name it advance. `BR` is not. CB-C §4.2 gives `AC-F3` **three**
escape horns — accept `W ≠ 0` (which *destroys* `AC-A1`), supersede the
sole-bridge canon premise (a canon-level move), or use framed/String walls (which
is `AC-F5`'s route). Any one suffices.

**The ledger's `distance` field cannot express a disjunction.** Twenty-five of the
26 rows are AND-typed and one is OR-typed, and the schema does not distinguish
them. I modelled `BR` as a single conjunctive atom, which is **wrong in a way I
cannot repair inside this channel** — it understates `AC-F3`'s movability (three
routes, not one) and it hides the overlap between `BR`'s third horn and
`{U3, P3}`. The rank-7 result does not change under any of the three readings I
checked, but the Pareto frontier at `k = 7..9` does, and I would not defend those
three rows of the table as hard as the rest.

Second seam, smaller: **the sign structure.** §2.10 found a genuine anti-edge —
discharging `AC-A1` over-determines `AC-F3` — and the incidence matrix carries all
entries as `+1`. A signed incidence would be the right object. I did not build it,
because one anti-edge is not enough structure to compute anything with, and
guessing at others would be fabrication.

### 3.4 Grant-hygiene, second pass

**No grant is taken in this artifact.** `U1`, `U2`, `U3`, `U4`, `EMB`, `BV`, `N1`,
`P3` and `BR` are all treated as *unsupplied throughout*; every result is a
statement about what would follow *if* they were supplied, and in what
combinations. Nothing is laundered, because nothing is granted.

The one place a grant could have crept in is §2.9. The `phi` rank bound is stated
in **two branches** precisely so that the strong branch — the one that would make
`AC-D1..D5` unconditional — is visibly an *antecedent*, not an assumption. Had I
written only the strong branch, I would have granted `phi(ker M) ⊆ L` and then
"derived" a constraint from it. That is the laundering shape, and it is the one
this channel exists to refuse.

### 3.5 Comparator-routing auditor, second pass

Two comparator objects were computed here: the 4D anomaly lattice `L` (fork 1) and
its `Z/3` saturation index. Neither is transported.

- `L` is used only to bound `rank(phi)` — a **bridge-burden specification**, which
  the routing method explicitly licenses and in fact requires.
- The `Z/3` is **fenced, not banked** (§2.8). It is the shape of finding that
  would be most tempting to launder in this repository, and the fence is the
  deliverable rather than the number.

Classification stands: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

### 3.6 Honesty auditor, closing

**The count, plainly.** Rows advanced: **0**. Grants taken: **0**. Verdicts moved:
**0**. Canon touched: **0**. New computations that are load-bearing: the incidence
rank, the immovable set, the 80-state enumeration, the Pareto frontier, the
`AC-C2` corollary, the two intrinsic Smith forms, and the `phi` rank bound. New
row-level defects found: **3** (`AC-A4` unfireable trigger, `AC-F4`/`AC-F5` one
fact, `AC-C2` corollary-not-peer). Prior art that turned out to own more than the
briefing implied: **the 27-lens council owns 6 of 13 lens names**, and the
computational substrate is ~80% pre-owned.

**The difficulty, re-assessed honestly.** This was *easier* than it looked. The
briefing framed the central question as hard ("the grant→row incidence rank is a
real number nobody has"). It is a 26×9 integer matrix and the rank is a one-line
computation; the work was in the *typing*, not the algebra, and the typing took
about four fifths of the effort. What is genuinely hard — and remains untouched —
is `phi`. Everything downstream of §2.9 is bounded by an object nobody has
written down, and no amount of ledger analysis will produce it.

---

## 4. THE VERSIONLESS DELTA — against base revision `a148ed80`

**No ledger edit is performed.** The following are *proposed* and carry
`canonical_effect: pending_integration`.

### 4.1 Row re-typings proposed (7 rows, all decrements or clarifications)

| row | current | proposed | ground |
|---|---|---|---|
| `AC-C2` | `SAME / DERIVED` | `SAME / DERIVED_CONDITIONAL`, condition declared identically to `AC-D1..D5` | it is *entailed by* `AC-D1..D5` on `L`; it cannot be stronger than its own premises (§2.5a) |
| `AC-A4` | trigger: *"a counterterm changing the anomaly polynomial"* | trigger: *"a new reducible counterterm class outside the tested factorization — i.e. `AC-A6` must revive first"* | `U5` is retired by `AC-A6`; the trigger as filed cannot fire (§2.5b) |
| `AC-F4` | `DIFFERS / ROUTE_KILLED`, no recorded edge | add `coupled_to: [AC-F5, AC-F3]` | `AC-F4`'s revival condition is *identically* `AC-F5`'s discharge condition (§2.5c) |
| `AC-E1` | `SAME / IMPORTED` | add the declared condition `{U4, EMB}` | same signature as the `AC-D` block; currently the only row on the axis whose condition is undeclared *and* whose evidence is un-rederived |
| `AC-A5` | trigger fires at will (already filed) | trigger: *"a content violating one of the four conditions beyond `W = 0`"* | the row is a rank theorem; no content selection can falsify it |
| `AC-A7` | counted as a physics requirement | mark `row_kind: meta` | it states the *structure of the condition set*, not a condition (§2.2) |
| `AC-G2` | counted as a physics requirement | mark `row_kind: meta` | it states whether a premise was needed, not a physics requirement (§2.2) |

### 4.2 Residue movement proposed

`U4`: **T2 → T3**. Type fixed as a lattice homomorphism `phi : Z^15 → Z^6`;
dimension attached — on the strong branch `phi` must annihilate ≥ 8 of the 10
admissible content directions and ≥ 5 of the 7 Hodge-antisymmetric ones (§2.9).

### 4.3 One new named task, with an owner

`LA5-N1` (T3): decide whether `CB-C-N1` (`AC-B2`) and `AC-G1a`'s "global
receptacle" are the same object. Owner: the global-anomaly-leg custodians — the
owner CB-C already assigned to `CB-C-N1`. Cost: hours. Both outcomes change the
axis's live-row count.

### 4.4 Schema observations, filed not executed

1. The ledger has **no field recording which grant paid for which row**; this
   artifact reconstructed 27 such edges by substring matching against
   `distance || revival_trigger || mapping_grade`. A `grants: []` field would make
   the incidence machine-derivable rather than machine-*verifiable*.
2. `distance` cannot express a **disjunction**; `AC-F3` is the axis's only
   OR-typed row and is currently indistinguishable from an AND-typed one (§3.3).
3. `distance` and `revival_trigger` are written as one axis of one object; the
   rank asymmetry (7 vs 10) shows they are two different channels (§2.6).

### 4.5 What does NOT change

No verdict, reason-kind, mapping-grade, canon claim, count, bar, priority,
promotion, lane status or public posture moves. The generation count stays OPEN,
`PH-K1-PHYSICAL` stays OPEN/BLOCKED, `P3` stays reinstated, `SG4` remains the
unique open decider, and the total theory remains explicitly non-chiral. Nothing
in this artifact licenses a chiral reading of any block.

---

## 5. Reproduction

```
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  lab/active-research/joe-directed/ledger-advancement/la5-anomaly-axis-degrees-of-freedom-probe.py
```

Green on 2026-08-15, **127/127, exit 0** (87 `[E]`, 31 `[C]`, 9 `[R]`). It
imports `tests/anomaly/cb_c_anomaly_rank.py` rather than reimplementing the 14D
system, reads `lab/process/conditional-physics-ledger-v0.258.json` directly for
its work list, and carries a real failure path (`sys.exit(1)` on any failed
check).

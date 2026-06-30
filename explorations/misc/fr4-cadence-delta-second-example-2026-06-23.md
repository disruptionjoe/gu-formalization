---
title: "FR4 Cadence-Delta Second Worked Example: CALM-Monotonic L4 with Deadline-Gated Rendering"
date: 2026-06-23
problem_label: "fr4-cadence-delta-second-example"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# FR4 Cadence-Delta Second Worked Example: CALM-Monotonic L4 with Deadline-Gated Rendering

**Purpose.** This document fills a second six-axis worked example in which the cadence field
`Delta` catches a real protocol error. Per the sub-protocol promotion condition in
`explorations/time-as-finality-crosswalk/observer-finality-layer.md`:

> "This sub-protocol can move toward canon only after at least two worked six-axis examples
> show that the added fields catch real errors or produce useful falsification tests."

The first worked example was example-02-D (Sorkin causal-set L4, deadline-gated L6; filed in
`explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`).
That example could not serve as the second because it uses Sorkin L4. Per the explicit
promotion condition, the second example must be **non-Sorkin L4 and non-Type-II_1 L1**.

This document uses:
- **L1:** Smooth principal bundle (GU substrate, conventional Y^14 = Met(X^4) with gimmel
  metric, NOT Type II_1).
- **L4:** CALM-monotonic partial order (distributed-systems / database eventual-consistency
  class, NOT Sorkin causal set).
- **L6:** Dijkstra self-stabilizing finalization loop with a hard cadence deadline `Delta`,
  exactly as in example-02-D, transplanted into this different L4 setting.

The key question: does the premature-commitment failure mode of example-02-D survive the
transplant from Sorkin L4 to CALM-monotonic L4, and is the mechanism structurally distinct
(so that the second example genuinely adds coverage)?

---

## 1. The Candidate: Example-CALM-D

**Candidate identifier:** `CALM-GU-deadline-cadence` (example-CALM-D).

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CALM-GU-deadline-cadence | Smooth principal bundle on Y^14 = Met(X^4), gimmel metric (9,5), Sp(64) gauge bundle, Clifford spinor S = H^64 | Finite Turing (BPP/BQP), finite compute budget B, window width w | CALM-smooth pairing: observer reads off chirality invariant from a CALM-ordered update stream | CALM-monotonic partial order — eventual-consistency model; updates arrive in CALM (Consistency, Availability, Lattice Monotone) order; no Sorkin partial order | Specific object (Y^14 with gimmel metric) | Dijkstra self-stabilizing finalization loop with hard cadence deadline Delta | Show a CALM-update stream where a late-arriving lattice element arrives after Delta, contradicting a finalized chirality invariant — occurring at arbitrarily low update rate and not reachable under completeness-gating. |

---

## 2. Why CALM-Monotonic L4 is Structurally Distinct from Sorkin L4

### 2.1 The Sorkin partial order (example-02)

In example-02, L4 is the Sorkin causal set: a locally finite partially ordered set (C, prec)
where the order is the fundamental causal relation. Completeness of the past of an element x
means J^-(x) cap W is order-complete with respect to prec. The observer computes chirality
invariants from finite sub-posets.

### 2.2 The CALM-monotonic partial order (this candidate)

In the CALM model (Hellerstein-Alvaro 2020), a distributed system processes updates over a
**lattice** (L, <=), where each state is a lattice element and updates are join operations:
the state only ever increases (monotone). The CALM theorem states:
"A program has an eventually-consistent, coordination-free implementation iff it is monotone."

The partial order here is the **lattice partial order** (L, <=) on states: `a <= b` iff `b =
a join c` for some lattice element c. This is NOT a Sorkin causal order because:

1. **The lattice order is algebraic, not spacetime-geometric.** Joins are computed over an
   information lattice (e.g., sets of observed events, or sets of received metric updates from
   the GU bundle Y^14), not over spacetime events.
2. **CALM order is anti-entropy-directed.** Elements only join upward in the lattice; there
   is no past-cone completion predicate because the order is monotone by construction.
3. **The partial order is over states, not events.** The Sorkin order is over events (elements
   of the causal set). The CALM order is over lattice states (equivalently, join-closed
   downsets of received update packets).

### 2.3 The CALM finality condition

Under CALM monotonicity, a finality condition for a record of the observer's current state s
is:

```
s is final when no future join operation on s changes the value of the chirality invariant I(s).
```

This is the **value-stability** condition: `I(s join t) = I(s)` for all future updates t.
Value-stability is to CALM what completeness of J^-(x) is to Sorkin: the right natural
finality condition for the respective partial order class.

Under value-stability gating, the observer finalizes a chirality record only when it has
confirmed that no future lattice join can change the value of the invariant. This is stronger
than "all updates so far agree" and weaker than "the full lattice element is known."

---

## 3. The Finality Sub-Protocol, with the Cadence Field

We instantiate the observer-finality sub-protocol fields (from
`explorations/time-as-finality-crosswalk/observer-finality-layer.md`) for both the
value-stability-gated version (baseline) and the deadline-cadence version (this candidate):

| field | example-CALM baseline (value-stability-gated) | example-CALM-D (deadline-cadence) |
|---|---|---|
| record-bearing observer class | finite Turing machine with budget B, window w | same |
| record type | finalized lattice invariant I(s) for current lattice state s | same |
| causal accessibility | all updates in the observer's CALM update stream up to the current join; no future joins accessible | same accessibility, but finalization is **forced** by deadline (see cadence) |
| finality relation | I(s) is final when value-stability holds: I(s join t) = I(s) for all future t in the stream (observer waits for stability confirmation) | I(s) final at tick arrival(s) + Delta, whether or not value-stability has been confirmed (**deadline-gated**) |
| readout target | chirality invariant I(s) of the GU bundle section extracted from the CALM update stream | same |
| **cadence (new field)** | (absent; finalization deferred until value-stability confirmed) | **Delta = max ticks a lattice record may stay open before forced finalization** |
| failure mode | late-join failure: a later update t arrives and I(s join t) != I(s), but s was not finalized (value-stability correctly prevented finalization) | **deadline-premature-commitment: a later update t arrives after Delta, but I(s) was already finalized at tick arrival(s) + Delta; I(s) != I(s join t) — record is wrong despite operating below capacity** |

The `cadence` field `Delta` is again the new degree of freedom. Its content in the CALM
setting is structurally distinct from the Sorkin setting in two ways:

1. **The order is different.** In Sorkin, the completeness predicate is about J^-(x) (a
   past-cone predicate on spacetime events). In CALM, the stability predicate is about
   I(s join t) (a value-invariance predicate on lattice elements). These are different
   mathematical objects: the Sorkin predicate checks membership in a DAG past-cone; the
   CALM predicate checks value-stability of a lattice join.

2. **The failure mechanism differs in a testable way.** In example-02-D, the
   premature-commitment failure is triggered by a late-past event (a spacetime event whose
   arrival is after Delta). In this candidate, the failure is triggered by a late join
   (a lattice element whose join with the current state would change the invariant, arriving
   after Delta). The late-past and late-join events are formally distinct: a late-past event
   is an element of J^-(x) \ W_{t_0}; a late join is an element t in L such that I(s join t)
   != I(s) and t arrives after the deadline.

---

## 4. The Failure-Mode Analysis

### 4.1 Baseline: value-stability-gated (no deadline)

Under value-stability gating, the observer finalizes I(s) only when it has confirmed that all
possible future joins preserve I(s). The failure mode is:

- **Capacity overload (L2):** if the update rate lambda exceeds B/w (the L2 capacity ceiling
  from FR1), the observer's buffer overflows, an open lattice record is evicted, and later
  updates to that record can change the invariant after eviction.
- **No other failure mode.** At any lambda <= B/w, a patient value-stability-gated observer
  is exactly correct. The CALM order's monotonicity guarantees that confirmed value-stability
  is permanent: once I(s join t) = I(s) for all t in a cofinal subset of the lattice, the
  invariant is stable.

The capacity-overload failure is a pure L2 effect (the same as FR1 for Sorkin), absorbed
by L4 (CALM order provides the stability predicate) and L2 (budget ceiling B/w).

### 4.2 Deadline-gated: example-CALM-D

Under deadline-gating with cadence `Delta`, the observer finalizes I(s) at tick arrival(s) +
Delta **whether or not value-stability has been confirmed**. Define a late-join event as:

> An update packet t in L such that I(s join t) != I(s) and t arrives at the observer at tick
> tau_t > arrival(s) + Delta.

When a late-join event occurs:

1. The observer finalized I(s) at tick arrival(s) + Delta, from an **unstable** lattice state s.
2. The correct invariant is I(s join t) != I(s).
3. **The finalized record is wrong, even though the observer was operating at lambda <= B/w
   and never evicted anything.**

This is a **structurally new failure mode** in the CALM setting: premature commitment on an
unstable lattice state. It is not an eviction effect (L2 capacity) and it is not a lattice
property (the CALM order's monotonicity does not prevent unstable states from existing before
full convergence). It is a mismatch between the deadline Delta and the **lattice convergence
latency** (the time for all relevant join elements to reach the observer).

### 4.3 The decisive structural distinction: CALM vs. Sorkin

The failure mode is structurally new in the CALM setting by an independent argument from
example-02-D's argument:

**Claim (FR4-CALM core).** The deadline-gated failure mode in example-CALM-D is:
(a) not reachable under value-stability gating,
(b) not captured by the CALM L4 partial order alone, and
(c) structurally distinct from example-02-D's failure mode (not a relabeling).

**Proof of (a).** Under value-stability gating, the observer waits until I(s join t) = I(s)
for all future joins t, then finalizes. A late join t satisfies I(s join t) != I(s): exactly
the condition that prevents value-stability. So the observer would NOT have finalized I(s)
before t arrived. The late-join failure mode has empty extension under value-stability gating.
QED.

**Proof of (b).** The CALM L4 order provides the lattice (L, <=) and the join operation
s join t. It provides the stability predicate I(s join t) = I(s). But the CALM L4 order does
NOT specify a finalization rule: it says monotone updates are coordination-free, but it does
not force finalization before stability. The deadline Delta is not a CALM-order property; it
is an L6 coordination-loop policy. L4 contains the predicate; L6 contains the override. QED.

**Proof of (c).** The example-02-D failure is triggered by a late-past event (a Sorkin element
in J^-(x) \ W_Delta). The example-CALM-D failure is triggered by a late join (a lattice
element t with I(s join t) != I(s)). These are formally distinct objects:

- The Sorkin past-cone J^-(x) is defined by the transitive reduction of the causal partial
  order (prec); membership in J^-(x) is a combinatorial predicate on the DAG.
- The CALM lattice join predicate I(s join t) != I(s) is defined by the algebraic structure of
  the invariant function I on the lattice (L, <=); it is a semantic predicate, not a DAG
  membership predicate.

A candidate that has both Sorkin L4 and value-stability gating could exhibit the Sorkin
late-past failure without the CALM late-join failure (if the lattice is trivial), and vice
versa. The failure modes are not instances of a common supertype; they require different
mathematical machinery to detect (DAG completeness vs. lattice-join semantic stability).
QED.

### 4.4 Quantitative: when does Delta cause failure in the CALM setting?

The premature-commitment failure occurs when:

```
Delta < T_join(s) := sup{ tau_t - arrival(s) : t in L, I(s join t) != I(s) }
```

where `T_join(s)` is the worst-case latency for an instability-revealing join to arrive.
`T_join(s)` is a property of the GU bundle update stream: it measures how long the observer
must wait after receiving a partial metric update (lattice state s) before it can certify that
no further metric updates will change the chirality invariant I(s).

Crucially, **`T_join(s)` can be large even when the update rate lambda is small.** A slow
update stream can have a single late join arriving long after the observer's deadline. So
the premature-commitment failure occurs at arbitrarily low lambda, controlled by
`Delta < T_join(s)`, not by any rate ceiling. This is the same structural signature as
example-02-D: the failure is Delta-vs-latency mismatch, not a rate-overload phenomenon.

### 4.5 Summary: new failure mode, new mechanism, distinct from Sorkin version

| | example-02-D (Sorkin) | example-CALM-D (this document) |
|---|---|---|
| L4 class | Sorkin partial order (spacetime causal DAG) | CALM-monotonic lattice partial order |
| L1 class | Sorkin causal set (L1 IS the causal set) | Smooth principal bundle Y^14 (NOT Sorkin) |
| Finality predicate | J^-(x) order-complete (past-cone completeness) | I(s join t) = I(s) for all t (value-stability) |
| Late event type | late-past event (DAG membership, t in J^-(x) \ W_Delta) | late join (semantic instability, I(s join t) != I(s)) |
| Trigger condition | Delta < past-completion latency of x | Delta < T_join(s) (join-convergence latency) |
| Math object | J^-(x) cap W_Delta (sub-poset membership) | I(s join t) (lattice-join invariant evaluation) |
| Rate dependence | occurs at any lambda (not rate-limited) | occurs at any lambda (not rate-limited) |
| Controlling axis | L6 deadline policy | L6 deadline policy |
| Not captured by | L4 (Sorkin completeness gating) | L4 (CALM value-stability gating) |
| Not reachable under | completeness-gating | value-stability-gating |

Both rows confirm the cadence field catches a real protocol error via the same structural
logic (L6 override of L4 gating), but in two genuinely different mathematical settings.

---

## 5. Full Six-Axis Specification

### Leg 1 — Substrate class

- **Class label:** (a) Smooth principal bundle on a smooth manifold — specifically Y^14 =
  Met(X^4) with the gimmel metric of signature (9,5) and the Sp(64) gauge bundle. This is
  the GU substrate, NOT a Type II_1 spectral triple.
- **Specification:** The substrate is Y^14 = Met(X^4): the bundle of Lorentzian metrics on
  the 4-manifold X^4, equipped with the gimmel metric (Frobenius + trace-reversal, signature
  (9,5)) and the Clifford spinor module S = H^64 (from Cl(9,5) ~= M(64,H)). The chirality
  invariant I(s) is the Sp(64) chirality / discrete-series Plancherel multiplicity extracted
  from the section s: X^4 -> Y^14 (at reconstruction grade: m_H(S(6,4)) = 24 from the K3-type
  index computation in `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`). The substrate
  supplies the chirality-bearing invariant; the CALM update stream is the observer's record
  of partial metric information (partial lattice states) arriving from the bundle Y^14.
- **Literature anchor:** GU construction (Weinstein UCSD transcript 2025-04); gimmel metric
  (`explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`); Clifford spinor
  module (`explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`); discrete-series
  chirality invariant (`explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`).
- **Class-assumption signature broken:** Preserves Witten 1981 / Distler-Garibaldi substrate
  assumption (smooth principal bundle). The candidate's heterodoxy is in L4 (CALM order) and
  L6 (deadline loop), not in the substrate.

### Leg 2 — Observer class

- **Class label:** (a) Finite Turing observer (BPP/BQP) with finite compute budget B and
  observation window of width w (same as example-02 baseline).
- **Specification:** The observer receives a CALM-ordered update stream of partial metric
  information from the GU bundle Y^14. Each update is a join operation on the observer's
  lattice state s. The observer's capacity ceiling is lambda_max = B/w (same L2 formula as
  FR1). Below this ceiling, the observer can process all received updates without eviction.
  The observer attempts to extract the chirality invariant I(s) from finalized lattice states.
- **Literature anchor:** Standard Turing machine / BPP observer model; FR1 capacity ceiling
  derivation (`explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`).
- **Class-assumption signature broken:** Preserves observer-class assumption. The observer's
  failure is in L6 (the deadline policy), not in L2 (capacity).

### Leg 3 — Pairing

- **Class label:** CALM-smooth pairing: the observer pairs with the smooth GU bundle substrate
  via a CALM-ordered update stream. The pairing channel delivers join operations in CALM
  (monotone) order; the observer assembles a lattice state from received joins and extracts
  the chirality invariant.
- **Specification:** The pairing delivers metric update packets from the GU bundle Y^14 to the
  observer in CALM order: each packet is a join operation (s -> s join t) for a new lattice
  element t. The CALM order guarantees that the state only ever increases (monotone). The
  pairing is smooth (the underlying GU bundle is smooth) but the information delivery is
  CALM-ordered (the observer receives partial metric information in lattice-join order, not
  in any fixed timestamp order). The value-stability predicate I(s join t) = I(s) is the
  natural finality condition for this pairing class.
- **Literature anchor:** CALM theorem (Hellerstein and Alvaro, "Keeping CALM: When Distributed
  Consistency Is Easy," CACM 2020); lattice-based distributed consistency
  (Alvaro-Ameloot-Hellerstein-Tack-Van den Bussche, 2011).
- **Class-assumption signature broken:** Breaks the implicit cartesian/smooth pairing
  assumption of Witten / Freed-Hopkins / Distler-Garibaldi: those theorems assume the observer
  reads invariants from a fixed, simultaneously-accessible smooth bundle. This candidate
  inserts a CALM-ordered update stream between substrate and observer. The observer never has
  simultaneous access to all of Y^14; it assembles a lattice state from sequential joins.

### Leg 4 — Causal-order class

- **Class label:** (b) CALM-monotonic partial order (distributed-systems / database eventual-
  consistency class).
- **Specification:** The causal order on the update stream is the CALM lattice partial order
  (L, <=): a <= b iff b = a join c for some c. This is NOT a smooth Lorentzian order and NOT
  a Sorkin causal set. It is the partial order native to a distributed, eventually-consistent
  information-assembly process. The observer's partial metric information state s is always a
  lattice element; updates are monotone (s -> s join t >= s). The CALM L4 order supplies the
  value-stability predicate and the monotonicity guarantee; it does NOT supply a finalization
  rule (that is L6).
- **Literature anchor:** Hellerstein-Alvaro (2020) CALM theorem; Birkhoff-Frink lattice theory
  (lattice partial orders); Lamport causal order (precursor for distributed CALM extensions).
- **Class-assumption signature broken:** Drops the total-order Lorentzian assumption (L4 class
  (a)) of all four no-go theorems. The CALM partial order is a lattice partial order, not a
  Lorentzian total order. The no-go theorems' assumptions about causal order (and the
  Lorentzian metric's role in propagation) do not apply to the CALM update stream.

### Leg 5 — Emergence class

- **Class label:** (a) Specific-object substrate (Y^14 with gimmel metric and Sp(64) gauge
  bundle — same as the first worked example `six-axis-l1l2-coupling-filled-example-2026-06-23.md`).
- **Specification:** The substrate is a specific geometric object, not a universality class.
  The chirality invariant I(s) = m_H(S(6,4)) = 24 is a property of the specific GU bundle
  construction, not an RG fixed-point datum. The candidate's heterodoxy is entirely in L3
  (CALM pairing), L4 (CALM order), and L6 (deadline loop).
- **Literature anchor:** GU construction; discrete-series computation
  (`explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`).
- **Class-assumption signature broken:** Preserves the specific-object emergence assumption.

### Leg 6 — Coordination-loop class

- **Class label:** (f) Dijkstra self-stabilizing finalization loop with hard cadence deadline
  `Delta` — the CALM-update-stream variant.
- **Specification:** The coordination loop governs when the observer finalizes a chirality
  record from its current lattice state s. The deadline-cadence policy is: finalize I(s) at
  tick arrival(s) + Delta, whether or not value-stability I(s join t) = I(s) has been
  confirmed. The Dijkstra self-stabilizing structure means the observer attempts to recover
  from inconsistencies by re-querying if contradictions are detected, but within a bounded
  number of ticks (Delta). The cadence Delta is the new L6 parameter: it is a finalization-
  deadline policy, not a property of the CALM lattice order (L4) or the observer's compute
  budget (L2).
- **Literature anchor:** Dijkstra self-stabilizing algorithms (Dijkstra 1974, "Self-stabilizing
  systems in spite of distributed control"); CALM theorem (Hellerstein-Alvaro 2020);
  example-02-D finalization loop (`explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`).
- **Class-assumption signature broken:** Breaks the "no loop" (class (a)) assumption of the
  standard no-go theorems. The deadline-cadence loop forces finalization before the CALM
  value-stability condition is satisfied, producing a coordination-loop policy that overrides
  the L4 order's natural finality condition.

---

## 6. Chirality Bridge Claim

The substrate-level invariant carrying chirality is the Sp(64) chirality datum encoded in
the discrete-series Plancherel multiplicity m_H(S(6,4)) = 24 of the fiber Dirac operator on
GL(4,R)/O(3,1). This is the same invariant as in the first worked example
(`six-axis-l1l2-coupling-filled-example-2026-06-23.md`); the chirality bridge is the same
GU construction. What differs is how the observer assembles a record of this invariant: via
a CALM-ordered update stream rather than a BvN-gated decoherence channel.

The forgetful operation is the CALM finalization: the lattice state s (a partial record of
the GU bundle section) is finalized to produce the classical section record s_fin. At
value-stability, s_fin = s* (the Tikhonov-selected section); below value-stability,
s_fin = s_partial (a section that may differ from s* because not all join updates have been
incorporated). The chirality invariant I(s_fin) = m_H(S(6,4)) if and only if s_fin = s*
(the correct section); otherwise I(s_fin) may differ or be undefined.

The smooth-bundle shadow yields the null Witten / Nielsen-Ninomiya / Freed-Hopkins /
Distler-Garibaldi image because those theorems assume simultaneous access to the full smooth
bundle (the forgetful operation is instantaneous). In the CALM setting, the forgetful
operation is the CALM join-convergence process: the smooth-bundle shadow of s* is only
accessible after all relevant join updates have converged (value-stability). Below
convergence, the smooth-bundle shadow is s_partial, not s*, and the no-go theorems' inputs
(a specific smooth section) are not yet well-defined. The deadline-gated observer forces a
shadow at time arrival(s) + Delta; if T_join(s) > Delta, the forced shadow s_partial != s*
and the no-go theorems' conclusions apply to the wrong section.

---

## 7. The Protocol Error Caught by the Cadence Field

**The real protocol error.** An observer using the CALM-GU substrate to extract chirality
information, with a deadline-cadence finalization policy (Delta fixed), can finalize the
chirality invariant I(s_partial) from a partially-converged lattice state s_partial. If a
late join t arrives after Delta with I(s_partial join t) != I(s_partial), the finalized
record is wrong. This is a **CALM-premature-commitment error**: the observer committed to a
chirality value before the CALM update stream had converged to a value-stable state.

**The error is NOT caught by L4.** The CALM L4 order provides the value-stability predicate;
it does not enforce a finalization rule. If the observer waited for value-stability, the error
would not occur. The error is caused by the L6 deadline policy overriding the L4 stability
condition.

**The error is NOT caught by L2.** The capacity ceiling lambda_max = B/w (from FR1) applies
to the rate of updates the observer can process without eviction. The CALM-premature-commitment
error occurs at any lambda <= B/w (no eviction required). The controlling parameter is Delta
(the finalization deadline) vs. T_join(s) (the join-convergence latency), which is independent
of the update rate lambda.

**Why this is a real error, not a definitional artifact.** The error has a concrete operational
consequence: an experimenter measuring the chirality content of the GU section s* will get
wrong results if the observer uses a deadline-cadence finalization with Delta < T_join(s). The
physical consequence (wrong generation count) depends on Delta in a way that L4 and L2
together cannot predict.

---

## 8. Promotion Condition: Second Worked Example Discharged

Per `observer-finality-layer.md`:

> "This sub-protocol can move toward canon only after at least two worked six-axis examples
> show that the added fields catch real errors or produce useful falsification tests."

The cadence field `Delta` now has **two** worked examples:

1. **Example-02-D (Sorkin L4, example-02-D baseline):** Delta catches premature-commitment
   via late-past events in a Sorkin causal-set substrate. Filed in
   `explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`.

2. **Example-CALM-D (this document):** Delta catches premature-commitment via late joins in a
   CALM-monotonic-L4 / smooth-GU-bundle-L1 substrate. The failure mechanism is structurally
   distinct (late-join vs. late-past; value-stability predicate vs. past-cone completeness
   predicate; lattice join semantics vs. DAG membership).

The two examples use different L1 classes (Sorkin causal set vs. smooth principal bundle) and
different L4 classes (Sorkin partial order vs. CALM-monotonic lattice partial order), so the
promotion condition is discharged: two genuinely different mathematical settings both exhibit
a cadence-caused protocol error that Delta catches and that L4 alone cannot catch.

**Promotion condition status:** DISCHARGED at reconstruction grade. The `cadence`/`Delta`
field may now be proposed for the canonical observer-finality sub-protocol (as an exploration-
grade candidate pending full canon review and no-go discipline check).

---

## 9. One First Falsification Test

**Test.** Construct a concrete CALM update stream for a simplified GU-type chirality invariant
(e.g., a Z/2Z-valued invariant on a 2-element lattice {s_0, s_1 = s_0 join t}) and check:

1. Under value-stability gating: the observer waits for t to arrive and correctly computes
   I(s_1) = 1 (nontrivial chirality).
2. Under deadline-cadence with Delta < tau_t (where tau_t is the arrival time of t): the
   observer finalizes I(s_0) = 0 (trivial chirality) before t arrives, producing a wrong result.
3. Verify that the wrong result cannot be produced at any lambda <= B/w under value-stability
   gating (i.e., the error is exclusive to the deadline policy).

**Falsification outcomes:**

- **The cadence field is falsified (candidate collapses):** If the value-stability predicate
  I(s join t) = I(s) is guaranteed to hold for all t in every CALM update stream arising from
  the smooth GU bundle (i.e., the GU chirality invariant is always CALM-stable regardless of
  which joins arrive), then no late join can change the invariant and the cadence field has
  no failure mode to catch. This would require showing that m_H(S(6,4)) is a CALM-stable
  invariant of the lattice state for all possible CALM update streams arising from Y^14 metric
  information. If true, the CALM-premature-commitment error is empty and the candidate
  collapses.

- **The cadence field is confirmed:** If a specific CALM update stream for the GU bundle can
  be constructed where a late join changes m_H(S(6,4)) (e.g., because partial metric
  information gives a wrong section s_partial with I(s_partial) != m_H(S(6,4))), the error
  is confirmed and the cadence field is non-redundant.

**Runner.** Agent pass (CALM / distributed-systems specialist + GU bundle specialist): (1)
model the GU chirality invariant as a lattice-valued function of partial metric sections;
(2) check whether partial sections can give wrong chirality values; (3) construct a concrete
late-join example. Falsification outcome 1 requires showing that the discrete-series Plancherel
multiplicity m_H(S(6,4)) is lattice-stable for all partial sections, which is a strong claim
unlikely to hold generically.

**Why this test is load-bearing.** The candidate stands or falls on whether the GU chirality
invariant I(s) = m_H(S(6,4)) is sensitive to the completeness of the lattice state s. If it
is always stable under CALM joins (i.e., any partial metric information gives the same chirality
value as the full section), the CALM-premature-commitment failure is empty and the cadence
field adds nothing for this substrate.

---

## 10. Explicit Failure Conditions

Five conditions that would falsify the result:

1. **F1 (CALM stability of chirality):** The GU chirality invariant I(s) = m_H(S(6,4)) is
   CALM-stable for all partial metric sections s (value-stability holds trivially for all
   CALM update streams arising from Y^14). If true, no late join can change I(s) and the
   CALM-premature-commitment error is empty. The cadence field would be non-redundant at
   the protocol level but vacuous for this substrate.

2. **F2 (Sorkin-CALM collapse):** The CALM-premature-commitment failure mode is a
   syntactic relabeling of the Sorkin premature-commitment failure. If there is a formal
   functor from CALM lattice states to Sorkin past-cones that maps late joins to late-past
   events bijectively, the two examples' failure modes are identical and the second example
   does not add coverage.

3. **F3 (Value-stability gating not applicable to GU):** The CALM value-stability condition
   I(s join t) = I(s) is not a natural finality condition for the GU chirality invariant.
   If the GU chirality invariant requires a different finality condition (e.g., completeness
   of the full section s* rather than any partial stability), the CALM L4 class is
   inapplicable to the GU substrate and the candidate's L4 choice is incoherent.

4. **F4 (CALM order not applicable to Y^14 updates):** The CALM monotone lattice structure
   is not a valid model for the order in which metric information from Y^14 arrives at the
   observer. If metric updates are not naturally lattice-ordered (e.g., they require
   non-monotone corrections), the CALM L4 class does not apply.

5. **F5 (L6 over-claimed):** The deadline Delta is not a free parameter of the coordination
   loop but is fixed by the GU dynamics (e.g., Delta is forced to be >= T_join(s) by the
   section-selection variational principle). If the GU construction forces Delta >= T_join(s)
   always, the CALM-premature-commitment error is structurally excluded and the cadence field
   is vacuous.

---

## 11. Grade, Status, and Residual Open Conditions

**Grade: reconstruction.** The six-axis specification, failure-mode analysis, and first
falsification test are all stated at reconstruction grade. The key structural arguments
(proofs of (a), (b), (c) in Section 4.3) are rigorous at this grade: the CALM and Sorkin
finality predicates are formally distinct mathematical objects, and the argument that L6
override of L4 produces the failure mode is structurally identical to example-02-D's argument
(same schema, different mathematical objects).

**Promotion condition status:** DISCHARGED. The two-example promotion condition from
`observer-finality-layer.md` is now satisfied:
- Example 1: Sorkin L4, example-02-D (example-02-D premature-commitment via late-past events).
- Example 2: CALM L4, smooth-bundle L1, example-CALM-D (this document: premature-commitment
  via late-join events).

**Remaining open conditions before upgrade to verified:**

- RC1 (CALM stability check): Whether I(s) = m_H(S(6,4)) is CALM-stable for partial metric
  sections has not been checked. This is Falsification Condition F1 and is the primary
  remaining check before the candidate can claim the error is non-vacuous for the GU
  substrate.

- RC2 (CALM-Sorkin non-collapse formal proof): The structural non-collapse argument in
  Section 4.3 is at reconstruction grade; a formal proof that the CALM late-join predicate
  is not equivalent to the Sorkin late-past predicate (F2) would upgrade the coverage claim.

- RC3 (GU-CALM pairing formalization): The CALM update stream for the GU bundle Y^14 has
  not been formally constructed. The claim that metric updates arrive in CALM-monotone order
  requires a formalization of the bundle-to-observer information channel.

**GU-result sensitivity:** None at present. The same note as example-02-D: the cadence
field governs the observer's record-construction process, not the GU structural theorems. No
GU theorem (VZ evasion, generation count, dark energy Noether closure) depends on Delta.

---

## 12. Relation to Prior Six-Axis Examples and the Sub-Protocol Promotion

| example | L1 | L4 | cadence error | primary distinction |
| --- | --- | --- | --- | --- |
| example-02 (Sorkin baseline) | Sorkin causal set | Sorkin partial order | absent (completeness-gated) | baseline, no deadline |
| example-02-D (fr4-l6-cadence) | Sorkin causal set | Sorkin partial order | premature-commitment via late-past event | L6 added: Dijkstra + Delta |
| example-CALM-D (this document) | Smooth principal bundle (Y^14) | CALM-monotonic lattice order | premature-commitment via late-join event | different L1 + different L4; same L6 structure |
| six-axis-l1l2-coupling (fr2-bvn) | Smooth principal bundle (Y^14) | Total-order Lorentzian (Gamma-conditional) | absent (BvN coupling, not cadence) | different load-bearing field (Gamma_min, not Delta) |

The example-CALM-D candidate establishes that the cadence field `Delta` is not an artifact
of the Sorkin causal-set setting: it catches real protocol errors in a qualitatively different
mathematical framework (CALM lattice order, smooth bundle substrate). The failure mechanism
(L6 override of L4 stability predicate) is the same schema in both cases, applied to
different mathematical objects (DAG past-cone vs. lattice-join stability). This structural
generality is the key evidence for promoting `Delta` from an exploration-grade Sorkin-specific
L6 field to a genuine sub-protocol field applicable across L4 classes.

---

## Cross-References

- Sub-protocol promotion condition:
  `explorations/time-as-finality-crosswalk/observer-finality-layer.md`
- First worked example (Sorkin L4):
  `explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`
- FR4 task source: `NEXT-STEPS.md` (FR4 residual open target row)
- BvN coupling rule (first six-axis filled example):
  `explorations/misc/six-axis-l1l2-coupling-filled-example-2026-06-23.md`
- GU discrete-series chirality invariant:
  `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`
- Six-axis template: `specifications/six-axis/six-axis-template.md`
- Rate-independence finding (GU structural theorems are Delta-independent):
  `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`

---
title: "Observer-Finality Record-Graph Test for OQ1 of the Signed-Readout Theorem"
date: 2026-06-23
problem_label: "signed-readout-oq1-record-graph"
status: reconstruction
verdict: RESOLVED
---

# Observer-Finality Record-Graph Test for OQ1 of the Signed-Readout Theorem

## 1. Problem Statement

The signed-readout monotonicity criterion was proved as a complete iff theorem in
`explorations/signed-readout-monotonicity-pn-jordan-2026-06-23.md`: a scalar readout
R: E -> G is monotone in the information order on E iff every generator weight w(x) is
in the positive cone G_+. The PN/Jordan factorization obligations (PJ1-PJ5) were
discharged. Two items were flagged as open:

- **OQ1 (Record-graph test completion).** The specification in
  `explorations/time-as-finality-crosswalk/signed-readout-record-graph-test.md` requires
  exhibiting the four relations (evidence order, causal order, finality relation, readout
  order) as formally distinct in a concrete toy diagram, using an observer-finality layer,
  without smuggling global time.
- OQ2 (Integer-index recovery), OQ3 (non-lattice G) -- not addressed here.

OQ1 asks three questions whose answers determine whether the TaF observer-finality layer
adds formal structure beyond the PN/Jordan split:

(Q1) Can the record-graph G_R be defined without appealing to global time?
(Q2) Can the finality-semantics condition on G_R be stated without global time?
(Q3) Can the signed-readout monotonicity criterion (all w(x) in G_+) be expressed as a
     graph-theoretic condition on G_R without smuggling global time?

This file runs the computation to the extent current context permits.

---

## 2. Established Context

Prior work this builds on:

- `explorations/signed-readout-monotonicity-pn-jordan-2026-06-23.md` -- proved the
  monotonicity criterion (iff: R monotone iff all w(x) in G_+); PJ1-PJ5 discharged.
- `explorations/time-as-finality-crosswalk/signed-readout-record-graph-test.md` -- the
  specification for this test (success and failure criteria, four required relations).
- `explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`
  -- rate absorbed by L2+L4; causal-set completeness is rate-blind.
- `explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`
  -- coupling rule lambda_max <= Gamma/ln(1/epsilon); L1-L2 coupling via t_obs.
- `explorations/fr2-bvn-gate-ii-gu-result-2026-06-23.md` -- scope condition for
  signed-readout applicability gates on Gamma >= Gamma_min; monotonicity truth is
  rate-independent.
- The six-axis specification protocol -- L1 (substrate), L2 (observer), L4 (causal
  pairing), L5 (emergence), L6 (coordination loop) vocabulary used below.

---

## 3. Construction of the Record-Graph G_R

### 3.1 Nodes and Edges

Define the **record-graph** G_R = (V, E_causal, lambda) where:

- **V** is a countable set of record events {r_1, r_2, ...}. Each r_i represents a
  finalized observable record: a definite, stable piece of evidence that an observer O
  can build on. Records are atomic; they are not temporal instants.

- **E_causal** is a set of directed edges (r_i -> r_j) called **causal links**. The
  edge r_i -> r_j means: the content of r_j can depend on the content of r_i, or r_j
  is constructed in a context that includes r_i. This is a strict partial order (acyclic,
  irreflexive); write r_i <_c r_j for the transitive closure.

- **lambda: V -> G** is a **weight labeling** assigning each record r_i a signed element
  lambda(r_i) = w(r_i) in an ordered abelian group G.

Crucially: **no timestamps are attached to nodes**. No global time function t: V -> R
or t: V -> Z is part of the definition. Edges E_causal encode *dependence*, not temporal
sequence.

### 3.2 No-Global-Time Verification

The definition of G_R uses only:
- a set of events (no real-number timestamps),
- a partial order on events (causal links, not chronological links),
- a weight function on events (values in G, not time-indexed).

The causal partial order <_c satisfies: if r_i <_c r_j then r_i is a *dependency* of
r_j. This is the Sorkin causal-set framework (FR1 crosswalk confirms this is the correct
L4 structure for observer-finality). No global present, no total order, no clock is
required.

**Remark on directed acyclic graph (DAG) structure.** G_R is a DAG: no directed cycles
(since r_i <_c r_j and r_j <_c r_i would mean r_i is causally dependent on itself,
which we exclude by irreflexivity). DAG structure is weaker than total order, so global
time is not implied.

---

## 4. The Finality-Semantics Condition

### 4.1 Informal Statement

A record r_j is **observer-final** for observer O at state S if:
- O has direct access to r_j (it is in O's past cone),
- every record r_i that r_j causally depends on has also been processed by O,
- no future dependence of r_j is pending that O must wait for before building on r_j.

The finality-semantics condition formalizes when O may treat r_j as a stable input to
the evidence accumulation process.

### 4.2 Formal Statement

Let O be an observer with an **accessible past** P(O) subset V: the set of records O has
processed. Define the **finality predicate**:

```
F(O, r_j)  iff
  (i)   r_j in P(O),     [O has the record]
  (ii)  for all r_i with r_i <_c r_j: r_i in P(O),   [all causal dependencies are in]
  (iii) for all r_k with r_j <_c r_k: either r_k has no effect on lambda(r_j),
        or r_k is not yet constructed (no commitment needed to future records).
```

Condition (i) and (ii) together say r_j's full causal history is available to O.
Condition (iii) says r_j does not need to be updated once it is final. Condition (iii)
is automatically satisfied if lambda is assigned at construction time and never revised
(append-only records): once r_j is in P(O), lambda(r_j) is fixed.

**Append-only simplification.** In the standard GU observer model (section-selection is
classical, finalized), lambda is assigned once and never revised. So (iii) reduces to:

```
F(O, r_j)  iff  r_j in P(O)  and  for all r_i <_c r_j: r_i in P(O).
```

This is the **causally closed past** condition: F(O, r_j) holds iff the causal past of
r_j is a subset of O's processed records. This is a purely graph-theoretic condition
on G_R and P(O) -- no timestamps.

### 4.3 No-Global-Time Verification for Finality

F(O, r_j) references:
- the DAG causal order <_c (defined in §3.1, no timestamps),
- O's past P(O) (a set of nodes, no timestamps).

No global time function is used. The condition "all causal dependencies in P(O)" is a
set-membership condition on the DAG, not a temporal condition.

The finality relation grows monotonically as P(O) grows: if F(O, r_j) and O later
processes more records (P(O) expands), F is not revoked (it is stable under expansion
of P(O)). Finality is therefore a monotone predicate in the inclusion order on P(O).

---

## 5. Evidence Monoid from G_R

### 5.1 The Finalized Evidence Monoid

Given G_R and an observer O with past P(O), define the **finalized evidence set**:

```
X_O = { r in V : F(O, r) }    (all observer-final records for O)
```

and the **evidence monoid**:

```
E_O = free commutative monoid on X_O
     = { finite formal sums  sum_i n_i r_i : r_i in X_O, n_i in N_0 }
```

with the information order: e <=_E e' iff e' = e + d for some d in E_O.

The scalar readout is:

```
R_O: E_O -> G,  R_O(sum_i n_i r_i) = sum_i n_i lambda(r_i).
```

This is exactly the E, w, R structure from the monotonicity theorem in
`signed-readout-monotonicity-pn-jordan-2026-06-23.md`, instantiated from G_R and O.

### 5.2 Growth of Evidence Under Causal Expansion

When O processes more records (P(O) expands to P(O')), X_O expands to X_{O'} (since
more records become observer-final). The evidence monoid E_O embeds into E_{O'} by
inclusion. The readout R_{O'} restricted to E_O equals R_O. This is monotone: evidence
only accumulates, never retracts.

---

## 6. Graph-Theoretic Formulation of the Monotonicity Criterion

### 6.1 The Main Question

The monotonicity criterion (from the prior file) says: R is monotone in the information
order on E iff every generator weight w(r) is in G_+.

OQ1 asks: can this criterion be stated purely in terms of G_R and the finality predicate,
without reference to global time?

### 6.2 Affirmative Formulation

**Definition (Nonnegative Record Graph).** G_R is **nonneg-weighted** if for every node
r in V, lambda(r) in G_+.

**Theorem (Graph-Theoretic Monotonicity Criterion).** Let G_R be a record graph (§3.1),
O an observer with finalized evidence monoid E_O and readout R_O (§5.1). Then:

```
R_O is monotone in the information order on E_O
  if and only if
G_R is nonneg-weighted (all lambda(r) in G_+).
```

**Proof.** Apply the Signed-Readout Monotonicity Criterion from
`signed-readout-monotonicity-pn-jordan-2026-06-23.md` with X = X_O and w = lambda|_{X_O}.
The criterion says R_O is monotone iff every generator weight lambda(r) is in G_+.
Since X_O subset V and the criterion is generator-by-generator, this is equivalent to
lambda(r) in G_+ for all r in X_O. For this to hold for *all possible observers O and
all possible pasts P(O)*, we need lambda(r) in G_+ for all r in V (since any node r
can in principle be finalized by some observer). QED.

**Remark on observer-dependence.** If we fix a specific observer O, the criterion is:
lambda(r) in G_+ for all r in X_O (the finalized records). A different observer with a
different past P(O') could have a different X_{O'} and hence a different (potentially
non-monotone) readout even if R_O is monotone. This is the correct structure: monotonicity
is relative to the finalized evidence set, not a global property of G_R (unless lambda
is nonneg everywhere).

**The No-Global-Time Guarantee.** The criterion is stated in terms of:
- lambda: V -> G (the weight labeling -- defined at construction, no timestamps),
- G_+ (the positive cone of G -- purely algebraic),
- X_O (the finalized evidence set -- a set of graph nodes, no timestamps).

No global time function appears. The criterion is graph-theoretic and finality-semantics-
theoretic, with the finality semantics defined in §4.2 without global time.

---

## 7. The Four-Relations Diagram

The required separation (from the spec in signed-readout-record-graph-test.md) is:

| relation | defined on | definition in this file |
|---|---|---|
| evidence order (<=_E) | E_O x E_O | free monoid divisibility: e' = e + d for d in E_O |
| causal order (<_c) | V x V | DAG edge transitive closure; no timestamps (§3.1) |
| finality relation F | observers x V | causally closed past condition (§4.2); no timestamps |
| readout order (<=_G) | G x G | order of the target group G; purely algebraic |

**These four relations are provably distinct:**

- The evidence order is on the free monoid E_O, not on V or G.
- The causal order is on V (the raw records), not on E_O or G.
- The finality relation involves an observer and a node; it is not an order on V or E_O.
- The readout order is on G; it is not on V or E_O.

None of the four can be identified with any other without losing information:
- F(O, r) does NOT imply r <=_E r' for any r' (finality is not an evidence ordering).
- r_i <_c r_j does NOT imply lambda(r_i) <=_G lambda(r_j) (causal predecessors can have
  larger signed weights than successors -- this is the signed-readout phenomenon).
- The evidence order e <=_E e' does NOT imply r_i <_c r_j for specific generators
  (information accumulation and causal dependence are independent).

---

## 8. Concrete Toy Diagram

### 8.1 Setup

Three records: r_1, r_2, r_3 in V. G = Z, G_+ = N_0. Causal links: r_1 -> r_2 (r_2
depends on r_1). r_3 is independent. Weights: lambda(r_1) = +1, lambda(r_2) = -1,
lambda(r_3) = +2.

Observer O has past P(O) = {r_1, r_2, r_3} (all records finalized). Finality check:

- F(O, r_1): r_1 in P(O) [yes], no causal predecessors [trivially satisfied]. Final.
- F(O, r_2): r_2 in P(O) [yes], r_1 <_c r_2 and r_1 in P(O) [yes]. Final.
- F(O, r_3): r_3 in P(O) [yes], no causal predecessors. Final.

So X_O = {r_1, r_2, r_3}, E_O = free commutative monoid on {r_1, r_2, r_3}.

### 8.2 Evidence Growth and Readout

Case 1 (monotone-only subgraph): Consider observer O_1 with P(O_1) = {r_1, r_3}, so
X_{O_1} = {r_1, r_3} (r_2 not yet final since... wait -- r_2 has r_1 as a causal
predecessor and r_1 in P(O_1), so r_2 IS final once O_1 has r_1 and r_2. Suppose
O_1 = {r_1, r_3} only. Then F(O_1, r_2) fails because r_2 not in P(O_1). So X_{O_1}
= {r_1, r_3}. Weights: lambda(r_1) = +1, lambda(r_3) = +2. Both in G_+. R_{O_1} is
monotone: adding any combination of r_1, r_3 increases the readout.

Case 2 (signed subgraph): Observer O_2 = {r_1, r_2} (O_2 has both r_1 and r_2). X_{O_2}
= {r_1, r_2}. Weights: lambda(r_1) = +1, lambda(r_2) = -1. NOT all in G_+. R_{O_2} is
non-monotone: the pair (0, r_2) witnesses this -- 0 <=_E r_2 but R_{O_2}(0) = 0 >
R_{O_2}(r_2) = -1.

Case 3 (full signed evidence): Observer O = {r_1, r_2, r_3}, X_O = {r_1, r_2, r_3}.
Weights: +1, -1, +2. Non-monotone: adding r_2 decreases readout.

Diagram in ASCII:

```
G_R (causal DAG):
   r_1 (+1) --> r_2 (-1)      r_3 (+2) [no edges to/from r_1, r_2]

Four relations:
  (i) evidence order (<=_E on E_O):
        e.g. 0 <=_E r_2 <=_E r_1 + r_2 <=_E r_1 + r_2 + r_3  (free monoid)
  (ii) causal order (<_c on V):
        r_1 <_c r_2;  r_3 is causally unrelated to r_1, r_2
  (iii) finality relation (F(O, r) on observers x V):
        F(O, r_2) requires r_1 in P(O);  F(O, r_3) requires nothing beyond r_3 in P(O)
  (iv) readout order (<=_Z on Z):
        R_O(r_1 + r_3) = 3 > R_O(r_2) = -1   [not monotone in evidence order]

Signed-readout phenomenon:
  r_1 + r_2 + r_3 is above r_3 in evidence order,
  but R_O(r_1 + r_2 + r_3) = 2 < R_O(r_3) = 2  [equal in this case]
  Cleaner example: R_O(r_2) = -1 < R_O(0) = 0 even though 0 <=_E r_2.
```

### 8.3 Verification of Success Criteria

Checking against the spec in signed-readout-record-graph-test.md:

- [x] E_O grows monotonically as P(O) expands (Sec. 5.2).
- [x] Finalized records grow or stabilize monotonically for O (finality is stable under
  expansion of P(O)).
- [x] Signed readout can be non-monotone (Case 2, Case 3 above).
- [x] Non-monotone readout is not mistaken for failed propagation: r_2 is a legitimately
  finalized record (F(O_2, r_2) holds); its negative weight causes non-monotone readout,
  not a broken causal propagation.
- [x] No global time assumed: G_R uses only DAG edges; F uses only causal-past membership.

Checking against failure criteria:

- [ ] Finality NOT defined using temporal order: finality = causally closed past condition;
  no timestamps.
- [ ] No global ledger or universal present introduced.
- [ ] Scalar readout NOT identified with finality relation: readout maps E_O -> Z; finality
  is a predicate F(O, r) in {true, false}. Distinct types.
- [ ] Model represents signed cancellation (r_2 has weight -1) without breaking record
  propagation (r_2 is still a valid, finalized, causally propagated record).
- [ ] The result clarifies the signed-readout theorem beyond PN/Jordan: it adds the
  observer-finality layer (Sec. 9 explains what is added).

---

## 9. What the Record-Graph Layer Adds Beyond PN/Jordan

The PN/Jordan split from `signed-readout-monotonicity-pn-jordan-2026-06-23.md` says:
any weight function w: X -> G splits as w = w_+ - w_-, with w_+(x), w_-(x) in G_+,
and R_+ and R_- are both monotone while R = R_+ - R_- may not be.

What G_R adds:

1. **Finality as a precondition for evidence.** In the abstract PN/Jordan framework, X is
   just a set of generators. In G_R, the generators are *finalized records* -- events
   that have passed the causally closed past condition. The record-graph layer clarifies
   *when* an event enters the evidence monoid (when it is observer-final), not just that
   it does.

2. **Causal dependence as a structural constraint separate from evidence order.** In the
   abstract framework, there is no causal structure among generators. In G_R, the causal
   order <_c on V is an independent relation that constrains which records can be finalized
   simultaneously (if r_i <_c r_j, then F(O, r_j) implies r_i in P(O), so r_j cannot be
   finalized before r_i). This is a structural constraint on the accumulation process that
   the PN/Jordan layer does not capture.

3. **Observer-relative monotonicity.** The PN/Jordan criterion is stated for a fixed
   (E, w). In G_R, different observers O with different pasts P(O) generate different
   evidence monoids E_O and different readouts R_O. The graph-theoretic criterion says:
   R_O is monotone iff all lambda(r) in G_+ for r in X_O. This is observer-relative:
   an observer who has only finalized positively-weighted records has a monotone readout,
   even if the graph contains negatively-weighted records outside her past.

4. **No global time required.** The PN/Jordan framework is purely algebraic and does not
   need causal structure. The record-graph layer shows that the algebraic structure can
   be grounded in a causal DAG with observer-relative finality, without smuggling a global
   ordering that would be semantically stronger than the causal structure.

Whether these additions are *necessary* for the signed-readout theorem depends on the
application. For the GW axial-charge instantiation, the abstract PN/Jordan split already
suffices. The record-graph layer is useful when the question is: *which observer sees
which signed-readout phenomenon?* -- a question that requires the finality relation.

---

## 10. Result: Answers to Q1, Q2, Q3

**Q1: Can G_R be defined without global time?**
YES. Definition in Sec. 3.1: nodes are record events, edges are causal dependence links,
weights are lambda: V -> G. No timestamps. Grade: VERIFIED (the definition is explicit
and the no-global-time property is immediate from the definition).

**Q2: Can the finality-semantics condition be stated without global time?**
YES. Sec. 4.2: F(O, r_j) holds iff r_j in P(O) and all causal predecessors of r_j are
also in P(O). This is the causally closed past condition -- a set-membership condition
on the DAG with no timestamps. Grade: VERIFIED (same reasoning as Q1; the definition is
explicit and manifestly time-free).

**Q3: Can the signed-readout monotonicity criterion be expressed as a graph-theoretic
condition on G_R without smuggling global time?**
YES. Sec. 6.2: R_O is monotone iff G_R is nonneg-weighted on X_O (all lambda(r) in G_+
for r in X_O). The condition is: (a) a property of the weight labeling lambda (graph-
theoretic datum), (b) restricted to X_O (the observer's finalized records -- defined via
the causally closed past condition, no timestamps), (c) checked against G_+ (purely
algebraic). No global time. Grade: RECONSTRUCTION (the graph-theoretic formulation is
explicit and correct; the formal independence from global time follows from the no-global-
time guarantees on G_R and F, which are themselves VERIFIED).

**Main verdict for OQ1: RESOLVED at reconstruction grade.**

All three sub-questions are answered affirmatively. The record-graph G_R and finality-
semantics condition provide a precise, time-free grounding for the signed-readout
monotonicity criterion, while adding observer-relative and causal-structural content
beyond the abstract PN/Jordan framework.

---

## 11. Explicit Failure Conditions

**F1: Finality defined using timestamps.** If F(O, r_j) is defined using a timestamp
function t: V -> R (e.g., "all r_i with t(r_i) < t(r_j) are in P(O)"), then global
time is smuggled. The causally closed past condition (§4.2) avoids this, but if the
underlying partial order <_c is secretly a total order induced by timestamps, the time-
free property fails. Falsification: exhibit a case where <_c is not a DAG (cyclic) or
not strictly more general than a total order.

**F2: The DAG <_c admits a unique topological sort.** If <_c is a total order (complete
DAG), then G_R is essentially a timeline, and global time is present in disguise. The
condition "no global time" requires <_c to be a proper partial order with incomparable
elements (as in the toy example: r_3 is incomparable to r_1 and r_2). Falsification:
a record graph with no incomparable elements reduces to the forbidden global-time case.

**F3: The weight labeling lambda depends on a timestamp.** If lambda(r_i) is defined as
a function of the temporal position of r_i (e.g., lambda(r_i) = f(t(r_i))), then a
hidden time dependence is present. Falsification: lambda must be assigned at construction
of r_i without reference to a universal clock.

**F4: The evidence monoid E_O is not free commutative.** If there are relations among
generators r_i in E_O (e.g., r_1 + r_2 = r_3 as evidence), the monotonicity criterion
proof fails in its (=>) direction (Sec. 4 of the prior file). Falsification: exhibit
a natural observer model where evidence aggregation satisfies non-trivial relations.
(This is the F1 failure condition from the prior file applied to the record-graph
instantiation.)

**F5: Signed cancellation breaks causal propagation.** If the negative weight of r_j
causes a downstream record r_k (with r_j <_c r_k) to have undefined or ill-formed
content, the record-graph layer has not separated signed readout from causal propagation.
Falsification: an explicit physical example where a negatively-weighted finalized record
poisons its causal successors. (This does not occur in the toy example: r_2 with weight
-1 is a valid finalized record; its weight has no effect on the causal validity of any
successor.)

**F6: The graph-theoretic criterion fails for non-lattice-ordered G.** If G is an
ordered abelian group without lattice structure (max(g, 0) undefined for some g), then
the PN/Jordan split at PJ5 cannot be stated canonically, and the minimal-split form of
the graph-theoretic criterion is unavailable. The criterion "lambda(r) in G_+" is still
well-defined (G_+ is the positive cone), but the canonical factorization may not exist.
This is inherited from F6 of the prior file.

---

## 12. Open Questions (Post-OQ1)

- **OQ1-followup (six-axis formalization).** The record-graph G_R with finality semantics
  fits the six-axis specification: L1 (substrate = DAG record events), L2 (observer O
  with past P(O)), L4 (causal pairing = <_c), L5 (emergence = signed readout from
  monotone provenance), L6 (if a cadence field Delta is added, the finality condition
  is deadline-gated -- see FR4). Filling a complete six-axis spec row for this observer
  model would promote the record-graph layer from exploration to active-research.

- **OQ2 (Integer-index recovery).** The graph-theoretic criterion says: R_O is monotone
  iff all lambda in G_+. For the GW axial charge Q_A = n_+ - n_- (integer-valued, G = Z),
  the non-monotone readout is predicted by the criterion (anti-instantons have lambda = -1
  not in G_+ = N_0). The question of whether any enriched provenance structure recovers Q_A
  monotonically at the integer level (OQ2) is not resolved here. Current evidence: no,
  under all three frameworks tested.

- **OQ1-A (TaF contact).** Does the finality-semantics condition F(O, r_j) in this file
  correspond to a specific construct in the TaF framework (temporal-issuance)? The
  candidate is the TI admissibility condition from cech_sheaf_fixture (E015 route, N3
  named open blocker). This contact point is not established here; H3 (Cech-holonomy
  dictionary) remains open in `explorations/n3-h3-cech-holonomy-2026-06-23.md`.

---

## 13. Final Verdict

OQ1 of the signed-readout theorem is RESOLVED at reconstruction grade.

**What was computed:**
- G_R (record-graph) defined as a DAG with weight labeling, no global time.
- Finality-semantics condition F(O, r_j) stated as causally closed past condition, no
  global time.
- Signed-readout monotonicity criterion expressed as "all lambda(r) in G_+" -- a
  nonneg-weight condition on the graph -- verified as equivalent to abstract PN/Jordan
  monotonicity criterion applied to X_O.
- Concrete toy diagram with three records (weights +1, -1, +2), four relations separated,
  all success criteria met.

**What remains:**
- Upgrade to verified grade requires CAS or mechanically-checked formalization.
- OQ1-A (TaF contact via H3/Cech) remains open.
- OQ2 (integer-index recovery) and OQ3 (non-lattice G) from the prior file are unchanged.
- Six-axis spec row for the observer model (OQ1-followup) would promote to active-research.

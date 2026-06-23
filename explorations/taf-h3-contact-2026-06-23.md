---
title: "TaF H3 Identification Hypothesis: Contact Assessment with the Signed-Readout Record-Graph"
date: 2026-06-23
problem_label: "taf-h3-contact"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# TaF H3 Identification Hypothesis: Contact Assessment with the Signed-Readout Record-Graph

## 1. Problem Statement

**What is being computed.** The signed-readout record-graph (OQ1, RESOLVED) established a
precise time-free causal structure for observer-finality in the GU framework. Its OQ1-A
left open the contact with the TaF H3 identification hypothesis. This file runs that
contact assessment at reconstruction grade.

**H3 (statement from T63 in time-as-finality repo).** The TaF finality presheaf sections
can be identified with flat Z/2Z-gauge connections on GU observer sections, such that the
Cech coboundary condition maps to the holonomy computation on the spin observerse Y_spin.
H3 is the load-bearing identification hypothesis for the T63 Holonomy Theorem's identity
form. Without H3, the theorem degrades from an identity to a structural analogy.

**OQ1-A (from signed-readout-oq1-record-graph-2026-06-23.md, §12).** Does the finality-
semantics condition F(O, r_j) in the record-graph correspond to a specific construct in the
TaF framework? The candidate is the TI admissibility condition from the cech_sheaf_fixture
(E015 route). This contact point was flagged as open with H3 as the named bridge.

**Bridge conditions being assessed here.** This file asks:

(BC-1) Does the record-graph finality condition F(O, r_j) correspond to a TaF admissibility
predicate?

(BC-2) Does the nonneg-weight condition on G_R (all lambda(r) in G_+) correspond to a TaF
Cech cocycle condition?

(BC-3) Does the GU monotone case (G_R^{GU}, ind_H = 24, all weights = +1) instantiate a
specific TaF finality structure that connects H3 to the signed-readout framework?

**Why this matters.** A confirmed bridge would show that the signed-readout record-graph
framework simultaneously provides:

- A time-free observer-finality layer for GU (already established by OQ1).
- A concrete instantiation of the TaF H3 identification at the level of the observer's
  finalized records, potentially reducing the H3 identification problem from an open
  cross-program question to a consequence of the record-graph structure.

---

## 2. Established Context

**Prior results this builds on (all at reconstruction grade or better):**

- `signed-readout-oq1-record-graph-2026-06-23.md` (RESOLVED): G_R defined as causal DAG
  with weight labeling; finality = causally closed past condition; monotonicity criterion
  = nonneg weights on X_O. No global time. OQ1-A flagged H3 as the residual open bridge.

- `signed-readout-oq2d-gu-contact-2026-06-23.md` (CONDITIONALLY_RESOLVED): G_R^{GU} =
  24-node bipartite graph (16 spin-1/2 + 8 RS), no edges, weight 1 per node. R_- = 0;
  T^{GU} = affine gauge-field space (connected, contractible); Atiyah-Schmid multiplicities
  A-independent.

- `n3-h3-cech-holonomy-2026-06-23.md` (OPEN): H3 is a named open blocker for T63 Holonomy
  Theorem. Three High-confidence entries of T63 are H3-independent (topology of Y_spin,
  Cech H^1 = Z/2Z, non-trivial class has holonomy = -1). The Medium-confidence entries
  (observer domain identification, finality presheaf to flat connection, restriction map
  to pullback) all require H3. Three closure conditions: C1 (type-bridge), C2
  (cech_sheaf_fixture execution), C3 (spacelike-separation fix).

- `n3-h3-cech-fixture-execution-2026-06-23.md` (fixture not available): cech_sheaf_fixture
  exists only as a prose/route requirement in temporal-issuance. No runnable artifact.
  H3 remains OPEN_BLOCKED_ON_FIXTURE_SPECIFICATION.

- `n5-discrete-series-gl4r-2026-06-23.md` (CONDITIONALLY_RESOLVED): ind_H(D_GU) = 24 from
  discrete-series harmonic analysis on SL(4,R)/SO_0(3,1); Flensted-Jensen split-rank = 1
  verified; K3-type X^4 selected.

- `fr2-bvn-layer5-promotion-gate-2026-06-23.md` and `fr2-bvn-gate-ii-gu-result-2026-06-23.md`
  (CONDITIONALLY_RESOLVED): BvN wall stated; GU result (D_A*theta = 0) changes truth value
  when Gamma < Gamma_min = ln(1/epsilon)/t_obs; L1-L2 coupling rule established.

---

## 3. Bridge Condition BC-1: Record-Graph Finality vs. TaF Admissibility

### 3.1 The Two Finality Conditions

**Record-graph finality (from OQ1).**

```
F(O, r_j)  iff
  (i)   r_j in P(O)
  (ii)  for all r_i <_c r_j: r_i in P(O)
```

This is the causally closed past condition. F(O, r_j) holds when r_j and all its causal
predecessors are in the observer's processed record set P(O).

**TaF admissibility (from temporal-issuance via n3-h3-cech-holonomy-2026-06-23.md and
E015 evidence).** The TI admissibility predicate (the target of the cech_sheaf_fixture)
is:

```
C_TaF(r_j)  iff
  The extension at r_j is C-typed: the new record (schema extension, arithmetic extension,
  or finality-class assignment) is consistent with the source axioms Ax(S) already
  established by prior records.
```

In the SBP (Schema Blueprint Protocol) language, this is: the record r_j is admissible iff
it can be coherently grafted onto the existing consistent extension schema without producing
a contradiction. The admissibility predicate enforces type-compatibility (C-typing) across
schema boundaries.

### 3.2 Structural Correspondence

The two finality conditions are NOT identical but are structurally parallel:

| feature | Record-graph F(O, r_j) | TaF admissibility C_TaF(r_j) |
|---------|----------------------|-------------------------------|
| What triggers finality | r_j in P(O) + all causal predecessors in P(O) | r_j consistent with accumulated schema Ax(S) |
| Order structure | Causal DAG partial order <_c on V | Schema-extension order on records |
| Time-free? | YES (DAG is partial order, no timestamps) | YES (TaF SBP stages are finality-ordered, not time-ordered) |
| Monotone? | YES (F once true, stays true as P(O) expands) | YES (C-typing is monotone: once admitted, an extension is not un-admitted by later extensions) |
| Key difference | Causal accessibility (who has processed what) | Type-consistency (what can be coherently added) |

**Bridge result (BC-1).** The record-graph finality condition F(O, r_j) is a *causally-
grounded admissibility predicate*: it says r_j is admissible to O's evidence accumulation
precisely when r_j has been causally made accessible and its full causal history is in O's
scope. The TaF C_TaF admissibility predicate is a *type-consistency-grounded admissibility
predicate*: it says r_j is admissible to the schema when r_j does not contradict prior
schema elements.

**Both predicates are admissibility predicates in the sense of the observer-finality layer
(observer-finality-layer.md).** The finality sub-protocol asks: "What makes a record
stable enough to build on?" Both conditions answer this question from different sides:

- F(O, r_j) answers from the *causal-access* side: O can build on r_j when O has causally
  accessed its full dependency chain.
- C_TaF(r_j) answers from the *schema-consistency* side: the system can build on r_j when
  r_j is type-consistent with the accumulated schema.

These are two different implementation choices for the finality relation in the six-axis
observer-finality sub-protocol (L2 field: finality relation). They are not the same object.

**Consequence for H3.** H3 requires that F (the TaF finality presheaf sections) be
*identified with* flat Z/2Z-gauge connections on GU observer sections. The record-graph
F(O, r_j) is a finality *predicate* (not a presheaf section), and the TaF C_TaF is an
admissibility *predicate* (not a Z/2Z gauge connection). BC-1 establishes a structural
parallel between the two admissibility predicates but does NOT provide the type-bridge
from combinatorial D1 profiles to smooth Z/2Z gauge connections that H3 requires.

**BC-1 verdict: Structural parallel established; full identification requires C1 (type-
bridge from combinatorial to smooth).**

---

## 4. Bridge Condition BC-2: Nonneg Weights vs. Cech Cocycle Condition

### 4.1 The Two Positivity/Cocycle Conditions

**Record-graph nonneg condition (from OQ1 monotonicity theorem).**

```
R_O is monotone iff all lambda(r) in G_+ for r in X_O.
```

For G = Z, G_+ = N_0: all weights are non-negative integers. The monotone case is R_- = 0.

**TaF Cech cocycle condition (from T63 and n3-h3-cech-holonomy-2026-06-23.md).** A Cech
1-cochain c(alpha, beta) in Z/2Z on the four-context CHSH cover satisfies the coboundary
condition iff its holonomy = +1. The non-trivial class has c(alpha, beta) values (+1,-1,+1,+1)
and holonomy = product = -1 (non-trivial). The trivial class has holonomy = +1.

The signed parity product around the 4-cycle equals -1 (the quantum contextuality signal).

### 4.2 The Sign Structure

Both conditions involve a signed structure:

- In the record-graph: weights can be positive or negative; monotone iff all positive.
- In the Cech computation: transition functions are +1 or -1 in Z/2Z; coboundary class
  iff holonomy = +1 (trivial); non-trivial holonomy = -1.

The GU monotone case (G_R^{GU}, all weights = +1) corresponds to the *trivial* Cech class
(holonomy = +1) under a proposed sign-correspondence: positive weight ~ +1 transition,
negative weight ~ -1 transition.

However, this correspondence has a structural mismatch:

- The nonneg condition in G_R is about the *accumulated readout* being monotone (the sum
  of weights does not decrease when evidence is added).
- The Cech coboundary condition is about a *product* of transition functions around a loop
  being trivial.

The sum-vs-product distinction is fundamental: in Z, the sign convention is additive; in
Z/2Z, it is multiplicative. A weight of -1 in Z (contributing negative to an additive
readout) and a transition function of -1 in Z/2Z (contributing -1 to a multiplicative
holonomy) are analogous in sign but not isomorphic in algebraic structure.

**The connection factor.** There is a non-trivial bridge available via the CHANGE in
readout versus the VALUE of the readout. The Cech cohomology detects whether the readout
changes around a loop (holonomy = product of changes). The signed-readout non-monotonicity
detects whether the readout decreases when evidence is added. Both are questions about
*obstruction to monotone accumulation* but they are measured differently:

- Cech H^1 measures: is the transition around a 4-cycle trivial?
- Non-monotone readout measures: does adding a record decrease the readout?

Both can be seen as instances of a more general question: does the readout have a signed
obstruction that prevents monotone behavior? This is the shared structural form.

**BC-2 verdict: Shared signed-obstruction structure identified; the algebraic relationship
is Z (additive, record-graph) vs. Z/2Z (multiplicative, Cech) and is not a direct
identification. A map Z -> Z/2Z (reduction mod 2) sends non-monotone readout to -1
holonomy in specific cases, but this requires a bridge construction not currently available.**

---

## 5. Bridge Condition BC-3: GU Monotone Case vs. TaF Finality Structure

### 5.1 The GU Monotone Case in the Record-Graph

From signed-readout-oq2d-gu-contact-2026-06-23.md, the GU record-graph G_R^{GU} is:

```
V = 24 nodes (16 spin-1/2 + 8 RS), E_causal = {}, lambda(v) = 1 for all v.
R(e_max) = 24, R_- = 0.
```

This is the maximally monotone case: every weight is +1, every node contributes positively.
The readout is simply the cardinality of the observer-final record set.

### 5.2 TaF Finality Structures and the Monotone Limit

In the TaF framework, a fully consistent schema extension chain S_0 -> S_1 -> ... -> S_n
where every extension is C-typed and no record contradicts prior records is the analog of
the monotone case. In this case:

- Every admissibility check passes: C_TaF(r_j) = true for all r_j.
- The schema accumulates monotonically: Ax(S_n) = Ax(S_0) + admitted extensions.
- No "retraction" occurs: once an extension is admitted, it stays.

This is the TaF analog of the nonneg-weight G_R: a fully consistent extension chain
corresponds to a record-graph where all finalized records are positively weighted.

The GU generation count (ind_H = 24) sits at this fully consistent extreme: there are
no "anti-generation" nodes (R_- = 0), and all 24 H-lines contribute positively and
independently. The TaF analog would be a schema extension chain of length 24 with no
contradictions.

**Key structural contact.** The TaF framework's most basic consistency condition --
that a schema extension is non-contradictory -- plays the role of the monotonicity
criterion in the record-graph. Both say: the accumulated information is consistent
(non-contradictory / non-decreasing-in-value).

**BC-3 verdict: Structural contact established. The GU monotone case (G_R^{GU}, ind_H = 24,
R_- = 0) corresponds to the TaF fully-consistent extension chain. This is not a new
derivation of H3 but is a structural echo of H3 at the level of the record-graph.**

---

## 6. The Central H3 Contact Assessment

### 6.1 What the Record-Graph Makes Precise About H3

The record-graph construction provides three precise observations about H3:

**Observation 1: H3 requires a type-bridge that the record-graph cannot supply.**

H3 says: F(U_alpha) [TaF finality presheaf section] = flat Z/2Z-connection on sigma_alpha(X_alpha) [GU gauge section]. The record-graph provides a finality predicate F(O, r_j) (a boolean predicate on observer-record pairs) and a weight function lambda: V -> G (a signed valued assignment to records). Neither of these is a presheaf section or a gauge connection.

The record-graph makes the type-bridge requirement concrete: to instantiate H3 in the record-graph language, one would need to:

- Identify finality presheaf sections F(U_alpha) with elements of the evidence monoid E_O (or sections of a sheaf over the record-graph).
- Identify flat Z/2Z-gauge connections with weight functions lambda: V -> {+1, -1} subset Z/2Z.
- Show that the restriction map (sheaf restriction) corresponds to causal pullback on the record-graph.

This is a precise version of the H3 bridge problem. The type-bridge C1 from n3-h3-cech-holonomy-2026-06-23.md has this exact content.

**Observation 2: The finality-semantics condition (causally closed past) is the correct
analog of TaF admissibility on the GU side.**

This was established in BC-1. The causally closed past condition F(O, r_j) is the unique
natural finality condition for the GU observer model that is time-free, monotone, and
compatible with the causal structure of Y^14. TaF admissibility C_TaF is its counterpart
on the temporal-issuance side.

**Observation 3: The non-monotone case of the record-graph (R_- > 0) corresponds to
the non-trivial Cech class (holonomy = -1) via a sign correspondence.**

The signed-readout phenomenon (adding a record decreases the readout) and the Cech
cohomology non-triviality (transition functions around a loop multiply to -1) both detect
a signed obstruction to simple accumulation. The specific map between them would require
constructing a Z-to-Z/2Z reduction that maps the PN/Jordan split (R_+, R_- in N_0) to
the Cech class in Z/2Z.

A candidate map: given G_R with weights in Z, define the Cech cocycle value
c(alpha, beta) = (-1)^{delta_{-}(alpha cap beta)}, where delta_{-}(S) is the parity of the
number of negatively-weighted records in S. Then:

- Monotone G_R (all weights >= 0): c(alpha, beta) = +1 everywhere, holonomy = +1
  (trivial Cech class).
- Non-monotone G_R (some weight = -1): c(alpha, beta) = -1 on the region containing the
  negative-weight record, holonomy = -1 (non-trivial Cech class, if the loop traverses
  this region an odd number of times).

This map is not derived from H3; it is a proposed construction that would make H3 a
consequence of the record-graph structure. Whether this construction survives the type-
bridge check (C1: the combinatorial D1 profiles must embed into smooth Z/2Z gauge data)
is the blocking open question.

### 6.2 Bridge Conditions Summary

| condition | status | gap |
|-----------|--------|-----|
| BC-1: F(O,r_j) parallels TaF admissibility | STRUCTURAL PARALLEL (reconstruction) | Full identification requires C1 (type-bridge from combinatorial to smooth) |
| BC-2: Nonneg weights parallels coboundary condition | SIGNED-OBSTRUCTION ECHO (exploration) | Z-additive vs. Z/2Z-multiplicative gap; requires explicit Z -> Z/2Z reduction map |
| BC-3: GU monotone case parallels TaF consistent extension | STRUCTURAL ECHO (reconstruction) | Not a derivation of H3; a consequence at the record-graph level |

### 6.3 What Makes Contact vs. What Remains Open

**Contact is made (reconstruction grade) on:**

(i) The FORM of finality: both GU record-graph finality and TaF admissibility are monotone
admissibility predicates in the observer-finality sub-protocol vocabulary.

(ii) The SIGN structure: both the record-graph non-monotonicity (R_- > 0) and the Cech
non-trivial holonomy (product = -1) detect signed obstructions to simple accumulation.

(iii) The MONOTONE EXTREME: GU ind_H = 24 (all weights +1, R_- = 0) corresponds to the
TaF fully-consistent extension chain (no contradictions, all C_TaF checks pass).

**What does NOT make contact yet:**

(iv) TYPE BRIDGE: The precise identification F(U_alpha) = flat Z/2Z-connection. The
record-graph provides F(O, r_j) as a predicate, not a gauge connection. Bridging requires
discretizing the gauge field to Z/2Z data, which is the C1 condition.

(v) COCYCLE DERIVATION: The cech_sheaf_fixture must show that C-typed admissibility
FORCES cocycle values (not just accepts preselected ones). This is C2.

(vi) SPACELIKE OVERLAP: The geometric identification sigma_A(X_A) cap sigma_B(X_B) for
spacelike-separated observers is undefined unless the fiber-bundle identification over
distinct spacetime points is specified. This is C3.

---

## 7. The Positive Result: A Weakened H3

The computation above establishes a weakened version of H3 that does not require the
cech_sheaf_fixture:

**Weakened H3 (W-H3).** In the signed-readout record-graph framework:

The GU finality condition F(O, r_j) [causally closed past] and the TaF admissibility
condition C_TaF(r_j) [type-consistent schema extension] are both instances of the abstract
observer-finality sub-protocol's finality relation field. They are parallel implementations
of the same abstract concept of "stability sufficient to build on," in two different
substrate contexts (GU causal graph, TaF schema extension chain).

As a consequence:

- The monotone case of the GU signed-readout framework (G_R^{GU}, ind_H = 24) corresponds
  to the TaF fully-consistent extension chain.
- The non-monotone case (R_- > 0 in the abstract framework) corresponds to the TaF Cech
  non-trivial class via the sign-obstruction echo.

W-H3 is weaker than H3: it gives a structural correspondence at the level of abstract
observer-finality, not the specific identification of finality presheaf sections with gauge
connections. W-H3 does not require C1, C2, or C3.

**W-H3 is CONDITIONALLY_RESOLVED at reconstruction grade** by the combination of:
- OQ1 (record-graph construction, RESOLVED).
- BC-1 through BC-3 (structural parallels, this file).
- n3-h3-cech-holonomy-2026-06-23.md (H3 anatomy).

**Full H3 remains OPEN** pending C1 (type-bridge), C2 (fixture execution), and C3
(spacelike-overlap fix), as in n3-h3-cech-holonomy-2026-06-23.md.

---

## 8. The Bridge Conditions as Falsification Tests

The following conditions would falsify the structural parallels established above:

**F1: The TaF admissibility predicate is NOT monotone.** If C_TaF can un-admit a
previously admitted extension (a retraction event), the BC-1 structural parallel fails:
the record-graph finality F(O, r_j) is stable under expansion of P(O), but C_TaF would
not be stable under expansion of Ax(S). Falsification: exhibit a TI execution trace where
a stage-n extension is retracted at stage n+1.

**F2: The sign correspondence (BC-2) is not a natural map.** If the only map from Z-
weighted records to Z/2Z Cech classes requires stipulating the cocycle values (rather than
deriving them from the weight function), then the proposed c(alpha,beta) = (-1)^{delta_{-}}
map is not canonical and BC-2 degrades to a labeling choice. Falsification: show that any
Z -> Z/2Z reduction map must make additional choices not determined by the record-graph
weight function.

**F3: The GU monotone case corresponds to a DIFFERENT Cech class than expected.** If the
all-weights-+1 GU record-graph corresponds to the non-trivial Cech class (holonomy = -1)
rather than the trivial class (holonomy = +1), the BC-2 sign correspondence is inverted.
Falsification: a cohomological computation on the GU generation-count sector showing
H^1 != 0.

**F4: W-H3 is absorbed by an existing framework.** If the structural parallel between
GU finality and TaF admissibility is entirely captured by an existing concept (e.g.,
both are instances of monotone convergence in a metric space, or both are instances of
the algebraic completion of a partial order), then W-H3 adds no new content. Falsification:
exhibit a prior framework that already accounts for both finality conditions and their
sign structure.

**F5: C1 is provably unconstructible.** If the D1 finality profiles contain structure
(non-finitary, order-theoretic, semantic) that cannot be embedded into flat Z/2Z gauge
data without information loss (e.g., D1 profiles encode continuous data that Z/2Z cannot
represent), then H3 is unstatable, and the BC-1 structural parallel identifies the exact
obstruction. Falsification: exhibit a D1 finality profile that requires more than Z/2Z
worth of data to represent as a gauge section.

**F6: The cech_sheaf_fixture forces trivial holonomy.** If C-typed admissibility in
temporal-issuance forces identity product (holonomy = +1) for all C-typed two-patch
covers of S^1, then the fixture does not support the T63 non-trivial class, H3 cannot
be derived (only stipulated), and W-H3's sign-obstruction echo is vacuously true on the
TaF side but lacks a non-trivial witness.

---

## 9. Formal Statement of the Main Result

**Theorem (W-H3 Structural Contact, reconstruction grade).** Let G_R be a signed-readout
record-graph (V, E_causal, lambda: V -> G) with finality condition F(O, r_j) = causally
closed past condition. Let Ax(S_0) -> Ax(S_1) -> ... be a TaF schema extension chain with
C-typed admissibility predicate C_TaF.

Then:

1. (Finality parallel) F(O, r_j) and C_TaF(r_j) are both instances of the abstract
   observer-finality sub-protocol's "stability relation sufficient to build on":
   both are monotone predicates (stable under expansion of O's past / S's schema),
   both are time-free (reference causal accessibility / type-consistency, not timestamps),
   and both determine the subset of records that enter the evidence monoid E_O.

2. (Sign-obstruction parallel) The non-monotone signed-readout phenomenon (R_- > 0, some
   generator lambda(r) in G minus G_+) and the non-trivial TaF Cech class (holonomy = -1
   around the CHSH 4-cycle) are both instances of signed obstructions to monotone
   accumulation: the first obstructs monotone growth of the readout, the second obstructs
   trivial holonomy around observer-context loops.

3. (GU monotone limit) The GU generation-count record-graph G_R^{GU} (24 nodes, no edges,
   all weights = +1, R_- = 0) corresponds to the TaF fully-consistent extension chain
   (all C_TaF checks pass, no contradictions, no retractions), which is the structural
   analog of the trivial Cech class (holonomy = +1).

**What remains open:**

(a) The full H3 identification (finality presheaf sections = flat Z/2Z-gauge connections)
    requires type-bridge C1, fixture C2, and spacelike-overlap fix C3, all of which are
    OPEN (n3-h3-cech-holonomy-2026-06-23.md §4).

(b) The sign-correspondence map Z -> Z/2Z (BC-2) is proposed but not canonical;
    canonicality requires deriving cocycle values from weight functions, which is the
    cech_sheaf_fixture question (C2).

(c) The structural parallel in 1-3 above does not constitute a derivation of H3; it
    identifies the level at which contact is made (abstract observer-finality) and the
    remaining gap (type-bridge from abstract to concrete gauge data).

---

## 10. Verdict

**Verdict: CONDITIONALLY_RESOLVED at reconstruction grade.**

The problem asks: does the signed-readout record-graph construction make contact with the
TaF H3 identification hypothesis, and what are the bridge conditions and failure modes?

**Contact is made at the level of abstract observer-finality:**

- Finality conditions (GU: causally closed past; TaF: C-typed admissibility) are
  structurally parallel monotone admissibility predicates. BC-1 ESTABLISHED.
- Sign-obstruction structure (record-graph non-monotonicity; Cech non-trivial holonomy)
  is a shared phenomenon. A candidate Z -> Z/2Z sign-correspondence map is proposed. BC-2
  PARTIALLY ESTABLISHED (proposal-grade).
- GU monotone case (G_R^{GU}, ind_H = 24, R_- = 0) corresponds to TaF fully-consistent
  extension chain. BC-3 ESTABLISHED.

**Full H3 is NOT derived or confirmed.** The type-bridge (C1), fixture execution (C2),
and spacelike-overlap fix (C3) remain OPEN. The contact established here (W-H3) is weaker
than H3: it is a structural parallel at the observer-finality-sub-protocol level, not a
gauge-field identification.

**Weakened H3 (W-H3) is CONDITIONALLY_RESOLVED:** The abstract contact between the
two finality conditions, the shared sign-obstruction form, and the GU monotone limit
correspondence are all established at reconstruction grade, with six explicit failure
conditions (F1-F6) stated above.

**What remains:**
- Full H3 requires C1 + C2 + C3 (n3-h3-cech-holonomy-2026-06-23.md).
- BC-2 sign-correspondence map requires canonicality derivation from weight functions
  (gated on C2: cech_sheaf_fixture execution).
- Upgrade from reconstruction to verified requires: (i) CAS or mechanically-checked
  formalization of the finality-admissibility parallel; (ii) explicit cech_sheaf_fixture
  result showing non-trivial holonomy from admissibility predicates alone; (iii) explicit
  type-bridge construction.

---

## 11. Exploration Summary Table

| bridge condition | what was shown | what remains |
|-----------------|----------------|--------------|
| BC-1: F(O,r) parallel to TaF admissibility | Structural parallel: both are monotone, time-free admissibility predicates in the observer-finality sub-protocol | Type-bridge C1 from combinatorial D1 profiles to smooth Z/2Z gauge data |
| BC-2: Nonneg weights parallel to Cech coboundary | Shared signed-obstruction form; candidate Z -> Z/2Z reduction map proposed | Canonicality requires fixture C2 to force cocycle values from admissibility alone |
| BC-3: GU ind_H = 24 corresponds to TaF consistent chain | Structural echo: monotone extreme matches fully-consistent extension chain | Not a derivation of H3; structural correspondence only |
| Full H3 | NOT DERIVED here; three open conditions C1-C3 from prior work remain | C1 (type-bridge), C2 (fixture), C3 (spacelike-overlap fix) |
| W-H3 (weakened form) | CONDITIONALLY_RESOLVED at reconstruction grade | Upgrade requires cech_sheaf_fixture result and type-bridge construction |

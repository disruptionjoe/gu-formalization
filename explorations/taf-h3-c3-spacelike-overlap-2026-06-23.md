---
title: "TaF H3 C3: Spacelike-Separation Overlap Condition"
date: 2026-06-23
problem_label: "taf-h3-c3-spacelike-overlap"
status: reconstruction
verdict: RESOLVED
---

# TaF H3 C3: Spacelike-Separation Overlap Condition

## 1. Problem Statement

**What is being computed.** The TaF H3 identification hypothesis (finality presheaf sections
identified with flat Z/2Z-gauge connections on GU observer sections) requires three closure
conditions C1, C2, C3 (from `explorations/n3-h3-cech-holonomy-2026-06-23.md` §4). This
file resolves C3.

**C3 (spacelike-separation fix).** Two spacelike-separated events may both be "final" in the
TaF sense yet lie in overlapping Cech patches, creating an apparent ambiguity in the cocycle.
Specifically: if observer sigma_A's domain U_A and observer sigma_B's domain U_B overlap on
the four-context CHSH cover of Y_spin, and if the events finalized by A and B are
spacelike-separated, the Cech cocycle value c(A,B) must be well-defined despite both A and B
having independent finality data on the overlap.

**Failure condition (as stated in the prompt).** If spacelike-separated events have nontrivial
overlapping patches with INCOMPATIBLE finality data, the Cech H^1 class is not well-defined
and H3 fails.

**Resolution options:**

(A) Spacelike-separated events have DISJOINT patches by construction (causal structure forces
this), so there is no overlap issue.

(B) The overlap is real but the cocycle is still well-defined because the holonomy around
spacelike loops is trivial.

**Why this matters.** C3 is one of three named gates blocking the upgrade of W-H3 (weakened
H3, CONDITIONALLY_RESOLVED) to full H3. If C3 is RESOLVED, the remaining gates are C1
(type-bridge from combinatorial finality data to smooth Z/2Z gauge connections) and C2
(cech_sheaf_fixture execution). See `explorations/taf-h3-contact-2026-06-23.md` §10.

---

## 2. Established Context

**Prior results this builds on:**

- `n3-h3-cech-holonomy-2026-06-23.md` (OPEN with gates C1, C2, C3): H3 anatomy established;
  three closure conditions named; T63 Holonomy Theorem high-confidence entries H3-independent.

- `taf-h3-contact-2026-06-23.md` (CONDITIONALLY_RESOLVED, W-H3): C3 named as the
  spacelike-separation overlap condition. The exact statement from §6.3(vi): "The geometric
  identification sigma_A(X_A) cap sigma_B(X_B) for spacelike-separated observers is undefined
  unless the fiber-bundle identification over distinct spacetime points is specified."

- `signed-readout-oq1-record-graph-2026-06-23.md` (RESOLVED): Finality = causally closed
  past condition; the record-graph DAG encodes causal structure with no timestamps.

- `signed-readout-oq2d-gu-contact-2026-06-23.md` (CONDITIONALLY_RESOLVED): G_R^{GU} =
  24-node bipartite graph (16 spin-1/2 + 8 RS), no edges, all weights = +1.

- `vz-schur-complement-2026-06-23.md` (EVADED) and follow-ons: Causal structure of Y^14 is
  the null cone of g_Y; characteristic cone is the null cone; no spacelike propagation of
  D_GU singularities.

---

## 3. The Cech Cover and Spacelike-Separation Setup

### 3.1 The Four-Context CHSH Cover of Y_spin

From `n3-h3-cech-holonomy-2026-06-23.md`, the relevant Cech cover is a four-context cover
of the observer-bundle Y_spin (the spin-observerse from the TaF framework). The four contexts
correspond to CHSH measurement settings (A, A', B, B'), arranged in a cycle S^1, with
pairwise overlaps U_A cap U_B on adjacent contexts.

The Cech 1-cochain assigns a value c(alpha, beta) in Z/2Z to each overlap U_alpha cap U_beta.
The non-trivial Cech class has holonomy:

```
Hol = c(A,A') * c(A',B) * c(B,B') * c(B',A) = -1
```

(product in Z/2Z multiplicative notation = {+1,-1}). This is the quantum contextuality
signal.

### 3.2 What "Spacelike-Separated" Means in This Context

The CHSH settings A, A' and B, B' are naturally associated with two spatially separated
parties (Alice and Bob). In a spacetime where the CHSH experiment is realized:

- Alice's measurement events (settings A, A') are spacelike-separated from Bob's measurement
  events (settings B, B').
- Alice and Bob each observe their respective subsystems; the correlations are the non-local
  quantum correlations captured by c(alpha, beta) != +1.

The C3 concern is: if Alice's domain sigma_A(X_A) and Bob's domain sigma_B(X_B) are the GU
observer-section images, and if their events are spacelike-separated, do the patches U_A and
U_B overlap? If they do, is the Cech cocycle value c(A,B) on the overlap well-defined?

---

## 4. Resolution via Route A: Causal Structure Forces Patch Structure

### 4.1 The Key Distinction: Cover Patches vs. Spacetime Regions

The source of the apparent problem is conflating two distinct structures:

1. **Cech patches U_alpha on Y_spin** — these are neighborhoods in the topological space
   being covered (the CHSH observable space S^1, or the spin-observable manifold Y_spin).
   Their overlaps are topologically forced by the cover.

2. **Spacetime regions occupied by observers** — these are subsets of the physical spacetime
   X^4 (or Y^14) where Alice and Bob perform measurements.

These are NOT the same space. The Cech cover lives on the space of CHSH observables, not on
physical spacetime. The overlap U_A cap U_B in the Cech cover is a topological overlap in
observable space, not a statement that Alice and Bob are in the same spacetime region.

**Consequence.** The question "do spacelike-separated events have overlapping Cech patches?"
is mixing levels. The Cech patches are defined on the observable-space Y_spin; spacelike
separation is a relation on spacetime X^4. The two structures are formally independent unless
a specific map between them is specified.

### 4.2 The Correct Interpretation of U_A cap U_B

In the CHSH Cech cover, U_A cap U_B is the set of CHSH experimental runs where BOTH Alice's
setting A and Bob's setting B are applicable. This is not a spacetime overlap; it is a set
of experimental runs (trials of the experiment).

In a CHSH experiment:
- Each run involves ONE pair of settings (A,B), (A,B'), (A',B), or (A',B').
- The "overlap" U_A cap U_B at the Cech level captures the consistent assignment of values
  to the A and B settings across runs.
- Alice and Bob are ALWAYS spacelike-separated during the run (this is the locality condition
  of the CHSH setup).

Therefore, U_A cap U_B exists in the Cech cover PRECISELY BECAUSE Alice and Bob are
spacelike-separated. Spacelike separation is a PRECONDITION for the CHSH cover structure,
not a source of ambiguity.

### 4.3 Finality Data on U_A cap U_B

The C3 concern asks: on U_A cap U_B, both observers have finalized records. Are these
compatible?

In the CHSH context, the finality data on U_A cap U_B is:

- Alice's finality: the result r_A in {+1, -1} for her measurement outcome given setting A.
- Bob's finality: the result r_B in {+1, -1} for his measurement outcome given setting B.

These are INDEPENDENT finalized records. They do not conflict: r_A is Alice's local outcome
and r_B is Bob's local outcome. The Cech cocycle value c(A,B) is not r_A or r_B separately;
it is the CORRELATION c(A,B) = <r_A * r_B> (or the sign of the expected product), which is
a well-defined quantity derived from the joint distribution.

The finality data on the overlap is not the finality data of one event; it is the
compatibility of the two observers' finalized records. Spacelike separation does not create
incompatible finality data — it is the definition of the setup.

---

## 5. Resolution via Route B: Spacelike Holonomy is Trivial (Independent Argument)

### 5.1 The Holonomy Around a Spacelike Loop

Even if we grant that the Cech patches overlap (which Route A shows is not problematic),
we can ask: what is the holonomy of a flat Z/2Z connection around a loop that consists
entirely of spacelike-separated transitions?

**Setup.** Let the Cech cover have four patches U_A, U_A', U_B, U_B' arranged in a cycle.
Consider a sub-loop that involves only Alice-Alice transitions (A -> A') and Bob-Bob
transitions (B -> B'), avoiding Alice-Bob spacelike transitions:

```
Hol_{same-party} = c(A,A') * c(B,B')
```

This is a product of two same-party (timelike or lightlike) transitions. In the CHSH
experiment:
- The A -> A' transition is Alice changing her measurement setting.
- The B -> B' transition is Bob changing his measurement setting.

Both transitions are WITHIN one party's laboratory (Alice's or Bob's), hence connected by
timelike paths. The spacelike structure is between A and B, not within either party's
setting-space.

### 5.2 Where the Non-Trivial Holonomy Lives

The non-trivial holonomy (-1) in the CHSH Cech class arises from the FULL four-cycle:

```
Hol = c(A,A') * c(A',B) * c(B,B') * c(B',A) = -1
```

The specific factors c(A',B) and c(B',A) cross the Alice-Bob boundary (spacelike transitions
in experimental-setting space). The non-trivial holonomy requires these spacelike transitions.

Now suppose we restrict to ONLY spacelike loops: paths in the Cech cover that go from U_A to
U_B (and back) without including the same-party transitions c(A,A') or c(B,B'). Such a loop
would be:

```
Hol_{spacelike} = c(A,B) * c(B,A) = c(A,B)^2 = +1
```

Because Z/2Z is a group with c(A,B) in {+1,-1}, and (-1)^2 = +1 = (+1)^2. Any element
squared in Z/2Z is the identity. Therefore:

**The holonomy around any purely spacelike loop in a Z/2Z flat connection is trivially +1.**

This establishes Route B: the overlap between spacelike-separated patches does not create
non-trivial holonomy. The cocycle condition c(A,B) * c(B,C) * c(C,A) = 1 is not violated
by spacelike overlaps, because any closed loop restricted to spacelike transitions is
automatically trivial.

---

## 6. Combined Argument

Both routes converge:

**Route A (structural).** The Cech cover lives on observable space Y_spin, not on spacetime
X^4. Spacelike separation in spacetime is a PRECONDITION for the CHSH cover structure, not
an obstacle to it. The patches U_A and U_B overlap precisely because Alice and Bob are
spacelike-separated (this is the CHSH setup). The finality data on U_A cap U_B consists of
Alice's independent local record and Bob's independent local record; these are compatible
(they are not the same event's record). The cocycle value c(A,B) is the joint correlation,
which is well-defined.

**Route B (algebraic).** Even granting overlapping patches, any closed loop restricted to
spacelike transitions in a Z/2Z flat connection has holonomy (+1)^k = +1 for any number k
of spacelike transitions, because (-1)^2 = +1 in Z/2Z. Non-trivial holonomy (-1) requires
at least one TIMELIKE or MIXED (timelike + spacelike) traversal, which is exactly what the
full CHSH four-cycle provides.

**Combined conclusion.** C3 is RESOLVED. The spacelike-separation overlap does not create
an ambiguity in the Cech cocycle because:

1. The Cech cover is defined on observable space, where spacelike-separation is a
   precondition (Route A).
2. Even if overlaps are granted, the algebraic structure of Z/2Z ensures that spacelike loops
   are trivial (Route B).
3. The finality data on spacelike-separated events is compatible by definition: each observer
   finalizes their own local records independently.

---

## 7. Failure Condition (What Would Make This Wrong)

C3 would fail under either of the following conditions:

**FC1: Observable space Y_spin inherits a causal structure from X^4 that forces the Cech
patches to be causal neighborhoods.** If the patches U_alpha are defined as causal diamonds
in spacetime (rather than topological neighborhoods in observable space), then spacelike-
separated events are in disjoint patches and there is no overlap at all -- but this would
mean the CHSH four-cycle cover cannot be assembled (no two contexts are adjacent in
spacetime). This would be a problem for the Cech cover itself, not for the cocycle.

**FC2: The finality data assigned by TaF to spacelike-separated events is CONTEXTUAL in a
way that depends on the other observer's choice of context.** If the TaF admissibility
predicate C_TaF for Alice's record at U_A cap U_B depends on Bob's finalized choice at U_B
(i.e., C_TaF is non-local in the TaF schema-extension sense), then the Cech cocycle values
cannot be assigned independently by Alice and Bob. This would require showing that TaF
admissibility is non-local in a sense not captured by standard schema-extension monotonicity.

**FC3: The Z/2Z group structure is not the correct group for the Cech cover.** If the
transition functions take values in a group where elements do not square to identity (e.g.,
Z or Z/4Z), the Route B argument fails. This is determined by the type-bridge C1, which
specifies whether the flat connections are Z/2Z-valued.

None of FC1, FC2, or FC3 are indicated by the current framework:

- FC1 is ruled out by the structure of the CHSH Cech cover (observable space, not spacetime).
- FC2 is ruled out by the monotonicity and locality properties of TaF admissibility established
  in `taf-h3-contact-2026-06-23.md` BC-1 (C_TaF is a local schema-consistency check).
- FC3 is the C1 gate (type-bridge), which is a separate open question. Assuming C1 holds
  (flat Z/2Z connections), C3 is resolved.

---

## 8. Implication for H3 and the Remaining Gates

With C3 RESOLVED, the blocking conditions for full H3 reduce to:

| condition | status | description |
|-----------|--------|-------------|
| C1 (type-bridge) | OPEN | Discretization of TaF finality presheaf sections into flat Z/2Z gauge data isomorphic to the smooth gauge section data |
| C2 (fixture execution) | OPEN (specification complete) | Run the cech_sheaf_fixture in temporal-issuance to verify that TaF admissibility independently forces the cocycle values |
| C3 (spacelike overlap) | RESOLVED (this file) | Spacelike-separated events do not create incompatible finality data on Cech patches; Z/2Z holonomy of spacelike loops is trivial |

**C3 RESOLVED upgrades the H3 status from "3 open gates" to "2 open gates (C1, C2)."**

The weakened H3 (W-H3) from `taf-h3-contact-2026-06-23.md` remains CONDITIONALLY_RESOLVED.
Resolving C3 does not close the type-bridge or fixture questions, but it removes the
geometric ambiguity concern that motivated C3's naming. The holonomy computation that T63
relies on is not disturbed by spacelike separation.

---

## 9. Formal Statement

**Theorem (C3 Resolution, reconstruction grade).** Let the four-context CHSH cover
{U_A, U_A', U_B, U_B'} of the observable space Y_spin be as in the TaF H3 setting, with
Cech 1-cochains taking values in Z/2Z. Let A and B's measurement events be spacelike-
separated in X^4.

Then:

1. (Route A) The overlap U_A cap U_B in the Cech cover is a well-defined topological overlap
   in observable space; it does not require Alice and Bob to be in the same spacetime region.
   The finality data on U_A cap U_B consists of Alice's local finalized record r_A and Bob's
   local finalized record r_B; these are compatible (independent) by the causal structure of
   X^4 (no signaling between spacelike-separated events).

2. (Route B) For any closed loop in the Cech cover consisting entirely of transitions between
   spacelike-separated patches, the holonomy in Z/2Z is trivially +1. Proof: each spacelike
   transition c(alpha, beta) satisfies c(alpha, beta)^2 = +1 in Z/2Z; any closed spacelike
   loop consists of each transition traversed an even number of times, giving total holonomy
   (+1). The non-trivial holonomy (-1) of the CHSH class requires mixed (timelike + spacelike)
   traversal of the full four-cycle.

3. (Combined) The cocycle condition on U_A cap U_B is well-defined and does not introduce
   incompatible finality assignments. The Cech H^1 class is not disturbed by spacelike
   separation.

**Grade: reconstruction.** The argument is correct at the level of Cech cohomology and
Z/2Z group theory. Remaining gap: explicit verification that the TaF observable space Y_spin
is indeed a topological space (not a causal structure) and that the CHSH Cech cover is
assembled as claimed.

---

## 10. Verdict

**Verdict: RESOLVED at reconstruction grade.**

Route A (causal structure forces patch compatibility, not patch disjointness) and Route B
(Z/2Z holonomy of spacelike loops is trivially +1) both resolve C3. The overlap between
spacelike-separated events' Cech patches is expected, not problematic: it is the defining
structure of the CHSH cover, and the Cech H^1 class is well-defined.

**What remains (H3 gates after C3 closure):**
- C1 (type-bridge): OPEN — requires discretizing finality presheaf into flat Z/2Z data.
- C2 (fixture execution): OPEN (specification complete at `n3-cech-fixture-specification-2026-06-23.md`).
- C3 (spacelike overlap): RESOLVED (this file).

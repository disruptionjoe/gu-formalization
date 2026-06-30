---
title: "Six-Axis Specification Row for the Observer-Finality Record-Graph Model (OQ1-Followup)"
date: 2026-06-23
problem_label: "six-axis-observer-model-row"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Six-Axis Specification Row: Observer-Finality Record-Graph (OQ1-Followup)

**Purpose.** This file fills the six-axis candidate specification row for the
observer-finality model derived from the signed-readout record-graph (OQ1-followup).

The parent computation (`explorations/signed-calm-jordan/signed-readout-oq1-record-graph-2026-06-23.md`)
RESOLVED at reconstruction grade that the signed-readout record-graph G_R with finality
semantics provides a concrete, time-free grounding for the monotonicity criterion, adding
observer-relative finality and causal-dependence structure beyond the abstract PN/Jordan
framework. The final open item from that file:

> "OQ1-followup (six-axis formalization). Filling a complete six-axis spec row for this
> observer model would promote the record-graph layer from exploration to active-research."

This file discharges that obligation.

---

## Acceptance Summary (One-Line Table)

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Observer-finality-record-graph | Signed-readout record-graph G_R = (V, E_causal, lambda): countable DAG of finalized evidence events, no global timestamps, weight labeling lambda: V -> G (ordered abelian group) | Finite Turing observer O with accessible past P(O) subset V: O processes records one at a time, accumulates finalized evidence set X_O, extracts readout R_O | Causally closed past pairing: O pairs with G_R by checking the finality predicate F(O, r_j) = [r_j in P(O) and all causal predecessors of r_j in P(O)]; no classicality requirement; no timestamps | Sorkin causal-set partial order: E_causal is a locally finite DAG partial order (acyclic, irreflexive) on V; substrate IS the causal order (L1 and L4 coupled, per protocol coupling rule) | Specific-object substrate: the signed-readout phenomenon (R: E_O -> G non-monotone despite evidence order being monotone) is a specific structural fact about a particular G_R and weight labeling, not a universality class | No coordination loop (class (a)): the record-graph is fixed, the observer accumulates records, no feedback from readout back to substrate; the signed-readout phenomenon is a static structural property, not a dynamical attractor | Construct a concrete signed-readout physical system (e.g., a GW instanton network with identified causal ordering and integer weights per node); verify that the four required relations are formally distinct in the physical system; if the causal order on physical records collapses to a total order (timestamps identified with causal order), the model's structural claims fail |

---

## 1. Problem Statement

The signed-readout boundary theorem (`signed-readout-monotonicity-pn-jordan-2026-06-23.md`)
and the record-graph test (`signed-readout-oq1-record-graph-2026-06-23.md`) establish:

- A scalar readout R: E -> G on a free commutative evidence monoid is monotone in the
  information order iff every generator weight w(x) is in G_+ (the positive cone).
- The record-graph G_R = (V, E_causal, lambda) grounds this abstractly in a DAG of
  causally ordered finalized records, with observer-relative finality semantics (the
  causally closed past condition F(O, r_j)).
- The four relations (evidence order, causal order, finality, readout order) are formally
  distinct and the signed-readout phenomenon (non-monotone readout from monotone evidence
  accumulation) is identified as a property of the weight labeling, not of causal propagation.

The six-axis row is needed to:
1. Admit this model as a typed candidate within the six-axis protocol.
2. Make explicit which no-go theorem assumptions it breaks or preserves.
3. State a first falsification test.
4. Connect the observer-finality layer to the GU research program.

---

## 2. Established Context

This builds directly on:

- `explorations/signed-calm-jordan/signed-readout-oq1-record-graph-2026-06-23.md` -- the RESOLVED
  record-graph computation. All definitions in this file derive from Sections 3-9
  of that document.
- `explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md` -- the iff
  monotonicity theorem and PN/Jordan split (PJ1-PJ5 discharged). The six-axis model
  is the record-graph instantiation of the abstract PN/Jordan framework.
- `explorations/misc/six-axis-l1l2-coupling-filled-example-2026-06-23.md` -- the prior
  six-axis filled example (GU-section-BvN-coupling). The observer-finality-record-graph
  candidate has a different L1 (DAG, not smooth bundle), a different L4 (Sorkin partial
  order, not Lorentzian), and a different L6 (no loop, not Tikhonov-Willmore gradient
  flow). Axis-by-axis comparison is given in Section 9.
- `explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`
  -- confirmed that lambda_max is absorbed by L2+L4, and that causal-set completeness is
  rate-blind. The rate-independence of the record-graph G_R's signed-readout phenomenon is
  consistent with that finding.
- `canon/six-axis-specification-protocol.md` -- canonical coupling rules, including the
  Sorkin L1-L4 coupling.

---

## 3. Leg 1 — Substrate Class

**Class label:** (k) Sorkin causal-set substrate. The substrate is the record-graph
G_R = (V, E_causal, lambda) itself: a countable DAG of finalized observable record events
with a weight labeling, and the substrate IS the causal order.

**Specification (1-3 sentences):** The substrate is the triple G_R = (V, E_causal, lambda)
where V is a countable set of record events (finalized, stable evidential facts), E_causal
is a directed acyclic edge relation on V encoding causal dependence (r_i -> r_j means the
content of r_j can depend on the content of r_i), and lambda: V -> G is a weight labeling
taking values in an ordered abelian group G (e.g., G = Z for integer-valued signed
readouts). No global timestamps are attached to nodes. The signed-readout phenomenon lives
at this substrate level: a weight labeling with some lambda(r) outside G_+ produces a
non-monotone readout R_O: E_O -> G, even though the evidence monoid E_O accumulates
monotonically.

**Literature anchor:** Sorkin causal-set framework (Bombelli, Lee, Meyer, Sorkin 1987;
Sorkin 1991, "Spacetime and causal sets"); example-02-sorkin-causal-set in
`specifications/six-axis/examples/example-02-sorkin-causal-set.md` (established prior
example in this repo); FR1 Sorkin absorption worked check
(`explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`).

**Class-assumption signature broken:** The standard no-go theorems (Witten 1981,
Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi) assume a smooth principal bundle on a
smooth manifold as the substrate. The record-graph substrate has no smooth manifold
structure, no bundle, no continuous differentiable geometry. The chirality-bearing content
(signed weights lambda(r) in G and their distribution) is a combinatorial property of the
DAG, not a topological invariant of a smooth bundle. Specifically: Nielsen-Ninomiya
requires a Brillouin zone (smooth compact manifold); the record-graph has no such
structure. Freed-Hopkins requires a smooth oriented manifold with a spin structure;
G_R is a directed graph. Distler-Garibaldi requires a connected compact gauge group
acting on a smooth bundle; G_R has no gauge group action. Witten 1981 requires smooth
fermion fields on a manifold; G_R's "fields" are discrete weights on graph nodes.
The no-go theorems do not fire at the record-graph substrate level. This does not claim
the record-graph evades any no-go theorem for physical matter fields; it is a different
mathematical object at a different level.

---

## 4. Leg 2 — Observer Class

**Class label:** (a) Finite Turing observer (BPP class) -- the standard implicit baseline,
here made explicit with a record-accumulation protocol.

**Specification:** The observer O is a finite-resource computational agent with an
accessible past P(O) subset V: the set of records O has processed. O processes records
one at a time (no hypercomputation, no oracle access to the full DAG), checking the
finality predicate F(O, r_j) at each step: does r_j satisfy the causally closed past
condition (all causal predecessors of r_j in P(O))? When F(O, r_j) holds, r_j enters
the finalized evidence set X_O and contributes weight lambda(r_j) to the readout
R_O: E_O -> G via R_O(sum n_i r_i) = sum n_i lambda(r_i). The observer can be slow
(finalization latency t_obs) or fast; the signed-readout phenomenon (non-monotone R_O)
is rate-independent (confirmed: `fr1-sorkin-absorption-worked-check-2026-06-22.md` and
`rate-independence-negative-finding-2026-06-22.md`).

**Literature anchor:** BPP observer class (standard complexity theory); Sorkin causal-set
observer model (FR1 worked check,
`explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`);
signed-readout monotonicity proof
(`explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md`); record-graph
construction (`explorations/signed-calm-jordan/signed-readout-oq1-record-graph-2026-06-23.md`, Sec. 3-5).

**Class-assumption signature broken:** The no-go theorems use an unlimited-fidelity
observer that reads off a fixed smooth-bundle invariant without any accumulation protocol.
The record-graph observer has a specific accumulation protocol -- the causally closed past
condition -- that determines which records are available at each step. The observer's
evidence monoid E_O depends on P(O), so two observers with different pasts P(O) and P(O')
may have different readouts R_O and R_{O'} from the same G_R. This observer-relative
monotonicity is not present in the standard no-go theorem setup. The class-assumption
broken is: "observer reads off fixed invariant without protocol". Here the invariant
(readout value) is observer-relative and protocol-dependent. This does not break any no-go
theorem for physical chirality; it relocates the chirality question from "does the no-go
theorem fire for this bundle?" to "does this observer's evidence set produce a monotone
readout?".

---

## 5. Leg 3 — Pairing

**Class label:** (a) Cartesian / smooth (implicit baseline) -- but here instantiated as a
purely combinatorial pairing, not a smooth tensor-product channel.

**Specification:** The observer O pairs with the record-graph G_R via the finality predicate:
F(O, r_j) is a predicate on observers x V -> {true, false}, computed from set membership
in P(O) and the DAG edge relation E_causal. The pairing is deterministic and requires no
gauge, no connection, no metric, and no classicality certification. When F(O, r_j) = true,
the weight lambda(r_j) is transmitted to the observer's readout exactly (append-only records;
lambda is assigned at construction and never revised). The pairing channel is append-only,
causally gated, and deterministic. There is no BvN wall in this pairing: the record-graph
substrate is classical (no quantum metric fluctuations), and O extracts weights from a
classical combinatorial object without performing any classicality certification.

**Specification of the four relations transmitted through the pairing:**
The pairing transmits four formally distinct relations (established in
`signed-readout-oq1-record-graph-2026-06-23.md`, Sec. 7):

| relation | domain | transmitted via |
| --- | --- | --- |
| evidence order (<=_E) | E_O x E_O | monoid structure of X_O (finalized records) |
| causal order (<_c) | V x V | E_causal DAG edges on G_R |
| finality relation F | observers x V | causally closed past condition on P(O) and E_causal |
| readout order (<=_G) | G x G | order on G (e.g., Z with usual order) |

**Literature anchor:** Standard monoid / free-commutative-monoid construction (textbook
algebra); causally closed past condition (Sorkin, 1991 and FR1 worked check); four-relation
separation (`signed-readout-oq1-record-graph-2026-06-23.md`, Sec. 7-8).

**Class-assumption signature broken:** No standard no-go theorem assumption is broken
by this pairing in the sense of creating a novel evasion mechanism. The pairing preserves
the "cartesian / smooth" class (a) baseline in spirit (no exotic coupling), instantiated
for a combinatorial substrate. What is added over the baseline: the causal-gate structure
of the finality predicate means the observer cannot read off all weights at once -- it
must wait for causal predecessors to be processed first. This sequential causal constraint
is not present in the standard no-go setup (where all of a fixed bundle's sections are
simultaneously available). In particular, the pairing makes explicit which observer can
observe which signed-readout phenomenon, a question the no-go theorems do not address.

---

## 6. Leg 4 — Causal-Order Class

**Class label:** (d) Sorkin causal-set (substrate IS a locally finite partially ordered
set; Lorentzian metric is absent or emergent).

**Specification:** The causal order on the substrate is E_causal: the directed acyclic
graph partial order on V. This is a strict partial order (acyclic, irreflexive, transitive
closure defines the causal precedence relation r_i <_c r_j). The order is locally finite
(each node has finitely many causal predecessors in any bounded region); globally there
may be infinitely many nodes (countable V). No global Lorentzian metric is assumed: the
DAG captures causal dependence, not chronological time. In the language of the six-axis
protocol, L1 (the record-graph DAG) and L4 (the causal partial order) are coupled -- the
substrate IS the causal order, as per the protocol coupling rule for Sorkin causal-set
substrates.

**Literature anchor:** Sorkin causal-set formalism (Bombelli-Lee-Meyer-Sorkin 1987;
Henson 2006 review, "The causal set approach to quantum gravity"); example-02-Sorkin in
`specifications/six-axis/examples/example-02-sorkin-causal-set.md`; FR1 Sorkin absorption
check (`time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`).

**Class-assumption signature broken:** Witten 1981, Freed-Hopkins, Distler-Garibaldi all
assume total-order Lorentzian causal structure (smooth manifold, Cauchy slicing). The
record-graph uses a proper partial order: there are incomparable elements (records r_i
and r_j with neither r_i <_c r_j nor r_j <_c r_i, as in the toy example where r_3 is
causally unrelated to r_1 and r_2). This partial order is strictly more general than a
total order. The absence of a total order means there is no canonical "causal past of the
universe at time t" -- only the causally closed past relative to a specific observer O.

**Note on rate-independence.** The signed-readout phenomenon is rate-independent:
the non-monotonicity of R_O when some lambda(r) not in G_+ is a structural property of
the weight labeling, not of the rate at which O processes records (FR1 confirmed: the
causal-set completeness condition is rate-blind; `rate-independence-negative-finding-2026-06-22.md`
confirmed: the signed-readout monotonicity criterion is rate-independent). The partial
causal order enforces WHICH records can be simultaneously finalized, but not HOW FAST.

---

## 7. Leg 5 — Emergence Class

**Class label:** (a) Specific-object substrate. The signed-readout phenomenon is a
specific structural fact about a particular G_R and weight labeling lambda, not a
universality class or RG fixed point.

**Specification:** The emergence class is specific-object for each instantiation: a
particular choice of DAG G_R = (V, E_causal, lambda) with a specified G and weight
function lambda: V -> G determines whether R_O is monotone or non-monotone for each
observer O. Two different instantiations may differ in whether the signed-readout phenomenon
fires. The claim is NOT that all record-graphs of a universality class exhibit non-monotone
readout. The signed-readout boundary theorem (`signed-readout-monotonicity-pn-jordan-2026-06-23.md`)
provides the iff criterion: R_O is monotone iff all lambda(r) for r in X_O are in G_+.
This is a specific-object fact (it depends on the specific weights lambda, not on the
topological class of G_R).

**GU instantiation.** The GU-specific record-graph is G_R^{GU} (constructed in
`explorations/signed-calm-jordan/signed-readout-oq2d-gu-contact-2026-06-23.md`): 24 nodes in a bipartite
structure (16 spin-1/2 + 8 RS), no causal edges, all weights lambda(v) = 1 (in G_+ = N_0).
This is the MONOTONE case: R_O = 24 for any O with P(O) = V, and no signed-readout
non-monotonicity fires. The GU record-graph is a specific object within the general
framework; other instantiations (e.g., with negative weights) produce non-monotone readouts.

**Literature anchor:** Signed-readout monotonicity theorem
(`explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md`); GU record-graph
construction (`explorations/signed-calm-jordan/signed-readout-oq2d-gu-contact-2026-06-23.md`); specific-object
class (a) template usage as in example-01-type-ii1-spectral-sm.

**Class-assumption signature broken:** No specific no-go theorem assumption broken by
the specific-object emergence class. The standard no-go theorems also assume specific-object
substrate. The difference is in L1 (DAG vs. smooth bundle) and L4 (partial order vs.
Lorentzian), not in L5. The emergence class is preserved from the baseline.

---

## 8. Leg 6 — Coordination-Loop Class

**Class label:** (a) No coordination loop (baseline). The record-graph is a static DAG;
the observer accumulates records; there is no feedback from the readout R_O back to the
record-graph G_R.

**Specification:** Once G_R = (V, E_causal, lambda) is fixed, the substrate is
static. The observer O processes records in any order consistent with the causal constraint
(O cannot process r_j before all causal predecessors of r_j are processed), but O's
processing does not modify the DAG, the edge structure, or the weights. The readout R_O
is a function of the finalized evidence set X_O, which depends on P(O), but P(O)'s
growth does not back-react on G_R. This is class (a) no-loop.

**Exception: cadence loop (exploration-grade).** If a cadence field Delta is added
(per FR4, `explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`
and `explorations/misc/fr4-cadence-delta-second-example-2026-06-23.md`), the finality predicate
is deadline-gated: F_Delta(O, r_j, t) = [F(O, r_j) AND t <= t_construction + Delta].
Under a cadence loop, a record finalized after the deadline is discarded (the observer
commits on an incomplete past), producing a structurally new failure mode (premature
commitment). This converts L6 from class (a) to a deadline-cadence loop class. The
cadence field was confirmed exploration-grade in FR4 and promoted as a sub-protocol
candidate. Without the Delta field, this candidate is class (a).

**Literature anchor:** Static DAG / append-only record model (standard; see the
finality-semantics Sec. 4.2 of `signed-readout-oq1-record-graph-2026-06-23.md`);
FR4 cadence field `explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`;
CALM-cadence second example `explorations/misc/fr4-cadence-delta-second-example-2026-06-23.md`.

**Class-assumption signature broken:** The class (a) no-loop L6 is the same as the
standard no-go theorem baseline. No L6 assumption is broken. If the cadence-loop variant
is used, L6 changes from class (a) to a deadline-policy class that introduces the
premature-commitment failure mode -- structurally distinct from the standard no-go
theorem setup (which has no cadence, no deadline policy, and no commitment failures).

---

## 9. Chirality Bridge Claim

The substrate-level invariant is the signed weight labeling lambda: V -> G restricted
to the GU record-graph G_R^{GU}. For the GU instantiation, lambda(v) = 1 for all 24
nodes (16 spin-1/2 + 8 RS generation nodes), all in G_+ = N_0. The readout R_O = 24
for any observer O with P(O) = V (all records finalized). This 24 is the integer index
ind_H(D_GU) = 24, identified as 3 SM generations via the 2+1 split (established at
reconstruction grade in `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`, §12-19,
and confirmed in `explorations/signed-calm-jordan/signed-readout-oq2d-gu-contact-2026-06-23.md`).

The forgetful operation is the Atiyah-Jannich / Atiyah-Schmid forgetful map from the
discrete-series Plancherel decomposition of L2(SL(4,R) x_{SO_0(3,1)} S(6,4)) to the
integer ind_H(D_GU): each irreducible summand (a Harish-Chandra discrete series
representation) maps to its Hom-multiplicity count (1 per summand, by Flensted-Jensen
multiplicity-one, `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md` §18, AF3). The
24 H-lines in ind_H are the 24 node-weights in G_R^{GU}.

The smooth-bundle shadow of this construction is the classical section s*: X^4 -> Y^14
selected by the Tikhonov-Willmore variational principle. At the smooth-bundle level, the
no-go theorems (Witten, Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi) compute on
the forgetful image of s* and find no chirality obstruction from their assumptions,
because: (a) GU's chirality content is carried by the discrete-series Plancherel
multiplicity m_H(S(6,4)) = 24, which is a substrate-level (record-graph / Harish-Chandra)
invariant, not a smooth-bundle Chern number; (b) the smooth bundle shadow (the pulled-back
principal bundle s*(P_sp(64)) over X^4) does carry Sp(64) gauge structure, but Sp(64) is
anomaly-free (n_L - n_R = 0 by pseudoreality), so the no-go theorems find no anomaly to
obstruct. The chirality (generation count) is thus not visible to the no-go theorems
operating at the smooth-bundle shadow level; it requires the discrete-series / record-graph
substrate level to see.

---

## 10. One First Falsification Test

**Test: Physical causal ordering of GW instantons.**

Identify a concrete physical system that is a candidate instantiation of G_R: a network
of gravitational-wave (GW) instanton events in some spacetime region. Specifically:

1. Take a network of GW instanton events {r_i} in a spacetime region of (3+1)D GR.
2. Define the causal order: r_i <_c r_j iff the causal future of r_i overlaps the
   causal past of r_j (standard GR causal precedence).
3. Assign integer weights: lambda(r_i) = +1 if the instanton contributes n_+ to the
   axial charge Q_A, and lambda(r_i) = -1 if it contributes n_- (the GW axial charge
   assignment from `explorations/signed-calm-jordan/signed-readout-monotonicity-pn-jordan-2026-06-23.md`,
   Sec. 5, GW instantiation).
4. Define an observer O with past P(O) = some subset of the instanton network, satisfying
   the causally closed past condition.
5. Compute R_O(e_max) = sum of all weights in X_O and compare with the direct instanton
   count n_+ - n_- in the same region.

**Pass condition (model confirmed):** The four relations (evidence order, causal order,
finality, readout order) are formally distinct in the GW instanton network:
- Causal order r_i <_c r_j is a partial order with incomparable elements (there exist
  pairs of instantons in spacelike separation with no causal precedence).
- Finality F(O, r_j) is non-trivial: some instantons r_j have causal predecessors in
  the network that O has not yet processed.
- Readout R_O is non-monotone if some lambda(r_i) = -1: adding an anti-instanton to X_O
  decreases R_O.
- The signed-readout phenomenon (non-monotone readout from monotone evidence accumulation)
  matches the known GW axial charge accounting (Q_A = n_+ - n_- can decrease as more
  anti-instantons are finalized).

**Fail condition (model falsified):** If the GW instanton causal order on the network is
a TOTAL order (any two instantons are causally comparable -- no spacelike instantons in
the region), then <_c collapses to a timeline, global time is present in disguise, and the
no-global-time property of G_R is violated (failure condition F2 from
`signed-readout-oq1-record-graph-2026-06-23.md`, Sec. 11). This would mean the
record-graph layer adds no structure over a standard time-ordered event list.

**Secondary fail condition:** If the integer weights lambda(r_i) are not determined at
the time of instanton finalization (they depend on future events, i.e., lambda is not
assigned at construction time), then failure condition F3 from the same file applies
(hidden time dependence in the weight labeling).

**Runner.** Can be run by a GW / instanton physics specialist, or by an agent pass that
constructs an explicit causal diagram for a multi-instanton spacetime configuration and
checks the four relations using the GR causal precedence relation.

**Tied to no-go theorem assumption.** The test is tied to the Nielsen-Ninomiya assumption
that the lattice Brillouin zone is a smooth compact torus: in the GW instanton network,
the causal order is a DAG on a countable set of events, with no torus structure and no
smooth momentum space. Nielsen-Ninomiya cannot fire at the record-graph substrate level.
The test checks that the physical system actually has the DAG partial-order structure
required (incomparable instanton pairs), rather than a total order that would collapse
the record-graph model to a disguised timeline.

---

## 11. Explicit Failure Conditions

The record-graph model is falsified in any of the following ways (six conditions):

**F1 (Finality uses timestamps).** If the causally closed past condition F(O, r_j) can
only be implemented by maintaining a global clock (e.g., the only feasible way to check
"all causal predecessors in P(O)" is to check "all events before time t(r_j) are in P(O)")
then timestamps are effectively required, and the no-global-time property fails. This is
the strongest structural falsification: it would mean the record-graph layer is equivalent
to a time-ordered list for any physical observer.

**F2 (DAG admits only a total order in the physical system).** If every physically
realizable causal order for the signed-readout application (e.g., GW instanton events in
the universe's history) is a total order (all events in timelike or lightlike relation),
then <_c has no incomparable elements, and the partial-order advantage of the record-graph
is absent. Falsification: exhibit a physically realizable causal set with spacelike
instanton pairs.

**F3 (Weight labeling lambda depends on future events).** If the weight lambda(r_j) of
a finalized record r_j can change after r_j enters P(O) (e.g., because a future event
r_k changes the attribution of the GW charge to r_j), then the append-only property
(lambda assigned at construction) fails. The monotonicity criterion proof requires the
append-only property (condition (iii) in F(O, r_j) simplification, Section 4.2 of the
parent file).

**F4 (Evidence monoid has non-trivial relations).** If the free commutative monoid
structure on X_O is not the correct evidence structure (i.e., there are non-trivial
relations r_i + r_j = r_k as evidence, not just as record labels), the monotonicity
criterion proof fails in the (=>) direction. The monoid must be free for the
iff-theorem to hold in both directions.

**F5 (Signed cancellation breaks causal propagation).** If a negatively-weighted record
r_j (lambda(r_j) not in G_+) causes downstream records r_k (with r_j <_c r_k) to have
undefined or inconsistent content in the physical application, then the record-graph
model has not separated signed readout from causal propagation. The signed-readout
phenomenon is then not a clean structural feature but an artifact of pathological causal
dependencies.

**F6 (Non-lattice-ordered G prevents PN split).** If G is an ordered abelian group
without the lattice property (max(g, 0) not well-defined for all g in G), the
PN/Jordan split PJ5 (minimal split form) cannot be stated canonically. The if-and-only-if
direction of the monotonicity criterion holds (the "lambda in G_+ iff monotone" formulation
is still correct), but the minimal factorization into R_+ and R_- is not canonical. For
G = Z, this does not arise (Z is a lattice-ordered group). For more general G, this must
be checked per application.

---

## 12. Explicit Computation

### 12.1 What is Being Claimed

At this reconstruction grade, the six-axis row is filled with class labels, specifications,
literature anchors, class-assumption-signature entries, chirality bridge claim, and one
first falsification test. The claim is:

1. The observer-finality record-graph model is a well-defined typed candidate in the
   six-axis protocol.
2. It is distinct from the prior six-axis candidates (example-01 through example-03,
   and the GU-section-BvN-coupling candidate) on at least two axes (L1 and L4).
3. Its chirality content (the GU generation count 24) is traceable to the substrate
   (discrete-series Plancherel multiplicity m_H(S(6,4)) = 24, CONDITIONALLY_RESOLVED).
4. The six-axis filling satisfies the protocol requirements (no axis left vague; first
   falsification test stated; chirality bridge claim written).

### 12.2 Axis Comparison with Prior Candidates

| axis | GU-section-BvN-coupling (prior) | observer-finality-record-graph (this file) |
| --- | --- | --- |
| L1 substrate | Smooth principal bundle Y^14 = Met(X^4), Cl(9,5), quantum metric fluctuations | Signed-readout record-graph G_R: DAG with weight labeling lambda: V -> G |
| L2 observer | Snowball / metastable consensus observer with Gamma, t_obs, epsilon bounds | Finite Turing observer O with accessible past P(O) and causally closed past check |
| L3 pairing | BvN-gated metastable-consensus pairing (Gamma_min coupling rule) | Causally closed past pairing (deterministic finality predicate, no BvN wall, no classicality certification) |
| L4 causal order | Conditional Lorentzian on X^4, quantum-indefinite fibers below Gamma_min | Sorkin causal-set partial order (DAG E_causal, no total order, no timestamps) |
| L5 emergence | Specific-object (Y^14 with gimmel metric, Tikhonov-selected s*) | Specific-object (particular G_R and lambda) |
| L6 coordination loop | Tikhonov-Willmore gradient flow (Lambda = 8 epsilon^2 / t_obs^2) | No loop (class (a)); cadence-loop variant exploration-grade |

The two candidates are distinct on L1, L2, L3, L4, and L6. They share L5 (specific-object).
The GU-section-BvN-coupling candidate is the GU physics construction level;
the observer-finality-record-graph candidate is the signed-readout / observer-finality
abstract layer. They are not competitors: the latter is a formal framework that the former
can be instantiated within (the GU record-graph G_R^{GU} is a specific instance of the
general G_R framework established here).

### 12.3 Coupling Rules Confirmed

Per `canon/six-axis-specification-protocol.md` "Current Coupling Rules":

- **Sorkin L1-L4 coupling confirmed.** The record-graph DAG (L1) is the causal order
  (L4). These are the same mathematical object: E_causal is both the substrate causal
  dependence structure and the causal-order model. This instantiates the canonical Sorkin
  coupling rule.
- **No L5-L6 coupling required.** L5 = specific-object and L6 = no-loop; the protocol
  coupling rule "RG universality (L5) requires RG flow (L6)" does not apply here.
- **No L2 decoherence-rate coupling.** The signed-readout phenomenon is rate-independent
  (confirmed multiple times). No Gamma_min type coupling rule applies to this candidate.
  The BvN coupling rule from the prior candidate is absent here.

---

## 13. Result and Verdict

**Verdict: CONDITIONALLY_RESOLVED at reconstruction grade.**

All six axes are filled with class labels, specifications, literature anchors, and
class-assumption signatures. The chirality bridge claim and first falsification test
are stated. The Sorkin L1-L4 coupling rule is respected. The candidate is formally
distinct from prior six-axis candidates on four of six axes.

**Grade: reconstruction.** The six-axis filling is based on the RESOLVED record-graph
computation (`signed-readout-oq1-record-graph-2026-06-23.md`) and the iff monotonicity
theorem (`signed-readout-monotonicity-pn-jordan-2026-06-23.md`). The chirality bridge
claim rests on m_H(S(6,4)) = 24 (CONDITIONALLY_RESOLVED, discrete-series program). The
first falsification test is stated but not yet run.

**What remains for upgrade to verified:**

- RC1: The first falsification test (GW instanton causal order check) must be run by a
  specialist. Until the causal order of a physical GW instanton network is explicitly
  checked to have incomparable elements, the "Sorkin partial order" claim is structural
  but not empirically verified for the physical application.

- RC2: The chirality bridge claim (m_H(S(6,4)) = 24 lifted to G_R^{GU}) requires the
  discrete-series program open conditions OQ3a (K3-type variational selection), OQ3b
  (RS index = 8, analytic Fredholm), and OQ3c (index additivity) to upgrade to RESOLVED.
  These are named open conditions in `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`.

- RC3: The four-relation formal distinctness proof is VERIFIED at the abstract level
  (all four relations are defined on distinct domains with distinct types). The physical
  instanton instantiation of the formal distinctness has not been checked; it is
  plausible but reconstruction-grade.

**Open follow-on questions:**

- OQ1-A (TaF H3 contact): Does the finality predicate F(O, r_j) in this file correspond
  to the TaF admissibility condition (temporal-issuance E015 route)? H3 remains a named
  open blocker; N3 is OPEN_BLOCKED_ON_FIXTURE_SPECIFICATION.

- OQ2 (integer-index recovery): CONDITIONALLY_RESOLVED in `signed-readout-oq2-integer-index-2026-06-23.md`
  and `signed-readout-oq2d-gu-contact-2026-06-23.md`. The six-axis row does not change
  this status.

- Cadence-loop (L6 extension): The FR4 cadence field Delta is an exploration-grade
  sub-protocol candidate. If promoted, it would change L6 from class (a) to a
  deadline-cadence loop, adding a new failure mode (premature commitment) to the
  record-graph model. The promotion condition is met (two worked examples, FR4 +
  `fr4-cadence-delta-second-example-2026-06-23.md`), pending canon review.

---

## 14. Open Questions After This File

The signing-readout / observer-finality research lane is now at the following state:

| item | status | what remains |
| --- | --- | --- |
| Signed-readout monotonicity criterion | RESOLVED | -- |
| OQ1 record-graph test | RESOLVED | -- |
| OQ1-followup six-axis row | CONDITIONALLY_RESOLVED (this file) | RC1 (first falsification test run), RC2 (discrete-series OQ3a-c), RC3 (physical four-relation check) |
| OQ2 integer-index recovery | CONDITIONALLY_RESOLVED | RV1-RV4 (CAS/peer verification); K-theory lift OQ2-A; explicit G_R^{GU} (CONDITIONALLY_RESOLVED) |
| OQ2-A K-theory lift | CONDITIONALLY_RESOLVED | Fred_H classification for non-compact Y^14 |
| OQ2-D GU contact | CONDITIONALLY_RESOLVED | RV-OQ2D-1, RV-OQ2D-2 |
| OQ1-A TaF H3 contact | OPEN (N3 named blocker) | cech_sheaf_fixture specification and execution |
| Cadence sub-protocol promotion | Promotion condition met (exploration-grade) | Canon review before inclusion |

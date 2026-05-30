# Problem-Shape — DAG / Partial-Order Causality Heterodox Lens

**Date:** 2026-05-28
**Persona:** DAG-based ledger / Hashgraph / IOTA Tangle / partial-order causality specialist (heterodox lean).
**Predecessors accepted as baseline:** 00, 00b, 00c, 00d.
**Mode:** Hegelian dialectic within DAG / partial-order. Heterodox. `[speculation]` where stated.

## (a) Thesis (mainstream)

Time is a totally-ordered linear parameter. Spacetime is a smooth Lorentzian manifold; causal order between events is given by light cones; "happens-before" is encoded by the Lorentzian metric and reduces to a single global scalar time after a Cauchy-slice foliation. In GU's smooth-KK setting, evolution is a total-order flow on Met(X); the bundle's section is read along a totally-ordered worldline. Chirality is a property of total-order Lorentz reps.

## (b) Heterodox antithesis (DAG / partial-order)

Causality is **partial-order, not total**. Distributed-systems substrate provides the model: Lamport happens-before on message-passing graphs, vector clocks, Hashgraph gossip-about-gossip, IOTA Tangle (each tx confirms two prior txs), NANO block-lattice, Avalanche DAG. None of these require a global linear time; total order is an **emergent property** of partial-order gossip, not a primitive. Sorkin's causal-set program already proposes discrete posets as the spacetime substrate, with continuum Lorentzian geometry as coarse-graining. CRDT theory (Shapiro et al.) and the CALM theorem (Hellerstein-Alvaro) prove monotonic programs admit coordination-free distributed implementations — consistency without total order. Chirality, on this view, is an **orientation of the partial-order DAG** (a directed-acyclic-graph invariant), distinct from any totally-ordered shadow.

## (c) Aufhebung — extending 00d

00d's three-leg specification (substrate class + observer class + pairing) implicitly assumed each leg lives in a totally-ordered narrative: the substrate has states, the observer extracts in a sequence, the pairing is single-valued at each moment. The DAG lens forces a **fourth axis** onto 00d: a **causal-order axis** specifying whether the substrate-to-bundle projection is **total-order linearization of a partial-order substrate** or **partial-order all the way down**.

Concretely: each substrate candidate in 00d's Leg 1 has both a total-order and a partial-order reading.
- Connes II_1 + Jones subfactor: planar algebras are partial-order tangle diagrams; total-order linearization is the spectral triple's Dirac flow.
- Holographic QEC: tensor-network contraction order is a DAG (partial), not a line; ER=EPR entanglement is a partial-order graph of mutual information.
- Wolfram multiway: causal graphs ARE DAGs by construction; rulial "linearizations" are foliation choices.
- Higher / motivic: ∞-categorical morphism composition is a partial-order weak Kan structure.

The Aufhebung: **chirality is a DAG-invariant of the partial-order causal substrate**; the smooth Lorentzian manifold is the total-ordered shadow obtained by **section-of-the-DAG-projection** (a Cauchy-slice-style linearization of the partial-order). Witten 1981, Freed-Hopkins, Nielsen-Ninomiya, Distler-Garibaldi each compute the chirality content of the totally-ordered shadow, where the DAG-invariant has been **forgotten by linearization**. The no-go theorems are the **CRDT-merge image** of a partial-order substrate invariant — chirality survives in the substrate's partial-order orientation, even when the linearized shadow shows zero net handedness. `[speculation]`

This extends 00d by adding **causal-order (total vs partial)** as a fourth specification axis: 10 substrate classes × 3 observer classes × 5 pairings × 2 causal orders = 300 candidate triples, of which roughly half (the partial-order branch) inherit substrate-level chirality content invisible to bundle-level no-gos.

## (d) WRK-326 next ask

Add **Leg 4: causal-order class** to the 00d triple-specification. Options:
- (i) Total-order substrate (the implicit 00d default): chirality must survive the bundle projection directly.
- (ii) Partial-order substrate, CALM-monotonic: chirality is a coordination-free DAG-invariant; bundle is a CRDT-merge.
- (iii) Partial-order substrate, non-monotonic: requires consensus / gossip-style total-order emergence; bundle is the Hashgraph-style consensus shadow.
- (iv) Sorkin-class causal-set substrate: discrete partial-order; continuum is coarse-graining.

Joe locks (i) through (iv) alongside the existing three legs.

## (e) Falsifiable sub-question

**Does any of the four 00d substrate candidates (Connes II_1, holographic QEC, Wolfram multiway, motivic/tmf) admit a partial-order causal-DAG presentation whose linearization to a Cauchy-foliated total-order substrate produces precisely the chirality content the Witten / Freed-Hopkins / Nielsen-Ninomiya theorems compute as null AND whose un-linearized DAG-invariant is non-null and SM-compatible?** Falsified if every partial-order presentation of these substrates either (A) collapses to the same linearized invariant the no-gos already constrain, or (B) carries a non-null DAG-invariant that fails to reduce to SM chirality content under any CRDT-merge-class linearization. `[speculation]`

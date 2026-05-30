# Persona 31 — Avalanche / Snowball / Metastable Consensus (Heterodox Lean)

**Date:** 2026-05-28
**Persona:** Distributed-systems specialist in the Avalanche / Snowball / Slush family (Team Rocket 2018), repeated subsampled voting, probabilistic safety/liveness, DAG-based ledgers, metastability, FLP, CAP, asynchronous BFT, VRF sortition.
**Heterodox lean.** Builds on 00d's three-leg specification (substrate-class + observer-class + pairing); does not mutate it.

## (a) Thesis-in-domain

Mainstream consensus theory (Nakamoto longest-chain, PBFT, Paxos, Raft) treats consensus as **convergence to a single global totally-ordered state at finality**. One truth, one log, one history. Safety and liveness are deterministic guarantees relative to a fault model (f < n/3 for BFT, honest-majority hashrate for Nakamoto). The system has a "current state" that all correct nodes eventually agree on.

Carried to physics: there is a single global state of the universe, an objective "now-slice," and observers asymptotically read the same fact. The bundle shadow is the one true ledger.

## (b) Heterodox antithesis (Avalanche / Snowball / DAG)

Avalanche-family consensus reaches **probabilistic certainty via repeated subsampled queries**: each node samples k peers, adopts the majority preference, accumulates a confidence counter, and finalizes when the counter exceeds β. Safety holds with probability 1 minus ε, for **any** ε chosen ex ante. Crucially:

- **Metastability is preserved between rounds.** The system genuinely hovers between equivalent states until a small perturbation tips it. There is no hidden "real" state being progressively revealed; the state IS the metastable distribution over query histories.
- **The ledger is a DAG, not a chain.** Time and causality emerge from a partial order. Different observers committing different vertices can both be "correct" simultaneously; no total order exists or is needed.
- **FLP (1985) is broken by randomization.** Deterministic async consensus is impossible with one fault; Avalanche escapes by being probabilistic. The price of consensus is non-determinism baked into the substrate.
- **CAP-class is a design choice.** You pick which two of (consistency, availability, partition-tolerance) the substrate honors. Different physical regimes might be different CAP classes.
- **Heard-of-model:** correctness requires only that you "heard from" a sufficient subsample; full visibility is neither possible nor needed. `[speculation]` Observers in physics may be heard-of-model observers, not omniscient ones.

Truth here is **observer-time-relative**: what you've finalized depends on which subsamples you drew and when you stopped querying.

## (c) Aufhebung problem-shape (extends 00d)

The 00d three-leg specification implicitly treats the substrate-to-bundle map as a deterministic forgetful functor: one substrate state, one bundle shadow. The Avalanche lens reframes the map itself as **a metastable consensus process running among observer-fragments**.

`[speculation]` The "observerse projection" of GU (or any candidate substrate → bundle reduction) is the output of repeated subsampled voting among observer-fragments over substrate configurations. Chirality is **the metastable consensus invariant**: the property that survives sufficient rounds of subsampled queries with probability ≥ 1 minus ε. The Freed-Hopkins forgetful image is what gets finalized under that consensus protocol, not what is "really there."

This adds a fourth leg to 00d's triple, or rather refines the pairing axis (Leg 3) and the observer-class axis (Leg 2) jointly:

- **Leg 2 refinement (observer-class):** add a **Snowball-class observer** — finite, subsampling, confidence-accumulating, ε-bounded. Distinct from BPP/BQP/Malament-Hogarth/Ω-oracle. This observer-class can finalize chirality only up to probability 1 minus ε; the residual ε is irreducible.
- **Leg 3 refinement (pairing):** add a **metastable-consensus pairing** — substrate and observer-fragment population are co-constituted by the protocol parameters (k, α, β). Different (k, α, β) define different physics. This is a structural cousin of P10's constructor pairing but quantitative.
- **Bundle-level no-go theorems** (Witten, Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi) then compute **the consensus-finalized image** of substrate chirality, not the substrate invariant itself. The no-go is a statement about what gets finalized at ε → 0 in the standard subsampling protocol, not what exists upstairs.

The dialectical move: 00d says chirality is a substrate invariant whose forgetful image in the smooth bundle is null. Avalanche-31 says **the "forgetful image" itself is a consensus-protocol output**, and different protocols (different (k, α, β), different CAP-class, different DAG vs chain) yield different no-go theorems. The no-gos are protocol-relative.

## (d) WRK-326 next ask from this discipline

For any candidate substrate-class chosen in 00d Leg 1, specify the **consensus protocol** by which substrate states project to bundle shadows:

1. Is the projection chain-class (total order, single finalized history) or DAG-class (partial order, multiple compatible finalizations)?
2. What is the protocol's (k, α, β) analog — the subsampling parameters that determine how observer-fragments aggregate substrate facts into finalized bundle data?
3. Which CAP corner does the substrate sit in? (Consistency-availability without partition-tolerance ≈ classical physics; availability-partition-tolerance without consistency ≈ many-worlds-ish; consistency-partition-tolerance without availability ≈ superselection-sector physics.)
4. Is the no-go theorem (Witten / Freed-Hopkins) the ε → 0 limit of the standard subsampling protocol, or a protocol-independent statement? If protocol-relative, alternative protocols may yield distinct no-go images.

## (e) One falsifiable sub-question

`[speculation]` For a specified substrate-class candidate from 00d Leg 1 (e.g., Connes Type II_1 + Jones subfactor), does there exist a non-trivial **DAG-class consensus protocol** (partial-order finalization, subsampling parameters (k, α, β) with α > k/2 and β finite) under which **chirality finalizes with probability ≥ 1 minus ε but the Freed-Hopkins forgetful image is non-null**? If yes, Freed-Hopkins is protocol-relative and the no-go shifts from a theorem-about-physics to a theorem-about-the-default-consensus-protocol. If no (i.e., every DAG-class protocol still yields the Freed-Hopkins null image), then Freed-Hopkins is protocol-robust and the substrate-inversion strategy must locate chirality content that survives **all** subsampling protocols, not just the standard one. This is a concrete mathematical question in the intersection of subfactor planar algebras (P23) and randomized consensus theory.

## Honesty contract

No GU literature read. No silent strengthening of 00d. The Avalanche / Snowball / DAG / FLP / CAP material is established distributed-systems theory (Team Rocket 2018, Fischer-Lynch-Paterson 1985, Brewer 2000, Charron-Bost / Schiper heard-of-model). The mapping from consensus theory to physics-substrate is `[speculation]` and tagged.

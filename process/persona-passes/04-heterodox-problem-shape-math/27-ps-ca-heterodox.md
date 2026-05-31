---
title: "Problem Shape — Cellular Automata Theorist (Heterodox)"
status: process
doc_type: persona_pass
updated_at: "2026-05-31"
---

# Problem Shape — Cellular Automata Theorist (Heterodox)

**Date:** 2026-05-28
**Baseline accepted:** Computation is substrate. Geometry is observer-frame artifact. The bundle is emergent. No-go theorems constrain observer-frames, not substrate. (00c)
**Predecessor in same domain:** `17-cellular-automata-loophole.md` named Nielsen-Ninomiya as the sharp lattice analog of Witten 1981 and closed the standard CA reading. This pass drops the Nielsen-Ninomiya premises.
**Persona:** Cellular automata theorist with strong heterodox lean — 't Hooft CA interpretation of QM, asynchronous / probabilistic CA, second-order reversible CA, continuous-state CA, Margolus partition CA with explicit chirality, spin-foam-as-CA (Penrose, Reisenberger-Rovelli, Engle-Pereira-Rovelli-Livine), Petri-net discrete physics, Gubrud's anti-mainstream CA-physics.

## (a) Thesis (mainstream-in-domain)

Textbook CA on a substrate-first reading: a regular hypercubic lattice with synchronous, deterministic, reversible, translation-invariant, local update rules over a small finite alphabet. The observerse projection is the hydrodynamic / Chapman-Enskog coarse-graining functor sending lattice configurations to bundle sections over an emergent 4-manifold. Chirality is supposed to be installed at the collision-table level and carried through the limit. Persona 17 already showed that under these textbook premises Nielsen-Ninomiya is the sharp lattice analog of Witten 1981: any local, Hermitian, translation-invariant, chirally-symmetric lattice fermion action produces fermion doubling. The CA pathway trades Witten for Nielsen-Ninomiya at the same load-bearing point. The textbook reading closes.

## (b) Heterodox antithesis

Nielsen-Ninomiya has four explicit premises: **locality**, **reversibility / hermiticity**, **translation-invariance**, and **smoothness in the lattice gauge field**. The heterodox CA literature drops each of these by design. Seven moves:

1. **'t Hooft cellular automaton interpretation of QM.** [speculation] Ontic states live at the CA cell level; quantum mechanics is the coarse-grained observer-frame readout. Chirality is an **ontic-substrate fact** about the rule's parity, not a derived feature of an emergent action. Nielsen-Ninomiya is a statement about a Hamiltonian action; the substrate has no action, only a rule. The theorem speaks past the substrate.

2. **Asynchronous CA (Nehaniv, Worsch).** [speculation] Cells update at independent times drawn from a Poisson process on each cell. There is no global lattice time. Nielsen-Ninomiya's locality premise presupposes a Brillouin zone, which presupposes a global time slicing; an asynchronous CA has neither. Fermion doubling is a Fourier-domain artifact that does not even type-check in the asynchronous setting.

3. **Margolus partition CA with explicit chirality.** [speculation] The block-partition itself is a Z$_2$-choice that breaks translation-invariance at the lattice level by one Margolus-block worth. The rule is reversible by construction (second-order CA) but parity-asymmetric at the partition seam. Chirality is built into the partition lattice, not into the collision table; the no-go theorem's translation-invariance premise fails by construction.

4. **Continuous-state CA (real-valued lattice gauge theory in CA form).** [speculation] Each cell carries a real-valued state; the update rule is a smooth local map. This is in a **different no-go class** than discrete-state Nielsen-Ninomiya, which is stated for finite-dimensional fiber Hilbert spaces. Continuous-state CA may admit chirality classes that the discrete theorem cannot rule out.

5. **Probabilistic / random CA.** [speculation] The rule itself is sampled per cell from a distribution. Chirality emerges as a **statistical-mechanical phase** of the rule-ensemble: a parity-broken phase exists in part of the rule-space's phase diagram, separated by a transition from the unbroken phase. Nielsen-Ninomiya is a zero-temperature statement; phase coexistence is a finite-temperature phenomenon.

6. **Spin-foam models as CA (Reisenberger-Rovelli, EPRL).** Combinatorial 4-simplices with local amplitudes; the "lattice" is a triangulation, not a hypercube; chirality enters at the foam-vertex level through the Immirzi parameter's complex phase. Nielsen-Ninomiya's hypercubic Fourier analysis does not apply to simplicial foams.

7. **Petri-net discrete physics (Sorkin causal-set adjacent).** [speculation] Causality is a **partial order**, not a total order. There is no notion of "the same time slice" at distant cells; locality is replaced by light-cone causality. Nielsen-Ninomiya's premises require a Cauchy slicing, which partial-order substrates do not have.

## (c) Aufhebung as a problem-shape question

Thesis says CA must respect locality + reversibility + translation-invariance + smoothness and then loses chirality to Nielsen-Ninomiya. Antithesis says the heterodox CA literature has dropped each premise individually for independent physical reasons. The Aufhebung within the domain:

> **The observerse is a CA-class substrate that drops at least one Nielsen-Ninomiya premise by construction (asynchrony, partial-order causality, partition-chirality, continuous-state, probabilistic-rule, or simplicial-foam), and SM chirality is a substrate-level rule-property whose 1-categorical synchronous-hypercubic-Hermitian shadow vanishes by the no-go theorem.**

Problem-shape question:

> **What is the minimal Nielsen-Ninomiya premise-violation class such that the substrate carries an ontic chirality (in 't Hooft's sense) whose hypercubic-synchronous-Hermitian shadow is null and whose coarse-grained observer-frame reproduces the SM chirality at the bundle-emergence boundary?**

## (d) WRK-326 next ask

Stop testing standard CA reductions. Start asking: **name the premise-violation class.** Concretely: (i) for asynchronous CA, compute whether a Poisson-update parity-broken rule has a continuum limit whose effective action admits a chiral SM-shaped subgroup, and check whether the asynchrony scale is observationally bounded by Margolus-Levitin. (ii) For Margolus partition CA with explicit chirality, ask whether the partition-seam parity survives the Chapman-Enskog limit or averages to zero. (iii) For spin-foam EPRL with complex Immirzi, check whether the Immirzi phase IS the SM chirality at the foam level (this is an established research direction). (iv) For 't Hooft CA, identify the ontic-substrate parity bit and ask whether a coarse-grained Born-rule readout reproduces the observed parity-violation amplitude.

## (e) Falsifiable mathematical sub-question

> **Does there exist an asynchronous or Margolus-partition CA with parity-broken local rule whose hydrodynamic continuum limit reproduces a chiral fermion action on a 4-manifold without fermion doubling, and is the required premise-violation (asynchrony rate, partition coarseness, or continuous-state range) bounded above by an observable Lorentz-invariance test at current precision?**

A negative answer (every premise-violation class that produces non-doubled chirality also produces Lorentz-invariance violation above current bounds, or the chirality re-doubles in the hydrodynamic limit by a Reisenberger-Rovelli-class anomaly-matching argument) closes the heterodox CA route: the premise-violations needed to escape Nielsen-Ninomiya are themselves observationally ruled out. A positive answer with bounded premise-violation hands WRK-326 a concrete CA-substrate working specification that competes with the Connes spectral-triple, chiral-PEPS, and multiway-hypergraph candidates of 00c, with a sharp Lorentz-violation experimental target rather than a family-frontier exhaustion.

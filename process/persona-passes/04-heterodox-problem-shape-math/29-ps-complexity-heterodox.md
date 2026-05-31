---
title: "Complexity / Decidability — Heterodox Hegelian Pass (Problem Shape)"
status: process
doc_type: persona_pass
updated_at: "2026-05-31"
---

# Complexity / Decidability — Heterodox Hegelian Pass (Problem Shape)

**Persona:** Computational complexity / decidability theorist, heterodox lean. Penrose non-computable physics, hypercomputation, MIP* = RE, Chaitin Ω, ZFC-independence of physics, descriptive complexity beyond PH, physical Church-Turing as hypothesis not theorem.
**Predecessors:** `00-`, `00b-`, `00c-` (substrate-inversion baseline), prior pass `19-complexity-decidability-loophole.md` (Rice-undecidability meta-frame).
**Date:** 2026-05-28.
**Output:** problem-shape. No GU lit. No silent strengthening.

## (a) Thesis (mainstream-in-CS)

Physical laws are Turing-computable. Quantum dynamics sits in BQP under reasonable encodings; classical limit lands in BPP / P. The "physical Church-Turing thesis" is taken as load-bearing background assumption: any physically realizable process can in principle be simulated by a Turing machine to arbitrary precision in bounded resources. Under this thesis, derivation questions are decidable when the underlying structure is regular (smooth-KK, cobordism, invertible field theory) and undecidable in the Rice sense when extensional semantic properties of arbitrary UV theories are asked. The prior pass `19-` lived inside this thesis: Rice was the meta-frame, but the universe of discourse was still Turing-bounded computation.

## (b) Heterodox antithesis

Physical reality is not required to be Turing-computable, and several established results suggest it is not.

- **Penrose-Lucas / "shadows of the mind"** `[speculation]`: Gödel-style self-reference arguments claim mind (and by extension physics, if mind is physical) contains non-algorithmic elements. The argument is contested but live.
- **MIP* = RE (Ji-Natarajan-Vidick-Wright-Yuen 2020)**: the quantum value of nonlocal games is RE-complete, hence undecidable. Quantum mechanics, formalized with commuting-operator vs tensor-product entanglement models, has provably undecidable separations. This is established theorem, not speculation.
- **Hypercomputation in Malament-Hogarth spacetimes** `[speculation]`: certain general-relativistic spacetimes admit worldlines along which an observer receives signals from infinitely-long proper-time computations. If physically realizable, halting becomes decidable for some observer-class.
- **Chaitin's Ω** `[speculation]`: algorithmically random, encodes halting, no finite proof system computes more than finitely many bits. If a physical observable were Ω-like, no finite-axiomatized physical theory could derive it.
- **ZFC-independence of physics propositions** `[speculation]`: spectral gap problem (Cubitt-Perez-Garcia-Wolf 2015) is undecidable for arbitrary translation-invariant Hamiltonians. Some physical questions may be set-theoretically independent.
- **Descriptive complexity beyond PH**: physical theories indexed by structures whose definability sits above the polynomial hierarchy. BQP-vs-PH separation (Raz-Tal 2019) is established.

The antithesis: drop the physical Church-Turing thesis. Treat "physics is computable" as a hypothesis the substrate is not obligated to honor.

## (c) Aufhebung problem-shape

Computability is not a property of physics. It is a property of observer-extracted descriptions. Different observer-classes (finite Turing, quantum BQP, hypercomputing Malament-Hogarth, Ω-oracle-equipped) extract different computability-bounded descriptions of the same substrate. The derivation question is observer-class-relative: a structurally meaningful class-invariant, undecidable for finite Turing observers, decidable for some hypercomputing observers, RE-complete in the quantum-correlation regime per MIP* = RE.

This refines the 00c substrate-inversion. 00c said: computation is substrate, geometry is observer artifact. Heterodox refinement: **the substrate is not even required to be Turing-computational**. The substrate may be a structure whose observer-extracted descriptions form a hierarchy of computability classes, none of which is the substrate. "Is the GU derivation question decidable" is the wrong shape. The right shape: **what is the observer-class minimum at which the derivation question becomes decidable, and does the GU lane's three-year exhaustion pattern reflect Joe operating below that minimum?** `[speculation]`

If the minimum observer-class is BQP, quantum simulation is in principle a path. If it is RE-complete (MIP* analogy), no Turing-bounded search terminates. If it is hypercomputational, no physically realizable observer in our spacetime decides it.

## (d) WRK-326 next ask

Before picking substrate class A-D in 00c, ask: what observer-class is Joe deploying when he searches? If the search is finite-Turing (analytic-symbolic), it cannot terminate on an MIP*-class or Ω-class question. Re-stage WRK-326's central question to: **"specify the observer-class required to decide the GU derivation question, and check whether any physically realizable observer-class meets that requirement."** If none does, the lane closes not as undecidable-by-analytic-search but as **physically-unobservable-by-finite-observers**.

## (e) Falsifiable sub-question

Is the chirality-content of the SM bit-sequence Chaitin-Ω-like (algorithmically random, no finite-axiomatized derivation possible)? Concrete test: compute the Kolmogorov complexity lower bound on the bit-string encoding (gauge group, generation count, chiralities, Yukawa pattern, CKM, PMNS). If K is bounded by a short program (the SM Lagrangian itself), chirality is not Ω-like and finite derivation remains possible in principle. If K saturates the bit-length (incompressible), chirality is Ω-like and no finite derivation exists for any UV theory, GU or otherwise. `[speculation]` The empirical SM parameter values appear partially compressible (gauge structure compresses, Yukawa hierarchy resists), suggesting a mixed regime: structural chirality finitely derivable, parameter values Ω-like.

## Dialectical move

Drop the physical Church-Turing thesis. Relocate computability from substrate property to observer-class property. Reframe WRK-326's central question as observer-class-minimum specification, not substrate-class selection.

---
title: "Problem Shape — Tensor Network / Quantum Circuit (Heterodox)"
status: process
doc_type: persona_pass
updated_at: "2026-05-31"
---

# Problem Shape — Tensor Network / Quantum Circuit (Heterodox)

**Date:** 2026-05-28
**Baseline accepted:** Computation is substrate. Geometry is observer-frame artifact. The bundle is emergent. No-go theorems constrain observer-frames, not substrate. (00, 00b, 00c)
**Prior pass built past:** 18-quantum-circuits-tensor-network-loophole.md (chiral PEPS / HaPPY as adjacent positive program, Freed-Hopkins as substantive closure).
**Persona:** Tensor-network / quantum-circuit theorist, heterodox lean maximized.

## (a) Thesis (mainstream-in-TN)

Orthodox TN: a finite tensor network with bounded bond dimension, MERA-style coarse-graining, a chiral PEPS / HaPPY-style holographic code whose 14D bulk encodes 4D boundary content. Chirality of the boundary CFT is read off the chiral central charge c_- of the bulk topological order. The tensor network is a combinatorial object whose tensors live in finite-dimensional Hilbert spaces; isometries are explicit; Reshetikhin-Turaev assigns a TQFT to the modular tensor category of bulk anyons; boundary anyon content is supposed to encode SM gauge data. The substrate is "tensors plus bonds." (This is 18's framing.)

## (b) Heterodox antithesis

The finite combinatorial reading is itself a smuggled-in regularization. The further-heterodox reading refuses it:

1. **"It from Qubit" inverts substrate-bundle.** Wheeler's "it from bit" promoted to qubits as substrate. Geometry is not what tensor networks discretize; geometry IS the entanglement pattern of a quantum state in an abstract Hilbert space, with no underlying manifold. Van Raamsdonk: spacetime connectivity = entanglement. Witten's argument that geometry IS entanglement in CFT/AdS makes this literal, not metaphorical. The 14D observerse, on this lens, is not a discretized manifold but an entanglement graph whose "dimensionality" is a coarse statistic. [speculation]

2. **ER=EPR (Maldacena-Susskind).** Wormholes ARE entangled qubits. Geometric and entanglement descriptions are dual. The "14D bulk" and the "4D boundary" are not two layers; they are two readings of one entanglement pattern. The projection is gauge, not dynamics. Chirality is then an entanglement-pattern invariant, not a smooth or even tensor-graph invariant. [speculation]

3. **Almheiri-Dong-Harlow: bulk = logical qubits, boundary = physical qubits.** AdS/CFT IS a quantum error correcting code. Reverse-engineer: 14D bulk = logical qubits carrying GU's content; 4D boundary = physical qubits we observe. Chirality is a **logical-qubit phase** that the QEC decoding preserves even when the boundary smooth shadow cannot see it. Witten 1981 then applies to the smooth shadow, not to the logical content. [speculation]

4. **Random tensor networks (Hayden-Nezami-Qi-Thomas-Walter-Yang).** Generic bulk gives generic holographic codes with maximal entanglement. Chirality could be a **generic logical phase** of random tensor networks at large bond dimension, robust against perturbation of the bulk Hamiltonian. The tensor network goes infinite-dimensional and "rough" in a Hairer-regularity sense: states are not in finite Hilbert spaces but in distributional limits. [speculation]

5. **Spin networks (LQG, Penrose) and MTC beyond Drinfeld center.** Spin networks are combinatorial precursors to geometry with chirality at the spin-network level. Modular tensor categories with nontrivial chiral central charge (beyond Drinfeld centers) carry chirality as a categorical invariant. SM as a specific MTC's boundary content moves chirality from "smooth or discrete" to "categorical."

## (c) Aufhebung as problem-shape

Thesis: finite TN bulk encodes 4D boundary via isometry. Antithesis: there is no TN substrate; there is an abstract entanglement pattern, and the tensor network is one observer-frame discretization. The Aufhebung: **the substrate is the entanglement pattern of an infinite-dimensional QEC code with logical-qubit chirality; the tensor network, the smooth manifold, and the 14D/4D split are all decoding-map readouts at different observer resource bounds. Chirality is a categorical/logical phase preserved by the QEC decoder, invisible to smooth-shadow no-goes that operate only on the physical boundary.**

Problem-shape:

> **Does there exist a QEC code whose logical Hilbert space carries an MTC chirality invariant (chiral central charge c_- consistent with SM) that survives decoding to a physical 4D boundary whose smooth shadow obeys Witten 1981, such that the logical-physical decoding is the observerse projection?**

## (d) WRK-326 next ask from this lens

Stop asking "does GU's bundle reduction deliver chiral SM." Start asking: **what is the QEC code class GU is implicitly proposing, and what is the chiral central charge of its logical algebra?** Concretely: specify the logical algebra (modular tensor category beyond Drinfeld center), compute c_- of the logical layer, check whether the decoding isometry preserves chirality into the physical boundary while letting the boundary smooth-shadow obey Witten 1981. The "loophole" lives in the logical-physical gap, not in the bulk-boundary holography.

## (e) Falsifiable sub-question

> **Does there exist a holographic quantum error correcting code whose logical algebra is a chiral MTC with nontrivial c_- consistent with SM chirality, such that (i) the decoding isometry preserves chirality from logical to physical layer, (ii) the physical boundary smooth-shadow obeys Witten 1981 / Freed-Hopkins as a derived consequence of the decoding, and (iii) the logical-qubit chirality is unobservable from any boundary-region reconstruction, yet operationally testable via complementary recovery on entanglement-wedge boundaries?**

Negative answer (no such code exists, or chirality cannot survive decoding without violating complementary recovery) closes the heterodox TN route and confirms Freed-Hopkins as terminal at the logical layer too. Positive answer hands WRK-326 a concrete logical-MTC specification to stress-test against Freed-Hopkins at the logical-physical boundary, not just at the bulk-boundary boundary.

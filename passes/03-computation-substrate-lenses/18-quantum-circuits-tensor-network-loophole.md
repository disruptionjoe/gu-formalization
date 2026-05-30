# Persona 18 — Quantum Computation / Tensor Network / Holographic Codes

**Lens:** Spacetime as emergent from entanglement structure. MERA, holographic codes (HaPPY), AdS/CFT as tensor network, chiral PEPS, topological order, ER=EPR. Bulk-boundary as encoding/decoding map.

## (a) One-sentence steelman

The 14-dim observerse is the bulk Hilbert space of a holographic quantum code; the observerse projection is the decoding isometry sending bulk operators to a 4D boundary CFT, with MERA-style coarse-graining picking out emergent locality and chiral topological order in the bulk supplying the Standard Model anyon content on the boundary.

## (b) Strongest first-principles construction

Replace "Met(X)" as a smooth bundle with a tensor network T whose graph approximates a discretization of a 14-dim region. Each tensor is a local isometry from a higher-bond-dimension level to a lower-bond-dimension level (MERA structure). The boundary of T is a 1+3-dim quantum state |Psi>_4. The "projection" is the holographic decoding map V: H_bulk^14 -> H_bdry^4, an isometric embedding that satisfies complementary recovery (HaPPY code property): every bulk local operator at a point p is reconstructible from a boundary region whose entanglement wedge contains p.

In this reading the 4D "observed" physics is not a geometric quotient of a 14D manifold but a holographic encoding. The 10 fiber directions are not extra dimensions to be reduced over but ancilla / virtual bond legs that carry entanglement structure rather than propagating modes. [speculation]

## (c) Where it does load-bearing work for chirality and SM emergence

**Chirality from chiral topological order.** Chiral topological orders (e.g., Kitaev's 16-fold way, chiral spin liquids) exhibit gapless chiral edge modes by bulk-boundary correspondence: the bulk has non-zero chiral central charge c_- and the boundary inherits chiral CFT content that **cannot be regularized lattice-locally without breaking some symmetry**. This is structurally different from smooth KK: chirality is not derived from smooth-manifold parity, it is built into the entanglement pattern of the bulk ground state.

**Chiral PEPS / chiral MERA** are tensor-network states known to host chiral topological order. They have the suggestive property of evading certain lattice-fermion no-go arguments (Nielsen-Ninomiya-like) because the construction is not a discretized smooth field theory, it is an entanglement-defined state. If the 14D observerse-as-tensor-network is built from chiral PEPS primitives, the boundary 4D theory **inherits chirality structurally rather than by-input**. [speculation]

**SM as anyon content.** Reshetikhin-Turaev assigns a 3D TQFT to a modular tensor category; a 4D bulk TQFT yields a 3D boundary modular content. Push this one dimension up: a 14D bulk topological / entanglement theory could in principle have a 4D boundary TQFT whose anyon content encodes SM gauge data. The SM group would be the symmetry group of the modular category, not a subgroup of GL(4). [speculation, large]

## (d) What must be true

1. The bulk 14D tensor network is a **chiral** topological-ordered state with non-zero chiral central charge.
2. The boundary entanglement spectrum (Li-Haldane) reproduces the SM chiral fermion content (48 Weyl fermions in three generations).
3. The decoding isometry V satisfies complementary recovery and **respects monogamy of entanglement**: no two boundary 4D regions can independently reconstruct the same 14D bulk operator, which is what enforces causal structure / no-cloning at the 4D level.
4. The Ryu-Takayanagi formula (or higher-dim analogue) holds, so 4D emergent geometry has area = entanglement; this is where 4D GR is supposed to come from (Van Raamsdonk-style).
5. Hayden-Preskill information recovery delineates **which boundary observers can access which bulk degrees of freedom** — this is the operational meaning of the "observerse projection."

## (e) Verdict on whether tensor-network substrate opens a path the prior lenses missed

**Formally: yes, weakly.** Tensor-network / holographic-code substrates are structurally distinct from the 5 loophole classes in 00b (stochastic, measurement-channel, orbit-equivalence, derived-stack, Cartan-tractor). They are entanglement-defined rather than smooth-defined, so Witten 1981 narrowly does not apply, **and** chiral-PEPS constructions historically dodge Nielsen-Ninomiya-class lattice obstructions in a way the prior lenses did not articulate.

**Substantively: opens a real but adjacent direction, not a derivation from GU.** This is closer in spirit to "Geometric Unity as holographic code" — a re-foundation, not a derivation. It collides with Freed-Hopkins the same way P4 does: invertible-field-theory anomaly classification lifts to topological-order classification (Kitaev-Wen) and the chirality has to be cobordism-consistent. Plus the construction requires the 14D bulk to **be** a chiral topological order with very specific c_-, which is an installed input, not delivered by Met(X).

**Closest converged adjacent program:** holographic code + chiral PEPS as a substrate for SM emergence, which is a live research direction (HaPPY, Pastawski-Yoshida, Van Raamsdonk, Vidal, Cirac) independent of GU. WRK-326 could legitimately re-scope around it the same way 00b suggested re-scoping around Connes spectral triples. Both are stronger adjacent programs than continuing to chase GU's stated geometry.

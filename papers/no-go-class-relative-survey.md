---
title: "No-Go Theorems as Class-Relative Obstructions: A Survey with a Geometric Unity Test Case"
status: draft
doc_type: paper
updated_at: "2026-06-20"
depends_on:
  - "canon/no-go-class-relative-map.md"
  - "active-research/pati-salam-chain-verification.md"
  - "active-research/signed-readout/signed-readout-consolidated.md"
  - "paper-formalization-candidates.md"
  - "canon/six-axis-specification-protocol.md"
---

# No-Go Theorems as Class-Relative Obstructions: A Survey with a Geometric Unity Test Case

## Abstract

Four families of no-go theorems — Witten (1981), Nielsen-Ninomiya (1981), Freed-Hopkins (2021, confirmed Grady 2023), and Distler-Garibaldi (2010) — constrain the emergence of chiral fermions, anomaly cancellation, and gauge unification in physics. Each is a correct theorem. Each also fixes an input class: smooth compact geometry, local on-site lattice symmetry, invertible extended functorial QFT, or single-E₈ representation theory. We survey each theorem's exact assumptions and the published literature on class exits, then organize the results through a *forgetful-image framework*: every known evasion adds structure that a class-specific forgetful operation discards, and the no-go theorem is a statement about the image of that operation.

As a concrete test case, we apply this framework to Eric Weinstein's Geometric Unity program (2021 draft), whose constructions propose specific class exits for three of the four families. We report a computational verification of the program's most falsifiable claim — the Pati-Salam reduction chain Spin(7,7) → ⋯ → SU(3) × SU(2) × U(1) and the associated 16-state quantum number table — confirming that the group theory is internally correct (19/19 assertions pass with independent cross-check). We also report a signed-readout boundary theorem that provides a partial bridge between chirality obstructions and coordination-freedom in distributed systems, addressing the Nielsen-Ninomiya family from a novel angle.

The survey's contribution is organizational, not physical: a six-axis specification protocol that forces any proposed class exit to state its substrate, observer, pairing, causal order, emergence class, and coordination loop before making chirality or anomaly claims. A structural finding is that the four theorems divide into two logical types: three are *class-relative* no-go theorems (constraining categories of structures) for which the forgetful-image framework applies naturally, while the fourth (Distler-Garibaldi) is a *group-specific* impossibility result (constraining E₈ representations specifically) that lies outside the framework's scope — a distinction that sharpens both the framework and the analysis of D-G.

---

## 1. Introduction

The Standard Model of particle physics has a chiral fermion sector: left-handed and right-handed fermions transform differently under the electroweak gauge group. Any proposed unification or extension of the Standard Model must eventually produce this chirality, and several powerful theorems constrain how it can arise. These are commonly called "no-go theorems," and they are correct — but they are correct *within specific mathematical classes*. Outside those classes, they have nothing to say.

This distinction matters because the most common use of no-go theorems in the physics literature is as universal slogans: "you can't get chiral fermions from extra dimensions," "you can't put chiral fermions on a lattice," "anomalies must cancel." Each slogan omits the class assumptions that make the theorem true. The omission is usually harmless when everyone is working inside the same class. It becomes harmful when someone proposes a construction in a different class and the slogan is deployed as if it still applies.

This paper does three things. First, it surveys four no-go theorem families with their exact assumptions and known class exits (§2–§5). Second, it introduces a *forgetful-image framework* that organizes all known evasions under a common pattern: a richer mathematical object maps to the theorem's input class via a forgetful operation, and the theorem correctly reports that the image has no chirality — because the chirality data was carried by exactly what the forgetful operation discarded (§6). Third, it applies this framework to a specific test case — the Geometric Unity program of Weinstein (2021) — as a worked example of how a concrete proposed class exit can be evaluated against the framework, including a computational verification of its most falsifiable group-theoretic claim and a novel lattice-theoretic result (§7–§8).

### 1.1 What this paper does not claim

This paper does not claim that any no-go theorem is wrong. Inside their stated classes, they are correct theorems with confirmed proofs. It does not claim that Geometric Unity is correct physics. It does not claim that the forgetful-image framework is itself a theorem — it is an organizational device. And it does not claim that the framework handles all four theorem families equally well; §5 and §9 are explicit about where it strains.

---

## 2. Witten (1981) — Chirality from Smooth Kaluza-Klein Reduction

### 2.1 Statement

In smooth compactifications of higher-dimensional theories with internal manifold X smooth, compact, and closed, and with trivial background gauge data, the four-dimensional fermion spectrum is non-chiral. The canonical restatement: chiral fermions do not arise when the internal manifold X is smooth.

### 2.2 Assumptions

1. Internal manifold X is smooth, compact, closed (no boundary).
2. Reduction is Kaluza-Klein at the level of the action, with smooth Levi-Civita data.
3. No nontrivial gauge background, instanton, or flux on X.
4. No orbifold singularities, branes, or topological defects.
5. The four-dimensional fermion sector is read off as zero modes of the Dirac operator on X coupled only to gravity.

### 2.3 Known evasions

All successful published evasions are *geometric* class exits:

- **Flux/instanton background** (Randjbar-Daemi, Salam, Strathdee 1983): drops assumption (3).
- **Boundary** (Hořava-Witten 1996): 11d on a manifold-with-boundary; E₈ on each boundary component. Drops (1).
- **Orbifold + brane-localization** (Georgi, Grant, Hailu 2000; fat-brane chirality): drops (1)/(4).
- **Twisted boundary conditions** (Dobrescu-Pontón 2004): drops (1)/(4).
- **Singular G₂-holonomy** (Acharya-Witten 2001): drops (1) directly.
- **Freund-Rubin with singularities** (Acharya, Denef, Hofman, Lambert 2003).

No published evasion uses stochastic, observer-relative, causal-set, or hypergraph language.

### 2.4 Forgetful-image reading

**Richer datum**: a stratified geometric substrate (X̃, S, B) where X̃ is a singular or boundary variety, S ⊂ X̃ is the singular/boundary stratum, and B is gauge/flux/brane data on the stratification. Chirality is carried by data at S.

**Forgetful operation**: the smoothing functor ϕ_smooth : (X̃, S, B) ↦ (X', trivial-bg) that resolves singularities, deletes boundary/brane data, and trivializes gauge background.

**What gets lost**: net chirality data localized on S; anomaly-inflow contributions from boundary components; the topological class of the gauge background. The four-dimensional effective spacetime (the *relation*) survives; the mechanism (where chirality enters) does not.

**Analogy strength**: STRONG. Every cited evasion fits this template.

### 2.5 GU's proposed exit

The 2021 Geometric Unity draft proposes a specific construction that addresses the Witten class. The Observerse (X⁴, Y¹⁴ = Met(X⁴), {ι}) replaces the conventional setup: spacetime X⁴ is not the arena of field theory; the 14-dimensional space of metrics Y = Met(X⁴) is. Gauge fields, spinors, and connections live natively on Y and are *pulled back* to X via the observation map ι, making them "invasive" rather than "native" in the paper's terminology.

This construction does not evade Witten by the standard route (adding singularities, boundaries, or flux to X). Instead, it changes the *unit*: fields do not live on a compactified internal manifold at all. They live on Met(X), and the four-dimensional fermion spectrum is read off via pullback through a metric choice, not via zero modes of a Dirac operator on a smooth internal space. Assumption (5) — that fermions are zero modes on X — does not apply, because the construction's fermions are chimeric spinors on Y observed via ι.

**Assessment**: the exit is geometrically precise (the Observerse is a well-defined fiber bundle) and does not invoke any of the structures that Witten's theorem constrains. Whether it produces the correct physics is a separate question; the claim here is only that it is not *within* the Witten class.

---

## 3. Nielsen-Ninomiya (1981) — Lattice Fermion Doubling

### 3.1 Statement

A free bilinear lattice fermion action that is local, Hermitian, translation-invariant, and carries exact lattice U(1)_V and U(1)_A symmetries necessarily has an equal number of left- and right-handed fermion species. The modern restatement: the obstruction is anomaly-theoretic and survives in any system where chiral symmetry is realized on-site with a discrete energy-momentum spectrum.

### 3.2 Assumptions

1. Locality (finite-range hopping).
2. Hermiticity of the lattice Hamiltonian.
3. Translation invariance.
4. Exact lattice U(1)_V with conserved charge.
5. Exact lattice U(1)_A realized on-site.
6. Free/bilinear action.
7. Spectrum is continuous in lattice momentum and has discrete on-site charge structure.

### 3.3 Known evasions

- **Domain wall** (Kaplan 1992): drops (3) by going to d+1 with a defect; chirality lives on the defect.
- **Overlap/Ginsparg-Wilson** (Neuberger 1997; Lüscher 1998): drops (5) in its naive on-site form; chirality is realized by a modified algebra. Lüscher: "no contradiction because the symmetry is realized in a different way than assumed in the theorem."
- **Chiral PEPS** (Wahl, Tu, Schuch, Cirac 2013): partial success in 2d.
- **2d anomaly-free chiral gauge** (Berkowitz, Cherman, Jacobson 2024): Villain/bosonization.
- **QCA flavoring** (Bakircioglu, Arnault, Arrighi 2025): coexists with the theorem.

The 3+1d local chiral-gauge regularization remains open.

### 3.4 Forgetful-image reading

**Richer datum**: a (d+1)-dimensional bulk + d-dimensional boundary anomaly-inflow object together with the symmetry-realization data on the boundary.

**Forgetful operation**: the on-site locality and exact symmetry functor ϕ_local : (bulk + boundary + modified-symmetry algebra) ↦ d-dim local on-site lattice.

**What gets lost**: the bulk SPT data; the modified Ginsparg-Wilson algebra structure; the anomaly-inflow current.

**Analogy strength**: STRONG. The bulk+boundary inflow reading is the standard modern understanding of why domain-wall and overlap fermions work.

### 3.5 GU's proposed exit

The 2021 paper's effective chirality claim (Section 11.4) proposes that the Dirac operator on Y¹⁴ is globally non-chiral — the theory has no fundamental chirality. What appears as chirality in the Standard Model is claimed to be an effective phenomenon: in regions of low scalar curvature, the non-chiral theory effectively decouples into chiral sectors.

This places chirality on the *emergence axis* (L5 in the six-axis protocol, §8) rather than the substrate axis. If correct, the Nielsen-Ninomiya theorem would apply to the effective, decoupled theory (which does exhibit chirality) but would say nothing about the fundamental, non-chiral theory on Y — because the fundamental theory does not claim to have chiral fermions.

**Assessment**: this is the *weakest* of GU's proposed exits. The effective chirality claim is stated narratively, without a decoupling theorem, without an energy scale estimate, and without specifying what "standard decoupling arguments" means. As a proposed class exit it is structurally coherent (changing the emergence class is a legitimate axis change), but as a mathematical claim it is under-specified.

### 3.6 The signed-readout boundary theorem

A complementary approach to the Nielsen-Ninomiya family comes from the signed-readout boundary theorem, developed independently of the GU program. This result provides a precise vocabulary for how a globally non-chiral theory can have effectively chiral readouts.

The core result is a factorization: every lattice observable Q factors as Q = read ∘ acc, where acc is a monotone-provenance accumulator (per-site, bounded-radius, locally-computable, append-only) and read is a fixed scalar readout. The composite is CALM-extension monotone (coordination-free) if and only if every generator-weight of the readout lies in the positive cone of the output group.

For a signed observable like the axial charge Q_A = n₊ − n₋, the provenance layer is monotone (each site's contribution accumulates without coordination), but the readout is signed — adding more input data can decrease the aggregate. The Jordan-decomposed CALM (JD-CALM) framework resolves this by splitting Q into Q⁺ and Q⁻, each accumulated monotonically, with the signed difference computed only at read time. Under JD-CALM, the instanton/anti-instanton signed cancellation is reclassified from "monotonicity violation" to "expected behavior of a Jordan-decomposed signed aggregate."

The bridge to Nielsen-Ninomiya: assumptions (1), (3), (4), (5), and (7) translate precisely onto named distributed-systems concepts (bounded communication radius, anonymous network model, CRDT safety invariant, strong per-replica consistency, finite state space). Assumption (5) — exact on-site chiral symmetry — maps to "strong per-replica consistency with no coordination round," and Lüscher's explanation of why Ginsparg-Wilson evades the theorem ("the symmetry is realized in a different way") is exactly the statement that the GW algebra relaxes strong-consistency-without-coordination.

**Honest scope**: the bridge recovers at the signed-real readout layer but *fails* at the integer topological-index readout layer, because integer recovery requires either unbounded truncation or a non-CALM rounding step. The analogy is "theorem-shaped, second-pass justified" — strong enough to deserve theorem-grade work but not yet a theorem.

---

## 4. Freed-Hopkins (2021, confirmed Grady 2023) — Anomaly Classification

### 4.1 Statement

Deformation classes of reflection-positive, invertible, extended functorial field theories with fixed symmetry type are classified by a generalized cohomology/bordism group. This is not a no-go theorem in the Witten/Nielsen-Ninomiya style; it is a classification theorem that functions as a no-go via the Wang-Wen-Witten/Córdova-Ohmori-Shao package: it tells you which anomalies can be canceled and which cannot, and when an anomalous boundary cannot be made symmetric and gapped.

### 4.2 Assumptions

1. Extended functorial field theory in the Lurie-Freed-Hopkins sense.
2. Invertibility (partition function is a unit).
3. Reflection positivity.
4. Fixed symmetry type / tangential structure.
5. Existence of a valid low-energy EFT approximation.
6. Boundary obstruction: boundary is invertible/trivially gapped (Wang-Wen-Witten extension).

### 4.3 Known evasions

- **Boundary topological order** (Wang, Wen, Witten 2017): drops (6); anomalous boundary becomes non-anomalous after symmetry extension on a topologically-ordered boundary.
- **Symmetry-extension obstruction** (Córdova, Ohmori, Shao 2019): sharp limit — extension fails when an anomaly-inflow obstruction persists.
- **Mixed spatial/crystalline symmetry** (Debray 2021): extends (4) to mixed spatial-fermion-parity symmetries within the same paradigm.
- **Grady 2023**: confirms the Freed-Hopkins conjecture, establishing the bordism description as rigorous.
- **Kapustin-Sopenko 2024**: anomaly index for locality-preserving spin-chain actions; persistence even beyond band-fermion setting.

### 4.4 Forgetful-image reading

**Richer datum**: an enriched bordism category whose objects carry data beyond (symmetry type, tangential structure). Two concrete candidates: (a) observer-pairing enriched bordism (objects carry observer worldlines or QRF data); (b) average/crystalline/mixed-symmetry enriched bordism.

**Forgetful operation**: the underlying-bordism functor ϕ_underlying : Bord^{enriched} ↦ Bord^{symmetry-type}.

**What gets lost**: observer-worldline/QRF data, average-symmetry information, or any structure not encoded in (symmetry type, tangential structure).

**Analogy strength**: MEDIUM. For adjacent enrichments (crystalline, mixed, average), the analogy is essentially what the literature already does. For observer-enrichment, it is a research proposal, not an established result.

**Where it may break**: Córdova-Ohmori-Shao shows that anomaly-inflow obstruction often persists even after class changes. Kapustin-Sopenko shows locality-preserving extensions don't generally evade. If observer-enrichment has a similar persistence theorem, the forgetful-image frame yields no new information.

### 4.5 GU's proposed exit

The 2021 paper does not directly engage Freed-Hopkins anomaly classification. The paper's construction lives in smooth differential geometry, not in the bordism/cobordism framework. The six-axis protocol (§8) handles this gap by noting that a GU-class construction would need to specify what happens at the L2 (observer) and L4 (causal order) axes to make contact with the Freed-Hopkins input data.

**Assessment**: OPEN. This is a genuine gap in the GU program's interface with modern anomaly theory.

---

## 5. Distler-Garibaldi (2010) — Single-E₈ Representation Theory

### 5.1 Statement

There is no real Lie group E together with subgroups SL(2,ℂ) and G such that: (ToE1) G is connected, compact, and centralizes SL(2,ℂ); (ToE2) in the SL(2,ℂ) × G decomposition of Lie(E), V_{m,n} = 0 for m+n > 4; (ToE3) V_{2,1} is a complex G-representation — inside complex E₈ or any real form of E₈.

### 5.2 Assumptions

1. Single real form of E₈ as the symmetry group.
2. Four-dimensional Lorentz/spin-statistics structure embeds as SL(2,ℂ) ⊂ E.
3. Internal gauge structure embeds as a connected compact subgroup G centralizing SL(2,ℂ).
4. Matter content lives in V_{m,n} with m+n ≤ 4 (no exotic higher-spin matter).
5. Chirality means V_{2,1} is complex as a G-representation.
6. The construction is finite-dimensional and at the level of representation theory of one E.
7. No bundle/compactification/flux data is added.

### 5.3 Known evasions

All successful evasions leave the class entirely:

- **E₈ × E₈ heterotic with Calabi-Yau** (Braun, He, Ovrut, Pantev 2005–2006): drops (1) and (7). Realistic three-generation SM.
- **Flux breaking** (Anderson et al. 2014–2015): same class exit.
- **GraviGUT SO(3,11)** (Nesti-Percacci 2009–2010): drops (1) entirely. One family only.
- **K(E₁₀) Kac-Moody quotient** (Meissner-Nicolai 2025): drops (1) and (6). Far from finished.

There is no known richer-substrate datum that lives inside single-E₈ representation theory and reproduces three SM generations plus gravity.

### 5.4 Why D-G is structurally different from the other three

The first three no-go theorems constrain *broad classes* of mathematical structures: smooth geometries (Witten), local lattice actions (Nielsen-Ninomiya), invertible extended functorial QFTs (Freed-Hopkins). Each class has internal room for enrichment — smooth geometry can be enriched to singular geometry, a local lattice can be enriched with a bulk, standard bordism can be enriched with additional data. The forgetful-image framework works naturally for these theorems because evasions add structure *within a nearby category* and the forgetful operation projects back to the original class.

Distler-Garibaldi is fundamentally different. It constrains representations of *one specific group family*: real forms of E₈. Single-group representation theory is atomically narrow — there is no "enriched E₈ representation theory" that contains E₈ representation theory as a shadow. You cannot make E₈ richer while staying inside E₈. Every successful construction that produces chiral SM fermions necessarily uses a *different algebraic object*: a product group (E₈ × E₈), a different Lie group (SO(3,11)), a Kac-Moody extension (K(E₁₀)), or a geometric structure group (Spin(7,7)).

This means D-G is not a "stress case" for the forgetful-image framework. It is *outside the framework's scope*. The framework applies to class-relative no-go theorems — theorems that constrain a category of structures. D-G is a group-specific impossibility result that constrains one specific algebraic atom. Calling D-G a stress case was a category error in the earlier analysis: the framework was being asked to handle a theorem of a different logical type.

The correct classification:

| Theorem | Type | Input class structure | Admits enrichment? |
|---|---|---|---|
| Witten | Class-relative | Category of smooth geometries | Yes — singular, boundary, brane |
| Nielsen-Ninomiya | Class-relative | Category of local lattice actions | Yes — bulk+boundary, modified algebra |
| Freed-Hopkins | Class-relative | Category of invertible extended QFTs | Yes — enriched bordism |
| Distler-Garibaldi | Group-specific | Single algebraic atom (E₈ reps) | No — can only use different groups |

The forgetful-image framework applies cleanly to the first three. It does not apply to D-G, and this is not a deficiency — it is a scope boundary that reflects a genuine structural difference between the theorems.

### 5.5 What D-G does contribute

Although D-G is outside the forgetful-image framework, it constrains the landscape of possible unification groups. Any program that uses E₈ as its unification group must either add external data (bundle, compactification, flux — as in E₈ × E₈ heterotic) or abandon E₈ entirely. This is useful information, but it is information about *which groups work*, not about *which classes of structures can carry chirality*.

D-G's real import is as a *selection rule* on the space of candidate unification groups: it eliminates one specific (and culturally prominent) candidate. Programs that never proposed E₈ — including the SO(10) GUT tradition, Pati-Salam, GraviGUT, and Geometric Unity — are simply not addressed by D-G.

### 5.6 GU's relation to D-G

GU's construction does not use E₈. Its structure group chain is:

```
Spin(7,7) → Spin(1,3) × Spin(6,4) → SU(4) × SU(2) × SU(2) → SU(3) × SU(2) × U(1)
```

This chain has been **computationally verified** (§7). It passes through Pati-Salam (SU(4) × SU(2)_L × SU(2)_R), not through E₈. Spin(7,7) is a real form of Spin(14), which has dimension 91 and rank 7 — not even the same rank as E₈ (dimension 248, rank 8). The two groups live in disjoint parts of the Lie classification. D-G's hypotheses are not met, and there is no natural map between the constructions.

The deeper point: GU produces SM quantum numbers from the *normal-bundle spinor* S/(ℝ^{6,4}), which gives the well-known SO(10) ⊃ Pati-Salam ⊃ SM chain. This is the same **16**-spinor representation that appears in SO(10) grand unification — a construction that has been known since the 1970s and that D-G does not constrain (because SO(10) is not E₈). GU's novelty is not the group theory of the chain (which is textbook) but the *geometric origin* of the chain (the **16** arises as a Weyl spinor of the Observerse's normal bundle under observation, rather than being postulated). D-G has nothing to say about this geometric origin because it addresses representation theory, not fiber-bundle geometry.

**Assessment**: the relation between GU and D-G is not "evasion" — it is "non-intersection." GU never enters the class D-G constrains. The Pati-Salam chain verification confirms that GU's alternative group theory produces the correct SM quantum numbers where E₈ cannot.

---

## 6. The Forgetful-Image Framework

The four per-theorem analyses above share a common architectural pattern in their successful published evasions:

| Theorem | Added structure that works | Forgetful operation that loses it |
|---|---|---|
| Witten | boundary, orbifold, brane, flux, singularity | smoothing |
| Nielsen-Ninomiya | (d+1)-bulk, modified symmetry algebra | demand on-site exact symmetry |
| Freed-Hopkins | topological-order boundary, symmetry extension, mixed spatial | demand invertible boundary / standard symmetry type |
| Distler-Garibaldi | product group, bundle, Kac-Moody extension | demand single finite-dim E₈ adjoint |

The first three rows share an architectural shape: add bulk/boundary/enrichment, the forgetful operation discards it, the no-go theorem correctly reports that the discarded image has no chirality. The fourth row is structurally different: the "added structure" is a category change, not an enrichment.

### 6.1 Partial topological unification

The first three theorems increasingly read as anomaly statements:

- Nielsen-Ninomiya in its strong modern form is anomaly-theoretic (Lüscher; sigma-model anomaly arguments).
- Freed-Hopkins is the cohomological classification of anomalies directly.
- Witten 1981 is not framed in cobordism language, but most of its successful evasions are mediated by anomaly inflow.

Distler-Garibaldi resists this unification. Representation theory of single-E₈ is not naturally a cobordism statement.

### 6.2 The "what gets lost" pattern

Across the three class-relative theorems, what the forgetful operation discards is consistently the *mechanism* (where chirality enters: defect, boundary, bulk, enriched bordism) while preserving the *relation* (a smooth four-dimensional EFT-shaped object). Every prior successful evasion adds structure at the mechanism level.

Distler-Garibaldi is excluded from this framework because it is not a class-relative no-go theorem. It constrains a specific algebraic atom (E₈ representations), not a category of structures. See §5.4 for the full analysis. The forgetful-image framework covers three theorems cleanly, and the scope boundary is itself an informative structural fact: no-go theorems come in (at least) two logical types — class-relative and group-specific — and different analytical tools are appropriate for each.

---

## 7. Test Case: Geometric Unity's Pati-Salam Chain (Computational Verification)

The most falsifiable claim in the 2021 Geometric Unity draft is the structure group reduction chain that produces Standard Model quantum numbers from the geometry of the Observerse. This section reports a computational verification of that chain.

### 7.1 The claim

The paper (Sections 4.1, 11.2–11.3) asserts that choosing a metric on X⁴ (an "observation") breaks the structure group of the chimeric bundle as:

```
Spin(7,7)
  → Spin(1,3) × Spin(6,4)          [observation]
  → Spin(1,3) × Spin(6) × Spin(4)  [maximal compact of Spin(6,4)]
  ≅ SL(2,ℂ) × SU(4) × SU(2) × SU(2)  [accidental isomorphisms]
  → SL(2,ℂ) × SU(3) × SU(2) × U(1)   [Pati-Salam → SM]
```

The Weyl spinor of the normal bundle S/(ℝ^{6,4}) yields 16 complex internal states. The paper presents an explicit table assigning Standard Model quantum numbers to these 16 states.

### 7.2 Method

Two independent Python scripts were written:

1. **Weight-diagram branching**: constructs the Spin(10) chiral spinor **16** from its weight diagram (±½)⁵ with an even number of minus signs, embeds Pati-Salam by partitioning the rank-5 Cartan, and computes B−L, weak isospin, hypercharge, and electric charge from group theory alone.
2. **Explicit Clifford matrices**: constructs 32×32 gamma matrices for SO(10) via Jordan-Wigner tensor product, verifies the Clifford relations numerically, projects onto each chirality, and reads Cartan eigenvalues directly.

### 7.3 Results

**All assertions pass.** The dimensional checks, accidental isomorphisms, branching rules, and quantum number assignments match exactly. The 16 states collapse to:

| Multiplet (SU(3), SU(2)_L, n = 6Y) | Dim | SM identification |
|---|---|---|
| (3, 2, +1) | 6 | quark doublet Q |
| (3̄, 1, +2) | 3 | dᶜ |
| (3̄, 1, −4) | 3 | uᶜ |
| (1, 2, −3) | 2 | lepton doublet L |
| (1, 1, +6) | 1 | eᶜ |
| (1, 1, 0) | 1 | νᶜ |

Total: 16 states. Hypercharge trace Σ Y = 0 and charge trace Σ Q = 0 (anomaly-free generation). The independent cross-check confirms that one chirality reproduces the paper's table exactly, while the other is its exact CP conjugate.

An embedding-ambiguity probe confirmed that only the standard Pati-Salam → SM embedding Y = T_{3R} + (B−L)/2 reproduces the table; the naive alternative (B−L alone as hypercharge) fails.

### 7.4 Scope honesty

The verification establishes that the paper has correctly re-derived the well-known SO(10) ⊃ Pati-Salam ⊃ SM embedding of one fermion generation in the **16**-spinor. This embedding is standard and textbook. The paper's *novelty* claim is geometric — that the **16** arises as a normal-bundle Weyl spinor under "observation" of the Observerse — and that geometric origin is *not* tested here. What is tested and confirmed is that the group theory the paper hangs that claim on is arithmetically sound.

The verification also does *not* address: the effective-chirality claim (§3.5), the 2+1 imposter-generation proposal, or whether the construction produces the SM without also forcing larger non-compact groups.

---

## 8. The Six-Axis Specification Protocol

The forgetful-image framework organizes *which class a no-go theorem fixes*. A complementary tool is needed to organize *which class a proposed exit claims to occupy*. The six-axis specification protocol serves this role.

Every candidate substrate program must specify:

1. **L1 — Substrate**: the mathematical object on which the candidate invariant lives.
2. **L2 — Observer**: the observer or computational class extracting the shadow.
3. **L3 — Pairing**: the channel or coupling between substrate and observer.
4. **L4 — Causal order**: the causal-order model in force.
5. **L5 — Emergence**: whether the candidate is a specific object, universality class, fixed point, or attractor.
6. **L6 — Coordination loop**: the feedback or dynamics that makes observer extraction well-defined.

A proposal that leaves any axis blank or filled by aesthetic language is returned for sharpening — not rejected on substance.

### 8.1 GU's six-axis profile

Applying the protocol to the 2021 paper:

| Axis | GU's specification | Source | Precision |
|---|---|---|---|
| L1 (substrate) | Y¹⁴ = Met(X⁴), chimeric bundle C(Y) with metric of signature (4,6), main principal bundle P_H with H = U(64,64) | §3, Definition 3.1; §3.2; §3.6 | DEFINITION |
| L2 (observer) | choice of metric ג on X⁴, embedding X → Y via ג | §4 | DEFINITION |
| L3 (pairing) | pullback of Y-native fields to X via the observation map ι* | §4 | DEFINITION |
| L4 (causal order) | partially addressed: ℝ¹ is the unique dimension with a natural total order; temporal arrow reconstructed from Observerse structure | §12.2 | CLAIM |
| L5 (emergence) | effective chirality: non-chiral theory decouples into chiral sectors at low curvature | §11.4 | NARRATIVE |
| L6 (coordination loop) | not specified | — | GAP |

The strongest axes are L1–L3, which are stated at definition level. L5 is the weakest — the effective chirality claim is the paper's answer to the chirality question and it is the least rigorous part of the paper. L6 is absent.

### 8.2 Comparison with known evasions

Published Witten-evasions operate on L1 (substrate-class extensions: orbifold, boundary, singular, brane, flux). GW/overlap operates on L1 + L5 (modified substrate + modified symmetry realization). Freed-Hopkins enrichments operate on L2/L3/L4 (observer, pairing, causal order). GU's proposed construction is distinctive in operating primarily on L1 (a genuinely different substrate: the Observerse) with a secondary claim on L5 (effective chirality). This profile is most similar to the Hořava-Witten boundary construction (L1 change) but with a much more radical L1 replacement.

---

## 9. Cross-Theorem Assessment of GU

The four no-go families divide into two logical types, and GU's relation to each differs accordingly.

### 9.1 Class-relative theorems (forgetful-image framework applies)

| Theorem | GU's proposed exit | Exit type | Rigor of exit | Verified? |
|---|---|---|---|---|
| Witten | Observerse replaces smooth-KK setting | L1 (substrate) | HIGH — definition-level | Definition verified; physics not tested |
| Nielsen-Ninomiya | Effective chirality / decoupling | L5 (emergence) | LOW — narrative claim | Not verified; under-specified |
| Freed-Hopkins | Not addressed | — | — | Open gap |

The strongest class-relative exit is against Witten, where the Observerse construction operates on a genuinely different substrate (Y¹⁴ rather than smooth compact KK). The weakest is against Nielsen-Ninomiya, where the effective chirality claim needs substantial clarification before it can be formalized.

The signed-readout boundary theorem (§3.6) provides an independent, partial bridge for the Nielsen-Ninomiya family. It does not validate GU's specific mechanism, but it demonstrates that the structural picture — monotone provenance with signed readout as the source of apparent chirality — is mathematically coherent at the lattice level.

### 9.2 Group-specific impossibility (D-G)

| Theorem | GU's relation | Type | Status |
|---|---|---|---|
| Distler-Garibaldi | Non-intersection: GU uses Spin(7,7), not E₈ | Group-specific impossibility | Pati-Salam chain computationally verified (§7) |

GU does not "evade" Distler-Garibaldi — it never enters the class D-G constrains. Spin(7,7) and E₈ live in disjoint parts of the Lie classification (different rank, different dimension, no natural embedding). The Pati-Salam chain verification confirms that GU's group theory produces the correct SM quantum numbers where E₈ cannot. This is not a loophole or a stress case — it is a straightforward non-intersection that D-G itself makes no claim about.

### 9.3 Summary verdict

The forgetful-image framework handles all three class-relative no-go theorems naturally. D-G is correctly classified as a group-specific impossibility result outside the framework's scope. The earlier framing of D-G as a "stress case where the framework strains" was a category error: it applied a class-relative tool to a group-specific theorem. Recognizing this distinction strengthens rather than weakens the analysis — it sharpens the framework's scope and adds a new structural observation (no-go theorems come in different logical types).

---

## 10. Discussion

### 10.1 What the framework establishes

The forgetful-image reading of no-go theorems is not new — it is implicit in the evasion literature for each theorem family. What this survey adds is three things: (1) the explicit organization — naming the forgetful operations, cataloging what each one discards, and confirming that all three class-relative families admit a natural enrichment-then-projection structure; (2) the recognition that no-go theorems come in (at least) two logical types — class-relative (Witten, Nielsen-Ninomiya, Freed-Hopkins) and group-specific (Distler-Garibaldi) — and that the forgetful-image framework applies to the first type but not the second; (3) the observation that a candidate program's relation to a group-specific impossibility is better described as "non-intersection" than as "evasion" when the program never enters the constrained group.

The six-axis protocol adds a complementary constraint: any proposed class exit must fill out a typed specification before making chirality or anomaly claims. This keeps heterodox proposals testable rather than atmospheric.

### 10.2 What remains open

1. **Effective chirality formalization**: GU's answer to the chirality question (§3.5) is the most important open claim and the least rigorous. A precise decoupling theorem — with an energy scale, a controlled approximation, and a statement about what happens to the non-chiral remnant at high curvature — would be the single highest-value contribution to the GU program's interface with the no-go literature.

2. **Freed-Hopkins interface**: GU has no specification for L2/L3/L4 at the level Freed-Hopkins requires (tangential structure, bordism category). Filling this gap would either strengthen the program or reveal a genuine obstruction.

3. **The CALM ↔ Ginsparg-Wilson functor**: the signed-readout line's sharpest falsifier is whether the proposed correspondence between CRDT protocols and lattice-fermion algebras can be made functorial. If the direct CALM check on the Ginsparg-Wilson generator comes back negative, the protocol analogy drops from "theorem-shaped" to "structured metaphor."

4. **Integer-index obstruction permanence**: the signed-readout bridge fails at the integer topological-index readout under every framework tested. A permanence proof for this failure would be a clean negative theorem.

5. **Formalizing the class-relative / group-specific distinction**: the classification of D-G as group-specific (§5.4) rests on the structural observation that E₈ representation theory is atomically narrow. A sharper version would define necessary and sufficient conditions for "class-relative" vs. "group-specific" no-go theorems and survey the broader literature for other examples of each type.

### 10.3 Closing posture

The four no-go families divide into two logical types: three are class-relative (the forgetful-image framework applies cleanly) and one is group-specific (D-G constrains E₈, not a class of structures). This distinction resolves the earlier "stress case" framing — the framework was never the right tool for D-G, and recognizing this sharpens both the framework's scope and the D-G analysis. The GU program provides a concrete test case with one computationally verified group-theoretic claim, one under-specified chirality claim, and one open gap. The signed-readout boundary theorem provides an independent partial bridge for the lattice-fermion family. The six-axis protocol provides the specification discipline to keep all of this falsifiable.

The recommendation is to publish with the scope boundary (class-relative vs. group-specific) as a structural finding, and to use the ranked open questions above as the falsification surface.

---

## References

Acharya, B. S., Witten, E. (2001). Chiral fermions from manifolds of G₂ holonomy.

Anderson, L. B., et al. (2014–2015). Flux breaking in heterotic compactifications.

Bakircioglu, Arnault, Arrighi (2025). QCA flavoring and Nielsen-Ninomiya.

Berkowitz, Cherman, Jacobson (2024). 2d anomaly-free chiral gauge theory via bosonization.

Braun, V., He, Y.-H., Ovrut, B. A., Pantev, T. (2005–2006). Heterotic Standard Models.

Córdova, C., Ohmori, K., Shao, S.-H. (2019). Anomaly obstructions to symmetry-preserving gapped phases.

Debray, A. (2021). Crystalline and mixed-symmetry extensions.

Distler, J., Garibaldi, S. (2010). There is no "Theory of Everything" inside E₈.

Dobrescu, B. A., Pontón, E. (2004). Chiral compactification on a square.

Freed, D. S., Hopkins, M. J. (2021). Reflection positivity and invertible topological phases.

Georgi, Grant, Hailu (2000). Fat-brane chirality.

Grady, D. (2023). Proof of the Freed-Hopkins conjecture.

Hellerstein, J. M., Alvaro, P. (2020). Keeping CALM: When distributed consistency is easy.

Hořava, P., Witten, E. (1996). Heterotic and type I string dynamics.

Kaplan, D. B. (1992). A method for simulating chiral fermions on the lattice.

Kapustin, A., Sopenko, N. (2024). Anomaly index for locality-preserving spin-chain actions.

Lüscher, M. (1998). Exact chiral symmetry on the lattice.

Meissner, K. A., Nicolai, H. (2025). K(E₁₀) and the Standard Model.

Nesti, F., Percacci, R. (2009–2010). GraviGUT SO(3,11) unification.

Neuberger, H. (1997). Exactly massless quarks on the lattice.

Nielsen, H. B., Ninomiya, M. (1981). Absence of neutrinos on a lattice.

Randjbar-Daemi, S., Salam, A., Strathdee, J. (1983). Spontaneous compactification with flux.

Wang, J., Wen, X.-G., Witten, E. (2017). Symmetric gapped interfaces of SPT phases.

Weinstein, E. (2021). Geometric Unity (Draft, April 1, 2021). Unpublished manuscript.

Witten, E. (1981). Search for a realistic Kaluza-Klein theory.

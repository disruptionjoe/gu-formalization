---
title: "No-Go / Forgetful-Image Map"
status: canon
doc_type: canon
updated_at: "2026-05-31"
---

# No-Go / Forgetful-Image Map

**Status.** Public draft artifact.
**Source basis.** `literature/03-assumption-decomposition-no-go-evasion-literature.md`, `process/syntheses/00b-loophole-synthesis-witten-evasion-test.md`, `roadmap/potential-insights-novelty-and-tests-v1.md`, `roadmap/15-persona-pathway-ranking.md`. Cross-built against the six-axis protocol (internal origin artifact, `specifications/six-axis/six-axis-template.md`).
**Generated.** 2026-05-30

## 0. Honesty contract

This map is **not** a claim that the no-go theorems are wrong. Inside their stated classes they are correct theorems and the literature confirms them. The map's only claim is that each theorem fixes a **class** and therefore each theorem admits a question: *what richer substrate datum, if any, would survive a class-respecting reformulation, and what does the smooth-bundle shadow forget?* For three of the four families that question is already implicit/adjacent in the literature. For the fourth (Distler-Garibaldi) the framing is original-once-included and is treated explicitly below as the stress case.

The verdict is **not** "the no-goes are wrong." The verdict is **which** no-goes have plausible richer-data shadows and **which** resist the frame.

## 1. Acceptance summary

One-line per theorem. Full rows below.

| theorem | class fixed | strongest evasion class in literature | candidate richer datum | candidate forgetful operation | analogy strength | open stress |
| --- | --- | --- | --- | --- | --- | --- |
| Witten 1981 | smooth compact internal geometry, trivial gauge background | orbifolds, boundaries, branes, fluxes, singularities (Hořava-Witten, Acharya-Witten, Dobrescu-Pontón, Randjbar-Daemi-Salam-Strathdee) | singular / orbifold / brane-localized chirality data, or higher-categorical bundle | smoothing functor: `(singular X, brane/flux data) ↦ (smooth shadow X', trivial-bg)` | strong (well-documented class exits) | non-geometric exits (stochastic/observer/causal-set) are not in established literature |
| Nielsen-Ninomiya | local Hermitian translation-invariant lattice fermion w/ exact on-site U(1)_V and U(1)_A | domain walls, GW/overlap (modified symmetry realization), bosonized/Villain 2d, partial PEPS chirality | bulk+boundary anomaly-inflow object, or modified-chiral-symmetry algebra, or QCA flavoring | locality-and-on-site-symmetry functor: `(d+1)-bulk+defect anomaly object ↦ d-dim local on-site lattice` | strong for the modified-symmetry and bulk-evasion framing; 3+1d local chiral gauge regularization still open | distributed-systems / protocol-model evasion has no published bridge yet (cf. internal origin artifact / sibling #27) |
| Freed-Hopkins | reflection-positive invertible extended functorial QFT, fixed symmetry type, valid low-energy EFT | symmetry extension + topological-order boundary (Wang-Wen-Witten); allowing non-invertible boundary; mixed/crystalline symmetry (Debray) | enriched bordism category — e.g. observer-pairing, QRF, crystalline mixed-symmetry, average symmetry | underlying-bordism functor: enriched bordism category ↦ ordinary symmetry-type bordism input | medium — symmetry / boundary / spatial extensions are real and accepted; observer-pairing enrichment is not in the literature (open program) | Córdova-Ohmori-Shao obstruction + Kapustin-Sopenko persistence: anomaly often re-appears at a deeper level even after class change |
| Distler-Garibaldi | single real form of E8, low-spin (V_{m,n}=0 for m+n>4), SL(2,C) × G centralizer, V_{2,1} complex G-rep | E8 × E8 heterotic (Braun-He-Ovrut-Pantev; Anderson et al.), GraviGUT SO(3,11) (Nesti-Percacci), beyond-finite-dim K(E10) (Meissner-Nicolai) | richer infinite-dim / bundle-with-flux / product-group / Kac-Moody-quotient object | "single-finite-E8-adjoint" functor: richer compactification/Kac-Moody ↦ V_{m,n} adjoint of one real E8 | **outlier — stress case**: every successful "evasion" leaves the class entirely; no loophole inside single-E8 representation theory | smooth-bundle-shadow framing has the weakest analogical purchase here; this is where the unified frame is most original and most vulnerable |

## 2. Per-theorem map

### 2.1 Witten 1981 — chirality from smooth Kaluza-Klein reduction

**Statement, as used in the literature.** In smooth compactifications of higher-dimensional supergravity / M-theory with internal manifold X smooth and compact and trivial background gauge data, the 4d fermion spectrum is non-chiral. In the canonical late-1990s restatement: **"chiral fermions do not arise when the internal manifold X is smooth."**

**Assumptions (formal list).**

1. Internal manifold X is smooth, compact, closed (no boundary).
2. Reduction is Kaluza-Klein at the level of the action, with smooth Levi-Civita data.
3. No nontrivial gauge background / instanton on X.
4. No orbifold / singular loci / branes / topological defects.
5. The 4d fermion sector is read off as zero modes of the Dirac operator on X coupled only to gravity.

**Known evasions in published literature.**

- *Flux / instanton background:* Randjbar-Daemi-Salam-Strathdee 1983. Drops assumption (3).
- *Boundary:* Hořava-Witten 1996, 11d on a manifold-with-boundary; E8 on each boundary component. Drops (1).
- *Orbifold + brane-localization:* Georgi-Grant-Hailu 2000; fat-brane chirality. Drops (1)/(4).
- *Twisted boundary conditions:* Dobrescu-Pontón 2004, chiral compactification on a square. Drops (1)/(4).
- *Singular G2-holonomy:* Acharya-Witten 2001. Drops (1) directly; theorem statement made explicit ("only if X is singular").
- *Freund-Rubin with singularities:* Acharya-Denef-Hofman-Lambert 2003. Restates the theorem in the smooth/singular language used here.

Successful published evasions are uniformly **geometric** class exits. No published evasion uses stochastic, observer-relative, causal-set, or hypergraph language (see Witten evasion table in `roadmap/potential-insights-novelty-and-tests-v1.md`, I12).

**Candidate richer substrate datum.** A singular / orbifold / brane-stratified geometric object, or a higher-categorical bundle with anomaly-inflow data attached at singular strata. Specifically: a *stratified geometric substrate* `(X̃, S, B)` where `X̃` is a singular variety, `S ⊂ X̃` is the singular stratum, and `B` is gauge/flux/brane data on the stratification. The chirality content is carried by the data at `S` (zero modes localized on defects).

**Candidate forgetful operation.** The *smoothing functor*

```
ϕ_smooth : (X̃, S, B) ↦ (X', trivial-bg)
```

that resolves singularities, deletes boundary/brane data, and trivializes gauge background. The Witten 1981 class is the image of this functor. The theorem is the statement that on the image of `ϕ_smooth` the 4d Dirac index vanishes.

**What gets lost in the smooth-bundle shadow.** Net chirality data localized on `S`; anomaly-inflow contributions from boundary components; the topological class of the gauge background. The relation-side (a smooth 4d effective spacetime) survives; the mechanism (where chirality enters) does not.

**Analogy strength.** Strong. Every cited evasion fits this template by naming what `B` or `S` is. The forgetful-image frame is essentially the standard reading of the published evasion literature for Witten.

**Where the analogy may break.** A *non-geometric* substrate (stochastic, observer-relative, causal-set) is not yet shown to admit a smoothing functor producing exactly the Witten image. This is an open derivation problem; the formal opening exists (`process/syntheses/00b-loophole-synthesis-witten-evasion-test.md`) but the substantive derivation does not.

**Six-axis cross-ref.** Standard published Witten-evasions live on L1 (substrate-class extensions: orbifold, boundary, singular, brane, flux). They preserve L2-L6. Non-geometric proposals live on L4 (causal-order: causal-set), L2 (observer: QRF/hypercomputing), L3 (pairing: superdeterministic), or L5 (emergence: RG universality class). Those L2/L3/L4/L5 paths have no Witten-evasion literature yet, consistent with I12.

### 2.2 Nielsen-Ninomiya — lattice fermion doubling

**Statement.** A free bilinear lattice fermion action that is local, Hermitian, translation-invariant, and carries exact lattice U(1)_V and U(1)_A symmetries necessarily has an equal number of left- and right-handed fermion species. Stronger modern restatement: the obstruction is anomaly-theoretic and survives in any system where chiral symmetry is realized on-site with a discrete energy-momentum spectrum.

**Assumptions (formal list).**

1. Locality (finite-range hopping).
2. Hermiticity of the lattice Hamiltonian / Dirac operator.
3. Translation invariance of the lattice.
4. Exact lattice U(1)_V with conserved charge.
5. Exact lattice U(1)_A realized on-site.
6. Free / bilinear action (no interactions, in the original; the deeper version drops this).
7. Spectrum is continuous in lattice momentum and has discrete on-site charge structure.

**Known evasions in published literature.**

- *Domain wall:* Kaplan 1992. Drops (3) by going to d+1 with a defect; chirality lives on the defect.
- *Overlap / Ginsparg-Wilson:* Neuberger 1997; Lüscher 1998. Drops (5) in its naive on-site form; chirality is realized by a modified algebra. Lüscher: "no contradiction because the symmetry is realized in a different way than assumed in the theorem."
- *Chiral PEPS:* Wahl-Tu-Schuch-Cirac 2013. Partial success in 2d; locality+gap obstruction reappears.
- *2d anomaly-free chiral gauge with exact lattice symmetry:* Berkowitz-Cherman-Jacobson 2024 (Villain / bosonization).
- *Translation-noninvariant extensions are NOT an evasion:* Zenkin 1998 strengthens to translation-noninvariant via index theorem.
- *Non-Hermitian PT (Chernodub 2017):* drops (2) but with PT-breaking and complex spectra (proof-of-principle, not physical).
- *Staggered (Chatterjee-Pace-Shao 2024):* lattice noncommutativity matches the continuum anomaly *consistently with* the theorem, not against it.
- *QCA (Bakircioglu-Arnault-Arrighi 2025):* flavoring construction; explicitly coexists with the theorem.

**Candidate richer substrate datum.** A *(d+1)-dimensional bulk + d-dimensional boundary* anomaly-inflow object together with the symmetry-realization data on the boundary. Equivalently: an invertible / SPT bulk whose anomaly inflow accounts for the boundary chiral content. The chirality is a topological invariant of this pair, not of the d-dim lattice alone.

**Candidate forgetful operation.** The *on-site locality and exact on-site symmetry* functor

```
ϕ_local : (bulk + boundary + modified-symmetry algebra) ↦ d-dim local on-site lattice
```

that forgets the bulk and demands on-site realization of the full chiral symmetry. The Nielsen-Ninomiya class is the image of `ϕ_local`; the theorem is the statement that the image of this functor has zero net chirality.

**What gets lost in the smooth-bundle shadow.** The bulk SPT data; the modified Ginsparg-Wilson algebra structure on the boundary; the anomaly-inflow current between bulk and boundary. The relation-side (a d-dim lattice with chiral-looking fermions) can survive; the conserved on-site symmetry presentation cannot.

**Analogy strength.** Strong. The bulk+boundary inflow reading is the standard modern reading of why domain-wall and overlap work. Lüscher's own framing ("realized in a different way") is exactly the forgetful-image picture.

**Where the analogy may break.** The 3+1d local chiral-gauge regularization is still open; the bulk+boundary substrate has not yet produced a complete Standard Model regulator. The richer datum is real, but its application is not yet a finished construction.

**Six-axis cross-ref.** Standard evasions live on L1 (substrate: bulk+boundary; modified-algebra spectral triple) and on L2 in a weak sense (observer is still finite Turing, but reads the boundary not the bulk). The protocol/distributed-systems framing — recasting (1)-(5) as system-model assumptions (locality = communication radius, translation invariance = homogeneous node model, on-site symmetry = local consistency model) — is the Nielsen-protocol-analogy lane (sibling artifact #27, internal origin artifact). That lane lives on L3/L6 (pairing + coordination-loop) and is the one place the no-go-map suggests a genuinely original axis-drop.

**Cross-artifact finding for sibling #27.** Nielsen-Ninomiya's assumptions (1), (3), (4), (5), (7) read naturally as protocol-model assumptions in a distributed system. Sibling #27 should treat (3) as homogeneous-node-model, (5) as on-site / local consistency model with exact conserved charge, and (1) as bounded communication radius. The evasion literature already accepts that modifying (5) (Lüscher) is the cleanest exit; sibling #27's analogy should expect modified-consistency-model to be the protocol-side analog of GW/overlap.

### 2.3 Freed-Hopkins — invertible-extended-functorial anomaly classification

**Statement.** Deformation classes of reflection-positive, invertible, extended functorial field theories with fixed symmetry type are classified by a generalized cohomology / bordism group of a Thom spectrum. Applied to lattice phases, the classification controls invertible SPT phases under the assumption that a valid low-energy EFT exists.

This is **not** a no-go theorem in the Witten / Nielsen-Ninomiya style. It is a classification theorem. It functions as a no-go in two ways: (i) it tells you which anomalies can be canceled and which cannot, and (ii) the Wang-Wen-Witten / Córdova-Ohmori-Shao package tells you when an anomalous boundary cannot be made symmetric and gapped.

**Assumptions (formal list).**

1. Extended functorial field theory in the sense of Lurie-Freed-Hopkins.
2. Invertibility (the theory's partition function is a unit).
3. Reflection positivity.
4. Fixed symmetry type / tangential structure (the input data for the relevant bordism category).
5. Existence of a valid low-energy EFT approximation (when applied to lattice systems).
6. Boundary obstruction variant additionally assumes the boundary is to be invertible / trivially gapped (Wang-Wen-Witten extension).

**Known evasions / extensions in published literature.**

- *Boundary topological order:* Wang-Wen-Witten 2017. Drops (6); anomalous G-symmetry boundary becomes non-anomalous after lifting to extended H-symmetry on a topologically-ordered boundary.
- *Symmetry-extension obstruction:* Córdova-Ohmori-Shao 2019. Sharp limit: extension fails when an anomaly-inflow obstruction does not vanish; symmetry-preserving gapped phase is impossible, must go gapless or break.
- *Mixed spatial symmetry / crystalline:* Debray 2021. Extends (4) to mixed spatial-fermion-parity symmetries. Inside the same invertible-cobordism paradigm.
- *Grady 2023:* proves the Freed-Hopkins conjecture, confirming the bordism description is not merely heuristic.
- *Kapustin-Sopenko 2024:* anomaly index for locality-preserving spin-chain actions; anomalous → no invariant gapped ground state. Persistence: even when one leaves the band-fermion setting, the obstruction often persists.

**Candidate richer substrate datum.** An *enriched bordism category* whose objects carry richer data than (symmetry type, tangential structure). Two concrete proposals worth naming:

- (a) *Observer-pairing enriched bordism:* objects are bordisms equipped with observer worldlines / QRF data. (Genuinely original, see I7 / I8 / deep-research 02.)
- (b) *Average / crystalline / mixed-symmetry enriched bordism:* already adjacent (Debray; average-symmetry literature).

Both candidates posit a *forgetful functor* back to the standard input data.

**Candidate forgetful operation.** The *underlying-bordism* functor

```
ϕ_underlying : enriched bordism category (Bord^enriched) ↦ Bord^{symmetry-type}
```

that forgets the enrichment and returns the standard input the Freed-Hopkins-Grady computation runs on. The classification result then computes the anomaly group of `ϕ_underlying(Bord^enriched)`, which may be strictly coarser than the anomaly classification of the enriched category.

**What gets lost in the smooth-bundle shadow.** Observer-worldline / QRF data, average-symmetry information, or any structure not encoded in (symmetry type, tangential structure). If the enrichment is trivial under `ϕ_underlying`, the classification cannot see it.

**Analogy strength.** Medium. For the *adjacent* enrichments (crystalline, mixed, average) the analogy is essentially what the literature is already doing — they are documented extensions inside the same paradigm. For the *original* enrichment (observer/QRF pairing) the analogy is a research proposal, not an established result. Per `literature/02` and I7/I8: no published or arXiv-standard literature treats Freed-Hopkins in observer-relative / QRF / QBist / superdeterministic / IIT terms. This is a genuinely open extension proposal.

**Where the analogy may break.** Two specific places.

- Córdova-Ohmori-Shao shows that even when one drops invertibility for topological order, an anomaly-inflow obstruction persists and re-blocks symmetric-gapped phases. If observer-enrichment turns out to have a similar persistence theorem (the enriched anomaly maps surjectively onto the standard one), the smooth-bundle-shadow frame yields no new information.
- Kapustin-Sopenko shows that locality-preserving extensions of the substrate don't generally evade the obstruction. By analogy, observer-extensions might not, either.

**Six-axis cross-ref.** Freed-Hopkins enrichment lives primarily on L2 (observer class), L3 (pairing), and L4 (causal order — if enriched bordisms carry observer worldlines or QRF data). The Type II_1 example-01 candidate preserves L2/L3/L4 and absorbs all richer data into L1, which is one valid strategy: keep Freed-Hopkins untouched, move the richer substrate into the spectral triple.

**Cross-artifact finding for siblings #24 (six-axis protocol) and #26 (Type II_1 SM checklist).** The map's reading of Freed-Hopkins as a *classification* rather than a *no-go* sharpens what `Type II_1 spectral SM` (`example-01`) is doing: it preserves L2/L3/L4 precisely so that Freed-Hopkins acts on the standard input data and the new structure lives entirely in L1, where Freed-Hopkins has no purchase. Sibling #26's checklist should make this explicit: the Type II_1 candidate's bet is that the standard bordism classification cannot see L1 enrichment because the Connes-channel pairing forgets it.

### 2.4 Distler-Garibaldi — single-E8 representation-theoretic obstruction

**Statement.** There is no real Lie group E together with subgroups SL(2,C) and G such that:

- (ToE1) G is connected, compact, and centralizes SL(2,C);
- (ToE2) in the SL(2,C)×G decomposition of Lie(E), V_{m,n}=0 for m+n>4;
- (ToE3) V_{2,1} is a complex G-representation;

inside complex E8 or any real form of E8.

**Assumptions (formal list).**

1. Single real form of E8 as the symmetry group of a "theory of everything."
2. The 4d Lorentz / spin-statistics structure embeds as SL(2,C) ⊂ E.
3. Internal gauge structure embeds as a connected compact subgroup G centralizing SL(2,C).
4. Matter content lives in V_{m,n} with m+n ≤ 4 (excludes exotic higher-spin matter).
5. Chirality means V_{2,1} is complex as a G-representation.
6. The construction is finite-dimensional and at the level of representation theory of one E.
7. No bundle / compactification / flux data is added.

**Known evasions in published literature.** All successful evasions leave the class entirely.

- *E8 × E8 heterotic with Calabi-Yau:* Braun-He-Ovrut-Pantev 2005, 2006. Drops (1) by going to E8 × E8; drops (6) by adding bundle data on a CY threefold. Realistic three-generation SM.
- *Flux breaking visible E8 directly to SM:* Anderson et al. 2014/2015. Same class exit; drops (1) and (7).
- *GraviGUT SO(3,11):* Nesti-Percacci 2009/2010. Drops (1) entirely; single chiral SO(10) family from a Majorana-Weyl rep of the larger group. One family only.
- *K(E10) Kac-Moody quotient:* Meissner-Nicolai 2025. Drops (1) and (6) by going to an infinite-dimensional Kac-Moody object. Far from a finished theory.
- *Lisi-Smolin-Speziale 2010:* remains inside the obstructed class; counted as a "fails inside" rather than an evasion.

**Candidate richer substrate datum.** Three honest candidates, all of which leave the class:

- (a) *Product-group / bundle-with-flux object:* E8 × E8 with a holomorphic vector bundle on a Calabi-Yau. The "richer datum" is the bundle V → X with c_1(V) and structure-group data.
- (b) *Larger Lie group object:* SO(3,11), F4, E6, or similar; matter content from a representation of the larger group.
- (c) *Infinite-dimensional Kac-Moody / K(E10) object:* the richer datum is the Kac-Moody algebra and its maximal compact subgroup quotient.

There is **no known richer-substrate datum that lives inside single-E8 representation theory and reproduces three SM generations plus gravity**. This is the stress case.

**Candidate forgetful operation.** The *single-E8-adjoint* functor

```
ϕ_singleE8 : richer compactification/Kac-Moody data ↦ V_{m,n} decomposition of one real E8
```

that forgets bundle data, compactification data, or Kac-Moody extension and keeps only the SL(2,C) × G branching content of one E8 adjoint. Distler-Garibaldi is the statement that the image of this functor cannot satisfy (ToE1)-(ToE3) simultaneously.

**What gets lost in the smooth-bundle shadow.** Bundle data; product-group structure; Kac-Moody extension; compactification geometry. The single-E8-adjoint shadow keeps almost none of what the working evasions add. Unlike Witten / Nielsen-Ninomiya / Freed-Hopkins, where the richer datum sits "near" the no-go class (singular geometry, bulk+boundary, enriched bordism), the Distler-Garibaldi richer data is genuinely *outside* single-E8 representation theory.

**Analogy strength.** **Weak — this is the stress case.** The smooth-bundle-shadow frame fits the first three theorems naturally because their richer-datum candidates are nearby enrichments of the same structure. Distler-Garibaldi's richer-datum candidates are *category changes* (representation theory → bundle theory; finite-dim Lie → infinite-dim Kac-Moody; one group → product group), not enrichments. The forgetful operation in (a)-(c) is more like "collapse a category" than "compute a shadow."

**Where the analogy may break.** Distler-Garibaldi may simply be a theorem about the *wrong unit*: representation theory of a single finite-dim group is the wrong place to look for a unified theory regardless of substrate philosophy. If that diagnosis is correct, folding Distler-Garibaldi into the same forgetful-image framework as the other three is a category error, and the unified frame should explicitly carve out Distler-Garibaldi as "right theorem, wrong unit; class-exit is mandatory, no richer-datum-inside-class is possible."

**This is the falsification surface for the whole map.** Per I14: "If the framework handles Distler-Garibaldi, the synthesis is more than anomaly/topology rephrasing." The honest reading right now is that the framework *does not* handle Distler-Garibaldi in the same way it handles the other three. The map should be published with this admission visible, not papered over.

**Six-axis cross-ref.** Distler-Garibaldi has no clean axis-drop in the six-axis protocol: the theorem's class assumptions sit at a level (specific finite-dim group, specific representation type) below L1. The protocol's existing handling — make L1 a Type II_1 spectral triple or a different substrate object entirely — does sidestep Distler-Garibaldi (since the substrate is no longer "single finite-dim Lie group"), but it does so by changing the unit, not by computing a shadow. This is the honest reading.

## 3. Cross-theorem patterns

### 3.1 Common architectural move in successful evasions

Per `literature/03` and I11: in all four families, successful published evasions add **hidden bulk, boundary, singular, bundle, or higher-symmetry structure**. The smooth-bundle shadow loses exactly that added structure.

| theorem | added structure that works | shadow operation that loses it |
| --- | --- | --- |
| Witten | boundary, orbifold, brane, flux, singularity | smoothing |
| Nielsen-Ninomiya | (d+1)-bulk, modified symmetry algebra | demand on-site exact symmetry |
| Freed-Hopkins | topological-order boundary, symmetry extension, mixed spatial | demand invertible boundary / standard symmetry type |
| Distler-Garibaldi | product group, bundle, Kac-Moody extension | demand single finite-dim E8 adjoint |

The first three rows share an architectural shape: add bulk/boundary/enrichment, the shadow forgets it. Distler-Garibaldi's row is structurally different: the "added structure" is a category change.

### 3.2 Partial topological unification

The first three increasingly read as anomaly statements:

- Nielsen-Ninomiya in its strong modern form is anomaly-theoretic (Lüscher; sigma-model anomaly arguments).
- Freed-Hopkins is the cohomological classification of anomalies directly.
- Witten 1981 is not framed in cobordism language but most of its successful evasions are mediated by anomaly inflow (boundaries, branes, singularities).

Distler-Garibaldi resists this unification. Representation theory of single-E8 is not naturally a cobordism statement. This is consistent with the analogy-strength reading above.

### 3.3 The "what gets lost" pattern

Across the first three theorems, what the smooth-bundle shadow forgets is consistently:

- the *mechanism* (where chirality enters: defect, boundary, bulk, enriched bordism)
- while preserving the *relation* (a smooth 4d EFT-shaped object).

This matches the internal origin artifact family-frontier diagnosis (I3): every prior family failure was at the relation/mechanism boundary. The no-go-map is therefore *consistent with* the local execution history: the relation can be drawn, the mechanism is what gets forgotten.

Distler-Garibaldi instead forgets the entire *category*, not just the mechanism.

## 4. Ranked next tests the map makes obvious

Ordered by leverage on the map's open questions. Sibling-artifact references where applicable.

1. **Nielsen-protocol-analogy formal pilot (sibling #27, internal origin artifact).** Confirm the prediction that (5) — exact on-site chiral symmetry — is the protocol-side analog of GW/overlap, and that distributed-systems consistency-model relaxation is the cleanest evasion. Falsifiable: if the protocol-side analog of (5) cannot be relaxed without breaking another assumption, the analogy fails at the Lüscher-class point.
2. **Six-axis Type II_1 finite-control checklist (siblings #24, #26).** Verify the claim above that the Type II_1 candidate's Freed-Hopkins compatibility is exactly because the Connes-channel pairing forgets the L1 enrichment. Falsifiable: if the anomaly inflow of the Type II_1 extension produces a nontrivial obstruction that the finite Connes-Chamseddine model passes, the candidate dies.
3. **Observer-pairing-enriched bordism toy model (literature/02 program).** Write down one enriched bordism category that carries observer worldlines or QRF data, compute its anomaly group in a low-dimensional example, and check whether `ϕ_underlying` makes it agree with the standard Freed-Hopkins result. Falsifiable: if `ϕ_underlying` is essentially surjective on anomaly classes, the observer-enrichment is trivial and the analogy collapses (cf. Córdova-Ohmori-Shao persistence pattern).
4. **Distler-Garibaldi stress test.** Try to express a single E8 × E8 heterotic CY-bundle construction as a lossy functor `ϕ_singleE8` and ask explicitly whether the lost information has a *substrate-shadow* interpretation or just a *category-change* interpretation. Falsifiable: if no honest functor exists from bundle data to single-E8-adjoint data that captures the chirality content as a shadow, the unified frame should explicitly carve out Distler-Garibaldi as outside the synthesis.
5. **Witten non-geometric evasion search.** Per I12, no Witten evasion using observer/stochastic/causal-set language is published. Either find one and document it, or formalize that absence as a structural feature of the no-go-map (the smooth-bundle shadow really does only admit *geometric* class exits, not observer/computation class exits).

## 5. Closing posture

Three of four no-go families admit a forgetful-image reading that is at most an adjacent reformulation of the published evasion literature. The fourth (Distler-Garibaldi) is the stress case where the frame works least well: every successful evasion changes the category, not the shadow. The map's recommendation is to **publish with the stress case visible**, not buried, and to use the ranked tests above as the falsification surface.

The map does not say the no-go theorems are wrong. It says they fix classes, and for three of the four families the "what gets lost in the smooth-bundle shadow" question has plausible substrate-level answers that the literature is already approaching from the geometric side. The unified meta-frame ("forgetful images of richer substrate invariants") is implicit/adjacent for Witten / Nielsen-Ninomiya / Freed-Hopkins, and is **originally and contentiously** at stake for Distler-Garibaldi.

## Appendix A — Siblings referenced

- **internal origin artifact / six-axis specification protocol (sibling #24).** This map cites and is consistent with the six-axis protocol; each per-theorem map names the L1-L6 axis(es) the richer-data candidate occupies. The Type II_1 example (example-01) is treated as a worked illustration of "preserve L2-L4, push richer data into L1" for the Freed-Hopkins-compatibility argument.
- **Sibling #26 / Type II_1 spectral SM checklist .** This map's Freed-Hopkins section makes a specific architectural prediction for the Type II_1 candidate (that L1 enrichment is invisible to the standard bordism input via the Connes-channel pairing). Sibling #26 should record this as a checklist item, not just as a derivative reading.
- **Sibling #27 / Nielsen protocol-analogy pilot (internal origin artifact).** This map's Nielsen-Ninomiya section makes a specific prediction for the protocol-analogy: assumption (5) — exact on-site chiral symmetry — is the protocol-side analog of GW/overlap, and modified-consistency-model is the expected cleanest evasion.

All other siblings in the coordination list are independent of this map's content as of 2026-05-30 draft.

## Appendix B — Honest gaps in this map

- The map does not formally construct any of the candidate forgetful operations as functors between specified categories. They are named structurally; the construction is an open task.
- The Distler-Garibaldi handling is unresolved on substance, not just on framing. The honest verdict is that the unified frame strains here; the map ships this as a visible stress, not a solved problem.
- The "what gets lost" column for Distler-Garibaldi is genuinely speculative because the framework does not pick out a unique forgetful operation; (a), (b), (c) above are three different shadow-candidates with different lost-data content.
- The map cites the literature in `literature/03` but does not independently verify each citation. The map's correctness about the no-go theorems is downstream of that brief's correctness.

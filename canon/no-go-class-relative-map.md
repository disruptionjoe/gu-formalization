---
title: "No-Go / Forgetful-Image Map"
status: canon
doc_type: canon
updated_at: "2026-06-23"
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
| Witten 1981 | smooth compact internal geometry, trivial gauge background | orbifolds, boundaries, branes, fluxes, singularities (Hořava-Witten, Acharya-Witten, Dobrescu-Pontón, Randjbar-Daemi-Salam-Strathdee) | singular / orbifold / brane-localized chirality data, or higher-categorical bundle; **additionally (GU-specific, 2026-06-23): Met(X⁴) = Y¹⁴ non-compact fiber datum** — violates assumption (1) via non-compact fiber GL(4,ℝ)/O(3,1); the generation-count analytic mechanism is currently open after the scalar rank-one BC1 chain was superseded | smoothing functor = **Riemannian-reduction functor** `ϕ_Riemann ∘ ϕ_geom`: `ϕ_Riemann` sets distortion `θ = A − Γ` to zero, projecting out all Ehresmannian structure; image is smooth manifolds with Levi-Civita data (the Witten class) | strong (well-documented class exits); GU-specific Met(X) entry at reconstruction grade | non-geometric exits (stochastic/observer/causal-set) are not in established literature; GU generation count requires a corrected rank-3 or direct tau-twisted computation |
| Nielsen-Ninomiya | local Hermitian translation-invariant lattice fermion w/ exact on-site U(1)_V and U(1)_A | domain walls, GW/overlap (modified symmetry realization), bosonized/Villain 2d, partial PEPS chirality | bulk+boundary anomaly-inflow object, or modified-chiral-symmetry algebra, or QCA flavoring | locality-and-on-site-symmetry functor: `(d+1)-bulk+defect anomaly object ↦ d-dim local on-site lattice` | strong for the modified-symmetry and bulk-evasion framing; 3+1d local chiral gauge regularization still open | distributed-systems / protocol-model evasion has no published bridge yet (cf. internal origin artifact / sibling #27) |
| Freed-Hopkins | reflection-positive invertible extended functorial QFT, fixed symmetry type, valid low-energy EFT | symmetry extension + topological-order boundary (Wang-Wen-Witten); allowing non-invertible boundary; mixed/crystalline symmetry (Debray) | enriched bordism category — e.g. observer-pairing, QRF, crystalline mixed-symmetry, average symmetry | underlying-bordism functor: enriched bordism category ↦ ordinary symmetry-type bordism input | medium — symmetry / boundary / spatial extensions are real and accepted; observer-pairing enrichment is not in the literature (open program) | Córdova-Ohmori-Shao obstruction + Kapustin-Sopenko persistence: anomaly often re-appears at a deeper level even after class change |
| Distler-Garibaldi | single real form of E8, low-spin (V_{m,n}=0 for m+n>4), SL(2,C) × G centralizer, V_{2,1} complex G-rep | E8 × E8 heterotic (Braun-He-Ovrut-Pantev; Anderson et al.), GraviGUT SO(3,11) (Nesti-Percacci), beyond-finite-dim K(E10) (Meissner-Nicolai) | Sp(64) Clifford module over Y^{14} with chirality ind_H(D_GU): not a richer-datum-in-the-same-class but a different mathematical framework | "single-E8-adjoint" functor phi_singleE8 does not exist from GU's construction (GU is not in DG_E8) | **outlier — stress case RESOLVED as scope exit: GU violates DG-A1/A2/A6/A7, no residual obligation** | no residual; reopen only if F_DG: GU_data -> DG_E8 is constructed |
| Velo-Zwanziger 1969 | spin-3/2 matter minimally coupled to a nontrivial gauge group on flat or mildly curved background | supergravity Rarita-Schwinger gravitino (couples only to gravity via local SUSY, not to internal gauge group) | spin-3/2 field with trivial or absent coupling to internal gauge groups — coupling only to gravity | "minimal coupling" functor: `(spin-3/2 field with coupling data) ↦ (field with nontrivial gauge coupling forced)` | medium — supergravity shows spin-3/2 without VZ problems is possible; GU spin-3/2 coupling structure not yet specified | GU spin-3/2 evasion candidate (trivial internal coupling) is UNCONFIRMED; a physical (non-decoupled) spin-3/2 field with no internal gauge coupling and no SUSY guardian has no established literature analog |

**2026-06-23 correction.** The GU-specific Witten-row generation-count language that relied on the rank-one `BC1` discrete-series chain is now superseded. `explorations/rc1-discrete-series-verification-pack-2026-06-23.md` finds that the actual metric symmetric-pair analysis for `SL(4,R)/SO_0(3,1)` has split rank 3 and restricted root system `A3`, not rank-one `BC1` with `(m1,m2)=(7,1)`. Treat the Met(X) entry as a non-compact-fiber class exit whose generation count is currently unproven pending a corrected rank-3 computation.

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

**[Met(X) = Y¹⁴ non-compact fiber entry, 2026-06-23 — pc3-riemannian-ehresmannian-annotation]**

Additional GU-specific candidate: the metric bundle

```
(Y¹⁴, π, Met(X⁴), s : X⁴ → Y¹⁴, S = ℍ⁶⁴, D_GU)
```

where `Y¹⁴ = Met(X⁴)` is the bundle of Lorentzian metrics on a 4-manifold `X⁴` with fiber `GL(4,ℝ)/O(3,1)` (non-compact; homotopy type `ℝP³ × ℝ⁺`). This datum violates Witten's assumption (1) via **non-compact fiber** rather than via orbifold singularities or branes. The earlier rank-one scalar `BC1` discrete-series mechanism is superseded for the actual metric pair: the scalar split rank is `3`, the scalar restricted-root system is `A3`, and scalar FJ equal-rank fails. Any generation-count analytic mechanism for this Met(X) entry must now be a corrected rank-3 computation or a direct tau-twisted/vector-bundle admissibility computation; the rank-independent RS physical count may be cited separately but does not verify scalar Plancherel data. The forgetful operation that maps this substrate to the Witten class is `ϕ_Riemann : (Y¹⁴, A) ↦ (X⁴, Γ_{g_s})` — it collapses the metric bundle to its base, replaces the general Sp(64) connection by the Levi-Civita connection of the chosen section `g_s = s*(𝔾)`, and discards the non-compact fiber. Status: GU-specific, reconstruction grade.

**Candidate forgetful operation.** The *smoothing functor*

```
ϕ_smooth : (X̃, S, B) ↦ (X', trivial-bg)
```

that resolves singularities, deletes boundary/brane data, and trivializes gauge background. The Witten 1981 class is the image of this functor. The theorem is the statement that on the image of `ϕ_smooth` the 4d Dirac index vanishes.

**[Riemannian-Ehresmannian annotation, 2026-06-23 — pc3-riemannian-ehresmannian-annotation]**

`ϕ_smooth` decomposes as `ϕ_smooth = ϕ_Riemann ∘ ϕ_geom`, where `ϕ_Riemann` is the *Riemannian-reduction functor*:

```
ϕ_Riemann : (M, A) ↦ (M, Γ_M)
```

that replaces a general Ehresmann connection `A` by the unique Levi-Civita connection `Γ_M` compatible with the metric `g_M`. In GU language, `ϕ_Riemann` sets the distortion `θ = A − Γ` to zero, projecting out all Ehresmannian data and retaining only the Riemannian piece. The three irreducible SO(1,3) torsion pieces `T^{(1)}, T^{(2)}, T^{(3)}` encoded in `θ` — which source the three hidden curvature components `H^{(1)}, H^{(2)}, H^{(3)}` (established in `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md`) — are deleted by `ϕ_Riemann`. The mechanism by which Ehresmannian data could source chirality (e.g., via torsion-activated curvature on a non-compact fiber) is exactly what `ϕ_Riemann` forgets. Analogy: Einstein's Ricci contraction (Riemannian curvature of `Γ`) is to Yang-Mills curvature of `A` as the Riemannian class is to the Ehresmannian class; Witten fixes the Riemannian class.

**What gets lost in the smooth-bundle shadow.** Net chirality data localized on `S`; anomaly-inflow contributions from boundary components; the topological class of the gauge background; and (under the Riemannian-Ehresmannian framing) the Ehresmannian residual `θ = A − Γ` and the torsion-activated hidden curvature `H^{(1,2,3)}`. The relation-side (a smooth 4d effective spacetime) survives; the mechanism (where chirality enters) does not.

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

**Observer-pairing toy status (2026-06-23).** The first explicit observer-record enriched-bordism toy fails as a new anomaly construction (`explorations/freed-hopkins-observer-pairing-enriched-bordism-toy-2026-06-23.md`). If observer records are metadata, the underlying-bordism functor forgets them and the anomaly datum is unchanged. If observer data carries topological charge, the construction is ordinary defect/background enrichment inside the standard Freed-Hopkins paradigm, not observer-relative anomaly theory. Reopening this lane requires a specified observer datum that is neither forgettable metadata nor ordinary background/defect structure.

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

**Functor-audit status (2026-06-23).** The dedicated DG audit confirms this as a category-change stress case (`explorations/distler-garibaldi-functor-audit-2026-06-23.md`). The defensible collapse maps land in coarse branch data, 4D EFT data, or spectral-shadow data, not in the actual DG target category `DG_E8`; none preserve the chirality/generation invariant needed by the theorem. The map should therefore keep DG as a visible carve-out: class exit is mandatory, not a successful forgetful-image computation.

**[Precision carve-out, 2026-06-23 — distler-garibaldi-precision-carveout]**

**Formal verdict: EVASION BY SCOPE EXIT.** GU violates DG assumptions DG-A1 (gauge group is Sp(64), not E8), DG-A2 (Lorentz group does not embed inside the gauge group), DG-A6 (chirality is ind_H(D_GU) from the Clifford module operator index, not V_{2,1} complexity), and DG-A7 (GU is geometric bundle data on the non-compact Y^{14} = Met(X^4)). GU is not an object of the category DG_E8 that the theorem addresses. The theorem is inapplicable, not contradicted or circumvented within its domain.

The condition GU satisfies instead of DG-A6 is:

> **GU-Chir:** ind_H(D_GU) = 24 via the Atiyah-Singer theorem on (Y^{14}, Sp(64), S=H^{64}) with K3-type X^4 (A-hat=2), decomposing as 16 H-lines (spin-1/2, two generations) + 8 H-lines (RS sector, one generation). Generation count = ind_H(D_GU) / 8 = 3.

GU-Chir replaces DG's Lie-algebraic chirality test with an operator-analytic index theorem. No functor from GU's construction to DG_E8 is known that preserves ind_H(D_GU), because DG_E8 forbids bundle/compactification data (DG-A7) and the generation invariant depends on X^4 topology and Clifford module structure, not E8 adjoint branching. The DG carve-out from the functor audit (see Functor-audit status entry above) is therefore promoted from a structural observation to a precision theorem: GU's class exit from DG is at the level of the category of objects, not a clever condition-by-condition evasion. Reopen only if a functor F_DG: GU_data -> DG_E8 is exhibited that lands in the correct category and preserves ind_H(D_GU).

### 2.5 Velo-Zwanziger 1969 — spin-3/2 matter in nontrivial gauge backgrounds

**Statement, as used in the literature.** Massless (or massive) spin-3/2 fields minimally coupled to a nontrivial external gauge field develop acausal propagation (superluminal modes), tachyonic instabilities, or loss of the required number of degrees of freedom — the Cauchy problem becomes ill-posed. The original papers are Velo and Zwanziger (1969), Phys. Rev. 186:1337, and Johnson and Sudarshan (1961), Ann. Phys. 13:126 (precursor). The problem arises because the subsidiary conditions that enforce the correct spin-3/2 DOF count (the Rarita-Schwinger constraint γ^μ Ψ_μ = 0 in the flat-space case) become inconsistent in a nontrivial gauge background.

**Physical content.** In flat space with no coupling:
- Massive spin-3/2: 4 × 4 - 4 = 12 components of Ψ_μ, constrained by subsidiary conditions to 2(2s+1) = 8 physical DOF. Propagation is causal.
- Massless spin-3/2 (as a gauge field): 2 physical DOF (like a gravitino in supergravity). Local gauge invariance maintains the subsidiary conditions.

When a nontrivial gauge connection is switched on (minimal coupling ∂_μ → D_μ = ∂_μ + A_μ), the subsidiary conditions γ^μ D_μ Ψ_ν = 0 and the equations of motion become inconsistent (the Dirac operator and the constraint no longer commute with the propagator). In the original language: the "characteristic matrix" of the hyperbolic system has zero determinant for some spacelike normal, producing superluminal characteristics.

**Assumptions (formal list).**

1. The field Ψ_μ is a spin-3/2 field (Rarita-Schwinger field, a spinor-vector).
2. Coupling is minimal: ∂_μ → D_μ = ∂_μ + A_μ, where A_μ takes values in a nontrivial Lie algebra representation of the gauge group G.
3. The gauge group G is nontrivial: the representation of G acting on Ψ_μ is a non-singlet.
4. The background is flat or mildly curved (the original theorem; the gravitational case is more complex).
5. No local symmetry principle (gauge symmetry or local SUSY) maintains the subsidiary conditions against loop corrections.

**Degrees of freedom analysis.**

| case | physical DOF | Velo-Zwanziger |
|---|---:|---|
| Massive spin-3/2, free | 8 | no problem |
| Massless spin-3/2 as gauge field (gravitino) | 2 | no problem — local SUSY maintains constraints |
| Massive spin-3/2, nontrivial gauge coupling | ill-posed | VZ obstruction; DOF count inconsistent |
| Massless spin-3/2, nontrivial gauge coupling | ill-posed | VZ obstruction |
| Massive spin-3/2, coupling only to gravity | open | depends on background; see literature |

**Known evasions in published literature.**

- *Supergravity / Rarita-Schwinger gravitino (de Wit-Freedman 1979; Deser-Zumino 1976):* The gravitino in N=1 supergravity is a gauge field for local supersymmetry. Its subsidiary conditions are maintained by the SUSY algebra (not by a Lagrange multiplier). The gravitino couples to the stress tensor (to gravity), not to internal gauge groups. This evades assumption (3): the gravitino's coupling to gravity is not the type of "nontrivial gauge coupling" VZ applies to, because the gravitational coupling is via the vierbein and spin connection, not via a Lie-algebra-valued gauge potential for an internal symmetry group G. The gravitino is not in a non-singlet of any internal G.

- *Extended supergravity with matter (Cremmer-Julia 1979; de Wit-Nicolai 1982):* In N≥2 extended supergravity, the gravitini couple to the gauge group but are still protected by local SUSY. The subsidiary conditions are maintained by the larger SUSY algebra. The protection does not extend to spin-3/2 fields that are not gravitini.

- *Coupling to Abelian gauge group only (Kobayashi-Shamaly 1978):* A spin-3/2 field coupled to a U(1) gauge group (electromagnetism) avoids some VZ pathologies in specific limits. This is a partial evasion and requires additional conditions.

- *No known evasion for spin-3/2 in non-Abelian internal gauge background without SUSY.* The VZ obstruction is robust for spin-3/2 matter in non-Abelian gauge backgrounds when no local symmetry principle (SUSY, higher-spin gauge symmetry) protects the subsidiary conditions.

**GU evasion candidate: Dirac-DeRham non-decoupling at 14D.**

GU predicts one family of 16 flipped-chiral spin-3/2 particles arising from the Dirac-DeRham-Einstein complex on Y¹⁴ (see `explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md`, Claim 7). These are not gravitini (GU has no local SUSY structure as far as can be determined from the published record). Weinstein's statement ([00:41:48–00:42:09]): "if your model differs by having no internal symmetry groups, I have no idea whether it has any kind of a Velo Zwanziger problem."

**VZ1 full analysis: `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md` (2026-06-22).**

**Finding 1 — "Trivial internal coupling" fails at the 4D level.** The RS(3,1) ⊗ S(6,4) sector carries non-trivial SM gauge quantum numbers: under SU(3)×SU(2)_L×U(1)_Y, it decomposes as (Q̄_L, L̄_L, ū_R, d̄_R, ē_R, ν̄_R)_{flipped} — one full Pati-Salam generation. VZ hypothesis (H3) is satisfied after 4D reduction. The "trivial coupling" claim cannot be maintained for the 4D effective theory.

**Finding 2 — The coherent evasion mechanism lives at the 14D level.** GU's spin-3/2 sector is NOT a standalone Rarita-Schwinger field with its own Lagrangian. It is the RS(3,1) component of the full spinor S = H^{64} on Y¹⁴, propagated by the Dirac-DeRham operator D_GU. The Dirac operator D_GU has the light cone as its characteristic cone (Berline-Getzler-Vergne §2.1: the principal symbol of a Dirac operator is hyperbolic with characteristic cone = metric light cone, regardless of gauge coupling). VZ applies to standalone RS Lagrangians; if the RS sector does not decouple into an independent dynamical variable at the 14D level, VZ's hypotheses are not satisfied at 14D.

**GU evasion status: EVADED (reconstruction) at 14D; VERIFIED at 4D principal-symbol level (2026-06-23).**

**Summary of 2026-06-23 computation chain (vz-schur + OQ1 + OQ2 + OQ3-V1/V2/V3):**

At 14D: the Schur complement symbol `D_RS_eff(xi) = S_R^{14D}(xi)` has `ker = 0` for all 14D covectors with `g_Y(xi,xi) != 0`, including mixed horizontal+normal covectors. Proof: Clifford module identity `sigma_D(xi)^2 = xi2 Id_E` forces `ker S_R = 0` via the block-inversion argument (§8 of `explorations/vz-schur-complement-2026-06-23.md`). VZ at 14D: EVADED (reconstruction grade -- 14D E-block explicit form is structural, not CAS-verified).

At 4D: all three open verification conditions (OQ3-V1/V2/V3) are RESOLVED (§18). OQ3-V1: the principal symbol `s*(sigma_{D_GU})(eta)` has no anomalous normal-direction terms -- exact horizontal Clifford computation gives `c_s(eta)^2 = g_s(eta,eta) Id_S`. OQ3-V2: the 4D E-block `[[0, 1/4],[1, 3/2]]` has determinant `-1/4 != 0` (explicit computation); overall invertibility from Clifford identity. OQ3-V3: `R_s = ker Gamma^{4D}` exactly -- section pullback on H*/N* split is exact, normal RS components are KK scalars not spin-3/2 fields. 4D VZ evasion: characteristic cone of `D_RS_eff^{4D}` = null cone of `g_s`; no spacelike characteristics. VERIFIED at 4D principal-symbol level.

**Remaining open conditions (not VZ obstruction, dynamical residuals):**

**F5.** Lower-order curvature terms at 4D: Sp(64) gauge curvature `F_A` and 4D Riemann tensor `R_{g_s}` are zero-order terms in `D_GU^{4D}`. Cannot modify the principal symbol (CONDITIONALLY_RESOLVED by vz-oq2, vz-subprincipal). The constrained-Hamiltonian propagation of the subsidiary condition `Gamma^{4D} psi = 0` in an Sp(64) background: residual open at full dynamical level.

**~~F6~~ CONDITIONALLY_RESOLVED (vz-schur §19, 2026-06-23).** 4D EFT decoupling: the KK zero mode sub-bundle `E_s^{(0)}` inherits the full Clifford module property from `D_GU^{4D}` because the horizontal Clifford element `c_s(eta) = eta_a gamma^a_H` commutes with the KK mode projector `P_{(0)}`. The §8 kernel argument (`ker S_R = 0` for non-null covectors) applies verbatim to the EFT. The B/C coupling blocks are O(1) algebraic functions of eta in the zero-mode sector (not KK-suppressed). Even in the deep IR limit where `B E^{-1} C` is small, the RS-RS diagonal block A(eta) is itself causal (`A S_R = xi2 Id_R` from block identity (II)-(III)). The gamma-trace constraint is intrinsic to the Clifford module structure (not an external subsidiary condition), so the VZ constraint-propagation mechanism cannot fire. Remaining open: KK zero mode existence (requires discrete-series spectrum); loop corrections to B/C blocks. The 4D EFT RS characteristic cone argument survives the KK mass-gap condition.

**OQ2 (guardian symmetry for decoupled RS).** F6 is now CONDITIONALLY_RESOLVED (RS does not decouple into a standalone field at the kinematic level). OQ2 is therefore contingent-RESOLVED: the guardian symmetry question is moot at the EFT principal-symbol level. A guardian would only be needed if loop corrections to the B/C blocks drove them to zero in the IR -- a named open gap but not an established failure mode.

**OQ (gravitational VZ from gimmel metric).** The Weyl tensor of the gimmel metric on `Y^{14}` could in principle produce curvature-induced VZ acausality (Buchdahl 1962, Aurilia-Umezawa 1969) independent of gauge coupling. The zero-order argument from vz-oq2 shows this cannot modify the principal symbol; the sub-leading level requires the Hamiltonian analysis of F5.

**Failure conditions remain:** VZ becomes a genuine obstruction at 4D if (F5-full) lower-order curvature generates new characteristics in the constrained-Hamiltonian analysis, OR (F6-loop) large IR loop corrections drive B/C coupling blocks to zero and simultaneously a guardian symmetry is absent. Neither of these is established.

**Candidate richer datum.**

A spin-3/2 field together with a **guardian symmetry specification** — either local SUSY, a higher-spin gauge algebra, or a specific coupling structure that maintains the subsidiary conditions without SUSY. The candidate richer datum is the pair (Ψ_μ, G_guardian) where G_guardian is the guardian symmetry that maintains subsidiary conditions.

**Candidate forgetful operation.**

The *minimal coupling* functor:

```
ϕ_mc : (spin-3/2 field, coupling data, guardian symmetry) ↦ (spin-3/2 field, nontrivial gauge coupling, no guardian)
```

that forgets the guardian symmetry and enforces minimal coupling to a nontrivial gauge group. Velo-Zwanziger is the statement that the image of this functor is ill-posed. The known evasion (supergravity) exits the class by naming a specific guardian (local SUSY) that is not forgotten.

**What gets lost in the smooth-bundle shadow.** The guardian symmetry specification. The relation (a physical spin-3/2 particle in the spectrum) can survive; the guardian that protects its causal propagation cannot.

**Analogy strength.** Medium. The supergravity example shows that a physical spin-3/2 field without VZ problems is possible — so the class-exit is real. The evasion mechanism (local SUSY as guardian) is well-understood. The open question is whether a different guardian principle (not SUSY) can protect a spin-3/2 field that is a singlet under the internal gauge group but couples to gravity. This has limited published precedent.

**Where the analogy may break.** Two specific places:

- *No guardian, no protection.* If GU's spin-3/2 particles have no guardian symmetry (no local SUSY, no higher-spin gauge invariance), then the claim that trivial internal coupling evades VZ may be insufficient. The gravitational coupling alone may produce VZ pathologies in curved backgrounds, and without a guardian these are not prevented.

- *DOF count in Y¹⁴ geometry.* The VZ theorem applies to spin-3/2 on X⁴. GU's spin-3/2 particles arise on Y¹⁴ and are pulled back to X⁴. The DOF count in the pullback (how many physical DOF survive) depends on the structure of the Dirac-DeRham-Einstein complex (Claim 7 / N2 / SC1 tasks). If the pullback does not give a standard Rarita-Schwinger field on X⁴, VZ may not apply as stated — but a different (potentially worse) consistency problem may apply instead.

**Action required to confirm or refute.**

1. *Specify the GU spin-3/2 Lagrangian* (or at minimum the kinetic term and coupling structure for the flipped-chiral spin-3/2 family). This is downstream of N2 (shiab operator) and the Dirac-DeRham-Einstein complex specification.

2. *Check VZ conditions for the pulled-back field.* Given the Lagrangian, apply the Velo-Zwanziger characteristic analysis: compute the characteristic matrix of the field equations for the pulled-back spin-3/2 field on X⁴. Check whether the determinant of the characteristic matrix vanishes for spacelike normals.

3. *Identify a guardian symmetry or prove absence.* Either (a) show that GU's proposed super-IG extension (Claim F in the analysis document) maintains the subsidiary conditions for the spin-3/2 field in the relevant background, or (b) show that no guardian symmetry is available and derive the consequences for causal propagation.

**Six-axis cross-ref.** Velo-Zwanziger is primarily an L1 (substrate) constraint: it restricts what spin content a theory can have without specifying a guardian. It also touches L3 (pairing): the coupling between the spin-3/2 field and the gauge group is a pairing structure, and trivializing this coupling is the evasion candidate. An L3 enrichment (a guardian symmetry that enters as a coupling between field and background) is what the supergravity evasion provides.

**Source.** Primary source: Weinstein UCSD April 2025 transcript [00:41:48–00:42:29], analyzed in `explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md`, Claim 8 / New Object C / Section 4.3. Original theorem: Velo and Zwanziger (1969), Phys. Rev. 186:1337; Johnson and Sudarshan (1961), Ann. Phys. 13:126. Task identifier: VZ1 in `NEXT-STEPS.md`.

---

## 3. Cross-theorem patterns

### 3.1 Common architectural move in successful evasions

Per `literature/03` and I11: in all four families, successful published evasions add **hidden bulk, boundary, singular, bundle, or higher-symmetry structure**. The smooth-bundle shadow loses exactly that added structure.

| theorem | added structure that works | shadow operation that loses it |
| --- | --- | --- |
| Witten | boundary, orbifold, brane, flux, singularity; GU-specific: non-compact fiber Met(X⁴) + discrete-series harmonic analysis + Ehresmannian distortion θ | Riemannian-reduction functor ϕ_Riemann (sets θ = 0, collapses fiber to base, retains Levi-Civita only) |
| Nielsen-Ninomiya | (d+1)-bulk, modified symmetry algebra | demand on-site exact symmetry |
| Freed-Hopkins | topological-order boundary, symmetry extension, mixed spatial | demand invertible boundary / standard symmetry type |
| Distler-Garibaldi | product group, bundle, Kac-Moody extension | demand single finite-dim E8 adjoint |
| Velo-Zwanziger | Dirac-DeRham non-decoupling of RS sector (no standalone RS Lagrangian at 14D); or guardian symmetry (super-IG) if RS decouples | minimal-coupling functor that forgets the Dirac-DeRham embedding and treats RS as an independent matter field |

The first three rows share an architectural shape: add bulk/boundary/enrichment, the shadow forgets it. Distler-Garibaldi's row is structurally different: the "added structure" is a category change.

### 3.2 Partial topological unification

The first three increasingly read as anomaly statements:

- Nielsen-Ninomiya in its strong modern form is anomaly-theoretic (Lüscher; sigma-model anomaly arguments).
- Freed-Hopkins is the cohomological classification of anomalies directly.
- Witten 1981 is not framed in cobordism language but most of its successful evasions are mediated by anomaly inflow (boundaries, branes, singularities).

Distler-Garibaldi resists this unification. Representation theory of single-E8 is not naturally a cobordism statement. This is consistent with the analogy-strength reading above.

Velo-Zwanziger also resists the anomaly unification: it is a classical field theory consistency constraint (Cauchy problem well-posedness), not an anomaly statement. Its evasion is via a guardian symmetry principle (local SUSY), which is algebraic rather than topological. VZ is orthogonal to the cobordism / anomaly theme and should be read as a separate family: a **kinematic consistency** constraint rather than a topological obstruction.

### 3.3 The "what gets lost" pattern

Across the first three theorems, what the smooth-bundle shadow forgets is consistently:

- the *mechanism* (where chirality enters: defect, boundary, bulk, enriched bordism)
- while preserving the *relation* (a smooth 4d EFT-shaped object).

This matches the internal origin artifact family-frontier diagnosis (I3): every prior family failure was at the relation/mechanism boundary. The no-go-map is therefore *consistent with* the local execution history: the relation can be drawn, the mechanism is what gets forgotten.

Distler-Garibaldi instead forgets the entire *category*, not just the mechanism.

## 4. Ranked next tests the map makes obvious

Ordered by leverage on the map's open questions. Sibling-artifact references where applicable.

1. **Nielsen-protocol-analogy formal pilot (sibling #27, internal origin artifact).** Confirm the prediction that (5) — exact on-site chiral symmetry — is the protocol-side analog of GW/overlap, and that distributed-systems consistency-model relaxation is the cleanest evasion. Falsifiable: if the protocol-side analog of (5) cannot be relaxed without breaking another assumption, the analogy fails at the Lüscher-class point.
2. **Six-axis Type II_1 finite-control checklist (siblings #24, #26).** 2026-06-23 specialist pass completed. KO-6 signs are not an immediate no-go at the formal sign-package level, but no finite-control selector was constructed; principal graphs fail as full SM representation data and remain only conditionally useful for generation count. Next falsification: produce the actual finite-control selector or demote the lane to a generation-count-only analogy.
3. **Observer-pairing-enriched bordism toy model (literature/02 program).** 2026-06-23 first toy completed and failed as a new anomaly construction. Falsifiable reopening condition: specify an observer datum that neither descends away under `ϕ_underlying` nor reduces to ordinary defect/background structure.
4. **Distler-Garibaldi stress test.** 2026-06-23 audit completed. The test supports the carve-out: DG is category-change, not a genuine forgetful-image case. Reopen only if an honest functor lands in the DG target category while preserving the chirality/generation invariant.
5. **Witten non-geometric evasion search.** Per I12, no Witten evasion using observer/stochastic/causal-set language is published. Either find one and document it, or formalize that absence as a structural feature of the no-go-map (the smooth-bundle shadow really does only admit *geometric* class exits, not observer/computation class exits).

## 5. Closing posture

Three of five no-go families admit a forgetful-image reading that is at most an adjacent reformulation of the published evasion literature. The fourth (Distler-Garibaldi) is the stress case where the frame works least well: every successful evasion changes the category, not the shadow. The fifth (Velo-Zwanziger) is GU-specific: it constrains GU's own spin-3/2 matter prediction directly. Full analysis completed 2026-06-22 in `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md`. The evasion mechanism has been refined: "trivial internal coupling" fails at the 4D level (the RS sector carries SM charges); the coherent evasion candidate is that the RS sector is not a standalone dynamical variable at the 14D level (Dirac-DeRham non-decoupling). Status: OPEN — evasion mechanism identified but not verified. Three open questions (OQ1–OQ3) with explicit failure and confirmation conditions. The map's recommendation is to **publish with both the stress case and the OPEN VZ evasion visible**, not buried, and to use the ranked tests above as the falsification surface. OQ1 (RS decoupling question) is the priority sub-task.

The map does not say the no-go theorems are wrong. It says they fix classes, and for three of the five families the "what gets lost in the smooth-bundle shadow" question has plausible substrate-level answers that the literature is already approaching from the geometric side. The unified meta-frame ("forgetful images of richer substrate invariants") is implicit/adjacent for Witten / Nielsen-Ninomiya / Freed-Hopkins, is **originally and contentiously** at stake for Distler-Garibaldi, and is **GU-prediction-specific and currently open** for Velo-Zwanziger.

## Appendix A — Siblings referenced

- **internal origin artifact / six-axis specification protocol (sibling #24).** This map cites and is consistent with the six-axis protocol; each per-theorem map names the L1-L6 axis(es) the richer-data candidate occupies. The Type II_1 example (example-01) is treated as a worked illustration of "preserve L2-L4, push richer data into L1" for the Freed-Hopkins-compatibility argument.
- **Sibling #26 / Type II_1 spectral SM checklist .** This map's Freed-Hopkins section makes a specific architectural prediction for the Type II_1 candidate (that L1 enrichment is invisible to the standard bordism input via the Connes-channel pairing). Sibling #26 should record this as a checklist item, not just as a derivative reading.
- **Sibling #27 / Nielsen protocol-analogy pilot (internal origin artifact).** This map's Nielsen-Ninomiya section makes a specific prediction for the protocol-analogy: assumption (5) — exact on-site chiral symmetry — is the protocol-side analog of GW/overlap, and modified-consistency-model is the expected cleanest evasion.

All other siblings in the coordination list are independent of this map's content as of 2026-05-30 draft.

## Appendix B — Honest gaps in this map

- The map does not formally construct any of the candidate forgetful operations as functors between specified categories. They are named structurally; the construction is an open task.
- The Distler-Garibaldi handling is unresolved on substance, not just on framing. The honest verdict is that the unified frame strains here; the map ships this as a visible stress, not a solved problem.
- The "what gets lost" column for Distler-Garibaldi is genuinely speculative because the framework does not pick out a unique forgetful operation; (a), (b), (c) above are three different shadow-candidates with different lost-data content.
- The Velo-Zwanziger entry is GU-specific. Full analysis completed 2026-06-22: `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md`. Status updated from UNCONFIRMED to OPEN with the refined evasion mechanism (Dirac-DeRham non-decoupling rather than trivial internal coupling). Remaining open questions: (OQ1) whether the RS sector decouples from spin-1/2 in D_GU — this is the priority; (OQ2) what guardian symmetry protects a decoupled RS field (super-IG candidate, speculation-grade); (OQ3) gravitational VZ problems via Weyl tensor of gimmel metric on Y¹⁴. The "trivial internal coupling" claim was found to be false at the 4D level (RS sector carries SM charges).
- The map cites the literature in `literature/03` but does not independently verify each citation. The map's correctness about the no-go theorems is downstream of that brief's correctness.

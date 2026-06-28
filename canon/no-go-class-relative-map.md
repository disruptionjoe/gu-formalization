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

### 0.1 Scope of the spacetime base X⁴ (standing note, 2026-06-23 — CANON-5)

> **W2-FC1 — RESOLVED (2026-06-26; follows CORRECTION W2-01).** W2-01 corrected `canon/w2-y14-spin-structure.md` to **w2(Y14) = pi*w2(X⁴), i.e. Y14 spin iff X⁴ spin**. Re-derivation outcome (adversarially verified): **(1)** the Witten class-exit (§2.1) is via the *non-compact fiber* `GL(4,ℝ)/O(3,1)`, which is spin-independent, so it SURVIVES unchanged. **(2)** Y14 is spin-c for every orientable X⁴ (`W3(Y14)=π*W3(X⁴)=0`), but spin-c does NOT rescue GU: the GU chirality invariant is the quaternionic H-linear index `ind_H(D_GU)` on `S=ℍ⁶⁴`, and a U(1) spin-c twist `S⊗_ℂ L^{1/2}` breaks H-linearity (so `ind_H` and the `/8` generation arithmetic become undefined) and shifts the index off `Â(K3)=2`; on non-spin CP2 there is no genuine spin Dirac index at all (`Â(CP2)=−1/8∉ℤ`). **So X⁴ spin is a genuine standing PRECONDITION, not a free structure choice** (a quaternionic-compatible Spin^h enhancement is the only structure that could relax it; not in the current formalization — OPEN, **W2-FC2**). **(3)** The "no-import-K3" posture SURVIVES with corrected justification: K3 is not forced because the construction holds for any **spin** X⁴ (a broad class), and K3 enters only via `Â(K3)=2`, a spin invariant. The Met(X⁴) genericity narrows from "any orientable X⁴ (instancing CP2)" to **"any spin X⁴"**; CP2 is retired as an example. **(4)** Consistent everywhere — the K3-conditional entries already use K3 (spin), so requiring X⁴ spin tightens rather than breaks them. The "spin for any orientable X⁴ / CP2" citations below are corrected accordingly. Full entry: DERIVATION-PROGRESS.md W2-FC1.

**X⁴ = K3 is NOT a global standing assumption of this map.** This map's entries operate at two distinct scopes for the spacetime base X⁴, and the distinction is load-bearing for every verdict that touches a generation count:

- **Generic-X⁴ entries (no K3 specialization).** The Witten Met(X⁴) entry (§2.1) treats X⁴ as a *generic* oriented 4-manifold — fiber `GL(4,ℝ)/O(3,1)`, homotopy type `ℝP³ × ℝ⁺` — and asserts nothing topology-specific. The spin-structure result it relies on (`canon/w2-y14-spin-structure.md`, corrected by W2-01) is **w2(Y14)=π*w2(X⁴), i.e. Y14 spin iff X⁴ spin**; the entry therefore treats X⁴ as a generic **spin** 4-manifold (CP2 is excluded — it is non-spin, so Y14 over CP2 is non-spin and carries no quaternionic Dirac index; see the §0.1 W2-FC1 note). These entries do **not** assume K3 (many spin 4-manifolds exist) and must not be read as if they did.
- **K3-conditional entries (working hypothesis, not canon).** Two entries silently import `X⁴ ∈ K3` as a *working hypothesis* in order to evaluate a candidate generation count: the Freed-Hopkins Option-B closure (§2.3) uses `X_obs^sol = M_RF(K3)` and the Hitchin-Thorpe/Ricci-flat K3 selection; the Distler-Garibaldi GU-Chir block (§2.4) uses `Â(K3) = 2` to get the spin-1/2 leg `16 = 2 · 8` and the candidate count `24 / 8 = 3`. **Wherever those entries depend on K3, the dependence is now tagged explicitly as "conditional on X⁴ in the K3 topological class," and the verdicts that rest on it (FH lane-narrowed; DG generation count) inherit that hypothesis.**

Why K3 is a working hypothesis and not promoted to a global assumption: K3 is not forced — the construction holds for any **spin** X⁴ (a broad class: K3, T⁴, …), per W2-FC1, so K3 need not be singled out (CP2 is excluded as non-spin). Declaring `X⁴ = K3` globally would still contradict `CANON.md`, which lists the three-generation count as an open analytic-index problem on the non-compact `Y14 = Met(X⁴)` with no base fixed. The K3 specialization is therefore a *local* working hypothesis of the two generation-count-bearing entries only, never a base fixed for the whole map. **No entry may depend on K3 while the Witten/w2 entries assume genericity without this cross-reference.** Closing the K3 dependence into a genuine result requires either (a) deriving that the GU solution locus forces `X⁴ ∈ K3` from first principles (currently absent), or (b) recomputing the FH and DG generation-count claims base-independently.

## 1. Acceptance summary

One-line per theorem. Full rows below.

| theorem | class fixed | strongest evasion class in literature | candidate richer datum | candidate forgetful operation | analogy strength | open stress |
| --- | --- | --- | --- | --- | --- | --- |
| Witten 1981 | smooth compact internal geometry, trivial gauge background | orbifolds, boundaries, branes, fluxes, singularities (Hořava-Witten, Acharya-Witten, Dobrescu-Pontón, Randjbar-Daemi-Salam-Strathdee) | singular / orbifold / brane-localized chirality data, or higher-categorical bundle; **additionally (GU-specific, 2026-06-23): Met(X⁴) = Y¹⁴ non-compact fiber datum** — violates assumption (1) via non-compact fiber GL(4,ℝ)/O(3,1); the generation-count analytic mechanism via the non-compact fiber is now CLOSED as FAILED (scalar rank-one BC1 chain superseded; rank-3 Atiyah-Schmid empty; tau-twisted FAILS AS STATED; BC1 Jacobi route GENUINE_OBSTRUCTION 2026-06-23). the 3-generation count is OPEN — the "compact APS/K3" formula ind_H = 8·Â(K3) + 8 = 24 is a **compact-toy-model heuristic**, not an operative theorem: Atiyah-Singer is the COMPACT index theorem and does not apply on the non-compact Y¹⁴, and the formula silently assumes a non-compact→compact-K3 reduction that is itself OPEN; the actual non-compact framework is APS/L²/Fredholm (gates OQ-RK1/OQ-RK2 OPEN, FC4 OPEN) | smoothing functor = **Riemannian-reduction functor** `ϕ_Riemann ∘ ϕ_geom`: `ϕ_Riemann` sets distortion `θ = A − Γ` to zero, projecting out all Ehresmannian structure; image is smooth manifolds with Levi-Civita data (the Witten class) | strong (well-documented class exits); GU-specific Met(X) entry at reconstruction grade | non-geometric exits (stochastic/observer/causal-set) are not in established literature; GU generation count: OPEN — all non-compact analytic routes FAILED and the compact APS/K3 route is a toy-model heuristic (Atiyah-Singer is the compact theorem; non-compact→compact-K3 reduction unproved; APS/L²/Fredholm is the applicable framework; gates OQ-RK1/OQ-RK2 OPEN, FC4 OPEN) |
| Nielsen-Ninomiya | local Hermitian translation-invariant lattice fermion w/ exact on-site U(1)_V and U(1)_A | domain walls, GW/overlap (modified symmetry realization), bosonized/Villain 2d, partial PEPS chirality | bulk+boundary anomaly-inflow object, or modified-chiral-symmetry algebra, or QCA flavoring | locality-and-on-site-symmetry functor: `(d+1)-bulk+defect anomaly object ↦ d-dim local on-site lattice` | strong for the modified-symmetry and bulk-evasion framing; 3+1d local chiral gauge regularization still open | distributed-systems / protocol-model evasion has no published bridge yet (cf. internal origin artifact / sibling #27) |
| Freed-Hopkins | reflection-positive invertible extended functorial QFT, fixed symmetry type, valid low-energy EFT | symmetry extension + topological-order boundary (Wang-Wen-Witten); allowing non-invertible boundary; mixed/crystalline symmetry (Debray) | enriched bordism category — e.g. observer-pairing, QRF, crystalline mixed-symmetry, average symmetry | underlying-bordism functor: enriched bordism category ↦ ordinary symmetry-type bordism input | medium — symmetry / boundary / spatial extensions are real and accepted; **observer-pairing enrichment CONDITIONALLY_RESOLVED / lane-narrowed (reconstruction grade), NOT a closed GENUINE_OBSTRUCTION (2026-06-23 correction FH-01): the closure reading rests on a same-session, all-conditional dependency chain whose root is still OPEN; do not carry as a top-strength closed verdict (see §2.3 and CORRECTION FH-01 in DERIVATION-PROGRESS.md)** | Córdova-Ohmori-Shao obstruction + Kapustin-Sopenko persistence: anomaly often re-appears after class change. Closure is blocked on three live conditions, none independently closed: (RC1) the OPEN root `freed-hopkins-nonforgettable-observer` (verdict OPEN); (IC4 F3) the IC4 reduction to source-free Einstein is only CONDITIONALLY_SUPPORTED — open F3 vacuum/trace gate (nonzero trace-free GU source unresolved); (RC4) the KSp⁰=KO⁴ lift is proved for finite-CW / compact-Hausdorff bases, NOT the non-Hausdorff arithmetic-orbifold base actually used |
| Distler-Garibaldi | single real form of E8, low-spin (V_{m,n}=0 for m+n>4), SL(2,C) × G centralizer, V_{2,1} complex G-rep | E8 × E8 heterotic (Braun-He-Ovrut-Pantev; Anderson et al.), GraviGUT SO(3,11) (Nesti-Percacci), beyond-finite-dim K(E10) (Meissner-Nicolai) | Sp(64) Clifford module over Y^{14} with chirality ind_H(D_GU): not a richer-datum-in-the-same-class but a different mathematical framework | "single-E8-adjoint" functor phi_singleE8 does not exist from GU's construction (GU is not in DG_E8) | **outlier — stress case RESOLVED as scope exit: GU violates DG-A1/A2/A6/A7, no residual obligation. Scope-exit only; the numerical generation count ind_H(D_GU)=24 / 3 generations is a SEPARATE OPEN problem (§2.4 GU-Chir; agrees with w2 + shiab) and the scope-exit verdict does NOT depend on it** | no residual on the scope-exit claim; reopen only if F_DG: GU_data -> DG_E8 is constructed. (Generation-count number stays OPEN regardless — not part of this verdict) |
| Velo-Zwanziger 1969 | spin-3/2 matter minimally coupled to a nontrivial gauge group on flat or mildly curved background | supergravity Rarita-Schwinger gravitino (couples only to gravity via local SUSY, not to internal gauge group) | RS sub-bundle permanently coupled to spin-1/2 sector via off-diagonal Clifford blocks B and C in D_GU — RS is not a sub-Clifford-module of E, so it cannot propagate as a standalone field | "minimal coupling" functor: `(spin-3/2 field, Clifford module embedding, B/C coupling data) ↦ (standalone RS field with nontrivial gauge coupling forced)` — forgets the Dirac-DeRham non-decoupling | medium — supergravity shows spin-3/2 without VZ problems is possible via guardian; GU evasion is via Clifford non-decoupling (different mechanism, no guardian required at principal-symbol level) | **CONDITIONALLY_RESOLVED** (4D principal-symbol, reconstruction; subprincipal order open per FC-VZ-4) — also CONDITIONALLY_EVADED at 14D (horizontal + mixed covectors, reconstruction grade, gated on E-block invertibility FC-VZ-1). Remaining open: subprincipal/extrinsic-curvature characteristics (FC-VZ-4); constrained-Hamiltonian propagation of subsidiary conditions at full dynamical level (F5 — CONDITIONALLY_RESOLVED only, load-bearing on FC1 plus the still-open FC3/OQ-H1 energy estimate; the gamma-trace constraint does leave the RS sub-bundle at the field-equation level and the §4.8 propagation theorem closing that leak is an admitted proof sketch with the decisive energy estimate not done; **⚠ same-session, pending inter-session check (F5-SS-01): open state and closure both 2026-06-23 on an untracked same-session file, the kinematic-vs-dynamical FC1 claim self-referential and open — the full-dynamical gate is NOT settled**); loop corrections to B/C blocks (F6/OQ-RS-2). |

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

where `Y¹⁴ = Met(X⁴)` is the bundle of Lorentzian metrics on a 4-manifold `X⁴` with fiber `GL(4,ℝ)/O(3,1)` (non-compact; homotopy type `ℝP³ × ℝ⁺`). This datum violates Witten's assumption (1) via **non-compact fiber** rather than via orbifold singularities or branes. The earlier rank-one scalar `BC1` discrete-series mechanism is superseded for the actual metric pair: the scalar split rank is `3`, the scalar restricted-root system is `A3`, and scalar FJ equal-rank fails. Any generation-count analytic mechanism for this Met(X) entry must now be a corrected rank-3 computation or a direct tau-twisted/vector-bundle admissibility computation; the rank-independent RS physical count may be cited separately but does not verify scalar Plancherel data. The forgetful operation that maps this substrate to the Witten class is `ϕ_Riemann : (Y¹⁴, A) ↦ (X⁴, Γ_{g_s})` — it collapses the metric bundle to its base, replaces the general Sp(64) connection by the Levi-Civita connection of the chosen section `g_s = s*(𝔾)`, and discards the non-compact fiber. Status: GU-specific, reconstruction grade. **Scope (CANON-5, §0.1): this entry treats X⁴ as a GENERIC oriented 4-manifold and assumes nothing topology-specific; it does NOT specialize to K3. This is deliberately divergent from the Freed-Hopkins Option-B closure (§2.3) and the DG GU-Chir generation-count block (§2.4), which are conditional on X⁴ ∈ K3. Per W2-FC1, this entry treats X⁴ as a generic **spin** 4-manifold: X⁴ spin is a standing precondition for D_gimmel's quaternionic index `ind_H` (Y14 is spin-c for any orientable X⁴, but the U(1) spin-c twist breaks H-linearity and shifts the index off Â(K3)=2, so spin-c does not suffice; CP2 is excluded). Consistent with corrected `canon/w2-y14-spin-structure.md`. Do not silently import K3 into this entry.**

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

**Cross-artifact finding for GU paper §12.9 (effective chirality).** GU paper §12.9 proposes that the Dirac operator on Y is globally non-chiral, with apparent chirality emerging in low-curvature regions through coupling to scalar curvature R(y). This is structurally distinct from all four standard Nielsen-Ninomiya evasion routes: it does not add a bulk (domain-wall), modify the symmetry algebra (GW/overlap), or change the lattice geometry. Instead it places chirality on L5 (emergence class: chirality is a low-energy effective property, not a substrate property). The relevant question for the no-go map is whether GU's scalar-curvature mechanism constitutes a modification of assumption (5) in an effective sense (chirality is realized in a region-dependent, not on-site-exact, way) or whether the globally non-chiral Dirac operator simply has zero net chirality in the Nielsen-Ninomiya sense and GU's "effective" claim is a physical interpretation layered on top. This distinction is unresolved and is the sharpest formalization challenge for GU's chirality program. Tracked in `paper-formalization-candidates.md` claim 6C; reference surfaces in `sources/gu-paper-reference-surfaces.md`.

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

**Observer-pairing Option-B lane CONDITIONALLY_RESOLVED / lane-narrowed (2026-06-23) — NOT a closed GENUINE_OBSTRUCTION; see CORRECTION FH-01.** The structural no-go (`explorations/freed-hopkins-nonforgettable-observer-2026-06-23.md`) left exactly one escape: Option B, a noncontractible observer-state space X_obs whose KSp^0 index class is non-extendable beyond ordinary background. The optionb file (`explorations/freed-hopkins-optionb-ksp-family-2026-06-23.md`) eliminated two of three candidates: Met(X^4) is contractible (convex cone); Omega^2 B Sp(64) (gauge-connection moduli) is noncontractible but relabels as Sp(64) gauge background. The sole survivor X_obs^sol was analyzed in `explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md`: via the IC4 metric-selection result (GU section field equation → source-free Einstein → Ricci-flat by Hitchin-Thorpe on K3), X_obs^sol IS the moduli M_RF(K3) of Ricci-flat/hyperkahler metrics on K3 = Γ\O(3,19)/(O(3)×O(19)), Γ = O(3,19;Z), a dim-57 aspherical K(Γ,1). **[Scope tag, CANON-5: this identification is CONDITIONAL ON X⁴ ∈ K3 topological class. The Hitchin-Thorpe/Ricci-flat selection that names the moduli as M_RF(K3) presupposes the K3 base; it is a working hypothesis local to this entry, NOT a global map assumption (§0.1). The Witten Met(X⁴) entry (§2.1) and `canon/w2-y14-spin-structure.md` treat X⁴ as generic-orientable and explicitly admit X⁴ = CP2, so this entry's K3 specialization is not shared by them. The lane-narrowed verdict below inherits the K3 hypothesis.]** It is **noncontractible** (FC1 settled negative) but its noncontractibility is argued to be exactly that of the K3 Einstein-metric **gravitational background** moduli, so its KSp^0 = KO^4 class **relabels** via the gravitational/tangential-structure background-extension functor (FC2 fires). The reading is that all three GU-derivable observer-state spaces would then be eliminated — contractible (Met), gauge-relabel (Ω²BSp), gravitational-relabel (X_obs^sol) — and the no-go lemma's two escape doors (noncontractible + non-extendable) never open together.

**Why this is held at CONDITIONALLY_RESOLVED and NOT promoted to a closed GENUINE_OBSTRUCTION (2026-06-23 correction FH-01).** The GENUINE_OBSTRUCTION reading above rests on a dependency chain in which every load-bearing link was authored in this same session and none is VERIFIED, and the root of the chain is still OPEN. A top-strength "closed" verdict cannot rest on a same-session, all-conditional, partly-OPEN substrate — that is the same-session-circularity pattern this map's own workflow auditor flags ("be especially suspicious of files promoted today"). The explicit conditional chain, with three independent open conditions any one of which reopens the lane:

- **(RC1) OPEN root.** `explorations/freed-hopkins-nonforgettable-observer-2026-06-23.md` carries verdict **OPEN**. The Option-B no-go lemma whose "two escape doors never open together" is the whole argument is itself the open file; the chain is built on an unclosed foundation.
- **(IC4 F3) vacuum/trace gate.** The X_obs^sol = M_RF(K3) identification depends on the IC4 metric-selection result (`explorations/ic4-ricci-flat-k3-selection-2026-06-23.md`), whose verdict is only **CONDITIONALLY_SUPPORTED**, with an explicit open failure condition **F3 (OQ-FH-Bsol-3): nonzero trace-free GU source.** If the GU trace equation forces a nonzero effective `Λ_eff`, the K3 vacuum/source-free-Einstein gate is obstructed and X_obs^sol is not the Ricci-flat K3 moduli. F3 is unresolved.
- **(RC4) KO⁴-over-orbifold lift.** The KSp⁰ = KO⁴ relabeling uses `explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`, whose Atiyah-Jänich identification `[X, Fred_H(H_H)] = KSp⁰(X) = KO⁴(X)` is proved **for compact Hausdorff / finite-CW X only**. The base actually used (the arithmetic-orbifold moduli Γ\O(3,19)/(O(3)×O(19)) with Γ = O(3,19;Z)) is a **non-Hausdorff arithmetic orbifold**, not a finite CW complex; the identification is asserted, not proved, over that base. This is RC4.

Additionally, the two files carrying the GENUINE_OBSTRUCTION verdict and its CONDITIONALLY_RESOLVED support (`freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` and `freed-hopkins-optionb-ksp-family-2026-06-23.md`) are **untracked** in git — created this session and not yet reviewed in a later pass. **Disposition:** the lane is correctly **narrowed** (Met and Ω²BSp candidates are eliminated; X_obs^sol is the sole surviving candidate and is plausibly a background-moduli relabel), but the verdict carried into this canon map is **CONDITIONALLY_RESOLVED / lane-narrowed at reconstruction grade**, not a closed GENUINE_OBSTRUCTION. **This lane-narrowing is additionally CONDITIONAL ON X⁴ ∈ K3 topological class (CANON-5, §0.1): the surviving candidate X_obs^sol = M_RF(K3) is the Ricci-flat K3 metric-moduli, an identification that holds only on the K3 base; the generic-X⁴ Witten/w2 entries do not share this hypothesis. K3 here is a working hypothesis, not a global map assumption.** Promotion to a closed GENUINE_OBSTRUCTION requires, in a later session and on independently-reviewed (tracked) files: closing the OPEN root (RC1), closing the IC4 F3 vacuum/trace gate, and proving the KO⁴ lift over the actual non-Hausdorff arithmetic-orbifold base (RC4).

The source file (`explorations/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` §10) carries a GENUINE_OBSTRUCTION verdict with an explicit hedge. At canon level that verdict is **not promoted as a closed GENUINE_OBSTRUCTION**: it rests on a same-session, all-conditional, partly-OPEN dependency chain (root `freed-hopkins-nonforgettable-observer` is OPEN; IC4 is only CONDITIONALLY_SUPPORTED with open F3; the KO⁴ lift is unproved over the actual non-Hausdorff arithmetic base; the carrying files are untracked). The canon-level disposition is therefore **CONDITIONALLY_RESOLVED / lane-narrowed at reconstruction grade**, with the conditionality kept load-bearing and visible. The lane REOPENS — equivalently, the obstruction does NOT close — under any of four named conditions (`freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` §8):

- **RC1 (independent quaternionic observer structure).** An Sp(64)- or H-structure on the GU observer Hilbert space whose moduli is noncontractible and whose KSp^0 class is NOT pulled back from either the gauge-connection moduli (Ω²B Sp) or the Einstein-metric moduli (M_RF(K3)). Absent from the current GU formalization.
- **RC2 (IC4 reduction fails).** If the GU section field equation does NOT reduce to the source-free Einstein equation on K3 — e.g. a surviving trace-free GU source makes the solution locus an Einstein-with-matter moduli with different topology that is NOT a pure gravitational background — the gravitational-relabeling identification breaks and X_obs^sol must be re-analyzed. IC4 is only CONDITIONALLY_SUPPORTED, so this is the primary reopening risk.
- **RC3 (GU solution locus is a non-generic sublocus of M_RF(K3)).** If the GU solution sections are a proper subvariety of M_RF(K3) carrying a KO⁴ class that does not extend to the ambient Einstein-background moduli, the pullback/relabeling argument needs the extra class checked separately.
- **RC4 (KO⁴ lift fails over the arithmetic orbifold base).** The KSp^0(X) = KO^4(X) identification is stated for finite CW complexes; M_RF(K3) = Γ\D is a **non-Hausdorff arithmetic orbifold** (root-hyperplane degenerations). If the lift fails over this base, the family may not even define a well-defined KO⁴ class, "the class relabels" is the wrong frame, and the analysis must move to equivariant/orbifold KSp^0 with the relabeling conclusion re-derived.

Per §0 (Honesty contract) and Appendix B, this entry ships visible stress, not a solved problem: the RC1/RC2/RC4 conditionality is load-bearing and is kept visible at canon level rather than dropped on promotion. A closed GENUINE_OBSTRUCTION is earned only when, in a later session and on independently-reviewed (tracked) files, the OPEN observer root is closed, the IC4 F3 vacuum/trace gate is closed, and the KO⁴ lift is proved over the actual non-Hausdorff arithmetic-orbifold base.

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

**Formal verdict: EVASION BY SCOPE EXIT.** GU violates DG assumptions DG-A1 (gauge group is Sp(64), not E8), DG-A2 (Lorentz group does not embed inside the gauge group), DG-A6 (chirality is ind_H(D_GU) from the Clifford module operator index, not V_{2,1} complexity), DG-A7 (GU is geometric bundle data on the non-compact Y^{14} = Met(X^4)), and DG-A3 (the indefinite-Krein / drop-Hilbert-positivity route used for the matter sector requires a non-compact internal G -- SO(5,5), not compact SO(10) -- by the Weyl unitarian trick, so it negates the compact-centralizer assumption rather than enriching inside the class; A0 audit 2026-06-28, see canon/swing-ghost-parity-no-chiral-selection.md). GU is not an object of the category DG_E8 that the theorem addresses. The theorem is inapplicable, not contradicted or circumvented within its domain.

The condition GU satisfies instead of DG-A6 is:

> **GU-Chir (the chirality *test* GU uses — NOT a proven generation count):** GU replaces DG's Lie-algebraic chirality criterion (V_{2,1} complex as a G-rep) with an operator-analytic one: chirality is the quaternionic index ind_H(D_GU) of the Clifford-module Dirac operator on Y^{14}. **This is a statement about *which invariant* carries chirality in GU, not a computed value of that invariant.** The candidate generation count ind_H(D_GU) = 24 = 16 (spin-1/2) + 8 (RS — *CONDITIONALLY_RESOLVED-pending-rank_H: the RS leg ind_H(D_RS) = 8 rests entirely on rank_H(S_RS^+) = 4, which is uncomputed / curve-fit with an undismissed alternative; primary remaining gate is OQ-RK1 [first-principles RS rank], with OQ-RK2 [APS boundary conditions on K3] also open — see the RS-leg bullet below*), giving a candidate generation count = 24 / 8 = 3 **that is therefore only as settled as its weakest leg**, is **OPEN — reconstruction-grade target only, not established**, and is held at exactly the same status as in the two resolved canon files it must agree with: `canon/w2-y14-spin-structure.md` (§"What This Does Not Establish": "The analytic index ind_H(D_gimmel) = 24 ... is a separate computation requiring Fredholm theory on non-compact Y14"; generation count "open") and `canon/shiab-existence-cl95.md` (§"Known Failure Modes": "Shiab existence does not establish the generation count. That requires an index theorem on a non-compact Y^14 — a separate open problem"). CANON.md lists "Three-generation count (analytic index ind_H(D_gimmel) on non-compact Y14)" under **Not Yet Canon**. **Do NOT cite "ind_H(D_GU) = 24" or "3 generations" as an established value or a theorem anywhere; it is the open target of an unfinished index computation.**
>
> **Status of the two legs (asymmetric — read before quoting any number):**
> - *Spin-1/2 leg (16 H-lines) — compact-K3-MODEL expectation, NOT a theorem on Y¹⁴; CONDITIONAL ON X⁴ ∈ K3 (CANON-5, §0.1) AND on the non-compact→compact reduction (CANON-2).* 16 = Â(K3) · rank_H(S(6,4)) = 2 · 8 is what the spin-1/2 index *would* be **IF** the non-compact-Y¹⁴ problem reduced to an Atiyah-Singer computation on a compact K3 factor (Â(K3) = 2 a compact-K3 topological invariant; rank_H(S(6,4)) = 8 genuine, from Cl(9,5) = M(64,ℍ) module theory). **It is NOT "a genuine Atiyah-Singer computation" on Y¹⁴: Atiyah-Singer is the COMPACT index theorem and does not apply to D_GU on the non-compact open Y¹⁴ = Met(X⁴).** This leg is therefore a **compact-toy-model heuristic** that presupposes the non-compact → compact-K3 reduction, itself OPEN (the topology/index gate; GC-FC4 below; `explorations/discrete-series-fiber-dirac-index-2026-06-23.md` finds the finite homogeneous-fiber kernel statement on `GL(4,ℝ)/O(3,1)` incoherent). The framework that actually applies on the non-compact base is an APS / L²-index / Fredholm (Atiyah-Jänich–KSp) analysis — open proof obligation: a continuous H-linear Fredholm family for the actual GU operators (`explorations/signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md`) — matching `canon/w2-y14-spin-structure.md` ("Standard compact index theorems do not apply … requires a separate Fredholm/APS-type analysis") and `canon/shiab-existence-cl95.md` ("an index theorem on a non-compact Y^14 — a separate open problem"). The rank_H(S(6,4)) = 8 module fact survives; only its packaging into a finite Â-genus index requires the unestablished compactification. **The value Â(K3) = 2 — and hence the spin-1/2 leg = 16 and the candidate count 24 / 8 = 3 — is specific to the K3 topological class and changes for a different base (e.g. Â(CP2) ≠ 2). This is a working hypothesis local to this block, NOT a global map assumption: the Witten Met(X⁴) entry (§2.1) and corrected `canon/w2-y14-spin-structure.md` treat X⁴ as generic-**spin** (W2-FC1); CP2 is excluded (non-spin, Â(CP2)=−1/8 is non-integral — no genuine spin Dirac index). The candidate generation count therefore inherits the K3 hypothesis on top of its already-OPEN status, and X⁴ spin is a standing precondition (spin-c does not carry the quaternionic ind_H). Closing it requires either deriving X⁴ ∈ K3 from the GU solution locus (currently absent) or a base-independent recomputation.**
> - *RS leg (8 H-lines) — physical/kinematic polarization count only; NO surviving analytic index derivation.* As of 2026-06-23 every analytic route to ind_H(D_RS) = 8 has FAILED or is OPEN: the scalar Flensted-Jensen / rank-one BC1 chain was superseded (correct involution → split-rank 3, A3 root system, no scalar discrete series); the direct rank-3 Atiyah-Schmid route is an empty formal-degree sum (SL(4,ℝ) has no discrete series); the tau-twisted rescue FAILS AS STATED on four independent criteria; the BC1 Jacobi fiber-wavefunction route to G2a is a **GENUINE_OBSTRUCTION** (oq-kk1-bc1-jacobi-operator-parameters, 2026-06-23: discrete spectrum at ν = 5/2, 1/2 only, not ν = 3/2); and the SU(2)-holonomy / APS-K3 route is **OPEN, not conditionally resolved** — per CORRECTION FC4-HOLONOMY-01 (2026-06-23), ten independent index computations gave {960, −288, −384, −192, −336, −128, 128, −8, −480, 60} with no convergence to 16, and the only support for "8" is the kinematic helicity count (a polarization count, NOT an analytic index). Gates OQ-RK1 (first-principles RS rank rank_H(S_RS^+) = 4) and OQ-RK2 (APS boundary conditions for the constrained RS operator on K3) remain OPEN.
>
> **Failure conditions / reopen-or-stays-open triggers for GU-Chir (the count stays OPEN until ALL clear; any one firing keeps it open):**
> 1. **(GC-FC1) No analytic RS index.** ind_H(D_RS) = 8 has no first-principles analytic index derivation surviving (all known routes FAILED/OPEN; current support is kinematic only). FIRING.
> 2. **(GC-FC2) OQ-RK1 open.** The Rarita-Schwinger rank rank_H(S_RS^+) = 4 is not derived from first principles (the "half of chiral = 4" final halving is an unjustified heuristic per CORRECTION GEN-01). FIRING.
> 3. **(GC-FC3) OQ-RK2 open.** The APS boundary conditions for the constrained RS operator on the compact K3 factor are not established, and the standard vector-spinor-minus-trace operator gives ind_H = −144 (not +8) on the file's own computation. FIRING.
> 4. **(GC-FC4) Non-compact base unresolved.** Y^{14} = Met(X^4) is non-compact (open Lorentzian-signature condition); standard compact index theorems do not apply, and the Fredholm/APS reduction to a compact factor is itself reconstruction-grade. FIRING.
>
> The count would advance toward RESOLVED only when GC-FC1–GC-FC4 all clear (an independent analytic derivation of ind_H(D_RS), closing OQ-RK1 and OQ-RK2, on the actual non-compact base). Until then: **OPEN, reconstruction-grade target.**

GU-Chir replaces DG's Lie-algebraic chirality *test* with an operator-analytic *test* (the invariant ind_H(D_GU) in place of V_{2,1} complexity). No functor from GU's construction to DG_E8 is known that preserves ind_H(D_GU), because DG_E8 forbids bundle/compactification data (DG-A7) and the chirality invariant depends on X^4 topology and Clifford module structure, not E8 adjoint branching. The DG carve-out from the functor audit (see Functor-audit status entry above) is therefore a **precision *class-membership* result**: GU's exit from DG is at the level of the category of objects (which invariant carries chirality, and whether GU is an object of DG_E8), not a clever condition-by-condition evasion. **The precision-theorem status attaches ONLY to the scope-exit / class-membership claim (DG is inapplicable to GU because GU is not in DG_E8 and uses a different chirality invariant); it does NOT attach to the *numerical value* of that invariant. "ind_H(D_GU) = 24" and "3 generations" remain OPEN (see the GU-Chir block above), and the EVASION-BY-SCOPE-EXIT verdict does not depend on them: GU exits DG's class via DG-A1/A2/A6/A7 regardless of what ind_H(D_GU) ultimately evaluates to.** Reopen only if a functor F_DG: GU_data → DG_E8 is exhibited that lands in the correct category and preserves the chirality invariant.

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

**GU evasion status: CONDITIONALLY_EVADED (reconstruction) at 14D — gated on E-block invertibility (FC-VZ-1 / VZ-01), which is closed ONLY by a same-session reconstruction-grade argument and therefore, per the loop's same-session-circularity rule, requires an intervening external/inter-session verified computation before the 14D leg can be called VERIFIED or EVADED (see the SAME-SESSION-CIRCULARITY note in the GUARD block below); CONDITIONALLY_RESOLVED at 4D principal-symbol level (reconstruction; subprincipal order open per FC-VZ-4) (2026-06-23).**

**Summary of 2026-06-23 computation chain (vz-schur + OQ1 + OQ2 + OQ3-V1/V2/V3):**

At 14D: the Schur complement symbol `D_RS_eff(xi) = S_R^{14D}(xi)` is **claimed** to have `ker = 0` for all 14D covectors with `g_Y(xi,xi) != 0`, including mixed horizontal+normal covectors. **Read this as a single conditional claim, not two independent facts.** The argument is: Clifford module identity `sigma_D(xi)^2 = xi2 Id_E` ⟹ `ker S_R = 0` **via the block-inversion / Schur-complement formula `S_R = A - B E^{-1} C`** (§8 of `explorations/vz-schur-complement-2026-06-23.md`). That formula uses `E(xi)^{-1}` and is therefore *defined only when the E-block `E(xi)` is invertible* — which is exactly the unproven precondition FC-VZ-1 (FC-VZ-1: `E(xi)` has nontrivial kernel for some non-null `xi` ⟹ Schur complement undefined). **Consequence (do not lose this): `ker S_R^{14D} = 0` is DERIVED THROUGH E-block invertibility; it is the SAME claim as "FC-VZ-1 holds," not independent corroboration of it.** The source file's own VZ-01 correction states this plainly: "the `det(M) = det(E)·det(S_R)` identity requires `E` invertible as a precondition and cannot be used to prove `E` invertible without circularity" (`explorations/vz-14d-mixed-covectors-2026-06-23.md` §correction). So the "14D `ker S_R = 0`" result and "E-block invertible" are one and the same load-bearing assumption, and the 14D verdict is CONDITIONALLY_EVADED *precisely because that one assumption (FC-VZ-1) is unverified* (reconstruction grade; not CAS-verified -- the 14D E-block explicit form is structural, not CAS-verified). A reader must not count `ker S_R = 0` and E-block invertibility as two separate pieces of evidence.

At 4D: OQ3-V2 and OQ3-V3 are RESOLVED (exact, gauge-independent); OQ3-V1 is CONDITIONALLY_RESOLVED (§18). OQ3-V1: the principal symbol `s*(sigma_{D_GU})(eta)` has no anomalous normal-direction terms -- horizontal Clifford computation gives `c_s(eta)^2 = g_s(eta,eta) Id_S`, **but this is computed ONLY in the constant-coefficient flat Minkowski gauge** (flat section `s(x) = (x, eta)`); the curved/general-section case is asserted pointwise, not computed (this is the open OQ3-V1 curved-background frame-splitting check). OQ3-V2: the 4D E-block `[[0, 1/4],[1, 3/2]]` has determinant `-1/4 != 0` (explicit computation); overall invertibility from Clifford identity. OQ3-V3: `R_s = ker Gamma^{4D}` exactly -- section pullback on H*/N* split is exact, normal RS components are KK scalars not spin-3/2 fields. 4D VZ evasion: at the **principal-symbol** order the characteristic cone of `D_RS_eff^{4D}` = null cone of `g_s`; no spacelike characteristics. CONDITIONALLY_RESOLVED at 4D principal-symbol level (reconstruction grade). This 4D principal-symbol evasion is **overturnable at the next (subprincipal) order** if the second fundamental form `II_s = s*(θ)` sources spacelike characteristics — see FC-VZ-4 below; `vz-subprincipal` finds no such sub-characteristics, but that result is itself reconstruction grade, so the verdict is held at CONDITIONALLY_RESOLVED, not VERIFIED.

**Remaining open conditions (not VZ obstruction, dynamical residuals):**

**F5.** Lower-order curvature terms at 4D: Sp(64) gauge curvature `F_A` and 4D Riemann tensor `R_{g_s}` are zero-order terms in `D_GU^{4D}`. Cannot modify the principal symbol (CONDITIONALLY_RESOLVED by vz-oq2, vz-subprincipal). The constrained-Hamiltonian propagation of the subsidiary condition `Gamma^{4D} psi = 0` in an Sp(64) background: **CONDITIONALLY_RESOLVED 2026-06-23 (vz-f5-hamiltonian-subsidiary-propagation, reconstruction) — LOAD-BEARING ON THE UNPROVEN CLAIM FC1 (no standalone GU RS Lagrangian); the verdict is an assumption-conditional, not a free-standing derivation. ⚠ SAME-SESSION, PENDING INTER-SESSION CHECK (CORRECTION F5-SS-01, 2026-06-23): the residual-open state of this full-dynamical-level gate AND its closure to CONDITIONALLY_RESOLVED are BOTH dated 2026-06-23 and rest on `vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md`, which is UNTRACKED in git — authored this same session and not yet reviewed in any later pass. The closing argument (the gamma-trace `Gamma^{4D} psi = 0` is KINEMATIC, not a dynamical subsidiary condition, so the Dirac-Bergmann chain never initiates) IS the FC1 claim; FC1 (no standalone GU RS Lagrangian exists) is OPEN and self-referential to the same reasoning that closes the gate — it is established only as absence-of-identification, not proof of absence. The full-dynamical-level VZ gate is therefore NOT settled. The kinematic-vs-dynamical claim must be independently re-derived in a LATER session, on a tracked/reviewed file, before any downstream file treats F5 as closed; until then read this cell as a same-session conditional reading, not a resolved dynamical gate.** The Dirac-Bergmann analysis itself derives (vz-f5 §4.6(b), §4.10) that when `F_A != 0` the gamma-trace constraint is NOT preserved under time evolution (`[Gamma^{4D}, Phi(F_A)] Psi_R != 0`; `phi = Gamma^{4D} Psi` does not stay zero) — i.e. **the constraint DOES leave `ker Gamma^{4D}` (the RS sub-bundle) at the field-equation level**: a configuration that is purely RS at `t=0` develops non-RS components under evolution (vz-f5 §4.6(b): "the time derivative of an RS field leaves the RS sub-bundle"; §4.10: "`phi = Gamma^{4D} Psi` does not remain zero for all t"). In the classical VZ analysis this non-preservation of the gamma-trace under gauge coupling IS the obstruction signature. It is reinterpreted as benign here ONLY IF the Schur-complement system is the correct dynamics (gamma-trace kinematic, `Psi_Q` slaved, no externally-imposed subsidiary condition to propagate) — which is exactly FC1. FC1 is OPEN: vz-f5 establishes only that no standalone RS Lagrangian has been *identified* (absence of identification, not proof of absence; the GU action on `Y^14` is not available at reconstruction grade). Under the alternative reading (FC1 false) the §4.6(b)/§4.10 non-preservation is a GENUINE_OBSTRUCTION. **The benign reading ALSO rests on an unproved energy estimate.** vz-f5 §4.8's "Constraint Propagation Theorem" (`Gamma^{4D} Psi|_{t=0} = 0` ⟹ `Gamma^{4D} Psi = 0` for all t) is explicitly an admitted **proof sketch**: it recasts the constraint leak `phi = Gamma^{4D} Psi` as a *sourced* symmetric-hyperbolic system `D_GU^{4D} phi = source(Psi_R)` and then needs an energy estimate `||phi||_{H^k} <= C ||source||_{H^k}` with `||source|| -> 0` as `||Psi_R|| -> 0` to conclude `phi = 0`. **That estimate is NOT done — it is the open gate FC3 / OQ-H1** (vz-f5 §7 FC3, §9 OQ-H1): the sourced energy estimate for `phi = Gamma^{4D} Psi`, including the `K_{mu nu}` extrinsic-curvature source term, is the decisive unproven step on the propagation side. So at the field-equation level the constraint leaks the sub-bundle, and closure rests on BOTH (a) the FC1-conditional Schur-complement reframing AND (b) the unproved FC3/OQ-H1 energy estimate. Four failure conditions FC1-FC4: FC1 (standalone GU RS Lagrangian — load-bearing, open negative-existence claim), FC2 (F_A enters B/C at first order), **FC3 / OQ-H1 (the sourced symmetric-hyperbolic energy estimate for `phi = Gamma^{4D} Psi` that would make the §4.8 proof sketch rigorous is NOT established; whether `K_{mu nu}` extrinsic-curvature sourcing produces a spacelike effective characteristic for `phi` is exactly what this open estimate would settle; the §4.8 `K_{mu nu}` commutator algebra is reconstruction grade with a visible mid-proof self-correction, not independently re-derived/CAS-checked — this is the load-bearing analytic gap on the constraint-propagation side)**, FC4 (RS mass term enters S_R at first order). None established as a structural obstruction; the verdict rests on FC1 (kinematic-vs-dynamical reframing) and the still-open FC3/OQ-H1 energy estimate (constraint propagation). See `explorations/vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md` (§4.8 proof sketch; §7 FC1/FC3; §9 OQ-H1).

**~~F6~~ CONDITIONALLY_RESOLVED (vz-schur §19, 2026-06-23).** 4D EFT decoupling: the KK zero mode sub-bundle `E_s^{(0)}` inherits the full Clifford module property from `D_GU^{4D}` because the horizontal Clifford element `c_s(eta) = eta_a gamma^a_H` commutes with the KK mode projector `P_{(0)}`. The §8 kernel argument (`ker S_R = 0` for non-null covectors) applies verbatim to the EFT — and so it inherits the §8 contingency verbatim: it is still derived through `S_R = A - B E^{-1} C` and is therefore the SAME conditional claim as FC-VZ-1 (E-block invertibility), not an independent EFT-level corroboration of causality. The B/C coupling blocks are O(1) algebraic functions of eta in the zero-mode sector (not KK-suppressed). Even in the deep IR limit where `B E^{-1} C` is small, the RS-RS diagonal block A(eta) is itself causal (`A S_R = xi2 Id_R` from block identity (II)-(III)). The gamma-trace constraint is intrinsic to the Clifford module structure (not an external subsidiary condition), so the VZ constraint-propagation mechanism cannot fire. Remaining open: KK zero mode existence (requires discrete-series spectrum); loop corrections to B/C blocks. The 4D EFT RS characteristic cone argument survives the KK mass-gap condition.

**OQ2 (guardian symmetry for decoupled RS).** F6 is now CONDITIONALLY_RESOLVED (RS does not decouple into a standalone field at the kinematic level). OQ2 is therefore contingent-RESOLVED: the guardian symmetry question is moot at the EFT principal-symbol level. A guardian would only be needed if loop corrections to the B/C blocks drove them to zero in the IR -- a named open gap but not an established failure mode.

**OQ (gravitational VZ from gimmel metric).** The Weyl tensor of the gimmel metric on `Y^{14}` could in principle produce curvature-induced VZ acausality (Buchdahl 1962, Aurilia-Umezawa 1969) independent of gauge coupling. The zero-order argument from vz-oq2 shows this cannot modify the principal symbol; the sub-leading level requires the Hamiltonian analysis of F5.

**Failure conditions status (updated 2026-06-23):** (F5-full) constrained-Hamiltonian analysis CONDITIONALLY_RESOLVED **— load-bearing on the unproven negative-existence claim FC1 (no standalone GU RS Lagrangian); assumption-conditional, not a free-standing derivation. ⚠ SAME-SESSION, PENDING INTER-SESSION CHECK (F5-SS-01): the gate's open state and its closure are both 2026-06-23 and rest on an untracked same-session file; the full-dynamical-level gate is NOT settled and the kinematic-vs-dynamical (FC1) claim must be independently re-derived in a later session on a tracked file before F5 is treated as closed downstream.** The Dirac-Bergmann chain does not fire ONLY IF FC1 holds (gamma-trace kinematic, not dynamical subsidiary condition); the analysis itself derives that the gamma-trace is NOT preserved when `F_A != 0` (vz-f5 §4.6(b)/§4.10), which in classical VZ is the obstruction signature and is benign here only under the FC1-conditional Schur-complement reading. `F_A != 0` only contributes zero-order to the Schur complement; remaining FC1-FC4 are not established obstructions, but FC1 is open (absence of identification, not proof of absence) and the verdict rests on it. The closure ALSO rests on the still-open FC3/OQ-H1 energy estimate: the gamma-trace constraint does leave `ker Gamma^{4D}` at the field-equation level (vz-f5 §4.6(b)/§4.10), and the §4.8 Constraint Propagation Theorem that would close this leak is an admitted proof sketch whose decisive step — a sourced symmetric-hyperbolic energy estimate for `phi = Gamma^{4D} Psi` (vz-f5 §9 OQ-H1, §7 FC3, including the `K_{mu nu}` extrinsic-curvature source) — is NOT done. (F6-loop) large IR loop corrections driving B/C coupling blocks to zero: OPEN -- requires explicit one-loop B/C computation. Neither F5-full nor F6-loop is an established obstruction; VZ evasion status: CONDITIONALLY_EVADED at 14D (reconstruction; gated on E-block invertibility, VZ-01) and CONDITIONALLY_RESOLVED at 4D principal-symbol level (reconstruction; subprincipal order open per FC-VZ-4).

**[Fifth-theorem formal canon entry, 2026-06-23 — no-go-velo-zwanziger-canon-entry]**

A formal four-part VZ entry (matching the shape of the DG precision carve-out in §2.4) is recorded in `explorations/no-go-velo-zwanziger-canon-entry-2026-06-23.md`. Its content:

- **Assumptions (formal list).** VZ-H1 (standalone RS Lagrangian with externally-imposed gamma-trace subsidiary condition), VZ-H2 (minimal coupling `∂ → D = ∂ + A`), VZ-H3 (non-singlet gauge representation), VZ-H4 (flat/mildly-curved background), VZ-H5 (no guardian symmetry).
- **Condition GU satisfies instead of VZ-H1 (evasion type = Clifford-module-non-sub-module mechanism).** `GU-VZ`: the RS sector is the gamma-trace kernel `R = ker Γ ⊂ E` of the single Clifford module bundle of `D_GU`; Clifford multiplication does not preserve `R` (`R` is **not a sub-Clifford-module** of `E`), so the off-diagonal blocks `B`, `C` are kinematically nonzero and the exact entanglement identity `A S_R = S_R A = g_Y(xi,xi) Id_R` holds (from block-square identities (I)/(II)/(III)). This forces the effective RS characteristic cone `{det S_R = 0}` into the null cone `{g_Y(xi,xi) = 0}`: no spacelike characteristics, no VZ acausality. GU does **not** evade by trivial coupling (H3 fires: the RS sector carries a full Pati-Salam generation) nor by a guardian (no established SUSY); it evades by violating H1 — there is no standalone RS field.
- **Forgetful operation.** The minimal-coupling functor `ϕ_mc` forgets the Clifford-module embedding `R ⊂ E` (the `B`/`C` datum) and treats `R` as a standalone matter field; the VZ class is `image(ϕ_mc)`, and GU lies in the domain but not the image.
- **Explicit failure conditions FC-VZ-1…5.** (1) `E(xi)` has nontrivial kernel for some non-null `xi` (Schur complement undefined; the open VZ-01 precondition); (2) a standalone GU RS Lagrangian exists whose field equations are not the section-restricted `D_GU Ψ = 0`; (3) `F_A` enters `B`/`C` at first order in `xi`; (4) `II_s = s*(θ)` (the extrinsic curvature of the section embedding) sources an effective first-order term in `S_R^{4D}` producing spacelike characteristics — i.e. the 4D principal-symbol evasion is overturned at the next (subprincipal) order (`vz-subprincipal` finds no such sub-characteristics, but at reconstruction grade only, which is exactly why the 4D leg is held at CONDITIONALLY_RESOLVED rather than VERIFIED); (5) IR loop corrections drive `B`/`C` to zero (decoupling). None is an established obstruction as of 2026-06-23.

This entry is a synthesis/no-go-map formalization of the existing §2.5 analysis chain, not a new computation. It binds the verdict honestly: **14D is reconstruction (CONDITIONALLY_EVADED), 4D is CONDITIONALLY_RESOLVED at the principal-symbol level (reconstruction; subprincipal order open per FC-VZ-4)** — neither leg over-stated, and neither labelled VERIFIED while a known higher-order route to being overturned (FC-VZ-4) remains unaddressed. The single gap separating 14D from EVADED is external verification of E-block invertibility (FC-VZ-1). **Note that this is not a gap *in addition to* the `ker S_R^{14D} = 0` result — it IS that result: `ker S_R = 0` is obtained via the Schur-complement formula `S_R = A - B E^{-1} C`, which is only defined when `E(xi)` is invertible. The 14D kernel claim and FC-VZ-1 are one and the same load-bearing assumption; closing FC-VZ-1 is what would turn the conditional `ker S_R = 0` into an established result and the verdict into EVADED.** The gap separating the 4D leg from VERIFIED is closure of the subprincipal/extrinsic-curvature check (FC-VZ-4).

**GUARD (FC-VZ-1, 2026-06-23) — SAME-SESSION-CIRCULARITY: do not treat E-block invertibility as established.** FC-VZ-1 (E-block `E(xi)` invertibility on the non-null cone) is supported ONLY by a same-session, externally-unverified direct Clifford argument (`explorations/vz-e-block-direct-clifford-2026-06-23.md`, self-described as "same-session reconstruction-grade direct Clifford argument; not externally verified"). This is the single load-bearing precondition of the 14D `ker S_R = 0` Schur argument, and it has NO external/inter-session verification. The loop's same-session-circularity rule is explicit and binding here: **a flag (here the VZ-01 / CR-04 E-block circularity flag) that was raised and resolved within the same session cannot be treated as closed; separation by file does not constitute external or inter-session verification.** FC-VZ-1 is therefore closed only by a same-session sibling, which by that rule cannot close a same-session flag. **An intervening external / inter-session verified computation of E-block invertibility is required before the 14D leg may be called VERIFIED or EVADED; it must be independently re-checked in a later session, on a tracked/reviewed file, before 14D is upgraded from CONDITIONALLY_EVADED.** A future loop pass must NOT read this canon block — or the NEXT-STEPS.md `vz-e-block-direct-clifford` log entry, which still carries a same-session "RESOLVED / verified grade / upgraded to EVADED" phrasing superseded by CORRECTION CR-04 — as having settled the E-block question. The residual risk this GUARD exists to prevent is a future reader treating the 14D leg as more settled than "one same-session unverified argument away from collapse." The same-session origin of the supporting file is exactly the circularity pattern this map's workflow auditor flags ("be especially suspicious of files promoted today").

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
**Cross-artifact finding for GU paper §12.9 (effective chirality).** GU paper §12.9 proposes effective chirality: the Dirac operator on Y is globally non-chiral, with apparent chirality arising in low-curvature regions through coupling to scalar curvature R(y). Assessed against Distler-Garibaldi assumption (5) — "V_{2,1} is a complex G-representation" — GU's claim is that the complex-representation character of the fermionic sector is emergent (L5) rather than fundamental. The formalization question is whether GU's scalar-curvature coupling produces a region-dependent effective G-representation that is complex as seen by a low-energy observer, and whether the DG representation-theoretic argument applies to this effective spectrum or only to the global (non-chiral) one. If the latter, GU may sidestep DG via an L5 class-change (emergence: chirality is not a property of the substrate but of an observer-relative effective description). This is not an established evasion; it is an open formalization challenge. Tracked in `paper-formalization-candidates.md` claim 6C; reference surfaces in `sources/gu-paper-reference-surfaces.md`.

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

Three of five no-go families admit a forgetful-image reading that is at most an adjacent reformulation of the published evasion literature. The fourth (Distler-Garibaldi) is the stress case where the frame works least well: every successful evasion changes the category, not the shadow. The fifth (Velo-Zwanziger) is GU-specific: it constrains GU's own spin-3/2 matter prediction directly. Full analysis chain completed 2026-06-22 through 2026-06-23 across `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md` and the vz-* exploration pack (vz-schur, vz-oq1, vz-oq2, vz-subprincipal, vz-f5, vz-f6, vz-14d-mixed-covectors). The evasion mechanism: "trivial internal coupling" fails at the 4D level (the RS sector carries SM charges); the coherent evasion is Clifford module non-decoupling — the RS sub-bundle is not a sub-Clifford-module of E, so it cannot propagate as a standalone field, and VZ's standalone-RS-Lagrangian assumption H1 is violated. The Schur complement kernel argument (vz-14d-mixed-covectors §4, reconstruction grade) **claims** `ker S_R^{14D}(xi) = 0` for all 14D non-null covectors including mixed horizontal+vertical — but this claim is *contingent on FC-VZ-1 (E-block invertibility) and is not independent of it*: `ker S_R = 0` is derived through the Schur-complement formula `S_R = A - B E^{-1} C`, which presupposes `E(xi)^{-1}` exists. **"14D `ker S_R = 0`" and "FC-VZ-1 holds" are the same claim, not two separate results** (the source file's VZ-01 correction: the block-determinant identity "requires `E` invertible as a precondition and cannot be used to prove `E` invertible without circularity"). The 14D leg is therefore CONDITIONALLY_EVADED, not EVADED, precisely because that single precondition is unverified. The 4D section-pullback resolves OQ3-V1/V2/V3 at the principal-symbol order, but remains overturnable at subprincipal order per FC-VZ-4 (extrinsic-curvature characteristics) and so is held at CONDITIONALLY_RESOLVED, not VERIFIED. Status: **CONDITIONALLY_RESOLVED** at 4D principal-symbol level (reconstruction; subprincipal order open per FC-VZ-4), and **CONDITIONALLY_EVADED** at 14D (horizontal + full mixed covectors, reconstruction grade, gated on E-block invertibility FC-VZ-1). Remaining open: subprincipal/extrinsic-curvature characteristics (FC-VZ-4); full constrained-Hamiltonian analysis of subsidiary-condition propagation under Sp(64) gauge curvature (F5); loop corrections to B/C blocks (F6/OQ-RS-2); KK zero-mode existence requires discrete-series spectrum. The map's recommendation is to **publish with both the DG stress case and the VZ CONDITIONALLY_RESOLVED status visible**, and to use the ranked tests above as the falsification surface.

The map does not say the no-go theorems are wrong. It says they fix classes, and for three of the five families the "what gets lost in the smooth-bundle shadow" question has plausible substrate-level answers that the literature is already approaching from the geometric side. The unified meta-frame ("forgetful images of richer substrate invariants") is implicit/adjacent for Witten / Nielsen-Ninomiya / Freed-Hopkins, is **originally and contentiously** at stake for Distler-Garibaldi, and is **GU-prediction-specific and CONDITIONALLY_RESOLVED at reconstruction grade** for Velo-Zwanziger.

## Appendix A — Siblings referenced

- **internal origin artifact / six-axis specification protocol (sibling #24).** This map cites and is consistent with the six-axis protocol; each per-theorem map names the L1-L6 axis(es) the richer-data candidate occupies. The Type II_1 example (example-01) is treated as a worked illustration of "preserve L2-L4, push richer data into L1" for the Freed-Hopkins-compatibility argument.
- **Sibling #26 / Type II_1 spectral SM checklist .** This map's Freed-Hopkins section makes a specific architectural prediction for the Type II_1 candidate (that L1 enrichment is invisible to the standard bordism input via the Connes-channel pairing). Sibling #26 should record this as a checklist item, not just as a derivative reading.
- **Sibling #27 / Nielsen protocol-analogy pilot (internal origin artifact).** This map's Nielsen-Ninomiya section makes a specific prediction for the protocol-analogy: assumption (5) — exact on-site chiral symmetry — is the protocol-side analog of GW/overlap, and modified-consistency-model is the expected cleanest evasion.

All other siblings in the coordination list are independent of this map's content as of 2026-05-30 draft.

## Appendix B — Honest gaps in this map

- The map does not formally construct any of the candidate forgetful operations as functors between specified categories. They are named structurally; the construction is an open task.
- The Distler-Garibaldi handling is unresolved on substance, not just on framing. The honest verdict is that the unified frame strains here; the map ships this as a visible stress, not a solved problem.
- The "what gets lost" column for Distler-Garibaldi is genuinely speculative because the framework does not pick out a unique forgetful operation; (a), (b), (c) above are three different shadow-candidates with different lost-data content.
- The Velo-Zwanziger entry is GU-specific. Full analysis chain 2026-06-22 through 2026-06-23: `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md` and vz-* pack (vz-schur, vz-oq1, vz-oq2, vz-subprincipal, vz-f5, vz-f6, vz-14d-mixed-covectors). Status upgraded from OPEN to CONDITIONALLY_RESOLVED at 4D principal-symbol level (reconstruction; subprincipal order open per FC-VZ-4, OQ3-V1/V2/V3 resolved only at principal-symbol order) and CONDITIONALLY_EVADED at 14D (horizontal + full mixed covectors, reconstruction grade, gated on E-block invertibility FC-VZ-1). Not labelled VERIFIED: a verdict is reserved for VERIFIED only when there is no acknowledged route to being overturned, and FC-VZ-4 (extrinsic-curvature-sourced spacelike characteristics at subprincipal order) is exactly such an open, unaddressed route. Evasion mechanism: Clifford module non-decoupling (RS sub-bundle is not a sub-Clifford-module of E, so VZ assumption H1 is violated). Remaining open: FC-VZ-4 (subprincipal/extrinsic-curvature characteristics); F5 (full constrained-Hamiltonian analysis under Sp(64) curvature); OQ-RS-2 (loop corrections to B/C blocks); KK zero-mode existence. The "trivial internal coupling" claim was found to be false at the 4D level (RS sector carries SM charges); OQ2 (guardian symmetry) is contingent-RESOLVED because RS does not decouple kinematically.
- The map cites the literature in `literature/03` but does not independently verify each citation. The map's correctness about the no-go theorems is downstream of that brief's correctness.

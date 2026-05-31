---
title: "Stochastic Reduction — Parity / Chirality Falsification Test"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# Stochastic Reduction — Parity / Chirality Falsification Test

**Status.** Public draft artifact.
**Source basis.** `process/persona-passes/02-substrate-loophole-lenses/11-stochastic-geometer-loophole.md`, `process/persona-passes/04-heterodox-problem-shape-math/21-ps-stochastic-heterodox.md`, `process/syntheses/00b-loophole-synthesis-witten-evasion-test.md`, `process/persona-passes/02-substrate-loophole-lenses/12-quantum-measurement-loophole.md`, `process/persona-passes/02-substrate-loophole-lenses/13-nondeterminism-loophole.md`. Cross-built against the six-axis protocol (WRK-375), the no-go-forgetful-image map (WRK-376), and the Nielsen protocol-analogy pilot (WRK-378).
**Generated.** 2026-05-30
**WRK card.** WRK-382.

## 0. Honesty contract

This draft is a **single-pass falsification test**. The question is narrow and binary-ish:

> When a "stochastic reduction" replaces smooth Kaluza-Klein dimensional reduction with a measure-theoretic / stochastic-dynamical operation on the metric bundle Met(X), does parity (and the chirality content the SM requires) **emerge** from the reduction dynamics, or is it **inserted** by hand somewhere in the construction (in the noise term, in the boundary conditions, in the measure, in the Kraus operators)?

The verdict is binary at the level of each proposal: **derived**, **inserted**, or **literature-silent** (proposal exists but published analysis does not address parity / chirality emergence). "Literature-silent" is reported as itself, not extrapolated.

No claim is made that any reviewed proposal is wrong. The claim is only about whether parity-breaking is a theorem of the proposal or an input to it.

This draft does **not** introduce new physics. Where the surveyed material does not engage a proposal (notably GRW, CSL, Diosi-Penrose collapse models), the answer is "not addressed in the GU-repo material surveyed for this pass." That gap is reported, not papered over.

## 1. What "derived" vs "inserted" means here

A stochastic reduction path proposes:

- a substrate with a probability measure or stochastic dynamics (the "noise"),
- a forgetful / projection / collapse operation that produces a 4D effective field theory or observation,
- an output: the 4D effective spinor content, including its parity / chirality structure.

**Derived** means: parity-asymmetry in the 4D output is a **theorem** of the (substrate, dynamics, projection) triple. Specifically, the 4D parity-violating two-point function, axial anomaly, or chiral-spectrum asymmetry follows from the substrate-level construction without any parity-odd structure being put into the noise, the drift, the boundary, the measure choice, the Kraus operators, or the channel by hand.

**Inserted** means: somewhere in (substrate, noise, drift, measure, channel, Kraus operators, boundary conditions, observer split) a parity-odd structure is stipulated. The construction then reports back the parity it was told to report. This is what Witten 1981 morally rules out — Witten's no-go is precisely about smooth deterministic reductions where parity isn't snuck in via input.

**Literature-silent** means: the proposal exists in published form, but the published literature has not stated whether its parity content is derived or inserted. We record this as a gap to fill, not as evidence for either side.

The four insertion sites we will explicitly check at each proposal:

1. **Noise / drift insertion** — is the stochastic driver parity-odd, dimension-asymmetric, or oriented?
2. **Measure insertion** — is the prior or pushforward measure parity-asymmetric in a way not derived from the substrate?
3. **Boundary / initial-condition insertion** — does parity enter through CMB-style boundary data, Wick rotation choice, or contour selection?
4. **Channel / Kraus / collapse-operator insertion** — does the collapse / measurement / decoherence operator project onto a chiral subspace by stipulation?

A "derived" verdict requires all four to be clean. A single insertion site is enough to flip the verdict to "inserted."

## 2. Surveyed proposals

Six families of stochastic-reduction proposal. The first three are covered by the GU-repo persona passes; the next three are flagged as part of the standard physics literature on stochastic state-vector reduction but were not engaged by the GU-repo passes. We treat each family one at a time and report what the surveyed material actually says.

### 2.1 Parisi-Wu stochastic quantization (P1, persona 11)

**Proposal.** Replace deterministic dimensional reduction with a Langevin SDE in a fictitious time `τ` driving sections of the metric bundle Met(X). The 4D physics is the `τ → ∞` equilibrium measure restricted to base-manifold observables.

**Where parity could enter.**

- Noise term: standard Parisi-Wu uses white Gaussian noise, which is parity-symmetric.
- Drift term: the standard drift is `-δS/δφ` for the Euclidean action `S`; parity-symmetric iff `S` is.
- Measure: the equilibrium is the Gibbs measure `exp(-S) Dφ`; parity-symmetric iff `S` is.
- Boundary: equilibrium limit `τ → ∞` is parity-symmetric iff the Langevin generator is.

**Verdict on derivation.** **Inserted.** The honest reading from persona 11 (paragraph (e)): "Stochastic quantization, in its standard Parisi-Wu form, is constructed precisely to reproduce the deterministic Gibbs measure in the equilibrium limit, so it gives the same physics — no parity-breaking drift survives without being put in by hand." The construction's `τ → ∞` limit is, by design, the deterministic Gibbs measure; if that measure is parity-symmetric (which it is for any Levi-Civita Witten-class action), so is the equilibrium.

The only way Parisi-Wu evades Witten on parity is to add a parity-odd drift term not derivable from the Euclidean action. That is insertion.

**Falsification criterion already satisfied.** Persona 11 (paragraph (d)): "either: the stochastic-quantization fictitious-time evolution has a parity-breaking drift term that survives the equilibrium limit, OR the GFF restriction-to-X produces a parity-asymmetric two-point kernel." For Parisi-Wu specifically, no published construction supplies the parity-breaking drift from the substrate. Path verdict for this proposal: **inserted; parks unless a derivation of the drift from substrate is supplied.**

### 2.2 Gaussian Free Field restriction (P1, persona 11; also persona 21 heterodox)

**Proposal.** Define a Gaussian Free Field (GFF, log-correlated random field) on the total space of Met(X) and take its trace on X as the observed 4D field. Restriction of a GFF is a generalized random field with anomalous scaling.

**Where parity could enter.**

- The GFF's covariance kernel is determined by the Laplacian on the total space; parity-symmetric iff the underlying metric is.
- Anomalous scaling exponents (sub-section (b)(2) of persona 11) could in principle source a parity-violating two-point function — this is the proposal's strongest steelman.
- Boundary / restriction: choice of which sub-σ-algebra to restrict to (curvature scalars, tetrad at base, etc.) is itself a measurement / projection choice.

**Verdict on derivation.** **Literature-silent, leans inserted.** Persona 11 lists "anomalous scaling exponents could in principle source a parity-violating two-point function" explicitly tagged `[speculation]`. No published GFF-restriction construction is cited in the GU-repo material that delivers a parity-asymmetric two-point kernel without parity-odd input in either the GFF's covariance or the restriction choice.

Persona 21's heterodox extension (Hairer regularity structures, Liouville quantum gravity / DKRV) does sharpen the substrate-level picture but does **not** supply a parity-derivation. Persona 21's own falsifiable sub-question (paragraph (e)) is: *"Does there exist a parity-breaking, reflection-positivity-preserving Gaussian-free-field-class log-correlated random field in d=4 whose Hairer regularity-structure renormalization admits a Type II_1-factor large-N limit?"* This question is **open**; persona 21 does not claim a positive answer.

Path verdict for this proposal: **literature-silent on derivation; would be derived if the open question in persona 21 (e) is answered positively. Until then, treat as inserted-leaning because the standard log-correlated Gaussian fields in even d are parity-symmetric (Bochner-class symmetry constraints).**

### 2.3 Type II_1 / orbit-equivalence measure-class quotient (P3, persona 13)

**Proposal.** Re-read the observerse projection as the canonical map Met(X) → Met(X)/G for a non-locally-compact group G acting by a non-free, measure-class-preserving action. The orbit space is a non-standard Borel space; the field theory lives on a Type II_1 factor; "chirality" becomes a continuous Murray-von Neumann trace difference rather than an integer mode count.

**Where parity could enter.**

- Choice of G: the action's symmetry class determines whether the trace difference is structurally constrained or free.
- Choice of measure class: orbit-equivalence is defined up to measure-class; the chosen class can be parity-symmetric or not.
- Connes spectral-triple internal algebra: the SM-shaped spectral triple's KO-dimension 6 mod 8 carries parity content; extending to II_1 internal algebra (open mathematical program) does not automatically preserve or break that.

**Verdict on derivation.** **Inserted in the sense that matters here.** Persona 13 (paragraph (c)): "the chirality obstruction would dissolve into a statement that the left-minus-right trace difference in M can be any real number, and the requirement that it match the SM chiral content becomes a tuning condition on the equivalence relation, not a topological impossibility."

That is the load-bearing sentence. The II_1 construction does not derive parity; it makes parity into a **continuous tuning parameter**. The 4D chirality content is selected by choosing the equivalence relation; that selection is the insertion. Persona 13 (paragraph (e)) is explicit: "It evades Witten 1981 by dissolving the smooth-mode-counting premise rather than by satisfying it. The construction is not a derivation; it is a reframing that buys evasion at the cost of changing what the projection means."

Path verdict for this proposal: **inserted (via tuning). Reframes the question, does not answer it. Connects to the strongest positive adjacent research direction (Connes II_1-extended spectral triples, syntheses/00b Finding B) but that program too is open on the parity-derivation question and is independent of GU.**

### 2.4 GRW (Ghirardi-Rimini-Weber) spontaneous localization — *not addressed in literature surveyed*

**Proposal.** Stochastic state-vector reduction via Poissonian spontaneous localization events on each particle, with two parameters (rate `λ`, localization width `r_C`). Originally a non-relativistic collapse model.

**Where parity could enter.**

- The Gaussian "hitting" function is parity-symmetric (Gaussian in `(x - x_0)^2`).
- The Poisson rate `λ` is a scalar — parity-even.
- Relativistic GRW extensions (e.g., Tumulka's flash ontology) require choices that may or may not be parity-symmetric.

**Verdict on derivation.** **Not addressed in the literature surveyed for this pass.** None of the GU-repo persona passes engage GRW, and we have not found a GU-repo claim that GRW collapse derives parity or chirality. The standard non-relativistic GRW is, by inspection of the hitting function and rate, parity-symmetric — so it cannot derive parity-breaking. Relativistic extensions are an open program and we make no claim about them.

This proposal is flagged as **literature-silent in this corpus**, not as derived or inserted. A follow-on pass would need to engage the GRW literature directly.

### 2.5 CSL (Continuous Spontaneous Localization, Pearle / Ghirardi-Pearle-Rimini) — *not addressed in literature surveyed*

**Proposal.** Replaces GRW's Poissonian jumps with a continuous stochastic differential equation for the state vector, driven by a Wiener process. The "mass-density" coupling makes the rate effectively scale with macroscopicity.

**Where parity could enter.**

- The driving Wiener process can be chosen scalar (parity-even) or vector (parity-odd by choice).
- The coupling operator (mass density) is parity-even in the standard formulation.
- Relativistic CSL is an active open problem; no consensus formulation.

**Verdict on derivation.** **Not addressed in the literature surveyed for this pass.** Same status as GRW. Standard non-relativistic CSL uses scalar mass-density coupling and a scalar Wiener driver, both parity-even, so it cannot derive parity. Relativistic CSL is open and we report no claim. A follow-on pass should engage the CSL literature directly.

### 2.6 Diosi-Penrose gravity-induced reduction — *not addressed in literature surveyed*

**Proposal.** Wavefunction collapse driven by gravitational self-energy differences; collapse rate set by the Newtonian gravitational self-energy of the mass-density difference between branches.

**Where parity could enter.**

- Newtonian gravity is parity-symmetric; the self-energy functional is parity-even.
- Any general-relativistic extension (Penrose's `OR` proposal in curved spacetime) might in principle couple to parity through the spacetime structure, but the published Diosi-Penrose collapse rate is parity-even.

**Verdict on derivation.** **Not addressed in the literature surveyed for this pass.** Standard Diosi-Penrose is parity-even by construction (Newtonian gravitational self-energy). A relativistic extension that uses Lorentzian / metric structure could in principle pick up parity from spacetime, but no derivation of SM-shape chirality from Diosi-Penrose has been published that we have surveyed.

This proposal is flagged as **literature-silent in this corpus**, not as derived or inserted.

## 3. Aggregate verdict table

| proposal | derived? | inserted? | literature-silent? | one-line reason |
| --- | --- | --- | --- | --- |
| Parisi-Wu stochastic quantization | no | yes | no | equilibrium limit IS the deterministic Gibbs measure; any parity-breaking drift is hand-installed (persona 11) |
| GFF restriction / Hairer-renormalized log-correlated field | unproven | leans yes | partly | persona 21 (e) open question; no published GFF construction supplies parity-asymmetric two-point kernel without parity-odd input |
| Type II_1 / orbit-equivalence quotient (Connes II_1 extension) | no | yes (via tuning) | no | persona 13 explicit: parity becomes continuous trace tuning parameter, not a theorem |
| GRW spontaneous localization | not in this corpus | not in this corpus | yes | non-relativistic GRW parity-even by construction; relativistic open |
| CSL (Pearle / GPR) | not in this corpus | not in this corpus | yes | non-relativistic CSL parity-even by construction; relativistic open |
| Diosi-Penrose gravity-induced reduction | not in this corpus | not in this corpus | yes | Newtonian self-energy parity-even by construction; relativistic extension open |

**Aggregate verdict.** Of three proposals the surveyed material does engage (Parisi-Wu, GFF, II_1 orbit-equivalence), **none derives parity / chirality breaking from substrate dynamics**. Parisi-Wu and II_1 are explicit insertions; GFF is unproven and leans inserted given the open status of persona 21's (e) question. Three further proposals from the standard stochastic-reduction literature (GRW, CSL, Diosi-Penrose) are **literature-silent in this corpus**; their non-relativistic forms are parity-even by construction, but their relativistic extensions are open.

The stochastic route, as represented in the GU-repo material, has **zero derived parity-breaking outputs**. It has one reframing-of-the-question (II_1 / Connes) that is a real adjacent research direction but does not deliver derivation.

## 4. Falsification criteria

For this lane to **upgrade** from "parks" to "remains plausible" or "useful only as analogy," one of the following must happen:

### 4.1 Upgrade criteria — "remains plausible"

A stochastic-reduction proposal would clear the bar for "remains plausible" only if **all four insertion sites** in §1 are clean AND the construction is supported by published mathematics. Specifically:

1. A specified stochastic-dynamical substrate (Langevin SDE, GFF + RG, orbit-equivalence, GRW-class, CSL-class, or Diosi-Penrose-class) on Met(X) or an equivalent richer object.
2. The substrate's noise, drift, measure, and (where present) collapse / Kraus operators are all **parity-symmetric** as a structural property.
3. The 4D effective spinor content, derived from the substrate's reduction operation, nevertheless exhibits parity-breaking that **matches SM chiral structure** (axial anomaly, three generations, charge assignments).
4. The construction satisfies Osterwalder-Schrader reflection positivity (so a unitary 4D QFT interpretation exists), as flagged in persona 11 (d).

The most concrete operational form of this is persona 21's falsifiable sub-question:

> Does there exist a parity-breaking, reflection-positivity-preserving Gaussian-free-field-class log-correlated random field in d=4 whose Hairer regularity-structure renormalization admits a Type II_1-factor large-N limit?

A positive answer would clear bar (1)-(4) for the GFF + Hairer + II_1 substrate combination. A negative answer (by Bochner / reflection-positivity obstruction on log-correlated fields in even d) closes this combination of the lane.

### 4.2 Upgrade criteria — "useful only as analogy"

A weaker form survives if a stochastic proposal does not derive parity but does provide a **forgetful-image-style class restatement** of Witten 1981 that makes the no-go theorem's class-dependence visible in a new vocabulary. The II_1 / Connes reframing meets this bar in principle (it makes parity into a tuning parameter rather than a topological invariant — that is information). But it does not deliver chirality from substrate dynamics, so it cannot replace a derivation.

### 4.3 Downgrade criteria — "should be parked"

A proposal should be parked if all of the following hold:

1. No insertion-free derivation has been produced in the literature.
2. The non-relativistic baseline of the proposal is parity-symmetric by construction (so no derivation is possible without nontrivial relativistic extension).
3. The relativistic extension is itself an open problem with no published candidate construction that addresses parity.

By this criterion: **Parisi-Wu (parks), GRW (parks pending its own relativistic literature), CSL (parks pending its own), Diosi-Penrose (parks pending its own)**.

II_1 / Connes does not park because its reframing is independently valuable as a class restatement (even though it does not derive parity). GFF + Hairer + II_1 does not park because persona 21's open question (e) is a genuine falsifiable upgrade test.

## 5. Verdict for this pass

**Path verdict: useful only as analogy.** No stochastic-reduction proposal in the surveyed corpus derives parity / chirality breaking from substrate dynamics. The strongest positive content of the path is the II_1 / Connes reframing of "what the observerse projection means" (which connects to syntheses/00b Finding B and is independently valuable), not a derivation of chirality.

**Recommendation for the WRK card:** mark the stochastic-reduction route as **useful only as analogy** with one **named upgrade gate**: persona 21's open question (e). If that question resolves positively, the route earns a re-pass and could be promoted to "remains plausible." If it resolves negatively or remains unresolved after a defined window, the route should be parked.

The route is **not** recommended for closure as "plausible" on this pass. The honest reading is that the stochastic path reframes Witten 1981's question rather than answering it, exactly as persona 11 (e) and the synthesis 00b's convergent verdict already state.

## 6. Six-axis cross-reference (WRK-375)

This proposal touches the following axes of the six-axis specification:

| axis | class drop / movement |
| --- | --- |
| L1 substrate | (g) Stochastic / log-correlated GFF noise class — directly. Also (c) Type II_1 spectral triple extension via the orbit-equivalence persona 13. |
| L2 observer | (a) Finite Turing observer baseline; can extend to (e) QRF if measurement-channel framing is loaded (persona 12). |
| L3 pairing | (a) Cartesian / smooth baseline mostly preserved; persona 12 channel framing optionally drops to a non-cartesian POVM pairing. |
| L4 causal order | (a) Total-order Lorentzian preserved by default; the stochastic dynamics live ON the smooth bundle. Not a causal-set substitute. |
| L5 emergence | Strong activity here: GFF + Hairer + RG framing in persona 21 is exactly L5 = (b) universality class / RG fixed point. The "parity emerges at the RG fixed point" framing is the route's strongest move. |
| L6 coordination loop | (g) Stochastic gradient / RG flow as coordination dynamics — directly. The Langevin / SPDE evolution IS the coordination dynamics. |

The stochastic route is **primarily an L1 + L5 + L6 drop**, with L1 carrying the substrate choice (GFF or II_1), L5 carrying the universality-class / RG-fixed-point framing, and L6 carrying the stochastic-gradient / RG-flow coordination dynamics. L2-L4 are preserved at baseline unless the route is layered with the measurement-channel framing of persona 12.

**Finding to propagate to WRK-375 coordination pass.** L5 and L6 are tightly coupled in the stochastic route (the RG flow IS both the emergence mechanism and the coordination dynamics); the same coupling that WRK-375's draft coordination note already records for the universality-class example. Stochastic-route candidates therefore cannot fill L5 and L6 independently. The six-axis template's note recommending the L5-L6 coupling should be applied here directly.

## 7. Cross-references to other pipeline cards

### 7.1 WRK-376 (no-go-forgetful-image map, #25)

The Nielsen-Ninomiya per-theorem section of WRK-376 has direct stochastic-relevant content: assumption (2) Hermiticity, with Chernodub 2017's non-Hermitian PT-symmetric evasion explicitly cited. The non-Hermitian / open-system / dissipative dynamics class is the natural lattice-side analog of stochastic reduction (an open-system stochastic operator is, generically, non-Hermitian). The no-go-map already records that Chernodub's evasion has "PT-breaking and complex spectra (proof-of-principle, not physical)" — i.e., the same insertion vs derivation problem appears in lattice form: the parity-breaking lives in a hand-installed non-Hermitian / dissipative term.

**Cross-finding for coordination pass.** The stochastic-reduction insertion-vs-derivation pattern documented here in continuum / measure language is the **same structural problem** as the Chernodub non-Hermitian lattice evasion noted in WRK-376's Nielsen-Ninomiya section. Both close honestly on the same insertion failure mode. The no-go-map's "modified-consistency-model is the cleanest evasion" verdict for Nielsen-Ninomiya should be paired with this draft's "II_1 reframing is the cleanest analogy" verdict for Witten 1981 — they are the same structural move (modify the algebra rather than derive from the substrate) in two no-go contexts.

For the no-go-map specifically: the Witten-section "Where the analogy may break" line *"A non-geometric substrate (stochastic, observer-relative, causal-set) is not yet shown to admit a smoothing functor producing exactly the Witten image. This is an open derivation problem; the formal opening exists (syntheses/00b) but the substantive derivation does not."* is now empirically corroborated by this pass for the stochastic case. The forgetful operation `ϕ_smooth` does not exist as a derived map from any stochastic substrate covered in this pass; it would have to be installed as a tuning operation.

### 7.2 WRK-378 (Nielsen protocol-analogy pilot, #27)

WRK-378's load-bearing translation is on-site exact axial symmetry ↔ strong-consistency-without-coordination, with the forgetful operations `ϕ_local` (physics) and `ϕ_onsite` (protocol) being the same functor in two vocabularies. The stochastic-reduction question is **orthogonal** at the assumption level — stochastic reduction works on the substrate of the metric bundle, not on the lattice / protocol — but **convergent** at the failure-mode level. WRK-378's verdict that the CALM ↔ Ginsparg-Wilson bridge characterizes "which observables admit coordination-free / on-site-exact realization" is the lattice analog of this pass's verdict on which observables admit derivation-free emergence from stochastic substrate.

**Cross-finding for coordination pass.** WRK-378's notion of "CALM-monotonic observables" (those that can be evaluated without coordination) maps in physics language to "observables that can be realized on-site exactly." The stochastic-reduction analog is: **observables that can be derived from the stochastic substrate without insertion**. The "without insertion" condition is to the stochastic route what "without coordination" is to the protocol route; both are the load-bearing constraint. The CALM ↔ GW bridge from WRK-378 thus has a natural cousin: **CALM ↔ Witten-derivable observables in stochastic reduction**. This is a candidate predictive bridge worth flagging for a future pass but not load-bearing on this draft.

### 7.3 WRK-375 (six-axis specification protocol, #24)

Already addressed in §6. The stochastic-route axis profile is L1 (g) + L5 (b) + L6 (g), with L2/L3/L4 preserved at baseline. WRK-375's draft coordination note already records the L5-L6 coupling for universality-class candidates; this pass confirms that coupling is also tight for the stochastic route, and the six-axis README should reflect that L5 (b) and L6 (g) are not independently fillable for stochastic-substrate candidates.

### 7.4 Connes spectral-triple research direction (syntheses/00b Finding B; WRK-377 #26)

WRK-377's Type II_1 spectral-triple SM checklist is the most direct extension of the II_1 reframing surfaced here. The stochastic / orbit-equivalence persona 13 motivates a Type II_1 internal algebra; WRK-377 produces the actual checklist of what would need to be built to make that spectral triple SM-compatible. This pass does **not** evaluate WRK-377's checklist on parity specifically — that's a separate evaluation — but flags that **WRK-377 item 3 (KO-dimension 6 mod 8 for Type II_1) is the parity-carrying control item**; the parity derivation question for the II_1 route reduces to whether the KO-dimension constraint is satisfiable in the non-embeddable II_1 regime.

**Cross-finding for coordination pass.** The II_1 route's parity-derivation question reduces to WRK-377 item 3 (KO-dim 6 mod 8 in the non-embeddable II_1 regime). This is a sharper question than the unfocused "does II_1 extension deliver chirality" framing. If WRK-377 item 3 is structurally obstructed, the II_1 reframing's parity content is inserted; if it is satisfiable, the II_1 reframing has a genuine derivation handle. WRK-377 should be informed that this is the parity-load-bearing item from the stochastic / II_1 side; not new information for WRK-377 itself, but a cross-card priority signal.

## 8. What would have to be true to upgrade the path

Concretely:

1. **For Parisi-Wu:** a derivation of a parity-odd drift term from the substrate (not from input). No published candidate.
2. **For GFF / Hairer:** a positive answer to persona 21 (e). Open.
3. **For II_1 / Connes:** a positive resolution of WRK-377 item 3 (KO-dim 6 mod 8 in II_1) plus a structural reason the trace-difference tuning is fixed by the substrate rather than free. WRK-377 already records item 3 as a high-risk control item.
4. **For GRW / CSL / Diosi-Penrose:** a published relativistic extension that delivers parity-breaking from the collapse mechanism, plus engagement of that literature by the GU-repo material. Currently not in this corpus.

A single positive resolution on any of (1)-(4) would upgrade the path from "useful only as analogy" to "remains plausible" for that specific proposal. Until then, the lane verdict stands.

## 9. Final per-proposal verdicts

| proposal | path status (per DoD §5) | upgrade gate | recommended action |
| --- | --- | --- | --- |
| Parisi-Wu | should be parked | derivation of parity-odd drift from substrate | park; do not re-evaluate without a derivation in literature |
| GFF / Hairer / log-correlated | useful only as analogy | persona 21 (e) open question | hold open; re-pass on positive answer to (e) |
| II_1 / orbit-equivalence / Connes II_1 | useful only as analogy | WRK-377 item 3 resolution + tuning fix | track via WRK-377; do not double-track here |
| GRW | literature-silent → park pending literature | published relativistic GRW with parity-derivation | park; not in scope without a literature pass |
| CSL | literature-silent → park pending literature | published relativistic CSL with parity-derivation | park; not in scope without a literature pass |
| Diosi-Penrose | literature-silent → park pending literature | published relativistic DP with parity-derivation | park; not in scope without a literature pass |

**Overall lane verdict:** useful only as analogy, with the II_1 / Connes reframing carrying the lane's actual positive content. Parisi-Wu and the three uncovered collapse models park. GFF / Hairer holds open on a single named gate.

## 10. Honesty contract observed

- No silent strengthening. The "literature-silent" verdicts for GRW, CSL, and Diosi-Penrose are reported as gaps in the surveyed corpus, not as evidence for or against.
- No new physics. All substantive claims about Parisi-Wu, GFF, and II_1 reductions are sourced from persona 11, persona 13, persona 21, and synthesis 00b.
- No claim that the stochastic route is wrong. The claim is only that the surveyed material does not deliver parity-derivation, and the falsification criteria above name what would change that.
- Persona 21's open question (e) is left open — no claim is made about its answer.
- No direct artifact mutation. Cross-findings for WRK-375, WRK-376, WRK-377, WRK-378 are flagged for the coordination pass to consume, not written into related artifacts.
- The path verdict for the WRK card (useful only as analogy) follows DoD §5 categorical options exactly.

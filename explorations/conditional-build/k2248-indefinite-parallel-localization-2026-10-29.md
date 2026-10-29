---
title: "K2248 Indefinite parallel localization has null inherited pairing"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2248_indefinite_parallel_localization_probe.py
---

# K2248 Indefinite parallel localization has null inherited pairing

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: Indefinite parallel localization has null inherited pairing
carrier: finite-rank Hermitian bundle on connected normal fibres with auxiliary positive L2 norm LAYER=toy CHIRALITY=N/A
pairing: inherited indefinite G versus explicitly separate positive h ON=declared_carrier
real_structure: complex conjugation and Hermitian adjoint as specified
grading: normal connection eigenlines or excitation number, not families
action_owner: repository-construction -- explicitly supplied models
target: normal parallel kernel and its inherited form MAP-TYPE=intertwiner
```

## Question and scope

[K2245](k2245-localized-normal-domain-2026-10-29.md) excludes nonzero L2 all-normal-parallel sections for a positive-metric-compatible connection on an infinite-volume fibre, but explicitly leaves indefinite compatibility separate. Here indefinite compatibility permits localized parallel sections, yet under a stated boundedness condition their ENTIRE inherited Gram form vanishes. The dimension bound is sharp on each connected normal fibre. An auxiliary positive norm does not turn that zero form into an inherited positive physical pairing.

This is conditional bundle mathematics, not a construction on the actual raw1920 source operator. No compatibility with its principal/lower coefficients or propagation is claimed. SC-META-53 remains UNCERTAIN; SC-OP-04 ASSERTS candidate operator grammar, SC-OP-05 is UNCERTAIN on rivals, and SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita. No new source assertion or ledger0.263 LT-SM8/LT-GR6b/AC-F1 verdict follows. K2245's supplied raw solution remains unchanged. Layer0 keeps positive normalizability, indefinite pairing, and physical positivity distinct. This is not a chirality or family-count candidate.

## 1. Whole-Gram integrability theorem

Let F be a connected smooth normal fibre with positive smooth measure dmu. Let E have finite rank n, smooth positive auxiliary Hermitian metric h, and smooth nondegenerate Hermitian form G of constant inertia (p,q). Let nabla=partial+A be G-compatible. In a trivialization this means

    partial_a G=A_a* G+G A_a.

Assume C(y)=||G(y)||_h>0 obeys integral_F C(y)^(-1) dmu=infinity. Define K to be the space of smooth sections parallel in EVERY normal direction and square integrable in h,dmu. For any psi,phi in K,

    partial_a(psi*G phi)=0,
    psi(y)*G(y)phi(y)=c,
    |c|/C(y)<=|psi(y)|_h |phi(y)|_h.

Integration and Cauchy-Schwarz force c=0. This proves ALL cross-pairings vanish, not only individual null norms. A bounded C and infinite mu-volume suffice. No flatness assumption is needed: curvature can shrink K but cannot evade this argument.

Evaluation K->E_y at any point is injective by parallel-transport uniqueness along paths. Its image is totally isotropic. In a basis G=diag(I_p,-I_q), projection of an isotropic subspace onto either positive or negative coordinates is injective; hence

    dim K<=min(p,q).                                      (1)

This is a fibrewise statement. Over a tangential base, arbitrary coefficient functions of x can give an infinite-dimensional product-space L2 sector. It is not a bound on the total field Hilbert space. Distributional parallel L2 sections are also locally smooth under the stated smooth coefficients: partial_a psi=-A_a psi bootstraps local Sobolev regularity. The theorem does not cover constraints in only SOME normal directions or a nonparallel differential constraint.

## 2. Sharp indefinite-compatible localized family

On R^d with Lebesgue measure and h=I, put

    G=diag(1,-1), K=[[0,1],[1,0]], A_a=beta y_a K, beta>0,
    v_+=(1,1)/sqrt(2), v_-=(1,-1)/sqrt(2).

K*G+GK=0, so this connection preserves G. The complete parallel family is

    psi(y)=exp(-beta |y|^2/2)c_+ v_+
           +exp(+beta |y|^2/2)c_- v_-.

Orthogonality of v_+,v_- for h shows L2 iff c_-=0. With f=(beta/pi)^(d/4)exp(-beta |y|^2/2), the map z->f v_+ z is an isometry from C into L2(h). Its image is closed, but v_+*Gv_+=0. Use min(p,q) independent hyperbolic pairs and leave unmatched positive/negative directions with trivial connection to attain (1). Unmatched constant sections are not L2. On X times R^d, this gives a closed isometric copy of L2(X;C^min(p,q)), with identically zero inherited G form.

The complement v_- grows. The indefinite connection has not become compatible with the auxiliary positive h. This construction resolves the existence question left open in K2245 without silently identifying its Hilbert norm with the source pairing.

## 3. Consequence for inheritance and quotient proposals

The restriction of the inherited integral pairing to K is zero pointwise, so its integral is zero. Its radical is ALL of K. Quotienting that restricted form by its radical therefore gives the zero space. No nonzero positive inherited state space can be obtained solely by that restriction and radical quotient.

An observation can assign an independent positive form, or another differential constraint/domain/action can select a different space. Those operations change the required bridge and are not forbidden. Pairing with a nonnormalizable growing dual also exits this L2 space; it does not repair the zero inherited form inside K. Nothing here rules out arbitrary indefinite-to-positive physical quotients.

## 4. Sharp limits: density and unbounded relative pairing

Finite volume changes the result: take A=0, constant G and dmu=exp(-|y|^2)dy. Constant sections are L2, and their inherited integral retains inertia (p,q). Choosing a positive subspace requires a further selection; this example shows the bounded-form/infinite-volume corollary can fail when finite volume is allowed; it does not provide that selection.

An unbounded relative form changes it even with Lebesgue measure. Take G(y)=exp(beta |y|^2)G0 and A_a=beta y_a I. Compatibility holds because partial_aG=2beta y_aG. Every exp(-beta |y|^2/2)v is L2(h), while its pointwise G pairing is the possibly nonzero constant v*G0w. Here integral C^-1 is FINITE. The inherited integral generally diverges, so auxiliary normalizability alone does not even define that unbounded form on the whole constrained sector. This is a counterexample to dropping the hypothesis, not a positive inherited Hilbert construction.

More generally, if c is nonzero, the proof supplies the necessary condition integral C^-1<infinity. It is necessary, not sufficient for an arbitrary connection to possess any parallel sections.

## Review and next scientific input

The cheapest structural route settled the full Gram form and sharp rank, eliminating a matrix-by-matrix search over compatible connections in this class. Followthrough supplied a maximal-rank null construction, quotient consequence, finite-density escape and unbounded-form counterexample. Independent review corrected the reciprocal-integral direction and the fibrewise rank scope before acceptance. Source-native application still requires the actual fibre measure, relative G/h growth, constraint owner and propagation on the full raw carrier. A nonparallel constraint or finite-volume geometric density is a concrete next alternative. No claim about source physical positivity changes.

## Reproduction and evidence kinds

Run `python tests/channel-swings/k2248_indefinite_parallel_localization_probe.py`. Default execution recomputes exact finite controls and genuine input faults, then checks report/code/note/dependency hashes. `--write` refreshes the report. Universal proofs are written mathematics independently reviewed internally; finite controls do not prove them. No external-expert, novelty or proof-assistant claim.

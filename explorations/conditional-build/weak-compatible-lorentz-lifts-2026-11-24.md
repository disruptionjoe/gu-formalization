---
title: 'Fixed geometric weak symmetry: complete Lorentz lift and compensation test'
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3; P1 fields/symmetry
tier: T2
expected_delta: Settle a source-to-test implication across the declared class and preserve source-compatible
  countercontrols
actual_delta: The actual compact weak centralizer forces the block Lorentz lift across the declared class.
  Spin-only compensation fails at fixed contraction; moving contraction cancels the defect. No source
  or family-count verdict.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: SOURCE-RELEVANCE-APPLICABILITY
canon_verdict_change: none
class_covered: Every real split-preserving metric Lorentz lift with fixed geometric left-quaternionic
  weak SU2, and full-parent lifts normalizing the same real Clifford-vector space; moving geometry remains
  separate.
premises:
- 'SC-FER-05 and SC-GRP-02/03/06 in lab/sources/source-claim-register.yaml: source product branching,
  geometric weak factor and larger parent gauge arena.'
- 'SA-1/SA-2 and weak-endogenous-grading-2026-11-24.md: soldered lifts and prior branching retained.'
- 'source-weak-action-transport-2026-11-13.md: fixed spin-only versus geometric versus moving-observation
  categories; physical current/domain not chosen.'
source_bridge:
  status: conditional
  reason: The displayed product action supports the block lift; fixed physical symmetry and current/domain
    realization are still conditional. Moving epsilon is source-admitted and is retained as a positive
    control.
kill_condition: An inconsistent lift excludes a source realization only if that fixed geometry, weak action
  and observation are source-required. Source product branching and moving-observation compensation survive
  this test.
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: Source applicability conditions with retained countercontrols
carrier: fullCl14 S128 and raw one-form/scalar carrier with actual observed contraction LAYER=ambient+observed BRIDGE=declared-source-variation-and-observation CHIRALITY=S-FULL-DIRAC
pairing: K95 nondegenerate indefinite Krein pairing; independent density-dual bars ON=declared_carrier
real_structure: K95 quaternionic reality; no transfer to source K77
grading: correlated ambient Omega and prescribed horizontal chi_H kept distinct
action_owner: repository-construction -- source primitive grammar retained; complete physical action and response unselected
target: actual q on one-form/scalar fields MAP-TYPE=contraction
```

program_target: X-P1-P2-P3
tier: T2
expected_delta: Settle source applicability across declared classes
actual_delta: The actual compact weak centralizer forces the block Lorentz lift across the declared class. Spin-only compensation fails at fixed contraction; moving contraction cancels the defect. No source or family-count verdict.

# Fixed weak symmetry forces the block Lorentz lift; compensation has a form-leg cost

Internal T2 result; evidence base `14778ad8a4308d2d88357bba8a81819cedbc3f40`. Root executed the accompanying probes; validation and independent reviews are recorded below.

## Result

For the actual normal weak factor, **every split metric Lorentz lift commuting with that same fixed weak action is the block lift**. This is an all-lift statement, not another comparison of block and endogenous examples. It remains true if a commuting abelian target factor is admitted, and for full parent endomorphisms that normalize the same fixed Clifford-vector realization.

The compensating normal rotation relative to the endogenous lift is therefore fixed: it must remove both the normal **form** action and normal **spin** action. A source-style spinor-only epsilon wrapper does not do that while the Clifford contraction/observation is held fixed. The already-owned moving-Clifford/epsilon law supplies an explicit surviving covariance between observation tensors. Thus the test identifies what the source's physical interpretation must establish; it does **not** eliminate that interpretation.

## 1. Source and scope

SC-GEN-51 ASSERTS ambient-inequivalent representations can agree under subgroup restriction. SC-GEN-56 ASSERTS the opposite-half zero-form/one-form package yields three observed families. SC-GEN-57 ASSERTS the rolled-up 2+1 imposter mechanism. None of these identifies a representation multiplicity with a physical count. The relevant direct representation premise is source eq11.6, which gives the displayed factorization under `Spin(1,3)×Spin(6,4)` (SC-FER-05), alongside the geometric normal weak subgroup of SC-GRP-03. SC-GRP-02 ASSERTS the full U(64,64) parent. SC-GRP-06 ASSERTS that these are geometric rather than independent internal symmetries.

Reused evidence:

- SA-1, `lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md`, already proves the associated bundle is soldered and exhibits the two lifts, differing by δ(X) in the declared normal gauge algebra.
- SA-2, `.../sa2-two-lorentz-source-package-classifier-2026-08-20.md`, already owns the F/Z/16/144 branching, the absence of pure Weyl F submodules on the endogenous graph, and simultaneous-PS obstruction. No branching calculation is repeated.
- `explorations/conditional-build/weak-endogenous-grading-2026-11-24.md` already proves graph-Lorentz plus geometric weak generates the product. No Lie-generation calculation is repeated.
- `explorations/conditional-build/source-weak-action-transport-2026-11-13.md` §1 owns Categories F/G/M, the maximal fixed-q spin-only normal algebra, and the exact moving-q transport law. Those theorems are reused in the compensation test.
- The primary section9 extraction and `source-prescription-current-2026-11-13.md` distinguish primitive metric, epsilon and varpi. Epsilon acts in the spinor gauge representation; at fixed metric it is not an independently supplied active transformation on the cotangent leg.

**class_covered:** connected real Lorentz Lie algebra lifts with prescribed horizontal vector action, fixed nondegenerate H⊕N splitting, fixed geometric weak factor, and simultaneous metric vector/form/spin action. H has signature(3,1); actual trace-reversed N has signature(6,4). The positive6/negative4 reduction may be any maximal-compact placement. Full-parent normalizers of this *fixed* Clifford-vector geometry are covered by §3. Generic moving parent embeddings, changed observation tensors, physical quotient actions and disconnected parity are separate.

**source_bridge:** conditional. The source's displayed product action meets this kinematic condition, but neither the realized fixed physical symmetry nor its weak current/domain is selected by the display. There is no appeal to a general Coleman–Mandula theorem and no assumption that covariance of a moving background equals commutation on a fixed background.

## 2. Complete metric lift theorem

Let `g=so(1,3)` and `N=P⊥Q`, with P positive six-dimensional and Q negative four-dimensional. Let k=su(2)_L act trivially on P and as real left quaternion multiplication on Q. Fix the horizontal identity projection of a lift

    i:g → so(H) ⊕ so(N,K).

Every such Lie algebra homomorphism is `i(X)=(X,φ(X))` for a homomorphism φ.

**Lemma (complete centralizer).**

    z_so(N,K)(k) = so(P) ⊕ sp(1)_R ≅ so(6) ⊕ su(2),
    dimension =15+3=18.                                      (L1)

Proof: a commuting off-diagonal block P↔Q would be a weak intertwiner between a trivial module and Q. Q has no fixed vector, so both blocks vanish. The P block is arbitrary skew. The commutant of left quaternion multiplication on Q is right quaternion multiplication: an intertwiner is determined by its value at1 and satisfies A(q)=q A(1). Skewness for the quaternion norm requires A(1) imaginary, giving precisely right sp(1). Since each diagonal metric block is definite, all matrices in (L1) are also skew for a positive Euclidean form. Thus this centralizer is compact. ∎

**Theorem.** If `[i(g),(0,k)]=0`, then φ=0. Hence the unique lift is

    i_block(X)=(X,0).                                      (L2)

Proof: φ takes values in (L1). A nonzero homomorphism from the simple real algebra so(1,3) is injective. Pulling back the positive invariant form `−tr(AB)` on the compact centralizer would yield a positive invariant form on so(1,3). This is impossible directly: take horizontal matrices K1=E14+E41, K2=E24+E42, J12=E12−E21. They obey `[K1,K2]=J12`, `[K1,J12]=K2`, so Y=K2+J12 is a nonzero +1 eigenvector of ad(K1). Invariance gives `<Y,Y>=<[K1,Y],Y>=−<Y,[K1,Y]>=−<Y,Y>`, a contradiction. ∎

The argument is real-form sensitive. Complexifying first and claiming every map to so(6,C) vanishes would be false. Adding any abelian central target does not help: g is perfect, so its homomorphism to that center is zero. A connected group lift on Spin⁺(1,3) has no additional infinitesimal or continuous central character; discrete/parity extensions are not decided.

This theorem is conjugacy invariant over all supplied maximal-compact P/Q placements. It uses the source's left quaternionic weak factor. If the weak group were the diagonal SU2 in Spin4, Q would be1⊕3. Then P plus the fixed negative line has signature(6,1), its so(6,1) centralizer contains so(3,1), and a nonzero φ exists. This is a contrary representation control, not permission to replace the source weak factor.

## 3. Parent normalizers: what “full U” changes and what it does not

For a fixed faithful irreducible complex Cl14 realization with real Clifford vectors sharp-selfadjoint, suppose a parent generator A_X normalizes the real Clifford-vector subspace:

    [A_X,c(v)]=c(r_X v),

and r_X preserves the H/N split with its H action X. The Clifford relations themselves force r_X to be metric-skew: commuting A_X through `{c(v),c(w)}=2G(v,w)I` gives `G(r_Xv,w)+G(v,r_Xw)=0`. Subtract the ordinary spin lift σ(r_X); the difference commutes with every Clifford vector, hence with End(S), and is scalar. Thus

    A_X=σ(X,φ(X))+λ(X)I.

Lie compatibility makes λ vanish on commutators, hence λ=0 for g. If the lift commutes with the fixed geometric weak action, §2 again forces φ=0. This extends uniqueness to every full-parent lift **normalizing the same vector geometry**, not merely a preselected list of bivectors.

A generic U(64,64) generator can move the Clifford embedding rather than normalize its vector span. The source permits this larger category through epsilon. Such a generator is not included by calling it a normal connection or by imposing the fixed-vector equation above. For example a suitable skew-sharp degree4 Clifford word can commute with the weak factor while its commutator with a normal vector has degree3 rather than degree1. This is an outside-category control, not a constructed alternative physical Lorentz embedding.

## 4. Compensation on the full source carrier

Use the already-owned raw carrier and observation

    E=(V*⊗S)⊕S,
    q(ζ,ν)=(P_Hζ, Γ_Yζ, ν),  ker q=kerΓ_N ⊂ N*⊗S.

Write r=δ(X), t=σ_N(r) with `[t,c(n)]=c(rn)`. All form actions use the metric-identified covector convention consistently.

The endogenous geometric lift has, relative to the block action, the additional normal operator

    T_G(r)=r_form⊗I + I⊗t       on ζ,
           t                    on ν.

Thus **full geometric compensation** `−T_G(δ(X))` gives exactly the block lift on all legs. Clifford covariance gives `Γ T_G=tΓ`, and q transports this geometric action. This is the unique split metric compensation satisfying §2. The negative map −δ is not asserted to be a separate Lie algebra homomorphism. At group level the compensator is U(g)=D(g)⁻¹ relative to the endogenous normal representation D(g); it obeys the conjugation cocycle law U(g₁g₂)=U(g₁) Ad_{D(g₁)}U(g₂), so the combined action is the block representation.

By contrast the source-style **spinor-only compensation** is

    T_F(−r)=−I⊗t on ζ,   −t on ν.

Adding it to the endogenous action leaves

    T_res(r)=r_form⊗I on ζ,  0 on ν.                       (L3)

The residual is real information, not a sign convention. Its commutator with a fixed geometric weak generator is `[r,w]_form`; the full Lorentz family cannot make it vanish because δ is a nonzero Lorentz homomorphism and §2 forbids its image in the compact weak centralizer.

It also fails the fixed-q observation test. From Clifford covariance,

    Γ_N r_form|kerΓ_N = −Γ_N(I⊗t)|kerΓ_N.                  (L4)

The November13 Category-F classification proves that no nonzero normal spin bivector preserves kerΓ_N. Therefore (L4) is nonzero for every nonzero r. No different receiver representation can repair this kernel-invariance failure. On scalar spinors alone, subtracting t does produce the block action; on the full one-form spinor it does not.

This identifies a precise limit of the old “δ belongs to the gauge algebra” escape: it proves availability on the spin factor, not automatic cancellation on the form factor with fixed q. We do not retrospectively attribute the stronger full-carrier assertion to SA-1, whose principal object was the associated spin/gauge bundle.

## 5. Moving epsilon is a surviving transport, not a fixed-q repair

The source's moving Clifford prescription must remain available. For a spinor gauge change U,

    c^U(v)=Uc(v)U⁻¹,
    Γ^U=UΓ(I⊗U⁻¹),
    q^U diag(I⊗U,U)=diag(U,U,U)q.                          (L5)

This is the existing Category-M identity. It includes the observation motion that a fixed-q calculation omits. Infinitesimally, for U with generator −t,

    dotΓ=−tΓ+Γ(I⊗t)=−Γ r_form.

Therefore `dotΓ+ΓT_res=0`: the same form-leg remainder that obstructs fixed q is canceled by the moving contraction. The result is a correctly transported block-labelled receiver along the family, without having supplied an independent active form-gauge transformation.

The finite normal formula makes the distinction transparent. If R is a normal rotation with spin lift S_R, the combined endogenous plus spin-only compensation leaves raw form transformation R but spin identity. With U=S_R⁻¹,

    c^U(Rn)=S_R⁻¹ c(Rn) S_R=c(n).

This is a positive covariance control. It does **not** assert that c, q, the selected weak reduction and the physical current all remain fixed, or that a selected background/domain is invariant. A common change of coordinates preserves brackets of already specified actions; it cannot turn a noncommuting fixed pair into a commuting fixed pair. A field-dependent compensated action on a moving background must instead carry its background/connection transformation and actual receiver/current. The source permits that investigation; the required selected physical action is not supplied by (L5).

## 6. Consequence for the attempted falsification

The endogenous-versus-block choice is no longer an arbitrary list of two examples **inside the fixed geometric weak/metric class**: the block option is uniquely necessary. But the source's product branching already names that surviving option, and its parent gauge arena admits moving compensation. Therefore the test does not falsify SC-GEN-51/56/57 or SC-CHI-01/04.

What moves is a sharpened source requirement: a physical interpretation using the displayed product branching must realize either the full geometric compensation, or the moving-Clifford/observation compensation with its weak current and physical domain transported, or a separately typed realization outside this fixed metric class. Source-style spin-only cancellation at frozen q is excluded. No action, potential, source operator, family count, index, observed generation or global physical quotient is constructed.

Next useful discriminator is the actual source weak/luminous current and its response under the admitted moving realization. Repeating SA-2 branching, the imposter dimension count or the old provenance-separation calculation would not advance this bridge.

## Validation boundary

The executed exact probe checks the complete 45-variable metric centralizer (dimension18), quaternion actions, the horizontal boost eigenvector, the diagonal-SU2 contrary control, and explicit Clifford fixed-q versus moving-q identities. The universal statements rest on the displayed proofs. Root executed 23 exact checks and confirmed rejection of three deliberately incorrect variants. Independent mathematical and hostile reviews accepted the written proofs.

## Evidence and verification

- [GEOMETER-VS-PHYSICS-OBJECTS.md](../../GEOMETER-VS-PHYSICS-OBJECTS.md)
- [source-claim-register.yaml](../../lab/sources/source-claim-register.yaml)
- [conditional-physics-ledger-v0.263.json](../../lab/process/conditional-physics-ledger-v0.263.json)
- [source-relevance-wave.json](../../lab/process/source-relevance-wave.json)
- [2026-11-24-source-relevance-wave-review.md](../../lab/process/hostile-reviews/2026-11-24-source-relevance-wave-review.md)
- [source-prescription-current-2026-11-13.md](source-prescription-current-2026-11-13.md)
- [source-weak-action-transport-2026-11-13.md](source-weak-action-transport-2026-11-13.md)
- [weak-endogenous-grading-2026-11-24.md](weak-endogenous-grading-2026-11-24.md)

Exact probes validate the finite identities and contrary controls; the written arguments supply the quantified statements. Internal agent review is not external scientific certification. These results do not select a physical spectrum, a family count or an empirical prediction.

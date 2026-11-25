---
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T2
expected_delta: Construct one explicit action and geometric external datum, with actual variations and
  tested inference limits.
class_covered: One K95 local classical reconstruction on a declared relatively compact metric-bundle chart;
  full Dirac zero/one-form fields and independent dual rows; no whole-C theorem.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-OP-05
- lab/sources/source-claim-register.yaml#SC-GEO-55
- explorations/conditional-build/source-premise-custody-2026-11-25.md
- explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md
source_bridge:
  status: conditional
  reason: Source-shaped ingredients are completed by explicitly declared product, dual-row, frame, domain
    and boundary choices. No physical weak-chirality/index receiver or source uniqueness is proved.
kill_condition: An inconsistency closes only this chosen reconstruction; physical acceptance requires
  a stationary background, native observed receiver and positive physical domain.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
title: Action-first variations and tests of the constructed external datum
actual_delta: True bosonic and four-field Euler/current identities, frame covariance, a smooth balanced-charge
  connection and the remaining observation/domain failure are stated and checked without a physical verdict.
---

# Action-first variations and tests of the constructed external datum

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Construct one explicit action and geometric external datum, with actual variations and
  tested inference limits.
actual_delta: True bosonic and four-field Euler/current identities, frame covariance, a smooth balanced-charge
  connection and the remaining observation/domain failure are stated and checked without a physical verdict.
```

```gu-typed-objects
result: Action-first variations and tests of the constructed external datum
carrier: full Dirac one-form plus zero-form, with independent dual rows LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=S-FULL-DIRAC
pairing: Krein H and metric-form pairing; independent complex dual rows ON=full_Dirac_field_module
real_structure: K95 complex spinor construction with U64,64; no K77/quaternionic transfer
grading: auxiliary form-shifted Clifford grade only; boundary Krein splitting is not physical chirality
action_owner: repository-construction using source-print ingredients
target: coupled local variational action and external boundary connection MAP-TYPE=contraction
```

## 1. Action variation, not an endpoint substitution

Use the [fixed candidate](source-action-external-datum-candidate-2026-11-25.md). For clarity set B=A0, T=T_hat and define Φ_B=*^{-1}S_0, where the inverse star includes the signature/degree sign; then the bosonic pairing is the declared indefinite form pairing. Freeze geometry for this partial variation and put

    Fbar=F_B+(1/2)D_BT+(1/3)T²,
    L_T v=(1/2)D_Bv+(1/3)(v∧T+T∧v),
    M_T b=D_Bb+(1/2)(b∧T+T∧b),
    Q=Φ_B^† T.

The actual interior derivatives are

    E_T^B=Φ_B(Fbar)+L_T^†Q+T,
    E_B^B=M_T^†Q.

Formal adjoints include all coefficient and density derivatives. The local boundary contribution, under the chosen form Green convention, is

    ∫_∂U b(Q^{ai}, δB_i+(1/2)δT_i) dΣ_a.

Here dΣ_a is the oriented coordinate density flux, so no unit-normal sign or nonexistent null unit normal is hidden. No well-posedness follows from this formal flux identity.

In general E_T^B is **not** Φ_B(F_A)+T. The source prints both the path functional and that endpoint; equality is an additional Helmholtz/cyclicity identity, previously found false for selected full-domain contractions. This candidate is action-first and retains the actual E_T. It also does not add I2B=residual-square: δ||F||²=2 DF^†F, with possible stationary points F≠0. The familiar control F(x)=(x,1) makes that distinction exact.

At fixed T=0, I1B vanishes identically along the correlated locus Ahat=A0[g]. Its Hessian restricted to that locus is zero. The pure-g Hessian at fixed independent Ahat need not vanish because δT=−δA0; the mixed Hessian and elimination problem remain. No Einstein kinetic term is established merely by restricting the action to T=0. Stationarity still requires Φ_B(F_A0) plus matter current to vanish. Neither a flat base nor zero fermions proves this. The proposed nonzero-charge field configuration is off shell.

## 2. Four independent fermion variations and current

For D=M^a∂_a+V, independent bar variation gives Dχ=0. Independent unbarred variation gives the dual-row equation

    D^t barχ=−μ^{-1}∂_a(μ barχ M^a)+barχ V=0,

with the appropriate Grassmann left/right sign convention if used. The boundary concomitant is barχ M^a δχ dΣ_a. Omitting ∂M or ∂log μ changes this equation. No formal self-adjointness assumption is needed, and setting barχ=χ†H before varying is a different field space.

For a compatible connection variation a, hold metric, Clifford tensors and density fixed. Since δ_aδ_A ζ=−i_aζ,

    δ_aD(ζ,ν)=(C(a∧ζ)+aν, i_aζ),
    J_F[a]=Re ∫[barζ C(a∧ζ)+barζ aν+barν i_aζ] μ.

These are the three primitive current types from the source grammar. Their normalization and exact contractions belong to this chosen completion. A separate −T·J term would double-count/change the current. In the independent dressed variables (B,T), Ahat=B+T, so the same J enters E_T and E_B; no matter term is added by hand.

The metric equation is the functional chain rule on the base:

    δ_g S = δ_explicit(G,star,Φ,C,H,μ) S
           + <E_B^tot−E_T^tot, (D_g A0)[δg]> + boundary terms
         = δ_explicit S + <E_B^B−E_T^B, (D_g A0)[δg]> + boundary terms.

Here the primary variables are (g,A,ε,χ_ref,barχ_ref): at fixed A,ε the dressed Ahat is fixed, so δB=δA0 and δT=−δA0. The two identical J_F terms cancel in this chain, while metric dependence of C,δ,H and μ remains in δ_explicit S. In coordinates (g,T_hat) instead, δAhat=δA0 and the chain term is <E_B^B+J_F,δA0>. These are different off-shell metric derivatives related by the connection Euler equation, not competing formulas to mix.

After integration by parts and fibre integration this gives a base tensor density E_g(x). It includes the variation of the horizontal splitting and A0[g]. It is not the Euler derivative for an independent ambient metric G(y), and not merely a conventional stress tensor. The exact functional defines it; its full expanded PDE, derivative-order degeneracies and boundary realization have not been solved or certified for class C.

## 3. Dressing identity and its actual Noether scope

The composition identity (A0^k)^(k^{-1}εh)=(A0^ε)^h proves B transforms as a connection. It also proves Ahat transforms only in the reference frame. In a fixed reference frame the right h redundancy is

    δA=D_A ξ,      δε=εξ,      δχ_ref=0,

and leaves Ahat unchanged. The ε Euler equation is therefore dependent on the A Euler equation through the corresponding formal covariant adjoint. This is an actual action-derived Noether identity for the compensator parametrization, not an independent physical field equation. At T=0, the right-frame action on T is [T,ξ]=0: it supplies no spurious D_Bξ distortion column. This respects the K1127 correction.

It does not prove the source's complete active tilted symmetry at held background/observation data. Moving all frames and Clifford tensors establishes covariance; the physical constraint algebra, gauge orbit and BV properness still need an active definition.

## 4. Boundary datum calculation and exact ceiling

Write α=U_k^{-1}dU_k, so dα=−α². Then A=fα gives

    F=f' dr∧α+(f²−f)α².

The angular manifold has dimension13, so the only top-degree contribution to tr F^7 contains one dr. Cyclic trace gives

    tr F^7=7 f'(f²−f)^6 dr∧tr α13.

The beta integral and the standard odd Chern character give charges(k,−k) relative to the supplied boundary framing and J splitting. The full ordinary Chern character sees sum0. A gauge-invariant physical receiver must therefore genuinely distinguish the supplied subbundle data; it cannot recover3 from the total polynomial alone.

This is an actual connection attachment, unlike a proposed ε extension. It demonstrates a nonempty smooth classical configuration space with external integer data. It does not demonstrate a nonempty **solution** space with three massless observed families, and does not certify the action-class width witness.

## 5. The chosen kinetic symbol has an explicit inverse off the null cone

For a covector ξ, write cξ=γ^aξ_a, Γζ=γ^aζ_a, iξζ=G^{ab}ξ_aζ_b and q=G^{-1}(ξ,ξ). The chosen operator has principal symbol

    σξ(ζ,ν)=(cξζ−ξΓζ+ξν, iξζ).

If q≠0, its inverse on (r,s) is explicit:

    w=(iξr−cξs)/q,
    ζ=cξ(r−ξw)/q,
    ν=(2iξr−cξΓr)/q.

Clifford anticommutation gives iξζ=s and Γζ=ν−w, hence the first equation equals r. This verifies nondegenerate first-order kinetic data on noncharacteristic covectors for the full chosen carrier. It is not an ellipticity statement on the real K95 cotangent space: null characteristics remain. It supplies neither a positive physical Hamiltonian nor well-posed multi-time evolution, and does not cure observation nonclosure. The native128-matrix vector control checks this identity at a mixed-sign non-null covector; the displayed Clifford proof owns the general statement.

## 6. First substantive obstruction: literal observation still does not close

The candidate has not evaded the previously proved off-shell non-autonomy of source literal observation. In a frozen flat-symbol chart, take ν(x,y)=y^a s with ζ=0 and a normal coordinate y^a, at the observing section y=0. Then q0χ=0, while the normal derivative enters the ambient one-form equation. A five-slot equation trace may discard that particular normal output, but choose instead a normal derivative of ζ_H: C dζ has horizontal component γ^a ∂_aζ_H, which can be nonzero. Thus q0χ=0 does not imply q0Dχ=0.

There is no D_obs satisfying q0D=D_obsq0 on the unrestricted first-jet class. This is an applicability check using the already owned obstruction, not a new source kill. Solving the bulk equations and defining observables by q0 remains meaningful; deriving an autonomous observed equation requires restrictions/constraints or an enlarged receiver. H7 regularity repairs trace boundedness, not this algebraic mismatch.

The external charge does not fix that mismatch or supply a physical weak grading. In particular, assigning the ±Krein blocks to observed/hidden sectors would be an extra map, not a consequence of their opposite charges. The source's balanced-total claim concerns a specified chiral grading, not this Krein decomposition.

## 7. Acceptance and next tests

The candidate passes local type, frame and variational bookkeeping at the scope of the explicit formulas and exact controls. It fails to deliver an autonomous literal-observation operator on unrestricted jets, reusing a known result. It has no established stationary charged background, native global-end attachment, positive physical quotient or integer-index receiver. Those are substantive limitations of this attempt, not unspecified requests for a source to do all the work.

Useful tests of this fixed candidate are: solve or exclude a stationary charged background under its actual Eulers; identify a source-compatible solution/constraint domain where literal observation has a closed physical meaning; then test the boundary charge against that realized operator's index or spectrum. No claim that the Bott datum alone settles the index, that a positive Euclidean comparator transfers, or that a fresh coefficient search is authorized by this artifact.

Exact controls: `tests/program-focus/source_action_datum_probe.py`. Review and the verified-versus-physical boundary: `lab/process/hostile-reviews/2026-11-25-source-action-datum-review.md`. No Lean claim is made for this T2 construction; the actual infinite-dimensional Eulers/topology are written derivations with primary references and independent specialist review.

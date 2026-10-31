---
title: "K2354 Actual mixed Euler coefficients and transverse nonclosure"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2354_native_mixed_euler_slice_probe.py
---

# K2354 Actual mixed Euler coefficients and transverse nonclosure

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2354
carrier: four real time-dependent selected Cl(7,7) one-form components on a flat chart LAYER=toy CHIRALITY=N/A
pairing: scalar Clifford trace with exterior Hodge form ON=declared_carrier
real_structure: real parameters; complex Hilbert structure only for quantum channels
grading: internal Clifford parity separate from exterior degree
action_owner: repository-construction -- fixed-geometry selected I1 transgression backend with B=0
target: explicit auxiliary matrix and native off-slice consistency tests MAP-TYPE=evaluation
```

## Result and backward demand

[K2351](k2351-mixed-parity-auxiliary-reduction-2026-10-30.md) gives a general nonlinear even-field reduction and one native cubic coefficient. This note evaluates an actual two-even/two-odd selected-Clifford slice, its derivative coefficients and reduced odd Euler equations. It also constructs restricted stationary solutions and explicitly tests full transverse equations. A smooth restricted orbit crosses its one-line auxiliary singularity, while a rational four-field stationary configuration fails the native full Euler test. Additional transverse rows prove that the zero field is the only full fixed-geometry stationary field within this real four-component flat slice at nonzero kappa. This is not a general GU no-go.

The demand is the actual stationary background and common domain needed before the physical-response continuation fromK2345/48. This is a concrete consistency discriminator on the existing action convention, not a curved-background solution or metric/epsilon variation. SC-ACT-01 ASSERTS I1 and SC-GEO-55 ASSERTS connection displacement; the selected fixed flat B=0 chart and Cl(7,7) implementation remain repository choices. Source, ledger0.263 GR6b/SM8, physical quotient, prediction and canon remain unchanged. No I2 Hessian is imported.

## Actual native four-component density

Use the K77 backend with Shiab tuple(comm,symi,symi), its fixed14-dimensional real metric, oriented exterior algebra and scalar Clifford trace. Let t=x^0. Define

    E=e(t) dx0 gamma01 + h(t) dx1 gamma01,
    O=x(t) dx1 gamma1 + y(t) dx1 gamma0.

Other field components are set to zero only for this restriction; variations outside it remain allowed in the original theory. Pairing the full selected action directly yields

    L=kappa(e^2-h^2+x^2-y^2)/2
       +e y' +h x' -(4/3)e^2 x -(4/3)e h y.               (1)

The companion probe computes EVERY4x4 mass/derivative tensor entry and4x4x4 ordered cubic entry from the backend; it does not merely encode(1). For basisV_i, D_ij=P(V_i,S(dt wedge V_j)), M_ij=P(V_i,*V_j), C_ijk=P(V_i,S(V_j wedge V_k)). The factors1/2,1/2,1/3 in the native action reproduce(1). All scalar coefficients lie in the rational component of the backend's exact pair representation.

On a local interval with compactly supported variations, the restricted Euler equations are

    (kappa-8x/3)e-(4y/3)h+y'=0,
    -kappa h-(4y/3)e+x'=0,
    kappa x-(4/3)e^2-h'=0,
    -kappa y-(4/3)eh-e'=0.                               (2)

The full-field Euler system contains more equations. Boundary terms are(e delta y+h delta x); compactly supported variations remove them, while a global problem must retain them. The transverse coordinates can be treated locally or with test-function densities; no divergent infinite transverse-volume action is asserted.

## Evaluated regular-stratum elimination and principal coefficient

Set a=kappa-8x/3,

    A=[[a,-4y/3],[-4y/3,-kappa]], b=(y',x'),
    Delta=det A=-kappa a-16y^2/9.

On Delta!=0,

    e*=[kappa y'-(4y/3)x']/Delta,
    h*=-[a x'+(4y/3)y']/Delta,
    Leff=kappa(x^2-y^2)/2
         -[a(x')^2+(8y/3)x'y'-kappa(y')^2]/(2Delta).       (3)

The actual reduced odd equations are

    kappa x-(4/3)(e*)^2-(h*)'=0,
    -kappa y-(4/3)e*h*-(e*)'=0.                           (4)

All derivatives in(4) differentiate A,Delta and the field velocities. Substitution into the original restricted system proves equivalence on this regular stratum; the probe independently variesLeff to verify it. The matrix multiplying(x'',y'') is

    P=Delta^-1 [[a,4y/3],[4y/3,-kappa]], det P=1/Delta.     (5)

This is a time-only field-space principal coefficient, not a spacetime characteristic cone, hyperbolicity theorem or physical positivity statement. It has been derived rather than inferred from a scalar Schur analogy. A zero coefficient in a one-dimensional restriction need not make the full even matrix singular: at kappa=1,x=3/8,y=3/4, a=0 butDelta=-1 and A=[[0,-1],[-1,-1]]. The coupling repairs that restricted degeneracy. Neither invertibility nor a zero determinant of this two-dimensional restricted block decides invertibility of the full even-field operator. Conversely genuineDelta=0 branches cannot be discarded by the regular formulas.

## Restricted orbit, singular crossing and first transverse test

First restrict further to h=0 before variation and keep onlye,x,y. For kappa>0 the three Euler equations reduce to

    x=4e^2/(3kappa), y=-e'/kappa,
    e''=kappa^2e-(32/9)e^3.

They admit the exact local/smooth orbit

    e=(3kappa/4)sech(kappa t),
    x=(3kappa/4)sech^2(kappa t),
    y=(3kappa/4)sech(kappa t)tanh(kappa t).                 (6)

At sech^2(kappa t)=1/2 the scalar coefficient kappa-8x/3 vanishes, yet(6) is smooth; also y'=0 there, as the algebraic equation requires. This is a restricted stationary orbit, not evidence for full singular stationary solutions. The omitted h-equation is the ACTUAL native transverse row

    R_h=x'-(4/3)ey=4ee'/kappa,

which is nonzero wherever e e'!=0. Thus the pulse fails before any global/domain or physical interpretation. At a point with tanh(kappa t)=3/5,sech(kappa t)=4/5 andkappa=1, the residual is-108/125. This supplies a concrete repair test for the tempting singular-crossing solution instead of promoting a reduced ODE solution to the full action.

## Genuine four-field singular stationary counterexample

The full four equations(2) still do not close the native field tangent. Take constant

    kappa=4, e=h=x=3, y=-3.

All four restricted Euler equations vanish, and A=[[-4,4],[4,-4]] is singular. This is a rational singular stationary point of the restricted model, retained by the original equations although eliminated by(3). Test the missing odd field Z=dx0 gamma0. The full native Euler value, computed BEFORE restriction, is

    R_Z=kappa P(Z,*T)
       +[P(Z,S(T wedge T))+P(T,S(Z wedge T+T wedge Z))]/3
       =12 !=0.                                         (7)

No derivative term remains at these constant fields andB=0. The equally direct Z=dx0 gamma1 andZ=dx2 gamma2 controls also give12. Therefore this exact restricted stationary point is NOT a stationary native configuration. These rows are genuine native Clifford computations, not a polynomial surrogate. A nonzero row suffices to reject this candidate; no complete full-rank or class-exhaustion statement follows.

## Exact closure test for the whole four-field ansatz

The same backend gives, for arbitrary smooth real time-dependent fields,

    R_(dx0 gamma0)=4h^2/3,
    R_(dx2 gamma2)=h'+4y^2/3,
    R_(dx2 gamma12)=-4(ex+hy)/3,
    R_(dx2 gamma02)=-x'.

If a field confined to this ansatz were stationary under ALL fixed-geometry native translations, the first row forces h identically zero. Thus h' is zero and the second row forces y identically zero. The third gives ex=0. The restricted x equation gives kappa x=4e^2/3; for kappa!=0, multiplication by e implies e^3=0, hence e=0 and x=0. Conversely T=0 is translation-stationary on the declared flat B=0 background. Therefore the zero field is the only such full stationary field within this slice. The kappa=0 branch is not covered. This is a local exact exclusion of the named real ansatz, not a complete mixed-grade, curved-background, metric/epsilon or physical-domain theorem. It eliminates further searches for a nonzero fixed-geometry vacuum inside precisely this four-field family.

## Evidence and next condition

The probe reconstructs(1) from native tensors, differentiates all equations, evaluates the regular inverse and full derivative chain, verifies the pulse and both singular phenomena, and computes the omitted native rows directly. Controls remove cross coupling, freeze denominator derivatives, discard singular solutions or suppress transverse receivers and show the resulting wrong conclusion. Universal reduction statements are analytic proofs; finite exact computations certify their specified coefficient examples. No arbitrary low-grade truncation is promoted to a consistent truncation. Next needs a closed native tangent ansatz or the full coupled mixed equations on the curved geometry with boundary/domain conditions; these explicit failed candidates should not be requeued as stationary backgrounds.

---
title: "K2369 Nonsymmetric grade-one fields do not repair the selected curved action"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical evidence; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2369_nonsymmetric_native_derivative_probe.py
---

# K2369 Nonsymmetric grade-one fields do not repair the selected curved action

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
result: K2369
carrier: all real endomorphism-valued grade-one translation fields on the K2345 metric LAYER=toy CHIRALITY=N/A
pairing: nondegenerate metric and selected scalar Clifford trace ON=declared_carrier
real_structure: real Cl(7,7), metric adjoint, including null and nonsemisimple endomorphisms
grading: Clifford grades, tangent indices and symmetric/skew decomposition are distinct
action_owner: repository-construction -- fixed geometry and epsilon, LC reference, selected comm/symi/symi I1
target: full grade-one translation stationarity and independent transverse-grade obstruction MAP-TYPE=evaluation
```

## Result and scope

[K2366](k2366-curvature-codazzi-rigidity-2026-10-31.md) excludes symmetric grade-one fields. Here the same conclusion is proved for every smooth grade-one field T_i=A_i^j gamma_j, with arbitrary real A, on the actual K2345 metric. No diagonalizability, non-nullness, sign of kappa or symmetry of A is assumed. The proof combines the full derivative-adjoint equation with the nonsymmetric cubic equation, curvature integrability and K2366's already established Codazzi rigidity.

A separate transverse grade-five equation forces the skew part to have rank at most two on any Levi-Civita geometry with the same parallel Clifford/Hodge data and selected action. A nonzero flat null-skew stationary field supplies a genuine escape on changed geometry. Thus this is not a universal grade-one exclusion, a mixed-grade exclusion or GU falsification.

The backward demand is a stationary receiver background for the matter/light inverse. SC-ACT-01 and SC-GEO-55 ASSERTS retain their source meanings; SC-ACT-06 ASSERTS its Euclidean rich-moduli claim, not this selected indefinite reconstruction. SC-META-56 DISAVOWS requiring an odd action as a prerequisite to the graded-IG claim; none is imposed. Source polarities and ledger0.263 remain unchanged. Independent metric/epsilon variations, full mixed fields and common-domain/observation inputs remain open.

## 1. Derive the full nonsymmetric operator

Lower the second index of A with g and decompose A=S+K, S*=S, K*=-K. All traces below are endomorphism traces. The selected Clifford action's cubic scalar density is

    L3=4e3(S)+(2/3)tr(S)tr(K²)-(4/3)tr(SK²).

This follows without assuming an indefinite spectral theorem. Metric-invariant cubic contractions of three rank-two tensors are traces of three cycles: the three symmetric invariants combine in 4e3(S), while the two extra invariants are trS trK² and trSK². Odd-K contractions vanish by transpose; no rank14 epsilon contraction occurs. The known symmetric result fixes 4e3(S); two native mixed coefficients fix the remaining constants. For simple spacelike K=e0 wedge e4, S=P0 gives L3=0 and S=P5 gives L3=-4/3. Polynomial identity extends the symmetric result from its open diagonalizable set to arbitrary self-adjoint S. The probe also checks noncommuting S,K and negative-signature cases directly, so this is not a reuse of the invalid formula 4Newton2(A).

With pairing tr(delta A* C), differentiation gives

    C_sym=4(S²-trS S+e2(S)I)+(2/3)trK² I-(4/3)K²,
    C_skew=(4/3)(SK+KS-trS K).

The first-order derivative Euler, including its formal adjoint, is entirely grade two:

    E_i;jk=2(nabla_j S_ik-nabla_k S_ij)+g_ik q_j-g_ij q_k,
    q_j=nabla^l A_lj-nabla_j tr A.

It is not Codazzi(S) alone. For pure skew fields the derivative equation only requires div K=0. Invariant index contractions and exact native coefficients determine this expression; scalar or grade-four derivative receivers vanish by the selected Shiab grade rules. Those rules also show cubic receivers have grades one and five only. Curvature and mass have grade one, so equations of different grades cannot cancel.

## 2. Odd equations force the symmetric part to commute with Ricci

Write t=trS and let G=Ric#-(R/2)I denote the Einstein endomorphism, distinct from the scalar action density. The grade-one equations are

    -2G+kappa S+C_sym=0,
    kappa K+(4/3)(SK+KS-tK)=0.                 (1)

The skew equation gives SK+KS=(t-3kappa/4)K. Multiply it on the right and left by K and subtract: [S,K²]=0, with no division by K or kappa. Commuting the symmetric equation with S then gives [Ric#,S]=0. This remains valid at nilpotent, rank-deficient or zero K and kappa=0.

## 3. Close the derivative integrability, then use the actual metric

Regard S as a tangent-valued one-form. E=0 is d_nabla S=(1/2)Id wedge q. Applying d_nabla gives

    R wedge S=-(1/2)Id wedge dq.

Contracting the vector output with the first form slot gives the Ricci commutator on the left: the middle curvature trace vanishes because S is self-adjoint. On the right the contraction of Id wedge dq is (n-2)dq. Since n=14 and [Ric#,S]=0, dq=0. Locally q=df, hence S+(f/2)I is Codazzi: d_nabla(fI)=df wedge Id=-Id wedge df. K2366's actual-metric theorem therefore forces S=aI pointwise. No global exactness of q is needed; local patches cover the chart.

This is why a co-closed skew field is not a repair by itself: the independent algebraic equations force the missing integrability needed to reduce S.

## 4. Two independent final obstructions

For S=aI, the symmetric equation becomes

    -2G+[kappa a+312a²+(2/3)trK²]I-(4/3)K²=0.  (2)

On the actual metric G has eigenvalues21/4 and15/4 with multiplicities5 and9, on nondegenerate orthogonal eigenspaces W and N. Equation(2) expresses G as a scalar combination of I and K², so K commutes with G and preserves both eigenspaces. Its restriction to each odd-dimensional nondegenerate space is skew-adjoint, hence singular (detK=det(-K*)=-detK). Equation(2) also makes K² scalar on each eigenspace. Singularity forces each scalar to zero. Then(2) would require the distinct Einstein eigenvalues to be equal, a contradiction. This proof includes null/nonsemisimple K.

Independently, the grade-five cubic covector, with Ktwo=sum_(j<k)K_jk e^j wedge e^k, is proportional to

    (8/3)e_i^flat wedge Ktwo wedge Ktwo.        (3)

Its first cubic term supplies this; the cubic adjoint cannot pair a grade-five receiver back with grade-one T. The only metric-invariant quadratic five-form expression is metric insertion into the full alternation of A tensor A, which removes S and gives Ktwo wedge Ktwo. The coefficient is fixed by native K=e04+e56. If all receivers vanish, Ktwo wedge Ktwo=0, hence rankK<=2 over the real field, including null forms. Equation(2) would then equate a matrix of rank at least5, namely -2G+cI, to rank-at-most2 K², also impossible. This transverse test is useful independently of the curved proof and prevents accepting restricted grade-one Euler roots while discarding grade-five receivers.

## 5. Genuine escapes and evidence

On a flat (7,7) chart with kappa=0 choose constant K=u wedge v for independent orthogonal null covectors u=e0+e1, v=e4+e10. Then K!=0, rankK=2, K²=0, trK²=0 and Ktwo wedge Ktwo=0. Derivative, curvature, mass and both cubic grades vanish: this is a nonzero full translation-stationary field for the changed flat geometry. It rejects an invalid positive-definite or universal extension. K2360's changed parallel-product geometry also retains its earlier symmetric stationary witness.

The companion evaluates actual selected Clifford contractions, tests nonsymmetric derivative coefficients and both cubic gradients, computes exact rank/null controls and checks the integrability/commutator algebra. Universal conclusions rest on the invariant-contraction and differential proof, not finite samples. No proof assistant, external-expert or novelty certification is claimed. The next actual-metric stationary construction must include Clifford grades beyond one or change an explicit geometry/action premise and recheck all receivers; merely adding an antisymmetric grade-one tensor is now settled for this model.

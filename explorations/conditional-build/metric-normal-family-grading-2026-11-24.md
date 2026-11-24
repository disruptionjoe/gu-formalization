---
title: 'Metric-normal family: exhaustive observation and horizontal-grade obstruction'
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T1
expected_delta: Settle the declared metric connection family and compare grading laws
actual_delta: 'The entire 910-dimensional space of metric normal-connection values in R6-metric-normal-coherent is classified: full
  observation descends exactly on a 64-dimensional family, and horizontal-grade oddness there forces the
  native nonzero shape to vanish. Thus no metric normal extension repairs this horizontal realization.
  A distinct ambient-correlated grading survives the same metric-spin operator and admissible observation.
  No GU/classC/effective-chirality exclusion follows.'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: R6-METRIC-NORMAL-COHERENT-HORIZONTAL-GRADE
target_claim_verdict: excluded in declared family; distinct ambient grade survives
canon_verdict_change: none
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
result: Exact metric-normal observation class and distinct grading verdicts
carrier: K95 fullCl14 S128; raw E1920; observed6S768; hidden1152 LAYER=ambient+observed BRIDGE=declared-coherent-jet-observation-quotient CHIRALITY=S-FULL-DIRAC
pairing: nondegenerate indefinite metric and compatible Krein pairing ON=declared_carrier
real_structure: quaternionic C; ambient Omega C-even; horizontal chi_H C-odd
grading: ambient Omega skew-sharp involution versus prescribed horizontal chi_H
action_owner: repository-construction -- held exterior zero-SE two-channel operator
target: actual contraction q=(P_H,Gamma_Y,nu) MAP-TYPE=contraction
```

program_target: X-P1-P2-P3
tier: T1
expected_delta: Settle all metric-normal repairs of held horizontal-grade realization
actual_delta: Universal named-family exclusion with distinct ambient grading survivor; no source/class verdict

# All metric normal extensions: quotient classification and horizontal-grade obstruction

## 1. Fixed and variable data

Retain H(3,1), actual trace-reversed N(6,4), full faithful complex Cl14 spinor S128, raw E1920, actual q=(P_H,Gamma_Y,nu), K=ker Gamma_N, and observed six-spinor receiver. Keep the natural two-channel exterior operator, c0=-a/12, a,e,g nonzero, SE=0 and the existing weighted formal adjoint with grad f=Hmean. Tangential B_X is the full coherent split correction. Allow every metric B_n in so(H+N) at the section and use the corresponding coherent normal jets D'_n=0.

All normal extensions may be written uniquely

`B_n X=A_n X+M_n X`,
`B_n m=-M_n^dagger m+C_n m`,

with A_n in so(H), C_n in so(N), and M_n:H→N. The pointwise unconstrained space has dimension10·91=910. No naturality restriction is used to manufacture a no-go: this is a superset of the natural metric-induced choices. The source's larger spin-parent connection need not be in this set.

The coherent tangential operator already descends through q and is odd for its previously forced horizontal receiver grade. The full remaining difference is the owned identity

`V_B(zeta,nu)=(Phi[zeta composed T_B], g zeta(w_B+grad f))`.

## 2. Exhaustive quotient-admissibility theorem

**Proposition.** In this family, `q V_B|K=0` if and only if there are arbitrary A_n∈so(H) and one horizontal covector ell such that

`B_n X=A_n X+ell(X)n`,
`B_n m=-K(n,m)ell#`.                                      (N1)

Thus C_n=0, and the admissible pointwise normal-extension space has dimension `10·6+4=64`. This is an exhaustive classification of the declared metric normal values, not of all source connections, lower completions, jet prescriptions or actions.

**Proof, first NW row.** On hidden z, write `F=zeta composed T_B`. Since `Gamma Phi=(L/2)Gamma C`, with L=2a+14c0=5a/6 nonzero, full q-closure implies Gamma C(F)=0. Its horizontal NW row then reduces to a C_H(F)=0. For each X∈H,

`C_H(F)(X)=sum_r eta_r c(n_r) z(M_(n_r) X)`.

Set L_X(n)=M_n X. The displayed map annihilates ker Gamma_N iff it factors through the surjective Gamma_N. Comparing coefficients gives an endomorphism Q_X with

`c(L_X^dagger n)=Q_X c(n)` for every n∈N.             (N2)

Using one nonnull n in (N2) shows Q_X has only pure-normal Clifford degrees0 and2. Write Q_X=lambda I+beta_2. For Q_X c(n) to have only degree1 for every normal n, beta_2 wedge n=0 for every n. Since dim N=10>2, independent Clifford blades force beta_2=0. Faithfulness then gives L_X^dagger=lambda(X)I; equivalently M_n X=ell(X)n. Linearity makes ell a single horizontal covector.

**Proof, normal block.** With this mixed form, its contribution to the hidden total-Gamma row vanishes because it factors through Gamma_N. The remaining row comes from normal torsion `C_n m-C_m n` and has pure-normal bivector coefficients. Annihilation on ker Gamma_N again factors it as `Q c(n)`. Multiplication by a nonnull c(n) shows Q has pure-normal degrees1 and3. The degree0 part of Qc(n) forces its vector part to pair to zero with every normal vector; the degree4 part forces its3-form part to wedge to zero with every normal vector. Nondegeneracy and dim N>3 force Q=0. Thus `C_n m=C_m n`. Metricity also makes K(C_n m,l) skew in m,l. Cycling the symmetric first pair and skew last pair forces this tensor to vanish, so C_n=0. This is the same pure-normal implication as source-exterior-connection E9–E11, now composed with the complete horizontal condition rather than left as a one-row necessity.

**Proof, sufficiency and scalar row.** Under (N1),

`T_B(X,n)=(S_n-A_n)X-ell(X)n`, `T_B(n,m)=0`,
`w_B+Hmean=-m ell#`, m=10.

For hidden z, C_H(F)=ell Gamma_Nz=0 and Gamma_N C_N(F)=c(ell#)Gamma_Nz=0. The scalar row is zero because z annihilates H. Hence all three observed rows vanish. No scalar-row repair was omitted. ∎

## 3. Exact descended lower operator

Use receiver `(b,sigma=tau-Gamma_H b,nu)`. Put L_n=S_n-A_n, v=ell#, and define

`A_L(b)(n)=sum_mu eps_mu c(e_mu)b(L_n e_mu)`,
`F_A(b)=Gamma_N A_L(b)`,
`C_H^A(b)(X)=-sum_r eta_r c(n_r)b(L_(n_r)X)`.

Horizontal Clifford anticommutation gives `Gamma_H C_H^A=F_A`. Direct substitution of (N1), retaining all input channels, gives

`V_b=a C_H^A(b)+a ell sigma+c0 J_H(F_A(b)+c(v)sigma)`,
`V_sigma=(a+m c0)(F_A(b)+c(v)sigma)`,
`V_nu=-m g b(v)`.                                    (N3)

The original total-trace output is

`V_tau=(2a+(h+m)c0)(F_A(b)+c(v)sigma)=L(F_A(b)+c(v)sigma)`.

There is no normal-normal torsion contribution after admissibility. The independent scalar remains present; no hidden reduction to five spinors has occurred.

## 4. Horizontal-grade exclusion for every admissible extension

The principal symbol is unchanged. The prior arbitrary-block proof forces

`G_H,o=diag(chi_H,-chi_H,-chi_H)`.

Tangential B_X and its Clifford/split connection are unchanged, so this same grade is parallel. Derivatives of a putative varying grade cannot cancel a lower defect; pointwise principal uniqueness has already fixed it.

Every ell-dependent block in (N3) is odd for G_H,o. It therefore cannot cancel the shape/A contribution. F_A is mixed normal-horizontal Clifford degree2: it anticommutes with chi_H. On input `(b,0,0)`, the sigma anticommutator is

`{G_H,o,V}_sigma(b,0,0)=-2(a+m c0) chi_H F_A(b)`
`                           =-(a/3)chi_H F_A(b)`.      (N4)

Because a≠0, full oddness implies F_A(b)=0 for every horizontal one-form spinor b. For each input component b_j, the coefficient in F_A is a linear combination of the distinct mixed blades c(n_r)c(e_mu), with coefficients equal to those of L_(n_r)e_mu. Faithfulness of full Cl14 forces every L_n=0. Thus

`S_n=A_n` for every n.

S_n is g-selfadjoint and A_n is g-skew. Over characteristic0 these can be equal only if both vanish. Hence II=0 and A_n=0.

Conversely, within the quotient-admissible family, if II=0 and A_n=0, the remaining ell terms have the stated oddness. Thus the **observed** horizontal grade is compatible exactly on that zero-shape/A locus. This converse is a control for the receiver equation only; it does not independently certify every raw hidden extension, source field law or global domain.

The native metric-bundle shape `S_n=-(1/2)g^-1 n` is nonzero, so every quotient-admissible metric normal extension fails the same-horizontal-grade test. If a normal extension is not quotient-admissible, it has already failed the full observation equations. Together these exclude the simultaneous observation-plus-horizontal-grade realization for the entire 910-dimensional space of metric normal values in the declared coherent/exterior family.

## 5. A robust witness, but no uniform rank claim

For b=J_H psi,

`F_A(J_H psi)=c_N(Hmean)psi - sum_r eta_r c(n_r) sum_mu eps_mu c(e_mu)c(A_(n_r)e_mu)psi`.

The first summand has pure Clifford degree1; the second has degree3 because every A_n is skew. The native mean Hmean=t/2 is nonzero with square−1. Therefore the degree1 component cannot be canceled by any A_n. This is a simple witness of a nonzero operator for every extension. It does **not** prove that the complete operator stays injective or has rank128 after adding arbitrary degree3 pieces. Only the previous B_n=0 witness has that injection certificate.

## 6. Scope and the ambient countercontrol

The source-correlated ambient grade `diag(Omega on zeta,-Omega on nu)` is a different grade. Metric-spin connections preserve Omega; exterior derivative/codifferential commute with it, while Phi is ambient-odd. It survives this metric connection family, and descends as `diag(Omega,-Omega,-Omega)` whenever q does. In particular F_A is ambient-even, exactly the parity required between those opposite-sign receiver slots. The companion source review supplies the detailed counterproof and K95 reality/pairing laws.

Therefore this exclusion does not mean there are no native-correlated grades, and does not falsify SC-CHI-01/04's effective claim. It excludes the fixed plain-horizontal-readout same-grade realization. Larger source-parent varpi, distinct field/equation grades, SE/Shiab/lower completions, different coherent-jet prescriptions, physical current/domain reduction and K77 remain outside. No classC, source, canon or integer index verdict follows.

## Proof scope and validation design

A small exact Clifford-word probe checks all60 skew basis variations A_n skew basis variations and all4 ell variations, all-metric tensor identities, complete q rows on the canonical K projector, forbidden normal-normal and non-scalar mixed plants, the fixed Clifford-degree witness, and ambient/horizontal parity distinction. The written factorization/blade proof supplies exhaustion. A conditional Lean core can certify symmetric+skew=0 and its contrapositive after the mixed-blade injection premise; it should not claim geometric construction or analytic domains are formalized.

## Evidence and acceptance

Root ran the exact sparse Clifford probe:344 controls PASS. The conditional
Lean core compiles without sorry. It proves finite implications under the
written geometric premises, not the complete Clifford/domain theorem.
Two mathematical specialist lenses and one hostile source lens accepted the
named-family result; these are internal agent reviews, not human certification.

- [Machine evidence](../../lab/process/metric-normal-family-grading.json)
- [Exact probe](../../tests/program-focus/metric_normal_grading_probe.py)
- [Lean finite core](../../Lean/GUFormalization/MetricNormalGradingCore.lean)
- [Review](../../lab/process/hostile-reviews/2026-11-24-metric-normal-family-review.md)
- [Prior full receiver/principal proof](six-spinor-grading-compatibility-2026-11-24.md)
- [Actual source weak transport and existing effective estimates](source-weak-action-transport-2026-11-13.md)
- [Source register](../../lab/sources/source-claim-register.yaml): SC-CHI-01/04/51/52, SC-OP-04/05, SC-GEO-55, SC-META-56.

No source/physics ledger, classC, canon, physical count or current verdict changes.

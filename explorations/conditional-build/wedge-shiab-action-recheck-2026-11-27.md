---
title: The wedge-Shiab action has a corrected Euler row and surviving epsilon redundancy
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T2
expected_delta: Derive the wedge candidate's own action and completed moving identity before conservation or energy tests
actual_delta: Exact primitive and moving rows; the epsilon row is D_A of the corrected connection row; identical printed-endpoint matching remains excluded
class_covered: Normalized wedge insertion in the first bosonic trace action, source primitive fields and conjugated metric Clifford insertion, compact local variations and retained mass/metric terms
premises:
- Theta equals epsilon-inverse times star Phi3 of g times epsilon, degree eleven in fourteen dimensions
- Ordinary matrix exterior products and graded cyclic trace; S2 is minus the wedge anticommutator
- Full primitive translation and actual metric/epsilon chain rule
- GU* interpretation, not a uniquely selected historical Shiab
source_bridge:
  status: conditional
  reason: Source supplies action packet and primitive transformations; wedge selection is a declared alternative
kill_condition: A cyclic sign, integration-by-parts, primitive-transformation or native-normalization failure invalidates the affected identity
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Action ownership and scoped positive evidence only; no scientific verdict changes
---

# Wedge recheck, wave one: an action-level survivor with a fidelity cost

program_target: LB-CLASS
tier: T2
expected_delta: Test the wedge alternative on its own equations, retaining the completed eddy and moving geometry.
actual_delta: Coherent first-action variation and epsilon redundancy; an explicit difference from the printed unit-curvature row.

**ESTABLISHED:** the actual wedge Euler equation has an extra quadratic term required by variation. Including the source epsilon transformation makes the epsilon equation the covariant derivative of this **corrected** connection equation. The correction does not destroy that redundancy.

**RULED OUT, by reuse:** identifying this nonzero fixed full-Spin/full-U member's variation with the uncorrected printed unit endpoint under the previously tested universal hypotheses. **NOT MODELED / UNDETERMINED:** a native stationary full-system wedge solution, positive physical energy, observed conserved stress and GR recovery.

The tested GU* member **SURVIVES** its own-action and first-bosonic redundancy checks. Exact printed-endpoint identification is **FALSIFIED within the already declared class**. Gravity and overall SOURCE/GU* remain **INCOMPLETE**. Neither a Riemann response nor one candidate's failure settles the whole gravity pillar.

```gu-typed-objects
result: normalized wedge action variation and primitive epsilon identity
carrier: End_C(S128)-valued forms on Y14, full source u(H) translations LAYER=ambient CHIRALITY=N/A
pairing: nondegenerate trace and top-form pairing, not a positive physical Hilbert norm ON=bosonic_adjoint_forms
real_structure: primary-minus Clifford adjoint, K95 and K77 controls separately declared
grading: exterior degree, not physical chirality or spinor-module grading
action_owner: repository-construction -- source-shaped first bosonic action with the existing normalized wedge candidate
target: actual Euler rows and source primitive pullback MAP-TYPE=intertwiner
```

## 1. Source custody, reuse and declared outcomes

Basis `4910d449e277bc3f742911134c3beb4c5f8af143`. Joe27r step1, wave1 of at most3; the [ordered packet](../../lab/process/work-packets/quick-win-sequence-2026-11-27.md) preserves the six-step order and discovery-bet cadence.

Draft pp42–43, Definition8.1/eq8.7 and eq9.2–9.3 (SC-OP-02/03) supplies invariant ingredients, the missing historical selector and curvature-response intent. Draft p44 eq9.4, pp44–45 eq9.7–9.10 and p57 eq12.4 (SC-ACT-01/02) supplies the completed action packet, ordinary matrix wedge, translation variation and printed endpoint. Portal2020 **02:31:34–02:35:10 explicitly retains the quadratic eddy**: bare Shiab-applied curvature is not the completed exactness target.

The [source primitive dictionary](source-prescription-current-2026-11-13.md) §§1–2, from draft eq6.22/7.3/9.7 and moving-Shiab source receipts, fixes

```
A=A0[g]+varpi, B=A0[g]^epsilon, T=A−B,
delta B=Ad_(epsilon^-1) beta+D_B eta,
delta T=alpha+(Id−Ad_(epsilon^-1))beta−D_B eta,
beta=(D_g A0)[h], eta=epsilon^-1 delta epsilon.
```

The candidate insertion is `Theta=epsilon^-1(*_G Phi3[g])epsilon`; thus `delta_epsilon Theta=[Theta,eta]` and `D_B Theta=0` for the compatible reference. The source supplies conjugation of invariant Phi constructions, not unique selection of this wedge. Theta is not an independently adjustable source field. Here the parallelism simplification uses the matching torsion-free metric-spin reference in [the owned chimeric/LC reconstruction](source-chimeric-trace-compatibility-2026-11-13.md) §1, transported with Theta. A connection preserving only a more general chimeric structure need not satisfy it; the formulas below retain K for that case.

Already decided, without new credit:

- [Wedge companion](shiab-bianchi-companion-class-2026-11-27.md): `Splus2(F)=Theta F+F Theta` has an LC companion and nonzero Einstein response. Use **S2=−Splus2** to match the selected Riemann normalization.
- [Universal variation theorem](full-shiab-variational-consistency-2026-11-27.md) and [endpoint audit](printed-shiab-endpoint-audit-2026-11-27.md): fixed-linear and wedge overlap. This nonzero member does not evade exact printed-Euler exclusion, including the stated arbitrary-C2-action/fixed-multiplier extensions.
- W2 roots, energy and symbols belong to W2; the full-system CW theorem belongs to the selected printed low-Phi equation. Neither is this wedge action's dynamics.

Outcomes were fixed first: retain a consistent own-action survivor; exhibit its exact fidelity cost; include moving/eddy terms before testing redundancy; and use only this action's solutions and constraints for energy. No new coefficient, state rule, vacuum or physical norm is adopted.

## 2. Exact variation

Juxtaposition means ordinary matrix exterior product. Put `D=D_B`, `F=F_B`, `Y=DT`, `K=DTheta`; degrees are `T:1`, `F,Y:2`, `Theta:11`, `K:12`. For compact local variations,

```
C=F+(1/2)Y+(1/3)T²,
I_w=−integral tr[T(Theta C+C Theta)],
I_mass=(kappa/2) integral tr(T *_G T).
```

The declared trace may carry a fixed real normalization. It is not a positive physical pairing. Kappa is a coefficient, not a derived particle mass. The top form already includes volume; a second independent density would change the model. Global convergence/boundary data remain separate.

Graded cyclicity gives `L_w=tr Theta[FT+TF+(1/2)(YT+TY)+(2/3)T³]`. Temporarily vary T,B,Theta independently to calculate the chain rule, not to introduce extra source equations. With variations placed at the left,

```
delta L_w=tr(delta T E_T+delta B E_B+delta Theta E_Theta)
           +d tr[(delta B+(1/2)delta T)(Theta T−T Theta)],

E_T=−{Theta,F+Y}+(1/2){K,T}
    −(2/3)(Theta T²+T² Theta−T Theta T),
E_B={K,T}−{Theta,Y}−(1/2){Theta,T²}+T Theta T,
E_Theta=FT+TF+(1/2)(YT+TY)+(2/3)T³.
```

Braces are ordinary ordered sums. Derivative-on-variation terms are `(1/2)tr D(delta T)(Theta T−T Theta)`; integration by parts has a **plus** sign because delta T has degree1. Cubic cyclic rotations give `−T²Theta`, `+TThetaT`, `−ThetaT²`, independently of any intended endpoint.

The mass adds `kappa *_G T` to E_T and `(kappa/2)tr(T delta(*_G)T)` to explicit metric variation. At fixed T,g it has no B or Theta row. Pairing and boundary conventions must remain the same throughout.

## 3. Exact endpoint difference

Since `F_A=F+Y+T²` and `D_A Theta=K+TTheta+ThetaT`,

`E_T=S2(F_A)+(1/6){D_B Theta+2D_A Theta,T}`.

On the actual compatible reference,

`E_T^total=S2(F_A)+(1/3){D_A Theta,T}+kappa *_G T`.

The correction is generally nonzero on full-U translations. Its coefficient is fixed by the action, not a tuning parameter. The native check uses `T=e0 gamma2+e1 gamma3` with full `Theta=*Phi3`, separately in the declared K95/K77 layouts. The difference has ten nonzero13-form/grade5 components, coefficients of magnitude8/3. This is a concrete control of the owned exclusion, not new source-falsification credit.

A graded-central parallel insertion is a positive algebraic control: `D_A Theta=0` restores the unit curvature endpoint. The Clifford insertion is noncentral. Restricting translations to its stabilizer would change the source primitive space and is not adopted.

## 4. Epsilon redundancy survives for the corrected equation

The exact rows obey the formal covariance identity

`D_B E_B+{T,E_T}+{Theta,E_Theta}=0`.

It follows from simultaneous connection/tensor conjugation and is checked directly in the free graded algebra. This is an application of Noether's identity to the actual wedge rows, not a new general Noether theorem.

At fixed g,varpi the source epsilon variation is `delta T=−D_B eta`, `delta B=D_B eta`, `delta Theta=[Theta,eta]`. Integrating by parts gives

```
E_epsilon=D_B(E_T−E_B)−{Theta,E_Theta}
         =D_B E_T+{T,E_T}=D_A E_T.
```

This own-action first-bosonic residual relation does **not** require `D_A Theta=0`. The mass respects it: `{T,*_G T}=0` as a matrix-valued top form by symmetry of metric contraction, so `kappa D_B *_G T=kappa D_A *_G T`.

Conjugation of the insertion supplies the needed epsilon term; freezing it would manufacture a defect. This result does not equate corrected E_T with the printed unit row, establish the unpublished spinor cancellation, or incorporate the independent fermion/other-action pieces without their variations.

The completed packet separately satisfies

```
D_A C=(1/2)[T,F_B]+(1/6)[T,D_B T],
D_A S2(C)=S3(D_A C)−{D_A Theta,C},
S3(G)=Theta G−G Theta.
```

These terms generally do not vanish. The residual identity closes through the action rows, not a false bare-curvature exactness premise. A transgression-shaped path expression has a formal derivative of degree15 on Y14; that vacuous top-degree identity is not a conservation proof.

## 5. Moving metric, current and remaining physical tests

The actual pullback of the wedge bulk variation is

```
tr[alpha E_T+beta E_T
   +Ad_(epsilon^-1)beta (E_B−E_T)
   +Ad_(epsilon^-1)(delta_g(*_G Phi3)) E_Theta],
```

Here E_T includes its mass row when mass is retained; add the explicit mass metric term as well. Derivatives in beta and delta_g Theta need further integration by parts to give the base-metric equation. E_B=0 and E_Theta=0 are not independent source equations. Hodge, Clifford identification and reference motion cannot be discarded.

The exact boundary form in §2 gives the independent-coordinate presymplectic potential. Its antisymmetrized variation is the action's bilinear current; conservation requires actual linearized solutions of all varied rows and declared boundary conditions. Further metric-chain-rule integration by parts adds boundary terms before this becomes the full primitive-field current. It is an input to the next energy test, not positive physical energy or already conserved four-dimensional stress.

At `T=0,F_B=0`, all first rows of this first action vanish by field degree. This is a conditional flat-ambient reference. **Flat X does not supply it:** the owned native flat-base Observerse has nonzero upstairs Ricci, eigenvalues1/4 on horizontal-plus-trace and−5/4 on traceless vertical, scalar−10. The owned actual spin-LC Einstein-response normalization therefore makes `S2(F_B)` nonzero. It is not a stationary zero-distortion wedge vacuum.

Even at a genuine flat ambient reference, the joint Hessian contains `tr(t S2(delta F_B[h]))`. A held-metric connection mode must satisfy its adjoint metric row before it is a full-system solution. W2 roots or a discarded metric row cannot justify wedge stability claims. These observations reuse native geometry; no new vacuum is chosen.

## 6. Verification and next gate

Twenty-one exact controls independently differentiate the graded action, integrate by parts, verify all rows/boundaries and compact identities, and check sparse full-Clifford witnesses in both declared layouts. The old Riemann census is not rerun. Source attribution, field-space pullback and physical limits receive independent review; finite controls do not prove dynamics. See [evidence](../../lab/process/wedge-shiab-action-recheck.json).

The own-action and first-bosonic residual-identity portions of Joe27r step1 are complete. Next: this action's own temporal constraints and canonical current on a declared native stationary background, or an explicitly conditional frozen reference retaining the mixed metric row. If native stationarity is unavailable within the three-wave cap, name that burden and move through the ordered sequence. The printed low-Phi CW result remains accepted but does not transfer to the changed wedge operator.

Choice budget remains10/4/net6/0 source-selected predictions. The correction introduces no tunable family; it follows from the existing wedge candidate. No selected physical replacement, new physical prediction, canon promotion or ledger verdict follows.

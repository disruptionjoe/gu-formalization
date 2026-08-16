---
title: "Selected-K144 native I1B T=0 curved local-inverse owner gate"
status: active_research
doc_type: exact_frozen_nilpotence_curved_operator_composition_and_quotient_basicness_gate
created: "2026-08-16"
registry: lab/process/selected-k144-native-i1b-t0-curved-local-inverse-owner-gate.json
probe: tests/channel-swings/selected_k144_native_i1b_t0_curved_local_inverse_owner_gate_probe.py
grade: "K144 PROVES THAT K135'S FIXED-KAPPA FROZEN NULL INVERSE DOES NOT DETERMINE A CURVED-NEIGHBORHOOD REDUCTION OR FIVE-CLASS LOWER COEFFICIENT. THE ACTION OWNS THE LOCAL COUPLED HESSIAN [[0,A*],[A,C]], AND K135'S NILPOTENT FROZEN PRINCIPAL MATRIX DOES ADMIT A FINITE POLYNOMIAL INVERSE AT CONSTANT COEFFICIENTS. BUT PRINCIPAL-SYMBOL NILPOTENCE DOES NOT DETERMINE OPERATOR COMPOSITION WHEN COEFFICIENTS VARY. AN EXACT TWO-BY-TWO CONTROL P_S=U_S V_S^T D WITH V_S^T U_S=0 HAS THE SAME FROZEN NILPOTENT PRINCIPAL MATRIX FOR EVERY S AT X=0, YET P_S^2=S P_S AND (KAPPA I+P_S)^{-1}=KAPPA^{-1}I-[KAPPA(KAPPA+S)]^{-1}P_S. A SCALAR CONTROL WITH THE SAME POSITIVE-ORDER/FIXED-MASS SHAPE INSTEAD HAS ONLY THE RATIONAL PSEUDODIFFERENTIAL INVERSE (KAPPA+I A(X)XI)^{-1}; ITS FIRST LEFT SYMBOL CORRECTION IS I A A' XI/(KAPPA+I A XI)^3 WHILE THE WEYL FIRST CORRECTION VANISHES. THUS BOTH LOCAL DERIVATIVE-DEPENDENT AND NONLOCAL CALCULUS-DEPENDENT CONTINUATIONS ARE COMPATIBLE WITH FROZEN POINT DATA. K138'S INDEPENDENT BRINKMANN CURVATURE-GRADIENT THREE-JETS LEAVE THE PRINCIPAL NULL QUOTIENT FIXED. NO COMPLETE VARIABLE-COEFFICIENT I1B REDUCTION EVALUATOR, GREEN/PARAMETRIX EQUIVALENCE, CLOSED DOMAIN OR FIVE-CLASS ENDOMORPHISM IS PRESENTLY OWNED. RADICAL/GAUGE BASICNESS REMAINS UNDEFINED, NOT ZERO, PASS OR FAIL."
target_claim: K143_NEXT_GATE__FIXED_KAPPA_CURVED_LOCAL_OPERATOR_COEFFICIENT_AND_RADICAL_GAUGE_BASICNESS_OR_EXACT_MISSING_OWNER
target_verdict: LOCAL_COUPLED_HESSIAN_ACTION_OWNED__FROZEN_NILPOTENT_INVERSE_DOES_NOT_DETERMINE_CURVED_OPERATOR_COMPOSITION__LOCAL_DERIVATIVE_DEPENDENT_AND_NONLOCAL_CONTINUATIONS_SHARE_FROZEN_DATA__FIVE_CLASS_BASICNESS_UNDEFINED_PENDING_COMPLETE_CURVED_REDUCTION_EVALUATOR
canon_verdict_change: none
---

# Selected-K144 native I1B T=0 curved local-inverse owner gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K144 binds the displayed local source-native `I1B` Hessian at the
Ricci-flat `T=0` germs of K127 and K138, fixed nonzero `kappa_1`, K135's
finite-frequency distortion elimination, and K138's null metric quotient.
It decides what the frozen inverse does and does not determine on a curved
neighborhood. It does not select a Green operator, quantization, gauge,
boundary condition, closed domain, BFV reduction, positivity, state space, or
physical propagation law.

## Result in plain English

The action owns the local coupled differential Hessian

```text
H_I1B = [[0,A*],[A,C]].                              (1)
```

The five-class metric response used in K135--K143 is the Schur expression

```text
S_eff = -A* C^{-1} A.                               (2)
```

K135's frozen null matrix has a nilpotent generalized principal coefficient,
so at constant coefficients its inverse is genuinely a finite polynomial.
Positive differential order alone does **not** rule out a differential inverse
for such a system. The curved question is whether frozen nilpotence survives
variable-coefficient operator composition.

Frozen data do not decide that question. Two exact controls give opposite
continuations. The scalar normal form

```text
c(x,xi)=kappa+i a(x)xi                              (3)
```

has a rational rather than polynomial inverse. Its neighborhood inverse is a
pseudodifferential/Green object. By contrast, let

```text
u_s=(1,sx)^T,  v_s=(-sx,1)^T,  M_s=u_s v_s^T,
P_s=M_s d/dx.                                       (4)
```

Then `v_s^T u_s=0`, so the principal matrix squares to zero at every point,
and all values of `s` have the same frozen matrix at `x=0`. Operator
composition sees the derivative:

```text
P_s^2=s P_s,
(kappa I+P_s)^-1=kappa^-1 I-[kappa(kappa+s)]^-1 P_s. (5)
```

This inverse is local and differential, but its coefficient depends on the
neighborhood derivative invisible in the frozen matrix. The scalar and matrix
controls prove that the same frozen-order description can lead to a nonlocal
inverse or a derivative-dependent local inverse. Neither control is imported
as the `I1B` answer.

For the scalar control, standard left-symbol recursion gives

```text
r_0=c_0^-1,
r_1=-c_0^-1(1/i)(partial_xi c_0)(partial_x r_0)+...,
r_1^left=i a a' xi/(kappa+i a xi)^3,                (6)
r_1^Weyl=0.                                         (7)
```

The left/Weyl difference is a symbol-equivalence issue, not physical
nonuniqueness. It proves that a named symbol coefficient is under-typed until
the calculus and invariant equivalence rule are declared.

K138 supplies the action-side neighborhood freedom: its Ricci-flat Brinkmann
family has two independent curvature-gradient parameters `a_1,b_1` while the
null Schur projector and rank-five quotient remain fixed. A complete curved
`I1B` evaluator could still close finitely, require a parametrix, or expose a
new obstruction. K127's point two-jet and K135's frozen matrix do not select
among those outcomes.

```text
local coupled Hessian:                 action-owned;
frozen fixed-kappa nilpotent inverse:  exact at its stated grade;
curved local inverse:                  possible, not implied;
curved nonlocal inverse:               possible, not implied;
complete I1B neighborhood evaluator:   absent;
five-class coefficient:                not presently determined;
radical/gauge basicness:               UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR.
```

## 0. Layer-0 packet and pre-wave answers

| object | exact meaning here | not identified with |
| --- | --- | --- |
| coupled local Hessian | differential operator (1) | reduced metric response (2) |
| frozen inverse | inverse of `C(x,xi)` at one point/covector | inverse of `C(x,D)` on a neighborhood |
| operator nilpotence | vanishing under differential composition | principal-matrix nilpotence alone |
| null quotient | `ker ell_n / im(n odot -)` at finite-Schur principal grade | physical cohomology |
| basicness | preservation by an owned reduced map | a property inferable from frozen data |

1. **Construction fork.** Local coupled coefficients, frozen matrix inverse,
   and curved operator inverse are three different objects.
2. **Cheapest decisive condition.** Test whether frozen principal nilpotence
   determines operator nilpotence. Equations (3)--(5) prove it does not.
3. **Positive route.** Derive complete variable-coefficient `I1B` composition,
   then classify its inverse as local, parametrix, Green, or unavailable.
4. **Negative route.** Do not relabel K135's frozen polynomial inverse as a
   curved action-owned five-by-five coefficient.
5. **Claim ceiling.** No no-go for local inversion or a future parametrix, no
   zero-subprincipal claim, and no physical/domain conclusion.

## 1. Frozen-symbol non-identifiability theorem

The scalar control proves that one fixed-mass positive-order operator has no
polynomial inverse: if `(kappa+i xi)p(xi)=1` for nonzero polynomial `p`, the
left degree is `deg p+1`, not zero. The matrix control proves that a
nilpotent system can have a local differential inverse whose coefficient
depends on a first neighborhood jet. Both results are exact.

K135 lies on the matrix-sensitive horn. Its frozen generalized coefficient is
nilpotent and its finite Neumann inverse is exact. But K135 checks matrix
powers after freezing `(x,xi)`, not differential-operator powers on the
Brinkmann neighborhood. Equation (5) shows why the distinction is material:
derivatives of a nilpotent principal frame enter composition even when the
point matrix is unchanged.

## 2. Symbol recursion and Ricci-flat jet freedom

For left symbols,

```text
(c # r)(x,xi)=sum_alpha (1/i)^|alpha|/alpha!
  (partial_xi^alpha c)(partial_x^alpha r).            (8)
```

Solving `c#r=1` yields (6). A curved evaluator must therefore know the
complete variable-coefficient `C`, its lower symbol, coefficient jets, and the
convention in which results are compared. At `x=0`, the family
`a_s(x)=1+s x` has the same frozen scalar symbol for every `s`, while

```text
r_1^left(0,xi)=i s xi/(kappa+i xi)^3.                 (9)
```

K138's exact independent Brinkmann curvature-gradient parameters make the
same ownership point on action-admissible Ricci-flat neighborhoods: principal
quotient equality does not fix the lower neighborhood evaluator.

## 3. Quotient basicness at the correct type

The raw operator (1) carries the action's coupled Noether identities. The
five-class object is metric-only and arises after distortion elimination.
Before the complete curved reduction exists, there is no owned map

```text
L_Q : ker ell_n/im(n odot -) -> ker ell_n/im(n odot -)  (10)
```

whose basicness can be tested. An owned representative must preserve both the
radical and gauge image. Planted good and bad maps share the same principal
quotient, so principal covariance does not decide the test. Basicness remains
`UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR`, not zero, pass, or fail.

## 4. Route census and hostile bookends

- **Frozen finite Neumann route:** exact and retained at K135's grade.
- **Local curved route:** viable in the nilpotent matrix control and must be
  tested from the complete `I1B` operator composition.
- **Formal parametrix route:** viable after a calculus and full coefficient
  jets are declared.
- **Green route:** viable after a domain/boundary realization.
- **Coupled Noether route:** already local and the strongest action-owned
  successor.
- **Five-by-five brute force:** rejected because the reduced map is untyped.

Strongest overclaim: the scalar control must not be generalized to K135's
nilpotent system. K144 explicitly retains local inversion as a live horn.

Strongest contrary construction: the exact matrix control supplies a local
inverse. It defeats the initial “positive order implies nonlocal” conjecture
and is incorporated into the result rather than hidden.

Weakest reproducibility seam: neither control computes the full Clifford
system. Any successor must derive the variable-coefficient `I1B` composition
and test actual cancellations instead of importing either control as physics.

Postflight revalidates the serialized K138/K143 invariants, checks scalar
polynomial noninvertibility, the exact nilpotent matrix composition/inverse,
left/Weyl first corrections, same-frozen-symbol jet freedom, and planted
basic/non-basic quotient maps.

## 5. Reverse scaffold and next gate

```text
R0 physical propagation needs a closed action-owned reduced operator.
R1 K127/K138: Ricci-flat germs and a covariant five-class principal quotient.
R2 K135/K143: exact frozen elimination on a bounded nonconic band.
R3 K144: frozen nilpotence does not decide curved operator composition; exact
   local derivative-dependent and nonlocal controls share frozen point data.
R4 K144: without the complete curved I1B evaluator, no five-class lower
   endomorphism is determined and basicness is undefined.
R5 K145: derive the variable-coefficient coupled Noether/compatibility complex
   and exact C-composition on the Brinkmann family; classify locality before
   any parametrix/domain selection.
R6 only after R5: construct an owned reduction, KT/BFV, pairing and states.
```

K145 should prefer the local coupled Noether route because it can decide
whether K135's frozen nilpotence survives curved operator composition before
selecting an inverse. Joe input is not required for that bounded audit.
Selecting a Green/domain realization, pseudodifferential calculus, gauge
fixing, or boundary functional remains a separate authority decision.

## K145 successor classification

K145 writes `P=K E(D_B)` and proves that extending K135's degree-four frozen
null Neumann polynomial leaves exact right remainder `kappa_1^-5 P^5` and
left remainder `kappa_1^-5 K P^5 K`. The actual spacelike generalized
principal spectrum makes full differential `P^5=0` impossible, so the frozen
polynomial does not silently become a neighborhood operator inverse. On the
Brinkmann null characteristic the order-five symbol does vanish; the exact
curvature and first curvature jet are live lower inputs, while their selected
`comm/symi/symi` projection remains
`UNEVALUATED_SELECTED_SHIAB_REMAINDER`. The coupled diffeomorphism Noether
chain closes through `A G=0` and `G^* A^*=0` but imposes no identity on `C`,
because the distortion gauge component vanishes at `T=0`. K146 owns the
bounded selected-Shiab order-at-most-four remainder and quotient-preservation
test before any inverse, parametrix, gauge, boundary, or domain selection.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k144_native_i1b_t0_curved_local_inverse_owner_gate_probe.py
```

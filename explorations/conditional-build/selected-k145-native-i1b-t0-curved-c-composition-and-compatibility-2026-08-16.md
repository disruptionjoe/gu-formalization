---
title: "Selected-K145 native I1B T=0 curved C-composition and compatibility complex"
status: active_research
doc_type: exact_generalized_distortion_polynomial_remainder_and_coupled_noether_complex_gate
created: "2026-08-16"
registry: lab/process/selected-k145-native-i1b-t0-curved-c-composition-and-compatibility.json
probe: tests/channel-swings/selected_k145_native_i1b_t0_curved_c_composition_and_compatibility_probe.py
grade: "K145 DERIVES THE EXACT VARIABLE-COEFFICIENT GENERALIZED-C COMPOSITION. WITH C=KAPPA_1 K+E(D_B), K^2=I, NABLA K=0 AND P=K E(D_B), ONE HAS K C=KAPPA_1 I+P. K135'S DEGREE-FOUR NEUMANN CANDIDATE HAS EXACT RIGHT REMAINDER KAPPA_1^-5 P^5 AND LEFT REMAINDER KAPPA_1^-5 K P^5 K. THE FROZEN NULL RELATION L(N)^5=0 KILLS ONLY THE ORDER-FIVE PRINCIPAL SYMBOL AT THAT COVECTOR. IT DOES NOT GIVE P^5=0 AS A DIFFERENTIAL-OPERATOR IDENTITY: THE ACTUAL SPACELIKE PRINCIPAL FAMILY HAS NONZERO GENERALIZED EIGENVALUES, SO P^5 IS GLOBALLY NONZERO ALREADY AT FLAT COEFFICIENT GRADE. ON THE BRINKMANN FAMILY THE TOTAL COVARIANT SQUARE ALSO HAS THE EXACT NONZERO TRANSVERSE WEYL MATRIX [[-A,-B],[-B,A]], WITH U-DERIVATIVE [[-A1,-B1],[-B1,A1]]; THE SELECTED-SHIAB PROJECTION OF THE NULL-CHARACTERISTIC LOWER P^5 REMAINDER IS NOT YET EVALUATED. DIFFEOMORPHISM INVARIANCE OWNS THE LOCAL CHAIN X -> (L_X G,0) -> H(L_X G,0)=0 AND ITS ADJOINT COMPATIBILITY, SO A G_DIFF=0 AND G_DIFF^* A^*=0. IT IMPOSES NO C^2=0 OR P^5=0 IDENTITY BECAUSE THE DISTORTION GAUGE COMPONENT VANISHES AT T=0. THE COUPLED LOCAL COMPLEX IS ACTION-OWNED; A CURVED FIVE-CLASS REDUCED ENDOMORPHISM AND ITS BASICNESS REMAIN UNDEFINED."
target_claim: K144_NEXT_GATE__VARIABLE_COEFFICIENT_CURVED_COUPLED_NOETHER_COMPATIBILITY_COMPLEX_AND_EXACT_C_COMPOSITION_ON_BRINKMANN_FAMILY
target_verdict: KC_OPERATOR_POLYNOMIAL_EXACT__K135_TRUNCATED_INVERSE_HAS_EXACT_P5_REMAINDER__FULL_DIFFERENTIAL_P5_NONZERO_BY_SPACELIKE_PRINCIPAL_SYMBOL__NULL_CURVED_SELECTED_SHIAB_REMAINDER_UNEVALUATED__DIFFEOMORPHISM_NOETHER_COMPLEX_CONSTRAINS_A_NOT_C__FIVE_CLASS_BASICNESS_UNDEFINED
canon_verdict_change: none
---

# Selected-K145 native I1B T=0 curved C-composition and compatibility complex

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K145 binds the selected displayed `comm/symi/symi` source-native `I1B`
Hessian at the Ricci-flat `T=0` germs of K127/K138, fixed nonzero `kappa_1`,
the actual all-grade K132--K135 distortion coefficients, and the K138
Brinkmann family. It classifies the exact differential remainder left by
extending K135's frozen null Neumann polynomial and the action-owned
diffeomorphism Noether chain. It does not select an inverse, parametrix,
quantization, Green operator, gauge fixing, boundary condition, closed domain,
BFV reduction, positivity, state space, or physical propagation law.

## Result in plain English

The distortion block is

```text
C = kappa_1 K + E(D_B),       K^2=I,       nabla K=0.        (1)
```

Define the generalized differential operator

```text
P = K E(D_B),                 K C = kappa_1 I + P.           (2)
```

K135 proved that the frozen null symbol `L(n)=sigma_1(P)(n)` has
`L(n)^5=0`. K145 now performs the operator composition before choosing an
inverse. The degree-four Neumann candidate is

```text
R_4 = kappa_1^-1 sum_(j=0)^4 (-kappa_1^-1 P)^j K.            (3)
```

Direct multiplication, with no commutation assumption beyond scalar
`kappa_1`, gives

```text
R_4 C = I + kappa_1^-5 P^5,
C R_4 = I + kappa_1^-5 K P^5 K.                             (4)
```

Thus K135's frozen inverse becomes the same local differential inverse on a
neighborhood **if and only if** the corresponding full operator remainder
vanishes. The frozen equation `L(n)^5=0` says only that the order-five
principal symbol of `P^5` vanishes at that null covector.

The full operator identity is false. K134's actual all-grade generalized
principal family has nonzero spacelike eigenvalues at 27 exact squared radii.
If `P^5` were the zero differential operator, its principal symbol
`sigma_1(P)(xi)^5` would vanish for every `xi`; those nonzero eigenvalues give
an exact contradiction. This obstruction is already present at flat
coefficient grade. Curvature is not needed to defeat a neighborhood-wide
finite-polynomial inverse.

Curvature still owns the lower null-characteristic remainder. On K138's
Brinkmann family, along the central null geodesic,

```text
R_(u i u j) = [[-a(u),-b(u)],[-b(u),a(u)]],
d_u R_(u i u j) = [[-a_1,-b_1],[-b_1,a_1]],                 (5)
a(u)=a_0+a_1 u,  b(u)=b_0+b_1 u.
```

The connection vanishes on that geodesic, but its commutator does not:
`D_B^2` acts by the total curvature on `Omega1(Cl(7,7))`, including the
one-form curvature and Clifford-adjoint curvature. Equation (5) proves that
the curved covariant substrate and its first jet are live while the principal
null quotient remains fixed. It does **not** by itself compute the
`comm/symi/symi` projection of the lower-order part of `P^5`. That selected
remainder is the exact remaining local evaluator, not a value that may be
inferred from `D_B^2` alone.

The coupled action nevertheless owns a local Noether complex. At `T=0` the
connection difference transforms tensorially, so the infinitesimal
diffeomorphism generator is

```text
R_diff X = (G X,0),          G X = L_X g.                    (6)
```

For the stationary Ricci-flat germ and
`H=[[0,A*],[A,C]]`, diffeomorphism invariance gives

```text
H R_diff=0  <=>  A G=0,
R_diff^* H=0 <=> G^* A^*=0.                                (7)
```

These are exact consecutive-zero identities. They do not prove homological
exactness at the middle term. More importantly, `C` drops out of both
compositions because the distortion component of (6) is zero. The action
therefore owns a coupled diffeomorphism Noether/compatibility complex without
making `C`, `P`, or their characteristic radicals into a differential,
reducibility tower, or distortion gauge complex.

```text
full coupled local Hessian:                 action-owned;
diffeomorphism Noether chain:               action-owned;
frozen null polynomial inverse:             exact at K135 grade;
same polynomial as neighborhood inverse:    obstructed by exact P^5 remainder;
null-characteristic lower P^5 projection:   UNEVALUATED_SELECTED_SHIAB_REMAINDER;
five-class reduced endomorphism:             not owned;
radical/gauge basicness:                     UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR.
```

## 0. Layer-0 packet and route selection

| object | exact meaning here | not identified with |
| --- | --- | --- |
| `E(D_B)` | selected formal-Euler first-order operator | exterior/covariant differential |
| `P=K E(D_B)` | generalized differential operator | one-covector matrix `L(n)` |
| `L(n)^5=0` | null frozen-symbol identity | `P^5=0` on a neighborhood |
| Noether complex | consecutive-zero coupled gauge/Euler chain | exact distortion KT/BV resolution |
| Brinkmann curvature | exact total-covariant curvature substrate | evaluated selected-Shiab `P^5` remainder |

The principal route was structural: derive the exact polynomial remainder,
then use the actual spacelike symbol as the cheapest decisive control. A
brute-force `229376`-square variable-coefficient matrix was rejected because
the global operator identity is already decided by its principal symbols. The
fallback route is the bounded selected-Shiab projection of the order-at-most-
four null remainder on the two-profile Brinkmann jet; switch to it only for a
null-microlocal coefficient or quotient-basicness claim.

## 1. Exact generalized-C polynomial theorem

Let `x=P/kappa_1`. Since `(I+x) sum_(j=0)^4(-x)^j=I+x^5`, equations
(3)--(4) follow exactly. No symbol calculus, boundary adjoint, or inverse
choice enters. The theorem also explains the distinct K133 and K134 facts:

- the selected Euler coefficient `C_1(n)` is not square-zero even on the null
  representative;
- the generalized coefficient `K C_1(n)` is nilpotent of index five there;
- the generalized spacelike coefficient has nonzero spectrum and therefore
  cannot satisfy the same fifth-power identity for all covectors.

Consequently the null Neumann polynomial is a frozen characteristic formula,
not a differential identity for the full neighborhood operator. Another local
inverse is not ruled out merely by this calculation, but it cannot be obtained
by silently replacing `L(n)` with `P` in K135's polynomial.

## 2. Brinkmann curvature and the remaining null remainder

For

```text
g=2 du dv+dx^2+dy^2+[a(u)(x^2-y^2)+2b(u)xy]du^2,            (8)
```

the exact Ricci tensor vanishes. All Christoffel symbols vanish on `x=y=0`,
while (5) is nonzero unless `a=b=0`. Its determinant is
`-(a(u)^2+b(u)^2)`. The derivative contains the independent `a_1,b_1` jets.

This is the correct order distinction:

1. `L(n)^5=0` removes the order-five symbol on the null characteristic.
2. The differential remainder `P^5` can have orders four and below from
   coefficient derivatives and covariant-derivative commutators.
3. Brinkmann curvature supplies exact nonzero admissible commutators without
   changing `L(n)` or the rank-five principal quotient.
4. Whether the selected Shiab and fivefold generalized composition cancel all
   of those terms remains an explicit finite local calculation.

Calling the remainder zero would repeat K144's frozen-to-curved error. Calling
it nonzero solely from (5) would commit the opposite projection error. Its
honest status is `UNEVALUATED_SELECTED_SHIAB_REMAINDER`.

## 3. Coupled Noether/compatibility complex

The local chain is

```text
Gamma(TM) --R_diff--> Gamma(Sym2 T* plus Omega1(Cl))
          --H-------> Gamma(equation duals)
          --R_diff*-> Gamma(T*M),                            (9)
```

with both consecutive compositions zero at the stationary germ. This is the
complete action-owned gauge identity available at `T=0`. It removes four
metric diffeomorphism directions. It does not remove K132's distortion
radicals, provide a distortion ghost, or prove that the kernel of one map is
the image of the preceding map.

The distinction matters for reduction. A local coupled Noether identity can
be exact while the Schur-reduced metric operator remains undefined, because
forming that operator still requires `C^-1`. The local chain is therefore the
right action-owned object to preserve; it is not a substitute inverse.

## 4. Hostile controls and claim ceiling

- **Frozen/operator control:** a five-step Jordan block makes (3) exact; a
  nonnilpotent principal block leaves the stated fifth-power remainder.
- **Flat/curved control:** spacelike spectrum already defeats global `P^5=0`;
  Brinkmann curvature separately proves the lower null remainder has live
  admissible inputs.
- **Noether/non-Noether control:** arbitrary nonnilpotent `C` coexists with
  `H R_diff=R_diff^*H=0` whenever `A G=0`.
- **Projection control:** nonzero total curvature is not automatically a
  nonzero selected-Shiab fifth-power remainder.
- **Quotient control:** without an owned reduced map there is no pass/fail
  basicness statement.

No canon, ledger, claim status, particle, phenomenology, published paper, or
GU-wide verdict changes.

## 5. Reverse scaffold and next gate

```text
R0 K132/K133: E(D_B) is not a distortion differential; only metric
   diffeomorphisms are action-owned gauge.
R1 K134/K135: L(n)=K C_1(n) is nilpotent of index five at frozen null grade.
R2 K144: frozen nilpotence does not determine variable operator composition.
R3 K145: the exact Neumann extension remainder is P^5; full P^5 is nonzero by
   the actual spacelike principal family.
R4 K145: the null top symbol vanishes, while Brinkmann curvature and its first
   jet are live inputs to the unevaluated lower selected-Shiab remainder.
R5 K145: the coupled diffeomorphism Noether complex constrains A, not C.
R6 K146: compute the order-at-most-four selected-Shiab part of P^5 on the
   two-profile Brinkmann null jet and test preservation of H_n and G_n.
R7 only after R6: decide whether a microlocal parametrix/gauge/domain owner is
   required for the five-class reduction.
```

K146 is a bounded local coefficient audit and requires no inverse or domain
selection. Joe input is not required. A pseudodifferential calculus, Green
realization, boundary functional, gauge fixing, or physical quotient remains
a separate authority decision.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k145_native_i1b_t0_curved_c_composition_and_compatibility_probe.py
```

## K146 successor classification

K146 corrects the direct quotient test: `P^5` acts on the distortion carrier,
while `H_n` and `G_n` are metric subspaces. The first well-typed polynomial
metric operator is `S_4=-A^*R_4A`. It kills `G_n` exactly by `A G=0`, but
preservation of `H_n` remains a separate curved composition. The complete
selected-Shiab lower remainder is
`NOT_MATERIALIZED_FROM_CURRENT_SERIALIZED_EVALUATOR`; it is not assigned a
zero or nonzero value. K147 owns the sparse covariant evaluator and the exact
`ell_n S_4|H_n` test.

---
title: "Selected-K129 native I1B T=0 A/C kernel and domain classification"
status: active_research
doc_type: exact_t0_mixed_curvature_and_distortion_operator_kernel_characteristic_domain_gate
created: "2026-08-16"
registry: lab/process/selected-k129-native-i1b-t0-ac-kernel-and-domain-classification.json
probe: tests/channel-swings/selected_k129_native_i1b_t0_ac_kernel_and_domain_classification_probe.py
grade: "K129 IDENTIFIES THE ACTUAL K128 BLOCKS AT THE K127 RICCI-FLAT T=0 GERM. A IS THE NATURAL SELECTED-SHIAB CURVATURE LINEARIZATION, EQUIVALENT ON THE HORIZONTAL RICCI-FLAT PACKET TO -2 DELTA G WITH PRINCIPAL RANKS 6,6,4 AND THE EXACT DIFFEOMORPHISM RADICAL; GENERIC WEYL CURVATURE STILL LEAKS OUTSIDE THE SELECTED TT PLANE. C IS NOT THE EARLIER NONZERO-PHI1 HESSIAN: AT T=0 IT IS C=KAPPA_1 K+E(D_B), WITH K THE NONDEGENERATE QUADRATIC-T FLAT MAP AND E THE COVARIANT FIRST-ORDER FORMAL-EULER DBT BLOCK. THE ALREADY-CERTIFIED CL1/HORIZONTAL-CL2 CROSS HAS RANKS 12,12,11 AND PARITY-COMPLETED RANKS 24,24,22. NONZERO KAPPA REMOVES THE ZERO-MOMENTUM ALGEBRAIC KERNEL BUT DOES NOT SELECT KAPPA OR A GLOBAL CLOSED INVERSE; KAPPA=0 LEAVES THE COMPLETE ZERO-MOMENTUM T CARRIER AS A CONSTRAINT/MULTIPLIER KERNEL. A FIXED-SYMBOL SCHUR COMPLEMENT IS GENERICALLY LEGAL AWAY FROM A COVECTOR-DEPENDENT EXCEPTIONAL LOCUS, WHILE A GLOBAL SCHUR/BFV REDUCTION STILL REQUIRES THE COMPLETE CHARACTERISTIC, GREEN, ADJOINT, GAUGE AND COMMON-DOMAIN PACKET K130."
target_claim: K128_NEXT_GATE__EVALUATE_ACTUAL_A_C_AND_CLASSIFY_KERNEL_GAUGE_ADJOINT_DOMAIN
target_verdict: T0_A_CURVATURE_LINEARIZATION_EXACT__C_KAPPA_K_PLUS_COVARIANT_DBT_EULER_EXACT__POINTWISE_NONDEGENERACY_NOT_GLOBAL_INVERSE__CAUSAL_ADJACENT_GRADE_RANKS_EXACT__K130_COMMON_DOMAIN_BV_BFV
canon_verdict_change: none
---

# Selected-K129 native I1B T=0 A/C kernel and domain classification

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, Ricci-flat curvature-linearization, adjacent-Clifford-
> grade, variational-operator and domain calculation. Ordinary Einstein-action,
> particle-spectrum, Higgs/VEV, family-index, chirality, anomaly and symmetry-
> breaking constructions do not adjudicate it without an explicit typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this result binds the source-native `I1B` quadratic germ in independent
`(g,T)` coordinates at K127's local horizontal Ricci-flat `T=0` fixed-boundary
family. It does not bind the earlier nonzero-`Phi1` stationary branch, a
source-global GU vacuum, or a selected closed physical domain.

## Result in plain English

K128 proved that the quadratic action is coupled, `[[0,A*],[A,C]]`, but left
the two operators unevaluated. K129 closes their local variational identity
and the strongest exact finite-symbol classification currently licensed.

At `T=0`, direct differentiation of

```text
I1B=<T,S(F_B)>+(1/2)<T,S(D_B T)>+(1/3)<T,S(T^2)>
    +(kappa_1/2)<T,*T>
```

gives

```text
A=D_g[S_g(F_B)]|Ricci-flat,
C=kappa_1 K+E(D_B),                                  (1)
```

where `K` is the nondegenerate flat map from the quadratic `T` norm and
`E(D_B)` is the covariant formal-Euler operator of the `d_BT/2` term. The
cubic `T` term has zero second derivative at `T=0`.

Equation (1) corrects a tempting retrieval error. The repository's earlier
grade-one Schur packet uses the Hessian at a selected nonzero-`Phi1`
stationary branch. Its irreducible eigenvalues and coefficient polynomial are
not the K127 `T=0` block and are not ported here.

## 1. The mixed block A

On the selected curvature module `S|Riem=-2G`. Consequently `A` is the
natural linearized Einstein-type curvature row, including the moving
frame/Shiab/pairing packet required for covariance. At a Ricci-flat
background its principal ranks on the ten-dimensional horizontal metric
carrier are

```text
timelike 6, spacelike 6, null 4.                     (2)
```

For nonnull covectors the kernel is exactly the four-dimensional
diffeomorphism image. On the null cone it additionally contains the two TT
principal polarizations. This is operator typing, not a physical-graviton
theorem. K127's curved lower-order result remains load-bearing: generic Weyl
curvature sends the selected plus/cross plane into off-TT components.

## 2. The distortion block C

The algebraic part of `C` is simple but not sufficient. At zero covector,

```text
C(0)=kappa_1 K.                                      (3)
```

The held full-norm theorem makes `K` nondegenerate on the tracked source
carrier. Thus for `kappa_1!=0` there is no pointwise zero-momentum distortion
kernel. At `kappa_1=0`, the whole zero-momentum distortion carrier is a kernel
and its rows must be treated as constraints/multipliers until a gauge or BV
complex says otherwise. Stationarity selects neither fork nor the value of
`kappa_1`.

For nonzero covector, `E(D_B)` changes Clifford parity. The previously
certified `Cl1` to horizontal-`Cl2` cross has ranks

```text
timelike 12, spacelike 12, null 11,                  (4)
```

and the parity-completed derivative operator has ranks

```text
timelike 24, spacelike 24, null 22.                  (5)
```

The same-grade derivative blocks vanish, although their pre-pairing Shiab
images are live. This is a type-selection zero, not an absent derivative.

For any fixed finite symbol, `det(kappa_1 K+E(k))` is a nonzero polynomial in
`kappa_1` whose leading coefficient is `det K`. Hence only finitely many
values are exceptional for that one fixed symbol. The exceptional values may
vary with `k`; the full carrier, bundle, boundary and domain have not been
totalized. Pointwise or fixed-symbol generic invertibility is therefore not
a global inverse theorem.

## 3. Gauge, Schur, Green, and domain disposition

Because `T` is a connection difference, it transforms tensorially. At the
`T=0` background its infinitesimal adjoint gauge motion is zero rather than a
new `d chi` distortion column. Ricci-flat diffeomorphism directions act in
the metric block and remain an exact radical through `A`.

Whenever one has actually selected a domain on which `C` is invertible and
`A*` is the operative boundary adjoint, the formal reduction is

```text
H_eff=-A* C^{-1} A.                                  (6)
```

Equation (6) preserves every direction in `ker A`, including the principal
diffeomorphism radical and the null TT kernel at principal order. Curved Weyl
terms can mix the TT representatives and must be included before any closed
two-polarization claim.

The complete `C` operator is first order, indefinite, and covariant. A global
reduction still needs its characteristic variety on the full source carrier,
one closed Krein/Green domain, boundary conditions, the actual adjoint,
constraint propagation, and the coupled BV-BFV complex. No pseudoinverse or
coefficient fit supplies those data.

## 4. Reverse scaffold and next gate

```text
R0 K127: local Ricci-flat T=0 stationary family.
R1 K128: exact coupled Hessian [[0,A*],[A,C]].
R2 K129: A is the selected curvature linearization; gauge/null ranks typed.
R3 K129: C=kappa_1 K+E(D_B); algebraic and derivative kernels separated.
R4 K129: adjacent-grade causal ranks 24/24/22 are exact.
R5 K130: total full-carrier characteristic and Green concomitant.
R6 K130+: select or obstruct a common closed Krein domain and BV-BFV complex.
R7 only then: test reduced spectrum, positive cohomology and attachment.
```

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes. Joe input is not required.

## K130 successor classification

K130 composes the serialized `196+24` carrier dimensions with the held causal
ranks. The principal and Green coefficients have ranks `24/24/22` and
radicals `196/196/198`, so every conormal is characteristic on this tracked
carrier. Since `kappa_1 K` is zero order it cannot repair that Green radical,
and the order-two `A` plus order-one `C` Hessian selects no unweighted common
domain. Use K130's constraint-splitting and mixed-order successor; do not port
the distinct K77 four-field domain or silently quotient the radical.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k129_native_i1b_t0_ac_kernel_and_domain_classification_probe.py
```

---
title: "Selected-K148 native I1B null-cone principal descent gate"
status: active_research
doc_type: exact_null_characteristic_bundle_and_principal_descent_theorem
created: "2026-08-16"
registry: lab/process/selected-k148-native-i1b-null-cone-principal-descent-gate.json
probe: tests/channel-swings/selected_k148_native_i1b_null_cone_principal_descent_gate_probe.py
grade: "K148 DEFINES THE CORRECTLY PAIRED NULL-CHARACTERISTIC OBJECT LEFT OPEN BY K147 AND CORRECTS K147'S MUSICAL TYPING. OVER EACH NONZERO NULL RAY [N], H_N=KER ELL_N CONTAINS G_N AND Q_N=H_N/G_N HAS DIMENSION FIVE. K135'S FROZEN HESSIAN HAS ONLY -48 ELL_N ELL_N^T; AFTER THE NATIVE DEWITT MAP G^-1 IT ANNIHILATES H_N AND INDUCES ZERO ON Q_N. K147'S UNRAISED SPACELIKE -384 WITNESS IS RETRACTED; THE FULL-MODULE FAILURE SURVIVES BY A DEWITT-RAISED TIMELIKE LEAKAGE -648704. K138 LORENTZ TRANSPORT GLOBALIZES THE NULL LAW. THE CURVED LOWER TRANSPORT REMAINS UNDEFINED BECAUSE THE UNIFIED MOVING CL(7,7) EVALUATOR IS UNSERIALIZED."
target_claim: K147_NEXT_ROUTE__NULL_CHARACTERISTIC_SYMBOL_TRANSPORT_MODULE
target_verdict: COVARIANT_NULL_CONE_QUOTIENT_BUNDLE_EXACT__FROZEN_PRINCIPAL_DESCENT_PASS_ZERO_MAP__CURVED_LOWER_TRANSPORT_UNDEFINED_EVALUATOR_NOT_SERIALIZED
canon_verdict_change: none
---

# Selected-K148 native I1B null-cone principal descent gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K148 binds the selected conditional `comm/symi/symi` local `I1B`
branch at `T=0`, its exact frozen null symbols, and K138's Lorentz-covariant
null-stratum transport. It proves a principal-symbol bundle theorem. It does
not evaluate the curved lower coefficient, recover the preferred historical
Shiab, or select a reduction, inverse, domain, BFV complex, or physical state.

## Result

K147's original `-384` witness used one fixed null constraint `ell_n`, an
independent spacelike derivative covector, and an unraised Hessian covector.
It is retracted as an endomorphism certificate. After the native DeWitt map,
that spacelike row is exactly `-64 ell_n` and has no radical leakage. The broad
full differential-module failure still holds: a timelike derivative covector
has DeWitt-raised leakage `-648704` on the radical vector `h_11=1`. The
microlocal object instead pairs each nonzero null
covector with its own radical and gauge image:

```text
N* = { n != 0 : eta^-1(n,n)=0 },
H_n = ker ell_n,  G_n = im(n symmetric-product -),  Q_n = H_n/G_n.
```

Rescaling `n` multiplies `ell_n` quadratically and `G_n` linearly, so the
subspaces depend only on the null ray. Their dimensions are `9`, `4`, and `5`.

## Null-cone principal descent theorem

K135 computed the complete frozen metric polynomial:

```text
Jordan degree:  0  1  2  3  4
metric rank:    1  0  0  0  0
S_null(n) = -48 ell_n ell_n^T.
```

The Hessian outer square is a map `Sym2 -> Sym2*`. Raising it with the native
DeWitt map gives `N_null=G^-1(-48 ell_n ell_n^T)`. This endomorphism
annihilates `H_n`, hence `G_n`, and induces zero on `Q_n`. K138 owns exact
Lorentz transport of these objects; each nonzero future
or past null cone is a Lorentz orbit and null-ray scaling changes no quotient.
The standard and rationally rotated representatives replay the congruence and
dimensions exactly. Therefore the law globalizes over the nonzero null cone.

```text
null-cone quotient bundle Q:           EXACT_RANK_FIVE;
frozen positive polynomial degrees:    ZERO_AFTER_METRIC_COMPOSITION;
frozen degree-zero Schur coefficient:  -48 ELL_N ELL_N^T;
induced principal map on Q_n:           ZERO_EXACT;
curved lower transport on Q_n:          UNDEFINED_EVALUATOR_NOT_SERIALIZED.
```

## Why zero principal descent is not zero dynamics

K147 proves that the curved restricted residual needs ordinary, one-form and
Clifford-adjoint connections; moving Shiab, Hodge, pairing and density; a
mechanical formal Euler adjoint; Leibniz-complete composition; the curved
bridge `A`; and generic profile jets. The conditional formulas are owned, but
they are not unified in one executable. A zero frozen quotient map therefore
does not name a Dencker endomorphism, propagator, domain, or five physical
states. It only removes principal descent as an additional obstruction.

## Route selection and controls

An inline council spanning Lorentz geometry, characteristic varieties, PDE,
Noether/BV, Clifford algebra, representation theory, quotient categories,
exact computation, source custody, evaluator construction, falsification, and
physics ceilings selected the orbit theorem before evaluator construction.
Controls include standard and rotated null representatives, null-ray scaling,
gauge containment, K135's coefficient ranks, K141's DeWitt musical map, the
retracted unraised spacelike control, the surviving raised timelike leakage,
and the explicit lower-order owner fence.

## K147 index-raising correction

`UNRAISED_HESSIAN_COVECTOR_RETRACTED`: the raw spacelike contraction
`ell_n^T B_8 h=-384` does not test the metric endomorphism. The typed row is
`ell_n^T G^-1 B_8=-64 ell_n^T`, so its radical leakage is zero. The corrected
full-module obstruction is the timelike row
`[0,0,0,0,-648704,0,0,-648704,0,-648768]`, with `h_11=1` and leakage
`-648704`. This changes the witness, not K147's broad route verdict.

## Reverse scaffold

```text
K147/K148 correction: the unraised spacelike -384 witness is retracted;
      DeWitt-raised timelike leakage -648704 kills the full module.
K148: pair n with H_n/G_n; frozen principal descent passes with zero map.
K149: serialize the minimal moving evaluator and compute the first curved
      null restricted residual/lower leakage with frozen and rotated controls.
```

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k148_native_i1b_null_cone_principal_descent_gate_probe.py
```

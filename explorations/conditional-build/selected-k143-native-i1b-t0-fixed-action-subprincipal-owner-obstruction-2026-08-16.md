---
title: "Selected-K143 native I1B T=0 fixed-action subprincipal-owner obstruction"
status: active_research
doc_type: exact_fixed_coupling_conic_homogeneity_quantization_and_quotient_basicness_gate
created: "2026-08-16"
registry: lab/process/selected-k143-native-i1b-t0-fixed-action-subprincipal-owner-obstruction.json
probe: tests/channel-swings/selected_k143_native_i1b_t0_fixed_action_subprincipal_owner_obstruction_probe.py
grade: "K143 PROVES THAT K141'S COMPACT SHELL-FREE FAMILY DOES NOT OWN A LOWER-ORDER SUBPRINCIPAL COEFFICIENT OF THE ORIGINAL FIXED-COUPLING LOCAL I1B ACTION. FOR FIXED NONZERO KAPPA_1, MU=KAPPA_1/RHO AND 13<=|MU|<=14 IS ONLY THE BOUNDED FREQUENCY BAND |KAPPA_1|/14<=RHO<=|KAPPA_1|/13; IT IS NOT CONIC AND IS NOT PRESERVED BY COVECTOR DILATION. THE JOINT RULE KAPPA_1=RHO MU MAKES C=RHO(IC_1+MU K): THE HODGE MASS IS THEN HOMOGENEOUS ORDER ONE AND PART OF THE PROMOTED PRINCIPAL FAMILY, NOT ITS LOWER-ORDER COEFFICIENT. REALIZING RHO AS AN OPERATOR REQUIRES AN AUXILIARY HOMOGENEOUS NORM, QUANTIZATION, ADJOINT AND EQUIVALENCE THEOREM NOT OWNED BY THE DISPLAYED LOCAL ACTION; THE LORENTZ SCALAR SQRT(|Q|) VANISHES ON THE NULL CONE AND CANNOT REALIZE THE NONZERO ANNULUS. THE ORIGINAL FIXED KAPPA_1 K IS A GENUINE ZERO-ORDER DISTORTION COEFFICIENT, BUT K132 ALREADY SHOWS IT BREAKS PRINCIPAL DISTORTION NULL IDENTITIES, AND K139 SHOWS THE COMPLETE DN NULL QUOTIENT IS 106634-DIMENSIONAL RATHER THAN FIVE. PRINCIPAL GRAPH AND QUOTIENT DATA ALONE ADMIT BOTH BASIC AND NON-BASIC LOWER ENDOMORPHISMS, SO RADICAL/GAUGE BASICNESS OF A FIVE-CLASS ACTION COEFFICIENT IS UNDEFINED UNTIL A FIXED-ACTION CURVED OPERATOR COEFFICIENT OR AN EXPLICIT NEW PSEUDODIFFERENTIAL/GAUGE/BOUNDARY OWNER IS SUPPLIED."
target_claim: K142_NEXT_GATE__ACTUAL_LOWER_ORDER_ACTION_COEFFICIENT_ON_COMPACT_NULL_FAMILY_AND_RADICAL_GAUGE_BASICNESS
target_verdict: FIXED_ACTION_ANNULUS_IS_BOUNDED_NONCONIC_FREQUENCY_BAND__JOINT_SCALING_PROMOTES_HODGE_MASS_TO_PRINCIPAL_ORDER_AND_IS_NOT_THE_FIXED_LOCAL_ACTION__NO_OWNED_FIVE_CLASS_SUBPRINCIPAL_COEFFICIENT_EXISTS_ON_THE_COMPACT_FAMILY__BASICNESS_UNDEFINED_PENDING_FIXED_ACTION_CURVED_COEFFICIENT_OR_EXPLICIT_NEW_OWNER
canon_verdict_change: none
---

# Selected-K143 native I1B T=0 fixed-action subprincipal-owner obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, real `Cl(7,7)`, mixed-order symbol, parameter-scaling
> and indefinite quotient calculation. Ordinary Einstein, Higgs/VEV,
> family-index, chirality, anomaly, symmetry-breaking and familiar particle-
> spectrum constructions do not adjudicate it without an explicit typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K143 binds the selected displayed local `I1B` Hessian at `T=0`, its
fixed scalar coupling `kappa_1`, K141's separate compact joint family
`13 <= |mu| <= 14`, and K138's smooth null quotient. It classifies whether
that family owns an action-specific lower-order coefficient. It does not add a
pseudodifferential action, select a background neighborhood, construct a
closed domain, or decide physical propagation.

## Result in plain English

The original distortion operator has frozen symbol

```text
C(rho,n)=i rho C_1(n)+kappa_1 K,                       (1)
```

where `kappa_1` is one fixed action coupling. K140 introduced
`mu=kappa_1/rho`. For fixed nonzero `kappa_1`, K141's annulus means

```text
13 <= |kappa_1|/rho <= 14
iff
|kappa_1|/14 <= rho <= |kappa_1|/13.                  (2)
```

Equation (2) is a compact frequency band. It is not conic: multiplying a
covector by `t` replaces `mu` by `mu/t` and ordinarily leaves the annulus.
Consequently the fixed action has no homogeneous high-frequency
characteristic family living on K141's annulus and no Dencker subprincipal
coefficient attached to that annulus.

The alternative rule used to obtain uniform graph order is

```text
kappa_1=rho mu,
C_joint=rho(i C_1(n)+mu K).                            (3)
```

In (3), `mu K` is homogeneous order one after restoring `rho`. It belongs to
the promoted principal parameter family. It is not a lower-order coefficient
of that family and it is not the fixed zero-order mass term of one local
`I1B` action.

Turning (3) into an operator would require replacing `rho` by a first-order
pseudodifferential operator. That requires a homogeneous norm or defining
function, quantization, adjoint, covariance statement and equivalence theorem.
The action supplies none. The only Lorentz scalar candidate built directly
from `q=g^{-1}(xi,xi)`, namely `sqrt(|q|)`, vanishes on the null cone, whereas
K141 requires `rho>0` and `13<=|mu|<=14`. A positive auxiliary norm would be a
new background choice and generally not Lorentz invariant.

Thus K143 cannot honestly write the requested five-by-five action
subprincipal matrix. The fixed action does own the zero-order distortion map
`kappa_1 K`, but K132 proves that it makes principal distortion-null rows
algebraically live rather than preserving their candidate identities. K139
also proves that the homogeneous fixed-action DN quotient has dimension
`106634`, not five. Neither fact produces an endomorphism of K138's separate
finite-Schur quotient.

## 0. Pre-wave answers

1. **Construction fork.** A bounded fixed-coupling Fourier band and a conic
   joint semiclassical family are different objects. Dencker/subprincipal
   language requires the latter kind of homogeneous operator data.
2. **Cheapest decisive condition.** Test dilation with `mu=kappa_1/rho` before
   calculating any coefficient. Failure of conicity blocks the proposed
   subprincipal owner at once.
3. **Positive route.** The fixed action remains a legitimate finite-frequency
   local operator on (2), and K141's exact graph remains a uniformly bounded
   algebraic elimination there.
4. **Negative route.** The uniform joint family promotes `K` to principal
   order and requires a new pseudodifferential/action owner before it can
   carry an invariant subprincipal coefficient.
5. **Claim ceiling.** No no-go for bounded-frequency response, no statement
   that a future owned coefficient is zero, and no physical/domain conclusion.

## 1. Fixed-action band versus conic family

For fixed `kappa_1`, dilation `xi -> t xi` gives

```text
rho -> t rho,       mu -> mu/t.                        (4)
```

Taking the interior annulus value `mu=27/2` and `t=2` gives `mu'=27/4`,
strictly outside `[13,14]`. The full positive ray through an annulus covector
therefore is not contained in the annulus. A homogeneous principal symbol and
its subprincipal correction are asymptotic objects on conic sets; (2) is a
spectral band instead.

This does not invalidate K141. Its uniform inverse, graph and derivatives are
exact on the band. It changes the type of the next question: finite-band
operator response and a conic amplitude connection are not interchangeable.

## 2. Symbol-order and action-owner theorem

Under fixed coupling, (1) has

```text
principal order one: i rho C_1(n),
lower order zero:    kappa_1 K.                        (5)
```

Under the joint scaling, (3) has

```text
principal order one: rho(i C_1(n)+mu K),
lower order zero:    not supplied by (3).              (6)
```

Calling `mu K` the subprincipal term in (6) is therefore an order error. It is
precisely the term whose promotion repairs the `mu->0` inverse blow-up. The
repair and the claimed lower-order status cannot both be retained.

Nor can `rho` be silently made into a local differential coefficient. A norm
such as `|xi|_aux` is pseudodifferential and imports an auxiliary positive
structure. `sqrt(|q|)` is invariant but zero on the null characteristic set.
No current source/action record supplies another nonzero homogeneous null-cone
radius with the needed covariance and adjoint properties.

## 3. Quotient basicness disposition

K142 gave the abstract test for a genuine lower endomorphism `L`:

```text
L(H_n) subset H_n modulo the declared equation ideal,
L(G_n) subset G_n.                                    (7)
```

The exact probe plants two lower maps on the same principal quotient data.
One preserves both nested spaces and descends; the other sends a gauge vector
to a nongauge radical class and fails. Since both share the same principal
and graph information, that information does not decide (7).

There are two nearby zero statements that must not be substituted:

- K138's frozen null Schur symbol `-48 ell_n ell_n^T` annihilates `H_n`, so
  the characteristic equation itself induces the zero map on `Q_n`;
- K142's projected graph derivative is zero.

Neither is the missing lower amplitude coefficient. Basicness remains
`UNDEFINED_NO_OWNED_COEFFICIENT`, not pass and not fail.

## 4. Route reassessment and hostile bookends

The materially distinct routes were:

- **fixed-action conic route:** fails because the annulus is the bounded band
  (2), not a conic high-frequency set;
- **joint homogeneous route:** succeeds algebraically but promotes `K` to
  principal order and is not the original fixed local action;
- **Lorentz-scalar quantization:** `sqrt(|q|)` vanishes on the null cone;
- **auxiliary positive norm:** can define a pseudodifferential family but adds
  unowned structure and needs its own action/adjoint/equivalence proof;
- **coefficient brute force:** rejected because there is no typed coefficient
  to compute before the owner and symbol order are fixed.

Strongest overclaim: “no owned annulus subprincipal” is not “the physical
subprincipal is zero.” The artifact keeps those statements separate.

Strongest contrary construction: explicitly add a covariant
pseudodifferential action/reduction with a nonzero null-cone radius, fixed
quantization, adjoint and equivalence theorem. That would create a new testable
owner, but the current action does not already contain it.

Weakest reproducibility seam: the argument assumes the ordinary symbol
meaning of `rho` used in K140-K141 and fixed scalar `kappa_1` from the
displayed action. A separately declared semiclassical parameter independent
of covector dilation would be a new calculus and must state that distinction.

Postflight controls replay K140-K142, check the exact annulus/band arithmetic,
verify the symbol orders, plant good and bad quotient maps, and preserve the
action, quotient and physical ceilings.

## 5. Reverse scaffold and next gate

```text
R0 physical propagation needs an owned closed reduced operator.
R1 K138-K142: exact five-class finite-Schur quotient and natural connection.
R2 K143: fixed kappa turns K141's annulus into a bounded nonconic band.
R3 K143: joint kappa=rho mu promotes K to principal order and is not the
   fixed local action's lower coefficient.
R4 K143: no current action-owned five-class subprincipal coefficient exists;
   radical/gauge basicness is therefore undefined.
R5 K144: on a selected Ricci-flat background neighborhood, extract the actual
   fixed-kappa local operator coefficient and test (7) without using compact-
   annulus conic language; if no source-owned neighborhood/coefficient exists,
   prove that exact missing-owner result.
R6 alternative: explicitly authorize and construct a pseudodifferential,
   gauge or boundary owner before reopening a conic Dencker/domain route.
```

K144 must keep fixed-frequency response distinct from conic transport. It may
use K138's Brinkmann controls to test generic curvature-gradient dependence,
but it must not select a new action, norm, quantization, background, gauge or
boundary law by convenience. Joe input is not required for that bounded
owner audit.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k143_native_i1b_t0_fixed_action_subprincipal_owner_obstruction_probe.py
```

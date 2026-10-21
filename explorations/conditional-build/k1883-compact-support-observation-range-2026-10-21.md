---
title: "K1883: Compact-support observation range and local recovery obstruction"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional compact smooth range and support obstruction for the fixed observation and its rotating repairs; no native GU or physical causality verdict
---

# K1883: Compact-support observation range and local recovery obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact four-charge compact-support range and constructive compact lifting
carrier: K1840 real16 source and real4 target on R3, four coordinate types LAYER=toy CHIRALITY=N/A
pairing: positive source H and target Euclidean form ON=smooth_compactly_supported_fields
real_structure: real coefficient fields and real exponential dual solutions
grading: compact-support range versus maximal L2 range
action_owner: repository-construction -- constant conservative first-order system
target: compact preparation, local right inverses and transported charges MAP-TYPE=quotient
```

## 1. L2 recovery does not imply compact preparation

[K1881](k1881-dynamical-minimum-energy-observation-lift-2026-10-21.md)
proves massive L2 surjectivity and nonlocality of the minimum-energy inverse.
It does not exclude all other local inverses: adding a kernel-valued map can
change support. This result classifies the compact smooth range itself.

For the same fixed mass-direction system, every R in R, write
`O=sum T_i partial_i+R S1`. For all four coordinate types the actual
serialized matrices give
```
Z=stack(T1,T2,T3), rank Z=12,
K=-D1 B1=diag(1,-1,-1,1), K^T=K, K²=I,
S1=24 K T1.                                             (1)
```
With kappa=24R (signed), its exact compact-support range is
```
O(Cc∞(R3,R16))={y in Cc∞(R3,R4):
                 Q_R(y):=integral e^(kappa K x1)y(x) dx=0}. (2)
```
These are four independent real conditions. Consequently no map that sends
every compactly supported smooth y to a compactly supported smooth source
can be a right inverse on all such targets. In particular, no finite-order
linear differential right inverse with smooth variable coefficients exists;
no linearity premise is needed for the stronger support statement.

This is an internal conditional realization, not native GU. SC-OP-04 ASSERTS
candidate four-field grammar, SC-MAS-01 and SC-CHI-02 ASSERTS the stylized
curvature-mass/decoupling toy; SC-OP-05 and SC-META-53 remain UNCERTAIN.
WGS05 does not supply the full20 placement, injection, physical pairing or
observed domain. RA-F1, AC-F1, LT-SM8 and source/ledger/canon verdicts stay
unchanged. A compact-preparation obstruction is not a physical chirality,
family-count or faster-than-light signal claim.

## 2. Exact reduction to a weighted divergence

Set f_i=T_i psi. Since Z has full row rank, every smooth compact tuple
(f1,f2,f3) is realized by psi=N stack(f_i), where a constant right inverse
N of Z is reconstructed separately for each coordinate type. Equation(1) gives
```
O psi=(partial1+kappa K)f1+partial2 f2+partial3 f3,
e^(kappa K x1)O psi=div(e^(kappa K x1)f).                (3)
```
Necessity in(2) follows by integration by parts. More precisely, all smooth
solutions of the formal-adjoint equation O^dagger h=0 are
`h(x)=e^(kappa K x1)c`, c in R4. Indeed invertibility of H and injectivity
of Z^T reduce that equation to
`partial1 h=kappa K h, partial2 h=partial3 h=0`.
There are no other smooth adjoint constraints on this connected whole space.
The growing h are legitimate duals of Cc∞; for R!=0 none is a nonzero L2
function. Confusing these test-function duals with the L2 adjoint kernel would
contradict the valid massive L2 surjectivity result.

## 3. Sufficiency with an explicit compact construction

Given y with Q_R(y)=0, let h=e^(kappa K x1)y. Choose scalar smooth compact
bumps rho_i of integral1 on each coordinate axis, inside a rectangle containing
the coordinate projections of supp h. Set
```
H1(x2,x3)=integral h(s,x2,x3) ds,
H2(x3)=integral H1(s,x3) ds,
F1=integral_(-infinity)^x1 [h(s,x2,x3)-rho1(s)H1(x2,x3)] ds,
F2=rho1(x1) integral_(-infinity)^x2 [H1(s,x3)-rho2(s)H2(x3)] ds,
F3=rho1(x1)rho2(x2) integral_(-infinity)^x3 H2(s) ds.
```
Every primitive is compactly supported: the first two integrands have zero
integral in their integration coordinate; the last has integral zero by
Q_R(y)=0. Differentiation gives div F=h by cancellation of the two marginal
terms. Put f_i=e^(-kappa K x1)F_i and psi=N stack(f_i). Equation(3) proves
O psi=y. This is a linear construction once the rectangle and bumps are fixed,
but it integrates across space and is not a support-preserving pointwise rule.
It may enlarge support within the rectangle. It supplies no uniform norm
bound independent of that rectangle or its location.

The divergence primitive is standard compact-support calculus; the new
repository calculation is its applicability to all four actual observation
matrices and its precise recovery consequences. No novelty claim. The
construction is proved here explicitly rather than inferred from a rank count.

## 4. Strong contrary controls and relation to Hilbert-space results

For any nonnegative nonzero scalar bump rho and any coordinate vector e_a,
y=rho e_a has a strictly nonzero exponential charge. It has a massive L2
lift by K1881 but no compact smooth lift. For every compact vector field f,
y=(partial1+kappa K)f1+partial2 f2+partial3 f3 is a positive existence
control: its charges vanish and (3) constructs a compact lift.

At R=0,(2) becomes the four ordinary mean-zero constraints. This does not
contradict the proper raw massless L2 range in K1881: a compact smooth mean-zero
target has Fourier transform O(|xi|) at zero and meets the Hminus1 condition.
In fact all Cc∞ targets in dimension3 meet that infrared integrability
condition, including those with nonzero mean. The latter have L2 lifts but
still have no compact lift. Do not equate the compact-range restriction with
the entire massless L2 range restriction.

The range in(2) is codimension4 in Cc∞ and dense in L2. For R!=0, cancel
each charge by a fixed bump translated far in the sign direction where that
component's exponential weight grows; its required coefficient and L2 norm
decay exponentially. For R=0, normalized broad bumps have fixed integral and
L2 norm tending to0. Thus the charge functionals are not continuous in the
whole-space L2 topology. Density does not give a compact lift of an arbitrary
fixed target, nor a uniformly support-bounded approximation.

A second independent obstruction covers constant-coefficient polynomial
inverses: at complex frequency xi=(24iR,0,0), R!=0, the full4x16 symbol
`iT_i xi_i+R S1=24R(K-I)T1` has rank2. A polynomial right inverse would
remain a right inverse there, impossible. A real-frequency surjectivity test
would miss this. The support proof is stronger because it also covers smooth
variable-coefficient differential inverses and R=0.

## 5. Dynamics and rotating repairs

Since K=-D1B1, the constant target generator L_Q=d_i partial_i+R B1 has
`L_Q^dagger(e^(kappa K x1)c)=0` exactly. Consequently Q_R(y(t)) is
constant for smooth compactly supported target solutions. On finite time
intervals constant symmetric-hyperbolic evolution preserves compact support
up to a finite propagation cone, so integration by parts is justified.

For any charge-zero compact initial target, construct a compact source at
the initial time as in section3 and evolve by the original source equation.
Intertwining and target uniqueness make its observation equal to the requested
target evolution. The source stays compact on finite intervals. This executes
a dynamically consistent compact lift on the compatible subspace, despite the
absence of an all-target compact right inverse. It need not be the minimum
energy lift; its difference from that lift lies in ker O.

For K1879's repaired rotating frames O_theta(t)=U(t) O W(t)^-1, smooth
unitary multiplication preserves compact supports. The exact criterion is
```
Q_theta,t(y)=integral e^(kappa K x1) U(t,x)^-1 y(x) dx=0. (4)
```
Lift by W times the base compact construction applied to U^-1y. With the full
connection and transported propagator retained, Q_theta,t is constant along
repaired target evolution. Omitting U^-1 gives generally wrong charges;
omitting the time connection invalidates conservation. Smooth phases suffice
on compact sets; the stronger hypotheses in K1881 remain necessary for its
whole-space fixed-domain L2 claims. Odd winding on a torus is a different
domain problem: (2) is a whole-space compact-support theorem, not a torus
zero-mode count.

## 6. Verification and next scientific boundary

The producer checks Z rank/right inverses, S factorization, K identities,
adjoint charges, target stationary duals, and complex rank defects on all
four types. The independent probe reconstructs the weighted divergence from
row actions, verifies a compact polynomial primitive fixture and cancelling
marginal construction, and injects coefficient/sign/mass/domain-report faults.
The analytic compact primitive and propagation arguments carry the continuum
result, not finite checks. Inline hostile review distinguished arbitrary versus
minimum inverses, smooth duals versus L2 kernels, necessary versus sufficient
moment constraints, massless infrared versus compact range, and preparation
versus propagation. No external expert, independent agent or proof assistant.

Native source identification and the pure-mass rotating nonlinear class remain
open. The present exact support obstruction belongs to this fixed observation;
a changed leading observation or target connection is a new class. Repeating
polar decomposition or real-frequency rank cannot remove these four charges.

---
title: "Selected-K101 projected dressed-connection Hamiltonian type gate"
status: active_research
doc_type: exact_conditional_symmetric_pair_projection_and_hamiltonian_type_correction
created: "2026-08-15"
registry: lab/process/selected-k101-rsap-projected-dressed-connection-hamiltonian-type-gate.json
probe: tests/channel-swings/selected_k101_rsap_projected_dressed_connection_hamiltonian_type_gate_probe.py
grade: "BALANCED DRESSED-CONNECTION SPLIT EXACT; ZERO SELF-HESSIAN TEST WITHDRAWN; SOURCE-OWNED HAMILTONIAN MULTIPLIER TYPE-MISSING"
target_claim: K100_NEXT_GATE__PROJECTED_NORMAL_H_BAL_COMPONENT_IS_RELEASED_ACTION_MULTIPLIER
target_verdict: TYPE_MISSING_AT_SOURCE_HAMILTONIAN_GRADE
canon_verdict_change: none
---

# Selected-K101 projected dressed-connection Hamiltonian type gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> connection, action and boundary problem. Ordinary Higgs/VEV, family-index,
> net-chirality and familiar four-dimensional gauge-model conclusions are not
> substitutes for Weinstein's objects. Use
> `lab/methods/source-native-comparator-routing.md` before importing any such
> comparator.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE`

## Result first

Conditional on K100's one balanced seed `R_0`, the dressed source connection
does split exactly and without another field:

```text
theta(X) = R_0 X R_0
P_h(X)   = (X+theta(X))/2
P_p(X)   = (X-theta(X))/2
B(epsilon) = a + phi,  a=P_h B(epsilon),  phi=P_p B(epsilon).
```

The ranks are `42+49`. Under a local right `H_bal` change of the epsilon
frame, `a` transforms as an `H_bal` connection and `phi` transforms
homogeneously. The exact bracket laws are

```text
[h,h] subset h,   [h,p] subset p,   [p,p] subset h.
```

Thus the projection step of Variancer's reverse scaffold is closed.

The requested variational conclusion is not. The released records do not
supply a preferred codimension-one non-null collar, a normal evolution
direction, a Legendre map for the full source action, or a canonical action
written in these projected variables. This is not a mere missing
calculation: Weinstein explicitly distinguishes the ordinary one-time
Hamiltonian problem from the ambient multiple-time ultrahyperbolic problem
and leaves the latter as technical debt. A conditional local collar can be
chosen, but that choice is not source selection.

K100's proposed `zero self-Hessian` criterion is also withdrawn. It is not a
necessary test for a connection multiplier. A connection's normal component
may occur quadratically in a covariant second-order Lagrangian while carrying
no normal velocity; after the Legendre transform and spatial integration by
parts it occurs linearly and imposes Gauss law. The correct test is the
**normal-velocity Legendre kernel**, followed by an explicit canonical
coupling—not the coordinate self-Hessian of the unsplit action.

The honest verdict is therefore:

```text
balanced h+p projection:                         EXACT CONDITIONAL
right-H transformation typing:                   EXACT CONDITIONAL
zero-self-Hessian as necessary multiplier test:  FALSE / WITHDRAWN
source-owned normal or one-time collar:           TYPE-MISSING
released-action projected Legendre transform:     TYPE-MISSING
a_normal imposes J_R,H_bal=0:                     NOT ESTABLISHED
```

## The exact conditional split

A `Q`-self-adjoint involution with `R_0^2=1` is `Q`-orthogonal, so conjugation
by it is an involutive automorphism of `so(7,7)`. Its fixed and anti-fixed
spaces are

```text
h_bal = so(3,4)+so(4,3),  dim 42,
p_bal = off-diagonal balanced block, dim 49.
```

For `h(x) in H_bal`, right dressing gives

```text
B(epsilon h)=h^-1 B(epsilon) h+h^-1 d h,
a'            =h^-1 a h+h^-1 d h,
phi'          =h^-1 phi h.
```

Infinitesimally, for `xi in h_bal`,

```text
delta a   = d xi+[a,xi],
delta phi = [phi,xi].
```

These identities prove that the 42-component piece has the *geometric type*
needed for a subgroup connection. They do not prove that its normal component
is an independent Euler multiplier or that right `H_bal` has been selected as
gauge. Those remain variational and boundary questions.

## Why the old Hessian test was wrong

Consider the exact finite analogue

```text
L = 1/2 ||v-D a_0||^2,
```

where `D` is a nonzero skew spatial-difference operator. There is no velocity
`dot(a_0)`, so the Legendre velocity Hessian has a kernel in every `a_0`
direction. Yet the ordinary coordinate Hessian is

```text
d^2 L / d a_0^2 = D^T D != 0.
```

With momentum `e=v-Da_0`, the first-order action is

```text
<e,v>-1/2||e||^2-<e,D a_0>
= <e,v>-1/2||e||^2-<a_0,D^T e>,
```

so `a_0` is linear and imposes the Gauss-type constraint `D^T e=0`. The
probe verifies this identity over exact integers and also verifies that the
coordinate Hessian is full rank while the missing-velocity block is zero.

This counterexample does not identify Weinstein's action with ordinary
Yang--Mills. It corrects a general variational diagnostic that K100 proposed
using. The source-native action must still be decomposed on its own terms.

## What a conditional Hamiltonian split would have to produce

If a non-null collar and Legendre map are supplied, decompose tangential
connection and momentum variables as

```text
A_i=a_i+phi_i,   E^i=e^i+pi^i.
```

The symmetric-pair identities force the projected full Gauss expression to
have the form

```text
G_h = partial_i e^i+[a_i,e^i]+[phi_i,pi^i],
G_p = partial_i pi^i+[a_i,pi^i]+[phi_i,e^i].
```

The `p`-sector current `[phi_i,pi^i]` in `G_h` is compulsory. Omitting it is
not the balanced subgroup Gauss law. But even deriving `-<a_normal,G_h>` from
the source action would not yet prove `G_h=J_R,H_bal`: K97's `J_R` is the
right moment map on the epsilon endpoint cotangent parent, while a bulk Gauss
covector and its boundary flux require an explicit preboundary bridge.

This exposes two separate remaining identifications:

1. source action `->` projected canonical Gauss covector `G_h`;
2. projected Gauss boundary flux `->` endpoint right moment map `J_R,H_bal`.

The charged-boundary versus gauge horn then still decides whether the zero
level is imposed or retained as a physical charge.

## Source and claim ceiling

The 2021 source owns `I1B`, `I2B`, the dependent gauge-rotated connection
`B(epsilon)`, the independent `varpi`, and `T=varpi-B(epsilon)`. It does not
print the balanced projection, collar, canonical momenta, projected Legendre
map or the desired `-<J_R,a_normal>` term. The 2025 transcript explicitly
confirms the one-time versus multiple-time distinction and the unresolved
ultrahyperbolic Hamiltonian problem.

Accordingly, the earlier pointwise Hessian certificates remain valid for the
pointwise questions they answered, but they cannot decide this canonical
normal-component role. Nonzero pointwise response is neither a proof nor a
disproof of a normal Gauss multiplier.

No ledger, datum, quotient, canon claim, public posture, W/mirror choice,
chirality or generation count changes.

## Corrected next gate

Do not compute another pointwise self-Hessian. Supply or derive one explicit
source-compatible **non-null collar/domain and Legendre map** for `I1B` (and,
separately if relevant, `I2B`). Then test in order:

1. the normal velocity of `a_normal=P_h B(epsilon)(n)` is absent or lies in
   the Legendre radical;
2. the canonical action contains `-<a_normal,G_h>` with the full mandatory
   `[phi,pi]` current;
3. the preboundary map identifies the boundary flux of `G_h` with K97's
   `J_R,H_bal` coefficient by coefficient; and
4. the boundary disposition selects its zero level rather than the charged
   horn.

Until all four pass, the projected field is an exact conditional connection,
not an action-owned multiplier. Reproduce with:

```bash
python3 tests/channel-swings/selected_k101_rsap_projected_dressed_connection_hamiltonian_type_gate_probe.py
```

> **Successor correction (K102).** The conditional local `I1B` partial
> Legendre split is now exact. `B(epsilon)_n` contains the epsilon normal
> velocity and is not the multiplier. The independent `varpi_n` is affine in
> the canonical action, but it imposes the diagonal full-`G` equation
> `Div(Pi)-lambda=0`. Its balanced projection equates `lambda_h` to bulk flux;
> it does not impose the standalone `J_R,H_bal=lambda_h=0` level. The next gate
> is boundary ownership/polarization, not another collar Hessian.

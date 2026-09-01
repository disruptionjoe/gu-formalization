---
title: "K77 I1B action-induced connection wave"
status: active_research
doc_type: reverse_scaffold_i1b_repository_owned_action_connection_result
date: 2026-09-01
claim_ceiling: exact repository-owned conditional quadratic action whose variable covariant derivative induces the fixed-stratum I1B quotient connection and computed hyperbolic holonomy; no source-native coupled Hessian, cross-null bundle, selected majorant, prediction, confirmation, or verdict
manifest: lab/process/k77-i1b-action-induced-connection-wave.json
probe: tests/channel-swings/k77_i1b_action_induced_connection_probe.py
---

# K77 I1B action-induced connection wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: repository-owned I1B quadratic covariant action inducing a curved fixed-stratum quotient connection and computed hyperbolic holonomy
carrier: H1 sections of the native rank-220 timelike I1B fibre split as rank-196 radical plus rank-24 Green quotient LAYER=conditional CHIRALITY=N/A
pairing: native nondegenerate alternating Green form J on the quotient ON=timelike_fixed_rank_candidate_action
real_structure: real I1B fluctuation carrier in one global candidate trivialization
grading: radical gauge summand to quotient short sequence; not a nonlinear BV master complex
action_owner: repository-owned reverse-scaffold candidate; not the source-native complete coupled I1B Hessian
target: action-to-connection-to-curvature-to-holonomy descent on one fixed-rank timelike slab MAP-TYPE=construction
```

## The connection is now a written action coefficient

Let the native timelike I1B fibre split as `E=K_196 direct_sum Q_24`, with
`K` the Green radical and

```text
J = [[0,I12],[-I12,0]]
```

the descended alternating form on `Q`. On

```text
M = [0,1]_t x [0,1]_x x [0,1]_y
```

write `H=diag(I12,-I12)` and the covariant derivative

```text
D_A = d + A,       A_t=0,       A_x=0,
A_y = log(2) x H.
```

The repository-owned conditional action is

```text
S_A[k,q] = 1/2 integral_M (
    |D_t q|^2 - |D_x q|^2 - |D_y q|^2 - |q|^2
).
```

The radical field `k` is absent, so arbitrary shifts in `K` are gauge. The
action Hessian is the complete variable-coefficient operator
`D_A^*D_A+1` on `Q` and zero on `K`. Thus, for this candidate, the connection
is not supplied after the fact: it is a written coefficient of the quadratic
action and its Hessian.

Because `H^T J+JH=0`, `A` is `sp(24,R)`-valued and preserves the native Green
form. The `K` summand is parallel, so the connection descends through the
closed direct-summand functional quotient to `Q`.

## Curvature and loop transport

The induced curvature is

```text
F_A = log(2) H dx wedge dy.
```

All connection values commute. Transport around the positively oriented unit
rectangle at fixed `t` is therefore

```text
Hol_A = exp(-log(2) H)
      = diag((1/2)I12,2I12).
```

The result has determinant one, characteristic polynomial
`(lambda-1/2)^12(lambda-2)^12`, minimal polynomial
`(lambda-1/2)(lambda-2)`, and 24 one-dimensional eigenspaces. It preserves
`J` and no positive majorant: on a half-eigenvector, invariance would imply
`g(v,v)=g(v,v)/4`.

The exact certificate passes `18/18`; its hostile selftest catches `13/13`
mutations. It checks that the connection occurs in the action/Hessian, not
only in a holonomy declaration.

## Ownership and nonselection boundary

This advances the prior packet from a *supplied compatible connection* to an
*action-induced connection for a complete repository-owned quadratic
candidate*. It still does not reconstruct the source-native coupled I1B
Hessian. The written action is a reverse-scaffold candidate built to meet the
frozen connection/domain demands, and it does not cross the rank-24/rank-22
null jump.

Nonselection remains exact. Replacing `log(2)` by `log(3)` gives another
Green-compatible repository-owned action on the same domain and quotient,
with holonomy `diag((1/3)I12,3I12)`. Native fibre and Green data therefore do
not choose either coefficient. Neither candidate preserves a positive
majorant.

No source-selected background, physical gauge/BV quotient, nonlinear
interaction, cross-null connection, positive-majorant selection, observable
export, prediction or confirmation follows. Delayed-choice entanglement
swapping remains reserved and unscored.

## Next condition

The next I1B gate is no longer merely to attach an action to a connection. It
is to select or falsify the candidate coefficient from a source-owned coupled
Hessian term, a cross-stratum singular-reduction theorem, or an independent
physical requirement with declared decision power between the `log(2)` and
`log(3)` actions.

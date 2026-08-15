---
title: "Selected-K99 balanced RSAP multiplier-owner exhaustion"
status: active_research
doc_type: exact_minimal_gauged_completion_and_current_owner_exhaustion
created: "2026-08-15"
registry: lab/process/selected-k99-rsap-balanced-multiplier-owner-exhaustion.json
probe: tests/channel-swings/selected_k99_rsap_balanced_multiplier_owner_exhaustion_probe.py
grade: "MINIMAL RIGHT-H_BAL MULTIPLIER COMPLETION CONSTRUCTED; CURRENT SERIALIZED ACTION OWNS NEITHER THE BALANCED PROJECTOR NOR ITS MULTIPLIER"
target_claim: K98_NEXT_GATE__SOURCE_OR_CURRENT_ACTION_OWNS_RIGHT_H_BAL_MULTIPLIER_CONNECTION_OR_BOUNDARY_GAUGE_TERM
target_verdict: CURRENT_SERIALIZED_NO__MINIMAL_NEW_COMPLETION_EXACT
canon_verdict_change: none
---

# Selected-K99 balanced RSAP multiplier-owner exhaustion

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE`

Scope: the released source/action records, their formal epsilon preboundary
cotangent parent, and the reverse-constructed balanced symmetric pair. This is
not a universal nonexistence theorem about unreleased GU actions or every
Hamiltonian/collar decomposition of the field theory.

## Result first

K98's required completion can be written exactly. In left trivialization let

```text
g in G = Spin_0(7,7),
lambda in g*,
a_t in h_bal = so(3,4) + so(4,3),
v = g^(-1) dot(g).
```

The minimal first-order constraint sector is

```text
L_min = <lambda, v - a_t>.
```

For a time-dependent `xi in h_bal`, the infinitesimal law

```text
delta_xi g      = g xi,
delta_xi lambda = [lambda,xi]       (under the invariant trace pairing),
delta_xi a_t    = dot(xi) + [a_t,xi]
```

gives `delta_xi L_min=0` exactly. Independent variation of the 42 components
of `a_t` gives

```text
J_R,H_bal(g,lambda) = lambda restricted to h_bal = 0.
```

Its Jacobian has rank `42`; the multiplier Hessian in the `a_t-a_t` block is
zero and the mixed `lambda-a_t` block has rank `42`. The resulting constraint
surface and quotient are therefore exactly K98's regular sequence

```text
182 -> 140 -> 98.
```

Local gauge invariance supplies the Noether identity, and K98 supplies the
already-closed irreducible classical BFV charge. The multiplier construction
is canonical up to an invertible invariant pairing/rescaling on the two simple
factors; those presentation choices do not change the zero set.

This is the exact mathematical answer to what the missing term must look like.
It is **new completion data**, not a term recovered from the current serialized
action.

## The owner stack exposed by reverse scaffolding

The reverse build had compressed three logically separate owners into the
phrase “add a multiplier”:

1. a balanced involution `R_0` or equivalent reduction datum selecting
   `h_bal` inside `so(7,7)`;
2. the declaration that local right `H_bal` transformations are gauge rather
   than charged boundary symmetries; and
3. an independent `h_bal`-valued multiplier/connection component `a_t` whose
   Euler equation is the right moment constraint.

K98 then makes the ghost sector canonical. The current source/action record
owns none of the first three. In particular, a full `so(7,7)` connection is
not enough: without an owned projector it produces a full-algebra Gauss law,
not the required 42 balanced constraints.

The mismatch is exact. The source-selected physical K77 split is

```text
(1,3) + (6,4),
dim[so(1,3)+so(6,4)] = 6 + 45 = 51.
```

The reverse RSAP split is

```text
(3,4) + (4,3),
dim h_bal = 21 + 21 = 42.
```

Reducing `T*G` by the physical-split stabilizer would have formal dimension
`182-2(51)=80`, not `98`. Equal ambient group and the word “split” do not
identify these subgroup objects.

## Exhaustion of current no-new-field candidates

| candidate owner | exact disposition |
|---|---|
| existing epsilon `g` | It is the configuration coordinate. Free endpoint variation forces all 91 momentum components to zero, which is stronger than `J_R,H_bal=0`; fixed epsilon supplies no constraint. It is not an independent multiplier. |
| restrict epsilon variations to `h_bal` | This can impose a partial variational boundary condition, but it first assumes the unowned balanced projector and does not declare the characteristic right action gauge. Like K98's invariant graph, it selects boundary data rather than the full reduced phase space. |
| project `B`, `varpi`, or their endpoint pullback to `h_bal` | The projection already requires the unowned `R_0`. At the certified pointwise grades the connection sectors have genuine nonzero quadratic response rather than an algebraic multiplier block. A future Hamiltonian normal/tangential split is not excluded, but none is serialized or certified here. |
| dress a full connection by epsilon and project | This is a legitimate new Stueckelberg-like construction, but it still imports `R_0` and a new coupling to `J_R`; neither occurs in the released action grammar. A composite is not an independent Euler owner unless the varied field and boundary term are supplied. |
| reuse the earlier edge field | The edge horn is conditional on first declaring all boundary transformations gauge. It restores horizontality while preserving generic charge; it does not select `H_bal`, impose this zero level, or settle gauge versus charged symmetry. |
| introduce independent `a_t in h_bal` | This is the exact minimal completion above. It works, but it is a new field/term and therefore cannot certify present action ownership. |

This exhausts the current serialized, no-new-field candidates at the available
preboundary and pointwise variational grades. It does not forbid an unreleased
action term, a source-owned moving order parameter, or a full Hamiltonian
decomposition that proves an existing normal connection component has exactly
this role.

## Source and action boundary

The source return owns epsilon, `B(epsilon)`, `T=varpi-B(epsilon)`, and their
variation. The released zero-fermion action grammar owns `I1B` and `I2B`; it is
silent on an additional balanced boundary multiplier coupling. The selected
action's exact preboundary analysis makes compactly supported transformations
gauge/basic but leaves unrestricted endpoint transformations with a live
charge unless a boundary disposition or edge completion is added.

The existing connection-Hessian results add a narrower point: at their
certified pointwise grades, `B` and `varpi` cannot simply be relabelled as a
zero-Hessian algebraic multiplier. They do not settle a not-yet-constructed
Hamiltonian collar split, so this result does not claim that no component of a
future canonical decomposition could serve as `a_t`.

> **Successor correction (K101).** Nonzero coordinate self-Hessian is not a
> negative test for a normal connection multiplier. The canonical test is
> absence of normal velocity (a Legendre-kernel statement), followed by the
> explicit linear Gauss coupling after transformation. K101 leaves that
> source-owned collar and Legendre construction type-missing.

## Hostile boundary and claim ceiling

- The completion proves mathematical gauge invariance, the Euler constraint
  and the finite Noether identity. It does not prove a source-selected boundary
  time, analytic domain, quantum BRST operator, positivity or physical
  cohomology.
- The physical K77 split is not “close enough” to the balanced split: its
  stabilizer dimension and resulting reduction dimension are different.
- Conversely, absence from the inspected serialized grammar is not universal
  nonexistence. A newly located source term or an exact Hamiltonian split can
  reopen ownership.
- Ordinary Higgs, family-index and chirality comparators have no bearing on
  this source-native classical moment-map question and may not be substituted
  for the missing owner.

## Next gate

The highest-leverage successor is no longer another BFV or multiplier-algebra
calculation. Construct or obstruct an **action-owned balanced reduction
datum**: an involution/order parameter `R` with eigenspace signatures
`(3,4)|(4,3)` whose stabilizer is exactly `H_bal`. Then perform a boundary
Hamiltonian/collar decomposition and ask whether an existing normal connection
component becomes an independent `h_bal` multiplier with coupling
`-<J_R,a_t>`. Both layers must pass. A normal multiplier for the full algebra,
or for the source physical-split stabilizer, does not recover the 98D RSAP.

No ledger, datum, quotient booking, canon claim, public posture, W/mirror
choice, chirality or generation count changes.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k99_rsap_balanced_multiplier_owner_exhaustion_probe.py
```

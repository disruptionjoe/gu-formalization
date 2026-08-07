---
title: "G1 derivative cocycle and moving reference: construction, quotient correction, and G2 handoff"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: lab/process/runs/GUH-20260731T140229Z-g1-derivative-cocycle-moving-reference/run-plan.md
specification: lab/specifications/g1-global-tilted-moving-reference-packet-2026-07-31.md
certificate: lab/process/g1-derivative-cocycle-certificate.json
probe: tests/channel-swings/g1_derivative_cocycle_moving_reference_probe.py
grade: "G1 CONDITIONAL PASS. The full first-jet connection cocycle, tilted subgroup, displacement, moving LC/reductive reference, lift/patch descent, conjugation law, fixed-fibre quotient, and stabilizer correspondence are constructed exactly. The native induced Spin bundle needs no new local reference coefficient. A selected global reduction sector, equivalence to Conn(P)/G, complete source action, Noether identity, VEV, Higgs, index, count, and cosmological output remain unbuilt."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# G1 derivative cocycle and moving reference

## Result first

G1 succeeds, conditionally and with a useful correction.

The full connection cocycle

\[
q_A(g)=A-\operatorname{Ad}_gA+(dg)g^{-1}
\]

retains every algebraic payoff of the finite E0 shadow:

- its graph is a subgroup of the inhomogeneous gauge group;
- the distortion is invariant under the left tilted copy;
- it transforms by the adjoint under the right tilted copy; and
- its two-sided stabilizer is exactly the adjoint stabilizer of the resulting
  distortion.

The derivative term is indispensable. A gauge transformation can have
`g(y0)=1` and `dg(y0)!=0`; every zero-jet coboundary vanishes at that point,
while the connection cocycle does not.

The moving reference can also be built. On the native bundle induced from the
`Spin_0(9,5)` frame bundle, the trace-reversed Levi--Civita connection extends
through a moving reduction and is independent of the local lift. It remains
right-quaternionic and preserves the moving `(9,5)` soldering. On a general
`G`-bundle, existence and topological component of the reduction remain a
real global condition.

The correction is the quotient. At fixed reference, the tilted double-action
groupoid is

\[
[\Omega^1(Y,\operatorname{ad}P)/\mathcal G]_{\rm Ad},
\]

not automatically the ordinary affine connection quotient
`[Conn(P)/calG]`. When the reference moves, the reduction/reference field
travels with it, so the natural object is

\[
[\mathcal E_{\rm ref}\times
\Omega^1(Y,\operatorname{ad}P)/\mathcal G].
\]

Erasing `E_ref` requires another theorem: an equivariant, essentially unique,
stabilizer-preserving reference owner. G1 does not assume it.

## Plain English

Eric's core idea survives the first global repair. The missing derivative
does not wreck the tilted construction. Instead, it tells us what the
construction really is.

We need two different actors. A gauge transformation changes frames and
carries the derivative `dg`. A moving soldering/reduction field tells us which
copy of the Lorentz/Spin geometry is being used inside the much larger gauge
bundle. From that reduction we can transport the Levi--Civita connection.
Their interaction produces a family of tilted subgroups that move together.

What we cannot yet say is that this family is simply “the usual space of
connections modulo gauge.” The moving reference is extra configuration until
the action makes it a unique composite or selects it dynamically. That is not
a failure of the source-action route. It is exactly the field-space choice G2
now has to expose before varying anything.

## 1. Layer-0 adjudication

### `epsilon` versus `epsilon_IG`

The podcast/draft `epsilon` is used as a gauge transformation. The old
construction's `epsilon_IG` moves the Clifford plane/reduction. They are
homonyms. The constructed relation is the gauge action

\[
g:\epsilon_{\rm red}\longmapsto g\epsilon_{\rm red},
\]

not an equality of fields.

### “Gauge-rotated Levi--Civita”

There are now two precise rivals:

1. extend the native Levi--Civita Spin connection through the moving
   reduction; or
2. project a supplied transforming `G`-connection `A0` onto the moving
   stabilizer algebra.

They agree only if

\[
\operatorname{pr}_{\mathfrak h}
(u^{-1}A_0u+u^{-1}du)=\omega_{\rm LC}.
\]

The phrase no longer hides the fork.

### “Double coset equals A/G”

The exact fixed-reference result is an adjoint distortion quotient. The
ordinary connection quotient uses an affine action. Their stabilizers already
separate in the pure-jet plant: `T=0` is fixed by every adjoint action, while a
generic connection is moved by a gauge transformation with value one and
nonzero derivative. Thus set-level cancellation of two `G` symbols cannot
establish stack equivalence.

## 2. Construction

Use the left connection convention

\[
g\boldsymbol\cdot A=\operatorname{Ad}_gA-(dg)g^{-1}.
\]

The derivative cocycle satisfies

\[
q_A(gh)=q_A(g)+\operatorname{Ad}_gq_A(h).
\]

For

\[
\mathrm{IG}=\mathcal G\ltimes
\Omega^1(Y,\operatorname{ad}P),
\quad
(g,a)(h,b)=(gh,a+\operatorname{Ad}_g b),
\]

put

\[
\tau_A(g)=(g,q_A(g)),
\quad
\Theta_A(g,a)=\operatorname{Ad}_{g^{-1}}(a-q_A(g)).
\]

The E0 identities now hold with the full first jet. The earlier E0
coefficient plant selected consistency between its chosen `tau` and `Theta`;
it did not independently derive the physical coefficient of `dg`. Here that
coefficient comes from the declared transformation law of a connection and
is not counted as constraint surplus.

For a moving reduction with local lift `u`, the native branch is

\[
A_{\rm LC}(\epsilon_{\rm red})
=u\omega_{\rm LC}u^{-1}-(du)u^{-1}.
\]

If `u->uh`, the connection on the reduction changes inhomogeneously and the
two derivative terms cancel. The planted bare `-(du)u^-1` expression fails
this test.

The RB3 comparator is

\[
B=u^{-1}A_0u+u^{-1}du,
\quad
\Gamma_\epsilon^{A_0}
=u\operatorname{pr}_{\mathfrak h}(B)u^{-1}-(du)u^{-1}.
\]

It descends because the reductive projection is `Ad_H`-equivariant. It is
gauge covariant only when `A0` transforms. The inert-background plant fails.

## 3. Global and native checks

### Patch law

When a transition function `k_ij` changes the local gauge frame, both the
reduction and the reference connection move. The exact conjugation law is

\[
q_{k\epsilon}(kgk^{-1})
=\operatorname{Ad}_k q_\epsilon(g).
\]

Therefore transition functions carry one tilted subgroup to the next and
carry `Theta` homogeneously. Freezing the local reference breaks this law.

### Trace reversal

The exact control reconstructs the four negative directions of the native
metric fibre: the trace line plus the three time--space symmetric directions.
The six complementary directions are positive. A Lorentz boost generator
acts infinitesimally skew with respect to this trace-reversed form. Hence the
LC reference lives on the `(6,4)` native fork rather than silently reverting
to raw `(7,3)` Frobenius geometry.

### Right quaternions

The native connection acts on the left of the quaternionic spinor module.
The probe verifies that a left quaternionic generator commutes with an
independent right quaternionic scalar and rejects the planted claim that
arbitrary left generators commute. No hidden complex polarization is used.

## 4. Quotient and stabilizer theorem

For `omega=(g,a)`, left multiplication by `tau_A(g^-1)` gives the unique
canonical representative

\[
(1,\Theta_A(\omega)).
\]

and the residual right action is adjoint. If `h` stabilizes `Theta`, the
unique left factor that stabilizes `omega` is

\[
k=gh^{-1}g^{-1}.
\]

The probe verifies both directions on a noncommuting exact fixture and rejects
a generic nonstabilizing factor.

This is stronger than a set-level orbit calculation because it preserves the
isotropy information needed for an action groupoid or stack. It is also why
the correction to `[Conn/G]` matters.

## 5. Datum and surplus consequence

G1 does not add a fitted local coefficient on the native induced bundle. The
LC reference is a graph composite of the native metric, Spin reduction, and
moving reduction field.

It does expose three quantities that G2 must price honestly:

1. the global/topological component of the reduction;
2. whether the reduction is varied, boundary-supplied, or action-selected;
3. whether the native LC graph or the `A0` reductive graph is used.

These are not P1, P2, or P3. The constraint surplus remains
`UNCOMPUTABLE`; the cocycle, homomorphism, and equivariance identities are
algebraically linked and cannot be counted as independent empirical
constraints.

## 6. What G1 changes downstream

G2 can no longer write an action over an ambiguous list such as
`(A,varpi,epsilon)`.

The recommended field policy is:

```text
free fields:          varpi and the other declared source fields
varied reduction:     epsilon_red
graph composite:      A_ref = A_LC(epsilon_red, g_DW)
gauge parameter:      g, never varied as a physical field
hostile comparator:   A_ref = Gamma_epsilon^A0 with transforming A0
```

Because `A_ref` contains `d epsilon_red`, varying the action necessarily
produces an integration-by-parts term and boundary potential. That obligation
now enters G2/G3 by construction rather than being discovered after a Noether
claim.

The quotient correction also tells G2 what a native bosonic Shiab must act
on: the adjoint distortion and its density-dual Euler response on the full
field groupoid, not a falsely erased connection-moduli coordinate.

## 7. Validation

The executable probe reports:

```text
G1-DERIVATIVE-COCYCLE-MOVING-REFERENCE:
19 exact checks + 10 planted failures = 29 PASS
```

The plants cover the missing jet, frozen patch reference, bare Maurer--Cartan
lift, inert `A0`, false LC identification, generic stabilizer, false quotient
equivalence, and fake quaternionic commutativity.

## Boundary

G1 is a construction result, not a source-action or phenomenology verdict.
It does not select a global reduction component, identify the N1 independent
`U`, prove a full quotient equivalence, produce a differentiable action or
Noether identity, or move any VEV, mass, index, observed count, cosmological
amplitude, or PP3 claim.

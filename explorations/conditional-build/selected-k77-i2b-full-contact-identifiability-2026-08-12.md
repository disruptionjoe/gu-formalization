---
title: "Selected K77 I2B full-contact identifiability gate"
status: exploration
created: 2026-08-12
canon_verdict_change: none
---

# Selected K77 I2B full-contact identifiability gate

## Result

The v0.218 state-dependent observer line cannot yet be promoted through the
full moving observation contact—and it cannot be killed there either.  The
reason is now exact: every currently constructed restricted derivative leaves
one ambient first normal jet of `Upsilon` undetermined, and that jet controls
which observer stratum the total section derivative occupies.

All owned pieces compose consistently:

- co-moving metric/Hodge/Shiab/frame transport is functorial and does not
  choose the missing normal jet;
- the fixed-`varpi` radial Levi-Civita chain has four live residual derivatives
  but zero first action derivatives by exact grade orthogonality;
- observation is a dependent graph-section receiver, not a second action
  field; and
- restricted pullback does not determine the ambient derivative normal to the
  observation section.

Thus the total response has the chain-rule form

```text
D_total Upsilon = D_restricted Upsilon + (D_normal Upsilon) J_section.
```

The second term is the one unbuilt owner.

## Paired exact completions

At an adapted timelike line the active four response coordinates decompose
under the stabilizer as `1 + 3`.  The rank-ten observation normal contains a
scalar trace line.  A coefficient `q` mapping that normal scalar to the active
response scalar is therefore exactly `SO(3)`-equivariant; covariance does not
fix its value.

Three exact completions, all sharing the same restricted derivative, show the
consequence:

1. `q=0` preserves a response with `A>0` and hence preserves the simple line.
2. An equivariant scalar contact cancelling the active scalar sends that same
   restricted response to `A=0` and destroys selection.
3. Starting from a nonzero restricted response with `A=0`, an equivariant
   scalar contact creates `A>0` and hence creates a simple line.

The scalar-contact discriminant is

```text
A_contact = (a0 + q s)^2 + a1^2 + a2^2 + a3^2.
```

The line survives exactly when this is nonzero.  Any nonzero active spatial
component protects it from scalar contact, while a purely scalar response can
hit the cancellation locus.  This means selection is locally robust and
generic, but not determined by the data currently in the repository.

## Layer-0 fence

This is an identifiability theorem, not a constructed full-contact answer.
The paired extensions are witnesses that present premises are insufficient;
none is adopted as physics.  Restricted pullback, ambient normal jet,
co-moving coefficient transport, fixed-`varpi` Levi-Civita contact, observer
Euler tensor and physical stress-energy remain different objects.

Likewise, a simple timelike line is not a time arrow, and a lossless
observation receiver is not a quotient or a presymplectic phase space.

## Constraint-surplus reading

The missing object is no longer “all moving terms.”  It is the source-native
first normal jet

```text
J1_normal(Upsilon_B)
```

on the observation graph.  Supplying a fitted scalar `q` would consume freedom
and has zero derivational standing.  Constructing the complete jet from the
two-connection/augmented-torsion/observation geometry can instead be tested
against the exact discriminant above and the full non-scalar response.

## Hostile scope

The strongest contrary reading is that the scalar contact witnesses are too
small to represent the actual source jet.  That does not weaken the
identifiability result: one admissible unowned equivariant coefficient is
enough to prove nonuniqueness from current premises.  It does mean that these
witnesses say nothing about which outcome the actual source-native jet will
produce.

The result therefore does not justify booking an external normal jet, removing
the observer cost globally, changing the action, or inferring a domain,
spectrum, stability, arrow, BV quotient or physical stress tensor.

## Accounting

No datum, residue, quotient, parameter, P1/P2/P3, canon verdict or public
posture moves.  The three-function observer cost remains conditionally avoided
only after the actual total response is shown to lie in `A>0`.

## Verification

`selected_k77_i2b_full_contact_identifiability_probe.py` passes `45/45`,
including three planted failures.  It replays v0.218, verifies the exact
`SO(3)` intertwiner, constructs preserve/destroy/create completions, and derives
the scalar-contact discriminant exactly.

## Next gate

Construct the source-native ambient first normal jet of `Upsilon_B` from the
two-connection, gauge-rotated Levi-Civita, augmented-torsion and observation
section grammar.  Then insert that one owned jet into the total chain rule and
recompute the coupled observer tensor.  Retain both `A=0` and a protected
nonzero-spatial fixture as controls; do not fit `q`.

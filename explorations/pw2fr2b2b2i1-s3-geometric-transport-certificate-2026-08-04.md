---
title: "PW2F-R2B2B2I1 exact S3 geometric-transport certificate"
status: reconstruction
doc_type: exploration
updated_at: "2026-08-04"
run_id: RUN-20260804-163503-gu-formalization-pw2fr2b2b2i1-s3-geometric-transport
---

# PW2F-R2B2B2I1 exact S3 geometric-transport certificate

## Outcome

The finite subgroup that permutes the three positive base axes now has a
durable exact certificate on the complete geometric input layer used by the
conditional active coefficient evaluator. Both registered generators pass:

```text
BOTH_S3_GENERATORS_CERTIFIED_ON_UNIVERSAL_OWNER_CONORMAL_GEOMETRIC_TRANSPORT_LAYER
```

This admits the finite action and its 380 joint label orbits as the next
implementation candidate. It does **not** promote a 380-representative action
evaluator. The remaining `Phi`/Hodge/Shiab, residual, moving-primalizer, and
action layers have not received universal durable certification. The
unconditional fallback therefore remains `1,925` cells per bank.

## Layer 0

The following objects remain separate:

- the public `(7,7)` source action presentation and active trace-reversed
  `(9,5)` repository reconstruction;
- the finite S3 label action and the induced nonlinear geometric transport;
- geometric transport and full evaluator equivariance;
- an orbit representative set and a computed complete coefficient bank;
- the separate conditional-active `I1 A4` and `I2B C4` banks; and
- the Eric construction and Curt's formally separated rival track.

The source is silent on this active finite reduction. The result is entirely
repository-derived and is graded only at its executed structural scope.

## Exact finite action

The two base generators are the reflection `tau01` and positive-axis cycle
`cycle012`. They have exact orders two and three and generate six elements.
Each preserves

```text
G4 = diag(1,1,1,-1)
```

and induces an exact bijection of the ten coordinate `Sym2` owners. Passing to
the point-orthonormal fourteen-coordinate frame gives a constant action that
preserves the active

```text
ETA = diag(1,1,1,-1, +1 x 6, -1 x 4).
```

For each generator, the exact probe verifies:

- the base DeWitt tensor;
- all `10/10` first owner derivatives;
- all `100/100` ordered second owner derivatives;
- all `40/40` owner/conormal connection-column generators;
- all `10/10` normalized-trace owner directions;
- closure of the 35-point quartic interpolation lattice;
- bijection of all `55 x 35 = 1,925` joint owner-pair/lattice labels; and
- dense held-out nonlinear metric, symmetric-coframe, normalized-trace, and
  density transport.

The dense held-out is preregistered in the machine-readable certificate:

```text
owners = (0,9)
xi     = (1,-1,2,3)
zeta   = (-2,3,1,-1)
```

The symmetric-coframe identity is the exact conjugation forced by the
constant `ETA`-isometry; no moving Lorentz compensator or fitted correction is
inserted.

## Orbit census

On the joint grid of 55 symmetric owner pairs and 35 interpolation-lattice
points, the six-element action has

```text
orbit sizes: {1: 2, 3: 115, 6: 263}
orbit count: 2 + 115 + 263 = 380
```

Independent Burnside counts agree:

```text
identity:                   1,925 fixed
each of 3 transpositions:     117 fixed
each of 2 three-cycles:          2 fixed

(1925 + 3*117 + 2*2) / 6 = 380.
```

The first probe run exposed a real verifier bug: it treated the 35 registered
tuples as monomial exponent labels under polynomial pullback instead of as the
interpolation **points** they are in the accepted bank construction. The dual
actions have the same fixed-point counts but their accidental mixture breaks
the diagonal group law and produced impossible five-element pseudo-orbits.
The repair transports each lattice tuple as a conormal point. The full probe
then passed `19 exact + 2 source + 12 type + 6 planted = 39` with zero failures.

## Fail-closed admission

Six planted promotions reject:

1. treating 380 label/geometric representatives as a full evaluator;
2. dropping the 1,925-cell fallback early;
3. merging the two action banks because the finite index action is shared;
4. beginning Green/Helmholtz from geometric transport alone;
5. spending P1/P2/P3 on a symmetry certificate; and
6. merging Curt or promoting a third lane.

No coefficient, rank, support, `kappa1`, Green/Helmholtz, C3, domain,
observation, characteristic, or physics verdict changes here.

## Next gate

Resume at

```text
PW2F-R2B2B2I1-REMAINING-EVALUATOR-LAYERS-ON-ORBIT-REPRESENTATIVES-PLUS-DENSE-HELDOUTS-THEN-SEPARATE-C4-BANKS
```

Use the admitted finite action to certify `Phi`, Hodge, Shiab, residual,
moving-primalizer, and action evaluation on orbit representatives plus dense
held-outs. Only after that durable universal gate passes may a resumable
380-representative engine replace the 1,925-cell fallback. Assemble `I1 A4`
and `I2B C4` separately afterward.

P1/P2/P3 remain unchanged and unused. Curt remains
`FORMALLY_SEPARATE_INSIDE_ERIC_LANE`. `TG-1 AND TG-2 AND TG-3` remains
`NOT_PROMOTED`.

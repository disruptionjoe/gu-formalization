---
artifact_type: exact_construction_and_composition_result
created: 2026-08-12
status: FULL_AND_TWO_HALF_HERMITIAN_GEOMETRY_CONSTRUCTED_CONDITIONALLY_ON_NON_NULL_Q__Q_AND_PHYSICAL_BLOCK_UNSELECTED
target_claim: NONE-NOT-A-KILL
ledger: lab/process/conditional-physics-ledger-v0.193.json
canon_verdict_change: none
---

# Selected K77 two-half Hermitian/Witt-rotation gate

## Result in plain English

The full `U(64,64)` geometry and the source-sized description as two
`U(32,32)` Weyl halves can coexist on the complexified K77 spin carrier. They
are not two unrelated parent theories. They are two presentations of one
Hermitian space after one additional geometric choice: a normalized non-null
covector line `q`.

With `B` the exact real `Spin(7,7)`-invariant form, define

```text
H_q = i B gamma(q).
```

For every canonical non-null K77 axis, `H_q` is Hermitian of signature
`(64,64)` and its restrictions to the two ambient Weyl halves each have exact
signature `(32,32)`. An explicit complex Witt rotation carries the original
cross-paired `B` presentation into this block-nondegenerate presentation.
Thus the phrase “full `U(64,64)`, or possibly two `U(32,32)` halves” is now a
precise conditional compatibility statement rather than an unresolved size
count.

The price matters. The split alone has no invariant same-half Hermitian form:
the relevant exact bilinear spaces have dimensions `0/0`. A fixed `q` reduces
`spin(7,7)` from dimension `91` to its dimension-`78` stabilizer, and reduces
the split `spin(1,3)+spin(6,4)` algebra from `51` to dimension `48`. The moving
family is Spin-natural, but nothing in this gate selects a particular `q`.
P1 can orient an already supplied line; it cannot manufacture the line.

## Pre-wave and Layer 0

- **Inherited construction:** the admitted real `Cl(7,7)` carrier and its
  `4+10` observation split. No action-parent or physical-Higgs fork is assumed.
- **Search dimension:** the complete finite Hermitian compatibility problem is
  decided on `S_R tensor C = C^128`. Global sections, action Euler equations,
  BV and analytic domains cannot be decided wholesale here.
- **New unowned object:** yes, conditionally: one normalized non-null covector
  line `q`, unless the observation/soldering geometry independently supplies
  it. A free choice lives on a 13-dimensional pseudo-sphere orbit before gauge;
  this is not booked as residue because no datum is adopted.
- **What dies:** only the claim that a full `(64,64)` form and two nondegenerate
  `(32,32)` Weyl-half forms are algebraically incompatible on the source-sized
  carrier. The fully split-equivariant same-half route is killed.

The following objects remain different:

| object | real/complex size | role |
|---|---:|---|
| `(S_R,J10)` | `C^64` | native split-complex carrier from C3-prime |
| `S_R tensor_R C` | `C^128` | source-sized complexification used here |
| `B` | `(64,64)` on `C^128` | full form; Weyl halves are maximal neutral |
| `H_q=iB gamma(q)` | `(64,64)` on `C^128` | full form; Weyl halves are `(32,32)` |
| `J10` | real endomorphism | native complex structure, not scalar `i` |
| scalar `i` | complex coefficient | required in `H_q` |
| block `U(32,32)xU(32,32)` | stabilizer of `H_q` and `omega` | conditional two-half parent |
| full `U(64,64)` | stabilizer of `H_q` | includes half-exchanging blocks |

## Exact construction

The certified `B` is symmetric, involutive and has trace zero. Ambient
chirality `omega` anticommutes with it, so both `omega` eigenspaces are maximal
`B`-isotropic. That is why C3-prime correctly found one cross-paired Krein
space rather than two same-half forms.

For a normalized non-null covector `q`, `B gamma(q)` is real skew. Multiplying
by the external scalar `i` produces a Hermitian involution:

```text
H_q^dagger = H_q,
H_q^2 = 1,
signature(H_q) = (64,64),
[H_q,omega] = 0.
```

Consequently

```text
signature(H_q|S_+) = (32,32),
signature(H_q|S_-) = (32,32).
```

For the positive representative with `Q=gamma(q)`, the explicit map

```text
M = 1 + iQ
```

satisfies `M^dagger B M = 2 H_q`. It mixes the old `omega`-neutral
polarization, demonstrating that the two descriptions are Witt-related while
their relationship to the fixed Weyl decomposition is genuinely different.

## Symmetry, naturality and the datum cost

A fixed `q` does not preserve full `Spin(7,7)`. Exactly `78/91` spin
generators preserve `H_q`; inside the split algebra exactly `48/51` do. A
nontrivial rational Spin rotation verifies the correct moving law:

```text
q -> R q R^-1,
H_q -> H_(Rq),
R^T H_(Rq) R = H_q.
```

Freezing `q` while moving the frame fails, which is a planted control. The
family is therefore equivariant, while any selected member is reduction data.
An observation foliation or normalized conormal could supply a local member;
the present action and P1/P2/P3 do not yet do so. Calling the line “gauge” or
“external datum” before a global observation/action descent would overstate
the result.

## Conditional `varpi` block port

The predecessor decomposed the moving connection into

```text
Ahat = H + K_J + K_omega.
```

Relative to ambient chirality:

- `H+K_J` is block diagonal;
- `K_omega` is block off-diagonal and exchanges the two halves.

This now has a definite Hermitian arena: the diagonal pieces can be tested in
`u(32,32)+u(32,32)` and the exchange piece in the complement inside
`u(64,64)`, all relative to `H_q`. But the draft's equation 9.16 does not
define its `+/-` labels as these `omega` halves, and the source merely assigns
Higgs-like/CKM/Yukawa functions to components of `varpi`. Block parity cannot
by itself identify the physical Higgs or a Yukawa matrix. The operative action
parent, observation descent, scalar-doublet representation and kinetic/
potential/Yukawa terms remain to be constructed.

## Adaptive specialist preassessment

- **Clifford/Krein — actual math, very high:** owns `B`, `omega`, `H_q` and
  exact inertia.
- **Principal-bundle geometry — actual math, very high:** prices the fixed-`q`
  reduction and moving-family naturality.
- **Representation theory — actual math, high:** keeps the source `2x16`
  branching separate from mere block dimensions.
- **Symplectic/BV — actual math, high:** compatibility is not an action-owned
  reduction or quotient.
- **Variational bicomplex — actual math, high:** a physical block must survive
  Euler and preboundary construction.
- **Analytic/PDE — actual math, high:** finite Hermitian inertia is not energy
  positivity or a closed domain.
- **Construction versus selection — actual math, very high:** the path exists;
  selection of `q` and a physical block does not.
- **Contrary path — actual math, high:** a full connection with live exchange
  fields remains admissible rather than being mislabeled a defect.

## Source return and accounting

The authorial source asserts the full `U(64,64)` principal arena. Curt's
exposition displays two complex `(32,32)` Weyl halves. The 2021 draft assigns
gauge, Higgs-like, CKM and Yukawa functions to `varpi` components and displays
two `2x16` terms per complex ambient half. None of those sources prints
`H_q`, selects `q`, identifies equation-9.16 signs with `omega`, or derives a
physical Higgs block.

The exact probe passes `53/53`, including four planted controls. Six ledger
rows move in distance/evidence only. Verdicts, residue `84`, at least `19`
function-valued slots, nine forks, five quotients, P1/P2/P3, canon and public
posture do not move.

## Next gate

The highest-information truth-status research successor is:

```text
CONSTRUCT_OR_KILL_AN_OBSERVATION_OR_ACTION_OWNED_NON_NULL_Q_LINE;
TEST_ITS_GLOBAL_DESCENT_AND_WHETHER_IT_COSTS_NEW_DATUM;
THEN_DECOMPOSE_THE_H_Q_UNITARY_VARPI_BLOCKS_UNDER_THE_OBSERVED_STABILIZER
AND_REQUIRE_AN_ACTION_OWNED_SCALAR_DOUBLET_WITH_KINETIC_POTENTIAL_YUKAWA_SURPLUS.
```

If no source/observation/action object supplies `q`, retain the compatibility
map as a conditional path and book the line's true datum cost before any fit.

The bounded postflight mailbox review found no GU scientific note newer than
the already absorbed 2026-08-10 packets. The 2026-08-12 PROG-004 and live-
workbench notes concern process/steerability and do not reorder this scientific
successor.

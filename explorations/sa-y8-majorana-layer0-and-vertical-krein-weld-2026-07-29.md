---
artifact_type: exploration
status: exploration
created: 2026-07-29
work_item: VERTICAL-KREIN-WELD
title: "SA-Y8 LAYER-0 + VERTICAL--KREIN WELD: the SW 'Majorana block' is a HOMONYM, not the SHIAB-05 same-Weyl scalar; the vertical Lambda^1 connection channel is an exact 4D Lorentz-scalar, cross-chirality, nonzero Krein bilinear on the observer-compatible branch; and all four previously untyped B5 X-sector special orbits are vertical-only RS-symbol edges reached by the canonical projected vertical symbol. Composing the pairing a second time produces the antilinear Krein-dual coflip C_perp=K J_obs: it has exactly the B5 dual-slot action and gives one uniform relative parity to all ten special vertical edges. Therefore P2 is typed and conditionally welds to P1 as one global orientation bit, rather than four independent X signs. The actual differential sign, fibre-loop identification, Green form, and domain remain open."
grade: "EXACT for Layer-0 object typing against the two source maps; exact finite matrix algebra on a factorized Cl(9,5)=Cl(3,1) hat-tensor Cl(6,4) representation; exact observer-subgroup support classification against the certified B5 matrix; exact for the C_perp chirality action, contragredient covariance, projector preservation, and uniform algebraic parity of the canonical vertical symbol. RECONSTRUCTION for identifying C_perp with the physical metric-fibre loop coflip and for translating its whole-module parity into normalized B5 slot phases. This is a channel/support and conditional one-bit-weld result, not a source-action solution, vacuum construction, mass prediction, native B5 packet, signed phase sum, or claim-status change."
run: archived private execution record
probe: tests/channel-swings/vertical_krein_weld_probe.py
construction: "program-native Cl(9,5), Krein pairing included in every physical fermion bilinear, declared 4+10 observer split, gamma-traceless RS projectors, and the symmetric metric fibre. The complexified Spin(4,C) x Spin(10,C) branching is used only for the already-certified B5 support ledger. No positive-Hilbert substitution."
canon_verdict_change: none
outcome: "L0-HOMONYM + 4D-SCALAR-BRIDGE + P2-VERTICAL-SYMBOL-TYPED + CONDITIONAL-P1-P2-ONE-BIT-WELD"
---

# SA-Y8 Layer 0 and the vertical--Krein weld

## Result in one paragraph

Four questions that had been made to look separate land on one object, but at
different levels. First, the Seiberg--Witten construction's “Majorana
block” is **not** the same map as the same-Weyl scalar excluded by `SHIAB-05`;
the apparent `SA-Y8` contradiction is a homonym. Second, the earlier open
`SA-Y1` bridge closes positively at the physical four-dimensional channel
level: a vertical component of the 14D connection is a Lorentz scalar after
the declared `4+10` split, and its physical bilinear
`Psi^dagger K c(a_perp) Psi` is scalar, nonzero, Hermitian, and
cross-chirality. Third, the four B5 X-sector special orbits are exactly the
vertical-symbol edges of the two product-rule RS families, and the canonical
projected vertical symbol is nonzero on both. This types `P2` and creates the
first concrete interface between a forced source-action row and B5. Fourth,
the bare observer reality has the wrong chirality action, but its Krein-dual
composite `C_perp = K J_obs` has exactly the B5 dual-slot action and gives the
canonical vertical symbol one uniform relative parity on all ten special
edges. Conditional on identifying that algebraic map with the metric-fibre
loop coflip and the written differential, `P1` and `P2` are one global
orientation bit. No absolute B5 phase or constraint surplus is computed.

## 1. Layer 0 first: the two “Majorana blocks”

The two source objects are:

| use | mathematical object | support/codomain | predicate called “Majorana” |
|---|---|---|---|
| `SHIAB-05` / `SA-Y8` | invariant bilinear on two Weyl spinors | `S+ tensor S+ -> Lambda^0_14` | a same-Weyl scalar mass |
| SW source-action construction | moment map followed by Clifford action | `S+ tensor S- -> Lambda^2`, then `c(mu) in End(S)` | an even, vectorlike endomorphism occupying a seesaw matrix block |

They differ in domain, codomain, form degree, and the predicate being applied.
The fact that `c(mu)` preserves chirality as an **endomorphism** is not the
existence of a scalar bilinear on two same-chirality **inputs**.

**Layer-0 verdict: `HOMONYM`.**

The independent SHIAB and Yukawa certificates were rerun. Both reproduce:

```text
dim Hom(S+ tensor S+, Lambda^0_14) = 0
dim Hom(S+ tensor S-, Lambda^0_14) = 1
```

The SW construction instead states that its moment map vanishes on one
chirality alone and fires on cross-chirality inputs. That confirms rather than
repairs the type difference.

### Consequence for `SA-Y8`

`T3 = |F-mu(Psi)|^2` does **not** supply the conditional `SA-Y8`
equivariance-breaking same-Weyl scalar spurion merely because an older source
called `c(mu)` a “Majorana block.” If a physical same-chirality scalar mass is
wanted, the `SHIAB-05` requirement remains.

This is a terminology/type correction. It does not alter the SW result's
computed vectorlike block, zero-index no-go, or overall verdict.

## 2. Layer 0 again: which scalar?

The previous channel table is exact in its scope:

```text
under full Spin(9,5):
  Lambda^0_14 is the invariant scalar carrier;
  Lambda^1_14 is the vector carrier.
```

The physical mass question is posed after the already-declared observer split:

```text
Spin(9,5) -> Spin(3,1) x Spin(6,4)

Lambda^1_14 -> (4,1) + (1,10).
```

The two terms called “scalar” are therefore:

| term | meaning |
|---|---|
| ambient scalar | trivial representation of the full `Spin(9,5)` |
| physical scalar | trivial representation of the observed `Spin(3,1)`, possibly nontrivial under the internal `Spin(6,4)` |

They are not the same test. The vertical `(1,10)` part is a multiplet of ten
four-dimensional Lorentz scalars even though it remains a 14D one-form.

That does not contradict the exact 14D channel table. It corrects the
extrapolation from that table that `k=0` is the unique route to a
four-dimensional mass-type coupling.

## 3. The physical bilinear, with the pairing composed

The probe constructs a factorized program-native representation

```text
Cl(9,5) = Cl(3,1) hat-tensor Cl(6,4)
```

with exact signature `(9,5)`, verifies all 91 infinitesimal generators preserve
the Krein form, and tests

```text
B_i(Psi) = Psi^dagger K c(e_i) Psi,
```

for all ten vertical directions.

Results:

- all ten have zero `Spin(3,1)` scalar-covariance defect;
- a planted horizontal component is not an individual Lorentz scalar;
- all ten `K c(e_i)` anticommute with four-dimensional chirality;
- the identity-pairing control leaves the bare vertical Clifford action
  chirality-preserving;
- all ten matrices are nonzero and Hermitian.

The gauge/endomorphism factor matters. An observer-compatible internal
`Spin(6,4)` connection factor preserves scalarity exactly. A planted mixed
base--vertical generator produces a nonzero covariance defect. The surviving
statement is therefore not “every vertical component of an arbitrary
`Sp(64)` connection is a Higgs.” It is:

> The observer-compatible vertical induced-gravity connection channel carries
> a legitimate 4D Lorentz-scalar, cross-chirality, nonzero Krein fermion
> bilinear without adding a separate ambient `Lambda^0_14` field.

### Consequence for `SA-Y1`

At channel grade, `T1 + T2` can host the physical Yukawa/mass coupling. `T10`
is not required merely to create the carrier.

Still open:

1. whether the native curvature action produces a stable nonzero vertical
   background;
2. whether the required background-curvature sign is forced or declared;
3. the vacuum orbit and unbroken internal subgroup;
4. magnitude, family texture, and hierarchy;
5. whether the full connection term stays in the observer-compatible internal
   subalgebra dynamically.

So the result closes the **channel** question, not the Higgs/vacuum problem.

## 4. The B5 X-sector is the same vertical-symbol problem

The exact B5 carrier branches as:

```text
ker Gamma_14
  = RS(3,1) tensor S(6,4)       [384]
  + S(3,1) tensor RS(6,4)       [1152]
  + S(3,1) tensor S(6,4)        [128, imposter]
```

The first two terms are the `1536`-dimensional B5 block `X`.

The new support audit separates every B5 cell into its horizontal
`(2,2,1)` and vertical `(1,1,10)` contribution. Exact result:

```text
all 10 special mirror edges: vertical-only
all  4 X-sector special edges: vertical-only
```

The four X pairs are:

```text
X32+ <-> X32-
X23- <-> X23+
X2T+ <-> X2T-
X1T- <-> X1T+.
```

The first pair-family lives in `RS4 tensor S10`; the second lives in
`S4 tensor RS10`.

This is not support bookkeeping alone. The probe builds the
signature-correct gamma-traceless projectors:

```text
rank P_RS4  = 12
rank P_RS10 = 288,
```

and verifies that the canonical projected vertical Clifford symbol is nonzero
on both product-rule families, remains gamma-traceless, and flips internal
chirality. For every vertical direction, the projected `RS10` block has rank
`288`.

### Consequence for `P2`

The previous label “X-sector datum, type unknown” can now be sharpened:

> `P2` is the phase/orientation of the program-native vertical projected
> Rarita--Schwinger symbol on the four X mirror edges.

This is a typed operator-interface datum, not another arbitrary flavor label.
At this stage alone it is not yet identified with the chirality-orientation
`Z/2` that addresses the six `E+/E-` edges. The next construction makes that
identification conditionally.

## 5. Compose the pairing again: the conditional one-bit weld

The first tempting coflip is the observer reality

```text
J_obs = J_(3,1) tensor J_(6,4).
```

It is antilinear and observer-equivariant, but it flips both base and internal
chirality. Therefore it maps `(chi_4, chi_10)` to
`(-chi_4, -chi_10)` and does **not** implement B5's declared normal-only
mirror.

An “internal-only” conjugation has the desired chirality labels, but it fails
Lorentz covariance. That is the planted near-miss in the probe.

The physical duality map must include the pairing:

```text
C_perp = K J_obs.
```

The matrix construction proves:

- `C_perp` is an antilinear involution;
- it fixes four-dimensional chirality and flips internal chirality;
- it sends total 14D chirality to its opposite;
- it obeys exact observer **contragredient** covariance
  `C_perp S C_perp^-1 = -S^dagger`;
- its support action is therefore exactly
  `(2,1,16+) <-> (2,1,16-)`,
  `(1,2,16-) <-> (1,2,16+)`, and the analogous `144` exchanges used by
  every B5 mirror pair.

The distinction between ordinary commutation and contragredient covariance is
load-bearing. The mirror slots are dual representations; testing `C_perp` as
an ordinary commuting symmetry would ask the wrong question.

### Relative parity of the vertical symbol

The induced duality preserves both gamma-traceless projectors. Including the
duality action on the symbol's vector input gives:

```text
horizontal Clifford symbol: coflip-even in all 4 directions
vertical Clifford symbol:   coflip-odd  in all 10 directions
```

The horizontal result is the contrast control. The vertical sign transfers
unchanged to both X families:

```text
RS4 tensor S10
S4 tensor RS10.
```

Because all ten B5 special edges were independently proved vertical-only, one
whole-module construction relates their **relative algebraic parity**. Under
this candidate there are not six oriented `E` signs plus four free X signs;
there is one coherent ten-edge orientation.

### Consequence for the datum ledger

Conditional on two identifications still to be built,

1. the metric-fibre loop holonomy coflip is the same map as `C_perp`; and
2. the actual first-order differential uses the canonical vertical
   Clifford/RS symbol with one global formal-adjoint convention,

`P2` is not independent of `P1`. The ledger conditionally reduces from

```text
P1 orientation + P2 X phase/orientation + P3 count datum
```

to

```text
one P1/P2 global orientation + P3 count datum.
```

This is the sought three-to-two reduction, but only at conditional
construction grade. The Layer-0 correction reinstating `P3` is untouched:
symbol multiplicity and chiral index remain different objects.

## 6. What the weld earns, and what it does not

Before this run, `SA-Y1` and B5 shared no certified object. They now share:

```text
K-paired vertical Clifford/RS symbol on the declared 4+10 split.
```

That is now an **interface bridge plus a conditional relative-phase
construction**. It supplies an antilinear coflip candidate and one uniform
whole-module parity. It does not supply:

- normalized invariant pairing phases on all 20 slots;
- an identification of `C_perp` with the independently constructed
  metric-fibre loop holonomy;
- the actual differential expression's formal-adjoint sign;
- a program-native Green boundary form;
- a common closed, symmetry-compatible domain.

The fail-closed B5 packet contract still rejects the result as incomplete.
Accordingly:

- no B5 phase is selected;
- the eleven parity-dimension pairs remain the unconditional repo state;
- the conditional `C_perp` construction narrows them to a one-global-sign
  fork only after the two identifications above are made;
- the signed phase sum remains unknown;
- B5 constraint surplus remains uncomputable;
- no count, claim status, canon verdict, or public posture moves.

## Validation

All passed:

- `tests/channel-swings/vertical_krein_weld_probe.py`;
- `tests/chase/MOVE-4/move4_spinor_square_forms.py`;
- `tests/yukawa-scoping/yukawa_trilinear_channels.py`;
- `tests/channel-swings/krein_paired_bilinear_chirality_probe.py`;
- `tests/shiab_b5_observer_symbol_multiplicity_matrix.py`;
- `tests/shiab_b5_krein_mirror_orbit_reduction.py`;
- `tests/shiab_b5_native_packet_contract.py`;
- the B5 phase-sum and chirality-orientation audit probes.

## Next

Do not return to another carrier or coflip search. The candidate is built. Run
the two exact identification steps it generated:

```text
metric-fibre loop holonomy
  -> transport J_obs and test whether K J_obs returns as +/- C_perp

written first-order B5 differential
  -> induced 20-slot pairing table + one formal-adjoint sign
  -> absolute ten-edge delta_e assignment
  -> signed phase sum
  -> Green form/domain lift.
```

Predeclare the decisive outcomes:

1. **identity:** loop holonomy is `+/- C_perp`, merging `P1` and `P2`;
2. **residual modulus:** transport leaves an extra relative X phase;
3. **homonym/incompatibility:** the loop's anchor coflip and B5's
   representation-dual coflip are different maps.

Each is a construction-level answer. None should be replaced by a support
count or a convenient phase choice.

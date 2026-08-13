---
artifact_type: exact_topological_interface_and_parameter_accounting_result
created: 2026-08-10
status: ONE_P3_ORIENTATION_MATCHES_CHIRAL_SPIN_BUNDLE__TOPOLOGICAL_DIAGONAL_EXISTS_UP_TO_GAUGE__CONNECTION_DIAGONAL_CONDITIONAL_ON_HOMOGENEOUS_ROUND_BPST
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_SILENT_P3_SOURCE_CONNECTION_DIAGONAL_AND_RESTRICTED_ACTION__SOURCE_CORRECTS_SELF_DUALITY_AS_EINSTEINIAN_TANGENTIAL_NOT_BARE_INTERNAL_YANG_MILLS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 P3 chiral-spin bundle diagonal

## Result in plain English

The proposed P3-to-self-dual-source route passes its first global topological
test. It is not yet an action construction.

On the model four-sphere, the positive and negative chiral spin bundles have
second Chern numbers `+1` and `-1`. P3 supplies exactly the same three
clutching choices:

```text
P3 n=+1  <->  S+ chiral spin bundle
P3 n=-1  <->  S- chiral spin bundle
P3 n= 0  <->  neither chiral spin bundle
```

Thus one P3 orientation has exactly the right principal-`SU(2)` isomorphism
class. The earlier fear that the bundle diagonal necessarily adds an arbitrary
function-valued physical datum was too strong: bundle isomorphisms form a
gauge torsor, and after quotient the class match carries no continuous
topological coordinate.

But equal characteristic classes do not identify connections. Charge-one
`SU(2)` anti-self-dual connections on `S4` have a five-dimensional moduli
space. If “the BPST connection” means an arbitrary point in that space, the
construction has five continuous choices. If it means the round
`Spin(5)`-homogeneous connection, then the invariant connection has zero
deformation multiplicity and is the standard chiral Levi-Civita/BPST orbit.
The packet has not yet written that same-object connection map into the varied
source bundle.

The route therefore survives, with one sharply localized remaining interface:

> Pull the `n=+1` P3 bundle into the actual source support and prove that its
> supplied BPST connection is the round homogeneous positive-chiral
> Levi-Civita/source connection, not merely a bundle with the same `c2`.

Only after that should the action be restricted and varied.

## Layer 0

| phrase | exact object | not the same as |
| --- | --- | --- |
| P3 `H_n` | real rank-four quaternionic line with clutching `q -> L_(q^n)` | its rank-three adjoint bundle |
| P3 principal lift | principal `SU(2)` bundle of clutching degree `n` | the full source principal parent |
| `S+` | positive complex rank-two chiral spin bundle of `TS4` | four-dimensional chirality projector alone |
| class match | equality of `c2` and clutching degree | a specified bundle isomorphism |
| bundle diagonal | an isomorphism of the two principal `SU(2)` bundles | equality of their connections |
| connection diagonal | a bundle map carrying one connection to the other | equality of characteristic numbers |
| gauge torsor | all bundle maps differing by source gauge transformations | a physical function-valued external datum before quotient |
| arbitrary BPST orbit | charge-one ASD connection modulo gauge | the unique round homogeneous invariant connection |
| restricted action | `I1` pulled to connections on the reduced source bundle before variation | projection of the old unreduced solution |

Two normalizations must also stay separate. For the fundamental real
four-plane underlying an `SU(2)` complex doublet,

```text
p1(H_n) = -2 c2 = -2n.
```

For the adjoint rank-three bundle used in the framed e-invariant computation,

```text
p1(ad H_n) = -4 c2 = -4n.
```

The factor of two is a change of associated representation, not a
contradiction.

## Exact topological calculation

For an oriented spin four-plane `E`, adopt

```text
p1(E) = -2(c2(S+) + c2(S-)),
e(E)  =  c2(S+) - c2(S-).
```

On `S4`, `p1(TS4)[S4]=0` and `e(TS4)[S4]=chi(S4)=2`. Therefore

```text
c2(S+) + c2(S-) = 0,
c2(S+) - c2(S-) = 2,
```

whose unique integral solution is `(c2(S+),c2(S-))=(1,-1)`.

Principal `SU(2)` bundles on `S4` are classified by
`pi3(SU2)=Z`, precisely the degree of their equatorial clutching map. P3's
`q -> q^n` therefore produces a bundle isomorphic to `S+` exactly at `n=+1`
in the declared orientation. Reversing the orientation exchanges the labels;
the statement “exactly one nontrivial horn matches the selected chirality” is
convention-independent.

## Why topology is not yet the connection

The exact planted control uses two finite curvature distributions with the
same total charge and different quadratic energy. It demonstrates the general
fact: a characteristic number classifies the bundle here, not a connection
orbit.

The index of the unframed charge-one `SU(2)` ASD moduli space on `S4` is

```text
8k - 3(1-b1+b+) = 8 - 3 = 5.
```

Those five parameters are not available for free if the construction allows
an arbitrary instanton representative.

The round model provides a narrower escape. Write
`S4=Spin(5)/Spin(4)`. Invariant connections differ by

```text
Hom_Spin(4)(m, su(2)+).
```

The isotropy types are `m=(2,2)` and `su(2)+=(3,1)`, so this Hom space is
zero. The homogeneous chiral connection has no invariant deformation. This
supports a zero-continuous-parameter diagonal if the packet explicitly owns
the round homogeneous BPST/Levi-Civita orbit.

## Constraint accounting

- **Topological class:** zero new continuous coordinates after gauge quotient;
  `n=+1` is already one of P3's finite horns.
- **Orientation:** finite; reversing orientation swaps `S+` and `S-`.
- **Arbitrary charge-one connection:** five real moduli.
- **Round homogeneous connection:** zero invariant deformation coordinates.
- **Actual support/source map:** unbuilt. Its gauge-torsor freedom must not be
  double-counted as physical, but existence and compatibility with the source
  parent, observation support and BV gauge action still require proof.

No residue reduction is booked. P3 is not reassigned from auxiliary operator
data to source-action data until the differential diagonal exists.

## Source return

The source material supports treating self-duality as Einsteinian/tangential
rather than as a bare internal Yang--Mills insertion. It does not identify the
repository's P3 Hopf bundle with the varied source connection, specify the
round homogeneous BPST representative, or restrict and vary the action on
that bundle. Those are reconstruction steps.

## Efficient science-council return

1. **Principal bundles — ACTUAL MATH, very high.** The `c2` match removes the
   global isomorphism-class obstruction in one orientation.
2. **Spin geometry — ACTUAL MATH, very high.** `S+` and `S-` on `S4` have
   charges `+1/-1`; this is the exact object P3's clutching family can supply.
3. **Chern--Weil — ACTUAL MATH, very high.** Fundamental `p1=-2c2` and adjoint
   `p1=-4c2` must not be mixed.
4. **Instanton geometry — ACTUAL MATH, high.** Same `c2` leaves five ASD
   moduli unless the homogeneous representative is owned.
5. **Homogeneous spaces — ACTUAL MATH, high.** The round invariant connection
   has no homogeneous deformation because `(2,2)` and `(3,1)` are inequivalent.
6. **Variational geometry — ACTUAL MATH, high.** This result licenses an action
   restriction attempt; it does not supply its Euler equation.
7. **Symplectic/BV — ACTUAL MATH, high.** Gauge-torsor freedom is redundancy
   only after the actual source gauge action and reduced BV complex are built.
8. **Source criticism — ACTUAL MATH, high.** Weinstein's tangential cue helps
   type the route but does not provide the P3/source diagonal.

## Progress

```text
Ledger v0.147 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

The next bounded gate is to construct the actual support-pullback bundle map
for `n=+1` and prove connection equality with the source positive-chiral
connection. If the packet means an arbitrary BPST point, price five moduli and
do not proceed. If it owns the round homogeneous orbit, advance to the
restricted `I1` variation.

Validation: exact probe `36/36`; planted rank-only and characteristic-only
identifications fail. No action, P1/P2/P3 assignment, verdict, residue,
quotient, canon or public posture changes.

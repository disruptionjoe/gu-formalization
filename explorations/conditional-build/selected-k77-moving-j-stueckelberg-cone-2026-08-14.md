---
artifact_type: exact_partial_moving_split_cone_and_associated_complex_structure_result
created: 2026-08-14
status: LOCAL_MOVING_SPLIT_CONE_EXACT__ASSOCIATED_SPINOR_J_EXACT__TOTAL_PHYSICAL_DESCENT_TYPE_MISSING
target_claim: NONE-NOT-A-KILL
claim_grade: EXACT_LOCAL_ALGEBRA_AND_SYMBOL_COMPARATOR__CONDITIONAL_GU_COMPOSITION
revision_basis: 7fd3b872414dadc5f784d45dc88bb63595dc6133
probe: tests/channel-swings/selected_k77_moving_j_stueckelberg_cone_probe.py
hostile_review: explorations/conditional-build/selected-k77-moving-j-stueckelberg-cone-hostile-review-2026-08-14.md
canon_verdict_change: none
ledger_row_changes: none
---

# Selected K77 moving-`J` Stueckelberg cone

## Result first

The first partial moving-`J` cone closes exactly, and it clarifies what the
surviving complex structure is.

Let

```text
G = Spin_0(7,7),
H = Spin_0(1,3) x Spin_0(6,4),
B_split = G/H.
```

At the selected `4+10` split, the Lie algebra decomposes as

```text
so(7,7) = h + m,
dim h = 51,
dim m = 40,
m = R^(1,3) tensor R^(6,4).
```

For the split involution `R=diag(+I_4,-I_10)`, the orbit map

```text
kappa:m -> T_R B_split,
kappa(xi)=[xi,R]
```

is an isomorphism.  Its exact inverse is

```text
q(delta R)=delta R R/2.
```

At every declared observed covector `k`, define the partial symbol sequence

```text
0 -> m --K_k--> (T*X tensor m) + T_R B_split --D_k--> T*X tensor m -> 0,

K_k(xi)=(-k tensor xi,[xi,R]),
D_k(a,delta R)=a+k tensor q(delta R).
```

Then exactly

```text
D_k K_k=0,
rank K_k=40,
D_k is onto,
ker D_k=im K_k.
```

The formulas prove this for every `k`; the exact probe separately fires
timelike, spacelike, null, generic and zero-covector controls.  Thus the local
moving-split fluctuation and the mixed ghost form a contractible
Stueckelberg/BRST sector at this partial symbol grade.  The dressed mixed
connection is `a+k tensor q(delta R)`.

The spinor statement is different and positive.  The normal volume `J10`
commutes with all 51 stabilizer generators, anticommutes with all 40 mixed
generators and squares to `-1`.  It therefore defines a well-defined
fibrewise complex structure

```text
mathcal J[g,s]=[g,J10 s]
```

on the associated real spinor bundle

```text
E_S = G x_H S -> B_split.
```

This is the exact mechanism by which moving the reduction repairs the frozen
`J10` basicness failure: full `G` covariance transports `J`, while the residual
`H` action commutes with it.

The ceiling matters.  The split-orbit tangent itself has no
`H`-invariant real complex structure:

```text
End_so(1,3)(R^4)=R,
End_so(6,4)(R^10)=R,
End_H(m)=R.
```

So there is no natural split-invariant block-diagonal rule that turns the
moving bosonic reduction coordinate into a complex field.  This is not fatal
to the partial cone because that coordinate is gauge-exact locally.  It does
mean that the fibrewise spinor `mathcal J` is not by itself a complex structure
on the entire coupled bosonic-plus-fermionic deformation complex.

The exact disposition is therefore

```text
moving split plus mixed ghost, local symbol grade:  EXACT CONTRACTIBLE PAIR
associated spinor J10:                              EXACT FIBRE COMPLEX STRUCTURE
natural invariant complex structure on split orbit: CANDIDATE KILLED
tautological moving-J route:                        NOT-YET-FALSIFIED
total physical J and positive cohomology:           TYPE-MISSING
intrinsic physical superposition:                   NOT ESTABLISHED
```

## Why this is not a repetition

Prior work already proved three separate facts:

1. fixed `J10` fails basicness through live mixed gauge directions;
2. allowing `sJ=[c,J]` restores longitudinal covariance and nilpotence; and
3. a moving reduction sources the connection equation, so an ordinary pure
   connection detour need not close on the coupled shell.

This result supplies the missing local homological map between them.  It
constructs the contractible mixed ghost/reduction pair, the invariant dressed
connection coordinate and the associated-bundle `J`.  It does not construct
the still-missing action-owned total residual complex.

## Scientific preflight

Repository-wide priority and unrelated channel order were held unchanged.
The selected question was only the reverse-chain successor to RF-1.

| lens | why fired | exact question | preregistered kill | evidence | forbidden inference |
| --- | --- | --- | --- | --- | --- |
| Layer 0 | four different moving or complex objects were in play | are `R`, `J10`, normal `J_N` and physical `J` kept separate? | any silent carrier identification stops the gate | RF-1, twistor gate, new probe | same letter means same object |
| prior art/source | moving BRST and coupled-current work already existed | what is new relative to those results? | duplicate nilpotence or current computation | novelty checks plus three predecessor artifacts | prior compatibility is new ownership |
| construction/selection | an associated bundle may exist without action selection | does the result construct or dynamically select the reduction? | any claimed selection without an Euler owner | coupled reduction-current result | natural construction is action-selected |
| principal bundles | fixed basicness failed | is `J10` well-defined on `G x_H S`? | one stabilizer generator failing to commute kills it | complete 51/40 Clifford census | fibrewise `J` is global physical `J` |
| gauge/BV | moving `R` adds gauge directions | do mixed ghosts pair with all split tangents? | `rank kappa<40` | exact orbit map | longitudinal pair is full BV cohomology |
| homological algebra | the successor was explicitly a cone | is the three-term partial sequence exact? | `D K!=0` or `ker D!=im K` | exact rational ranks and inverse | exact comparator is the total GU complex |
| representation/commutant | the whole coupled carrier might need `J` | does the orbit tangent admit invariant `I^2=-1`? | a non-scalar stabilizer commutant revives the candidate | exact base and normal centralizers | one candidate kill exhausts all dynamical complex structures |
| exact computation | rank and cancellation are load-bearing | do causal and sign controls fire? | any failed exact causal control | `66/66` probe | floating agreement is a proof |
| microlocal/PDE contrary | `k` enters but no domain is owned | does symbol exactness imply propagation or closedness? | prohibited promotion, not a numerical kill | causal covector controls | symbol quotient is physical solution space |

The contrary route remains live: a separately selected normal twistor field
`J_N` reduces `SO(6,4)` to `U(3,2)` and supplies a different invariant complex
geometry.  No current adapter identifies that twenty-dimensional normal
twistor orbit with the forty-dimensional moving split orbit or with spinor
`J10`.

## Exact derivation

For `xi in m`, `{xi,R}=0`.  Therefore

```text
[xi,R]=2 xi R,
q([xi,R])=[xi,R]R/2=xi.
```

This gives injectivity and surjectivity of `kappa` without a rank search.
The exact `40/40` computation is a certificate and convention control.

With the repository connection-sign convention at the frozen point,

```text
delta_xi a=-k tensor xi,
delta_xi(delta R)=[xi,R].
```

Hence

```text
D_k K_k(xi)
 = -k tensor xi+k tensor q([xi,R])
 = 0.
```

`D_k` is onto because its first block is the identity.  Its kernel has
dimension 40 and contains the rank-40 image of `K_k`, proving equality.
Changing the dressing sign makes the composition nonzero for every nonzero
control covector.  Freezing `delta R` leaves the mixed gauge shift at rank 40.

For the spinor bundle, well-definedness under the associated-bundle relation
uses only

```text
h J10=J10 h for h in H.
```

The complete infinitesimal census proves this for the 51-dimensional
stabilizer.  The 40 mixed generators move `J10`, as required for the
tautological family rather than a frozen operator.

## What the result does and does not say

The result makes one part of the superposition hypothesis more credible: the
fixed-`J` gauge obstruction was an artifact of freezing a reduction that must
move.  On the associated spinor bundle, the same structure is exactly basic.

It also removes an overread.  A complex spinor fibre does not automatically
make geometry, connection perturbations, ghosts, residuals and their quotient
one complex physical state space.  That requires an action-owned total
complex, a descended `J` on its cohomology, and a positive closed Lorentzian
realization.

The local contraction may also fail to globalize through:

- nontrivial reduction-bundle topology;
- lower-order or curvature terms in the coupled differential;
- action terms that make additional reduction variables physical;
- boundary-nonvanishing transformations that remain charged; or
- orbit-type changes where the stabilizer and rank jump.

None of those is decided by the partial symbol cone.

## Source return

`SOURCE-SILENT`.  `SC-GRP-01`, `SC-FER-05` and `SC-CHI-03` confirm the parent,
split and half-carrier inputs already used by RF-1.  The source does not print
this Stueckelberg cone, the associated-bundle `J10` descent, or an intrinsic
physical complex cohomology.

## Next in-channel gate

The next gate is not another abstract orbit computation.  On one declared
candidate background and boundary horn, assemble the action-owned partial
maps

```text
mixed ghost + stabilizer ghost
  -> connection + reduction + rolled fermion perturbations
  -> coupled bosonic and fermionic residuals,
```

rewrite them in the dressed coordinate, and test both compositions together
with

```text
L_dressed mathcal J = mathcal J_E L_dressed.
```

The newly filed frozen-frame residual-zero branches cannot silently supply
that background.  The concurrent native-legality refinement at `969c56e2`
sharpens the missing input to the explicit Zorro induced-`Y` connection and
its labelled curvature one-jet.  The branches' own stabilizer and reducibility
ranks also remain type-missing.

## Accounting and reproduction

```text
ledger_row_changes: none
canon_verdict_change: none
public_posture_change: none
GU-wide priority effect: none
```

Run:

```text
sage -python tests/channel-swings/selected_k77_moving_j_stueckelberg_cone_probe.py
```

The probe passes `66/66` exact prior-art, Layer-0, orbit, Clifford,
associated-bundle, cone, causal-control, commutant, contrary-route and scope
checks.

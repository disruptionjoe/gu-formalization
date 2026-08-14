---
artifact_type: exact_reverse_falsification_candidate_census_and_sign_equivalence_result
created: 2026-08-14
status: FIXED_SPLIT_NATURAL_ROLLED_J_FAMILY_KILLED_AT_SELECTED_LOCAL_SCOPE__PLUS_MINUS_JHAT10_CONNECTED_BY_CONDITIONAL_MOVING_REDUCTION_REDUNDANCY__MOVING_J_NOT_YET_FALSIFIED__TOTAL_PHYSICAL_DESCENT_TYPE_MISSING
target_claim: NONE-NOT-A-KILL
lane_id: SRC-RES-COH-01
channel_gate: RF-1
revision_basis: 8c286f9ac39a12bb903e822fa7f6d7c0f92740ac
fork_assumed: SELECTED_CL77__AUTHOR_DECLARED_1_3_PLUS_6_4_SPLIT__SPLIT_NATURAL_ROLLED_LIFTS__CONDITIONAL_MOVING_J_ASSOCIATED_FAMILY
search_space_dim: "complete real split commutant dimension 4; four square-minus-one units; two B-compatible units; complete 91-parameter source gauge bank with rank 25 and kernel 66"
free_object_delta: 0
residue_touched: none
source_return: SOURCE-SILENT
canon_verdict_change: none
ledger_row_changes: none
probe: tests/channel-swings/selected_k77_reverse_j_descent_census_probe.py
hostile_review: explorations/conditional-build/selected-k77-reverse-j-descent-census-hostile-review-2026-08-14.md
---

# Selected K77 reverse-`J` descent census

## Result first

The first reverse-falsification gate now has a clean scoped answer.

On the selected local K77 bank, **no fixed complex structure in the complete
split-equivariant spinor commutant, equipped with its split-natural diagonal
rolled lift, survives all currently owned necessary conditions**:

- the complete split-equivariant family is exactly
  `{+J4,-J4,+J10,-J10}`;
- the correctly rolled `J4` lift fails complex linearity for all four observed
  principal axes and is an anti-isometry of the owned `B` pairing;
- the correctly rolled `J10` lift is complex-linear on the four observed axes
  and preserves both owned action pairings, but fixed `J10` is not basic for
  the selected ordinary-gauge quotient because the rank-25 gauge image
  contains a rank-eight mixed, `J10`-breaking subimage.

There is a stronger new result about the proposed sign bit.  Let

```text
A = gamma_0 gamma_1,
g(t) = exp(t A),                0 <= t <= pi/2,
V = diag(-1,-1,+1,...,+1),
U = (V tensor A) direct-sum A.
```

Axes `0` and `1` are same-sign positive axes, one base and one normal.  Exact
integer arithmetic gives

```text
A^2 = -1,
U Jhat10 U^-1 = -Jhat10.
```

The path `g(t)` fixes the selected source background supported on axes `12`
and `13`; its infinitesimal generator is exactly in the 66-dimensional kernel
of the selected source gauge map.  It preserves both owned action pairings,
and it covariantly rotates the Clifford/rolled symbol with the frame.  Thus
`+Jhat10` and `-Jhat10` are in the same connected source-frame redundancy
orbit when `J` is treated as a moving reduction field.

Therefore:

```text
fixed split-natural J10:      candidate killed
fixed split-natural J4:       candidate killed
physical +/- polarization:    killed in the conditional local moving-J family
tautological moving J:         NOT-YET-FALSIFIED
total physical J descent:      TYPE-MISSING
intrinsic-superposition H1-R:  not killed
```

“Gauge-equivalent” here is not “physically unitarily equivalent.”  The latter
still has no object to refer to because the total physical quotient, positive
pairing and common closed Lorentzian domain do not exist in the repository.

## Lane-1 preflight

### Reservation

```text
pinned HEAD: 8c286f9ac39a12bb903e822fa7f6d7c0f92740ac
gate: RF-1 candidate-J descent and +/- equivalence
writable result: this file
writable probe: tests/channel-swings/selected_k77_reverse_j_descent_census_probe.py
writable review: explorations/conditional-build/selected-k77-reverse-j-descent-census-hostile-review-2026-08-14.md
postflight propagation added after hostile review:
  lab/active-research/source-residual-cohomology/target-theorem-reverse-falsification-chain-2026-08-14.md
ledger rows declared before computation: none
```

No conditional-ledger row owns the proposed identification of a complex
spinor endomorphism with physical superposition.  This is a necessary-
condition test inside an active-research content channel, so the evidence-
backed ledger declaration is `ledger_row_changes: none`.  No lane schema,
sequence, registry, canon or public posture is in the write set.

### Anti-redo and source collision

The preflight inspected `lab/sources/media-index.md`,
`lab/sources/source-claim-register.yaml`, `lab/process/NAMES.md`, the target
reverse chain, and the existing split-commutant, J10/BV/Green, twistor/BV and
physical-operator artifacts.  `novelty-check.py` returned `0` exact and many
near hits for the search phrases, so all near hits relevant to this object
were treated as prior art rather than as evidence of novelty.

Why the answer was not already fixed or empty: prior work killed fixed `J10`
and built moving-`J` covariance, but it neither typed the rolled `J4` candidate
against the observed operator nor decided whether the two `J10` signs were in
one owned gauge orbit.  Those are the new computations here.

Source claims `SC-GRP-01`, `SC-FER-05` and `SC-CHI-03` own the complex parent,
split fermion labels and two ambient halves.  They do not identify a physical
state-space `J`, select a sign, or decide the gauge orbit of `+/-J10`.

### Adaptive specialist lenses

| lens | why fired | exact question | preregistered kill | artifact/source inspected | forbidden inference | basis / confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Layer-0 object typing | `J` occurs on spinors, vectors, twistors and quotients | which carrier does each candidate actually act on? | any composition that changes carrier without an adapter is rejected | target chain; `GEOMETER-VS-PHYSICS-OBJECTS.md`; `NAMES.md` | pointwise `J` = physical scalar multiplication | DIRECT / very high |
| prior art and source collision | fixed `J10` was already tested | what is genuinely undecided? | if a held theorem already decides sign equivalence, this swing is duplicate | split-commutant, J10 descent, source register | repo-near hit = novelty | DIRECT / very high |
| construction versus selection | a compatible `J` need not be action-selected | does the action/gauge structure select one fixed member? | a source-frame redundancy joining the signs kills the sign bit | moving-split and moving-BV artifacts | constructed reduction = selected observable | DIRECT / high |
| Clifford/commutant | the fixed candidate family may be exhaustible | what are all split-equivariant square-minus-one units? | any additional unit outside `+/-J4,+/-J10` reopens the census | C3-prime exact certificates | four candidates exhaust every admissible physical `J` | DIRECT / very high |
| gauge/BV | descent requires basicness | does fixed `J` preserve the owned gauge image; does moving `J` transform covariantly? | one active noncommuting gauge direction kills fixed descent | selected source BVKT and J10 probes | longitudinal BRST = physical BV cohomology | DIRECT / very high |
| homological algebra | the physical test is `ker L / closure(im K)` | can the available `G:R91->R196` legally carry spinor `J10`? | carrier mismatch blocks the composition before kernels are compared | source-residual target and operator inventory | raw rank quotient = physical cohomology | DIRECT / very high |
| Krein/real-complex structures | `B`, `H_q` and positivity differ | which candidates preserve which owned forms? | failure of every owned candidate pairing kills that candidate only | C3-prime and trace-`H_q` artifacts | algebraic isometry = positive physical unitarity | DIRECT / high |
| exact computation and negative controls | the sign claim is finite and algebraic | is there an explicit background-fixing conjugator and is its generator in `ker G`? | nonzero source variation or pairing failure kills equivalence witness | exact K77 bank and new probe | endpoint matrix similarity = connected gauge equivalence | DIRECT / very high |
| symplectic/variational | the target ultimately concerns reduced physical states | does the sign define a nonzero reduced observable? | membership in a source-frame redundancy orbit kills the local sign observable | action-pairing and source-gauge artifacts | unreduced label = phase-space observable | PRINCIPLE / high |
| contrary path | a disconnected sign could support superselection | could `+J` and `-J` remain separate under every owned symmetry? | one connected owned redundancy joining them kills this contrary path | new `exp(t gamma_0 gamma_1)` witness | algebraic conjugacy outside the owned group settles physics | DIRECT / very high |

## Candidate census

| proposed object | exact status | RF-1 disposition |
| --- | --- | --- |
| external scalar `i` on the source complexification | native only after complexification; source parent `U(64,64)` | fails the endpoint's intrinsic-versus-imported requirement; does not kill ordinary quantization |
| `+/-J10` on the real spinor | exactly the only split-equivariant `B`-compatible complex units | fixed candidates killed by rank-eight mixed gauge image |
| `+/-J4` on the real spinor | remaining two split-equivariant complex units; `B`-anti-compatible | correctly rolled candidate killed by all four observed principal axes |
| `Jhat10=(R10 tensor J10) direct-sum J10` | correct `Omega1(S)+Omega0(S)` lift; observed-symbol linear and action-pairing isometric | strongest fixed carrier candidate, but inherits fixed-gauge kill; moving family survives |
| moving normal `J_N in O(6,4)/U(3,2)` | exact vector-space orbit and longitudinal BRST covariance | no spin lift/associated-bundle map to `Jhat10`; type-missing |
| base local-twistor scalar `i` | native on the rank-four complex spin-tractor; Bach-flat detour complex exists | no adapter to the total GU residual complex; type-missing |
| Lorentzian four-dimensional Hodge `*` on two-forms | conditional square-minus-one form-sector operator | not constructed as a gauge-basic endomorphism of the physical carrier |
| `omega`, split reflections and moving projectors | square `+1` | gradings/reductions, not complex structures |
| W/mirror and charge conjugations | anti-linear or square `+1` real structures | reality/polarization data, not `J_phys` |
| retired `Cl(9,5)` quaternionic units | genuine only on the rejected real-form control | non-transfer to selected `Cl(7,7)` |

This census exhausts repo-owned named candidates, and the commutant theorem
exhausts the finite **fixed split-equivariant spinor** family.  The rolled
conclusion covers the split-natural diagonal lifts actually constructed here;
it does not classify arbitrary non-diagonal endomorphisms of the rolled
carrier or every action-admissible complex structure on a future total
physical carrier.

## Exact computation

### 1. Correctly rolled `J4` and `J10`

With

```text
BASE   = (0,7,8,9),
NORMAL = (1,2,3,4,5,6,10,11,12,13),
J4     = product_BASE gamma_a,
J10    = product_NORMAL gamma_a,
```

both volume elements square to `-1`.  Their gamma commutation parities force
different vector reflections on the one-form spinor carrier:

```text
R10 = +1 on BASE,   -1 on NORMAL,
R4  = -1 on BASE,   +1 on NORMAL.
```

Both `(R tensor J) direct-sum J` lifts preserve the gamma-trace carrier.  For
the released rolled principal symbol, the axis-`k` commutator vanishes exactly
when the relevant `R_k=+1`.  Hence `Jhat10` is linear on precisely the four
observed base axes, whereas `Jhat4` is linear on precisely the ten normal axes.
This kills `Jhat4` as a complex structure for the owned observed operator.

### 2. Fixed-gauge obstruction

The prior exact gauge computation is composed, not relabeled:

```text
G : R^91 -> R^196,
rank G = 25,
dim ker G = 66,
rank im(G)_split = 17,
rank im(G)_mixed = 8.
```

All 40 mixed Spin generators break both `J4` and `J10`.  Therefore the active
rank-eight mixed subimage kills fixed descent of either complex unit through
the current full ordinary-gauge action.

The `196`-dimensional `Cl1` tangent itself cannot be silently endowed with
spinor `J10`: left multiplication sends a normal `Cl1` blade to `Cl9`, while
conjugation preserves `Cl1` but acts as the square-plus-one split reflection.
Thus `G` is useful for the gauge-orbit test, but it is not the missing
`J_F K=KJ_g` physical descent complex.

### 3. The connected sign witness

For the positive base-normal pair `(0,1)`, set `A=gamma_0 gamma_1`.  Then
`A^2=-1`, so

```text
g(t)=cos(t) 1 + sin(t) A
```

is a connected Spin path from the identity to `A` at `t=pi/2`.  Conjugation
rotates axes `0,1` and fixes the remaining twelve.  At the endpoint its vector
action is `V`, and exactly

```text
A J10 A^-1 = -J10,
A J4  A^-1 = -J4,
U Jhat10 U^-1 = -Jhat10,
U Jhat4  U^-1 = -Jhat4.
```

The selected background is supported on axes `12,13`, so `A` commutes with it
for the entire path.  The corresponding `(0,1)` source-gauge column vanishes
coefficientwise and is one of the 66 kernel directions.  The generator is
skew for both `B` and `B omega`, so the path preserves both owned action
pairings.  Clifford covariance holds on all fourteen axes.

The endpoint returns the unoriented `4+10` split projector while reversing
both block orientations.  A frozen oriented split makes the signs look
disconnected; the source-owned moving frame connects them.  That is why the
sign cannot be a local measurement-selected bit in this model.

## Source return

`SOURCE-SILENT` for the new result.  `SC-GRP-01`, `SC-FER-05` and
`SC-CHI-03` confirm the parent/split objects used as inputs.  The source does
not decide the `J4/J10` principal-symbol discriminator, the `+/-Jhat10` gauge
orbit, or a physical superposition interpretation.

## What survives

The surviving steelman is no longer a fixed sign or a fixed polarization.  It
is a **tautological complex structure over a moving reduction family**.  The
next legitimate equation is therefore a mapping-cone/extended-BV descent
question, not another fixed commutator:

```text
fields plus moving J
    -- extended K -->
linearized fields plus delta J
    -- extended L -->
residuals,
```

with the tautological `J` tested on the resulting cohomology.  That successor
cannot run as a physical theorem until a common total carrier and residual
linearization exist.  A smaller conditional mapping-cone control can run
next, provided it remains explicitly partial.

## Claim ceiling and ledger accounting

This result kills the split-natural rolled lifts of the fixed split-commutant
candidate family on the selected local rolled/gauge bank.  Within the
conditional moving-`J` associated family, it also kills the proposed physical
`+/-` bit at the local source-frame scope.  It does not kill arbitrary rolled
lifts or every intrinsic-complex-state-space route, construct physical
cohomology, prove positivity, establish a closed domain, or derive quantum
superposition.

```text
ledger_row_changes: none
reason: RF-1 is a candidate-level necessary-condition result with no owned
        conditional-ledger row and no physical-cohomology promotion.
canon_verdict_change: none
public_posture_change: none
```

## Executable receipt

Run:

```text
sage -python tests/channel-swings/selected_k77_reverse_j_descent_census_probe.py
```

The probe uses only exact signed-permutation Clifford arithmetic, and composes
the independently replayed exact rational-rank receipt rather than importing
or rebuilding its whole bank.  Its hostile review is filed separately at the
path in frontmatter.

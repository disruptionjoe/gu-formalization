---
artifact_type: exact_construction_composition_and_kill_result
created: 2026-08-10
status: NATIVE_QUADRATIC_PAIRING_ZERO_ALL_CURRENT_PARENTS__DIRECT_P3_AMPLITUDE_HORN_KILLED__SELF_DUAL_REDUCTION_REVIVAL_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_SILENT_P3_SOURCE_CONNECTION_DIAGONAL_AND_SELF_DUAL_REDUCTION
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 P3 native characteristic pairing

## Result in plain English

The v0.144 topological theorem is correct, but the most direct attempt to use
it on the source curvature fails.

The remaining source family has

```text
F_B=(t^2/3)(Phi1 wedge Phi1).
```

On P3's oriented framed four-plane, the two-form `Phi1 wedge Phi1` contains
equal self-dual and anti-self-dual Spin(4) pieces. Their quadratic
characteristic numbers are nonzero and opposite. Every invariant quadratic
trace currently owned by the moving-Spin parent, either `U(32,32)` Weyl half,
or full `U(64,64)` adds them and gets exactly zero.

Therefore the current source curvature has `C_B=0` for all named parents. A
direct equality to P3 gives:

```text
n=-1: no amplitude is allowed
n= 0: every amplitude is allowed
n=+1: no amplitude is allowed
```

No P3 stratum selects a finite nonempty amplitude set. The direct v0.144
source/P3 quadratic horn is killed.

A narrower revival remains. Projecting onto only the self-dual `SU(2)` piece
gives a nonzero pairing in every spinor parent. But that projection is not a
current parent-invariant trace: it uses the chosen four-plane, orientation and
a reduction of the source connection. P3 supplies the framed cycle and BPST
object, so this is a plausible external construction, but the action does not
yet own it.

## Layer 0

| phrase | exact object | kept distinct from |
| --- | --- | --- |
| native quadratic pairing | invariant polynomial of the current source parent applied to `Phi1 wedge Phi1` | a chirality-weighted or self-dual trace |
| P3 BPST curvature | fixed self-dual curvature on the auxiliary quaternionic line | unprojected source curvature |
| four-plane chirality | volume element of the framed normal four-plane | ambient K77 chirality or a central element of full `U(64,64)` |
| self-dual projector | reduction to one `SU(2)` factor of `Spin(4)` | an invariant of full moving Spin or unitary parents |
| zero native pairing | cancellation of opposite chiral components | zero source curvature |
| topological mismatch | nonzero P3 class versus zero native source class | an Euler equation or BV quotient |

The load-bearing warning is:

> Substituting P3's BPST curvature for the actual source curvature manufactures
> the nonzero pairing the gate is supposed to test.

## Exact Clifford and Chern--Weil calculation

On an oriented Euclidean four-plane choose exact Clifford generators
`gamma_1,...,gamma_4` and write

```text
F_ij = gamma_i gamma_j.
```

The coefficient of the oriented volume form in `F wedge F` is an exact matrix
whose traces are

```text
Tr(F wedge F)                 =  0
Tr(P_plus F wedge F)          = +12
Tr(P_minus F wedge F)         = -12
Tr(chi_4 F wedge F)           = +24.
```

The vector representation gives zero matrixwise, so the unique quadratic
Spin/Killing invariant also vanishes.

For either complex 64-dimensional K77 Weyl half,

```text
S14+ = (S4+ tensor S10+) + (S4- tensor S10-)
S14- = (S4+ tensor S10-) + (S4- tensor S10+),
dim_C S10+ = dim_C S10- = 16.
```

Thus each half contains sixteen copies of each opposite four-plane pairing:

```text
U(32,32) half 1: 16(+12)+16(-12)=0
U(32,32) half 2: 16(+12)+16(-12)=0
full U(64,64):                     0.
```

Independent weights on the two halves cannot revive zero. The second unitary
quadratic invariant, `Tr(F) wedge Tr(F)`, also vanishes because every curvature
component is traceless.

The self-dual control instead gives relative values

```text
half 1 = 192, half 2 = 192, full = 384,
```

and the anti-self-dual control reverses the sign. These numbers are not booked
as physical normalizations; they prove that the zero is a cancellation, not a
vacuous computation.

## What this does to v0.144

The general theorem survives:

```text
fixed nonzero k_B and C_B => t^4=9k_B/C_B.
```

Its direct application to the current unprojected source family does not. Here
`C_B=0`, so `n=0` leaves the continuous family untouched and `n=+/-1` is
incompatible. The amplitude residue therefore does not move.

The only current revival is a new source reduction:

1. use P3's framing to define a self-dual `SU(2)` subbundle of the source
   parent;
2. prove the varied source connection preserves it, for example
   `D_B P_sd=0` or an equivalent reduction-section equation;
3. derive that condition from the action/domain rather than append it after
   solving;
4. recompute the Euler, Ward, presymplectic and characteristic equations on
   the reduced field space.

If the source action does not own this reduction, the topological amplitude
route is dead at the current construction grade.

## Efficient specialist return

1. **Clifford algebra — ACTUAL MATH, very high.** The full trace vanishes and
   the two chiral traces are exact opposites; the planted chiral trace proves
   the cancellation is real.
2. **Representation theory — ACTUAL MATH, very high.** Equal 16-fold
   multiplicities of `S4+` and `S4-` inside each 14D Weyl half force the two
   `U(32,32)` cancellations separately.
3. **Chern--Weil geometry — ACTUAL MATH, very high.** A characteristic number
   must use an invariant polynomial of the actual principal parent. The
   chirality-weighted trace is only invariant after a four-plane reduction.
4. **Principal-bundle topology — ACTUAL MATH, high.** P3 supplies enough
   framing to formulate an `SU(2)` reduction, but not a theorem that the
   source connection preserves it.
5. **Variational bicomplex — ACTUAL MATH, high.** Restricting the configuration
   space changes admissible variations and must be returned to the Euler map.
6. **Symplectic/BV--BFV — ACTUAL MATH, high.** A reduction projector is not a
   quotient; its constraint and ghosts must be included before booking a
   physical sector.
7. **Krein/operator theory — ACTUAL MATH, medium.** Nonzero topology would not
   establish positivity or a common closed domain; the current zero is
   algebraic and domain-independent.
8. **Source criticism — ACTUAL MATH, high.** The source owns full `P_H` and
   the connection grammar but does not state the P3 diagonal or self-dual
   source reduction.
9. **Constraint accounting — ACTUAL MATH, high.** The direct horn removes zero
   coordinates. A fixed reduction could still have positive surplus, but its
   ownership constraints must be ranked before use.
10. **Adversarial physics — ACTUAL MATH, medium.** A higher or reduced
    characteristic sector could survive; that does not rescue the named
    quadratic four-cycle route without a new field-space construction.

## Hostile boundary

The strongest overreach would be “P3 cannot select the amplitude.” What is
killed is narrower: the direct quadratic match between current P3 and the
unprojected `Phi1 wedge Phi1` source family across the three named parents.
Higher characteristic classes, another cycle, or an action-owned self-dual
reduction are not tested.

The strongest underclaim would be “the pairing is merely unknown.” It is not:
for every current parent-invariant quadratic trace it is exactly zero.

## Progress and next gate

```text
Ledger v0.145 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

Next construct or kill the P3-framed self-dual `SU(2)` reduction on the varied
source bundle, including preservation by `B` and action/BV ownership. Only if
that passes should the nonzero projected characteristic equation be carried
into the common Green/Krein and BV--BFV domain.

Validation: exact main route `61/61 PASS`. An attempted independent Sage run
could not start because the installed Sage launcher points to a missing
`sage-site`; no independent-Sage claim is made. The vector/Killing and spinor
trace constructions are nevertheless separate exact representations inside
the main certificate.

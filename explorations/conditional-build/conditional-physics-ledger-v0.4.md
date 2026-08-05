---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.4"
machine_source: lab/process/conditional-physics-ledger-v0.4.json
predecessor: lab/process/conditional-physics-ledger-v0.3.json
status: APPEND_ONLY_AMBIENT_CURVATURE_VEV_ACTION_RANK_EXACT__OBSERVED_RECEIVER_AND_BV_OPEN
---

# Conditional physics ledger v0.4

## Progress meter

```text
Ledger v0.4 — 82/82 active target rows mapped (100% of current denominator)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Ambient curvature/VEV covariation rank: 105 exact; total T-Euler rank: 196
Observed post-Shiab route: killed by rank-10 kernel; native BV quotient: undefined
Residue — 83 continuous real + >=19 function-valued + 10 open discrete forks
Quotients ranked: 0; no global residue reduction booked
```

Coverage and verdict counts are unchanged. What changed is the quality and
location of the construction: the action already owns a real ambient
curvature/distortion equation, while the physical observation and quotient
interfaces are now the exact bottlenecks.

## Row movements

| row | verdict/kind | v0.4 result | distance |
| --- | --- | --- | --- |
| `LT-GR2b` variable distortion/VEV | `SAME/DERIVED_PARTIAL` | source `theta` and action `T=A-B` are the same connection-difference object up to the tilted trivialization; the ambient Euler row is action-owned | select a nonzero vacuum branch and carry it through the observed equation dual |
| `LT-GR2c` curvature covariation | `NEEDS/MISSING_CONSTRUCTION` | selected ambient Einstein curvature covaries with `T` at exact rank 105; total homogeneous `T`-Euler rank is 196 | action-own the pre-Shiab Gauss receiver and compute its rank through native BV |
| `LT-GR2d` scale and stability | `NEEDS/PROVEN_UNABLE_BY_CURRENT_ACTION` | the current homogeneous action transfers an independent vacuum shift into `T`, but does not hold observed curvature fixed, fix the common amplitude or remove the free gain | derive a separate vacuum-selection/non-equilibrium rule stable under independent shifts |

The new `PROVEN_UNABLE_BY_CURRENT_ACTION` reason is intentionally narrower
than `PROVEN_UNSUPPLYABLE`. It says the built action cannot do the job at the
tested homogeneous value locus; it does not forbid an additional source-owned
term, global constraint, boundary condition or non-equilibrium mechanism.

## Why 105 and 196 are different

On algebraic Riemann curvature in fourteen dimensions,

```text
3185 = 1 scalar + 104 traceless-Ricci + 3080 Weyl.
```

The selected displayed Shiab equals `-2 G_14` on this carrier. Consequently
only the `1+104=105` scalar/Ricci directions enter the curvature side. The
action's invertible Krein/Hodge `kappa*T` term acts on all 196 tested
`Omega^13 tensor Cl^1` distortion coordinates. The full homogeneous `T`
equation therefore has rank 196: 105 rows relate curvature to `T`, while 91
rows constrain `T` without a curvature partner. Reporting 196 as the
curvature-covariation rank would be a support/rank Layer-0 error.

Independent variation of the distinguished connection does not add a second
algebraic field-value equation at `T=0`: its Euler row begins with derivatives
and commutators of `T`. It remains a live PDE/domain equation away from the
homogeneous locus, but cannot be double-counted as the second half of a
two-value equality.

## Why this is not yet physical curvature tracking

The exact prior receiver theorem gives

```text
rank(G_4 res_H | ker G_14) = 10.
```

Thus every observed symmetric two-tensor direction can occur on ambient
curvature that the selected post-Shiab route erases. Ambient `G_14` tracking
is real, but it is not the source interview's physical spatial-flatness or
observed-curvature statement without another map. The surviving candidate is
the already-built pre-Shiab Gauss/second-fundamental-form receiver; its
equation dual is local and exact, but the one source action has not yet been
proved to own it.

The obstruction is an order-of-operations result—contracting upstairs before
restricting—not a defense of fixed `Lambda g`. A cosmological constant spans
only the trace direction, whereas the lost observed target has dimension ten.
The fluctuating distortion, moving section and Gauss/`II` terms are outside
the killed factorization and may be the repair. Hence the theorem changes the
receiver we must build; it does not count against the complete fluctuating
geometry.

Bianchi removes the ambient Weyl kernel at this value grade. The even Ward
identity is derivative-valued and adds zero homogeneous zero-jet rank. The
odd BV tangent differential remains unbuilt, so its quotient rank is
`UNDEFINED`, not zero. The global residue meter therefore stays unchanged.

## Vacuum-shift control

For one active mode the current action linearizes schematically to

```text
c + kappa*t + rho_vac = 0.
```

This is rank one. It makes `t` follow a shift, but `c` remains a free
coordinate, and a free `kappa` remains a free normalization. Holding `c=0`
requires a second independent equation; the homogeneous `B` variation does
not supply it. This is field tracking—the limited two-problems-to-one win—not
radiative screening or a first-principles magnitude derivation.

## Next work

1. `LT-GR1b/LT-GR2c`: put the pre-Shiab Gauss receiver inside the one K77
   action and derive its complete moving observation-jet equation dual.
2. `LT-GR2b/c/d` plus `LT-SM8`: construct the actual BV tangent differential
   and compute the observed curvature/distortion quotient rank.
3. `LT-GR2b/d`: only then construct/select a nonzero vacuum branch and repeat
   the independent vacuum-shift test.
4. `LT-GR2e`: derive FLRW and perturbations from that action-owned branch.

Evidence and controls:
`source-native-curvature-vev-euler-rank-2026-08-05.md`.

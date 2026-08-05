---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.12"
machine_source: lab/process/conditional-physics-ledger-v0.12.json
predecessor: lab/process/conditional-physics-ledger-v0.11.json
status: APPEND_ONLY_P2_NORM_FORK_RETIRED__FULL_II_DERIVED_ON_CANONICAL_GAUSS_SECTOR__SELECTED_K77_NONZERO_ALGEBRAIC_STATIONARY_BRANCH_EXACT__PHYSICAL_STABILITY_TOTALIZATION_AND_DOMAIN_OPEN
---

# Conditional physics ledger v0.12

## Progress meter

```text
Ledger v0.12 — 82/82 active target rows mapped (100% of current denominator)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
P2_norm: full |II|^2 derived from the written connection norm
Canonical Gauss receiver: rank 100; trace-first rival: rank 10
Observed gravity: one simple massless pole + one distinct massive GU partner
Selected non-cyclic K77 action: t* = -kappa_1/312 algebraically stationary
Radial Hessian: -14*kappa_1; physical stability/domain still open
Residue — 84 continuous real before quotient + >=19 function-valued
          + 9 open discrete forks
Quotients ranked: 2 local/defect symbol quotients; no global residue reduction
```

Coverage is unchanged. One verdict and one discrete fork move. `LT-GR1`
migrates from `NEEDS/ONE_BIT` to `SAME/DERIVED_CONDITIONAL`, reducing the
verdict counts from `32/19/25/6` to `33/19/24/6`. Retiring the
full-`|II|^2`-versus-trace-first action fork reduces the open horn product from
2304 to 1152. The homonymous external object `P2_datum` does not move.

## What closed

The written augmented-torsion term measures the full difference of two
connections. On the canonical horizontal Gauss sector, a normal-valued
symmetric tensor

```text
II in Sym^2(H*) tensor V
```

embeds into the off-diagonal block of an `so(H plus V)`-valued horizontal
one-form. The exact receiver has rank 100 and the insertion is its
action-metric adjoint right inverse. Consequently the written quadratic form
restricts to the full ordered `II` norm. Taking the mean-curvature trace first
has rank ten and erases 90 traceless directions, so it cannot be the same
quadratic form under a convention or rescaling.

This selects the predecessor's two-pole matrix inside the admitted canonical
K77 construction:

```text
J_TT = [[alpha_II*z, z], [z, kappa_1]]
det J_TT = z*(alpha_II*kappa_1-z).
```

It gives one simple massless Einstein pole and one distinct massive GU
partner. The partner is retained for physical classification rather than
removed to imitate pure GR.

## Selected nonlinear branch

The selected displayed `comm/symi/symi` Shiab was evaluated directly, not
replaced by the predecessor's cyclic control. At flat reference connection,
constant `T=t Phi1` and fixed metric,

```text
bar F = T^2/3
I(t) = 1456*t^3 + 7*kappa_1*t^2
t* = -kappa_1/312.
```

All 196 grade-one and 196 grade-thirteen translation derivatives vanish at
`t*`. Spin invariance and the invariant-line classification close the full
algebraic adjoint gradient, and the co-moving epsilon-orbit derivative also
vanishes. The source-printed endpoint happens to vanish on this invariant
branch, but the earlier non-cyclic counterexample remains, so this is a
special coincidence locus rather than a restored global identity.

This is an algebraic stationary branch, not yet a physical vacuum. Its radial
Hessian is `-14*kappa_1`, hence it is radially unstable for positive
`kappa_1`; derivative constraints, totalization/current closure and the
common Krein/Green domain remain unbuilt.

## Row movements

| row | v0.12 disposition | distance now |
| --- | --- | --- |
| `LT-GR1` | `SAME/DERIVED_CONDITIONAL` | close totalization/stress/current and the physical domain; `P2_norm` itself is derived |
| `LT-GR2b` | `SAME/DERIVED_PARTIAL` | extend the selected algebraic branch to the derivative/constraint system and establish physical stability |
| `LT-GR2c` | `NEEDS/MISSING_CONSTRUCTION` | close the totalization/current chain on the construction-selected two-pole system |
| `LT-GR2d` | `NEEDS/MISSING_CONSTRUCTION` | resolve or interpret radial instability, then test magnitude and independent-shift screening |
| `LT-GR3` | `DIFFERS/STRUCTURAL_DIFFERENCE` | classify the selected distinct massive partner on a common physical domain |
| `LT-GR5` | `DIFFERS/STRUCTURAL_DIFFERENCE` | complete the augmented-torsion spectrum without losing the exact `10 -> 6 -> 2` carrier |
| `LT-GR6` | `DIFFERS/STRUCTURAL_DIFFERENCE` | identify Hilbert stress, source up-and-back totalization and connection current in one linearized system |

`LT-GR1b`, `LT-SM8`, all representation/anomaly rows, external P1/P2/P3,
canon and public posture do not move.

## Source return

`SOURCE-CONFIRMS-INGREDIENTS__REPO-DERIVES-COMPOSITION`.

Released source material supplies the full connection-difference carrier, the
unprojected `kappa_1 <T,*T>/2` term, the gauge-rotated Levi-Civita comparison
and the moving-Phi grammar. It does not print the rank-100 Gauss
restriction, coefficient `-1/312`, stability theorem or physical domain.

## Next gate

```text
CLOSE_SELECTED_BRANCH_LINEARIZED_TOTALIZATION_STRESS_CURRENT_AND_COMMON_KREIN_GREEN_DOMAIN__THEN_CLASSIFY_MASSIVE_PARTNER_STABILITY_AND_TEST_VACUUM_SHIFT_SCREENING
```

Evidence:

- `selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md`;
- `selected_moving_k77_vacuum_p2_norm_probe.py`;
- `selected_moving_k77_vacuum_p2_norm_independent.sage`; and
- `2026-08-05-selected-moving-k77-vacuum-p2-norm-review.md`.

---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.10"
machine_source: lab/process/conditional-physics-ledger-v0.10.json
predecessor: lab/process/conditional-physics-ledger-v0.9.json
status: APPEND_ONLY_ACTION_HILBERT_STRESS_EXACT__OBSERVED_NULL_10_TO_6_TO_2_RETAINED__REPAIRED_GRAVITY_DOUBLE_POLE_AND_ZERO_INDEFINITE_VACUUM_EXPOSED
---

# Conditional physics ledger v0.10

## Progress meter

```text
Ledger v0.10 — 82/82 active target rows mapped (100% of current denominator)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Action-owned Hilbert stress: exact radial transgression of mixed return block
Exact Krein-Dirac control: symmetric, conserved and trace-free on shell
Literal VU = nonlinear stress: killed by type
Observed flat null quotient: 10 -> 6 -> 2, plus/cross retained
Repaired pre-Shiab metric response: double pole, not Einstein single pole
Current unshifted quadratic distortion vacuum: zero indefinite stationary point only
Independent vacuum shift: tracked linearly, not screened
Residue — 84 continuous real before quotient + >=19 function-valued
          + 10 open discrete forks
Quotients ranked: 2 local/defect symbol quotients; no global residue reduction
```

Coverage, verdict counts and global residue do not change. Five row distances
do. The matter stress is no longer an unspecified missing object, but the
place where the current repaired action inserts it is now shown not to be
ordinary Einstein gravity.

## What was constructed

Let the common action's matter contribution to the metric Euler covector be

```text
T_H(g,psi) = E_g^matter(g,psi),
V_raw(g,psi) = D_psi T_H(g,psi),
T_H(g,0) = 0.
```

Then the fundamental theorem of calculus gives the exact, parameter-free
reconstruction

```text
T_H(g,psi) = integral_0^1 V_raw(g,t psi)[psi] dt.
```

This is the nonlinear action-owned Hilbert stress. It is symmetric by metric
variation and conserved on the matter shell by the full diffeomorphism Ward
identity. An exact Lorentzian Dirac control includes the active Krein pairing
`K=gamma^0`; for a massless null plane wave its stress is symmetric,
conserved and trace free.

The construction does **not** make the literal diagonal composite `VU` the
stress tensor. `VU` is a linear Hessian-response operator. The stress is the
radial path integral of the return block itself. Nor does this identify the
projected connection current with stress: rescaling a null momentum keeps the
same algebraic spinor current but scales the stress, so any relation needs the
derivative/soldering data explicitly.

## The propagation result that changes the priority

The inherited observed flat null system remains exact:

```text
10 coupled characteristic directions
- 4 harmonic-constraint violations
= 6 constraint-compatible directions
- 4 residual diffeomorphisms
= 2 physical directions: plus and cross.
```

This closes the dimension-level normal constraint question on the flat
Lorentzian defect horn. It does not make the action's propagator Einsteinian.
On either transverse-traceless polarization, the repaired quadratic action is

```text
L_TT = v z h + (kappa_1/2) v^2 + tau h,
```

where `z` is the wave/Einstein symbol. Its field matrix and inverse are

```text
J_TT = [[0,z],[z,kappa_1]],
det J_TT = -z^2,
(J_TT^-1)_hh = -kappa_1/z^2.
```

Eliminating `v` therefore produces a squared wave/Einstein operator. The
plus/cross labels survive, but each carries a generalized double-pole partner.
The present repaired action is Green-hyperbolic as an operator composition on
the already stated flat defect domain; it is not the single-pole Einstein
response. A source-owned cancellation, boundary constraint or different
action placement must remove that partner without erasing the two physical
polarizations.

## Vacuum result

At zero curvature and zero matter source, the observed rank-ten quadratic
distortion equation is

```text
kappa_1 W_DW v = 0.
```

For nonzero `kappa_1`, `W_DW` is invertible with inertia `(6,4)`. Hence
`v=0` is the unique unshifted stationary point and is indefinite, not a stable
minimum. An independent trace source gives

```text
v = -(kappa_1 W_DW)^-1 rho,
```

so doubling the source doubles the response. The current action tracks the
shift; it does not screen it, select a stable nonzero VEV or fix a magnitude.

## Row movements

| row | v0.10 disposition | new distance |
| --- | --- | --- |
| `LT-GR2b` | still `SAME/DERIVED_PARTIAL` | derive a stable nonlinear or non-equilibrium nonzero vacuum; the present unshifted quadratic branch is only zero and indefinite |
| `LT-GR2c` | still `NEEDS/MISSING_CONSTRUCTION` | convert the double pole to one Einstein pole with the action-derived stress, or produce a constrained ambient domain whose observed reduction does so |
| `LT-GR2d` | scope-corrected to `NEEDS/MISSING_CONSTRUCTION` | compute the existing full nonlinear `T`-cubic/non-equilibrium vacuum before judging inability; the observed quadratic horn alone is zero/indefinite and transmits shifts |
| `LT-GR5` | still `DIFFERS/STRUCTURAL_DIFFERENCE` | remove or justify the generalized distortion partner while retaining harmonic constraints and plus/cross |
| `LT-GR6` | still `DIFFERS/STRUCTURAL_DIFFERENCE` | identify the Hilbert radial stress with the stabilized source totalization and place it in a single-pole observed equation; derive any current relation |

`LT-GR1b`, `LT-SM8`, all representation/anomaly rows, P1/P2/P3, canon,
verdict counts and public posture do not move.

## Source correction

Portal/Oxford `02:03:07--02:03:53` says stress energy *should* be the
up-and-back path and that the order, invariance, indices, signs and handedness
still needed cancellation. It does not publish a literal `VU` identity. The
decisive return is `SOURCE-CORRECTS`: the source corrects the repo's overtyped
diagonal-composite and momentum-free readings while confirming the unfinished
path architecture. The radial-transgression theorem is this repository's
action construction, not a quotation from Weinstein.

## Next work

1. `LT-GR2c/GR5/GR6`: construct the cancellation, constraint or alternative
   placement that turns the repaired double pole into the Einstein single pole
   while retaining action-owned stress and plus/cross.
2. `LT-GR2c/GR5/SM8`: keep the constrained ultrahyperbolic domain as an
   independent rival horn.
3. `LT-GR6`: construct the typed chain comparison among Hilbert radial stress,
   the unfinished source up-and-back totalization and connection current.
4. `LT-GR2b/d`: compute the existing full nonlinear `T`-cubic and
   non-equilibrium vacuum first, then derive any missing selector; do not fit a
   source, scale or boundary condition to create the desired VEV.
5. Only after those gates, derive FLRW/perturbation observables in `LT-GR2e`.

Evidence and controls:

- `observed-upback-stress-normal-constraint-vacuum-2026-08-05.md`;
- `observed_upback_stress_normal_constraint_vacuum_probe.py`; and
- `observed_upback_stress_normal_constraint_vacuum_independent.sage`.

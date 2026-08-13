---
artifact_type: construction_result
created: 2026-08-13
status: FIXED_NATURAL_ENDPOINT_CUBIC_TORSION_ZERO__FIRST_LIVE_QUARTIC_TORSION_ABSORBED__MOVING_ACTION_AND_PHYSICAL_BV_OPEN
run_id: RUN-20260813-214746-gu-i2b-first-nonlinear-torsion
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_SC_ACT_04_ENDPOINT_GRAMMAR__SOURCE_SILENT_NONLINEAR_TORSION_AND_SPENCER_ABSORPTION
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
fork_assumed: none
search_space_dim: "one exact 16-support compatible stationary two-jet; 140 cubic and 280 quartic compatibility cells; 3920 symmetric third jets and 6860 symmetric fourth jets"
free_object_delta: 0
scripts:
  - tests/channel-swings/selected_k77_i2b_first_nonlinear_torsion_absorption_probe.py
---

# First nonlinear torsion absorption on the fixed-natural K77 I2B endpoint

## Result first

No nonlinear formal obstruction survives through the first live quartic
compatibility order on the tested source-natural fixed-grade endpoint stratum.

The exact sixteen-support compatible stationary two-jet has:

```text
cubic Euler compatibility support:       0 / 140
first-prolonged symbol rank:             770 / 784
third-jet plus torsion map rank:         910 / 924
induced cubic absorber rank:             140 / 140

quartic Euler compatibility support:      3 / 280
second-prolonged symbol rank:           1904 / 1960
fourth-jet plus torsion map rank:        2184 / 2240
induced quartic absorber rank:            280 / 280
```

Thus the cubic representative is zero before quotient. The first nonzero
representative occurs at quartic order, in three cells, but its class vanishes
after quotienting by fourth jets that already preserve the second prolonged
equations.

## Why the quotient matters

A nonzero compatibility representative is not yet a torsion obstruction.
Allowed higher jets may absorb it, but only if they continue to solve the
previous prolonged equations.

For cubic order, the exact first prolonged symbol has rank `770`; its kernel
has dimension `3920-770=3150`. Stacking the 140-cell lower-order absorber with
that map raises rank from `770` to `910` at two primes. Therefore the absorber
restricted to the actual symbol kernel is surjective onto all 140 targets.

For quartic order, the exact second prolonged symbol has rank `1904`; its
kernel has dimension `6860-1904=4956`. Stacking the 280-cell absorber raises
rank from `1904` to `2184` at both primes. Therefore the fourth-jet absorber
restricted to the second prolonged kernel is surjective onto all 280 targets.

The rank bounds make both results exact over the rationals: the modular ranks
reach their maximal possible values given the independently certified symbol
ranks and target dimensions.

## Nonlinear calculation

On the admitted local connection jet,

```text
A(x) = A_0 + (1/2)c_00 x_0^2 + c_01 x_0 x_1,
```

where `(c_00,c_01)` is the exact sixteen-support stationary/compatibility
witness. For the printed endpoint residual

```text
R(A) = Shiab(F_A) + *T,
```

the residual-square Euler variation was expanded directly.

Both possible cubic contributions vanish on this stratum, so the 140-cell
differentiated compatibility representative is zero. At quartic order the two
residual-square contributions are live and yield a three-cell compatibility
representative. The exact fourth-jet quotient then absorbs it.

The cubic zero is a theorem on this admitted stratum, not a claim that the
complete nonlinear Euler polynomial vanishes for every jet.

## What this closes

- the first cubic fixed-natural endpoint torsion class on the exact compatible
  stationary two-jet;
- the first live quartic torsion class on the same stratum;
- any interpretation of the three-cell quartic representative as an
  obstruction before the admissible fourth-jet quotient;
- further cubic/quartic fixed-natural obstruction hunting as the primary next
  route on this stratum.

## What remains open

This is not a theorem that the full GU system is formally integrable. It does
not include:

1. moving or field-dependent `Q_B` and `H_q`;
2. moving Shiab, metric, Levi-Civita, section and observation coefficients
   beyond the already certified tensorial transport packets;
3. the complete source-unitary action or the separate first-action
   `E_act/Q_u` rival;
4. the action-owned physical tangent and BV/Koszul--Tate complex;
5. higher nonlinear compatibility orders;
6. analytic convergence, hyperbolicity, a Green domain, positivity, spectrum,
   BFV reduction or global descent.

The third- and fourth-jet kernels are formal solution freedom, not external
data and not particle counts.

## Source return

`SC-ACT-04` supports the printed endpoint residual-square and connection/
covariant-derivative grammar. It does not publish the cubic or quartic
representatives, the `140/140` or `280/280` absorber ranks, or a nonlinear
formal-integrability theorem.

```text
SOURCE-CONFIRMS: SC-ACT-04 endpoint residual-square grammar.
REPO-DERIVES:    cubic zero, live quartic representative and both quotient ranks.
SOURCE-SILENT:   moving-action torsion, physical BV and analytic/global closure.
```

No ledger row, physics verdict, residue, quotient, external datum, P1/P2/P3,
canon claim or public posture changes.

## Specialist and hostile review

- **Spencer/EDS:** both absorbers are restricted to the appropriate prolonged
  symbol kernel; unconstrained-jet quotienting is explicitly rejected.
- **Variational bicomplex:** the cubic and quartic terms come from the actual
  fixed-endpoint residual-square variation.
- **Principal-bundle geometry:** moving coefficients and section data remain a
  separate successor rather than being silently frozen forever.
- **Symplectic geometry:** formal jet absorption supplies neither a stationary
  quotient nor a BV/BFV phase space.
- **Analytic/hyperbolic/Krein:** no existence, propagation, positivity or
  spectral theorem follows.
- **Source criticism:** the source owns the grammar; the ranks are repository
  results.

The hostile review returns `PASS_WITH_SCOPE_FENCES`.

## Next gate

Move from the now-low-yield fixed-natural cubic/quartic obstruction search to
the first action-owned moving-coefficient torsion packet: `Q_B`, `H_q`, Shiab,
metric/Levi-Civita, section and observation derivatives on the same compatible
jet. Keep construction of the physical tangent/BV graph as an independent
parallel gate. Higher fixed-natural nonlinear orders remain a fallback if the
moving packet does not decide the route.

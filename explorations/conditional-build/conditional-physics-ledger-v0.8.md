---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.8"
machine_source: lab/process/conditional-physics-ledger-v0.8.json
predecessor: lab/process/conditional-physics-ledger-v0.7.json
status: APPEND_ONLY_GLOBAL_EVEN_OWNER_AND_FORMAL_MINIMAL_CME_COMPOSED__NULL_4_CONSTRAINT_4_GAUGE_2_PHYSICAL_SPLIT_EXACT__DEFECT_GREEN_DOMAIN_CONDITIONAL__LAMBDA_DEF_CHARGED_AS_84TH_PREQUOTIENT_REAL__GLOBAL_Y14_DOMAIN_PHYSICS_OPEN
---

# Conditional physics ledger v0.8

## Progress meter

```text
Ledger v0.8 — 82/82 active target rows mapped (100% of current denominator)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Global K77 gamma_epsilon and rank-ten gravitational receiver: exact
Selected moving Shiab + primitive epsilon + complete even Ward owner: composed
Formal minimal homogeneous even CME: pass at algebraic/compact-core grade
Null coupled kernel: exact 10 -> 6 -> 2 constraint/gauge dimension filtration
Defect Green complex: conditional on flat globally hyperbolic X and harmonic gauge
Global coupled noncompact Y14 Krein/Green/BFV domain: open
Residue — 84 continuous real before quotient + >=19 function-valued
          + 10 open discrete forks
Quotients ranked: 2 local/defect symbol quotients; no global residue reduction
```

Coverage and verdict counts do not change. `LT-GR2c` moves closer because the
formerly separate global frame, displayed Shiab selector, primitive
`epsilon` derivative and full homogeneous Ward owner now support a formal
minimal even BV master action. The former six-direction null uncertainty is
also resolved without erasing physics: four independent constraint conditions
reduce the kernel dimension from ten to six, and quotienting four residual
gauge directions leaves the two expected gravitational wave polarizations.
This is a dimension filtration, not a canonical direct-sum decomposition.

The relative defect coefficient is now counted honestly. CB-D's 83-real total
was packet subtotal 82 plus the gimmel block ratio. `lambda_def` is a later,
independently written relative coefficient between `S_Y` and `S_X`; it is not
the internal `T` gain `kappa_1`, and `source_norm` was never a charged CB-D
coordinate. Therefore the prequotient count is 84. A future normalization
quotient may reduce it, but no such quotient has been ranked.

## Row movements

| row | v0.8 disposition | reason |
| --- | --- | --- |
| `LT-GR1b` | no change | the selected post-Shiab factor route remains killed; the pre-Shiab construction does not revive that factorization |
| `LT-GR2b` | no change | no nonzero stationary or non-equilibrium vacuum branch is selected |
| `LT-GR2c` | migrated, still `NEEDS/MISSING_CONSTRUCTION` | global owner composition, formal even CME, null physical quotient and conditional defect Green complex reduce the distance |
| `LT-GR2d` | no change | no magnitude, screening or radiative-stability rule is built |
| `LT-SM8` | no change | a formal homogeneous even CME is not a positive physical BV/BRST cohomology |

## Exact null result

For `k=(1,1,0,0)`, the repaired coupled `(h,v)` Hessian has rank 10 and a
10-dimensional kernel. The de Donder symbol

```text
C_k(h)_nu = k^mu h_mu,nu - (1/2) k_nu tr(h)
```

has rank four both on the metric carrier and when restricted to the coupled
kernel. The constraint-compatible kernel is therefore six-dimensional. Null
diffeomorphisms have rank four, lie in the coupled kernel, and preserve the
constraint because `C_k D_0(k)=k^2 I=0`. Hence

```text
dim[(ker J cap ker C_k) / im D_0(k)] = 10 - 4 - 4 = 2.
```

Explicit plus and cross tensors are independent representatives modulo gauge.
This supersedes the earlier wording “six non-gauge characteristic directions
remain” as a sufficient physical diagnosis. Four are constraint violations;
two are physical null modes.

## Formal even BV and analytic boundary

The global primitive chain is

```text
gamma_epsilon = Ad(epsilon^-1) gamma_0
delta Phi_i = [Phi_i, chi]
delta B = D_B chi
delta T = -D_B chi
E_epsilon = D_B^!(E_B-E_T) + (D_epsilon Shiab_epsilon)^! K_S.
```

Together with all separately typed metric, section, density, projector,
background and boundary owners, this gives the complete homogeneous even Ward
identity. Ordinary gauge-algebra closure and Jacobi then give the standard
minimal formal even BV action and classical master equation.

That statement is not the odd square-root-of-connections algebra, a quantum
master equation, a global analytic BV phase space or positive cohomology.

On the flat globally hyperbolic `X` background tested here, harmonic gauge
turns the defect Einstein operator into an invertible trace-reversal
automorphism times a wave operator. The advanced/retarded Green complex and
its operator composition are therefore available conditionally. A curved
background requires a separate normally-hyperbolic lower-order completion.
The full noncompact ultrahyperbolic `Y14` coupled domain remains open, exactly
as Weinstein's own multiple-time technical-debt warning requires.

## Residue movement

| quantity | v0.7 | v0.8 |
| --- | ---: | ---: |
| continuous reals before quotient | 83 lower / 84 upper | 84 |
| function-valued slots | at least 19 | at least 19 |
| discrete forks | 11 | 10 |
| horn product | 4608 | 2304 |
| ranked quotients | 1 | 2 |

The second quotient is the exact null constraint/gauge quotient of dimension
two. Neither quotient is booked as a reduction of the global parameter
residue.

## Next work

1. `LT-GR1b/LT-GR2c/LT-SM8`: construct moving-observation no-leakage and the
   global coupled noncompact `Y14` Krein/Green/BFV domain, or a sharp
   obstruction, while preserving the exact two-mode null quotient.
2. `LT-GR2b/c/d`: after that domain gate, derive the observed Einstein,
   stress-energy and dynamic cosmological Euler equations from the complete
   action.
3. `LT-GR2b/d`: construct and select a nonzero vacuum branch and rerun the
   independent vacuum-shift test without retuning `lambda_def` or `kappa_1`.
4. `LT-GR2e`: only then derive FLRW and perturbations.
5. `LT-SM8`: extend the formal even result to the actual odd super-IG/Clifford
   closure and test positive physical cohomology.

Evidence and controls:

- `k77-global-even-bv-null-green-domain-2026-08-05.md`;
- `k77_global_even_bv_null_green_domain_probe.py`; and
- `k77_global_even_bv_null_green_domain_independent.sage`.

The decisive source return is `SOURCE-SILENT`. The source owns the moving
frame ingredients and warns about the upstairs analytic debt; the formal BV,
null quotient, defect Green complex and normalization adjudication are this
repo's constructions.

---
artifact_type: construction_result
created: 2026-08-12
status: SC_ACT_04_OWNS_RESTRICTED_MEXICAN_HAT__FULL_FIXED_HQ_STATIONARITY_FAILS_IN_CONSTANT_CURVATURE_TRUNCATION
ledger_rows: [RA-E1, RA-E3, LT-SM6]
source_claims: [SC-ACT-04]
source_return: SOURCE_CONFIRMS_SC_ACT_04_RESIDUAL_SQUARE_OWNER__SOURCE_SILENT_ON_HQ_REDUCTION_BACKGROUND_AND_TRANSVERSE_CANCELLATION
target_claim: NONE-NOT-A-KILL
free_object_delta: "zero fields, parameters, data, selectors, quotients or boundary conditions"
scripts:
  - tests/channel-swings/selected_k77_source_i2b_hq_stationarity_probe.py
registry: lab/process/selected-k77-source-i2b-hq-stationarity.json
---

# Selected K77 source-I2B moving-Hq stationarity gate

## Outcome

The source-owned action question is now one step sharper. The draft's second
bosonic action `SC-ACT-04` is the norm square of the complete bosonic residual,
not the raw eddy-square comparator used in v0.200. On the exact moving-`H_q`
weak-doublet family it gives

```text
Upsilon_B(r) = (rho+r^2/3) S_q + kappa_1 r H_q,
S_q = Shiab(T_q wedge T_q),
H_q = *T_q,

<S_q,S_q> = 192,
<S_q,H_q> = 0,
<H_q,H_q> = 0,

I2B(r) = 1/2 <Upsilon_B,Upsilon_B>
        = 96 (rho+r^2/3)^2.
```

Thus `SC-ACT-04` really does own the conditional radial Mexican-hat shape at
this grade. The nonzero restricted branch is

```text
r^2 = -3 rho,
d^2 I2B/dr^2 = -256 rho > 0  when rho<0.
```

But the branch is not yet a full vacuum. At the branch the Shiab component
cancels while

```text
Upsilon_B = kappa_1 r H_q != 0,
<Upsilon_B,Upsilon_B> = 0.
```

The action vanishes because the remaining residual is Krein-null, not because
the first-order equation `Upsilon_B=0` holds. Differentiation through the
complete 196-real-dimensional fixed-`H_q` Clifford-vector connection bank
finds fourteen nonzero diagonal gradient cells. The four-real
`J`-completed doublet tangent cancels them, but the ambient connection bank
does not.

The correct verdict is therefore conditional and constructive:

> `SC-ACT-04` owns the restricted potential, while an action-owned reduction
> to the moving doublet—or a complete source-owned connection-jet/background
> cancellation—is still required before the branch is a physical stationary
> vacuum.

No new datum, fitted lift, background magnitude, or cancellation term was
introduced.

## Plain English

We now know the quartic was not merely sitting in the geometry waiting for an
action. Eric's written second action actually produces the desired bowl-and-
rim shape after restriction to the candidate Higgs field.

There is a catch caused by GU's indefinite geometry. The candidate bottom of
that potential still carries a nonzero error signal whose squared length is
zero. Along the four Higgs directions the errors cancel in the derivative, but
in fourteen other allowed connection directions they do not. So this is a
real source-action fit, but only on the proposed Higgs subspace. The next
burden is to show that GU itself selects that subspace, or that the complete
connection/background terms cancel the transverse forces.

## Layer 0

| object | constructed here | kept distinct |
| --- | --- | --- |
| eddy | `T_q wedge T_q` | its Shiab image `S_q` |
| raw residual | `Upsilon_B=S_q+*kappa_1T_q` with the curvature coefficient restored | its quadratic action value |
| second action | `SC-ACT-04`, the bosonic residual norm square | an unbuilt total Einstein--Dirac square |
| zero action value | a nonzero Krein-null residual is allowed | `Upsilon_B=0` |
| restricted critical point | first variation along the four moving-doublet tangents | stationarity in the full connection space |
| local background | supplied co-moving `F_0=rho(T_q wedge T_q)` | a derived cosmological magnitude or global connection |
| positive radial Hessian | a finite restricted calculation | analytic stability or a physical Higgs mass |

This is the Layer-0 check that changes the conclusion. A positive radial
Hessian is not enough when the surrounding action is indefinite and has live
transverse directions.

## Source ownership

`SC-ACT-04` asserts

```text
I2B = ||Upsilon_B||^2,
D_omega^* Upsilon_B = 0,
```

as the second bosonic layer. The source also connects that layer with the
Yang--Mills--Maxwell/Higgs stratum. This licenses the residual-square owner.
It does not publish the moving-`H_q` reduction, choose `J`, supply `rho`, or
show that the fourteen transverse cells are absent or cancelled.

The v0.200 eddy-square scalar remains a useful comparator. Its coefficient is
`2`, whereas the actual source residual square has coefficient `96`. They
have the same stationary ratio only because both depend on
`(rho+r^2/3)^2`; they are not the same action.

## Exact residual calculation

The four co-moving representatives all give the same three Gram entries:

```text
<S_q,S_q> = 192,
<S_q,H_q> = 0,
<H_q,H_q> = 0.
```

Both residual pieces are Clifford grade one. Therefore the unresolved relative
weights between grades one, two, and five in the v0.92 residual-pairing fork do
not affect this result: only the single grade-one scale occurs. Its overall
normalization rescales the potential but neither creates nor removes the
stationary ratio or transverse support.

## Full fixed-Hq first variation

The exact 128-real Clifford representation verifies the real-form bank:

```text
gamma(q)              is H_q-unitary with a real coefficient,
i gamma(v_perp)       is H_q-unitary for all 13 perpendicular directions.
```

Tensoring those fourteen algebra directions with all fourteen one-form legs
gives 196 real connection directions. At `rho=-1/3`, `r=1`, and
`kappa_1=1`, the nonzero first variation has support

```text
(mu,a)=(0,0),...,(11,11):  8/3,
(12,12):                    1,
(13,13):                   -1.
```

The `J`-completed radial tangent contains the last two cells together, so
`1+(-1)=0`. Its three angular partners also annihilate the gradient. Each
diagonal cell is live separately, leaving fourteen transverse failures in the
full bank.

This is evaluated in a legitimate local constant-curvature zero-jet
truncation: vary the connection difference while holding the supplied
background curvature and normal-frame geometry fixed at the point. A complete
moving background, derivative terms, or an action-owned reduction can change
the result and remain explicit rivals. They have not been constructed here.

## Adaptive specialist assessment

- **Invariant theory:** the residual square is orbit-radial on the moving
  family, so four representative agreement is meaningful rather than a fit.
- **Principal-bundle geometry:** a reduction can make the four-real tangent the
  admissible field space, but only if the action or source geometry selects it.
- **Variational bicomplex:** restricted Euler zero is not the ambient Euler
  equation; the fourteen-cell gradient is the decisive object.
- **Krein/operator theory:** `I2B=0` does not imply `Upsilon_B=0`; this is the
  central non-Hilbert phenomenon, not a numerical defect.
- **Symplectic geometry:** no constraint reduction, momentum map, Goldstone
  quotient, photon kernel, or BFV phase space follows from the finite potential.
- **Analytic PDE:** the positive radial Hessian establishes no closed-domain
  spectrum or stability theorem.
- **Source criticism:** `SC-ACT-04` owns the bosonic residual square, while the
  total Dirac square and this exact `H_q` reduction remain unprinted.
- **Contrary-path review:** co-moving connection jets, an action-selected
  reduction, or other already-owned residual blocks may remove the transverse
  force; no universal Higgs no-go is claimed.

## Constraint accounting

The construction uses the already-located doublet, existing `J` completion,
written coefficient `1/3`, source-owned `SC-ACT-04`, and the v0.92 local
residual pairing. It adds zero parameters or fields. The background `rho` and
the 20-dimensional choice of `J` remain unselected; they are not booked as new
freedom because they were already open. P1/P2/P3 remain unchanged and unused.

## Progress meter

```text
Ledger v0.201 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: SC-ACT-04 ownership of the restricted radial potential
Frontier opened/sharpened: fourteen-cell transverse stationarity/reduction gate
```

## Next gate

Construct the source-owned moving reduction or the complete local connection-
jet background extension and evaluate the same fourteen-cell first variation.
The burden is exact: either derive that the physical field tangent is the
four-real `J`-completed bank, or cancel every displayed transverse coefficient
using already-owned terms. Only then derive the kinetic normalization,
Goldstone/photon quotient, Yukawa placement, BV class, and analytic spectrum.

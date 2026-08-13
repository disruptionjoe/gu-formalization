---
artifact_type: conditional_build_variational_result
created: 2026-08-12
run_id: RUN-20260812-163746-gu-i2b-real-primalizer-phase-gate
status: CONDITIONAL_PAIRING_REPAIR_EXISTS__CURRENT_ACTION_PROJECTOR_AND_TWO_HALF_WEIGHTS_FAIL__MOVING_REDUCTION_OWNERSHIP_OPEN
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 I2B real-primalizer phase gate

## Result

The rank-two Higgs kinetic block found in v0.213 is **not forced by the four
live derivative responses alone**. It is forced by those responses together
with the current real complex-bilinear trace pairing.

On the same exact response, a conjugation-sensitive phase-even pairing gives

```text
time block:     +8 I4
spatial blocks: -8 I4
mixed blocks:    0
```

Thus its principal symbol is

\[
-8(-k_0^2+k_1^2+k_2^2+k_3^2)I_4,
\]

which has rank four off the null cone and rank zero on it. This is the first
exact pairing-only path in the current construction that gives all four local
Higgs directions—including the radial direction—a wave-like principal term.

It is not yet the source action. An exact noncompact `U(1,1)` sub-block keeps
the complex-bilinear trace invariant but changes the phase-even value from
`1` to `1681/81`. Since that sub-block embeds in `U(32,32)`, the candidate is
not automatically invariant under either the two-block subgroup or the full
`U(64,64)` parent. A moving fundamental symmetry or action-selected reduction
must own it; otherwise it is an imported pairing choice.

## Plain English

The geometry can support a complete four-component Higgs wave term. The
problem is no longer “the shape cannot fit.” The problem is “the currently
invariant way of measuring the residual sees only two components, while the
way that sees all four is not yet selected by the action's full symmetry.”

That is genuine conditional progress. It means an external datum or source
action could select the needed pairing, but the repo has not yet shown that
GU's own moving geometry does so. The next test is selection/ownership, not
another brute-force search over the same fixed selectors.

## Exact carrier classification

After Hodge duality the live responses lie in

\[
V\otimes\Lambda^2V,
\qquad \dim=14\cdot91=1274.
\]

The metric-orthogonal tensor decomposition is

| component | dimension |
| --- | ---: |
| total alternating `Lambda^3 V` | 364 |
| trace copy of `V` | 14 |
| traceless hook | 896 |

Each live response was reconstructed exactly as alternating + trace + hook,
and the three pieces are pairwise orthogonal. Allowing a real symmetric
`2 x 2` coefficient form on real/imaginary components for each tensor type
gives the displayed nine-weight restricted ansatz. Its timelike determinant
is

\[
\frac{1024}{351}(c_A+2c_H)^2
\times(a_A+2a_H+2b_A-2b_H+c_A+2c_H)
\times(a_E+12a_H+2b_E-2b_H+c_E+12c_H),
\]

The current complex-bilinear
point uses `(a,b,c)=(1,0,-1)` on all three tensor types and gives
`diag(-8,-8,0,0)`. The phase-even point `(1,0,1)` gives `8 I4`.

This is a finite restricted classification, not a claim that every global
action-natural `Q_B` has nine physical parameters. No weights are booked.

## What does not repair the block

1. **The already action-owned real projector.** `P_+` has ranks
   `(2,2,2,2)` across the four base directions; `P_-` does too. They split
   the current quadratic action but neither reaches rank four.
2. **Two Weyl-half scalar weights.** Exact real chirality projectors have
   ranks `64+64`. For all `8 x 8` live grade-two blade products,
   `Tr(chi X Y)=0`, so the two half traces agree. Relative weights reduce to
   their sum and the maximum rank remains two.
3. **The eight displayed Shiab selectors.** V0.213 already exhausted them:
   six rank two and two rank zero.

The second point directly preserves the source distinction: two
`C^(32,32)` carrier halves are real and important, but their existence does
not by itself create two independently weighted connections or cure this
particular grade-two radical.

## Layer 0

| object | decided here | not established |
| --- | --- | --- |
| current residual pairing | invariant complex-bilinear real trace comparator | unique physical `Q_B` |
| phase-even pairing | exact finite rank-four candidate | action ownership or global covariance |
| `P_+`/`P_-` | action-owned fixed-real Euler projectors | nonlinear residual replacement |
| two half traces | equal on this grade-two response | equality on arbitrary grades/parents |
| rank-four Lorentz block | finite principal symbol | hyperbolicity, energy, domain or spectrum |
| moving reduction | legitimate ownership route | constructed fundamental symmetry |

Keep distinct: source `C^(32,32)+C^(32,32)` carrier halves, derived
`U(32,32)xU(32,32)` subgroup, full `U(64,64)` parent and independent
connection fields.

## Source return

```text
SOURCE-CONFIRMS: bosonic residual norm-square and adjoint grammar.
SOURCE-SILENT: exact real K77 Q_B and any reduction selecting phase-even Q_B.
REPO-DERIVES: conditional rank-four pairing plus noncompact-unitary obstruction.
```

## Hostile review and scope

- **Representation theory:** the grade-two carrier decomposition and half-
  trace equality are exact; no full global invariant-carrier classification
  is claimed.
- **Krein theory:** phase-even is not synonymous with positive Hilbert; the
  base factor and full carrier remain indefinite.
- **Symplectic geometry:** no principal Hessian is promoted to a
  presymplectic/BFV quotient.
- **Variational bicomplex:** fixed-real Euler projector ownership does not
  select the nonlinear `Q_B` action.
- **Principal-bundle geometry:** a moving reduction/fundamental symmetry is
  the exact missing ownership arrow.
- **Analytic/PDE:** no domain, energy, propagator, spectrum or vacuum follows.
- **Contrary review:** the exact `U(1,1)` plant prevents a hidden invariance
  claim; coupled contact and expanded-parent repairs stay live.

Hostile verdict:
`CANDIDATE_SURVIVES__CONDITIONAL_RANK4_EXISTS__ACTION_OWNERSHIP_NOT_ESTABLISHED`.

## Progress and next gate

```text
Ledger v0.214 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 4 conditions closed · 1 sharper ownership gate opened · 2 remain
```

No field, parameter, selector, quotient or external datum is added.
P1/P2/P3 remain unchanged and unused.

Next construct or kill an action-owned moving fundamental symmetry/reduction
that transports the phase-even `Q_B` covariantly. In parallel, retain the
coupled metric/section/gauge contact parent as the independent repair. Do not
attempt a Higgs spectrum until one route supplies rank four together with
observation/gauge basicness and an analytic domain.

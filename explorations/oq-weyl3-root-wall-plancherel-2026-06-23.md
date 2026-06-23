---
title: "OQ-weyl-3: Root-Wall Plancherel Support for lambda_RS in the Corrected A3 Analysis"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "oq-weyl3-root-wall-plancherel"
verdict: TAU_TWISTED_ADMISSIBLE_NOT_SCALAR_ATOM
---

# OQ-weyl-3: Root-Wall Plancherel Support for lambda_RS

## Scope

This note resolves the specific root-wall question left open by
`explorations/weyl-group-s4-orbit-2026-06-23.md` in light of the corrected A3 analysis in
`explorations/rc1-discrete-series-verification-pack-2026-06-23.md`,
`explorations/oq1-split-rank-verification-2026-06-23.md`, and
`explorations/oq3b-rs-index-8-2026-06-23.md`.

The question is:

```text
lambda_RS = (1/2, 0, 0, -1/2)
<e_2 - e_3, lambda_RS> = 0.
```

Does this root-wall condition:

1. kill the discrete Plancherel atom,
2. downgrade it to a limit-of-discrete-series contribution, or
3. remain admissible in the tau-twisted RS sector?

## Inputs Read

- `explorations/weyl-group-s4-orbit-2026-06-23.md`
- `explorations/oc1-noncompact-atiyah-jannich-2026-06-23.md`
- `explorations/oq3b-rs-index-8-2026-06-23.md`
- `NEXT-STEPS.md`
- `DERIVATION-PROGRESS.md`

Additional local context used:

- `explorations/oq-weyl3-limit-discrete-series-2026-06-23.md`
- `explorations/rc1-rs-kk-zero-mode-2026-06-23.md`
- `explorations/rc1-discrete-series-verification-pack-2026-06-23.md`
- `explorations/rc1-root-multiplicity-check-2026-06-23.md`
- `explorations/oq1-split-rank-verification-2026-06-23.md`
- `explorations/n5-plancherel-multiplicity-2026-06-23.md`

## 1. Corrected A3 Baseline

The corrected metric-involution analysis gives the scalar symmetric pair

```text
(G,H) = (SL(4,R), SO_0(3,1))
```

with the metric involution

```text
sigma_B(X) = -J X^T J^{-1},    J = diag(1,1,1,-1).
```

For this actual Lorentz-metric pair:

```text
p_G cap q_B = span{H_1,H_2,H_3,S_12,S_13,S_23},
maximal diagonal abelian subspace = span{H_1,H_2,H_3},
split-rank = 3.
```

Thus the scalar rank-one `BC_1` Flensted-Jensen pole story is not the safe baseline for
the corrected problem. The corrected scalar root system is A3 with positive roots:

```text
e_1-e_2, e_1-e_3, e_1-e_4, e_2-e_3, e_2-e_4, e_3-e_4.
```

The scalar Flensted-Jensen equal-rank test fails:

```text
split-rank(G/H) = 3,
rank(K/(K cap H)) = rank(SO(4)/SO(3)) = 1,
3 != 1.
```

So there is no established scalar discrete Plancherel atom in `L^2(G/H)` to protect by
the old rank-one argument. Any surviving RS contribution must come from the coefficient
problem `L^2(G x_H tau_RS)`, not from the scalar space.

## 2. The Wall Is Real But It Is Not the Formal-Degree Zero

The wall computation is exact:

```text
lambda_RS = (1/2, 0, 0, -1/2)
<e_2-e_3, lambda_RS> = 0.
```

This explains the nontrivial Weyl stabilizer:

```text
Stab_{S_4}(lambda_RS) = {id, (23)},
|W.lambda_RS| = 12.
```

But the A3 formal-degree polynomial used in the local Atiyah-Schmid calculation is evaluated
at `lambda_RS + rho_G`, not at `lambda_RS` alone. With

```text
rho_G = (3/2, 1/2, -1/2, -3/2),
lambda_RS + rho_G = (2, 1/2, -1/2, -2),
```

the root values are:

```text
<e_1-e_2, lambda_RS + rho_G> = 3/2
<e_1-e_3, lambda_RS + rho_G> = 5/2
<e_1-e_4, lambda_RS + rho_G> = 4
<e_2-e_3, lambda_RS + rho_G> = 1
<e_2-e_4, lambda_RS + rho_G> = 5/2
<e_3-e_4, lambda_RS + rho_G> = 3/2
```

Every factor is nonzero. Therefore:

```text
P(lambda_RS + rho_G) / P(rho_G)
= (3/2)(5/2)(4)(1)(5/2)(3/2) / (1)(2)(3)(1)(2)(1)
= 225/48 != 0.
```

The wall in `lambda_RS` does not create a zero in the formal-degree product actually used
by the A3 computation. In Harish-Chandra-parameter language, the regularity test is on the
shifted infinitesimal-character parameter. Here `lambda_RS + rho_G` is strictly regular.

This is the main correction to the earlier "limit-of-discrete-series boundary" phrasing.

## 3. Does the Wall Kill the Atom?

No, not by itself.

The wall `lambda_2 = lambda_3` only says that `lambda_RS` is a boundary dominant weight
with a repeated zero coordinate. It explains the Weyl stabilizer and orbit size. It does
not imply zero Plancherel weight, because the shifted A3 product has no vanishing root
factor.

However, the scalar A3 atom is still not established. The scalar problem fails the corrected
equal-rank test (`3 != 1`). Thus:

```text
The wall does not kill an atom.
But the scalar atom should not be claimed from the old rank-one argument.
```

The correct conclusion is sharper: the old scalar discrete atom is unavailable for a reason
independent of the `e_2-e_3` wall. The obstruction is the corrected metric-involution rank,
not the zero root value of `lambda_RS`.

## 4. Does It Downgrade to a Limit of Discrete Series?

Not in the literal sense used by the earlier note.

There are two separate notions that were being mixed:

1. Ordinary Harish-Chandra discrete series for `G`.
2. Relative or residual discrete contributions in `L^2(G/H,tau)`.

For `G = SL(4,R)`, ordinary group discrete series are already not the right object for the
GU fiber analysis. The relevant object is the relative/twisted Plancherel contribution in
`L^2(SL(4,R) x_{SO_0(3,1)} tau_RS)`.

Moreover, if the local `lambda_RS` is treated as a highest-weight-style parameter, then the
corresponding shifted parameter `lambda_RS + rho_G` is regular:

```text
<alpha, lambda_RS + rho_G> != 0 for every A3 root alpha.
```

So the specific `e_2-e_3` wall does not force a Harish-Chandra limit-of-discrete-series
classification. Calling the RS contribution "limit-of-discrete-series" is at best a
boundary-weight shorthand and should not be used as the Plancherel verdict.

If a boundary phenomenon remains, it is a tau-twisted residual-spectrum question, not an
ordinary scalar limit-of-discrete-series downgrade.

## 5. Does It Remain Admissible in the Tau-Twisted Sector?

Yes, conditionally. This is the best current verdict.

The RS coefficient is not scalar:

```text
tau_RS = S(6,4)|_{SO_0(3,1)}
       = 4D(1/2,0) + 4D(0,1/2).
```

The corrected OQ3b file keeps the RS index alive by treating the coefficient problem as
tau-twisted:

```text
L^2(G x_H tau_RS), not scalar L^2(G/H).
```

In that setting, the wall does not remove the H-type:

- the `S_4` orbit still has the unique dominant representative `lambda_RS`;
- the shifted A3 formal-degree product remains nonzero;
- the coefficient bundle supplies eight Lorentz spinor H-types;
- the physical RS degree-of-freedom count gives a chiral fiber `C^16`, hence `dim_H = 8`;
- the remaining analytic gate is the Oshima-Matsuki/Kobayashi admissibility or tau-correction
  theorem for the twisted space.

Thus the root-wall concern should be marked:

```text
NOT A KILLER.
NOT A SCALAR LIMIT-DS RESOLUTION.
TAU-TWISTED ADMISSIBLE, CONDITIONAL ON THE OQ3b TAU-CORRECTION/H-ADMISSIBILITY GATE.
```

## 6. Consequences for OQ3b

OQ3b should retain `ind_H(D_RS) = 8` at reconstruction grade, but the representation-theoretic
route must be phrased carefully.

Surviving parts:

```text
Physical RS count:
(4 vector components - 1 gamma-trace - 1 gauge) x C^16 = C^32,
chiral half = C^16,
dim_H(C^16) = 8.
```

```text
H-type content:
S(6,4)|_H = 4D(1/2,0) + 4D(0,1/2).
```

```text
A3 shifted product:
P(lambda_RS + rho_G)/P(rho_G) = 225/48 != 0.
```

What must be demoted:

```text
Do not claim a scalar rank-one Flensted-Jensen atom for SL(4,R)/SO_0(3,1).
Do not claim the root wall is a harmless BC1 compact root in the corrected A3 scalar model.
Do not use the old scalar BC1 pole ladder as the decisive proof.
```

What remains as the live OQ3b gate:

```text
Prove the tau-twisted Oshima-Matsuki/Kobayashi admissibility statement for
tau_RS = 4D(1/2,0) + 4D(0,1/2).
```

If that gate passes, OQ3b remains `CONDITIONALLY_RESOLVED` with RS index 8. If it fails,
the physical H-line count remains a kinematic count but no longer proves a Fredholm/Plancherel
index contribution.

## 7. Consequences for OC1

OC1 should remain conditional, not closed.

The noncompact Fredholm statement in `oc1-noncompact-atiyah-jannich-2026-06-23.md` depends
on a genuine discrete or residual tau-twisted sector:

```text
P_disc L^2(Y^14, H^64)
```

must be interpreted as the tau-twisted RS/spinor discrete sector, not the scalar discrete
sector of `L^2(SL(4,R)/SO_0(3,1))`.

Updated OC1 consequences:

- Noncompactness still does not by itself kill the Fredholm framework.
- The scalar rank-one discrete-sector argument is not valid after the corrected A3 analysis.
- The root wall does not create a formal-degree zero and should not be listed as the primary
  obstruction.
- The primary obstruction is now the tau-twisted admissibility/Fredholm projection:

```text
Does L^2(SL(4,R) x_{SO_0(3,1)} tau_RS) contain the required discrete/residual summand
with finite multiplicity 8?
```

If yes, OC1's discrete-sector Fredholm completion survives. If no, OC1 loses the RS piece
and the `ind_H = 24` noncompact Fredholm claim collapses to a spin-1/2-only or continuous-
spectrum problem.

## 8. Failure Conditions

**F1: Shifted A3 product error.** If the formal-degree calculation should use `P(lambda_RS)`
instead of `P(lambda_RS + rho_G)`, then the `e_2-e_3` factor vanishes and the note's
nonzero-product argument fails. Current local conventions use `lambda + rho_G`; under those
conventions F1 does not fire.

**F2: Tau-twisted admissibility fails.** If the Oshima-Matsuki/Kobayashi condition for
`L^2(G x_H tau_RS)` fails, then the RS representation has no finite discrete/residual
Plancherel contribution. Consequence: `ind_H(D_RS) = 8` is not analytically established,
and OC1 loses its RS discrete Fredholm sector.

**F3: H-type branching fails.** If

```text
S(6,4)|_{SO_0(3,1)} != 4D(1/2,0) + 4D(0,1/2),
```

then the eight-H-line RS count changes.

**F4: Scalar A3 atom is asserted without twist.** If a future note continues to claim a
scalar rank-one Flensted-Jensen atom for the corrected metric pair, it is using the wrong
involution or an unproved rank-reduction. The corrected scalar A3 analysis does not support
that claim.

**F5: Continuous-spectrum fallback.** If the tau-twisted contribution is only continuous
Plancherel support, not a discrete/residual finite-multiplicity summand, then it does not
produce an integer Fredholm index by the Atiyah-Schmid sum. This would reopen OC1 and OQ3b.

## 9. Verdict

The root wall

```text
<e_2-e_3, lambda_RS> = 0
```

does **not** kill the RS Plancherel contribution by a vanishing A3 formal-degree factor.
The shifted parameter `lambda_RS + rho_G` is regular and gives the nonzero local product
`225/48`.

It also should **not** be classified as an ordinary limit-of-discrete-series downgrade.
For the corrected Lorentz-metric A3 problem, the scalar discrete atom is not established
at all; the surviving representation-theoretic claim is tau-twisted.

Best current answer:

```text
lambda_RS remains admissible in the tau-twisted RS sector,
conditional on proving the Oshima-Matsuki/Kobayashi tau-correction/H-admissibility gate.
```

Consequently:

```text
OQ3b remains CONDITIONALLY_RESOLVED, with the physical 8-line count intact.
OC1 remains CONDITIONALLY_RESOLVED only if its P_disc is read as the tau-twisted
discrete/residual sector, not the scalar A3 sector.
```

## References

- Flensted-Jensen, M. (1980). Discrete series for semisimple symmetric spaces.
- Oshima, T. and Matsuki, T. (1984). A description of discrete series for semisimple
  symmetric spaces.
- Kobayashi, T. (1994, 1998). Discrete decomposability of restrictions of Harish-Chandra
  modules.
- Local: `explorations/weyl-group-s4-orbit-2026-06-23.md`.
- Local: `explorations/oq3b-rs-index-8-2026-06-23.md`.
- Local: `explorations/oc1-noncompact-atiyah-jannich-2026-06-23.md`.
- Local: `explorations/rc1-discrete-series-verification-pack-2026-06-23.md`.
- Local: `explorations/oq1-split-rank-verification-2026-06-23.md`.

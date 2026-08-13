---
artifact_type: build_result
created: 2026-08-08
status: ACTION_OWNED_DEGREE14_EPSILON_COMPANION_EXACT__MOVING_K77_OBSERVATION_INSERTION_OPEN
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 action-owned degree-fourteen companion

## Result in plain English

The missing degree-fourteen partner now has an action-derived formula. It is
not the draft's printed `Xi=D Upsilon`.

The selected first-order action has two connection directions, `B` and
`T=A-B`, plus a Shiab map that moves with `epsilon`. Varying `epsilon` changes
all three. Consequently the degree-fourteen Euler owner paired with the
zero-form epsilon variation is

```text
E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S.          (1)
```

Both connection Euler owners and the moving-Shiab term are independently
necessary. An exact noncyclic rational fixture differentiates all nine matrix
directions and rejects every deletion. It also rejects both signs of the naive
replacement `D_A E_T`.

This closes the formula/type gap left by ledger v0.63. It does not yet insert
the formula coefficientwise into the full moving K77 Hodge/Krein/observation
graph, antisymmetrize the Green current, select a common domain, or construct a
BFV phase space.

## 1. Layer 0

| phrase | object here | distinct object |
| --- | --- | --- |
| printed `Xi` | `D_omega Upsilon_print`, redundant after the printed residual vanishes | action derivative, because `Upsilon_print` is superseded on the selected noncyclic domain |
| action companion | equation (1), the top-degree dual of primitive epsilon variation | homogeneous gauge Ward identity |
| primitive epsilon equation | a generally nonzero Euler equation | a Noether identity that vanishes off shell |
| Green owner | boundary pairing of `eta` with normal `E_B-E_T` | antisymmetrized presymplectic current or reduced charge |

The degree count is literal in fourteen dimensions. `B` and `T` are one-forms,
their Euler density duals have degree thirteen, `eta` has degree zero, and
integrating the `D_B eta` term by parts produces a degree-fourteen epsilon
dual. The moving-Shiab orbit covector lands in the same top-degree target.

## 2. Source collision

The 2021 draft prints

```text
Xi_print = D_omega Upsilon_print
```

and describes it as redundant once the printed residual vanishes. The source
does not derive equation (1). K77-B3 already proves that the printed endpoint
is not the derivative of the selected noncyclic action. The repository's
earlier primitive-epsilon calculation did contain equation (1), but it had not
been recognized as the missing action-owned degree-fourteen companion.

```text
SOURCE-CONFIRMS: printed Xi is D Upsilon and is on-residual redundant
REPO-DERIVES:    action companion is D_B^!(E_B-E_T)+(D_epsilon S)^!K_S
SOURCE-SILENT:   coefficientwise moving K77 observation insertion and BFV
```

## 3. Exact certificate

For the frozen rational noncyclic Shiab fixture, entrywise Fréchet
differentiation gives nonzero, distinct connection Euler matrices `E_B` and
`E_T`. Their covariant-adjoint contribution and the moving-Shiab contribution
are also separately nonzero. The complete epsilon owner is

```text
E_epsilon =
[[-326/21,  -71/21, 145/14],
 [-1007/42, -201/7,  -25/42],
 [  58/7,  -508/21, 929/21]].
```

For the held-out epsilon direction its pairing is `-103/42`. The same identity
passes independently on all nine matrix units. Three planted omissions fire:
dropping `E_B`, dropping `E_T`, or freezing Shiab changes the answer. A fourth
control shows `E_epsilon` differs from both signs of the naive covariant
derivative of `E_T`.

The homogeneous moving-Shiab gauge contraction vanishes exactly on the same
fixture, while the primitive epsilon Euler pairing is nonzero. This is the
decisive control preventing an Euler equation from being relabeled as Ward.

Main probe: `37/37 PASS`, including the complete v0.63 predecessor replay.

## 4. Symplectic review

Equation (1) is one first variation. A covariant presymplectic current requires
the antisymmetrized second variation of the action's preboundary potential.
The existing Green flux locates a boundary owner but does not perform that
antisymmetrization, prove basicness, select boundary conditions, or construct a
reduced charge. The next wave must move Hodge, Krein pairing, Shiab,
background, target, section, labelled reduction and reciprocal null label
together before performing it.

## 5. Seven-axis disposition

- **Layer 0:** printed Xi, primitive epsilon Euler, homogeneous Ward, Green
  owner and presymplectic current are separated.
- **L1 syntactic:** source formulas and the existing primitive-epsilon chain
  are located.
- **L2 type:** the `13+1=14` and `0+14=14` pairings close.
- **L3 algebraic:** exact entrywise Fréchet/adjoint identity passes.
- **L4 geometric:** fixed finite noncyclic fixture; actual moving K77 bundle
  insertion remains open.
- **L5 variational:** the epsilon Euler companion is derived; antisymmetrized
  preboundary and BV/BFV remain open.
- **L6 analytic:** no common closed, self-adjoint or hyperbolic domain is
  inferred.
- **L7 physical:** no Einstein, Standard Model, spectrum or cosmology claim.

## 6. Ledger v0.64

```text
Ledger v0.64 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 0
remaining_named_conditions: 1
```

Five rows migrate in distance, evidence and mapping grade only. P1/P2/P3,
verdicts, residue, quotients, canon and public posture stay frozen.

Next:

`MOVING_HODGE_KREIN_SECTION_TARGET_GREEN_IDENTITY_ON_ACTION_EULER__THEN_ANTISYMMETRIZE`.

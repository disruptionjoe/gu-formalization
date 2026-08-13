---
artifact_type: construction_result
created: 2026-08-13
status: CONSTANT_COMPLETION_FALSIFIED__MOVING_COVARIANT_COMPLETION_OPEN
source_return: SOURCE_CONFIRMS_AND_SOURCE_SILENT
ledger_change: none
target_claim: NONE-NOT-A-KILL
scripts:
  - tests/channel-swings/selected_k77_i2b_frozen_hessian_compatibility_probe.py
---

# Selected K77 I2B frozen-Hessian compatibility gate

## Result first

The exact fourteen-row principal compatibility family does **not** extend
through the complete frozen-coefficient residual-square Hessian by adding a
constant lower-order correction. This is an exact finite obstruction, but it
is deliberately narrower than a Noether/BV no-go.

Write the frozen linearized Hessian as

\[
 H(k)=H_2(k)+H_1(k)+H_0,
 \qquad C(k)=\sum_{\mu=0}^{3}k_\mu C_\mu, \tag{1}
\]

where `C_mu` selects equation rows `(mu,a)`, `a=0,...,13`. A constant
completion `C_0` would have to make

\[
 (C(k)+C_0)H(k)=0. \tag{2}
\]

The exact selected K77 blocks give

```text
rank H0:                         196 / 196
rank H1_mu:                     0, 0, 0, 0
rank span(B00):                 182
rank span(B00,B01):             196
degree-two defect ranks:        0 x 10
degree-one defect ranks:        14,14,14,14
combined degree-one defect:     56 / 56
```

Because the principal blocks span the entire equation carrier, the degree-two
equations force `C_0=0` uniquely. With that forced value, the degree-one
equations reduce to `C_mu H0`; each has rank fourteen, and all four together
have rank fifty-six. There is therefore no constant-coefficient completion.

This is the positive information in the negative result: the remaining route
cannot be another frozen algebraic correction. It must come from coefficient
motion in the covariant operator—moving `Q_B`, `H_q`, Shiab, section,
observation, and the affine source connection—or else the principal family is
not the leading part of a complete Noether/BV identity.

## Layer 0

| phrase | exact object here | not identified with |
| --- | --- | --- |
| frozen Hessian | full `196 x 196` residual-square Hessian with all coefficients held fixed | the complete stationary linearization with coefficient derivatives |
| `H0` | Gram plus the residual-dependent `Upsilon.D2Upsilon` term | a mass matrix or physical spectrum |
| compatibility | the fourteen principal rows `C(k)` | source gauge, nonlinear Bianchi identity, or BV differential |
| constant completion | one `14 x 196` algebraic matrix `C0` | a moving covariant divergence or connection term |
| rank-56 defect | four independent rank-14 polynomial coefficients | particles, constraints, anomalies, or degrees of freedom |

The background residual is nonzero and Krein-null, so omitting the
residual-dependent second variation would change `H0`. The same restricted
radial branch is nonstationary on the full 196-cell field bank. The separately
constructed stationary connection two-jet cancels the Euler covector at the
base point, but its moving-coefficient contribution to the arbitrary-field
Hessian has not yet been assembled. Those two facts must not be compressed
into “the stationary theory violates Bianchi.”

## Exact polynomial test

At polynomial degree three, the predecessor already proves `C(k)H2(k)=0`.
At degree two, (2) requires

\[
 C_\mu H_{1,\nu}+C_\nu H_{1,\mu}+C_0B_{\mu\nu}=0. \tag{3}
\]

Every `H1_mu` vanishes. Since `B00` and `B01` jointly have full row rank,
(3) forces `C0=0`. All ten degree-two equations then pass exactly.

At degree one, (2) requires

\[
 C_\mu H_0+C_0H_{1,\mu}=0. \tag{4}
\]

With `C0=0`, the four left sides have rank fourteen apiece and combined rank
fifty-six. They contain 40 nonzero coefficients each, 160 in total. A planted
nonzero `C0` breaks the mixed principal block, while deleting `H0` falsely
erases the obstruction.

## Hostile scope

The strongest overreach would be to call this a failure of every Bianchi or
Noether identity. A covariant divergence has connection and coefficient-
derivative terms that are absent from this frozen calculation. The earlier
Ward chain has already shown that such terms can cancel raw derivative
failures at constant and parameter-jet grades. That prior art makes the moving
successor mandatory, not optional.

The result also says nothing about constraint propagation, hyperbolicity,
Krein positivity, closed domains, global descent, spectrum, stability,
preboundary reduction, or physical carrier. The nonzero preboundary owner is
unchanged.

## Source return

The source material confirms the I2B residual square, a distinct `Q_B`
primalizer slot, the moving Shiab/observation grammar, and an affine source
connection. It does not state this exact frozen polynomial decomposition,
the full-rank `H0`, the rank-56 defect, or a complete moving Noether/BV
identity.

```text
SOURCE-CONFIRMS: I2B residual-square and moving connection/primalizer grammar
SOURCE-SILENT:   exact frozen completion obstruction and its covariant repair
```

## Constraint fence and next gate

```text
new fields: 0
new coefficients: 0
new selectors: 0
new quotients: 0
P1/P2/P3 consumed: 0
ledger/canon/residue/posture movement: 0
```

Next, construct the complete stationary coefficient derivative on **all**
196 field directions through the already-owned stationary two-jet, moving
`Q_B/H_q`/Shiab/section/observation data, and affine source connection. Apply
the covariantized fourteen-row operator coefficientwise. Exact cancellation
would promote a local Noether-identity candidate; a surviving defect after
all owners are present would be the first genuine local obstruction.

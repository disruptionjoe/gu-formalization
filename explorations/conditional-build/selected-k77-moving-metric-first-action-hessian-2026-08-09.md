---
artifact_type: exact_construction_and_scope_result
created: 2026-08-09
status: SELECTED_SPIN_MOVING_METRIC_HESSIAN_COMPLETE__FULL9_HORIZONTAL9_OFFSLICE4__321_REMAINS_NOT_CLOSED
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected-K77 moving metric first-action Hessian

## Result in plain English

The ten missing metric columns of the selected-Spin first-action Hessian are
now complete at local principal-symbol grade.

The frozen calculation from v0.122 was not missing an extra cancellation.
At either exact stationary branch, all metric, density, pairing, Hodge, Phi,
Shiab, frame and observation motion can be evaluated in the exact co-moving
K77 frame. The geometric coefficients are then stationary. The only remaining
motion is the source-owned Levi-Civita chain at fixed `varpi`, already encoded
by the cached `(delta B,delta T)=(-u,u)` columns. Density and receiver terms
multiply the zero Euler covector and vanish.

The complete metric block has the same exact ranks in every causal class and
both `QQ(sqrt(3))` branches:

| receiver | rank |
|---|---:|
| all 1,274 grade-two equations | 9 |
| observed-horizontal 24 | 9 |
| off-slice 1,250 | 4 |

Together with v0.123's complete epsilon ranks `91/6/88`, this confirms that
the 321-field selected-Spin truncation is not Hessian-closed. It does **not**
select the full 1,571-coordinate low-grade parent and does not create an
equation quotient. The next construction must type the off-slice image as
either a minimal source/action-owned tangent closure or a derived constraint
image. An algebraic cokernel alone is not sufficient.

## Layer 0

| phrase | object proved here | object kept distinct |
|---|---|---|
| moving metric Hessian | local principal `D_g E_T` on the first-transgression action | raw `D_g Upsilon` and residual-square Hessian |
| metric source direction | fixed-`varpi,epsilon` chain through `B_LC` and `T=varpi-B_LC` | independent `B` at fixed `T` |
| co-moving completion | intrinsic Hessian in a frame where the K77 coefficient geometry is stationary | seven separately invariant owner terms |
| stationarity | zero source Euler covector on the two exact local branches | a global saddle, selected amplitude or complete tangent |
| off-slice image | rank-four metric and rank-88 epsilon equation response | an action-derived constraint quotient |
| selected parent | conditional real `Spin(7,7)` low-grade carrier | two `U(32,32)` halves and full `U(64,64)` |

## Why the moving terms do not repair the block

For a field-frame change `x=R(g)y`, an Euler covector transforms as

```text
E_y = R(g)^T E_x.
```

Differentiating gives

```text
d_g E_y = (d_g R^T) E_x + R^T d_g E_x.
```

The first term vanishes at a stationary point. The same is true of the volume
term `(d_g log rho) E`. The v0.67 exact ten-normal bank supplies a compensator

```text
A_a = -(1/2) G_Y^-1 d_a G_Y
```

for which metric, density, degree-two pairing and Hodge transport are exact.
The tautological Phi/Shiab packet is functorial in the same frame, while v0.68
proves complete cotangent naturality. Thus, at local principal grade, the
intrinsic metric Hessian can be computed in the co-moving frame with those
coefficients frozen.

The source-coordinate field chain remains live. At fixed `varpi`,

```text
delta T = -delta B_LC,
delta A = 0,
delta F_A = 0.
```

The last equality is an expanded cancellation. The calculation never
differentiates the branch identity `F_A=T^2` as though it were an off-branch
definition.

## Exact construction

The primary probe loads the versioned v0.124 bank through its hash-verifying
API; it executes no recursive predecessor. The ten metric columns are
evaluated on both Galois branches and on timelike, spacelike and null symbol
representatives. Exact sparse elimination over `QQ(sqrt(3))` gives `9/9/4`
in all six cases.

The independent Sage/FLINT route reads only the serialized rational bank and
rebuilds all six matrices. It reproduces the same ranks. A separate exact
cotangent calculation checks that receiver transport vanishes at a zero Euler
covector and is live off shell.

## Source return

```text
SOURCE-CONFIRMS:
  source coordinates (g,varpi,epsilon), the two-connection difference,
  metric-dependent gimmel/Hodge/Phi/Shiab geometry and observation.

REPO-DERIVES:
  co-moving stationary completion of the ten selected-Spin metric columns
  and exact 9/9/4 ranks on both branches and all causal classes.

SOURCE-SILENT:
  the 321 truncation, complete Hessian ranks, expanded tangent, equation
  quotient, action-parent choice and physical interpretation.
```

## Efficient specialist assessment

Every entry below is **ACTUAL MATH**; no analogy is used.

- **Layer-0 semantics — very high confidence.** Exact object: `D_g E_T`, not
  `D_g Upsilon`. Strongest attack: the bank may encode the wrong source
  tangent. Cheapest test: compare its `(-u,u)` chain with the fixed-`varpi`
  source registry. Scope: local selected-parent principal block.
- **Prior art — very high.** Exact object: composition of v0.67, v0.68, v0.95,
  v0.111, v0.123 and v0.124. Attack: accidentally advertise an old rank as
  new. Test: dependency-by-dependency object table. Scope: no predecessor
  theorem is rederived.
- **Differential geometry — high.** Exact object: one co-moving vielbein
  compensator for metric, density, Hodge, pairing and Phi/Shiab. Attack:
  physical metric motion is not merely a frame change. Test: retain the
  Levi-Civita first jet separately. Scope: pointwise coefficients plus local
  principal jet.
- **Representation/Clifford — high.** Exact object: grade-two equation dual of
  the selected real-Spin carrier. Attack: a zero or rank may change under the
  two-half or full-unitary parent. Test: explicit parent fence. Scope: no port.
- **Variational bicomplex — high.** Exact object: mixed derivative of an Euler
  covector at a stationary source branch. Attack: density/receiver terms need
  not vanish off shell. Test: nonstationary plant. Scope: first action only.
- **Symplectic/BV-BFV — high.** Exact object: cotangent-natural Hessian prior to
  quotient. Attack: treating epsilon as gauge would erase a live endpoint
  charge. Test: preserve v0.123's primitive source direction and forbid a
  quotient by fiat. Scope: no BV/BFV promotion.
- **Operator/Krein — very high.** Exact object: finite exact sparse block on an
  indefinite carrier. Attack: rank says nothing about closed domains or
  positivity. Test: make no analytic inference. Scope: algebraic local gate.
- **Adversarial scope — very high.** Exact object: a truncation failure, not a
  GU no-go. Attack: “321 killed” can be misread as “GU killed.” Test: retain
  expanded-parent and derived-quotient horns. Scope: selected Spin only.
- **Exact-computation architecture — very high.** Exact object: hashed rational
  bank. Attack: stale or recursively rebuilt cache. Test: verified API load
  and independent Sage replay. Scope: coefficient reuse.
- **Invariant theory — high.** Exact object: causal-orbit and Galois-branch rank
  invariance. Attack: one representative hides exceptional rank. Test: all
  three classes and both branches. Scope: declared local orbit census.
- **PDE/microlocal — medium.** Exact object: principal-symbol matrix. Attack:
  lower-order terms or domains change propagation. Test: label them open.
  Scope: no hyperbolicity or Green theorem.

## Hostile disposition

Verdict:
`CANDIDATE_SURVIVES_WITH_PRINCIPAL_AND_PARENT_SCOPE__MOVING_METRIC_BLOCK_COMPLETE`.

The strongest surviving caveat is that this is a local principal result on a
conditional action parent and stationary branch. It does not decide the
complete lower-order/global Hessian, parent selection, amplitude, analytic
domain or physical quotient.

## Progress and next gate

```text
Ledger v0.125 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
conditions_closed: 2
  - completed all ten moving metric/source first-action columns
  - decided the selected 321 metric-plus-epsilon closure question: not closed
conditions_opened: 0
remaining_named_conditions: 1
```

Next:
`CLASSIFY_OFFSLICE_IMAGE_AS_MINIMAL_SOURCE_TANGENT_CLOSURE_OR_DERIVED_CONSTRAINT_IMAGE__NO_QUOTIENT_BY_FIAT`.

Evidence:

- primary probe: `49/49 PASS`;
- independent Sage/FLINT: `12/12 PASS`;
- P1/P2/P3 unchanged and unused.

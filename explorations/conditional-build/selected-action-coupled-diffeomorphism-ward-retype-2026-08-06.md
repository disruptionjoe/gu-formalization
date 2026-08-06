---
artifact_type: layer0_correction_and_coupled_ward_target
created: 2026-08-06
status: COUPLED_DIFFEO_ORBIT_CORRECTS_METRIC_ONLY_TARGET__ACTUAL_I1B_BLOCKS_OPEN
lane: "1"
functional_channels: [COMPOSE, BUILD, SOURCE, VERIFY]
source_return: SOURCE-CORRECTS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_action_coupled_diffeomorphism_ward_retype_probe.py
registry: lab/process/selected-action-coupled-diffeomorphism-ward-retype.json
---

# Selected-action coupled diffeomorphism Ward retype

## Result first

The v0.31 `34+21` theorem is exact, but it was attached to a stronger target
than the source action requires.

That theorem asks for a symmetric ten-by-ten metric companion `C` satisfying

\[
 C D=-H_{gg}^{\rm spin}D,
\]

where `D` is the metric diffeomorphism symbol. This is the correct Ward
problem only after suppressing every nonmetric component of the gauge orbit.
The source action does not live on metrics alone: its domain contains the
inhomogeneous gauge data and `MET(X)`, and its augmented torsion is an
adjoint-valued one-form. A diffeomorphism therefore moves both the metric and
that one-form.

On the observed horizontal slice of the invariant background
`T_mu^nu=t delta_mu^nu`, the principal Lie derivative is

\[
 (G_T(k)\xi)_\mu{}^\nu=k_\mu\xi^\nu .
\]

`G_T(k)` has rank four for every nonzero timelike, spacelike and null
covector. The principal gauge generator **restricted to this minimal observed
horizontal vector-one-form subcarrier** is therefore

\[
 R(k)=\binom{D(k)}{G_T(k)},
\]

not `(D,0)`.

Holding the already computed metric block fixed, exact rational linear
algebra constructs symmetric coupled Hessians with `H R=0` and **no added
metric-metric companion at all**. On this `10+16` minimal subcarrier, the
unknown metric--connection and symmetric connection blocks have dimension
`296`; the coupled Ward system has rank `98` and affine dimension `198`.
Those numbers measure uncomputed block freedom, not physical parameters, and
are not the dimensions of the full adjoint-valued one-form problem.

This is a queue correction, not a completed action. The next calculation is
the actual same-`I1B` block Hessian

\[
 H_{I1B}=\begin{pmatrix}H_{gg}&H_{gT}\\H_{Tg}&H_{TT}\end{pmatrix}
\]

together with the complete principal diffeomorphism lift. It must satisfy both
block Ward equations. Agents should no longer search for an arbitrary
ten-by-ten metric completion or try to match 34 metric-only directions.

No field, coefficient, quotient or datum is added.

## Plain English

The last wave treated a diffeomorphism as if it moved only the metric. But the
GU action contains a connection-like one-form too, and diffeomorphisms move
that field at the same time.

Once that missing part of the gauge motion is restored, the apparent demand
for a new metric term disappears. The cancellation can happen in the cross
terms between the metric and the connection field. We constructed exact
examples showing this on all three causal kinds of momentum while leaving the
old metric Hessian unchanged.

That does not prove GU's written action performs the cancellation. It tells us
the right next question: calculate the actual metric--connection cross terms
and connection Hessian from the same action, then test the full coupled Ward
identity.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| v0.31 Ward target | metric-only slice `(D,0)` and a ten-by-ten companion | full source-action gauge orbit |
| minimal source-native principal slice | `(D,G_T)` on metric plus the observed horizontal vector-one-form component | full adjoint-valued one-form orbit or connection Lorentz gauge alone |
| coupled completion | a symmetric block matrix radical on `(D,G_T)` | action-derived `I1B` coefficients |
| `198` directions | affine freedom among uncomputed cross/connection blocks | 198 residue parameters or physical modes |
| full Ward radical | degeneracy of the stationary unreduced field Hessian | BV cohomology or BFV phase space |
| observation | a separate field/receiver map | the connection Lie derivative |

The v0.31 theorem remains valid as a metric-only linear-algebra statement. Its
scope, not its arithmetic, is corrected.

## Source collision

The primary-source pack records

\[
 I_1^B:\mathcal G\times\operatorname{MET}(X^{1,3})\to\mathbb R,
 \qquad T_\omega\in\Omega^1(Y,\operatorname{ad}P).
\]

The UCSD source separately describes the action-derived tensor as
perpendicular to diffeomorphism orbits. Read together, these statements do not
license replacing the full orbit by its metric projection. The older
selected-branch report already states the correct abstract theorem using all
primitive fields and the complete gauge generator; v0.31 accidentally
specialized it too early.

```text
SOURCE-CORRECTS: the Ward object is the full metric-plus-connection orbit
SOURCE-SILENT:   actual H_gT and H_TT coefficients, complete nonlinear lift,
                 odd BV, global domain and BFV
```

## Exact coupled construction

Let `H` be the v0.30 metric block, `D` the rank-four metric symbol and `G` the
rank-four one-form Lie symbol. Set

\[
 L=(G^TG)^{-1}G^T,
 \qquad Q=(1_{10},-DL).
\]

Then `LG=1_4`, so `Q(D,G)^T=0`. Therefore

\[
 H_{\rm diagnostic}=Q^THQ
 =\begin{pmatrix}
 H&-HDL\\
 -L^TD^TH&L^TD^THDL
 \end{pmatrix}
\]

is symmetric, has the original `H` as its metric block, and annihilates the
complete gauge image on both sides. Its metric--connection cross block is
nonzero and load-bearing.

This construction is deliberately diagnostic. The Euclidean left inverse
`L` is not promoted as GU geometry. It proves only that Ward symmetry does not
force a metric-metric companion once the correct field-space orbit is used.

## Identifiability count

With `H_gg=H` fixed on this minimal `10+16` slice, the unknown blocks are

- `H_gT`: `10 x 16 = 160` entries; and
- symmetric `H_TT`: `16*17/2 = 136` entries.

The `296` unknowns map to the `26 x 4` Ward equations. Exact row reduction on
all three causal representatives gives

\[
 \operatorname{rank}\mathcal W_{D,G}=98,
 \qquad \dim\ker\mathcal W_{D,G}=296-98=198.
\]

The target produced by the fixed metric block is compatible. These are slice
counts, not a census of the full `Omega1(Y,ad P)` Hessian. By contrast,
the metric-only problem has rank `34` and affine dimension `21`. Both counts
are correct for their own domains; only the coupled count types the current
source-action problem.

## Corrected queue

1. Compute the actual same-`I1B` `H_gT` and `H_TT` blocks from the moving
   Hodge/Shiab/Krein/density/coframe and connection dependence already built.
2. Construct the complete principal diffeomorphism lift on the selected
   stationary background, including coefficient/internal transport rather
   than only the displayed horizontal `G_T` slice.
3. Test both block equations

   \[
   H_{gg}D+H_{gT}G_T=0,
   \qquad H_{Tg}D+H_{TT}G_T=0.
   \]

4. Only after exact closure build the diffeomorphism/odd BV complex, global
   domain and BFV. Keep `I2B` to observer full-`II` as the separate `LT-GR3`
   owner-map gate.

## Ledger v0.32

```text
Ledger v0.32 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Five distances are corrected. Verdicts, reason kinds, revival triggers,
residue, quotient count and P1/P2/P3 do not move.

## Seven-axis disposition

- **Layer 0:** metric-only and full field-space Ward objects are separated.
- **L1 syntactic:** the coupled block equations and gauge generator are named.
- **L2 type:** the source action owns both metric and connection-one-form
  directions.
- **L3 algebraic:** ranks `4`, `98` and affine dimension `198` are exact on all
  causal representatives.
- **L4 geometric:** the horizontal invariant-background Lie symbol is exact;
  the complete global natural lift remains open.
- **L5 variational/symplectic:** coupled Ward solvability is exact, but the
  action-derived blocks and reduced covariant phase space remain open.
- **L6 analytic:** no global Green/Krein or hyperbolic-domain claim.
- **L7 physical:** no Einstein recovery, graviton, cosmology, Q1 or unitarity
  claim.

## Constraint fence

```text
new fields: 0
new coefficients: 0
new quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.

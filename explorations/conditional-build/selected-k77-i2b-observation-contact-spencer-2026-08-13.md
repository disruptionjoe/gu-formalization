---
artifact_type: construction_result
created: 2026-08-13
status: LOCAL_STATIONARY_OBSERVATION_DUAL_CLOSED__FIRST_SPENCER_COKERNEL_EXACTLY_14
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_CONFIRMS_AND_SOURCE_SILENT
ledger_change: none
scripts:
  - tests/channel-swings/selected_k77_i2b_observation_contact_spencer_probe.py
---

# Selected K77 I2B observation/contact and first Spencer gate

## Result first

Two immediate gates are now exact, with different outcomes.

First, complete equation-dual observation does **not** reopen the already
covariantly closed Euler row at a stationary point. If `O` is the inverse-
transpose equation receiver and `E` the Euler covector, then

\[
 \delta(OE)=(\delta O)E+O\,\delta E. \tag{1}
\]

On the stationary Ward locus `E=0` and `delta E=0`, both terms vanish. The
same exact rational receiver has a nonzero `delta O E` away from stationarity,
so this is not a frozen-observation trick. It is also not a statement about
the preboundary term: the previously constructed observation/soldering
preboundary contact remains nonzero.

Second, the complete selected ten-block holonomic symbol is not formally
surjective after one prolongation. Its first prolongation

\[
 \sigma^{(1)}:\operatorname{Sym}^3(T^*X)\otimes F_{196}
 \longrightarrow T^*X\otimes E_{196} \tag{2}
\]

has exact rank `770` in a `784`-dimensional receiver. The cokernel is exactly
fourteen-dimensional. It is spanned by the rational divergence-shaped rows

\[
 C_a(v)=\sum_{\lambda=0}^{3}v_{\lambda,(\lambda,a)},
 \qquad a=0,\ldots,13. \tag{3}
\]

Every `C_a` annihilates every column of (2), the fourteen rows have disjoint
pivots, and changing one relative sign breaks the identity. Two independent
good-prime reductions reproduce rank `770` and the same twenty-step rank
profile. Therefore (3) is the entire first compatibility cokernel, not a
sampled relation.

This is a useful narrowing: the next problem is no longer an unspecified
Spencer failure. It is whether the fourteen linear divergence identities
extend to the complete nonlinear/moving-primalizer source equation and are
owned by a Bianchi/Noether/BV identity. Nothing here proves that ownership.

## Layer 0

| phrase | exact object here | not identified with |
| --- | --- | --- |
| equation observation | inverse transpose of the complete section-germ map acting on Euler covectors | naive pullback of residual forms |
| stationary no-reopening | equation (1) at `E=0`, `delta E=0` | an off-shell observation theorem |
| contact | coefficient motion in (1) | the separately nonzero Green/preboundary contact term |
| source connection | affine inhomogeneous connection that covariantizes jets | the effective homogeneous 196-real distortion carrier |
| first prolongation | equation (2) for the complete ten symmetric principal blocks | zeroth symbol surjectivity or full formal involutivity |
| compatibility family | the fourteen rows (3) on `T*X tensor E_196` | the source `Cl2` gauge map, a physical constraint count, or BV cohomology |

The `a=0,...,13` label is the existing Clifford-vector coordinate on the
equation carrier. Calling it fourteen particles or fourteen gauge generators
would be a category error.

## Exact construction

The complete observation germ is represented by the same block triangular
map used in the physical soldering chain,

\[
 M(J)=\begin{pmatrix}I&J^T\\0&I\end{pmatrix},\qquad
 O=M(J)^{-T}. \tag{4}
\]

Differentiating `O M^T=I` gives

\[
 (\delta O)M^T+O\,\delta M^T=0, \tag{5}
\]

which the rational fixture verifies coefficientwise. Equations (1) and (5)
then prove the stationary result without fitting a contact cancellation.

For the Spencer calculation, write the complete principal Euler operator as

\[
 E_i=\sum_{\mu\leq\nu}B^{\mu\nu}_{ij}u^j_{\mu\nu}. \tag{6}
\]

The ten `196 x 196` blocks are rebuilt directly from the selected K77
principal responses. A sparse one-cell assembly is independently checked
against the predecessor's exact rank-182 timelike Gram. For every symmetric
third jet `u^j_alpha`, differentiation of (6) places the block
`B^(alpha-e_lambda)` in the `lambda` equation row. There are `20 x 196 =
3920` such domain columns and `4 x 196 = 784` receiver rows.

Exact modular elimination gives the cumulative ranks

```text
182,364,378,378,560,574,574,574,574,574,
756,770,770,770,770,770,770,770,770,770
```

for both primes `1000003` and `1000033`. Because rank cannot exceed 784 and
the fourteen rational rows (3) are independent annihilators, the rational
rank is exactly 770 and the cokernel is exactly their span.

## Symplectic and analytic scope

Stationary Euler no-reopening does not erase the preboundary potential. The
Green identity still has an unrestricted nonzero boundary owner, and no
presymplectic quotient, BFV phase space or charge algebra has been built.

Likewise, a first formal compatibility operator is not a hyperbolicity
theorem. It supplies neither propagation of constraints nor a noncharacteristic
Cauchy surface, closed Krein domain, positive energy, spectrum, mass, or
stability statement. Higher Spencer cohomology and nonlinear formal
integrability remain open.

## Source return

The located sources confirm rich observation beyond naive pullback and the
affine connection/covariant-derivative grammar. They do not state equation
(1) at the selected stationary K77 branch, rank `770`, or the fourteen rows
(3). Those are repository-derived.

```text
SOURCE-CONFIRMS: rich observation; affine Maurer-Cartan/connection grammar
SOURCE-SILENT:   stationary equation-dual no-reopening; first-prolongation
                 rank; divergence-shaped compatibility ownership
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

Next, apply the exact compatibility operator (3) to the **complete**
stationary linearized Euler owner: lower-order residual-square Hessian,
moving `Q_B/H_q`/Shiab/observation coefficients, and the source-derived
affine tangent. Determine whether a nonlinear Bianchi/Noether/BV identity
owns its completion or whether a genuine fourteen-row obstruction remains.
Only after that should higher Spencer involutivity or symplectic reduction be
attempted.

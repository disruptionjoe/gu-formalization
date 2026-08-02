---
title: "Eric/Curt Wave 3D-B2C15R3: same-bundle descent, derived split response, and section-current observation"
status: active_research
doc_type: construction_result
created: 2026-08-02
branch: agent/null-clifford-omega1-repair
run: RUN-20260802-122445-gu-formalization-ecw3d-b2c15r3-direct
registry: lab/process/eric-curt-wave3d-b2c15r3-same-bundle-native-variation-observation-support.json
probe: tests/channel-swings/eric_curt_wave3d_b2c15r3_same_bundle_native_variation_observation_support_probe.py
grade: "PARTIAL CONSTRUCTION PASS WITH ABSTRACT REDUCED DESCENT, STRUCTURAL INDUCED-BUNDLE COMPARATOR, DECLARED-GERM DERIVED-K ACTION RESPONSE, TEN-FIBRE SECTION CURRENT, AND FULL-ORDER2 STOP"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# B2C15R3 same-bundle descent, derived split, and observation support

## Result first

B2C15R3 closes two of B2C15R2's concrete construction gaps and sharpens the
other two.

The covariant correction

\[
K_u=-\Delta\,\operatorname{pr}_2\!
\left[\operatorname{ad}_A\phi(\Delta\operatorname{ad}_A^2)D_BA\right]
\]

obeys an exact abstract reduced-bundle descent theorem. The executable atlas
is an `SL(2) -> Sp(4)` structural comparator, not the active 128-dimensional
Clifford inclusion. Together with the prior G1/R2 actual-equivariance receipts,
it gives a formal conditional corollary for the existing native induced
`Sp(32,32;H)` bundle, but this gate does not newly machine-check that corollary
on overlaps. The public Euclidean/U(128)-style presentation also never
supplies the real-form principal-bundle morphism identifying its literal
source bundle with the active induced one.

The action test now derives its split direction from the finite `B,T` field
values instead of supplying `K` independently. Because the recorded exterior
jet `dT` does not determine the symmetric first jet of `T`, the fixture also
declares a compatible constant-`A` full germ. A nonconstant-`A` held-out germ
with the same `dT` changes `dK`, exposing that debit. For the structural port
`L_fin(T)=T_0`, Cayley--Hamilton sums the full series to

\[
K=f\bar K,\qquad f=\frac{1-\cos\sqrt{21}}7,
\]

and direct substitution into the written first-action grammar gives

\[
I(s)=\frac{378s^2+280s+23}{2},\qquad
I(f)-I(0)=189f^2+140f>0.
\]

Thus the declared-germ derived correction is visible to the source action
while the total connection and exterior curvature jet remain fixed. No
`lambda_red` or new action coefficient is introduced. The finite port is
deliberately not called the native `Alt(T)` map; two held-out ports give
different responses. Native promotion therefore still requires the actual
moving grade-two source projection, `Alt` map, and complete first-jet owner in
the same source bundle.

For observation, the trace-reversed metric fibre has a natural invariant
absolute density, but its radial measure is `d lambda/lambda` and has infinite
mass. It supplies no canonical positive Gaussian, compact cutoff, decay, or
normalization. A normalized delta-current supported on the supplied
observation section does give a precise, properly supported ten-fibre current.
Its inverse Jacobian is checked under a non-unimodular `GL(4)` congruence.
Separately, the Levi-Civita horizontal coefficient lift descends across
patches and has the correct Krein dual. This is selected distributional
observation data, not smooth decay derived from the bulk action, and the
independent no-leakage condition remains necessary.

The effective order-two owner does not close. The actual B2C15P fixture has
nonzero first derivatives in every base direction, so `A1 Z1` and
`2 A2 partial Z1` cannot be erased by calling the fixture normal-coordinate
constant. An exact hostile comparator shows that `A1 Z1` can cancel a live
`A2 Z0` block even when the order-three symbol vanishes. The earlier ranks
`10` and `4` therefore remain a live subroute, not the complete coefficient.

## Plain English

The connection correction has an exact abstract gluing theorem and a finite
induced-bundle control, and a nontrivial declared-germ version really changes
Weinstein's proposed action. The active native overlap port still depends on
the earlier inclusion receipts rather than a new 128-dimensional atlas test.

Two bridges are still missing. First, we need to connect the public source's
bundle and real form to the active `Spin(9,5) -> Sp(32,32;H)` bundle, and put
the actual `Alt(T)` map through that bridge. Second, the observation section
can support an equation as a delta-current, but the bulk action has not
selected that current or proved that the unobserved components vanish. The
external datum cannot solve either problem because P1/P2/P3 has the wrong
type.

## Layer 0

| object | type | status |
| --- | --- | --- |
| `Q` | active reduced `Spin_0(9,5)` bundle | constructed owner |
| `P_nat=Q x_H G_nat` | active native induced `Sp(32,32;H)` bundle | constructed owner |
| public-source `P` | literal source gauge bundle/real form | not identified with `P_nat` |
| source `T` | full adP-valued one-form/distortion | source explicit |
| `pr_h^epsilon T` | moving grade-two source component | required port, unbuilt in literal source bundle |
| `A=Alt(pr_h^epsilon T)` | grade-three reduction owner | native candidate; finite comparator uses declared `L_fin` |
| `K_u` | tensorial reduced connection difference | abstract reduced theorem; structural atlas control; active `P_nat` corollary conditional on prior receipts |
| `delta_s` | normalized distributional current on the observation section | constructed selected observation route |
| physical Euler pushdown | functional adjoint with support and no leakage | unbuilt |

Raw pullback of a thirteen-form, ten-fibre Gysin, a delta-current, the dual of
a coefficient lift, the Krein adjoint of that lift, and a physical Euler
equation are not synonyms.

## Source collision

- `SOURCE-CONFIRMS`: the written first action uses adP-valued `T`, fixed
  `1/2` and `1/3` transgression weights, the trace-reversed fibre pairing,
  and observation-section language.
- `SOURCE-CONFIRMS`: the Shiab object is an upstairs thirteen-form/current
  intended to yield an observed four-dimensional equation.
- `SOURCE-CORRECTS`: ordinary de Rham pullback cannot be that Euler pushdown;
  it vanishes by degree.
- `SOURCE-CORRECTS`: the contorsion slot uses the gauge-rotated Levi-Civita
  reference, so a frozen projector/reference is not the Eric-lane object.
- `SOURCE-SILENT`: the active real-form bundle morphism, moving grade-two
  source projection, `Alt` port, `K_u`, split substitution, observation
  current, support law, no-leakage theorem, BV quotient, and domain.

## Same-bundle theorem

Let `Q -> Y` be the active native `Spin_0(9,5)` reduction, with local
transition functions `h_ij`. If

\[
B_j=\operatorname{Ad}_{h_{ij}^{-1}}B_i+h_{ij}^{-1}dh_{ij},
\qquad A_j=\operatorname{Ad}_{h_{ij}^{-1}}A_i,
\]

then `D_B A`, every odd adjoint power, the entire function `phi`, and
`pr_2` are reduced intertwiners. Consequently

\[
K_j=\operatorname{Ad}_{h_{ij}^{-1}}K_i,
\qquad
(B+K)_j=\operatorname{Ad}_{h_{ij}^{-1}}(B+K)_i+h_{ij}^{-1}dh_{ij}.
\]

The executable three-patch nonconstant-overlap fixture verifies this algebra
in an `SL(2) -> Sp(4)` structural model: cocycle, tensorial `K`, affine `B+K`,
failure of raw `dA`, bracket preservation, and the absence of an arbitrary
inclusion scale all pass. The formal active-native corollary additionally uses
the prior G1 construction of `P_nat`, R2's all-91 reduced equivariance, and the
previous right-H/Krein inclusion receipts; they are not replayed as an actual
128-dimensional three-patch atlas here.

The structural comparator also shows why a fixed reduced projector cannot be
promoted to full ambient covariance and why a conjugated moving projector is
required. It is not an actual grade-three/Sp transition test. Literal-source
descent is conditional on a supplied reduction/bundle isomorphism, not
declared absent on every possible bundle component.

## Actual derived split response

The finite G2 comparator reuses B2C15R2's exact `B,T,dB,dT`, adds an explicit
compatible full first jet with `dA=0`, and replaces its independently chosen
split by

\[
A=L_{\rm fin}(T)=T_0,
\quad \bar K_i=-[A,[B_i,A]],
\quad d\bar K_{ij}=-[A,[dB_{ij},A]].
\]

Its discriminant is `-7`, so the entire bridge with `Delta=3` gives the
displayed `f`. Five exact rational evaluations recover the action polynomial,
the full-series response is approximately `27.5093637771`, and differentiating
with respect to `Delta` exactly equals the explicit `K` chain rule. A second
full first jet with identical exterior `dT` but nonzero `dA` produces a
different `dK`, proving that the selected constant-`A` germ is an explicit
fixture choice rather than a consequence of `dT`. Common conjugation
covariance passes. Omitting `dK`, using raw `dA`, recomputing `K` from shifted
`T-K` as an implicit fixed point, or calling `L_fin` native would change the
problem and is rejected.

At the full native level the first variation must retain

\[
\delta I_{\rm split}
=\langle E_B,\beta\rangle+\langle E_T,\tau\rangle
+\langle E_B-E_T,DK[\beta,\tau,\ldots]\rangle
+C_{\rm Shiab}+C_\rho+C_{\rm Krein}+C_{\rm lowerer},
\]

plus the Green boundary from the first-order `Alt/K` owner. Fixed-`varpi`
source coordinates and fixed-total-connection variations have different
chains. This gate types that return but does not claim the literal-source
native coefficient has been assembled.

## Observation support

For the Lorentz metric fibre, under `h -> lambda h`, the ten-dimensional
Lebesgue Jacobian contributes `lambda^10` while
`|det h|^{-5/2}` contributes `lambda^-10`. More generally, for the
non-unimodular control `A=diag(2,1,1,1)`, the `Sym2` Jacobian is
`det(A)^-5=1/32` and the determinant-density factor is `32`, so they cancel.
The resulting invariant density is non-normalizable. The indefinite `(6,4)`
DeWitt metric does not provide a canonical positive distance cutoff.

The selected alternative is

\[
\mathcal O_s(E)=\pi_!(\delta_s E),\qquad \pi_!\delta_s=1.
\]

The delta current uses all ten metric-fibre coordinates. Its density transforms
by the inverse `Sym2` Jacobian, so `pi_! delta_s=1` survives the non-unimodular
overlap; leaving it untransformed fails. Separately, on an exact three-patch
`4+9` trace-complement coefficient fixture, the LC-horizontal lift, its Krein
left inverse, and equation-covector dual descend. The ten support directions
and nine hidden coefficient directions are not identified. `R L=1` still does
not imply no leakage: an explicit hidden covector has zero observed value and
nonzero complementary projection, and an explicit vertical lift perturbation
preserves `R L=1` while breaking overlap descent.

This route selects the four horizontal legs already eligible for fibre
integration. The other nine require a geometric vertical soldering block;
they may not be chosen by fitting the desired equation. A functional Euler
equation additionally requires the transverse current and Green/domain data,
not merely the coefficient transpose.

## Trace-reversed versus positive fork

The Cech algebra works on either signature fork. The source-action and support
conclusions here are native trace-reversed conclusions. On the native fibre,
the invariant density is non-normalizable and no positive Gaussian is
canonical. A positive/block-product comparator may choose a Gaussian, but
that adds rival geometry and does not repair the native construction. No kill
is transferred from one fork to the other.

## External datum and surplus

P1/P2/P3 is unchanged and unused. P1/P2 is an orientation line over a
configuration loop, not the source-bundle morphism, moving projector,
observation current, support normalization, or no-leakage projector. P3 is a
real-KO/count twist, not a gauge or observation map.

There is no new `lambda_red`. The linear bridge still exposes only the one
effective continuous combination `Delta=c3^2-c11^2`; the source `1/2` and
`1/3` weights are fixed. Physical constraint surplus remains `UNCOMPUTED`
until the native source port and at least one descended, no-leakage observed
equation exist. Counts must then use the response Jacobian rank, not the
number of written rows.

## Boundary and next gate

This gate does not construct the literal source-to-native real-form bundle
morphism, the actual native `Alt(pr_h^epsilon T)` port, the complete source
first variation, the complete effective order-two coefficient, smooth
dynamical decay, a physical Euler pushdown, BV closure, an analytic domain,
or an SM/GR equation. It makes no vacuum, mass, anomaly, generation-count,
cosmological, or quantum claim.

The next gate is
`ECW3D-B2C15R4-NATIVE-ALT-SOURCE-BUNDLE-PORT-AND-FULL-EFFECTIVE-ORDER2-ASSEMBLY`:

1. construct or obstruct the literal-source `P -> P_nat` real-form/reduction
   morphism componentwise;
2. build `pr_h^epsilon T` and native `Alt(T)` on that same bundle and rerun
   the exact derived split/action/Ward/Green calculation;
3. assemble `A2(2 partial Z1+Z0)+A1 Z1` and every moving coefficient at the
   actual Zorro--DeWitt background;
4. only if that coefficient survives, pair it with the normalized section
   current and prove functional-adjoint descent plus zero leakage.

Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`; `TG-1 AND TG-2 AND TG-3`
remains `NOT_PROMOTED`.

Validation: `46` exact checks, `5` primary-source receipts, `24` type-level
guards, and `17` live planted rejections pass (`92/92`). Three independent
hostile specialist re-reviews pass after repairing the active-native scope,
the missing full first-jet debit, and the ten-fibre delta-current Jacobian.

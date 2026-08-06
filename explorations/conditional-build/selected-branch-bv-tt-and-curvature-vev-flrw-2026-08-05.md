---
artifact_type: construction_result
created: 2026-08-05
status: METRIC_SOLDERING_MOD_GAUGE_EXACT__MASSIVE_TT_PARTNER_SURVIVES_EVEN_BV__FINITE_TREE_KREIN_MAJORANT_POSITIVE__LOCAL_CURVATURE_VEV_TRACKING_EXACT_AND_SCREENING_FAILS
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR2e, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_branch_bv_tt_curvature_vev_flrw_probe.py
  - tests/channel-swings/selected_branch_bv_tt_curvature_vev_flrw_independent.sage
registry: lab/process/selected-branch-bv-tt-curvature-vev-flrw.json
---

# Selected-branch BV TT survival and curvature/VEV FLRW horn

## Result first

This wave closes two of the prior gate's most useful finite questions without
spending external datum.

First, the source-named gauge-rotated Levi-Civita reference gives an exact
metric-to-connection derivative. Modulo the moving-reduction gauge
compensator,

\[
 D_g B[h]^\rho{}_{\mu\nu}
 =\operatorname{Ad}_{\epsilon^{-1}}\!\left[
 {1\over2}g^{\rho\sigma}
 (\nabla_\mu h_{\nu\sigma}+\nabla_\nu h_{\mu\sigma}
 -\nabla_\sigma h_{\mu\nu})\right].
\]

Its flat symbol has rank ten on timelike, spacelike and null covector orbits.
A moving `epsilon` changes it by `D_B chi`, which is zero in the connection-
gauge quotient. This constructs the physical soldering derivative required by
the one-action chain at linearized defect grade. It is not a full nonlinear
ambient-`Y14` connection theorem.

Second, the opposite-residue massive partner is **not** removed by ordinary
diffeomorphism BV. Plus and cross span a rank-two TT carrier with trivial
intersection with the rank-four diffeomorphism image. The massive eigenvector
therefore supplies at least two non-exact even-BV classes. The full massive
multiplet and odd super-IG complex remain open.

The surviving partner is nevertheless not an automatic failure. For the
exact two-field TT system, the spectral involution

\[
 P=I+{2L\over m^2}
\]

squares to one, commutes with the dynamics, is Krein self-adjoint and gives a
positive finite TT majorant `K P` when the Einstein residue `alpha_II` is
positive. This is an exact tree-level keep-and-grade result. It does not prove
uniform boundedness over the UV tower, interaction stability, type-III
positivity or loop unitarity.

Third, the scalar irrep of the same action has an exact local curvature/VEV
horn:

\[
 I_{\rm sc}=\int\sqrt{-g}\left[(a+\beta t)R
 +{\kappa\over2}t^2-\rho_{\rm vac}\right].
\]

No new potential or fitted gain was added: `a` is the existing Einstein
coefficient, `beta` the fixed curvature/distortion normalization and `kappa`
the selected distortion gain. At constant curvature its two variations give

\[
 R={2\rho_{\rm vac}\over a},\qquad
 t=-{2\beta\rho_{\rm vac}\over a\kappa}.
\]

One input amplitude controls both field values. That earns Weinstein's stated
**two problems to one** bar on this local horn. But
`dR/d rho_vac=2/a`, so it does not screen an independent vacuum shift or
derive why the remaining amplitude is small.

## Layer 0

| phrase | object used | not identified with |
| --- | --- | --- |
| metric soldering | derivative of gauge-rotated Levi-Civita at fixed independent distortion, modulo `D_B chi` | naked Levi-Civita matrix or full nonlinear ambient connection |
| BV survival | nonzero TT class modulo the even diffeomorphism image | full odd super-IG cohomology |
| positive majorant | finite spectral fundamental symmetry of the distinct two-pole TT block | uniform UV/type-III metric or loop unitarity |
| curvature field | scalar irrep `R` of the constructed local action horn | spatial three-curvature `k/a^2` or every Shiab/Einstein component |
| tracking | one source amplitude controls `R` and `t` | radiative screening or first-principles magnitude selection |

Spatial flatness is especially important. In FLRW,

\[
 R=6\left(\dot H+2H^2+{k\over a_{\rm FLRW}^2}\right).
\]

Setting spatial `k=0` does not set `R=0`; flat-slicing de Sitter has
`R=12H^2`. The source's spatial-flatness wording therefore does not identify
the curvature variable used here.

## Exact soldering calculation

Let `B(g,epsilon)` be the gauge transform of the Levi-Civita connection and
let `A=B+T`, with `T` independently varied. For a moving reduction,

\[
 \delta B
 =\operatorname{Ad}_{\epsilon^{-1}}(D_g\Gamma^{LC}[h])
 +D_B\chi,\qquad \chi=\epsilon^{-1}\delta\epsilon.
\]

Thus on the connection-gauge quotient,

\[
 [D_gA[h]]=[\operatorname{Ad}_{\epsilon^{-1}}D_g\Gamma^{LC}[h]].
\]

The exact rational probe builds the full `64 x 10` flat symbol and finds rank
ten on all three nonzero Lorentz covector types. Gauge conjugation preserves
rank. Appending a compensator `D_B chi` leaves the quotient class unchanged.

The one-action current/stress relation can therefore be instantiated at this
grade:

\[
 T_{\rm reduced}
 =E_g^{\rm direct}+(D_gB)^!J_A
\]

modulo connection gauge and at fixed independent `T`. This does not say that
`J_A` alone is stress, and it does not construct every vertical or nonlinear
piece of the chimeric connection.

## Even-BV TT theorem

For a null wave covector along the third spatial direction, the linearized
diffeomorphism map is

\[
 \xi_\mu\longmapsto h_{\mu\nu}=k_\mu\xi_\nu+k_\nu\xi_\mu.
\]

Its image has rank four. The usual plus/cross tensors have only `11`, `22`
and `12` components and span a rank-two complement with zero intersection
with that image. The predecessor already established the massless
`10 -> 6 -> 2` quotient. Here the same TT carrier is tensored with the
massive eigenvector of the exact coupled metric/distortion block. Therefore:

\[
 \dim H^0_{\rm even,BV}(\text{massive TT})\ge 2.
\]

This lower bound is decisive against “the partner is ordinary-diffeomorphism
exact.” It does not count helicity zero or one, nor decide an odd super-IG
differential not yet constructed.

## Canonical finite Krein grading

On each TT polarization the kinetic and lower-order matrices are

\[
 K=\begin{pmatrix}\alpha&1\\1&0\end{pmatrix},\qquad
 M=\begin{pmatrix}0&0\\0&b\end{pmatrix},\qquad
 L=K^{-1}M,
\]

where `b=124*kappa_1/117` and `m^2=alpha*b`. The massless and massive
eigenvectors may be taken as

\[
 u_0=(1,0),\qquad u_m=(1,-\alpha),
\]

with Krein norms `+alpha` and `-alpha`. For nonzero distinct real poles,

\[
 P=I+{2L\over m^2}
 =\begin{pmatrix}1&2/\alpha\\0&-1\end{pmatrix}.
\]

Exact identities:

- `P^2=I`;
- `[P,L]=0`;
- `P^T K=K P`; and
- `K P=[[alpha,1],[1,2/alpha]]`, whose leading minor is positive and whose
  determinant is one for `alpha>0`.

The result is precisely the program-native keep-and-grade answer at finite
free-field TT grade. At the coincident-pole locus `m^2=0`, `P` is undefined;
across an interacting UV tower its boundedness and inverse-boundedness are
separate global questions already identified elsewhere in the repository.

## Curvature/VEV variation and FLRW trace

The scalar action is the minimal scalar-irrep reduction of the already-owned
linear `T`-curvature term plus quadratic `T` gain and induced Einstein term.
Its distortion equation is

\[
 E_t=\beta R+\kappa t=0.
\]

The metric equation is

\[
 (a+\beta t)G_{\mu\nu}
 +(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu)(\beta t)
 -{1\over2}g_{\mu\nu}\left({\kappa\over2}t^2-\rho_{\rm vac}\right)=0.
\]

Its trace, followed by `t=-beta R/kappa`, gives

\[
 aR+{3\beta^2\over\kappa}\Box R=2\rho_{\rm vac}. \tag{1}
\]

Equation (1) is the action-owned homogeneous/FLRW response of this local horn.
For a constant source and constant-curvature attractor it reduces to the
solution quoted above. The count is exact:

| question | result |
| --- | --- |
| independent field values before equations | `R,t` |
| independent variations | 2 when `a*kappa != 0` |
| independent unexplained value inputs | one, `rho_vac` |
| fitted construction coefficients | 0 |
| curvature shift susceptibility | `2/a`, nonzero |
| distortion shift susceptibility | `-2 beta/(a kappa)`, nonzero |

So the dark field value is no longer independent of curvature. But the local
static horn lies inside the ordinary Weinberg-class burden and does not
self-adjust against radiative shifts. An ambient/global/nonlocal GU equation
could be a different horn; this calculation neither builds nor kills it.

## Seven-axis audit

| layer | disposition |
| --- | --- |
| Layer 0 | all five homonym pairs above separated |
| L1 source | `SOURCE-CONFIRMS` limited architecture and two-to-one bar; exact maps remain repo-derived |
| L2 algebra | LC symbol ranks, TT intersection, parity identities and scalar Jacobian exact |
| L3 geometry | gauge-rotated LC derivative closes modulo gauge; ambient nonlinear connection open |
| L4 variation | both scalar equations derived from one action horn |
| L5 covariance/BV | massive TT survives even diffeo BV; odd super-IG open |
| L6 analytic | existing common defect Green domain retained; UV/type-III majorant open |
| L7 physics | finite tree keep-and-grade and local tracking exact; loop stability, screening and `w(z)` open |

## Constraint surplus and ledger movement

No new field, potential, gain, projector, boundary selector or external datum
was added. `rho_vac` appears only as the hostile independent source. Eight
ledger-row distances move, while coverage, verdict counts, continuous and
function-valued residue and the nine open forks stay fixed.

The important adverse result is not a global GU kill: the **local scalar
action horn** fails radiative screening. The source's limited two-to-one claim
passes there. The ambient/global/nonlocal horn remains open and now has a
sharper burden: it must change the nonzero `dR/d rho_vac` result without
retuning `a`, `beta`, `kappa`, boundary data or initial conditions.

## Next gate

1. Construct the full odd super-IG interacting cohomology and test whether the
   finite spectral majorant remains uniformly bounded over the UV tower.
2. In parallel, construct the genuinely ambient/global/nonlocal curvature/VEV
   horn and test an independent vacuum shift.
3. Only if that cosmological horn survives, derive action-owned FLRW
   perturbations and held-out `w(z)` predictions.

P1/P2/P3 remain unused. Curt remains formally separate. No third lane, canon,
Lane-count or public-posture change is made.

## Reproduction

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_branch_bv_tt_curvature_vev_flrw_probe.py
DOT_SAGE=/private/tmp/gu-bv-tt-flrw-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/selected_branch_bv_tt_curvature_vev_flrw_independent.sage
```

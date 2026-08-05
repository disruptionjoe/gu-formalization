---
artifact_type: construction_result
created: 2026-08-05
status: K77_RANK10_GRAVITATIONAL_RECEIVER_AND_SAME_STRATUM_ORTHOGONAL_WELD_EXACT__GLOBAL_FULL_EPSILON_REDUCTION_BULK_DEFECT_NORMALIZATION_NONLINEAR_BV_AND_DOMAIN_OPEN
lane: "1"
functional_channels: [BUILD, SOURCE, COMPOSE, VERIFY]
ledger_rows: [LT-GR1b, LT-GR2c, LT-GR2d, LT-SM8]
fork_assumed: SIGNATURE_AMBIENT_K77__FULL_CLIFFORD_SOLDERING_REDUCTION_CONDITIONAL
search_space_dim: "rank-ten canonical composite after full epsilon_IG is supplied; related Lorentz-equivariant Sym2 bilinear receiver grammar has at least five independent maps, so equivariance alone is not uniqueness"
free_object_delta: "zero new fields and zero receiver coefficients; global full epsilon_IG reduction remains unconstructed; bulk/defect placement retains one support/relative-normalization owner"
source_return: SOURCE-SILENT
scripts:
  - tests/channel-swings/k77_epsilon_gravitational_soldering_weld_probe.py
  - tests/channel-swings/k77_epsilon_gravitational_soldering_weld_independent.sage
registry: lab/process/k77-epsilon-gravitational-soldering-weld.json
---

# K77 epsilon gravitational soldering receiver and action weld

## Result first

The missing ten-dimensional gravitational receiver has an explicit canonical
formula—conditional on `epsilon_IG` being a **full Clifford soldering
reduction**, not merely a moving Clifford plane:

\[
 \boxed{\;
 \sigma_\epsilon(v_T)
 =\operatorname{pr}_V\pi_1^\epsilon\bigl(v_T(q)\bigr),
 \qquad q=\frac{g}{2},\quad \lVert q\rVert_{DW}^2=-1 .
 \;} \tag{1}
\]

Here `v_T` is a vertical covector with adjoint coefficient. It first acts on
the canonical trace vector `q`; the moving grade-one Clifford projector then
returns a chimeric vector; the already-typed split
`C=V plus H-star` retains its ten-dimensional vertical part.

This corrects one sentence in the predecessor. `q` itself is one line, but an
arbitrary endomorphism acting on a nonzero `q` has a ten-dimensional image.
The exact receiver has rank ten. No new field, bit, vector or fitted receiver
coefficient is needed.

The construction also supplies an adjoint right inverse and an orthogonal
rank-ten gravitational projector. The load-bearing sign is Krein: every real
K77 grade-one Clifford generator is `B`-skew, so the coefficient pairing is
the **negative** of the chimeric metric. That minus sign cancels the negative
DeWitt norm of `q`. Consequently the insertion is an isometry, not an
anti-isometry.

This is enough to split a same-stratum action exactly and replace its
gravitational receiver without appending a second Einstein term. It is not
enough to identify a fourteen-dimensional bulk density with a
four-dimensional defect density. The complete bulk/defect action still needs
an explicit support architecture and relative normal-density/normalization
owner. Nonlinear BV/CME, the null/Green domain and physical cosmology also
remain open.

## 1. Layer 0

| name | object used here | not identified with |
| --- | --- | --- |
| source `epsilon` | gauge transformation in the translated-connection construction | `epsilon_IG` |
| coarse Clifford orbit | a moving fourteen-plane in the adjoint carrier | a full frame/soldering isometry |
| full `epsilon_IG` | an isometry `gamma_epsilon:C -> ad(P)` intertwining the already split chimeric bundle | an unframed plane or a source quote |
| `q=g/2` | canonical unit DeWitt-negative vertical trace vector | a free external datum or the whole receiver |
| `v_T` | element of `V-star tensor ad(P)`, hence a map from `V` to the adjoint | an ordinary symmetric tensor |
| `pi_1^epsilon` | moving projection from the adjoint to the epsilon-defined Clifford grade-one carrier | the Shiab |
| `sigma_epsilon` | the composite in (1) | the K95 IC1 injection in the opposite direction |
| same-stratum weld | orthogonal coefficient-sector replacement | a bulk/defect support identification |
| finite Ward control | naturality under one exact stabilizer action | nonlinear BV/CME or a Green domain |

The June IC1 file is useful archaeology, not the answer. It constructs an
injection `N_s -> ad(P_s)` in the rival `Cl(9,5)=M64(H)` / compact-`Sp(64)`
fork, leaves frame independence and quaternionic-`J` issues open, and points
in the opposite direction from (1). Importing it would violate the settled
real-Clifford fork.

## 2. Pre-assessment lenses

| lens | preregistered danger | outcome |
| --- | --- | --- |
| differential geometry | a coarse homogeneous orbit may be mistaken for a soldering frame | only a full reduction makes (1) global |
| Clifford representation | an adjoint coefficient may be flattened without a grade test | exact `Cl(7,7)` trace projection recovers grade one and kills a bivector |
| Krein geometry | the negative `q` line may flip the gain sign | the `B`-skew coefficient sign cancels it |
| representation theory | equivariance may be advertised as uniqueness | five independent Lorentz-equivariant `Sym2 x Sym2 -> Sym2` maps survive |
| variational bicomplex | a new term may simply be added to the old one | orthogonal split gives a literal sector replacement identity |
| stratified action engineering | same-stratum algebra may be promoted to a bulk/defect weld | normal-density and relative normalization remain open |
| Ward/BV | one finite cancellation may be called a master equation | only naturality and a primitive owner ledger are claimed |
| source archaeology | source `epsilon` may be relabelled as `epsilon_IG` | primary sources do not construct that identity |
| epistemic breadth | exact work may defend a superseded K95 arrow | K95 IC1 is retained only as a negative control |

## 3. Bundle construction

Let

\[
 C_y=V_y\oplus H_y^*,\qquad
 G_C=G_{DW}\oplus g^{-1},
\]

with signatures `(6,4)` and `(1,3)`, hence `(7,7)`. A full soldering
reduction is a fibrewise Clifford isometry

\[
 \gamma_\epsilon:C_y\longrightarrow\operatorname{ad}(P_y)
\]

onto the moving real grade-one subspace. With the `B`-adjoint coefficient
pairing `beta`, define `pi_1^epsilon` intrinsically by

\[
 G_C\bigl(\pi_1^\epsilon(A),c\bigr)
 =-\beta\bigl(\gamma_\epsilon(c),A\bigr). \tag{2}
\]

In the faithful 128-dimensional real representation this is the familiar
trace formula

\[
 \pi_1^\epsilon(A)^a
 =\eta^{aa}\frac{\operatorname{tr}(\gamma_a^\epsilon A)}{128}.
\]

It recovers every grade-one coordinate and kills an exact bivector control.
If the coefficient and epsilon-frame co-transform by Spin conjugation, the
coordinates are unchanged; freezing epsilon makes the planted control fail.

The tautological metric-bundle vector `q=g/2` is global on the Lorentz-metric
component and has `G_DW(q,q)=-1`. Equation (1) is therefore global whenever
the full reduction is global. Gauge naturality follows from

\[
 \gamma_{a\epsilon}=\operatorname{Ad}_a\gamma_\epsilon,
 \qquad
 \pi_1^{a\epsilon}(\operatorname{Ad}_a A)=\pi_1^\epsilon(A).
\]

An unframed plane does not supply the inverse coordinate projector or prove
that the vertical/horizontal split is intertwined. That is the exact global
existence burden left on `epsilon_IG`.

## 4. Right inverse and orthogonal projector

Define

\[
 \iota_\epsilon(u)
 =\frac{q^\flat}{G_{DW}(q,q)}\otimes\gamma_\epsilon(u),
 \qquad u\in V. \tag{3}
\]

Then

\[
 \sigma_\epsilon\iota_\epsilon=1_V,
 \qquad
 P_{\rm grav}=\iota_\epsilon\sigma_\epsilon,
 \qquad
 P_{\rm grav}^2=P_{\rm grav}.
\]

On the grade-one carrier `V-star tensor C`, the exact dimensions are

| object | rank |
| --- | ---: |
| domain | 140 |
| `sigma_epsilon` | 10 |
| `P_grav` | 10 |
| `Q=1-P_grav` | 130 |

The relevant domain pairing is

\[
 H_D=G_{DW}^{-1}\otimes(-G_C). \tag{4}
\]

The minus is forced by `gamma_a^times=-gamma_a`. Since `q^2=-1`, exact
calculation gives

\[
 \iota_\epsilon^*H_D=G_{DW}\sigma_\epsilon,
 \qquad
 \iota_\epsilon^*H_D\iota_\epsilon=G_{DW},
 \qquad
 P_{\rm grav}^*H_D=H_DP_{\rm grav}. \tag{5}
\]

Dropping the Krein sign makes (3) an anti-isometry. This is the planted
control and repeats the earlier lesson that the indefinite pairing is active
mathematics, not bookkeeping.

## 5. Equivariance is not uniqueness

The receiver (1) is canonical **after** the full reduction, the split, the
grade-one projection and `q` are named. It is not selected by equivariance
alone.

As a lower-bound control, the exact Lorentz representation
`Sym2 = 1 plus Sym2_0` admits five independent equivariant bilinear maps
`Sym2 x Sym2 -> Sym2`:

1. `tr(h) tr(k) g`;
2. `<h0,k0> g`;
3. `tr(h) k0`;
4. `tr(k) h0`;
5. the traceless Jordan product of `h0` and `k0`.

Their structure tensors have exact rank five and all pass a held-out rational
Lorentz boost. Thus no result here says “equivariance uniquely forces the
receiver.” The information comes from the surplus geometric inputs already
present in the K77 metric-bundle construction.

## 6. Exact same-stratum weld

After the Hodge/Krein Riesz conversion needed to put the old curvature row in
the same coefficient carrier, write it as `R_old`. Let
`E_G=G4(res_H P_R barF+Q(II_s))`. On any common stratum define

\[
\begin{aligned}
 L_{\rm split}
 ={}&\langle QT,Q R_{\rm old}\rangle_D
 +\langle\sigma T,E_G\rangle_{DW}\\
 &+\frac{\kappa_1}{2}
 \left(\langle QT,QT\rangle_D
 +\langle\sigma T,\sigma T\rangle_{DW}\right). \tag{6}
\end{aligned}
\]

Orthogonality proves two identities before any equation of motion:

\[
 \langle T,R_{\rm old}\rangle_D
 =\langle QT,QR_{\rm old}\rangle_D
 +\langle\sigma T,\sigma R_{\rm old}\rangle_{DW}, \tag{7}
\]

\[
 \langle T,T\rangle_D
 =\langle QT,QT\rangle_D
 +\langle\sigma T,\sigma T\rangle_{DW}. \tag{8}
\]

Therefore (6) exactly reconstructs the old term when
`E_G=sigma(R_old)`. With the faithful pre-Shiab receiver it differs by exactly

\[
 \langle\sigma T,E_G-\sigma R_{\rm old}\rangle_{DW}. \tag{9}
\]

That is a genuine one-sector replacement. Appending the new receiver to the
unsplit old action fails a planted double-counting control.

## 7. Why the full bulk/defect weld is still open

Equations (6)--(9) assume a common integration stratum. The standing
source-guided architecture instead distinguishes

\[
 S_Y^{ED}+S_Y^{YMH}+S_X^{\rm independent}.
\]

The four-dimensional pre-Shiab term can be placed in the independent defect
sector, or the gravitational projector sector can be removed from the bulk
and replaced on the defect, or an ambient distribution `delta_s L_X` can be
used. Those choices have different equations and relative normalization.

The projector supplies none of the following:

- the inverse normal-density line carried by the codimension-ten section
  current;
- a transverse profile for a localized bulk replacement;
- the relative coefficient between a 14D bulk action and an independent 4D
  density; or
- a proof that the two strata share one closed variational/Green domain.

Accordingly this wave retracts any reading of the prior “unit replacement
horn” as a completed bulk/defect normalization. The exact advance is the
receiver and same-stratum split. The support/normalization choice remains an
explicit action-architecture owner.

## 8. First-variation owner ledger

For `Q=1-P`, the unreduced first variation of (6) contains

\[
\begin{aligned}
 \delta L_{\rm split}={}&
 \langle Q\delta T-(\delta P)T,QR\rangle_D
 +\langle QT,Q\delta R-(\delta P)R\rangle_D\\
 &+\langle(\delta\sigma)T+\sigma\delta T,E_G\rangle_{DW}
 +\langle\sigma T,\delta E_G\rangle_{DW}\\
 &+\kappa_1\langle Q\delta T-(\delta P)T,QT\rangle_D
 +\kappa_1\langle(\delta\sigma)T+\sigma\delta T,\sigma T\rangle_{DW}\\
 &+\delta(H_D,G_{DW},*,\mu,s)\text{ terms}. \tag{10}
\end{aligned}
\]

This exposes the owners that a nonlinear Ward/BV construction must retain:

| owner | required derivative |
| --- | --- |
| full soldering | `D_epsilon pi1`, `D_epsilon sigma`, `D_epsilon P` |
| metric fibre | `D_g q`, `D_g G_DW`, vertical split and density |
| observation | `D_s res_H`, Gauss/second-fundamental-form and section-current terms |
| connection | `D_A barF`, Hodge/Krein Riesz and augmented-torsion terms |
| boundary/domain | Green formula, conormal trace and preboundary polarization |

An exact stabilizer generator verifies
`sigma(delta X)=delta sigma(X)`, projector naturality and cancellation of the
paired scalar Ward variation. This is a useful formal nonlinear owner check,
not a complete ghost differential or classical master equation.

## 9. Source return

**Decisive return: `SOURCE-SILENT`.**

The source corpus explicitly supplies the 10+4 chimeric split, trace-reversed
`(6,4)` fibre, gauge-transformed connection difference, augmented torsion and
source `epsilon` as a gauge transformation. It does not print (1), (3), (6),
the moving grade-one projection, or an identity between source `epsilon` and
the repo's full `epsilon_IG` reduction.

This is not an argument from silence against the construction. It fixes
provenance: (1)--(10) are repo-native conditional mathematics.

## 10. Constraint and residue accounting

| quantity | result |
| --- | ---: |
| new fields/data | 0 |
| receiver rank | 10 |
| receiver coefficients fitted | 0 |
| related equivariant-map lower bound | 5 independent maps |
| exact same-stratum projector quotients | rank 10 + rank 130 complement |
| global full `epsilon_IG` reductions constructed | 0 |
| bulk/defect normalizations selected | 0 |
| nonlinear/global BV quotients ranked | 0 |
| P1/P2/P3 | unchanged and unused |
| Lane count / canon / public posture | unchanged |
| Curt track | formally separate; not promoted into the Eric construction |
| `TG-1 AND TG-2 AND TG-3` | unchanged and not promoted |

The formerly arbitrary `sigma_epsilon` construction slot is reduced to the
already-open existence/topology of a full soldering reduction. The action
residue is not zero: support architecture and relative normalization remain,
followed by nonlinear BV and the null/Green domain.

## 11. Seven-axis audit

| layer | disposition |
| --- | --- |
| Layer 0 | six epsilon/plane/frame/receiver/support objects separated |
| L1 source | `SOURCE-SILENT` at receiver/weld; source ingredients only |
| L2 algebra | faithful K77 grade projection, rank ten, adjoint right inverse, orthogonal projector and five-map lower bound exact |
| L3 geometry | global formula conditional on a full soldering reduction; reduction existence/topology open |
| L4 variation | same-stratum action identity and complete primitive derivative owner ledger written |
| L5 covariance | moving-frame and finite stabilizer Ward controls exact; nonlinear BV/CME open |
| L6 analytic | bulk/defect normalization, null/Green and closed common domain open |
| L7 physics | no vacuum, FLRW, screening, positivity or Standard Model recovery claim |

## 12. Hostile disposition and next gate

The hostile pass accepts the receiver and same-stratum weld after refusing
three promotions: old K95 injection to current K77 receiver, one-line `q` to
one-dimensional image, and orthogonal algebra to cross-dimensional action
normalization.

Next gate:

```text
CONSTRUCT_GLOBAL_FULL_EPSILON_IG_REDUCTION_OR_OBSTRUCTION_AND_TYPED_BULK_DEFECT_SUPPORT_NORMALIZATION__THEN_ASSEMBLE_NONLINEAR_EVEN_BV_AND_NULL_GREEN_DOMAIN
```

The efficient order is global reduction topology first, then choose one of
the already-enumerated support architectures and rank its relative
normalization, then assemble (10) into the actual nonlinear tangent/Noether
complex. A failure must name whether it is the reduction, support line,
normalization, BV closure or domain. It may not return to “no source
action/external datum.”

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/k77_epsilon_gravitational_soldering_weld_probe.py
DOT_SAGE=/private/tmp/gu-k77-epsilon-weld-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/k77_epsilon_gravitational_soldering_weld_independent.sage
```

Main receipt: `2 source + 7 repo + 26 exact + 14 type + 11 planted =
60/60`. Independent Sage/QQ reconstruction passes.

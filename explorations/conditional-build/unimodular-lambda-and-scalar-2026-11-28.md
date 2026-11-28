---
title: Volume restriction frees a curvature datum but retains the quadratic scalar mode
status: exploration
doc_type: structural-result
created: '2026-11-28'
program_target: LB-CLASS
tier: T1
expected_delta: Decide the source-to-unimodular bridge and whether volume-restricted metric equations can stabilize the owned quadratic reduction
actual_delta: Source bridge remains unbuilt; tracefree equations free one constant but retain a growing determinant-tangent full-row scalar mode at every de Sitter curvature, including the critical sector
class_covered: Four-dimensional constant-coefficient local real quadratic metric equations with A/(6b) negative, b nonzero, ordinary local perturbations, and pointwise fixed-volume variation; owned leading positive-reference wedge subclass
premises:
- Source action domain and variation distinguished from the repository fixed-volume normal seed theorem
- Owned leading K95 wedge reduction, covariantly moving finite reference and constant moments; no finite unregulated native integral
- Complete metric variation and its diffeomorphism identity, or separately named conservation defect
- Lorentz signature minus-plus-plus-plus, compact interior variations, ordinary real local metric solution germs
source_bridge:
  status: conditional
  reason: Source supplies geometry and action grammar, but selects neither this reduction, volume-restricted metric variations nor its physical state domain
kill_condition: A valid determinant-tangent full-row growing scalar excludes unimodularity alone as a stability repair in this class; a failed row, variation or domain match defeats only that inference
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: scoped class evidence only; no source or ledger verdict change
---

# What volume restriction does and does not buy

program_target: LB-CLASS
tier: T1
expected_delta: Test the actual variation, conservation and scalar-mode gates.
actual_delta: A free integration datum is compatible with the modified law, but does not cure the ordinary local scalar instability.

**ESTABLISHED:** In the declared quadratic metric class, changing from unrestricted to pointwise volume-preserving variations admits an integration constant when the complete Euler tensor is conserved. It changes the background curvature but leaves the scalar mass unchanged. An explicit perturbation tangent to an exactly fixed-volume metric path solves every linearized metric row and has growing nonzero curvature at every expanding de Sitter background, including the exceptional zero-effective-Einstein-coefficient background.

**RULED OUT:** Removing that mode merely by imposing the volume constraint and choosing the integration constant, while retaining this local real metric state class and coefficients. This is a class-level statement about a possible GU* modification, not a SOURCE GU falsification.

**NOT MODELED / UNDETERMINED:** Source-selected unimodular dynamics, the native physical quotient/domain, finite native reduction, full fourteen-dimensional or higher-order stability, or an observed cosmological-constant prediction. No modification is adopted here. The historical candidate grouping remains 10 choices / 4 obligations / net6 / 0 source-selected predictions; it is not a parameter count for all GU.

```gu-typed-objects
result: volume-restricted metric equation and scalar compatibility test
carrier: observed Lorentz metric X4 in a declared leading K95 reduction LAYER=observed CHIRALITY=N/A
pairing: native K95 contractions upstream; ordinary real metric perturbations downstream ON=bosonic_metric
real_structure: real Lorentz minus-plus-plus-plus; K77 and quantum PT domains not transferred
grading: derivative order; no fermionic or physical chirality grading inferred
action_owner: repository-construction -- owned wedge reduction and a conditional changed variation class
target: metric Euler equation, integration datum and curvature mode MAP-TYPE=intertwiner
```

## 1. Reuse and source custody: three different meanings of volume

Basis `fe43936285c50706eaeb54f942ba439dbde07bda`. The [rotation-rigidity theorem](source-action-rotation-rigidity-2026-11-26.md), §§4–5, already classifies its constant normal seed hyperplanes. Lorentz covariance selects `tr S=0`; `det y=det eta exp(-2 tr S)` makes this a fixed-volume **fibre seed hypersurface**. Its analytic CK extension still realizes every analytic observed history. Neither the theorem nor its nonnull trace conormal restricts variations of the base metric. No new credit is taken for that classification.

The [source register](../../lab/sources/source-claim-register.yaml) and [primary draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf) give:

| Source | Affirmed object; limit relevant here |
|---|---|
| SC-GEO-03, draft p17 and p31 §5.1.1 | Metric bundle and base metric as a section; not a prescribed base volume form. |
| SC-ACT-01, p43 eq9.1 and p44 eq9.4 | Action domain `G × MET(X^{1,3})`; no determinant-constrained metric domain displayed. |
| SC-ACT-02, p45 eq9.7–9.10 | The displayed variation is in varpi at fixed g; annotated Einstein recovery does not supply the missing observed metric Euler equation. `Ric−Rg/2` is trace-reversed, not tracefree. |
| SC-COS-01 / SC-MAS-03, p62 eq12.21 and p64 item iii | Cosmological term, gauge-field/mass relation and VEV interpretation; not a derivation of a unimodular integration datum. |
| SC-COS-50/51, [TOE transcript](../../lab/sources/transcripts/toe-weinstein-gu-40-years.md), 02:14:44 and 02:22:20; standard-GR identity rationale at 02:16:33 | The conditional DESI discussion asks for a variable, VEV-capable replacement with a differential identity. Its adjoint one-form is different from a constant Lambda integration datum. |
| SC-COS-52, [UCSD seminar transcript](../../papers/drafts/Transcript%20into%20the%20impossible.md), 00:02:05, completed at 00:25:56–00:27:00 | The seminar separately states the one-form replacement. It is not a TOE-interview claim or a unimodular derivation. |

All named register statements retain their recorded ASSERTS polarity. Absence of a determinant prescription in this inspected material is **not** exclusion of an unprinted completion. Source GU's unimodular bridge is undetermined. Native K95 trace reversal, spacetime Einstein trace reversal and removing the spacetime Euler trace are three different operations.

A finite fibre moment or a normalized reference is a third object: fixing it does not fix the metric volume on X. The [owned wedge reduction](wedge-shiab-einstein-reduction-2026-11-27.md), §§3–7, explicitly varies the metric in its covariantly moving reference class. A held external regulator has a different variation and even a different quadratic Einstein sign. The native unregulated indefinite fibre volume is infinite. None of those alternatives is silently substituted below.

## 2. Variational classification

For local compact interior variations in four dimensions, let

    S = integral dVol_g [A R + alpha Ric² + beta R² + c],
    b = beta + alpha/3,
    delta S = integral dVol_g E_mu nu delta g^mu nu.

Coefficients are constants. Boundary terms are retained or avoided by compact interior support. The complete metric Euler tensor obeys the diffeomorphism identity `nabla^mu E_mu nu=0`. Its trace is

    T = 6b box R - A R - 2c.                           (1)

On an Einstein metric `Ric=Lambda g`, both quadratic Euler tensors vanish, including for nonzero Weyl curvature, and

    E = -(A Lambda+c/2)g.                              (2)

Thus unrestricted stationarity with `A != 0` fixes `Lambda=-c/(2A)`. A continuum of Einstein Lambda at unchanged coefficients requires `A=c=0`. Pure quadratic gravity is the appropriate contrary control. This is a classification of these Einstein sectors, not of all solutions.

Pointwise prescribed volume density instead permits exactly tracefree metric tangents. Its stationarity law is

    E_TF = E - (T/4)g = 0.

By the same complete conservation identity, `dT=0`; on each connected component,

    E = ell g,  ell constant.                         (3)

This is precisely the unrestricted metric equation with `c_eff=c+2ell`, because a constant addition `2ell` to the action density shifts its Euler tensor by `-ell g`. The tracefree law is invariant under `c -> c+Delta`, `ell -> ell-Delta/2`. It moves the vacuum-density constant into a sector label; it does not select that label.

This is the standard classical unimodular mechanism, not a novelty claim: [Eichhorn, 1501.05848, §2.1](https://arxiv.org/abs/1501.05848) derives the corresponding f(R) equivalence with the conservation premise. The Weyl/Euler decomposition in the owned reduction supplies its application here. A fixed **total** volume is different: under the ordinary regular global variational assumptions its annihilator supplies a constant Lagrange multiplier directly. A pointwise density gives a multiplier function first, then needs the identity to make it constant. Neither restriction follows from the normal seed theorem.

For the reviewed leading wedge class,

    A=-a=-99 h m1/4, alpha=h m0/2,
    b=17 h m0/12, c=2115 h m2/16.

Here h is nonzero; the positive-moment class has `m0,m1>0`, `m0m2>=m1²`. At `ell=0`, the owned `Lambda=(235/88)m2/m1` is an action-coefficient ratio, not an integration constant. Under (3),

    R_ell=2(c+2ell)/a,  Lambda_ell=R_ell/4,
    m_s² = A/(6b) = -99m1/(34m0) < 0.                 (4)

The constant drops out of the mass. Equation (4) alone is insufficient to claim mode admission; the next section checks all rows and the volume constraint.

## 3. Structural full-row theorem, including the critical sector

**Theorem.** Fix any real constant-coefficient quadratic action above with `b != 0`, `A/(6b)<0`. For every `H>0`, choose the sector `ell` making `R_ell=12H²`. The volume-restricted metric equations have a real local linear solution tangent to an exactly fixed-volume metric path, with `delta R=exp(r t)` and `r>0`, on the flat expanding de Sitter patch. This includes `F0=A+24bH²=0`.

This does not require a positive kinetic pairing, normalizability on an infinite spatial slice, or a physical observer identification. It excludes local linear stability only in the stated ordinary real solution class.

**Proof.** Let

    gbar = -dt² + exp(2Ht) delta_ij dx^i dx^j,
    mu²=-A/(6b)>0,
    r=(-3H+sqrt(9H²+4mu²))/2>0,
    q(t)=exp(rt)/[3(r+3H)(r+4H)].

Use the exact metric path

    g_epsilon,00=-(1+epsilon q)^(-3),
    g_epsilon,ij=exp(2Ht)(1+epsilon q)delta_ij,
    g_epsilon,0i=0.                                    (5)

On any bounded patch, small epsilon preserves its Lorentz signature. Its determinant is exactly `-exp(6Ht)` for every such epsilon. Its tangent has `h00=3q`, `hij=q gbarij`, zero trace. The path is a variational path; only its tangent is claimed to solve the linearized equations.

Keep the lapse `N=(1+epsilon q)^(-3/2)` while differentiating. The proper-time Hubble variation and scalar curvature variation are

    delta H=(qdot+3Hq)/2,
    delta R=3(qddot+7H qdot+12H²q)=exp(rt).             (6)

Four-dimensional `Ric²= C²/2-E4/2+R²/3`. Every metric in (5) is flat FLRW, hence Weyl-flat; its Bach tensor is zero. The constant Euler term contributes no interior row. The remaining complete metric equation is that of

    f(R)=A R+bR²+c_eff.

For the de Sitter background, the linear temporal constraint and spatial evolution row reduce to

    6F0 H delta H = 6b H(H-r) delta R,
    -2F0 delta Hdot = 2b(delta Rddot-H delta Rdot).     (7)

Their tensor origin is checked independently in the exact probe using the Ricci tensor and scalar Hessian of the arbitrary-lapse FLRW metric, before substituting the mode. Offdiagonal and momentum rows vanish by homogeneity/isotropy, not by omission. The identities

    r²+3Hr=mu²,
    F0=6b(H-r)(r+4H)

make both equations (7) zero. No division by F0 occurs. Since Rbar is constant, every infinitesimal diffeomorphism has `delta R=Lie_xi Rbar=0`; the nonzero curvature perturbation is not pure gauge. This proves the theorem.

### Critical background is not an untested escape

At `F0=0`, `r=H` and `q=exp(Ht)/(60H²)`. Equations (5)–(7) remain valid. The usual conformal representative becomes degenerate; a separate check uses `psi=t exp(Ht)/(15H)`, `delta g=psi gbar`. It gives `delta R=exp(Ht)` and `D(delta R)=0`, where `D=gbar box−nabla nabla+3H²gbar`. A diffeomorphism brings this representative to (5)'s tangent. The polynomial factor belongs to that representative; it is not a new Jordan defect of the original 14D operator.

The elementary GR control has `b=0`, so no scalar box term exists in (1); it lies outside the theorem. The healthy `A>0,b>0` R+R² control gives positive mass. Fixing determinant removes the metric trace variable but not, in this quadratic class, this gauge-invariant curvature mode.

## 4. Growth, choice cost and the remaining alternatives

For the conventional sign sector `a,b>0`, `F0>0` is equivalent to

    ell > a²/(8b)-c/2,
    H² > a/(24b),
    0 < mu²/H² < 4,    0 < r/H < 1.                   (8)

F0 positivity here is a named scalar-tensor/Einstein coefficient condition, not a full physical positivity proof for quadratic gravity. Critical F0 gives `r/H=1`; negative F0 sectors also have the mode, without any positive-norm claim. For fixed a,b, selecting larger finite H can make growth slow, but cannot make r zero. The previous unshifted moment bound `r/H<=0.849700` is not a bound on the new ell-family.

A fixed-volume modification therefore has a specific price and limitation: an added variational rule plus a global sector datum (possibly one per disconnected component), while no scalar-stability gain is earned in this class. No such rule is added to the adopted choice inventory. No observed Lambda, dark-energy equation of state, or relation to DESI follows.

Survivors include changed coefficient signs or a vanishing scalar coefficient, nonreal/physical projections, nonlocal or restricted state domains, matter/background corrections, higher-order or nonlocal reduction, and other source-admissible Shiab members. These alter tested premises and need their own equations. Signed measures and the infinite native integral retain their prior status. This is not a universal GU tachyon inference.

## 5. Conservation is an independent, testable prerequisite

For any symmetric Euler/source residual with `nabla E=j`, equation `E_TF=0` entails

    d ell=j,  dT=4j.                                  (9)

Thus `dj=0` is necessary locally; on a contractible patch it supplies a local primitive, but does not prove the other field equations have a solution. A globally defined ell requires zero periods, i.e. exactness, not merely closedness. Only `j=0` makes ell constant. No GU coderivative is identified with j by name.

For example, an externally held scalar density coefficient c(x) gives `E=−c(x)g/2`, hence `E_TF=0` but `ell=−c(x)/2` is not constant. For externally held scalar coefficients the spurion identity is

    nabla E=−(1/2)[R dA+Ric² d alpha+R² d beta+dc].     (10)

It follows by varying the metric and the transforming scalar backgrounds under a common compact diffeomorphism. These fields are not varied in the metric Euler equation itself. If coefficients instead depend on the metric, all their metric variations must be included; if dynamical, their own equations enter. Equation (10) cannot be reused as if those were the same cases.

This gives a quick necessary test for observer-dependent reference proposals: an arbitrary moment profile cannot simply be called a variable cosmological constant; its full current must satisfy (9). `j=x dy` fails even locally; `j=dtheta` on a circle is locally closed but has a nonzero period. An exact nonzero current gives a variable multiplier plus an undetermined constant. These are calibrated differential controls, not claims that GU selects those currents.

The [owned ambient-conservation descent result](bet-cosmology-conservation-descent-2026-11-27.md) and [theta divergence audit](source-action-theta-divergence-2026-11-27.md) are reused for their stated scopes. Their one-form identities do not by themselves produce the conservation of the same observed symmetric tensor required here. Full coupled equations, normal-jet restrictions or a nonlocal readout could supply it; that bridge remains undetermined. No discovery-lane verdict is promoted through this citation.

## 6. Literature, validation and consequence

The mechanism is familiar unimodular gravity. Eichhorn's [§2.1](https://arxiv.org/abs/1501.05848) supplies the classical conserved f(R) comparison. [Nojiri–Odintsov–Oikonomou, 1605.00993](https://arxiv.org/abs/1605.00993) explicitly distinguishes covariant and noncovariant formulations and their Newton-law calculations. Its flat static scalar-elimination wording is not a proof about the exact fixed-density de Sitter metric path (5). Here the claimed mode is decided directly on the named metric equations; no general verdict on every unimodular quantization follows. The [standard f(R) stability review](https://arxiv.org/abs/1002.4928) remains the ordinary scalar-mass comparator. No world-novelty claim is made.

[Exact probe](../../tests/program-focus/unimodular_lambda_probe.py) and [certificate](../../lab/process/unimodular-lambda-certificates.json) derive lapse-corrected curvature and both independent metric rows; they include the critical case, a lapse-omission mutation, GR and positive-mass controls, moment substitution and local/global conservation controls. [Lean](../../Lean/GUFormalization/UnimodularLambda.lean) checks seven finite algebraic/order cores only. Differential geometry, Noether identities, local mode interpretation and source custody are written proofs checked by independent reviewers; they are not fully Lean-formalized. Acceptance lives in the [review record](../../lab/process/hostile-reviews/2026-11-28-unimodular-lambda-review.md).

The scoped question is settled: the source bridge is unbuilt; the owned unrestricted reduction fixes its Einstein curvature; the conditional tracefree variant frees a datum but retains the full-row growing scalar throughout its de Sitter sectors. This consumes the basic unimodular stability-repair test. No new physical choice, source claim, physics-ledger verdict or completed GU theory follows.

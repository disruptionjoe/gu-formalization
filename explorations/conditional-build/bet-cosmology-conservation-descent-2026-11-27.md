---
title: Conserved bulk one-forms have arbitrary local observed traces
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-COSMOLOGY
tier: T1
expected_delta: Decide whether ambient one-form conservation alone supplies a conserved observed stress
  through a local readout.
actual_delta: Weighted covariantly coclosed one-forms restrict surjectively onto arbitrary smooth local
  observed one-forms. Conservation of any finite-order observed-only stress readout is therefore an off-shell
  identity or requires additional premises; every zero-order such readout is field-independent on each
  connected field domain.
class_covered: All fixed smooth nondegenerate ambient metrics, nondegenerate sections of positive codimension,
  finite-rank real or complex coefficient bundles with fixed smooth connection, and smooth positive weights
  independent of the unknown one-form; local smooth germs satisfying the coderivative equation alone.
  Readouts use only finite jets of the literal observed one-form and fixed backgrounds.
premises:
- lab/sources/source-claim-register.yaml#SC-COS-50
- lab/sources/source-claim-register.yaml#SC-COS-51
- lab/sources/source-claim-register.yaml#SC-COS-52
- explorations/conditional-build/source-action-theta-divergence-2026-11-27.md
- explorations/conditional-build/source-action-slice-completion-2026-11-25.md
- explorations/conditional-build/k2242-ambient-conormal-descent-2026-10-29.md
source_bridge:
  status: conditional
  reason: The source requires an automatic dark-energy identity and names an adjoint one-form, but does
    not select this coderivative alone, a local stress readout, unrestricted local solution germs or the
    physical domain. The theorem tests a proposed implication class, not the full source equations.
kill_condition: Local surjectivity excludes any genuinely field-dependent zero-order observed stress whose
  conservation is alleged to follow from ambient coderivative conservation alone; higher-order readouts
  survive exactly when already identically conserved.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-AMBIENT-CODERIVATIVE-TO-OBSERVED-STRESS
internal_target_verdict: zero-order field-dependent implication class excluded under the declared local-only
  premises
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# Conserved bulk one-forms have arbitrary local observed traces

```yaml
program_target: BET-COSMOLOGY
tier: T1
expected_delta: Test the automatic ambient-to-observed conservation bridge without another candidate action.
actual_delta: Arbitrary smooth observed one-forms lift to local weighted covariantly coclosed fields; a local observed stress gains no new differential identity from that premise alone.
```

## Result in plain English

**Even successfully making the bulk one-form divergence-free would not, by itself, supply a conserved observed stress tensor.** Locally, one unobserved normal component can balance any prescribed behavior of the observed one-form. This holds for arbitrary smooth connection coefficients, positive weights and nondegenerate metric signatures in the class below.

The consequence is stronger than one counterexample. A stress tensor built from finitely many derivatives of the observed one-form is conserved for every such bulk field **if and only if** it is already conserved for arbitrary observed fields, without using the bulk equation. If it uses the observed field value but no derivatives, it must be independent of that field on each connected component of the field-value fibre domain. Background-only tensors remain possible.

This identifies an additional burden for a dark-energy interpretation: an actual observed identity, further equations or restrictions linking normal and observed data, or a readout outside this local observed-only class. It constructs none of them and does not claim the source requires this insufficient bridge.

| State | Scope |
|---|---|
| **ESTABLISHED** | Local smooth trace surjectivity for the weighted covariant coderivative; the finite-order identity equivalence; zero-order field independence. |
| **RULED OUT** | Genuinely field-dependent algebraic observed stress acquiring conservation from the ambient coderivative equation alone on the unrestricted local class. |
| **NOT MODELED / UNDETERMINED** | Full source or W2 stationary systems, physical solution spaces, global flux/boundary restrictions, nonlocal/normal-jet readouts, cosmological history, DESI/CMB predictions or GU falsification. |

```gu-typed-objects
result: local conservation descent and observed-only stress readout classification
carrier: coefficient-bundle-valued ambient one-form and its literal section contraction with full coefficient fibre retained LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=N/A
pairing: nondegenerate ambient metric and smooth positive scalar integration weight; compatible fibre pairing when formal-adjoint language is used ON=coefficient_valued_forms
real_structure: arbitrary fixed real coefficient connection, including real adjoint Lie algebra; complex version componentwise; K77 and K95 separately within signature-independent assumptions
grading: exterior degree1; no chirality or physical-count grading
action_owner: repository-construction of a conservation-equation comparison only; no action or stationary system constructed
target: weighted covariant coderivative and observed stress divergence MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a typed implication test between an ambient adjoint one-form and an observed stress tensor, not their identification. No scalar quintessence, ordinary Higgs, repeated-family or positive-metric model replaces the source object. Read [routing](../../lab/methods/source-native-comparator-routing.md). Source2+1, independent bars, fullU/optionalSp and K77/K95 remain distinct.

## 1. Precise hypotheses and reuse

Let (M,G) be a smooth pseudo-Riemannian manifold and i:S→M a smooth embedded nondegenerate section of positive codimension. Let E→M be a finite-rank real vector bundle with fixed smooth connection A; the complex case is the underlying real statement. Let rho be any fixed smooth strictly positive scalar weight, independent of the unknown E-valued one-form theta. Set qtheta=i*theta, retaining E|S as coefficient bundle.

Use the covariant divergence definition

\[
\delta_A^\rho\theta
=-\mu^{-1}\left[\partial_i(\mu G^{ij}\theta_j)
                  +A_i(\mu G^{ij}\theta_j)\right],
\qquad \mu=\rho\sqrt{|\det G|}.
\]

For an adjoint bundle, A_i acts by commutator. With a compatible nondegenerate fibre pairing this is the weighted formal coderivative. Neither a positive fibre norm nor a global self-adjoint realization is needed for this local differential equation.

All statements concern germs near a section point. The extension neighborhood may depend on the data. No uniform fixed-tube estimate, Hilbert norm, closed observation domain, finite total action or global boundary condition is asserted. A density depending on theta itself is not quantified by this theorem; that would change the differential equation.

Already owned and reused:

- [Slice completion](source-action-slice-completion-2026-11-25.md) §2: analytic arbitrary observed histories from a noncharacteristic normal equation, with its source/domain ceilings.
- [K2242 conormal descent](k2242-ambient-conormal-descent-2026-10-29.md) §§1–3: free normal-jet obstructions and constant-coefficient solution controls.
- [Theta divergence](source-action-theta-divergence-2026-11-27.md) §2: actual W2 convention and the affine connection cancellation below. Its stationary counterexamples are not recomputed.

New content is the **smooth weighted covariant divergence extension**, including variable coefficients, and its consequence for the entire class of local observed stress readouts. This is an application of classical ODE and jet reasoning, not a claim of a new general mathematical discovery.

## 2. Local extension theorem

**Theorem.** Every smooth E|S-valued one-form beta near a point of S is the literal restriction of a smooth local theta satisfying delta_A^rho theta=0.

Because TS and G are nondegenerate, the normal bundle is nondegenerate and has a locally non-null section n. Choose a local hypersurface H containing S whose tangent along S is n-perpendicular. This can be built in a local tubular chart using the remaining normal directions. After shrinking, H is nondegenerate. Its Gaussian normal collar has coordinates (r,z^a), H={r=0}, and

\[
G=\epsilon\,dr^2+G_{ab}(r,z)dz^a dz^b,\quad
\epsilon\in\{+1,-1\},\quad G^{ra}=0.
\]

Extend the prescribed tangential one-form beta smoothly to all components theta_a on the collar. Prescribe any smooth initial normal component on H, for example zero. Since G^{ar}=0, the raised tangential components u^a=G^{ab}theta_b are known independently of theta_r.

Put w=mu u^r=mu epsilon theta_r. The sole conservation equation becomes

\[
\partial_r w+A_r w
=-\sum_a\left[\partial_a(\mu u^a)+A_a(\mu u^a)\right]. \tag{1}
\]

The right-hand side is known smooth data. Equation(1) is a finite-dimensional linear ODE in r, with z as parameters. Local existence and smooth dependence give w(r,z), hence theta_r=epsilon w/mu. This changes no prescribed tangential component, so qtheta=beta exactly. All tangential derivatives of beta are consequently unrestricted as well. The equation holds in a neighborhood, not only at a point or to finite Taylor order.

This argument works for either normal sign and every smooth positive rho. It preserves the actual real coefficient bundle through its real connection. It does not transfer any Clifford, adjoint or Fredholm data between signatures: it is a geometric divergence theorem whose hypotheses are separately satisfied in each admitted local setting.

For classical ODE input, see Conrad's [linear ODE notes](https://math.stanford.edu/~conrad/diffgeomPage/handouts/linearode.pdf) and [integral curves and smooth dependence](https://math.stanford.edu/~conrad/diffgeomPage/handouts/intcurve.pdf). Feres's [notes §7.5](https://www.math.wustl.edu/~feres/545.pdf) supply the standard divergence/codifferential relation; the indefinite, weighted bundle formula is stated explicitly above rather than imported from a Riemannian sign convention.

### Distortion-dependent connection: an existing extension

In the adjoint case, for fixed B and any prescribed smooth scalar s,

\[
\delta_{B+s\theta}^{\rho}\theta-\delta_B^{\rho}\theta
=-sG^{ij}[\theta_i,\theta_j]=0.
\]

Symmetric contraction kills the antisymmetric bracket; no derivative of s occurs in the connection difference. Thus the same theorem applies to the ordinary A=B+theta distortion dictionary for this equation alone. It does not imply that these freely extended fields satisfy a full action's Euler equations. General field-dependent connections and weights are not included by this cancellation.

## 3. What can descend to observed stress?

Fix all observed background structures, including the nondegenerate metric g=i*G. Let a smooth local stress rule have finite differential order k:

\[
\mathcal T[\beta](x)=F(x,j^k\beta(x)).
\]

It uses only the observed field and its tangential jets, not unobserved normal values/derivatives, integrals, global choices or extra equations. Any gauge-covariance or symmetry condition may be imposed as an additional restriction on F; the following implication holds even without requiring it.

**Corollary.** Conservation of T[qtheta] for every local solution of delta_A^rho theta=0 holds if and only if

\[
\nabla^\mu\mathcal T[\beta]_{\mu\nu}\equiv0
\quad\text{for every smooth local beta}. \tag{2}
\]

The reverse direction is immediate. For the forward direction, extend each beta by the theorem and apply the assumed conservation. Since every finite jet of beta can be realized by a smooth local field, (2) is an off-shell differential identity on the readout's jet domain. The ambient equation adds no constraint to that domain. The same logic applies to any other claimed local differential identity on qtheta.

### Zero-order classification

Suppose T_mu nu=F_mu nu(x,beta), on an open field-value domain, componentwise in each fibre. At a point choose normal coordinates for g. Hold x and beta fixed while varying each first derivative partial_lambda beta_A independently. The derivative-dependent part of the divergence is

\[
g^{\mu\lambda}\frac{\partial F_{\mu\nu}}{\partial\beta_A}
\,\partial_\lambda\beta_A.
\]

Each coefficient must vanish. Invertibility of g gives partial F_mu nu/partial beta_A=0 for every mu,nu,A. Thus F is independent of beta on each connected component of the field-value fibre domain. Its remaining x/background dependence must itself have zero divergence. This does **not** say F is constant in spacetime or that only Lambda g is possible; background curvature tensors may carry their own identities.

### Differential positive control

In flat observed space with constant nondegenerate metric eta,

\[
\mathcal T_{\mu\nu}
=(\partial_\mu\partial_\nu-\eta_{\mu\nu}\Box)f(\beta)
\]

is identically conserved by commuting partial derivatives, and can be nonzero. It is a countercontrol to an overclaim that all differential readouts vanish. No physical stress or action is selected by writing it. On a curved metric, covariant derivatives introduce curvature terms; the displayed flat formula cannot be carried over unchanged.

## 4. Direct controls and escape boundaries

A flat scalar control with G=dx²+epsilon dr² is

\[
\theta=x\,dx-\epsilon r\,dr.
\]

Its ambient divergence is zero, while its observed trace at r0 is x dx, whose divergence is1. This already calibrates the distinction. The exact probe also checks nonconstant weights, matrix connection terms and free finite jets; the universal variable-coefficient theorem comes from equation(1), not a finite fixture census.

The theorem makes no claim for global or boundary domains, simultaneous field equations, required symmetries or finite-energy domains, physical quotients, nonlocal readouts, or readouts using normal jets. Whether a particular additional condition actually prevents arbitrary extension needs its own proof. No such restriction is proved sufficient, source-selected, or physically viable here. A degenerate/null section also needs its own analysis. No new restriction is installed as a rescue.

This result is not solution-trace nonclosability. Surjectivity gives no sequence with small bulk norm, no common tube, and no norm estimate. The earlier changed-operator trace burden remains open; CK or a principal-symbol computation alone does not remove it.

## 5. Source relevance, selection and status

SC-COS-50 (TOE2025,02:14:44, transcript lines578–582) asserts a variable dark-energy term with an automatic identity opposite the Einstein tensor. SC-COS-51 (02:22:20, lines608–610) and SC-COS-52 (UCSD2025,00:02:05) identify an adjoint-valued one-form replacement. They do not specify this coderivative alone as the complete observed identity, nor the readout and admitted solution domain used here.

Therefore the source claim is not refuted. The class result says precisely why even establishing the previously conditional ambient identity would leave a second obligation: show how a conserved observed quantity follows in the actual source system. The full equations may supply normal constraints or a different identity; those possibilities are **NOT MODELED / UNDETERMINED** here.

This LC-BETS wave adds no guessed action, potential, weight selection, state rule or choice family. Choice inventory remains10/4/bookkeepingnet6/0source-selected predictions, with no new obligation credit. No matrix cell, ledger verdict, canon or paper changes. A lane-B rederivation would be required before scientific matrix absorption.

The quick reconnaissance prevented two redundant routes: all-section density incompatibility is false for the owned source-adapted geometry, and existing paired-current comparisons do not supply the missing physical map. The selected theorem instead removes a whole proposed conservation-import class. It does not license repeated tests of alternative zero-order readouts within that class.

## Verification

Fresh independent replay passed61 grouped exact controls, including148 collar lifts over both normal signs and two positive nonconstant weights, nonabelian connection controls, a rank108 polynomial chain-rule calibration and the nonzero flat differential control. Runtime was0.099821917seconds; the deterministic certificate is47,367bytes. These fixtures calibrate the formulas, not the universal smooth theorem.

Four finite Lean cores and internal specialist/hostile review are recorded in [evidence](../../lab/process/bet-cosmology-conservation-descent.json) and [review](../../lab/process/hostile-reviews/2026-11-27-conservation-descent-review.md). The smooth geometric ODE theorem and source applicability are written mathematics, not fully Lean-formalized. Internal review is not external-expert verification or publication.

```sh
python3 tests/program-focus/conservation_descent_probe.py --verify
```

---
title: The constructed stationary action does not imply its proposed dark-energy conservation law
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-COSMOLOGY
tier: T1
expected_delta: Test the actual source-shaped one-form coderivative at both certified W2 stationary roots,
  and determine the homogeneous or analytic-branch mechanism.
actual_delta: Both kappa1 coupled stationary roots have certified nonzero ambient and literal-section
  coderivatives of the reconstructed theta. The ambient homogeneous map has rank12/kernel47; the observed
  map rank11/kernel48. The entire sufficiently-small nonzero inverse-kappa analytic branch fails ambient
  conservation first at order h3, coefficient -27/32, and observed conservation at order h, coefficient21/16.
  This excludes the automatic C3 implication for this action/dictionary, not GU.
class_covered: Fixed W2/K95 full-U candidate with its source-shaped theta=T dictionary; complete owned59-dimensional
  symmetry-fixed homogeneous family and both certified kappa1 roots; actual convergent near-inverse-kappa-zero
  branch. The affine-connection identity and homogeneous observation defect hold independently of the59
  restriction. No classification of all stationary roots, action classC or source-required physical domain.
premises:
- lab/sources/source-claim-register.yaml#SC-COS-50
- lab/sources/source-claim-register.yaml#SC-COS-51
- lab/sources/source-claim-register.yaml#SC-COS-52
- lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md
- explorations/conditional-build/source-action-wave2-construction-2026-11-25.md
- explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md
- explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md
- lab/process/source-action-deep-coefficients.json
source_bridge:
  status: conditional
  reason: The source prints a distortion one-form and demands an automatic differential identity, but
    does not uniquely select this action, K95 realization, theta dictionary or particular coderivative.
    The displayed dictionary is exact within the reconstructed candidate; a 4D Einstein stress/readout
    bridge remains absent.
kill_condition: A certified nonzero coderivative on a coupled stationary solution disproves the proposed
  universal on-shell C3 implication for this action/dictionary. It does not exclude other actions, all
  stationary backgrounds, global boundary-selected states, a different differential identity, or GU.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-W2-AUTOMATIC-THETA-CONSERVATION
internal_target_verdict: excluded for both certified roots and the sufficiently-small nonzero inverse-kappa
  branch
canon_verdict_change: none
---

# The constructed stationary action does not imply its proposed dark-energy conservation law

```yaml
program_target: BET-COSMOLOGY
tier: T1
expected_delta: Test the candidate's dark-energy one-form conservation on actual coupled stationary fields.
actual_delta: Both roots and a punctured analytic branch violate the proposed coderivative identity; source and physical verdicts unchanged.
```

## Result first

**The action's stationary equations do not enforce the proposed conservation law for its dark-energy one-form.** At both already-certified kappa1 backgrounds, the actual ambient covariant divergence is nonzero. This remains true for every connection of the form B+sT, even when s is a smooth real function. The observed one-form obtained by literal section contraction also has nonzero divergence in its retained ambient adjoint bundle.

The failure is not limited to those two backgrounds. On the already-proved convergent branch near h=1/kappa=0, the first two ambient orders cancel, but the third is exactly

    delta_B T(h) = -(27/32) h^3 gamma4 + O(h^4).

Thus every sufficiently small nonzero member fails the proposed identity. This is a counterexample to an implication of the actual candidate equations, not a failure to construct a missing solution.

| State | Established scope |
|---|---|
| **ESTABLISHED** | Exact ambient/observed coderivative maps, certified nonzero values at both roots, and nonzero divergence on a punctured analytic branch. |
| **RULED OUT** | The implication “the declared W2 coupled stationary equations imply delta_A theta=0” under this candidate's theta=T dictionary. Literal pullback does not preserve coderivative conservation automatically. |
| **NOT MODELED / UNDETERMINED** | Whether every GU source completion requires this dictionary or operator; whether other stationary/global boundary-selected solutions conserve theta; an observed Einstein stress tensor, cosmological history or GU falsification. |

No new action, coefficient, state selector or condition is imposed. The action and roots remain mathematically valid stationary constructions. Their proposed dark-energy interpretation has failed this additional test. Choice budget remains 10 families / 4 obligation bundles / net 6 / zero source-selected predictions. This is a substantive BET-COSMOLOGY attempt with no new guessed action or scalar potential, consuming the carried-over discovery-bet opportunity.

```gu-typed-objects
result: stationary counterexamples to reconstructed theta conservation
carrier: native K95 full-U adjoint-valued one-form on metric-fibre geometry and its literal flat-section contraction LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=N/A
pairing: native nondegenerate real trace/form pairing with actual absolute density ON=adjoint_valued_forms
real_structure: primary-minus K95 u64,64; independent matter and bars vanish at the tested backgrounds
grading: Clifford degree used for exact coefficient receivers only; no physical chirality or family grading
action_owner: repository-construction fixed W2 action with held SEminusonehalf
target: ambient and observed gauge-covariant coderivatives, not Einstein stress divergence MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** This tests an actual source-shaped one-form in the constructed candidate. It does not replace that one-form with a scalar Higgs/quintessence or a conventional Yang–Mills-square action. Preserve source 2+1, independent bars, full U versus optional Sp, primary-minus, contraction and K95/K77. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Source dictionary and the exact question

SC-COS-50 requires a variable dark-energy term with an automatic differential identity. SC-COS-51/52 point to the source's displayed

    T_omega = varpi - epsilon^-1 d0 epsilon.

They do not uniquely specify the operator delta_A, the candidate completion or a four-dimensional stress construction. The older [C3 discussion](../../canon/dark-energy-theta-divergence-free.md) makes the divergence-free inference conditional on an unproved Euler-sector identification. Its historical title is not evidence that the identity is established.

In the chosen two-frame candidate, define

    varpi=A-A0,     d0 epsilon=d epsilon+A0 epsilon-epsilon A0,
    B=epsilon^-1 A0 epsilon+epsilon^-1 d epsilon,
    T=A-B,         T_hat=epsilon T epsilon^-1=Ahat-A0.

Then `varpi-epsilon^-1d0epsilon=T` by direct algebra. This is an exact dictionary **inside the reconstruction**, not proof that the source uniquely chooses it. In the reference frame below, B denotes A0 and T denotes T_hat. The coderivative conjugates under the same frame transport, so changing frames cannot erase a nonzero result.

The test is precise: do the already-owned W2 coupled stationary configurations satisfy delta_A T=0 in this interpretation? Gauge covariance alone cannot answer it. The candidate's epsilon dressing identity is already known; it expresses compensator redundancy, not this extra equation. The old W180 record-current construction uses a different theta identification and action and cannot supply this candidate's conservation law.

## 2. Actual one-form coderivative

For the native ad-invariant trace pairing and absolute metric density, the coordinate formula is

    delta_A T = -G^{ij}(partial_i T_j+[A_i,T_j]-Gamma^k_ij T_k).

It is also the density-divergence formula with the same connection and metric. This fixes the indefinite-signature convention directly; a Riemannian Hodge sign or a transpose of a finite invariant matrix is not substituted.

The owned homogeneous frame has diagonal metric

    d=(1,1,1,-1,-16,8,24,48,8,8,-8,8,-8,-8),

spin-LC coefficients beta_i and Nomizu coefficients Lambda[i][j][k]. For an invariant one-form with constant components in this equivariant frame,

    D(T):=delta_B T
      =-sum_i (1/d_i)([beta_i,T_i]-sum_j Lambda[i][i][j]T_j).   (1)

The form-connection term is essential: this homogeneous model is not unimodular in the trace direction. An independent coefficientwise integration-by-parts calculation using `div(e4)=-4` gives the same map on every basis column.

For any scalar s, including a smooth function of position,

    delta_(B+sT)T-delta_B T = -s G^{ij}[T_i,T_j]=0.              (2)

The symmetric inverse metric contracts an antisymmetric commutator. No derivative of s appears in this connection difference. In contrast, `D_(B+sT)T=D_B T` for the exterior covariant derivative would be false: its self-wedge term does not cancel. Equation(2) removes only the stated affine connection ambiguity.

### Controls that fix the convention

- The Clifford solder form Phi1 is LC-parallel, hence `delta_B Phi1=0`.
- The admissible central one-form `i theta4 I` gives `delta_B(i theta4 I)=-iI/4`. Here d4=-16; omitting the form/density term would incorrectly give zero. The identity matrix alone is not a native u(H) generator.
- Native metric compatibility and the spin/Clifford connection identity are checked independently.
- Two constructions of the full one-form map agree on all 59 basis columns. The old degree-two adjoint is not reused as though it already computed this map.

## 3. Whole homogeneous family and stationary roots

The published 59-dimensional real family is a symmetry-fixed subfamily of the complete 216-dimensional connected-isotropy invariant carrier. Its basis, full Euler coefficients and two root contraction certificates are already owned. This wave adds no invariant-field ansatz and does not claim that59 exhausts all natural fields or all stationary solutions.

The exact ambient map D on this family has rank12 and kernel dimension47. Its 300 nonzero Clifford-coordinate receivers are dependent; their number is not the rank. The certificate retains the sparse map, exact row reduction and kernel data. The probe verifies the complete basis against the declared invariant/reality/reflection conditions and authenticates its existing generation/completeness claim.

At kappa=1, both roots solve the actual full connection equation. The previously proved original-density argument also makes them stationary under compact arbitrary base-metric variations on the fixed product regulator; zero independent matter/bars solve their equations, and compact epsilon variations are induced connection variations. These are **coupled local stationary witnesses**, not merely roots of a selected Hessian. They are not certified to satisfy the separately proposed charged external boundary datum or to belong to a physical state space.

A single coefficient already proves nonconservation. Let a_H be the horizontal Clifford-vector amplitude and a_tr the normal trace amplitude, in the published basis coordinates. The gamma4 receiver is

    [D(T)]_gamma4 = (a_H-a_tr)/4.                             (3)

The actual certified root balls give the following outward bounds. Every endpoint is a terminating rational; decimals do not replace the interval computation.

| Coupled stationary root | Ambient gamma4 coefficient | Observed gamma4 coefficient |
|---|---:|---:|
| First kappa1 root | [-0.003383081580965, -0.003383081580962] | [0.0002781620842724, 0.0002781620842726] |
| Second kappa1 root | [0.010353978945645, 0.010353978945649] | [-0.0082824555895261, -0.0082824555895257] |

For each linear receiver ell and the exact infinity-norm root ball of radius r,

    |ell(t_true)-ell(t_center)| <= r sum_j |ell_j|.

The verifier reconstructs the polynomial residual/Jacobian contraction bounds and propagates the existing rational ball. It recomputes all receivers, while the compact certificate stores the simplest separating component and hashes of the full bounds. This is not a floating residual or a claim based on a rounded zero.

Both stationary witnesses therefore disprove the proposed universal conservation implication. Imposing conservation as a separate condition would remove these witnesses; that condition is not silently added to the candidate equations here.

## 4. A branch-wide obstruction, not just two points

Use h=1/kappa. The full homogeneous Euler equation is

    T+h(S+KT+N(T,T))=0,

where N uses the already-owned symmetric quadratic convention. The existing implicit-function/convergence theorem supplies an actual analytic branch through T(0)=0. Its first coefficients are uniquely

    T1=-S,
    T2=KS,
    T3=-K^2S-N(S,S).

The exact new map gives

    D(S)=0,        D(KS)=0,
    D(K^2S)=(27/32)gamma4,        D(N(S,S))=0.

There are no other components in the displayed third-order divergence. Consequently

    D(T(h))=-(27/32)h^3 gamma4+O(h^4).                       (4)

Analyticity implies that its gamma4 coefficient divided by h^3 tends to -27/32. There exists epsilon>0 such that the coefficient is nonzero for every 0<|h|<epsilon. In particular it fails throughout the sufficiently-large positive-kappa part of this actual stationary branch. No numerical epsilon, global branch exhaustion or continuation from that neighborhood to either kappa1 root is claimed.

The simpler proposed identity D(S)=D(K)=D(N)=0 does **not** hold: D(K) has 47 nonzero columns and D(N) 1486 nonzero symmetric input pairs out of 1770. The first two branch cancellations are genuine and insufficient. The third coefficient is independently recomputed from the published sparse polynomial data.

This does not reopen the already-owned convergence theorem or stationary certificates. Their validity is what makes the conservation counterexample decisive for the candidate implication.

## 5. Literal observation does not commute with conservation

On the actual constant-base observation section, the normal one-form legs pull back to zero and the horizontal coframe is constant. Keep **every ambient Clifford/endomorphism component** of the horizontal T_h. The restricted connection is A_obs=s_g^*Ahat on the ambient adjoint bundle; it is not replaced with an intrinsic 4D spin connection. Although the flat base Christoffels vanish, its inherited spin coefficients beta_h generally do not.

The actual observed one-form coderivative is

    O(T):=delta_Aobs(s_g^*T)
      =-sum_(h=0..3)(1/d_h)[beta_h,T_h].                    (5)

The self-commutators again vanish. There is no ambient normal form-connection term in the four-dimensional form derivative. The exact geometry has beta_n=0 for every normal direction and

    sum_i (1/d_i)Lambda[i][i][j] = -delta_(j4)/4.

It follows for every invariant one-form in this homogeneous construction, independently of the59-dimensional restriction, that

    O(T)-D(T)=T4/4.                                        (6)

Thus simultaneous ambient and observed coderivative conservation requires the normal trace component T4=0. This is a typed observation-descent condition, not an integer-count or physical-chirality statement.

On the owned59 family, O has rank11 and kernel dimension48. The root values in the table are certified nonzero. On the analytic branch,

    O(T(h))=(21/16)h gamma4+O(h^2),                         (7)

so observed conservation also fails throughout a sufficiently small punctured neighborhood. As independent non-descent controls, Phi1 has ambient divergence zero but observed divergence gamma4/4, while i theta4 I has ambient divergence -iI/4 and observed divergence zero.

Neither D nor O is an Einstein stress-tensor divergence. SC-COS-50's physical analogy still requires an action-owned map to the observed rank-two tensor and its differential identity. This calculation does not replace that bridge by a shared word, nor does it introduce a gamma-trace projection or a compact-group truncation.

## 6. What this changes and what remains

The old conditional C3 proposition is not promoted or regraded. The corresponding conservation implication is tested on the newly constructed action and fails at the declared stationary witnesses; the old source-level missing premise remains unresolved. This does not separately identify which off-shell Noether or Euler-sector premise would have to change. Gauge covariance, compensator redundancy, an Euler current in a different action, and a vanishing leading-order divergence do not restore the failed implication.

The fixed candidate cannot use its known stationary branch/roots as evidence that this reconstructed dark-energy one-form is automatically conserved. To recover that interpretation, a source-supported change of action, identification, differential identity or admitted solution class would have to do substantive work. None is chosen or counted as a successful repair here.

Other stationary solutions and source-compatible constructions are not classified by this wave. Failure of the ordinary coderivative is not failure of every possible source differential identity. No scalar potential, CMB comparison or DESI prediction follows. The previously held EXP/COS comparator results remain unchanged and still lack their full transfer/likelihood and native one-form bridges.

The scientific continuation is a bounded source-class discriminator: determine whether the actual source's alternative identity, rather than the reconstructed C3 condition, is selected strongly enough to be tested on this same action. Do not continue adding cosmological fits or action variants under an unproved identification. Ordinary eligible research continues; no new stopping or approval rule is created.

## Verification

The exact native probe reconstructs the one-form maps, checks their complete invariant-family ranks/kernels and controls, propagates both rational stationary-root certificates, tests the whole homogeneous Euler composition and computes the first nonzero analytic-branch coefficient. Previously proved convergence and full stationary scope remain separately reviewed inputs.

Five targeted Lean lemmas cover symmetric self-commutator contraction, affine-connection cancellation, interval separation, the conditional stationary-kernel implication, and persistence of a separated leading power. They do not formalize the full native geometry, analytic existence or source dictionary. Two independent specialists and a hostile reviewer inspect the concrete result; internal agent review is not external peer review.

[Evidence](../../lab/process/source-action-theta-divergence.json) · [Exact certificate](../../lab/process/source-action-theta-divergence-certificates.json) · [Review](../../lab/process/hostile-reviews/2026-11-27-source-action-theta-divergence-review.md).

```sh
python3 tests/program-focus/source_action_theta_divergence_probe.py --verify
```

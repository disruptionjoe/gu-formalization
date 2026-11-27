---
title: Local off-shell conserved readouts carry no compact excitation charge
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Decide whether higher-derivative readouts surviving conservation descent can carry nonzero compact excitation energy.
actual_delta: Finite-order local off-shell conserved readouts have zero background-subtracted compact charge. Nonnegative smooth charge density consequently vanishes on compactly realizable jets, and on every jet in the admitted full-domain case.
class_covered: Fixed backgrounds on an open finite time/spatial product patch; smooth finite-order observed-only local readouts; off-shell conservation on the full vector-bundle field domain or an explicitly cutoff-closed domain; compact support away from patch boundaries. Stress-to-current passage additionally requires flat translations or a specified Killing field and symmetric stress.
premises:
- explorations/conditional-build/bet-cosmology-conservation-descent-2026-11-27.md
- lab/sources/source-claim-register.yaml#SC-COS-50
- lab/sources/source-claim-register.yaml#SC-COS-51
- lab/sources/source-claim-register.yaml#SC-COS-52
source_bridge:
  status: conditional
  reason: The source asserts an automatic dark-energy identity and an adjoint-one-form replacement, but does not select coderivative conservation alone, an observed-only local stress readout, a cutoff-closed physical domain or a nonzero compact excitation charge. This is a declared implication-class result, not a full-source verdict.
kill_condition: Nonzero background-subtracted compact charge is incompatible with the stated finite-order locality, off-shell conservation and cutoff closure. A counterexample retaining all hypotheses invalidates the theorem; a changed domain or equation is outside it.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-LOCAL-CONSERVATION-TO-COMPACT-EXCITATION-ENERGY
internal_target_verdict: Nonzero compact excitation charge excluded in the declared local off-shell class; no physical or source-wide exclusion.
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# Local conservation identities and compact excitation charges

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Resolve the compact-charge content of higher-derivative local readouts left open by conservation descent.
actual_delta: Background-subtracted conserved charges vanish on every cutoff-admissible compact slice jet; nonnegative smooth charge density vanishes on every such jet.
```

## Result first

**A local stress tensor can be nonzero and identically conserved while carrying no compact excitation energy.** If ambient coclosure alone conserves a finite-order observed-only readout on unrestricted local germs, the conservation law is already an off-shell identity. After subtracting its zero-field background, a compact perturbation can be turned off in time without violating that identity. Conservation then forces its initial charge to be zero.

This does not forbid on-shell positive energy: turning a field off in time generally violates its equations of motion. Nor does zero integrated charge imply zero local stress. A further nonnegativity assumption forces the corresponding smooth charge density to vanish.

| State | Scope |
|---|---|
| **ESTABLISHED by the written proof** | The normal-flux implication rederived below; zero compact excitation charge; the nonnegative-density corollary. Acceptance and execution receipts are recorded separately. |
| **RULED OUT** | Nonzero background-subtracted compact charge carried by a finite-order observed-only readout in the stated off-shell, cutoff-closed class. |
| **NOT MODELED / UNDETERMINED** | Actual PDE-restricted states, sectors failing cutoff closure, homogeneous/noncompact backgrounds, nonlocal or normal-jet readouts, a source-selected stress or physical energy, and GU falsification. |

```gu-typed-objects
result: compact-charge obstruction for local off-shell conserved observed readouts
carrier: coefficient-bundle-valued ambient one-form and literal observed one-form; real current or symmetric stress readout LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=N/A
pairing: fixed divergence density and observed current flux; positive slice measure for the stated nonnegativity corollary ON=declared_local_current
real_structure: real coefficient bundle and connection; complex version componentwise, with nonnegativity only for real charge density
grading: exterior degrees only; no physical chirality or generation count
action_owner: repository-construction of a conservation-equation comparison only; no action or stationary system constructed
target: background-subtracted local current and compact slice charge MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** The source adjoint one-form is not a scalar quintessence field or a stress tensor by definition. This tests a typed readout class. Full-U/optional-Sp, K77/K95, literal observation and physical admission remain distinct. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Lane-B rederivation of the local implication

The [conservation-descent report](bet-cosmology-conservation-descent-2026-11-27.md) was attached to BET-COSMOLOGY. Its needed implication is rederived here before the new quantified result. No lane-C result is automatically promoted to a matrix decision.

Let a nondegenerate observed section S lie in a smooth pseudo-Riemannian (Y,G), with positive codimension. Fix a finite-rank real coefficient bundle E, smooth connection A and smooth positive scalar weight rho independent of the unknown one-form theta. Put beta=i*theta, retaining the coefficient fibre, and mu=rho sqrt(|det G|). The ambient equation is

    delta_A^rho theta
      = -mu^-1 [partial_i(mu G^ij theta_j)+A_i(mu G^ij theta_j)] = 0.

A non-null normal direction exists locally. Extend S to a nondegenerate hypersurface H with that normal and use a Gaussian collar (r,z):

    G=epsilon dr^2+G_ab(r,z) dz^a dz^b,  G^ra=0,  epsilon=+1 or -1.

Extend an arbitrary observed beta to smooth tangential components theta_a. Their raised components u^a=G^ab theta_b are known. For w=mu epsilon theta_r the ambient equation becomes

    partial_r w+A_r w
      = -sum_a [partial_a(mu u^a)+A_a(mu u^a)].                  (1)

This is a finite-dimensional linear ODE in r with smooth parameters z. Arbitrary smooth initial w, including zero, gives a local smooth solution without changing beta. Thus every smooth observed germ is the literal trace of a local ambient-coclosed germ. The neighborhood may depend on the data; this proves neither a uniform tube nor a global ambient lift or physical-domain estimate.

Suppose a smooth finite-order observed-only stress rule

    T[beta](x)=F(x,j^k beta(x))

is conserved for every such lift. Local surjectivity implies that its divergence vanishes for every observed beta in the admitted germ domain. It is an **off-shell differential identity**, for the entire readout class, not a new equation restricting beta. The same reasoning applies directly to current readouts.

For adjoint coefficients the owned affine cancellation also holds:

    delta_(B+s theta)^rho theta-delta_B^rho theta
      = -s G^ij[theta_i,theta_j]=0.

B and the smooth scalar s are fixed; no derivative of s enters this connection difference. General field-dependent weights or other field-dependent connections are not covered.

## 2. Field domain and support

Work on P=I times U, where I is a finite open time interval and U is an open spatial coordinate patch. All backgrounds are fixed and smooth. Supports below are compact inside a smaller slab in P, away from every patch boundary.

The **full-domain version** admits all smooth sections beta of the observed vector bundle and defines the readout on its full finite jet bundle. Zero is admitted. Bumps in local trivializations realize every finite jet at an interior point.

A **restricted-domain version** is possible only when zero is admitted and the domain is explicitly closed under the compact extension in section3. It applies only to slice jets with such an admitted extension. Openness alone does not imply this property: restrictions on values or derivatives and topological sectors may prevent it. No arbitrary-jet conclusion is claimed for that version.

Define the background and excitation stress by

    T0(x)=T[0](x),    J[beta](x)=T[beta](x)-T0(x).              (2)

Both terms are conserved by the off-shell identity. T0 may be nonzero and position-dependent. It is not removed from the underlying theory; only the excitation charge is at issue.

Finite-order locality supplies the support fact: wherever beta vanishes on a neighborhood, its finite jet equals the zero-field jet, so J vanishes there. Compact beta therefore gives compact J even with position-dependent readout coefficients. The raw background stress need not be integrable.

## 3. Compact-charge theorem

Use a real background-subtracted vector current j[beta] of finite order k, with the support property just stated. Suppose for every admitted beta it obeys

    partial_t(nu j^t)+sum_a partial_a(nu j^a)=0,               (3)

where nu(t,x)>0 is a fixed smooth density. Its slice charge is

    Q_beta(t)=integral_U nu(t,x) j^t[beta](t,x) d^d x.         (4)

**Theorem.** For t0 interior to I, every compact slice k-jet having an admitted compact extension has Q_beta(t0)=0.

**Proof.** Compatible compact slice jets can be represented in a bundle trivialization by smooth compact temporal Taylor coefficients b_0(x),...,b_k(x). Choose chi(t) compactly supported inside I and identically1 near t0. The field

    beta_tilde(t,x)=chi(t) sum_(r=0)^k ((t-t0)^r/r!) b_r(x)    (5)

has the prescribed full k-jet along t0, including spatial derivatives of the coefficients. Bundle-local constructions and a finite partition of unity suffice on compact supports; no natural or physical extension law is asserted. Equivalently, an existing slice germ with uniform compact spatial support can be extended with a time cutoff. In a restricted domain, admissibility of this construction is the explicit additional premise.

The current agrees with the prescribed one at t0 by finite order. Let t1 be a later interior time after the support of chi. The current vanishes near t1 and outside a fixed compact spatial K contained in U. Choose a smooth compact spatial region Omega inside U containing K in its interior. Integrating (3) over the slab yields

    0=Q_beta_tilde(t1)-Q_beta_tilde(t0)+side_flux
     =-Q_beta(t0).                                         (6)

The final charge and side flux vanish by locality and support. This is Stokes on the compact slab (allowing its corners), or directly coordinate integration of (3). No global ambient theta is needed: section1 already gave a local identity at every point. **End of proof.**

The argument uses an arbitrarily short interior time slab, not a complete evolution or a limit at infinity. It does not classify superpotentials; locality, conservation and cutoff closure alone give the result.

## 4. Stress, Killing contraction and nonnegative density

On flat observed space, a translation contraction of a conserved stress gives a current of the form (3). On a curved observed patch, require J symmetric and fix an actual Killing field K. Then

    j^mu=J^mu_nu K^nu,
    nabla_mu j^mu
      =(nabla_mu J^mu_nu)K^nu+J^(mu nu) nabla_(mu K_nu)=0.    (7)

Use nu=sqrt(|det g|). No Killing field is claimed for an arbitrary background. Covariant stress conservation by itself does not supply a conserved coordinate energy on a general time-dependent geometry.

For an energy interpretation choose an actual spacelike slice, timelike Killing/translation generator and consistent flux orientation. Let e[beta] be its real background-subtracted energy density relative to a positive smooth slice measure. This interpretation is extra data, not a consequence of an indefinite ambient pairing.

**Corollary.** If e[beta] is nonnegative everywhere for every admitted compact test, it is zero pointwise for every such test. Its integral is zero by the theorem. A strictly positive value would, by smoothness and positive measure, give a positive integral over a neighborhood.

On the full vector-bundle jet domain, any finite jet at an interior point is realized by a local Taylor polynomial times a bump equal to1 near that point, with zero extension outside a compact chart. Hence the local function defining e vanishes on the entire jet fibre. On a restricted domain the conclusion covers only compactly realizable jets. It does not cross disconnected sectors or assume that an arbitrary cutoff preserves derivative constraints.

This concerns the chosen charge density, not every component of J. **Zero energy is not zero local stress.**

## 5. Controls and escape boundaries

In flat1+1 coordinates with eta=(-,+), the improvement

    T_mu nu=(partial_mu partial_nu-eta_mu nu box) f(beta)

has T00=f_xx, T01=f_tx and T11=f_tt. Commuting derivatives gives conservation without an equation for beta. For smooth compact f, integral T00 dx=0 although the stress can be nonzero. A nonzero energy density on a slice must then take both signs. This is the prior report's differential positive control, now with its charge evaluated. Boundary-vanishing polynomial fixtures calibrate these derivative and integral identities; they do not replace the smooth theorem.

Conversely, a conventional real massless scalar right-moving wave phi=h(x-t), with compact smooth nonconstant h, has positive finite energy on each slice. Its stress conservation holds on wave-equation solutions. A time cutoff produces nonzero wave-equation terms and leaves that domain. This is a valid outside-class control, not a GU scalar replacement or a counterexample.

Connected field values alone do not suffice. An S1-valued field in1+1 dimensions can carry an identically conserved winding current from its angular one-form. A nonzero winding profile, constant outside a compact spatial interval, cannot be deformed to the vacuum through admissible compactly supported S1 histories. Its charge is outside the theorem because the required cutoff/homotopy is unavailable. This illustrates why the full linear field domain or actual cutoff admissibility is a hypothesis, rather than a consequence of connectedness.

Limits remain explicit:

- Actual PDE, physical constraints and boundary/topological sectors can prevent the extension. They require their own admission and conservation proofs.
- Homogeneous/noncompact configurations, boundary charges and the unsubtracted T0 are outside the compact-excitation conclusion. Subtracting a cosmological background does not falsify it.
- Normal-jet, nonlocal and integral readouts need not have the observed-only support property.
- The metric and other backgrounds are held; allowing them to vary changes the problem. No W2 or full source solution space is identified with these arbitrary test fields.
- Complex charges vanish componentwise. Nonnegativity requires a real density and its actual positive measure.

## 6. Source relevance, prior work and decision

**SC-COS-50 ASSERTS** the variable dark-energy/automatic-identity claim, with the conditional continuing-DESI framing: TOE2025 at02:14:44, transcript lines578–582. **SC-COS-51 ASSERTS** the adjoint-one-form replacement at02:22:20, lines608–610; its spoken-formula transcription caveat remains. **SC-COS-52 ASSERTS** the formula claim in the UCSD2025 seminar at00:02:05, `papers/drafts/Transcript into the impossible.md:17`, not the interview. Custody remains with the [source register](../../lab/sources/source-claim-register.yaml) and [primary pack](../../lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md).

These assertions do not select ambient coclosure alone, a stress readout, cutoff closure or a nonzero compact charge. The source bridge is **conditional**. This result rules out a proposed local conservation-import route to nonzero compact excitation energy, not the source cosmology claim. Searching another derivative improvement cannot repair that bridge under the same premises. No action, physical selector, choice family, prediction, matrix verdict or physics-ledger verdict is added.

The prior conservation-descent report owns the local ODE argument and nonzero differential control. This artifact gives an explicit lane-B rederivation and the compact-charge consequence. [K1883](k1883-compact-support-observation-range-2026-10-21.md) and [K1886](k1886-support-bounded-observation-approximation-2026-10-21.md) instead study compact range and charges for a particular conservative observation operator; their PDE-restricted charges neither prove nor contradict this arbitrary-readout theorem.

Standard mathematical inputs, with no world-novelty claim:

- Brian Conrad's [Stokes notes](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokesthm.pdf) explain the compactly supported differential-form formulation without a positive-definite metric prerequisite. Equation(6) also follows directly from coordinate integration of the displayed divergence law.
- Francois Gieres, [Improvement of a conserved current density versus adding a total derivative to a Lagrangian density](https://arxiv.org/abs/2205.01459),2022, discusses why superpotential improvements preserve charges with appropriate boundary behavior. This is prior background, not an assumed classification of every readout here.
- The inherited conservation-descent report cites the standard smooth parameter-dependent linear-ODE input for (1); the actual implication is restated above rather than inferred from finite samples.

## 7. Verification limits

`Lean/GUFormalization/CompactCharge.lean` checks only two finite cores: cancellation in a supplied initial/final/side-flux balance, and a finite nonnegative zero-sum list vanishing termwise. It does not formalize the ODE, cutoff construction, support, Stokes, Killing identity, continuum positivity, arbitrary-jet realization or source applicability.

Fresh exact calibration passed29 grouped rational-polynomial checks: derivative/integral arithmetic controls, four nonzero improvement currents with zero charge, both signs of an improvement density, an on-shell compact wave with positive charge131072/45045, and its inadmissible time cutoff. Both finite Lean cores compiled without errors or sorry. Independent review receipts and exact artifact hashes are recorded in [evidence](../../lab/process/compact-excitation-charge.json) and [review](../../lab/process/hostile-reviews/2026-11-27-compact-charge-review.md). The continuum statements are the written proofs in sections1–4; finite checks calibrate signs and boundaries rather than replace those proofs. Internal review is not external-expert verification or publication.

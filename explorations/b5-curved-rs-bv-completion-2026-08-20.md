---
title: "B5 curved Rarita--Schwinger BV completion: Einstein-tensor defect and exact Einstein-background closure"
status: active_research
doc_type: exact_curved_action_completion
created: "2026-08-20"
registry: lab/process/b5-curved-rs-bv-completion.json
probes:
  - tests/channel-swings/b5_curved_rs_bv_completion_probe.py
grade: "ON THE ACTUAL COMPLEXIFIED (9,5) B5 SPINOR/VECTOR-SPINOR CARRIER, THE COVARIANT TRIPLE-CLIFFORD RARITA--SCHWINGER GAUGE DEFECT IS EXACTLY ONE-HALF THE EINSTEIN TENSOR ACTING BY CLIFFORD MULTIPLICATION. THE MASSLESS BV/NOETHER COMPLEX THEREFORE CLOSES ON EVERY RICCI-FLAT SPIN BACKGROUND, INCLUDING NONFLAT WEYL CURVATURE. THE MINIMAL NATURAL LOWER-ORDER DEFORMATION CLOSES ON EINSTEIN BACKGROUNDS WHEN M=-(D-2)ALPHA AND ALPHA^2=-KAPPA/4. THIS IS LOCAL FORMAL COMPACT-CORE CLOSURE, NOT NULL EXACTNESS, GLOBAL COHOMOLOGY, A DOMAIN, A SOURCE-ATTESTED ACTION OR A PHYSICAL QUOTIENT."
target_verdict: B5_CURVED_RS_BV_COMPLETION_EXISTS_ON_EINSTEIN_BACKGROUNDS
target_claim: internal target B5-CURVED-RS-BV-COMPLETION; verdict action-owned curved Noether complex constructed on Ricci-flat and minimally deformed Einstein background classes
canon_verdict_change: none
---

# B5 curved Rarita--Schwinger BV completion

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the standard action-owned covariantization of the
strict native B5 Rarita--Schwinger complex on the actual complexified `(9,5)`
spinor/vector-spinor carrier. It uses a metric/Clifford-compatible spin
connection and proves local formal compact-core Noether closure on stated
Einstein background classes. It is not Weinstein's unreleased cyclic
two-connection complex, the current graph-mixing Stage-B Hessian, a selected
GU source background, a global complex, or a physical state space.

```gu-typed-objects
result: the strict B5 Rarita--Schwinger BV/Noether complex has exact curved closure on Ricci-flat backgrounds and a unique minimal natural lower-order closure on Einstein backgrounds
carrier: U0=S rank128, U1=T*Y tensor S rank1792, U2=density dual rank1792, U3=S density dual rank128 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: program-native (9,5) invariant spinor Krein form and induced metric tensor Krein form ON=independent-B5-full20-carrier
real_structure: complexified (9,5) Clifford carrier with local pseudo-Riemannian spin connection; absolute coflip and global real-domain realization remain UNTYPED
grading: linear abelian BV ghost/field/antifield/Noether grading at local formal compact-core curved grade
action_owner: repository-construction quadratic Rarita--Schwinger action; historical source-preferred nonlinear action remains unowned
target: curved master/Noether identities and minimal Einstein-background completion MAP-TYPE=homomorphism
```

## Result first

Let `Y` be a fourteen-dimensional pseudo-Riemannian spin background of
signature `(9,5)`, with a metric/Clifford-compatible connection. On the strict
carrier define

```text
(A_nabla epsilon)_mu = nabla_mu epsilon,
(K_nabla psi)^mu    = gamma^{mu nu rho} nabla_nu psi_rho.
```

Antisymmetry of `gamma^{mu nu rho}` converts the left Noether composition to
a spin-curvature commutator:

```text
(K_nabla A_nabla epsilon)^mu
  = (1/2) gamma^{mu nu rho} [nabla_nu,nabla_rho] epsilon
  = (1/8) gamma^{mu nu rho} R_{nu rho ab} gamma^{ab} epsilon.
```

The algebraic Bianchi identity and exact Clifford reduction give

```text
K_nabla A_nabla = (1/2) G^mu{}_nu gamma^nu,
```

where `G=Ric-(Scal/2)g` is the Einstein tensor. This is the complete
massless curvature defect: the Weyl tensor cancels identically. The formal
density-dual composition vanishes on the same background because it is the
adjoint Noether identity of the quadratic Euler Hessian.

In dimension greater than two, `G=0` is equivalent to `Ric=0`. Hence the
undeformed curved complex closes on every Ricci-flat spin background, not
only flat space. The exact certificate includes a nonzero algebraic Weyl
fixture with zero Ricci tensor and obtains zero defect in all fourteen output
slots.

## Minimal Einstein-background deformation

The natural two-parameter lower-order ansatz is

```text
(A_alpha epsilon)_mu = nabla_mu epsilon + alpha gamma_mu epsilon,
(K_m psi)^mu = gamma^{mu nu rho} nabla_nu psi_rho
               + m gamma^{mu nu} psi_nu.
```

The two exact Clifford contractions are

```text
gamma^{mu nu rho} gamma_rho = (d-2) gamma^{mu nu},
gamma^{mu nu} gamma_nu      = (d-1) gamma^mu.
```

First-order cancellation therefore forces

```text
m = -(d-2) alpha.
```

For an Einstein background `Ric=lambda g`, write
`kappa=lambda/(d-1)`. The remaining zero-order term vanishes precisely when

```text
alpha^2 = -kappa/4 = -lambda/[4(d-1)].
```

At `d=14`, an exact rational control takes `alpha=1`, `m=-12`, and
`kappa=-4`. Adding the nonzero Ricci-flat Weyl fixture leaves closure intact.
Within this minimal natural ansatz and nonzero `alpha`, the first- and
zero-order equations fix `m` and the Einstein curvature relation; a wrong
mass or wrong curvature is detected by separate planted controls. The
massless Ricci-flat branch is the `alpha=m=kappa=0` specialization.

The relation is algebraic over the complexified carrier. Choosing a real
form, reality convention and global Einstein background is a later owner;
this result does not silently call the deformation physical AdS supergravity.

## Relation to the W177 obstruction

The prior full-20 curvature packet found a live, full-column-rank physical
`R` curvature defect at the W177 seeded metric and already fenced W177 as a
nonstationary discriminator rather than a vacuum. The present calculation
does not fit a compensator to W177. It classifies the strict triple-Clifford
branch instead: massless closure requires Ricci flatness, while the minimal
lower-order branch requires an Einstein background with its curvature tied to
`alpha`. W177 remains an adverse background for the prior ansatz and supplies
no action/source selection of the Einstein branch.

## Preflight, route choice and controls

Mechanism-level retrieval covered the native principal lift, the full-20
curvature remainders, W177 convention correction, coarse BV bridge, Euler
separation and five-field packet. None had reduced the new strict
triple-Clifford covariant defect to the Einstein tensor or certified the
minimal Einstein deformation on the actual `(9,5)` Clifford algebra.

The route council compared spin-geometric curvature identities,
Rarita--Schwinger gauge theory, abstract BV duality, dense connection-matrix
evaluation, W177-specific fitting, source-action custody and hostile scope
review. Exact Bianchi/Clifford reduction dominated because it determines the
complete background condition and exposes Weyl cancellation without fitting
the seeded control. Computation is the final symbolic certificate.

The probe passes `33/33` exact checks. It verifies the two dimension-dependent
Clifford contractions in positive and negative directions, the Einstein-
tensor identity in every output slot for a generic rational algebraic
curvature, a nonzero Ricci-flat Weyl positive control, the Einstein-plus-Weyl
completion, and wrong-mass, wrong-curvature and non-Einstein adverse plants.

## Boundaries and continuation

The curvature obstruction is closed for the standard action-owned strict
branch: curved Noether/BV closure exists on the stated background classes.
This does not repair the null-symbol nongauge kernel from the principal lift,
prove exactness of the curved complex, select an Einstein/source background,
construct a global cohomology or domain, identify the historical
source-preferred Shiab, or transfer the result to the current graph-mixing
Stage-B family.

Strict field (iii) is now `ANTI-PRINCIPAL-SYMBOL / ACTION-CLOSED-EINSTEIN` at
the declared local curved grade. The separate current full-nine Euler family
remains `EXTERNAL-VIA-GRAM`, and the five-field packet stays fail-closed.

The exact next owner is `B5-COFLIP-GREEN-TRANSPORT-ON-CURVED-COMPLEX`: transport
the already relative coflip and formal Green packet through this assembled
curved action, determine what descends without inventing an absolute phase,
and freeze the boundary trace form needed before any common-domain claim.

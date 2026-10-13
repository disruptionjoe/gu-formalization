---
title: "K1716--K1720 nonlinear circle-observation quotient closure"
status: active_research
doc_type: conditional_research_result
created: "2026-10-12"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
direction: observed_to_native
target_claim: SC-META-53
claim_effect: none
---

# K1716--K1720 nonlinear circle-observation quotient closure

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`. This packet composes the exact
K1711--K1712 kernel of one repository-selected compact-circle action with an
already formalized elementary group-action quotient theorem. It does not prove
a new general orbit theorem, identify source hypercharge, construct the
source's observation map, or select a physical quotient.

Scope: the K1356 original circle `C`, its half-period
`z=C(pi)=[-1,1]`, the exact target kernel
`H={1,z}=ker(C->U(H_ps))`, and arbitrary source `C`-sets `X` equipped with a
declared original-circle-equivariant observation into `H_ps=L2(K/M)` or a
target assembled from factors on which `z` acts trivially.

```gu-typed-objects
result: exact half-period-orbit factorization and noninjectivity theorem for deterministic nonlinear, joint-product and randomized original-circle-equivariant observations
carrier: arbitrary source C-set X, quotient X/{1,z}, target H_ps=L2(K/M), indexed products of z-trivial targets and probability laws on z-trivial outcome carriers LAYER=observed BRIDGE=compact-circle-observation CHIRALITY=N/A
pairing: none required for the set-level theorem; probability-valued extension uses pushforward of outcome laws ON=repository_owned_control
real_structure: none required beyond the declared C-actions; no physical Hilbert real form is selected
grading: original-circle action with order-two half-period z and effective quotient C_eff=C/{1,z}; no physical family or chirality grading
action_owner: repository-construction -- no source-selected circle, quotient, kinetic coefficient, observation, state, measure, common domain or physical output law
target: whether nonlinear, accumulated or randomized equivariant observation can distinguish x from z.x when z acts trivially on every target component MAP-TYPE=quotient
```

## Preflight bookend and route choice

K1711 proves `z` acts identically on the complete target carrier, and K1712
proves `{1,z}` is its exact original-circle kernel. K1713 used weight spaces to
exclude injective *linear* primitive intertwiners. It explicitly left nonlinear
or nonlocal observation open.

Mechanism retrieval found the general mathematical step already held in
`Lean/GUFormalization/GroupActionFixedPoints.lean`:
`equivariantMapEquivOrbitValuation_of_trivial` identifies equivariant maps into
a trivially acted codomain with functions on the domain orbit quotient, and
`equivariantMapEquivPi` identifies product-valued equivariant maps with their
component family. The present work therefore does not rederive or claim
novelty for that group-action fact. It restricts the original circle to the
subgroup `H=<z>` and composes the held theorem with the newly established
K1711 target kernel.

This structural route dominates polynomial expansion, K-type enumeration and
regularity estimates because the core identity uses only equivariance. A
finite `C4` control checks the composition and quotient typing. Measurement
closure then checks indexed products and pushforward probability laws so that
adding observables or private randomness is not mistaken for a reopener.

## K1716: arbitrary equivariant maps are half-period blind

Let `X` be any `C`-set and let

```text
F:X -> H_ps
```

be a `C`-equivariant set map. No vector-space, linear, continuous, measurable,
differentiable, local or polynomial structure is assumed. For every `x in X`,
equivariance and K1711 give

```text
F(z.x)=z.F(x)=F(x).                                  (1)
```

Thus `F` is constant on every orbit of `H={1,z}`. Nonlinearity cannot repair
the lost sign while the same original-circle equivariance and target action
are retained. This is stronger than K1713 in map class but narrower in its
input: it assumes the source action and observation are actually typed as the
same `C`-equivariant problem.

Equation (1) is also the complete proof. The Lean orbit theorem supplies the
formal reusable classification after restricting from `C` to `H`; K1711
supplies the previously missing fact that the `H` action on this specific
target is trivial.

## K1717: exact effective-quotient factorization

Write

```text
pi_X:X -> X/H,            H={1,z}.
```

Because of (1), there is a unique set map

```text
F_bar:X/H -> H_ps
```

such that `F=F_bar o pi_X`. Existence follows by assigning an orbit the common
value of `F`; independence of representative is (1), and uniqueness follows
from surjectivity of `pi_X`.

The circle is abelian, so `H` is normal. Therefore `C/H=C_eff` acts on `X/H`.
The K1712 action on `H_ps` also factors through `C_eff`, and direct substitution
shows

```text
F_bar([c.x])=c.F_bar([x]).                            (2)
```

Hence `F_bar` is `C_eff`-equivariant. If `X` is a topological `C`-space and
`F` is continuous, the same factor is continuous for the quotient topology by
the defining universal property. This adds no Hausdorff, manifold, smooth or
closed-domain claim.

The factorization is through the *source orbit quotient*. It is not an
automorphism of the original circle and does not prove that the source action
or a physical reduction selects `X/H`.

## K1718: faithful source actions force noninjectivity

Suppose the `C` action on `X` is faithful. Since `z` is a nonidentity element
of `C`, faithfulness implies that its transformation on `X` is not the
identity. Thus some `x` satisfies

```text
z.x != x.
```

Equation (1) then gives a collision between distinct source points:

```text
F(z.x)=F(x).
```

No original-circle-equivariant map from a faithful source `C`-set into
`H_ps` can be injective. The conclusion covers arbitrary set maps and removes
K1713's linearity and primitive-weight hypotheses. It does not cover a
nonfaithful source whose kernel already contains `z`, a different compact
circle, or a target on which `z` acts nontrivially.

The exact reopener is now typed. At least one of the following must occur:

1. the source is replaced by or physically identified with `X/H`;
2. one output carrier has nontrivial `z` action;
3. the observation breaks original-circle equivariance under a named owner;
4. separately owned `z`-sensitive output data are added.

These are alternatives, not constructions supplied by this packet.

## K1719: products and randomized channels do not restore the bit

### Indexed products

Let `F_i:X->Y_i` be any indexed family of `C`-equivariant maps, with `z`
acting trivially on every `Y_i`. The joint observation satisfies

```text
F_joint(z.x)=(F_i(z.x))_i=(F_i(x))_i=F_joint(x).      (3)
```

This is the direct componentwise consequence of (1), formally aligned with
`equivariantMapEquivPi`. An arbitrary number of same-kernel observables does
not restore injectivity; one component must carry new `z`-sensitive structure.

### Probability-valued observation

Let `Y` be an outcome carrier on which `z` acts trivially, and let

```text
K:X -> Prob(Y)
```

be a `C`-equivariant Markov kernel, where `C` acts on probability laws by
pushforward. Since the pushforward by `z` is the identity on `Prob(Y)`,

```text
K(z.x)=z_*K(x)=K(x).                                 (4)
```

Private randomness and outcome mixing therefore do not restore the lost
`z`-bit. For standard Borel spaces and measurable kernels, (4) remains a
pointwise equality of probability laws; this packet does not construct a
physical measure, instrument, Born rule or interacting state.

## K1720: admission boundary

The typed nonlinear alternative is now classified for this target:

- every deterministic original-circle-equivariant observation is constant on
  source `{1,z}` orbits;
- every such map factors uniquely through `X/{1,z}` and becomes
  `C_eff`-equivariant;
- no such map is injective on a faithful source circle action; and
- indexed products and equivariant randomized channels into same-kernel
  targets remain half-period blind.

This closes nonlinearity, accumulation and private randomness as escapes *when
the declared equivariance and target kernel are unchanged*. It does not close a
different circle, a target with nontrivial `z` action, explicit symmetry
breaking, external `z`-sensitive data or a source-selected physical quotient.

`SC-META-53` remains `UNCERTAIN`; `SC-ACT-01/02/06` retain their source
polarity. `LT-SM1b`, `LT-SM2`, `LT-SM8`, `LT-GR6b`, `RA-F1` and `AC-F1`
retain their ledger verdicts and mapping grades. The source register, standing
ledger, canon, papers, predictions, confirmations and public posture do not
move.

## Postflight hostile review

**Strongest hidden-assumption challenge.** The conclusion applies only when
the source and target really carry the declared original-circle action and
the observation intertwines it. Calling a map “physical observation” does not
establish that hypothesis. A source-owned observation could instead use a
different group, break the symmetry or carry a nontrivial `z` action.

**Strongest contrary construction.** A target with a two-point output on
which `z` swaps the points can distinguish the sign; likewise the effective
source quotient removes the distinction rather than reconstructing it. These
are genuine counterexamples to any broader “no nonlinear observation can ever
work” claim. The durable result is exactly the same-kernel equivariant
factorization.

**Weakest reproducibility seam.** The finite `C4` model checks the subgroup,
quotient, product and probability-pushforward composition, but it is not the
proof of the infinite-dimensional target statement. The mathematical load is
K1711's complete-carrier identity plus elementary equivariance and the held
formal orbit theorem.

**Overclaim fence.** No source action, physical carrier, common domain,
interacting quotient, hypercharge identification, family count, observed
chirality, positive state space or probability law is constructed. The result
is a necessary-condition theorem for one repository-selected circle action.

## Exact next input and reranked frontier

The next gate on this arc is one source/action-owned reopener: select the
effective quotient on a physical source carrier, exhibit a target/output with
nontrivial `z` action, or derive a named symmetry-breaking observation with its
kinetic coefficient, state/domain and faithful physical interpretation. A
different compact circle is the strongest group-theoretic alternative because
the nonlinear same-target route is now closed.

The wider scalar finite-strength envelope remains the strongest independent
mathematical alternative, but still needs a realizable wider-seed
parameterization and uniform remainder or certified finite-strength control.
The corrected K77 observation-symbol diagram retains higher source-to-physics
payoff but still lacks one same-carrier packet containing both differentials
and the nontrivial observation/gauge-parameter maps. The coupled-PDE endpoint
still waits for source-owned current/curvature equations on a common nonlinear
domain.

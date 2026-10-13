---
title: "K1721--K1725 faithful diagonal compact circle on the spherical carrier"
status: active_research
doc_type: conditional_research_result
created: "2026-10-12"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
direction: observed_to_native
target_claim: SC-META-53
claim_effect: none
---

# K1721--K1725 faithful diagonal compact circle on the spherical carrier

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`. This packet tests the explicit
different-circle reopener left by K1720 on the same repository-selected
spherical control. It does not identify source hypercharge, select a physical
global group, or construct a positive interacting quotient.

Scope: `G=Spin_0(7,7)`,
`K=(Spin(7) x Spin(7))/diagonal{plus_or_minus 1}`,
`M=Z_K(A)` for the split Cartan, `H_ps=L2(K/M)`, K1356's one-factor circle
`C`, and the new primitive diagonal circle

```text
D(beta)=[exp((beta/2)e1e2), exp((beta/2)e3e4)],
beta in R/(2 pi Z).
```

```gu-typed-objects
result: exact homogeneous-space action kernel and a faithful primitive diagonal-circle alternative on the same complete spherical carrier
carrier: G=Spin_0(7,7), K=(Spin(7)xSpin(7))/diagonal center, finite M=Z_K(A), K/M and H_ps=L2(K/M) LAYER=ambient BRIDGE=maximal-compact-circle-choice CHIRALITY=N/A
pairing: positive principal-series L2 pairing and the product compact quadratic form normalized by unit one-factor bivectors ON=repository_owned_control
real_structure: unitary complex Hilbert representation with real compact-circle generators
grading: integer D charges with gcd one; no physical family, chirality or hypercharge grading
action_owner: repository-construction -- no source-selected circle, kinetic coefficient, physical domain, state, quotient or observed map
target: whether K1711's half-period blindness persists for every compact circle on the same K/M carrier MAP-TYPE=restriction
```

## Preflight bookend and route choice

K1711--K1712 prove that the one-factor circle `C` has exact kernel
`{1,[-1,1]}` on `H_ps`. K1716--K1719 then show that no nonlinear, joint or
randomized `C`-equivariant observation into the same kernel-trivial target can
restore the missing bit. K1720 leaves a different compact circle as the
strongest internal group-theoretic reopener.

Mechanism retrieval found no earlier packet classifying the primitive
diagonal circle below. A K-type census is dominated by a global homogeneous
space argument: the kernel of the `K` action on `K/M` is the normal core of
`M`; connectedness of `K` and finiteness of `M` identify that core with the
center. One then only has to compute how a proposed circle meets the center.

Compact Lie theory supplies the core argument, Clifford exponentials certify
the global loop, harmonic analysis transports faithfulness to `L2`, and
source/physics routing withholds all physical identification. The fallback was
a Peter--Weyl charge census, but the kernel theorem decides the complete
carrier without enumerating K-types.

## K1721: the complete homogeneous action kernel is the center

For any homogeneous space, the kernel of left translation is

```text
ker(K -> Homeo(K/M)) = core_K(M) = intersection_(k in K) k M k^{-1}.   (1)
```

Here `K` is connected and `M=Z_K(A)` is finite because `G` is split. The core
is therefore a finite normal subgroup of the connected group `K`. Conjugation
of any core element has a connected orbit lying in that finite subgroup, so
the orbit is a point. Hence `core_K(M)` is central.

Conversely every central element of `K` centralizes `A`, hence lies in `M`,
and centrality places it in every conjugate of `M`. Therefore

```text
core_K(M)=Z(K).                                                    (2)
```

Since `Z(Spin(7))={plus_or_minus 1}`, quotienting the product center by its
diagonal subgroup leaves

```text
Z(K)={1,z},                 z=[-1,1].                              (3)
```

The quasi-regular representation on `L2(K/M)` has the same kernel. If a group
element moves a coset, continuity gives an open set whose indicator is moved
in `L2`; equality almost everywhere cannot enlarge the kernel of this compact
homogeneous action. K1711 is recovered as the restriction of (2) to `C`.

## K1722: an explicit primitive diagonal circle misses the center

Let `E=e1e2` in the first `Spin(7)` factor and `F=e3e4` in the second, with
`E^2=F^2=-1`. Define

```text
D(beta)=[exp((beta/2)E), exp((beta/2)F)].                           (4)
```

At `beta+2 pi`, both lifted factors acquire `-1`, so the pair changes by the
diagonal central element and (4) is a well-defined `2 pi`-periodic circle in
`K`. It is primitive and embedded: its class is the identity only when both
lifts are the same scalar sign, which occurs at `beta=0 mod 2 pi`.

A point of `D` can lie in `Z(K)` only when both lifted exponentials are scalar.
On one period this happens only at the two endpoints, and both endpoints
represent the identity after the diagonal quotient. Thus

```text
D intersection Z(K)={1}.                                          (5)
```

In particular `D(pi)` is not central and is not K1711's `z`. The half-period
mechanism that killed the one-factor circle is absent.

## K1723: faithful action and primitive charge lattice

Combining (2) and (5), the kernel of the restricted `D` action on `K/M` is

```text
D intersection core_K(M)=D intersection Z(K)={1}.                  (6)
```

So `D` acts faithfully on both `K/M` and `H_ps=L2(K/M)`. A unitary circle
representation decomposes into integer charge spaces. If the gcd of all
occurring charges were `d>1`, rotation by `2 pi/d` would lie in its kernel.
Faithfulness forces

```text
gcd{q : H_q(D) is nonzero}=1.                                     (7)
```

Therefore at least one odd `D` charge occurs on the complete spherical
carrier. This is an existence consequence of the global action kernel, not an
identification of a particular physical K-type or observed particle charge.

## K1724: genuinely different circle and normalization

Precomposition by either automorphism of `U(1)` (`beta -> plus_or_minus beta`)
preserves the kernel of a circle representation. The `C` action has kernel of
order two while the `D` action is faithful, so no original-circle automorphism
turns one action into the other. The repair is a different embedded circle in
the same `K`, not a relabeling of K1711's action.

With the product compact quadratic form normalized by
`||(E,0)||^2=||(0,F)||^2=1` and orthogonal factors, the primitive generators
satisfy

```text
T_C=(E,0),       ||T_C||^2=1,
T_D=(E/2,F/2),   ||T_D||^2=1/2.                                   (8)
```

Thus the primitive diagonal parameter has a calculable one-half bare norm in
this control convention. Equation (8) does not supply a physical gauge
coupling: a source-owned action must choose the circle, normalization and
kinetic coefficient together before any comparison with hypercharge.

## K1725: admission boundary

The different-circle alternative is now classified on the complete control
carrier:

- the full `K/M` and `L2(K/M)` action kernel is exactly `Z(K)={1,z}`;
- the primitive diagonal circle `D` meets that center trivially;
- `D` therefore acts faithfully and has a gcd-one charge lattice containing
  an odd charge; and
- `D` is not an automorphic relabeling of `C`, and its primitive generator has
  a different bare compact norm.

This proves that K1711's parity obstruction is circle-specific rather than a
property of every compact circle on the same spherical carrier. It also
exhibits the exact internal escape. It does not select `D`, identify it with
source hypercharge, construct the source action, or establish a physical
carrier, common domain, positive interacting quotient or observed map.

`SC-META-53` remains `UNCERTAIN`; `SC-ACT-01/02/06` retain their source
polarity. `LT-SM1b`, `LT-SM2`, `LT-SM8`, `LT-GR6b`, `RA-F1` and `AC-F1`
retain their ledger verdicts and mapping grades. The source register, standing
ledger, canon, papers, predictions, confirmations and public posture do not
move.

## Postflight hostile review

**Strongest hidden-assumption challenge.** The core argument requires `M` to
be finite and `K` connected. Both hold for the maximal compact and split
Cartan in `Spin_0(7,7)`. The proof would not transfer unchanged to a
non-split group with positive-dimensional `M`.

**Strongest global-group challenge.** Writing `(E/2,F/2)` only at Lie-algebra
level is insufficient. The loop closes because its `2 pi` endpoint is
`(-1,-1)`, which is precisely the diagonal center killed in `K`; without that
quotient the same path would not be a `2 pi` loop.

**Strongest contrary construction.** K1711's one-factor circle remains a
valid counterexample to any claim that every circle on `K/M` acts faithfully.
The durable classification is by intersection with `Z(K)`, not “diagonal good,
one-factor bad” as a universal slogan.

**Weakest reproducibility seam.** The producers check the core logic, quotient
endpoint arithmetic, center intersection, charge-gcd implication and norm
ratio. They are exact reporting/algebra controls, not a machine formalization
of the compact Lie group theorem.

**Overclaim fence.** The existence of an odd `D` charge does not locate its
K-type, multiplicity or particle interpretation. No source field is identified
with `H_ps`, and no action selects `C`, `D`, their kinetic coefficient or a
physical observation.

## Exact next input and reranked frontier

The compact-circle comparison is now internally complete: one explicit circle
has an exact order-two kernel and one explicit primitive circle is faithful.
The next gate is source/action ownership that chooses a global circle and its
normalization on one physical carrier/domain, then constructs the faithful
observed map and positive quotient. Further arbitrary circle examples would
not decide that owner question.

The wider finite-strength scalar envelope remains the strongest independent
mathematical alternative, requiring a realizable wider-seed parameterization
and uniform remainder or certified finite-strength control. The corrected K77
observation-symbol diagram retains higher source-to-physics payoff but still
lacks one same-carrier packet containing both differentials and the nontrivial
observation/gauge-parameter maps. The coupled-PDE endpoint still waits for
source-owned current/curvature equations on a common nonlinear domain.

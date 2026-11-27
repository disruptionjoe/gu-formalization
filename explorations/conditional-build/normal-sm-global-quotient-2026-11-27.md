---
title: The constructed normal special-unitary reduction has the global SM quotient
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T2
expected_delta: Resolve the global group and geometric observation descent for the already-constructed fixed-Spin normal reduction.
actual_delta: The lifted compact reduction is globally (SU(3) times SU(2) times U(1))/mu6 and its associated geometric observation map descends; physical selection and fixed-data requirements remain separate.
class_covered: Oriented normal bundles of signature (6,4) with a prescribed Spin lift over paracompact bases of CW homotopy dimension at most seven, a fixed compatible negative U(2) reduction, and free positive complex structure and determinant volume; observation uses the existing simultaneous form-plus-spin action.
premises:
- explorations/conditional-build/normal-special-unitary-existence-2026-11-25.md
- explorations/conditional-build/global-normal-complex-reduction-2026-11-24.md
- explorations/conditional-build/source-weak-action-transport-2026-11-13.md
- lab/sources/source-claim-register.yaml#SC-GRP-03
source_bridge:
  status: conditional
  reason: The source proposes the compact/complex intersection and permits the special-unitary branch; it does not select the complex structure, preserved connection, physical gauge group or observed current.
kill_condition: No scientific kill. Without the inherited fixed-Spin reduction premises this corollary does not decide existence; it does not exclude the source-admitted unitary alternative or a different physical realization.
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# A global geometric quotient, with physical selection still separate

```yaml
program_target: X-P1-P2
tier: T2
expected_delta: Resolve the global group and geometric observation descent for the already-constructed fixed-Spin normal reduction.
actual_delta: The lifted compact reduction is globally (SU(3) times SU(2) times U(1))/mu6 and its associated geometric observation map descends; physical selection and fixed-data requirements remain separate.
```

**Result.** The already-constructed normal special-unitary reduction has compact
group `H ≅ (SU(3) × SU(2) × U(1))/mu6`, globally inside the prescribed normal
Spin bundle. The existing simultaneous geometric form-plus-spin observation
is an associated-bundle map for this group. This closes a geometric condition,
not the selection of a physical gauge group, vacuum or current.

Basis: `8b1fe36a30526e86257d2ef660f8e781560aeac0`.

```gu-typed-objects
result: global normal compact quotient and associated geometric observation descent
carrier: normal real rank10 bundle N=P6+Q4; separately the existing full Dirac S128 on an H4/N10 observation split LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: normal signature6,4 and its compact split; no positive physical Hilbert form ON=normal_bundle
real_structure: prescribed connected Spin(6,4) double cover; complex associated spinors, no K77/K95 identification
grading: none required for group descent; no generation or physical chirality count
action_owner: repository-construction -- corollary of existing bundle and observation results; no action or vacuum selected
target: global group quotient and geometric q covariance MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read
> [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> The normal geometric group is not a conventional Higgs-VEV stabilizer by
> definition. Its quotient does not establish a physical particle spectrum,
> family count, current or coupling normalization. Independent source bars,
> the full-unitary parent and the source's effective2+1 interpretation remain
> unchanged.

## 1. What the source and previous results supply

SC-GRP-03 records the 2021 draft **p29, equation4.6**: the Standard Model group
is proposed inside simultaneous maximal-compact and complex reductions, with
an extra U(1) if SU(3,2) is not privileged over U(3,2). The present corollary
uses that optional special-unitary branch. It neither chooses it nor removes
the unitary alternative.

The [November25 fixed-Spin theorem](normal-special-unitary-existence-2026-11-25.md)
applies to `N=P⊕Q`, of positive rank6 and negative rank4, with component
orientations and a specified Spin(6,4) lift, over a paracompact base B of CW
homotopy dimension at most7. Fix a compatible orthogonal complex structure
J_Q on Q. The positive structure J_P and unit determinant volume are free.
That theorem constructs the compatible reduction of the **specified** Spin
bundle; it does not merely show vanishing characteristic classes.

The compact subgroup used there is

    H0 = {(C,D) in U(3) × U(2) : det C det D = 1}.

Its fundamental-group generator has determinant windings (1,-1). Under
realification its image in `pi1(SO(6)×SO(4))=Z2×Z2` is (1,1), annihilated by
the Spin covering character `(a,b) -> a+b`. Consequently H0 lifts injectively
to a connected subgroup H of Spin(6,4). The full inverse image also contains
`-H`; H is the identity lift, not that entire inverse image. This uses the
covering parity, not the false assertion that SU(3,2) is simply connected.

For completeness, the inherited bundle existence proof reduces the fixed
Spin bundle first to the inverse image K of `SO(6)×U(2)`. The quotient is

    K/H = Spin(6)/SU(3) = SU(4)/SU(3) ≅ S7.

The associated S7 bundle has no section obstruction below degree8. Thus the
stated dimension bound supplies an H reduction of the specified Spin bundle,
extending J_Q. This is reused evidence, not a new obstruction calculation.

## 2. Exact global quotient

Define a group homomorphism

    f: SU(3) × SU(2) × U(1) -> H0,
    f(A,B,z) = (z² A, z⁻³ B).

Its determinant product is `z^6 z^-6=1`. Given `(C,D)` in H0, choose any
sixth root z of det C and set `A=z^-2 C`, `B=z^3 D`. Both determinants are1,
so f is surjective. No continuous global choice of that sixth root is used;
pointwise existence proves surjectivity of the homomorphism.

Its kernel is exactly

    {(z⁻² I3, z³ I2, z) : z⁶=1} ≅ mu6.

These elements are central. The first isomorphism theorem therefore gives

    H ≅ H0 ≅ (SU(3) × SU(2) × U(1))/mu6.              (1)

This is a compact Lie-group isomorphism, not just a Lie-algebra match.
The powers2 and−3 agree with the previously computed central plane weights;
no physical gauge-coupling normalization is inferred from them.

## 3. Geometric observation descends on associated bundles

Use the existing observation split `V=H4⊕N10`, its full complex Dirac module
S, and the source-shaped map

    q(zeta,nu) = (P_H zeta, Gamma_V zeta, nu).

Here H4 denotes the horizontal vector bundle, not the compact group H. The
group H acts trivially on the horizontal vector factor and geometrically on
the normal vector and spinor factors. It acts on a one-form spinor by the
**simultaneous form-plus-spin representation**, not spin-only multiplication
with the normal Clifford tensor frozen. Clifford covariance gives

    Gamma_V(h·zeta) = h·Gamma_V(zeta),
    P_H(h·zeta) = h·P_H(zeta),
    q(h·(zeta,nu)) = h·q(zeta,nu).                      (2)

These are group-level tensor identities, so local expressions patch across
the principal H transition functions. Hence q and its invariant kernel
define associated-bundle maps wherever the existing full observation carrier
is supplied. Restricting that construction to the section preserves (2).
Every representation pulled back along f is trivial on ker f=mu6, so there
is no additional mu6 descent obstruction for these associated bundles.

This reuses [Category G](source-weak-action-transport-2026-11-13.md), now on
the constructed global reduction. It does not claim that a source connection
preserves the reduction, that an arbitrary fixed-spin-only action descends,
or that (2) identifies the independently barred physical readout. No ambient
Spin structure is constructed by relabeling the normal Spin lift.

## 4. Conditions that remain, and evidence-accounting consequence

The [native global reduction result](global-normal-complex-reduction-2026-11-24.md)
still governs existence of J_Q. On the admitted native bases, absolute normal
SU existence is equivalent to the matching almost-complex condition on TX.
For closed spin Lorentz four-bases retain its integral condition
`4a²[X]=3 signature(X)` and orientation qualifications. The earlier positive
existence statement on admitted noncompact/boundary spin bases remains as
proved; no claim that every closed base qualifies is added.

| Additional data held fixed | Remaining requirement |
|---|---|
| Both J_P and J_Q | Integral triviality of their combined determinant, including torsion. |
| J fixed and total Spin prescribed | Compatibility of the induced Spin structure; changing volume phase only realizes the image of `H1(B;Z) -> H1(B;Z2)`. |
| J and volume fixed | Compare their induced Spin lift with the specified one. |
| Connection fixed | Parallel J and preserved volume are additional differential conditions. |
| Boundary/end reduction fixed | A relative extension problem, outside the absolute theorem. |
| Physical gauge group/current | Source realization, admissible fields and the actual observed current remain unproved. |

The lens-space determinant and RP3 Spin-phase countercontrols in the
November25 report remain valid. This result allows changing J_P; it does not
repair every already-fixed J by renormalizing its volume.

RA-A6 in [ledger0.263](../../lab/process/conditional-physics-ledger-v0.263.json)
still combines the global mu6 construction with selected-J descent. Equation(1)
and (2) supply the geometric construction and descent for the reduction just
constructed. They do not fire that row's recorded rank-one `(10bar,1,3)`
V_PSB selection trigger: that conventional selector is neither a premise nor
a consequence of this normal geometric construction. RA-A8's stationary
selection requirement is also not discharged. This report supplies evidence
for separating those conditions; it changes no row verdict or trigger.

The older `tests/anchored-leads/sm_z6_quotient_bridge.py` tests tangent frame
charge and a torsion-to-integer bridge. It does not prove or disprove this
global group/bundle construction and need not be rerun. No charge table,
anomaly arithmetic, generation count or source-selected prediction is added.

## 5. Verification ceiling

The new content is the explicit quotient map and its composition with the
already-proved fixed-Spin reduction and geometric covariance. The written
proof uses no numerical matrix rank or new topology computation. Independent
review, not author self-review, must check this composition. No execution
or physical applicability is certified by this report alone.

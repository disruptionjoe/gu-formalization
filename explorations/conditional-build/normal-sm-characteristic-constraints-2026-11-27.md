---
title: Normal geometric SM bundles have correlated topology and a sharp product-lift criterion
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T1
expected_delta: Determine split Chern classes and the exact direct-product-lift condition for closed spin Lorentz normal reductions.
actual_delta: All optional SU normal reductions obey the split Chern relations; some reduction lifts to the direct product exactly when the base signature is divisible by 48.
class_covered: Smooth closed connected oriented spin Lorentz four-bases, native trace-reversed normal signature (6,4), prescribed normal Spin lift, optional SU(3,2) reduction; absolute section bundles with freely chosen compatible complex structures and volume for the existence assertion.
premises:
- explorations/conditional-build/global-normal-complex-reduction-2026-11-24.md
- explorations/conditional-build/normal-special-unitary-existence-2026-11-25.md
- explorations/conditional-build/normal-sm-global-quotient-2026-11-27.md
- explorations/conditional-build/closed-spin-normal-reduction-2026-11-27.md
- explorations/conditional-build/native-rs-moving-section-index-2026-11-11.md
- lab/sources/source-claim-register.yaml#SC-GRP-03
source_bridge:
  status: conditional
  reason: The source permits the optional normal SU intersection; closedness, a lift to the direct product and the physical gauge-bundle identification are not source-required.
kill_condition: Incompatible Chern data cannot realize this geometric reduction; signature not divisible by 48 forbids its direct-product lift, not the quotient reduction or GU.
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Scoped mathematical exclusion and realizability condition only; no cell, class-C, source or ledger verdict change.
---

# Geometric weak and color bundles cannot have independent topology

```yaml
program_target: X-P1-P2
tier: T1
expected_delta: Determine split Chern classes and the exact direct-product-lift condition for closed spin Lorentz normal reductions.
actual_delta: All optional SU normal reductions obey the split Chern relations; some reduction lifts to the direct product exactly when the base signature is divisible by 48.
```

**Result.** On the declared closed section, every geometric normal
`H=S(U(3)×U(2))` reduction has Chern data fixed as below by `p1(TX)`.
The quotient reduction exists on every base in this class, by the prior theorem.
A reduction that additionally lifts to `SU(3)×SU(2)×U(1)` exists **if and only if
`signature(X)` is divisible by 48**. A specified reduction has the stronger,
integral determinant-root test. This does not require an action or connection.

Basis: `cb77c122924f6615574011bffc99b81193ffe58a`.

```gu-typed-objects
result: split characteristic constraints and product-lift criterion
carrier: N=Sym2(T*X)=P6+Q4 on a closed spin Lorentz observation section; E3_R=P and E2_R=Q LAYER=observed BRIDGE=literal-section-pullback CHIRALITY=N/A
pairing: trace-reversed normal signature6,4, with definite positive and negative factors; integral intersection pairing ON=declared_carrier
real_structure: real normal bundle and prescribed Spin(6,4) lift; optional SU(3,2) complex reduction
grading: positive6/negative4 normal split, not fermionic or physical chirality
action_owner: repository-construction -- geometry and topology only; no action or physical current selected
target: geometric bundle realizability and central-cover lifting MAP-TYPE=not-a-map
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Follow
> [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> These are actual normal associated bundles, not independent conventional
> gauge bundles. Their Chern classes are not by definition physical instanton
> numbers or family indices. K77/K95 ambient real forms, independent bars,
> full-unitary parent and effective 2+1 interpretation remain distinct.

## 1. Source custody and what is already owned

SC-GRP-03, [2021 draft p29, equation4.6 and adjacent text](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf),
proposes simultaneous compact and complex normal reductions and permits the
special-unitary branch; it also retains the larger unitary alternative.
SC-META-50 (TOE2025 00:03:06) names the active spin structure as starting data.
The 2021 opening p4 additionally says "unique spin structure". This theorem
assumes a chosen Spin structure; its closed examples are not asserted to satisfy
that stronger literal uniqueness clause. Neither the cited reduction claim nor
the later active-spin statement requires closed spacetime, a direct-product
lift, or every abstract SM gauge bundle to arise from this normal reduction. Physical identification is
the weakest unproved bridge here. Class-C representativeness remains unproved;
the failed width witnesses are not repaired by this topology result.

The [normal splitting](global-normal-complex-reduction-2026-11-24.md),
[fixed-Spin extension](normal-special-unitary-existence-2026-11-25.md),
[global quotient](normal-sm-global-quotient-2026-11-27.md), and
[closed-spin existence](closed-spin-normal-reduction-2026-11-27.md) are reused.
So is `p1(Sym²T*X)=6p1(TX)`, already proved in the
[November11 moving-section index analysis, §6](native-rs-moving-section-index-2026-11-11.md).
The delta is their composition with the positive/negative split and the exact
extra lift condition. No new general topology theorem or world novelty is claimed.

The global-form distinction is standard; [Tong2017](https://arxiv.org/abs/1705.01853)
explains why quotient choices affect allowed gauge data. That literature does
not derive the native normal-bundle constraints below and does not supply the
physical identification missing here.

## 2. Every compatible reduction obeys the same Chern relations

Let `p=p1(TX)` and `d=c1(E2)`, where E3 and E2 are the rank-three positive
and rank-two negative complex bundles. Determinant trivialization gives
`c1(E3)=-d`. In integral cohomology on X:

    c2(E2)=0,        d²=p,        d mod2=0,
    c2(E3)=-2p,     c2(E3⊕E2)=-3p.                 (1)

**Proof.** The native negative bundle is
`Q=1⊕(L*⊗E*) ≅ L*⊗T*X`, with L the timelike real line and E its
rank-three complement. Its trace line supplies a nowhere-zero section, so
`e(Q)=0` and `c2(E2)=0`. This does not require a time orientation.
On the time-orientation double cover L is trivial and Q has the same p1 as
TX. Transfer makes their difference 2-torsion; `H⁴(X;Z)=Z` removes that
ambiguity. Thus `p1(Q)=p` integrally. The owned normal identity gives
`w2(Q)=w2(TX)=0`. Realification and the coefficient exact sequence give
`p1(Q)=d²-2c2(E2)=d²` and `d=2a` for an integral a, including torsion.

Additivity and the owned symmetric-square formula give `p1(P)=5p`.
Consequently `5p=d²-2c2(E3)=p-2c2(E3)`, hence `c2(E3)=-2p`, since
H⁴ has no 2-torsion. Whitney multiplication then gives total second class
`-2p-d²=-3p`. No division in torsion cohomology on all of Y is assumed.

If `signature(X)=16k`, the signature theorem yields:

| Characteristic number | Value |
|---|---:|
| `d²[X]` | `48k` |
| `c2(E2)[X]` | `0` |
| `c2(E3)[X]` | `-96k` |
| `c2(E3⊕E2)[X]` | `-144k` |

Reversing base orientation reverses these evaluations and signature together.
The Euler zero is insensitive to the orientation of Q. The base complex
structure used in existence proofs is not Lorentz-orthogonal; the normal
negative metric is definite.

## 3. Fixed-reduction lifting versus existence of some lift

The owned covering map is

    f(A,B,z)=(z²A,z⁻³B),     kernel(f)=mu6.          (2)

A specified H bundle lifts to the direct product precisely when there is a
complex line L0 with `L0^6 ≅ det(E3)`. Equivalently,

    c1(E3) in 6H²(X;Z).                            (3)

This is integral, including torsion, not just a condition on characteristic
numbers. Necessity follows from the U(1) factor of a lift. Conversely, with
such a line, `C0=E3⊗L0^-2` and `W0=E2⊗L0^3` have trivial determinants;
choose the compatible determinant trivializations using the H volume. Their
special-unitary frame bundles together with L0 yield the lift. This is a lift
of the specified H bundle, not a change of its global group.

**Existence theorem.** With the complex structures and volume free but the
normal Spin lift prescribed, there exists some product-liftable H reduction
on X if and only if `48 | signature(X)`.

Necessity: put `ell=c1(L0)`. Equations(1)–(3) give
`d=-6ell` and `3 signature=36 ell²[X]`, so signature is divisible by12.
Spin gives divisibility by16. Thus it is divisible by48.

Sufficiency: write `signature=48m`. For m nonzero, the already-proved
closed-spin theorem supplies a hyperbolic pair e,f in the integral
intersection lattice modulo torsion. Take an integral lift
`ell=e+2m f`, so `ell²[X]=4m`; take ell=0 if m=0. Set `d=-6ell`.
Then `d mod2=w2(Q)=0` and
`d²=p1(Q)+2e(Q)`, since both sides evaluate to144m in H⁴(X;Z)=Z.
The rank-four obstruction criterion in the November24 owner §3 applies
**to this chosen integral lift d**: its obstruction satisfies
`4o4=p1(Q)-d²+2e(Q)`, hence vanishes. Thus it realizes a compatible
complex structure on Q with first Chern class d. The fixed-Spin extension
then chooses the positive structure and volume, preserving this negative
structure and the prescribed total Spin lift. Since `c1(E3)=6ell`, (3)
applies. This proves existence, not that every reduction lifts.

No product-lift extension over all of Y, relative boundary data or a
prescribed connection is proved. The quotient observation descent already
works without this extra lift.

## 4. Charges, countercontrols and the unitary alternative

If a product lift exists, E3 and E2 need not themselves be SU bundles:

    E3=L0²⊗C0,       E2=L0^-3⊗W0,
    c2(W0)=-9ell²,   c2(C0)=-84ell².               (4)

These follow from the tensor-line Chern formula. Therefore `c2(E2)=0`
does **not** imply `c2(W0)=0`: the determinant contribution matters.
Even without a product lift, the rational trace-free classes
`c2(E_n)-(n-1)c1(E_n)²/(2n)` equal `-p/4` for rank2 and `-7p/3` for
rank3. Their evaluations are `-12k` and `-112k`; these are named
mathematical classes, with no physical normalization or instanton solution
asserted. Equation(4) matches them when a lift exists.

| Control | What it shows |
|---|---|
| `K3#12(S1×S3)`, chi0, signature−16 | The quotient reduction exists; no reduction has a product lift. This is a positive quotient control, not a GU counterexample. |
| `3K3#34(S1×S3)`, chi0, signature−48 | A product-liftable reduction exists: ell²=−4, `c2(W0)=36`, `c2(C0)=336`. Here `3K3` means connected sum. |
| T4, d=0 | A liftable reduction with all displayed Chern numbers zero. |
| T4, d=2e for a primitive null vector e | A realized negative complex structure and H extension with signature0, but d not divisible by6, so this particular reduction does not lift. Signature alone tests existence of some lift. |
| T4, an abstract SU2 bundle with c2=1 | Valid abstract group data, incompatible with E2 being this native negative bundle. |
| Noncompact R4 | Ordinary H⁴ vanishes but framed/relative instanton charges need not. No exclusion of such physical sectors follows from this closed-section theorem. |

For optional **U(3,2)** without a chosen total determinant trivialization,
write `b=c1(E3)`. The trace argument still gives `c2(E2)=0`, `d²=p`;
only `2c2(E3)=b²-5p` follows for the positive factor. Do not import
`b=-d` or the special-unitary product-lift theorem into that source-admitted
alternative.

## 5. Three-state return and verification ceiling

- **ESTABLISHED:** the geometric class relations, fixed-reduction sixth-root
  criterion, and existence iff signature divisible48 under the stated
  absolute/free-data conditions.
- **RULED OUT:** geometric realizations with incompatible characteristic
  data, and product-liftable reductions in this closed spin Lorentz class
  when signature is not divisible48. The H quotient survives there.
- **NOT MODELED / UNDETERMINED:** physical selection/current, actual
  instanton solutions, observed chirality/counts, source-required compact
  topology, end/relative sectors, prescribed connection and global-Y lift.

The topology argument uses the cited standard identities and owned theorems.
The accompanying exact probe checks polynomial identities, line twists,
divisibility and positive/negative controls. Lean checks only their finite
arithmetic core, not Wu, Rokhlin, Furuta, bundle classification or the
physical interpretation. Tier1 requires two specialists and a separate
hostile reviewer before acceptance. The versionless RA-A2/RA-A6 attachment
carries evidence only: no verdict, grade or revival-trigger change.

Choice budget remains **10 families / 4 grouped obligations / net6 /
0 source-selected predictions**. These universal constraints add no choice
and are not another obligation satisfied by the W2 candidate. The consumed
successor is unrestricted independent Chern-data sampling within this exact
geometric branch. A physical test still needs an authenticated gauge-bundle
identification; a generic conventional instanton is not that bridge.

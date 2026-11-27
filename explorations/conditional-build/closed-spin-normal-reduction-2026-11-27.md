---
title: Closed spin Lorentz four-bases always admit the normal complex reduction
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: P2xglobal_index / X-P1-P2
tier: T2
expected_delta: Resolve the retained integral-square condition for all smooth closed spin Lorentz four-bases, without assumptions on fundamental group or torsion.
actual_delta: The square condition is always soluble; the inherited normal U(3,2) and optional fixed-Spin SU(3,2) absolute reductions therefore exist throughout this class. Selection and fixed or relative data remain separate.
class_covered: Smooth closed connected oriented spin four-manifolds admitting a Lorentz metric; native trace-reversed normal signature (6,4), with the component orientations and normal Spin lift of the inherited reduction theorems.
premises:
- explorations/conditional-build/global-normal-complex-reduction-2026-11-24.md
- explorations/conditional-build/normal-special-unitary-existence-2026-11-25.md
- explorations/conditional-build/normal-sm-global-quotient-2026-11-27.md
- lab/sources/source-claim-register.yaml#SC-META-50
- lab/sources/source-claim-register.yaml#SC-GRP-03
source_bridge:
  status: conditional
  reason: Spin and the proposed normal compact/complex reductions are source-attested; closed Lorentz topology is the declared domain, and existence does not select a physical reduction or connection.
kill_condition: No GU kill. A counterexample satisfying all stated hypotheses would invalidate this positive closure; removing spin, smoothness, or the absolute-data scope changes the theorem.
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: No verdict promotion; resolves the closed-base existence condition inherited by P2 and X-P1-P2.
---

# The closed-base existence condition closes positively

```yaml
program_target: P2xglobal_index / X-P1-P2
tier: T2
expected_delta: Resolve the retained integral-square condition for all smooth closed spin Lorentz four-bases, without assumptions on fundamental group or torsion.
actual_delta: The square condition is always soluble; the inherited normal U(3,2) and optional fixed-Spin SU(3,2) absolute reductions therefore exist throughout this class. Selection and fixed or relative data remain separate.
```

**Result.** Every smooth closed oriented spin Lorentz four-manifold admits an orientation-compatible almost-complex structure. Consequently the native normal bundle admits the previously constructed U(3,2) reduction, and its optional SU(3,2) refinement can match any prescribed normal Spin lift under the inherited free-data hypotheses. This is an application of standard topology, not a new general topology theorem or a physical prediction.

Basis: `ffa6fbe79169e098de7a6bf257048ba2cd9e9ba4`.

```gu-typed-objects
result: automatic closed-spin absolute normal complex reduction
carrier: TX over closed oriented spin X4; native N=Sym2(pi*TX)* over Y=Met(3,1)(X), its time-oriented cover and an admitted metric section LAYER=ambient+observed BRIDGE=literal-section-pullback CHIRALITY=N/A
pairing: integral intersection form on H2 modulo torsion; separately trace-reversed normal metric of signature6,4 ON=declared_carrier
real_structure: real tangent and normal bundles; chosen almost-complex reductions and prescribed normal Spin lift
grading: positive6/negative4 normal metric split, not a fermionic or family grading
action_owner: repository-construction -- absolute bundle topology, no action or physical vacuum selected
target: existence of normal U(3,2) and optional fixed-Spin SU(3,2) reductions MAP-TYPE=not-a-map
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Follow [source-native routing](../../lab/methods/source-native-comparator-routing.md). This geometric existence result supplies no conventional Higgs/VEV, family-index, chirality, anomaly or vector-mass inference. The full-unitary source parent, independent bars and effective 2+1 interpretation are unchanged. Literal section pullback is not an arbitrary physical projection.

## 1. The closed four-manifold theorem

Let X be smooth, closed, connected, oriented and spin, and suppose X admits a Lorentz metric. There is an integral class c with

    rho2(c)=w2(TX)=0,       c²=p1(TX)+2e(TX).                 (1)

Thus the [owned Wu criterion](global-normal-complex-reduction-2026-11-24.md#3-the-negative-rank-four-problem-and-the-base-criterion) gives an almost-complex structure of the chosen orientation. Here is a complete solution of (1), not merely a divisibility check.

**Step 1 — topology of the base.** The Lorentz metric supplies a timelike line field. On its time-orientation double cover that line is trivial, so the Euler characteristic is zero; multiplicativity under this finite cover gives chi(X)=0 even without time orientability. Poincare duality makes the intersection lattice

    L=H²(X;Z)/torsion

unimodular; spin makes it even. Rokhlin gives signature(X)=16k for some integer k. These statements impose no restriction on the fundamental group. If k=0, take c=0: both sides of (1) evaluate to zero, and H⁴(X;Z)=Z makes this an equality of integral classes.

**Step 2 — exclude a nonzero definite form.** Suppose k is nonzero and L is definite. Form X'=X#(S²×S²), a smooth closed spin manifold with indefinite intersection form L⊕H. [Furuta's Theorem 1, p279](https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/2001/0008/0003/MRL-2001-0008-0003-a005.pdf) gives

    b2(X)+2 >= (5/4)|signature(X)|+2.

Definiteness gives |signature(X)|=b2(X)>0, contradicting this inequality. Furuta's theorem has no simply-connectedness or b1=0 hypothesis; its §2 explains the spin-preserving surgery reduction used in its proof. Applying it to X' avoids importing a simply-connected version of Donaldson's theorem. X' need not be Lorentz: only the stated spin and indefinite-form hypotheses are used there.

**Step 3 — exhibit the square.** An even indefinite unimodular lattice contains a hyperbolic plane. Specifically the [indefinite classification, Peters–Sterk, Corollary 2.4.3, p63](https://cpeters1.win.tue.nl/Books/QuadraticForms/QuadForms.pdf) decomposes it as signed E8 summands and H summands, with at least one H in the indefinite case. Choose e,f in that plane with e²=f²=0 and e·f=1, and set

    a=e+6k f,       a²=12k,       c=2a,       c²=48k.          (2)

Lift a from L to H²(X;Z) before defining c. Then rho2(c)=0 exactly, including any torsion in H²; torsion contributions to its square vanish in H⁴(X;Z)=Z. The signature theorem and chi=0 give

    (p1+2e)[X]=3 signature(X)+2 chi(X)=48k=c²[X].            (3)

Again H⁴(X;Z)=Z upgrades (3) to (1). This completes the proof for arbitrary fundamental group and integral cohomology torsion. No lattice classification of simply-connected manifolds, integrability theorem, or numerical search is used.

## 2. Transfer to the already-owned native normal bundle

The [November24 normal-bundle theorem](global-normal-complex-reduction-2026-11-24.md) establishes the splitting and equivalence: an orientation-compatible almost-complex structure on TX supplies a normal U(3,2) reduction on a metric section, on all of Y, and on its time-oriented cover. The relevant negative factor is

    Nminus ≅ L* ⊗ pi*TX,

as a real bundle, with its definite negative metric. Pull back the base complex structure, tensor with L*, and orthogonalize for that definite metric. **The base complex structure is not Lorentz-orthogonal on TX:** signature (3,1) cannot support such an orthogonal complex structure. The bundle isomorphism above is not a Lorentz isometry. The positive rank-six extension and component orientations are precisely those of the inherited theorem.

The [November25 fixed-Spin theorem](normal-special-unitary-existence-2026-11-25.md) then applies. X has dimension four, while Y and its time-oriented cover have CW homotopy models of dimension at most seven (RP³ and S³ fibres). Given the resulting negative U(2) structure and any prescribed total normal Spin lift, one may choose the positive U(3) structure and unit determinant volume to obtain a compatible SU(3,2) reduction. This retains the Spin lift, not only its second Stiefel–Whitney class.

The [global quotient corollary](normal-sm-global-quotient-2026-11-27.md) already identifies the compact subgroup as (SU(3)×SU(2)×U(1))/mu6 and proves descent of the specified geometric observation map. That is inherited evidence, not new quotient or charge-quantization credit. The arithmetic coefficient 6 in (2) is unrelated to that group kernel or a generation count.

## 3. Sharp domain and fixed-data controls

| Change of hypotheses | Consequence |
|---|---|
| Retain all hypotheses, allow nonzero signature | K3#12(S¹×S³) has chi=0 and signature=-16; a=e-6f gives c²=-48. This previously owned example now belongs to the whole-class theorem. |
| Drop spin | 2 CP²#2(S¹×S³) is Lorentz with chi=0, signature=2. Every characteristic square is 2 mod8, but 3 signature=6 mod8: no almost-complex structure. This is not a counterexample in the source-spin class. |
| Drop Lorentz/chi=0 | S4 is closed and spin but H²=0 and 2 chi+3 signature=4, so (1) has no solution. |
| Fix both normal complex structures | Their integral determinant class must still vanish; the freedom used by the SU existence proof is unavailable. |
| Fix a determinant phase, relative boundary/end reduction, or connection | Compatibility and extension remain separate; a preserved connection needs parallel complex structures and volume. No relative problem is solved here. |
| Drop smoothness or closedness | The Furuta argument is not a theorem for arbitrary topological four-manifolds. Open/boundary absolute existence has its own already-owned proof. |

This proves existence, not a natural metric-only choice, an integrable complex structure, or a Lorentz-invariant selection. Closed Lorentz examples are not asserted to be globally hyperbolic or physically realized. Nor is Wu sufficiency exported to arbitrary four-dimensional CW spaces with torsion in H⁴.

## 4. Source meaning, novelty and validation ceiling

SC-META-50 records the active spin structure among the source's starting data (TOE2025 00:03:06; [transcript](../../lab/sources/transcripts/toe-weinstein-gu-40-years.md)). SC-GRP-03 records the 2021 draft **p29, equation4.6**: simultaneous compact and complex normal reductions, allowing U(3,2) with an extra U(1) or the optional SU(3,2) branch. See the [global-reduction source reinspection](../../lab/sources/k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md). Closedness is our declared topological domain, not an additional universal source assertion.

The November24 result retained (1) as an unresolved closed-base condition and did not infer its automatic solvability from signature divisibility. The new step is the complete Furuta-plus-lattice construction (2), so that this condition no longer excludes any smooth closed spin Lorentz base. The optional SU and global mu6 consequences are composed from accepted owners, not independently recounted as discoveries.

Physical selection, connection preservation, the source's full-unitary chimeric parent, actual observed currents and any prediction remain separate. The native normal signature is explicitly (6,4); this result does not identify source-asserted ambient K77 with derived K95, or replace full U(64,64) by an optional quaternionic subgroup. No source, ledger or canon verdict is changed here.

**Verification status.** T2 written proof using the cited standard theorems and the linked repository constructions. Independent specialist review and small arithmetic controls belong to the enclosing run. No Lean certification of Furuta, lattice classification, Wu's criterion or this topology argument is claimed. The useful next condition is selection or fixed-data compatibility already named by those owners, not another absolute closed-base square search.

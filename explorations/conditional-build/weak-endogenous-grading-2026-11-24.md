---
title: "Endogenous Lorentz plus geometric weak symmetry: the exact trace-motion criterion"
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Decide when actual geometric weak symmetry restores the independent-product restriction in the grading comparison
actual_delta: Any normal generator moving the negative metric-trace line restores the full product commutant; geometric weak SU2 satisfies that condition, while moving-selector covariance alone does not
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Weak symmetry and the four-grading comparison

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `INTERNAL_STRUCTURAL_ONLY`. This is a conditional theorem
> about a common symmetry commutant. It does not select GU's physical grading.

program_target: X-P1-P2-P3
tier: T2
expected_delta: Replace an untested symmetry enlargement by an exact structural criterion
actual_delta: Common fixed-object graph-Lorentz and geometric-weak equivariance forces product equivariance; moving-reduction covariance remains distinct

```gu-typed-objects
result: Exact trace-motion Lie-generation theorem and its conditional grading consequence
carrier: H of Lorentz signature (3,1), N=Sym²H* with trace-reversed vertical form lambda=1/2; existing canonical tangential RS symbol LAYER=ambient+observed BRIDGE=literal-contraction CHIRALITY=S-FULL-DIRAC
pairing: actual vertical form of signature (6,4); separately the existing K95 graded-pairing fixture where stated ON=declared_carrier
real_structure: real normal so(6,4), complexified representation proof; no K77/K95 real-structure identification
grading: fixed zero-order RS grading with observed g=chiH in the declared Nov21 symbol category; source physical projector remains unspecified
action_owner: N/A -- structural common-equivariance condition, no source action or background selected
target: common symmetry commutant and the admissible grading set MAP-TYPE=restriction
```

## 1. Result and source boundary

The earlier [four-grade theorem](native-descending-grading-classification-2026-11-21.md)
requires independent `Spin(H) × Spin(N)` covariance. Endogenous frame
covariance alone is weaker, as that theorem explicitly acknowledges.
Here is the missing discriminator:

**If one fixed grading commutes with endogenous Lorentz and with the actual
geometric normal weak `SU(2)_L`, it already commutes with the independent
product Lie algebra.** In fact, one nonzero weak generator is enough. This
holds for every maximal-compact positive-six/negative-four placement, not
just a chosen matrix fixture.

The qualifier **one fixed grading** matters. A family of grades depending
on a moving weak/complex reduction may transform covariantly while its
value at one reduction does not commute with the full endogenous Lorentz
algebra. The source has not supplied the physical weak-current projector or
its fixed-versus-moving transformation law. Thus the result strengthens a
specified structural subclass; it does not close the native-grading packet.

Source custody:

- SC-GRP-03 asserts the simultaneous compact/complex normal reductions;
  SC-FER-07 locates the apparent internal quantum numbers in normal spinors.
  Use the normal geometric weak action, with form and spin factors transformed
  together: Category G in [weak-action transport](source-weak-action-transport-2026-11-13.md).
  Fixed spin-only action is Category F and fails the stated observation
  intertwiner. No independent internal gauge carrier is substituted.
- SC-CHI-01/04 assert a nonchiral total and effective observed separation;
  SC-GEN-01/02/03 retain the `2+1` and imposter labels. Neither fixes a
  Fredholm grading or converts a representation into an integer count.
- The physical ledger's RA-A2/RA-A6/RA-A8 still require selection/globalization
  of the reduction and its source owner. RA-A7's observation-image commuting
  statement is not identification of the endogenous embedding with the block
  embedding. No ledger row, source adherence, action class or canon verdict
  changes here.

## 2. The trace-motion theorem

Let `H` be a real Lorentz four-space with metric `eta`, and set

    N = Sym² H*,
    K(h,k) = tr(eta^-1 h eta^-1 k)
             - (1/2) tr(eta^-1 h) tr(eta^-1 k).

Let `t=eta` denote the metric-trace vector and `U=ker tr_eta`. Then

    N = U ⊥ R t,     K(t,t) = -4,
    signature(K|U) = (6,3),
    delta(X) h = -X^T h - h X,      X in so(1,3).

The induced algebra `h=delta(so(1,3))` fixes `t` and acts irreducibly on
`U` over the reals and after complexification. Its complex representation
is `(2,2)` in **doubled** `sl2 × sl2` highest-weight notation, dimension9.
The already-owned [SA-2 branching](../../lab/active-research/joe-directed/soldered-ad/sa2-two-lorentz-source-package-classifier-2026-08-20.md)
contains this `9+1`; it is reused, not newly counted.

**Theorem.** For any set `k` of normal `K`-skew generators, let
`l` be the real Lie algebra generated by `h` and `k` inside `so(N,K)`.
Then

    l = so(6,4)   iff   at least one W in k has Wt != 0.       (1)

If every generator fixes `t`, the generated algebra lies in
`so(t-perp,K)=so(6,3)`, of dimension36, so the reverse direction is immediate.
The forward generation statement needs the representation argument below;
merely moving one vector would not imply it for an arbitrary representation.

**Proof.** Identify `so(N_C,K)` with `Λ²N_C`. Under `h_C`,

    Λ²N_C = Λ²U_C ⊕ (U_C ∧ t),
    Λ²U_C = (2,4) ⊕ (2,0) ⊕ (4,2) ⊕ (0,2),
    U_C ∧ t = (2,2).                                      (2)

Indeed `U_C=A3⊗B3`, and
`Λ²(A⊗B)=(Λ²A⊗Sym²B)⊕(Sym²A⊗Λ²B)`;
`Λ²A3=A3` and `Sym²A3=A5⊕A1`, with the same identities for B.
Thus the `(2,2)` summand is irreducible and is absent from `Λ²U`.
The `h_C`-submodule generated by a `W` with `Wt !=0` therefore contains
all of `U_C∧t`. This projection is legitimate inside any `h_C`-stable
linear subspace: complete reducibility and the inequivalent isotypic
summands separate it. More explicitly, if `C` is the sum of the two
quadratic Casimirs normalized to `m(m+2)+n(n+2)`, its eigenvalues are
16 on `(2,2)` and 8 or32 on the other summands; the projector is

    P_U = -(C-8)(C-32)/128.                               (3)

Every application of `C` is a linear combination of repeated commutators
with endogenous Lorentz generators. Finally,
`[u∧t,v∧t]` is a nonzero scalar multiple of `u∧v`, since `K(t,t) !=0`.
These brackets span `Λ²U_C`. Therefore the complexified generated algebra
is all `so(10,C)` and the real subalgebra of `so(6,4)` has dimension45,
so equals it. No dimension-only identification of real forms is used:
containment in the actual `K`-skew algebra was retained throughout. ∎

### The product, not just the normal factor

The relevant simultaneous actions lie in
`so(H) ⊕ so(N)`:

    endogenous graph: (X,delta(X)),
    geometric weak:   (0,W).

The normal ideal in their generated algebra is stable under
`ad delta(so(H))`. If `Wt !=0`, applying the same projector (3) to `(0,W)`
and taking brackets generates `(0,so(N))`. Subtracting `(0,delta(X))`
from the graph generators then generates `(X,0)`. Hence

    Lie< graph(delta), (0,k) > = so(H) ⊕ so(N)             (4)

under exactly the trace-motion hypothesis. Commutation with the two
starting actions consequently implies commutation with the full product
on any honest representation of this direct-sum algebra, including the
form-plus-spin RS carrier. This conclusion concerns the connected
infinitesimal symmetry; no discrete quotient or global bundle lift is supplied.

## 3. Why the actual geometric weak subgroup meets the criterion

For any chosen maximal-compact splitting
`N=W6_positive ⊥ W4_negative`, Category-G `SU(2)_L` fixes `W6` and acts
on `W4` as the real quaternionic fundamental. Every nonzero Lie generator
on that four-space squares to a strictly negative scalar times the identity.
Its kernel on N is therefore exactly the positive six-plane.

The metric trace has negative norm. It cannot lie in that kernel.
Consequently every nonzero geometric weak generator moves `t`, and (4)
applies. This uses the **source-derived weak factor of Spin(4)**, not an
arbitrary embedded group called `SU(2)`.

A useful contrary construction is the diagonal `SU(2)` in
`SU(2)_L×SU(2)_R`: its vector action on the four-plane is `1⊕3`, and a
placement can fix the trace. Such a group need not generate all normal
rotations with endogenous Lorentz. It is not the factor action used in the
source-normal weak transport. This contrast shows why retaining the actual
weak representation is load-bearing.

This theorem neither selects a maximal-compact reduction nor proves that
it is preserved by a source connection. It says that **where such a
reduction is supplied**, its weak action has the required trace-motion
property. No new connection, source operator or action is built.

## 4. Consequence for descending gradings

Retain every other hypothesis of Nov21 §3: canonical tangential projected
RS symbol on `R_Y=ker Gamma_Y`, nondegenerate `4+10` split, literal
contraction q and its canonical orthogonal right inverse, complex zero-order
grade, observed `g=chiH`, no extra scalar companion/background tensor or
physical quotient. Replace its independent-product condition by

    [G,rho(X,delta X)] = 0 for all X,
    [G,rho(0,W)] = 0 for the geometric weak generators.   (5)

Equations (4)–(5) recover the independent-product condition. Thus **exactly
four** grades remain in this fixed-object symbol category:

    T = 0,
    A = chiH ⊗ (epsilon_+ P_N^+ + epsilon_- P_N^-),
    epsilon_+,epsilon_- in {-1,+1}.

Conversely, those four product-equivariant grades obey (5), so this is an
exact equivalence of the two declared symmetry restrictions. The coherent
horizontal lift is only the `(-,-)` choice, not uniquely selected.
Requiring the existing K95 cross-grade quaternionic law further restricts
`epsilon_+=epsilon_-`, leaving two. Its K95 premise remains separate from
K77. Full lower-order oddness, common domains, barred duality and a physical
projector still have to be checked on the same object.

The existing closed positive elliptic comparison therefore keeps its same
four totals `(-820,368,368,1556) sigma(X)` and its stated parity/mod24
information when its topology/domain assumptions also hold. This is reuse
of that table under a newly justified *conditional symmetry subclass*,
not a new native index calculation, integer generation prediction, or a
transfer of an elliptic number to Lorentzian Y14.

### Fixed symmetry is stronger than moving covariance

Suppose a reduction selector J transforms under endogenous Lorentz and a
family satisfies

    G(g·J) = rho(g) G(J) rho(g)^-1.

Differentiation gives
`[rho_endo(X),G(J)] = dG_J(X·J)`, which need not vanish. Even if every
`G(J)` commutes with the weak subgroup selected by J, condition (5) at a
fixed J does not follow.

A concrete tensor countercontrol is the Cartan involution
`S_W=+1 on W6, -1 on W4`. It commutes with the chosen weak action and
transforms covariantly when W moves, but at the standard adapted splitting
it fails to commute with each endogenous boost. This is a counterexample
to the **logical covariance-to-commutation inference**; it is not offered as
an extra admissible RS grade or as a source-selected background.

The source's physical weak-current projector and its dependence on a moving
reduction remain unbuilt. This result therefore establishes the common-fixed
case completely without asserting that all source-native realizations meet it.
Extra mixed intertwiners from endogenous branching alone do not establish
additional admissible grades; conversely this theorem does not exclude
moving-selector grades merely because they are absent from (5).

## 5. What changed and what remains decisive

**New constraint:** in the fixed-object common-symmetry subclass, adding the
actual weak action removes the extra commutant freedom of endogenous Lorentz
alone. The four-grade result no longer needs independent product symmetry as
an unexplained extra assumption there. The trace-motion criterion gives the
exact reason and applies across all maximal-compact placements.

**No re-credit:** SA-2 already owns the 16/144 endogenous branching and the
full-PS closure. This result reduces the needed additional symmetry from
all21 Pati–Salam generators to one nonzero actual weak generator, proves the
placement-independent criterion, and separates fixed-object invariance from
moving-reduction covariance.

**Native missing datum:** specify whether the physical observed projector and
its lifted grading are fixed under both actions in (5), or form a covariant
family tied to the moving reduction, and identify that reduction's actual
stabilizer on the operator/domain. This is narrower than asking for a whole
action. The observation continuity and global-reduction investigations in
this wave address separate premises; neither supplies (5) by itself.

Matrix `X-P1-P2-P3` and `P3xglobal_index` remain constrained/open; Item1's
`NATIVE-GRADED-FREDHOLM-OBSERVATION` blocker is not cleared. No balanced-total
witness or all-C nonzero-total theorem follows, so neither prior packet is
killed or reopened automatically. This result provides no new stopping rule.

## 6. Exact supporting checks

Replay `tests/program-focus/weak_endogenous_grading_probe.py`; retained data:
`lab/process/weak-endogenous-grading.json`.

The probe reuses only SA-1's rational construction of `Sym²H*`, its actual
lambda-half form, and the induced Lorentz matrices. It independently checks:

- the real signature, negative fixed trace and metric-skew actions;
- a genuine weak quaternionic triple over exact `Q(sqrt2)` represented as
  rational matrix pairs, its brackets, squares and trace motion;
- the separating Casimir projector on those weak generators;
- a nine-dimensional trace-motion orbit (ranks1,6,9,9), whose brackets span
  the36-dimensional trace stabilizer and together span all45 normal directions;
- the character identity (2) and separated Casimir eigenvalues; and
- the moving-Cartan countercontrol and endogenous-only dimension6.

These controls support the explicit proof; a finite embedding check alone
would not establish all placements. No floating-point rank, inferred physical
index, source-group selection or numerical family count is used. Two independent specialist reviews accepted the theorem and fixed-versus-moving scope at T2. The exact probe passes19 checks; deleting trace motion or boosts each produces the expected failure. See the [review](../../lab/process/hostile-reviews/2026-11-24-structural-compatibility-review.md).

---
title: "Non-Forgettable Observer Datum for Freed-Hopkins Enriched Bordism"
date: 2026-06-23
problem_label: "freed-hopkins-nonforgettable-observer"
status: exploration
verdict: OPEN
---

# Non-Forgettable Observer Datum for Freed-Hopkins Enriched Bordism

## 1. Problem Statement

The first Freed-Hopkins enriched-bordism toy
(`explorations/time-as-finality-crosswalk/freed-hopkins-observer-pairing-enriched-bordism-toy-2026-06-23.md`)
failed because observer metadata is forgotten by the underlying-bordism functor
`U : Bord_2^{xi,obs}(Z) -> Bord_2^xi`. If observer records are metadata, the forgetful
functor has contractible fibers and the anomaly datum descends unchanged. If observer
data carries topological charge, the construction reduces to ordinary defect/background
enrichment.

The present note looks for a structure on the observer that cannot be trivialized by
bordism -- a *non-forgettable observer datum* -- and asks whether any such structure
provides a genuine enrichment of the bordism category that changes the Freed-Hopkins
anomaly classification.

The problem is precise: find a datum `d(O)` attached to an observer worldline `O`
embedded in a bordism `W` such that:

1. `d(O)` is not determined by the underlying manifold data `(W, sigma_W)` alone.
2. `d(O)` cannot be made trivial by a bordism of `O` (i.e., it is bordism-invariant).
3. `d(O)` is not equivalent to ordinary defect/background field data under relabeling.

Three candidates are analyzed: (1) the eta-invariant as a secondary characteristic
class; (2) the choice of pin^+ vs pin^- structure; (3) the Maslov index for Lagrangian
observer submanifolds.

**Failure condition:** if all three candidates are bordism-trivial (vanish after
choosing a bordism of the observer) or reduce to ordinary symmetry/background extensions,
the Freed-Hopkins enrichment adds no new structure beyond what Freed-Hopkins already
classifies, and the observer-pairing program collapses to relabeling.

## 2. Established Context

This computation builds on:

- The failed first toy, which established the two obstruction modes (metadata-descends
  vs. defect-relabeling).
- `lab/literature/02-observer-dependence-freed-hopkins-anomaly-classification.md`, which
  finds no published observer-pairing Freed-Hopkins extension.
- `canon/no-go-class-relative-map.md` §2.3 (Freed-Hopkins as classification theorem),
  which names "enriched bordism category" as the formal door for extension but requires
  the observer datum to be neither forgettable nor relabeling.
- The GU context: the observer geometries in GU are sections `s: X^4 -> Y^14 = Met(X^4)`
  with spinor bundle `S = H^64`, gauge group `Sp(64)`, signature `(9,5)`. An observer
  worldline in GU is a 1-dimensional submanifold of `X^4` (or `Y^14`).

## 3. Candidate 1: Secondary Characteristic Class (Eta-Invariant)

### Setup

Let `O` be a compact 1-manifold embedded in a 2-manifold bordism `(W, sigma_W)`. The
eta-invariant `eta(O, A_O)` of a Dirac-type operator on `O` twisted by a connection
`A_O` on a flat bundle over `O` is a secondary characteristic class: it vanishes when
`O` bounds and the connection extends, but it can be nonzero when no such extension
exists.

The eta-invariant is a bordism invariant *of the pair* `(O, A_O)` in the following
precise sense: if `(O_0, A_0)` is bordant to `(O_1, A_1)` via a `(W, A_W)`, then
`eta(O_1, A_1) - eta(O_0, A_0) = 2 * ind(D_W, A_W)` (mod-2 version: Atiyah-Patodi-
Singer), where the index is an integer. The real-valued eta-invariant is therefore
*not* a bordism invariant; it shifts by twice an integer under bordism.

The mod-2 reduction `xi(O, A_O) = eta(O, A_O) mod 2` is a genuine Z/2Z bordism
invariant for the pair (1-manifold with flat bundle).

### Is It Non-Forgettable?

The mod-2 eta invariant `xi(O, A_O)` is not determined by `(W, sigma_W)` alone -- it
depends on the flat bundle `A_O` on `O`. However, that flat bundle is classified by the
holonomy representation `pi_1(O) -> G`, and for `O = S^1` this is an element of the
representation variety `Hom(pi_1(S^1), G) / G = G / G` (conjugacy class in `G`).

So the datum is: a conjugacy class in `G` together with the resulting mod-2 eta invariant.

**Is this ordinary background data?** Yes. A flat bundle on the observer worldline `O`
is exactly a background field on `O` -- a defect/background labeled by a conjugacy class
in `G`. The mod-2 eta invariant is a function of this data, not an additional datum.
This means: the eta-invariant construction does not produce a datum *independent of* an
ordinary flat-bundle background. It is a derived quantity of an existing background field.

**Assessment for Candidate 1:** The mod-2 eta-invariant is bordism-invariant but is a
function of a flat bundle, which is ordinary defect/background data. It does not produce
a non-forgettable datum that is independent of background-field enrichment. Candidate 1
fails condition (3).

### Why the Full Real Eta Does Not Help

The full real-valued `eta(O, A_O)` shifts by integers under bordism, so it is not
bordism-invariant. One cannot use it to define an anomaly invariant without choosing a
trivialization (framing), and that trivialization is again extra structure.

## 4. Candidate 2: Pin^+ vs Pin^- Structure

### Setup

For an unoriented or orientation-reversing observer worldline, the structure group can
lift to either `Pin^+(1)` or `Pin^-(1)`. The two differ by the sign of the generator
`r` in the pin group: `r^2 = +1` for `Pin^+` and `r^2 = -1` for `Pin^-`. For
1-dimensional manifolds, `Pin^+(1) = Z/2Z` and `Pin^-(1) = Z/4Z`.

The choice of pin structure is classified by `H^1(O; Z/2Z)` (whether the orientation
double cover is trivial or not, combined with the pin lift).

### Is It Non-Forgettable?

**For compact bordism:** the inclusion-restriction map on cohomology gives a constraint.
If `O` is a boundary component of a pin^pm-structured 2-manifold `W`, the pin structure
on `O` is the restriction of the pin structure on `W`. So the choice of pin structure
on `O` is determined by the global structure of `W` -- it is not an independent observer
datum.

**Is the choice of Pin^+ vs Pin^- non-trivializable?** For a closed 1-manifold `O` that
bounds a compact 2-manifold `W`, the pin structure on `O` is always extendable to `W`
(since the bordism group `Omega_1^{Pin^-} = Z/2Z` and `Omega_1^{Pin^+} = 0`). Specifically:

- `Omega_1^{Pin^+} = 0`: every compact 1-manifold with pin^+ structure is pin^+-bordant
  to the empty set. So pin^+ structure adds no bordism invariant for 1-manifolds.
- `Omega_1^{Pin^-} = Z/2Z`: there is one nontrivial bordism class. `S^1` with the
  nontrivial pin^- structure represents the generator.

The nontrivial class in `Omega_1^{Pin^-} = Z/2Z` is a genuine bordism invariant for
1-manifolds. It is NOT determined by the underlying oriented manifold -- two different
lifts of the same oriented circle to a pin^- manifold can give different bordism classes.

### Is This an Ordinary Background?

The pin^- structure on `O` is a geometric structure (a lift of the frame bundle from
`O(1)` to `Pin^-(1)`). It is classified by `H^1(O; Z/2Z)` and is exactly the kind of
tangential structure data that Freed-Hopkins already allows in its input category. It is
an enrichment of the *symmetry type* or *tangential structure* `xi`, not an independent
observer datum.

Concretely: adding "observer worldline with pin^- structure" to the bordism category
replaces `xi` with `xi^+` or `xi^-` (the symmetry type augmented by pin^pm data on
the observer stratum). This is inside the Freed-Hopkins framework: the classification
theorem applies to any fixed symmetry type including those involving pin structures on
strata.

**Assessment for Candidate 2:** The pin^-/pin^+ distinction produces a nontrivial
bordism invariant in `Omega_1^{Pin^-} = Z/2Z`. However, it is a tangential structure
on `O` and falls squarely within the Freed-Hopkins framework as a refined symmetry
type. It does not produce an *observer-pairing-specific* datum not already classified
by Freed-Hopkins with the appropriate `xi`. Candidate 2 fails condition (3) -- it
reduces to ordinary tangential-structure enrichment (relabeling).

### Potential GU Relevance

In GU the observer worldline `O subset X^4` is embedded in a Lorentzian 4-manifold.
The pullback of the Cl(9,5) spinor structure to `O` determines whether the restricted
Dirac operator on `O` has a pin^+ or pin^- interpretation. Given that `Cl(9,5) = M(64,H)`,
the spinor module `S|_O = H^{64}|_O` carries the pullback structure. This may determine
a preferred pin structure on `O`, but it does so by the ambient GU geometry, not by
an independent observer choice. No new invariant arises beyond the ambient spinor data.

## 5. Candidate 3: Maslov Index for Lagrangian Observer Submanifolds

### Setup

Let `(W, omega)` be a symplectic manifold (or a manifold with a symplectic structure
on a relevant bundle). An observer worldline `O subset W` is *Lagrangian* if `T_p O`
is a Lagrangian subspace of `(T_p W, omega)` for each `p in O`. The Maslov index
`mu(O, Lambda_0)` of a Lagrangian submanifold relative to a reference Lagrangian
`Lambda_0` is an integer-valued invariant that counts the number of intersections
(with sign) of the Lagrangian Grassmannian path with the Maslov cycle.

For a closed Lagrangian curve `O` in a symplectic 2-manifold, the Maslov index is an
integer `mu(O) in Z`. If `(W, omega)` is a surface with an area form, every embedded
curve is Lagrangian if the ambient dimension is 2 (every 1-submanifold of a
2-manifold is automatically Lagrangian). So for the 2-dimensional bordism toy, every
observer worldline is Lagrangian and the Maslov index is well-defined.

The Maslov index is *bordism-dependent* in the following sense: if `O_0` and `O_1` are
Lagrangian cobordant (there is a Lagrangian 2-chain `L subset W x [0,1]` bounding
`O_1 - O_0`), then `mu(O_0) = mu(O_1)`. However, Lagrangian cobordism in dimension 2
is more restrictive than ordinary cobordism: not every ordinary cobordism is Lagrangian.
So the Maslov index is bordism-invariant under *Lagrangian* bordism but can vary under
*ordinary* bordism.

### Is the Maslov Index Non-Forgettable?

The question is whether the Maslov index provides a datum that:

(a) Is not determined by the underlying manifold data alone.
(b) Survives (is non-trivial) even after ordinary bordism.
(c) Is not equivalent to ordinary defect/background data.

For (a): the Maslov index depends on the Lagrangian Grassmannian path, not just on the
underlying topological manifold. Two embedded circles in the same symplectic 2-manifold
that are topologically isotopic can have different Maslov indices if the isotopy passes
through a caustic. So the Maslov index adds data beyond the underlying manifold.

For (b): Under ordinary cobordism (not Lagrangian cobordism), the Maslov index can
change. The ordinary bordism group of `O` (ordinary closed 1-manifolds) is trivial
(`Omega_1 = 0`: every closed 1-manifold bounds a disk). If `O = S^1` bounds a disk
`D^2 subset W`, the Maslov index is the Maslov index of the disk, which by the
Maslov-Viterbo formula equals the degree of the map from `O` to the Lagrangian
Grassmannian `U(n)/O(n)`. For a 2-dimensional symplectic manifold (`n=1`), this is
`pi_1(U(1)/O(1)) = pi_1(S^1) = Z`, and the Maslov index is the winding number of
the angle function on `O`. If `O` bounds a disk, the Maslov index is the total winding
on the boundary, which need not be zero.

However: the Maslov index under ordinary bordism (where the cobordism need not be
Lagrangian) is:
- If `W` is simply-connected, any two Lagrangian framings are homotopic through the
  2-dimensional moduli, and the Maslov index is computable from the homotopy class.
- For `W = R^2` with standard symplectic form, the Maslov index of a closed embedded
  curve is 2 times the winding number. This is an ordinary topological datum (the
  winding number of the curve), which is determined by the homotopy class in `pi_1(W)`.

For (c): in the context of the bordism category, a Lagrangian structure on the observer
worldline requires the ambient bordism `W` to carry a symplectic structure. Symplectic
structures are additional geometric data on `W` -- they are a type of background field.
If `W` carries a symplectic form `omega` as a background field, then the Maslov index
is a derived quantity of this background.

**Assessment for Candidate 3:**

The Maslov index is interesting but fails condition (3) for the same reason as
Candidate 2: it requires auxiliary background structure (a symplectic form `omega` on
`W`) to be defined. The Maslov index is an invariant of the pair `(O, omega)`, not of
`O` alone. Adding `omega` to the bordism data is ordinary background field enrichment
(a 2-form background). Within the Freed-Hopkins framework, a symplectic form is a
particular type of tangential/geometric structure that the classification already
handles.

The Maslov index does not fail conditions (1) and (2): it is not determined by the
manifold alone (needs `omega`) and has a nontrivial bordism invariant (for non-simply-
connected targets or non-trivial symplectic structures). But it fails condition (3).

## 6. Structural Analysis: Why All Three Candidates Fail

The failure mode of all three candidates shares a common structure. For any proposed
non-forgettable observer datum `d(O)`:

**Claim:** If `d(O)` is a bordism invariant of the observer worldline `O`, then it is
classified by a bordism group `Omega_*(O, E)` for some coefficient spectrum `E`. The
Freed-Hopkins classification theorem asserts that anomaly groups of invertible theories
are computed by `Omega_*^{xi}(E)` for an appropriate Thom spectrum `Mxi` and target
spectrum `E`. Any bordism-invariant datum on the observer worldline `O` either:

(a) Factors through the underlying manifold data (it is a topological invariant of `O`
    as a manifold, hence already determined by `(W, sigma_W)` and the position of `O`),
    or
(b) Depends on additional structure on `O` (flat bundle, pin structure, symplectic form,
    etc.), in which case it is ordinary background/symmetry-type data enriching the
    bordism category -- which Freed-Hopkins classifies in the standard way.

There is no room for a third option because `d(O)` is a functor from the bordism
category of observer worldlines to some abelian group (or spectrum), and functors from
bordism categories to abelian groups are classified by generalized cohomology theories
(Brown representability). Any such functor has spectrum-level data (i.e., a `E` and a
map `BO -> E`) which, when added to the bordism category, produces an ordinary enriched
bordism category within the Freed-Hopkins paradigm.

This is the *no-go for non-forgettable observer data*: the structural constraint
says that any bordism-invariant datum is either (a) already present in the underlying
bordism or (b) an ordinary background/symmetry enrichment. There is no third option
within the framework of functorial field theory.

## 7. Sharpened Failure Condition

The failure condition stated in the problem header is satisfied:

**All three candidates are either bordism-trivial or reduce to ordinary background/
symmetry enrichment.** Specifically:

- Candidate 1 (eta-invariant): bordism-invariant (mod 2) but is a derived function of
  a flat bundle on `O`, which is ordinary defect data. Fails condition (3).
- Candidate 2 (pin structure): the nontrivial class in `Omega_1^{Pin^-} = Z/2Z` is a
  genuine bordism invariant of `O`, but it is a tangential structure -- exactly the
  type of data Freed-Hopkins classifies by varying `xi`. Fails condition (3).
- Candidate 3 (Maslov index): requires a symplectic background on `W`, making it
  ordinary background field data. Fails condition (3).

**Corollary:** The Freed-Hopkins observer-pairing enrichment, if it is to produce new
anomaly structure, cannot arise from any of the three candidate observer data. The
enrichment either descends away (metadata) or is relabeled (background).

## 8. Structural No-Go Result

The analysis yields a sharpened no-go:

**Lemma (informal).** Let `Cat_obs` be any bordism category enriched by observer
worldlines with a datum `d(O)` satisfying: (i) `d(O)` is a functor to a spectrum `E`;
(ii) `d(O)` is invariant under bordism of `O` relative to fixed endpoints. Then either:

- `d(O)` factors through the forgetful functor `U : Cat_obs -> Bord^xi` (the datum is
  determined by the underlying bordism), or
- `d(O)` is classified by a map `xi -> E` in the category of tangential structures,
  making `Cat_obs ~= Bord^{xi'}` for some enriched tangential structure `xi' = xi + d`.

**Consequence for GU:** The observer geometries in GU (sections `s: X^4 -> Y^14` with
spinor structure `S = H^64`) do not supply a natural candidate for `d(O)` that evades
this lemma. The GU spinor structure on an observer worldline `O` pulls back to a
representation of `Cl(1,0)` or `Cl(0,1)`, which is a finite-dimensional representation
data -- exactly the type of tangential structure Freed-Hopkins handles.

## 9. What Would Constitute a Genuine Non-Forgettable Datum

For completeness, the analysis identifies what structure *would* be needed to evade the
no-go:

**Option A: Non-functorial observer data.** If `d(O)` is not a functor (it cannot be
composed with bordisms, or it is not compatible with gluing), it avoids the Brown
representability argument. But non-functorial data cannot be used to define invertible
field theories (the theory must assign consistent values to composable bordisms). This
is not viable.

**Option B: Data from a noncontractible observer state space.** The failed first toy
(Section 10) identified the correct criterion: if the observer-state space `X_obs` is
noncontractible, a continuous family of Fredholm operators or anomaly data over `X_obs`
can define a class in `K^0(X_obs)` or `KSp^0(X_obs)` that does not descend from an
ordinary symmetry/background extension *provided* the family cannot be extended to any
ambient space containing `X_obs` as a retract.

This requires:
- A noncontractible `X_obs` built from the observer data (not from the ambient manifold
  data -- that would make it ordinary background data).
- A proof that the resulting K-theory class is not in the image of any symmetry/background
  extension functor.

No such `X_obs` has been constructed in the GU context. The space of GU sections
`Gamma(pi)` (sections of the fibration `Y^14 -> X^4`) is in principle a candidate for
`X_obs`, but the Fredholm family over it (given by varying sections `s` and pulling back
`D_GU`) defines a class in `KSp^0(Gamma(pi))` that is the index-bundle of the GU Dirac
family -- which is already part of the GU index theory, not a new observer-pairing
datum.

**Option C: Operational observer data outside the field theory framework.** If the
observer datum is defined by an operational protocol (e.g., a measurement history, a
Bayesian prior, a QRF) that is not a geometric or topological object in the bordism
category, it is outside the domain of Freed-Hopkins entirely. The classification theorem
applies to geometric field theories; operational data that is not geometric has no
natural home in the bordism category. This is not an enrichment of the bordism category
but a replacement of the framework.

## 10. GU-Specific Assessment

In the GU context, the three candidates correspond to:

1. **Eta-invariant:** The eta-invariant of the GU Dirac operator `D_GU` restricted to
   an observer worldline would depend on the Sp(64) connection and the spinor structure.
   This is background field data (the gauge connection and spinor structure are already
   part of the GU action). No new observer-pairing invariant arises.

2. **Pin structure:** The Cl(9,5) = M(64,H) structure on Y^14 determines a canonical
   spin structure on any embedded submanifold, including observer worldlines. The pin
   structure on `O subset X^4` is the pullback of the spin structure on `X^4`, which
   is in turn constrained by `w_2(Y^14) = 0` (established: N6, RESOLVED). The pin
   structure is determined by the ambient GU geometry, not by an independent observer
   choice.

3. **Maslov index:** A natural symplectic structure on the space of metrics on `X^4`
   has been proposed in the mathematical physics literature (the Atiyah-Bott symplectic
   form on the gauge field space, transported to the metric bundle). If the GU metric
   bundle `Y^14 = Met(X^4)` carries a natural symplectic form, the observer worldline
   in `Y^14` could have a Maslov index. However: the fiber `GL(4,R)/O(3,1)` does not
   carry a natural symplectic form compatible with the signature-(9,5) structure. The
   natural structure on `Y^14` is pseudo-Riemannian (the gimmel metric), not symplectic.
   No canonical Maslov index is available.

## 11. Verdict

**Verdict: OPEN**

The Freed-Hopkins observer-pairing enrichment program is structurally blocked by the
no-go in Section 6: any bordism-invariant observer datum either descends through the
forgetful functor (forgettable metadata) or is equivalent to ordinary tangential-
structure/background data (relabeling). All three concrete candidates (eta-invariant,
pin^pm structure, Maslov index) fall into the relabeling case.

The program is not closed: Option B (noncontractible observer state space with a
non-extendable K-theory class) remains open as a formal possibility. But no concrete
construction exists in the GU context.

**The Freed-Hopkins enrichment adds no new anomaly structure beyond ordinary
symmetry/background enrichment, for any of the three candidate observer data analyzed.**

The observer-pairing anomaly program for GU cannot be advanced by attaching secondary
characteristic classes, pin structures, or Maslov indices to observer worldlines. A
genuine advance requires either a noncontractible observer-state space with a
non-extendable Fredholm family, or a departure from the functorial field theory
framework entirely.

## 12. Open Questions

1. **OQ-FH-1 (Noncontractible observer-state space).** Can the GU section space
   `Gamma(pi: Y^14 -> X^4)` be completed to a noncontractible homotopy type with a
   natural Fredholm family that is not a symmetry/background extension? The index-bundle
   `ind(D_GU)` over `Gamma(pi)` defines a class in `KSp^0(Gamma(pi))`; is this class
   outside the image of any ordinary symmetry-type functor?

2. **OQ-FH-2 (Steenrod operations and secondary phenomena).** Secondary cohomology
   operations (Steenrod squares, Massey products) can produce invariants of enriched
   bordism categories that are not visible to primary cohomology. Is there a natural
   secondary operation associated to the GU spinor structure that acts non-trivially on
   an enriched observer bordism?

3. **OQ-FH-3 (Non-invertible observer defects).** The standard Freed-Hopkins framework
   requires invertibility. Non-invertible defects (categorical symmetries) can carry
   data not classified by the invertible theory. Is there a natural non-invertible
   observer defect in the GU context (e.g., associated to the Sp(64) gauge structure
   on the observer worldline) that produces new anomaly data?

## 13. Explicit Failure Conditions

The OPEN verdict would upgrade to GENUINE_OBSTRUCTION if:

- A concrete noncontractible observer-state space `X_obs` is constructed with a
  Fredholm family `{D_x}_{x in X_obs}` such that `[D_x] in KSp^0(X_obs)` is NOT
  in the image of any ordinary symmetry/background-extension map `xi -> E`.

The OPEN verdict would downgrade to RESOLVED (no observer enrichment possible) if:

- A general theorem is proved showing that for any compact `X_obs` built from the GU
  observer data (worldlines in `Y^14` with Sp(64) gauge data), the index bundle
  `ind(D_GU|_{X_obs})` is always in the image of the forgetful-image map.

The no-go in Section 6 provides strong evidence for the downgrade direction but does
not fully close it because it relies on Brown representability, which requires the
functor to be a genuine functor (Option A exclusion) and does not rule out Option B.

---
title: "Distler-Garibaldi Functor Audit"
date: 2026-06-23
problem_label: "distler-garibaldi-functor-audit"
status: exploration
verdict: "NEGATIVE_CATEGORY_CHANGE_STRESS_CASE"
---

# Distler-Garibaldi Functor Audit

## 1. Question

Test whether the unified frame

> no-go theorem = obstruction on the forgetful image of a richer substrate invariant

genuinely applies to Distler-Garibaldi (DG), or whether DG is a clean stress case where
the working "evasions" change category rather than compute a lossy shadow.

This note is bounded. It does not update the shared coordination docs. It only audits the
functor shape suggested in `canon/no-go-class-relative-map.md` section 2.4 against the
Type II_1 and Y14 generation-count lanes.

## 2. Source Basis

Read for this audit:

- `canon/no-go-class-relative-map.md`, especially section 2.4 and the ranked DG stress test.
- `literature/03-assumption-decomposition-no-go-evasion-literature.md`, DG section.
- `literature/04-spectral-triples-anomaly-chirality-distributed-systems-analogies.md`, DG and Type II_1 sections.
- `NEXT-STEPS.md`, especially Type II1, PC1/PC2/PC3, SC1, and generation-count updates.
- Type II_1 notes: `canon/type-ii1-spectral-sm-checklist.md`, `specifications/six-axis/examples/example-01-type-ii1-spectral-sm.md`, and `specifications/type-ii1-spectral-sm/*`.
- Y14 / generation-count notes: `explorations/pc1-spin77-spinor-decomp-2026-06-23.md`, `explorations/pc2-met-x4-bundle-formalization-stub-2026-06-22.md`, `explorations/generation-count-cl95-dirac-derham-2026-06-22.md`, `explorations/generation-count-sm-branching-closure-2026-06-22.md`, `explorations/discrete-series-fiber-dirac-index-2026-06-23.md`, `explorations/n5-discrete-series-gl4r-2026-06-23.md`, and `explorations/signed-readout-oq2d-gu-contact-2026-06-23.md`.

## 3. DG Target Category

A minimal target category for DG is:

```text
DG_E8
```

Objects are tuples

```text
(E, i_L, G, Lie(E) = sum V_{m,n})
```

where:

- `E` is complex `E8` or a real form of `E8`;
- `i_L: SL(2,C) -> E` is the Lorentz embedding;
- `G` is connected, compact, and centralizes `i_L(SL(2,C))`;
- `Lie(E)` is decomposed under `SL(2,C) x G`;
- the low-spin condition asks `V_{m,n}=0` for `m+n>4`;
- the chirality condition asks `V_{2,1}` to be complex as a `G`-representation.

Morphisms should at least be conjugacies or isomorphisms preserving the Lorentz embedding
and compact centralizer data. The DG theorem says the full subcategory satisfying all
ToE conditions inside one `E8` is empty.

This matters: a proposed forgetful functor into DG must land in this category, not merely
in "some representation category with an `E8` label."

## 4. What A Successful Forgetful-Image Reading Would Need

For DG to match the Witten / Nielsen-Ninomiya / Freed-Hopkins pattern, there should be a
non-arbitrary functor

```text
F_DG: C_rich -> DG_E8
```

such that:

1. `C_rich` contains known broader constructions, for example heterotic `E8 x E8`
   compactifications, a Type II_1 spectral triple, or a Y14 Dirac-DeRham object.
2. `F_DG` is canonical enough to be functorial under natural isomorphisms of the source.
3. The physically relevant chirality or generation invariant has a meaningful shadow in
   `DG_E8`.
4. If two source objects have the same `F_DG` image, then their DG-relevant chirality
   content should not differ for reasons entirely invisible to the image.

Condition 4 is the useful stress criterion. If generation count varies while the
single-`E8` branch table is fixed, then the generation invariant does not factor through
the DG shadow.

## 5. Candidate 1: Heterotic `E8 x E8` Collapse

The most tempting source category is a marked heterotic compactification category:

```text
Het_E8xE8^marked
```

Objects might be

```text
(X, V_vis, V_hid, W, flux, Wilson-line data)
```

where `X` is a Calabi-Yau threefold, `V_vis` is a visible-bundle choice inside one marked
`E8`, and the compactification data determine a four-dimensional spectrum.

A weak collapse functor exists only after adding a marking:

```text
U_branch: Het_E8xE8^marked -> Branch(E8)
U_branch(X,V_vis,...) = Res_H^{E8}(248)
```

where `H` is the commutant of the bundle structure group inside the marked visible `E8`.

This is a real coarse branch-table operation, but it is not a DG functor:

- The target is `Branch(E8)`, not `DG_E8`, because Lorentz `SL(2,C)` is external to the
  heterotic gauge `E8`, not embedded inside it as DG requires.
- The operation depends on choosing a visible `E8`; the exchange automorphism of
  `E8 x E8` shows the unmarked version is not canonical.
- The data producing chirality are bundle cohomology, Chern classes, Wilson lines, and
  compactification geometry, not the `248` branch table alone.
- Two compactifications can have the same visible branch pattern but different bundle
  indices and hence different net generation counts.

Therefore the generation invariant

```text
gen_Het(X,V_vis) = index/cohomology count of the compactification
```

does not factor through `U_branch`. At best:

```text
Het_E8xE8^marked -> 4D EFT data
```

is a compactification/readout functor. DG is not a theorem about that target category.

## 6. Candidate 2: GraviGUT / Larger Finite Lie Group

For `SO(3,11)`-style GraviGUT objects, the source category is already a different
finite-dimensional Lie-group category:

```text
Rep(SO(3,11)) or related larger-group data
```

There is no canonical functor to `DG_E8` unless one supplies an embedding into a real form
of `E8`; that is exactly the missing and obstructed structure. A forgetful operation that
just says "forget the group and compare dimensions" is not functorial representation
theory and does not preserve the Lorentz-centralizer data DG tests.

Verdict: this is a group-change evasion, not a forgetful-image case.

## 7. Candidate 3: Kac-Moody / `K(E10)` Truncation

For a `K(E10)` or infinite-dimensional Kac-Moody source, one can imagine a truncation to
finite levels or a distinguished finite subalgebra. But the needed map would have to land
in the adjoint of one real `E8` with the DG Lorentz-centralizer conditions.

No such canonical truncation is established in the local notes or literature review. More
importantly, the claimed physics in these constructions lives in level structure,
quotients, or infinite-dimensional symmetry data. Collapsing to one finite `E8` adjoint
forgets the category in which the construction works.

Verdict: this is another category collapse, not a DG shadow.

## 8. Candidate 4: Type II_1 Spectral SM

The Type II_1 lane is explicitly single-axis heterodox in L1. It replaces the finite
internal algebra with a Type II_1 / subfactor spectral-triple object. Its candidate
generation mechanism is principal-graph or standard-invariant data, with the finite
Connes-Chamseddine Standard Model as the control shadow.

The relevant forgetful operation is not `F_DG`. It is closer to:

```text
U_Connes: TypeII1SpectralData -> finite/smooth Connes-channel anomaly data
```

This is why the Type II_1 checklist naturally interacts with Freed-Hopkins compatibility:
the Connes-channel pairing is conjectured to forget L1 enrichment and land in ordinary
smooth anomaly constraints.

It does not land in `DG_E8`:

- There is no single real `E8` object.
- There is no Lorentz subgroup embedded in one `E8`.
- The candidate generation data are subfactor / trace / KO-theoretic data, not `E8`
  adjoint branching.

Verdict: Type II_1 sidesteps DG by changing the unit of internal structure. That is a
valid class exit, but not a forgetful-image realization of DG.

## 9. Candidate 5: Y14 / Dirac-DeRham-Einstein Generation Count

The Y14 lane supplies a more concrete local comparison because it has an actual
forgetful/pullback shape:

```text
Y14Data = (Y=Met(X), gimmel metric, S=H^64, D_GU, A, section s)
```

and a section-pullback / Riemannian-reduction operation:

```text
U_s: Y14Data -> 4D Clifford/SM-charge data on X
```

The generation-count notes put the mechanism in:

- `S(6,4) = C^16`, whose maximal compact `Spin(6) x Spin(4) ~= SU(4) x SU(2) x SU(2)`
  gives one Pati-Salam generation.
- A conditional index target `ind_H(D_GU)=24`, interpreted as three SM generations via
  8 quaternionic lines per generation.
- A relative discrete-series / Atiyah-Schmid count, currently reconstruction-grade and
  still gated by noncompact/discrete-spectrum verification.

This is a coherent candidate forgetful-image story for Witten-style chirality, because
`U_s` forgets noncompact metric-fiber and Dirac/Clifford data to produce a 4D shadow.

It is not a DG story. The target is a Clifford/operator/geometric category, not `DG_E8`.
PC1 strengthens this point: there is no natural equivariant map

```text
S -> Lambda^k(R^14)
```

for the relevant spinor module into pure exterior form data. The spinor remains an
additional coefficient object in `Omega^* tensor S`; it is not absorbed into a single
ordinary exterior/bundle category, much less into one `E8` adjoint.

Verdict: Y14 supplies a forgetful-image candidate for a different no-go row, not a
single-`E8` DG shadow.

## 10. Negative Result

No honest functor was found:

```text
F_DG: C_rich -> DG_E8
```

from the relevant richer categories such that DG becomes an obstruction on the
forgetful image of the same chirality/generation invariant.

The strongest precise negative statement is:

> For the known broader constructions, the physical chirality/generation invariant does
> not factor through single-`E8` adjoint branching data.

For heterotic compactifications, the obstruction is explicit: bundle/cohomology data can
change the net chiral spectrum while the coarse visible `E8` branch table is unchanged.
For Type II_1 and Y14, the obstruction is categorical: their invariants live in subfactor /
spectral-triple / Clifford / relative-discrete-series categories and have no canonical
single-`E8` target.

## 11. What Can Be Salvaged

A weaker category-collapse operation can be named:

```text
C_rich -> CoarseBranchData
```

Examples:

- heterotic marked visible `E8` branch table;
- finite approximation of a Type II_1 spectral triple;
- section-pullback of Y14 Dirac/Clifford data to 4D SM-charge data.

But `CoarseBranchData` is not `DG_E8`, and the collapse is not invariant-preserving for
generation count. It forgets too much: not just the mechanism, but the category in which
the mechanism is defined.

This is different from the Witten / Nielsen-Ninomiya / Freed-Hopkins rows. There the
richer datum is near the theorem's target class: singular geometry to smooth geometry,
bulk-boundary data to a boundary lattice, enriched bordism to ordinary bordism. In DG,
the broader successes change the mathematical unit itself.

## 12. Verdict

**DG is a category-change stress case, not a forgetful-image case.**

The canon row's cautious language should stand. The best formalization is:

```text
DG theorem = correct obstruction inside DG_E8
known successes = objects in other categories
collapse to one E8 adjoint = destroys the chirality/generation invariant
```

The unified frame should therefore carve out DG explicitly:

- DG is not falsified by heterotic, GraviGUT, Kac-Moody, Type II_1, or Y14 lanes.
- Those lanes avoid DG by not being objects of `DG_E8`.
- Any future claim that the unified no-go map "handles DG" must exhibit a functor into
  `DG_E8` and prove the chirality/generation invariant factors through its image.

## 13. Failure Conditions For This Negative Verdict

The negative verdict would be overturned by any one of the following:

1. A canonical functor from heterotic `E8 x E8` compactifications to `DG_E8` that includes
   Lorentz `SL(2,C)` inside one real `E8` and preserves net chirality/generation content.
2. A proof that the heterotic generation index is determined solely by single-`E8` adjoint
   branching data.
3. A Type II_1 or Y14 construction whose smooth shadow is naturally a DG object, not merely
   a 4D EFT or spectral-triple object.
4. A revised DG-target category, accepted as the theorem's actual domain, in which product
   groups, bundle cohomology, or Clifford coefficient spinors are already part of the
   objects. This would be a theorem change, not a proof that the original DG theorem was a
   forgetful-image case.

None of these is present in the local corpus reviewed here.


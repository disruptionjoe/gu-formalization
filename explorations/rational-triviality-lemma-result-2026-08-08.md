---
artifact_type: exploration_result
created: 2026-08-08
status: FIBRE_RATIONALLY_INVISIBLE__WILSON_AND_FIBRE_FLUX_EXCLUDED__RA_D2_NEGATIVE_CONTROL_SUPPLIED
grade: "EXACT for what it computes. tests/rational_triviality_fibre_index_lemma.py
  is green and derives the integral homology of RP^3, S^2 and CP^1 from CW
  boundary matrices by Smith normal form -- no cohomology is hard-coded. Three
  standard ingredients (flat => torsion Chern classes; Atiyah-Singer; free-action
  G-index localisation) are INVOKED and not re-derived, and the certificate says
  so in its own docstring."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/five-lens-analytic-council-2026-08-08.md
  - explorations/c1-domain-moduli-result-2026-08-08.md
---

# The rational-triviality lemma: GU's fibre cannot create a rational index

## Computed

```text
RP^3 integral homology, by Smith normal form on the CW boundary matrices
  H_0 = Z        H_1 = Z/2        H_2 = 0        H_3 = Z
  rational Betti numbers (1, 0, 0, 1)
  H^even(RP^3;Q) above degree 0 : NONE

CONTROL -- S^2 = CP^1
  rational Betti numbers (1, 0, 1)
  ind(D twisted by O(n)) = n + 1 : ..., -1: 0, 0: 1, 1: 2, 2: 3, ...
  flux MOVES the index. THE CONTROL FIRES.
```

## The lemma

`H^even(F;Q) = Q`, concentrated in degree 0, where `F = GL(4,R)/O(3,1) ~ RP^3`.
Therefore:

1. **No vertical characteristic class of positive even degree exists**, so fibre
   integration of `ch . A-hat` has nothing to integrate.
2. **Wilson lines cannot chiralise.** A flat datum has torsion Chern classes, so
   `ch(L) = rk(L)` rationally and `ind(D_{E (x) L}) = rk(L) . ind(D_E)`. Index
   zero in, index zero out. Independently, GU's canonical `Z/2` is the deck
   transformation of `S^3 -> RP^3` and acts **freely**, so the `G`-index localises
   on an empty fixed set.
3. **Fibre flux does not exist.** `H_2(RP^3;Z) = 0` and `H^2(RP^3;Z) = Z/2` is
   pure torsion, so there is no 2-cycle to quantise over and any torsion class has
   zero Chern character.

**Consequence: the fibre can multiply a base index; it can never create one.**

Wilson lines and fibre flux move from *unexplored escapes* to *excluded*.

## The control, and why it matters

`RA-D2` has never carried a firing negative control — recorded as a defect on
2026-08-07, where the proposed control was to build a parent whose halves are not
conjugate reps.

This is a better one, because it tests the **class** statement rather than the
mass argument. The identical lemma **fails** on a fibre with even-degree rational
cohomology: on `CP^1` the line bundle `O(n)` has `ch_1` integrating to `n`, and the
twisted Dirac index is `n + 1`, so the flux route fires immediately. The
certificate computes both sides.

So the lemma is a statement about **GU's fibre specifically**, not a vacuous
generality — which is exactly what a firing control is for.

## The elegance worth recording

GU's fibre **is** the free quotient. That is why it is `RP^3` and not `S^3`. The
same structure that makes a Wilson line *available* — `pi_1(F) = Z/2` is real and
unconditional — is the structure that makes it *powerless*, because a free action
has no fixed points for the `G`-index to localise on.

The repository had already computed two instances of this without naming the
theorem: flat `S(6,4)` on `S^3` gives `eta = 0` and `ind_APS = 0`, and a full SM
generation coupled to a flat `Z_3` Wilson line gives mod-3 phase `0`.

## What this does NOT close

- **Orbifold projection.** Excluded separately and for a different reason: GU's
  canonical `Z/2` acts freely, and building a fixed-point involution requires a
  preferred timelike line, i.e. a metric, i.e. the section GU declines to fix.
  Not covered by this lemma.
- **The index/zero-mode route.** It survives as a *type*. Its realisations fail
  for separate reasons — `pi_!` undefined on a non-compact 10-dimensional fibre,
  `SL(4,R)` has no discrete series, and the base-side realisation imports the
  number.
- **Base flux.** Exists, works, and is already canon's **external** datum
  (`canon/external-topological-index-flux-RESULTS.md`), where the odd count
  "enters ONLY through the external topological background" and the flux
  background breaks the interior Krein class. Not a new lane.

## Owed, and not done here

`RA-D2`'s evasion column should be populated with all four routes **and their
exclusions**, which converts its negatively-phrased revival trigger — "an exact
chiral physical carrier not obtained by equivariant mass splitting" — into a
**closed enumeration**. That is a ledger row change and takes the proper path; it
is not made by this artifact.

With that populated, `RA-D2` reads closer to a **class kill** than a mechanism
kill: mass/VEV excluded by index zero, Wilson lines and fibre flux by this lemma,
orbifold by the free action, and the index route surviving only as a type with no
GU-side realisation.

---
title: "External Quadratic-Gravity Papers: Obligations for GU"
status: exploration
doc_type: exploration-note
updated_at: "2026-06-30"
---

# External Quadratic-Gravity Papers: Obligations for GU

Exploration note, 2026-06-30. Source: a Joe-fed reading set of three external GR/QG papers, assessed against
the Church-of-AI repos via an inline persona/council pass. This note records only what is GU-facing.

**Posture compliance.** These papers are **external calibration targets and obligations to attack**, never
evidence for GU. Nothing here is a derivation, a compatibility-as-derivation, or a credibility transfer. The
move is the posture's own: manufacture a falsifiable obligation, drive it to a verdict, keep what survives.

## Source papers

1. **Tzanavaris, Boyle, Turok**, *The free boundary problem in general relativity*, arXiv:2606.18128 (2026).
   Treats a singularity as a free boundary; stationarity under unconstrained variation **derives** an on-shell
   boundary condition (a computable filter excluding Kasner/BKL, admitting conformally-regular FLRW). Tetrad
   formalism, Lovelock, GHY+Myers, Chern-Gauss-Bonnet.
2. **K.S. Stelle**, *Renormalization of higher derivative quantum gravity*, Phys. Rev. D 16, 953 (1977).
   Curvature-squared gravity is **renormalizable**, at the cost of a massive spin-2 **ghost** (negative norm)
   that breaks **unitarity**. The canonical renormalizability-vs-unitarity no-go.
3. **Avramidi, Barvinsky**, *Asymptotic freedom in higher-derivative quantum gravity*, Phys. Lett. B 159, 269
   (1985). One-loop counterterms of the unique effective action; quadratic gravity is **asymptotically free**
   (Euclidean positive-definite case), and they float restoring unitarity via radiative corrections + positivity.
   See also `explorations/rg-universality/`.

## Obligation 1 (rigor bar, from paper 1): derivations must terminate in a checkable filter

The free-boundary paper's payload is a derivation that ends in a **computable, class-separating filter**: it
names what it excludes (Kasner/BKL), what it admits (FLRW, 0 <= w < 1), and an on-shell finiteness check
(stiff fluid w=1 killed by non-finite action). That is the shape of a result whose correctness can be
**checked rather than asserted** -- precisely the layer where GU's verification has historically failed (the
w2-y14 spin claim was asserted, then verified wrong; prose-checking tests could not catch it).

**Rigor rubric to apply internally** (re-score existing GU tests against it):
- (a) does the derivation terminate in a *computable* filter, not a prose claim?
- (b) does the filter state its excluded class *and* its admitted class explicitly?
- (c) is an on-shell finiteness / well-definedness check performed, not assumed?

The tetrad / boundary-term bookkeeping in paper 1 (GHY+Myers, Chern-Simons forms) is a known-correct
**reference calculation**: when a GU sub-derivation touches tetrad boundary terms, diff its *steps* against the
paper to catch sign/contraction/corner errors. This checks method only; it confers no validity on any GU
conclusion.

## Obligation 2 (the residual, from papers 2+3): GU's prize cannot be "UV-respectable gravity"

This is the sharp, cumulative finding. Stelle + Avramidi-Barvinsky together establish that **plain
curvature-squared gravity already secures renormalizability *and* asymptotic freedom -- with none of GU's
machinery.** Therefore:

- GU's differentiator **cannot** be "a UV-sensible higher-curvature gravitational action." That prize is
  already claimed by a far simpler theory.
- GU's richer structure must justify itself on the **residual** problems that quadratic gravity does *not*
  solve: the **ghost / unitarity** pathology (Stelle), or the **derivation of matter content / the specific
  bundle structure** (which quadratic gravity does not supply).
- Avramidi-Barvinsky shows the *form* a credible ghost-cure argument takes: tie unitarity to Euclidean
  positivity and radiative running, computed explicitly. Any GU claim to evade the ghost must walk through a
  door like this, or name precisely why GU's structure removes the negative-norm mode that local
  higher-derivative terms generate.

**Falsifiable obligation (attack, do not defend):** state, for the current GU reconstruction, whether its
effective gravitational sector incurs an Ostrogradsky / massive-spin-2-ghost cost. If it does, GU inherits
Stelle's unitarity problem and must address it; if it claims not to, the mechanism that removes the ghost is a
specified missing ingredient, on the same footing as the chiral-count gap. Either verdict is a success.

## Refusals

- One-way, method-level. These papers anchor GU's rigor bar and obligations; GU claims never cite them as
  support, and they are never used as connective tissue between GU and time-as-finality / temporal-issuance.
- No credibility laundering: sharing the differential-geometry toolbox (tetrad, Lovelock, heat-kernel) with a
  rigorous result confers no rigor on GU's particular contractions. A correct reference calculation makes GU's
  errors *more* visible, not less.

## Candidate next actions

- Re-score 2-3 existing GU tests against the Obligation-1 rubric; record which assert vs. check.
- Open a lead-hypothesis-style entry for Obligation 2 (ghost/Ostrogradsky audit of the current effective
  gravitational sector), driven to a verdict like any other.

---
title: "The external topological datum carries the odd chiral count: a 2D magnetic-flux Wilson-Dirac has net chiral index = flux number (Aharonov-Casher / Atiyah-Singer), odd for odd flux -- computed + independently re-verified. This completes the boundary/APS side of WC-FUNCTION-SPACE-EXT: the interior/closed cross-chirality Krein-Dirac sector is forced EVEN (2-primary), and the ODD count enters only through an external topological background (flux / instanton number), which is ANY integer -- NOT 2-primary-constrained and NOT a selection of 3. This decisively realizes and concretizes the paper's 'external on present evidence -- supplied by a net-self-dual chiral background' conclusion."
status: staged
doc_type: result
created: 2026-07-02
grade: "computed + INDEPENDENTLY RE-VERIFIED on the explicit lattice: net chiral index = flux number Phi for Phi = 0..3 (main, 16x16) and Phi = 0..6 across sizes 20x20, 24x24 (independent check), including odd Phi = 1,3,5 (odd index). Standard Aharonov-Casher / Atiyah-Singer index theorem (index = magnetic flux number) realized on a 2D Wilson-Dirac torus; NOT novel mathematics -- its value is decisively CONFIRMING and CONCRETIZING the paper's external mechanism and pinning its parity. Internal tier (caveat (e))."
addresses: "the boundary/APS side of WC-FUNCTION-SPACE-EXT; the paper's 'external on present evidence' conclusion (Section: the count is external, supplied by instanton zero-modes / flux / K3)."
depends_on:
  - canon/function-space-index-conservation-RESULTS.md
  - explorations/analytic-index-fredholm/external-chiral-background-parity-2026-07-02.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
scripts:
  - tests/function-space-ext/flux_index_2d.py
  - tests/function-space-ext/verify/flux_index_2d_indep_check.py
---

# The external topological datum carries the odd chiral count (index = flux)

## The full arc (three computed facts)

1. **Interior (v2.8):** in the cross-chirality Krein-Dirac class every self-adjoint, chirality-odd,
   Krein-self-adjoint Fredholm family has net chiral spectral flow 0 -- the interior is
   chirality-balanced (2-primary, even). (`canon/function-space-index-conservation-RESULTS.md`.)
2. **Closed parity:** on a closed 1D circle any real background's domain walls pair off into
   opposite chiralities; a closed 1D manifold hosts no odd net count -- the interior 2-primary
   balance is genuinely an *interior* phenomenon.
   (`explorations/analytic-index-fredholm/external-chiral-background-parity-2026-07-02.md`.)
3. **External topological datum (this note):** a 2D magnetic-flux Wilson-Dirac has net chiral
   zero-mode count **= the flux number** (Aharonov-Casher / Atiyah-Singer). Odd flux gives an ODD
   count. The interior/closed sector provably cannot host this; the external topological background
   does.

## The computation

`tests/function-space-ext/flux_index_2d.py` (7 asserts, exit 0): a 2D Wilson-Dirac on an `Lx x Ly`
torus, uniform magnetic flux `Phi` (Landau gauge `A_y = 2*pi*Phi*nx/(Lx*Ly)` with the x-seam twist
`exp(-i 2*pi*Phi*ny/Ly)`), `D = sigma_1 (x) T_x + sigma_2 (x) T_y + sigma_3 (x) (r*Wilson)`,
`Gamma = sigma_3 (x) I`, cross-chirality `K = sigma_1 (x) I`. Result (16x16):

| flux Phi | net chiral index | parity |
|---|---|---|
| 0 | 0 | even |
| 1 | -1 | **ODD** |
| 2 | -2 | even |
| 3 | -3 | **ODD** |

All zero modes share one chirality (Aharonov-Casher); `|index| = Phi` exactly. The flux background
breaks the interior Krein-self-adjoint class (Krein violation ~1.9). **Independent re-check**
(`verify/flux_index_2d_indep_check.py`, 7 asserts, exit 0): `index = flux` across sizes 20x20 and
24x24 and flux up to 6, including odd `Phi = 1,3,5`.

## What this settles (and what it does not)

- **The odd count enters only externally, and it is not 2-primary-constrained.** The interior is
  forced even; the odd chiral count is a topological index (flux / instanton number), which is ANY
  integer. This is the clean, decisive realization of the paper's "external on present evidence --
  supplied by a net-self-dual chiral background (instanton zero-modes, flux, K3/CY)" conclusion.
- **It does NOT single out 3.** The external index is the flux/instanton number, any integer; `Phi`
  odd gives an odd count, but nothing here privileges 3 over 1, 5, 7, ... Fully consistent with the
  paper explicitly not claiming three.
- **Honest grade.** This is the STANDARD index theorem (index = flux), computed on the lattice and
  independently re-verified; not new mathematics. Its contribution is to close the boundary/APS side
  of the WC-FUNCTION-SPACE-EXT story at computed grade and to pin the parity: interior even,
  external any-integer. The remaining genuinely-open analytic item is the full APS/noncompact-end
  and family-index statement for the actual Rarita-Schwinger operator (the residual named in
  `canon/function-space-index-conservation-RESULTS.md`); the 2D flux torus is a faithful realization
  of the mechanism, not that RS operator.

## Paper relevance (pauses for Joe)

The paper's "external" discussion already cites instanton zero-modes / flux / K3 as the mechanism.
This note lets that sentence, if Joe wants, gain a one-line pointer: the external route is a
topological index (flux/instanton number), explicitly = any integer, computed here -- confirming it
is not 2-primary-constrained and does not single out 3. **Not applied to the paper** (staged, not
CANON.md-promoted; paper edits pause for Joe). No number was fitted; the only integers are the flux
numbers and their equal chiral indices.

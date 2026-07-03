---
title: "The generation count is external BY STRUCTURE (not merely on present evidence): a synthesis theorem. In the Clifford Rarita-Schwinger sector the net chiral generation count decomposes as (sector-interior contribution) + (external topological index). The interior contribution is provably EVEN / 2-primary -- Theorem 1 (no enumerated obstruction is an odd-prime congruence; enum-complete for the delimited class C), Theorem 2 (linear Krein-isometric index conservation, symbolically proved), and the antilinear null-eigenspace bound (no admissible antilinear re-grading forces an odd count, symbolically proved). The external contribution is a topological index (flux / instanton number, APS boundary eta) that equals ANY integer (computed: 2D flux Dirac has index = flux). THEREFORE any ODD generation count is NECESSARILY external: 'located, not forced' upgrades from an evidence claim to a structural decomposition -- the interior cannot supply an odd count over the complete delimited class, and the count is a boundary/topological datum. This does NOT derive three; the external index is any integer and nothing privileges 3."
status: staged
doc_type: result
created: 2026-07-02
grade: "SYNTHESIS THEOREM assembling separately-verified components. INTERIOR-EVEN: proof-grade / symbolic for the core (index-nullity, antilinear null-eigenspace, 2-primary obstruction identities -- canon/core-theorems-symbolic-proof-RESULTS.md), computed-grade + engine-swept for the exhaustion of the class (canon/enum-completeness-class-c-RESULTS.md). EXTERNAL-INDEX: computed + independently re-verified (index = flux, canon/external-topological-index-flux-RESULTS.md). DECOMPOSITION COMPLETENESS: rests on the class-C enum-completeness (computed grade, delimited class). Honest residual: the full function-space Rarita-Schwinger APS/end + family-index statement is NOT closed (canon/function-space-index-conservation-RESULTS.md); the synthesis is 'external by structure' MODULO that analytic residual. NOT a derivation of 3, and internal tier (caveat (e))."
depends_on:
  - canon/core-theorems-symbolic-proof-RESULTS.md
  - canon/enum-completeness-class-c-RESULTS.md
  - canon/antilinear-bound-RESULTS.md
  - canon/antilinear-nonkrein-admissibility-RESULTS.md
  - canon/function-space-index-conservation-RESULTS.md
  - canon/external-topological-index-flux-RESULTS.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
---

# The generation count is external by structure (a synthesis theorem)

The paper's verdict is "located, not forced -- external on present evidence." "On present evidence"
was the honest hedge: perhaps some unexamined interior route could still force an odd count. Three
results proved / computed in this program now let that hedge tighten to a structural statement.

## The decomposition

For the net chiral generation count `chi` of the Clifford Rarita-Schwinger sector (real `Cl(p,q)`,
`p+q=14`, the `j=1` triplet carrier with its cross-chirality `(+96,-96)` Krein form), write

> `chi = chi_interior + chi_external`,

where `chi_interior` is the contribution of every structure the sector supplies from its own data
(covariant / equivariant operators, forms, indices, characteristic classes of its spin / gauge /
boundary / ghost data -- the delimited class C), and `chi_external` is the contribution of a
topological background not internal to the sector (a chiral flux / instanton / APS boundary datum).

## Theorem (external by structure, modulo the function-space residual)

**(I) `chi_interior` is even (2-primary).** Three independent, separately-verified legs:

1. **Enumeration is complete and 2-primary (Theorem 1).** The 7-item obstruction list is complete for
   the delimited class C (computed grade, engine-swept, boundary sharp), and every generator is
   2-primary -- no sector-interior structure imposes an odd-prime (mod-3) congruence
   (`enum-completeness-class-c-RESULTS.md`). Symbolically, each obstruction is a power-of-two
   statement (`core-theorems-symbolic-proof-RESULTS.md`).
2. **Linear index conservation (Theorem 2).** Every linear Krein-isometric operator conserves the
   net chiral index at 0; proved from the axioms of a cross-chirality Krein space
   (`core-theorems-symbolic-proof-RESULTS.md`).
3. **Antilinear null-eigenspace bound.** No admissible antilinear re-grading (the whole
   null-eigenspace class, strictly larger than the Krein-compatible operators) forces a nonzero
   count; symbolically proved via the same transversality (`antilinear-nonkrein-admissibility-RESULTS.md`,
   `core-theorems-symbolic-proof-RESULTS.md`).

**(II) `chi_external` is a topological index equal to ANY integer.** A chiral topological background
carries net chiral count = its flux / instanton number (Aharonov-Casher / Atiyah-Singer), computed
and independently re-verified as `index = flux` for flux `0..6` including odd `1,3,5`
(`external-topological-index-flux-RESULTS.md`). Such a background breaks the interior Krein-self-adjoint
class -- exactly why it lies outside (I).

**Corollary.** Since `chi_interior` is even and the only source of an odd contribution is
`chi_external`, **any ODD generation count is necessarily external**. The interior of this sector
provably cannot supply it over the complete delimited class. "Located, not forced" is thus a
structural decomposition, not merely an evidential one: the interior is even; an odd count is a
boundary / topological datum.

## What this does and does not do

- **Upgrades the verdict's modality.** From "external on present evidence" (an inductive hedge over
  routes tried) to "external by structure" (the interior is proved even over the *complete* delimited
  class; the odd count is provably a topological/boundary index). This is the strong-firewall reading
  the program targets -- in the honest, delimited form, not the dead over-strong form.
- **Does NOT derive three.** `chi_external` is the flux / instanton number, ANY integer; nothing here
  privileges 3 over 1, 5, 7. The paper's "we do not claim three" is untouched and reinforced: three,
  if realized, is external data of the same kind that produces chirality in known chiral theories.
- **Honest residual (the one open gap).** The completeness of the interior class and the
  interior-even proofs are at computed / symbolic grade for the finite-dimensional structural sector;
  the full function-space **Rarita-Schwinger APS / noncompact-end + family-index** statement is the
  one genuinely open analytic item (`function-space-index-conservation-RESULTS.md`). So the synthesis
  is "external by structure **modulo** the RS function-space residual." Closing that residual would
  make the structural verdict unconditional.

## Grade and status

Synthesis theorem over separately-verified components (symbolic/proof-grade interior core; computed +
engine-swept class-C completeness; computed + re-verified external index=flux). Internal tier
(caveat (e)); no external replication. **Staged, NOT CANON.md-promoted.** Paper relevance: this would
let Section 9 / the status table upgrade "external on present evidence" to "external by structure
(interior provably even over the complete class; the odd count is a boundary/topological index),
modulo the RS function-space residual" -- **pauses for Joe** (paper edits and CANON promotion are his
call). No number was fitted; the only integers are `0`, `(+96,-96)`, the 2-primary moduli, and the
external flux numbers.

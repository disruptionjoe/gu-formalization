# Proposed Zenodo metadata

- **Title:** A Diagonal No-Go for Self-Valuations and an Invariance Classification
- **Upload type:** Publication / Preprint
- **Creator:** Joe Hernandez
- **Affiliation:** Independent Researcher
- **Email:** joe@disruptionjoe.com
- **ORCID:** Not supplied; omit rather than infer
- **Publication date:** 2026-07-13
- **Version:** 1.0.0
- **Language:** English
- **Primary license:** Creative Commons Attribution 4.0 International (`CC-BY-4.0`)
- **Bundled code license:** MIT
- **Related identifier:** <https://github.com/disruptionjoe/gu-formalization> — code repository, relation “is supplemented by”
- **Funding:** None declared
- **Communities:** None preselected

## Description / abstract

Let A and B be sets. A valuation is a function from A to B, and a candidate self-enumeration is a function from A × A to B whose rows are intended to exhaust all valuations. Given a fixed-point-free map from B to B, we prove two elementary facts. First, no such candidate is weakly point-surjective, and for every candidate the associated diagonal valuation is absent from its rows. Second, if A is nonempty, no valuation is invariant under the fixed-point-free map. For a two-element codomain and the swap, the first fact is the Cantor–Lawvere diagonal argument and the second is a pointwise fixed-point observation. A group action on B also induces the standard classification of valuations as invariant or non-invariant; under the swap, every valuation lies in the latter class. This classification adds no selection theorem. Observer, admissibility, and symmetry-breaking language is offered only as interpretation. The contribution is a specific synthesis of known pieces, not a new fixed-point or symmetry theorem. The function-level core and its Boolean corollaries are machine-checked in Lean 4; the interpretive classification is not formalized.

## Keywords

- diagonal argument
- weak point-surjectivity
- valuation no-go
- invariance
- self-reference
- Lawvere fixed-point theorem

## Subject classification

- MSC 2020: 03E20 (primary); 18A15, 03A05 (secondary)
- Recommended arXiv category: `math.LO` primary
- No `math-ph` classification is claimed

## Notes for the depositor

Use `main.pdf` as the primary article file. The record-level license should be `CC-BY-4.0`; `LICENSE-CODE.md` preserves MIT terms for the bundled Lean and Python code. Do not mint or insert a DOI before Zenodo assigns one. ORCID is optional and should remain absent unless Joe supplies it directly.

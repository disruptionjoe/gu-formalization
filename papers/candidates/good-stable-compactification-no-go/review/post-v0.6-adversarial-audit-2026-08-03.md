---
title: "Post-v0.6 adversarial audit"
date: "2026-08-03"
status: "internal zero-actionable pass; clean external rerun still required"
---

# Post-v0.6 adversarial audit

This is one consolidated internal audit through divergent specialist lenses,
not a claim of independent external review.

| lens | attack | result |
|---|---|---|
| theorem quantifiers | Search the abstract, result table, theorem, specialization, and conclusion for a version of the extremal claim missing `dR(Z)` diagonalizability, the corresponding sign, or nonzero nilpotent `dι`-image. | Pass. Every summary carries all three conditions; the split-torus counterexample demonstrates their necessity. |
| representation theory | Try to make the proof exchange maximal/positive and minimal/negative assumptions or silently use both witnesses. | Pass. Theorem 3(3) and (4) are independent sign-specific clauses. |
| real Lie theory | Treat one real weight as full `ad`-hyperbolicity, or treat the three-grading as a novel depth-two grading. | Pass. The mixed split/elliptic distinction is explicit, and the specialization is identified as a standard `|1|` parabolic pattern. |
| quaternionic algebra | Reverse multiplication order, change the module side, or challenge the transformed block signs. | Pass. Side conventions are explicit; Sage checks 2,721 exact identities and the independent Python layer checks the division-free basis change. |
| Krein-space terminology | Read “majorant” as an undeclared infinite-dimensional topology or challenge the fundamental-symmetry converse. | Pass. The local finite-dimensional definition, domination inequality, equivariance, eta-self-adjointness, symmetry, positivity, and invariance are all proved. |
| prior art and novelty | Recast the grading decomposition as a new classification or use contextual papers as direct precedent. | Pass. Čap–Slovák and Draper–Meulewaeter locate the standard structure; Khare and Richardson–Slodowy are explicitly contextual; novelty remains synthesis/diagnostic. |
| reproducibility | Review only the Markdown and challenge present-tense claims about invisible files. | Pass with a packaging condition. The manuscript assigns no evidentiary weight to unavailable supplements and requires the complete checksum-locked tree in an archival package. |
| hostile editor | Search for duplicated caveats, GU leakage, physical-stability implications, or a title stronger than the theorem. | Pass. Scope is consolidated, the conclusion is compact, no GU dictionary remains, and the title stays within the compact-image result. |

## Internal saturation result

No additional current-paper hardening action was found. Remaining objections
would ask for a different theorem or successor paper: non-extremal
classification, infinite-dimensional Krein analysis, a physical realization,
or a GU-specific application.

The formal production contract still requires a clean hostile rerun against
v0.6 with the complete supplement set before this candidate can be called
post-ready.

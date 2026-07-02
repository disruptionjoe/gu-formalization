# Changelog v2.7 -- antilinear admissible-class strengthening (2026-07-02)

Trigger: adversarial-review criticism #2 (raised in two independent passes): the delimited antilinear class S
(Krein-compatible operators, `M^dag K M = lambda K-bar`) is an improvement, but "operators breaking Krein/ghost
compatibility fail admissibility" leaves a loophole -- could an operator evade S while still acting on the
physical chiral sector? Worked to a computed + independently re-verified result
(`canon/antilinear-nonkrein-admissibility-RESULTS.md`). Both copies edited in sync. **No core theorem, number,
or grade changed; the index-nullity theorem is unchanged -- only its stated scope is corrected (upward).**

## The result folded in

The index-nullity proof never used the full Krein condition; it used only that the re-graded chirality
eigenspaces `C(W_+), C(W_-)` are **K-null (Lagrangian)** -- the intrinsic mark of a *chirality* re-grading
(the original chirality's own eigenspaces `W_+/-` are K-null). So the admissible class is the strictly larger
**null-eigenspace class P_iso ⊋ S**, and index nullity holds on all of it. The paper's earlier residual
"outside the Krein class admissibility fails" was too strong (some non-Krein operators supply a valid chirality
and are still index-null); the correct residual is: a nonzero count requires a **K-definite** re-grading, which
is not a chirality (it grades physical-vs-ghost, carrying the vectorlike `+96`) and does not act on the physical
sector.

**Certificates.** `tests/antilinear-bound/nonkrein_physical_admissibility.py` (61 hard asserts: P_iso strictly
contains S -- non-Krein operators with K-null re-graded eigenspaces constructed, Krein residual order 1; index
nullity chi_C(P)=0 on P_iso as exact integer ranks; the K-definite re-grading carries +-96).
`tests/antilinear-bound/verify/nonkrein_indep_check.py` (69 hard asserts: independent re-check on OWN
recursive-doubling gammas + a different seed + `Cl(7,7)` cross-signature, with a Euclidean `(14,0)`
premise-failure control firing `|chi|=96`). Grade: computed + independently re-verified -- same as the main
bound.

## EDITS APPLIED (v2.7, both copies)

1. **Caveat (d)** (abstract front matter): "closed over a delimited class (every Krein-compatible antilinear
   operator ...); outside that class admissibility itself fails" -> "an index-nullity theorem holding on every
   antilinear operator whose re-graded chirality eigenspaces are K-null (strictly larger than the
   Krein-compatible operators; the proof uses only that isotropy), so a nonzero count would require a K-definite
   re-grading that is not a chirality."
2. **Abstract body**: the "every Krein-compatible ... outside that class admissibility fails" clause replaced by
   the null-eigenspace-class statement.
3. **Intro contribution item 3** (+ its grade tag): "all Krein-compatible antilinear operators" -> "the
   null-eigenspace class ... strictly larger than the Krein-compatible operators."
4. **Section 6**: added the paragraph explaining the class is strictly larger than Krein-compatible (proof uses
   only isotropy), the null-eigenspace class, and re-scoped the residual to the K-definite re-gradings; the
   bolded summary now reads "linear, or antilinear with K-null re-graded chirality eigenspaces."
5. **Status-table row**: "closed over the delimited Krein-compatible class; residual: non-Krein operators fail
   admissibility" -> "closed over the null-eigenspace class, strictly larger than Krein-compatible; residual: a
   nonzero count needs a K-definite non-chirality re-grading."
6. **Conclusion**: "the antilinear side closed over the delimited Krein-compatible operator class" -> "closed
   over the null-eigenspace class of re-gradings, strictly larger than the Krein-compatible operators."
7. **Version bookkeeping**: .tex header -> v2.7; .md version marker + version-history paragraph.

## NOT CHANGED

- The index-nullity theorem, Theorem 1, Theorem 2, the CRT structure, and every integer are untouched. This
  pass only widens the *stated admissible class* (from Krein-compatible S to the null-eigenspace class P_iso),
  which the existing proof already supported.
- Internal tier unchanged (caveat (e)); the result is computed + internally-re-verified, not externally
  replicated. `canon/antilinear-nonkrein-admissibility-RESULTS.md` is staged, **not CANON.md-promoted**.
- The honest residual is the same function-space open card (WC-FUNCTION-SPACE-EXT); the genuine QFT
  effective / non-perturbative half of #2 is NOT closed.

## STATUS

Publication remains **DEFERRED** (Joe). Both journal-gating cards are reflected in the paper (WC-ANTILINEAR-BOUND
v2.5.2 + this v2.7 strengthening; WC-ENUM-COMPLETENESS v2.6). Publication flips only on Joe's review and the
CANON.md-promotion decision.

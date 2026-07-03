---
title: "Reviewer #2 addendum to WC-ANTILINEAR-BOUND: the admissible class is not the Krein-compatible S but the strictly larger null-eigenspace class P_iso (antilinear operators whose re-graded chirality eigenspaces C(W_+), C(W_-) are K-isotropic); index nullity holds on ALL of P_iso, because the index-nullity proof used only isotropy, never the full Krein condition M^dag K M = lambda K-bar. Non-Krein members are constructed (Krein residual order 1, eigenspace isotropy < 1e-8) and are still index-null. A nonzero count requires a K-DEFINITE (non-null) re-grading, which is not a chirality (it grades physical-vs-ghost, carrying the vectorlike +-96) and does not act on the physical sector."
status: canon
canon_promoted_at: "2026-07-03"
doc_type: result
created: 2026-07-02
grade: "computed + INDEPENDENTLY RE-VERIFIED on the explicit carrier (main script 61 hard asserts; independent re-check tests/antilinear-bound/verify/nonkrein_indep_check.py 69 hard asserts, on OWN recursive-doubling gammas + a different seed + Cl(7,7) cross-signature, with a Euclidean Cl(14,0) premise-failure control firing |chi|=96 so the null-eigenspace hypothesis is load-bearing, not vacuous; exact-integer chi ranks throughout). The structural core -- a K-positive subspace meets a K-null subspace only at 0 -- is proof-shaped finite-dimensional linear algebra with machine-certified premises; same grade as the main bound. Two self-corrections were made during the pass and are recorded in Integrity below."
addresses: "adversarial-review criticism #2 (the delimited antilinear class still leaves loopholes: could an effective / non-perturbative operator evade the Krein-compatible class while still acting on physical chirality?)"
depends_on:
  - canon/antilinear-bound-RESULTS.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
script: tests/antilinear-bound/nonkrein_physical_admissibility.py
---

# The antilinear admissible class is P_iso (>> S), and index nullity holds on all of it

**Reviewer #2 (both adversarial passes).** The delimited class S (Krein-compatible antilinear
operators, `M^dag K M = lambda K-bar`) is an improvement, but "operators breaking Krein/ghost
compatibility fail admissibility" leaves a loophole: could an effective or non-perturbative
operator *evade the Krein class while still acting on the physical chiral sector*?

**Result (computed grade, finite-dimensional kinematics).** Yes, an operator can evade S -- and
it still forces nothing. The admissible class is not S; it is the strictly larger, intrinsic

> **P_iso := { antilinear `C = M . conj` : the re-graded chirality eigenspaces `C(W_+)`,
> `C(W_-)` are K-isotropic (K-null / Lagrangian) }  ⊋  S.**

This is the right class because it is the intrinsic mark of a *chirality* re-grading. The
original chirality `Gamma_c` already has K-**null** eigenspaces `W_+/-` (K is purely
cross-chirality: it pairs `W_+` with `W_-`). A re-grading "of the same kind" -- a chirality --
must likewise have K-null eigenspaces. That, and nothing more, is what the index-nullity theorem
needs.

## Why it holds on all of P_iso (the proof only ever used isotropy)

For any physical (maximal K-positive) subspace `P` and any `C` in P_iso: `C(W_+)` and `C(W_-)`
are K-null, and a K-positive vector cannot be K-null, so `P ^ C(W_+) = P ^ C(W_-) = 0`. Hence the
net re-graded chiral index `chi_C(P) = dim(P ^ C(W_+)) - dim(P ^ C(W_-)) = 0 - 0 = 0`. The full
Krein condition `M^dag K M = lambda K-bar` is never used -- only isotropy of the two images. So
the theorem that was stated for S actually holds on the much larger P_iso.

## What the script certifies (`tests/antilinear-bound/nonkrein_physical_admissibility.py`, 61 asserts, exit 0)

- **(B) P_iso strictly contains S.** Non-Krein operators are constructed whose re-graded
  chirality eigenspaces are an arbitrary complementary pair of K-Lagrangians (the Lagrangian
  Grassmannian -- vastly larger than the S-orbit): Krein residual `= 1.00` (order 1, not in S),
  eigenspace isotropy `~ 2e-14`. A chirality re-grading need not be Krein-compatible.
- **(C) Index nullity on P_iso.** Every constructed non-Krein member gives `chi_C(P) = 0` on
  every physical subspace, as **exact integer ranks** (`[0,0,0,0]` across the batch).
- **(D) The null condition is the load-bearing boundary.** A re-grading whose eigenspaces are
  K-**definite** (e.g. the K-positive / K-negative split) is *not* a chirality -- it grades
  physical-vs-ghost norm -- and it is exactly this that carries the **vectorlike `+-96`** (raw
  index `[96,0,0,0]`). Such an operator also fails to act on the physical sector: it maps a
  physical subspace to a K-indefinite (non-physical) image (Gram range order `+-600`). So a
  nonzero count requires *abandoning chirality* (a non-null re-grading), not merely abandoning
  Krein-compatibility.

## What this changes for the paper (pauses for Joe)

The paper's caveat (d) residual can sharpen from "non-Krein operators fail admissibility (a
computed control)" to the stronger, intrinsic statement: **the admissible class is the
null-eigenspace class P_iso, strictly larger than the Krein-compatible S, and index nullity holds
on all of it; escaping requires a K-definite re-grading, which is the vectorlike physical-vs-ghost
grading, not a chirality.** This is a one- or two-sentence refinement of caveat (d) / Section 6.
**Not applied to the paper here** (paper edits pause for Joe; this note is staged, not
CANON.md-promoted).

## Honest residual (unchanged)

This is finite-dimensional kinematics on the explicit carrier. A genuine QFT effective /
non-perturbative operator lives in the function-space setting, where "physical / K-definite
subspace" and the chirality grading are subtler -- the separate open card WC-FUNCTION-SPACE-EXT,
not closed here. What #2 asks at the kinematic level is answered: admissibility is P_iso (`>> S`),
and index nullity holds on all of it.

## Integrity (self-corrections recorded, not hidden)

1. A first draft asserted "isotropic images ⟺ the induced grading `Gamma_C` is a K-cross-chirality
   operator." That is FALSE: isotropy is a condition on the Krein *form* (`E^dag K E = 0`);
   operator-anticommutation is a *similarity* condition; they are not equivalent. Caught by a
   failing assert. The surviving statement uses only isotropy of the images -- which is exactly
   (and only) what the index-nullity proof needs.
2. The induced grading is `Gamma_C = M . conj(Gamma_c) . M^{-1}` (not `M Gamma_c M^{-1}`):
   `Gamma_c` is genuinely complex on this carrier, so the conjugate is load-bearing -- the same
   `K-bar != K` subtlety caught in the main bound. The eigenspaces `C(W_+/-) = M . conj(W_+/-)`
   are correct throughout.

No number was fitted; the only target integers anywhere are the carrier's own `(+96, -96)` and
`0`.

# Publication plan: a two-paper portfolio

Date: 2026-06-28. Source: the "most worthy publishable result" judge panel (5 independent judges +
synthesis) plus the standing decision that the technical result and the meta-result are both worth
publishing and do not compete.

## The portfolio (both, not one)

**Paper 1 (technical, the lead).** The judge panel's most-worthy result, unanimous in shape:

> **Two-Primary Blindness and a Three-Primary Boundary Invariant: Krein-Isometric Index Conservation, a
> Necessary Antilinear Escape, and the Adams e-Invariant in a Clifford Rarita-Schwinger Sector.**

A single math-ph paper whose **load-bearing claims are two GU-INDEPENDENT impossibility theorems**, with the
program's most novel idea carried on top as an explicitly-bridged **open conjecture**:

- **Theorem 1 (candidate A): the 2-primary blindness lemma.** Every obstruction the no-go literature can
  assemble in this sector is even or mod-`2^k`, so it carries no odd-prime modular content and is
  structurally blind to the 3-primary summand of `pi_3^s = Z/24 = Z/8 (+) Z/3`. [theorem-grade,
  GU-independent]
- **Theorem 2 (candidate B, the operator hinge): Krein-isometric index conservation and its necessary
  antilinear escape.** The invariant Krein form on the generation triplet is purely cross-chirality
  `(+96,-96)`, so every *linear* Krein-isometric operator conserves the net chiral index (machine-verified
  `net ~ -2.4e-15` across signatures `(9,5)/(7,7)/(14,0)`; structurally, maximal positive-norm subspaces are
  graphs of a chirality-exchanging isometry, forcing an exact 50/50 split). The unique symmetry-respecting
  escape is **antilinear** (CPT / particle-hole, Altland-Zirnbauer class CII). Corroborated independently by
  candidate G: a Krein-isometric Seiberg-Witten moment map is degree-2 homogeneous while `ch2` is degree-0
  and connection-independent, so the constructed source action is provably orthogonal to the count.
  [machine-verified; largely GU-independent]
- **Open conjecture (candidate D): the boundary Adams e-invariant count.** If a surviving generation count
  is homotopy-theoretic it lives in exactly the blind 3-primary sector, read by the Adams e-invariant via
  the image of `J`, with a concrete nonzero class `e_R = 1/12` (gravitational `-p_1/24` channel) for the
  self-dual `Lambda^2_+` tangential framing on the `RP^3` spine (Kirby-Melvin + framed-bordism formula). The
  "GU forces three generations" headline is **not claimed**; it is stated as three named, unbuilt bridges
  (fibered-boundary Bismut-Cheeger reduction; an explicit twisted Rarita-Schwinger index operator; an
  order-3-class-to-integer-3 argument). [homotopy backbone theorem-grade; physical identification
  reconstruction-grade]

Why this framing wins: it leads with the GU-independent theorems (survive a referee who rejects GU), banks
the highest available novelty (no prior art ties a family count to the J-homomorphism / Adams e-invariant;
distinct from Wang 2023 and Wan-Wang-Yau 2026), and reframes the no-go literature by sorting a correct mod-2
no-go body and a nonzero odd count into *coprime* summands of `pi_3^s` (complementary, not contradictory).
It quarantines D's order-3-to-3 reading (the program's single largest adversarial vulnerability) as
conjecture rather than claim. This is the landing already reached in
`canon/final-verdict-generation-count-and-the-open-bridge.md`, now sharpened with the antilinear hinge.

Judge composite scores (novelty / profundity / defensibility / publishability): B ~7.4 (most defensible,
the hinge), D ~7.2 (highest novelty+profundity, reconstruction-grade so quarantined), A ~7.1 (referee-proof
spine). The synthesis out-publishes every standalone.

**Paper 2 (meta, the companion, candidate H).** A demonstration of AI-directed adversarial, self-correcting
mathematical research: the process killed its own headline repeatedly with running-code receipts (the w2-y14
error; the `1/6 -> 1/12` correction; the dimension error; the source-action orthogonality; the temporal-lead
refutation). Its credibility rests on Paper 1 being real, which is why the two ship together: the companion
is the method, Paper 1 is the proof the method produced something.

## The single convergent next computation

Both the publishability gap for Paper 1 and the firewall-unification question reduce to **one** computation:
relocate the interior antilinear re-grading (the operator that yields the net-chiral `+96` by breaking
`C = J_quat.G`) to the `RP^3` boundary spine and compute its reduced `eta-bar` under APS / Dai-Freed
boundary conditions (Bismut-Cheeger fibered-boundary reduction). It is computable on a MODEL Clifford-RS
boundary operator without first building GU's full source action. One computation, three payoffs:
- upgrades Theorem 2's escape from "exhibited + sampled (8 ghost parities)" toward a proven uniqueness
  theorem with a built `+96`;
- tests whether the firewall selector and carrier **unify** into one operator (the C3 question);
- tightens the bridge under the open conjecture D (does the selecting operator's `eta` carry the order-3?).

## Honest grade caveat

The referee-proof core is Theorems 1 and 2 plus the homotopy backbone of D (all GU-independent or
standard-applied). Reconstruction-grade and explicitly quarantined: D's physical identification (the
tangential-vs-gauge fork resolves tangential only at reconstruction grade; the gauge branch zeroes the
3-part) and the order-3-to-integer-3 step. The paper claims neither three generations nor a rescue of GU. It
claims a precise no-go-and-escape structure and the exact location an odd count could live, with the bridges
named as open.

## Venue and path

Technical paper: arXiv math-ph (cross-list hep-th), targeting a letters-style math-physics venue, with an
explicit "external review requested" framing (Joe lacks pedigreed-reviewer access). Companion meta-paper:
a methods/AI venue or a long-form preprint. Draft Paper 1 first; the clean-room draft at
`papers/drafts/two-primary-no-go-three-primary-boundary-class-2026-06-28.md` is the starting point and needs
the antilinear-hinge theorem (B) folded in as the second load-bearing result.

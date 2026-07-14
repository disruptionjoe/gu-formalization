# Staging Notes: uv-structure-fourth-order-gravity

**Candidate:** `uv-structure-fourth-order-gravity-2026-07-11.md`

## Scope

GU-independent structural packet for fourth-order (Stelle-type) gravity with a kinematically projected
Rarita-Schwinger sector. The candidate stages a one-loop ultraviolet picture with four linked claims:

1. The projected spin-3/2 sector does not spoil power-counting renormalizability because the `ker Gamma`
   projector has momentum degree zero and removes the relevant Velo-Zwanziger modes.
2. The dimensionless one-loop system has a Gaussian asymptotically-free ultraviolet route, with no isolated
   interacting fixed point in the homogeneous-quadratic truncation.
3. The ghost sector is unitary only at tree/algebraic grade: the keep-and-grade/Krein structure preserves the
   physical spin-2 sector through the interacting one-loop regime, while loop positivity remains a
   positivity-vs-causality trade.
4. The same asymptotic-freedom route forces the conformal scalaron mass-squared negative, so stability requires
   leaving that route through a non-Gaussian/asymptotic-safety alternative or another explicit escape.

This is not a claim that GU is proven, that loop unitarity is settled, or that the asymptotic-safety branch is
available. It stages the exact ultraviolet fork for the class: asymptotic freedom with conformal instability, or
some non-Gaussian route that still needs its own computation.

## Honest grade

**Structural one-loop / bounded-theorem packet.** Renormalizability and asymptotic freedom are results inside the
stated one-loop truncation and projected-sector assumptions. The unitarity section is deliberately weaker than a
loop-unitarity theorem: it combines tree/algebraic Krein grading, one-loop trade maps, and free-case or
quasi-local metric obstructions. The tachyonic-price statement is a sign computation inside the one-loop
asymptotically-free construction.

The candidate cites local checks across `tests/W44`-`tests/W80`, with the most load-bearing anchors including
`tests/W44_H58_rs_power_counting.py`, `tests/W45_H57_stage1_beta_system.py`,
`tests/W46_H57_stage2_fixed_point.py`, `tests/W47_H60_firm_af.py`,
`tests/W48_path2_A_cutkosky.py`, `tests/W53_path2_target1_af_vs_locus.py`,
`tests/W54_path2_target3_no_local_metric.py`, `tests/W79_scalaron_normsign_and_vacuum.py`, and
`tests/W80_native_r2_sign.py`. These checks support the staged packet; they do not promote the open forks to
settled canon or change any claim status.

## Light staging gate (per `papers/candidates/README.md`)

1. Title matches the theorem-grade core: PASS WITH GRADE BOUNDARY. The title advertises renormalizability,
   asymptotic freedom, tree-grade unitarity, and the tachyonic price; it does not claim all-orders loop
   unitarity or a stable ultraviolet completion.
2. No retracted or downgraded wording: PASS. The candidate repeatedly names the loop-positivity trade,
   the open rank-`>1` Krein/Tomita frontier, the conformal-sector subtlety, and the asymptotic-freedom versus
   stability fork.
3. External citations resolve: PENDING. The text names the relevant prior-work families (Stelle,
   Fradkin-Tseytlin, Avramidi-Barvinsky, Salvio-Strumia, Bender-Mannheim, fakeon/Lee-Wick lines, and
   conformal-factor literature), but this staging pass did not verify every bibliographic detail against primary
   sources.
4. Sharpest open issue acknowledged in-text: PASS. The status section names the `ker Gamma` heat-kernel `R^2`
   beta coefficient and the non-Gaussian/asymptotic-safety route as the live ultraviolet fork.
5. Overlap with other staged candidates: DELINEATED. `keep-and-grade-loop-cost/` isolates the loop-cost and
   positive-metric question. This candidate uses that cost map as one part of a broader UV synthesis that also
   includes renormalizability, asymptotic freedom, and the tachyonic conformal-sector price.

## Open items (ranked)

1. Compute or source-verify the projected spin-3/2 heat-kernel contribution to the `R^2` beta coefficient.
2. Decide whether a non-Gaussian/asymptotic-safety route exists and whether it can avoid the conformal scalaron
   instability without giving up the rest of the ultraviolet structure.
3. Close the remaining loop-positivity frontier items or keep them explicitly separated from tree/algebraic
   unitarity.
4. Verify all external citations and prior-art deltas before any public posting.

## Before posting

Keep this as a staged candidate until the ultraviolet fork and citation checks are tight enough for Joe's chosen
publication path. Any submission, upload, DOI/tag/release action, publication move, or public-posture change
remains Joe-gated.

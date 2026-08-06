---
title: "PP3 v0.4 release-hardening decision record"
status: frozen_record
date: 2026-07-22
package_id: PP3
external_action: none
---

# PP3 v0.4 release-hardening decision record

## Authority and scope

Joe directed a full adversarial preparation swing through local validation,
commit, and push, leaving Zenodo publication as the next exact approval. This
record documents the source correction required by that audit. No canon grade,
claim status, public posture, or external publication moves here.

## Release-blocking findings against v0.3

1. **Band-scope error:** v0.3 applied the M²=8 f0 and CPL ceiling across an
   unresolved M²∈{3,7,8} family. W129 already contained distinct limits
   f0≤0.2076, 0.0389, and 0.0274.
2. **Partial-grid claim:** the curvature envelope was built from an M²=8 sweep
   with only M²=3,7 spot checks, then stated band-wide.
3. **Non-formal scoring:** K2 divided correlated fitted quantities and used an
   arbitrary 35% tolerance; K3 used a universal scalar threshold. Neither was
   a joint-posterior distance-to-union test.
4. **Retrospective-evidence wording:** “zero weight” blurred no prospective
   credit with the continuing scientific relevance of adverse DR2 evidence.
5. **Condition-chain omissions:** scalar pullback, mixing/coupling control,
   healthy covariant realization, and FLRW/slow-roll applicability were
   load-bearing but absent.
6. **Overclaims:** the global family was called one-parameter; Branch N was
   called shape confirmation; four tests were called numeric; residual
   direction was said to identify a failed link; and root-system attribution
   was too broad.
7. **Projection ambiguity:** the old fit inherited its weights from the solver
   grid. Re-running on a fixed uniform-x grid showed this convention matters.

These are outcome-independent specification defects. They require a
superseding packet under the standing rule; silently editing v0.3 would destroy
the preregistration record.

## Adopted corrections

- Register the union of three branch curves and forbid data-driven branch
  selection.
- Keep branch-specific calibration-reference segments and a separate extended
  scoring domain.
- Freeze a 512-point uniform-x linear CPL projection; derive curvature only
  from its residual. A tested direct quadratic fit was rejected because its
  linear coefficient is not the standard CPL slope and flipped sign on two
  branches.
- Replace ratio cuts with 99.73% joint-region intersection against numerical
  branch tubes. K2 tests the extended union; K3 tests own-calibration closure.
- Preserve PP1's distinct 2σ CPL-proxy and 3σ pointwise phantom rules.
- State DR2 as adverse pre-freeze evidence with no prospective scoring credit.
- Expand the condition chain to seven explicit links and narrow every failure
  to the conjunction it actually reaches.
- Generate machine-readable locus, distance-observable, and convergence
  receipts; verify by resolution doubling.

## Independent audit roles

Three separate adversarial passes covered scientific scope, numerical
reproducibility, and citation/release integrity. The source-scope pass produced
the three-branch specification; the numerical pass reproduced v0.3 before the
correction; the release-integrity pass identified unsigned-Git, novelty,
citation, licensing, preview, and archive-manifest requirements. Their findings
are incorporated in v0.4 and the Drafting Factory release bundle.

## Outcome

PP3 v0.3 is superseded and sealed. PP3 v0.4 is the source of record for release
v1.0.0. The scientific verdict remains CONDITIONAL at exploration tier. The
next external step remains Joe's exact approval to upload and publish the
verified release artifact.

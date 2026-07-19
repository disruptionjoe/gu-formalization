---
title: "Integration Readiness Scorecard"
status: living_surface
doc_type: channel_readiness_ledger
created: 2026-07-19
updated: 2026-07-19
owner_item: CONSTRUCTION-SPACE-EXPLORATION
axiom: lab/process/boundary-adapter-standing-axiom.md
update_rule: "Each channel updates its row when evidence moves; integration begins only when every row's three questions reach YES and the payload consistency check passes."
---

# Integration Readiness Scorecard

Three questions per leg, answered honestly from current evidence:
**Q1** — do we understand that a construction EXISTS for this leg that fits
GU (or the greater GU-type geometry class)?
**Q2** — do we understand the parameter boundaries the leg requires to work?
**Q3** — do we understand the range/parameters the boundary adapter must
supply for those constructions to work?

Grades: YES / PARTIAL / NO, each with the evidence pointer and the exact gap.

## CH-GR (gravity / vacuum)

- **Q1: PARTIAL.** A candidate family is NAMED with provenance (C10
  distortion VEV, transcript [00:25:56]; C9 ambient/H-class adjacent) but no
  formalized construction exhibits even a conditional fit. The strawman
  family (C3 scalar-isotropic) is dead by lemma.
- **Q2: YES — the sharpest of all legs.** Requirements fully characterized:
  vacuum-supported, trace-free Q^TF(B)-slot cancellation at O(M^2),
  curvature-conditioned response, linear cheap-read clears preserved; the
  kill lemma bounds what cannot work (metric-proportional stress).
- **Q3: PARTIAL.** Hypothesized: one VEV branch selection + one frozen
  coefficient (possibly Z/2-linked). The branch SPACE is unknown until C10
  is formalized, so the range is not yet stated.
- **Gap to card-freeze:** formalize C10; compute VEV stress on the three
  sub-branches (curvature-locked anisotropic / homogeneous /
  gradient-dominated). CRITICAL PATH: CH-COSMO and CH-SM conditioning hang
  on this result.

## CH-QM (quantum sector)

- **Q1: PARTIAL.** The Krein/BRST skeleton exists in-branch; the conditional
  construction path (graded quotient given an orientation) is defined but
  the finite toy has not been built or run.
- **Q2: YES.** P4's six certificates are the boundary, itemized and
  machine-checklistable.
- **Q3: YES — the best-understood adapter item.** One global Z/2,
  topologically stored, loop-coherent; p2c demonstrated the habitat exists
  with mimic-rejecting controls. Range: binary.
- **Gap to card-freeze:** build and run the finite graded-quotient toy with
  the wrong-orientation kill test and the record register (shared with
  CH-REC).

## CH-COSMO (dark energy / cosmological scalar)

- **Q1: NO — weakest leg.** No physical scalar projector has ever been
  exhibited (C1 R0_FAIL); the only candidate (magnitude mode of the C10
  VEV) is derivative of CH-GR and has no independent standing.
- **Q2: PARTIAL.** Structural requirements are clear (projector, observable
  map, closed SVT truncation, residues discharged); quantitative boundaries
  exist on the DATA side via Lane 2 (CMB-calibrated amplitude audit READY;
  one-sided ceiling tripwire) but not yet on the construction side.
- **Q3: PARTIAL.** One absolute scale hypothesized; its allowed RANGE is
  already constrainable now by the DE ceiling data — the one adapter item
  with an empirical bracket available before any construction exists.
- **Gap to card-freeze:** blocked on CH-GR for the construction; meanwhile
  run the Lane 2 DE amplitude audit to tighten the empirical scale bracket
  (no dependency, data-facing, ready).

## CH-SM (Standard Model selector)

- **Q1: PARTIAL — strongest existence evidence of any leg.** Host
  containment is real and verified (Pati-Salam/Spin(10) hosting, relative
  arithmetic; transcript: "general relativity knows Pati-Salam"). The
  SELECTOR construction is unknown; the VEV-conditioned candidate is named
  but unformalized.
- **Q2: YES.** Seven sharp constraints plus the new alignment-rigidity
  condition; all machine-checkable via the existing P2 harness; plus a real
  observational tripwire (varying-constants bounds kill any
  drifting-alignment branch).
- **Q3: PARTIAL, and CLOSABLE NOW — with a recovered hard constraint.**
  Hypothesized: one finite subgroup-chain datum + shared scale. The
  candidate range is a FINITE ENUMERABLE LIST (Spin(10)/Pati-Salam breaking
  chains) that the existing harness can sweep today — no dependencies. BUT
  (2026-06-27 archaeology): the chain datum is NOT sufficient for
  generations — the quaternionic-parity no-go (even index for all GU-native
  carriers) forces either an a-priori rank pin or a non-quaternionic
  payload structure; ch2 = -5376 kills the natural characteristic-class
  route. Decisive joint probe: is the Z/2 orientation non-quaternionic?
- **Gap to card-freeze:** enumerate the breaking chains and harness-sweep
  them; the surviving list IS the adapter range for this leg. Cheapest card
  on the board.

## CH-REC (records / entropy / arrow of time — fifth leg)

- **Q1: OPEN (new leg).** H-REC identification: arrow of time = Krein sign
  = cancellation sign, one transmitted orientation. Hypothesis with
  repo-native support (record-sourced branch; TI 2026-07-15 note; tri-repo
  Z/2 result) but no test run yet.
- **Q2: PARTIAL.** The requirement is the co-flip identity itself: flipping
  the orientation must flip physical-sector selection AND
  record-accumulation direction together, always.
- **Q3: YES trivially, IF H-REC holds.** Zero new payload items — the
  strongest version of the one-hole picture. If the co-flip test finds a
  decoupling counterexample, N goes to 5 and this row gets its own item.
- **Gap to card-freeze:** the co-flip test, riding on CH-QM's finite toy.

## Overall: what maximal integration-readiness requires

Payload target: N <= 4 (Z/2 orientation; VEV branch; absolute scale;
subgroup datum) — with H-REC claiming the Z/2 carries thermodynamics free.

Ordered work to reach integration:

1. **CH-GR: formalize C10 + VEV stress computation** — the critical path;
   two other legs' conditioning waits on it.
2. **CH-SM: breaking-chain enumeration + harness sweep** — independent,
   computable NOW; freezes the first adapter-range item.
3. **CH-COSMO: run the Lane 2 DE amplitude audit** — independent,
   data-facing NOW; brackets the scale item empirically.
4. **CH-QM: finite graded-quotient toy + record register** — serves CH-QM
   and CH-REC in one build.
5. **External: p2c instance progress** on the Z/2 topological carrier
   (items 1-2 of the payload) — tracked, not waited on.

Two of the five (CH-SM sweep, CH-COSMO audit) have zero dependencies:
hourlies can freeze real card content immediately while C10 formalization
proceeds. Integration begins when all five rows read YES/YES/YES and the
welded payload passes the consistency check; mutual inconsistency at the
weld remains the honest falsification ending per the P0 pre-registration.

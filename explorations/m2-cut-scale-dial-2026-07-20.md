---
title: "M2 cut-scale dial on the N2 end family: conditional pass, sector-relative"
status: active_research
doc_type: exploration
created: 2026-07-20
owner_item: CONSTRUCTION-SPACE-EXPLORATION
lane_id: "1"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
  - explorations/n2-end-family-2026-07-20.md
runnable:
  - tests/channel-swings/m2_cut_scale_dial_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# M2 cut-scale dial: conditional pass, sector-relative

## Question

The P5 dossier's M2 rung asks whether the spectral-section choice carries a
cut-scale dial `lambda_0`, whether that dial can be the only dimensionful
datum, and whether exporting it leaves the C2 symbol law scale-free. The N2
truncated-real end model now supplies a genuine family on which to run this
test rather than a one-point toy.

## Construction fork

- The family, DeWitt `(9,5)` geometry, and spacelike/crossing/K-null end
  trichotomy are program-native at N2's truncated-real grade.
- The APS cut-point vocabulary is imported standard shape. Here it is used
  only as a threshold in the exact symbol spectrum `+/-sqrt(q(t,s))`; no
  positive-Hilbert boundary theory, end operator, or off-the-shelf spectral-
  section theorem is silently imported.
- `lambda_0` is boundary-condition data, not a mass inserted into the GU
  symbol kernel. The opposite fork is tested as F7's negative control.

## Result

`tests/channel-swings/m2_cut_scale_dial_probe.py` stays in the lightweight
14-dimensional N2 frame geometry and reports `4 [E] + 3 [F] = 7`, all pass.

1. On the uniformly spacelike-gapped conformal sub-end, the sampled infimum
   of `sqrt(q)` is nonzero. Every constant cut point strictly inside that gap
   selects the same rank-64 positive spectral half. A uniform cut-scale slot
   therefore exists there.
2. On the full end, the cone-crossing rays drive the positive gap to zero and
   then change Krein type. No nonzero cut point is uniform across the walls.
   The M2 slot is sector-relative for exactly the same reason N2 needs a
   sector-relative spectral-section theory.
3. Keeping `lambda_0` in the boundary condition leaves the exact
   `C2(2 xi)/C2(xi)=2` law intact. Co-scaling the family and the cut point by
   one external unit changes no dimensionless cut position.
4. Inserting `lambda_0` into a massive symbol kernel fails the factor-two law,
   firing the dossier's F7 leakage control.
5. The value is not derived or dynamically read: every point in the open gap
   gives the same symbol-grade section. M2 establishes a place where one
   imported scale may live, not why it is `2.24 meV` or how the geometry reads
   one value rather than another.

## Grade and disposition

M2 is `CONDITIONAL_PASS` at truncated-real, symbol grade under the standing
boundary-adapter axiom. The native slot survives, but its value remains payload
item 2, empirically imported. The result neither solves the cosmological-
constant hierarchy nor upgrades the P5 candidate to a recovery claim.

F7 does not fire for the boundary-only placement. It does fire for the
dimensionful-kernel control. The honest surviving statement is:

> A single sector-relative boundary scale can be exported without contaminating
> the scale-free GU symbol, but neither the cut projector nor the current end
> geometry derives or reads its value.

## Next-work handoff

- Current work: P5 M2 scale-dial rung.
- Disposition: `ENDPOINT_POSITIVE`, conditional and sector-relative.
- Recommended next: state the sector-relative spectral-section conjecture's
  wall clause precisely, using N2's computed gapped/crossing/K-null trichotomy.
- Strongest alternative: N1 families pushforward; N3 remains downstream of an
  actual operator-level boundary family.
- Overturning evidence: proof that no boundary scale is admissible on the
  spacelike sub-end, or a forced value incompatible with COSMO-A1.

No claim status, canon verdict, scorecard, public posture, PP3 packet, or
external action moves.

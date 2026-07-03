---
title: "The Signed-Readout Boundary Theorem (canon spine)"
status: canon
doc_type: results
created: 2026-07-03
canon_promoted_at: 2026-07-03
tier: internal
verdict: "RESOLVED (abstract core M/P/C + compact Part Z/K, unconditional and machine-certified); OC1/OC2 remain labeled hypotheses for the non-compact case"
certificate: tests/big-swing/R3_signed_readout_certificate.py
certificate_result: "22/22 checks PASS, exit 0 (re-run 2026-07-03)"
source_exploration: explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md
---

# The Signed-Readout Boundary Theorem

**Canon means: safe to cite as the current public spine. It does not mean proved physics.** This is the
GU-independent boundary theorem extracted by the R1-R5 big swing (canonical claim 6: GU-independent results
are co-equal products). **Internal tier** — reproduced and adversarially re-verified within this process,
not yet externally replicated.

## Canonical statement

A self-contained theorem in ordered-algebra + index theory, deliberately stated **without any reference to
Geometric Unity, to `chi(K3)`, or to the numbers 24 / 8 / 3**. No such number is assumed, divided by, or
normalized to. Two physical instances are given (a finite Ginsparg-Wilson lattice; abstract signed
accumulators); neither is GU.

| component | content | grade |
|---|---|---|
| **Part M** | monotone-readout criterion (iff) | proved, unconditional, elementary |
| **Part P** | the provenance layer is always monotone (PN / Jordan) | proved, unconditional |
| **Part C** | coexistence: monotone provenance + non-monotone readout iff a weight is negative | proved, unconditional |
| **Part Z** (compact/finite) | integer index + topological protection on a **finite** Ginsparg-Wilson operator | proved and machine-certified, unconditional |
| **Part K** (finite shadow) | the H-linear (quaternionic) index is even; `index_H = index_C / 2` is the `KSp^0(pt) = Z` augmentation | proved and machine-certified, unconditional (finite-dim) |
| **Part Z/K** (non-compact operator) | same conclusions for a non-compact Dirac operator on an open manifold `Y` | **CONDITIONAL** on two explicit analytic hypotheses OC1, OC2 — **not** discharged |

**Headline (citable).** The abstract boundary theorem (M, P, C) is a complete, unconditional theorem, and
its integer / K-theory enhancements (Z, K) are closed unconditionally on compact/finite spaces. The only
open piece is the non-compact operator extension, which is fenced behind two **labeled** hypotheses
(OC1, OC2) that are honestly not discharged here.

## Support

- Certificate `tests/big-swing/R3_signed_readout_certificate.py`: **22/22 checks PASS, exit 0** (re-run
  2026-07-03). Blocks: A (abstract criterion M/P/C), B (Part Z finite GW index), C (Part K KSp
  augmentation).
- Full proof and the OC1/OC2 fence: `explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md`.

## Scope / what this does NOT do

Does not touch the generation-count verdict (still OPEN). Does not claim the non-compact case. Contributes
the abstract spine that the program's signed-readout / integer-index results instantiate; complements
`canon/single-decider-integer-index-RESULTS.md` and the located-not-forced spine. The V3->V4 crossing
(independent replication / Lean port) is the outstanding tier upgrade.

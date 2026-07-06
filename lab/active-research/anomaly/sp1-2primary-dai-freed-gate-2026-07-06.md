---
title: "Sp(1) 2-Primary Dai-Freed Gate"
status: active_research
doc_type: gate_packet
created: 2026-07-06
depends_on:
  - explorations/internal-paths-2026-07-03/anomaly-sp64-i16-daifreed.md
  - tests/internal-paths/anomaly_sp64.py
  - tests/sp64_octic_trace_i16.py
validator: tests/anomaly/sp1_2primary_gate_validator.py
---

# Sp(1) 2-Primary Dai-Freed Gate

## Purpose

This packet sharpens the next step after `explorations/internal-paths-2026-07-03/anomaly-sp64-i16-daifreed.md`.

That exploration established the odd-primary global-anomaly arena is empty for `BSp(n)` in GU's Dai-Freed degree. It deliberately left the 2-primary leg open. The natural next target is the genuine Clifford commutant reading:

```text
G = Sp(1) = right-H
D = 14
Dai-Freed degree = D + 1 = 15
```

The validator here checks the first gate for the untwisted spin AHSS of `Omega^Spin_15(BSp(1))`.

## Gate Result

The front-page calculation has a null line in total degree 15:

```text
E2_{i,j} = H_i(BSp(1); Omega^Spin_j(pt)),  i + j = 15
H_i(BSp(1)) supported in i = 0, 4, 8, 12, ...
Omega^Spin_j(pt) for j = 15, 11, 7, 3 is zero in the low-degree table
```

So the untwisted `BSp(1)` total-degree-15 line has no visible 2-primary class. The same support reason also applies to the naive rank-32 `BSp(32)` reading in this degree.

This is not a canon verdict. It is a gate: before doing an eta pairing, first verify that the physical anomaly question really is this untwisted spin `BSp(1)` background. A different tangential structure, twist, shifted degree, non-`BSp` background, or physical-content model is a different computation.

## Non-Vacuity Controls

The validator must also detect known 2-primary structure:

- `Omega^Spin_5(BSp(1))` has the Witten-style `(i,j) = (4,1)` `Z/2` AHSS entry.
- `Omega^Spin_9(BSp(1))` has visible 2-primary entries from `Omega^Spin_9(pt)` and `(i,j) = (8,1)`.

These controls prove the script can see 2-primary classes when the degree supports them.

## Local-Anomaly Boundary

This packet only addresses the front page of the global torsion leg. It does not settle the local `I_16` leg.

The current local-anomaly record remains conditional on the assumed truncated content:

```text
Omega^0 tensor S+ plus Omega^1 tensor S-
net chirality = 1 - 14 = -13
```

Under that assumption the gravitational `tr R^8` channel remains nonzero. A chirally balanced content model would remove that local gravitational contribution. This packet does not decide which content model is physically forced.

## Required Follow-Up Before Any Status Change

1. Confirm the global-anomaly background is untwisted spin bordism of `BSp(1)` in degree 15.
2. If yes, independently review the null-line AHSS support calculation.
3. If no, define the exact twist, tangential structure, or background replacing `BSp(1)`.
4. Keep local `I_16` and physical-content assumptions separate from the global torsion gate.
5. Run `lab/process/runbooks/claim-status-consistency-quality-workflow.md` before any claim-status or canon movement.

## Validation

```text
python tests/anomaly/sp1_2primary_gate_validator.py
```

Expected result: the degree-15 `BSp(1)` and `BSp(32)` lines are empty, while degree-5 and degree-9 controls are nonempty.

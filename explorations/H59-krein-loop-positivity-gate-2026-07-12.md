---
artifact_type: exploration
status: exploration
created: 2026-07-12
hypothesis: H59
title: "H59 Krein loop-positivity gate: the terminal UV North Star is now an executable evidence contract, not a slogan. H57/H60 firm the coupling-flow side (Gaussian UV fixed point / AF, with the conformal direction carried along a negative fixed ratio), but H59 is the independent state-space side: can GU's keep-and-grade Krein rescue [P,S]=0 make that negative-ratio direction positive at loop level? Result: READY_FOR_LOOP_POSITIVITY_COMPUTE criteria defined; H59 remains OPEN. AF-flow-only evidence, tree-only Bateman-Turok/Bender-Mannheim positivity, positive-Hilbert substitution, and signature-only kills are all rejected as insufficient."
grade: "exploration / executable gate. The negative fixed-ratio target is computed by importing the H57 Stage-1 beta system and reproducing H57 Stage-2 roots. The gate logic is deterministic in tests/W48_H59_krein_loop_positivity_gate.py, 10/10 checks. No loop amplitude is computed. No positivity, unitarity, canon, claim-status, or public-posture verdict is changed."
depends_on:
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - explorations/wave42/renormalization-landscape-scan-2026-07-11.md
  - explorations/big-swing-2026-07-06/VG-SC-bateman-turok-loop-and-degenerate.md
  - explorations/big-swing-2026-07-06/R1-pu-pt-vs-ghost-parity.md
scripts:
  - tests/W48_H59_krein_loop_positivity_gate.py
---

# H59 Krein Loop-Positivity Gate

## What H59 is

H57/H60 settled the flow side as far as the current truncation allows: GU's induced fourth-order gravity
sector has a Gaussian UV fixed point, and the conformal coupling is carried to zero along a fixed ratio

```text
r = f_0^2 / f_2^2 < 0.
```

That is a coupling-flow result. It is not a state-space positivity result.

H59 is the missing state-space question:

```text
At the negative AF fixed ratio, does GU's keep-and-grade Krein rescue [P,S]=0 make projected
loop-level probabilities positive?
```

The answer remains OPEN. This note only makes the evidence contract explicit so future work cannot
mistake a nearby result for H59.

## Construction Forks Used

| Fork | Side used | Reason |
|---|---|---|
| Gravity action | GU-native induced `|II|^2` -> fourth-order Stelle/agravity couplings | H59 consumes H57's `(f_2^2, f_0^2)` AF trajectory; it does not rederive the flow. |
| Ghost clearance | GU-native keep-and-grade Krein structure `[P,S]=0`, with `P` the Cartan involution of `so(9,5)` | This is GU's object. Positive-Hilbert projection, SUSY positivity, Lee-Wick removal, or fakeon removal are different constructions. |
| Positivity | Loop-level projected Born-rule positivity | Tree-level positivity and pseudo-unitarity/optical-theorem claims are necessary context, not the H59 answer. |

## Gate Results

The executable gate is `tests/W48_H59_krein_loop_positivity_gate.py`.

It verifies:

- H57's fixed-ratio target is negative (`r ~= -23.575` and `r ~= -0.0848` at the current anchor).
- Positive-Hilbert projection is rejected as the wrong construction.
- AF-flow-only evidence is rejected as insufficient.
- Tree-only `[P,S]=0` / projector positivity is rejected as insufficient.
- A source action without an internal odd-ghost loop rule is rejected as insufficient.
- A source action without an IR regulator plus inclusive/resummed observable layer is rejected as insufficient.
- A signature-only kill from `r < 0` is rejected as a verdict.
- A complete precompute packet reaches only `READY_FOR_LOOP_POSITIVITY_COMPUTE`.
- Hypothetical positive and negative loop computations both route to review-required candidates, not automatic status changes.

## Minimum H59 Packet

A future H59 computation must provide, at minimum:

1. The H57 negative fixed-ratio target.
2. A built source action `S` for the relevant GU sector.
3. Renormalized `[P,S]=0`, not only tree-level commutation.
4. Counterterm closure under `P`.
5. Krein-diagonalizable real spectrum and no Jordan-boundary failure.
6. A rule or cancellation mechanism for odd/internal ghost-parity states on loop lines.
7. An IR regulator and inclusive/resummed observable layer.
8. Rarita-Schwinger / `ker Gamma` constraint closure under the loop calculation.
9. Projected optical-theorem / Cutkosky or spectral-density evidence.
10. Projected Born-rule probability positivity.

Only after those exist can the result be assessed as a candidate admissibility result or a candidate obstruction.
That assessment is still a review gate; it is not an automatic claim-status change.

## What This Does Not Do

This does not compute a GU loop amplitude, prove loop positivity, prove a UV-complete S-matrix, or refute GU.
It also does not change canon, `RESEARCH-STATUS.md`, `CANON.md`, claim status, public posture, or the North Star.

## Next Work

The next valid H59 swing is not another flow calculation. It is one of:

- build a minimal source-action fragment adequate for a one-loop projected probability check;
- derive the internal ghost-parity loop rule or cancellation mechanism;
- implement a toy loop computation at the negative fixed ratio with explicit IR treatment;
- prove a Jordan/Krein-diagonalizability failure for the relevant source action.

Until one of those is done, H59 should remain `OPEN`, with H57/H60 recorded as flow-side progress only.

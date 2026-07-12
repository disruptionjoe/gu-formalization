---
artifact_type: exploration
status: exploration
created: 2026-07-12
hypothesis: H59
branch: "Path-2 wave-2, Target 2 (Family-2 firm-up): two-loop CLOP pinch pre-gate"
title: "Target 2 pre-gate: the Lee-Wick / fakeon family's higher-loop obstruction localizes to the mixed conjugate-pole threshold. A single Lee-Wick pole is off the real axis at one loop, but the two-resonance mixed threshold s_mix=(m_+ + m_-)^2 is exactly real for every width. Same-sign thresholds stay off-axis. Therefore the broad derivative-coupled gravitational resonance does not automatically inherit the narrow scalar CLOP/GOW all-orders proof; the next valid Target 2 work is a true two-loop tensor discontinuity / contour computation near s=4M^2. No H59 verdict changes."
grade: "exploration / executable pre-gate. Deterministic arithmetic in tests/W55_path2_target2_clop_pinches.py, 15/15 checks. It identifies the pinch candidate and scalar-inheritance failure conditions, but computes no full two-loop amplitude and proves no all-orders unitarity or obstruction. No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture changed. H59 remains OPEN."
depends_on:
  - explorations/path2-wave1-synthesis-and-wave2-design-2026-07-11.md
  - explorations/path2-branchD-leewick-2026-07-11.md
  - tests/W51_path2_D_leewick.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W55_path2_target2_clop_pinches.py
---

# Path-2 Wave-2 Target 2 -- CLOP Pinch Pre-Gate

**Role.** Path-2 wave 1 left one Family-2 question: does the Lee-Wick / fakeon removal route stay
well-defined beyond the one-loop proof-of-concept? Branch D showed the Stelle spin-2 ghost admits the
Lee-Wick mechanism at one loop: the pole moves off the real axis as a complex-conjugate pair and the GOW
cut on real external states carries no negative ghost contribution. The named obstruction was higher-loop
CLOP stability for a broad, derivative-coupled gravitational resonance.

This run does not claim to solve that obstruction. It makes the obstruction exact enough that the next
Target 2 swing has a single computation target.

## 1. Construction Forks

| Object | Construction used | Why |
|---|---|---|
| **The ghost** | Lee-Wick complex-pole resonance | Target 2 tests Family 2, where the ghost is not an asymptotic state. This is distinct from GU-native keep-and-grade Krein positivity. |
| **Cutting rules** | CLOP / GOW deformed contour | Ordinary real-axis Cutkosky cutting is the stable-ghost construction; the Family-2 claim uses the deformed contour around conjugate poles. |
| **Obstruction** | Mixed two-resonance threshold / contour pinch candidate | The question is prescription stability at two loops, not a positivity verdict. |

## 2. The Arithmetic

Write the Lee-Wick masses as

```text
m_+ = M + i Gamma/2
m_- = M - i Gamma/2
```

At one loop, a single pole in `s=p^2` is off-axis, so the real-axis ghost cut is empty. At two-loop
order, two resonance thresholds appear:

```text
s(++) = (m_+ + m_+)^2
s(--) = (m_- + m_-)^2
s(+-) = (m_+ + m_-)^2 = (2M)^2
```

The same-sign thresholds stay off the real axis with opposite imaginary parts. The mixed threshold is
exactly real for every `Gamma/M`. Increasing the width does not move this threshold away from the real
axis; it only moves the same-sign thresholds farther away. A real mass counterterm shifts the real
location of `s(+-)` but still gives it no imaginary contour margin.

That makes `s=4M^2` the concrete CLOP pinch candidate for Target 2.

## 3. What Transfers From Scalar Lee-Wick

The narrow scalar Lee-Wick/GOW theorem handles this kind of mixed threshold by a prescription and
order-of-limits argument in the non-derivative setting. That inheritance is valid only under a
conservative gate:

- narrow resonance,
- no derivative numerator,
- no tensor numerator,
- scalar CLOP/GOW theorem available.

The gravitational case fails that gate. Branch D's concern is therefore not cosmetic: broad width,
dimensionful derivative couplings, and spin-2 tensor numerators mean the scalar theorem does not by
itself prove gravity's higher-loop contour is unambiguous.

The executable proxy also records that derivative numerators amplify the mixed-threshold region rather
than removing it. This is not a pinch proof; it is a reason the actual two-loop tensor computation cannot
be skipped.

## 4. Verdict

**Verdict: TARGET2_OPEN_WITH_PINCH_TARGET.**

Family 2 remains alive and is still the safer route after Target 1's boundary result and Target 3's
no-local-positive-metric theorem. But Target 2 is not settled by one-loop Branch D. The next valid swing is
specific:

```text
Compute the two-loop gravitational Lee-Wick discontinuity / CLOP contour near the mixed threshold
s = (m_+ + m_-)^2 = 4M^2, with the derivative spin-2 numerator retained.
```

A clean cancellation or prescription-independent deformation would firm up Family 2. A non-cancelling
pinch or order-of-limits ambiguity would be the honest gravity-specific obstruction.

## 5. What This Does Not Do

No two-loop amplitude is computed here. No all-orders Lee-Wick unitarity proof. No fakeon proof. No claim
that the mixed threshold is fatal. No `CANON.md`, `RESEARCH-STATUS.md`, claim-status, verdict, or public
posture change. H59 remains **OPEN**.

Artifact: `tests/W55_path2_target2_clop_pinches.py` (15/15 checks, exit 0).

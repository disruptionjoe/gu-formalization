---
title: "Hostile review — K128 T=0 coupled Hessian and Schur/domain gate"
status: reviewed
created: "2026-08-16"
target: explorations/conditional-build/selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate-2026-08-16.md
---

# Hostile review — K128

## Strongest objection

The zero pure metric block could be a coordinate artifact, and the mixed
coupled system might still generate a perfectly good effective metric
operator. Conversely, calling the formal Schur complement an operator could
hide a fitted inverse, a gauge quotient, or a boundary condition.

Both objections are load-bearing.

## Adversarial checks

1. The identity `I1B(g,0)=0` is read directly in native `(g,T)` coordinates
   and holds for every metric, so all pure graph-metric derivatives vanish.
2. Full stationarity is not inferred from that identity alone; K127's
   Ricci-flat condition separately kills the first translation row.
3. Direct differentiation distinguishes the quadratic Hessian blocks from the
   third derivative `D3[t,h,h]` measured by K127.
4. A coordinate mixing can generate an apparent `h-h` entry, but congruence
   preserves the coupled quadratic form and does not create a new owner.
5. The formal invertible branch gives `-A* C^{-1} A`; it is retained only as a
   conditional expression, not a selected local pencil.
6. An exact singular control turns one kernel row into a metric constraint and
   leaves the conjugate distortion variable as a multiplier.
7. Regularizing the kernel produces a reduction-dependent divergent
   coefficient, firing the fitted-inverse control.
8. The formal adjoint `A*` is not fixed before integration-by-parts and
   boundary conventions are selected.
9. K124's/K127's radial-response Green representative is not promoted to the
   full quadratic coupled boundary form.
10. A familiar Einstein/Lichnerowicz operator is not imported as source-native
    `I1B` data.

## Verdict

Accept the zero pure `h-h` block, the exact coupled form `[[0,A*],[A,C]]`, and
the retyping of K127's radial response as a third derivative rather than the
quadratic Hessian. Accept a Schur operator only after K129 evaluates `A,C`,
classifies kernels and gauge, and selects a common closed operator domain.
Reject any fitted inverse, silent pseudoinverse, imported GR operator, local
two-polarization spectrum, BFV charge, or physical superposition claim.

---
title: "WC-FUNCTION-SPACE-EXT First Probe: Krein-Paired Spectral Flow in a Finite Galerkin Model"
date: 2026-07-02
status: exploration
doc_type: exploration_note
work_card: WC-FUNCTION-SPACE-EXT
---

# WC-FUNCTION-SPACE-EXT First Probe

## Question

The located-not-forced paper proves a finite-dimensional theorem: on the `(+96,-96)`
cross-chirality carrier, linear Krein-isometric operators cannot force a net chiral count.

The open work card asks whether an analogous statement survives in the section/Fredholm
setting:

```text
Krein-isometric operators on L2 sections
Fredholm indices
spectral flow
APS/end corrections
```

This note records a first finite-Galerkin probe. It is not a function-space theorem and
does not change any canon verdict.

## Executable Probe

Script:

```text
tests/function-space-ext/krein_spectral_flow_probe.py
```

The model uses a finite chiral split `W = W_+ (+) W_-`, grading
`Gamma = diag(+1,-1)`, and cross-chirality Krein form
`K = [[0,I],[I,0]]`, so `Gamma K + K Gamma = 0`.

For diagonal Galerkin boundary operators, the modeled Krein-self-adjointness condition
`D^T K = K D` forces each `W_+` eigenvalue to be paired with a `W_-` eigenvalue of the
same value. A zero crossing in the modeled class therefore contributes

```text
(+ chirality crossing) + (- chirality crossing) = 0 net chiral flow.
```

The script checks three cases:

| case | result |
|---|---|
| Paired K-compatible crossing family | `D^T K = K D` residual zero; crossings occur in `+/-` pairs; net chiral spectral flow `0` |
| Pure Krein-isometric conjugacy | `U(t)^T K U(t)=K`; spectrum is constant; no spectral flow is created by carrier-frame motion |
| One-sided chiral-flow control | net chiral flow `+1`, but the family violates the modeled Krein-pairing condition |

## Interpretation

The probe supports the expected theorem shape:

```text
If a norm-continuous Fredholm family keeps the cross-chirality Krein pairing and its zero
crossings remain K-paired with the same orientation, the net chiral spectral flow is zero.
```

It also sharpens where a genuine failure must live. A counterexample to the function-space
extension should not be an interior carrier-frame move. It must find one of:

- a domain or boundary condition that breaks the paired-crossing hypothesis,
- an APS/end correction that supplies an unpaired chiral contribution,
- a non-Krein-compatible or non-admissible operator family,
- a topology/family-index term not seen by the finite Galerkin carrier model,
- or an actual Krein-compatible Fredholm family with unpaired chiral spectral flow.

## What Remains Open

The work card remains open. The next theorem/obstruction note still has to state and test:

- the Hilbert/Krein space of Rarita-Schwinger sections,
- a common dense domain for the unbounded operators,
- the correct self-adjoint/Fredholm condition,
- APS or noncompact-end boundary data,
- the continuity topology for the bounded transform or spectral section,
- whether zero modes are K-paired in the actual family,
- and whether end corrections can create an unpaired chiral contribution.

## Status

Exploration-grade first probe only. No paper edit, no CANON.md promotion, and no claim-status
change. The card `WC-FUNCTION-SPACE-EXT` remains open.

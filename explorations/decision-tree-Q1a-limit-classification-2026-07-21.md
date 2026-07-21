---
title: "Decision tree Q1a: the LP/LC horn is blocked by missing end asymptotics; the C0 wall does not degenerate the principal coefficient"
status: active_research
doc_type: exploration
created: 2026-07-21
directed_by: "CAI repository work cycle RUN-20260721-073617-repository-work-cycle-cai-hourly"
program: explorations/prereg-three-object-decision-tree-2026-07-21.md
question: Q1a
outcome: Q1A-END-ASYMPTOTICS-BLOCKED
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Q1a: limit-point or limit-circle?

## Verdict

**`Q1A-END-ASYMPTOTICS-BLOCKED`.** The current GU reconstruction does not
determine whether the true noncompact fiber ends are limit-point or
limit-circle. This is not another finding that the selector is external. It is
the exact internal blocker on the binary question: the committed construction
does not specify the end geometry or the asymptotic coefficients needed to
compute the deficiency indices.

The attempted shortcut through the wall fails by operator type. In the frozen
corrected expression

```text
A_tilde = B(s) d/ds + W_tilde(s),     B(s) = -i K_u(s) G,
P_0(z) = B(s) d/ds + W_z(s),          W_z(s) = K_u(s)V(s) - z C_0(s),
C_0(s) = q(s)^(1/2),
```

`B` is the principal coefficient while `C_0` is a zero-order pencil weight.
`explorations/continuum-pencil-domain-gate-2026-07-20.md` states both that
`B(s)` is invertible at every point and that the zero of `C_0` does not affect
that invertibility. Therefore `C_0 -> 0` cannot be used as evidence that the
principal coefficient degenerates at a noncompact end.

The same committed record calls the compact collar only a surrogate for the
source's noncompact fiber. Nothing currently frozen establishes that the
`q=0` wall is an end of that fiber, gives the metric distance to either end, or
supplies the end limits/rates of `B`, `W_tilde`, the measure, or the Krein
fundamental symmetry. Those are the data that decide the relevant square-
integrable solution counts. A compact-collar toy cannot fill them: hostile
verification already showed that compactness makes all endpoint solutions
square-integrable by construction.

## Native-versus-comparator check

- **Program-native object used:** the `(9,5)` Krein keep-and-grade expression
  with `B=-iK_uG` and the corrected `-i K_u'G/2` term. This is the applicable
  object because the operator question belongs to GU's native indefinite
  geometry.
- **Comparator used only as a discriminator:** ordinary Hilbert/Dirac LP/LC
  theory explains which asymptotic data would be required. Its generic
  nondegenerate-Dirac limit-point behavior is not promoted into a GU verdict.
- **Rejected conflation:** the zero of `C_0=q^(1/2)` is not a zero of `B`.
  Calling it principal-coefficient degeneration silently changes the operator.

## Binary adjudication

| horn | status | reason |
|---|---|---|
| `Q1A-LIMIT-POINT` | not earned | No GU-native end asymptotics or completeness theorem is frozen. |
| `Q1A-LIMIT-CIRCLE` | not earned | No singular-end coefficient/measure asymptotics or deficiency calculation is frozen. |
| `Q1A-END-ASYMPTOTICS-BLOCKED` | **fires** | The wall is typed as a zero-order weight, and the true end data are unspecified. |

Per the decision tree's anti-circling rule, this obstruction is named once and
Q1a is not rerun on the same inputs.

## Exact reopen packet

Q1a reopens only on one frozen, source-owned noncompact-end packet containing:

1. the actual fiber coordinate/range and identification of each end;
2. the native measure and Krein/Hilbert comparison used for square
   integrability;
3. asymptotic expansions or two-sided bounds for `B(s)`, `W_tilde(s)`, and the
   fundamental symmetry at each end, independent of `z` and `delta`;
4. proof that the corrected expression is closed and formally `J`-symmetric on
   that noncompact geometry; and
5. a deficiency/LP-LC computation that checks both ends and does not substitute
   a compact collar or finite box.

Until that packet exists, Q1b is inactive because the existence of boundary
phase freedom has not been established. The next independent decision-tree
question is Q2: whether the already-distinct sector bit `sigma` is forced,
free, or standpoint-supplied. B5 remains parked at its source-gap gate.

## Boundary

This is an exploration-grade disposition of Q1a, not a claim-status, canon,
scientific-verdict, paper, or public-posture change. It does not re-prove
externality and performs no external action.

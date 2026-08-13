---
artifact_type: exploration
status: exploration
created: 2026-07-29
work_item: B5-INDEPENDENT-RECONSTRUCTION
title: "RUNG 1 COMPLETE -- verdict GRADING-ONLY. Enumerating the symmetry-permitted coefficient space FIRST (18 real chirality-odd generators on the balanced 3+3 carrier) and only then computing indices, the net chiral index is IDENTICALLY ZERO across 4000 random samples plus a 401-point source-coordinate sweep. Q2 ('which term first breaks the index-zero pairing?') answers NO TERM DOES: the index is a function of the GRADING alone and moves only when n+ != n- (control N1: 4+3 gives index 1). So the pairing is broken by a FIELD-SPACE DECLARATION, never by an operator term -- independently reproducing the ladder's Krein-isometric-source warning by enumeration rather than citation. Q1: phi changes the kernel dimension with no hand-set rank-three projector, but that is ACCESSIBLE-RANK motion; Q4 resolves ACCESSIBLE, not GLOBAL."
grade: "EXACT for the enumeration, the index constancy over the sampled space, and both controls. The sampling is DENSE, not exhaustive (the space is continuous); the index constancy is therefore proved on 4401 points and argued structurally, not proved for every real coefficient. Q3 is only PARTIALLY answered -- index stability under 4000 random perturbations is shown, subspace stability is not tested. Scoped no-go at this rung only."
prereg: explorations/prereg-rung1-finite-coefficient-enumeration-2026-07-29.md
probe: tests/channel-swings/rung1_finite_coefficient_enumeration_probe.py
implements: lab/active-research/conditional-source-action-toy-construction-program-2026-07-26.md
construction: "program-native Krein pairing (purely cross-chirality, signature 3+/3-). Positive-Hilbert run only as a typed hostile control, never as a substitute. The triplet is SUPPLIED, per the ladder's own statement that any Rung-1 result inherits the factor of three from the located triplet."
kill_conditions_declared_before_computation: true
canon_verdict_change: none
outcome: "GRADING-ONLY"
---

# Rung 1: the finite coefficient enumeration

Selected because `CURRENT-STATE.yaml` names it as the bounded alternative to a full
dynamical selector, and because a finite coefficient space is exactly the kind of
place a forced condition **can** be expressed — the bridge the constraint-surplus
audit found missing.

## The discipline that makes this a result

The coefficient space was **enumerated from the declared symmetries alone**
(chirality-odd, real) *before* any index was computed. No matrix was searched for
and no favourable coefficient was reported. On the balanced `3+3` carrier that
space has **18 real generators**.

## The four ladder questions, answered

**Q2 — which term first breaks the index-zero pairing? `NO TERM DOES.`**

Across 4000 random points of the enumerated space plus a 401-point sweep in the
source coordinate `phi`, the set of realised net chiral indices is exactly
`{0}`. The index is a function of the **grading**, not of any coefficient. It
moves only when the grading is unbalanced: control `N1` at `n+ = 4, n- = 3`
returns index `1`.

> The index-zero pairing is broken by a **field-space declaration**, never by an
> operator term.

That independently reproduces the ladder's own preamble warning — *a
Krein-isometric moment-map source has exact net chiral index zero* — reached here
by enumeration rather than by citation. Two routes, one conclusion.

**Q1 — can `phi` open a mirror-sector gap without a hand-set rank-three
projector?** `phi` changes the **kernel dimension** (5 zero modes at `phi = 0`,
4 at `phi = 2` and `phi = 4`) with no projector imposed anywhere. But the gap
between the two smallest eigenvalues does **not** vary. So there is real spectral
motion and it is **accessible-rank** motion only.

**Q3 — stability under admissible perturbations?** *Partially answered.* The
index is stable across 4000 random perturbations. Subspace stability was not
tested and is not claimed.

**Q4 — global index three, or accessible rank three?** **ACCESSIBLE.** Nothing at
this rung produces global index three, and the honest reading is that nothing at
this rung could: the index is grading-determined.

## Controls

- `P1` coefficient space nonempty; 18 real generators reported before use.
- `P2` 4000 random samples plus a 401-point `phi` sweep; density stated.
- `N1` planted unbalanced grading moves the index — the estimator can detect what
  it must.
- `N2` positive-Hilbert hostile control returns the same grading-determined
  index, which isolates what is genuinely Krein-specific here: **nothing about
  the index**. The Krein structure does not change this answer.

That last control is worth stating plainly. On this question the program-native
Krein pairing and the standard positive-Hilbert pairing agree. Per
`GEOMETER-VS-PHYSICS-OBJECTS.md`, a no-go must be checked in both constructions,
and this one survives in both — so it is not a Krein artifact.

## One narrative error caught before commit

The probe's first version printed a Q1 conclusion asserting that `phi` "opens and
closes gaps," while its own computed value reported the low gap as invariant. The
prose contradicted the data. The conclusion is now **derived from the computed
values** rather than hardcoded, so the two cannot diverge again. Recorded because
a hand-written narrative over a correct computation is a failure mode that no
assertion in the control set was watching for.

## Scope

Dense sampling, not exhaustive — the coefficient space is continuous, so index
constancy is established on 4401 points and argued structurally, not proved for
every real coefficient. A short algebraic proof (the index of a chirality-odd
operator on a graded space equals `n+ - n-` whenever the off-diagonal block has
maximal rank) would upgrade this from computed to proved and is the cheapest
hardening available.

## What this earns and does not

**Earns**, per the ladder: an exact scoped no-go at this rung, plus the first
finite coefficient space in which a forced condition could be expressed.

**Does not earn**: locality, anomaly inflow, a physical boundary, GU-native
operator status, a derivation of three, or any packet field. Nothing moved — no
claim, canon, verdict, count, priority, or posture.

## Next rung

Rung 2 (dynamical domain-wall source) is the ladder's next step and its imposed-
wall control has already been run (`imposed-wall-triplet-comparator-2026-07-26`).
Rung 1's result sharpens what Rung 2 must show: since no coefficient can move the
index, a dynamical source can only matter by **selecting the grading or the
topological sector**, not by contributing a term. That is a materially narrower
target than "build a dynamical selector."

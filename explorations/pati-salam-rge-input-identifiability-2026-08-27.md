---
title: "Pati-Salam representation content does not identify the two-loop scale run"
status: exploration
doc_type: determination
created: "2026-08-27"
grade: "EXACT ONE-LOOP IDENTIFIABILITY STATEMENT AND TWO-LOOP INPUT TYPING; NO GU SCALE PREDICTION"
scripts:
  - tests/channel-swings/pati_salam_rge_input_identifiability_probe.py
target_claim: "M-M22"
target_claim_verdict: "RGE_UNCOMPUTABLE_PREBETA"
comparator_classification: STANDARD_FIELD_CONTROL_ONLY
canon_verdict_change: none
---

# M-M22 Pati-Salam scale-run ceiling

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `STANDARD_FIELD_CONTROL_ONLY`

```gu-typed-objects
result: Pati-Salam gauge-running input-identifiability statement
carrier: inverse gauge couplings across SM and SU4xSU2LxSU2R intervals LAYER=toy CHIRALITY=N/A
pairing: linear matching equations ON=logarithmic scale intervals
real_structure: real perturbative couplings
grading: exact symbolic input-rank result; no physical scale output
action_owner: comparator
target: M_PS and M_U scale identifiability MAP-TYPE=evaluation by piecewise perturbative RGE matching
```

Scope: this result binds the standard Pati--Salam comparator problem. It neither
selects the Pati--Salam vacuum in GU nor derives a threshold spectrum, scale,
proton lifetime, neutron--antineutron rate, Majorana mass or prediction.

## What the group theory supplies

At the Pati--Salam boundary the standard matching is

```text
alpha_3 = alpha_4,
alpha_2 = alpha_L,
alpha_1^{-1} = (3/5) alpha_R^{-1} + (2/5) alpha_4^{-1}.
```

If the normalized couplings are unified, `g_1=g_2` and
`g_Y^2=(3/5)g_1^2`, the standard identity gives
`sin^2(theta_W)=3/8`. The owner representation artifact already grades this
absolute normalization as **BOUGHT**. It is boundary convention/group content,
not a determination of either breaking scale.

## Exact identifiability condition

Let `x=ln(M_PS/M_Z)/(2 pi)` and `y=ln(M_U/M_PS)/(2 pi)`. At one loop the two
independent inverse-coupling differences obey a two-by-two system whose columns
are built from

```text
(b1-b2, b2-b3)
and
((3/5)bR+(2/5)b4-bL, bL-b4).
```

The two scales are identifiable only when those coefficients are supplied and
the determinant is nonzero. The certificate exhibits two different full-rank
coefficient packets that produce different `(x,y)`: group labels and the
`3/8` boundary identity alone therefore cannot choose a scale.

A two-loop result additionally needs the interval mass spectrum and breaking
assignments, one- and two-loop gauge matrices, Yukawa and scalar-coupling inputs,
the renormalization scheme, threshold matching at `M_PS` and `M_U`, and an
uncertainty prescription. None is owned by the current GU action/vacuum packet.
The requested decay and oscillation outputs require further operator and
matrix-element owners after the scales are known.

## Disposition

M-M22 is `PREMISE CORRECTED` at `RGE_UNCOMPUTABLE_PREBETA`: the representation
content survives, the `3/8` boundary value remains a bought standard
normalization, and no unique `M_PS` or `M_U` is computable before the beta,
spectrum and matching packet exists. Reopen on one frozen target-blind packet
that supplies those inputs; do not manufacture them from representation
containment.

`python3 tests/channel-swings/pati_salam_rge_input_identifiability_probe.py --selftest`
checks the matching algebra, rank dependence, bought-normalization custody and
two-loop owner inventory and catches five planted reference mutations.

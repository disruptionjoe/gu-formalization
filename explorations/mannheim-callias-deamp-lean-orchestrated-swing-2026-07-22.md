---
title: "Mannheim--Callias, DE-amplitude, and Lean orchestrated swing"
status: active_research
doc_type: exploration
lane: "1 primary; 2/3 bounded follow-through"
run_type: progress
started_at: "2026-07-22"
updated_at: "2026-07-22"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
outcome: MANNHEIM-CALLIAS-NO-END-POTENTIAL
probe: tests/channel-swings/mannheim_callias_end_admission.py
---

# Mannheim--Callias, DE-amplitude, and Lean orchestrated swing

## Pre-registered sequence

The swing was ordered by information value, not by apparent finishability:

1. test whether the Philip Mannheim material supplies the missing analytic
   ingredient for the Pin/Smith class-bearing object;
2. if it does, attempt a source-owned Callias/Fredholm completion; if it does
   not, isolate the first exact obstruction;
3. consume the next already-admitted Lane-2 or Lane-3 work without duplicating
   an executed result;
4. reconcile navigation and reproducibility evidence without silently moving
   a scientific status.

For every object with conventional and program-native meanings, the
construction is named.  Here the noncompact determinant-fixed observerse is
program-native; Callias estimates and PT/Stokes contours are conventional
analytic tools under admission test, not silently imported GU structure.

The Mannheim branch had three terminal outcomes:

- `MANNHEIM-CALLIAS-NATIVE-COERCIVE`: a displayed source-owned term gives a
  positive end estimate and the source owns the required domain transport;
- `MANNHEIM-CALLIAS-NO-END-POTENTIAL`: the displayed action has an escaping
  zero valley, so no source-owned Callias estimate exists;
- `MANNHEIM-CALLIAS-CHOICE-DEPENDENT`: coercivity can be imposed only by a
  freely selected contour, boundary condition, or deformation.

## Result: `MANNHEIM-CALLIAS-NO-END-POTENTIAL`

Mannheim's transcript is scientifically relevant but does not renormalize the
geometric infinity at issue.  Its renormalization discussion concerns
controlling infinitely many quantum modes with a finite counterterm structure
(`lab/sources/transcripts/toe-mannheim-conformal-gravity-2026-07-06.md`, around
00:39--00:46), and its fourth-order propagator improves the high-momentum tail
from `1/k^2` to `1/k^4` (around 01:34).  The later warning is especially useful:
stronger ultraviolet convergence can worsen the infrared and force a different
Hilbert space (around 02:17).  That is a precedent for taking domains and inner
products seriously, not a construction of GU's missing Fredholm family.

The exact obstruction is a flat zero-field valley.  For any primitive integer
`v = (v0,v1,v2,v3)` with `sum(v)=0`, the diagonal family

```text
g_n(v) = diag(-2^(n v0), 2^(n v1), 2^(n v2), 2^(n v3))
```

has determinant `-1`, signature `(3,1)`, and escapes every bounded set for
nonzero `v`.  This tests all three determinant-fixed diagonal Cartan directions,
not just one illustrative ray.

On that family take `A` flat and `Psi=0`.  Every displayed term in
`canon/source-action-seiberg-witten-construction.md` vanishes:
`||F_A||^2`, `<Psi,D_A Psi>`, and `|F_A^+ - mu(Psi)|^2`.  For the constant
tautological Levi--Civita section, the horizontal-normalized Willmore term also
vanishes because `II_s^H=0`; the repository already records
`E[s_LC]=0` for every such section in
`explorations/geometry-curvature-emergence/ic4-ricci-flat-k3-selection-2026-06-23.md`.
The compensator and Velo--Zwanziger guardian are named but not explicitly
constructed in the candidate action, so assigning either a coercive asymptotic
value would invent source data.

Consequently the only source-owned candidate deformation has, on an escaping
sequence,

```text
Phi^2 - ||[D,Phi]|| = 0,
```

not a positive lower bound outside a compact set.  The standard-library probe
enumerates primitive Cartan directions exactly and verifies this terminal
outcome.

This is scoped to the committed construction.  An external Callias mass,
compactification, APS boundary condition, or PT/Stokes contour could produce a
Fredholm problem, but its choice and domain transport would have to be added as
new source-owned structure.  The existing Mannheim PT intake already warns
that its Stokes-wedge and C-operator technology is an imported method, not GU
ontology (`explorations/mannheim-pt-intake-d1-method-2026-07-19.md`).

## Pin/Smith consequence

The result does not change `Omega_14^{Pin+} ~= Z/2` and does not evaluate its
bit.  It strengthens the analytic half of `PIN-SMITH-NOT-DEFINED`: the current
candidate action fails the first natural end-coercivity test on an explicit
rank-3 escape family.  The reopener is now concrete: supply an explicit
source-owned asymptotic term or contour, prove its Callias estimate, and prove
that the deck/real/quaternionic action transports the resulting domains.

## Lane-2 reconciliation: do not rerun an executed swing

The portfolio's `DE-AMP-DIAGNOSTIC` pointer still requests a full
`D_M(z_star)` high-redshift-tail re-solve and blind H46B likelihood.  That exact
swing is already executed at
`explorations/de-amplitude-audit-2026-07-20.md`, with runnable certificate
`tests/channel-swings/de_amplitude_audit_probe.py`:

- two independent high-redshift-tail treatments differ by only `3.3e-5`
  relatively;
- the canonical point gives `chi2_GU = 66.47` against `chi2_LCDM = 30.68`,
  `Delta AIC = +35.79`;
- the positive raw-BAO amplitude leg closes at exploration grade;
- no packageable GU amplitude prediction remains because the absolute scale is
  imported.

The correct use of compute is to reproduce that certificate, not spend a new
high-cost run rediscovering it.  Changing the authoritative portfolio item from
`READY` is a scientific-status movement and therefore remains a Joe decision;
this note records the exact stale pointer and proposed reconciliation without
silently making it.

Reproduction on 2026-07-22 initially exposed an environment-only failure: the
bundled runtime had NumPy but lacked SciPy, so two provenance-import checks could
not load even though all 18 load-bearing and confrontation checks passed.  SciPy
`1.18.0` was installed under ignored `_local/python-deps`; the rerun then returned
all seven setup checks plus all 18 substantive checks PASS, exit 0.  No additional
NumPy installation was needed.

## Lane-3 / Lean integrity target

The R4 two-arena theorem is already recorded as independently Lean-typechecked
in `canon/two-arena-rep-theory-core-RESULTS.md`, but its module remains under
`tests/big-swing/` rather than the default `Lean/GUFormalization.lean` target.
The remaining honest task was therefore integration and a fresh serialized
default-target baseline, not re-proving the theorem.  Both are now complete:

- exact toolchain `leanprover/lean4:v4.32.0-rc1` and committed mathlib revision
  `96ec947e9b66a5e6059131fc9c6d13a14cef756e`;
- pre-change default baseline: 8,643 jobs, exit 0;
- proof-bearing R4 source moved to `Lean/GUFormalization/R4TwoArena.lean` and
  imported by `Lean/GUFormalization.lean`;
- post-change default build: 8,644 jobs, exit 0; old path compatibility
  entrypoint: exit 0; pre-existing linter warnings only;
- the known unverified A1 draft duplicate was retired, leaving
  `Lean/GUFormalization/LocatedNotForcedLegs.lean` authoritative.

An attempted `lake update` was stopped when it demonstrated that the manifest's
moving `master` input could advance the toolchain to 4.33.0-rc1.  No such drift
remains in tracked state; the successful builds used the committed manifest
revision.  Reproducibility instructions should therefore prefer lockfile-driven
dependency materialization and `lake exe cache get`, not an unconditional
`lake update`.

## Reproduction

```bash
python3 tests/channel-swings/mannheim_callias_end_admission.py
```

No NumPy is needed for the Mannheim--Callias gate.  NumPy is needed only to
reproduce the already-existing DE likelihood certificate.

## Subsequent constructive reopener

The source-owned scalar search remains negative, but the strongest explicitly imported completion has now
been built.  A positive scalar Callias mass makes a chosen complete elliptic end Fredholm while remaining
homotopically class-zero.  Replacing it by the doubled quaternionic clutching map `q -> L_q` produces an
exact right-`H`, deck-equivariant, nonconstant Bott--Callias control with a positive end estimate.  The
remaining problem is no longer generic "renormalization"; it is whether the actual GU operator admits a
gap-preserving descent to that control and whether its equivariant class maps naturally to the degree-14
`Pin+` generator.  See
[`fredholm-end-clutching-big-swing-2026-07-22.md`](fredholm-end-clutching-big-swing-2026-07-22.md).

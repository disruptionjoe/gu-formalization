---
title: "Eric/Curt Wave 3A: observation duals and the leakage gate"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
campaign_wave: ECW3-G4-OBSERVATION
registry: lab/process/eric-curt-wave3a-observation-dual-leakage.json
probe: tests/channel-swings/eric_curt_wave3a_observation_dual_leakage_probe.py
grade: "DECISIVE FINITE GATE, NOT A GLOBAL OBSERVATION CONSTRUCTION. The field retract, equation dual, and active-real Krein adjoint are typed separately. Exact paired linear and nonlinear witnesses prove that a correct observed equation does not imply preservation of the observation image. The actual Y14 section, domain, quotient, and preboundary reduction remain open."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
third_lane_promotion: none
---

# Wave 3A observation duals and leakage

## Result first

Wave 3A closes one logical ambiguity before the campaign attempts a global
domain. Let

\[
L:\mathcal F_X\to\mathcal F_Y,
\qquad
R:\mathcal F_Y\to\mathcal F_X,
\qquad RL=1_X.
\]

This makes `P=LR` an image projector; it does not make `P=1_Y`. It also does
not identify three differently typed objects:

\[
R,\qquad
L^\vee:\mathcal E_Y^*\to\mathcal E_X^*,\qquad
L^!=\sharp_X\,L^\vee\,\flat_Y.
\]

`R` is a declared field retract. `L^vee` is the algebraic equation dual.
`L^!` depends on the selected real pairings and domains. In the active branch
those pairings are indefinite: the finite gate uses `(9,5)` upstairs and the
induced `(3,1)` pairing downstairs. A positive Hilbert Riesz map is not
substituted for the native Krein pseudo-musical.

The exact witness then constructs two ambient operators with the same induced
downstairs operator:

\[
R D_Y^{\rm keep}L
=R D_Y^{\rm leak}L
=D_X.
\]

Only the first preserves the image:

\[
(1-LR)D_Y^{\rm keep}L=0,
\qquad
(1-LR)D_Y^{\rm leak}L\ne0.
\]

The same separation survives a quadratic Euler-shaped extension. Both maps
give the same `E_X` after observation, but one carries a nonzero kernel-valued
term invisible to `R`. Therefore

\[
R E_YL=E_X
\]

is necessary but not sufficient. The Wave 3 dynamical gate must also require

\[
\boxed{(1-LR)E_YL=0}
\]

for the full nonlinear Euler map on the selected domain.

## Layer-0 precondition

| shared term | objects kept separate | disposition |
| --- | --- | --- |
| observation section | ambient pullback/restriction `Y->X`; defect pushforward or delta action `X->Y` | `HOMONYM` |
| dual map | field retract `R`; algebraic equation dual `L^vee`; Krein-Riesz adjoint `L^!` | `HOMONYM` |
| Riesz map | native indefinite pseudo-musical; positive Hilbert Riesz map | `HOMONYM` |
| recovered equation | correct observed shadow; dynamically preserved physical domain | `HOMONYM` |

No decomposition, retract, or equation shadow is read as a count or physical
sector.

## Exact finite construction

The probe uses rational arithmetic throughout:

1. `L` embeds a four-dimensional Lorentz-signature subspace into a
   fourteen-dimensional `(9,5)` real space.
2. `R` is a deliberately non-orthogonal left inverse. This makes the
   distinction from `L^vee` and `L^!` visible rather than only semantic.
3. `P=LR` is checked idempotent and proper.
4. Four explicit columns `N` lie in `ker R` and outside `im L`.
5. `D_Y^keep` and `D_Y^leak=D_Y^keep+NQR` induce the same `D_X`; only the
   latter has nonzero `(1-P)D_YL`.
6. A quadratic pair repeats the result for a nonlinear Euler-shaped map.

The test also plants the recurrent false inferences: `RL=1` implies `LR=1`,
`R=L^vee=L^!`, indefinite means positive, observed intertwining means zero
leakage, common complexification selects a real adjoint, or partial `TG-1`
promotes Curt.

Result: `34 exact + 11 planted = 45 PASS`.

## What this decides

- The map vocabulary and type order for Wave 3 are frozen.
- An observed equation cannot certify a physical domain by itself.
- Linear-symbol closure cannot replace the nonlinear leakage test.
- The active `(9,5)` branch has an exact finite pairing/adjoint control, not a
  global observation construction.

This is a decisive verification step because it kills a tempting shortcut
before the expensive global-domain construction: pull back the equation,
recognize the desired four-dimensional form, and declare the physical sector
closed. That shortcut is false even in exact arithmetic.

## Curt rival track and promotion gate

Curt remains a separately tagged rival/checklist track inside the Eric lane.

- `R95_ACTIVE`: the finite `(9,5)->(3,1)` pairing and leakage gate is exact;
  the global `Y^14` domain remains open.
- `R77_VERTICAL_FLIP`: the source-preferred `(7,7)` rival still owes its
  pairing adjoint, domain, action/variation, and observation-map port.
- `C14_COMMON`: the common complex algebra does not select a real Krein
  adjoint, right-`H` structure, or domain.

The pre-registered gate remains conjunctive:

```text
TG-1 AND TG-2 AND TG-3
```

`TG-1` is still partial because the source convention is not cleared. `TG-2`
still lacks a separate complete Curt dynamics/observation packet. `TG-3`
still lacks a no-refit discriminator on a common domain. No third lane is
promoted.

## Remaining uncertainty and next gate

The finite witness does not say whether the actual G2/G3 Euler map leaks. It
says exactly what must be proved or killed. The next bounded gate is
`ECW3B-GLOBAL-DESCENT-DOMAIN-QUOTIENT`:

The campaign's outer Wave 3 status remains `READY_AFTER_WAVE2_FROZEN_CLASS_EXIT`
for compatibility with the completed Wave 2 release contract; the nested
Wave 3A result records the partial scientific boundary and the narrower next
gate.

1. construct patch-compatible observation lift/retract data on the actual
   metric section;
2. fix the real pairings, right-`H` reality, and boundary-aware equation dual;
3. select a closed Krein domain and admissible polarization;
4. test the full nonlinear leakage identity; and
5. pull back `omega_G3` and quotient its kernel without calling the resulting
   object a BFV phase space prematurely.

No global section, physical equation, stationary state, Standard Model
sector, Higgs, generation count, cosmology, or theory verdict is claimed.

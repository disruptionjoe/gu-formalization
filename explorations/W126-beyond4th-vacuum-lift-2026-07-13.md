---
artifact_type: exploration
status: exploration
created: 2026-07-13
hypothesis: "H59 / H61a lineage -- W122's escape route #2 (beyond-4th-order vacuum lifting), run to ground"
branch: "W126 -- do the beyond-4th-order terms of the induced |II|^2 functional lift the tachyonic scalaron vacuum? Answered by evaluating the induced |II|^2 EXACTLY (all orders in the conformal factor, no truncation) on the conformal family g = e^{2 phi} eta, pointwise on 2-jets, in the pinned ii-s Convention-B literal-graph construction."
title: "VERDICT: NO-RESCUE -- the tachyon STANDS, hardened. The induced |II|^2 functional generates NO beyond-4th-order potential-sector invariants on the conformal family: on dphi = 0 jets, |II|^2 is an EXACT polynomial of total degree 2 in the scale-covariant curvature variable, all orders in phi (two independent routes). c_3 = c_4 = ... = 0 EXACTLY; f''(R) is EXACTLY constant at tree level; the scalaron potential is exactly W122's inverted structure (unique extremum = the tachyonic top; RUNAWAY to the f' = 0 wall). The only remaining source of f'' variation is LOOP-generated higher operators, and the R^3 rescue is ghost-infested in the window b^2/9gamma < c < b^2/4gamma and OUT-OF-VALIDITY beyond it on both W46 fixed-ratio branches (R* = sqrt(gamma/c) >> mu_DW^2). BONUS: the MSS-slice reduction of the tree functional is EXACTLY F(R) = 2 + R/3 - R^2/9 -- the tree-level scalar-slice R^2 coefficient is NEGATIVE relative to the H25-calibrated attractive Einstein term, corroborating (not proving) the ported f_0^2 < 0 direction of W45-47 natively at tree level."
grade: "exploration / Stage A EXACT (symbolic identities, all orders in phi, two routes, 32 checks exit 0); Stage B EXACT for the tree potential (unique-extremum + runaway are exact sympy facts) and TRUNCATION-BOUNDED for the loop-c_3 rescue quantification (loop-size estimate |c| <= k f^4/16pi^2 is a standard-power-counting ARGUED input; W46 ratio roots reproduced exactly); Stage C EXACT at tree level. LOAD-BEARING imports (cited, not re-derived): f_0^2 < 0 on the AF trajectory (W45-47/W46/W119), gamma > 0 with the attractive-sign calibration (H25), the Convention-B literal-graph II construction (ii-s-coordinate-formula). Convention forks CARRIED: keep-vs-subtract slice reference (computed both, same structural result); sqrt(det gbar)-vs-sqrt(det g) measure (provably identical on the dphi = 0 slice, where the claim lives); overall functional normalization (flat constant = 2 here vs c_L = 3/8 in the H50 horizontal-sectional chain -- ratio 16/3 FLAGGED for the W123 convention audit, signs robust). NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed."
depends_on:
  - explorations/W122-spin0-gauge-vs-physical-auxfield-2026-07-13.md
  - explorations/scalaron-normsign-and-vacuum-2026-07-11.md
  - explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md
  - explorations/wave35/source-action-carve-2026-07-11.md
  - tests/wave7/H25_II_first_variation_CRY.py
  - tests/W46_H57_stage2_fixed_point.py
  - tests/W122_spin0_scalaron_auxfield.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W126_beyond4th_conformal_iisq.py
external_refs:
  - "Starobinsky, PLB 91 (1980) 99 -- R^2 scalaron"
  - "De Felice & Tsujikawa, Living Rev. Rel. 13 (2010) 3 -- f(R) stability conditions f' > 0, f'' > 0"
  - "Stelle, PRD 16 (1977) 953 -- fourth-order gravity spectrum"
  - "Barrow & Ottewill, J. Phys. A 16 (1983) 2757 -- de Sitter condition 2f = R f' and stability in f(R)"
---

# W126 -- Beyond-4th-order |II|^2 terms vs the tachyonic scalaron vacuum: NO-RESCUE

**Role.** W122 established the scalaron as a genuine positive-norm tachyon
(m_0^2 = gamma/(6 f_0^2) < 0, f_0^2 < 0 trajectory-wide) and named the surviving escape
routes. Route #2: *"the 4th-order truncation (H49 landing): beyond-4th-order |II|^2
invariants giving non-constant f''(R) would break W79's background-independence and re-open
vacuum lifting."* The intuition: a tachyonic maximum at the origin is harmless if the full
potential has a stable minimum elsewhere. W126 runs that escape to ground by computing the
induced |II|^2 EXACTLY -- all orders in the conformal factor, no truncation anywhere -- on
the conformal family `g = e^{2 phi} eta` (the exact sector W122 used).

Five personas inline, one context. Deterministic test:
`tests/W126_beyond4th_conformal_iisq.py` (32 checks, exact sympy, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| **II of the section** | ii-s **Convention B** literal-graph immersion (coordinate product splitting), vertical representative `B^V` + normal lift `N(q)` | The repo's pinned construction (H15/H24/H25 all sit on it). Route 2 independently uses the FULL ambient components (base + fiber) and the block gimmel metric; agreement at a `dphi != 0` jet validates the Section-5 normal identification. |
| **Keep-vs-subtract slice reference** | BOTH computed | `|II|^2` and the slice-subtracted `|II - II_ref|^2` both give degree <= 2 potential sectors. The fork cannot resurrect higher terms. |
| **Measure** | `sqrt(det gbar)` vs `sqrt(det g)` | On the `dphi = 0` slice the two agree POINTWISE (the induced metric equals the section metric there), so the c_3 = 0 claim is measure-fork-independent. They differ only in the gradient (kinetic) sector -- flagged, not resolved. |
| **Which f_0^2 enters Stage B** | RG-run `f_0^2 < 0` (W45-47, ported) on top of the EXACT tree potential structure | The fork W122 carried, unchanged. Note the tree functional itself leans the SAME direction (Section 2, bonus). |
| **Overall normalization** | flat constant = 2 (this chain) vs `c_L = 3/8` (H50 horizontal-sectional chain) | Ratio 16/3 FLAGGED for the W123 convention audit. Signs and ratio structure are the claims; absolute magnitudes stay normalization-gated exactly as H25 graded them. |

## 1. Persona 1 -- differential geometer: the Stage-A computation (EXACT)

**Setup.** Pointwise, `|II|^2` of the graph section depends only on the 2-jet of the section.
On the conformal family the 2-jet of `phi` at a point is `(p ; v_mu ; s_{mu nu})` with
`E_0 = e^{2p}`. The *potential slice* is `v = dphi = 0` with `s` fully general (10 components):
this is exactly the slice that determines the constant-curvature (vacuum) structure, since
every gradient term vanishes there and `R = -6 e^{-2p} tr_eta(s)` (curvature convention pinned
by a from-scratch Part-0 computation, no imported formula).

**Route 1 (exact symbolic).** Convention-B `B^V` (graph Hessian - induced-Christoffel term -
algebraic slice - slope-quadratic term) with the normal-lift inner product, fully symbolic in
`(p, s_{mu nu})`. Results, each an exact sympy identity:

1. **Scale collapse (all orders in phi).** `W = |II|^2` depends on `(p, s)` only through
   `sigma = e^{-2p} s`. Every conformal-factor power cancels EXACTLY. This is the jet-level
   mechanism: `B^V` is a sum of an `E`-linear Hessian block and an `E^2`-linear algebraic
   block, and the four inverse-metric contractions in `|II|^2` remove all four powers.
2. **Degree termination.** `W(sigma)` is an exact polynomial of TOTAL DEGREE 2. Therefore
   the induced functional generates **NO cubic or higher potential-sector invariants:
   c_3 = c_4 = ... = 0 EXACTLY** -- not small, not truncated away; identically zero.
3. **Slice decomposition.** `W = a0 + a1 R + a2 R^2 + a3 Ric^2` exactly, with
   `a0 = 2`, `a1 = +1/3`, `a2 = 8/9`, `a3 = -4` (slice coefficients; on the `dphi = 0`
   slice `{R^2, Ric^2, C^2, GB}` project onto a 2D space, so a2/a3 are NOT a unique 4D
   `{R^2, C^2}` split -- stated to prevent over-reading).
4. **Family-wide.** `|H|^2` (the Willmore piece) and the slice-subtracted variant obey the
   same collapse and the same degree bound, hence the entire wave-35 shape-dimension-1
   family `alpha |II|^2 + beta |H|^2` has an exactly quadratic potential sector, for every
   `(alpha, beta)`. The beta/alpha residual freedom cannot re-open the escape.

**Checksum controls.** The flat section reproduces a positive DeWitt-Lambda-type constant
(`W(eta) = 2`; H24/H50 sign direction, normalization flagged); `a1 = +1/3 > 0` is the
attractive Einstein sign consistent with H25's CLEAR; the 4-derivative sector is present
(H49 landing visible on the slice).

**Route 2 (independent implementation).** Full-ambient `II` -- base AND fiber components from
the Section-2 ambient Christoffels, tangential subtraction, contraction with the block gimmel
metric -- evaluated in exact rationals on sampled jets. The exact interpolant through 5
MSS-type jets is degree <= 2 (`P(u) = -64 u^2 - 8 u + 2`), two held-out jets fall on it, and
it equals Route 1's polynomial identically. A `dphi != 0` jet confirms full-ambient ==
vertical-representative + normal lift where the two constructions genuinely differ.

**Where the beyond-quadratic content actually lives.** The cubic/quartic-in-phi terms of
`|II|^2` exist -- but exclusively in the GRADIENT sector
(`W(v, s=0, E_0=1) = 2 + 16 v^2 + 320 v^4 + ...`): kinetic-sector structure that vanishes
identically at `dphi = 0` and contributes nothing to `V(chi)` at constant curvature.

## 2. Persona 2 -- f(R)/scalaron specialist: Stages B and C

**The MSS-slice effective Lagrangian is a closed form, and it terminates:**

```
F(R) = 2 + R/3 - R^2/9        (exact, all orders in phi; pinned convention)
```

**Stage C first, because Stage A settles it:** `f''(R)` of the induced tree functional on the
conformal potential sector is EXACTLY CONSTANT (`= 2 f_0^2` in the physics normalization).
Non-constant `f''` does NOT arise from the induced geometry. W79's background-independence of
`m_0^2` is therefore not an artifact of truncating at 4th order: at tree level there is
nothing beyond 4th order to truncate. With `f_0^2 < 0` trajectory-wide (W46 roots reproduced:
r* = -23.575, -0.0848, both negative), `f'' > 0` fails at EVERY `R`; there is no shifted
minimum at which to re-test stability.

**Stage B, tree level (exact).** For `f = gamma R + b R^2 - 2 Lambda` the Einstein-frame
potential as a function of `R` is `V = (b R^2 + 2 Lambda)/(2 (gamma + 2 b R)^2)`, and its
ONLY finite critical point is `R* = 4 Lambda/gamma` (the dS/flat point) -- there is no second
extremum, so there is NOTHING for the vacuum to shift to. At `Lambda = 0` this reproduces
W122's `m_0^2 = gamma/(6 b)` exactly; `V''(flat) = b` exactly (gamma = 1 units); for `b < 0`
the extremum is a MAXIMUM and `V -> -infinity` at the `f' -> 0` wall on the positive-norm
branch: **RUNAWAY**. Positive control: `b > 0` (Starobinsky) gives `V >= 0` with the healthy
minimum -- the machinery distinguishes the signs.

**BONUS (W80-direction corroboration, ARGUED + convention-flagged).** The tree functional's
scalar-slice `R^2` coefficient is `-1/9 < 0` *relative to the H25-calibrated attractive
Einstein term* `+1/3 > 0`. The relative sign survives an overall normalization flip (flipping
it would flip the Einstein sign H25 fixed). So the induced `|II|^2` geometry natively leans
tachyonic on the vacuum slice -- the same direction the ported one-loop flow assigns `f_0^2`.
This is corroboration of W79/W80's residual ("the sign of GU's NATIVE R^2 running"), not a
closure of it: a tree-induced coefficient is not the running coupling of the quantum
effective action. But it removes any hope that the native tree structure supplies a
positive-`f_0^2` counterweight.

## 3. Persona 3 -- EFT theorist: the validity check on the loop rescue

Stage A closes the tree channel, so any `f''` variation must be LOOP-generated (higher
operators in the quantum effective action -- a channel the W45-47 4th-order truncation does
not compute). Standard power counting bounds a loop-induced `R^3` coefficient by
`|c| <= k f^4/(16 pi^2)` in `mu_DW` units, `f^2 in {f_0^2, f_2^2}`, `k = O(1)`. With
`f = gamma R + b R^2 + c R^3` (`Lambda = 0`), the shifted vacua sit at
`R* = +/- sqrt(gamma/c)` (they exist only for `c > 0`), and:

- **Large-root branch (r* = -23.575):** `c_needed = b^2/(4 gamma) ~ 1.4` vs
  `c_loop <= 6e-5` (at the representative finite scale `f_2^2 = 0.1`): the rescue is
  parametrically impossible by more than four orders, AND `R* >> mu_DW^2`.
- **Small-root branch (r* = -0.0848):** `b` is small, so `c_needed ~ 2e-5` and `c_loop`
  can numerically reach it -- but then `R* = sqrt(gamma/c) ~ 1.3e2 mu_DW^2`: the putative
  minimum sits two orders of magnitude ABOVE the DeWitt scale, far outside the validity of
  the induced-geometry derivative expansion, where every neglected dimension-8-and-up
  operator contributes at the same size as the `R^3` term that created the minimum.

**An out-of-range minimum is not a rescue.** The honest statement: within its domain of
validity the effective potential is the inverted W122 structure, full stop.

## 4. Persona 4 -- symbolic engineer: what the test pins down

`tests/W126_beyond4th_conformal_iisq.py`, 32 checks, exit 0, deterministic, exact sympy.
Two routes for every load-bearing sign/degree claim: Route 1 (symbolic, general 10-component
`s`, symbolic `p`) vs Route 2 (independent full-ambient implementation, exact rationals,
7-point overdetermined polynomial fit); the curvature convention is pinned by a from-scratch
Part-0 computation; the `dphi != 0` cross-route check validates the normal-lift identity;
flat-section, Starobinsky, W122-mass, and W46-roots positive controls all pass. Honest
route-independence note: at `dphi = 0` the two routes share the Section-2 ambient
Christoffels and the Hessian + algebraic-slice structure (pinned convention); what they do
NOT share is the contraction machinery (normal-lift inner product vs block ambient metric)
and the evaluation method (symbolic polynomial vs exact interpolation), and they differ
fully at `dphi != 0`, where they agree exactly.

## 5. Persona 5 -- adversarial skeptic: steelman NO-RESCUE, and where it lands

The steelman was: *the generic outcome for an inverted quadratic with a cubic correction is
a runaway, not a minimum; and any found minimum may be a maximum in disguise once the kinetic
sign is tracked.* Both prongs landed, and harder than the steelman asked:

1. **There is no cubic.** Not "small": identically zero, all orders in phi, for the whole
   shape family. The generic-runaway worry is moot at tree level -- the potential IS the
   inverted structure exactly.
2. **The kinetic-sign trap is real.** In the loop-`c` scenario, the window
   `b^2/(9 gamma) < c < b^2/(4 gamma)` gives `f''(R*) > 0` WITH `f'(R*) < 0`: a
   "stabilized" vacuum that is a GHOST vacuum -- exactly the maximum-in-disguise the brief
   warned about. The healthy window `c > b^2/(4 gamma)` is then killed by validity
   (Section 3).
3. **The one place the rescue could still hide** (named, not defeated): a NON-PERTURBATIVE
   mechanism generating `O(1)` higher-curvature structure at or below `mu_DW` -- the same
   residual escape W122 carried as its route #3. Nothing on the table produces it, and the
   tree geometry now provably does not.
4. **Also checked and closed:** the keep-vs-subtract reference fork, the measure fork (on
   this slice), and the beta/alpha shape freedom -- none re-opens the potential sector.

W122's honest negative therefore HARDENS: the tachyon's escape #2 is closed at tree level by
exact computation, and its loop remnant is ghost-infested or out-of-validity on both W46
branches.

## 6. Verdict

**NO-RESCUE. W122's tachyon verdict STANDS, hardened.**

- **Stage A:** cubic and all higher potential-sector coefficients of the induced functional
  are EXACTLY ZERO on the conformal family (two routes, all orders in phi; family-wide in
  beta/alpha; fork-robust). The MSS-slice reduction is exactly
  `F(R) = 2 + R/3 - R^2/9` in the pinned convention.
- **Stage B vacuum verdict:** **RUNAWAY** at tree level (unique extremum = the tachyonic
  top; no minimum exists, so no re-expanded mass and no induced Lambda shift -- the
  DeWitt-Lambda story is untouched by a vacuum shift because there is no shift). The
  loop-`R^3` variant is **GHOST-VACUUM** in `b^2/9gamma < c < b^2/4gamma` and
  **OUT-OF-VALIDITY** for `c > b^2/4gamma` on both W46 branches
  (`R* ~ 1.3e2 mu_DW^2` at the most generous loop size).
- **Stage C:** `f''(R)` is EXACTLY constant at tree level; `f'' > 0` fails at every `R` on
  the AF trajectory. W79's background-independence upgrades from truncation-bounded to
  exact-at-tree on this sector.
- **Bonus:** the tree-level scalar-slice `R^2` coefficient is NEGATIVE relative to the
  attractive Einstein term -- native corroboration of the `f_0^2 < 0` direction
  (ARGUED tier; the W79/W80 residual on the native RUNNING sign stays open).

**What would still change the answer** (unchanged in kind from W122, now narrower):
(1) the native `f_0^2` RUNNING sign derived from the induced geometry (the unique
load-bearing number); (2) a non-perturbative O(1) mechanism at `mu_DW`; nothing else -- the
tree-geometric channel is now exhausted.

**Concurrent-wave note (same day):** W126's Stage-A/B work was done in parallel with W123
(`explorations/W123-native-r2-running-sign-convention-audit-2026-07-13.md`), which
independently pinned the convention chain and found the positive-`f_0^2` AF trajectory
FORBIDDEN, closing the porting-artifact escape. W123 tightens W126's load-bearing input
(`f_0^2 < 0`) from ported-flagged toward native-robust; the two results compose: the sign
is native-robust (W123) AND the vacuum cannot be lifted (W126). W126's bonus tree-slice
sign (-1/9 relative to +1/3) is a third, tree-level pointer in the same direction.

## What this does NOT do

No canon / RESEARCH-STATUS / claim-status / verdict / posture change. No loop amplitude
(W48 gate). The 2-vs-3/8 normalization item and the measure/gradient-sector conventions are
FLAGGED for the W123 convention audit, not resolved. H59/H61a remain OPEN. The no-go remains
conditional on `f_0^2 < 0` (ported), exactly as in W122 -- but no longer on the 4th-order
truncation, which Stage A proved exact for the potential sector at tree level.

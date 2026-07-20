---
title: "Probe P-K2-GAUGE-COVARIANCE: is the branch-(a) cancellation identity a theorem or a harmonic-gauge artifact?"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "CH-GR channel dispatch, 2026-07-19 (P-K2-GAUGE-COVARIANCE; K2 predeclared in the CH-GR swing as the theorem-vs-artifact boundary)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/channel-swing-CH-GR-2026-07-19.md
inputs:
  - explorations/channel-swing-CH-GR-2026-07-19.md
  - explorations/channel-swing-CH-SIG77-port-2026-07-19.md
  - explorations/channel-swing-CH-SRC-2026-07-19.md
  - tests/channel-swings/ch_gr_vev_stress_probe.py
  - lab/process/boundary-adapter-standing-axiom.md
test: tests/channel-swings/pk2_gauge_covariance_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# P-K2: gauge covariance of the branch-(a) cancellation identity

Assignment: decide whether the CH-GR branch-(a) exact cancellation identity
(`Q^TF = -[t2]^TF` on harmonic-gauge linearized vacuum; `sigma kappa^2 = 1`,
`kappa^2 = 1`, hard Z/2 sign gate; Kerr-robust) is a THEOREM or a
harmonic-gauge ARTIFACT. K2 was predeclared in the CH-GR swing as exactly
this boundary. Protocol: council-amended three tiers (falsification sweep
with a FAMILY of random pure-gauge deformations; covariant restatement via
linearized Ricci; collateral checks on the C2 scale law and the Noether
identity), verdict against the prereg below.

## 0. PRE-REGISTERED SIGNATURES (written and frozen BEFORE any computation)

This section was authored before the probe script existed and before any
gauge-shifted quantity was computed. The decision rules below are binding;
the verdict section must score against them and may not reinterpret them
after the fact.

**ARTIFACT signature.** The cancellation coefficient becomes
gauge-parameter-dependent. Operationally: somewhere in the pure-gauge
deformation family there is a gauge presentation of the SAME physical
solution (same linearized Riemann tensor) in which cancellation of the
residual `Q^TF` by the curvature-locked stress requires a constant
`c != 1`, or in which the required `c` varies with the gauge parameter
(component-to-component or member-to-member retuning). If the frozen
number `kappa^2 = 1` must be retuned to follow the gauge frame, the
identity is a frame artifact and C10-GR closes honestly (branches (b), (c)
are already computed dead).

**THEOREM signature.** The coefficient is rigid: `c = 1` wherever constant
cancellation occurs, in every member of the deformation family, never
retuned by any gauge choice — and the residual terms that appear when the
identity's hypothesis is relaxed are proportional to (linearized) Ricci,
gauge-invariantly. Operationally: the obstruction block `t1` admits a
recast in which its gauge-invariant content is a linearized-Ricci
contraction (vanishing on-shell in vacuum for every gauge presentation),
so that harmonic gauge is exhibited as scaffolding and the true statement
is "on Ricci-flat backgrounds". If this lands, K2 and K5 unify: the
matter-background switch-on of `t1` IS the Ricci term.

**PARTIAL signature.** Some parts covariantize and some do not.
Operationally: the coefficient is rigid (ARTIFACT defeated) and the `t1`
obstruction recasts through Ricci (THEOREM tier-2 leg lands), but a fully
gauge-invariant restatement of the WHOLE identity (including the `t2`
stress slot) fails — e.g. locking theta to the gauge-invariant curvature
slot does not reproduce the cancellation. Then the surviving statement's
hypotheses must be listed exactly (which conventions, which gauge class,
which backgrounds), and which parts do not covariantize must be recorded
without smoothing over.

**Family requirement (tier 1).** A single chosen shift is a weak test. The
sweep must apply a FAMILY of random pure-gauge deformations
`h -> h + d(xi) sym` breaking harmonicity, with exact/symbolic arithmetic,
each member verified to (i) preserve the linearized Riemann tensor
(same physical solution) and (ii) break `box(h) = 0`. Residual
harmonic-preserving shifts (`box(xi) = 0`, nontrivial) must also be swept:
the identity claims to hold on the harmonic CLASS, so it must survive
those with the same frozen coefficient.

**Collateral (tier 3, binding).** (a) The C2 scale law
`C2(2xi)/C2(xi) = 2` must survive the covariant restatement (the covariant
kernel must remain scale-free), with the dimensionful-kernel control still
firing. (b) The Noether identity (constraint and gauge invariance the same
equation, per CH-SRC B.2) must survive: the cancellation defect must be
generated exactly by the gauge/constraint defect, not by an independent
structure. If covariantizing breaks either, the conflict is recorded, not
smoothed over.

**Conventions covered.** The CH-SIG77 port computed that the identity
survives the (7,7)-inducing X4 convention (`eta -> -eta`, `h -> -h`)
verbatim — pure algebra, signature-blind. This probe computes in the gate's
frozen (9,5)-inducing convention `eta = diag(-1,1,1,1)`; per that port
receipt, every algebraic identity established here transfers to the
mostly-minus convention unchanged, and the verdict is stated for BOTH X4
sign conventions on that basis.

---

*Everything below this line was computed AFTER the prereg above was
frozen. Probe: `tests/channel-swings/pk2_gauge_covariance_probe.py`.*

## 1. Headline

**Verdict against the prereg: PARTIAL, leaning theorem — and the PARTIAL
is precisely located.** The ARTIFACT signature did NOT fire anywhere in
the deformation family: the coefficient never becomes
gauge-parameter-dependent; off the harmonic class NO constant cancels at
all, and the failure is a structured defect exactly equal to the
constraint defect. Both THEOREM legs land: the coefficient is rigid
(`c = 1` across the entire harmonic class, both backgrounds, all residual
shifts), and `t1`'s vanishing is recast gauge-invariantly through
linearized Ricci — **K2 and K5 unify: the matter-background switch-on of
`t1` IS the Ricci term, computed exactly.** What does NOT land is the
fully gauge-invariant restatement: the covariant completion candidate K2
itself named (lock theta to the gauge-invariant linearized Riemann slot)
is computed DEAD, for a structural, dimension-specific reason — in 4D
every scale-free stress built from the curvature slot has identically
vanishing trace-free part (the algebraic Weyl/Lanczos identity), so it
cannot reach the `Q^TF` slot at all. The surviving statement is a
rigid-coefficient theorem about de Donder presentations of Ricci-flat
linearized backgrounds, not a statement about a gauge-invariant tensor.

Probe: `tests/channel-swings/pk2_gauge_covariance_probe.py` — exit 0,
**85/85 checks**, exact/symbolic arithmetic throughout (generic identities
proven on symbolic function entries; sweep quantities evaluated in exact
rational arithmetic at three exact points, r = 3, 7, 9; no floats).

## 2. The two generic identities (proven on function entries, not instances)

- **GEN1.** For GENERIC symmetric `h_ab(t,x,y,z)`:
  `box(h)_ab = (d_a H_b + d_b H_a) - 2 Ric^lin_ab`, where
  `H_a = d^c h_ca - (1/2) d_a h` is the de Donder defect vector and
  `Ric^lin` the linearized Ricci. So the gate's obstruction block
  `hmean = box(h)` IS (pure gauge-constraint defect) + (−2 × Ricci),
  identically. Corollary, since `t1` is linear in `hmean`:
  `t1 = (1/2)<(dH_sym).bhat> - <Ric.bhat>` for ANY `h`. On de Donder
  presentations (`H = 0`): **`t1 = -<Ric.bhat>` — `t1` vanishes on vacuum
  BECAUSE the background is Ricci-flat**, which is a gauge-invariant
  hypothesis. Harmonic gauge's role is exactly to kill the defect term:
  scaffolding for the `t1` sector, as Tier 2 hypothesized.
- **GEN2.** The linearized Riemann tensor of a pure-gauge deformation
  `d(xi)_sym` is ZERO for GENERIC `xi` — every sweep member below is the
  same physical solution by identity, not by per-instance check.

## 3. Tier 1 — falsification sweep (family, not one chosen shift)

Family (seed 20260719, exact rational coefficients, `xi` at `O(M)`):
five random polynomial members (four cubic, one quartic) plus one radial
non-polynomial member (`xi = M r dx`) on Schwarzschild, and two random
cubic members on Kerr-drag — all EIGHT breaking harmonicity; plus FOUR
residual harmonic-preserving members (`box(xi) = 0`): harmonic cubic,
time-dependent harmonic (`t x y`, `x y z`), dipole gradient `d(1/r)`, and
harmonic cubic on Kerr-drag.

Every non-harmonic member, all seven checks each (receipts in probe):

1. Constraint defect `H'_a = box(xi_a)` exactly — the de Donder defect of
   the shifted presentation is the gauge datum itself.
2. Harmonicity broken: `box(h') != 0`.
3. Linearized Ricci of `h'` STILL zero — same physical vacuum, any gauge.
4. The raw bhat-locked identity FAILS: `Q'^TF + [t2']^TF != 0`.
5. **NO constant coefficient cancels — and in particular no retuned
   `c != 1`.** The per-component required coefficient is not even
   constant within a single member (e.g. NH1: `24425/19583` vs `1`; NH4:
   `70112/46271` vs `226/307`; NH6: `22/27` vs `-20`; NHK1 on Kerr:
   `-269033/120982` vs `919/433`). The ARTIFACT failure mode (a
   gauge-tracking coefficient) is not what happens; what happens is
   stronger and cleaner — off the class there is no cancellation to
   retune.
6. The cancellation defect equals `[t1']^TF` EXACTLY (all components,
   all points).
7. **Noether leg:** `t1' = (1/2)<(dH'_sym).bhat'>` exactly — with Ricci
   zero gauge-invariantly, the defect is PURE constraint defect,
   generated by `H' = box(xi)` alone.

Every residual member: harmonicity preserved, and the cancellation
SURVIVES with the SAME frozen coefficient `c = 1` — while `t2'` itself
MOVES (checked: `bhat` is not invariant even inside the harmonic class).
The identity is rigid even though its ingredients are not: it is a
property of the de Donder class, closed under residual gauge, on both
backgrounds.

## 4. Tier 2 — covariant restatement

**4a. The Ricci recast lands (K2/K5 unification).** On the matter toy
background `h = 2 phi diag(1,1,1,1)`, `phi = M(x^2+y^2+z^2)/6` — a de
Donder presentation (`H = 0` computed) with `box(h) != 0` and linearized
Ricci NONZERO — the switch-on is computed exactly:
`t1 = -<Ric.bhat>` with `[t1]^TF != 0`. **The `t1`-shaped uncancelled
remainder K5 predicted on matter backgrounds IS the Ricci residual** —
K2's covariant recast and K5's matter discriminator are one statement:
the identity's two-sided structure (cancel on vacuum, remainder where
matter sits) is the single gauge-invariant statement
`defect^TF = -[<Ric.bhat>]^TF` on the de Donder class. CH-COSMO's opening
move (FLRW rides the `t1` sector) inherits this typed form.

**4b. The covariant lock is computed DEAD — with a named 4D mechanism.**
The candidate K2 named (lock theta to the gauge-invariant linearized
Riemann slot, `G_{mu nu,ab} = (1/2)(R_{mu a nu b} + R_{mu b nu a})`,
stress with the same contraction structure as `t2`):

- `[t2G]^TF = 0` IDENTICALLY on Schwarzschild — the stress is nonzero
  but trace-PURE: the covariant lock has NOTHING in the `Q^TF` slot.
- Same on Kerr-drag: not a Schwarzschild accident.
- Mechanism, computed on both backgrounds: the 4D Lanczos identity
  `R_{mabc} R_n^{abc} = (1/4) eta_mn |Riem|^2` (with `|Riem|^2 != 0`) —
  for a Ricci-flat algebraic curvature tensor (which linearized-vacuum
  Riemann is), every three-fold contraction of curvature x curvature
  with one free symmetric pair is pure trace (Bel-Robinson trace
  vanishing). So EVERY zero-derivative, scale-free kernel locked to the
  gauge-invariant curvature slot fails — not for lack of trying but by a
  4-dimension-specific algebraic identity. (In d != 4 this identity is
  absent; the no-go is a 4D accident, worth remembering if the
  construction's dimension assumptions ever move.)

**Honest tension with K2's original wording, not smoothed over.** The
CH-GR swing's K2 said: "if no gauge-covariant completion exists, the
cancellation was a frame artifact and C10-GR closes honestly." The
council-amended prereg split that binary, and the split turned out to be
load-bearing: the named covariant completion does NOT exist (4b), yet the
artifact signature also does NOT fire (Tier 1) — the coefficient never
follows the gauge, and the identity's hypotheses turn out to be stateable
almost entirely in gauge-invariant terms (Ricci-flat) plus one
gauge-CLASS condition (de Donder, `H_a = 0`), with the defect off the
class being exactly the constraint defect. Under the original binary this
result had no cell; under the amended prereg it is PARTIAL. What the
original wording got right survives as a real residue: **the `t2` slot
(and `Q^TF` itself) are de-Donder-presentation objects, not
gauge-invariant tensors.** Whoever wants the theorem must own the gauge
class as part of the construction's frozen data.

**Not exhausted (named boundary):** only zero-derivative scale-free
covariant kernels are killed by the Lanczos mechanism. Nonlocal
scale-free kernels (e.g. `dd/box`-type dressings) and derivative kernels
at higher symbol order were NOT swept; K3 (scale kill) constrains but
does not kill that family. This is the honest edge of the covariant
no-go, recorded per the exhaustion discipline.

## 5. Tier 3 — collateral

- **C2 scale law: SURVIVES.** Both the bhat lock and the Riemann-slot
  lock are second-derivative slots with pure-number kernels — the exact
  factor-2 law holds; the internal-scale control kernel still violates it
  (K3 stays armed; covariantizing does not relax it).
- **Noether identity: SURVIVES, strengthened.** In every sweep member the
  cancellation defect is generated EXACTLY by the constraint defect
  `H' = box(xi)` — the same object that defines the gauge class.
  Constraint and gauge invariance remain ONE equation under the Ricci
  recast (`defect = (1/2)(dH_sym).bhat contraction + Ricci term`, nothing
  left over) — the same "one equation, two names" shape as CH-SRC's B.2
  (`B_W A_W = 0` = `M_KT A_W = 0`). No conflict between covariantization
  and the Noether structure was found; the recast in fact EXHIBITS the
  Noether structure (the defect is the constraint's image).

## 6. Verdict vs prereg

- **ARTIFACT: NOT OBSERVED.** No member of the family (8 non-harmonic,
  4 residual, 2 backgrounds) admits a retuned constant `c != 1`; the
  coefficient never tracks the gauge parameter. Prereg's artifact
  criterion is cleanly defeated.
- **THEOREM legs: BOTH LAND.** Coefficient rigid (`c = 1` on the whole
  de Donder class, closed under residual gauge, both backgrounds);
  residuals proportional to Ricci, gauge-invariantly (GEN1 + matter
  receipt), with K2/K5 unified.
- **Full covariantization: FAILS** (4b) — so by the prereg's own PARTIAL
  clause the verdict is **PARTIAL**: the `t1`/hypothesis sector
  covariantizes completely; the `t2`/stress slot does not covariantize at
  scale-free kernel order (4D Lanczos no-go), and `Q^TF` itself is a
  presentation object.

**The surviving statement, with its exact hypotheses:**

> On a 4D flat-background linearized theory in the gate's frozen symbol
> conventions (either X4 sign convention — the (7,7)-inducing convention
> is covered by the CH-SIG77 port receipt, cited not recomputed), let the
> background satisfy the GAUGE-INVARIANT hypothesis `Ric^lin = 0` and be
> presented in the de Donder class `H_a = 0` (a gauge-class, not a
> per-solution tuning; equivalent to `box(h) = 0` given vacuum, by GEN1).
> Lock `theta_vac = kappa bhat` with the identity kernel and canonical
> quadratic stress. Then `Q^TF + sigma kappa^2 [t2]^TF = 0` exactly, with
> `sigma = +1`, `kappa^2 = 1` RIGID: the same frozen pure number for
> every solution in the class, every residual-gauge representative, and
> both computed backgrounds. Off the de Donder class the identity fails
> by exactly `[t1']^TF = (1/2)[<(dH'_sym).bhat'>]^TF` (pure constraint
> defect, no coefficient drift); on de Donder presentations of non-vacuum
> backgrounds it fails by exactly `-[<Ric.bhat>]^TF` (the K5 remainder =
> the Ricci term). The statement does NOT extend to a gauge-invariant
> tensor identity: every scale-free curvature-slot lock has zero
> trace-free stress in 4D.

**What this does upstream (proposals for owners, not applied here):**

- K2 is RESOLVED as computed-PARTIAL: the theorem/artifact boundary K2
  guarded is settled on the theorem side for coefficient and hypotheses,
  with the de Donder class promoted from "convention" to a NAMED
  hypothesis of the identity. C10-GR does NOT close; branch (a) stands,
  now with sharper typing.
- Proposal for the CH-GR card: G1's "harmonic gauge" entry should carry
  the K2 result — the gauge class is load-bearing for the `t2` slot and
  Ricci-recastable for the `t1` slot; DEM-GR-3 acquires a shadow demand:
  the source action must either DERIVE the de Donder presentation (e.g.
  as the equation of motion of a gauge-fixing/compensator sector — a
  CH-SRC-shaped question) or own it as frozen construction data.
- K5's discriminator is now typed: the matter remainder is
  `-[<Ric.bhat>]^TF`; a computation finding vacuum-style cancellation
  persisting on matter backgrounds would now contradict a computed
  identity, not just a prediction.
- The 4D-specificity of the covariant no-go is a new, cheap kill surface
  for any future proposal that covariantizes the stress slot with a
  local scale-free curvature kernel: dead on arrival by the Lanczos
  identity, no computation needed.

## 7. Receipts

- Probe: `tests/channel-swings/pk2_gauge_covariance_probe.py`, run
  2026-07-19, exit 0, 85/85 PASS, zero failures, `ARTIFACT_EVENTS` empty.
- Key exact numbers: non-constant required coefficients per non-harmonic
  member (NH1 `24425/19583` vs `1`; NH2 `7760/227` vs `1`; NH3
  `51541/23623` vs `424/289`; NH4 `70112/46271` vs `226/307`; NH5
  `176084/220067` vs `484/529`; NH6 `22/27` vs `-20`; NHK1
  `-269033/120982` vs `919/433`; NHK2 `676478/64847` vs `1`); residual
  members all `c = 1`; GEN1/GEN2 proven on generic function entries;
  Lanczos identity `L_mn = (1/4) eta_mn |Riem|^2` verified symbolically
  on Schwarzschild AND Kerr-drag with `|Riem|^2 != 0`;
  `[t2G]^TF = 0` identically on both.
- Prereg discipline: Section 0 of this file was written and saved before
  the probe script existed; the probe echoes the prereg in its header and
  scores the verdict against it.
- Killed-selector ledger respected: none of the eleven dead routes
  re-run; branches (b)/(c) not resurrected; C3 untouched.
- Convention coverage: computed in the gate's (9,5)-inducing frame;
  (7,7)-inducing coverage cited from the CH-SIG77 port receipt
  ("nothing in the branch-(a) computation depends on the (9,5) choice"),
  not recomputed — signature purity respected.

## 8. Boundary

Conditional construction under the standing axiom, weak-field symbol
frame, `R0_COND` working grade. `claim_status_change: none`; no map,
canon, scorecard, or register file was touched; Section 6's upstream
items are PROPOSALS for their owners. The coefficient's source-side
provenance (DEM-GR-1/2) remains exactly as open as the CH-GR swing left
it — this probe sharpens the identity's hypotheses and gauge status, not
its provenance. The covariant no-go is bounded honestly: local
scale-free curvature kernels only; nonlocal/derivative kernels not swept.

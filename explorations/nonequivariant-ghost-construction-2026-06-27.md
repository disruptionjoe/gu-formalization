---
title: "Constructing the non-equivariant RS ghost: the obstruction bends but does not close; the missing datum, pinned"
date: 2026-06-27
status: exploration
doc_type: exploration
verdict: speculation   # frontier construction: a non-equivariant anti-trap-passing ghost IS buildable, but none closes; NO claim promoted
method: "Design -> Build -> adversarial Kill workflow over 4 non-equivariant sigma_c constructions; each built + tested on the explicit Cl(9,5) rep; survivors re-run in the main loop"
builds_on:
  - explorations/source-action-necessary-conditions-and-causality-2026-06-27.md  (SOURCE-01 keystone)
  - explorations/rs_source_candidate_projected_differential_scratch.py  (the rep objects)
  - explorations/time-as-finality-crosswalk/ti-as-gu-source-action-three-steelmen-2026-06-27.md  (the parallel attack line)
tests:
  - tests/rs_ghost_steelman_geometric_carrier.py
  - tests/rs_ghost_fixed_null_covector_spurion.py
bears_on: "the unwritten GU RS/IG source action (the root blocker)"
---

# Constructing the non-equivariant RS ghost

The keystone (SOURCE-01) proved the compensator `sigma_c(xi)` must be **non-equivariant** (outside the
Spin(9,5)-equivariant family) and must resolve the RS escape **cohomologically** (s^2=0, escape s-exact)
**without** decoupling RS (which would reinstate Velo-Zwanziger acausality — the anti-trap). This run
attempted to build it, four ways, on the explicit Cl(9,5)=M(64,H) rep. **No construction closes the complex
— as the five-thread convergence predicted — but the obstruction is now bent, quantified, and pinned, and the
two independent attack lines (this rep-theory construction + the TI-as-source-action steelmen) have converged
on the SAME precisely-specified missing object.**

## 1. What was achieved (genuinely new)

**A non-equivariant, H-linear, anti-trap-passing ghost coupling IS constructible.** Two independent
constructions survived adversarial kill as genuine (neither the acausal trap nor a trivial subtraction):

- **Null-covector spurion** (`tests/rs_ghost_fixed_null_covector_spurion.py`): `sigma_c` built from a FIXED
  null covector `n` (breaking Spin(9,5) to its little group). Genuinely non-equivariant (defect 16.0,
  `n`-dependent 22.63), **exactly H-linear** (`‖[c(n),J]‖ = 0`), **nilpotent** (`s^2 = 1.4e-14`, via
  `c(n)^2 = 0`), and **anti-trap PASSED** (bare `‖[Π_RS, M_D]‖ = 58.72` exactly unchanged — RS stays coupled,
  VZ evaded). Most importantly it **BENDS the closure obstruction**: deforming the constraint surface to
  `ker(B_n)` drives `‖[Π_{ker B_n}, M_D]‖` from **58.72 down to a floor of 32.80** (a ~45% reduction) without
  ever touching the dynamics — the first construction to move the obstruction at all.
- **Steelman geometric carrier** (`tests/rs_ghost_steelman_geometric_carrier.py`): `sigma_c` built from the
  steelmen's required "GU-native geometric carrier" — a section-direction carrier that rotates `e_0`, breaking
  Spin(9,5). Genuinely non-equivariant (defect 308.17), **exactly H-linear** (0.0), **anti-trap PASSED**
  (58.72 unchanged). It cleanly **separates the legitimate ghost from the trap**: the trap path zeroes the
  escape on `C^0` (collapsing 58.72 → 2e-14, acausal), the legitimate ghost leaves 58.72 intact.

This is real progress: for the first time the construction is **outside the equivariant family AND past both
the acausal-decoupling trap and the trivial-subtraction trap** — exactly the regime the keystone said the
answer must live in. (The supergravity-gravitino approach was **killed**: its "independent background
spin-connection W" was actually `xi`-linear — an artifactual least-squares choice masking an equivariant
solution `Π_RS g` — so its non-equivariance was illusory and it reduced to a relocated trivial subtraction.)

## 2. Why none closes — the obstruction, pinned three ways

No construction reaches `s^2=0` AND s-exact escape AND anti-trap simultaneously. The obstruction is now
characterized with precision:

1. **Nilpotency vs escape-triviality are mutually exclusive for a single gauge map.** Enforcing `s^2=0`
   forces the ghost gauge orbit ON-surface (`Π_perp G_tot = 0`), after which the same ghost leg can no longer
   trivialize the dynamical escape (residual jumps back to the full 41.52). The escape is **co-exact** — it
   lives in `im(Γ^†)`, the **Koszul-Tate / antighost (Nakanishi-Lautrup) direction** — *not* ghost-exact. So
   closing it needs a **full BV bicomplex** with *both* the ghost (`eps`) leg and the antighost (Koszul-Tate)
   leg s-consistent, not a single gauge map.
2. **The resolver requires a Dirac-bracket propagator the symbol rep lacks.** The unique escape-resolver
   `X = (Γ·M_D·D)^{-1}·C2` exists abstractly (residual 1.2e-14) but requires the **global inverse**
   `(Γ·M_D·Π_RS·d_A)^{-1}` — a Dirac-bracket / propagator. The boundary spectral section provably cannot
   supply it; the **source action** must.
3. **A new secondary VZ-type constraint emerged.** The construction surfaced `C2` (norm 155.36), genuinely
   independent of `Γ` (zero reduction against it) — a *true new constraint* of the dressed system, not a
   restatement. Its appearance is itself a Velo-Zwanziger-flavored datum the source action must reconcile.

## 3. The convergence — both attack lines name the same object

The parallel **TI-as-GU-source-action steelmen** concluded the missing datum must be a **GU-native geometric
carrier** (a boundary holonomy/connection/curvature, a source-derived characteristic/KSp class, or a
family-coordinate functional). This construction now says *what that carrier must DO*, operationally:

> Supply a **source-derived invariant-surface selector** — a non-equivariant geometric datum that builds the
> deformed constraint surface `ker(B_n)` so that it becomes `M_D`-invariant (driving the bent obstruction
> 32.80 → 0), equivalently the **antighost/Koszul-Tate leg + the Dirac-bracket propagator** `(Γ·M_D·D)^{-1}`,
> while reconciling the new secondary constraint `C2`. This is exactly the steelmen's "curvature/connection /
> KSp class" carrier, now with a precise operational job.

The two independent lines — rep-theory construction (mine) and effect-typed source-extension (the steelmen) —
have **converged on the same object from opposite sides**, and it is the same object the keystone and all four
Track-2 verdicts pointed at: the **GU RS/IG source action**, now specified down to *the precise operator it
must supply* (a Koszul-Tate antighost leg + a Dirac-bracket propagator that drives the 32.80 floor to zero).

## 4. Net + the next gate

The frontier moved. We now have, on the verified rep: (a) a non-equivariant, H-linear, anti-trap-passing,
nilpotent ghost that **measurably bends the closure obstruction (58.72 → 32.80)**; (b) a precise reason no
single gauge map closes it (co-exactness in the Koszul-Tate direction); (c) the exact missing operator (the
source-derived invariant-surface selector / Dirac-bracket propagator); and (d) a new secondary constraint
`C2`. The decisive next gate: **promote `B_n` from a fixed null-covector spurion to a source-derived
curvature/KSp carrier and re-test whether the full BV bicomplex (both ghost and Koszul-Tate legs s-consistent)
drives the 32.80 floor to 0** — the first test that would genuinely need, and exercise, a candidate written
source term. That is where the source action stops being a black box and becomes a concrete object to write.

## What this does NOT establish
- It does not close the complex, construct `S_IG`, or compute the generation count / `q`.
- The supergravity approach's specific `sigma_c` was killed as artifactually-equivariant/trivial.
- The Stueckelberg approach did not return a structured result (its agent failed); not assessed here.

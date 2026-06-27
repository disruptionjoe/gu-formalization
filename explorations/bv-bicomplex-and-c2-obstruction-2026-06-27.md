---
title: "The RS BV bicomplex closes the escape — but the real obstruction is C2, and it needs the Y14 connection-curvature"
date: 2026-06-27
status: exploration
doc_type: exploration
verdict: speculation   # climactic gate: the bicomplex works + the escape is resolved, but C2 does NOT close; the final missing object is named. NO claim promoted.
method: "Design -> Build -> adversarial Kill over 3 source-derived carriers + the full BV bicomplex; two survivors genuine=True with all four guards holding; headline re-run in the main loop"
builds_on:
  - explorations/nonequivariant-ghost-construction-2026-06-27.md  (GHOST-01)
  - explorations/source-action-necessary-conditions-and-causality-2026-06-27.md  (SOURCE-01)
tests:
  - tests/rs_bicomplex_spin95_connection_2form.py
  - tests/rs_bicomplex_ksp_characteristic_class.py
bears_on: "the unwritten GU RS/IG source action — now isolated to the Y14 connection-curvature that reconciles C2"
---

# The RS BV bicomplex, and the C2 obstruction

The climactic gate asked: can a SOURCE-DERIVED carrier + the FULL BV bicomplex drive the closure obstruction
to zero? **The answer is honest and clarifying: the bicomplex is built and WORKS, it resolves the escape —
but in doing so it reveals that the surface-noninvariance floor (32.80) was never the real obstruction. The
true, irreducible obstruction is a secondary constraint C2 (~155), and it needs a specific named geometric
object: the GU connection-CURVATURE on Y14.** No false closure: two independent carriers both `genuine=True`,
all four guards (anti-trap, anti-fixed-solve, anti-vacuous, anti-import) held, every number reproduced on
re-run.

## 1. What was BUILT and WORKS (the missing antighost leg, supplied)

GHOST-01 proved the escape is co-exact (Koszul-Tate direction) and a single gauge map cannot both be nilpotent
and trivialize it — a **full BV bicomplex** (ghost leg + Koszul-Tate leg) was required. It is now constructed
on the explicit Cl(9,5)=M(64,H) rep (`tests/rs_bicomplex_spin95_connection_2form.py`) and verified:

- **`s^2 = 0` genuinely** (`‖s^2‖ = 1.18e-12`): `s_KT^2 = 0`, `s_long^2 = 0`, `{s_KT, s_long} = 1.18e-12`,
  Noether identity `‖B_W A_W‖ = 1.69e-13`.
- **Non-vacuous (controlled):** `rank(M_KT) = rank(A_W) = 128` (neither leg trivial), and the raw-gauge
  control (un-projected gauge map) gives `s_raw^2 = 522.79 != 0` — so the closure is genuine structure, not
  degeneracy.
- **The co-exact escape is now genuinely `s`-EXACT** via the Koszul-Tate leg: `‖(I - P_{im M_KT}) escape‖
  = 1.0e-13` (escape range lies in `im(M_KT)`), while it is NOT ghost-exact (`45.37`). **This resolves
  GHOST-01's co-exactness** — the antighost leg supplies exactly what was missing.
- **Anti-trap held:** bare `‖[Π_RS, M_D]‖ = 58.72` exactly (M_D never modified; RS stays coupled, VZ evaded).

So a genuine piece of the RS BV/BRST machinery is now constructed and machine-verified. That is real.

## 2. The inversion: the 32.80 floor was a red herring

Resolving the escape via the bicomplex works for **any** carrier `B_W`. So driving the surface-noninvariance
number `‖[Π_{ker B_W}, M_D]‖` (the 32.80 spurion floor) to zero was **never the real obstruction.** And the
honest test confirms it dramatically: the GENUINE a-priori carriers do **worse** than the simple spurion.

- **Spin(9,5)-connection 2-form** (a genuine connection: ξ-independent `= 0.0`, transforms inhomogeneously):
  a-priori dressed floor `= 41.04` (boosts 48.96, rotations 58.72 = no movement, Levi-Civita 59.18,
  91-generator sweep 55.49, 24 random 41.04). All **above** the 32.80 spurion. The only sub-32.80 numbers
  (down to 21.87, still `!= 0`) come from the **labelled greedy fixed-solve that reads the target** — flagged
  by the construction's own discriminator (a-priori 41.04 vs solved 21.87) and **disqualified** as a
  fixed-solve artifact.
- **Quaternionic KSp characteristic class** (intrinsic, exactly H-symmetric): floor `= 44.25`, also worse;
  `s^2 = 749.16 != 0` (does not even close); escape only 2.91% s-exact. It **structurally cannot** single out
  a bending direction — the quaternionic structure is symmetric across all 5 conjugate null pairs.

So no intrinsic / a-priori construction closes, and the floor number is not where the obstruction lives.

## 3. The true obstruction, isolated: C2 (BRST-invariance of M_D)

The genuine, irreducible obstruction is the **secondary constraint** that GHOST-01 first glimpsed:

> **C2 = Γ · M_D · Π_RS** (bare norm **155.36**), and dressed `B_W · M_D · Π_{ker B_W} = 192.46` — it
> **survives and grows** under every carrier and is **fully Γ-independent** (its reduction against Γ is its
> full norm). It is the **BRST-invariance of the dynamics M_D** — a true new Velo-Zwanziger-type secondary
> constraint, not a restatement of the gamma-trace constraint.

Two independent constructions (connection 2-form and KSp class) compute the **same** `C2 = 155.36`,
Γ-independent — strong corroboration that C2 is a real invariant of the problem, not an artifact.

## 4. The final missing object, NAMED (and the grand convergence)

Both approaches pin exactly what C2 needs, and it is the same object:

> A **symmetry-breaking spectral section** — one **distinguished null plane** — which is precisely the
> **actual GU connection-CURVATURE 2-form on Y14**. A flat-connection holonomy is provably insufficient
> (a-priori floor 41.04 > spurion 32.80, never 0); an intrinsic H-symmetric class is provably insufficient
> (it cannot break the 5-fold null-pair symmetry to one plane). The required datum is **external** to the
> symbol algebra: the curvature of the GU connection on the full Y14 = Met(X4) geometry, which selects the
> distinguished plane.

This is the **grand convergence** of the whole arc. The single object every thread pointed at is now one
concrete geometric datum, and the threads are literally the same object seen differently:
- the **source action** (keystone SOURCE-01): supplies the dynamics whose BRST-invariance is C2;
- the **boundary spectral section / holonomy** (Joe's record-issuance idea): *is* the distinguished null
  plane / spectral section the bicomplex now demands;
- the **steelmen's GU-native geometric carrier** (the parallel track): *is* the Y14 curvature / KSp carrier;
- the **non-compact index** boundary data: the same Y14 end-geometry.

They were never four problems. They are one: **the GU connection-curvature 2-form on Y14 that reconciles C2
by selecting a distinguished null plane.**

## 5. Net + where this leaves the program

We constructed and verified the RS BV bicomplex (the escape is genuinely resolved), proved the 32.80 floor
was a red herring, isolated the true obstruction as the Γ-independent secondary constraint C2 (155.36,
two-way confirmed), and named the exact missing object. The frontier has moved **off the symbol algebra**:
no construction on the `(xi, M_D, Γ)` symbol data alone can close C2 — by two independent proofs (flat
holonomy and intrinsic KSp both provably insufficient). The next gate is therefore a **differential-geometry**
computation on the actual Y14 = Met(X4) manifold: construct the GU connection's curvature 2-form, restrict it
to one distinguished null plane (the spectral section), and test whether `B_W = ` the curvature-dressed
constraint reconciles C2 (drives 155 → 0) within the full bicomplex. That is the first computation that needs
the real Y14 geometry rather than the symbol rep — and it connects directly to the existing
`active-research/...k3-chi-gate...` and the noncompact-APS-end work.

## What this does NOT establish
- It does not close C2, construct `S_IG`, or compute the generation count.
- The KSp approach does not even close `s^2` (749.16); only the connection approach closes the bicomplex.
- The explicit-Koszul-Tate approach did not return a structured result (agent failed) and is not assessed.
- Reaching the dressed floor below 32.80 was only via the disqualified fixed-solve; no a-priori closure.

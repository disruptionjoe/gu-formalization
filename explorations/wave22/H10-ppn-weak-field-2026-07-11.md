# H10 -- The PPN / weak-field solar-system bar for GU gravity

Wave 22. A cheap falsifier. Test: `tests/wave22/H10_ppn_weak_field.py` (deterministic, exit 0).

> [!IMPORTANT]
> **CORRECTED 2026-08-15 (H10-5).** This note as originally filed (2026-07-11) carried a WRONG
> Yukawa assignment: it gave the massive spin-2 a coefficient `+1/3` and handed `-4/3` to the
> scalar. The correct assignment is the exact inverse — the massive spin-2 is a **GHOST** with
> coefficient **`-4/3`, REPULSIVE**, and the scalaron carries `+1/3`, attractive. The defect was
> diagnosed against the literature on 2026-08-09 and remediated on 2026-08-15 only after being
> **re-derived from structure** (projector traces + the ghost sign of `box(box+m2^2)`, no
> literature number as input). Certificate:
> `tests/channel-swings/joe_directed_h105_stelle_ghost_sign.py` (45/45, 14 planted false facts
> each forcing exit 1).
>
> **What moved:** `alpha_Y = +1/3` → `-4/3` (magnitude ×4, attraction → repulsion);
> `gamma - 1 = -(2/3)e^{-m2 r}` → `+(2/3)e^{-m2 r}` (**sign flipped**: GU predicts `gamma > 1`).
> **What did not move:** the Cassini `m2` floor, the `mu_DW` floor, the ~45-decade clearance, and
> the verdict — because Cassini bounds `|gamma - 1|` two-sided and the leading *magnitude* is
> degenerate between the two assignments (the two floors differ by `5.6e-6` relative). See
> "Why no check caught it" below; that degeneracy is a **third** non-discriminating check beyond
> the two the 2026-08-09 banner identified, and it is the one this bar's verdict rides on.

**One-line verdict: GATED-ON-mu_DW, effectively PASSES.** (Unchanged by the correction.) GU's
tree-level gravity does *not* force a solar-system-visible deviation. `gamma` and `beta` return to
their GR values as an *exponentially suppressed* Yukawa from the massive spin-2 ghost; the pass
requires the free DeWitt scale `mu_DW` above a floor of `~1.5e-17 eV`, which the natural
`mu_DW ~ M_Pl` clears by ~45 orders of magnitude. The solar-system PPN bar is far weaker than the
pre-existing ghost-decoupling gate (BAR 2) and adds no new binding constraint.

**Second verdict, new and less comfortable: this bar is WEAK.** Its published numbers are
invariant under a ×4, sign-flipping error in its own central input. It cannot detect that class of
defect in itself, and it should not be ranked as a live falsifier on the strength of its pass.

## The object

GU gravity (Waves 1-10) is a tree-level Stelle-clear: induced Einstein-Hilbert `R^X` + a `Weyl^2`
(Bach, 4th-order) term + a DeWitt `Lambda`, conditional on the soldering postulate + `mu_DW`. On
the transverse-traceless graviton the operator is `box(box + m2^2)` (H15/H25): a healthy massless
graviton plus one *distinct massive spin-2* of mass `m2`. The repo's computed inputs:

- H15: `|II|^2 = |H|^2 - R^X`; in 4D `int R^X` is dynamical -> Stelle `R + Weyl^2`, flat-ambient `m^2 = +1/2`.
- H25: curved-ambient `m^2_eff = 1/2 + C_RY`, with `C_RY` **computed positive** by two independent
  methods (`+1/3 -> m^2_eff = 5/6`; `+3/4 -> m^2_eff = 5/4`). Sign robust, O(1), positive.
- H24/H25 BAR 2: the physical mass is `m2^2 = m^2_eff * mu_DW^2`. `mu_DW` is the source-action overall
  scale (dimensionless ratios geometric, dimensionful magnitude free); natural `mu_DW ~ M_Pl`.

**Key structural fact (decisive for PPN):** GU's action is `R^X + Weyl^2 + Lambda` with **no `R^2` term**.
In quadratic gravity the massive spin-0 mass obeys `m0^2 ~ 1/beta_{R^2}`; with `beta_{R^2} = 0` the
scalar decouples (`m0 -> oo`). So GU gravity is *pure Einstein-Weyl* (`R + Weyl^2`): a massless
graviton + one massive spin-2, and **no propagating scalar ghost**. This is the cleanest PPN case.

## Q1 -- The modified Newtonian potential (COMPUTED, derived 2026-08-15)

General quadratic-gravity point-mass potential (Stelle 1978, GRG 9, 353; Lu, Perkins, Pope &
Stelle, PRD 92, 124019 (2015), Eq. (4.7a)):
`V(r) = -(GM/r)[1 - (4/3)e^{-m2 r} + (1/3)e^{-m0 r}]`. GU has no `R^2` term, so `m0 -> oo` kills
the `+(1/3)` **scalar** Yukawa and **keeps the `-(4/3)` spin-2 ghost**. The two Newtonian-order
potentials:

```
Phi(r) (g_00) = -(GM/r)[1 - (4/3) e^{-m2 r}]
Psi(r) (g_ij) = -(GM/r)[1 - (2/3) e^{-m2 r}]
```

The massive spin-2 does **not** flip sign between the temporal and spatial potentials: **both are
repulsive**, and they differ in *magnitude*, `4/3` vs `2/3`. This is the point the original note
got backwards. The derivation, in three structural steps, none of which reads a literature number:

1. Between conserved sources the massless-graviton numerator carries a trace coefficient
   `1/(D-2) = 1/2`; the Fierz-Pauli massive spin-2 carries `1/(D-1) = 1/3`.
2. On a static point mass (`T_00 = M`, `T = -M`) both structures collapse to `M M'`, so the
   temporal weights are `1 - 1/2 = 1/2` massless and `1 - 1/3 = 2/3` massive. Their ratio,
   `(1 - 1/3)/(1 - 1/2) = 4/3`, is the **van Dam-Veltman-Zakharov enhancement** — and it is the
   *potential* coefficient. The spatial weights are `1/2` and `1/3`, ratio `2/3`.
3. The **sign** comes from the fourth-order operator itself:
   `1/(k^2(k^2 + m2^2))` has residue ratio `-1` between the massive and the massless pole. The
   massive spin-2 is a ghost, so its Yukawa is repulsive. No paper is needed for this step; it
   follows from the `box(box + m2^2)` operator the repo had already computed.

**Where the original error came from.** The 2026-07-11 clause "massive spin-2 projector carries
`-1/3` trace vs `-1/2` for the massless graviton" is *correct about the projector* — tracelessness
of `P^(2)` forces its `theta theta` coefficient to `-1/(D-1) = -1/3`. But that is the **projector
trace coefficient**, not the potential coefficient. A correct intermediate was placed in the wrong
slot, and the leftover `-4/3` was then handed to the scalar.

**The trap, stated so it is not repeated.** The *spatial* potential of the full theory is
`Psi = -(GM/r)[1 - (2/3)e^{-m2 r} - (1/3)e^{-m0 r}]` — different numbers, and **both same sign**.
A stray "`1/3` on the spin-2 term" can come from misreading it. It does not rescue `+1/3`: putting
that pair in the temporal slot reproduces neither the correct bracket nor the old wrong one.

As `m2 -> oo` both potentials collapse to the pure Newtonian `-GM/r`. At **short** range
(`m2 r << 1`) the Einstein-Weyl bracket goes to `1 - 4/3 = -1/3`: gravity is **repulsive** below
the Yukawa range. The old assignment gave `+4/3`, enhanced attraction. The two assignments are
physically opposite. Note also that Einstein-Weyl *alone* is **not** `r -> 0` finite — Stelle's
finiteness needs both massive modes, and the `1 - 4/3 + 1/3 = 0` sum rule does not apply to GU.

- **COMPUTED (this repo):** the `box(box + m2^2)` TT operator and `m^2_eff > 0` (H15/H25).
- **COMPUTED (in-file, 2026-08-15):** the explicit `Phi, Psi` and their coefficients, from the
  three steps above. This *replaces* the 2026-07-11 status of "ARGUED, transcribed from Stelle".
  The derivation reproduces Lu-Perkins-Pope-Stelle Eq. (4.7a) exactly and independently
  reproduces the spatial trap potential, so the literature and the derivation agree.
- **STILL IMPORTED, unchanged:** the matter coupling. This is not a re-linearization of GU's full
  `|II|^2` action *with sources*; that gap is source-action requirement `SA-G9` and it stays open.

## Q2 -- PPN gamma and beta (COMPUTED)

`gamma(r) = Psi/Phi = (1 - (2/3)e^{-m2 r}) / (1 - (4/3)e^{-m2 r})`.

### The old "cross-check" was a false anchor

The 2026-07-11 note asserted `gamma(m2 r -> 0) = 1/2` and called it an anchor against the
literature that would have caught a linearization error. **It was not an anchor, and that is why
the wrong assignment survived four weeks.** The value `1/2` is:

- the value for the **massive mode alone**, not for the massless+ghost theory this note is about;
- *also* the Brans-Dicke `omega = 0` / `f(R)` value, so it does not identify the theory; and
- **exactly what the wrong assignment produces.**

A check that cannot fail certifies nothing. The three checks now asserted do discriminate:

- **`Q2a`** — the **massive sector alone** has `Psi/Phi = (1/3)/(2/3) = 1/2`. That is the genuine
  vDVZ / Fierz-Pauli discontinuity (light bending 3/4 of GR), stated about the object it is
  actually true of.
- **`Q2b` (discriminating)** — the full **Einstein-Weyl** `gamma(m2 r -> 0) = -1`, **not** `1/2`.
  The wrong assignment gives `+1/2` here. This endpoint separates them, and had it been asserted
  in 2026-07-11 the error could not have survived a single run.
- **`Q2e` (sanity, not an anchor)** — `gamma(m2 r -> oo) = 1`, GR recovered. True under *both*
  assignments, so it is reported as a sanity check and explicitly not relied on.

For the solar-system regime (`m2 r >> 1`):

`gamma - 1 = +(2/3) e^{-m2 r} + O(e^{-2 m2 r})` -- **positive**, exponentially suppressed.
GU predicts `gamma > 1` at solar-system distances. The old note had `-(2/3)`.

`beta -> 1` likewise (the nonlinear Yukawa correction is also `O(e^{-m2 r})`). The Cassini `gamma`
bound is ~3.5x tighter than the LLR `beta` bound, so `gamma` sets the binding lower bound on `m2`.

### Why no check caught it -- a third non-discriminating check

The 2026-08-09 banner named two checks that fail to discriminate: the `r -> 0` sum rule
(`1 + 1/3 - 4/3 = 0` symmetric under the swap) and the `gamma = 1/2` endpoint. There is a third,
and it is the one this bar's *verdict* rides on:

**the leading magnitude of `gamma - 1` is `(2/3)e^{-m2 r}` under both assignments.** Only the sign
differs. Cassini bounds `|gamma - 1|`, two-sided. So every number in Q3 below is degenerate between
the wrong and the corrected physics — the two `m2 r` floors are `10.274597` and `10.274540`, a
relative difference of `5.6e-6`. Repairing a ×4 sign-flipping error moved the published floor by
parts per million.

## Q3 -- The m2 lower bound and mu_DW consistency (COMPUTED)

Published bounds (comparison only, cited; not imported as targets):
- Cassini: `|gamma - 1| < 2.3e-5` (Bertotti, Iess, Tortora, Nature 425, 374 (2003)).
- LLR/Mercury: `|beta - 1| < 8e-5` (Williams, Turyshev, Boggs, PRL 93, 261101 (2004)).

`|(2/3)u / (1 - (4/3)u)| < 2.3e-5` with `u = e^{-m2 r}` gives `m2 r > 10.2746` (exact solve; the
leading-order route `(2/3)u < 2.3e-5` gives `10.2746` too, agreeing to `5e-5`). Over a
solar-system scale:

| scale `r` | `m2` lower bound | Yukawa range `1/m2 <` |
|---|---|---|
| 1 AU (`1.50e11 m`) | `6.9e-11 /m = 1.4e-17 eV` | `0.10 AU` |
| 1.6 R_sun (`1.11e9 m`) | `9.2e-9 /m = 1.8e-15 eV` | `0.16 R_sun` |

These are the *same numbers the note carried before the correction*, to five significant figures.
The bound on `m2` is fantastically small (`~1e-17 eV`): solar-system data only requires the
massive spin-2's Yukawa range to be shorter than `~0.1 AU`.

**Contrary controls (added 2026-08-15).** A falsifier with no configuration that fails it is not a
falsifier, and this note had none:

- `mu_DW = 1e-18 eV` gives `|gamma - 1| = 1.0`, `~4.4e4 x` the Cassini bound → **FALSIFIED**. The
  same machinery passes `mu_DW = 1e-15 eV`. So the bar can say FAIL and the pass is not vacuous.
- External comparator Brans-Dicke `omega = 100` gives `gamma = 101/102`, `|gamma - 1| = 9.8e-3`,
  `426x` the bound → correctly **FALSIFIED**. Reproduces the repo's own W220 negative control.

GU's `m2 = sqrt(m^2_eff) * mu_DW`, `m^2_eff in [5/6, 5/4]` (O(1), positive). Translating the floor:
`mu_DW > 1.5e-17 eV`. The natural `mu_DW ~ M_Pl = 1.2e28 eV` clears this by **~45 orders of magnitude**
(GU's massive spin-2 is Planckian, Yukawa range `~1e-35 m`, utterly unobservable). Critically, the
Cassini floor on `mu_DW` (`~1e-17 eV`) is *far weaker* than the ghost-decoupling bar (BAR 2, which
wants `mu_DW ~ M_Pl`): **the solar-system test adds no new binding constraint.**

## Q4 -- Verdict: GATED-ON-mu_DW, effectively PASSES

- **NOT FALSIFIED.** GU does not force a solar-system-visible deviation. `gamma, beta -> 1` as an
  exponentially suppressed Yukawa, not a structural O(1) shift. The wrong outcome (a light,
  long-range massive mode) is *not* forced: `m^2_eff` is O(1) and positive, so `m2` tracks `mu_DW`.
- **GATED-ON-mu_DW.** The pass is conditional on `mu_DW > ~1.5e-17 eV` (inverse-`~0.1 AU`). This
  floor is ~45 orders below the natural (and BAR-2-required) `M_Pl`; any non-pathological scale
  clears it.
- **SIGN, reported plainly.** The corrected assignment flips the *sign* of the predicted deviation:
  GU predicts `gamma > 1`, where this note used to say `gamma < 1`. Bertotti et al. measured
  `gamma - 1 = (2.1 +/- 2.3)e-5` — a positive central value consistent with zero at `0.91 sigma`.
  So the correction moves GU's predicted deviation onto the same side as the measured central
  value. **The statistical significance of that is zero** (it is a null measurement). Recorded
  here only so that nobody, in either direction, reads more into the sign flip than the data
  supports.
- **The verdict did not change, and that is itself the finding.** The input was wrong by a factor
  of four *and* in sign, and this bar's published numbers did not move. A bar whose verdict is
  invariant under that class of error in its own central input is weak. That is a statement about
  this test's discriminating power, not about GU.

## COMPUTED vs ARGUED

| Claim | Status | Confidence |
|---|---|---|
| GU = Einstein-Weyl (no `R^2` -> no scalar Yukawa) | COMPUTED (repo: `R^X + Weyl^2 + Lambda`) | high |
| TT operator `box(box + m2^2)`, `m^2_eff > 0` | COMPUTED (H15/H25) | high |
| `Phi, Psi` explicit form, `-4/3` (temporal) and `-2/3` (spatial) coefficients | **COMPUTED** in-file 2026-08-15 (projector traces + ghost sign; matches LPPS Eq. 4.7a) — *was* ARGUED with the wrong `+1/3` | high |
| massive spin-2 is a GHOST, Yukawa REPULSIVE | COMPUTED (residue ratio `-1` of `box(box+m2^2)`) | high |
| `gamma(r)`, `gamma - 1 = +(2/3)e^{-m2 r}`, endpoints `-1` (EW) and `1` (GR) | COMPUTED (from `Phi, Psi`) | high |
| `m2 > ~1.4e-17 eV`, `mu_DW > ~1.5e-17 eV` floor | COMPUTED (Cassini + `m^2_eff`) | high |
| natural `mu_DW ~ M_Pl` clears by ~45 decades | COMPUTED | high (given the natural-scale premise) |
| the matter coupling of the massive spin-2 | **STILL IMPORTED** — `SA-G9`, unchanged by this remediation | -- |

## Honest limits

- The coefficients `-4/3` (temporal), `-2/3` (spatial) and `+1/3` (scalar) are now **derived**
  here from projector-trace structure plus the ghost sign of the fourth-order operator, and
  *cross-checked* against the literature rather than copied from it. What is still **not** done is
  a re-linearization of GU's full `|II|^2` action **with matter sources**: this note uses the
  `box(box + m2^2)` TT operator computed in H15/H25 and solves *that*. The matter coupling remains
  imported. That gap is source-action requirement `SA-G9` and it is unchanged by this remediation.
- The absence of the scalar Yukawa rests on GU having no `R^2` term. If a source-action build later
  induces an `R^2` term, a second spin-0 Yukawa `+(1/3)e^{-m0 r}` appears — **attractive** — and it
  would also restore Stelle's `r -> 0` finiteness, which Einstein-Weyl alone does **not** have.
  Its `m0` would need the same (trivially cleared) heavy-mass floor. Not currently present.
- `mu_DW`'s dimensionful value is not derived (H24/H25 BAR 2). The solar-system bar constrains it
  only to `> ~1.5e-17 eV` -- far weaker than BAR 2's `~M_Pl`, and far weaker than the **sub-mm**
  channel, which `explorations/track2-conditional-numbers-2026-07-13.md` already reports as the
  *binding* one (~14 orders tighter). Under the corrected assignment the sub-mm Yukawa is 4x
  stronger and repulsive, so that exclusion gets **stronger**, not weaker.
- **`beta` is not recomputed** from the corrected potentials. What is asserted is the structural
  fact that the nonlinear correction is also `O(e^{-m2 r})`, so `beta -> 1` exponentially — true
  under either assignment, and Cassini `gamma` is the binding bar anyway. But "`beta -> 1`" here
  is an *argued* structural statement, not a computed PPN `beta`. It is the weakest link in Q2,
  unchanged by this remediation.
- Loop-level unitarity (BAR 1) is untouched; PPN is a purely tree-level / classical test.

## Owed, and not done here

The 2026-08-09 banner named two files. The wrong `alpha_Y = 1/3` is in fact live in **six more**,
all outside the H10-5 write scope, and all still wrong:

| file | sites |
|---|---|
| `explorations/track2-conditional-numbers-2026-07-13.md` | L111, L119, L193, L196, L227 |
| `explorations/path4-branchA-eos-gravity-correlation-2026-07-11.md` | L37, L70, L72, L167 |
| `explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md` | L52, L112, L115, L133, L221 |
| `tests/W61_path4_A_eos_gravity.py` | L36, L233-236 |
| `tests/W66_path4_wave2_alphaW.py` | L118, L125-129, L174 |
| `tests/W138_issuance_kill_battery.py` | L147 |

Direction of the error there: the corrected Yukawa is 4x stronger and repulsive, so the sub-mm
exclusion that track2 calls binding gets **stronger**. No verdict in those files flips in GU's
favour under the correction, and the already-falsified H36 point stays falsified a fortiori. That
is why deferring them is safe — not why forgetting them would be.

## RE-RANK signal

**GATED-ON-mu_DW** (bound: `mu_DW > ~1.5e-17 eV`, i.e. inverse-`~0.1 AU`), cleared by ~45 orders
for the natural `mu_DW ~ M_Pl` -> **effectively PASSES**. The solar-system PPN test does not
falsify GU and does not tighten the pre-existing `mu_DW` gate.

**Second signal, new (2026-08-15): rank this bar DOWN.** Its verdict is invariant under a ×4,
sign-flipping error in its own central input; it could not detect that defect in itself, and for
six days it could not run at all. Its pass is real but carries far less information than its
"cheap falsifier" framing implies. The `gamma > 1` sign it now predicts is genuine observational
content and is *currently unmeasurable*, because Cassini's bound is two-sided.

**Single next object:** unchanged — the ghost-mass scale `mu_DW` itself (H24/H25 BAR 2), the one
dimensionful datum the whole gravity sector hangs on. Every gravity bar (ghost decoupling, PPN,
sub-mm) reduces to whether the source action pins `mu_DW ~ M_Pl`.

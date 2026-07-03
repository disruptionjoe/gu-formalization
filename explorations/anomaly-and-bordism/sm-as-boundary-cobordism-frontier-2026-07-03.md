---
artifact_type: exploration
status: exploration
created: 2026-07-03
updated_at: "2026-07-03"
title: "SM as a boundary / cobordism condition -- opening LANE-SM-BOUNDARY: does requiring SM-shaped (anomaly-free, gauged) chiral boundary data PIN the external chiral background that carries the generation count? First-exploration packet: precise boundary-data interface (reusing source-action-family-index-interface-SPEC), the exact literature hooks (Callan-Harvey inflow; Wang-Wen / Freed-Hopkins-Teleman Omega^Spin_* cobordism; Dai-Freed), and ONE decidable first test (a 2D anomaly-inflow / flux toy) -- RUN. Honest outcome: local anomaly-freedom imposes a PARTIAL (mod-2, 2-primary) constraint on the external count but NO mod-3 / count-selecting constraint; pinning the count is a global bordism/Dai-Freed question that routes to the source-action bottleneck."
grade: "exploration. Scoping + one honest toy, NOT a proof. The toy result (2D: anomaly-free U(1) content forces net external count EVEN, provably via q^2==q mod 2; leaves all mod-3 residues free) is computed + basis-free-proved (2008 asserts). Everything about the true RS Y14 bundle / actual SM group remains scoped, not computed. NO target import: 3 is never assumed, inserted, or divided out; the generation-count verdict stays OPEN."
depends_on:
  - canon/source-action-family-index-interface-SPEC.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - canon/external-topological-index-flux-RESULTS.md
  - canon/function-space-index-conservation-residual-closure-RESULTS.md
  - RESEARCH-PROGRAM.md
  - NEXT-STEPS.md
scripts:
  - tests/sm-boundary/anomaly_inflow_toy.py
---

# SM as a boundary / cobordism condition (opening LANE-SM-BOUNDARY)

**Status.** Exploration-grade. Steps are tagged `[scoped]`, `[computed]`, or `[open]`. This packet
opens the frontier lane named in `RESEARCH-PROGRAM.md` §"The frontier" (1) and
`NEXT-STEPS.md` LANE-SM-BOUNDARY. It does the three bounded first sub-goals: (a) state the
boundary-data interface precisely; (b) map the exact literature hooks; (c) name and RUN one decidable
first test. It does **not** attempt the lane's success condition (a computed constraint on the actual
external background from the actual SM); it establishes the interface and the honest current verdict.

**The offensive question.** The defensive result is banked: the mirror-balanced Clifford-RS interior
cannot force its own count (`canon/external-by-structure-synthesis-RESULTS.md`), and the count enters
as an external topological index = flux, ANY integer
(`canon/external-topological-index-flux-RESULTS.md`). The frontier turns this around: **fix the
interior, and REQUIRE the actual Standard Model (three anomaly-free generations, the SM gauge group)
as the chiral boundary data. Is the external structure then PINNED?** If yes, "an outside lights the
inside" sharpens to "the inside and its required outside are a matched pair."

---

## (a) The boundary-data interface, in exact terms

The interior sector hands the index theorem a *balanced* operator; the count is whatever an external
chiral background contributes through the index. Precisely, reusing the decomposition of
`canon/external-by-structure-synthesis-RESULTS.md`:

> `chi = chi_interior + chi_external`, with `chi_interior` provably even (2-primary) over the
> delimited class C, and `chi_external` the net chiral index of an external topological background.

`chi_external` is what an external background must SUPPLY to the index theorem. Reusing the four
objects the source action must expose (`canon/source-action-family-index-interface-SPEC.md`, "What
the source action MUST expose to the harness"), the boundary-data interface is exactly these,
now read as *what SM-shaped boundary data would have to fix*:

| # | interface object (SPEC 5(i)-(iii)) | what an external background supplies | what "SM-shaped" would fix it to |
|---|---|---|---|
| 1 | vertical bundle + clutching over the metric fiber `GL(4,R)/O(3,1)` (`K3`-fibered family) | the chiral bundle whose index is `chi_external` | the SM chiral rep content as the fiber's associated bundle |
| 2 | a-priori `Y14` boundary connection (replaces auxiliary spectral strength `t`) -> APS spectral section | the boundary condition / spectral section at the noncompact end | the SM gauge connection as the boundary datum (`eta`/APS) |
| 3 | family symbol of the GU RS operator (`Phi`-homotopy / symbol certificate) | the symbol class whose pushforward is the count | the SM-gauge-coupled Dirac symbol |
| 4 | the `ch2`/`eta` correction as an actual families-index integer `N`, + `H`-line normalization | the number `chi_external = N` itself | pinned iff SM anomaly-freedom + bordism-triviality force `N` |

**The precise interface statement.** An external background fixes a generation count iff it supplies
(1)-(3) and thereby determines the families-pushforward integer `N` of obligation (4), **without
importing `chi`** (no `chi(K3)=24`, no `/8`, no `Ahat=3`, no contractible-fiber=>1 -- the SPEC's
firewall-guarded DEAD-ENDS). The frontier question is then sharp:

> Does requiring the boundary data (1)-(3) to be **SM-shaped** -- anomaly-free under the SM gauge
> group, and a valid *boundary* of a bulk (cobordism-trivial / Dai-Freed anomaly = 0) -- CONSTRAIN
> the admissible `N`?

Two logically separate constraints an "SM-shaped boundary" imposes, at two different topological
depths:

- **Local (perturbative) anomaly inflow** -- Callan-Harvey. The boundary chiral content's local
  anomaly polynomial must be cancelled by inflow from the bulk. This is a condition on the *anomaly
  polynomial* (characteristic classes / the `ch` of the chiral bundle) -- a **rational / local**
  datum. It sees obligation (3)'s symbol but not the torsion in (4).
- **Global (nonperturbative) anomaly** -- Dai-Freed / cobordism. For the chiral theory to exist on a
  boundary at all, its partition function must extend over the bulk: the **bordism invariant** in the
  relevant `Omega^{Spin}_*` (or twisted/`Spin-G`) group must vanish, and the Dai-Freed `eta` must be
  well-defined. This is a **torsion** datum -- exactly the arena (`Z/3 ⊂ pi_3^s = Z/24`) where a
  count could hide, by the program's own CRT two-arena structure.

The interface prediction, before any computation: **the count-selecting question is a *global*
(torsion / bordism) question, not a *local* (anomaly-polynomial) one.** The decidable first test (c)
checks exactly this split.

---

## (b) Literature hooks and what each would constrain

Exact hooks, and the precise object each pins in the interface above. `[scoped]` throughout -- these
are the correct tools; none is executed here beyond the toy.

1. **Callan-Harvey anomaly inflow** (Callan & Harvey, *Nucl. Phys. B* 250 (1985) 427). A chiral
   zero-mode on a defect/boundary has a gauge anomaly cancelled by inflow from a bulk
   Chern-Simons/`theta`-term. **Constrains:** obligation (3) -- the boundary symbol's *local* anomaly
   polynomial must match the bulk inflow. In the interface this is a condition on the anomaly
   `ch`-classes, i.e. the *rational* part of `N`. **What it cannot do:** fix the torsion part of `N`;
   inflow-matching is a statement in de Rham / rational cohomology. This is the hook the toy (c)
   realizes in 2D.

2. **Wang-Wen / Freed-Hopkins cobordism classification of anomalies** (Wang & Wen, e.g.
   *PRX* 8 (2018) 011026 and the SM-anomaly / "gapping" analyses; Freed-Hopkins,
   *Reflection positivity and invertible topological phases*, and Freed-Hopkins-Teleman for the
   `TMF`/`Omega`-module machinery). Anomalies of a `d`-dim theory = the invertible-TQFT / deformation
   class = an element of a **bordism group** `Omega^{Spin(-G)}_{d+1}` (or its Anderson dual / `TMF`
   refinement). SM anomaly-freedom in 4D is the statement that the SM fermion content's class in the
   relevant `Omega^{Spin x_{Z/2} G_SM}_5` **vanishes** (all local + the mod-2 Witten `SU(2)` +
   any `Z/16` / new-SU(2) global pieces cancel per generation). **Constrains:** obligation (4)
   directly -- it is the *global* invariant `N` must be compatible with. In the interface this is the
   torsion datum; the SPEC's honest `ch2 = -5376`, `APS eta = 0` values are the rational/2-primary
   shadow of it. **What it would settle:** whether SM-shaped boundary data forces `N` into a subgroup
   that keeps (or kills) an odd-torsion (mod-3) piece.

3. **Dai-Freed theorem** (Dai & Freed, *J. Math. Phys.* 35 (1994) 5155; Witten-Yonekura exposition).
   The fermion partition function is the exponentiated `eta`-invariant of the Dirac operator; global
   consistency = the `eta` extends over every bounding manifold = the bordism invariant vanishes.
   **Constrains:** obligation (2) -- the APS spectral section / `Y14` boundary connection -- and ties
   it to (4). This is the exact machinery `canon/rs-boundary-eta-2primary-RESULTS.md` already touched
   (RS boundary reduced-`eta` on `L(2;1)` is 2-primary). **What it would settle:** whether the
   *actual* RS boundary `eta`, coupled to an SM gauge connection, carries an odd piece. This is the
   genuinely-open true-RS-Y14 computation named as the residual in
   `canon/function-space-index-conservation-residual-closure-RESULTS.md`.

**Convergent reading of the hooks.** (1) constrains the rational/local part; (2)+(3) constrain the
global/torsion part; the count -- if it lives anywhere -- lives in the torsion part (CRT `Z/3`
arena). So the hooks predict: **local inflow is necessary but count-blind; the count question is a
Dai-Freed / Wang-Wen bordism-torsion question.** The toy tests the first half of this decisively.

---

## (c) The one decidable first test (named + RUN)

**Named test.** The smallest computation that tells you whether *local* SM-shaped anomaly-freedom
constrains the admissible external chiral background: a **2D anomaly-inflow / flux toy**. Build the
external chiral background as a uniform U(1) flux `Phi` (the same 2D Wilson-Dirac that carries
`index = flux` in `canon/external-topological-index-flux-RESULTS.md`), let the boundary content be a
multiplet of 2D Weyl fermions `{(q_i, eps_i)}` (integer charge, chirality), and ask: **over all
multiplets that are anomaly-free** (`A_grav = sum eps_i = 0` and `A_gauge = sum eps_i q_i^2 = 0`,
the 2D Callan-Harvey inflow coefficients), **what net external count `Nhat = sum eps_i q_i` is
achievable?** (The realized count is `N = Nhat * Phi`.) This is decidable by bounded integer search
plus a basis-free parity proof. NO target imported: we read off the achievable set, never assume 3.

**Certificate.** `tests/sm-boundary/anomaly_inflow_toy.py` (2008 hard asserts, exit 0).
Part A confirms non-vacuously on a 16x16 lattice that a charge-`q` species sees effective flux
`q*Phi` and has `index = q*Phi` (checked `q = 1,2,3`). Part B enumerates anomaly-free multiplets
(`|q| <= 4`, up to 6 Weyls) and records the achievable `Nhat`, with a 2000-draw basis-free check of
the parity identity.

**Result (computed, honest, NO target import) -- outcome (iii), a PARTIAL constraint:**

- Local anomaly-freedom does **NOT** pin `Nhat` to a single value: a whole lattice
  `{..., -4, -2, 0, 2, 4, ...}` is reachable. So SM-shaped *local* anomaly data does **not** select a
  count and does **not** force or forbid 3.
- But it is **NOT** unconstrained either: **every anomaly-free `Nhat` is EVEN.** This is a *provable*
  mod-2 fact, not a search artifact: `q^2 == q (mod 2)`, so
  `A_gauge = sum eps_i q_i^2 == sum eps_i q_i = Nhat (mod 2)`, hence `A_gauge = 0 => Nhat` even.
  (Verified basis-free over 2000 random multiplets.)
- Crucially, **all residues mod 3 remain reachable** -- local anomaly-freedom imposes **no** mod-3 /
  odd-torsion constraint.

**Reading.** The local (Callan-Harvey / perturbative) anomaly condition constrains the external count
**entirely within the 2-primary arena** (it forces parity) and leaves the count-carrying odd-torsion
(`Z/3`) arena **completely free**. This *re-derives the program's CRT two-arena split from the
boundary side*: local anomaly inflow touches only `Z/8` (parity); the count lives in the disjoint
`Z/3` the local condition cannot see. Therefore **pinning the actual count is a global (mod-3 /
bordism / Dai-Freed `eta`) question, unreachable from the local anomaly polynomial.** That global
datum is exactly obligation (4) of `canon/source-action-family-index-interface-SPEC.md` -- the
`ch2`/`eta` correction and the family symbol -- i.e. the **source-action bottleneck**.

---

## Honest read: can this lane move now, or is it blocked?

- **Moves now (done here).** The boundary-data interface is stated precisely (a); the literature hooks
  are mapped to exact interface objects (b); one decidable test is named and run, with a genuine,
  non-trivial, target-free verdict (c): *local SM-shaped anomaly-freedom is count-blind (2-primary
  only)*. This is a real partial result -- not "unconstrained" (the lane's kill condition is NOT met)
  and not "pinned" (no count is selected). It converges with the CRT structure from a new direction.
- **Blocked on the source action (the pinning question).** Whether SM-shaped boundary data actually
  PINS the count is a **global torsion** question. The toy shows the local layer cannot answer it; the
  answer requires the `Omega^{Spin(-G_SM)}_*` bordism / Dai-Freed `eta` datum for the true RS Y14
  bundle -- i.e. interface obligations (2)-(4), which are the **exact same unbuilt objects** the
  source-action SPEC lists as OPEN (`5(iii)`: the family symbol and the `ch2`/`eta` correction). This
  routes straight to the source-action bottleneck already carded in the SPEC and in
  `canon/function-space-index-conservation-residual-closure-RESULTS.md`'s "model -> true RS Y14
  bundle" residual.

**Exact missing SPEC input to unblock the pinning question.** Obligation (4) of
`canon/source-action-family-index-interface-SPEC.md`: a geometric families-pushforward integer `N`
over the metric fiber (with the `H`-line normalization), delivered *with its torsion / `eta`
refinement*, and the family symbol (obligation 3) coupled to an SM gauge connection -- all without
importing `chi`. Until the source action exposes those, the lane's *pinning* verdict stays **OPEN**;
the generation-count verdict is **untouched and remains OPEN**.

**Not promoted in this pass.** Exploration-grade; GU-independent framing; no canon/paper edit. Canon
promotion is agent-owned as of 2026-07-03 (this note simply hasn't been promoted yet). The count verdict
stays OPEN (a verdict change would still pause for Joe).

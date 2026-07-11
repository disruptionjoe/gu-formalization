---
artifact_type: exploration
status: exploration
created: 2026-07-11
title: "H2 rep-canonicity (Wave 3, the COUNT crux): does the 2026-07-11 conformal/Bach identification SELECT a signature and break the (9,5)-vs-(7,7) tie? HONEST OUTCOME: UNDER-DETERMINED (with named decider). The conformal sector is PROVABLY BLIND to the deciding sign -- the conformal action sqrt|g| C^2 (=48 M^2/r^6 on Schwarzschild, BIT-IDENTICAL for g and -g, exact all orders in M), the Bach field equation, the base conformal group so(4,2)~so(2,4), and the (6,4)-native u(3,2)->so(4,2) chain are ALL invariant under eta->-eta of the base, and eta->-eta is EXACTLY the mostly-plus/mostly-minus toggle that swaps (9,5)<->(7,7). So conformal/Bach is not merely silent, it is STRUCTURALLY BARRED from being the decider: it factors through the conformal class, invariant under the very move that toggles the signature. Fifth independent signature-agnostic angle; STRENGTHENS not overturns BIG-SWING. Named decider: a GU-native quantity NOT invariant under eta->-eta (outside the now-blind Weyl/Bach sector) -- a base-pullback term linear in g, or the asymmetric 2-primary Witten Z/2. Count stays LOCATED-not-forced. No target imported."
grade: "exploration / strong. DECIDING computation is exact sympy from scratch (Christoffel->Riemann->Weyl->Weyl^2 on strong-field Schwarzschild for g and -g; Ricci-flat verified; Weyl NONZERO (24 components); Weyl^2 = 48 M^2/r^6 identical). Supporting: DeWitt fiber (6,4) bit-identical under eta->-eta (numpy, quadratic-in-eta => exact); so(4,2)~so(2,4) via Killing signature (8,7)/dim 15/rank 3 (numpy); so(4,2) embeds in both totals (signature arithmetic); VG-V3 EMPTY minimal certificate reproduced (no orthogonal J commutes with the trace-line projector, floor 5.2>=2). Honest limitations: (a) the g->-g invariance of Weyl^2 is a general index-counting fact WITNESSED on Schwarzschild, not a proof over all metrics (the index argument is stated; Schwarzschild is one exact witness). (b) 'no GU-native selector outside the conformal sector' is an absence-of-forcing argument, not a proof none exists -- but the burden is on FORCING a signature and none is exhibited. (c) does not compute the 2-primary Witten channel (asymmetric; can only exclude H). No verdict/canon/posture change; the prior UNDER_DETERMINED stands and is strengthened."
depends_on:
  - explorations/big-swing-2026-07-03/BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED.md
  - explorations/big-swing-2026-07-06/VG-V3-j-commutant-conformal-native.md
  - explorations/sequential-goals-2026-07-09/SG1-signature-carrier-parity-77.md
  - explorations/threads/D-structural-conformal-willmore-functor-scoping-and-first-swing-2026-07-11.md
  - explorations/wave1/H1-gravity-shadow-bach-branch-2026-07-11.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - canon/ghost-parity-krein-synthesis.md
scripts:
  - tests/wave3/H2_signature_canonicity.py
---

# H2 -- rep-canonicity: does the conformal/Bach identification select (9,5) or (7,7)?

## The swing

The C-07 quaternionic-parity wall -- the program's structural obstruction to an odd generation
count -- holds on the H-class carrier `Cl(9,5) = M(64,H)` (`J^2 = -1`, Kramers forces even signature)
and DISSOLVES on the R-class carrier `Cl(7,7) = M(128,R)` (`J^2 = +1`, an odd rank-3 J-projector is
reachable, SG1 2026-07-09). So the count is FORCED-even iff (9,5), and LOCATED-not-forced iff the
signature is a declared convention. BIG-SWING (2026-07-03) graded this **UNDER_DETERMINED**: the only
GU-native mover of `p-q mod 8` is the base Lorentzian metric-SIGN convention, and no GU-native
selector for that sign was found.

Wave 3 pushes the question with the **fresh 2026-07-11 lens**: D1 (`threads/D-...`) computed that
H-class GU's gravity section-EL IS the conformal-gravity **Bach** operator on the spin-2 sector
(`box^2 h = -4 Bach^(1)`), and H1 (`wave1/H1-...`) showed Bach-flat clears the exact vacua -- GU
gravity is **conformal-Willmore / fourth-order (Bach) class**, living on the **(6,4) DeWitt fiber**.
H1's own note flags H2 as deciding "whether the conformal reading is GU-native on the (6,4) DeWitt
form and forced-vs-located." So the decidable question is:

> **Does the conformal/Bach identification SELECT a signature -- i.e. does the conformal structure,
> now that it is GU-relevant, break the (9,5)-vs-(7,7) tie that BIG-SWING left under-determined?**

Adversarial pre-registration: the prior verdict is UNDER_DETERMINED; do not overturn it without a
GU-native quantity that FORCES `p-q`, and rule out that any claimed forcing is an imported
convention.

---

## What was computed (`tests/wave3/H2_signature_canonicity.py`, exit 0)

### Section 1 -- the (9,5)<->(7,7) toggle IS `eta -> -eta` of the base

Reproduced: the closed form `p-q = d + d^2/2` (`d = #space - #time` of the base) gives `d=+2`
(mostly-plus (3,1)) `-> p-q=4 ->` (9,5)/M(64,H)/`J^2=-1`; `d=-2` (mostly-minus (1,3)) `-> p-q=0 ->`
(7,7)/M(128,R)/`J^2=+1`. The DeWitt trace-reversed fiber form `G(h,k) = tr(eta h eta k) - 1/2
tr_eta(h) tr_eta(k)` is quadratic in `eta`, so its Gram matrix is **bit-identical** under
`eta -> -eta` (verified `np.array_equal`), giving fiber signature **(6,4) for both base signs**.
**The sole difference between (9,5) and (7,7) is the single move `eta -> -eta`.**

### Section 2 -- DECISIVE: the conformal/Bach sector is `eta -> -eta` invariant (exact Schwarzschild)

From scratch in exact sympy (Christoffel -> (1,3) Riemann -> Ricci -> Weyl -> Weyl^2) on strong-field
Schwarzschild, for the metric `g` and its sign-flip `-g`:

- Schwarzschild is Ricci-flat (exact vacuum), Weyl is **NONZERO** (24 nonzero (1,3)-components) -- so
  the invariance below is a genuine cancellation, not triviality.
- The **(1,3) Weyl tensor `C^a_{bcd}` is IDENTICAL for `g` and `-g`**, exactly, all orders in M.
  (Mechanism: `C^a_{bcd}` is built from Christoffels `~ g^{-1} dg`, invariant under `g -> lambda g`.)
- The **Weyl^2 action scalar `C_{abcd} C^{abcd} = 48 M^2/r^6` is IDENTICAL for `g` and `-g`**, exactly.
  (Mechanism: one lower-index `g` picks up `(-1)`, three upper-index `g^{-1}` pick up `(-1)^3`, product
  `+1`.)

So the conformal-gravity action density `sqrt|g| C^2` **and** the Bach field equation are blind to
`eta -> -eta`. That sign IS the (9,5)<->(7,7) toggle (Section 1). **The conformal/Bach identification
cannot select the signature.** Adversarial control: a "conformal selects" outcome would appear as
`W2[+] != W2[-]`; it does not.

### Section 3 -- the base conformal GROUP is the same real form for both signs

The conformal algebra of `R^{p,q}` is `so(p+1,q+1)`: base (3,1) `-> so(4,2)`, base (1,3) `-> so(2,4)`.
Built explicitly, both have **dim 15, rank 3, Killing signature (8,7)** -- the same real Lie algebra
(`so(4,2) ~ so(2,4)`). And `so(4,2)` embeds in BOTH `so(9,5)` and `so(7,7)` (a (4,2)-signature 6-plane
fits in both). The conformal symmetry algebra distinguishes neither the base convention nor the
carrier.

### Section 4 -- the (6,4)-native conformal `so(4,2)` sits in both totals and is not GU-native

The VG-V3 chain `so(6,4) > u(3,2) > su(2,2) ~ so(4,2)` is built from an orthogonal `J` on the (6,4)
fiber (exists: 6,4 both even). Since the fiber is (6,4) in BOTH totals (Section 1), the chain is
present identically in both -> signature-agnostic. And it is NOT GU-native: reproduced the minimal
VG-V3 EMPTY certificate -- no orthogonal `J` commutes with the trace-line projector `P1` (commutant
dim 82 = 1+81; constrained `||J^2+I||`-search floor **5.2 >= 2**; exact 1-dim + 9-dim odd-block parity
obstruction). The conformal `so(4,2)` is an import that breaks GU's fiber decomposition; it supplies
no selector.

---

## Verdict

**UNDER-DETERMINED (with named decider).** The conformal/Bach identification does **not** break the
(9,5)-vs-(7,7) tie. The conformal action `sqrt|g| C^2`, the Bach field equation, the base conformal
group `so(4,2)`, and the (6,4)-native `u(3,2) -> so(4,2)` chain are all invariant under `eta -> -eta`
of the base, and `eta -> -eta` is exactly the mostly-plus/mostly-minus toggle that swaps (9,5)<->(7,7).

This is a **fifth independent signature-agnostic angle**, after BIG-SWING's four (anomaly-freedom,
H-structure/shiab, the Clifford reconstruction, the base-sign adversary). It **strengthens**
UNDER_DETERMINED; it does not overturn it. No GU-native lever here forces `p-q`.

**The sharpening (the value added).** Conformal/Bach is not merely silent -- it is **structurally
barred** from being the decider, because it factors through the **conformal class**, which is
invariant under the exact move (`eta -> -eta`) that toggles the signature. The fresh gravity finding
does not resolve H2; it **narrows the decider** by removing the entire Weyl/Bach/conformal sector from
the candidate pool. Adversarially: I could not manufacture a forcing, and the one place the fresh
lens might have supplied one (the conformal structure being now GU-relevant) is provably blind.

**Named decider (not manufactured here).** A GU-native quantity that is **not** invariant under
`eta -> -eta` of the base (equivalently, fixes `sign(d)` = mostly-plus vs mostly-minus), and is
therefore OUTSIDE the now-blind conformal sector. Concretely one of:

1. a **base-pullback / observerse tautological term LINEAR in `g`** (not the quadratic DeWitt fiber
   form), carrying the timelike-norm sign. This is the single remaining lever from BIG-SWING's next
   steps; if GU structure supplies none, UNDER_DETERMINED is **final**.
2. the **2-primary Witten / global Dai-Freed `Z/2` anomaly** for GU's actual content -- **asymmetric**:
   it can only EXCLUDE the H-class (push toward (7,7)/dissolution), never FORCE (9,5). It cannot move
   the verdict toward FORCES_9_5.

Absent such a quantity the count stays **LOCATED-not-forced**: the C-07 even-parity wall is exactly as
firm as the standard mostly-plus (3,1) convention -- natural, but a declared choice (canon C-04).

---

## Honest caveats

1. **The Weyl^2 `eta -> -eta` invariance is a general index-counting fact WITNESSED on Schwarzschild,
   not a proof over all metrics.** The index argument (one lower `g`, three upper `g^{-1}`, product
   `+1`; Christoffels invariant under constant rescaling) is general and stated; Schwarzschild is one
   exact, strong-field, nonzero-Weyl witness. A fully general symbolic-metric check was not run (the
   index argument makes it unnecessary, but it is not machine-verified on a generic metric here).
2. **"No GU-native selector outside the conformal sector" is an absence-of-forcing argument, not a
   proof none can exist.** The burden is on FORCING a signature; none is exhibited anywhere. Candidate
   (i) (a base term linear in `g`) is named but not searched in GU's actual tautological/observerse
   structure -- that is the concrete next computation.
3. **The 2-primary Witten channel is not computed** (candidate (ii)); it is asymmetric and can only
   exclude H, so it cannot flip the verdict toward FORCES_9_5.
4. **VG-V3 dependence.** Section 4 reproduces only the minimal (trace-line) EMPTY certificate; the full
   four-datum EMPTY scan lives in VG-V3 and is cited, not re-run.

---

## Re-rank signal

- **Does this settle the count?** No -- and that is the honest, valuable outcome. It settles that the
  **conformal/Bach reading, the newest and most promising lever, cannot settle it**: the gravity
  finding is signature-agnostic by construction. The count stays LOCATED-not-forced; C-07 stays
  genuinely conditional; canon C-04 (signature is a declared input) is re-confirmed by a fifth angle.
  No canon/verdict/posture change; no target imported.
- **Coupling to H15's gravity fork (via the conformal structure).** DECOUPLED at the signature level.
  H15 (pure Bach `box^2` vs Stelle `R + Weyl^2`) is a fork WITHIN the conformal/fourth-order sector --
  the sector this test proves is blind to (9,5)-vs-(7,7). So H15's outcome cannot decide H2, and H2's
  outcome cannot decide H15: the count-crux and the gravity/ghost fork are **independent**, exactly as
  the Condorcet note posited ("H2 distinct from H15"). The "mild coupling" (O(1,1) vs O(96,96) Krein)
  is likewise signature-agnostic: the triplet Krein form is `(+96,-96,0)` in (9,5), (7,7), AND (14,0)
  (canon `ghost-parity-krein-synthesis`), so the ghost/Krein sector adds no selector either.
- **What the next reflection should focus on.** The decider is now sharply named and OUTSIDE gravity:
  search GU's **base-pullback / observerse tautological structure for a term LINEAR in `g`** that
  carries the timelike-norm sign (candidate (i)). Two outcomes, both terminal: if such a term exists
  and is GU-forced, it FORCES a signature (resolving the count); if the observerse -- the space of
  metrics -- provably carries no preferred metric-sign (as BIG-SWING argued), then UNDER_DETERMINED is
  **final** and the program should stop hunting a signature selector and record the count as
  irreducibly located-not-forced. Either way, do NOT route further signature work through the conformal
  sector -- this test proves that sector cannot decide it.

---
artifact_type: exploration
status: exploration
created: 2026-07-11
title: "H26 (Wave 23): does [P,S]=0 survive renormalization? The COMMUTATION leg is radiatively stable (P is a group element / exact automorphism, COMPUTED residual 0), but loop-level ghost UNITARITY (positivity) does not follow from it and is unproven anywhere for 4-derivative gravity -- VERDICT OPEN, obstruction pinned to the unbuilt source action"
grade: "exploration / THEOREM (algebraic scope: exact so(9,5) vector rep + Cl(9,5) spinor rep, residual 0) + primary-source-fenced loop statement + a model-grounded separation argument. Verdict vocabulary: OPEN. No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3} assumed, inserted, hardcoded, or divided by; no count is touched. The number 3 does not appear in any load-bearing step."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - tests/wave8/H23_source_action_construction.py
  - tests/wave5/H16_stelle_viability.py
  - explorations/big-swing-2026-07-06/VG-SC-bateman-turok-loop-and-degenerate.md
  - explorations/big-swing-2026-07-06/R1-pu-pt-vs-ghost-parity.md
  - papers/candidates/one-residual-complete-picture/one-residual-complete-picture-2026-07-11.md
scripts:
  - tests/wave23/H26_loop_ghost_unitarity.py
external_refs:
  - "Bateman & Turok, Escape from Ostrogradsky via Hidden Ghost Parity, arXiv:2607.00096 (2026)"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order derivative Pais-Uhlenbeck oscillator, PRL 100, 110402 (2008), arXiv:0706.0207"
  - "Stelle, Renormalization of higher-derivative quantum gravity, Phys. Rev. D 16, 953 (1977)"
---

# H26: does the ghost-parity clearance [P, S] = 0 survive loops?

**The object.** GU's gravity conditional theorem clears the massive Stelle/Bach ghost at
**tree level** via a Krein quantization: the ghost parity `P = K` implements the Cartan
involution of `so(9,5)` and commutes with the natural covariant dynamics, `[P, S] = 0`
(H23 A/B/C; canon `ghost-parity-krein-synthesis.md`), which is the Bateman-Turok
positivity condition. The deepest open question in the gravity leg: does `[P, S] = 0`
**survive renormalization**, or is it a tree-level accident that loops break -- the generic
killer of 4th-order-gravity unitarity (the Pais-Uhlenbeck / Stelle-Mannheim dispute)?

**One-line answer.** The **commutation** leg of `[P, S] = 0` is radiatively **stable**
(COMPUTED: `P` is an element of the gauge group and an exact automorphism, so it is
inherited by the effective action to all orders). But loop-level ghost **unitarity**
(positivity of the Born rule) is a *strictly stronger* condition that does **not** follow
from the commutation, is proven only at tree level anywhere in the literature, and cannot
be checked in GU because GU has no built source action / S-matrix. **Verdict: OPEN.**

---

## The four questions

### Q1 -- Is `[P, S] = 0` radiatively stable? Is `P` a symmetry of the *interacting* action?

**COMPUTED: the commutation is protected by symmetry.** This is the crux, and it is not
asserted -- it is exhibited (`tests/wave23/H26_loop_ghost_unitarity.py`, Parts A and B,
all residuals `0.00e+00`):

- **`P` is a GROUP element, not merely a linear map.** On the `so(9,5)` vector rep the
  Cartan involution is conjugation by the metric itself, `theta = Ad(eta)`, so the
  involution matrix `P_V = eta` satisfies `P_V^T eta P_V = eta` exactly -- `P in O(9,5)`
  (A1, residual `0`, `det P = -1`). On the spinor side, the Krein metric `beta_S`
  (product of the timelike gammas of `Cl(9,5)`) satisfies `beta_S^dag beta_S beta_S =
  beta_S` (B2, residual `0`): it is an element of the non-compact form `U(32,32;H) =
  Sp(32,32;H)`, signature `(+64, -64)` (B4), matching canon.
- **`theta` is an exact Lie-algebra automorphism** (A3, residual `0` over 300 sampled
  bracket pairs) that fixes the compact `so(9)+so(5)` (46 generators) and flips the 45
  boosts (A4), and it preserves every invariant tensor a covariant vertex can be built
  from: the metric `eta` (A1) and the Killing form (A6, mixed compact/boost block `0`).
- **Therefore every `so(9,5)`-covariant vertex commutes with `P` exactly.** GU's source
  action `S = |theta|^2` is the `eta`-contraction `Q(X) = eta_{ab} X^a X^b`, and
  `Q(P X) = Q(X)` to residual `0` (A5). On the spinor side `beta_S` implements the Cartan
  involution on the generators `sigma_{ab}` via pseudo-anti-Hermiticity `beta sigma +
  sigma^dag beta = 0` (B3, residual `0`), reproducing H23 (C) independently.

**The argument that makes it radiatively stable.** A symmetry realized by a *group
element* (here `P = beta_S in Sp(32,32;H)`, `P = eta in O(9,5)`) is a symmetry of the
classical action *and* of the full quantum effective action to all loop orders, because
the effective action is a gauge-/group-invariant functional (BRST / quantum action
principle), absent an anomaly. This is genuinely stronger than "P commutes with the free
kinetic operator": P is an automorphism of the entire covariant interaction structure, so
loops (which dress covariant vertices with covariant counterterms) cannot generate a
`P`-odd term. **`[P, S] = 0` in the commutation sense is COMPUTED radiatively stable.**

**The honest caveat (why this is not yet SURVIVES).** Two gaps keep this from closing the
physics question:
1. **Anomaly caveat.** "Absent an anomaly" is load-bearing. A discrete-symmetry anomaly in
   `P` would require the fermion `C2`/generation-count computation, which is itself OPEN
   (`swing-ghost-parity-no-chiral-selection.md`; the count sector is untouched here). No
   anomaly is exhibited, but none is excluded either.
2. **Commutation is not the operative loop condition** (see Q2/Q3). This is the decisive
   point and the reason the verdict is OPEN rather than SURVIVES.

### Q2 -- Does the Bateman-Turok mechanism extend to loops?

**ARGUED (primary-source-fenced, inheriting the VG-SC intake of arXiv:2607.00096).** BT's
"to all orders" and "tree level" claims are about **two different properties**:

| property | order | status in BT |
|---|---|---|
| pseudo-unitarity / optical theorem (`S^dag_K S = 1`) | **all orders** | claimed, from the spectral property + Krein-Hermitian interaction |
| **positivity** of transition probabilities | **tree level only** | proved (the theorem) |
| loop-integral IR finiteness | loop | claimed in a **to-appear** companion [25] |
| collinear IR divergences of asymptotic states | loop | **open** ("carefully regulated and resummed") |
| loop-level **positivity** | loop | **never claimed** |

So BT's all-orders result is exactly the *commutation/Krein-unitarity* leg that Part A/B
shows is protected. What BT do **not** prove at loops is **positivity**, and their stated
obstacle is analytic (collinear IR divergences of the massless double-pole theory), not a
ghost-symmetry failure. GU's Bach-sector `[P, S] = 0` therefore instantiates the
**tree-level** BT mechanism; the loop-stable *positive* version is not established in the
source itself. There is moreover **no rule in BT for odd-ghost-parity states on internal
lines** -- the positivity rule lives at the level of asymptotic projections/observables --
so the internal-line question is open *in the literature*, not just in GU's reconstruction.

### Q3 -- Pais-Uhlenbeck / Stelle-Mannheim benchmark: resolve, inherit, or sidestep?

**ARGUED: GU INHERITS the contested corner; it does not resolve it, and it partly
sidesteps the tree-level ghost.**

- **Sidesteps at tree level.** The wrong-sign antigravity kill is retired (H16: healthy
  massless graviton, `m^2 = +1/2 > 0`, attractive, positive `G`); GU lands on the
  *attractive* side of the Stelle-Mannheim corner.
- **Inherits at loop level.** Positivity at loops is precisely the Stelle-Mannheim /
  Pais-Uhlenbeck open dispute. R1 (`cg_r1_pu_pt_vs_ghost_parity.py`) sharpened this: on
  the PU toy the Bender-Mannheim `C` operator and the BT ghost parity are the *same* `Z2`
  on the PT-unbroken diagonalizable domain, and they **fail together** at the
  equal-frequency Jordan boundary, where a two-line theorem shows **no** positivity-
  compatible ghost parity of any kind exists (only the kinematic Krein metric survives).
  GU's kinematics-only status sits exactly on that boundary: it has the Krein metric
  (exact, `(+64,-64)`) but no `S` to certify PT-unbroken diagonalizability.
- **The settled-vs-contested split.** SETTLED: the Krein/kinematic structure (exact); the
  commutation's radiative stability (Part A/B); tree-level positivity (BT). CONTESTED
  everywhere, GU included: loop-level positivity for 4-derivative gravity.

### Q4 -- The verdict

**OPEN.** Not SURVIVES: naming SURVIVES would require exhibiting loop-level *positivity*,
not just the commutation, and Part C shows the two come apart -- `[P, S] = 0` can hold
exactly while the positivity guarantee (weak ghost symmetry) is broken by an IR regulator.
Not BROKEN: naming BROKEN would require a symmetry violation, which Part A/B exclude at
residual `0`. The honest register is OPEN, with the obstruction named exactly.

---

## The pin (Part C): why radiative stability of `[P,S]=0` is necessary but not sufficient

The operative loop obstruction is **not** `[P, S] != 0` (that is protected). It is
**loop-level positivity**: BT's positive Born rule `Prob(A) = tr(B^dag kappa B kappa) >= 0`
requires every physical observable to be **weakly ghost symmetric** (`A = B + C`, `B`
ghost-symmetric, `C` null with `tr(C^dag C) = 0`). The demonstration
(`H26_loop_ghost_unitarity.py`, Part C) on the hyperbolic `(generation, mirror)` pair:

- **Tree level:** the pair is exactly null (`<u,u> = <v,v> = 0`, residual `2e-17`), so the
  physical observable's odd part `C = 0` and `tr(C^dag C) = 0` (C2/C3) -- positivity holds.
- **Loop / IR regulator `delta`:** modelling BT's stated collinear-divergence obstacle as a
  regulator that lifts the pair off exact nullness, `tr(C^dag C) ~ 2 delta^2 > 0` for every
  `delta > 0` **while `||[P, S]|| = 0` throughout** (C4/C5, swept table). The positivity
  margin degrades as `delta` grows, even though the symmetry is untouched.

**Reading.** The loop question lives in the **analytic** (null-structure / IR) layer, not
the symmetry layer. Weak ghost symmetry rests on *exact nullness* of the hyperbolic pairs;
collinear-IR regularization of the massless double-pole theory is exactly what can spoil
that nullness, and it is exactly what BT delegate to an unpublished companion. A protected
`[P, S] = 0` does not carry the null structure through the regulator -- that is a separate,
harder, unproven step.

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| `P` is an element of `O(9,5)` and `Sp(32,32;H)` (group element) | **COMPUTED** | A1, B2 residual `0.00e+00` |
| Cartan involution is an exact automorphism preserving `eta`, Killing form | **COMPUTED** | A3/A4/A6 residual `0` |
| every `so(9,5)`-covariant vertex (incl. `S=|theta|^2`) commutes with `P` | **COMPUTED** | A5 residual `0`; B3 residual `0` |
| commutation leg of `[P,S]=0` is radiatively stable | **COMPUTED + ARGUED** | group-realized symmetry -> effective action to all orders (QAP), anomaly caveat |
| BT prove positivity at tree level only; loops open (collinear IR) | **ARGUED (source-fenced)** | VG-SC intake of arXiv:2607.00096 |
| loop positivity != commutation (weak ghost symmetry can break at `[P,S]=0`) | **ARGUED (model-grounded)** | Part C `tr(C^dagC)~delta^2` while `[P,S]=0` |
| GU inherits the contested Stelle-Mannheim corner (attractive side) | **ARGUED** | H16 + R1 Jordan-boundary theorem |
| generation count / chiral selection | **untouched (OPEN elsewhere)** | sign-blindness fence, not addressed here |

---

## Honest limits

- **Part A/B are exact but algebraic.** They establish that `P` is a group element and an
  automorphism of the *covariant* structure. They do **not** by themselves construct GU's
  interacting field theory; "the effective action inherits a group-realized symmetry" is a
  standard field-theory argument (QAP / BRST), invoked, not re-derived here. Its one escape
  hatch -- a discrete `P`-anomaly -- routes to the open `C2`/count sector.
- **Part C is a model, not GU's loop calculation.** It demonstrates the *logical
  separation* (positivity can fail while commutation holds) and identifies the controlling
  quantity (exact nullness under IR regularization). It does **not** compute a GU loop
  integral -- there is none to compute without a built `S`.
- **The Q2 loop statements are primary-source-fenced, not independently recomputed.** They
  inherit the VG-SC intake; the to-appear companions [25]/[27] remain unaudited (announced,
  not available).
- **No count, no chirality.** This route asserts no generation number and manufactures no
  chiral selection; the sign-blindness of `[P,S]=0` (H23 C) is respected throughout.

---

## RE-RANK signal

**OPEN.**

**Single next object:** the **soldering-carrier source action `S`** -- a GU-internal
dynamics or constraint that forces `A = spin-lift(grad^gimmel)` (H23 D's unbuilt object).
It is the *same* object that gates the gravity soldering, `mu_DW`, and the fermion count,
and it is the **only** thing that would supply an S-matrix on which the loop-positivity /
collinear-IR resummation could actually be run. The loop-ghost-unitarity question is
therefore **not a missing calculation on existing machinery -- it is a missing object**.
Until `S` is built, `[P, S] = 0`'s commutation leg is provably radiatively stable, and its
positivity leg is provably undecidable from GU-internal data.

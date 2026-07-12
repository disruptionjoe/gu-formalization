---
artifact_type: exploration
status: exploration
created: 2026-07-11
hypothesis: H60
title: "H60 FIRM the asymptotic-freedom result from INDICATION to SOLID. Extends the H57 flow (Waves 44-46: GU is asymptotically FREE at one loop / 2 couplings, Gaussian UV fixed point, critical-surface dim 3, robust for c_RS_weyl > -13.3) by (1) ADDING the RS dimensionless couplings z_B (Bbar D^3 B kinetic norm) and y_RS (Bbar Sigma.R B curvature coupling) with their leading one-loop STRUCTURE and redoing the fixed-point search in the enlarged 4-coupling space (f_2^2, f_0^2, z_B, y_RS); (2) TIGHTENING c_RS_weyl by honest ker-Gamma dof counting; (3) RECOMPUTING the stability matrix / critical-surface dimension in the enlarged space; (4) a qualitative FRG note. RESULT: CONFIRMED-FIRMER. The enlarged one-loop system is HOMOGENEOUS-QUADRATIC (beta(lambda g)=lambda^2 beta(g)), a structural fact that FORBIDS any isolated non-Gaussian (interacting) fixed point for ANY value of the unknown ker-Gamma RS coefficients -- so adding z_B, y_RS cannot manufacture a Landau pole or a Reuter FP at this order; the Gaussian point stays the unique isolated UV fixed point. z_B is REDUNDANT (wavefunction norm, beta ∝ z_B, +0 free parameters); y_RS adds +0 (irrelevant/AF) or +1 (relevant) depending on an undetermined ker-Gamma loop sign, so the critical-surface dimension moves from 3 to 3..4 (marginal sector), 5..6 (full). c_RS_weyl tightened to the band [1.02, 1.82] (central ~1.32) -- the ker-Gamma projector removes the gamma-trace spin-1/2 modes and drops the SUSY gauge-fixing ghosts, a shift of at most 0.4 in b_2 units off the 17/12 anchor, keeping the AF margin above the -13.3 threshold at >14.3. f_2 AF is UNSPOILED by the RS marginal couplings (they do not feed beta_{f_2^2} at one loop). Positivity NOT settled (independent of the flow verdict). This is FIRMER (structural no-interacting-FP result, robust to RS ignorance, tightened c_RS_weyl) but NOT a proof (FRG / higher loops / true ker-Gamma coefficients remain)."
grade: "exploration / DERIVED-on-PORTED + STRUCTURAL. The firming lever (homogeneous-quadratic => no isolated non-Gaussian FP), the enlarged Gaussian-FP uniqueness, the vanishing 4x4 stability matrix, the z_B redundancy, the f_2-AF isolation, and the robustness-to-unknown-coefficients sweep are DERIVED / STRUCTURAL facts of the assembled one-loop system (they hold for ANY value of the RS beta coefficients). The gravitational coefficients (133/10, 5/3, 5, 5/6) inherit Stage 1's KNOWN/PORTED grade. c_RS_weyl is now ESTIMATED-TIGHTER (band [1.02,1.82] from ker-Gamma dof counting via the KNOWN /180 c-charge rule; exact value still needs a ker-Gamma heat-kernel). The RS marginal-coupling beta coefficients (c_yy, c_src, c_zf, ...) are GUESS-grade TEMPLATES -- the asserted conclusions are exactly the ones INDEPENDENT of them. Deterministic test tests/W47_H60_firm_af.py, 17/17 checks, exit 0; W45 (12/12) and W46 (19/19) still exit 0. Truncation: 4 couplings, one loop -- a FIRMER indication, not a proof. NO positivity/unitarity claim (out of scope; explicitly independent). No forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed, inserted, hardcoded, or divided by; no generation count touched."
depends_on:
  - explorations/H57-flow-stage1-theory-space-betas-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W46_H57_stage2_fixed_point.py
  - tests/W47_H60_firm_af.py
scripts:
  - tests/W47_H60_firm_af.py
external_refs:
  - "Fradkin & Tseytlin, Renormalizable asymptotically free quantum theory of gravity, Nucl. Phys. B201, 469 (1982)"
  - "Avramidi & Barvinsky, Asymptotic freedom in higher-derivative quantum gravity, Phys. Lett. B159, 269 (1985)"
  - "Salvio & Strumia, Agravity, JHEP 06 (2014) 080, arXiv:1403.4226; Agravity up to infinite energy, EPJ C78 (2018) 124, arXiv:1705.03896"
  - "Christensen & Duff, Axial and conformal anomalies for arbitrary spin, Phys. Lett. B76, 571 (1978); Duff, Twenty years of the Weyl anomaly, CQG 11, 1387 (1994)"
  - "Codello & Percacci, Fixed points of higher-derivative gravity, PRL 97 (2006) 221301; Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984"
  - "Niedermaier, Gravitational fixed points from perturbation theory, PRL 103 (2009) 101303 -- Weyl coupling AF alongside the Reuter fixed point"
---

# H60 -- FIRM the asymptotic-freedom result (INDICATION -> SOLID within the truncation)

## What H57 left, and what H60 does

**H57 (Waves 44-46)** established, at one loop in a 2-coupling truncation `(f_2^2, f_0^2)`, that GU's
induced 4th-order (Stelle/agravity) gravity flows to the **Gaussian UV fixed point** -- asymptotic
**FREEDOM**, not safety; critical-surface dimension **3** in the KNOWN gravitational sector
`{M_Pl(=mu_DW), Lambda, f_0^2}` with `f_2^2` predicted by AF; AF **robust for `c_RS_weyl > -13.3`**.
That is an **INDICATION** (2 couplings, one loop, ported betas), explicitly not a proof.

**H60 (this work)** tests whether AF *survives a bigger truncation*. Four firming moves; I did all four
(Move 4 qualitative only, as required):

| Move | Done? | Result |
|---|---|---|
| **1** ADD RS dimensionless couplings `z_B`, `y_RS`; redo the fixed-point search in `(f_2^2,f_0^2,z_B,y_RS)` | YES | Gaussian point stays the **unique isolated** UV FP; **no** non-Gaussian FP appears |
| **2** TIGHTEN `c_RS_weyl` by honest ker-Gamma dof counting | YES | band **`[1.02, 1.82]`** (central ~`1.32`); AF margin stays `>14.3` |
| **3** STABILITY / critical exponents in the enlarged space; recount relevant directions | YES | 4x4 stability matrix still **zero** (all marginal); critical-surface dim **3->3..4** (marginal), **5..6** (full) |
| **4** qualitative FRG/Reuter note (NO faked FRG) | YES | FRG can add a Reuter FP (breaks homogeneity); `f_2` AF expected to persist -> mixed safety+freedom |

**VERDICT: CONFIRMED-FIRMER** (truncation-bounded; not a proof). The AF result did **not** weaken or
overturn under the enlarged truncation. The classic worry -- adding matter couplings destroys AF (Landau
pole) or introduces an interacting FP with more relevant directions -- **did not materialize** at this
order, and I can now say *why structurally*, not just numerically.

## Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md) -- named, with the side used

| Fork | Standard-field default | GU program-native | USED HERE + why |
|---|---|---|---|
| **Gravity action** | freely chosen `R^2`/Weyl^2 | INDUCED `\|II\|^2` -> 4th-order Stelle `(f_2,f_0)` (H49) | **Stelle/agravity truncation**, now enlarged by the RS marginal couplings. The enlarged fixed-point search lives on this side. |
| **RS sector** | massive-RS constraint-solved, naive gravitino dof; Porrati-Rahman vertex | `ker Gamma`-projected spin-3/2, background-independent, degree-0 KINEMATIC projector, gamma-traceless (H58) | **`ker Gamma` program-native**, used for BOTH (a) the `c_RS_weyl` dof counting (Move 2: the projector removes the gamma-trace spin-1/2 and needs no SUSY ghosts) and (b) the identification of `z_B`, `y_RS` as the RS marginal couplings (Move 1). Their exact beta coefficients need a ker-Gamma heat-kernel; treated as GUESS templates -- the asserted conclusions are the ones independent of them. |
| **unitarity/positivity** | positive Hilbert space | Krein-graded `[P,S]=0` | **NEITHER -- OUT OF SCOPE.** A fixed point is an RG statement about the *flow of couplings*, INDEPENDENT of positivity. Enlarging the truncation firms the flow verdict and does not touch positivity. Stated, not settled. |
| **`mu_DW`** | a mass to be measured | DeWitt/gimmel ratio-only free scale (H24) | **ratio-only** -> realized as the Einstein/Newton transmutation scale `M_Pl`, one of the counted relevant directions. |

## The firming lever: the one-loop system is HOMOGENEOUS-QUADRATIC

The single most important structural fact, and the reason the verdict is robust to everything we do
*not* know about the RS sector:

> At one loop, **every** beta of a marginal (dimensionless) coupling is a sum of monomials of degree
> **exactly 2** in the coupling variables `g = (f_2^2, f_0^2, z_B, y_RS)` -- there is no linear term
> (that is why the stability matrix vanishes at the Gaussian point). A homogeneous-quadratic vector
> field satisfies `beta(lambda g) = lambda^2 beta(g)`.

Consequence: **any nonzero zero `g*` of `beta` is not isolated** -- the whole ray `{lambda g*}` is a zero,
i.e. a fixed **RATIO** (an AF trajectory), never an isolated interacting fixed point. Therefore:

- Adding `z_B`, `y_RS` **cannot manufacture a non-Gaussian (interacting) fixed point** at this order.
- The only fixed points are the **Gaussian point** (the isolated one) plus possibly fixed-ratio rays
  (the AF trajectories, exactly like the `f_0^2/f_2^2` ratio found in H57 Stage 2).

Crucially, this holds for **ANY** value of the unknown ker-Gamma RS beta coefficients -- so the
`no-interacting-FP` conclusion does not depend on pinning the heat-kernel. The test verifies homogeneity
numerically (`max|beta(lam g) - lam^2 beta(g)| ~ 4e-16`) and confirms it across 30 sign/magnitude
combinations of the unknown coefficients (all keep the Gaussian FP, homogeneity, vanishing stability
matrix, `z_B` redundancy, and `f_2` AF).

## Move 1 -- the enlarged 4-coupling beta system

`g = (x, y, z_B, y_RS) = (f_2^2, f_0^2, z_B, y_RS)`, `t = ln mu`, `kappa = 1/(4pi)^2`:

```
beta_x    = -kappa x^2 b_2                                       # KNOWN + tightened c_RS_weyl
beta_y    =  kappa[ (5/3)x^2 + 5 x y + (5/6 + d_RS_R2) y^2 ]     # KNOWN + GUESS d_RS_R2
beta_zB   =  kappa * z_B * ( c_zz z_B + c_zf x + c_zy y_RS )     # GUESS template; note the overall z_B
beta_yR   =  kappa[ c_yy y_RS^2 + c_yf2 y_RS x + c_yf0 y_RS y + c_src x^2 ]   # GUESS template
```

Grading: `beta_x`, `beta_y` are the Stage-1 KNOWN/ported gravitational betas (reused, not re-derived).
The RS betas `beta_zB`, `beta_yR` are structurally honest **templates** at **GUESS** grade -- every term
is a degree-2 monomial (as required at one loop), but the numerical coefficients need a real ker-Gamma
heat-kernel. The conclusions below are exactly the ones that survive independent of those numbers.

**Two structural features that ARE determined (not guesses):**

- **`beta_zB` carries an overall factor of `z_B`** -> `z_B = 0` is an invariant subspace -> `z_B` is a
  **REDUNDANT** (multiplicatively-renormalized / wavefunction-normalization) coupling, removable by a
  field rescaling. A redundant coupling is **not** a physical relevant direction: it adds **+0** free
  parameters. (This is forced by `z_B` being a kinetic *norm*, not a physical interaction.)
- **`beta_x` does not depend on `z_B` or `y_RS`** -> `f_2` asymptotic freedom is UNSPOILED by the RS
  marginal couplings at one loop. RS matter enters the graviton (`f_2`) beta **only** through the trace
  anomaly `c_RS_weyl` (Move 2), which is a large positive number; the marginal RS couplings do not feed
  `beta_{f_2^2}` at this order, so they cannot turn AF into a Landau pole.

**Fixed-point search result.** The Gaussian point `(0,0,0,0)` is a fixed point (all four betas vanish).
By the homogeneity lever there is no isolated non-Gaussian fixed point; a 60-seed multistart Newton in
4D confirms every convergent root clusters at the origin within the degenerate-zero floor (no second
cluster). **No non-Gaussian FP appeared that the 2-coupling system could not see.**

## Move 2 -- tightening `c_RS_weyl` by honest ker-Gamma dof counting

Stage 1 anchored `c_RS_weyl = 255/180 = 17/12 = 1.4167` at the **standard massless spin-3/2 (gravitino)**
Christensen-Duff Weyl^2 trace-anomaly coefficient `255` (units `1/(360(4pi)^2)`), but left it a **named
parameter** because the ker-Gamma projection changes the effective propagating dof.

The honest dof counting (fork 2). The `ker Gamma` projector is a **kinematic, degree-0,
background-independent** projector onto the transverse, **gamma-traceless** spin-3/2 content. Relative to
the standard gauge-fixed gravitino it differs by:

1. **It removes the gamma-trace spin-1/2 modes.** The standard vector-spinor `psi_mu` decomposes as
   spin-3/2 **plus** a spin-1/2 gamma-trace `gamma^mu psi_mu`; ker-Gamma keeps only the gamma-traceless
   part, so it removes one spin-1/2's worth of positive `c`-charge.
2. **It needs no SUSY gauge-fixing ghosts.** The Faddeev-Popov + Nielsen-Kallosh spin-1/2 ghosts of the
   standard gravitino quantization are an artifact of gauge-fixing a *dynamical* gauge symmetry; a
   kinematic projector introduces none.

Both corrections are at the level of a **handful of spin-1/2 (Weyl/Dirac) modes**. Using the KNOWN
`/180` c-charge rule (reused from Stage 1): per spin-1/2 mode the `b_2` shift is
`9/180 = 0.05` (Weyl/Majorana) to `18/180 = 0.10` (Dirac). Bounding the net ker-Gamma-vs-gravitino
difference by up to **4 Dirac spin-1/2 modes** (one gamma-trace + up to three ghosts):

```
|Delta c_RS_weyl|  <=  4 x 0.10  =  0.40   (in b_2 units)
```

- **Central tightened estimate** (keep the `255` transverse core, subtract one gamma-trace spin-1/2):
  `(255 - 9..18)/180 = 1.37 .. 1.32`.
- **Conservative dof-counting band:** `c_RS_weyl in [1.02, 1.82]` (`= 17/12 +/- 0.40`).

**Re-check of the AF window.** AF needs `b_2 = 133/10 + c_RS_weyl > 0`, i.e. `c_RS_weyl > -13.3`. Across
the **entire** tightened band `b_2 in [14.32, 15.12] > 0`; the worst-case margin above the sign-flip is
**14.32** (anchor margin was 14.72). To reach `-13.3` you would have to remove ~147 Dirac spin-1/2
modes' worth of positive `c`-charge -- absurd. **So the dof counting TIGHTENS `c_RS_weyl` to a narrow
positive band and makes AF FIRMER, not weaker.** The only escape remains a large **negative-norm Krein**
contribution to the trace anomaly -- the out-of-scope positivity fork.

(`c_RS_weyl` is now **ESTIMATED-TIGHTER**: the band is dof-counted, but the exact value still needs a
ker-Gamma heat-kernel. This is honest tightening, not pinning.)

## Move 3 -- stability / critical exponents and the recounted critical surface

The 4x4 stability matrix `M_ij = d beta_i/d g_j` at the Gaussian FP is the **zero matrix** (no linear
term; all four couplings marginal, `theta = 0` at linear order). Relevance is decided at the nonlinear
(logarithmic) level, per coupling:

| Coupling | Nonlinear relevance | Free parameter? |
|---|---|---|
| `f_2^2` | marginally IRRELEVANT (`beta_x < 0`, AF) | **no** -- PREDICTED (fixed to 0) |
| `f_0^2` | marginally RELEVANT (conformal mode) | yes (+1) |
| `z_B` | REDUNDANT (`beta_zB ∝ z_B`, wavefunction) | **no** (+0) |
| `y_RS` | SIGN-CONDITIONAL: `c_yy>0` relevant / `c_yy<0` irrelevant | **+0 or +1** (undetermined) |

**Recounted critical-surface dimension (= number of free parameters):**

- **KNOWN gravitational sector: 3** `{M_Pl(=mu_DW), Lambda, f_0^2}` -- **UNCHANGED** from Stage 2;
  `f_2^2` still predicted by AF.
- **Adding the RS dimensionless couplings:** `z_B` gives **+0** (redundant); `y_RS` gives **+0 or +1**
  (undetermined ker-Gamma loop sign). So the enlarged **marginal-sector** critical-surface dimension is
  **3 .. 4** -- it did not blow up; it grows by at most one.
- **Full truncation: 5 .. 6**, adding the RS dimensionful `{m_RS, g4f}` (GUESS grade).

The RS dimensionless couplings therefore did **not** make GU dramatically less predictive: at worst one
extra free parameter (`y_RS`, if its self-coupling turns out positive), and `f_2^2` remains the one
genuine predictivity gain from AF.

## Move 4 -- FRG/Reuter qualitative note (NOT computed)

A genuine FRG (Reuter-type) truncation keeps the **full nonperturbative running** of the dimensionful
Einstein-Hilbert couplings (`g~ = G k^2`, `lambda~ = Lambda/k^2`). In Reuter-dimensionless form these
carry their **canonical scaling as LINEAR terms** in the betas -> the system is **no longer
homogeneous-quadratic**, so the firming lever (E2) no longer forbids an interacting fixed point: an FRG
**Reuter fixed point** (non-Gaussian, finite number of relevant directions) generically appears in the
EH sector. Published FRG of higher-derivative gravity (Codello-Percacci 2006; Benedetti-Machado-
Saueressig 2009; Niedermaier 2009) finds the **higher-derivative (Weyl / `f_2`) coupling remains
asymptotically free even alongside that Reuter FP**. So the perturbative `f_2` AF verdict is **likely
stable** under FRG, with the UV picture becoming the **mixed scenario** (asymptotic safety in the EH
sector + asymptotic freedom in the higher-derivative sector). This is a qualitative expectation; **no
FRG computation was performed here** (per the brief -- do not fake an FRG computation).

## Adversarial honesty -- what is firmer, what is still fragile

**Firmer (the gains):**
- The `no-interacting-FP` result is now **STRUCTURAL** (homogeneity), not just a numerical multistart
  search -- and it is **robust to the ker-Gamma ignorance** (holds for any RS coefficients).
- `c_RS_weyl` is **tightened** from an unpinned anchor to a narrow positive band `[1.02, 1.82]`; the AF
  margin (>14.3) does not approach the `-13.3` threshold.
- The enlarged critical-surface dimension is **essentially preserved** (3 -> 3..4); `z_B` redundant,
  `y_RS` at most +1.
- `f_2` AF is **provably isolated** from the RS marginal couplings at one loop.

**Still fragile (the honest limits):**
- **This is one loop / homogeneous-quadratic.** The `no-interacting-FP` conclusion is an artifact of the
  perturbative truncation; FRG (linear canonical terms) can add a Reuter FP -- not excluded, only
  expected to leave `f_2` AF intact.
- **The `y_RS` self-coupling sign is undetermined** (needs the ker-Gamma heat-kernel): if positive,
  `y_RS` is marginally relevant and adds one free parameter. AF is unaffected either way.
- **The RS beta coefficients are GUESS templates.** The structural conclusions are the ones independent
  of them, but the exact fixed-ratio trajectories in the `y_RS` direction depend on the true values.
- **Positivity is not touched.** A UV fixed point is a statement about the flow; Krein `[P,S]=0`
  loop-positivity is independent and remains the binding question for UV *completeness*.

## Does NOT settle positivity (explicit caveat)

A UV fixed point (asymptotic freedom) is a statement about the **RG flow of couplings**. It is
**independent** of the Krein `[P,S]=0` loop-positivity question, which is **not settled here** and is
untouched by enlarging the truncation. The single place the two conditions meet remains the sign of the
wrong-sign conformal / RS fixed ratio (H57 Stage 2), and it is left OPEN. Do not over-read the firmer AF
result as a unitarity result.

## What this leaves for H59

- **The true ker-Gamma heat-kernel** on the `Spin(9,5)`-equivariant subspace: pins the exact
  `c_RS_weyl` (inside the tightened band `[1.02, 1.82]`) AND the RS marginal-coupling beta coefficients
  (`c_yy` sign -> whether `y_RS` is a free parameter; `d_RS_R2`; the `z_B` anomalous dimension). This is
  the one computation that would upgrade the RS pieces from ESTIMATED/GUESS to KNOWN.
- **An FRG/Reuter truncation** of GU's induced action: would test whether the mixed safety+freedom
  picture actually holds and whether `f_2` AF persists nonperturbatively.
- **The positivity/Krein frontier** (the wrong-sign ratio's admissibility) remains the binding question
  for genuine UV completeness -- independent of, and untouched by, this firming.

---

*Reproducible: `python tests/W47_H60_firm_af.py` (17/17 PASS, exit 0); imports Stage 1's `BetaSystem`,
`THEORY_SPACE`, `KAPPA`, and the `/180` anomaly rule (does not re-derive). W45 (12/12) and W46 (19/19)
still exit 0. Exploration-grade; not promoted to canon. No git commit (orchestrator verifies+commits).
No canon/verdict/claim-status file touched.*

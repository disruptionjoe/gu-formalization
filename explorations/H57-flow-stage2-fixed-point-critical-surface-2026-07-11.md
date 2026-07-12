---
artifact_type: exploration
status: exploration
created: 2026-07-11
hypothesis: H57
title: "H57 asymptotic safety, STAGE 2 of 2 -- fixed point + critical surface for the GU UV flow. Consumes Stage 1's assembled beta system (imports tests/W45_H57_stage1_beta_system.py: BetaSystem, THEORY_SPACE) and SETTLES the fixed-point / predictivity questions. RESULT: the GAUSSIAN point (f_2^2,f_0^2)=(0,0) is the UNIQUE UV fixed point; there is NO non-Gaussian (interacting) fixed point at one loop in this 2-coupling truncation. GU's second UV route is therefore asymptotic FREEDOM (Gaussian UV FP), NOT asymptotic SAFETY. The stability matrix at the Gaussian FP VANISHES (both curvature-squared couplings are marginal, linear critical exponents theta=0); at the nonlinear level f_2^2 is marginally IRRELEVANT (asymptotically free -> predicted) and f_0^2 is marginally RELEVANT (the conformal mode). CRITICAL-SURFACE DIMENSION = number of free parameters = 3 in the KNOWN gravitational sector {M_Pl (= the ratio-only free scale mu_DW, via Newton/Einstein transmutation), Lambda (cosmological constant), f_0^2 (conformal mode)}, with f_2^2 PREDICTED by AF; up to 5 in the full truncation adding the RS-sector dimensionful {m_RS, g4f} (GUESS grade). The f_0 conformal-mode non-AF is resolved into a fixed RATIO f_0^2/f_2^2 -> both couplings -> 0 (total AF), but the fixed ratio is NEGATIVE (wrong-sign / conformal-factor direction), whose admissibility is exactly the OUT-OF-SCOPE positivity question. Robustness: AF survives for all c_RS_weyl > -13.3; the anchor +17/12 = +1.42 clears it by ~14.7. Krein loop-POSITIVITY is NOT settled and is INDEPENDENT of the AF/FP result."
grade: "exploration / DERIVED-on-PORTED. The fixed-point structure, vanishing stability matrix, marginal classification, fixed-ratio analysis, and c_RS_weyl robustness sweep are DERIVED (exactly / numerically) from Stage 1's PORTED agravity one-loop beta functions -- so the gravitational-sector conclusions inherit Stage 1's KNOWN grade for the pure-gravity coefficients (133/10, 5/3, 5, 5/6), ESTIMATED for the RS Weyl shift c_RS_weyl (anchor 17/12, ker-Gamma changes dof -> named parameter), and GUESS for the RS -> R^2 shift d_RS_R2 (anchor 0) and the RS dimensionful directions m_RS, g4f. Deterministic test tests/W46_H57_stage2_fixed_point.py, 19/19 checks, exit 0. Truncation: 2-4 couplings, one loop -- an INDICATION of the UV route, not a proof. NO positivity/unitarity claim (out of scope; explicitly flagged as independent). No forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed, inserted, hardcoded, or divided by; no generation count touched."
depends_on:
  - explorations/H57-flow-stage1-theory-space-betas-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W46_H57_stage2_fixed_point.py
scripts:
  - tests/W46_H57_stage2_fixed_point.py
external_refs:
  - "Fradkin & Tseytlin, Renormalizable asymptotically free quantum theory of gravity, Nucl. Phys. B201, 469 (1982)"
  - "Avramidi & Barvinsky, Asymptotic freedom in higher-derivative quantum gravity, Phys. Lett. B159, 269 (1985)"
  - "Salvio & Strumia, Agravity, JHEP 06 (2014) 080, arXiv:1403.4226"
  - "Salvio & Strumia, Agravity up to infinite energy, Eur. Phys. J. C78 (2018) 124, arXiv:1705.03896"
  - "Salvio, Quadratic Gravity, Front. Phys. 6 (2018) 77, arXiv:1804.09944"
  - "Gibbons, Hawking & Perry, Path integrals and the indefiniteness of the gravitational action, Nucl. Phys. B138, 141 (1978) -- the Euclidean conformal-mode wrong-sign feature"
  - "Codello, Percacci, Rahmede; Niedermaier; Reuter -- functional RG / asymptotic safety of higher-derivative gravity (the non-Gaussian Reuter FP the perturbative betas do not capture)"
---

# H57 asymptotic safety -- STAGE 2 of 2: fixed point + critical surface

## What this stage is (and is not)

The FLOW question (H57): **does GU flow to a UV fixed point, and how PREDICTIVE is that UV
completion** (dimension of the UV critical surface = number of free parameters)? This is the live
SECOND UV route now that power-counting renormalizability is confirmed (H58).

**Stage 1** assembled the ODE system `dg_i/dt = beta_i(g)` and PORTED the one-loop 4th-order-gravity
beta functions with citations. **Stage 2 (this document)** imports that system
(`tests/W45_H57_stage1_beta_system.py`: `BetaSystem`, `THEORY_SPACE`, `STAGE2_HANDOFF`) and SETTLES:
(Q1) the fixed point(s), (Q2) the critical-surface dimension, (Q3) robustness to the one uncertain
input, (Q4) the f_0 conformal-mode resolution, (Q5) the critical exponents. **The betas are reused,
not re-derived.**

**Out of scope (NOT settled here, stated explicitly):** Krein loop-POSITIVITY / `[P,S]=0` unitarity.
A UV fixed point in the couplings is a statement about the **RG flow of the couplings**; it is
**independent** of the positivity question. This flow result must not be over-read as a unitarity
result. See the caveat section -- the two conditions touch at exactly one place (the sign of the
f_0 fixed ratio) and that place is left OPEN.

## Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md) -- named, with the side used

Carried unchanged from Stage 1 (this stage adds no new object choice):

| Fork | Standard-field default | GU program-native | USED HERE + why |
|---|---|---|---|
| **Gravity action** | freely chosen `R^2`/Weyl^2 | INDUCED `\|II\|^2` -> 4th-order Stelle `(f_2,f_0)` (H49) | **Stelle/agravity `(f_2^2,f_0^2)` truncation.** The fixed-point search lives on this side; it IS GU's spin-2 + conformal-mode sector. The ported betas apply because GU's induced action is in the same derivative class. |
| **RS sector** | massive-RS constraint-solved, naive dof | `ker Gamma`-projected spin-3/2, background-independent (H58) | **`ker Gamma`.** The RS Weyl-beta shift `c_RS_weyl` is a **named parameter** (anchor `17/12`), SWEPT here for robustness (Q3). |
| **unitarity/positivity** | positive Hilbert space | Krein-graded `[P,S]=0` | **NEITHER -- out of scope.** The one place it touches this flow is the SIGN of the `f_0^2/f_2^2` fixed ratio; flagged, left open. |
| **`mu_DW`** | a mass to be measured | DeWitt/gimmel ratio-only free scale (H24) | **ratio-only.** Realized here as the Einstein/Newton transmutation scale `M_Pl` -- and it turns out to be **one of the counted relevant directions** (a free parameter), which is exactly the H24 "structurally free scale". |

## Q1 -- The fixed point(s): GAUSSIAN, and it is UNIQUE

Write `x = f_2^2`, `y = f_0^2`, `kappa = 1/(4pi)^2`, at the RS anchor (`c_RS_weyl = 17/12`,
`d_RS_R2 = 0`, so `b_2 = 133/10 + 17/12 = 14.7167`):

```
beta_x = -kappa x^2 b_2                              (b_2 > 0)
beta_y =  kappa[ (5/3) x^2 + 5 x y + (5/6) y^2 ]
```

**Fixed-point analysis (exact).**
- `beta_x = 0`  <=>  `x^2 = 0`  <=>  `x = 0` (because `b_2 != 0`). The Weyl coupling has a **double**
  zero only at the origin -- there is no `x != 0` root.
- On the line `x = 0`, `beta_y = kappa (5/6) y^2`, which vanishes **only** at `y = 0`.

**=> The GAUSSIAN point `(f_2^2, f_0^2) = (0, 0)` is the UNIQUE fixed point of the flow. There is NO
non-Gaussian (interacting) fixed point** at one loop in this 2-coupling truncation. A multistart
Newton search from 25 seeds spread over the `(x,y)` plane confirms it: every convergent root clusters
at the origin within the degenerate-zero precision floor (`~1e-5`; the FP is a *quadratic* zero, so a
tiny residual does not pin the location tighter than `~sqrt(residual)`), with no second cluster.

**(a) Is the Gaussian point a genuine UV fixed point of the full flow?** Yes. All dimensionless
couplings' betas vanish there, and the dimensionful ones (in Reuter-dimensionless form
`g~ = G k^2`, `lambda~ = Lambda/k^2`) have the free Gaussian point as their canonical fixed point too
(loops shift it perturbatively but do not remove it). It is UV-attractive in the `f_2^2` direction
(next section).

**(c) Is there a non-Gaussian fixed point (true asymptotic safety)?** **Not in this truncation.** The
perturbative one-loop betas are purely quadratic and admit only the Gaussian root. *Honest caveat:*
functional-RG treatments (Reuter, Codello-Percacci-Rahmede, Niedermaier) DO find an interacting
("Reuter") fixed point for higher-derivative gravity once the Einstein-Hilbert couplings' full
nonperturbative running is kept -- that physics is **not** in the ported perturbative system used
here. So this stage establishes the asymptotic-**freedom** route; it does not exclude a separate
asymptotic-**safety** route that a nonperturbative truncation could exhibit. GU is compatible with
both UV pictures; **the beta system Stage 1 assembled realizes FREEDOM.**

## Q5 -- Stability matrix and critical exponents: the marginal sector

The one-loop betas have **no linear term** in the marginal couplings (they start at `O(g^2)`), so the
stability matrix at the Gaussian FP **vanishes identically**:

```
M_ij = d beta_i / d g_j  |_(0,0)  =  [[0, 0],
                                      [0, 0]]        eigenvalues (0, 0),  theta = -eig = (0, 0)
```

Both `f_2^2` and `f_0^2` are **MARGINAL** (linear critical exponent `theta = 0`). Relevance is decided
at the **nonlinear (logarithmic) level**, by the sign of the quadratic beta along each axis:

- **`f_2^2` marginally IRRELEVANT.** `beta_x = -kappa x^2 b_2 < 0` for `x > 0`: the coupling flows
  *into* the fixed point as `t = ln mu -> +infinity` (UV). This is asymptotic freedom. A marginally
  irrelevant coupling is **PREDICTED** (fixed to 0 in the UV), NOT a free parameter -- it is traded
  for a single dimensional-transmutation scale.
- **`f_0^2` marginally RELEVANT.** At `x = 0`, `beta_y = kappa (5/6) y^2 > 0` for `y > 0`: the coupling
  flows *away* from the fixed point in the UV. This is the classic conformal-mode direction; it counts
  as one free (tuned) parameter. Q4 shows how it is resolved.

## Q2 -- Critical-surface dimension = number of free parameters (the payoff)

At a Gaussian (free) UV fixed point, relevance is by **canonical scaling**: a parameter with positive
mass dimension multiplies a relevant (super-renormalizable) operator and must be fixed by measurement;
dimensionless couplings are marginal (split above). Reading the directions off `THEORY_SPACE`:

| Direction | Operator | Scaling | Relevant? | Physical meaning | Grade |
|---|---|---|---|---|---|
| `G` (Newton) | `R` (dim 2) | canonical relevant | **YES** | **`M_Pl` = the Einstein/Newton transmutation scale = the ratio-only free scale `mu_DW`** | KNOWN |
| `Lambda` | `1` (dim 0) | canonical relevant | **YES** | cosmological constant / vacuum energy | KNOWN |
| `f_0^2` | `R^2` (dim 4) | marginally relevant | **YES** | the conformal (spin-0) mode | KNOWN |
| `f_2^2` | `C^2` (dim 4) | marginally IRRELEVANT | **no (predicted)** | Weyl / spin-2 coupling -- fixed to 0 by AF | KNOWN |
| `b_GB` | Gauss-Bonnet | topological | spectator | total derivative in 4D | KNOWN |
| `m_RS` | `Bbar B` | canonical relevant | **YES** | RS mass (ker-Gamma sector) | GUESS |
| `g4f` | `(Bbar B)^2` | canonical relevant | **YES** | four-fermi (RS sector) | GUESS |
| `z_B`, `y_RS` | dim-4 RS | marginal | undetermined | RS marginal couplings; loop sign not pinned at this grade | ESTIMATED |

**HEADLINE COUNT.**
- **KNOWN gravitational sector: the UV critical surface has dimension 3** = **`{ M_Pl (= mu_DW), Lambda,
  f_0^2 }`**. These are the three free parameters GU's asymptotically-free UV completion carries in its
  pure-gravity sector. `f_2^2` is **not** among them -- asymptotic freedom PREDICTS it (fixed to 0),
  which is the one genuine gain in predictivity over generic higher-derivative gravity.
- **Full truncation: up to 5** = `{ M_Pl, Lambda, f_0^2, m_RS, g4f }`, adding the two RS-sector
  dimensionful directions at **GUESS** grade (`z_B`, `y_RS` marginal-relevance undetermined at this
  grade, so the count could move by their number if a real ker-Gamma heat-kernel pins their loop
  signs).

**The `mu_DW` connection (falsifiability keystone).** One of the relevant directions IS the free
overall scale `mu_DW` -- realized as the Newton/Einstein transmutation scale `M_Pl`. The H24 result
that GU's geometry fixes only dimensionless RATIOS and leaves the overall scale structurally free is
**exactly** a relevant direction in the UV critical surface. The AS/AF language and the H24 ratio-only
language are the same statement: `mu_DW` is a free parameter of the UV completion, not a prediction.

**Honest predictivity read.** This is NOT a hyper-predictive UV completion. The gravitational critical
surface (dimension 3) is essentially that of ordinary higher-derivative gravity **minus one** (the
`f_2^2` Weyl coupling, removed by asymptotic freedom). The Einstein scale, the cosmological constant,
and the conformal `f_0^2` remain free; the RS sector adds more. Asymptotic freedom buys **one**
prediction (`f_2 -> 0`), not a dramatic collapse of parameters.

## Q4 -- The f_0 conformal-mode non-AF: resolved into a (wrong-sign) fixed RATIO

Because `f_2 -> 0` in the UV, the physical UV variable is the **ratio** `r = f_0^2/f_2^2`. Its flow:

```
dr/dt = kappa * x * [ (5/6 + d_RS_R2) r^2 + (5 + b_2) r + 5/3 ]
```

A UV **fixed ratio** `r*` (bracket = 0) means `f_0^2 = r* f_2^2 -> 0` as `f_2^2 -> 0`: **TOTAL
asymptotic freedom** (both couplings vanish in the UV along that trajectory). At the anchor
(`d_RS_R2 = 0`, `b_2 = 14.7167`) the bracket `0.8333 r^2 + 19.7167 r + 1.6667 = 0` has discriminant
`383.2 > 0` and two **real** roots:

```
r* = -0.0848   and   r* = -23.575        (both NEGATIVE)
```

Both fixed ratios are **negative** -- necessarily so: the product of roots is
`(5/3)/(5/6) = 2 > 0` and the sum is `-(5+b_2)/(5/6) < 0`, so both roots share the sign that makes them
negative. A negative `f_0^2/f_2^2` means `f_0^2` and `f_2^2` have **opposite sign**: the UV-complete
trajectory sits on the **wrong-sign conformal-factor direction**. This is precisely the known
Euclidean conformal-mode feature (Gibbons-Hawking-Perry: the conformal factor has a wrong-sign kinetic
term in Euclidean gravity) -- the same subtlety that makes people call higher-derivative gravity
"subtle."

**So the resolution is honest and specific:** the `f_0` non-AF does NOT block a UV limit -- the flow
reaches a Gaussian UV fixed point along a fixed-ratio trajectory (total AF), and the ratio freezes as
`f_2^2 -> 0` (verified: `dr/dt ~ kappa x -> 0`, so `f_0^2` is *carried to zero*, not sent to a Landau
pole, ON the fixed-ratio direction). **BUT** the trajectory that does this sits at `f_0^2/f_2^2 < 0`.
Whether that sign is physically admissible -- i.e. whether the spin-0 mode is a healthy state or a
ghost -- is the **positivity / Krein question**, which is out of scope. This is the single point where
the flow result and the positivity frontier touch, and it is left open. (The Salvio-Strumia
alternative resolutions -- `f_0 -> infinity` conformal-gravity limit, or conformally-coupled scalars
`xi -> -1/6` -- are other routes that live on the same open sign question; we do not need them to
establish the AF *flow*, only to decide the *sign*'s acceptability.)

## Q3 -- Robustness of the AF verdict to `c_RS_weyl` (the one uncertain input)

`f_2` asymptotic freedom requires `b_2 = 133/10 + (matter) + c_RS_weyl > 0`. With no extra standard
matter:

```
AF holds  <=>  b_2 > 0  <=>  c_RS_weyl > -133/10 = -13.3
```

A 4001-point sweep of `c_RS_weyl in [-20, +20]` confirms the sign flip is at **exactly `-13.3`**
(matching Stage 1's flagged threshold), AF holding for every `c_RS_weyl > -13.3` and failing for
every `c_RS_weyl < -13.3`. The standard massless-spin-3/2 anchor is `+17/12 = +1.4167`, which clears
the threshold by a **margin of ~14.7**. To break AF the ker-Gamma carrier would have to contribute a
Weyl trace-anomaly coefficient near `-2394` (i.e. `-13.3 x 180`) -- an enormous NEGATIVE value, whose
only conceivable source is a large negative-norm **Krein-ghost** contribution to the trace anomaly:
the out-of-scope positivity fork again. **=> The AF verdict is ROBUST** to the one genuinely uncertain
input across its entire plausible range; only a dramatic Krein-ghost effect (a positivity-sector
statement) could overturn it.

## HONEST FRAMING -- freedom vs safety, and the limits

- **GU realizes asymptotic FREEDOM, not asymptotic SAFETY, in this truncation.** The UV fixed point is
  the **Gaussian** point (couplings `-> 0`), reached with `f_2^2` marginally irrelevant (AF) and the
  conformal `f_0^2` carried to zero along a fixed-ratio trajectory. There is **no non-Gaussian
  (interacting) fixed point** at one loop / 2 couplings, so this is not the Reuter asymptotic-safety
  scenario.
- **Truncation limits.** This is 2-4 couplings at one loop, using ported agravity/higher-derivative
  betas -- an **INDICATION of the UV route, not a proof**. Higher loops, the RS marginal couplings'
  true (ker-Gamma) contributions, and any nonperturbative (FRG) effects that could produce an
  interacting fixed point are not included. The gravitational-sector conclusions inherit Stage 1's
  KNOWN grade; the RS pieces are ESTIMATED/GUESS.
- **This does NOT settle positivity.** A UV fixed point in the couplings is a statement about the RG
  **flow**; it says nothing about Krein/loop positivity (`[P,S]=0`). The two are **independent** UV
  conditions. The AF/FP verdict stands on its own; the positivity frontier (including the sign of the
  `f_0^2/f_2^2` fixed ratio) remains the separate binding question for UV *completeness*. **Do not
  over-read the AF result as a unitarity result.**
- **No forbidden target touched.** No `{3, 8, 24, chi(K3)=24, Ahat=3}` assumed, inserted, hardcoded,
  or divided by; no generation count used. (The `-133/10` and `17/12` are the ported/anchored beta
  coefficients from Stage 1.)

## FLOW SUMMARY -- what H57 concludes, and what remains open

**H57 (does GU flow to a UV fixed point, and how predictive is it?) -- CONCLUDED for the second UV
route, at truncation grade:**

1. **UV fixed point: YES -- the GAUSSIAN point, uniquely.** GU's induced 4th-order (Stelle/agravity)
   sector flows to a free UV fixed point. This is asymptotic **FREEDOM**. No interacting fixed point
   appears at one loop, so this route is not asymptotic safety (a separate FRG route is not excluded).
2. **Predictivity / critical-surface dimension: 3 in the KNOWN gravitational sector**
   `{ M_Pl (= the ratio-only free scale mu_DW), Lambda, f_0^2 }`, with `f_2^2` **predicted** by
   asymptotic freedom (the one predictivity gain over generic higher-derivative gravity). Up to 5 in
   the full truncation once the RS dimensionful directions `{m_RS, g4f}` are added (GUESS grade).
3. **Robustness: strong.** The AF conclusion survives for all `c_RS_weyl > -13.3`; the physical anchor
   `+1.42` clears that by ~14.7. Only a large Krein-ghost (positivity-sector) effect could overturn it.
4. **The f_0 conformal mode: resolved as a fixed RATIO** giving total AF, but at `f_0^2/f_2^2 < 0`
   (the wrong-sign conformal-factor direction).

**What remains OPEN (the honest frontier):**
- **Positivity / Krein unitarity (`[P,S]=0`)** -- untouched here and INDEPENDENT of the AF result. It
  is the binding question for genuine UV *completeness*, and it is exactly where the negative fixed
  ratio's sign would have to be adjudicated.
- **A possible non-Gaussian (asymptotic-safety) fixed point** in a nonperturbative/FRG truncation --
  not excluded; a distinct UV picture GU could also admit.
- **The true ker-Gamma value of `c_RS_weyl`** (and the RS marginal couplings' loop signs) -- needs a
  real heat-kernel computation on the `ker Gamma` subspace; the AF verdict is robust to it, but the
  exact critical-surface dimension in the RS sector depends on it.

---

*Reproducible: `python tests/W46_H57_stage2_fixed_point.py` (19/19 PASS, exit 0). Imports Stage 1's
`BetaSystem` / `THEORY_SPACE` (does not re-derive). Exploration-grade; not promoted to canon. No git
commit (orchestrator verifies+commits). No canon/verdict/claim-status file touched.*

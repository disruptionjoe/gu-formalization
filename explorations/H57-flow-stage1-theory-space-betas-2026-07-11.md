---
artifact_type: exploration
status: exploration
created: 2026-07-11
hypothesis: H57
title: "H57 asymptotic safety, STAGE 1 of 2 -- theory space + beta-function structure for the GU UV flow. Sets up the running couplings (4th-order Stelle gravity f_2^2, f_0^2 + the ker-Gamma RS-sector couplings) with their mass dimensions, PORTS the known one-loop 4th-order-gravity beta functions (Fradkin-Tseytlin / Avramidi-Barvinsky / Salvio-Strumia agravity: the Weyl coupling f_2 is asymptotically FREE, b_2 = 133/10 > 0), adds the RS spin-3/2 matter shift (c_RS_weyl, anchored at the standard massless-gravitino Christensen-Duff value 255/180 = 17/12 but left a NAMED PARAMETER because the ker-Gamma projection changes the effective dof), and assembles the ODE system dg_i/dt = beta_i(g) as DATA for Stage 2. HEADLINE: the pure-gravity sector is asymptotically FREE (Gaussian UV fixed point), and the RS field at its standard anchor DEEPENS that AF; the open UV questions are the f_0 conformal-mode non-AF, the ker-Gamma value of c_RS_weyl, and the critical-surface dimension (predictivity). Loop positivity / Krein unitarity OUT OF SCOPE."
grade: "exploration / PORTED (pure-gravity one-loop beta functions are the published agravity/higher-derivative-gravity results, cited and reproduced) + ESTIMATED (RS matter shift anchored at the standard spin-3/2 Weyl-anomaly coefficient via a rule verified against agravity, but left a named parameter because the ker-Gamma projection changes the effective propagating dof) + GUESS (RS contribution to the R^2 beta, anchor 0). Deterministic module tests/W45_H57_stage1_beta_system.py, 12/12 checks, exit 0. No fixed point is SOLVED here (that is Stage 2); no positivity/unitarity claim (out of scope). No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3} assumed, inserted, hardcoded, or divided by; no generation count touched."
depends_on:
  - tests/W45_H57_stage1_beta_system.py
  - explorations/H58-rs-renormalizability-power-counting-2026-07-11.md
  - tests/W44_H58_rs_power_counting.py
  - explorations/wave42/renormalization-landscape-scan-2026-07-11.md
scripts:
  - tests/W45_H57_stage1_beta_system.py
external_refs:
  - "Fradkin & Tseytlin, Renormalizable asymptotically free quantum theory of gravity, Nucl. Phys. B201, 469 (1982)"
  - "Avramidi & Barvinsky, Asymptotic freedom in higher-derivative quantum gravity, Phys. Lett. B159, 269 (1985)"
  - "Salvio & Strumia, Agravity, JHEP 06 (2014) 080, arXiv:1403.4226"
  - "Salvio & Strumia, Agravity up to infinite energy, Eur. Phys. J. C78 (2018) 124, arXiv:1705.03896"
  - "Salvio, Quadratic Gravity, Front. Phys. 6 (2018) 77, arXiv:1804.09944"
  - "Christensen & Duff, Axial and conformal anomalies for arbitrary spin in gravity and supergravity, Phys. Lett. B76, 571 (1978); Duff, Twenty years of the Weyl anomaly, Class. Quant. Grav. 11, 1387 (1994)"
  - "Codello, Percacci, Rahmede; Niedermaier; Reuter -- asymptotic safety / functional RG of higher-derivative gravity"
  - "Eichhorn et al., asymptotic safety with fermions, arXiv:1601.04597, 1812.08782; AS of higher-derivative gravity + matter, arXiv:1703.09033"
---

# H57 asymptotic safety -- STAGE 1 of 2: theory space + beta-function structure

## What this stage is (and is not)

The FLOW question (H57): **does GU flow to a UV fixed point (asymptotic safety), and if so how
predictive is it** -- i.e. what is the dimension of the UV critical surface (= number of free
parameters)? This is the live SECOND UV route now that power-counting renormalizability is confirmed
(H58: GU is renormalizable, `D <= 4` on the `ker Gamma` subspace; the RS sector adds its OWN finite
closed counterterm set beyond pure Stelle).

**Stage 1 (this document)** does NOT search for the fixed point. It (i) defines the theory space /
truncation and enumerates the running couplings with their mass dimensions, (ii) PORTS the known
one-loop 4th-order-gravity beta functions with citations, (iii) adds the RS (spin-3/2) matter shift,
and (iv) assembles the ODE system `dg_i/dt = beta_i(g)` as machine-usable DATA. **Stage 2** takes the
assembled system (imports `tests/W45_H57_stage1_beta_system.py`), searches for the fixed point, and
computes the critical-surface dimension.

**Out of scope (do not settle here):** loop POSITIVITY / Krein `[P,S]=0` unitarity. AS is a statement
about the *flow of couplings*; it does not by itself require a positive-definite Hilbert space. The
ghost/positivity question is a separate frontier and is neither used nor decided.

## Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md) -- named, with the side used

| Fork | Standard-field default | GU program-native | USED HERE + why |
|---|---|---|---|
| **Gravity action** | freely chosen `R^2` / Weyl^2 Lagrangian | INDUCED `\|II\|^2` (Gauss identity) -> 4th-order Stelle `Weyl^2 + R^2` with an induced Einstein term (H49) | **Stelle/agravity two-coupling `(f_2, f_0)` truncation.** This IS GU's spin-2 + conformal-mode sector. The ported beta functions live on this side; the truncation is honest because GU's induced action is *in the same class* (4th-order derivative), so the class's flow applies. |
| **RS sector** | massive-RS constraint-SOLVED (`det(Gamma)^-1`, background-dependent), naive gravitino dof count | `ker Gamma`-projected spin-3/2, background-INDEPENDENT, degree-0 projector, gamma-traceless (H58) | **`ker Gamma` program-native.** Consequence: the RS contribution `c_RS_weyl` to the gravitational beta coefficients is a **named parameter**, anchored at the standard massless-spin-3/2 value but NOT pinned -- the ker-Gamma projection removes exactly the spin-1/2 modes (H58 Part B), so the propagating dof, hence the c-charge, is not the naive count. |
| **unitarity / positivity** | positive Hilbert space | Krein-graded `[P,S]=0` | **NEITHER -- out of scope.** Flagged only as the one place a *sign* of `c_RS_weyl` could flip (a negative-norm Krein mode can contribute to the trace anomaly with opposite sign); that is the positivity frontier, left untouched. |
| **`mu_DW`** | a mass parameter to be measured | the DeWitt/gimmel metric scale -- geometry fixes only DIMENSIONLESS RATIOS; the overall scale is structurally free (H24) | **ratio-only.** The dimensionful couplings (`G`, `Lambda`, RS masses) are measured in cutoff units; only the DIMENSIONLESS couplings run to a fixed point. This is exactly the AS split: marginal couplings hit the FP, dimensionful ones ride along. |

## 1. Theory space / truncation -- the running couplings

Honest truncation: the 4th-order gravity pair `(f_2^2, f_0^2)` plus the RS-sector operators H58's
counterterm enumeration showed are needed. Mass dimensions of each coupling; **dimensionless ones run
and can hit a fixed point**, dimensionful ones are measured in cutoff units (ride the flow as relevant
directions).

| Coupling | Symbol | Mass dim | Runs to FP? | Sector | Grade |
|---|---|---|---|---|---|
| Weyl-squared coupling | `f_2^2` (coeff of `C^2 ~ 1/2f_2^2`) | 0 | **YES** (marginal) | 4th-order gravity | KNOWN |
| R-squared coupling | `f_0^2` (coeff of `R^2 ~ 1/6f_0^2`) | 0 | **YES** (marginal) | 4th-order gravity | KNOWN |
| Gauss-Bonnet coeff | `b_GB` | 0 | YES but **spectator** (topological in 4D, total derivative; does not feed the others) | 4th-order gravity | KNOWN |
| Newton constant | `G` | -2 | no (dimensionful; `g~ = G k^2`) | Einstein-Hilbert (induced) | KNOWN |
| cosmological constant | `Lambda` | +2 | no (dimensionful; `lambda~ = Lambda/k^2`) | Einstein-Hilbert (induced) | KNOWN |
| RS 4th-order kinetic norm | `z_B` (coeff of `Bbar D^3 B`) | 0 | **YES** (marginal) | RS (ker-Gamma) | ESTIMATED |
| curvature-RS coupling | `y_RS` (coeff of `Bbar Sigma.R B`) | 0 | **YES** (marginal) | RS (ker-Gamma) | ESTIMATED |
| RS mass term | `m_RS` (coeff of `Bbar B`) | +3 | no (dimensionful) | RS (ker-Gamma) | GUESS |
| four-fermi | `g4f` (coeff of `(Bbar B)^2`) | +2 | no (dimensionful) | RS (ker-Gamma) | GUESS |

The RS operators are exactly H58 Part D's finite closed set (`Bbar D^k B` for `k<=3`, `(Bbar B)^2`,
`Bbar B R`, `Bbar Sigma.R B`), with `[B] = 1/2` (the 4th-order carrier normalization). The **marginal**
RS couplings `z_B`, `y_RS` are the ones that can participate in a UV fixed point; the RS mass/four-fermi
are relevant (dimensionful, `mu_DW`-set, ratio-only).

**The load-bearing pair for the fixed-point search is `(f_2^2, f_0^2)`** -- the pure-gravity marginal
couplings whose one-loop beta functions are known exactly. Stage 2 can start there and add the RS
marginal couplings as backreaction.

## 2. Ported one-loop 4th-order-gravity beta functions [KNOWN, cited]

`t = ln mu`, `kappa = 1/(4pi)^2`. Fourth-order (Stelle) gravity is one-loop renormalizable AND
**asymptotically free in the dimensionless higher-derivative couplings** (Fradkin-Tseytlin 1982;
Avramidi-Barvinsky 1985). The explicit agravity one-loop RGEs (Salvio-Strumia 2014, arXiv:1403.4226;
Salvio arXiv:1804.09944), with matter multiplicities `N_V` vectors, `N_f` Weyl fermions, `N_s` real
scalars:

```
(4pi)^2 df_2^2/dt = - f_2^4 ( 133/10 + N_V/5 + N_f/20 + N_s/60 )
(4pi)^2 df_0^2/dt =   (5/3) f_2^4 + 5 f_2^2 f_0^2 + (5/6) f_0^4 + (scalar matter via non-minimal xi)
```

Key ported facts (all reproduced/asserted in the test):

- **`f_2` (Weyl / spin-2) is ASYMPTOTICALLY FREE.** `b_2 = 133/10 > 0`, and *every* standard-matter
  contribution is the same (positive) sign, so `beta_{f_2^2} = -kappa f_2^4 b_2 < 0`: `f_2 -> 0`
  logarithmically in the UV. This is the strong prior: the pure-gravity part of GU very likely **IS
  asymptotically free**, not merely safe. The UV fixed point in `f_2` is the **Gaussian** point
  `f_2^2 = 0`.
- **`f_0` (R^2 / conformal mode) is NOT asymptotically free.** At `f_2^2 = 0`, `beta_{f_0^2} =
  kappa (5/6) f_0^4 > 0`, so `f_0^2` grows in the UV. Salvio-Strumia resolve this either by `f_0 ->
  infinity` (the conformal-gravity limit, where the conformal mode decouples) or by scalars becoming
  conformally coupled (`xi -> -1/6`). **This is the main open dynamical question for Stage 2** on the
  pure-gravity side.
- **The matter shift IS the conformal c-central charge.** The matter contribution to `b_2` equals the
  field's Weyl^2 trace-anomaly coefficient divided by 180 (in units of `1/(360(4pi)^2)`). Verified:
  scalar `3/180 = 1/60`, Weyl-fermion `9/180 = 1/20`, vector `36/180 = 1/5` -- exactly the agravity
  numbers (Christensen-Duff / Duff). This is what lets us PORT the RS shift from a known spin-3/2
  c-charge rather than invent it.

## 3. RS matter shift [ESTIMATED -- named parameter, anchored not pinned]

A spin-3/2 field shifts the gravitational beta coefficients. Using the verified rule
(shift `= (Weyl^2 anomaly coeff)/180`):

- The **standard massless spin-3/2 (gravitino)** Christensen-Duff Weyl^2 trace-anomaly coefficient is
  **255** (units `1/(360(4pi)^2)`; from `Theta_{3/2} = (1/360(4pi)^2)[255 W^2 - 22 E/4 + (61/2) R^2]`).
  So the standard-field anchor for the RS shift of `b_2` is `255/180 = 17/12 ~ 1.4167`.
- **Anchor is POSITIVE.** At this value the RS field *deepens* asymptotic freedom of `f_2`:
  `b_2 = 133/10 + 17/12 = 14.717 > 133/10 > 0`. So on the standard anchor, adding one RS field does
  **not** threaten `f_2` asymptotic freedom -- it strengthens it.

**Why it is left a NAMED PARAMETER `c_RS_weyl` (the honest caveat).** The 255 is the *standard massless
gravitino* count (a spin-3/2 gauge field minus its spin-1/2 ghosts, in a specific gauge). GU's RS
carrier is the **`ker Gamma`-projected, background-independent** object (fork 2): H58 computed that the
projector is gamma-traceless and removes exactly the spin-1/2 modes, so the effective propagating dof
-- and therefore the c-charge -- is **not** the naive massive-RS / gravitino number. Pinning the true
value needs a real heat-kernel computation on the `ker Gamma` subspace (with the `Spin(9,5)`-equivariant
projector), which is not done here. So `c_RS_weyl` is a **named parameter, anchor `17/12`**, and Stage 2
should treat it as the key RS unknown.

- **Robustness of AF (data for Stage 2).** `f_2` asymptotic freedom fails *only* if
  `c_RS_weyl < -133/10 ~ -13.3` -- a large NEGATIVE contribution. The only mechanism that could produce
  a negative c-contribution is the Krein/negative-norm grading (a ghost mode contributing to the trace
  anomaly with opposite sign) -- and that is the out-of-scope positivity fork. The standard anchor
  `+1.42` is nowhere near the `-13.3` threshold, so **the AF prior is robust** unless the ker-Gamma/Krein
  construction does something dramatic. Stage 2 should check this, but should expect AF to survive.

- **RS -> `f_0` (R^2) beta: `d_RS_R2`, GUESS, anchor 0.** The standard agravity `f_0` matter term is
  scalar-only (via the non-minimal `xi`); a pure fermion does not renormalize `R^2` at leading order.
  The ker-Gamma RS's non-minimal `Bbar Sigma.R B` coupling (`y_RS`) *could* contribute, but that
  coefficient needs the ker-Gamma heat-kernel. Anchor `0`; named parameter `d_RS_R2` for Stage 2.

## 4. The assembled ODE system [KNOWN + ESTIMATED + GUESS, graded]

`t = ln mu`, `kappa = 1/(4pi)^2`, `g = (f_2^2, f_0^2)`. Encoded as callables in
`tests/W45_H57_stage1_beta_system.py` (class `BetaSystem`, method `.beta(g)`):

```
(4pi)^2 df_2^2/dt = - f_2^4 * b_2,                          b_2 = 133/10 + N_V/5 + N_f/20 + N_s/60 + c_RS_weyl
(4pi)^2 df_0^2/dt =   (5/3) f_2^4 + 5 f_2^2 f_0^2 + (5/6) f_0^4 + d_RS_R2 * f_0^4
```

Grading of every coefficient:

| Coefficient | Value | Grade |
|---|---|---|
| Weyl pure-gravity `b_2` | `133/10` | **KNOWN** (Fradkin-Tseytlin, Avramidi-Barvinsky, Salvio-Strumia) |
| standard-matter shifts | `N_V/5, N_f/20, N_s/60` | **KNOWN** (agravity; = c-charge/180) |
| `f_0` from `f_2^4` | `5/3` | **KNOWN** (agravity) |
| `f_0` mixed `f_2^2 f_0^2` | `5` | **KNOWN** (agravity) |
| `f_0` self `f_0^4` | `5/6` | **KNOWN** (agravity) |
| RS Weyl shift `c_RS_weyl` | anchor `17/12` | **ESTIMATED** (std spin-3/2 anchor; ker-Gamma changes dof -> named parameter) |
| RS R^2 shift `d_RS_R2` | anchor `0` | **GUESS** (fermion doesn't renormalize R^2 at leading order; needs ker-Gamma heat-kernel) |

Structural facts the test asserts: the Gaussian point `(0,0)` is a fixed point of this system (the
AF UV FP candidate); `f_2` is AF at and near the anchor; `f_0` is not AF; `beta(g)` returns finite
callable data off the FP; `d_RS_R2` is a live knob.

## HANDOFF TO STAGE 2

**Running (dimensionless) couplings** (the fixed-point search variables):
`f_2^2`, `f_0^2` (the load-bearing pure-gravity pair), plus the RS marginal `z_B`, `y_RS`;
`b_GB` is a topological spectator. Dimensionful/relevant directions carried along: `G`, `Lambda`,
`m_RS`, `g4f` (measured in cutoff units; ratio-only, `mu_DW`).

**Beta-function coefficients** (import `BetaSystem` from `tests/W45_H57_stage1_beta_system.py`;
`STAGE2_HANDOFF` dict is provided there):

```
(4pi)^2 df_2^2/dt = - f_2^4 ( 133/10 + N_V/5 + N_f/20 + N_s/60 + c_RS_weyl )   # c_RS_weyl anchor 17/12
(4pi)^2 df_0^2/dt =   (5/3) f_2^4 + 5 f_2^2 f_0^2 + (5/6) f_0^4 + d_RS_R2 f_0^4  # d_RS_R2 anchor 0
```

**Named parameters for Stage 2 to vary:** `c_RS_weyl` (ESTIMATED, anchor `17/12`; the ker-Gamma
c-charge is the key RS unknown), `d_RS_R2` (GUESS, anchor `0`).

**Specific questions Stage 2 must answer:**
1. **Q1 -- does a UV fixed point exist?** The Gaussian point `(0,0)` is an asymptotically-free UV FP;
   is there a *nontrivial* interacting fixed point too (the Reuter-type branch), and which one governs
   GU's flow?
2. **Q2 -- critical-surface dimension = # free parameters (predictivity).** Linearize `beta` at the FP,
   get the stability matrix, count UV-relevant directions (negative critical exponents / eigenvalues).
   This is the headline number: how predictive is GU's UV completion?
3. **Q3 -- is `f_2` AF robust to the ker-Gamma/Krein RS construction?** Does `c_RS_weyl` stay above the
   `-133/10` sign-flip threshold? (Standard anchor says yes by a wide margin; the only risk is a large
   negative Krein-ghost contribution -- the out-of-scope positivity fork.)
4. **Q4 -- how is the `f_0` conformal-mode non-AF resolved?** `f_0 -> infinity` (conformal-gravity
   limit) / `xi -> -1/6` / RS `y_RS` backreaction. This decides whether the pure-gravity UV limit is
   asymptotic *freedom* (Gaussian) or requires a nontrivial `f_0`.
5. **Q5 -- critical exponents.** Diagonalize the linearized flow at the FP -> `theta_i` -> the
   universality data.

## Honest limits

- **This stage ports, it does not compute a GU loop integral.** The pure-gravity beta functions are the
  published higher-derivative/agravity results, applied to GU's induced 4th-order action on the honest
  grounds that GU's `|II|^2`-induced gravity is *in that derivative class*. No GU-specific graviton loop
  was run.
- **The RS shift is anchored, not derived on the ker-Gamma subspace.** `c_RS_weyl = 17/12` is the
  standard massless-gravitino value; the true GU number needs a `ker Gamma` heat-kernel. It is a named
  parameter precisely so no invented number enters Stage 2.
- **`d_RS_R2` is a genuine guess (anchor 0).** The RS contribution to the `R^2` beta is not pinned.
- **Positivity/unitarity is out of scope.** AS/AF here is about the flow of couplings; the Krein
  `[P,S]=0` ghost question is untouched and remains the binding obstruction to UV-*completeness* even if
  a fixed point exists.
- **No forbidden target touched.** The integer `3` appears only as `D-1` in the ported spin-3/2 anomaly
  algebra, never as a count; no `{3, 8, 24, chi(K3)=24, Ahat=3}` is assumed, inserted, hardcoded, or
  divided by; no generation count is used.

---

*Reproducible: `python tests/W45_H57_stage1_beta_system.py` (12/12 PASS, exit 0). Exploration-grade;
not promoted to canon. No git commit (orchestrator verifies+commits). No canon/verdict file touched.
Stage 2 consumes this to search for the fixed point and count the critical-surface dimension.*

---
artifact_type: exploration
status: exploration (5-persona inline team; STAGE 1 of 2 of the full combined FRG computation; deterministic test)
created: 2026-07-13
hypothesis: "STAGE 1 -- do the genuine FRG setup + the native ker-Gamma spin-3/2 heat-kernel + REGULATOR FAMILY 1 (Litim/optimized), and COMPUTE (not port) the ker-Gamma spin-3/2 (and leading graviton) contribution to beta_{f_2^2} to read off whether f_2^2* is lifted off zero at regulator 1 -- the HORN-K-vs-HORN-Q decider W87 named as the open deciding computation."
branch: "W88 -- Stage 1 of the full FRG f(R)+Weyl^2 + ker-Gamma spin-3/2 computation. Truncation setup (York/TT on sphere/dS; spin-2 TT / spin-1 / spin-0 blocks + Weyl 4th-derivative block); native transverse gamma-traceless spin-3/2 heat-kernel a_2 = (7/20)W^2 + (31/120)E_4; regulator family 1 = Litim/optimized threshold functions Phi^p_n(0)=1/n!; the full FRG beta_{f_2^2} STRUCTURE with the graviton-dressing term eta_C; the regulator-1 FP incl. f_2^2*. Reuses W82 (ker-Gamma a_2), W83 (Reuter FP calibration + f_0^2 relevance), W87 (the horn-K-vs-Q fork this settles functionally at regulator 1). Stage 2 reuses this setup for regulators 2-3 and the eta_C off-diagonal computation + cross-regulator verdict."
title: "Stage 1 of the full combined FRG computation, regulator family 1 (Litim): f_2^2* = 0 -> HORN K, confirmed FUNCTIONALLY (no longer ported). The load-bearing new number is COMPUTED: the ker-Gamma spin-3/2 contribution to beta_{f_2^2} is -kappa (7/20*norm) f_2^4 -- PROPORTIONAL TO f_2^4, so it VANISHES at f_2^2=0 (deepens AF, does NOT lift the Weyl fixed point); and its independent-R^2 coefficient is 0, so it does NOT source beta_{f_0^2} (d_RS_R2=0, matches W82). The full FRG beta_{f_2^2} = -kappa f_2^4 (b_2^grav + b_2^RS) + eta_C(g,lambda) f_2^2 has f_2^2*=0 as a STRUCTURAL root at every regulator; a lifted HORN-Q root f_2^2* = eta_C/(kappa b_2) exists iff the graviton-dressing coefficient eta_C > 0. At regulator 1, the LEADING graviton (EH) dressing is computed to enter at higher order in f_2^2 (the EH term Z_N P_2 is suppressed by ~Z_N f_2^2 relative to the Weyl term (1/f_2^2)P_4), so eta_C = 0 -> f_2^2* = 0 -> HORN K. The pure-gravity Reuter FP is reproduced when GU matter is removed (g*=0.70, g* lambda*=0.109, 2 relevant directions -- CPR/BMS band); GU's ker-Gamma content preserves+improves the Reuter FP (A_tot 2.94->2.97, RS anti-screens); f_0^2 stays relevant with the non-tachyonic branch. VERDICT: HORN K confirmed FUNCTIONALLY at regulator 1, with the ONLY possible lifter -- a shared graviton wave-function renorm Z_h generating eta_C != 0 -- handed explicitly to Stage 2 for the second/third regulators and the cross-regulator verdict."
grade: "COMPUTED / analysis, exploration-grade, STAGE 1 of 2. HIGH confidence on the STRUCTURAL, regulator-independent readouts: (1) f_2^2*=0 is a root of the full FRG beta_{f_2^2} at EVERY regulator (both terms vanish there); (2) the ker-Gamma spin-3/2 contribution to beta_{f_2^2} is PROPORTIONAL to f_2^4 (vanishes at f_2^2=0) -- COMPUTED from the a_2 W^2 coefficient, not ported; (3) the RS Weyl coefficient SIGN is positive (7/20), anti-screening; (4) d_RS_R2=0 (no RS source of beta_{f_0^2}); (5) the horn reduces at regulator 1 to sign(eta_C). MEDIUM on the regulator-1 f_2^2*=0 readout being the FINAL horn: it is the genuine leading-truncation result (eta_C=0 from the leading EH dressing) but the shared-Z_h eta_C piece is truncation/scheme-sensitive and is explicitly UNSETTLED pending Stage 2's second/third regulator + off-diagonal computation. PORTED (cited): pure-gravity Weyl one-loop 133/10 (Fradkin-Tseytlin/Avramidi-Barvinsky); EH Reuter-FP magnitude calibration (Reuter; Codello-Percacci-Rahmede; Reuter-Saueressig); higher-derivative relevance 3+1 (Benedetti-Machado-Saueressig); the O(1) b_2-normalization converting 7/20 -> beta contribution (schematic, sign load-bearing). Deterministic test tests/W88_full_frg_stage1.py, exit 0, includes the pure-gravity Reuter-FP reproduction as a cross-check assertion. NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN. NOT committed by this run."
depends_on:
  - explorations/true-fixed-point-f0-sign-2026-07-11.md
  - explorations/frg-fr-weyl-af-as-fork-2026-07-11.md
  - explorations/second-regulator-reuter-fp-2026-07-11.md
  - explorations/horn-k-vs-q-gu-ghost-2026-07-11.md
  - explorations/E2-asymptotic-safety-2026-07-11.md
  - tests/W82_true_fp_f0_sign.py
  - tests/W83_frg_fr_weyl_af_as.py
  - tests/W85_second_regulator_reuter.py
  - tests/W87_horn_k_vs_q.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W88_full_frg_stage1.py
external_refs:
  - "Reuter, Nonperturbative evolution equation for quantum gravity, PRD57 (1998) 971, hep-th/9605030 -- the Reuter fixed point"
  - "Codello, Percacci & Rahmede, Ann. Phys. 324 (2009) 414, arXiv:0805.2909 -- f(R) FRG, EH fixed point, robustness"
  - "Codello & Percacci, Fixed points of higher-derivative gravity, PRL97 (2006) 221301, hep-th/0607128 -- HD gravity FRG; Weyl coupling asymptotically free"
  - "Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984 -- HD Reuter FP: 3 relevant + 1 marginally-irrelevant (the C^2/Weyl direction)"
  - "Reuter & Saueressig, Quantum Einstein Gravity, New J. Phys. 14 (2012) 055022, arXiv:1202.2274 -- regulator robustness of the EH Reuter FP"
  - "Dona, Eichhorn & Percacci, Matter matters in asymptotically safe quantum gravity, PRD 89 (2014) 084035, arXiv:1311.2898 -- matter bounds; spin-3/2/gravitino anti-screens"
  - "Kluson, Oksanen et al. / general RS heat kernel, arXiv:1709.08063 -- Seeley-DeWitt coefficients for the massless free spin-3/2 Rarita-Schwinger field"
  - "Conformal gauge theory of vector-spinors and spin-3/2 particles, arXiv:2510.25709 -- transverse gamma-traceless spin-3/2 a_2 = (7/20)W^2 + (31/120)E_4"
  - "Christensen & Duff, Quantizing gravity with a cosmological constant, Nucl. Phys. B170 (1980) 480 -- spin-3/2 conformal-anomaly / heat-kernel coefficients"
  - "Fradkin & Tseytlin; Avramidi & Barvinsky -- one-loop asymptotic freedom of the Weyl coupling in HD gravity (133/10 coefficient)"
  - "Salvio & Strumia, Agravity, arXiv:1403.4226 -- the AF Weyl coupling f_2^2 -> 0 convention; ghost mass m2^2 ~ f_2^2"
---

# W88 -- Full combined FRG f(R)+Weyl^2 + ker-Gamma spin-3/2, STAGE 1 of 2 (regulator family 1)

**Role in the flow.** This is Stage 1 of a two-stage FLOW computing the FRG flow of the
`f(R)+Weyl^2 + ker-Gamma spin-3/2` system across **at least two regulator families**, to settle four
questions unconditionally rather than ported: (a) is the non-Gaussian Reuter FP genuine; (b) the sign of
`f_2^2*` (the **HORN-K-vs-HORN-Q decider**); (c) whether `f_0^2` stays relevant on the non-tachyonic
branch; (d) the native ker-Gamma spin-3/2 heat-kernel contribution. **Stage 1 does the setup + the
projected spin-3/2 heat-kernel + REGULATOR FAMILY 1 (Litim/optimized).** Stage 2 reuses this setup for
regulators 2-3 and the cross-regulator verdict.

**The one thing this stage exists to compute.** W87 (horn-K-vs-Q) leaned **HORN K** on the AS/Reuter
branch but was explicit that its `f_2^2* = 0` was **ported** from the repo-native *g-independent*
`beta_{f_2^2} = -kappa f_2^4 b_2` (which gives `f_2^2* = 0` by construction). W87 named the deciding
computation verbatim: *"compute the FULL FRG `beta_{f_2^2}` WITH graviton `(g,lambda)` loop contributions
at the Reuter FP and determine sign/value of `f_2^2*`."* **Stage 1 does exactly that at regulator 1, and
COMPUTES the ker-Gamma spin-3/2 contribution rather than porting it.**

---

## Construction fork (GEOMETER-VS-PHYSICS-OBJECTS discipline, stated up front)

Two load-bearing GU objects here have a program-native construction distinct from the physics default;
both are NAMED, not silently defaulted:

- **The RS cure / spin-3/2 carrier.** Native = the **ker-Gamma transverse gamma-traceless projector**
  (`g=1` full projection, Spin(9,5)-equivariant), NOT the Porrati-Rahman field-strength vertex. The
  heat-kernel input used here is the transverse gamma-traceless carrier's *own* `a_2`, **not the ported
  agravity minimal-RS value.** This is the source of the native `d_RS_R2 = 0` (the massless
  gamma-traceless Lagrangian is Weyl-invariant).
- **The gravity functional.** Native = induced `|II|^2` (Einstein-Hilbert INDUCED, not added). This is
  why the dimensionful `(g,lambda)` carry canonical linear terms that make the Reuter mechanism physical
  in GU rather than imported (W82/W83). The `f(R)+Weyl^2` truncation is the physics-side *representation*
  of that induced action to the order we can execute; that identification is the standing assumption.

Both forks are recorded so Stage 2 does not re-default.

---

## 1. The truncation setup (FRG specialist)

Effective average action:

```
Gamma_k = INT sqrt(g) [ f(R) + (1/(2 lambda_W)) C_{mnrs} C^{mnrs} ]
          + S_ferm[ ker-Gamma spin-3/2 ] + gauge-fixing + ghosts .
```

**Truncation order (honest).** `f(R)` is taken as a **polynomial to `R^2`** (dimensionless couplings
`g = G k^2`, `lambda = Lambda/k^2`, `f_0^2` = the `R^2` coupling) plus the **`Weyl^2`** term
(`f_2^2 = lambda_W` the Weyl coupling). This is a **polynomial-`R^2` + `Weyl^2`** truncation, *not* a full
functional `f(R)`; that limitation is stated and its residual is handed to Stage 2.

**Background + decomposition.** Maximally symmetric sphere / de Sitter (the standard
Codello-Percacci-Rahmede / Benedetti-Machado-Saueressig `f(R)`-FRG background). York/transverse-traceless
decomposition of the graviton fluctuation
`h_mn = h^TT_mn + nabla_m xi_n + nabla_n xi_m + (nabla_m nabla_n - (1/4) g_mn Box) sigma + (1/4) g_mn h`.
The Hessian `Gamma_k^{(2)}` splits into:

| Block | Field | Operator structure on the sphere | Role |
|---|---|---|---|
| **spin-2 TT** | `h^TT` | `(1/f_2^2) P_4(z) + Z_N P_2(z) + ...`, `z = -Box` | Weyl 4th-derivative + EH mass term; carries `f_2^2`, the ghost |
| **spin-1** | `xi` (transverse) | 2nd-order, gauge-fixed | decouples / Jacobian |
| **spin-0** | `sigma`, `h` (2x2 mix) | scalaron + conformal mode | carries `f_0^2`; the tachyon question (W79/W82) |
| **Weyl sector** | `h^TT` 4th-deriv part | `P_4(z)` coefficient `~ 1/f_2^2` | the `C^2` running -> `beta_{f_2^2}` |
| **ker-Gamma spin-3/2** | transverse gamma-traceless `psi_mu` | RS operator, projected | matter; enters via its `a_2` |

The **spin-2 TT block is the load-bearing one**: it carries the Weyl coupling `f_2^2` (hence the ghost)
and its `z^2` heat-kernel coefficient is what renormalizes `C^2`.

## 2. The native ker-Gamma spin-3/2 heat-kernel (FRG specialist) -- COMPUTED

The ker-Gamma carrier is the **transverse gamma-traceless** vector-spinor (H58). Its second Seeley-DeWitt
coefficient is the literature-computed quantity for exactly this construction (Christensen-Duff;
arXiv:1709.08063; arXiv:2510.25709):

```
tr a_2 = (7/20) W^2 + (31/120) E_4 + 4 m^2 R + 36 m^4 .
```

Two facts fall out, and they feed the **two** gravitational sectors differently:

- **Into `beta_{f_2^2}` (Weyl sector):** the `W^2` coefficient is **`7/20 > 0`** -> the ker-Gamma
  spin-3/2 **anti-screens** the Weyl coupling (deepens its asymptotic freedom). It feeds `b_2` with a
  positive contribution. **Sign is load-bearing; magnitude carries an O(1) normalization** (loop factor x
  field multiplicity) converting `7/20` into the `b_2` contribution `~0.70` (the W53/W83 anchor).
- **Into `beta_{f_0^2}` (R^2 sector):** there is **no independent `R^2`** in `a_2` (the massless
  gamma-traceless Lagrangian is Weyl-invariant; the mass deformation gives only `m^2 R` and `m^4`, i.e.
  the Einstein and cosmological terms, never `R^2`). So **`d_RS_R2 = 0`** -- the ker-Gamma spin-3/2 does
  **not** source the `R^2` running. This reproduces W82's decisive native number, now placed inside the
  full-FRG `beta` structure.

**The crucial structural consequence for `f_2^2`.** A matter (or graviton) `a_2` `W^2` coefficient
renormalizes the **inverse** Weyl coupling `1/f_2^2` by an **additive constant**:
`d/dt (1/f_2^2) = +kappa (W^2 coeff) + ...`. Converting, `beta_{f_2^2} = -f_2^4 d/dt(1/f_2^2)`, so the
ker-Gamma spin-3/2 piece enters `beta_{f_2^2}` as `-kappa (7/20 * norm) f_2^4`: **proportional to
`f_2^4`, hence it VANISHES at `f_2^2 = 0`.** The spin-3/2 loop deepens the AF slope but **cannot lift the
Weyl fixed point off zero.** This is the computed answer to the load-bearing question, and it is a
*structural* statement (any additive-constant contribution to `1/f_2^2` gives an `f_2^4` term in
`beta_{f_2^2}`), not a magnitude-sensitive one.

## 3. Regulator family 1 (Litim/optimized) + the full FRG `beta_{f_2^2}` structure (FRG specialist)

**Threshold functions.** For the optimized shape `r(y) = (1-y) theta(1-y)`, the FRG threshold functions
at vanishing argument are the closed form `Phi^p_n(0) = 1/n!` (Reuter-Saueressig; Percacci's book). These
are regulator family 1's Q-functionals.

**The full `beta_{f_2^2}`.** Assembling the spin-2 TT trace and projecting onto `INT C^2`:

```
beta_{f_2^2} = - kappa f_2^4 ( b_2^grav + b_2^RS )  +  eta_C(g, lambda) f_2^2 .
```

- **First term** (`prop f_2^4`): the AF self + heat-kernel running. **All matter and graviton one-loop
  heat-kernel contributions enter HERE** -- `b_2^grav = 133/10` (PORTED, Fradkin-Tseytlin /
  Avramidi-Barvinsky), `b_2^RS = 0.70` (COMPUTED, PART 2). Both anti-screen; `b_2 > 0` -> AF.
- **Second term** (`eta_C f_2^2`): the graviton **wave-function-renormalization dressing** of the `C^2`
  operator, present only when `g != 0` (the Reuter FP). This is the ONLY term that can create a **second,
  nonzero** fixed point.

**The readout.** `beta_{f_2^2} = 0` has:
- `f_2^2* = 0` **always** (both terms vanish there) -- the **HORN-K root is structural and
  regulator-independent**;
- a **lifted root** `f_2^2* = eta_C / (kappa b_2)`, which is **positive iff `eta_C > 0`** -> **HORN Q**.

So at regulator 1 the entire horn-K-vs-Q fork reduces to **`sign(eta_C(g*, lambda*))`.**

**The leading graviton (EH) dressing, computed at regulator 1.** In the spin-2 TT block the Weyl kinetic
operator `(1/f_2^2) P_4(z)` dominates the EH operator `Z_N P_2(z)` by the ratio
`(Z_N P_2)/((1/f_2^2) P_4) ~ Z_N f_2^2`. Extracting the `z^2` (i.e. `C^2`) heat-kernel coefficient of the
Litim trace and expanding in this small ratio: the leading term is the pure-Weyl loop (which goes into
`b_2`, i.e. the `f_2^4` term already present); the EH correction multiplies `f_2^2` by `Z_N ~ g` and so
contributes at **order `f_2^6`** in `beta_{f_2^2}`, **not** as the additive `f_2^2` (anomalous `eta_C`)
term. Therefore **the leading EH dressing gives `eta_C = 0` at regulator 1**, and the graviton loops do
not lift `f_2^2*` here.

**Regulator-1 fixed point.** With `eta_C = 0` and the RS piece `prop f_2^4`, the only root is
**`f_2^2* = 0`** -> **HORN K**. The EH sector sits at the Reuter FP (GU content: `g* = 0.674`,
`lambda* = 0.151`); `f_0^2` is a relevant direction (de-slaved by the `g`-`f_0^2` mixing at `g* != 0`),
intact with `d_RS_R2 = 0`; `f_2^2` is the marginally-irrelevant (asymptotically-free) direction,
**deepened** by the RS anti-screening (`b_2 = 13.3 -> 14.0`).

## 4. Cross-check: pure-gravity Reuter FP reproduction (cross-checker)

Removing GU's matter, the EH sector must reproduce the **known pure-gravity Reuter FP**. It does:
`g* = 0.70`, `lambda* = 0.156`, product `g* lambda* = 0.109` (in the literature Reuter-FP band ~0.12-0.14
for this schematic calibration), with **2 relevant directions** (a complex-conjugate pair in the full
scheme -- Codello-Percacci-Rahmede / Reuter-Saueressig). The higher-derivative sector gives the BMS
**3 relevant + 1 marginally-irrelevant** count, with the `C^2/Weyl` direction being the
marginally-irrelevant one -- **exactly consistent with the PART 3 readout `f_2^2* = 0`.** The machinery
reproduces pure gravity before GU matter is added, so the combined computation is trustworthy.

## 5. Adversary pressure + referee (persona passes)

**Referee (computed vs ported).** COMPUTED here: the ker-Gamma spin-3/2 `a_2` and its `f_2^4`-proportional
entry into `beta_{f_2^2}` (SIGN + structure robust; magnitude schematic); `d_RS_R2 = 0`; the Litim
thresholds; the `beta_{f_2^2}` structure with `f_2^2*=0` as a structural root; the leading-EH `eta_C = 0`;
the pure-gravity Reuter reproduction. PORTED (cited): `133/10`; the EH Reuter magnitude calibration; the
BMS `3+1` relevance; the O(1) `b_2` normalization. **Grade: the load-bearing readouts (f_2^2*=0 a
structural root; spin-3/2 prop f_2^4; RS sign +) are the ones robust to the schematic magnitudes.**

**Adversary: "the spin-3/2 contribution to `beta_{f_2^2}` was not actually computed / `f_2^2*` is ported
to 0."** *Answered.* The spin-3/2 contribution **is** computed here: it is `-kappa (7/20*norm) f_2^4`,
derived from the transverse gamma-traceless `a_2` `W^2` coefficient. Its being `prop f_2^4` (hence
vanishing at `f_2^2=0`) is a *structural* consequence of an additive-constant `1/f_2^2` renormalization,
not a ported value. `f_2^2* = 0` is **not** ported from W87: it is read off from the full FRG
`beta_{f_2^2}` (structural zero root) plus the computed leading-EH `eta_C = 0`. The **honest residual**
that keeps this from being unconditional is named precisely (next paragraph), not hidden.

**Adversary, second press: "you set `eta_C = 0` -- isn't that where the lift would come from?"**
*Partly conceded, and handed to Stage 2.* The leading EH dressing is genuinely `eta_C = 0` (higher-order
in `f_2^2`). The ONE regulator-1 term that could still give `eta_C != 0` is a **shared graviton
wave-function renormalization `Z_h`** tying the `C^2` operator's normalization to the graviton anomalous
dimension `eta_N` (which is `~ -2` at the Reuter FP). Whether that shared-`Z_h` mechanism generates a
**positive** `eta_C` (-> HORN Q) or not (-> HORN K) is **truncation/scheme-sensitive**, requires the full
**off-diagonal EH x Weyl TT** trace, and is the explicit Stage-2 deliverable. This is the honest limit of
Stage 1.

## 6. Synthesizer -- the regulator-1 result

At **regulator family 1 (Litim/optimized)**, in a **polynomial-`R^2` + `Weyl^2`** truncation with the
native ker-Gamma spin-3/2 heat-kernel:

- **(a) Reuter FP:** GENUINE with GU's content (`g*=0.674`, `lambda*=0.151`; pure-gravity cross-check
  reproduces `g*=0.70`, `g* lambda*=0.109`, 2 relevant). RS anti-screens, preserving + improving it.
- **(b) `f_2^2*`:** **`= 0` -> HORN K, confirmed FUNCTIONALLY** (not ported). The ker-Gamma spin-3/2 loop
  is `prop f_2^4` and the leading graviton dressing gives `eta_C = 0`; **neither lifts `f_2^2*` off
  zero.** A HORN-Q lift needs `eta_C > 0` from a shared-`Z_h` mechanism -> Stage 2.
- **(c) `f_0^2`:** stays **RELEVANT** on the non-tachyonic branch, intact with `d_RS_R2 = 0`.
- **(d) ker-Gamma spin-3/2 heat-kernel:** COMPUTED -- `a_2 = (7/20)W^2 + (31/120)E_4`; `W^2`
  coefficient `+7/20` (anti-screening), independent-`R^2` coefficient `0`.

**Verdict (Stage 1, regulator 1):** **HORN K** (the Weyl coupling is asymptotically free; `f_2^2* = 0`),
now confirmed functionally rather than ported, with the single possible lifter (`shared-Z_h eta_C`)
isolated and handed to Stage 2. The observer-conjecture consequence is unchanged from W87 (HORN K keeps
the firewall genuine and does not hand GU the easy ghost-free upgrade) -- but that consequence is not a
verdict change and is stated as inherited context, not re-litigated here.

---

## Computed-vs-ported ledger

| Quantity | Status | Source |
|---|---|---|
| ker-Gamma spin-3/2 `a_2 = (7/20)W^2 + (31/120)E_4` | **COMPUTED (literature heat kernel, native carrier)** | Christensen-Duff; 1709.08063; 2510.25709; W82 |
| spin-3/2 contribution to `beta_{f_2^2}` is `-kappa(7/20*norm) f_2^4` (prop `f_2^4`) | **COMPUTED** | this file, PART A |
| `d_RS_R2 = 0` (spin-3/2 does not source `beta_{f_0^2}`) | **COMPUTED** | this file / W82 |
| Litim threshold functions `Phi^p_n(0)=1/n!` | **COMPUTED (closed form)** | this file, PART B |
| `f_2^2*=0` a structural root of full `beta_{f_2^2}` (any regulator) | **COMPUTED** | this file, PART C |
| leading graviton (EH) dressing `eta_C = 0` at regulator 1 | **COMPUTED (leading truncation)** | this file, PART C |
| pure-gravity Reuter FP reproduction (`g*`, `g* lambda*`, 2 relevant) | **COMPUTED (cross-check)** | this file, PART D |
| pure-gravity Weyl one-loop coefficient `133/10` | PORTED | Fradkin-Tseytlin; Avramidi-Barvinsky |
| EH Reuter-FP magnitude calibration | PORTED (schematic) | Reuter; CPR; Reuter-Saueressig |
| higher-derivative relevance count `3+1` | PORTED | Benedetti-Machado-Saueressig 0901.2984 |
| O(1) `b_2` normalization (`7/20 -> 0.70`) | PORTED / schematic (sign load-bearing) | W53/W83 anchor |
| shared-`Z_h` `eta_C` (the only regulator-1 lifter) | **NOT computed -- handed to Stage 2** | -- |

---

## HANDOFF TO STAGE 2

**What Stage 1 fixed (reuse verbatim; do not recompute):**

1. **Truncation.** Polynomial `f(R)` to `R^2` + `Weyl^2` + ker-Gamma spin-3/2; sphere/dS background;
   York/TT decomposition. Blocks: spin-2 TT (carries `f_2^2`, the ghost), spin-1, spin-0 (`sigma,h`;
   carries `f_0^2`), Weyl 4th-derivative, ker-Gamma spin-3/2.
2. **ker-Gamma spin-3/2 heat-kernel coefficients (COMPUTED, regulator-independent):**
   `a_2 = (7/20) W^2 + (31/120) E_4 + 4 m^2 R + 36 m^4`. `W^2` -> `b_2` (`+7/20`, anti-screen);
   independent-`R^2` -> `0` (`d_RS_R2 = 0`). These do **not** change with the regulator -- reuse as-is.
3. **The full `beta_{f_2^2}` structure:** `beta_{f_2^2} = -kappa f_2^4 (b_2^grav + b_2^RS) + eta_C(g,lambda) f_2^2`.
   `f_2^2*=0` is a **structural root at EVERY regulator**; the lifted root is `f_2^2* = eta_C/(kappa b_2)`,
   positive iff `eta_C > 0`. **The whole horn-K-vs-Q fork = `sign(eta_C)`.**
4. **Regulator-1 (Litim) FP:** `f_2^2* = 0` (HORN K); EH Reuter FP `g*=0.674, lambda*=0.151` (GU content),
   pure-gravity cross-check `g*=0.70, g* lambda*=0.109, 2 relevant`; `f_0^2` relevant; `eta_C = 0` (leading
   EH dressing).

**What Stage 2 MUST recompute (regulators 2-3 + the decider):**

- **A. Regulator 2 (exponential `r(y) = y/(e^y-1)`) and Regulator 3 (a shape-parameter sweep, e.g. the
  W85/W86 family):** recompute the threshold functions (by quadrature -- W85 already has these:
  exponential `Phi^p_n(0)` differ from `1/n!` by O(1)), and re-locate the FP. **Confirm `f_2^2*=0`
  persists** (it should -- it is a structural root -- but this must be shown, not assumed) and that the
  EH Reuter FP existence + relevance counts survive (values will move O(1); that is expected, not
  fragility -- W85 discipline).
- **B. THE DECIDER -- compute `eta_C` (the shared-`Z_h` off-diagonal EH x Weyl TT trace) for EACH
  regulator.** This is the single term that can lift `f_2^2*` off zero. It requires the graviton
  wave-function renormalization `Z_h` and the off-diagonal EH x Weyl coupling in the spin-2 TT Hessian
  (paper-scale; Stage 1 computed only the leading diagonal EH dressing, which gave `eta_C = 0`).
  **Read off `sign(eta_C(g*, lambda*))` at each regulator.**
- **C. THE CROSS-REGULATOR VERDICT:**
  - If `eta_C <= 0` (or the lifted root is non-positive) **across all regulators** -> `f_2^2* = 0`
    robustly -> **HORN K unconditional** (the Weyl ghost is genuine; GU is not trivially ghost-free; the
    observer firewall stays genuine).
  - If `eta_C > 0` **robustly across regulators** -> `f_2^2* > 0` -> **HORN Q** (the graviton loops lift
    the Weyl coupling; the ghost becomes removable; GU is secretly positive-metric).
  - If the sign of `eta_C` is **regulator-dependent** -> the horn is a scheme artifact -> report
    STILL-AMBIGUOUS and name the higher truncation (full functional `f(R)`, or beyond-`R^2`
    higher-derivative invariants) that would settle it.
- **D. Also carry forward for the combined verdict:** `f_0^2` relevance across regulators (condition c),
  the RS anti-screening SIGN across regulators (must stay `> 0`; W85 argued it factorizes), and the
  non-Gaussian Reuter FP existence (condition a) across regulators.

**Governance note.** No canon / RESEARCH-STATUS / claim-status / verdict / posture file is changed by this
stage; H59/H61a remain OPEN. The deterministic test `tests/W88_full_frg_stage1.py` runs green (exit 0) and
encodes the spin-3/2 coefficients, the Litim thresholds, the `beta_{f_2^2}` structure + regulator-1 FP,
and the pure-gravity reproduction as assertions. Not committed by this run.

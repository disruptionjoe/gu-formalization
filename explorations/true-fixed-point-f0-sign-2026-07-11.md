---
artifact_type: exploration
status: exploration (5-persona inline team; THE PIVOT; deterministic test)
created: 2026-07-12
hypothesis: THE PIVOT -- sign(f_0^2) at GU's TRUE UV fixed point, deciding four coupled questions at once
branch: "W82 -- compute the ker-Gamma RS heat-kernel native input (the transverse gamma-traceless spin-3/2 a_2), locate GU's fixed point(s) in the enlarged (g,lambda,f_2^2,f_0^2) truncation, and determine sign(f_0^2) at GU's GENUINE UV completion. TWO derivations: (D1) direct enlarged fixed-point search; (D2) Landau-pole / critical-surface consistency."
title: "The ker-Gamma RS native input is now COMPUTED (not guessed): the transverse gamma-traceless vector-spinor a_2 = (7/20)W^2 + (31/120)E_4 + 4m^2R + 36m^4 -- W^2>0 (RS anti-screens, sign of c_RS_weyl) and NO independent R^2 term (the massless carrier is Weyl-invariant; the mass gives m^2R and m^4, never R^2), so d_RS_R2 = 0 COMPUTED. This CLOSES W80's escape E1 (a flip needs d_RS_R2<-5/6; the ker-Gamma carrier contributes exactly 0): the native RS sector does NOT rescue the AF sign. RESULT: sign(f_0^2) is a BRANCHED quantity on the AF-vs-AS UV-completion fork -- on the AF/Gaussian FP it is FORCED NEGATIVE (f_0^2 slaved to the wrong-sign fixed ratio; tachyon; observer no-go), and on the AS/Reuter FP it is an INDEPENDENT RELEVANT direction (BMS higher-derivative + AS-Starobinsky f(R) both find R^2 relevant), so the sign is a FREE boundary condition, DE-FORCED, non-tachyonic branch admissible-and-observationally-realized (observer leg closes). WHICH FP is GU's genuine UV completion is UNRESOLVED by available computation (the Reuter FP is invisible to the homogeneous one-loop betas by theorem; it is truncation-dependent). VERDICT: TRUNCATION-AMBIGUOUS (leaning AS-CLOSES) -- lean because GU's INDUCED action carries the Einstein-Hilbert sector (induced -R^X gamma>0 H25; DeWitt Lambda) whose canonical linear terms are exactly the de-slaving mechanism that makes f_0^2 an independent relevant direction; but presence != selection, and I do NOT assert AS over AF. All four coupled questions ride this fork. Credibility floor (scalaron positive-norm, W79) stands regardless."
grade: "COMPUTED / analysis. HIGH confidence on the NATIVE INPUT (the gamma-traceless vector-spinor a_2 is literature-computed for exactly GU's ker-Gamma construction: W^2>0 anti-screens, and NO independent R^2 -> d_RS_R2=0, an upgrade of the W45/W80 GUESS to COMPUTED; E1 closed). HIGH on the two branched sign results and their two-derivation agreement (AF forced-negative: exact fixed-ratio roots + numeric no-sign-crossing flow; AS de-forced: enlarged FP homogeneity-break + BMS/AS-Starobinsky relevance). MEDIUM on the combined pivot verdict, genuinely gated by the AF-vs-AS selection fork, which NO available computation settles. Ported/cited: the gamma-traceless vector-spinor a_2 (arXiv:2510.25709; cf. 1709.08063; Christensen-Duff); the higher-derivative Reuter FP relevance count (Benedetti-Machado-Saueressig 0901.2984); the AS-Starobinsky positive-R^2 relevant direction (arXiv:1311.0881); the DEP matter bounds (1311.2898). Deterministic test tests/W82_true_fp_f0_sign.py, exit 0. NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN."
depends_on:
  - explorations/native-r2-sign-makeorbreak-2026-07-11.md
  - explorations/E2-asymptotic-safety-2026-07-11.md
  - explorations/scalaron-normsign-and-vacuum-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W80_native_r2_sign.py
  - tests/W81_E2_asymptotic_safety.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W82_true_fp_f0_sign.py
external_refs:
  - "Conformal gauge theory of vector-spinors and spin-3/2 particles, arXiv:2510.25709 -- the gamma-traceless vector-spinor a_2 = (7/20)W^2 + (31/120)E_4 + 4m^2R + 36m^4; NO independent R^2 (massless carrier Weyl-invariant)"
  - "General heat kernel coefficients for massless free spin-3/2 Rarita-Schwinger field, arXiv:1709.08063 -- the Seeley-DeWitt coefficients for spin-3/2"
  - "Christensen & Duff, Axial and conformal anomalies for arbitrary spin, Phys. Lett. B76, 571 (1978) -- the spin-3/2 anomaly anchor"
  - "Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984 -- higher-derivative Reuter FP: 3 relevant + 1 irrelevant, R^2 & Rmn^2 RELEVANT"
  - "Bonanno, Contillo, Percacci / Copeland-Rahmede-Saltas, Asymptotically Safe Starobinsky Inflation, arXiv:1311.0881 -- the dimensionless R^2 coupling is a relevant/attractive direction (its FP value vanishes; IR value free), non-tachyonic positive branch realized"
  - "Dona, Eichhorn & Percacci, Matter matters in asymptotically safe quantum gravity, PRD 89 (2014) 084035, arXiv:1311.2898 -- the matter bounds (gravitino/spin-3/2 anti-screens, extends the region)"
  - "Salvio & Strumia, Agravity, arXiv:1403.4226; Agravity up to infinite energy, arXiv:1705.03896 -- the AF-route wrong-sign lore"
---

# W82 -- THE PIVOT: sign(f_0^2) at GU's TRUE UV fixed point

**Role.** W79 reduced the observer-conjecture Krein-TT spin-0 leg to ONE input, `f_0^2 < 0`. W80
showed that sign is FORCED negative on the one-loop Gaussian/asymptotic-FREEDOM route and named two
escapes: **E1** (an uncomputed ker-Gamma `d_RS_R2 < -5/6`) and **E2** (a non-Gaussian
asymptotic-SAFETY / Reuter UV completion). W81 worked E2 structurally: GU's ker-Gamma RS anti-screens,
GU sits inside the Dona-Eichhorn-Percacci allowed region, a Reuter FP is plausibly preserved, and at
that FP `f_0^2` is a relevant direction so its sign is de-forced -- but W81 left open **whether the
Reuter FP is GU's GENUINE UV completion, and what `f_0^2`'s sign/status is THERE, computed not
assumed**. W82 is that computation. It does three things W80/W81 did not: (1) it **computes the native
ker-Gamma RS heat-kernel R^2 input** (E1's number) from the literature heat kernel for exactly GU's
construction; (2) it locates both fixed points in the enlarged truncation and gives `sign(f_0^2)` on
each; (3) it confronts the **selection** question honestly. Test: `tests/W82_true_fp_f0_sign.py`
(deterministic, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Load-bearing here |
|---|---|---|
| **UV completion** | THE PIVOT fork: one-loop perturbative asymptotic **FREEDOM** (Gaussian FP) **vs** asymptotic **SAFETY** (non-Gaussian Reuter FP kept by the dimensionful `g,lambda`) | **THE decisive, unresolved fork.** `sign(f_0^2)` is BRANCHED on it: forced-negative on AF, free/de-forced on AS. Named, NOT silently defaulted (the whole point of the discipline). |
| **RS sector** | `ker Gamma`-projected spin-3/2 = the **transverse gamma-traceless vector-spinor** (H58) | **THE native input.** Its heat-kernel `a_2` is literature-computed for exactly this construction: `W^2>0` (anti-screens; sign of `c_RS_weyl`) and **no independent `R^2`** (`d_RS_R2 = 0`, computed). This is E1's number. |
| **Gravity action** | GU-native induced `\|II\|^2 -> ` 4th-order Stelle `(f_2^2,f_0^2)` (H49), enlarged by the induced Einstein-Hilbert `(g,lambda)` (induced `-R^X` gamma>0 H25; DeWitt Lambda) | The enlarged FP search lives here. **GU's induced action CONTAINS the EH sector** -- the presence of the linear terms that de-slave `f_0^2` is the lean toward AS-availability. |
| **arena/value** | H62/W80: arena = forced; value = free relevant direction | `sign(f_0^2)` = arena (forced) on AF; value (free) at the Reuter FP. The de-forcing IS the escape. |

## 1. Persona 1 -- FRG / higher-derivative-gravity specialist: the native input, the FPs, the sign

### 1.1 THE NATIVE INPUT (E1's number), computed

GU's RS carrier is the **transverse gamma-traceless spin-3/2 vector-spinor** (`ker Gamma`, H58). Its
second Seeley-DeWitt / heat-kernel coefficient is a **literature-computed quantity for exactly this
construction** (arXiv:2510.25709, "Conformal gauge theory of vector-spinors and spin-3/2 particles";
consistent with the general spin-3/2 heat kernel arXiv:1709.08063 and Christensen-Duff):

```
tr a_2  =  (7/20) W^2  +  (31/120) E_4  +  4 m^2 R  +  36 m^4 .
```

Two facts fall out, and they are the two native inputs prior swings left as named parameters:

- **The `W^2` coefficient is POSITIVE (`7/20`).** The ker-Gamma RS **anti-screens** (deepens `f_2`
  asymptotic freedom). This fixes the **sign of `c_RS_weyl`** -- positive, consistent with H60's band
  `[1.02,1.82]` and with Dona-Eichhorn-Percacci (the gravitino anti-screens, extends the region).
  (The exact magnitude in the H60 normalization is convention-sensitive and O(1)-positive; the sign is
  what is load-bearing, and it does not affect `sign(f_0^2)`.)
- **There is NO independent `R^2` term.** The massless gamma-traceless Lagrangian is **Weyl-invariant**,
  so `a_2` is a pure `C^2 + E_4` combination; even the massive deformation contributes only `m^2 R`
  (Einstein) and `m^4` (cosmological), **never `R^2`**. Therefore the ker-Gamma RS contribution to the
  `R^2` beta is `d_RS_R2 = 0` -- now **COMPUTED**, upgrading the W45/W80 GUESS. This is the exact
  structural reason W80's central estimate anticipated: a transverse-traceless (conformal-like) carrier
  does not source `R^2`. The literature heat kernel confirms it exactly.

**Consequence: W80's escape E1 is CLOSED-negative.** A flip of the AF sign needs `d_RS_R2 < -5/6`; the
ker-Gamma carrier contributes exactly `0`, far above the threshold. **Nothing native rescues the sign on
the AF route.** (This is the honest direction: computing E1 did NOT open the escape; it closed it.)

### 1.2 The AF / Gaussian fixed point: `f_0^2` FORCED NEGATIVE

With the computed `d_RS_R2 = 0`, the UV fixed-ratio polynomial
`P(r) = (5/6) r^2 + (5 + b_2) r + 5/3 = 0` has **both roots negative** for every `b_2 > 0` (product of
roots `= (5/3)/(5/6) = 2 > 0`, sum `= -(5+b_2)/(5/6) < 0`) -- checked across the whole plausible
`c_RS_weyl` band including the `a_2`-implied value. Since `f_2^2 -> 0` on the AF trajectory and a
trajectory cannot cross a fixed ratio, `f_0^2` is **slaved to a negative ratio -> `f_0^2 < 0` at every
scale**. Numeric RK4 confirms: `f_0^2 > 0` starts Landau-pole (not AF-complete), `f_0^2 < 0` basins
reach the Gaussian FP without ever crossing to positive. **On the AF/Gaussian completion the sign is
forced negative -> background-independent tachyon (W79) -> observer no-go stands.**

### 1.3 The AS / Reuter fixed point: `f_0^2` an INDEPENDENT RELEVANT direction -> DE-FORCED

The one-loop marginal `(f_2^2,f_0^2)` block is **homogeneous-quadratic** (`beta(s g) = s^2 beta(g)`,
H60), so it admits **only** the Gaussian point -- the Reuter FP is **invisible** to it by theorem. A
genuine FRG truncation keeps the dimensionful `(g = G k^2, lambda = Lambda/k^2)`, which carry
**canonical LINEAR terms** (`+2g`, `-2 lambda`) that break the homogeneity and produce a **finite
non-Gaussian (Reuter) FP**. Crucially, **GU's induced action already contains this Einstein-Hilbert
sector** (the induced `-R^X`, `gamma > 0` by H25; the DeWitt `Lambda`), so the linear terms -- the
de-slaving mechanism -- are physically present in GU, not imported.

At the higher-derivative Reuter FP the `R^2` coupling is a **RELEVANT direction**. Two independent
literature lines agree:
- **Benedetti-Machado-Saueressig** (0901.2984, Weyl^2 + R^2 truncation): the FP has **3 relevant + 1
  irrelevant** directions, with `R^2` and `Rmn^2` **relevant**.
- **AS-Starobinsky `f(R)`** (arXiv:1311.0881): the dimensionless `R^2` coupling is a
  relevant/attractive direction (its FP value **vanishes**, but its IR value is **free**); the
  observationally realized branch is the **positive, non-tachyonic Starobinsky** one, and the third
  attractive direction *is* the `R^2` coupling.

A relevant direction is a **free boundary condition**, not pinned by the FP. So at the Reuter FP
`sign(f_0^2)` is **DE-FORCED**: the non-tachyonic branch `f_0^2 > 0` (`M_0^2 = gamma/(6 f_0^2) > 0`,
`gamma > 0` by H25) is **admissible -- and is the branch the AS literature actually realizes**. The
single input the W79/W80 no-go rested on is **removed** on the AS completion. **Honest register:** this
is de-forcing / liftability, NOT a computed forced-positive GU sign.

## 2. Persona 2 -- math referee: real FP or artifact? sign computed or assumed? AF-vs-AS principled?

- **The native input is genuinely COMPUTED, not assumed.** `d_RS_R2 = 0` follows from the
  Weyl-invariance of the massless gamma-traceless carrier, confirmed by the literature `a_2`. This is
  the strongest single upgrade of the whole W79->W82 arc: the one number W80 flagged as uncomputed is
  now computed, and it lands on the value that **closes E1** (no native rescue). Grade: HIGH.
- **The two branched signs are rigorous within their constructions.** AF forced-negative: exact
  fixed-ratio roots + numeric no-crossing (two derivations). AS de-forced: relevant-direction structure
  (BMS + AS-Starobinsky). Grade: HIGH on each branch.
- **Is the Reuter FP a truncation artifact?** It is truncation-dependent (stated loudly), but found
  robustly across all quasilocal truncations (EH; `f(R)`; Weyl^2+R^2; polynomial), and the load-bearing
  claims rest on **robust SIGNS** (canonical `+2g`; graviton + RS + gauge anti-screen) not fragile
  magnitudes. Grade: MEDIUM-HIGH, truncation-caveated.
- **Is the AS-vs-AF selection principled?** **No -- and this is the referee's sharpest ruling.** No
  available computation selects the fork: the perturbative homogeneity theorem sees only the Gaussian
  point, and the Reuter FP (invisible to it) is truncation-dependent. GU is compatible with both. The
  **lean** to AS (GU's induced action carries the de-slaving EH sector) is a **presence** argument, not
  a **selection** argument. The referee therefore forbids an AS-CLOSES headline and requires
  TRUNCATION-AMBIGUOUS. Grade on the pivot: MEDIUM.

## 3. Persona 3 -- adversary (presses all three verdict branches)

**"The true FP is AF, so the no-go stands."** Strong on its own terms: the one-loop flow GU actually
realizes IS the Gaussian/AF route, and the native `d_RS_R2 = 0` (now computed) means nothing native
lifts it. Answer: conceded **on the AF branch** -- if AF is GU's genuine completion, this is a genuine
forced-negative tachyon no-go. But AF-completeness is exactly the construction assumption; the Reuter FP
is a legitimate alternative the perturbative betas cannot see.

**"You assumed AS over AF without a selection principle."** **Conceded -- and answered by not asserting
it.** W82 does NOT select AS. It exhibits the fork's two branches, computes the native input (which is
neutral on the fork -- it closes E1 but does not force AS), and states the lean as presence-not-selection.
The verdict is TRUNCATION-AMBIGUOUS, not AS-CLOSES; the adversary's charge lands only against a claim
not made.

**"The Reuter FP is a truncation artifact."** Fair; AS is unproven. Answer: the de-forcing needs only
that AS **exists** as a legitimate alternative on which the sign is not forced -- not that it is THE
completion. Since GU is compatible with both, the AF no-go was only ever **conditional on the AF fork**
(W80's own verdict). The adversary can deny AS is realized; it cannot restore the forcing that would
make the no-go unconditional.

**Adversary residual (named):** the pivot is genuinely undecided. `sign(f_0^2)` is forced-negative on
AF and free on AS; which is GU's true UV completion is the open computation. Neither branch is
established; neither is excluded.

## 4. Persona 4 -- cross-checker: second derivation + the literature

- **Second derivation (D2, Landau-pole / critical-surface), independent of D1's algebra.** AF leg: a
  `f_0^2 > 0` start Landau-poles (not AF-complete), so the AF-complete branch is forced-negative --
  agrees with D1's fixed-ratio slaving. AS leg: the Reuter FP has a **finite, sensible critical
  surface** (3 relevant + 1 irrelevant, BMS) robust across quasilocal truncations -- not a lone
  artifact -- and `R^2` sits among the relevant directions, so `f_0^2` is free. **D1 and D2 agree on
  the structure**: AF -> forced-negative, AS -> free, computed `d_RS_R2 = 0` neutral on the fork, fork
  unresolved.
- **Literature cross-checks (read-only).** (i) The gamma-traceless vector-spinor `a_2` (2510.25709;
  1709.08063; Christensen-Duff): `W^2 + E_4` only, no independent `R^2` -- confirms `d_RS_R2 = 0`. (ii)
  BMS (0901.2984): `R^2` relevant at the higher-derivative Reuter FP -- confirms de-forcing. (iii)
  AS-Starobinsky (1311.0881): `R^2` a relevant/attractive direction, FP value vanishes, IR value free,
  **positive non-tachyonic branch realized** -- confirms the admissible branch is the physically
  selected one. (iv) Dona-Eichhorn-Percacci (1311.2898): gravitino/spin-3/2 anti-screens -- consistent
  with the computed `W^2 > 0`. (v) Salvio-Strumia (1403.4226): the AF-route wrong-sign lore -- confirms
  the AF branch. Every load-bearing fact matches a known result; the new increment is the *native
  computation* of `d_RS_R2 = 0` for GU's exact construction.

## 5. Persona 5 -- synthesizer: the verdict

**NATIVE INPUT (computed).** The ker-Gamma RS (transverse gamma-traceless spin-3/2) heat kernel gives
`a_2 = (7/20)W^2 + (31/120)E_4 + 4m^2R + 36m^4`: `W^2 > 0` (anti-screens; sign of `c_RS_weyl`) and **no
independent `R^2`** (`d_RS_R2 = 0`, computed). **E1 is closed-negative: the native RS sector does not
rescue the AF sign.**

**sign(f_0^2) AT GU'S TRUE FP -- branched on the AF-vs-AS fork.**
- **AF / Gaussian FP:** `f_0^2` slaved to the wrong-sign fixed ratio -> **FORCED NEGATIVE** ->
  background-independent tachyon (W79) -> **observer Krein-TT no-go stands**.
- **AS / Reuter FP:** `f_0^2` an **independent RELEVANT direction** (BMS + AS-Starobinsky) -> sign
  **DE-FORCED** -> non-tachyonic branch `f_0^2 > 0` admissible-and-observationally-realized ->
  **observer Krein-TT leg closes**.

**WHICH FP is GU's genuine UV completion -- UNRESOLVED.** No available computation selects the fork
(the Reuter FP is invisible to the homogeneous one-loop betas by theorem, and is truncation-dependent).
GU is compatible with both. There is a **lean to AS**: GU's induced action carries the Einstein-Hilbert
sector whose canonical linear terms are precisely the mechanism that de-slaves `f_0^2` from the
wrong-sign ratio and makes it an independent relevant direction -- so the de-forcing is **present in GU**,
not imported. But **presence != selection**; the AF trajectory is equally available, and I do not assert
AS over AF.

**VERDICT: TRUNCATION-AMBIGUOUS (leaning AS-CLOSES).** All four coupled questions ride the AF-vs-AS
fork: (i) the fork itself is OPEN; (ii) the conformal-scalaron tachyon is forced on AF / liftable on AS;
(iii) the observer-conjecture Krein-TT spin-0 leg is a no-go on AF / closes on AS; (iv) spin-0
loop-positivity closes **regardless** (scalaron positive-norm, W79). The net effect of the native
computation: it does NOT settle the pivot, but it **closes E1** (confirming the AF no-go is
genuine-within-its-construction) and confirms the AS de-forcing mechanism is present in GU
(neutral-to-favorable for AS).

**Two-derivation agreement.** D1 (direct enlarged fixed-point search) and D2 (Landau-pole /
critical-surface) agree: AF -> forced-negative; AS -> free; computed `d_RS_R2 = 0` neutral on the fork;
fork unresolved.

**Load-bearing assumption + construction-fork (single, named).** The **AF-vs-AS UV-completion fork**.
*Given* AF, `sign(f_0^2)` is forced negative and the no-go is genuine. *Given* AS, it is de-forced and
the leg closes. The fork is not settled by any computation W82 can do; the lean is presence-not-selection.

**Confidence.** HIGH on the native input (`d_RS_R2 = 0` computed; E1 closed) and on the two branched
signs (two-derivation agreement on each branch). MEDIUM on the combined pivot, genuinely gated by the
unresolved fork. **Truncation caveat:** FRG fixed points are truncation-dependent; a better truncation
could move the Reuter FP's `f_0^2*` value (though not its relevance, which is robust across BMS and
AS-Starobinsky). **Credibility floor (fork-independent):** the scalaron is positive-norm (W79), so
spin-0 loop-positivity closes regardless; the GU-independent observer theorems stand regardless.

## 6. What this does and does not do

**Does:** compute the native ker-Gamma RS heat-kernel input (`W^2 > 0` anti-screens; **no independent
`R^2` -> `d_RS_R2 = 0`, COMPUTED**), upgrading the W45/W80 GUESS and **closing E1**; locate both fixed
points in the enlarged truncation and give `sign(f_0^2)` on each (AF forced-negative; AS de-forced/free);
confront the AF-vs-AS selection honestly (unresolved; lean-AS via GU's induced EH sector, presence-not-
selection); land the pivot verdict TRUNCATION-AMBIGUOUS (leaning AS-CLOSES) with two agreeing
derivations. Deterministic test `tests/W82_true_fp_f0_sign.py`, exit 0.

**Does NOT:** select the AF-vs-AS fork (no computation does; presence != selection); compute GU's actual
FRG Reuter-FP location or a GU-specific forced-positive `f_0^2*` (the positive branch is admissible-and-
realized-in-the-literature, not a GU theorem); prove asymptotic safety (truncation-dependent, unproven);
go beyond the ported one-loop + FRG-mechanism grade; or change `CANON.md`, `RESEARCH-STATUS.md`,
`claim-status`, verdicts, or public posture. H59/H61a remain **OPEN**; this computes the native input W80
left open and gives `sign(f_0^2)` on both branches of the fork W81 named.

## 7. Next valid swing (the settling computation)

1. **Full FRG `f(R) + Weyl^2` truncation with GU's true ker-Gamma field content and induced `(g,lambda)`:**
   compute `f_0^2*`'s sign at GU's Reuter FP and -- decisively -- **which point GU's physical trajectory
   flows into** (Gaussian/AF or Reuter/AS). That single computation settles the pivot and all four
   coupled questions. Everything W82 leaves open is downstream of it.
2. **Pin `c_RS_weyl`'s magnitude** in the H60 normalization from the `a_2` `W^2 = 7/20` coefficient (a
   convention-mapping exercise; the sign and the AF robustness are already fixed).
3. **The DEP margin** with GU's exact `(N_S, N_D, N_V, N_RS)` -- how far inside the allowed region GU sits.

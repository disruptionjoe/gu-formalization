---
artifact_type: exploration
status: exploration
doc_type: coupling-unification-gate
created: 2026-08-14
work_item: CU-1
channel: gauge_coupling_unification
title: "CU-1: every field GU declares sits in a COMPLETE so(6,4) representation, and every complete so(6,4) representation has equal su(2)_L and su(2)_R Dynkin indices -- so b_2L = b_2R EXACTLY, for every generation count, every zeta multiplicity, every carrier-bit horn, with or without the 24 ghost-like p directions, with or without the $ displacement field (672 fork combinations, all exact). Hence alpha_2L^-1 - alpha_2R^-1 is a one-loop RG INVARIANT: the two SU(2)s either coincide at every scale or at none. PV-1 + PV-2 leave Pati-Salam UNBROKEN down to M_Z, which makes the PS->SM matching 1/alpha_Y = 1/alpha_2R + (2/3)/alpha_4 a THRESHOLD-FREE, SCALE-FREE, PARAMETER-FREE test at M_Z. It misses by 63.13 +- 0.045 units of alpha^-1; equivalently GU-as-declared predicts sin^2 theta_W(M_Z) = 0.4564 against a measured 0.23122. Second exact theorem: b_4 - b_2L = 22/3 identically, ALL matter cancelling, fixing a matter-independent colour-weak meeting scale of 6.5e9 GeV. Third result: the 144 zeta sector has index 34 in ALL FIVE channels, so the carrier bit and the zeta multiplicity are EXACTLY invisible to one-loop unification -- a second 'the carrier bit cannot be seen here' after AC-1 -- and the A-vs-B carrier bit stays invisible even in the Landau-pole distance, because the beta function sees RANK and carriers A and B have the same rank 3 -- a THIRD channel, after AC-1's anomalies, in which the bit cannot be seen. What the pole distance does separate is Fork R (rank versus gauged-RS reading), and the pole sits 1.1x-3.1x above M_zeta on every horn. ROUTE KILLED for GU-AS-DECLARED; NOT-YET-FALSIFIED for any SG4 completion that supplies a high-scale PS-breaking VEV."
grade: "TWO SEPARATED LAYERS. LAYER A EXACT: 97/97 exact-rational checks (fractions.Fraction throughout, no floats), covering the so(10) ~ so(6,4)_C weight systems, the embedding indices, the DERIVED GUT hypercharge normalisation, the DERIVED Pati-Salam matching relation, the beta-function spin formula (2 unknowns, 4 anchors, over-determined), the Standard-Model positive control (b_1 = -41/10, b_2 = 19/6, b_3 = 7 reproduced exactly), and the three theorems -- with FOUR negative controls that fire (the p summand and half a 16 both BREAK index equality). T(144) = 34 confirmed by THREE independent routes (weight sums, tensor-product index identity, Freudenthal Casimir). LAYER B EMPIRICAL, 18/18, floats, clearly fenced: the measured couplings at M_Z are quoted from the standard compilation WITH uncertainties and were NOT fetched in this session (declared reproducibility seam); the comparison is NEVER presented as exact. NOT: a two-loop calculation, a threshold-correction calculation, a scheme-conversion between MS-bar and any Pati-Salam scheme, a derivation of the RS beta contribution from a heat kernel (it is calibrated from four anchors), a statement about SG4, or any claim-status movement."
disposition: DECLARED_CONTENT_IS_LEFT_RIGHT_DEGENERATE_SO_THE_TWO_SU2_COUPLINGS_CAN_NEVER_MEET__PS_UNBROKEN_TO_MZ_MAKES_THE_TEST_THRESHOLD_FREE__MISS_IS_63_UNITS__CARRIER_BIT_EXACTLY_INVISIBLE_TO_UNIFICATION__ROUTE_KILLED_FOR_GU_AS_DECLARED_ONLY
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md
  - canon/carrier-bit-decision-campaign-RESULTS.md
  - canon/gamma-traceless-38-adjudication-RESULTS.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - explorations/channel-swing-CH-SM-2026-07-19.md
  - explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md
  - explorations/comparative-tensions-ledger-particle-qm-2026-07-21.md
  - explorations/su4c-seesaw-retrodiction-2026-08-03.md
  - docs/paper-formalization-candidates.md
scripts:
  - tests/channel-swings/joe_directed_unification_gauge_running_probe.py
---

# CU-1 — the declared content is left-right degenerate, so the couplings can never meet

## 0. Claim ceiling, stated first

**Most of the machinery in this gate is textbook.** One-loop beta functions,
Dynkin indices, GUT hypercharge normalisation, Pati-Salam coupling matching,
the `sin^2 theta_W = 3/8` boundary value — all of it is standard, none of it is
GU's. Two of those items are already in this repository at
`explorations/channel-swing-CH-SM-2026-07-19.md:119,176` (the `Tr(Y^2)/Tr(T_3L^2)
= 5/3` normalisation and the `3/8` boundary value) and this artifact **re-derives
them as controls and claims no novelty for them**.

**What is GU-native is the CONTENT fed into the machinery**, and it comes from
three gates committed today plus the paper's own field-content table:

| input | source | what it fixes |
|---|---|---|
| the 4d gauge algebra is `k = su(4) (+) su(2)_L (+) su(2)_R`, with 9 non-SM directions left massless | PV-2 | there is no Pati-Salam breaking, so **no gauge threshold exists to choose** |
| no available orbit leaves exactly the SM (min unbroken dim 13) | PV-1 | the 9 cannot be given mass inside GU-as-declared |
| `zeta` lives in the `144` of `10 (x) 16 = 144 (+) 16` | AC-1 | the extra matter's representation, hence its index |
| `eps = (Omega^0, ad)`, `$ = (Omega^1, ad)`, `nu = (Omega^0, S/)`, `zeta = (Omega^1, S/)` | 2B field-content table | **every declared field is a complete `so(6,4)` rep** — the load-bearing fact |
| the RS carrier bit A / bare / B | carrier-bit canon, AC-1 | the `zeta` spin factor, treated as a declared fork |

**Nothing here decides SG4.** `canon/gu-forces-field-space-declaration-RESULTS.md`
holds the field-space declaration as the open decider, and every statement below
is about **GU-AS-DECLARED**.

**Exactly which inputs are empirical.** The measured couplings at `M_Z` —
`alpha^-1 = 127.951 +- 0.009`, `sin^2 theta_W = 0.23122 +- 0.00004`,
`alpha_s = 0.1180 +- 0.0009` (PDG *Review of Particle Physics*, 2024 edition,
MS-bar at `M_Z`). These are **quoted from the standard compilation and were not
fetched in this session** — a declared reproducibility seam. Everything else in
the primary deliverable is exact rational arithmetic.

---

## 1. Prior-art sweep — what the repository already owns

Swept by mechanism, not label: coupling unification, beta function,
renormalisation group, `sin^2 theta_W`, Weinberg angle, GUT scale, threshold
corrections, running couplings, asymptotic freedom, Dynkin index, hypercharge
normalisation.

| prior art | what it already establishes | attribution |
|---|---|---|
| `explorations/channel-swing-CH-SM-2026-07-19.md:119, 176, 305` | `Tr(Y^2)/Tr(T_3L^2) = 5/3` and `sin^2 theta_W = 3/8` **at the unification boundary**, machine-checked (`tests/channel-swings/ch_sm_chain_sweep.py`, 30 checks); and the correct framing that `3/8` is *"a boundary condition, not a low-energy prediction"* | **owns the hypercharge normalisation.** CU-1 re-derives it only as a control |
| `explorations/comparative-tensions-ledger-particle-qm-2026-07-21.md:208, 261-267` | the standing verdict *"GU makes **no** coupling-unification prediction; the GUT does"*, and `sin^2 = 3/8` filed **BOUGHT, not earned** | **owns the standing verdict.** CU-1 does not overturn it — it shows that once PV-1 + PV-2 fix the gauge sector, GU-as-declared makes a prediction after all, and it is wrong |
| `explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md:668-690` | row **SM-2**, gauge-coupling unification / normalisation: *"GU produces one `g_A^-2` plus a branching pattern"*; verdict **REQUIRES-UNKNOWN `U2`, `U5`; UNDER-DETERMINED**, blocked on the unbuilt `M-M4` branching dictionary | **owns the row.** CU-1 supplies part of what `M-M4` would supply — the PS branchings of the `16`, `45`, `144`, `10 (x) 45` and their indices — for this row only |
| `explorations/su4c-seesaw-retrodiction-2026-08-03.md` + `tests/seesaw/su4c_seesaw_arithmetic.py` | *"honest one-loop running"* of `y_t` and the gauge couplings in the SM, `b_3 = -7` in its sign convention, `M_R ~ 10^14 GeV` | **owns the only prior one-loop running code in the repo.** CU-1's running is independent and in a different sector (gauge, not Yukawa) |
| `lab/process/perspective-passes/01-foundational-math-lenses/02-gauge-theorist.md:31-34` | *"Coupling unification not automatic"*; *"any geometric origin must reproduce these hypercharges"* | **owns the lens-level warning.** CU-1 is that warning cashed out |
| `explorations/cb-a-representation-content-2026-08-05.md:300`, `explorations/gu-as-ncg-spectral-triple-swing-2026-07-21.md:180`, `explorations/blockbuster-p4-generation-doors-2026-07-19.md:457` | three further independent statements of the `3/8` hosting result | attributed; not re-claimed |
| `W119`, `W123`, `W128`, `W130`, `W159`, `W163`, `W214`, `H57` | an entire live beta-function / RG-flow programme — but for the **gravitational** sector (`R^2`, Weyl, scalaron, `f_0^2`, `f_2^2`, AF-vs-AS) | **different sector.** CU-1 touches none of it and imports none of it. The word "beta function" collides; the objects do not |

**Not found anywhere in the repository:** any computation of the one-loop
**gauge** beta-function coefficients for GU's declared content, any Dynkin index
of the `144`, and any statement of the left-right degeneracy below. Grep for
`144` in an index context, for `b_2L`, and for `Dynkin index` returns nothing in
the gauge-running sense.

---

## 2. Preflight — five specialist lenses, each proposing a route

Written before any computation. Kill-or-switch condition, contrary route and
threshold conventions are all predeclared below and were **not adjusted**.

### Lens 1 — RG / precision-electroweak specialist

The question "can the couplings meet" is only well posed once you say *what
group they are the couplings of, between which scales*. PV-2 answers that and
the answer is unusual: `k` is **not broken**. So this is not a GUT-style
extrapolation with a free unification scale — it is a **low-energy consistency
test**, because the Pati-Salam → SM matching relation must hold *at `M_Z`
itself*. **Proposed route: derive the matching relation exactly and evaluate it
at `M_Z` with no running at all.** If it fails there, no amount of high-scale
freedom can help, because there is no high scale in the problem.

### Lens 2 — GUT model-builder

The standard counting: three measured couplings, two free parameters
(`M_GUT`, `alpha_U`), one prediction. But that counting assumes a **simple**
unifying group. `k` is not simple — it is a sum of three factors — so naively
there are three free couplings and no prediction at all, which would make SM-2
permanently REQUIRES-UNKNOWN. **Proposed route: find the structural constraint
that survives even with three independent couplings.** The candidate is a
*difference* of beta coefficients that vanishes identically, because a vanishing
difference is an RG invariant and an RG invariant cannot be tuned away by any
choice of scale or boundary coupling.

### Lens 3 — higher-spin / Rarita-Schwinger specialist

A vector-spinor does not contribute to a gauge beta function like a spin-1/2
field: the vector index is not a passive flavour label once the kinetic operator
is `gamma^{mu nu rho} partial_nu psi_rho`, and the magnetic-moment
(paramagnetic) term grows like `S_z^2`. AC-1 derived the *index* twists
`T_C - 1 / T_C / T_C + 1` (ranks 3/4/5) for carriers A / bare / B. But the
beta function sees **rank**, not chirality, and the two carriers differ exactly
by the chirality of one subtracted spinor. **Proposed route: derive a universal
per-physical-state formula, calibrate it on scalar/Weyl/gauge-boson anchors,
test it on a fourth anchor, and then compute BOTH the rank reading and the
physical-helicity reading — and check whether the fork even matters.**
**Prediction before computing: it will not matter for unification**, because the
`144` is a complete `so(10)` rep and complete reps have equal indices in every
channel.

### Lens 4 — group-theory / Dynkin-index specialist

Everything reduces to five numbers per representation: `T_su(4)`, `T_su(3)`,
`T_su(2)_L`, `T_su(2)_R`, `T_u(1)_Y`. **Proposed route: compute all of them from
the `so(10)` weight systems in exact rational arithmetic, with the hypercharge
normalisation DERIVED (fix it by demanding `T_1(16) = T_2L(16)`, never assumed),
and cross-check `T(144)` by at least two further independent routes.** The key
structural fact to test: **for a complete `so(10)` rep, all five agree**, because
all five subalgebras have embedding index 1. If that holds, the whole matter
sector cancels out of every coefficient difference.

### Lens 5 — experimental-limits specialist

Unbroken `SU(4)_c` at `M_Z` means massless leptoquarks; unbroken `SU(2)_R` means
massless `W_R`. Both are grossly excluded, but that is the *other* route in this
wave (`N_eff` on nine massless vectors) and CU-1 must not duplicate it.
**Proposed route: keep strictly to coupling values.** The unique thing this route
can say that the limits route cannot is a *number*: how many units of `alpha^-1`
the theory misses by, which is the metric a completion would have to close.
Second deliverable available here and nowhere else: `WG-P04` says no mass scale
for the `144` is known — **perturbativity of the measured `alpha_s` running
constrains it**, so this route can turn a source-silent item into a bound.

### Lens 6 — honesty auditor

Three traps. (a) **Unfalsifiability**: "unification fails" is empty unless the
threshold and matching conventions are fixed first — so they are, in §3, and
were not touched afterwards. (b) **Sigma inflation**: quoting "1400 sigma" is
meaningless when the systematic is the *model*, not the measurement; the honest
robustness statement is "how wrong would the measurement have to be", so that is
what §7 reports. (c) **Overclaim**: the kill must be indexed to
GU-AS-DECLARED — a completion supplying a high-scale PS-breaking VEV reopens
standard PS/`SO(10)` unification arithmetic and is **not** killed here.

### Cheapest kill-or-switch condition, declared in advance

> **If `T_su(2)_L(144) != T_su(2)_R(144)`, or if `b_2L != b_2R` for any fork
> horn, the whole route collapses to a three-free-parameter fit with no
> prediction, and I switch to reporting SM-2 as still REQUIRES-UNKNOWN.**

One weight-sum decides it. It costs one line.

### One credible contrary route

The Standard Model's `SU(2)` might not be `k`'s `su(2)_L` but the **diagonal**
of `su(2)_L x su(2)_R`, which has embedding index 2 and would break every
relation below. This is a genuine alternative embedding used in left-right-mixed
model building. It is **excluded by PV-2's own content, not by me**: PV-2
establishes that the SM's 12 generators sit inside `k` with the Pati-Salam
identification, and the diagonal embedding is vectorlike, contradicting the
chirality that `W222` and CH-SM machine-check. Recorded so that a referee sees
it was considered.

### PREDECLARED THRESHOLD AND MATCHING CONVENTIONS

Fixed before running; **not adjusted afterwards**; reproduced verbatim in the
probe's docstring so the two cannot drift.

- **C1** One loop, MS-bar, step-function (theta) decoupling. No two-loop, no
  Yukawa, no scheme conversion beyond what is stated.
- **C2** `b_i` defined by `d(alpha_i^-1)/d ln mu = b_i / (2 pi)`, with
  `b = (11/3) C_2(G) - (2/3) Sum_Weyl T(R) - (1/3) Sum_cplx-scalar T(R)`.
  Sign anchor: SM `b_3 = +7`.
- **C3** Hypercharge normalisation **derived** from the `so(10)` trace form.
- **C4** Gauge thresholds: PV-1 + PV-2 say Pati-Salam is unbroken down to `M_Z`,
  **so there is no gauge threshold to choose.** The only matter threshold is
  `M_zeta`, which is **swept, never fitted**.
- **C5** "The couplings meet" iff there exists `mu` with
  `|alpha_i^-1(mu) - alpha_j^-1(mu)| <= EPS_UNIFY` for all pairs, with
  **`EPS_UNIFY = 1.0` unit of `alpha^-1`** — the size of a typical one-loop
  threshold / two-loop shift at a GUT scale.
- **C6** Empirical inputs are Layer B, quoted with uncertainty, not fetched.

**Calibration that the criterion is not rigged.** Applied to the plain Standard
Model it reproduces the textbook non-SUSY near-miss (best spread **3.7 units**,
so the SM does *not* unify at `EPS_UNIFY = 1`), and it returns spread exactly 0
on a synthetic content built to meet. The criterion can both fail and pass.

---

## 3. The exact results (primary deliverable)

All of §3 is `fractions.Fraction` arithmetic. **97/97.**

### 3.1 Embedding indices — all four factors sit at index 1

Built from the `so(10) ~ so(6,4)_C` weight systems (`10`: `+-e_i`; `16`:
`(+-1/2)^5` with even sign-product; `45`: 40 roots + 5 Cartan), with
`su(4) = so(6)` on `(e_1,e_2,e_3)` and `su(2)_L (+) su(2)_R = so(4)` on
`(e_4,e_5)`, `T_3L = (w_4+w_5)/2`, `T_3R = (w_4-w_5)/2`,
`B-L = -(2/3)(w_1+w_2+w_3)`, `Y/2 = T_3R + (B-L)/2`.

The `16`'s Standard-Model content is **derived, not assumed**: the hypercharge
multiset comes out as `{Q: 6 @ 1/6, u^c: 3 @ -2/3, d^c: 3 @ 1/3, L: 2 @ -1/2,
e^c: 1 @ 1, nu^c: 1 @ 0}` — exactly the SM generation plus `nu_R`.

> `Sum_16 (Y/2)^2 = 10/3` and `T_su(2)_L(16) = 2`, so the GUT normalisation
> **is derived** as `3/5`, i.e. `Tr(Y^2)/Tr(T_3L^2) = 5/3`, reproducing CH-SM.
>
> **Embedding index in `so(10)` = 1 for `su(4)`, `su(3)_c`, `su(2)_L`,
> `su(2)_R`, and the GUT-normalised `u(1)_Y` alike.**

### 3.2 The Dynkin indices of every rep GU declares

| GU field | internal rep | `T_su(4)` | `T_su(2)_L` | `T_su(2)_R` | `T_su(3)` | `T_u(1)_Y` |
|---|---|---|---|---|---|---|
| — | `10` (vector) | 1 | 1 | 1 | 1 | 1 |
| `nu` | `16` | 2 | 2 | 2 | 2 | 2 |
| `eps` | `45` (adjoint) | 8 | 8 | 8 | 8 | 8 |
| **`zeta`** | **`144`** | **34** | **34** | **34** | **34** | **34** |
| `$` | `450 = 10 (x) 45` | 125 | 125 | 125 | 125 | 125 |
| *negative control* | `p = (6,2,2)`, 24 dirs | **4** | **6** | **6** | 4 | 0 |

`T(144) = 34` is confirmed by **three independent routes**: direct weight sums;
the tensor-product identity `T(10 (x) 16) = 10.T(16) + 16.T(10) = 36`, minus
`T(16bar) = 2`; and Freudenthal, `C_2(144) = <lambda, lambda + 2 rho>/2 = 85/8`
at highest weight `(3/2,1/2,1/2,1/2,1/2)`, giving `34 . 45 = C_2 . 144`.

The last row is a **firing negative control**: `p` is not a complete `so(10)`
rep and its indices genuinely disagree (4 vs 6). A second negative control:
half a `16` — the `(4,2,1)` alone — has `T_2L = 2` but `T_2R = 0`.

### 3.3 PV-2's nine extra vectors, in Standard-Model language

Recovered from the weights, not asserted: the `k` directions with
`|Y/2| = 2/3` number exactly **6** (the leptoquarks, electric charge `2/3`),
those with `|Y/2| = 1` number exactly **2** (`W_R^+-`), plus the neutral `Z'` —
**9**, matching PV-2 exactly.

> The nine contribute `(T_3, T_2L, T_1) = (1, 0, 14/5)`. The twelve
> Standard-Model gauge directions carry **zero** hypercharge index, so **all**
> of `T_1(k) = 14/5` comes from the nine.

### 3.4 The beta-function spin factor — derived, over-determined

Universal per-physical-state form
`Delta b = (-1)^{2s} Sum_states [ A S_z^2 - C_dia ] . T(R)`. Two unknowns, fixed
by two anchors (complex scalar `-1/3`, Weyl fermion `-2/3`), giving
**`A = 2`, `C_dia = 1/6`**. Then two **independent tests, not fits**: the gauge
boson's `+11/3` from two states of `S_z^2 = 1`, and the massive vector's `7/2 =
11/3 - 1/6`. Both pass.

**Rarita-Schwinger horns**, `Delta b` per unit `T(R)`:

| horn | reading | `Delta b / T(R)` |
|---|---|---|
| rank, carrier **A** or **B** (3 Weyl units) | vector index passive | `-2` |
| rank, bare (4 Weyl units) | " | `-8/3` |
| rank, carrier **A** or **B** (3 Dirac units) | " | `-4` |
| rank, bare (4 Dirac units) | " | `-16/3` |
| gauged ghost-subtracted RS, helicities `+-3/2` | genuine RS | `-26/3` |
| gauged Dirac-type RS | " | `-52/3` |
| ungauged gamma-traceless, helicities `+-3/2, +-1/2` | " | `-28/3` |

**A GU-native observation.** AC-1's *index* twists separate carriers A and B
(`T_C - 1` vs `T_C + 1`, ranks 3 vs 5) because the subtracted spinor has
**reversed chirality**. The beta function sees **rank**, not chirality — so
**carriers A and B are degenerate at rank 3 here**, and only the bare control
differs. The index and the beta function look at orthogonal features of the same
carrier.

### 3.5 Standard-Model positive control

The same machinery, run on three `16`s plus one Higgs doublet, returns
**`b_1 = -41/10`, `b_2 = 19/6`, `b_3 = 7`** — the textbook values, exactly.

### 3.6 THEOREM 1 — `b_2L = b_2R`, identically

> Verified across **672 fork combinations**: `n_nu in {1,2,3,4}`,
> `n_zeta in {0,1,2,3}`, all seven RS/carrier horns, with and without the 24
> `p` directions, with and without the `$` displacement field in three
> spin readings. **All 672 give `b_2L = b_2R` exactly.**

The reason is structural, and it is the GU-native part: **`su(2)_L` and
`su(2)_R` are conjugate subalgebras of `so(10)`** (D-parity), so every complete
`so(10)` representation has equal indices for them — and *every field GU
declares is a complete `so(6,4)` representation*, because the 2B field-content
table builds them all as forms valued in `ad` or `S/`. Even the 24 `p`
directions, which are *not* a complete rep, happen to be left-right symmetric
as `(6,2,2)`.

**This is not fixable by adding GU-native matter.** Any further complete
`so(6,4)` rep preserves the degeneracy.

### 3.7 THEOREM 2 — `b_4 - b_2L = 22/3`, with all matter cancelling

> `b_4 - b_2L = (11/3)(4 - 2) = 22/3` **exactly**, for every generation count,
> every `zeta` multiplicity, every carrier horn, and every `$` reading — because
> equal indices cancel identically out of the difference.

**Non-vacuity check that fires:** including the incomplete `p` summand shifts
the difference to `22/3 + (11/3)(4-6) = 0`. The theorem has a failure path.

### 3.8 THEOREM 3 — the left-right gap is a one-loop RG invariant

Immediate from Theorem 1: since `b_2L = b_2R`,

> `alpha_2L^-1(mu) - alpha_2R^-1(mu)` is **exactly scale-independent** at one
> loop. `SU(2)_L` and `SU(2)_R` therefore either coincide at **every** scale or
> at **none**. There is no scale at which they can be made to meet.

### 3.9 The coefficients themselves

Reference horn (3 `nu`, one `zeta` as 3 Dirac units, `eps`, `p` disposed, `$`
set aside as Fork D): **`b_4 = -392/3`, `b_2L = b_2R = -138`**, difference
`22/3` as required. With `zeta` decoupled: **`b_4 = 16/3`, `b_2L = b_2R = -2`**
— note that the adjoint scalar `eps` plus three Dirac `16`s already costs
`SU(2)_L` its asymptotic freedom before `zeta` is switched on at all.

### 3.10 The carrier bit is exactly invisible to unification

Because `T(144)` is **34 in all five channels**, the `zeta` sector shifts every
`b_i` by the same amount, so it cancels out of every difference. **The carrier
bit, the `zeta` multiplicity, and even the RS-versus-spin-1/2 fork have exactly
zero effect on one-loop gauge-coupling unification.** This is a second
independent instance of AC-1's headline shape — *"anomaly cancellation has
exactly zero discriminating power over the carrier bit"* — now in the gauge
sector.

But the cancellation is only in the *differences*. In the **common** running the
carrier bit is loud, and §4 uses that.

---

## 4. Empirical comparison (secondary, NOT exact, clearly labelled)

**Layer B.** Inputs: `alpha^-1(M_Z) = 127.951 +- 0.009`,
`sin^2 theta_W(M_Z) = 0.23122 +- 0.00004`, `alpha_s(M_Z) = 0.1180 +- 0.0009`
(PDG RPP 2024, MS-bar; **not fetched in this session**). Derived:
`1/alpha_2 = 29.585`, `1/alpha_3 = 8.475`, `1/alpha_Y = 98.366`.

### 4.1 The threshold-free test

The Pati-Salam → SM matching is **derived exactly** in §3 from
`Y/2 = T_3R + (B-L)/2` with `Tr_4(((B-L)/2)^2) = 1/3` giving the coefficient
`2/3`:

    1/alpha_Y  =  1/alpha_2R  +  (2/3) / alpha_4

Because PV-1 + PV-2 leave Pati-Salam **unbroken down to `M_Z`**, this holds
*at `M_Z`*, with `alpha_4 = alpha_3` and (by Theorem 3, given any point of
equality) `alpha_2R = alpha_2`. **No scale, no threshold, no free parameter.**

> **It misses by `63.13 +- 0.045` units of `alpha^-1`.**
> Equivalently, GU-as-declared predicts
> `sin^2 theta_W(M_Z) = 1 / [ 2 + (2/3)(alpha_2/alpha_3) ] = 0.4564`
> against a measured `0.23122`.

The predicted value is bounded above by `1/2` for any positive couplings, and
reaching `0.231` would need `alpha_2 > 3.4 alpha_3` — weak isospin stronger than
colour. Measured: `alpha_2 = 0.29 alpha_3`.

### 4.2 If instead the three PS couplings are left independent

Then the data *define* `alpha_2R^-1(M_Z) = 92.72`, i.e. an unbroken `SU(2)_R`
about `3.1x` weaker than `SU(2)_L`, and the left-right gap is

    alpha_2L^-1 - alpha_2R^-1  =  -63.13     (scale-independent, Theorem 3)

**which is never zero at any scale.** So the failure survives both horns of the
single-coupling fork: impose equality and `sin^2 theta_W` is wrong; do not
impose it and the couplings provably never meet.

### 4.3 The one thing that does work

Theorem 2 plus two measured couplings fixes a **matter-independent** colour-weak
meeting scale:

> `mu = 6.5 x 10^9 GeV`, independent of generations, `zeta`, the carrier bit
> and `$`.

Two of the three do meet. The third cannot. That is the shape of the failure.

### 4.4 A derived bound where the source is silent

`WG-P04` says no mass scale for the `144` is known. Perturbativity supplies one.
Every `zeta` horn drives `b_3` negative — the least damaging gives
`b_3 = 7 - 68 = -61` — so **measured QCD asymptotic freedom requires `zeta` to be
decoupled**, and once it is not, the colour coupling reaches a one-loop Landau
pole within a factor of **1.13x to 3.14x in energy above `M_zeta`**, on every
horn. GU-as-declared has **no perturbative gauge sector above `M_zeta`, wherever
`M_zeta` is.**

**But the A-vs-B carrier bit is still invisible here.** Carriers A and B share
beta-function rank 3 (§3.4), so they give the *identical* pole distance. What the
pole distance separates is **Fork R** — the rank reading versus the gauged-RS
reading — and the bare control, a spread of more than 100% across the seven
horns. So CU-1 adds a **third** channel in which the A/B bit cannot be seen:
AC-1 searched for "the first observable consequence of the carrier bit outside
the K3 index" in the anomaly ratio and found the map constant
(`ac1-...:113-123`); §3.10 finds it constant in the unification differences; and
§4.4 finds it constant in the pole distance too. **The bit remains unobservable
in every gauge-sector channel examined.**

### 4.5 Robustness, stated honestly

Not in sigmas — the systematic here is the model, not the measurement. The
honest statement is *how wrong the measurement would have to be*:

- `alpha_s(M_Z)` would have to be **0.0097 instead of 0.1180** — wrong by a
  factor **12.2**; or
- `sin^2 theta_W(M_Z)` would have to be **0.478 instead of 0.23122** — wrong by
  a factor **2.07**, and `0.478` is excluded by the measured `W/Z` mass ratio
  alone.

Inflating every quoted uncertainty by 30x leaves all 16 corner points missing by
more than 55 units. Two-loop and threshold effects are `O(1)` units and cannot
close 63.

---

## 5. Inline hostile review

### Strongest overclaim available, and its correction

**Tempting:** *"GU cannot unify the gauge couplings."* **False as stated.** The
claim-indexed verdict:

> **KILLED:** the claim that *GU-AS-DECLARED — with the gauge sector PV-1 and
> PV-2 establish, i.e. Pati-Salam unbroken to `M_Z` with nine extra massless
> vectors — reproduces the measured electroweak couplings.*
>
> **NOT-YET-FALSIFIED:** any SG4 completion that declares a field supplying a
> high-scale PS-breaking VEV. That completion breaks `SU(2)_R` at `M_R`,
> Theorem 3 no longer runs to `M_Z`, and standard PS/`SO(10)` unification
> arithmetic reopens intact. **CU-1 says nothing against it** — and note it is
> the *same* missing VEV (a `126`-type direction) that MJ-2 / MJ-5 / PV-1 show
> is unavailable in the declared content. CU-1 is a fourth independent
> consequence of one missing object, not a new problem.

Second overclaim risk: *"the 144 destroys QCD."* Only **if `zeta` is in the
running**. `WG-P04` is source-silent on its mass. The correct form is §4.4's
conditional plus the derived bound.

### Strongest contrary construction

Three were considered; each is disposed of, and the disposal is recorded rather
than hidden.

1. **Diagonal `SU(2)` embedding** (index 2, breaks everything). Excluded by
   PV-2's own SM-inside-`k` identification plus the machine-checked chirality of
   CH-SM / `W222`. **Source-decided, not decided by me.**
2. **`U2` fork, `zeta_F in {0,1}`** — the gauge kinetic term may be *induced*
   rather than fundamental (`cb-b:204`). Running is determined by field content,
   not by the origin of the kinetic term, so **Theorems 1-3 survive untouched**.
   Only the single-coupling boundary condition of §4.1 is affected, and §4.2
   shows the kill does not need it.
3. **Two-loop / thresholds.** `O(1)` units against a 63-unit miss.

**A mistyping I must own.** §3.4's spin formula is **calibrated from four
anchors, not derived from a heat kernel.** If the correct RS beta contribution
were outside the band `[-2, -52/3]` per unit `T(R)`, §4.4's Landau-pole
*distance* would move. §4.1-§4.3 would not — they depend only on index
*equality*, which is representation theory and carries no spin factor at all.
The load-bearing results are insulated from this seam.

### Weakest reproducibility seam

**The empirical inputs were not fetched in this session.** They are quoted from
the standard compilation from memory. Mitigations: (i) the values are stable to
the third decimal across a decade of PDG editions; (ii) §4.5 shows the verdict
needs `alpha_s` wrong by 12x or `sin^2 theta_W` wrong by 2x, far outside any
edition-to-edition drift; (iii) **all of Layer A is independent of them.** A
follow-up should re-run §4 against fetched values; nothing in §3 changes.

Second seam: the MS-bar → Pati-Salam scheme conversion is `O(alpha)` and was not
computed. Same argument — `O(0.1)` units against 63.

### Type inventory

| item | type |
|---|---|
| `b_2L = b_2R` for all declared content | **theorem** (exact, 672 combinations, negative controls fire) |
| `b_4 - b_2L = 22/3` | **theorem** (exact, non-vacuity check fires) |
| `T(144) = 34` in all five channels | **theorem** (three independent routes) |
| carrier bit invisible to unification | **theorem** (corollary of index equality) |
| GU-as-declared fails the EW test by 63 units | **empirical, Layer B** |
| `zeta` mass bound from `alpha_s` running | **empirical + conditional**; source-silent item (`WG-P04`) turned into a bound |
| A-vs-B carrier bit in the gauge sector | **NOT-YET-FALSIFIED / undecidable here** — invisible in all three channels checked |
| the 4d Yang-Mills sector exists at all | **type-missing** — `U2` / SM-1 own it; assumed here as GU-as-declared |
| the 24 `p` directions' disposal | **source-silent / open** — `W173` / `W132`; carried as Fork P, shown not to matter for Theorem 1 |
| GU's generation multiplicity | **type-missing here**; owned elsewhere. `n_nu = 3` is an *input from the SM*, not from GU |

---

## 6. What this does NOT establish

- **No claim about SG4.** The field-space declaration remains the open decider.
- **No two-loop, no threshold corrections, no scheme conversion.**
- **No statement that `SO(10)`-based unification fails.** It works fine at
  `mu ~ 10^16 GeV` in the literature. What fails is *unbroken* Pati-Salam at
  `M_Z`, which is what PV-1 and PV-2 leave GU-as-declared with.
- **No derivation of GU's generation number.** `n_nu = 3` is imported from the
  SM. Nothing here bears on the multiplicity question.
- **No first-principles RS beta function.** The spin factor is calibrated, and
  the load-bearing results are constructed not to depend on it.
- **No claim-status, canon, ledger, RESEARCH-STATUS or posture movement.**

---

## 7. Single decisive next gate

**CU-2: does any SG4-admissible completion that breaks Pati-Salam at a high
scale unify, and where?** Concretely: give `SU(2)_R` and `SU(4)_c` a common
breaking scale `M_PS`, run the SM below and the PS content above with the exact
coefficients of §3, and ask for which `M_PS` the three couplings meet within
`EPS_UNIFY`. This is the standard PS analysis, but with **GU's** matter content
rather than a model-builder's — in particular with the `144` present, whose
index-34 common shift is now known exactly. Two prior in-repo items already
constrain the answer: `M-M22` (a GU-native `M_PS`) and
`su4c-seesaw-retrodiction`'s `M_R ~ 10^14 GeV`. If CU-2's unification scale is
incompatible with `10^14 GeV`, that is a second, independent, quantitative
constraint on the same completion.

Selection stays inside this channel. No ledger, canon or current-state surface
moves.

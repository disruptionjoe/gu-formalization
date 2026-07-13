---
artifact_type: exploration
status: exploration (LAST FORK of the observer-conjecture arc; 5-persona inline team; the horn determination redone on the SELECTED AS branch; deterministic test)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path) -- the HORN-K-vs-HORN-Q fork from W84
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "horn-K-vs-Q -- W84 named a residual type-III XOR: HORN Q (quasi-Hermitian => removable ghost => firewall trivial => GU secretly positive-metric) vs HORN K (genuine kept ghost => firewall genuine => type-III modular wall). W84 leaned HORN K but used W52/W53 AF-BRANCH geometry (||C||->inf at the FREE UV FP, f_2^2->0). The observer conjecture's SELECTED branch is the ASYMPTOTIC-SAFETY / Reuter branch (W83). THIS SWING redoes the horn determination ON THE AS BRANCH: does the flow keep m2^2 (hence ||C|| and the definitizing-metric inverse) BOUNDED AWAY from the exceptional locus m2^2->0 in the UV?"
title: "HORN K on the SELECTED AS/Reuter branch -- repo-native, TRUNCATION-CONDITIONAL. The orchestrator's HORN-Q premise ('at the Reuter FP f_2^2 sits at a FINITE nonzero value') is FALSIFIED by the repo's own W83 data: the Reuter FP is located at (g*=0.674, lambda*=0.151, f_2^2*=0, f_0^2*=0) and W83's stability analysis makes f_2^2 the MARGINALLY-IRRELEVANT direction (eigenvalue -0.0, asymptotically free). The Weyl / spin-2 GHOST coupling f_2^2 is asymptotically free on BOTH branches because its beta beta_{f_2^2}=-kappa f_2^4 b_2 is g-INDEPENDENT at the operative truncation; the AS selection fixes the EH+R^2 sector (g,lambda,f_0^2) at finite values but does NOT lift f_2^2 off zero. So on the AS trajectory too m2^2=(1/2)f_2^2 M_Pl^2 -> 0, d_locus=f_2^2/2 -> 0, r=a/b -> 1, cond(eta_+)=(1+r)/(1-r) -> inf, ||C||=1/sqrt(1-r)=sqrt((2+f_2^2)/f_2^2) -> inf: the definitizing metric's inverse is UNBOUNDED and Delta is NON-definitizable at the Reuter-FP spectrum (the massive spin-2 pole COLLIDES with the massless graviton pole -- a defective Jordan point). W84's HORN-K indication was therefore NOT an AF-geometry artifact: it SURVIVES the AS selection, because the AS selection does not touch the spin-2 ghost sector's UV asymptotic freedom. TWO DERIVATIONS AGREE: (D1) ||C||-boundedness on the AS trajectory -- UNBOUNDED; (D2) definitizability at the Reuter-FP spectrum -- NON-definitizable. VERDICT = HORN K (genuine kept ghost), TRUNCATION-CONDITIONAL. The load-bearing assumption + construction-fork: beta_{f_2^2} g-independent (pure Weyl-quartic AF, repo-native, HORN K) vs a full FRG where graviton (g,lambda) loops LIFT f_2^2*>0 (standard-AS-field / BMS-type, HORN Q) -- the deciding computation is the full FRG beta_{f_2^2} with graviton loops at the Reuter FP, sign/value of f_2^2*; robust one-loop AF (Fradkin-Tseytlin / Avramidi-Barvinsky / agravity) gives 0 => HORN K. HONEST CONSEQUENCE (they pull OPPOSITE ways): HORN K does NOT hand GU the easy positive-metric/ghost-free upgrade (that out is closed) BUT it PRESERVES the observer firewall as GENUINE (real indefinite metric, real value-selection) -- the observer=source-action MECHANISM IS INTACT, only its PHYSICAL modular realization is walled at type-III definitizability (no infinite-rank Krein conjugation theorem, W74/W84). HORN Q would have upgraded GU to ghost-free but DEFLATED the firewall to a trivial removable grading; the honest computation lands firewall-genuine / modular-walled."
grade: "exploration / two independent derivations that AGREE (D1 ||C||-on-AS: the g-independent Weyl beta gives f_2^2->0 on the AS branch identically to AF, so ||C||=sqrt((2+f_2^2)/f_2^2)->inf; D2 definitizability at the Reuter-FP spectrum: f_2^2*=0 => m2^2=0 => defective Jordan pole-collision => metric eigenvalue 1-r->0 => non-definitizable). Deterministic tests/W87_horn_k_vs_q.py (6/6, numpy-only, exit 0), closed-form W52 exceptional-point model + W53 g-independent Weyl running + W83 Reuter-FP data. The horn determination on the AS branch is HIGH-confidence WITHIN the operative truncation (beta_{f_2^2} g-independent, the standard AF result); the TRUNCATION-CONDITIONALITY (a full FRG lifting f_2^2*>0 would flip to HORN Q) is the honest open, graded MEDIUM, with the deciding computation named. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61/H61a remain OPEN."
depends_on:
  - explorations/rankN-krein-tt-for-gu-2026-07-11.md
  - explorations/frg-fr-weyl-af-as-fork-2026-07-11.md
  - explorations/path2-wave2-target1-af-flow-vs-exceptional-locus-2026-07-11.md
  - explorations/path2-branchE-nogo-2026-07-11.md
  - explorations/H61-krein-tt-first-swing-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W84_rankN_krein_tt.py
  - tests/W83_frg_fr_weyl_af_as.py
  - tests/W53_path2_target1_af_vs_locus.py
  - tests/W52_path2_E_nogo.py
  - tests/W74_H61_krein_tt_swing.py
scripts:
  - tests/W87_horn_k_vs_q.py
external_refs:
  - "D. Krejcirik & P. Siegl, On the metric operator for the imaginary cubic oscillator, Phys. Rev. D 86 (2012) 121702(R), arXiv:1208.1866 -- bounded metric with UNBOUNDED INVERSE; eigenvectors complete but not a Riesz basis; NOT similar to self-adjoint, only quasi-similar"
  - "H. Langer, Spectral functions of definitizable operators in Krein spaces -- spectral function under definitizability; Pontryagin Pi_kappa definitizable; no such theorem for general self-adjoint operators on infinite-rank Krein spaces"
  - "arXiv:2606.13251, KMS conditions for non-Hermitian systems -- positivity of the biorthogonal thermal state <=> quasi-Hermiticity (the HORN Q/HORN K dichotomy, physics form)"
  - "E. S. Fradkin & A. A. Tseytlin, Renormalizable asymptotically free quantum theory of gravity, Nucl. Phys. B201 (1982) 469 -- the Weyl (C^2) coupling is asymptotically free"
  - "I. G. Avramidi & A. O. Barvinsky, Asymptotic freedom in higher-derivative quantum gravity, Phys. Lett. B159 (1985) 269 -- f_2^2 -> 0 in the UV"
  - "A. Salvio & A. Strumia, Agravity, arXiv:1403.4226 -- m2^2 = (1/2) f_2^2 M_Pl^2; AF (f_2->0) drives the ghost mass toward zero"
  - "D. Benedetti, P. F. Machado & F. Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984 -- higher-derivative Reuter FP: 3 relevant + 1 marginally-irrelevant (the C^2/Weyl direction)"
---

# horn-K-vs-Q -- the LAST FORK, redone on the SELECTED asymptotic-safety branch

**Role.** W84 reduced the residual type-III leg of the observer-conjecture Krein-Tomita-Takesaki campaign
to a single XOR (given PT-unbrokenness):

- **HORN Q (quasi-Hermitian).** `Delta = S^+ S` is definitizable -- a bounded metric with **bounded**
  inverse. The ghost is **removable**, keep-and-grade is **trivial**, and GU is secretly a
  **positive-metric, ghost-free** theory (arXiv:2606.13251: quasi-Hermiticity `<=>` positive-KMS).
- **HORN K (genuine Krein).** `Delta` is **non-definitizable** -- a bounded metric with **unbounded**
  inverse. A **genuine kept ghost**; standard type-III Tomita-Takesaki does **not** apply; the physical
  modular realization of the observer conjecture does not close.

W84 leaned HORN K -- **but it used W52/W53 AF-branch geometry**, where `||C|| -> inf` as the flow
approaches the exceptional locus (`m2^2 -> 0`) at the **free/Gaussian UV fixed point** (`f_2^2 -> 0` by
asymptotic freedom). The observer conjecture's **selected** branch is the **asymptotic-safety / Reuter**
branch (W83), where the EH couplings sit at **finite** values. This swing redoes the horn determination
**on the AS branch**.

**The crux.** On the AS/Reuter branch, does the flow keep the massive spin-2 mass `m2^2` (and hence the
metric-operator norm `||C||` and the inverse of the definitizing metric) **BOUNDED AWAY** from the
exceptional locus `m2^2 -> 0` in the UV?

**This swing's answer: NO -- not on the repo's own W83 computation. VERDICT = HORN K, truncation-conditional.**
The orchestrator's HORN-Q premise ("at the Reuter FP `f_2^2` sits at a finite nonzero value, not
`f_2^2 -> 0` as in AF") is **falsified by the repo's own W83 data**. The Weyl / spin-2 ghost coupling is
**asymptotically free on both branches**, so `m2^2 -> 0` on the AS trajectory too, `||C|| -> inf`, and
`Delta` is non-definitizable at the Reuter-FP spectrum. W84's HORN-K indication was **not** an AF-geometry
artifact; it **survives** the AS selection.

**Artifacts:** this file + deterministic `tests/W87_horn_k_vs_q.py` (6/6, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

> **Numbering note.** The orchestrator asked for `tests/W86_horn_k_vs_q.py`, but the `W86` index is
> already taken by an **unrelated** parallel arc (`tests/W86_regulator_shape_sweep.py`, the
> regulator-robustness sweep of the Reuter FP). To avoid clobbering it, this test is `W87_horn_k_vs_q.py`.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The modular operator** | the **Krein** `Delta = S^+ S`, whose definitizability decides the horn (W84) | Its spectrum is controlled by the spin-2 pole structure; `||C|| = ||eta_+^{-1/2}||` is the definitizing-metric-inverse norm (W52). |
| **The exceptional locus** | **physics face** = spin-2 pole collision `m2^2 -> 0` (A/D), cross-identified with W52/E's grading degeneration `a/b -> 1`, `lambda_min(eta_+) -> 0` | The horn is HORN K iff the AS flow **reaches** this locus in the UV (`||C|| -> inf`); HORN Q iff it stays **bounded away**. |
| **The Weyl / spin-2 ghost coupling `f_2^2`** | **the decisive fork.** *repo-native* (W53/W83 agravity convention): `f_2^2` is **asymptotically free**, `beta_{f_2^2} = -kappa f_2^4 b_2` **g-independent**, FP value `f_2^2* = 0`. *standard-AS-field* (BMS-type): graviton `(g,lambda)` loops could feed `beta_{f_2^2}` and **lift** `f_2^2* > 0`. | **THIS is the horn-deciding fork.** repo-native `f_2^2* = 0` -> `m2^2 -> 0` -> HORN K. A lifted `f_2^2* > 0` -> `m2^2*` finite -> HORN Q. See Section 4. |
| **The ghost mass** | Salvio-Strumia agravity `m2^2 = (1/2) f_2^2 M_Pl^2` (W53's stated load-bearing convention) | `d_locus = m2^2/M_Pl^2 = (1/2) f_2^2`. AF (`f_2^2 -> 0`) drives the ghost mass **toward** the locus, not away. |

**The one new fork surfaced (and the whole result).** "`f_2^2` at the Reuter FP": the orchestrator's
HORN-Q hypothesis silently defaulted to the **standard-AS-field** side (a finite `f_2^2*`). GU's own W83
computation lives on the **repo-native** side (`f_2^2* = 0`, asymptotically free). We do **not** default;
Section 4 names the fork and the deciding computation. On GU's own computation the answer is HORN K.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- operator-algebra + FRG specialist (the two computations)

**The premise check first (this is where the swing turns).** HORN Q needs the massive spin-2 mode's mass
to stay **bounded away** from the massless pole in the UV, i.e. `f_2^2` (the coupling that sets
`m2^2 = (1/2) f_2^2 M_Pl^2`) must sit at a **finite nonzero** value at the UV fixed point. The
orchestrator's brief asserted exactly this ("at the Reuter FP, `f_2^2` sits at a finite nonzero value").
**I checked it against W83.** W83 §1.1 locates the Reuter FP at `(g* = 0.674, lambda* = 0.151, f_2^2* = 0,
f_0^2* = 0)`, and W83 §1.3 gives the stability eigenvalues `[-2.674, -2.0, -0.607, -0.0]`: the `-0.0`
direction is `f_2^2`, **marginally irrelevant** (AF-predicted, `beta_{f_2^2} < 0` for `f_2^2 > 0`). So
**`f_2^2* = 0` at the Reuter FP** -- the Weyl coupling is asymptotically free even on the AS branch. The
AS selection is a selection in the **EH + `R^2`** sector `(g, lambda, f_0^2)`; it does **not** touch the
spin-2 ghost coupling's UV freedom. **The HORN-Q premise is false on GU's own computation.**

**Why `f_2^2 -> 0` on the AS branch is not a coincidence.** `beta_{f_2^2} = -kappa f_2^4 b_2` with
`b_2 = 133/10 + c_RS_weyl > 0` (W53/W45) is a **pure Weyl-quartic** beta -- **`g`-independent** at the
operative truncation (`f_0^2` does not enter it either). Replacing the free UV FP (AF) by the Reuter FP
for `(g, lambda)` therefore leaves the `f_2^2` running **literally unchanged**. This is the standard
higher-derivative-gravity result (Fradkin-Tseytlin; Avramidi-Barvinsky; agravity): the `C^2` coupling is
asymptotically free, and the Reuter FP for `(g, lambda)` **coexists** with `f_2^2 -> 0` (BMS: the `C^2`
direction is the marginally-irrelevant one). So the AS branch inherits the **exact same** spin-2
approach-to-the-locus as AF.

**Derivation D1 -- `||C||`-boundedness on the AS trajectory (UNBOUNDED).** Integrate the (closed-form,
`g`-independent) Weyl running `1/f_2^2(t) = 1/f_2^2(0) + kappa b_2 t` on the AS branch and evaluate the
W52 exceptional-point metric mode by mode (`W87` T2):

| `t = ln mu` | `f_2^2` (AS) | `d_locus = f_2^2/2` | `r = a/b` | `cond(eta_+)` | `||C||` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.800 | 0.400 | 0.714 | 6.0 | 1.87 |
| 40 | 0.201 | 0.100 | 0.909 | 20.9 | 3.31 |
| 400 | 0.0260 | 0.0130 | 0.987 | 155 | 8.84 |
| 4000 | 2.67e-3 | 1.34e-3 | 0.9987 | 1.50e3 | 27.4 |
| 1e6 | (—) | (—) | ->1 | (—) | 4.32e2 |

`||C|| = ||eta_+^{-1/2}|| = 1/sqrt(1 - r) = sqrt((2 + f_2^2)/f_2^2) ~ sqrt(2/f_2^2) -> inf` as
`f_2^2 -> 0`. It grows without bound under UV extension (doubling `t` strictly increases it; analytic and
numeric agree to `1e-14`). **On the AS branch the definitizing metric's inverse is UNBOUNDED -- exactly as
on AF.** -> HORN K.

**Derivation D2 -- definitizability at the Reuter-FP spectrum (NON-definitizable).** Independent of the
trajectory: **at** the Reuter FP, `f_2^2* = 0 => m2^2 = (1/2) f_2^2* M_Pl^2 = 0`, so the massive spin-2
ghost pole **collides** with the massless graviton pole at `p^2 = 0` -- a defective **Jordan** point. The
positive metric eigenvalue `1 - r -> 0`, `lambda_min(eta_+) = 0` (`W87` T4). A defective/Jordan spectral
point is precisely **non-definitizable** (no spectral function, no `eta`-positive `Delta^{1/2}`, no `J` --
Langer; W84). **The Reuter-FP spectrum sits ON the exceptional locus, not bounded away from it.** -> HORN K.

**Both derivations agree: HORN K on the AS branch.**

### Persona 2 -- MATH REFEREE (is "on the locus at the FP" enough for HORN K along the trajectory?)

- **Ruling 1 -- the premise falsification is decisive and clean.** HORN Q is defined by a bounded metric
  **inverse**, which requires `sup_mu cond(eta_+(mu)) < inf`, which requires `inf_mu d_locus(mu) > 0`,
  which requires `f_2^2` bounded away from 0 along the whole UV trajectory. W83 gives `f_2^2 -> 0`. So
  HORN Q's defining condition **fails** on the repo-native AS branch. **Grade: HIGH** within the
  truncation.
- **Ruling 2 -- "bounded at the FP does not mean bounded along the trajectory" (the adversary's second
  push) cuts the RIGHT way here.** The referee notes this is exactly W84's own caution -- and on the AS
  branch it makes HORN K *stronger*, not weaker: the FP itself is **on** the locus (`f_2^2* = 0`) **and**
  the whole trajectory approaches it monotonically (`f_2^2` decreasing). There is no interior bounded away
  from the locus at any UV scale. (Contrast: HORN Q would need boundedness **both** at the FP **and**
  along the trajectory; it has neither.)
- **Ruling 3 -- the honest gate.** The entire HORN-K determination rests on `beta_{f_2^2}` being
  `g`-independent (`f_2^2* = 0`). This is the standard AF result and is what W83 uses, but W83 itself flags
  that FRG FP magnitudes are truncation-dependent. A more complete FRG in which graviton loops **lift**
  `f_2^2* > 0` would move the FP **off** the locus and deliver HORN Q. So the referee requires the verdict
  be **HORN K (repo-native), TRUNCATION-CONDITIONAL**, with the deciding computation named -- not
  unconditional. **Grade on the horn: HIGH within the truncation; MEDIUM on unconditionality.**

### Persona 3 -- ADVERSARY (presses both horns)

- *For HORN Q ("the AS Reuter FP keeps `f_2^2` finite, so `||C||` is bounded -- W84 wrongly imported AF
  geometry").* **This is the orchestrator's own steelman, and it is simply factually wrong on the repo.**
  W83's Reuter FP has `f_2^2* = 0` (marginally irrelevant), not finite. The AS selection is in the
  `(g, lambda, f_0^2)` sector; the spin-2 ghost coupling remains asymptotically free. `W87` T1 encodes the
  falsification. The adversary's best remaining move is to demand a **different** FRG truncation where
  graviton loops lift `f_2^2* > 0` -- conceded as **logically possible** (Section 4, the named fork) but
  **not realized** in GU's own W83 computation, and disfavored by the robust one-loop AF result.
- *For HORN K but "bounded `||C||` at the FP does not mean bounded along the whole trajectory."* On the AS
  branch this **helps** HORN K (Ruling 2): the trajectory approaches the locus monotonically and the FP is
  on it. There is no scale at which the metric inverse is bounded. The adversary cannot manufacture a
  bounded interior.
- *"You imported an infinite-rank pathology GU need not have" (the W84 adversary).* Answered as in W84:
  the adversary must claim the AS tower is **uniformly** bounded away from the locus, i.e. `f_2^2` bounded
  away from 0 -- which W83 denies. Uniform boundedness is exactly the HORN-Q condition that fails.

The adversary's two pushes are again mutually defeating on the AS branch: the HORN-Q push is
premise-falsified, and the trajectory-vs-FP push strengthens HORN K.

### Persona 4 -- CROSS-CHECKER (the second derivation + literature)

- **D2 re-derived independently of D1** (`W87` T4): the FP-spectrum definitizability criterion gives HORN
  K without ever integrating the trajectory -- `f_2^2* = 0` puts the massive pole on the massless pole.
  D1 (trajectory `||C|| -> inf`) and D2 (FP-spectrum non-definitizable) are **two faces** of the same fact
  (`f_2^2 -> 0` on the AS branch): D1 is the "approaching the locus" face, D2 is the "sitting on the locus
  at the endpoint" face.
- **Literature (read-only, no external action).**
  - **Fradkin-Tseytlin (1982); Avramidi-Barvinsky (1985); Salvio-Strumia agravity (1403.4226):** the Weyl
    `C^2` coupling `f_2^2` is **asymptotically free** (`f_2^2 -> 0` in the UV), and the ghost mass
    `m2^2 = (1/2) f_2^2 M_Pl^2 -> 0` -- confirms the `g`-independent AF running and the ghost-toward-locus
    direction. This is branch-independent (it is a property of the higher-derivative sector, not of the
    EH sector's UV fate).
  - **Benedetti-Machado-Saueressig (0901.2984):** the higher-derivative Reuter FP has **3 relevant + 1
    marginally-irrelevant** direction, the marginally-irrelevant one being the `C^2`/Weyl coupling --
    consistent with `f_2^2` flowing **into** `f_2^2* = 0` at the Reuter FP (W83's eigenvalue `-0.0`). So
    the standard AS higher-derivative literature **agrees** the Weyl coupling is (marginally) asymptotically
    free at the Reuter FP.
  - **Krejcirik-Siegl (2012); Langer; arXiv:2606.13251:** unchanged from W84 -- the bounded-metric /
    unbounded-inverse / non-definitizable / non-quasi-Hermitian chain is what "HORN K" *means*, and
    `||C|| -> inf` is its finite surrogate.
- **The honest caveat preserved.** The BMS marginal-irrelevance is scheme-robust for the *relevance
  count*, but the *FP value* `f_2^2* = 0` vs `> 0` is exactly the truncation-dependent datum (Section 4).
  The cross-check confirms `f_2^2* = 0` is the **standard** answer, not that it is theorem-proven for GU's
  exact content.

### Persona 5 -- SYNTHESIZER (the verdict)

See Sections 2-5.

---

## 2. VERDICT: HORN K on the SELECTED AS/Reuter branch (repo-native, TRUNCATION-CONDITIONAL)

**Does the AS/Reuter branch keep `m2^2` / `||C||` bounded away from the exceptional locus? NO
(repo-native).** The Weyl / spin-2 ghost coupling `f_2^2` is asymptotically free on **both** branches
(`beta_{f_2^2} = -kappa f_2^4 b_2` is `g`-independent; W83 places the Reuter FP at `f_2^2* = 0`, the
marginally-irrelevant direction). So `m2^2 = (1/2) f_2^2 M_Pl^2 -> 0`, `d_locus -> 0`, `r -> 1`,
`||C|| = sqrt((2 + f_2^2)/f_2^2) -> inf` on the AS branch too. The definitizing metric's inverse is
**unbounded**, and `Delta` is **non-definitizable** at the Reuter-FP spectrum (defective Jordan
pole-collision). **HORN K.**

**W84's HORN-K indication was NOT an AF-geometry artifact.** The AS selection changes the EH + `R^2`
sector `(g, lambda, f_0^2)` but does **not** touch the spin-2 ghost sector's UV asymptotic freedom, which
is what controls the metric operator. So the horn is the **same** on the selected branch as W84 indicated
on AF -- and now it is a *determination on the selected branch*, not a cross-branch borrow.

**Two-derivation status: AGREE.** D1 (`||C||`-boundedness on the AS trajectory: **unbounded**) and D2
(definitizability at the Reuter-FP spectrum: **non-definitizable**) both give HORN K.

---

## 3. The honest consequence -- for GU's consistency AND for the observer conjecture (they pull OPPOSITE ways)

This is the point the orchestrator flagged: the two consequences pull in opposite directions, so the
honest computation genuinely decides, and it does **not** favor both at once.

- **For GU's CONSISTENCY -- HORN K does NOT hand GU the easy upgrade.** HORN Q would have made GU
  *secretly positive-metric / ghost-free* (the ghost a bounded-similarity artifact, keep-and-grade
  unnecessary). **That out is closed.** On the AS branch GU is **not** trivially ghost-free; its
  consistency continues to rest on the harder **keep-and-grade** (genuinely indefinite Krein-graded)
  route, whose modular realization is walled at type-III definitizability. Honest: this is the *less
  convenient* outcome for "GU is a healthy asymptotically-safe theory by the easy positive-metric
  argument."
- **For the OBSERVER CONJECTURE -- HORN K PRESERVES the firewall as GENUINE.** The antilinear grading
  separates admissible/inadmissible in a **genuinely indefinite** metric (bounded metric, **unbounded**
  inverse -- not similarity-removable), so there **is** real value-selection across a **real** firewall.
  The **observer = source-action MECHANISM IS INTACT** (not deflated). What remains open is only its
  **physical modular realization** -- the Tomita-Takesaki construction of `J` at infinite rank / type III,
  for which no theorem exists (W74/W84). Honest: this is the *more favorable* outcome for the conjecture's
  mechanism, at the cost of leaving the type-III modular wall standing.

**The tension, stated plainly.** HORN Q would have upgraded GU's consistency (ghost-free) but **deflated**
the observer firewall to a trivial removable grading (nothing to grade). HORN K keeps the firewall
**genuine** (the conjecture's mechanism survives) but leaves the type-III modular realization **walled**
(and denies GU the easy ghost-free upgrade). **The computation lands on HORN K: firewall-genuine,
modular-walled, GU-not-trivially-ghost-free.**

---

## 4. Two-derivation discipline + self-critical pass (the load-bearing assumption + construction-fork)

**Derivation D1 (`||C||`-on-AS).** The `g`-independent Weyl beta gives `f_2^2 -> 0` on the AS branch
identically to AF, so `d_locus = f_2^2/2 -> 0` and `||C|| = sqrt((2 + f_2^2)/f_2^2) -> inf`. Unbounded ->
HORN K. (`W87` T2, analytic = numeric to `1e-14`.)

**Derivation D2 (definitizability at the Reuter FP).** `f_2^2* = 0 => m2^2 = 0 =>` massive-massless pole
collision (defective Jordan) `=> lambda_min(eta_+) -> 0 =>` non-definitizable -> HORN K. (`W87` T4,
independent of D1.)

**They agree**, and they are genuinely independent (one is the trajectory approach, the other is the
endpoint spectrum).

**Self-critical pass (adversary, both horns).**
- *Adversary presses HORN Q: "the AS Reuter FP still has finite couplings, so `||C||` is bounded -- W84
  wrongly used AF geometry."* **Premise-falsified:** W83's Reuter FP has `f_2^2* = 0`, not finite; the
  finite couplings are `(g, lambda, f_0^2)`, none of which sets the spin-2 ghost mass. The one that does,
  `f_2^2`, is asymptotically free. (`W87` T1.)
- *Adversary presses HORN K: "bounded `||C||` at the FP does not mean bounded along the trajectory."* On
  the AS branch this **strengthens** HORN K: the FP is **on** the locus and the trajectory approaches it
  monotonically -- there is no bounded interior. (`W87` T2, T4.)
- *Adversary presses the negative conformal ratio (`f_0^2/f_2^2 < 0`, W53 §4) as a "different exceptional
  locus" -> HORN K by another route.* Consistent with HORN K, but note the **selected** branch resolves
  the spin-0 sign the *other* way: W83 selects `f_0^2 > 0` (non-tachyonic) at the Reuter FP, so the spin-0
  sector is **not** on the tachyonic (PT-broken) locus on the AS branch. So on the AS branch the HORN-K
  determination rests on the **spin-2** locus (`f_2^2 -> 0`), not the spin-0 one -- a cleaner basis than
  W53's AF spin-0 worry.

**The single load-bearing assumption + construction-fork (named, not defaulted).** That **`beta_{f_2^2}`
is `g`-independent (a pure Weyl-quartic AF running), so `f_2^2* = 0` at the Reuter FP.**
- *repo-native construction* (W53/W83 agravity convention; standard one-loop AF, Fradkin-Tseytlin /
  Avramidi-Barvinsky; BMS marginal-irrelevance): `f_2^2* = 0 => m2^2 -> 0 =>` **HORN K**. This is what
  GU's own computation gives.
- *standard-AS-field construction* (a full FRG where graviton `(g, lambda)` loops **feed** `beta_{f_2^2}`
  and lift `f_2^2* > 0`, BMS-type non-Gaussian higher-derivative FP): `m2^2*` finite, bounded away from
  the pole `=> ||C||` bounded `=>` **HORN Q**. This is the geometry the orchestrator's hypothesis assumed;
  it is **logically possible but not realized in W83**.

**The deciding computation (names what would flip the horn).** Compute the **full FRG `beta_{f_2^2}` with
graviton `(g, lambda)` loop contributions at the Reuter FP** and determine the **sign/value of `f_2^2*`**:
`f_2^2* = 0` (robust one-loop AF) `=>` HORN K; `f_2^2* > 0` `=>` HORN Q. Equivalently: does the massive
spin-2 ghost mass stay bounded away from the massless pole at the Reuter FP? Robust one-loop AF and the
BMS marginal-irrelevance both say `f_2^2 -> 0` (HORN K); only a truncation that lifts `f_2^2*` would give
HORN Q.

---

## 5. Confidence grade and what would move it

- **HORN-Q premise falsified on the repo (`f_2^2* = 0` at the Reuter FP):** **HIGH** -- direct from W83
  §1.1/§1.3 (FP value + marginal-irrelevance eigenvalue).
- **`f_2^2 -> 0` on the AS branch (`beta_{f_2^2}` `g`-independent):** **HIGH within the truncation** --
  the standard AF result (Fradkin-Tseytlin; Avramidi-Barvinsky; agravity), and W53's imported `g`-independent
  beta; consistent with BMS marginal-irrelevance.
- **`||C|| -> inf` on the AS branch (D1):** **HIGH** -- exact closed form, analytic = numeric to `1e-14`.
- **`Delta` non-definitizable at the Reuter-FP spectrum (D2):** **HIGH** -- `f_2^2* = 0` is a defective
  Jordan pole-collision; `lambda_min(eta_+) = 0` exactly.
- **VERDICT = HORN K on the AS branch:** **HIGH within the operative truncation; MEDIUM unconditionally**
  -- genuinely gated by the named truncation assumption (`f_2^2*` could be lifted `> 0` by graviton loops).
- **The honest opposite-pull consequence (GU not trivially ghost-free; observer firewall genuine but
  modular-walled):** **MEDIUM-HIGH** -- it follows directly from HORN K + arXiv:2606.13251 + W84, but
  inherits the truncation-conditionality of the horn.

**What would move it most.** (a) The deciding computation: a **full FRG `beta_{f_2^2}` with graviton loops
at the Reuter FP** for GU's exact `(N_S, N_D, N_V, N_RS)` content -- `f_2^2* = 0` confirms HORN K,
`f_2^2* > 0` flips to HORN Q. This is the single computation that settles the fork. (b) An infinite-rank /
type-III Krein conjugation theorem under uniform boundedness -- would conditionally close HORN Q's TT leg
if the horn ever flipped. (c) A definitizability criterion for the region algebra's `Delta` at infinite
rank -- would convert D2 from a spectrum-at-the-FP statement into a decidable test along the trajectory.

---

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action; all citations are read-only literature. The conjecture remains a conjecture; H61/H61a remain
**OPEN**. The deliverable is: the horn determination **redone on the selected AS branch** (not borrowed
from AF); the falsification of the HORN-Q premise by GU's own W83 data (`f_2^2* = 0`, marginally
irrelevant); the two agreeing derivations (D1 `||C||`-on-AS unbounded; D2 Reuter-FP-spectrum
non-definitizable) landing **HORN K**; the honest opposite-pull consequence (GU not trivially ghost-free;
observer firewall genuine but physical modular realization walled at type-III definitizability); and the
single load-bearing assumption + construction-fork (`beta_{f_2^2}` `g`-independent / `f_2^2* = 0`, with
the deciding computation named). Reproducible: `tests/W87_horn_k_vs_q.py` (6/6, exit 0).

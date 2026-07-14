---
artifact_type: exploration
status: exploration (W171 / TEAM RG-POSITIVITY; 5 personas inline; one deterministic test, 17/17, exit 0)
created: 2026-07-14
hypothesis: H59
branch: "W171 -- RG / asymptotic-safety positivity: does the RG structure DECIDE whether the Krein grading is OPERATIVE ([P_ghost,S]=0 at loop level = the interacting C-operator exists), or leave it open? Concretely: is finite-scale RG-stability of the grading = the C-operator existing at every physical scale = OPERATIVE?"
title: "W171 VERDICT: UV-MARGINAL-NARROWED. The equation the task asked to push -- finite-scale RG-stability of the grading = C-operator existence = OPERATIVE -- is FALSE as an equality, and the reason is exact, not truncation-bounded. RG-stability (W53/W119) establishes only that the grading is WELL-DEFINED (eta = P+ - P- exists, m2^2 = f_2^2 M_Pl^2/2 > 0, strictly OFF branch-E's Jordan locus) at every finite scale; it is NECESSARY for OPERATIVE. But OPERATIVE = [P_ghost,S] = 0 = B := P- S P+ = 0 is a SEPARATE condition, and W132's exact identity A^dag A = P+ + B^dag B with computed-nonzero odd cuts proves the FREE grading is NOT operative at finite coupling. The two statements are demonstrably distinct: a machine-checked Krein toy exhibits a grading that is well-defined (eta_+ = e^{-Q} positive-definite, off the locus) yet has B != 0 (physical row-sum 1.0144 > 1, W132 anti-damping) at the same finite coupling. What the RG structure DOES supply is a genuine narrowing: the ONLY surviving positivity sense (W132) is the interacting C-metric eta_+ = e^{-Q}, which is POSITIVE at every finite coupling in the toy (C-sense OPERATIVE survives the whole interacting flow), and asymptotic freedom drives the C-operator toward the free grading (||C - eta|| ~ ||B|| ~ f_2^2(t) -> 0) so that OPERATIVE-of-the-free-grading is reached ONLY at the free UV endpoint -- exactly W53's BOUNDARY, now read on the C-operator rather than the mass. The obstruction to OPERATIVE is thereby pushed entirely into the UV limit: either localization of the C-generator Q (which W54 forbids: no LOCAL positive metric exists) or the free-endpoint pinch (ghost decouples, B -> 0 trivially but the theory is free). A finite-dimensional toy has no locality notion and CANNOT decide the QFT admissibility (non-locality) of eta_+, so the verdict is NARROWED, not OPERATIVE-AT-FINITE-SCALE and not UNDECIDABLE. Effect on bar (b): UNCHANGED (W48 gate: no loop amplitude computed; the decidable object remains the finite-scale QFT C-operator construction, not any flow quantity). H59 remains OPEN."
grade: "DERIVED-on-PORTED / EXACT-toy, exploration-grade. EXACT: the (WD) vs (OP) distinction is two lines of algebra from W132's A^dag A = P+ + B^dag B (machine-verified 1e-15); the C-operator construction eta_+ = e^{-Q}, C = eta e^{-Q}, C^2 = 1, [C,S] = 0, S^dag eta_+ S = eta_+ (all verified 1e-15 on a 2+2 Krein toy). PORTED (cited, not re-derived): the W45 BetaSystem betas (b_2 = 14.71667, imported live), reproducing W53 grading RG-stability (f_2^2 > 0 at every finite t, RK4 vs analytic 1/f2 leading-log to rel_err 1.5e-15) and the W46/W119 negative fixed-ratio (r* = -0.0848, -23.5752, real and negative, Vieta-confirmed). STRUCTURAL (argued, standard): the lift of the toy's (WD)/(OP)/C-metric statements to QFT rests on W132 (fixed-order Fock grading + pseudo-unitarity) and the W54 non-locality theorem, both inherited. Test tests/W171_rg_positivity_flow.py: 17/17, exit 0, with 3 positive controls (AF, grading stability, negative ratio) and 4 negative controls (normal-sign, free endpoint, strong-coupling non-locality, Jordan-locus blow-up). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/path2-wave2-target1-af-flow-vs-exceptional-locus-2026-07-11.md
  - explorations/h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - explorations/H59-krein-loop-positivity-gate-2026-07-12.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W53_path2_target1_af_vs_locus.py
  - tests/W119_h59_frg_krein_negative_ratio.py
  - tests/W132_graded_optical_theorem_physical_subspace.py
  - tests/W48_H59_krein_loop_positivity_gate.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W171_rg_positivity_flow.py
external_refs:
  - "Salvio & Strumia, Agravity, JHEP 06 (2014) 080, arXiv:1403.4226 -- ghost-mass convention m2^2 = f_2^2 M_Pl^2 / 2"
  - "Fradkin & Tseytlin, NPB 201 (1982) 469; Avramidi & Barvinsky, PLB 159 (1985) 269 -- one-loop AF of the Weyl coupling (b_2 = 133/10 + matter)"
  - "Mostafazadeh, Pseudo-Hermiticity versus PT-symmetry, JMP 43 (2002) 205 -- eta_+ = eta C from the C-operator; the metric operator"
  - "Bender, Brody & Jones, Complex extension of quantum mechanics, PRL 89 (2002) 270401 -- the C-operator construction"
  - "'t Hooft & Veltman, Diagrammar, CERN 73-9 -- largest-time equation, pseudo-unitarity diagram by diagram"
---

# W171 -- RG / asymptotic-safety positivity: is finite-scale grading RG-stability = OPERATIVE?

**Role.** The H59 North Star is one object: is the Krein grading **OPERATIVE** = `[P_ghost, S] = 0` at
loop level = the interacting C-operator exists? OPERATIVE -> bar (b) clears; NOT -> the grading is
re-posed as the record-accretion engine. This team attacks it from the **RG / asymptotic-safety**
side. The repo established (W119, W57-W60, W44-W47) that GU's 4th-order sector is renormalizable and
asymptotically free with a negative fixed-ratio `f_0^2/f_2^2 < 0`, "the single point where flow and
positivity touch"; W132/W53 established that the spin-2 grading is RG-stable at all finite scales,
touching the exceptional/Jordan locus only at the free UV fixed point. The mandated question:
**does finite-scale RG-stability of the grading = the C-operator existing at every physical scale =
OPERATIVE?** Five personas ran inline; one deterministic test `tests/W171_rg_positivity_flow.py`
(17/17, exit 0) carries every load-bearing number, with positive controls reproducing the W119 AF
fixed points and W53 grading RG-stability and 4 negative controls.

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **"grading RG-stable"** | (WD) grading WELL-DEFINED: `eta = P+ - P-` exists, `m2^2 > 0`, off the Jordan locus; (OP) grading OPERATIVE: `[P_ghost,S]=0`, `B := P- S P+ = 0` | **Both named and separated** -- this separation IS the result |
| **The ghost** | keep-and-grade (Krein real-mass state, the mandate) | kept; the removal exit named, not defended |
| **Ghost mass** | agravity `m2^2 = f_2^2 M_Pl^2/2` (rides the coupling, W53) | used for the finite-scale flow readout (the standard convention; fixed-scale GU-native branch = W119's STAYS-CLEAR alternative, cited) |
| **Positivity object** | the interacting C-metric `eta_+ = eta C > 0` (Mostafazadeh) | the only survivor per W132; its finite-scale existence is the object computed |

## 1. Persona 1 -- FRG / asymptotic-safety specialist: reuse the AF machinery, restate what it proves

The imported `W45.BetaSystem` gives `b_2 = 133/10 + c_RS = 14.71667 > 0`, so
`beta_{f_2^2} = -kappa b_2 f_2^4 < 0`: `f_2^2` is asymptotically free, `1/f_2^2(t) = 1/f_2^2(0) + kappa b_2 t`,
strictly positive at every finite `t`, `-> 0` only as `t = ln mu -> infinity` (PC1, PC2; RK4 vs analytic
agree to `rel_err = 1.5e-15`). The UV-complete trajectory sits at the **negative fixed-ratio**
`r* = f_0^2/f_2^2 = -0.0848, -23.5752` (both roots real and negative; Vieta product `> 0`, sum `< 0`;
PC3, reproducing W46/W119 to the quoted digits). This is exactly the "single point where flow and
positivity touch."

**What the flow proves, stated precisely.** W53 (BOUNDARY) and W119 (SURVIVES) proved that the
positivity-defining grading is **RG-stable at every finite scale**: `d_locus = m2^2/M_Pl^2 = f_2^2/2 > 0`
for all finite `t`, forced by threshold positivity plus `b_2 > 0`, touching the Jordan locus `m2^2 = 0`
only at the free UV Gaussian fixed point. The specialist's honest claim is therefore narrow and exact:
**the grading is WELL-DEFINED (WD) at every finite scale**. That is the whole flow-side content.

## 2. Persona 2 -- Krein / PT specialist: (WD) is NOT (OP), and the gap is exact

The C-operator condition is `[P_ghost, S] = 0`. W132 gives the exact operator identity: for any
Krein-pseudo-unitary `S` (`S^dag eta S = eta`), with `A = P+ S P+` and `B = P- S P+`,

    A^dag A = P+ + B^dag B     (exact, all orders; C3a, verified 1e-15).

So **OPERATIVE `<=> B = 0 <=>` the odd-ghost sector decouples**. W132 also computed that `B != 0` (the
odd cuts are nonzero at one loop, sunset, and the overlapping kite), and the physical row-sum exceeds 1
(anti-damping, probability EXCESS). Therefore:

> **Being WELL-DEFINED (m2^2 > 0, off the Jordan locus) does NOT imply being OPERATIVE.** The Jordan
> locus is where the grading operator `eta_+` *degenerates* (loses positivity/rank). Staying off it keeps
> `eta` a good operator -- necessary. OPERATIVE is the *separate* demand that `S` **commute** with the
> grading, which W132 shows fails for the FREE grading at finite coupling.

The toy makes this concrete at a single finite coupling (C1-C3b): a pseudo-unitary `S` on a `2+2` Krein
space with `eta = diag(+,+,-,-)` well-defined (spectrum `{+-1}`, off the locus, C2) has `||B|| = 0.207`
and physical row-sum `1.0144 > 1` (C3b). Well-defined grading, not operative -- **at the same scale**.
This is not a truncation artifact; it is two lines of algebra plus a computed nonzero `B`.

## 3. Persona 3 -- higher-derivative-gravity RG specialist: the C-positivity flow, read on the C-operator

The one positivity sense W132 leaves alive is **C-metric unitarity on the full Krein space**:
`S^dag eta_+ S = eta_+` with `eta_+ = eta C > 0`, `C^2 = 1`, `[C, S] = 0`. The interacting C-operator is a
**coupling-dressed grading**, distinct from the free `eta`. The toy constructs it exactly
(`S = e^{Q/2} e^{ih} e^{-Q/2}`, `Q` Hermitian and `eta`-odd = the ghost/non-ghost mixing, `h` `eta`-even):
the invariant metric is `eta_+ = e^{-Q}`, positive-definite for every finite `Q` (C4a, min eig `0.50`),
with `S^dag eta_+ S = eta_+` and `C = eta e^{-Q}`, `C^2 = 1`, `[C,S] = 0` all verified to `1e-15`
(C4b, C4c). **So the C-sense grading is OPERATIVE at finite coupling in the toy.**

Now put it on the flow. Setting the toy's coupling to the actual AF trajectory `q = f_2^2(t)` (Section 4
of the test) gives:

| scale `t` | `f_2^2(t) = q` | `||B||` (free not operative) | `||C - eta||` (C-metric non-locality) | min eig `eta_+` |
|---:|---:|---:|---:|---:|
| 0 | 8.00e-1 | 2.84e-1 | 1.668 | 0.397 |
| 40 | 2.01e-1 | 6.67e-2 | 0.344 | 0.793 |
| 400 | 2.60e-2 | 8.58e-3 | 4.38e-2 | 0.971 |
| 2000 | 5.33e-3 | 1.76e-3 | 8.99e-3 | 0.994 |
| 4000 | 2.67e-3 | 8.84e-4 | 4.51e-3 | 0.997 |

Two things move together as AF drives `q -> 0` in the UV (C5a, both monotone): `||B||` (how far the free
grading is from operative) and `||C - eta||` (how far the C-operator is from the free grading) **both
shrink to 0**. The free grading becomes operative **only at the free UV endpoint** -- exactly W53's
BOUNDARY, now read on the C-operator instead of the ghost mass. Yet at **every finite scale** `eta_+`
stays strictly positive (C5b): the C-sense grading is operative all the way up the interacting flow; it
is only the *identification of C with the free grading* that is a UV-endpoint (free-theory) event.

## 4. Persona 4 -- symbolic engineer: the reproducible system and its controls

`tests/W171_rg_positivity_flow.py`, 17/17, exit 0 (numpy + imports W45). Positive controls: PC1 AF
(`b_2 = 14.717 > 0`); PC2 W53 grading RG-stability (RK4 vs analytic `1/f2` law, `rel_err 1.5e-15`);
PC3 W46/W119 negative fixed-ratio (`r* = -0.0848, -23.5752`, Vieta-confirmed). Core: C1 pseudo-unitarity;
C2 (WD); C3 W132 identity + free-grading non-operativeness; C4 the C-operator exists and is positive at
finite coupling; C5 the RG-narrowing table. Negative controls: **NC1** normal-sign theory (`eta = I`, no
ghost -> `S` unitary, no anti-damping: the effect tracks the Krein sign, not genericity); **NC2** free
endpoint (`Q = 0` -> `B = 0`, `C = eta`, operative *trivially* because the theory is free -- the W53
free-FP touch); **NC3** strong coupling (`eta_+` stays positive but `||C - eta|| = 30.9` grows unbounded
-- the toy has no locality obstruction); **NC4** Jordan-locus limit (`cond(eta_+) = 1e9` as
`lambda_min -> 0`, E repair-4c blow-up). Every load-bearing number has two routes or a matched control.

## 5. Persona 5 -- adversarial skeptic: steelman UV-MARGINAL-KILLS-IT

**The steelman, at strength.** The free-UV-FP touch is exactly where the ghost mass `-> 0` (W53 pinch)
AND where the free grading would become operative. Everywhere *below* it the free grading is provably NOT
operative (`B != 0`, exact). So the interacting theory is never operative on the free grading, and its
UV completion sits on the locus: **there is no scale at which the theory is both interacting and
free-grading-operative-with-positivity**. If "OPERATIVE" means the *free* grading commutes with the
interacting `S`, the answer is flatly NO at every physical (interacting) scale, and only-marginally-yes
at the free endpoint where there is nothing to grade. That kills OPERATIVE-of-the-free-grading outright.

**Where it lands, honestly.** The steelman is correct *about the free grading* and is fully conceded:
free-grading OPERATIVE is dead at finite coupling (that is just W132, restated). It does **not** kill the
**C-metric** OPERATIVE: the toy shows `eta_+ = e^{-Q} > 0` and `S^dag eta_+ S = eta_+` at every finite
coupling, so the interacting theory *is* exactly unitary in the C inner product at finite scale -- **if**
`eta_+` is admissible. The single load-bearing gap is admissibility: in QFT the C-generator `Q` carries
`1/sqrt(k^2+m^2)` energy denominators (branch B: C exists order-by-order in QM), and W54 proves **no
LOCAL positive metric exists**. NC3 is the toy's mirror of this: positivity survives, but the operator
becomes unboundedly non-local, and a finite-dimensional toy **cannot** decide whether that non-locality
is admissible. So the steelman narrows the claim -- from "OPERATIVE" to "C-metric OPERATIVE conditional
on a non-local-but-finite-range `eta_+`" -- without killing it. **NARROWED, not killed.**

## 6. Verdict

**UV-MARGINAL-NARROWED.**

- **Is finite-scale grading RG-stability = C-operator existence = OPERATIVE?** **NO -- the equality is
  FALSE, exactly.** RG-stability (W53/W119) gives only (WD) *grading well-defined*, which is **necessary**
  for OPERATIVE. OPERATIVE = `[P_ghost,S] = 0` = `B = 0` is a **separate** condition that W132 proves
  **fails** for the free grading at finite coupling (`A^dag A = P+ + B^dag B`, `B != 0`, exhibited in the
  toy at a well-defined off-locus grading: `||B|| = 0.207`, row-sum `1.0144 > 1`).

- **The C-positivity flow result at the negative fixed-ratio.** The only surviving positivity sense
  (W132) is the interacting C-metric `eta_+ = e^{-Q}`, and it is **positive-definite at every finite
  scale** in the toy along the AF trajectory (`min eig eta_+` from 0.40 at `t=0` to 0.997 at `t=4000`);
  **C-sense OPERATIVE survives the entire interacting flow.** Asymptotic freedom drives
  `||C - eta|| ~ ||B|| ~ f_2^2(t) -> 0`, so the free grading becomes operative **only at the free UV
  endpoint** (W53's BOUNDARY, re-read on the C-operator). The obstruction to OPERATIVE is thereby
  **narrowed to the UV limit**: localization of `Q` (W54-forbidden) or the free-endpoint pinch (ghost
  decouples, trivial).

- **Does finite-scale grading RG-stability = C-operator existence?** Not equal, but strongly
  **suggestive**: RG-stability is necessary and, combined with branch-B (order-by-order C in QM) and the
  observation that the W54 obstruction is **non-locality, not non-existence** (bounded at any finite
  cutoff, range `~1/k`), it makes a **finite-scale (non-local, effective-theory) C-operator PLAUSIBLE**.
  The finite-dimensional toy cannot upgrade plausible to proven, because it has no locality notion.

- **Effect on bar (b): UNCHANGED.** The flow side is necessary context, insufficient (W48 gate). No loop
  amplitude computed; the decidable object for H59 remains the finite-scale QFT C-operator construction
  (whether `eta_+`'s non-locality is admissible), **not** any flow quantity. H59 remains **OPEN**.

**Net reading for the orchestrator.** The RG structure does **not** decide OPERATIVE, and -- importantly
-- it decides the *wrong* thing if one is not careful: it robustly establishes the grading is
**well-defined** at every finite scale, which is easy to mis-read as OPERATIVE but is only necessary for
it. The honest positive is a *narrowing*: the whole OPERATIVE question is pushed off the finite-scale
interacting flow (where the C-metric is positive) and onto (i) the UV limit's localization demand
(W54) and (ii) the finite-scale QFT admissibility of a non-local `eta_+` -- the same `[P_ghost,S]=0`
loop-level object the W48 gate names. Convergence with the concurrent C-operator-perturbative team
(W169) is the natural next cross-check.

## What this does NOT do

No loop amplitude computed; no QFT C-operator constructed (the toy is finite-dimensional and cannot
settle the W54 non-locality question -- stated as the load-bearing gap). No claim that the free grading
is operative at any interacting scale (it is not; W132). No claim that the C-metric is admissible in QFT
(open). No resolution of the spin-0 conformal-mode sign (W78, unchanged). No canon / RESEARCH-STATUS /
claim-status / verdict / posture change. **H59 remains OPEN.**

**Artifacts:** this file + `tests/W171_rg_positivity_flow.py` (17/17, exit 0).

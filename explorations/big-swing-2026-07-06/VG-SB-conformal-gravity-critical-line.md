---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "VG-SB: the conformal-gravity critical line, pinned to primary sources — the lensing-sign kill did NOT already fire (it is definition-contested, Rindler-Ishak reverses it), Yoon vs Mannheim is a published standoff, and the strongest standing objection is the Horne/Hobson-Lasenby frame line (frame-INDEPENDENT no-flat-curves claim, stronger than the from-memory version), answered only by Sultana-Kazanas in a way that undercuts the fits themselves; SKY' adjudicated CONTESTED, not dead, not clean"
grade: "INTAKE_VERIFIED (rung 0 source intake; abstract/search granularity, not full-text audit). No mathematics graded — this route produces citation corrections and a dispute-state adjudication, not a computation. Verdict for federation bookkeeping: SKY' observational surface = CONTESTED-ADVERSE (three independent objection lines, none community-adjudicated, the frame line unanswered in print by Mannheim as of this search)."
depends_on:
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - explorations/big-swing-2026-07-06/CROSS-EXAM-weinstein-turok-mannheim-first-principles.md
  - explorations/generation-sector/mannheim-conformal-gravity-source-action-intake-2026-07-06.md
scripts: none (source-intake route; no numeric claim in this doc originates from a computation of ours — every number is a quoted literature value with its source pinned below)
---

# VG-SB: the conformal-gravity critical line (rung 0 source intake)

Executes the SKY' standing order from the 2026-07-06 all-persona review, Section 5.3 Tier 4:
"primary-source intake (Mannheim papers + the critical line: Edery-Paranjape, Yoon,
Hobson-Lasenby; from-memory citations to be verified) BEFORE any sky-facing claim."
This doc adjudicates whether the federation's SKY' surface is already dead, contested, or open.
It affects kill-condition bookkeeping only; per Section 6.2 of the persona doc, adverse sky
outcomes kill the OBSERVATIONAL surface, never the mathematical federation (T1'-T12').

Method honesty: intake was done via web search + page/abstract fetches on 2026-07-06. That is
abstract-and-summary granularity, not a full-text equation-by-equation audit. Where a claim
rests on a fetched summary rather than a directly quoted abstract sentence, it is marked
(summary-level). Full-text audit of Edery-Paranjape Section 3 and Hobson-Lasenby Sections 4-6
remains open work.

## 1. Citations pinned (from-memory IDs corrected)

| paper | from-memory guess in prompt/docs | actual, verified |
|---|---|---|
| Edery & Paranjape, "Classical tests for Weyl gravity: deflection of light and time delay" | "likely gr-qc/9708007" | **astro-ph/9708233**, Phys. Rev. D 58, 024011 (1998) |
| Yoon, "Problems with Mannheim's conformal gravity program" | "arXiv ~1305.xxxx, PRD 2013" | **arXiv:1305.0163**, Phys. Rev. D 88, 027504 (2013) |
| Mannheim, Comment on "Problems with Mannheim's conformal gravity program" | "arXiv ~1506.xxxxx" | **arXiv:1506.02479**, Phys. Rev. D 93, 068501 (2016) |
| Hobson & Lasenby, "Conformal gravity does not predict flat galaxy rotation curves" | "arXiv ~2103.xxxxx or 2110.xxxxx" | **arXiv:2103.13451**, Phys. Rev. D 104, 064014 (2021) |
| Hobson & Lasenby follow-up, "Conformally-rescaled Schwarzschild metrics do not predict flat galaxy rotation curves" | not in docs | **arXiv:2206.08097**, Eur. Phys. J. C 82 (2022) |
| Horne, "Conformal Gravity Rotation Curves with a Conformal Higgs Halo" | not in docs (precursor to the frame line) | **arXiv:1601.07537**, MNRAS (2016) |
| Sultana & Kazanas, "Bending of light in conformal Weyl gravity" | not in docs | Phys. Rev. D 81, 127502 (2010) |
| Cattani, Scalia, Laserra, Bochicchio, Nandi, "Correct light deflection in Weyl conformal gravity" | not in docs | **arXiv:1303.7438**, Phys. Rev. D 87, 047503 (2013) |
| Sultana & Kazanas, "Gauge Choice in Conformal Gravity" (reply to Horne) | not in docs | **arXiv:1701.03192** (2017) |
| Mannheim & O'Brien, "Fitting galactic rotation curves with conformal gravity and a global quadratic potential" | repo intake had this as 1011.3495 | **arXiv:1011.3495**, Phys. Rev. D 85, 124020 (2012) — confirmed |
| Mannheim, "Curvature and Cosmic Repulsion" (q0 source) | q0 ~ -0.37 "from memory" | **astro-ph/9803135**: "the conformal cosmology fits the supernova data with q0 = -0.37" — confirmed |

## 2. The lensing-sign result, exactly (Edery-Paranjape and its counter-line)

**Edery-Paranjape 1998 (astro-ph/9708233 abstract, direct):** in the Mannheim-Kazanas static
spherically symmetric exterior, the light deflection is the Einstein term 4GM/r0 plus an extra
term **-gamma * r0**, where r0 is the radius of closest approach. The extra term GROWS with
impact parameter, so it dominates at galactic scales and beyond. A **negative** gamma would
increase deflection at large scales and imitate dark matter in lensing; but the sign needed for
that is **opposite** to the gamma > 0 used to fit galactic rotation curves. They note
|gamma| is of order the inverse Hubble length. Assumption baked in: the bending angle is
computed with the formalism appropriate to **asymptotically flat** spacetimes, applied to a
metric that is not asymptotically flat (the gamma*r and quadratic terms diverge).

Two corrections to the federation docs' from-memory version (persona doc Section 4.6):

- The from-memory phrase "deflection ~ -(gamma)r/2" has the right sign and structure but the
  wrong coefficient: the E-P abstract states **-gamma * r0** (coefficient 1, not 1/2). The 1/2
  belongs to the potential term V ~ +gamma c^2 r / 2, not the deflection.
- The claim "the lensing sign is not a pending kill switch — it already fired" is
  **overstated**. It fired only under the asymptotically-flat definition of bending angle.
  The counter-line:
  - **Sultana & Kazanas 2010** (PRD 81, 127502): redo the bending calculation with the
    **Rindler-Ishak method** (the definition of bending angle appropriate to
    non-asymptotically-flat spacetimes, developed for Schwarzschild-de Sitter). Result: the
    effects of the gamma*r term become **insignificant**, and the discrepancy with E-P is
    attributed entirely to the definition of the bending angle between asymptotically flat and
    non-flat spaces (summary-level, consistent across two independent search results).
  - **Cattani et al. 2013** (PRD 87, 047503, "Correct light deflection in Weyl conformal
    gravity"): states the tension exactly as the federation docs do — rotation curves need
    gamma > 0, the conventional method gives a negative lensing contribution for gamma > 0,
    contrary to observation — and then shows the **Rindler-Ishak method gives a POSITIVE
    contribution to the Schwarzschild deflection for gamma > 0, as desired** (summary-level).

So the honest state of the lensing sign: **definition-contested for ~28 years** (not "~25",
minor). Under one angle definition the sign is adverse; under the definition arguably better
suited to the non-asymptotically-flat MK exterior it is neutral-to-favorable. Neither camp's
definition has been community-adjudicated as THE observable for real lensing data reduction.
A kill condition that fires or unfires depending on an unresolved definitional choice has not
fired.

One structural note (standard result, flagged from memory): **null geodesics are conformally
invariant**, so the photon trajectory itself is frame-independent even in conformal gravity;
the lensing ambiguity is purely about angle definition in a non-asymptotically-flat exterior,
NOT about conformal frame. This makes lensing the one surface the Section-3 frame objection
below does not automatically dissolve — but see Section 4: if the linear potential does not
cause rotation curves, nothing fixes gamma > 0, and the lensing-sign question loses its target.

## 3. Yoon's objection and Mannheim's answer (a published standoff)

**Yoon 2013 (arXiv:1305.0163, PRD 88, 027504), abstract-level:** two objections.

1. **Newtonian-limit / source-singularity objection:** the conformal-gravity potential
   (1/r term plus r term) does **not reduce to Newtonian gravity at short distances** unless
   one assumes "undesirable singularities" in the mass density of the proton (the microscopic
   source). Consequence: terrestrial Cavendish-type experiments confirming Newton would
   contradict the theory absent those singularities.
2. **Sign objection:** as long as the total mass of the proton is positive, the theory produces
   a **negative** linear potential — while the rotation-curve fits need a **positive** one.

Correction to the federation docs' from-memory version: persona doc 4.6 renders this as "the
fourth-order Poisson integration over extended sources may misassign the Newtonian **limb**" —
"limb" is a garble of "limit", and the emphasis is slightly off: Yoon's objection is about
recovering the Newtonian limit from microscopic sources and about the SIGN of the linear
potential forced by positive source mass, integrated through the fourth-order Poisson equation.
Substance close, wording corrupted.

**Mannheim's answer (arXiv:1506.02479, PRD 93, 068501, 2016), abstract-level:** Yoon's results
hold **only under the assumption that gravitational sources can be treated the same way as in
standard Newton-Einstein gravity**; since that assumption violates the theory's underlying
conformal invariance, the conclusions are invalidated. I.e., in conformal gravity the
microscopic source coupling is constrained by conformal invariance and the coefficients of the
1/r and r terms are independent inputs not tied by the naive positive-density integration.

**Status of this exchange:** Mannheim's Comment is published in PRD; **no published Yoon Reply
was located** (searches for PRD 93, 068502 and "Reply to Comment" returned nothing). So this is
a standoff hinging on one question — may macroscopic gravitational sources be coarse-grained
conventionally, or does conformal invariance forbid it? — that the community has not
adjudicated. Answered-in-print: yes (by Mannheim). Settled: no. Note Yoon's objection is
logically upstream of everything else: if the Newtonian limit is wrong, rotation curves and
lensing are both moot; if Mannheim's source-theory answer works, it must ALSO be deployed
consistently in the rotation-curve fits (which treat stars as N* conventional solar-mass
sources with per-unit-mass gamma* = 5.42e-41 cm^-1 — see Section 5).

## 4. The frame-artifact line (Horne, Hobson-Lasenby) — the strongest standing objection

**Horne 2016 (arXiv:1601.07537, MNRAS), abstract-level — the precursor:** with a conformally
coupled Higgs field, consistency requires the scalar profile S(r) = S0 * a/(r+a), and the
required conformal stretching of the MK metric **exactly cancels the linear potential** that
was invoked to fit rotation curves without dark matter.

**Hobson-Lasenby 2021 (arXiv:2103.13451, PRD 104, 064014), abstract + summary-level:** the
stronger, frame-INDEPENDENT version. Massive particles cannot just be assigned fixed rest mass
in the MK frame: in conformal gravity mass is generated dynamically by the scalar field, and
geodesics are not conformally invariant, so "test particles follow MK timelike geodesics" is an
assumption, not a result. Working with physically measurable quantities, they conclude that **in
both the MK frame and the Einstein frame — indeed in any conformal frame — ordinary matter
follows timelike geodesics of the Schwarzschild-de Sitter metric**, which has **no flat
rotation-curve region**. The apparent frame dependence is resolved, against Mannheim. Their
abstract also notes this clarifies the lensing uncertainties of Section 2 (if the linear
potential is not physical for matter dynamics, nothing in the rotation curves fixes gamma > 0).
**Follow-up 2022 (arXiv:2206.08097, EPJC 82):** generalizes beyond static spherical symmetry to
conformally invariant theories on Weyl-Cartan spacetimes; same conclusion.

Correction to the federation docs' from-memory version: persona doc 4.6 has "a frame exists
where the linear potential vanishes — the fitted gamma may be a frame artifact". The actual
claim is **stronger**: not "a frame exists" but "in EVERY frame the physical trajectories are
SdS geodesics"; Hobson-Lasenby explicitly claim frame-INDEPENDENCE of the negative verdict, so
"frame artifact" understates — their claim is that the flat-curve prediction was an artifact of
an inconsistent matter coupling (fixed mass in the MK frame), not of frame choice per se.

**Replies located:**

- **Sultana & Kazanas 2017 (arXiv:1701.03192)** reply to Horne (summary-level): (a) metric
  representations without the linear term were already exhibited by Mannheim and Kazanas
  themselves, no Higgs field needed; (b) the sign of the gamma*r term can be reversed by a gauge
  transformation, and **"the effects of this term are indeed too small to be observed"**. Note
  what (b) concedes: if the gamma*r term's effects are too small to observe, it cannot be what
  flattens rotation curves — a defense of the geometry that undercuts the phenomenology. This
  internal-camp tension is itself evidence the linear-potential phenomenology is not on solid
  ground even among conformal-gravity proponents.
- **Mannheim reply to Hobson-Lasenby: NOT LOCATED.** Multiple targeted searches (2022-2026
  windows) found no published or arXiv rebuttal by Mannheim to 2103.13451 or 2206.08097; the
  search trail shows only that Hobson-Lasenby acknowledge Mannheim commented on a draft.
  Recorded as "not located as of 2026-07-06", not "does not exist". Any Mannheim counter would
  have to dispute the mass-generation premise (how fermion masses arise from the scalar), which
  is exactly the T5'/condensate territory the federation cares about.

## 5. Mannheim's own fit practice (for the one-condensate lock design)

From arXiv:1011.3495 (PRD 85, 124020), full formula verified via ar5iv (summary-level but
formula-explicit):

v_TOT^2 -> N* beta* c^2 / R + N* gamma* c^2 R / 2 + gamma0 c^2 R / 2 - kappa c^2 R^2

with beta* = 1.48e5 cm (solar Schwarzschild), **gamma* = 5.42e-41 cm^-1 per solar mass**
(local, scales with N*), **gamma0 = 3.06e-30 cm^-1 universal**, **kappa = 9.54e-54 cm^-2
universal** (~(100 Mpc)^-2, fixed from the 21 most extended galaxies, then applied to all).
111 spiral galaxies; only mass-to-light ratios free. And astro-ph/9803135: **q0 = -0.37**
from the conformal-cosmology fit to type Ia supernovae — confirmed exactly as remembered.

Correction to persona doc 4.6: "gamma decomposed per-unit-mass plus **per-cluster kappa**" is
half right. The gamma = N*gamma* + gamma0 decomposition is real (and is itself a lock-relevant
fact: gamma is NOT one universal constant across systems — it grows with enclosed mass). But in
the rotation-curve papers **kappa is fitted as a single universal constant, not per-cluster**.
If a per-system kappa appears anywhere it is in cluster applications not verified here; as
written, the claim is wrong for the flagship fits. Note the corrected version still supports
4.6's conclusion, differently: the N*gamma* term means the one-condensate lock's "same gamma in
lensing and rotation curves of the same system" must be stated per-system as
gamma(N*) = gamma0 + N*gamma*, and the lock's cross-scale correlation must target gamma0 (the
cosmological piece) specifically.

## 6. The honest state of the dispute (adjudication)

Three independent objection lines against the SKY-relevant phenomenology, with different
statuses:

| objection | answered in print? | current status |
|---|---|---|
| Lensing sign (E-P 1998): gamma > 0 from rotation curves gives lensing deficit | Yes — Sultana-Kazanas 2010, Cattani et al 2013 (Rindler-Ishak method reverses/neutralizes) | **Contested, definition-dependent.** Not a fired kill. Unresolved which angle definition maps to real lensing observables. |
| Yoon 2013: no Newtonian limit without source singularities; positive mass forces negative gamma | Yes — Mannheim 2016 (PRD Comment): conventional source treatment violates conformal invariance | **Standoff.** No Yoon reply located; no third-party adjudication located. Mannheim's answer creates a consistency obligation for his own fits. |
| Horne 2016 / Hobson-Lasenby 2021-22: linear potential cancels / matter follows SdS geodesics in every frame; no flat curves | Partially — Sultana-Kazanas 2017 answer Horne only, and concede the term's effects are "too small to be observed"; **no Mannheim reply to H-L located** | **STANDS as of this search.** The strongest objection: frame-independent, attacks the fits themselves, and its only in-camp answer undercuts the fits a different way. |

**Verdict for SKY' bookkeeping: CONTESTED, leaning adverse — not already dead, not open.**

- The persona doc's 4.6 claim that the lensing kill "already fired" is **overturned**: rung-0
  intake shows a live 28-year definitional dispute, not a settled adverse result. The
  one-condensate lock's lensing leg is therefore a genuine (if murky) future surface, not a
  pre-fired kill switch.
- But SKY' inherits a worse problem than the one 4.6 priced: the Horne/Hobson-Lasenby line says
  the linear potential is not physical for matter dynamics AT ALL, in any frame. If that holds,
  gamma > 0 was never established by rotation curves, and both halves of the gamma-sign story
  (fits and lensing) lose their subject. The federation's T5' (VEV map / how mass is generated
  by the condensate) is exactly the point H-L attack — so SKY' is gated on T5' twice over:
  once by the persona doc's own demotion, and once because the critical literature's live
  objection is a mass-generation objection.
- No kill-condition number fires from this intake (sky outcomes are bookkept inside SKY' per
  Section 6.2). The bookkeeping update is: SKY' status field moves from "lensing sign arguably
  already adverse; possible frame artifact — all from memory" to "lensing sign
  definition-contested (adverse only under asymptotically-flat angle definition); frame line
  verified, stronger than remembered, unanswered by Mannheim in print; Yoon line a published
  standoff". The mathematical federation (T1'-T12') is untouched, as designed.

## 7. What remains unverified (open intake)

- Full-text audits: E-P's derivation (whether -gamma*r0 has hidden convention choices),
  H-L's Section on the unique MK frame where scalar energy-momentum vanishes, Yoon's
  fourth-order Poisson integration details.
- Whether any Mannheim response to Hobson-Lasenby exists outside the searched channels
  (conference proceedings, book chapters, post-2024 reviews).
- Cluster-scale fitting practice (whether any per-cluster parameter freedom exists in
  Mannheim-camp cluster papers) — the "per-cluster kappa" claim is corrected for galaxies but
  its cluster-side origin was not traced.
- The "quasi-static" descriptor attached to q0 = -0.37 in the federation docs: q0 = -0.37 is
  confirmed, but whether "quasi-static" fairly describes Mannheim's w(z) behavior was not
  verified (one fetched summary called the cosmology evolving; conformal cosmology's
  never-decelerating expansion is confirmed in the GRB-test literature at summary level).
- DESI DR2 evolving-dark-energy preference (3-4 sigma, from memory in persona doc 3.4): out of
  this route's scope, still unverified.
- All (summary-level) tags above: those points rest on fetched page summaries, not directly
  quoted abstract text.

## Sources

- https://arxiv.org/abs/astro-ph/9708233 (Edery-Paranjape, PRD 58, 024011)
- https://arxiv.org/abs/1305.0163 (Yoon, PRD 88, 027504)
- https://arxiv.org/abs/1506.02479 (Mannheim Comment, PRD 93, 068501)
- https://arxiv.org/abs/2103.13451 (Hobson-Lasenby, PRD 104, 064014)
- https://arxiv.org/abs/2206.08097 (Hobson-Lasenby, EPJC 82)
- https://arxiv.org/abs/1601.07537 (Horne, MNRAS)
- https://journals.aps.org/prd/abstract/10.1103/PhysRevD.81.127502 (Sultana-Kazanas 2010)
- https://arxiv.org/abs/1303.7438 (Cattani et al, PRD 87, 047503)
- https://arxiv.org/abs/1701.03192 (Sultana-Kazanas reply to Horne)
- https://ar5iv.labs.arxiv.org/html/1011.3495 (Mannheim-O'Brien, PRD 85, 124020)
- https://arxiv.org/pdf/astro-ph/9803135 (Mannheim, Curvature and Cosmic Repulsion; q0 = -0.37)

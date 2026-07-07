---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "A4 (route A4, basin & stability of the aligned condensate): STABILITY CARD DELIVERED, AND THE ALIGNMENT INVOICE SHRINKS TO ONE COUPLING SIGN. Under every orientation-blind native potential at quartic order the V8 aligned configuration phi*Pi_mirror is an exact SADDLE — Hessian spectrum {-2m^2 x 9216, +4m^2 x 9216} on the full P-even channel space (native slice {-4 x256, +8 x256} printed; block formula random-verified on family-tensor directions), the masslessness of all 96 generations sits at the TOP of the double well in every generation channel, and the global minimum gaps everything (mirror-blind, V1-consistent). But the measured commutant admits exactly ONE more P-even K-self-adjoint quadratic weighting — Q5 itself — and the single orientation-odd native invariant tr(Q5 Phi^2) at coupling h < -m^2 flips the aligned configuration to the GLOBAL MINIMUM (Hessian PD {+8 x256, +32 x256} at h=-6, no zero modes, symmetry-isolated, per-channel proof + 300 random configs): V8's two priced imports (orientation Z2 + alignment hypothesis) MERGE at potential grade — choosing the sign of one native coupling IS choosing which half is physical, and alignment stops being a fine-tuning question. Chi-conjugation flips h (a chi-symmetric potential provably cannot stabilize: saddle or marginal at h = -m^2 with 256 exact zero modes). Misalignment buffer refined: all 510 gap-closing native channels close at eps* = 1/sqrt(2) = 0.7071 exactly; the aligned plane {1, Q5} never closes; random family-tensor directions ~0.36; PROVED worst case at fixed Frobenius budget eps* = 1/(2 sqrt 48) = 0.0722 (split rank-1); V8's iJ+3 numbers reproduced to the digit. [M, P_ghost] = 0 is EXACT across the whole P-even basin at every eps (8.7e-14); only P-odd contamination breaks it, linearly (slope 2.0). The Weyl point IS the aligned configuration at scale 2mu: at the basin bottom with zero tuning iff the Dirac scale is condensate-born (the free 2D native scalar minimum lands exactly there, m_gen = 8.7e-9); one tuning if mu is external — and on the pure-Q5 ray the orientation coupling is INERT (tr Q5 = 0), so alignment dynamics requires the I-component. Masslessness survives A=0 mirror-channel perturbations to ALL orders (4.1e-15 at eps 0.5), degrades linearly under unforbidden tadpoles (gap-suppressed, m_gen = c1/2|m^2+h|, Phi -> -Phi needed for exactness — flagged assumption), quadratically under P-odd (Schur coefficient matched to 0.4%). CARD: saddle / attractor-compatible / marginal, keyed to one native coupling."
grade: "THEOREM (potential-class scope: exact machine-checked statements about the quartic single-trace native invariant ring on the 192-dim (9,5) triplet sector, with the quadratic-weighting classification exhaustive over the measured 4-element commutant {I, P, chi, P.chi} and the Hessian block formula verified on the full 18432-dim P-even space via random family-tensor directions, not only the 512-dim native Clifford slice; the worst-case misalignment threshold is proved at fixed Frobenius budget and confirmed against 24 random directions with none beating it. NOT a dynamics derivation: the Landau-type potential is postulated, not derived from any GU or Mannheim action; quartic order only; sextic and general multi-trace terms unclassified; the tadpole and Phi -> -Phi discussion names its assumption. Anchors reproduced first: rank(Gamma) = 128, ker = 1664, triplet 192, Krein (+96, -96, 0), beta_S residual 0.0e+00, ||Q5 + P|| = 3.7e-14. Target-import guard clean: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, or divided by; all dimensions (96, 192, 256, 512, 9216, 18432) are measured; couplings (m^2=2, lam=1, h=+-6, mu, q, c1) are free potential-class parameters. Controls with power: finite-difference Hessian (418.560594 vs 418.560000), nonzero gradient off criticality (13.99), PD Hessian at the mirror-blind global min (+8 x512 — the machinery is not saddle-rigged), random even weighting destroys criticality (|grad| = 332.6), orientation-flip control lands on the chi-image, V8 misalignment anchor reproduced (+1.000/+0.827/+0.134/-0.732), random threshold floor respected (0.354 >= 0.0722). From-memory items flagged inline: textbook degenerate perturbation theory; Mannheim's conformal ban on bare quadratic couplings."
depends_on:
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-06/VG-V1-condensate-ghost-parity-scan.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-06/VG-SA-mannheim-primary-sources.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
  - canon/ghost-parity-krein-synthesis.md
scripts:
  - tests/big-swing/as_a4_basin_stability.py
---

# A4: basin and stability of the aligned condensate (the stability card)

**Route A4 of the 2026-07-07 alignment swing.** V8 constructed the mirror-hiding direction at
kinematic grade: `phi * Pi_mirror` with `Pi_mirror = (I + Q5)/2 = (I - P_ghost)/2` gaps all 96
mirrors at `m = phi`, keeps all 96 generations exactly massless, `[M, P_ghost] = 0`. Its central
unproven hypothesis is ALIGNMENT — nothing shown yet makes any dynamics flow the condensate INTO
that direction, and V8 measured that misalignment `eps ~ 1` closes the gap. A4 assumes the
aligned configuration and measures its robustness as dynamics-facing kinematics: second
variation, misalignment thresholds, Krein positivity through the basin, and the Weyl point.

Script: `tests/big-swing/as_a4_basin_stability.py` (exit 0; every number below is printed by
it). Carrier machinery reused verbatim from V8; the invariant basis and potential class are
built fresh in this route (deliberately independent — no A1 results imported or read).

## 0. Anchors (reproduced before any claim)

(9,5) carrier, timelike = {4..8}: rank(Gamma) = 128, dim ker = 1664, triplet dim 192, beta_S
pseudo-anti-Hermiticity 0.0e+00, triplet Krein signature **(+96, -96, 0)**, P = sign(K) = K|_W
(3.7e-14), {P, chi} = 0 (5.3e-14), V8's identity ||Q5 + P|| = 3.7e-14, and the frame fact this
route leans on throughout: in the K-eigenbasis the Krein form is exactly ±I on the two blocks,
so the P-even channel space is `E = {diag(A, B) : A, B Hermitian}`, real dim 2·96² = 18432.

## 1. The channel space and the commutant (own construction)

- **Native Clifford slice of E:** all internal Clifford monomials with an even number of
  timelike factors (grammar: P-even), K-self-adjointized. Measured: **512 channels, none
  K-dead, all P-even (1.0e-14), span exactly 512**, chi-grading 256 chi-commuting (E⁺) + 256
  chi-anticommuting (E⁻), closed under Q5-multiplication (8.0e-15), and splitting exactly
  **256 generation-diagonal + 256 mirror-diagonal** directions.
- **Commutant classification (the load-bearing new fact).** The commutant of the native compact
  symmetry (su(2)± family, so(5)_s ⊕ so(5)_t) on W is spanned by {I, P, chi, P·chi} (residuals
  ≤ 1.1e-13). Of these, K-self-adjoint AND P-even: **{I, Q5} only** (chi is K-skew, its K-sa
  phase i·chi is P-odd; P·chi is P-odd). So the most general native-invariant P-even quadratic
  mass term is `tr((-m² + h·Q5) Phi²)` — **exhaustive at quadratic order**. The P-odd
  weightings source exactly the positivity-breaking condensates of V1's odd branch.
- **Symmetry isolation:** [Pi_mirror, every compact native generator] = 0 (4.3e-14) and J_quat
  fixes it (8.8e-14). The aligned configuration has **no Goldstone directions**; any Hessian
  zero mode is a tuning artifact, not a symmetry artifact.
- **Low-order invariant ring (measured):** linear {t1 = tr Phi, s1 = tr(Q5 Phi)}; quadratic
  {t2 = tr Phi², s2 = tr(Q5 Phi²), t2' = tr(chi Phi chi Phi)} — independent (probe value matrix
  rank 3). s2 is odd under chi-conjugation (ratio −1.000) and under orientation flip; it is a
  **pure E⁺/E⁻ cross form** (vanishes on chi-graded probes, ∓96 on block-diagonal probes) —
  exactly V8's |m|-splitting mixer class, now appearing as the alignment-selecting coupling.

## 2. (i) Second variation: saddle without the orientation coupling, global minimum with it

Potential class: `V_h(Phi) = tr((-m² + h Q5) Phi²) + lam tr(Phi⁴)` with m² = 2, lam = 1 (free
parameters; bounded below, so "stable"). Critical point on all of E at `Phi* = phi* Pi_mirror`,
`phi*² = (m² − h)/(2 lam)` (|grad| = 8.2e-14; control: |grad| = 13.99 off criticality).

**h = 0 (the simplest stable orientation-blind potential):**

> **Hessian spectrum (per unit tr X²): −4.000 ×256, +8.000 ×256 — INDEFINITE. The aligned
> point is an exact SADDLE.** Analytic block formula `Hess(X,X) = −2(m²+h)·tr A² + 4(m²−h)·tr B²`
> (A = generation-diagonal block, B = mirror-diagonal block), verified by finite differences
> (418.560594 vs 418.560000) and on random full-E directions — so the verdict covers **all
> 18432 dims of E including the 35 family-tensor cells**, not just the native slice: spectrum
> {−2m² ×9216, +4m² ×9216}.

The negative directions are precisely the generation-diagonal channels: the masslessness of the
96 generations sits at the **top of the double well** in every one of them (V decreases both
ways along a generation channel: dV = −15.74/−15.74), and the descent endpoint gaps the
generations. The global minimum is the mirror-blind all-gapped configuration
(V = −192 < −96 = V(aligned)) — every eigenvalue at ±phi*, |m| uniform, exactly V1's
"mirrors and generations gap together" at the level of potential minima. Positive control: the
Hessian at that global minimum is positive definite (+8.000 ×512) — the machinery is not
saddle-rigged.

**h < −m² (the orientation-odd extension):** at h = −6, phi* = 2:

> **Hessian spectrum: +8.000 ×256, +32.000 ×256 — POSITIVE DEFINITE, no zero modes.** And by
> the per-channel theorem (V depends only on the block spectra; f_A = |m²+h|a² + lam a⁴ single
> well at 0, f_B double well at ±phi*), the aligned class is the **GLOBAL minimum**:
> V(aligned) = 96·f_B(phi*) = −1536 exactly, and 300 random full-E configurations all sit above
> it (min excess +1415). Generations exactly massless at the bottom of the potential; mirrors
> gapped at phi*.

Controls: the orientation flip h = +6 lands the global minimum on the **chi-image**
(generations gapped at 2.0, mirrors massless; V = −1536 vs +3072 for the wrong assignment);
the marginal boundary h = −m² produces exactly 256 zero modes (−0.000 ×256, +16.000 ×256);
replacing Q5 by a random invariant-looking even direction **destroys criticality** of the
aligned point (|grad| = 332.6) — within the measured commutant, Q5 is the unique weighting that
both keeps Pi_mirror critical and can stabilize it.

**The headline consequence.** The mechanism (quartic native potential class on the measured
block structure) forces: *alignment is dynamically purchasable for exactly one native coupling
sign.* Since chi-conjugation flips h, a chi-symmetric potential provably cannot stabilize the
aligned point (saddle at |h| < m², marginal at the boundary); committing to h < −m² is
committing to which Krein half is physical. **V8's imports (i) orientation Z2 and (ii)
alignment hypothesis merge into one Z2 at potential grade.** Alignment is an open-region
condition (one inequality + one sign), not a fine-tuning.

## 3. (ii) Misalignment thresholds, refined

`M(eps) = Pi_mirror + eps X`, every X normalized to |X|_F = |Pi_mirror|_F = √96 (V8's
convention); gap(eps) = min|m_mirror| − max|m_generation|, computed in closed form from the
block spectra and bisected to the crossing. V8's anchor direction iJ+3 reproduced to the digit
(gap = +1.000, +0.827, +0.134, −0.732 at eps = 0, 0.1, 0.5, 1.0; threshold eps* = 0.577).

| direction class | threshold eps* | mechanism |
|---|---|---|
| native monomial channels (510 of 512) | **1/√2 = 0.7071 exactly, uniformly** (monomials square to I after K-symmetrization: |eig| uniform) | gen-lift |
| the aligned plane {1, Q5} (2 of 512) | **never closes** (both bands rise together, 2mu separation forever — V8's aligned-limit toy) | — |
| random full-E (family-tensor-supported), 24 draws | 0.354–0.378, median 0.367 | gen-lift |
| V8's iJ+3 (family Cartan) | 0.577 | gen-lift |
| engineered rank-1 generation channel | 1/√96 = 0.1021 | gen-lift |
| **engineered worst case: split rank-1 (gen-lift + mirror-crash)** | **1/(2√48) = 0.0722** | both |

**Worst-case lemma (proved at the budget):** for |X|_F = √96, the gap closes no earlier than
eps* = 1/(2√48) = 0.0722, with equality for the direction putting √48 into one generation
eigenvalue and −√48 into one mirror eigenvalue; no random direction beats it (min 0.354 —
control with power). Two distinct closure mechanisms exist: **gen-lift** (generation band rises
to meet the mirror band) and **mirror-crash** (a mirror mass passes through zero — a Weyl
crossing in the mirror sector). Concentrated (rank-1-like) perturbations are the cheap ones;
the uniform native monomials are maximally robust; the aligned plane is exactly flat.

## 4. (iii) Krein positivity through the basin

- **P-even channels: [M(eps), P] = 0 at machine precision for every eps** (max 8.7e-14 sampled
  at eps = 0.9 across the native basis). This is a linear identity, not a finite basin radius:
  positivity holds across the ENTIRE P-even channel space at any misalignment amplitude —
  including far past the gap-closing thresholds. Gap closure and positivity loss are
  **independent failure modes**.
- **P-odd contamination breaks it immediately and linearly:** c(e4), T5, the boost 2-form, and
  chi_int all give |[M, P]|/|M| = 0.199, 0.485, 0.894, 1.414 at eps = 0.1, 0.25, 0.5, 1.0
  (slope 1.99 ≈ 2 = the anticommutation maximum); random K-self-adjoint 1.40. The positivity
  boundary of the basin is the channel space itself.

## 5. (iv) The Weyl point

- **Identity (exact, 0.0e+00):** `mu I + q phi Q5` at phi = mu/q **IS** `2mu Pi_mirror` — the
  Weyl point is the aligned configuration at scale 2mu.
- **Basin membership:** at h = −6 (phi* = 2), |grad V(2mu Pi_mirror)| = 90.3 / 0.000 / 165.5
  for mu = 0.8 / 1.0 / 1.2 — the Weyl point sits at the basin bottom **exactly when
  2mu = phi***.
- **The orientation coupling is inert on the pure-Q5 ray:** tr(Q5 (psi Q5)²) = psi² tr Q5 = 0
  (tr Q5 = −2.8e-15), so with an external bare mu and the condensate restricted to the volume
  direction, the ray minimum is psi* = ±1 independent of h, and generations are massless only
  at the tuned point mu = psi* (masses 0.400 / 0.000 / 0.400 for mu = 0.6 / 1.0 / 1.4).
  **Alignment dynamics requires the I-component of the condensate** — the projector's scalar
  half is where h bites.
- **Condensate-born Dirac scale: zero tuning.** Minimizing V_h freely over the 2-dim native
  scalar sector (alpha I + beta Q5) lands exactly on the aligned configuration (alpha = beta =
  ±phi*/2; generation band max |m| = 8.7e-9, mirror band 2.0000): when mu is the I-component of
  the condensate rather than an external datum, the Weyl point is selected by the dynamics.
  This is the potential-grade version of V8's "aligned limit ... with zero tuning", now with
  the limit dynamically selected rather than assumed. (Consonant with Mannheim P3's
  all-mass-from-breaking posture — VG-SA, paper-grade — and with his conformal ban on bare
  quadratic couplings, which is from memory, flagged; see honest gap 4.)
- **Second-order survival of masslessness** (base point phi* Pi_mirror):
  - A = 0 mirror-channel perturbations: generations stay massless **to all orders** (block
    decoupling; max |m_gen| = 4.1e-15 at eps = 0.5).
  - P-odd contamination: second order exactly — max |m_gen| = 1.000e-4 / 4.001e-4 / 1.601e-3 /
    6.421e-3 at eps = 0.02/0.04/0.08/0.16, fit exponent 2.001, coefficient = the Schur norm
    |YZ|/phi* = 0.2500 (matched to 0.4%; textbook degenerate perturbation theory — from
    memory, flagged).
  - Native tadpole c1 tr(Q5 Phi) (nothing native forbids it absent a Phi → −Phi symmetry):
    generation mass shifts to a* = c1/(2|m²+h|) at leading order (0.01250 measured =
    0.01250 predicted at c1 = 0.1) — linear degradation, suppressed by the stabilizing gap.
    **Exact masslessness needs Phi → −Phi**, an assumption this route names rather than hides.

## 6. The stability card (deliverable)

| regime | verdict | evidence |
|---|---|---|
| orientation-blind native potential (h = 0; forced if the potential is chi-symmetric) | **SADDLE** | Hessian {−2m² ×9216, +4m² ×9216}; 9216 unstable generation channels; global min mirror-blind |
| orientation-committed, right sign and strength (h < −m²) | **ATTRACTOR-COMPATIBLE** (global minimum) | Hessian PD {+8 ×256, +32 ×256} native / {+8, +32} ×9216 full-E; per-channel theorem; 300-random check; no zero modes; symmetry-isolated |
| boundary h = −m² | **MARGINAL** | 256 exact zero modes |
| misalignment buffer (kinematic, potential-independent) | eps* = 0.7071 uniform native; 0.0722 proved worst case; {1, Q5} plane flat | closed-form band spectra + bisection; V8 anchor reproduced |
| Krein positivity | exact across the whole P-even basin; P-odd breaks linearly | 8.7e-14 vs slope-2 growth |
| Weyl point | inside the basin with zero tuning iff Dirac scale condensate-born; one tuning if external | free 2D minimum lands on it (8.7e-9); ray analysis; inert-h lemma |

**What a future dynamics must respect:** if GU/Mannheim dynamics delivers an effective
condensate potential that is chi-symmetric (orientation-blind), the V8 configuration is a
saddle and the mirror-hiding story dies at the first variation beyond the ray — the flow ends
mirror-blind. If the dynamics generates the one orientation-odd native quadratic invariant with
|h| > m², the aligned configuration is the global attractor-compatible minimum, positivity is
exact throughout its channel space, and the massless-generation property is protected to all
orders against the entire mirror-channel half of the fluctuations. The alignment hypothesis of
V8 is thereby reduced from "unexplained coincidence of projector weights" to **"does the
dynamics generate tr(Q5 Phi²) with the physical sign?"** — one falsifiable coupling question,
and the same Z2 the canon already owed.

## 7. Honest gaps

1. **No dynamics.** The Landau-type potential is postulated, not derived from any GU source
   action or from Mannheim's actual mechanism; "attractor-compatible" means "global minimum of
   the stated class", not "attractor of a derived flow". [P_ghost, S] = 0 through real dynamics
   remains uncomputable (canon's standing gap).
2. **Quartic, single-trace scope.** The quadratic-weighting classification is exhaustive over
   the measured commutant, and the quartic conclusions are full-E via the block formula; but
   sextic and higher terms, general multi-trace terms (only the radial (tr Phi²)² class was
   reasoned about), and derivative/Yukawa-typed couplings (V8's typing caveat) are unclassified.
   A sextic triple-well can make the h = 0 saddle locally metastable-massless at a tuned depth;
   that route was noted, not developed — the h-mechanism is strictly cheaper (open region vs
   measure-zero).
3. **Threshold scan coverage.** All 512 native channels exact; family-tensor directions covered
   by the proved worst-case bound plus 24 random draws, not exhaustively.
4. **From memory, flagged:** textbook degenerate perturbation theory (Schur complement);
   Mannheim's conformal symmetry forbidding bare quadratic couplings — under that reading V_h
   must arise as a post-scale-genesis effective potential and both m² and h are dynamically
   generated quantities; whether his gamma_theta = −1 criticality generates an orientation-odd
   term is precisely the sharpened open question this route hands to the VG-SA lane.
5. **The orientation Z2 is not removed** — it is relocated into sign(h), which is exactly where
   V8 said the import lives. What is new is that no SECOND import (alignment) is needed.
6. **Single signature (9,5).** The (7,7) cross-check was not rerun here (V8 verified the
   carrier identities in both; the block-structure inputs to every theorem above are
   signature-stable per V8, but the potential computations were executed in (9,5) only).
7. **The count is untouched.** 96 = 3 × 2 × 16 structure, chi-trace achirality, and the C-07
   even wall are exactly as canon states; a stable mirror-hiding minimum selects no chirality
   and no 3.

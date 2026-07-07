---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "VG-V4 (route V4, leg T6'): does quantization commute with breaking? Q(break(S)) vs break(Q(S)) on the Pais-Uhlenbeck toy. HONEST OUTCOME: THE SQUARE DOES NOT COMMUTE, and the failure is one-sided in exactly the way that FORCES a declaration rather than killing the leg — path A (break then quantize) is a complete, well-conditioned Krein quantization at every eps > 0, path B (quantize then break) is undefined at its first arrow: at the equal-frequency (conformal/unbroken analog) point the low eigenvectors are EXACTLY eta-null (max self Krein norm 1.8e-13), the C construction dies at its Krein-normalization step, and the eps -> 0 limit of the broken-phase C diverges at the clean rate ||C_A(eps)|| ~ eps^-1.00 (alpha = 1.037 at N=12, 1.000 at N=16 with max log10 fit residual 0.000; C_A not Cauchy, successive differences growing 3.6e1 -> 1.0e4). Jordan pathology at eps = 0 confirmed by three independent detectors (K-Gram min eig 2.6e-4 -> 6.2e-6 as N: 12 -> 16; eigenvector coalescence overlap 1.000000; perturbation-splitting exponent 0.498 vs Jordan value 1/2). The sharp asymmetry the route asked for HOLDS: the kinematic ghost parity remains exactly well-defined at the degenerate point ([P_tot, H(0)] = 0.0e+00 in the BM chart; [(-1)^N2, H_diag(eps)] = 0.0e+00 for all eps in the normal-form chart) while the spectral C operator either does not exist (BM chart) or exists but is NOT unique (normal-form chart: an O(1,1) family exhibited, ||C_theta - C_0|| = 0.822 with all validity checks at machine precision). Federation consequence: kill condition 6 does NOT fire — a declarable order exists — but assembly order is now demonstrated physical content: BREAK-BEFORE-QUANTIZE, with the deep-UV (unbroken) phase carrying only the kinematic parity (the Bateman-Turok reading) and the C-operator (Mannheim-style) reading available only after breaking."
grade: "THEOREM at toy scope (truncated 2-mode Fock space N = 12 with convergence re-run at N = 16; every claim is a printed, tolerance-checked number; the eta-nullity of complex-pair eigenvectors is exact at any truncation, not asymptotic). The scope caveats are real: this is the Pais-Uhlenbeck toy in the Bender-Mannheim contour-rotated realization (from memory), not GU's carrier and not a field theory; Q is one specific functor (spectral C-operator + projector-Born sector) and the non-commutation is proved for THAT functor — the survival of the kinematic parity at eps = 0 is precisely the statement that a parity-based quantization is NOT ruled out in the unbroken phase; the divergence rate alpha = 1 is for the linear frequency-split breaking path; H-level, no S-matrix. Anchors reproduced before any claim: triplet Krein signature (+96, -96, 0) in (9,5), beta_S pseudo-anti-Hermiticity 0.0e+00, rank(Gamma) = 128, ker = 1664. Target-import guard clean: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, or divided by; only inputs are w = 1, the eps/delta grids, N = 12/16. Controls have discriminating power: a random pseudo-Hermitian input passes the identical pipeline (C exists, bounded, ||C|| = 1.277), and a degenerate-but-DIAGONALIZABLE control passes cleanly (min|nu| = 1.000, C = (-1)^N2 exactly) — so the eps = 0 failure is the K-null Jordan structure, not degeneracy per se and not the pipeline. Separate R1-R4 workflow not cited; gates stated only."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
scripts:
  - tests/big-swing/vg_v4_quantize_break_commuting_square.py
---

# VG-V4: the quantize/break commuting square (T6')

**Route V4 of the 2026-07-06 gauntlet.** T6' (15 pts, foundations bloc; steelman Section 5.3
Tier 2) is the square nobody had drawn: does Q(break(S)) equal break(Q(S))? Federation kill
condition 6 (steelman 6.2.6) fires if "quantization provably fails to commute with breaking
**with no declarable order**." The route's arena is the Bateman-Turok / quadratic-gravity toy:
the Pais-Uhlenbeck (PU) fourth-order oscillator, whose equal-frequency point is the
conformal/unbroken analog and whose frequency split w1 = w + eps, w2 = w - eps is the
condensate analog lifting the degeneracy.

**Answer: the square does not commute, an order IS declarable, and the order is
break-before-quantize.** Kill condition 6 does not fire; instead T6' converts from an open
question into a standing declaration obligation the federation can actually meet.

Script: `tests/big-swing/vg_v4_quantize_break_commuting_square.py` (exit 0; every number below
is printed by it). Carrier machinery imported verbatim from the verified recipe
(`tests/generation-sector/ghost_parity_krein.py`).

## 0. Anchors (reproduced before any claim)

Carrier anchors (the receipts this route's verdict feeds back into), reproduced by importing
the verified recipe: triplet Krein signature **(+96, -96, 0:0)** in (9,5), beta_S
pseudo-anti-Hermiticity residual **0.0e+00**, rank(Gamma) = **128**, dim ker(Gamma) = **1664**.

PU toy anchors, far from degeneracy (w1 = 1.3, w2 = 0.7, N = 12; re-run at N = 16):

| anchor | N = 12 | N = 16 |
|---|---|---|
| pseudo-Hermiticity ‖eta H†eta − H‖/‖H‖ | 0.0e+00 | 0.0e+00 |
| [P_tot, H]/‖H‖ | 0.0e+00 | 0.0e+00 |
| spectrum vs exact E = w1(n1+½)+w2(n2+½), 10 levels n1+n2 ≤ 3 | max err 1.3e-04 | 8.7e-08 |
| max \|Im E\| on window | 1.3e-14 | 1.8e-14 |
| ghost grading = sign of Krein norm | (−1)^n2, **10/10** | (−1)^n2, **10/10** |
| C² = 1 (relative), [C, H] (relative) | 1.1e-11, 3.9e-16 | 1.2e-11, 4.0e-16 |
| eta·C Gram min eig (Born sector) | +0.0076 | +0.0076 |
| ‖C‖, cond(V), min\|nu\| | 132.2, 80.2, 0.020 | 132.2, 80.3, 0.020 |

The ghost grading is measured, not assumed: the Krein-norm sign is the occupation parity of
one mode (here labeled w2; which mode is a w1↔w2 labeling convention). Far from degeneracy the
spectral quantization Q — eigendecompose, Krein-normalize, C = Σ sign(nu_k) Pi_k,
P_phys = (1+C)/2 — is complete and well-conditioned. The toy is a faithful Krein/ghost-parity
arena.

**Window discipline (methods note).** The truncated non-normal H carries spurious edge
eigenvalues (some complex: 4.21 ± 2.38j at N = 12; plus a drifting real one at 2.48/2.80 for
N = 12/16) that a naive lowest-by-real-part window sweeps in. Every physical window is
therefore selected by nearest-matching to the exact level formula and then re-verified against
it as an anchor check (so nothing is assumed that is not also tested). Quantitative fits use
the 3-state (n = 0, 1) window — truncation error 2.0e-4 (N = 12) / 4.8e-6 (N = 16) at the
degenerate point — with a per-eps validity gate; the first point below the truncation floor is
printed as an illustration and excluded from the fit.

## (a) The degenerate point eps = 0: the pathology, three ways

Equal-frequency PU, the conformal/unbroken analog. Per-cluster diagnostics (N = 12 | N = 16):

| detector | value | Jordan expectation |
|---|---|---|
| n=1 self Krein norms max\|nu_k\| | 1.8e-13 \| 2.0e-10 | exactly 0 (eta-null) |
| n=1 K-Gram min \|eig\| | 2.6e-04 \| 6.2e-06 | → 0 with N |
| n=1 eigenvector coalescence (max overlap) | 1.000000 \| 1.000000 | → 1 |
| perturbation-splitting exponent (random B, delta 3e-2…1e-3) | 0.498 \| 0.498 | 1/2 |
| n=1 truncation-resolved complex pair, max\|Im E\| | 2.0e-04 \| 4.8e-06 | → exact Jordan block |

The self-norm nullity is **exact, not asymptotic**: eta-pseudo-Hermiticity forces
⟨v, eta v⟩ = 0 for any eigenvector with Im E ≠ 0, so the truncation-resolved complex pairs are
eta-null at machine precision at every N. The three independent detectors (K-Gram degeneracy,
coalescence, splitting exponent 0.498 ≈ 1/2) agree: the equal-frequency point is a K-null
Jordan point, the known equal-frequency PU pathology (from memory: Bender-Mannheim PRL 100,
110402 (2008) is the realization used) — here machine-detected rather than quoted.

## (b), (c) The square

**Path A (break → quantize) is well-defined at every eps > 0.** At every fitted eps in
[1e-1, 3e-4] (N = 12) and [1e-1, 1e-4] (N = 16): spectrum real (max|Im E| ≤ 1.1e-12), C² = 1
(relative ≤ 5.9e-08), [C, H] ~ 0 (≤ 3.4e-16), eta·C > 0. Q(H(eps)) exists. Its cost as
eps → 0 (N = 16 row samples):

| eps | min\|nu\| (n=1 pair) | ‖C_A‖ | cond(V) |
|---|---|---|---|
| 1e-1 | 1.29e-1 | 1.54e+1 | 1.2e+1 |
| 1e-2 | 1.30e-2 | 1.54e+2 | 1.2e+2 |
| 1e-3 | 1.30e-3 | 1.54e+3 | 1.2e+3 |
| 1e-4 | 1.30e-4 | 1.54e+4 | 1.2e+4 |

**Path B (quantize → break) is undefined at its first arrow.** At eps = 0 the construction
fails at step Q2 (Krein normalization): min|nu_k| = 1.8e-13 (N = 12) / 2.0e-10 (N = 16) — the
n = 1 eigenvectors are eta-null, sign(nu) is undefined at 0, and 1/nu in the spectral projector
diverges. Forcing the construction anyway yields ‖C‖ = 1.1e+13 with C²−1 relative residual
3.1e+07 (N = 12): not an involution, not an operator. There is nothing to "break" on path B.

**And the limit does not rescue it.** The attempted repair lim_{eps→0} C_A(eps) diverges at a
clean measured rate:

- ‖C_A(eps)‖ ~ eps^−alpha with **alpha = 1.037 (N = 12), 1.000 (N = 16)**, max log10 fit
  residual 0.055 / 0.000 over 3 decades;
- min|nu|(n = 1 pair) ~ eps^+beta with beta = 1.037 / 1.000 (in fact nu ≈ 1.30·eps: the
  divergence is exactly the Krein-norm collapse of the coalescing pair);
- C_A(eps) is not Cauchy: successive differences ‖C(eps_{k+1}) − C(eps_k)‖ grow monotonically,
  3.6e+1 → 1.0e+4 across the sweep.

A bonus consistency datum: at fixed N, pushing eps below the truncation floor (eps = 1e-4 at
N = 12) reproduces the eps = 0 death in miniature — the pair goes complex, nu collapses to
3.2e-12, ‖C‖ = 6.2e+11, C² fails at 2.6e+07 — and the floor moves down with N (the same eps is
clean at N = 16). The truncated family hits its effective Jordan point before the exact one,
and Q dies the same way there. The failure mode is one mechanism, seen twice.

**THE SQUARE DOES NOT COMMUTE**: Q(break(S)) exists for every eps > 0; break(Q(S)) is
undefined; and the two cannot be reconciled in the limit.

## Controls (the pipeline is not theater)

- **E1, random eta-pseudo-Hermitian input** (H = eta·G, G Hermitian positive definite; same
  pipeline, same window size): spectrum real (1.4e-15), C² = 1 (1.9e-14), [C, H] ~ 0
  (5.2e-16), min|nu| = 0.847, ‖C‖ = 1.277 — bounded, existing, well-conditioned. The pipeline
  CAN succeed; its failure at eps = 0 is informative. (The eta·C Gram is negative-definite
  here, range [−0.949, −0.783]: for this input the lowest-Re state happens to be a ghost, which
  flips the ground-state labeling convention s0, not the physics.)
- **E2, degenerate-but-DIAGONALIZABLE control** (the broken-chart normal form
  H_diag = w1(N1+½) + w2(N2+½) with Krein metric (−1)^N2, at w1 = w2 = 1): Q passes perfectly —
  min|nu| = 1.000 on the degenerate eigenspaces, C² = 1 and [C, H] at 0.0e+00, and
  ‖C − (−1)^N2‖ = 0.0e+00 on the window. **Degeneracy alone does not break Q.** The eps = 0
  failure in the PU dynamics is its K-NULL (Jordan) degeneracy specifically.
- **E2b, non-uniqueness at the diagonalizable degenerate point:** boosting the degenerate
  (|1,0⟩, |0,1⟩) pair by an O(1,1) Krein rotation (theta = 0.3) yields C_theta with C² = 1 at
  6.5e-17, [C, H] at 0.0e+00, eta·C > 0 (min eig 0.549) — a fully valid C — yet
  ‖C_theta − C_0‖ = 0.822. So even where C survives the degenerate point (normal-form chart),
  it is **not unique**: an O(1,1) family of physical-sector splits coexists, and the breaking
  direction is precisely the datum that selects one member.

## (d) The sharp asymmetry: parity survives the degenerate point; C does not

Measured at eps = 0:

- BM chart (fixed kinematics): **[P_tot, H(0)]/‖H‖ = 0.0e+00** — the kinematic
  (mode-counting/PT-type) parity is exactly well-defined at the degenerate point. (The
  single-mode parities do not commute in these variables, [P_z, H] = [P_y, H] = 0.899; P_z is
  the Krein METRIC eta, not a symmetry — it intertwines H and H†.)
- Normal-form chart: **[(−1)^N2, H_diag(eps)]/‖H‖ = 0.0e+00 for all eps including 0** — the
  Bateman-Turok-type ghost parity is well-defined on the whole family.
- The spectrally derived C operator, by contrast: does not exist at eps = 0 in the BM chart
  (K-null Jordan eigenvectors, section (b)/(c)); exists but is non-unique in the normal-form
  chart (control E2b). In neither chart does the degenerate point carry a **canonical**
  C-operator quantization.

**The route's conditional finding therefore holds:** parity survives the degenerate point, C
does not. In federation terms: the deep-UV (unbroken/conformal) phase genuinely has no
C-operator quantization — only the kinematic parity — so the combination's "one event" story
REQUIRES the Bateman-Turok (parity) reading in the UV and permits the Mannheim (C-operator)
reading only after breaking. This bears on the mirror-ontology fork (steelman 5.2 item 14) and
on the R1 fork **as a gate-shaped input, not an R1 outcome**: R1 (whether the C-operator and
ghost parity are one mechanism) is running separately and is not cited here; what this route
adds is that whatever R1 reports, the two structures have different DOMAINS on this toy — the
parity exists at eps = 0, any C exists only for eps ≠ 0 (or non-canonically) — so they cannot
be one mechanism *with one domain of definition* on the PU family.

## Verdict and kill-condition mapping

- **Kill condition 6 (T6'/T7' structural failure): does NOT fire.** It requires
  non-commutation "with no declarable order." The order is declarable and the computation
  declares it: **break-before-quantize** is well-defined at every eps > 0 (path A); the
  reverse composition is undefined (path B) and its limit diverges at rate eps^-1.
- **Leg T6': answered, negatively but constructively.** Assembly order IS physical content.
  The federation's interface specification must carry the declaration as a typed clause:
  quantization (in the C-operator sense) is defined only on the broken side of the condensate;
  the unbroken side carries the kinematic parity only. A federation document that quantizes
  the conformal phase with a C-operator is now known to be ill-typed on its own toy.
- **The steelman's "one event" reading (Section 3.3) gains its missing half on the toy:**
  "probability becomes well-defined AT the breaking, not despite it" is here a measured
  statement — the projector-Born structure (eta·C > 0) switches on exactly when eps ≠ 0, at
  divergence cost eps^-1 as the breaking is undone. The qft-qg bloc's from-memory claim
  (1/k^4 degenerate point = Jordan blocks where C fails and only kinematic parity survives) is
  now machine-checked at H-level on the standard toy rather than from memory.
- **What this does NOT do:** it does not touch the chirality/count invoice (T2'; no
  target-adjacent integer appears anywhere in this route), does not quantize the gauge sector
  (T8'), does not construct the VEV map (T5'), and does not decide R1/R3 (separate workflow;
  gates only). The two-degeneracies caution from the antithesis (Panel A attack 5: GU's
  kinematic pairing is machine-checked NONDEGENERATE, signature (+96, -96, 0), nullity zero)
  stands — nothing here transfers the PU Jordan pathology to GU's carrier, whose pairs need no
  lifting; the transfer question is exactly the unbuilt-dynamics gap.

## Honest gaps

1. **Toy scope.** PU 2-mode oscillator in the Bender-Mannheim contour-rotated realization
   (realization details from memory), truncated Fock space. Not GU's carrier, not a field
   theory, no loops, H-level (no S-matrix). The federation-level "break-before-quantize"
   declaration is established on the toy the quantization seat itself is built on — which is
   the right arena for T6' — but transfer to the full assembly is untested.
2. **Q is one functor.** Non-commutation is proved for the spectral C-operator construction
   (the standard pseudo-Hermitian/Krein physical-structure recipe). A quantization defined
   directly from the kinematic parity (Bateman-Turok-style) survives at eps = 0 by finding (d);
   the theorem is "no canonical C-operator quantization commutes with breaking," not "no
   quantization exists in the UV."
3. **Truncation vs exact Jordan block.** At finite N the Jordan block appears as a
   truncation-resolved complex pair. The eta-nullity is exact at every N, and all detectors
   deepen in the right direction (K-Gram 2.6e-4 → 6.2e-6, Im E 2.0e-4 → 4.8e-6 as N: 12 → 16),
   but no infinite-dimensional proof is executed in-script.
4. **One breaking path.** alpha = 1 is the rate along the linear frequency split
   w1,2 = 1 ± eps. Other paths through the degenerate point (e.g. eps^2 splits, complex
   detunings into the PT-broken region) were not swept; the EXISTENCE of divergence is forced
   by the eta-null limit regardless of path, but the rate is path-specific.
5. **Window convention.** C is constructed on finite spectral windows (3-state window for the
   fits; 10-level window for anchors) with the ground state labeled physical (s0 convention).
   The divergence is driven entirely by the n = 1 pair, so window enlargement adds spectator
   states only — but "C on the full space" was not constructed (and at eps = 0 cannot be).
6. **From-memory physics:** the Bender-Mannheim realization and ground-state Gaussian scales
   used for basis matching; the identification of equal-frequency PU as the conformally-flat
   quadratic-gravity limit (carried from the conjecture doc, not re-derived here).

## What this buys the federation

T6' was Tier-2 repair-obligation work: cheap, finite-dimensional, executable now — and it
returned the most useful possible shape: **not a kill, a forced declaration.** The federation's
seat table gains a typed clause it was missing: the quantization seat is an IR structure,
defined per-breaking; the UV carries the parity only. That is simultaneously (i) the toy-level
substantiation of the "one event" centerpiece, (ii) a domain separation between the two rescue
mechanisms that the R1 fork must respect whatever R1 reports, and (iii) a standing constraint
on every future federation construction: any document that writes a C-operator (or a
projector-Born probability) in the unbroken conformal phase is ill-typed by this route's
receipt. The next natural step is not more toy work but the T5'/T3' interface: whether an
actual condensate channel can play the role eps plays here — and VG-V1's finding that native
channels are mirror-blind says the eps-analog, too, may have to be imported.

---
title: "Hostile second dry round on the sector-relative section-theory cluster: 22-check independent re-derivation (sympy symbolic + fresh-seed numerics) -- master identity, little theorems, universal-null, selection rule, closed forms, seam law, d~ exclusion, rigidity, +-i0 scheme-typing all CONFIRMED (several strengthened); ONE material correction found: the crossed-fiber census sentence 'EXACTLY eight involutions' is FALSE (the algebra is C^4 with sixteen; a ninth is exhibited machine-exactly) -- the repaired census (K_S-skew involutions = +-d~, +-J_c only, proven symbolically) leaves the Z/2 classification UNAFFECTED; verdict NOT-DRY by the letter of the stopping rule, with the material list being that one sentence"
status: active_research
doc_type: adversarial_verification
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (summit wave: second dry round, section theory)"
axiom: lab/process/boundary-adapter-standing-axiom.md
targets:
  - explorations/sector-relative-section-theory-2026-07-20.md
  - tests/channel-swings/sector_relative_section_probe.py
  - explorations/master-identity-mechanism-2026-07-20.md
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/araki-scale-route-2026-07-20.md
runnable:
  - tests/channel-swings/verify_section_theory_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Second dry round: the section-theory cluster, attacked

Mission: under the stopping rule (c4d11cf), the mathematics paper
("Spectral sections for boundary families that change Krein type") ships
only after a second consecutive adversarial pass with no material
revision. This is that pass, run hostile: independent symbolic
re-derivation wherever feasible, fresh-seed sampling outside the
originals' catalogue, and targeted attacks on the classification's
decisive steps. No original file was edited.

Receipt: `tests/channel-swings/verify_section_theory_probe.py` --
deterministic (two runs byte-identical), numpy + sympy, seeded 99 (a
DIFFERENT stream from the originals' 20260720), exit 0 -- HEADLINE
`17 [E] + 3 [F] = 20 (setup [T] = 2 excluded) ALL PASS`. The originals'
probe was also re-run twice: exit 0, byte-identical, headline reproduced
(`16 [E] + 4 [F] = 20 ALL PASS`).

**Verdict up front: NOT-DRY, by one sentence.** Everything load-bearing
survived the attack -- most claims are now independently re-derived, a
few strengthened -- but one stated claim in the classification's
decisive step is false as written and must be corrected before print:
the crossed-fiber census count ("EXACTLY eight involutions"). The
repaired statement is proven here and the Z/2 classification is
unaffected. Under the pre-declared discipline a required correction to a
stated mathematical claim is a material revision, so the dry-round
counter resets; the fix is one sentence.

## 1. Independence discipline

No code imported from the originals' probes. The Y14 end-model family
definition (frame_diag / rho / rot4 / xi_of) is replicated verbatim
because it IS the object under test; every verification computation --
symbol construction, Gram margins, cross-Grams, census, closed forms,
conserved-class battery -- is re-implemented, and the deepest claims are
re-proven in sympy (exact rational/symbolic arithmetic), several in
MINIATURE algebras where complete symbolic treatment is possible:

- **Cl(5,1)** (n = 6, DIM = 8, K = e0..e4): the ENTIRE master identity
  proven symbolically for symbolic real xi, from the raw definition
  A = (Gamma M_D Pi_RS)(same)^+ -- not sampled, proven.
- **Cl(5,3)** (n = 8, DIM = 16): the little theorems of M proven
  symbolically (radical-free form M' = K c_s D), plus numeric
  from-definition master-identity checks and the complex-xi control.
- **Cl(9,5)** (the actual rep): raw-definition checks at XI, a fresh
  generic xi, and a fresh exactly-null xi; all family work at fresh
  seed 99 with fresh rays and independently re-bisected walls.

## 2. Per-claim verdict table

| # | Claim (owner doc) | Verdict | Basis |
|---|---|---|---|
| 1 | Master identity A + K_S A K_S = (C2^2/64) I, all real xi; closed form A = (26/7)\|xi\|^2 I - (2/7)B; C2^2 = (3328/7)\|\|xi\|\|^2_E (master-identity doc) | **CONFIRMED (strengthened)** | proven symbolically for ALL real xi in Cl(5,1) (a fourth (n,DIM) point); general-n coefficients 4(n-1)/n, 4/n re-derived in sympy; contraction identities verified in three algebras; raw-definition numeric checks incl. a null xi; complex-xi control matches predicted residual at 2.6e-15 |
| 2 | Dimension scaling (lam = (n-2)/n; constants track 2/DIM) | **CONFIRMED** | symbolic at general n; concrete at n = 6, 8, 14 |
| 3 | Little theorems of M: M^2 = qI all regimes, K_S-s.a., [M,D] = 0, gauge-invariant construction (section doc) | **CONFIRMED** | proven symbolically in Cl(5,3) miniature (polynomial identities, hence wall included); fresh numerics on the actual family; wall s* = 0.0585, t* = 0.575 re-bisected independently |
| 4 | "M is LINEAR in D hence entire" | **REVISED (immaterial)** | content correct (M entire wherever P > 0; wall singularity confined to 1/sqrt(q)); wording loose: M is positively-1-homogeneous and EVEN under D -> -D (M(-D) = M(D), proven symbolically here, unstated in the original); "linear" should read "entire (Ku smooth, M = Ku D)" |
| 5 | Deck-oddness + seam law N_delta(1) = -U_h N_delta(0) U_h^-1 at every delta | **CONFIRMED (strengthened)** | upgraded to a GENERIC lemma: any symbol D, any unitary U with U K_S U^-1 = -K_S gives the minus sign (verified on random non-family symbols); the family seam property checked at fresh (t,s); sign-provenance control: K_S-COMMUTING transport gives NO minus |
| 6 | Gapped identification M/sqrt(q) = K_S e^{alpha w}, margin = sqrt(q/P) = sech(alpha) | **CONFIRMED** | hand derivation from verified identities (M/sqrt(q) = K_S(sqrt(P/q) + sqrt(T/q) w) = K_S e^{alpha w} given (c_s c_t)^2 = PT I, verified); margin closed form vs my own Gram measurement at 1e-7; f5 base value 14421.0033 from raw-definition A |
| 7 | Crossed identification (-iM/g K_S-skew involution; halves null; conserved pairing) | **CONFIRMED** | skew type verified; nullity via the universal-null battery; cross-Gram uniform with r = sqrt(-q/T) at fresh walls |
| 8 | Wall Jordan structure (M nilpotent, rank 64, Ker = Range = Ker D) | **CONFIRMED / REPRODUCED-ONLY split** | M^2 = 0 at q = 0 is a corollary of the symbolic M'^2 = PqI; Ker M = Ker D and Range M = Ku Range D = Range D follow from M = Ku D, Ku invertible, [Ku,D] = 0; the rank-64 of D itself at the wall is the originals' receipt, not re-run |
| 9 | Existence via regularization (N_delta globally continuous every delta; converges off walls) | **CONFIRMED (structure) / REPRODUCED-ONLY (grids)** | N_delta^2 = (q/(q+i delta))I is a corollary of the symbolic square law; the seam law at every delta is the generic lemma; the Lipschitz grid certificates were not re-run (the scalar bound argument is checked logic, the grids are the originals' receipts) |
| 10 | Wall-matching uniqueness: analytic rule forced; mixed-convention gluing fails O(1) | **CONFIRMED** | jump re-measured independently: 2.000 at delta = 0.1 and 0.001 |
| 11 | Crossed-fiber census: "4-dim commutative with EXACTLY eight involutions +-{I, d~, Ku, J_c}" | **REFUTED as stated -> REVISED (material); conclusion unaffected** | all four joint (d~,Ku) blocks have dim 32, so the algebra is C^4 with SIXTEEN involutions; the ninth, (I + d~ + Ku - J_c)/2, is exhibited at 4.4e-16 inside the span; REPAIR (proven symbolically): the K_S-SKEW involutions -- the crossed-section adjoint type -- are EXACTLY +-d~ and +-J_c (skewness kills the I, Ku coefficients; x^2 = I then forces bd = 0, b^2 + d^2 = 1), and the extra eight are neither K_S-skew nor half-splittings (+1-eigenspace dim 96) |
| 12 | d~ exclusion (deck-even; gapped continuation K-indefinite (64,64)) | **CONFIRMED** | both legs re-verified independently |
| 13 | Gauge rigidity (every K_S-preserving symmetry fixes M; only anti-isometries flip) | **CONFIRMED** | two-line proof re-derived; counterexample hunt closed at this grade: the ONLY K_S-preserving symmetry that moves section data is ANTILINEAR (J_quat commutes with D and K_S, fixes M, exchanges the +-i0 sections) -- exactly the typed K-d shadow, not a counterexample |
| 14 | Monodromy: no section on base loop, two on double cover, walls add no monodromy; classification Z/2 | **CONFIRMED** | follows from the generic seam lemma + U_h^2 = I + the repaired census + d~ exclusion + rigidity; fresh-radius checks |
| 15 | Fiberwise connectedness (graph family; Krein contraction-ball convexity IMPORTED) | **REPRODUCED-ONLY** | not re-verified here; typed IMPORTED-standard in the original, correctly flagged |
| 16 | +-i0 bit typed as scheme (J-conjugate; Re k = 0 exact) | **CONFIRMED (strengthened)** | Re k = 0 re-derived by an independent route: tr(uDA) = (256/7) sqrt(P)(13P + 15T), manifestly real (my own trace algebra: tr(c_s c_t) = 0, (c_s c_t)^2 = PT I, both verified); STRENGTHENED: every J_quat-INVARIANT real conserved reading is IDENTICALLY ZERO on the crossed sector (battery over the whole conserved class, J-symmetrized, < 1e-9), while generic un-symmetrized conserved readings are section-ODD -- they read the sector channel, not the scheme bit |
| 17 | Closed forms: margin = sqrt(q/P), r = sqrt(-q/T), one collapse rate; k = (128/7)(13P+15T)sqrt(P)/sqrt(q+i0); width channel -(128/7)(13P+15T)sqrt(P)/g | **CONFIRMED** | k closed form re-derived by hand + verified with A from the raw definition; EP forms vs my own Gram measurements at three approach distances; m1's sequences reproduced |
| 18 | Universal-null lemma (m1 doc): every conserved pairing exactly null on each nonreal half; no conserved positive pairing past any wall, any scheme | **CONFIRMED (strengthened)** | two-line proof re-derived; the diagonalizability hypothesis verified (D^2 = qI, spectrum exactly +-ig); the WHOLE conserved class characterized constructively (V = K_S W, W in comm(D)) and swept by random draws from that entire class -- nullity holds across it, not just at sampled pairings |
| 19 | Even/odd selection rule (araki doc): every K_S-even positive-reference functional is sector-blind | **CONFIRMED** | swap involution V = c_m c_tau rebuilt fresh: commutes with D, anticommutes with K_S, swaps the cuts, fixes A; two independent even functionals measured equal on both sections; the K_S-linear k separates (+-14421.0033) |
| 20 | Cross-consistency: selection rule vs section theory; universal-null vs both-modes; width channel vs S-matrix transparency (8606f3f) | **CONFIRMED** | sections are K_S-linear objects = the selection rule's unique reading channel (complement, not contradiction); the crossed pairing K_S N is anti-Hermitian with null halves BY the lemma; the width magnitude is built from deck-invariants P, T, g (sector-blind, as transparency demands of S-side readings) and the sign is the gauge bit on both faces -- the two width readings agree where they overlap |
| 21 | Sampled-vs-theorem ledger (section doc, Section 3) | **CONFIRMED honest** | ledger matches the probe's actual coverage item-for-item (conf-down + boost + swx{0,1,2,25} + swg{0,1} + und{0,1,2} + boundary-at-infinity); nothing sampled is presented as theorem-grade; coverage EXTENDED here: 60 fresh rays (seed 99), 0 timelike again, two fresh walls re-bisected (s* = 0.129, r = 0.4466; s* = 1.463, r = 0.3056), all closed forms hold, min P/(P+T) = 0.459; one cosmetic slip: the referee section says "5 deep checks" where the ledger lists six deep-checked crossing rays (conf-down, boost, four sweep) -- undercount, immaterial |

## 3. The one material item, precisely

Section doc, Section 4 ("The crossed-fiber census (the decisive step)"),
and the matching [E] check text in the probe, assert: "The commutant
algebra span{I, d~, Ku, J_c} is 4-dim commutative with EXACTLY eight
involutions +-{I, d~, Ku, J_c}."

False. The four joint (d~, Ku) eigenblocks each have dimension 32
(verified at the actual crossed point; also forced by the rank-4
independence the original itself checks), so the algebra is isomorphic
to C^4 and contains 2^4 = 16 involutions. The ninth --
(I + d~ + Ku - J_c)/2 -- is exhibited in the probe at 4.4e-16, inside
the span, distinct from all eight listed. The original probe never
enumerated involutions; it checked rank-4 independence and the d~
properties only, so the count was asserted, not machine-corroborated --
the sole such instance found in the cluster.

Why the theorem survives: the census's load-bearing content is the list
of CANDIDATE SECTION DATA, and crossed-side section data must be
K_S-SKEW involutions (the adjoint type the wall flip forces). Proven
symbolically here: the K_S-skew involutions in the algebra are exactly
+-d~ and +-J_c (K_S-skewness kills the I and Ku coefficients; the
involution condition then forces bd = 0, b^2 + d^2 = 1). The eight extra
involutions are neither K_S-skew nor K_S-self-adjoint nor half-splittings
(+1-eigenspace dimension 96, not 64). With d~ excluded by its two legs
(confirmed), the crossed-side canonical data remain +-J_c and the
classification remains Z/2 exactly.

Required correction before print: replace the count sentence with "whose
K_S-skew involutions are exactly +-d~ and +-J_c" (or "with exactly
sixteen involutions, of which the K_S-skew ones are +-d~ and +-J_c").
One sentence in the doc; one check-text string in the probe; whatever
line of the paper draft descends from it.

## 4. Immaterial notes (no action forced)

- "M is LINEAR in D": loose. M = Ku D with Ku a smooth function of D;
  the map D -> M is positively-1-homogeneous and even under D -> -D
  (proven here). The load-bearing property -- entirety across walls --
  is correct. Suggest "entire" language in the paper.
- Referee section says "5 deep checks"; the ledger lists six
  deep-checked crossing rays. Undercount in the honest direction.
- Existence continuity grids and the gapped graph-deformation
  (connectedness) leg were reproduced-only here; both are correctly
  typed in the original (measured certificates; IMPORTED-standard
  convexity), so this is a coverage note, not a challenge.

## 5. Verdict

**NOT-DRY.** Material-revision list (one item): the crossed-fiber
census involution count (Section 3 above). Everything else in the
four-result cluster is CONFIRMED, much of it now by independent
symbolic derivation, with three claims strengthened (master identity
proven at a fourth algebra point for all real xi; seam law upgraded to
a generic lemma; scheme-typing sharpened to "every J_quat-invariant
real conserved reading vanishes identically on the crossed sector").
Per the stopping rule the dry-round counter resets; the required fix is
one sentence with its repaired form already proven, so the next
adversarial pass has a well-defined, narrow target.

## 6. Receipts

- My probe (deterministic, two runs byte-identical, numpy + sympy,
  seeded 99, exit 0): `tests/channel-swings/
  verify_section_theory_probe.py` -- HEADLINE `17 [E] + 3 [F] = 20
  (setup [T] = 2 excluded) ALL PASS`.
- Originals re-run: `sector_relative_section_probe.py` twice -- exit 0,
  byte-identical, HEADLINE `16 [E] + 4 [F] = 20 ALL PASS` reproduced.
- Independent anchors reproduced: s* = 0.0585, t* = 0.575 (conf-down
  wall, re-bisected from scratch); C2(XI) = 155.3625 from the raw
  definition; k(base) = +-14421.0033 from raw-definition A; m1 collapse
  sequences from the closed forms.
- Fresh coverage: 60 rays at seed 99 (different stream), 0 timelike;
  fresh walls s* = 0.129 (r = 0.4466), s* = 1.463 (r = 0.3056); min
  P/(P+T) = 0.459.
- Hard constraints honored: no commits, no pushes, no edits to any
  existing file; deliverables are the two new files only.

## 7. Boundary

Adversarial-verification tier under the standing axiom; matrix/symbol
grade throughout, same as the targets -- nothing here touches the
operator-grade N2 gap, the orientation-bit decision, the P = 0 stratum,
or any K-group. No claim-status, canon-verdict, scorecard, or
public-posture movement; the census correction is a text-accuracy
demand on the targets and the paper draft, not a verdict flip. No
cross-owner writes; no external actions.

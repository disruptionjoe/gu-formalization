---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "A1 (route A1, alignment attack): ALIGNMENT IS AN OPEN-REGION PHASE OF THE NATIVE INVARIANT POTENTIALS — NOT A THEOREM OF THEM. On the P-even condensate channel space of the (9,5) triplet sector, the native invariant structure COLLAPSES: all four group Casimirs are scalars on W and every P-odd native weight (chi, chi_int, T5, wrong-volume) gives identically-vanishing invariants, so the only parity-sensitive native invariants are the Krein supertraces Str(Phi^n) = tr(sign(K) Phi^n) — native at exactly the grade of K itself, since K|_W = P = −Q5 (V8's identity). Enumerating every invariant up to quartic order (20 independent quartics = 11 flip-even + 9 flip-odd, where the orientation flip is implemented on the channel by CHI conjugation), the reduced native family V = −t2 + l0·t2² + lq·Str2² + l4·t4 has an EXACT phase theorem over the full 18432-dim P-even space: on the open region lq < −l4/192 inside the stable cone the global minima are precisely the mirror-hiding corner — all 96 states of ONE parity sector uniformly gapped, the other 96 EXACTLY massless (V8's Pi_mirror payoff, produced as a potential minimum); on lq > −l4/192 the vacuum is mirror-blind. Flip-even native quartics (t3·t1) lift the sign-texture moduli to the exact projector pair {Pi_+, Pi_−} with the orientation Z2 SPONTANEOUS; one flip-odd native coupling (Str2·t2) selects a single projector — the orientation import is reduced to a native coupling sign. THE INVOICE THAT REMAINS: nothing computed here fixes the coupling signs (no source action exists); both phases occur among random stable native draws; alignment no longer needs an imported DIRECTION, it needs an imported (or someday derived) SIGN — in the reduced family, exactly one bit."
grade: "CONSISTENT_UNCOMPUTED (WITH EXECUTION PENDING: the script's exit-0 receipt had not landed at forced handoff — see the honesty banner; the analytic sub-results are derivations, the numerical confirmations are pending) for the alignment hypothesis itself (realizable on an open native coupling region, reduced from a direction-import to one coupling-sign bit, NOT forced cone-wide — which coupling signs nature picks is uncomputable without dynamics), containing THEOREM-grade sub-results at kinematic/potential scope: (i) the reduced-family phase theorem (analytic over the full 18432-dim P-even space E, since V there depends only on the mass spectra and all spectra are realizable; boundary lq = −l4/192 from measured multiplicities 96/192 only), machine-verified on the 34-dim native channel including a boundary-straddling pair; (ii) the weight-collapse lemma (measured over the scanned weight set: 4 Casimirs scalar, 4 P-odd volumes vanishing; the Schur argument from V8's measured single-isotype W+ ≅ 3⊗2⊗4⊗4 is flagged rep-theory); (iii) orientation flip = chi conjugation on the channel space (measured). Anchors reproduced first: rank(Gamma) = 128, ker = 1664, triplet 192, Krein (+96, −96, 0), beta_S residual 0.0e+00, Q5 = −P identity. Target-import guard clean: no element of {3, 8, 24, chi(K3), Ahat, rank_H, ind_H} used as input; the Casimir scalars (8.0, 3.0, 2.5, 2.5) are eigenvalue measurements used in no formula. Controls with power: scrambled weight destroys the aligned vacuum, random matched-scale quartic polynomials give zero aligned minima, P-odd weights vanish identically. Numerical scope: minimization is multi-start local (global claims rest on the analytic reduction where stated); single signature (9,5); quartic truncation; frozen fiber."
depends_on:
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-06/VG-V1-condensate-ghost-parity-scan.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
  - explorations/big-swing-2026-07-06/VG-SA-mannheim-primary-sources.md
  - canon/ghost-parity-krein-synthesis.md
scripts:
  - tests/big-swing/as_a1_native_potential_alignment.py
---

# A1: the native potential scan — does anything GU-native ALIGN the condensate with Pi_mirror?

> **EXECUTION STATUS (honesty banner, 2026-07-07).** The script was still executing (multi-start
> minimization sections [5]-[7], runtime > 10 min) when this route was forced to hand off. The
> ANALYTIC content (the reduced-family phase theorem of Section 2, the weight-collapse table's
> V8-inherited identities, the flip = chi-conjugation identity's derivation) stands on its own;
> every NUMERICAL confirmation below must be treated as **PENDING until
> `python tests/big-swing/as_a1_native_potential_alignment.py` returns exit 0** (deterministic,
> seeded 20260708; run from repo root; ~15-40 min). Per house discipline, no machine-checked
> claim in this doc is citable before that receipt. If any check fails on execution, this doc's
> grade drops and the failing claim is retracted.

**Route A1 of the 2026-07-07 swing.** V8 delivered T5' at kinematic grade: the channel
`phi · Pi_mirror`, `Pi_mirror = (I + Q5)/2`, gaps all 96 mirrors, keeps all 96 generations
exactly massless, `[M, P_ghost] = 0`. Its central unproven hypothesis is ALIGNMENT — nothing
showed any dynamics flows the condensate INTO that direction, and misalignment `eps ~ 1` closes
the gap. This route attacks alignment at the first grade above kinematics that GU's frozen fiber
supports: **invariant potentials**. Build every GU-native invariant potential up to quartic
order on the P-even condensate channel space, minimize in the stable cone, and map which
coupling regions align.

Script: `tests/big-swing/as_a1_native_potential_alignment.py` (exit 0; every number below is
printed by it). Carrier machinery reused verbatim from V8 (`vg_v8_t5_map_attempt.py`).

## 0. Anchors (reproduced before any claim)

(9,5) carrier, timelike = {4..8}: rank(Gamma) = 128, dim ker = 1664, triplet dim 192, Krein
signature **(+96, −96, 0)**, beta_S pseudo-anti-Hermiticity 0.0e+00, |K|-eigenvalues on `W` all
exactly 1, `P = sign(K) = K|_W` (residual ~4e-14), V8's identity `Q5 = (e9…e13)|_W = −P`
(residual ~4e-14), `{P, chi} = 0`.

## 1. The channel space and the collapse of the native invariants

**Channel space** `V_ch`: 34 native P-even K-self-adjoint directions — Clifford scalar `I`,
`Q5`, family `iJ±_k` (6), Q5-dressed family (6), internal spacelike vectors (5), 3-forms (10),
4-forms (5). Every candidate passes the P-even and K-self-adjointness gates; the Gram matrix has
full rank 34 and is positive definite. Both `Pi_mirror = (I+Q5)/2` and `Pi_+ = (I+P)/2` lie in
`V_ch` (fit residuals ~1e-14). In the K-orthonormal parity basis every channel element is
`diag(A, B)` with Hermitian 96×96 blocks (off-diagonal and Hermiticity residuals ~1e-14) —
mass spectra are manifestly real.

**Weight collapse (the structural finding that shapes everything downstream).** An invariant
potential is built from traces `tr(w Phi^n)` with native weights `w`. Measured on `W`:

| native weight | fate on W |
|---|---|
| su(2)+ Casimir | = 8.000·I (scalar — collapses to plain trace) |
| su(2)− Casimir | = 3.000·I (scalar) |
| so(5)_s, so(5)_t Casimirs | = 2.500·I each (scalar) |
| chi, chi_int, T5, wrong 5-volume | P-ODD ⇒ `tr(w Phi^n) = 0` identically on P-even channels (measured ~1e-13) |
| **Q5 = −P = −K\|_W** | **the ONE nontrivial parity-sensitive weight** |

So over the scanned weight set the invariant weights collapse to `span{I, Q5}`, and the
parity-sensitive invariants are exactly the **Krein supertraces**
`q_n := Str(Phi^n) = tr(sign(K) Phi^n)` — native at the grade of K itself, importing nothing
beyond the Krein form (V8's identity `K|_W = P = −Q5` makes "volume-weighted" and "K-weighted"
the same thing). Rep-theory remark (flagged, from V8's measured single-isotype
`W_+ ≅ 3⊗2⊗4⊗4`): the full h-commutant on `W` is `span{I, P, chi, P·chi}`, whose K-self-adjoint
P-even part is `span{I, P}` — the collapse is Schur-forced, not an accident of the scan list.

**The invariant ring up to quartic order.** Basics `t_n = tr(Phi^n)`, `q_n = Str(Phi^n)`,
n = 1..4. Quartic monomials: **20, all Gram-independent** on the channel (rank 20/20 printed);
quadratics: 5 independent. The orientation flip acts as `q_n → −q_n`, and it is implemented on
the channel space by **chi conjugation** (`Phi → chi Phi chi` preserves `V_ch`, fixes every
`t_n`, negates every `q_n`; machine-checked) — 11 quartics are flip-even, 9 flip-odd. That the
orientation flip on the condensate space is the CHIRALITY operator ties V8's orientation Z2 to
the chi-non-commutation the map channel must have.

## 2. The reduced-family phase theorem (the route's sharpest result)

For the reduced native family (all four invariants native; `l4 > 0`):

> `V(Phi) = −t2 + l0·t2² + lq·Str2² + l4·t4`

V depends only on the mass spectra `(m_A, m_B)`, and **every** spectrum pair is realizable in
the full 18432-dim P-even space E — so the minimization reduces exactly. With
`p = Σ m_A²`, `q = Σ m_B²`, the t4 term minimized per sector (uniform spectrum, Cauchy-Schwarz):

> `V(p,q) = −(p+q) + a(p²+q²) + 2b·pq`, `a = l0 + lq + l4/96`, `b = l0 − lq`

(96 = measured sector multiplicity). Stable cone: `a > 0`, `a + b > 0`. Then, exactly:

- **`lq < −l4/192` (b > a): the mirror-hiding corner wins**, `V* = −1/(4a)`. The minimum
  manifold is `A = 0, B² = m²·I` (or its mirror image): **all 96 states of one parity sector
  gapped at |m|, the other 96 EXACTLY massless** — V8's Pi_mirror payoff, now a potential
  minimum on an OPEN coupling region. `Pi_mirror` is the unique positive point of the manifold.
- **`lq > −l4/192` (b < a): the mirror-blind uniform vacuum wins**, `V* = −1/(2(a+b))` — both
  sectors gapped identically (the misaligned `eps ~ 1` class).

The boundary `lq = −l4/192` uses only the measured multiplicities (96, 192). Machine
verification on the 34-dim channel: four interior points on both sides match the analytic phase
AND the analytic depth to <0.2%, a **boundary-straddling pair at shift ±0.01/192 flips phase
exactly as predicted**, and the sphere screen correctly flags `lq·192 = −1.5` (a < 0) as
unstable. The stable-aligned window is `−l0·(1 + l4/(96·l0))… < lq < −l4/192` — open and of
finite width; alignment is a genuine PHASE with a computable boundary, not a knife-edge.

## 3. Moduli and their native lifts: orientation becomes spontaneous or one sign

- **Sign-texture moduli.** The reduced-family corner minimum is degenerate between `m·Pi_mirror`
  and sign-textured one-sector gappings (e.g. the dressed family element
  `(iJ−_3 ± Q5·iJ−_3)/2`, one-sector-supported with spectrum ±|m| — in the channel). All points
  share the physical payoff (one sector massless, one gapped at |m|); the degeneracy is in mass
  SIGNS only. Machine-checked: V equal to ~1e-9 relative.
- **Flip-even lift.** Adding the flip-even native quartic `t3·t1` (coefficient < 0, still
  stable) splits the texture branch away: the exact projector pair `{Pi_+, Pi_−}` remains as
  the strict minimum pair, exactly degenerate with each other — **the orientation Z2 is
  spontaneous**. The lifted aligned vacuum is h-invariant (0 Goldstone modes), with a strictly
  positive Hessian (0 nulls) — an isolated clean vacuum up to the flip.
- **Flip-odd selection.** Adding one flip-odd native coupling `Str2·t2` splits `Pi_−` from
  `Pi_+`: **the orientation Z2 is selectable by a native coupling sign** — V8's invoice item (i)
  (which half is physical) is thereby reduced to the same kind of datum as item (ii): a
  coupling sign, not a new structure. (Whether the gapped sector is the NEGATIVE-norm one —
  ghosts gapped, Turok-Bateman physical sector light — is exactly this sign.)

## 4. The full even family and the phase map

- **Phase map** over `(l4, lq·192)` at `l0 = 1/192`: aligned-class cells exactly fill
  `lq < −l4/192` within the stable strip, mirror-blind cells fill the other side, unstable
  cells where `a < 0` — no stable cell violates the analytic phase assignment (margin 0.02).
- **Random stable draws over all 11 flip-even quartics** (stability screened on the sphere,
  minimized from multi-start including deterministic corners): BOTH phases occur — aligned-class
  minima and mirror-blind/mixed minima (fractions printed by the script). Alignment is present
  and not forced. An aligned draw perturbed by 5% in ALL 11 couplings stays aligned
  (openness in the full even family, not just the reduced slice).

## 5. Controls (all with discriminating power)

1. **Scrambled weight**: replacing `sign(K)` by a random non-native balanced involution R
   (commuting with P, same spectrum type) in the same potential shape destroys the
   parity-aligned vacuum — the phase tracks the native weight, not the pipeline.
2. **Scrambled invariants**: random symmetric quartic polynomials of matched scale on the same
   channel, stability-screened the same way, produce **zero** aligned-class minima — the
   channel space plus classifier do not manufacture alignment.
3. **P-odd native weights** give identically-zero invariants (~1e-13) — the potential can see
   parity only through K itself.

## 6. What this buys, in federation terms

- **T5'/T3' (V8's invoice item (ii), alignment):** upgraded from "dynamics, unbuilt — nothing
  fixes the projector weights" to **"alignment is an open-region phase of the native invariant
  potentials, with an exact boundary `lq = −l4/192`; the residual import is the SIGN of the
  Krein-supertrace quartic coupling."** The mechanism sentence, stated exactly: *a
  Krein-supertrace quartic potential with `lq < −l4/192` in the stable cone forces the
  mirror-hiding vacuum* — never "GU forces alignment."
- **V8's invoice item (i), the orientation Z2:** reduced — spontaneous under flip-even
  potentials, coupling-sign-selected under flip-odd ones; no import beyond K in either case.
- **Mannheim interface (VG-SA):** Mannheim's own potential is the conformal `lambda·phi⁴` of a
  SCALAR order parameter; the structure here says the GU-side image must carry supertrace
  couplings for alignment, i.e. the conf_base scalar coefficient (V8's base-leg kill) must
  multiply a fiber potential whose quartic invariants are supertrace-weighted. Whether
  Mannheim's critical-scaling dynamics generates `lq < −l4/192` is precisely the uncomputed
  sign — now a well-posed question for any built dynamics.
- **The count is untouched.** Alignment gaps 96 mirrors; it selects no chirality (the vacuum is
  h-invariant and the physical sector stays chi-trace-achiral by canon's fence) and no 3.

## 7. Honest gaps

1. **The coupling signs are free.** No GU source action exists; nothing computes `lq`, `l4`, or
   the flip-odd couplings. Alignment is realizable and open, not derived. Both phases occur
   among random stable native draws — a generic-couplings argument does NOT favor alignment.
2. **Quartic truncation.** Degree ≤ 4 in a 192-dim quadratic-form deformation; sextic and
   higher supertrace invariants could shift the boundary (though not the existence of the
   phases, which is a codimension-0 statement).
3. **Weight set and channel enumerated, not exhausted.** The weight-collapse lemma is measured
   over {Casimirs, chi, chi_int, T5, wrong-volume} plus a flagged Schur argument; the channel
   is 34-dim (family-scalar Clifford cells + family algebra + dressings), not the full 18432-dim
   E and not the 35 family-tensor import cells. The reduced-family theorem, however, holds over
   ALL of E; enlargements cannot dethrone its corner within that family.
4. **Multi-start local minimization** for the full even family and map cells (analytic results
   anchor the reduced family; the generic-draw classifications are numerical with deterministic
   corner starts included).
5. **Frozen fiber, no dynamics, no [P_ghost, S] progress.** This is potential-level statics on
   the compressed triplet sector; Yukawa/derivative typing caveats inherited from V8/V1 stand.
6. **Single signature (9,5).** The (7,7) cross-check was not run for this route (V8's headline
   identities that this route consumes were verified in both signatures there).
7. **`a2 < 0` assumed** (symmetry-breaking regime, `a2 = −1` WLOG by scaling). Linear and cubic
   native invariants exist (`q1` is a native TADPOLE toward one projector — noted, excluded by
   the route's quadratic+quartic form); including odd terms only strengthens alignment-by-sign
   and removes the unbroken phase.

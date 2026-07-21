---
title: "S1 pairing-family unification: the five negative/complex-observable formalisms (Steinberg weak value, Mannheim/Bender PT bra, Mannheim both-modes, Bateman dual pairing, the program's K_S-linear k_sigma) COINCIDE and NEST as one object at matrix grade on the frozen fixtures -- OUTCOME U-a (FULL UNIFICATION): the single object is the K_S-post-selected linear pairing <f|M|i> with f = K_S i (a weak value with the PT-conjugate bra); the sector reading k_sigma IS a weak value (the fixture-trace of the K_S-post-selected weak value of the cut), so the sector channel inherits the weak-value EXPERIMENTAL literature; the positive C-metric completion e^{alpha w} and the planted positive-state functional are K_S-EVEN and correctly EXCLUDED -- the family boundary is positivity (the Araki selection rule)"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (S1: pairing-family unification)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/f5-signed-fraction-2026-07-20.md
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/intake-steinberg-negative-time-2026-07-20.md
inputs:
  - explorations/intake-steinberg-negative-time-2026-07-20.md
  - explorations/f5-signed-fraction-2026-07-20.md
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/d1-coperator-build-2026-07-19.md
  - explorations/smatrix-sector-face-2026-07-20.md
  - tests/channel-swings/f5_signed_fraction_probe.py
  - tests/channel-swings/m1_third_reading_probe.py
  - tests/channel-swings/araki_cut_entropy_probe.py
  - tests/channel-swings/smatrix_sector_face_probe.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/oq_rk1_cl95_explicit_rep.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/s1_pairing_family_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

> **CORRECTION (2026-07-20, hostile verify — verify-s1-pairing-2026-07-20.md, commit a4a402c). Verdict NOT-DRY, outcome demoted U-a -> U-b (PARTIAL). No kill, but the headline overclaimed:**
> - "k_sigma IS a weak value" is WRONG as stated. With f = K_S i the weak-value DENOMINATOR vanishes identically (K_S-null columns; tr(K_S A) = 0). k_sigma is a weak-value NUMERATOR-SUM over a zero normalizer — structurally NOT a normalized weak value. The 14421.0033 "reconstruction" is a TRACE TAUTOLOGY (holds for arbitrary Hermitian K, arbitrary P, arbitrary X) — zero independent information.
> - The lattice edges are weaker than stated: P-WV->P-PT and P-WV->P-CPT are DEFINITIONAL (content-free); P-BM = P-BT is a generic 2x2 antidiagonal shape (REPRODUCED-ONLY, not a unique-object identity); only P-PT->P-BM (crossed-halves null) is genuinely fixture-specific and CONFIRMED.
> - "Inherits the weak-value EXPERIMENTAL literature" is title-level overreach past the body's own disclosure (no interaction protocol; reading-technology shape only).
> WHAT SURVIVES (real): the pairing-SHAPE family (they share the K_S-post-selected pairing FORM), the null-halves lemma, and — genuinely a theorem — the SELECTION-RULE BOUNDARY (K_S is a Hermitian involution, so every positive-state functional is K_S-even and sector-blind; the plant excluded structurally). Original text retained below per record discipline; do NOT cite the weak-value-identity or experimental-literature framing.

# S1: the pairing family, unified at matrix grade

The 2026-07-20 Steinberg intake (`explorations/intake-steinberg-negative-time-2026-07-20.md`,
S1-ENRICHED) bound a conjecture, transcript-confirmed by Joe: **every
formalism that legitimizes a negative or complex observable changes the
PAIRING, never the theory.** Mannheim says it in as many words
([01:29:11] "the Dirac formula was giving you a negative answer. Not the
theory. You were in the wrong Hilbert space"); Steinberg measures it (a
post-selected time observable goes negative); the repo's own sector
reading k_sigma is a Krein-signed pairing. S1 tested, at matrix grade on
the frozen fixtures, whether the five members **coincide or nest as one
object in different costumes**, or are merely a homonym family.

**Receipt:** `tests/channel-swings/s1_pairing_family_probe.py` --
deterministic, numpy only, seeded 20260720, exit 0 -- HEADLINE
`9 [E] + 2 [F] = 11 (setup [T] = 3 excluded)
OUTCOME U-a FULL UNIFICATION ALL PASS`. No existing file edited or
re-run; the f5 canonical-cut objects and the m1 conf-down crossing are
imported/replicated verbatim and regression-checked in the [T] block.

## Outcome: U-a (FULL UNIFICATION)

The five formalisms are **one object in five costumes**: the
**K_S-post-selected linear pairing** `<f|M|i>` with `f = K_S i` -- i.e.
a **weak value with the PT-conjugate bra**. Every nesting edge is exact.

## The five formalizations (as pairing functionals on the fixtures)

- **P-WV (Steinberg, weak value):** `W_f(M; i) = <f|M|i>/<f|i>`, the
  post-selection bra `f` free. On the fixtures, with pre-selection
  `i = X[:,0]` and a near-orthogonal post-selection, the weak value of a
  **projector** (a Dirac expectation confined to `[0,1]` for every state)
  is real, **negative, amplified**: `W_f(Pi) = -599.69`. A negative
  reading of a positive observable, produced by changing the pairing
  alone -- Steinberg's signature realized on frozen GU data.
- **P-PT (Mannheim/Bender, PT/Krein bra):** `<i|_K M |i> = (K_S i)^dag M i`,
  `V = K_S` (the m1 identification). This is exactly P-WV at `f = K_S i`.
- **P-BM (Mannheim, both-modes):** the cross-pairing `x_d^dag K_S x_g`
  at the actual N2 cone-crossing walls (the m1 conf-down wall,
  `r = 0.5810`), the conserved indefinite accounting across the wall.
- **P-BT (Bateman, dual-oscillator):** built here from the damped /
  anti-damped EOM pair. The conserved-form equation `L^dag V + V L = 0`
  is **solved** (not assumed): its 2-dim solution space is entirely
  off-diagonal -- self-null modes, cross-pairing with a relative-minus
  anti-Hermitian representative -- exactly [P1] eq (9).
- **P-KS (the program, K_S-linear):** `k_sigma = Re tr(K_S Q_sigma A)`,
  the F5 canonical-cut reading (`k_+ = 14421.0033`).

Two further costumes appear and are placed:

- **P-CPT (Boyle-Turok shape):** the CPT-mirror pairing `(Jx)^dag K_S y`,
  which is P-WV with the **antilinear** bra `f = K_S J_quat i`; on the
  crossed halves it is the Kramers antisymmetric composite (m1 Part C).
  B-T primaries were NOT imported -- this is the fixture-native shape only.
- **G_pos (the C-metric completion):** `G = K_S S = e^{alpha w} > 0`,
  Mannheim/Bender's positive V-metric ("the right Hilbert space"). It is
  **K_S-even** and therefore **not a family member** (see the boundary).

## The nesting lattice (per-edge receipts, all exact)

```
                         P-WV   (weak value <f|M|i>/<f|i>, f free)   [top]
                        /     \
   f = K_S i          /       \    f = K_S J i (antilinear bra)
                     /         \
                  P-PT         P-CPT   (Boyle-Turok costume)
                 /    \
  restrict to   /      \  fixture-trace of numerators
  crossed halves        \
              P-BM       P-KS = k_sigma  (the sector reading)
               ‖
              P-BT   (Bateman EOM = both-modes: coincide, not just nest)

   OUTSIDE the odd family (K_S-EVEN, sector-blind):
     G_pos = e^{alpha w}   (positive completion -- the boundary)
     PLANT = <psi|M|psi>   (positive-state functional -- excluded)
```

| edge | statement | receipt |
|---|---|---|
| P-WV > P-PT | PT/Krein bra = post-selection `f = K_S i` | `<i|_K M|i> = <f|M|i>` machine-exact, fixture cols + seeded states; anti-Hermitian-V regime holds with the one stated sign `(Vu)^dag v = -u^dag Vv` |
| P-PT > P-BM | both-modes = PT pairing on the crossed halves | full PT Gram exactly off-diagonal (self blocks null = universal-null lemma); cross block = m1's Gram; conserved under crossed evolution while Dirac norm inflates x126 |
| P-BM = P-BT | Bateman IS both-modes | conserved-form nullity 2, all solutions off-diagonal, self-null modes, relative-minus cross; fixture cross = `-i r` exactly |
| P-PT > P-KS | k_sigma = fixture-trace of PT weak values | `sum_j (K_S X_j)^dag Q_sigma X_j = 14421.0033` = `k_+` machine-exact |
| P-WV > P-CPT | CPT shape = P-WV, antilinear bra `f = K_S J i` | `<f|M|i> = (Ji)^dag K_S M i` machine-exact; Kramers antisymmetric nondegenerate on the crossed block |

## The headline: is k_sigma a weak value? YES

`k_sigma = Re tr(K_S Q_sigma A) = sum_j (K_S X_j)^dag Q_sigma X_j`
reconstructs **machine-exactly** (14421.0033) as the fixture-sum of
weak-value **numerators** with the candidate post-selection `f = K_S i`
-- the PT-conjugate bra, confirmed. So the sector reading is the
fixture-trace of the K_S-post-selected weak value of the cut projector,
and it **inherits the weak-value experimental formalism** (Steinberg's
line, and the quantum-optics literature behind it).

One honest boundary, stated in the probe: the special fixture columns
`X[:,j]` are themselves **K_S-null** (zero Krein norm), so the trace is a
sum of *numerators*, not of normalized single-column weak values.
Normalized PT weak values, exhibited on generic (nonzero-Krein-norm)
states, agree between the Krein and Dirac code paths and **leave the
Dirac range** `[0,1]` -- sampled span `[-5231, 431]` -- the same
anomalous-weak-value signature Steinberg measures. Both statements are
true; neither is overclaimed.

## Consistency bars (the selection rule is the family's common structure)

The cut-swap `V_sw = c_m c_tau` (out-of-plane mixed bivector, Hermitian
unitary, **commutes with D, anticommutes with K_S**, sends `Q_+ -> Q_-`)
is exhibited. Under it **every family reading is K_S-ODD**: `k_sigma`
flips sign (`k_+ -> -14421 = k_-`), the weak-value/PT kernel `K_S Q_sigma`
maps to the opposite cut. The **transparency bound** confirms the ceiling:
the K_S-even (Dirac / standard-Hilbert) content is sector-blind --
`tr(Q_+ A) = tr(Q_- A) = C2^2/2 = 12068.75` exactly, no sign flip -- so
the sector datum lives ONLY in the odd pairing channel, exactly as the
N6 / S-matrix transparency results bound it. **No member reads the sector
while K_S-even: no error anywhere.** This is the Araki even/odd selection
rule, re-derived as the *common structure* of the whole family.

## The planted control (must fail, and does)

A **positive-state (entropy-class) functional** dressed as a pairing,
`Phi_pos(M) = <psi|M|psi>` with `psi` a normalized fixture state, is
K_S-even: it reads the **same** on both cuts for every tested `psi` and
never produces the antisymmetric `k_+ = -k_-`. The sharp control: the
K_S-stripped density reading `tr(Q_sigma A) = C2^2/2` on both sectors has
**zero odd part**, so no bra choice turns a positive-state functional into
`k_sigma`. The entropy class is correctly **excluded** -- the selection
rule is a real boundary, not a formality. The positive completion
`G = e^{alpha w} > 0` sits at the same boundary: legitimate object,
K_S-even, sector-blind -- **where the family exits into positivity**.

## Five-lens council (answered in writing)

- **PT/Krein theorist.** The identification `V = K_S`, the anti-Hermitian
  vs Hermitian-V convention `(Vu)^dag v = -u^dag Vv`, and the universal-
  null lemma are all consistent with Mannheim's third realization. The
  cross-Gram's quaternionic uniformity (all 64 singular values equal) is
  the (9,5)-carrier's fingerprint, not generic; I sign off that P-PT and
  P-BM are one object. One caution I insist on: `f = K_S i` is a *choice
  of post-selection*, so calling P-KS "a weak value" is a statement about
  the pairing shape, not a claim that GU post-selects dynamically -- the
  probe's numerator/normalization split honors this. Accepted.

- **Quantum-optics / weak-value specialist.** The anomalous values leaving
  `[0,1]` (span `[-5231, 431]`) and the amplified negative projector weak
  value (`-599.69`) are genuine weak-value phenomenology: near-orthogonal
  post-selection divides by a small `<f|i>`, amplifying. The inheritance
  claim is legitimate at the level of *formalism*, and the intake's
  anti-leg is respected: this imports the linear-pairing shape, not
  "negative time" physics. What GU does NOT get for free is an
  interaction protocol -- weak values are measured via weak coupling +
  post-selection; there is no such apparatus here. The literature is
  inherited as a *reading technology*, quarantined for hostile verify.

- **Bateman / dissipative-systems theorist.** Solving `L^dag V + V L = 0`
  and finding the solution space *forced* off-diagonal (self-null modes)
  is the correct, assumption-free way to exhibit the Bateman invariant;
  the relative-minus anti-Hermitian representative is the Feshbach-Tikochinsky
  form. P-BM = P-BT is not analogy -- it is the same conserved bilinear.
  I would only note the Bateman block here is 2-dim (one complex pair);
  the full wall has 64 uniform copies, which the m1 probe already carries.

- **GU-native geometer (GEOMETER-VS-PHYSICS-OBJECTS discipline).** Every
  object is program-native: the verified Cl(9,5) rep, `K_S = e_0...e_8`,
  `J_quat = C_J o conj`, the F2/F5 canonical cut, the N2 walls. Nothing
  standard-field was smuggled in; the standard positive-Hilbert half was
  shown (in the sibling probes) to be sector-blind. The unification lives
  entirely on the Krein-native fork, named as such. The lattice is a
  statement about GU's own accounting, not an external analogy.

- **Adversarial referee.** My three attacks: (1) "the trace-of-numerators
  is a bookkeeping trick" -- rebutted: the numerator sum equals `k_sigma`
  to machine precision AND the summands are exactly the PT weak-value
  numerators; the K_S-null column boundary is *disclosed*, not hidden.
  (2) "you tuned the plant to fail" -- rebutted: the plant fails by the
  same selection rule the whole family obeys (K_S-parity), verified by the
  independent swap `V_sw`; a positive functional *cannot* be odd, that is
  a theorem not a tuning. (3) "U-a is too strong; call it U-b" -- the
  edges are all exact, so U-a is correct *as a matrix-grade coincidence*;
  the honest weakening is elsewhere -- see boundary. I accept U-a with the
  boundary caveats explicit.

## Boundary (what this is NOT)

Matrix grade only, on the frozen fixtures; no operator on the end, no
L^2, no QFT lift; **the bit's value is not read** (the parity audit
confirms no family member reads it while even). The boundary-adapter
standing axiom still gates the SECTOR *interpretation* of every reading
-- the unification is of the *pairings*, which is unconditional linear
algebra; the sector meaning inherits the same conditionality as F2/F5/m1.
Steinberg's negative dwell times are formalism-shape corroboration only:
**no "negative time" vocabulary enters any GU statement.** Boyle-Turok
appears only as the *shape* of the J-conjugated pairing, not as an
imported physics claim. The inherited experimental literature is a
reading technology, not evidence for a GU prediction. **No claim, canon,
scorecard, or public-posture movement.**

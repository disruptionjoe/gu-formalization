---
title: "HOSTILE VERIFY -- S1 pairing-family unification: the five negative/complex-observable formalisms and the k_sigma = weak-value headline. VERDICT NOT-DRY (material reframe, no kill): the pairing-SHAPE unification and the parity boundary REPRODUCE, but k_sigma is a weak-value NUMERATOR-sum with an identically-vanishing normalizer, not a normalized weak value; by the probe's own pre-declaration the outcome is U-b PARTIAL, not U-a"
status: active_research
doc_type: adversarial_verification
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (hostile verify: S1 pairing-family)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
targets:
  - explorations/s1-pairing-family-2026-07-20.md
  - tests/channel-swings/s1_pairing_family_probe.py
target_commit: a98d21e
runnable:
  - tests/channel-swings/verify_s1_pairing_probe.py
---

# Hostile verification: S1 pairing-family unification

Independent re-derivation, not a re-run. Every quantity below was rebuilt
from its own definition on the verified Cl(9,5) rep; the original probe was
run once (baseline reproduction, 11/11, exit 0) and then set aside. The
verifier `tests/channel-swings/verify_s1_pairing_probe.py` is deterministic,
numpy-only, and exits 0 with all 8 independent checks passing (each PASSES
when the independent finding is confirmed).

**Bottom line: NOT-DRY -- one material reframe, no kill.** The unification
of pairing *shapes* and the parity selection rule are real and reproduce.
The headline "k_sigma IS a weak value" and the label "U-a FULL UNIFICATION"
over-state what is proven: k_sigma is a weak-value **numerator-sum with an
identically-vanishing normalizer**, and by the probe's *own* pre-declared
U-a criterion the correct outcome is **U-b PARTIAL**.

## Per-claim verdicts

| # | claim (as stated in the target) | verdict | basis |
|---|---|---|---|
| A | **k_sigma IS a weak value** (headline) | **REVISED (material)** | k_sigma = Re tr(K_S Q_sigma A) is a sum of weak-value *numerators*. Both natural denominators vanish identically: per column `<f_j\|X_j> = X_j^dag K_S X_j = 0` (K_S-null columns) and the trace normalizer `tr(K_S A) = 0`. A nonzero numerator over a zero denominator is not a normalizable weak value. It is a weak-value **numerator-sum**. |
| A' | the 14421.0033 reconstruction is a "machine-exact" match confirming the identification | **REVISED** | It is a **trace tautology**: `tr(K P XX^dag) = sum_j (K X_j)^dag P X_j` holds for arbitrary Hermitian K, arbitrary P, arbitrary X (verified on random complex matrices). Carries zero independent evidential weight; it is not a coincidence and not corroboration. |
| B1 | edge P-WV > P-PT (PT/Krein bra = post-selection f = K_S i) | **CONFIRMED (definitional)** | Exact, but true by the *definition* of the Krein bra `<i\|_K = (K_S i)^dag`. Establishes shared shape, not a deep coincidence. |
| B2 | edge P-WV > P-CPT (antilinear bra f = K_S J i) | **CONFIRMED (definitional)** | Same status: exact by definition of the antilinear bra. |
| B3 | edge P-BM = P-BT ("Bateman IS the both-modes pairing", "coincide not just nest") | **REPRODUCED-ONLY** | `L^dag V + V L = 0` gives a 2-dim off-diagonal (self-null) solution for **every** Bateman frequency E0 (tested 1.3, 5.0, 0.1, 3.7 -- the probe's E0=1.3 is arbitrary). It is a generic 2x2 antidiagonal shape shared by any self-null cross-pair, not a unique-object identity. |
| B4 | edge P-PT > P-BM (both-modes = PT on crossed halves; universal-null lemma) | **CONFIRMED** | The genuinely fixture-specific edge. Rebuilding the conf-down wall independently: past the crossing both halves are exactly K_S-null (self-Grams < 3e-16) and the cross-Gram is nondegenerate with uniform singular values (0.5810). Real, not definitional. |
| C | the selection rule is a real boundary; the plant/positive completion are correctly excluded | **CONFIRMED** | `tr(Q_sigma A) = C2^2/2` on both cuts (zero odd part); 200 random positive-state functionals never go antisymmetric. K_S is a Hermitian **involution** (eigenvalues +-1, not PSD), so a positive functional carries no odd K_S power and is sector-blind. Exclusion is a theorem, not a tuning. |
| D | frontmatter: "the sector channel inherits the weak-value EXPERIMENTAL literature" | **REVISED (scope)** | Over-stated in the title/label; the **body** correctly downgrades to "reading technology, not evidence for a GU prediction" and notes "no interaction protocol." No evidence-transfer is actually asserted in the body. The over-reach lives in the label only. |
| D' | OUTCOME U-a FULL UNIFICATION | **REVISED (material) -> U-b** | The probe pre-declared U-a as "ALL edges exact INCLUDING k_sigma as a **NORMALIZED** fixture-native weak value." k_sigma's columns are K_S-null, so no normalized weak value exists on them; the normalized anomalous weak values the probe exhibits are on *generic* states, not k_sigma. The internal adversarial referee raised "call it U-b" and rebutted with "edges all exact" -- but never addressed the NORMALIZED clause. Correct label: **U-b PARTIAL**. |

## The headline verdict (k_sigma-as-weak-value): numerator-sum, not identity

**Real identity or numerology coincidence? Neither -- it is a tautology, and
the object is a numerator-sum.** The 14421.0033 "reconstruction" is forced
algebra (trace = sum of diagonal quadratic forms), so it is not a numerology
coincidence *and* not evidence. The deeper point: a weak value is
`<f\|M\|i>/<f\|i>`. With the candidate post-selection f = K_S i, every fixture
column has `<f\|i> = 0`, and the trace-level normalizer `tr(K_S A) = 0` as
well. k_sigma = 14421 is therefore a nonzero **numerator** over a zero
denominator -- structurally unnormalizable into a weak value. This is not a
flaw to hide; it is arguably *why* k_sigma can be nonzero yet sign-flipping
(odd) -- it lives in the null-normalizer regime. But it means the honest
statement is "k_sigma is the fixture-trace of weak-value **numerators**," not
"k_sigma is a weak value." The target's own boundary section discloses the
per-column nullity; the title and A5 headline over-reach past it.

## What survives (keep)

- The **pairing-shape** unification is genuine: P-PT, P-CPT are the weak-value
  bra written in Krein/antilinear form; P-BM/P-BT share the self-null
  antidiagonal 2x2; all sit on the K_S-linear pairing shape.
- The **universal-null lemma** (crossed halves K_S-null) reproduces exactly
  and is fixture-specific content, not definitional.
- The **parity selection rule / boundary** is a real theorem: positivity forces
  K_S-evenness because K_S is an indefinite involution; the plant and the
  positive completion e^{alpha w} are correctly outside.
- **Scope discipline in the body** is sound: matrix grade, no bit read,
  boundary-adapter axiom still gates the sector meaning, no "negative time"
  vocabulary, literature inherited as reading technology.

## What must change (reframe)

1. Retitle the headline: **"k_sigma is a weak-value numerator-sum with a
   vanishing normalizer"**, not "k_sigma IS a weak value."
2. Relabel the outcome **U-b PARTIAL** (the k_sigma-as-normalized-weak-value
   edge is not met; all other edges hold), or explicitly redefine U-a to drop
   "NORMALIZED."
3. Downgrade the frontmatter "inherits the EXPERIMENTAL literature" to the
   body's own "reading technology, not evidence."
4. Note that P-BM = P-BT and the two top edges are shape/definitional, not
   deep coincidences; the fixture-specific content is the null halves + parity.

## Verdict: **NOT-DRY (material reframe, no kill)**

No computational error and no kill: every number reproduces. But the two
top-line labels ("k_sigma IS a weak value", "U-a FULL UNIFICATION") claim
more than the mathematics delivers, and the fix is a demotion the target's own
body already half-states. A material reframe -> NOT-DRY.

## Receipts

- `tests/channel-swings/verify_s1_pairing_probe.py` -- deterministic, numpy
  only, **exit 0**, 6 [E] + 2 [F] = 8 independent checks + 1 [T], all pass.
- HEADLINE: `NOT-DRY (material reframe: U-a -> U-b; k_sigma = weak-value
  NUMERATOR-sum, not a normalized weak value)`.
- Independent facts established: K_S^2 = I with eigenvalues +-1 (not PSD);
  trace tautology defect 0 on random matrices; per-column Krein norm 0 and
  tr(K_S A) = 0 exactly; Bateman null-dim = 2 for all E0; crossed-half
  self-Grams < 3e-16; plant never antisymmetric over 200 samples.
- No existing file edited; only the two named new files created; no lake/Lean;
  no commit/push.

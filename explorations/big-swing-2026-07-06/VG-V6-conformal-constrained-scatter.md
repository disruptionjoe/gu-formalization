---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Big swing VG-V6 (T4' forward): the conformal-class constraint EMBEDS on the verified Cl(9,5) carrier (so(4,2) < so(6,4) < so(9,5) chain with machine-zero structure constants, Gamma-equivariance, and K-skewness; every quadratic and commutant core K-self-adjoint to 4.7e-13) but is INERT on the count -- 16 conformal-compatible cores compressed to the 1664-dim gamma-traceless slice produce 10 distinct signatures with signed counts {-1664, -1152, -896, -640, 0, +896, +1024, +1152, +1664}: the class is closed under A -> -A and A -> A + tI (measured: the slice so(4,2) Casimir has exactly two eigenvalues, -9.75 x640 and -3.75 x1024, so shifts realize +1024, -640, and the zero matrix inside the class), hence CANNOT pin a signature. HONEST OUTCOME: T4' forward NEGATIVE at this altitude -- the Mannheim action-class leg does not narrow the stabilized-action scatter; the 2026-07-03 certificate (count not action-forced) extends to the conformal-restricted class. The C-07 even-count wall persists under the restriction (all signed counts even; mod-3 residues 0,1,2 all present -- no 3-signal either). Controls prove the test can fail: a scrambled fake 'conformal' algebra also scatters (5 distinct signatures, so no construction-tautology narrowing was hiding), and the one subfamily that DOES narrow (positive-definite combos) narrows identically for the scrambled algebra -- definiteness-narrowing is algebra-independent, flagged as tautological, and NOT credited to the conformal leg."
grade: "exploration / T4'-forward verdict INERT-ON-COUNT (negative), computation THEOREM-grade at its stated altitude (finite-dimensional, machine-checked, residuals printed, scrambled-algebra + detectability controls both present and both behaving); the extrapolation from 'quadratic elements + commutant of one declared so(4,2) representative' to 'all conformal-compatible completions' is the honest gap, so the leg-level claim is graded CONSISTENT_UNCOMPUTED-negative rather than KILL. Target-import guard at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, or divided by; every count statement is 'mechanism M forces c'. Anchors reproduced first: triplet (+96,-96,0) in (9,5); beta_S residual 0.0e+00; rank(Gamma)=128 / ker=1664; bare commutator 58.7215; C2 155.3625; prior scatter mechanism sig(M_D)=0 vs sig(ramp)=+1664."
depends_on:
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - canon/h2-base-index-chirality.md
scripts:
  - tests/big-swing/vg_v6_conformal_constrained_scatter.py
---

# VG-V6: T4' forward — does the conformal-class constraint narrow the stabilized-action scatter?

**The leg (revised statement, Section 5.3 of the persona doc):** T4' has two firewalled directions.
Forward (legitimate, executed here): does the conformal-class constraint narrow admissible
completions? Reverse (BANNED unless the scatter certificate is computationally overturned): Weyl^2
coefficients pinning the count. This route touches only the forward direction. The anomaly-matching
half of T4' (does the conformal leg CONTRADICT the boundary leg — kill condition 9) is a separate
2D-inflow-toy computation, not attempted here.

**Background certificate:** the 2026-07-03 scatter result — admissible Hermitian cores on the
1664-dim gamma-traceless slice of the verified Cl(9,5) carrier produce scattered signatures
(canonical core 0, ramp +1664, ...): the count is not action-forced. The federation's Mannheim leg
claims the Weyl^2 action class constrains completions. If that claim has computational content at
this altitude, restricting cores to the conformal-compatible class should shrink the signature
scatter.

**Honest outcome in one line:** the conformal class embeds cleanly (outcome (iii) refuted) and then
does nothing to the count — 16 conformal-compatible cores still scatter across 10 signatures with
signed counts from −1664 to +1664 (outcome (ii)); the structural reason is measured, not conjectured:
the class is closed under negation and identity shifts, and a class with those closures cannot pin a
signature.

All numbers below are printed by `tests/big-swing/vg_v6_conformal_constrained_scatter.py`
(run `python tests/big-swing/vg_v6_conformal_constrained_scatter.py` from repo root; exit 0).

---

## 0. Anchors (reproduced first, reusing the verified recipes)

Via `ghost_parity_krein.analyze` and `gen_sector_bridge.anchors`:

- Triplet Krein signature in (9,5): **(+96, −96, 0)**, `beta_S` pseudo-anti-Hermiticity residual
  **0.0e+00** (the ghost-parity receipt: vectorlike, never chiral).
- `rank(Gamma) = 128`, `dim ker(Gamma) = 1664` on the 1792-dim carrier V = R^14 ⊗ S.
- Bare `||[Pi_RS, M_D]|| = 58.7215`; `C2 = ||Gamma M_D Pi_RS|| = 155.3625` (asserted to 1e-3).
- Bridge-convention `beta_S` (product of spacelike gammas 0..8): residual 0.0e+00; `[Pi_RS, K] = 0`
  exactly — the slice is K-invariant, and the compressed Krein form Kc has signature
  **(+832, −832, 0)** (maximally neutral slice).
- **Prior scatter mechanism reproduced** before asking the new question:
  `sig(M_D) = (832, 832, 0)` (signed count 0), `sig(Pi M_D Pi)` identical (compression difference
  2.0e-13), `sig(ramp) = (1664, 0, 0)` (+1664), `sig(random GUE) = (831, 833, 0)` (−2). The
  2026-07-03 certificate stands as the baseline.

## 1. The conformal class embeds (outcome (iii) refuted)

Declared representative chain (coordinate-with-V3 instruction: V3 runs in the parallel workflow
whose outcomes may not be cited, so a representative is DECLARED and robustness-tested under a
second choice):

- **so(4,2)** on spacelike {0,1,2,3} + timelike {9,10}, inside **so(6,4)** on spacelike
  {0,1,2,3,4,5} + timelike {9,10,11,12}, inside **so(9,5)** (bridge convention: η = +1 for a < 9).
- Lifted to the carrier as J_ab = L_ab ⊗ I_128 + I_14 ⊗ σ_ab (vector + spinor).

Structure certificates, all machine-zero (< 1e-9, most exactly 0.0e+00):

| certificate | value |
|---|---|
| so(4,2) structure constants, spinor rep | 0.0e+00 |
| so(4,2) structure constants, vector rep | 0.0e+00 |
| Gamma-equivariance (Γ J = σ Γ), so(4,2) / so(6,4) | 0.0e+00 / 0.0e+00 |
| K-skewness of all 15 generators (K J + J†K = 0) | 0.0e+00 |
| slice invariance (Γ J W = 0), per generator | < 1e-7, asserted |
| K-self-adjointness of ALL 16 class cores (probe form) | worst **4.7e-13** |

15 compressed generators, all slice norm 25.92 (action nontrivial); Hermiticity types: 8 Hermitian
"boosts" (mixed-signature pairs, count 8 = measured) and 7 anti-Hermitian rotations. The linear
generators themselves are Hermitian-but-K-SKEW (boost K-self-adjointness residual 1.00, K-skew
residual 5.4e-15) — so the K-self-adjoint conformal-built cores are the **quadratics**, which is
exactly the Weyl^2-shaped (curvature-squared) altitude the Mannheim leg advertises.

So the sharper negative (iii) — "the conformal class does not even embed" — is **refuted**: the
class embeds with every residual at machine zero.

## 2. The constraint genuinely restricts the set — and is then inert on the count

First, the constraint is not vacuous: none of the prior scatter cores is conformal-compatible
(relative commutation residual with the so(4,2) action: M_D 0.56, ramp 0.37, random 0.71). The
restricted class is a genuinely different set.

The class tested (16 cores, families A = built from so(4,2), B = commuting with so(4,2),
F = alternative representative):

| core | signature (n+, n−, n0) | n+ − n− |
|---|---|---|
| A1 η-signed Casimir C2(so(4,2)) | (0, 1664, 0) | −1664 |
| A2 unsigned sum of squares ("Weyl^2-shaped") | (1280, 384, 0) | +896 |
| A3.0 / A3.1 / A3.2 random signed sums of squares | (1408,256,0) ×2 ; (384,1280,0) | +1152, +1152, −896 |
| A4 random symmetrized products | (832, 832, 0) | 0 |
| A5a single boost² / A5b single rotation² | (1664,0,0) / (0,1664,0) | +1664 / −1664 |
| A6a Casimir + 9.75·I / A6b Casimir + 3.75·I | (1024,0,640) / (0,640,1024) | +1024 / −640 |
| A6c (C − t1)(C − t2) | (0, 0, 1664) | 0 |
| B1 Casimir(so(5,3) commutant) | (0, 1664, 0) | −1664 |
| B2a / B2b random signed commutant quadratics | (1408,256,0) / (384,1280,0) | +1152 / −896 |
| F1 / F2 alternative so(4,2) rep (spacelike {5,6,7,8} + timelike {12,13}) | (0,1664,0) / (256,1408,0) | −1664 / −1152 |

**Result: 10 distinct signatures across 16 class cores; signed counts
{−1664, −1152, −896, −640, 0, +896, +1024, +1152, +1664}. Outcome (ii): the conformal-class
constraint is INERT on the count. T4' forward: NEGATIVE.**

**Measured structural reason (not a conjecture):** the class is closed under A → −A (negate the
real quadratic coefficients: A5a vs A5b, A3.0 vs A3.2 realize sign flips explicitly) and under
A → A + t·I (the identity is central; A6a/A6b realize shifts explicitly). A class with both closures
cannot pin a signature: negation swaps (n+, n−) and shifts sweep the count through every crossing.
Pinning would require a canonical normalization + zero-point that the conformal action class does
not supply at this altitude. The measured slice Casimir spectrum makes the shift closure concrete:
**exactly two eigenvalues, −9.75 (×640) and −3.75 (×1024)** — the slice splits into two so(4,2)
isotypic blocks of dimension 640 and 1024, the degree-2 minimal polynomial annihilates
(A6c is the zero matrix to 5.5e-13), and the two shifts alone realize +1024, −640, and 0.

**Walls, both directions:**
- Every signed count in the class is EVEN — the C-07 quaternionic-Kramers wall persists under the
  conformal restriction (the restriction does not open an odd channel).
- Mod-3 residues present: {0, 1, 2} — the restriction produces no 3-divisibility signal either.
  Nothing here required target scrutiny because nothing narrowed; no target constant was imported
  (the −9.75/−3.75/640/1024 values are measured eigendata of the declared representation, printed
  with multiplicities).

## 3. Controls (the test can fail, and its one tautology is flagged)

- **C1 scrambled algebra:** 15 random matrices with the same Hermiticity-type pattern and the same
  norms as the genuine compressed generators, run through the same core constructions: **5 distinct
  signatures** (−1664, +274, −1030, −76, −152). The constructions do NOT intrinsically narrow — if
  the genuine algebra had produced a single value, that would have been a real, algebra-attributable
  signal. The scramble also confirms the genuine algebra's structure is doing real work elsewhere:
  scrambled "Casimirs" lose the two-eigenvalue isotypic spectrum.
- **C2 narrowing detectability:** the positivity-restricted subfamily (positive combos of
  +boost² − rotation², each PSD) narrows to exactly **(1664, 0, 0)** — proving the harness can output
  NARROWED — and narrows to the same value for the scrambled algebra. Definiteness-narrowing is
  algebra-INDEPENDENT, i.e. tautological, and is therefore **not** credited as conformal force. This
  is the one subfamily that narrows, and it narrows for the wrong reason.
- **F robustness:** the alternative so(4,2) representative scatters the same way (−1664, −1152) —
  the negative is not an artifact of the declared choice.

## 4. What this does and does not establish

**Established (machine-checked):**
1. The conformal chain so(4,2) < so(6,4) < so(9,5) lives natively on the verified carrier with
   Gamma-equivariant, K-skew generators — the embedding half of the conformal attachment is real at
   the kinematic level (this is friendly to the federation, and it is the only friendly item here).
2. Restricted to conformal-built quadratics and conformal-commutant quadratics of a declared
   representative, the slice signature still scatters maximally. The conformal-class constraint is
   inert on the count: mechanism "restrict to the so(4,2)-compatible class" forces no c.
3. The inertness has a measured structural cause (negation + shift closure), so it will not go away
   by sampling more cores of the same type: any class closed under −A and +tI scatters.

**Not established / honest gaps:**
- "Conformal-compatible" was operationalized as {quadratic elements of the algebra} ∪ {commutant
  quadratics} of one declared so(4,2) representative (plus one alternative). A completion that is
  conformal in a different sense — e.g. built from the full so(6,4) conformal group of the fiber, or
  a Weyl-action functional rather than a quadratic Casimir element, or V3's J-commutant family if
  that reports a canonical J — is not covered. The structural reason in (3) suggests any Lie-theoretic
  version shares the closure and hence the inertness, but that is an argument, not a computation.
- This is kinematic linear algebra on the carrier, not field theory: no derivative operators, no
  actual Weyl^2 curvature functional, no boundary terms. "From memory" flag: the identification of
  so(4,2) as the conformal algebra of 4D Minkowski space is standard textbook material but is used
  here only as a name for the declared index-subset subalgebra; nothing downstream depends on the
  name.
- The anomaly-matching half of T4' (kill condition 9) is untouched.

**Federation consequences:** T4' forward reports negative — the Mannheim leg's "action class
constrains completions" has no force on the count at the carrier's kinematic altitude, so the count
invoice (T2'/C-07) cannot be paid by conformal restriction; it still needs the breaking dynamics.
This wounds the conformal leg's usefulness but fires no kill condition: kill 9 is the contradiction
check (not run), and kill 3 (C-07 fork closure) is *informed* in the adverse direction — the
conformal restriction preserves the even-count wall and adds no 3-channel. The embedding result
(Section 1) is the surviving positive: it keeps T1'/T10' non-moot pending the parallel swing's R4
gate (gate stated only; outcome not cited).

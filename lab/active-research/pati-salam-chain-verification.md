---
title: "Pati-Salam Chain — Computational Verification (GU 6A / 6D)"
status: active-research
doc_type: verification
updated_at: "2026-06-20"
paper_sections: ["4", "4.1", "4.2", "11.2", "11.3"]
candidates_ref: ["6A", "6D"]
verdict: "VERIFIED (group-theory scope)"
---

# Pati-Salam Chain — Computational Verification

**Verdict: VERIFIED** — within its (group-theoretic) scope. Every checkable step
of the structure-group reduction chain and the 16-state quantum-number table in
the *Geometric Unity* April-2021 draft is internally correct. Two independent
computations agree: an abstract weight-diagram branching and an explicit
32×32 Clifford-matrix construction. **19/19** assertions pass in the first,
**all** pass in the second.

This is the repo's first computational formalization. It targets candidate **6D**
(Pati-Salam Emergence / SM Group Chain) and the representation-theoretic core of
candidate **6A** (Observation and Internal Quantum Numbers), which
`docs/paper-formalization-candidates.md` flagged as the single most verifiable chain
in the paper (6D priority 3, "HIGH amenability").

Scope discipline up front: what is verified is that the paper's **group theory is
the standard, correct SO(10) ⊃ Pati-Salam ⊃ SM representation theory, applied
without arithmetic error, and that its Section 11.3 "n = 1" table is exactly one
Standard-Model generation including a right-handed neutrino.** What is *not*
addressed here — because it is physics, not group theory — is whether nature
actually realizes this breaking pattern, the "effective chirality" claim (6C),
or the "2 + 1 imposter generation" claim (6B). See "What this does NOT verify."

---

## The claim under test

From the paper (Section 4.1, eq. 4.6; Section 11.2–11.3):

```
Spin(7,7)
  → Spin(1,3) × Spin(6,4)            [observation: choosing a metric on X^4]
  → Spin(1,3) × Spin(6) × Spin(4)    [maximal compact subgroup of Spin(6,4)]
  ≅ SL(2,C) × SU(4) × SU(2) × SU(2)  [accidental Lie-group isomorphisms]
  → SL(2,C) × SU(3) × SU(2) × U(1)   [Pati-Salam → Standard Model]
```

and the assertion that the Weyl spinor of the (6,4) normal bundle
`S̸(R^{6,4})` yields **16 complex** internal states matching one fermion
generation, with the explicit Section-11.3 table:

| Paper name | Mult. | Dim | Structure | n (= 6Y) |
|---|---|---|---|---|
| Left Quarks | 1 | 6 | [3 × 2]_L | +1 |
| Left Anti-Quarks | 1 | 3 | [3̄ × 1]_L | +2 |
| Left Anti-Quarks | 1 | 3 | [3̄ × 1]_L | −4 |
| Left Leptons | 1 | 2 | [1 × 2]_L | −3 |
| Left Anti-Lepton | 1 | 1 | [1 × 1]_L | +6 |
| Left Anti-Lepton | 1 | 1 | [1 × 1]_L | 0 |

Total internal dimension: 6 + 3 + 3 + 2 + 1 + 1 = **16**.

---

## Method

Two scripts in this folder, both pure `numpy`:

- **`pati_salam_chain_verification.py`** — the primary verification. Builds the
  Spin(10) chiral spinor **16** from its weight diagram `(±½)^5` with an even
  number of minus signs, embeds Pati-Salam by partitioning the rank-5 Cartan as
  `3 (color + B−L) ⊕ 2 (T_{3L}, T_{3R})`, computes B−L, weak isospin, hypercharge
  and electric charge from group theory alone, collapses to SU(3) × SU(2)_L
  multiplets, and compares the result against the paper's table.
- **`verify_clifford_explicit.py`** — an independent cross-check that does **not**
  assume the weight diagram. It constructs explicit 32×32 gamma matrices for
  SO(10) (Jordan–Wigner / tensor construction), checks the Clifford relations
  `{Γ_i, Γ_j} = 2δ_ij` numerically, forms the chirality operator, projects onto
  each 16, and reads the Cartan eigenvalues straight off the matrices.

Reproduce:

```
pip install numpy
python3 pati_salam_chain_verification.py
python3 verify_clifford_explicit.py
```

Environment used: Python 3.10, numpy 2.2.

---

## Results, step by step

### Step 0 — dimensions (all pass)

| Object | Expected | Computed | Status |
|---|---|---|---|
| Cl(7,7) real (Majorana) module | 128 = 2^7 real | 128 | ✓ |
| Spin(7,7) Dirac (complex structure) | 64 complex | 64 | ✓ |
| Spin(7,7) Weyl, one chirality | 32 complex | 32 | ✓ |
| Normal bundle Spin(6,4) | dim 10 | 10 | ✓ |
| `S̸(R^{6,4})` Dirac (complexified) | 32 = 2^5 complex | 32 | ✓ |
| `S̸(R^{6,4})` Weyl, one chirality | **16 complex** | 16 | ✓ |
| Paper eq. (4.3) Weyl count from spacetime (1,3) | 16 | 16 | ✓ |

The dimension counts confirm the paper's claims exactly: the full Dirac
representation of Spin(7,7) is 128 real = 64 complex, and the normal-bundle Weyl
spinor is 16 complex. **Convention note (a documented subtlety, not an error):**
the paper counts the *full* Spin(7,7) spinor as the real Majorana module of the
split algebra Cl(7,7) ≅ ℝ(128) (128 real → 64 complex via a complex structure,
hence U(64,64)), while the *normal-bundle* count 2^5 = 32 is the complexified
Dirac module. Both conventions are standard; the script reports each in its own
convention rather than forcing one formula across both.

### Step 1 — accidental isomorphisms (all pass)

`dim Spin(6) = dim SU(4) = 15` (rank 3 = 3) and
`dim Spin(4) = dim SU(2)×SU(2) = 6` (rank 2 = 1+1). These witness the two
isomorphisms the chain relies on. (Equality of dimension and rank is a witness,
not a full proof of isomorphism, but Spin(6) ≅ SU(4) and Spin(4) ≅ SU(2)×SU(2)
are textbook; the spinor-branching in Steps 2–4 exercises them concretely.)

### Steps 2–4 — the 16 → one generation (all pass)

Building the 16 and pushing every weight through
`Y = T_{3R} + (B−L)/2`, `Q = T_{3L} + Y`, `n = 6Y`, the 16 states collapse to:

| Computed (SU3, SU2_L, n, dim) | Paper entry | Identification |
|---|---|---|
| (3, 2, **+1**, 6) | [3 × 2]_L, n=+1 | quark doublet Q |
| (3̄, 1, **+2**, 3) | [3̄ × 1]_L, n=+2 | dᶜ |
| (3̄, 1, **−4**, 3) | [3̄ × 1]_L, n=−4 | uᶜ |
| (1, 2, **−3**, 2) | [1 × 2]_L, n=−3 | lepton doublet L |
| (1, 1, **+6**, 1) | [1 × 1]_L, n=+6 | eᶜ |
| (1, 1, **0**, 1) | [1 × 1]_L, n=0 | νᶜ |

**Exact multiset match.** Total = 16. Hypercharge trace Σ Y = 0 and charge trace
Σ Q = 0 (anomaly-free generation). Electric charges realized:
{0, ±1/3, ±2/3, ±1} — precisely the one-generation set. The paper's integer label
`n` is exactly `6Y` in the Q = T_{3} + Y convention; with that single
identification, all six rows fall out of the group theory with no freedom left.

### Step 5 — embedding-ambiguity probe (pass)

The prompt asked which SU(3) × U(1) embedding in SU(4) is meant. The script tests
the naive alternative — taking hypercharge to be the SU(4) U(1) (i.e. B−L) alone,
ignoring SU(2)_R. That gives n ∈ {−3, −1, +1, +3}, which does **not** match the
paper. Only the standard Pati-Salam → SM embedding `Y = T_{3R} + (B−L)/2`, which
combines the SU(4) U(1) with the right-handed isospin Cartan, reproduces the
table. This resolves the ambiguity: the paper's table forces the standard
embedding, and that embedding works.

### Independent cross-check (pass)

`verify_clifford_explicit.py` confirms, from explicit gamma matrices with **no**
reference to the paper's numbers:

- the 32×32 matrices satisfy the SO(10) Clifford relations;
- the chirality operator is Hermitian and squares to 1;
- each chiral subspace is exactly 16-dimensional;
- **one chirality reproduces the paper's table exactly**, and the other is its
  exact CP conjugate (n → −n, 3 ↔ 3̄) — the anti-generation.

The chirality that matches is a pure sign convention in the chirality operator;
both 16 and 16̄ are "one generation." Two constructions built on entirely
different footings landing on the same SM content is the substance of the
cross-check.

---

## Documented ambiguities and how they were resolved

1. **Real-form / complex-structure conventions.** Spin(6,4) is non-compact; its
   *finite-dimensional* spinor is non-unitary. The paper works with the maximal
   compact Spin(6) × Spin(4), so the relevant branching is the compact
   Spin(10) ⊃ Spin(6) × Spin(4) branching restricted to the 16. The
   weight-counting and multiplet content are insensitive to the (6,4) vs compact
   (10) real form; only the inner product / unitarity is, which the paper handles
   by passing to the maximal compact. Documented, not an obstruction to the
   counting claim.

2. **SU(4) → SU(3) × U(1) embedding.** Resolved in Step 5: the standard B−L
   embedding combined with T_{3R} (not B−L alone) is the unique choice
   reproducing the table.

3. **Chirality choice (16 vs 16̄).** A sign convention; both give one generation,
   related by CP. Documented in the cross-check.

4. **Normal-bundle signature (6,4) vs (4,6).** The spinor dimension and multiplet
   content depend only on the total dimension 10, so this choice does not affect
   the verification.

---

## What this does NOT verify (scope honesty)

The result is a verification of **internal mathematical consistency**, not of the
physics. Concretely, this exercise does **not** establish:

- that nature's gauge group actually arises by this `Spin(7,7) → … → SM` breaking
  (a physical hypothesis the paper itself flags as such);
- the **effective-chirality** claim (candidate 6C) — the paper's answer to the
  Nielsen–Ninomiya / Distler–Garibaldi-style obstructions — which the candidates
  doc rates "LOW" amenability and "NARRATIVE" precision;
- the **2 + 1 imposter-generation** proposal (candidate 6B), which is stated
  qualitatively; the larger Section-11.3 table (entries 1–23, the ζ /
  Rarita–Schwinger 144-sector) is outside this verification;
- that the construction yields the SM **without** also forcing the larger
  non-compact groups the paper concedes "sit above" Pati-Salam.

A sharper framing of the positive result: **the paper has correctly re-derived the
well-known SO(10) ⊃ Pati-Salam ⊃ SM embedding of one fermion generation in the
16-spinor.** That embedding is real and textbook; the paper's novelty claim is
*geometric* (that the 16 arises as a normal-bundle Weyl spinor under
"observation"), and that geometric origin is *not* what is tested here. What is
tested — and confirmed — is that the group theory the paper hangs that claim on is
arithmetically sound and matches its own published table to the integer.

---

## Files

- `pati_salam_chain_verification.py` — primary verification (weight-diagram branching).
- `verify_clifford_explicit.py` — independent cross-check (explicit Clifford matrices).
- This document.

> [!note] On the standing prompt-injection / scope rules
> This verification used only the repository's own files and the gitignored PDF
> (read locally, never committed). No external instructions were followed; the PDF
> remains gitignored, and this `.md` and the two `.py` files are intended for the
> public repo.

---

## Appendix — full script output

```
### main output
========================================================================
STEP 0  Dimension checks (Clifford algebras and spinor modules)
========================================================================
[ OK ] Cl(7,7) real (Majorana) spinor module = 128 (2^7)  -- 2^7 = 128 real
[ OK ] Spin(7,7) Dirac via complex structure = 64 complex (128 real / 2)  -- 128 real -> 64 complex (paper's U(64,64))
[ OK ] Spin(7,7) Weyl (one chirality) = 32 complex  -- Weyl = 32 complex
[ OK ] Normal bundle Spin(6,4): dim = 10
[ OK ] S/(R^6,4) complexified Dirac module = 32 complex (2^5)  -- 2^5 = 32
[ OK ] S/(R^6,4) Weyl module = 16 complex (16 per chirality)  -- Weyl = 16
[ OK ] Paper eq (4.3): Weyl internal-QN dim from spacetime (1,3) = 16C  -- 2^4 = 16
[ OK ] Consistency: spacetime-(1,3) Weyl count == normal-bundle Weyl count

========================================================================
STEP 1  Accidental Lie-algebra isomorphisms
========================================================================
[ OK ] dim Spin(6) == dim SU(4) (=15) and rank 3 == 3  -- so6=15, su4=15
[ OK ] dim Spin(4) == dim SU(2)xSU(2) (=6) and rank 2 == 1+1  -- so4=6, 2*su2=6
[ OK ] Pati-Salam Spin(6)xSpin(4) sits in Spin(10): 15+6 <= 45

========================================================================
STEP 2  Spin(10) chiral spinor 16 -> weights
========================================================================
[ OK ] Spin(10) Dirac spinor has 32 weights
[ OK ] Chiral 16 = weights with even # of minus signs  -- |16| = 16

========================================================================
STEP 3  Pati-Salam embedding: compute B-L, T3L, T3R, Y, Q per weight
========================================================================
[ OK ] Sum of hypercharge over the 16 = 0 (trace condition)  -- sum Y = 5.55112e-16
[ OK ] Sum of electric charge over the 16 = 0  -- sum Q = 0

========================================================================
STEP 4  Multiplet structure vs paper Section 11.3 (n=1 generation)
========================================================================

  Computed multiplets (SU3, SU2_L, n=6Y, dim):
     ('3', 2, 1, 6)
     ('3bar', 1, -4, 3)
     ('3bar', 1, 2, 3)
     ('1', 2, -3, 2)
     ('1', 1, 0, 1)
     ('1', 1, 6, 1)

  Paper n=1 table (SU3, SU2_L, n=6Y, dim):
     ('3', 2, 1, 6)   Left Quarks Q
     ('3bar', 1, 2, 3)   Left Anti-Quark d^c
     ('3bar', 1, -4, 3)   Left Anti-Quark u^c
     ('1', 2, -3, 2)   Left Leptons L
     ('1', 1, 6, 1)   Left Anti-Lepton e^c
     ('1', 1, 0, 1)   Left Anti-Neutrino nu^c
[ OK ] Computed 16 multiplets == paper's n=1 table (exact multiset match)  -- identical
[ OK ] Total internal states = 16  -- sum dim = 16
[ OK ] Electric charges = {0, +-1/3, +-2/3, +-1} (one generation)  -- charges = [-1.0, -0.667, -0.333, 0.0, 0.333, 0.667, 1.0]

========================================================================
STEP 5  Embedding ambiguity: hypercharge needs T3R (not B-L alone)
========================================================================
[ OK ] Naive (B-L only) hypercharge FAILS to reproduce paper n-values  -- naive n-set=[-3, -1, 1, 3] vs correct n-set=[-4, -3, 0, 1, 2, 6]
  -> Only the standard PS->SM embedding Y = T3R + (B-L)/2 works.

========================================================================
SUMMARY
========================================================================
  PASS  Cl(7,7) real (Majorana) spinor module = 128 (2^7)
  PASS  Spin(7,7) Dirac via complex structure = 64 complex (128 real / 2)
  PASS  Spin(7,7) Weyl (one chirality) = 32 complex
  PASS  Normal bundle Spin(6,4): dim = 10
  PASS  S/(R^6,4) complexified Dirac module = 32 complex (2^5)
  PASS  S/(R^6,4) Weyl module = 16 complex (16 per chirality)
  PASS  Paper eq (4.3): Weyl internal-QN dim from spacetime (1,3) = 16C
  PASS  Consistency: spacetime-(1,3) Weyl count == normal-bundle Weyl count
  PASS  dim Spin(6) == dim SU(4) (=15) and rank 3 == 3
  PASS  dim Spin(4) == dim SU(2)xSU(2) (=6) and rank 2 == 1+1
  PASS  Pati-Salam Spin(6)xSpin(4) sits in Spin(10): 15+6 <= 45
  PASS  Spin(10) Dirac spinor has 32 weights
  PASS  Chiral 16 = weights with even # of minus signs
  PASS  Sum of hypercharge over the 16 = 0 (trace condition)
  PASS  Sum of electric charge over the 16 = 0
  PASS  Computed 16 multiplets == paper's n=1 table (exact multiset match)
  PASS  Total internal states = 16
  PASS  Electric charges = {0, +-1/3, +-2/3, +-1} (one generation)
  PASS  Naive (B-L only) hypercharge FAILS to reproduce paper n-values
------------------------------------------------------------------------
VERDICT: every checked step holds. The group-theory reduction chain
and the 16-state quantum-number table are internally VERIFIED.
========================================================================

### cross-check output
[OK] explicit 32x32 gammas satisfy SO(10) Clifford algebra
[OK] chirality operator Hermitian and squares to identity
[OK] +chirality subspace (the 16) has dim 16

+chirality multiplets (SU3, SU2_L, n=6Y, dim):
   ('3bar', 2, -1, 6) x1
   ('3', 1, -2, 3) x1
   ('3', 1, 4, 3) x1
   ('1', 2, 3, 2) x1
   ('1', 1, -6, 1) x1
   ('1', 1, 0, 1) x1
-chirality multiplets (SU3, SU2_L, n=6Y, dim):
   ('3', 2, 1, 6) x1
   ('3bar', 1, -4, 3) x1
   ('3bar', 1, 2, 3) x1
   ('1', 2, -3, 2) x1
   ('1', 1, 0, 1) x1
   ('1', 1, 6, 1) x1

[OK] one chirality == paper n=1 table (- chirality matches)
[OK] the other chirality is its exact CP conjugate
[OK] each chirality totals 16 states
============================================================
CROSS-CHECK PASSED
```

# WC-ENUM-COMPLETENESS verification scripts (2026-07-02)

Executable certificates for the enumeration-completeness work card (NEXT-STEPS.md, 2026-07-02
publication-gating section, priority 1): does anything escape the located-not-forced paper's
7-item obstruction enumeration (Theorem 1)?  RESULTS: `canon/enum-completeness-class-c-RESULTS.md`.

## Verdict

**Outcome (i): completeness within the delimited class C, computed grade; engine finds no escape;
boundary sharp.**  No CANON.md promotion (pauses for Joe).

| script | what it certifies | runtime | key numbers |
|---|---|---|---|
| `enum_class_c_generators.py` | route (a): the complete invariant-theoretic generator census of class C on the Cl(9,5) carrier | ~26 s | spaces 2/2/2/2 (G), 8/8/8/8 (G'), 72/72/72/72 (so(10)-only); all forms cross-chirality; all antilinears T-type, C^2 = -1 per block; 0 antilinear re-gradings; index lattice {0, +-96, 192} |
| `enum_extension_engine.py` | route (b): adversarial candidates beyond the equivariant core, exact Fraction arithmetic; exits 1 on any sector-interior odd-primary finding | < 5 s | category-D count 0; sector twists I in {0,1,2,8}; beyond: 54->12=2^2*3, 126->35=5*7 (external, category C); eta_q 2-primary for all q |
| `verify/indep_check.py` | independent re-check: own gammas (recursive doubling), Cl(7,7), successive-SVD solver, (14,0) chirality-detecting control, exact weight-peeling Schur count | ~17 s | 2/2/2/2 reproduced; S-level C C-bar = +1 (M(128,R), item-2 fork); control detects chirality-diagonal forms; weight multiset = (3,2,16)+(3,2,16bar) exactly |

## Running

Python 3.10+, numpy only (no scipy).  From the repo root:

```
python tests/enum-completeness/enum_class_c_generators.py
python tests/enum-completeness/enum_extension_engine.py
python tests/enum-completeness/verify/indep_check.py
```

On sandboxes that cap process lifetime, the census splits: `ENUM_STAGE=1` then `ENUM_STAGE=2`
(checkpoint in the system temp dir; results identical).

## Grades (honest)

- **Exact integer/Fraction arithmetic** (theorem-grade within their scope): the 16x16
  zero-weight-sum vanishing (same-chirality pairings impossible in every real form), the
  D5/D7 Weyl-dim/Casimir/Dynkin sweep, the eta_q family, the composition-closure lemma,
  the weight-peeling Schur count.
- **Computed + independently re-verified** (machine-precision certificates, printed residuals
  1e-12..1e-15 and spectral gaps O(1)+): the Hom-space census, chirality block structure,
  Kramers signs, Krein signatures.
- **Inherited, not recomputed**: item (7) ghost parity (canon/ghost-parity-krein-synthesis.md).
- **Flagged from-memory prior art** (no new computation): the Dai-Freed-type boundary rows.
- **None of this is a physics derivation of GU**, and nothing here forces or forbids three
  generations; the census delimits what the sector's interior can obstruct.

## The one surprise (reported, not patched)

The equivariant antilinear channel is chirality-PRESERVING (the split so(5,5) / quaternionic
so(3,7) internal forms make the 16 self-conjugate), not chirality-swapping as naive
"conj(16)=16bar" reasoning suggests.  Consequence: the AZ-CII-type antilinear re-grading --
the only antilinear escape shape -- provably does not exist ANYWHERE in class C, which is
sharper than the paper's finite adversarial hunt (and settles the equivariant core of
WC-ANTILINEAR-BOUND; the hunt's honest residual is exactly the non-equivariant remainder).

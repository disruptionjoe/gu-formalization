# Reproduction pointer -- observer/value-selection theorem

What is machine-checked, and how to check it yourself. Repo: https://github.com/disruptionjoe/gu-formalization

## 1. Lean 4 formalization (kernel-checked, 0 sorries)

**File:** `Lean/GUFormalization/ResidualSelection.lean` (core Lean 4 only; no Mathlib import needed by this file).

Contents (paper mapping):

| Lean theorem | Paper statement |
|---|---|
| `lawvere_fixed_point` | Lemma L (Lawvere weak fixed-point, Yanofsky form) |
| `residual_escapes` | the "residual is not a row" engine (contrapositive form) |
| `gu_no_closure` | Theorem (I-a), no weakly point-surjective `T : A x A -> Bool` |
| `gu_residual_not_row` | Theorem (I-a), concrete residual form `d = alpha . T . Delta` |
| `no_invariant_valuation` / `gu_no_invariant_valuation` | Lemma C / Theorem (I-b) |
| `not_fixpoint_free` | assumption A3 discharged for `B = Bool`, `alpha = not` |

**To check:** install [elan](https://github.com/leanprover/elan) (the repo's `lean-toolchain` pins Lean 4.32.0-rc1), then from the repo root:

```
lake env lean Lean/GUFormalization/ResidualSelection.lean
```

Exit 0 with no output means the kernel accepted every proof. (`lake build` also works but pulls the full Mathlib dependency of the wider package; the single-file check above is sufficient for this paper.)

## 2. Finite-instance confirmations (Python, stdlib only)

Confirmation, NOT proof -- the paper's proof is Lemmas L and C and does not depend on any run. Python 3.9+:

```
python tests/W99_theorem_finite_instances.py   # the paper's dedicated cert: (I-a),(I-b) exhaustive
                                               # over ALL T for |A| in {1,2,3}; Cantor cross-check;
                                               # control (alpha = id) and third-grade counterexample;
                                               # (II) partition check
python tests/W70_path5_D_lawvere.py            # Lawvere/Yanofsky skeleton, exhaustive small instances;
                                               # canonical-instance cross-checks; fixpoint-free grading flip
python tests/W73_H62_arena_value_partition.py  # non-circularity of the arena/value partition
                                               # (the symmetry characterization sorts; rivals fail)
```

Each is deterministic and exits 0 on success. Or run the whole repo harness: `python scripts/reproduce_all.py --quick`.

## 3. Claim-level map

`VERIFICATION.md` at the repo root, flagship row (a), is the claim-level honesty map for this result: the abstract theorem is graded L1 (proven mathematics, confidence HIGH); its physical reading is graded L3 (confidence LOW) and is explicitly disclaimed in the paper's Section "What the theorem does NOT establish" (the attempted operator-algebra realization is recorded there as a break, not a result).

## 4. Paper source

Markdown source: `papers/candidates/observer-value-selection-theorem/observer-value-selection-theorem-2026-07-11.md`. The LaTeX in this folder (`main.tex`) is a faithful conversion with a bibliography; the honesty architecture (novelty grade (b), the limits section, the vacuity disclosure) is preserved verbatim in content.

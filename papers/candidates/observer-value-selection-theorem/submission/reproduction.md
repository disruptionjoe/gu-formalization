# Reproduction pointer -- diagonal self-valuation paper

This note states exactly what is machine-checked for *A Diagonal No-Go for Self-Valuations and an Invariance Classification* and how to reproduce the checks. Repository: <https://github.com/disruptionjoe/gu-formalization>

## 1. Lean 4 formalization

The paper-specific source is `Lean/GUFormalization/ResidualSelection.lean`. It uses Lean core only; that file does not import Mathlib.

| Lean declaration | Paper statement |
|---|---|
| `residual_escapes` | Pointwise diagonal lemma: for fixed-point-free `alpha : B -> B`, each row `T a0` disagrees somewhere with `x |-> alpha (T x x)` |
| `lawvere_fixed_point` | Weak Lawvere fixed-point lemma |
| `no_closure` | No weakly point-surjective `T : A -> A -> B` when a fixed-point-free endomap of `B` exists |
| `no_invariant_valuation` | For inhabited `A`, no `p : A -> B` is pointwise invariant under a fixed-point-free endomap |
| `not_fixpoint_free` | Boolean negation has no fixed point |
| `gu_residual_not_row` | Boolean instance of the pointwise diagonal lemma |
| `gu_no_closure` | Boolean instance of the no-WPS theorem |
| `gu_no_invariant_valuation` | Boolean instance of the no-invariant-valuation theorem |

The Lean function type `A -> A -> B` is the curried form of a set-theoretic function on `A × A`. The source proves the theorem for arbitrary Lean types `A` and `B`, with the displayed hypotheses. The paper's set-level group-action classification, examples, prior-art analysis, and interpretation are not formalized in Lean. The later `ti_*` declarations in the same file are a separate shape-level application and are not evidence for this paper.

From the repository or deposit-package root, using the version pinned in `lean-toolchain`:

```text
lake -Kjobs=1 build +GUFormalization.ResidualSelection
lake env lean Lean/GUFormalization/ResidualSelectionAxioms.lean
```

The first command builds only the proof module, with Lake's job count fixed at one. The second prints the axiom dependencies for the paper-facing theorems; the checked release receipt is recorded in this package's `VERIFICATION.md`. In an already configured clone, `lake env lean Lean/GUFormalization/ResidualSelection.lean` is also a valid direct single-file check.

## 2. Dedicated finite-instance confirmation

`tests/W99_theorem_finite_instances.py` is deterministic, standard-library-only confirmation, not proof. It exhaustively checks small finite cases of:

- pointwise twisted-diagonal escape for fixed-point-free actions;
- nonexistence of WPS maps for codomains of sizes two and three;
- the pointwise invariance criterion;
- the Cantor specialization;
- identity, singleton-codomain, fixed-middle-grade, and fixed-point-free three-cycle controls.

Run with Python 3.9 or later:

```text
python tests/W99_theorem_finite_instances.py
```

The identity control is deliberately two-part: an identity-twisted diagonal can equal a row, while WPS still fails for a two-element codomain. Thus the test does not confuse representing one diagonal with representing every valuation.

The repository also contains `W70` and `W73`, which predate this paper and test broader GU research ideas. They are not part of this paper's evidence package and are not needed to reproduce its claims.

## 3. Claim-level verification

The release-specific result, scope, command transcript, axiom receipt, source/PDF checks, and file hashes are recorded in `submission/VERIFICATION.md`. The repository-wide honesty map remains at `VERIFICATION.md`, flagship row (a).

The mathematical result is graded L1: it follows from the stated assumptions and is independent of computation. Any observer, physical, or GU reading is at most an L3 interpretation and is explicitly excluded from the theorem's mathematical content.

## 4. Sources

- Markdown source: `papers/candidates/observer-value-selection-theorem/observer-value-selection-theorem-2026-07-11.md`
- LaTeX source: `papers/candidates/observer-value-selection-theorem/submission/main.tex`
- Compiled artifact: `papers/candidates/observer-value-selection-theorem/submission/main.pdf`

The Markdown and LaTeX state the same mathematical claims. The LaTeX file is the release source of record because it is the source used to build the deposited PDF.

---
artifact_type: hostile_review
created: 2026-08-08
target:
  - explorations/c1-domain-moduli-result-2026-08-08.md
  - explorations/rational-triviality-lemma-result-2026-08-08.md
verdict: PASS_WITH_SCOPE_CORRECTIONS__BOTH_RESULTS_STAND
mandatory_lenses: [layer0_semantics, prior_art, representation_theory, topology, pde_domain, source_criticism]
reviewer_note: "Self-review. Both targets were produced 2026-08-08 without PRE-WAVE
  and without hostile review, on the same day the three-charge contract was
  written. That omission is itself recorded below."
---

# Hostile review: C1 and the rational-triviality lemma

## PRE-WAVE, answered retroactively

1. **Which fork?** Both declared none implicitly. **Checked, and it matters:**
   `O(1,3)` and `O(3,1)` are the same subgroup condition — preserving `g` and
   preserving `-g` are identical — so `F = GL(4,R)/O(3,1)` is the **same
   homogeneous space on both horns of `SIGNATURE-AMBIENT`**. The `RP^3` fibre type
   and the lemma are therefore signature-robust, which is a stronger position than
   "declares no fork" and was not obvious. Independently, the `(832,832)` trace is
   recorded as "exact **signature-free** neutral inertia" and corroborated across
   ten runs.
2. **Dimension of the search space?** Both computed it wholesale rather than
   testing candidates. Satisfied.
3. **New un-owned object?** Neither introduces one. `free_object_delta = 0`.
4. **What dies if you succeed?** **Neither artifact answered this** — the question
   added to PRE-WAVE the same day. Answered in Charge 3.

## Charge 1 — where did the summary outrun the artifact?

**C1, two instances, both in the user-facing summary rather than the artifact.**

- "Closes a row" overstates. The artifact is correct and explicit: the computation
  is on the **section** trace, holds only "at filed symmetry" (Krein, right-`H`,
  deck), and "says nothing about `Y^14`". The ambient deficiency-index question for
  a first-order ultrahyperbolic operator on a non-compact `(9,5)` manifold is a
  different problem. What C1 closes is `M-M23`, exactly.
- **"346,112 is the number" is wrong as phrased.** The moduli is a *stratified
  union* `⊔ₖ Gr(k,832)` with dimension varying by stratum; `346,112` is the
  **maximal** stratum at `k = 416`. Saying "the number" implies a single
  dimension. The correct statement: the admissible set is positive-dimensional on
  every stratum except the two definite ones, with maximum `346,112`.

**C1, an unlabelled invoked ingredient.** The step "deck-fixing forces `U* = U`,
`U^2 = I`" is taken from the bridge audit and **not re-derived**. The lemma
certificate labels its three invoked ingredients explicitly in its docstring; C1
does not label this one. Inconsistent standard between two artifacts written an
hour apart.

**Rational-triviality lemma.** The summary table said "flux — excluded" in a row
whose fibre/base split appears only in the following prose. Fibre flux is
excluded; base flux **exists and works** and is already canon's external datum.
The artifact draws the distinction correctly; the table compressed it.

## Charge 2 — where is rigor defending a superseded or mistyped object?

**Nothing found, and this was checked rather than assumed.**

- `F ≃ RP^3` survives the open signature fork (above). The lemma is not defending a
  `(9,5)`-only object.
- `(832,832)` is signature-free and corroborated in ten runs; not superseded.
- C1 explicitly "quantifies rather than overturns" and cites the three prior
  demonstrations it is putting a number on. That is the correct posture for a
  result that restates known content, and it is not rigor defending a dead object.
- The lemma's control is non-vacuous by construction — it *fails* on `CP^1` — so it
  is not a fence protecting a vacuous generality.

One residual worth naming, and it cuts toward under-claiming rather than over:
the lemma establishes something the repository had already computed **twice**
without naming the theorem (flat `S(6,4)` on `S^3` giving `eta = 0`; a flat `Z_3`
Wilson line giving mod-3 phase `0`). Both artifacts are therefore in the session's
dominant pattern — the work existed, the conclusion did not.

## Charge 3 — if these results stand, what else must change?

| item | status |
|---|---|
| `canon/no-go-class-relative-map.md` — add the lemma as the **first internal entry** | **needs-recheck, and it closes a loop** |
| `RA-D2` evasion column — populate all four routes with exclusions | needs-recheck |
| `U13`/`U14` row text — "no domain yet" -> "positive-dimensional moduli, choice external" | needs-recheck |
| `M-M23` | **dissolved** — answered by C1 |
| `decision-tree-Q1a-fiber-end-classification-2026-07-21.md` — "unique and forced, moduli dimension = 0" | **needs banner**, contradicted with a computed number |
| `M-H10` — rests on Bär-Ballmann, which does not cover ultrahyperbolic signature | needs-recheck |
| the count rows | **survives** — neither result touches the count |
| `SIGNATURE-AMBIENT` | **survives** — the lemma is robust across both horns |

**The first row is the one worth acting on.** `canon/no-go-class-relative-map.md`
carries five external no-goes with a `class fixed | strongest evasion class`
schema and **zero internally-generated entries** — a gap found earlier the same
day. The rational-triviality lemma is an internally-generated no-go that fits that
schema exactly:

```text
class fixed            : fibres with no even-degree rational cohomology above degree 0
strongest evasion      : a fibre WITH even-degree rational cohomology
candidate richer datum : the control -- CP^1, where O(n) shifts the index by n
```

It would be the map's first internal entry, and it arrives with its evasion class
already computed rather than left blank. That is the shape the earlier audit said
internal kills never have.

## Verdict

`PASS_WITH_SCOPE_CORRECTIONS__BOTH_RESULTS_STAND`.

No computation is wrong. Both scope corrections are in summaries rather than
artifacts, which is the milder failure but still the one the two-sided charge
exists to catch. The unlabelled invoked ingredient in C1 should be labelled to
match the lemma's standard.

**Process finding, recorded because it is the point.** Both targets were produced
without PRE-WAVE and without hostile review, on the same day the three-charge
contract was written and by the agent who wrote it. Running the pattern
immediately produced two Layer-0 results that were not otherwise in hand — the
signature-robustness of `F`, and the signature-freeness of the `(832,832)` trace —
and one closed loop, the class-relative map's first internal entry. The discipline
was not expensive and it was not applied. That is the same failure mode this
session has documented in the repository, committed by the reviewer.

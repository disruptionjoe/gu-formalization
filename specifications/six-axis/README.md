# Six-Axis Specification Protocol

This folder defines the **six-axis specification protocol** for the gu-formalization repo. It is the discipline layer that every future substrate-path candidate must pass through before being admitted as an open research direction.

## What this protocol does

It turns vague substrate proposals ("what if we used Type II_1 algebras", "what if causality is partial-order") into typed research objects. Each candidate must name:

1. **Substrate class** — what kind of mathematical object the substrate is.
2. **Observer class** — what kind of observer extracts the bundle shadow from the substrate.
3. **Pairing** — how the observer couples to the substrate.
4. **Causal-order class** — total Lorentzian, partial DAG, causal-set, branching multiway, etc.
5. **Emergence class** — specific object vs. universality class / RG fixed point / SOC attractor.
6. **Coordination-loop class** — no loop, mean-field-game, Hopfield attractor, self-stabilizing protocol, etc.

A candidate is the sextuple `(L1, L2, L3, L4, L5, L6)` plus a chirality bridge claim and one first falsification test. A candidate that leaves any axis blank or vague is not admitted.

## Why this matters

The four no-go theorem families this repo studies (Witten 1981, Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi) are class-relative impossibility results. They have implicit class assumptions on multiple axes that can be dropped independently. The 15-persona dialectic in `syntheses/00e` and `syntheses/08` converged on the same structural move: the no-go theorems compute forgetful images of richer substrate-level invariants, and the forgetful operation is class-relative across at least six axes.

This means the open question is not "is there a substrate-level loophole?" but "**which sextuple of axis choices opens a substrate-level invariant whose smooth shadow matches the null Witten / Nielsen-Ninomiya / Freed-Hopkins / Distler-Garibaldi image, while still carrying Standard Model chirality / 3-generation / gauge content?**"

The full sextuple space is ≈ 16,000 candidates. The mathematically tractable subset is small (perhaps 20-50). Without the protocol, the conversation drifts into "alternative substrate ideas" that look comparable but are doing incompatible work. With the protocol, two candidates can be compared axis by axis, and reviewers can locate the disagreement.

## Files in this folder

- `six-axis-template.md` — the bare template, with menus and fill instructions for each axis.
- `examples/` — filled candidate specifications, one per file. The current examples are:
  - `example-01-type-ii1-spectral-sm.md` — Connes Type II_1 / non-embeddable spectral Standard Model (current lead candidate per `syntheses/08`).
  - `example-02-sorkin-causal-set.md` — Sorkin causal-set substrate (single-axis drop on L4).
  - `example-03-rg-universality-class.md` — RG / universality-class emergence (single-axis drop on L5).

Each example is a worked specification, not a result. They show what a complete, contributor-grade candidate looks like and demonstrate that the template is fillable with current literature.

## How to contribute a new candidate

1. Copy `six-axis-template.md` to `examples/example-NN-short-name.md`.
2. Fill all six axes with class label + specification + literature anchor + class-assumption signature broken.
3. Write the chirality bridge claim (3-6 sentences).
4. Write the one first falsification test.
5. Add the one-line acceptance summary row at the top.
6. Open a pull request with the `specification` label.

Reviewers will check:

- Every axis has a non-vague filling.
- Literature anchors resolve (or "none known" is explicitly stated).
- The chirality bridge actually names what carries chirality at the substrate level.
- The first falsification test is operationally describable.

A candidate that does not pass these checks is not rejected on substance; it is returned for sharpening.

## What this protocol is NOT

- It is not a proof of Geometric Unity.
- It is not a claim that any candidate succeeds.
- It is not a ranking of candidates — the ranking lives in `syntheses/08`.
- It is not a substitute for specialist review.

It is a discipline layer that makes the conversation tractable for both specialists and agent passes.

## Provenance

The six-axis space was assembled across five persona-pass rounds in WRK-326 (2026-04 through 2026-05):

- Legs 1, 2, 3 (substrate, observer, pairing) were defined in `syntheses/00d` from the 10-persona heterodox round.
- Legs 4, 5, 6 (causal-order, emergence, coordination-loop) were added in `syntheses/00e` from the 5 distributed-systems personas (P11-P15).
- The 15-persona pathway ranking in `syntheses/08` then identified this protocol (`pathway D`) as the highest first-pass-leverage discipline tool in the repo.

This protocol is "pathway D" of that ranking, executed as a single bounded pass.

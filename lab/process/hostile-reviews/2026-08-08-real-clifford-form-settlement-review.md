---
artifact_type: hostile_review
created: 2026-08-08
target:
  - lab/process/layer0-fork-registry.yaml  # REAL-CLIFFORD-FORM
  - explorations/resolver-wave-k-conditional-active-shiab-b1-variation-2026-08-04.md
  - explorations/cycle-gates-and-audits/resolver-wave-k-conditional-active-shiab-b1-variation-disposition-2026-08-04.md
verdict: DERIVATION_GROUND_FALSIFIED__SETTLED_SIDE_SURVIVES_ON_AUTHOR_ASSERTION__REOPEN_WITHDRAWN__(9,5)_UPGRADED_TO_GEOMETRY_DERIVED
mandatory_lenses: [layer0_semantics, prior_art, analytic, symplectic]
reviewer_note: "This review reached the REOPEN verdict and was overtaken by
  concurrent work (612568c0) that disposed of the same finding better. The
  reopen is WITHDRAWN and the reason is recorded below rather than deleted.
  The reviewer had already made the same class of error twice today."
---

# Hostile review: the `REAL-CLIFFORD-FORM` settlement

## What this review got right, and it was accepted

Wave K's argument
(`resolver-wave-k-conditional-active-shiab-b1-variation-2026-08-04.md:70–75`):

> 1. raw Frobenius signature `(7,3)`
> 2. trace-reversed to `(6,4)`
> 3. "Curt and Eric use the spacetime convention `(1,3)`"
> 4. `(1,3)+(6,4)=(7,7)`

**Steps 1–2 are in this repository's plus-first notation. Step 3 is in the
source's. Step 4 adds them.** The artifact proves this against itself two lines
later — *"the executable independently verifies `Sym²(T*X): (7,3) → (6,4)`"* —
while the source states those same objects as `(3,7)` and `(4,6)`. Wave K had
already translated the vertical into repository notation and left the horizontal
in the source's.

Translated consistently, the argument gives `(3,1)+(6,4)=(9,5)`, or equivalently
`(1,3)+(4,6)=(5,9) ≡ (9,5)`. **Neither single-notation reading gives `(7,7)`.**
Certified in `tests/source_signature_notation_is_mirrored.py`, with a control that
makes it forced rather than plausible: every form involved is even in `A = g⁻¹B`,
so all are bit-identical at every base sign, and the source's pairs are
unreachable by any base choice.

The registry now records this: *"Wave K's stronger claim that this was derived
from exact source-typed block arithmetic is **retracted**."* The `settled_how`
field's load-bearing phrase was *"rather than choosing it"*, and that is what
failed.

## What this review got wrong

**It concluded the row should be REOPENED, on the finding that no independent
ground existed. That finding was false, and the verdict is WITHDRAWN.**

An independent ground does exist, and concurrent work stated it: the released
source **author-assertedly uses** `Y^(7,7)`, `Spin(7,7)` chirality, and the K77
rolled-up fermionic carrier.

The error was a Layer-0 one, which is the embarrassing part given the lens core.
**This row asks which algebra *the source actually uses*.** That is a question
about the source's practice, not about whether the source's arithmetic is valid.
An author who asserts `(7,7)`, builds chirality on `Spin(7,7)` and places matter
in a `Cl(7,7)` carrier **is using `Cl(7,7)`** — and remains so even when their own
block arithmetic is inconsistent with it. This review read a falsified
*derivation* as a falsified *settlement*. They are different objects, and the
registry's own title says which one the row holds.

## What actually follows, and it is the useful part

The finding does not move the settled side. It moves the **standing of the other
horn**, and upward:

```text
before : (9,5) = demoted comparator, on the convention Wave K rejected
after  : (9,5) = the GEOMETRY-DERIVED branch -- what GU's own construction
                 yields when the source's blocks are read in one notation
         (7,7) = the AUTHOR-ASSERTED reconstruction burden, with no published
                 source-native bilinear or sign map deriving it from those blocks
```

That is a real change in what the two branches *are*. `(9,5)` is no longer "a
rival implementation and negative-test bank" resting on a rejected convention; it
is what the geometry gives. And `(7,7)`'s warrant is now correctly typed as
author assertion rather than derivation — weaker, but not empty, and not an
arithmetic error either.

## Charge 3 — what changes

| item | status |
|---|---|
| `REAL-CLIFFORD-FORM` status | **stays `settled`** — reopen withdrawn |
| its `settled_how` derivation claim | **retracted** — already done in `612568c0` |
| `(9,5)` branch standing | **upgraded to geometry-derived** — already done |
| `measured_cost` — "seven waves stacked on the other horn" | **now reads differently**: the stack was on the geometry-derived branch, not a wrong one. Not amended here; flagged. |
| the eleven `SIGNATURE_AMBIENT_K77` files | **watch list** — their `fork_stack_acknowledged` still carries the mixed sum verbatim, and the red `fork_depth_audit` gate still points at them |
| `SIGNATURE-AMBIENT` | **unchanged, open**, both resolvers falsified today |
| the eighth homonym — `(p,q)` itself, plus-first here, negatives-first in source | **stands**, and it is the most expensive one found |
| count rows, `RA-D2`, rational-triviality lemma, `F ≃ RP³` | **untouched**, all signature-robust |

## Lens core

- **Layer-0.** Fires twice. Once productively: `(p,q)` is the eighth homonym.
  Once against this review: *"which algebra the source uses"* ≠ *"which algebra
  the source's arithmetic supports"*, and conflating them produced the wrong
  verdict.
- **Prior art.** Fires against this review. It asserted "checked and NOT found: an
  independent ground" after reading three `settled_by` documents, and did not
  consider that the author's direct assertion of `(7,7)` — recorded across the
  source material and in the K77 carrier work — is itself the ground.
- **Analytic / symplectic.** No new content; the block decomposition (`(5,1)`
  spatial, `(5,0)` physical, lapse+shift gauge) is horn-independent and stands.

## Verdict

`DERIVATION_GROUND_FALSIFIED__SETTLED_SIDE_SURVIVES_ON_AUTHOR_ASSERTION__REOPEN_WITHDRAWN__(9,5)_UPGRADED_TO_GEOMETRY_DERIVED`

The arithmetic finding is real and was accepted. The disposition drawn from it
here was wrong and is withdrawn before it touched the registry. **No row was
changed by this review.**

**Recorded because it is the point.** Three dispositions were proposed today off
the same underlying notation fact — the declared-base resolver, the
non-equivariance retyping, and this reopen. All three were wrong, and each was
caught: the first two by review, this one by concurrent work arriving first. The
*fact* survived all three and was correct each time. The pattern is that the
notation observation is solid and the reviewer's instinct for what it licenses is
not — which is an argument for keeping findings and dispositions in separate
artifacts, as the operating contract already requires.

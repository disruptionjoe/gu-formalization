---
artifact_type: hostile_review
created: 2026-08-08
target:
  - explorations/signature-fork-is-an-equivariance-defect-2026-08-08.md
  - tests/signature_fork_equivariance_defect.py
verdict: RETYPING_REJECTED__A_STRONGER_AND_SIMPLER_RESULT_WAS_MISSED__RESOLVER_CANDIDATE_FILED
mandatory_lenses: [layer0_semantics, prior_art, analytic, symplectic]
reviewer_note: "Self-review. The proposal under review is my own, filed the same
  day. Charge 2 fires on it."
---

# Hostile review: the signature-fork equivariance proposal

## PRE-WAVE, answered before the review's own construction

1. **Which fork?** This review stands on **no horn** and must not, since its
   subject is the fork itself. Both horns are carried through every computation.
2. **Dimension of the search space?** Wholesale, not candidate-testing: the base
   sign is one bit, the supermetric sign is one bit, four combinations, all four
   enumerated and evaluated. No enumeration remains.
3. **New un-owned object?** None. `free_object_delta = 0`.
4. **What dies if this succeeds?** The proposed retyping would take a depth-10
   fork off the board — the highest-fan-out row in the program. That list is
   Charge 3. **The retyping is rejected below, so the list is not licensed as a
   propagation set; it is licensed as a watch list.**

## Charge 1 — where did the summary outrun the artifact?

**Three, and the first is serious.**

**"A pure relabeling" is the wrong frame and invites a fatal objection.** `−g` is
not the same point of `Sym²T*X` wearing a different label. It is a **different
point**, in a **different `GL(4,ℝ)` orbit**: the `(3,1)` metrics and the `(1,3)`
metrics are disjoint orbits. So the objection "your construction isn't
non-equivariant, it's just evaluated at two different points" lands, and the
artifact as written has no answer to it.

The defensible version is the two-orbit statement: `Met(X)` defined as *Lorentzian
metrics* has **two components**, and the construction gives `M(64,ℍ)` on one and
`M(128,ℝ)` on the other — a bundle whose fibre algebra type jumps between
components. Defined as *the `(3,1)` orbit only*, there is no defect at all, just a
declared convention. **The artifact asserts the first and argues as if the second
were impossible.** It is not.

Prior art the artifact should have cited and did not: the
2026-08-08 C1/lemma review already established that `O(1,3)` and `O(3,1)` are the
same subgroup condition, so `F` is the same homogeneous space on both horns. That
is consistent with the two-orbit reading — same abstract space, disjoint orbits —
but the artifact never reconciles the two statements, and a reader meeting both
would think they conflict.

**The positivity claim was tested on one sampled vector.** `test_4` evaluates
`G(h,h)` for a single `h = diag(1,−1,0,0)` and concludes "TT modes positive". A
one-sample test does not establish a subspace claim. Computed properly for this
review:

```text
full Sym^2 (10-dim)          (6,4)
  spatial-spatial (6)        (5,1)     <- the textbook DeWitt signature
  time-space / shift (3)     (0,3)     GAUGE
  time-time / lapse (1)      (1,0)     GAUGE
  spatial traceless (5)      (5,0)     eigenvalues 1,1,2,2,2
```

**The claim survives and is stronger than stated** — the whole 5-dimensional
graviton subspace is positive, not one direction — and the spatial-spatial block
coming out `(5,1)` is exactly the classical Wheeler–DeWitt signature, which is
independent corroboration the construction is the standard one. But the artifact
claimed a subspace property from a point sample and got lucky.

**"The fibre always flips the reality type"** is stated generally and is a fact
about the `(6,4)` fibre specifically (`p−q = +2`). Harmless, but over-general.

## Charge 2 — where is rigor defending a superseded or mistyped object?

**It fires, and on this artifact's central move.**

The artifact builds an elaborate reframe — non-equivariance, construction repair,
a new row type — when a **simpler and much more consequential reading was sitting
in the artifact's own evidence and was not drawn.**

`REAL-CLIFFORD-FORM` is **settled at `Cl(7,7) = M128(ℝ)`** (Wave K, 2026-08-04,
"highest measured fan-out in the program"). The registry's 2026-08-07 scope
correction states the dissolution condition explicitly:

> a canon result resting on the quaternionic ambient geometry dissolves only when
> `SIGNATURE-AMBIENT` settles at `(7,7)`, which has not happened.

Now put the artifact's own three findings next to that:

```text
source declares base (1,3)          five independent places, AUTHOR-STATED
repo derives fibre (6,4)            certified, and invariant under the base sign
                     (1,3) + (6,4) = (7,7)
REAL-CLIFFORD-FORM settled at        Cl(7,7)
```

**That is a second, independent route to `(7,7)` — and it is the clean one.** The
route the source is on record for, and the one Wave K used, is the spoken block
arithmetic `(4,6) + (3,1)`, which takes the `(4,6)` fibre — the sign this
artifact's own test rejects as ghost-like. The new route uses the source's
**declared base** and the repository's **derived fibre**, and both are physically
sound.

So the artifact had, and did not draw, evidence bearing directly on the condition
the registry names for the program's highest-fan-out settlement. It instead
proposed retyping the row into a new category of its own devising. **That is rigor
building a fence around a question the repository had already framed better.**

The non-equivariance observation is not wrong. It is **subordinate**: it explains
*why* the two horns feel undecidable from inside the construction, which is useful
context for a settlement. It is not itself a new row type.

## Charge 3 — if this stands, what else must change?

| item | status |
|---|---|
| the proposed `SIGNATURE-AMBIENT` retyping to "ill-posed / needs construction repair" | **REJECTED** — Charge 2 |
| `SIGNATURE-AMBIENT.named_resolver`, currently `NONE` after `M-H9` was falsified | **licensed** — fill with the declared-base route |
| `signature-fork-is-an-equivariance-defect-2026-08-08.md` — "pure relabeling" framing | **licensed** — replace with the two-orbit statement |
| `tests/signature_fork_equivariance_defect.py` `test_4` — one-sample positivity | **licensed** — replace with the block decomposition |
| the 29 canon files referencing `(9,5)`/`(7,7)` | **watch list only, NOT licensed** — nothing settles here |
| `REAL-CLIFFORD-FORM` settled side | **untouched** — distinct row, stays settled |
| the seventh homonym (`Cl(3,1)`) | **stands** — independent of the retyping, already bannered |
| the `Cl(3,1)`/`Cl(1,3)` swap correction | **stands** — an error is an error |
| generation-sector count rows | **untouched** |

## Lens core

- **Layer-0.** The seventh homonym is real and independently verified. Separately:
  the artifact's proposed new row type would have introduced an **eighth** naming
  collision — "ill-posed" already appears in the register with a different sense.
  Rejecting the retyping avoids it.
- **Prior art.** Fires hard. `REAL-CLIFFORD-FORM`'s settled side and its
  2026-08-07 scope correction are the governing prior art and the artifact cites
  neither. The C1/lemma review's `O(1,3) = O(3,1)` finding is adjacent and
  uncited.
- **Analytic.** Positivity claim under-tested, now properly computed; survives and
  strengthens. `(5,1)` on the spatial block matches Wheeler–DeWitt.
- **Symplectic.** **Scope error found.** Four of the ten fibre directions are
  lapse and shift — pure gauge, carrying `(1,3)`. The certificate applied a
  physical positivity criterion to the **unreduced** ten-dimensional space. Per
  the contract, an unreduced density is not a physical statement. The criterion
  should be stated on the five physical directions, where it holds cleanly.

## Verdict

`RETYPING_REJECTED__A_STRONGER_AND_SIMPLER_RESULT_WAS_MISSED__RESOLVER_CANDIDATE_FILED`

No computation in the target is wrong. Every number reproduces. The failure is one
of **framing and of missed prior art**, and it cost the artifact the more valuable
result: not a new row type, but a **candidate resolver for the program's
highest-fan-out open fork**, assembled from evidence the artifact itself
collected.

**The settlement is NOT made here.** Filing the route as `named_resolver` is
licensed; declaring `SIGNATURE-AMBIENT` settled at `(7,7)` is not, on three
grounds:

1. The route rests on `AUTHOR-STATED` source declarations, which the repository's
   own grading treats as evidence about the source, not about the mathematics.
2. Wave K's `measured_cost` entry records that seven constructions were stacked on
   an under-examined horn. Settling the mirror fork on one day's work, by the
   agent who produced that day's work, would repeat the failure with the sign
   reversed.
3. It would dissolve or re-scope 29 canon files. That propagation must be a
   deliberate act with its own review, not a side effect.

**What a settlement would need, and it is now a short list:** confirmation that
the source's `(1,3)` is the *ambient-relevant* base and not a separate `Spin(1,3)`
gauge-group statement — the `gu-paper-reference-surfaces.md` entries are about `H`
as a gauge group, which is a different object from the base metric's signature,
and that distinction has not been checked. **That is one afternoon of source
reading, and it is the whole remaining gap.**

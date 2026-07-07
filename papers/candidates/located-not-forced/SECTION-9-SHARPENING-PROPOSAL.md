---
title: "Located, Not Forced -- Section 9 sharpening proposal (tracked diff)"
status: APPLIED (2026-07-07, on maintainer go) to both .md (v2.11) and .tex (Section 9 synced); a .tex<->.md full reconcile + Overleaf compile is still required before submission (see the DRIFT FLAG below and in the .tex header)
doc_type: paper-edit-proposal
created: 2026-07-07
pauses_for: maintainer (APPLIED; the remaining pre-submission steps are Joe-side: full .tex reconcile, Overleaf compile, arXiv endorsement, go)
provenance:
  - explorations/big-swing-2026-07-07/BIG-SWING-RS-INDEX-STILL-GATED.md (RS-index swing, 4 routes)
  - explorations/big-swing-2026-07-07/BIG-SWING-FRAMED-BORDISM-STILL-GATED.md (framed-bordism swing, 4 routes)
---

# Section 9 sharpening -- tracked diff

**What this is.** A diff-style proposed replacement for the closing block of Section 9, folding the two
2026-07-07 swings. It is a **SHARPENING, not a status change**: the verdict stays *located, not forced*; no
grade, claim, or title moves. It strengthens the "candidate category error" standing to a mapped-and-walled
frontier and narrows the open bridge onto exactly one object. Presented as current -> proposed so the exact
wording can be approved before it touches the frozen submission. The paper style is double-hyphen, no em
dashes; matched.

## The change is local to the closing block of Section 9

Everything up to and including the sentence ending "...does that relative index exist on GU's 14-manifold and
reduce mod 3 to the located carrier?" is UNCHANGED. Only the final block changes.

### CURRENT (verbatim)

> To earn "forced," three things must be built, in one calculation, on GU's actual 14-manifold: a proven
> fibered-boundary reduction; the explicit twisted Rarita-Schwinger index operator (the unbuilt source
> action); and an integer extraction with the fork resolved. A toy of that twisted Rarita-Schwinger operator
> has now been built and tested four ways (Section 8); it does not fill the forcing slot, and every integer it
> produces is 2-primary or one -- which strengthens the conjecture's standing as a candidate category error
> over the gated-but-derivable alternative (the RS-side gate, when probed, opens onto the selector arena).
> Until then the result is a no-go that *locates*; no computation performed in this program yields the integer
> three.

### PROPOSED (replacement)

> To earn "forced," three things must be built, in one calculation, on GU's actual 14-manifold: a proven
> fibered-boundary reduction; the explicit twisted Rarita-Schwinger index operator (the unbuilt source
> action); and an integer extraction with the fork resolved. The two arenas in which a homotopy-theoretic
> count could hide have now been mapped and walled. In the *cohomology* arena the GU-forced base is 2-adic
> (`H^2(RP^3;Z) = Z/2`, `Hom(Z/2,Z) = 0`). In the *framed-bordism* arena the located carrier escapes into
> `pi_3^s = Z/24 = Z/8 (+) Z/3`, and there the class-to-count obstruction holds one level up:
> `Hom(Z/24,Z) = Hom(Q/Z,Z) = 0`, so the Adams `e`-invariant `e_R = 1/12`, an element of the finite image of
> `J`, provably has no integer-class preimage under any framing. The twisted Dirac operator was then built
> explicitly on the GU-forced `RP^3 = L(2;1)` spine with the self-dual `Lambda^2_+` framing, and *every*
> admissible flat twist leaves the index 3-adically fractional (the `Z/2` deck group is coprime to 3; a
> `Z/3`-deck control on the unforced `L(3;1)` does integerize, isolating the obstruction as the deck-group
> order, not a construction failure). The mirror-hiding source-action coupling does not double as the base
> selector -- it is base-agnostic with a 2-group selector -- so the count and the chiral-projection selector
> are two disjoint external inputs, which strengthens rather than bridges the two-arena picture. The only
> surviving route to a nonzero `Z/3` reading is a double external import (`3 | m` in a cubic coupling *and*
> `3 | sigma` in the spacetime signature), disjoint from the located carrier and forced by no anomaly-
> cancellation, Dai-Freed, or modular requirement. The open bridge therefore collapses onto a single object:
> a *relative* or *equivariant* twisted Rarita-Schwinger index -- integer-valued by construction and
> geometry-dependent, so its fractional part, not a class, may equal `e_R`, which is precisely why it is
> invisible to every homomorphism and `e`-invariant obstruction above -- and it remains unbuilt, gated on
> GU's own unstabilized matter action. Until it is built the result is a no-go that *locates*: the places to
> look are exhausted, one object remains to be built, and no computation performed in this program yields the
> integer three.

## Why this is safe to ship

- Flips no verdict, grade, claim, or title. "Located, not forced" is unchanged.
- Every new sentence is backed by a machine-checked, main-loop-re-run script (F1 built operator; F2
  `Hom(Z/24,Z)=0` laddered; F3 CRT projection; F4 imports-free), with the target-import guard clean (the 24
  is derived from the Bernoulli denominator of `Im J`, explicitly distinct from `chi(K3)=24`).
- It is corroboration Section 8/9 already anticipate; it makes the anticipated conclusion precise.

## Submission-readiness checklist (for the maintainer)

Math side -- DONE:
- [x] WC-ENUM-COMPLETENESS closed (`canon/enum-completeness-class-c-RESULTS.md`).
- [x] WC-ANTILINEAR-BOUND closed (`canon/antilinear-bound-RESULTS.md`, an index-nullity theorem).
- [x] Deductive spine Lean-verified (`Lean/GUFormalization/LocatedNotForcedLegs.lean`).
- [x] Both 2026-07-07 swings corroborate; verdict unchanged and sharpened.
- [ ] (optional) apply this Section 9 diff on maintainer approval.

Joe side -- REMAINING (nothing here is math):
- [ ] arXiv endorsement check: confirm the account can submit to hep-th (longest lead; do first).
- [ ] compile the `.tex` on Overleaf (clean single file, embedded bib, all refs resolve).
- [ ] (optional) final deep-research pass.
- [ ] explicit go -> submit (hep-th primary; math-ph, math.AT secondary).
- [ ] on live confirmation, move the folder to `papers/published/` with the arXiv id.

Post-publication (not blocking) -- the hardening queue (`HARDENING-QUEUE.md`) lowers the barrier to the
external replication the review asks for (reproducibility harness, Lean of the enumeration core, reviewer
packet). Convergent lane; runs in parallel.

## Application

On maintainer approval, apply the PROPOSED block to BOTH the `.md` (readable) and the `.tex` (arXiv source),
add a one-line changelog entry (v2.11: Section 9 sharpening -- both arenas walled, bridge collapses to one
object; verdict unchanged), and leave the rest of the paper untouched. Do not apply without the go.

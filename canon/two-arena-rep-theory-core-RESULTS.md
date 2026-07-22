---
title: "Two-Arena Rep-Theory Core (canon spine)"
status: canon
doc_type: results
created: 2026-07-03
canon_promoted_at: 2026-07-03
tier: internal
verdict: "RESOLVED (three exact, GU-independent facts; exact-integer certified; CRT/coprimality cores Lean-typechecked exit 0, no sorry/axiom, 2026-07-03)"
scripts:
  - tests/big-swing/R4_spin95_hom_vanishing.py
  - tests/big-swing/R4_crt_two_arena.py
  - Lean/GUFormalization/R4TwoArena.lean
  - tests/big-swing/R4_TwoArena.lean
source_exploration: explorations/big-swing-2026-07-03/R4-two-arena-rep-theory-core.md
---

# Two-Arena Rep-Theory Core

**Canon means: safe to cite as the current public spine. It does not mean proved physics.** A standalone,
GU-independent rep-theory note (canonical claim 6). **Internal tier.** It **does not derive a generation
count** and asserts no GU-specific physical premise.

## Canonical statement — three exact facts

- **(A) Spin(9,5) chiral-spinor Hom-vanishing.** `dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0`. Computed
  explicitly on the 128-dim Clifford module, re-derived in a second gamma basis and second signature
  `Cl(7,7)`, controlled against self-dual `Cl(4,0)/Cl(8,0)`, and cross-checked by exact-integer weight
  combinatorics. **Independently corroborated in canon**: the same object is recorded at
  `canon/shiab-existence-cl95.md` (CORRECTION SHIAB-05: exact rep theory over `Cl(9,5) = M(64,H)`, checksum
  `16384 = 128^2`, errors `0.00e+00`). Consequence: a same-chirality Majorana scalar-mass channel is absent
  from the equivariant family and must come from an external source-action spurion.
- **(B) CRT two-arena split with 2-primary blindness.** `pi_3^s = Z/24 = Z/8 (+) Z/3` (Chinese Remainder,
  exact; `gcd(8,3) = 1`, arenas meet only at 0), and **every power-of-two obstruction annihilates the
  order-3 arena** (2-primary blindness, exhaustively checked). This is the GU-independent arithmetic spine
  of "located, not forced." Certificate `R4_crt_two_arena.py`: exact-integer, **exit 0** (re-run
  2026-07-03).
- **(C) Class-C 2-primary generator arithmetic.** The class-C generator dimensions and their 2-primary
  factorizations, as exact arithmetic.

## Grade / verification (honest)

- **(B) and the arithmetic/finite cores** — exact-integer certified, re-run this session (`R4_crt_two_arena.py`,
  exit 0). Proof terms for the CRT split and the coprimality/blindness theorem are written in Lean
  (`Lean/GUFormalization/R4TwoArena.lean`, with the stable compatibility entrypoint
  `tests/big-swing/R4_TwoArena.lean`; `ZMod.chineseRemainder` + an `addOrderOf`/coprimality argument) with
  no `sorry` and no `axiom`. **Lean TYPECHECKS (2026-07-03; default-target integration reverified
  2026-07-22):** after two mathlib API-drift fixes
  (`Finset.card_sdiff_of_subset`; `AddMonoid.addOrderOf_eq_one_iff`), the proof-bearing module now lives in
  the default target as `Lean/GUFormalization/R4TwoArena.lean` and `lake build` returns **exit 0 with no
  `sorry`/`axiom`** (only benign linter warnings) — independently
  re-verified in the main loop. So the Lean leg is now machine-verified, not merely "proof terms written."
  The canonical content also stands independently on the exact-integer certificate and (A)'s canon corroboration.
- **(A)** — re-run this session (`R4_spin95_hom_vanishing.py`, **exit 0**: `dim Hom = 0` across explicit
  `Cl(9,5)`, a recursive-doubling basis, and `Cl(7,7)`; controls `Cl(4,0)/Cl(8,0)` correctly return 1),
  corroborating `canon/shiab-existence-cl95.md` (SHIAB-05, exact rep theory, errors 0.00e+00).

## Scope / what this does NOT do

Does not derive three; the generation-count verdict stays OPEN. (B)'s 2-primary blindness is the same fact
the located-not-forced spine records at `canon/enum-completeness-class-c-RESULTS.md` /
`canon/core-theorems-symbolic-proof-RESULTS.md`; this note adds a self-contained, Lean-backed restatement,
not a competing claim. Full write-up and caveats:
`explorations/big-swing-2026-07-03/R4-two-arena-rep-theory-core.md`.

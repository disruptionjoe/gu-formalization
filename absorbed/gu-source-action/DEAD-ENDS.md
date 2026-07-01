# DEAD-ENDS — tested and killed (do NOT re-walk)

These approaches looked convincing — several very convincing — and were killed by computation in the
`gu-formalization` campaign. Re-attempting one is only allowed if you have a genuinely DIFFERENT surviving
kernel, and you must state precisely what survives. "It fits beautifully" is the signature of this list.

## Selectors for the shiab (all fail)
- **shiab = the codifferential `d_A*`** — FALSE (Clifford parity: shiab is odd, `d_A*` is even).
- **gamma-trace / Rarita-Schwinger spectral projection** — computable but EXCLUDES the canon shiab (selects
  `wedge - 6*contract`).
- **folded-complex closure `d^2 = 0`** — UNSATISFIABLE (kills the whole family including canon).
- **seesaw self-adjointness** — vacuous, or forces the Clifford-even `d_A*`.
- **PO1 "forgetful = projection-with-loss = larger kernel"** — FALSE (all channels have identical kernel,
  nullity 4928; wedge is not injective).
- **conditional expectation on the M(64,H) fiber trace** — vacuous for a trace (existence automatic; selects
  nothing).
- **Kostant cubic algebraic Dirac** — re-hits the same `3 != 2` equal-rank wall as the analytic Dirac.
- **the "obstruction = a specific commutator number (343.73)"** — FALSE (different object).

## Forced analogies / vocabulary convergences (all fail on test)
- **record-issuance / boundary idea = a shiab selector** — NO; it lands on the non-compact index
  well-definedness, not the selector.
- **the source action = "the observer's slice" = ONE global object with the index** — FORCED ANALOGY. The
  obstruction C2 is not even an index; no computable handle links them; the apparent link (a "29% C2
  reduction" from a spectral section) was exactly the GENERIC rank-64 projection floor, random-indistinguishable.
- **C2 = the topological index** — NO. C2 is degree-1 homogeneous (scale-dependent), non-integer; an index is
  scale-invariant integer. Different KINDS of object.

## Target-imports (automatic FAIL)
- **ch2 = 24** — NO; the honest computation gives `ch2(S_X)[K3] = -5376`. The lone "24" (tangent-only
  `|p1/2|`) is a DISGUISED chi-import (it equals 24 only because K3 satisfies `2chi + 3sigma = 0`).
- **`24 / 8 = 3` as a normalization**, **`chi(K3) = 24` as a generation input**, **contractible-fiber =>
  pushforward 1**, **flat `Ahat = 3`** (Rokhlin: needs signature -24, not divisible by 16) — all blocked.

## Acausal traps (automatic FAIL)
- Any construction that drives the **bare** `||[Pi_RS, M_D]||` (58.72) to 0 — that decouples the RS sector and
  reinstates Velo-Zwanziger acausality. The obstruction to drive down is the DRESSED one, never the bare.
- A trivial block-subtraction `sigma_c = -(escape block)` added to the bare dynamics — same acausal trap.

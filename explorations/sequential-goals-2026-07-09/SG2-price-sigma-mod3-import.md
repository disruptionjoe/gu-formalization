---
artifact_type: exploration
status: exploration
created: 2026-07-09
title: "SG2 -- pricing the 3 | sigma external import: is the surviving count channel available?"
grade: "COMPUTED (exact number theory + standard 4-manifold realizability); reconstruction-tier on the recalled manifold invariants (K3, CP^2 signatures, Rokhlin). Internal. No verdict/canon/posture change."
depends_on:
  - explorations/big-swing-2026-07-07/BIG-SWING-RS-INDEX-STILL-GATED.md
  - canon/w2-y14-spin-structure.md
  - tests/big-swing/rs_s2_relative_index_nogo.py
scripts:
  - tests/big-swing/sg2_price_sigma_mod3_import.py
---

# SG2 -- is the surviving `3 | sigma` import even available on a GU-admissible spacetime?

## The swing

BIG-SWING-RS-INDEX (2026-07-07) narrowed the single surviving escape from `Hom(Z/3,Z)=0` to a
**double external import**: a cubic `3 | m` Yukawa coupling **and** a base signature `3 | sigma`,
disjoint from the located carrier `e_R = 1/12`. Its next-step #2 asks explicitly whether **any
GU-admissible spacetime carries `3 | sigma`** -- to test whether the import is *available*, not just
conceivable. This goal prices the `3 | sigma` leg.

## What was computed (`tests/big-swing/sg2_price_sigma_mod3_import.py`, exit 0)

1. **Rokhlin lattice fact.** A closed smooth **spin** 4-manifold has `16 | sigma` (Rokhlin). Hence on
   a spin base, `3 | sigma <=> sigma in 16Z cap 3Z = lcm(16,3)Z = 48Z` (derived; first common
   multiple 48). No signature in `(0,48)` is divisible by both 16 and 3.
2. **Non-spin realizability.** `a CP^2 # b (CP^2-bar)` realizes every integer signature `a-b` (odd
   intersection form). So `3 | sigma` is free at `|sigma| = 3` (`# 3 CP^2`). **Cost:** `X^4` non-spin
   => (canon `w2-y14-spin-structure.md`) `Y^14` non-spin => the GU Dirac/RS operator needs a
   `Spin^c`/twisted setup -- a real structural cost.
3. **Spin realizability.** `# k K3` realizes `sigma = -16k`; the first `3 | sigma` is `k=3`
   (`sigma = -48`, `b2 = 66`). **Cost:** a spin base carrying `3 | sigma` needs `|sigma| >= 48`
   (a "large" spacetime).
4. **Disjointness home-check.** `e_R = 1/12 in Q/Z` (order 12, 3-adic valuation 1) is a
   framed-bordism/eta class on the `RP^3` spine; `sigma in Z` is a bulk signature of `X^4`. No
   GU-forced map ties them (full independence proved in SG5).

## Verdict

**The `3 | sigma` import is AVAILABLE (not obstructed).** Therefore located-not-forced **cannot** be
upgraded to "provably not forceable" by killing this channel: the surviving escape is real. But it is
a genuine **external boundary datum** with a priced cost -- *free-but-non-spin* (`Y^14` loses its spin
Dirac operator) **or** *spin-but-large* (`|sigma| >= 48`). It is the **spacetime's signature**, not
any GU-native carrier, that would supply the factor 3, consistent with the firewall-boundary reading.

No target imported (3 enters only as the modulus under test; `48 = lcm(16,3)` is derived). No verdict,
canon, or posture change; generation count stays OPEN (located, not forced).

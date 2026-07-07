---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "FB-F4 (image-of-J is fractional BY CONSTRUCTION, and the two surviving external imports are FREE choices): does the framed-bordism escape offer a native integer, or is it torsion like cohomology -- and is EITHER remaining door (3|m cubic coupling, 3|sigma spacetime signature) forced by any physical consistency requirement? HONEST OUTCOME: KILL of the external-import-forcing route. (a) The framed-bordism route offers NO native integer, exactly like the cohomology route: pi_3^s = Z/24 is ALL torsion (|Im J_3| = denom(B_2/4) = 24 MEASURED via Bernoulli; CRT split Z/8 (+) Z/3 DERIVED from factorint(24)={2:3,3:1}, iso verified bijective+additive), the Adams e-invariant is a Q/Z mod-Z reduction BY CONSTRUCTION (e_R=1/12 a proper fraction, order 12, CRT image (2,2) with nonzero Z/3 component = the order-3 info), and Hom(Z/24,Z)=Hom(Z/3,Z)=Hom(Z/2,Z)=0 while the free-rank control Hom(Z,Z)!=0 shows 'no integer' is a MEASURED property of torsion, not a tautology (CP^2's free-rank 3 IS import-class). Parallel wall printed: cohomology Hom(Z/2,Z)=0 on the RP^3 spine, framed-bordism Hom(Z/24,Z)=0 -- neither native route supplies an integer. (b) The DOUBLE external import (RS-S2 Leg B reproduced: ind_full = 12k+16 m^2 d' - 2 sigma == m^2 d' + sigma (mod 3), so section-independent 3-divisibility <=> 3|m AND 3|sigma) is characterized exactly, and BOTH imports are FREE: 3|m is not forced by local anomaly cancellation (color triality is a MULTIPLICITY divisibility, mult_1=mult_2=6, NOT a twist-degree m constraint; every native twist m in {1,2,5} has m^2==1 mod 3, carrier 3-inert), not by Dai-Freed (SM Theta=4 integer -> mod-3 phase 0, R2's empty arena Omega^Spin_5(B G_SM) (x) Z_(3)=0; non-vacuity bare Weyl gives 1/3), not by modular invariance (GU is not a worldsheet theory); the L(3) deck group that WOULD supply mod-3 characters is a genuine import (GU-forced spine is L(2;1)=RP^3, H^2=Z/2 measured, never L(3;1), H^2=Z/3). 3|sigma is not forced by Rokhlin (2-adic: 16|sigma, K3 sigma=-16 FAILS 3|sigma; 3|sigma <=> 48|sigma) nor any 4D pure gravitational anomaly. (c) Every route to the integer 3 therefore requires a FREE external choice; 'forced' is NOT reachable via an external-but-physically-forced import. conjecture_signal = KILL of the external-import-forcing route; it composes with RS-S2's KILL (native carrier 3-inert). The distinct RS-S4 operator-bridge GATE (unbuilt relative/equivariant twisted-RS index) is NOT claimed killed, but its mod-3 value reduces (Leg B) to these two now-free imports, so building it cannot rescue 'forced' absent a free import. Paper generation-count verdict unchanged: OPEN."
grade: "CONSISTENT_UNCOMPUTED (route verdict KILL of the import-forcing branch); sub-results at THEOREM grade at their stated scopes. (a) arithmetic THEOREM: |Im J_3|=denom(B_2/4)=24 (sympy Bernoulli), Z/24=Z/8(+)Z/3 a DERIVED CRT isomorphism (factorint + verified bijective/additive map, not recalled), e_R=1/12 order 12 in Q/Z with nonzero Z/3 CRT component, Hom(Z/n,Z)=0 for n in {24,3,2} enumerated with a Hom(Z,Z)!=0 free-rank control (the fractionality is torsion-caused, machine-discriminated). (b) symbolic THEOREM (exact sympy): ind_full == m^2 d' + sigma (mod 3) verified over 200 random inputs; section-independent 3-divisibility <=> 3|m AND 3|sigma swept m=0..8; every native m in {1,2,5} has m^2==1; L(2;1) H^2=Z/2 vs L(3;1) H^2=Z/3 MEASURED via Smith normal form; SM local anomaly (sumY=sumY^3=0) and color-triality multiplicities (4,6,6) and Dai-Freed phase Theta=4 (integer => phase 0) reproduced from R2 with a nonzero bare-Weyl non-vacuity control (1/3); Rokhlin 16|sigma 2-adicity + K3 sigma=-16 failing 3|sigma + lcm(16,3)=48. FROM-MEMORY flags (arithmetic consequences machine-checked, the inputs not re-derived): the Adams e-invariant as a Q/Z mod-Z reduction of a Chern/Ahat number (definitional); p_1=4 Kirby-Melvin framing normalization (cross-checked against the class-2/24 Adams route, agreeing at 1/12); Rokhlin 16|sigma for spin 4-manifolds; K3 signature -16; 4D has no pure gravitational anomaly; Garcia-Etxebarria-Montero Z_9 -> N in 3Z. Anchors reproduced first: pi_3^s=Z/24 CRT split (derived), e_R=1/12 (two agreeing normalizations), L(2;1) reduced eta (-1/8,+1/8) 2-adic validated by sum_a xi_a=0 with an L(3;1) (-2/9,1/9,1/9) 3-adic control, the transparent-fiber APS value -1/12, the 12k index. TARGET-IMPORT GUARD at maximum strictness: no element of {3,8,24,chi(K3)=24,Ahat=3,rank_H=4,ind_H=8} assumed, inserted, hardcoded as an answer, or divided by to GET an answer -- 24 is denom(B_2/4) [Bernoulli], the 8 and 3 are prime-power factors of 24 [factorint], e_R denominators measured, chi(K3)=24 kept provenance-distinct as a Betti sum; every 3 carries its printed provenance chain. Every count stated as 'mechanism/import M forces c', never 'GU forces c'. Internal tier: computed + self-adversarial, not externally replicated or peer-reviewed."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - explorations/big-swing-2026-07-07/RS-S4-base-forcing-bismut-cheeger.md
  - explorations/big-swing-2026-07-07/RS-S2-relative-index-nogo.md
  - canon/h2-base-index-chirality.md
scripts:
  - tests/big-swing/fb_f4_imageofJ_fractional_and_imports.py
---

# FB-F4: image-of-J is fractional by construction, and the surviving imports are free choices

**The swing.** The RS-index swing (2026-07-07) closed the native-construction escape four ways and narrowed
the located-not-forced generation count to ONE remaining carrier: the paper's Section 9 framed-bordism carrier.
The GU-forced `RP^3 = L(2;1)` spine with the self-dual `Lambda^2_+` tangential framing escapes the 2-adic
cohomology wall (`H^2(RP^3;Z) = Z/2`) into **framed bordism** `pi_3^s = Z/24 = Z/8 (+) Z/3` (CRT). The
generation count, if homotopy-theoretic, would live in the `Z/3` summand, read by the Adams `e`-invariant via
the image of `J`, with `e_R = 1/12`. RS-S2/S4 pinned the two non-operator bridges and named the only surviving
route to a nonzero mod-3 class: a **double external import** `3|m` (cubic coupling / section degree) AND
`3|sigma` (spacetime signature). This route (F4) does not attack the unbuilt operator. It asks two things:
does the framed-bordism escape offer a **native integer** (or is it torsion, like cohomology), and is
**either** external import **forced by any physical consistency requirement**?

**Honest outcome: KILL of the external-import-forcing route.** The framed-bordism route offers no native
integer -- the `e`-invariant is fractional by construction and `pi_3^s = Z/24` is all torsion, exactly the same
`Hom(-, Z) = 0` wall as cohomology -- and both surviving external imports (`3|m`, `3|sigma`) are **free
choices**: neither is forced by anomaly cancellation, the Dai-Freed anomaly, or modular invariance for the
actual SM/GU content. Every route to the integer 3 requires a free external choice.

All numbers below are printed by `tests/big-swing/fb_f4_imageofJ_fractional_and_imports.py` (run from repo
root, exit 0). Anchors reproduced first: `pi_3^s = Z/24` with the CRT split **derived** (not asserted),
`e_R = 1/12` by two agreeing normalizations, the `L(2;1)` reduced eta `(-1/8, +1/8)` (2-adic, validated by
`sum_a xi_a = 0`) with an `L(3;1)` 3-adic control, the transparent-fiber APS value `-1/12`, and the `12k` index.

---

## (a) Image-of-J is fractional BY CONSTRUCTION: no native integer, exactly like cohomology

**`pi_3^s = Z/24`, and the CRT split is derived, not recalled.** `|Im J_3| = denom(B_2/4) = denom(1/24) = 24`
(sympy Bernoulli; homotopy provenance, kept distinct from `chi(K3) = 24`). `factorint(24) = {2:3, 3:1}`, so the
prime-power summands are `8` and `3` and `Z/24 = Z/8 (+) Z/3` -- and the isomorphism `k -> (k%8, k%3)` is
verified **bijective and additive** on all 24 elements, so the `Z/8` and the `Z/3` are measured factors, never
hardcoded. The genuine order-3 classes (`3k == 0 mod 24`, `k != 0`) are `{8, 16}`, whose CRT images `(0,2)` and
`(0,1)` are the **pure `Z/3` summand** (first coordinate 0); their `e`-values are the order-3 fractions `1/3`,
`2/3`.

**The `e`-invariant is a `Q/Z` (mod-`Z`) reduction by construction.** The Adams `e`-invariant sends a class
`k in Z/24` to `k/24 in Q/Z` -- a fraction. `e_R = 1/12` is class 2, CRT image `(2, 2)`: its `Z/3` component
`2 != 0` **carries the order-3 information**, and `1/12` is a proper fraction (denominator 12 > 1, order 12 in
`Q/Z`, 3-adic valuation of the order = 1). This is the e-invariant / `Hom(Z/3,Z)=0` discipline made explicit:
`e_R` is not an integer, and cannot be, because the invariant that detects it is a mod-`Z` reduction.

**The wall: `Hom(finite, Z) = 0` on both native routes.** The script enumerates the homomorphisms and finds
`Hom(Z/24, Z) = Hom(Z/3, Z) = Hom(Z/2, Z) = 0` (the generator's image `g` must satisfy `n g = 0` in `Z`, forcing
`g = 0`). The **free-rank control** `Hom(Z, Z) != 0` (the generator `1 -> 1` is a genuine nonzero homomorphism)
discriminates: "no integer" is a **measured consequence of torsion**, not a tautology. This is exactly why
`CP^2`'s "3" (a **free-rank** `H^2 = Z` degree) is import-class while the `RP^3` carrier's order-3 is not an
integer at all. Both native routes hit the same wall:

| native route | invariant | detector | integer? |
| --- | --- | --- | --- |
| cohomology (RS-S4's 2-adic wall) | `H^2(RP^3) = Z/2` | -- | `Hom(Z/2, Z) = 0` -> **no** |
| framed bordism (this route) | `pi_3^s = Z/24` | Adams `e`-invariant (`Q/Z`) | `Hom(Z/24, Z) = 0` -> **no** |

**Verdict (a).** The framed-bordism escape offers **no native integer**. The `e`-invariant is fractional by
construction; `pi_3^s` is all torsion; `Hom(-, Z) = 0`. The escape from cohomology into framed bordism changed
the *arena* (from `Z/2` to a group that genuinely carries order 3) but not the *type*: still torsion, still no
integer. An integer must come from **outside** this group -- a relative/equivariant/rank invariant (RS-S4's
gated operator) or an **external import** (characterized next).

---

## (b) The two surviving external imports, and whether physics forces either

**The law (RS-S2 Leg B, reproduced symbolically).** With `X` spin (`d = 2 d'`),
`ind_full = 12k + 16 m^2 d' - 2 sigma`, and mod 3 (`12 == 0`, `16 == 1`, `-2 == 1`):

```
ind_full == m^2 d' + sigma   (mod 3)          [verified over 200 random integer inputs]
```

Section-independent 3-divisibility (`3 | ind_full` for all `d'`, `k`) holds **iff `3|m` AND `3|sigma`** (`m^2 == 0
mod 3 <=> 3|m` kills the `d'` coefficient; the constant then forces `3|sigma`). A **double** import. Each leg
examined against the three physical consistency requirements the route names:

### Import 1 -- `3|m` (cubic coupling / L(3) deck group): FREE

- **Carrier is 3-inert.** Every natively selected twist `m in {1, 2, 5}` has `m^2 == 1 (mod 3)`. To reach
  `3|m` needs a **non-native** twist; the located carrier's own twist never supplies it.
- **The `L(3)` deck is a genuine import.** An `L(3;1)` deck group `Z/3` would supply mod-3 Wilson characters
  (`H^2(L(3;1)) = Z/3`, measured via Smith normal form) -- but the GU-forced spine is `L(2;1) = RP^3`
  (`H^2 = Z/2`, deck `Z/2`; `p-q=4` forces `GL(4,R)/O(3,1) -> RP^3`, never `L(3;1)`). Choosing `L(3)` is an
  import of the same unforced class as `K3`/`CP^2`.
- **Not forced by local anomaly cancellation.** The anomaly-relevant divisibility in the SM is **color
  triality** -- charged Weyl multiplicities `mult_1 = mult_2 = 6 == 0 (mod 3)` -- a **multiplicity** condition,
  not a constraint on the twist degree `m`, and it is automatically satisfied (`sum Y = sum Y^3 = 0`), imposing
  nothing on `m`.
- **Not forced by the Dai-Freed anomaly.** Reproducing R2 on the genuine `Z_3`-carrying `L(3;1,1)`: the SM
  one-generation phase `Theta = sum_a mult_a rho_a = 4`, an **integer**, so the mod-3 phase `Theta mod Z = 0`
  for any normalization -- `Omega^Spin_5(B G_SM) (x) Z_(3) = 0`, the mod-3 arena is **empty**. (Non-vacuity: a
  bare charge-1 Weyl gives `Theta = 1/3 != 0`, so the toy *can* detect a pin; the SM simply does not.)
- **Not forced by modular invariance.** GU is not a worldsheet theory; no modular-invariance requirement
  applies. (FROM-MEMORY.)
- **The one literature forcing mechanism does not rescue it.** Garcia-Etxebarria-Montero `Z_9 -> N in 3Z`
  (FROM-MEMORY) forces only membership `in 3Z` (not the integer `3`), **requires importing** a genuinely
  3-primary `Z_9` anomaly (itself unforced), and is **absent** for actual SM data (R2's empty arena). It is a
  conditional forcing resting on a free import.

`3|m` is a **free external choice**.

### Import 2 -- `3|sigma` (spacetime signature): FREE

- **Rokhlin is 2-adic.** A spin 4-manifold has `16 | sigma` (Rokhlin; FROM-MEMORY) -- `16 = 2^4`, a power of 2,
  a purely 2-adic constraint. It does **not** force `3|sigma`.
- `3|sigma <=> 48|sigma` (`lcm(16,3) = 48`); the allowed spin signatures divisible by 3 in `[-48,48]` are
  `{-48, 0, 48}`. The **canonical** spin 4-manifold `K3` has `sigma = -16`, which is **not** divisible by 3 --
  it fails `3|sigma`.
- No 4D **pure gravitational anomaly** forces a signature congruence mod 3 (anomalies live in `4k+2`;
  FROM-MEMORY); no Dai-Freed or modular requirement forces `3|sigma`.

`3|sigma` is a **free external topological choice**.

---

## (c) Honest readout and conjecture signal

- **(a)** The framed-bordism route offers **no native integer** -- `e_R = 1/12` fractional by construction,
  `Hom(Z/24, Z) = 0`, parallel to the cohomology wall `Hom(Z/2, Z) = 0`. Both native routes are torsion.
- **(b)** The **only** remaining doors are the double external import `3|m` AND `3|sigma`, and **both are free**
  -- not forced by local anomaly cancellation, the Dai-Freed anomaly, or modular invariance for the actual
  SM/GU content.
- **(c)** Therefore **every route to the integer 3 requires a free external choice.** "Forced" is not reachable
  via an external-but-physically-forced import. Located, not forced -- **permanently**, unless a future physics
  requirement forces one of the two imports.

**SIGNAL = KILL** (of the external-import-forcing route).

**Scope and composition.** This KILLs the branch "forced via a physically-forced import." It **composes** with
RS-S2's KILL (the located carrier is 3-inert in every native RS-sector relative/equivariant/rank invariant):
RS-S2 closed the *native* transfer through the carrier; F4 closes the *external-forcing* escape that RS-S2 left
named-but-open. The distinct **RS-S4 operator-bridge GATE** -- the unbuilt relative/equivariant twisted-RS
index whose nonzero geometry-dependent bulk could give `e_R` an integer preimage -- is **not** claimed killed
here. But F4 sharpens why building it cannot rescue "forced": by RS-S2 Leg B the mod-3 value of *any* such
twisted index is `m^2 d' + sigma`, carried entirely by the two imports this route just showed are free. So even
the gated operator, once built, would force nothing mod 3 without an additional free import.

**Proposal for Section 9 (pauses for the maintainer; the frozen paper is not touched).** Record, under Section
9, that the framed-bordism escape is subject to the *same* `Hom(-, Z) = 0` wall as the cohomology route (the
`e`-invariant is `Q/Z`-valued by construction), and that the two named external imports (`3|m` cubic coupling,
`3|sigma` signature) are each a **free external choice** -- not forced by anomaly cancellation, the Dai-Freed
anomaly (SM mod-3 arena empty, R2), or modular invariance -- so "forced" is reachable only through a free import.
The generation-count verdict is unchanged: **OPEN** (external by structure; now with both the native carrier
bridge and the external-import-forcing route specifically closed, leaving only the RS-S4 operator gate, itself
import-carried mod 3).

---

## Honest gaps carried

1. **From-memory inputs (arithmetic consequences machine-checked, inputs not re-derived):** the Adams
   `e`-invariant as a `Q/Z` mod-`Z` reduction of a Chern/`A-hat` number (definitional); `p_1 = 4` Kirby-Melvin
   (cross-checked against the class-2/24 Adams route, agreeing at `1/12`); Rokhlin `16|sigma`; `K3` signature
   `-16`; the absence of a 4D pure gravitational anomaly; Garcia-Etxebarria-Montero `Z_9 -> N in 3Z`.
2. **"Not physically forced" is scoped to the SM/GU content and the three named requirements** (anomaly
   cancellation, Dai-Freed, modular invariance). A future, currently-unknown consistency requirement -- or GU's
   own unbuilt stabilized source action turning out to contain a genuinely 3-primary discrete anomaly -- could
   in principle force an import. That is precisely the open condition; the R2 empty-arena result closes it for
   the *known* SM data. If such a forcing route were exhibited, the signal would move to GATED.
3. **F4 does not attack the RS-S4 operator bridge.** The relative/equivariant twisted-RS index remains the one
   unbuilt object; F4's contribution is to show its mod-3 value is import-carried and the imports are free, not
   to build or refute the operator.
4. **Dimension note on the Dai-Freed toy:** `L(3;1,1)` is 3-dimensional (a direct Dai-Freed test for a
   2D-theory-shaped object); the rigorous 4D SM statement is R2's `Omega^Spin_5` certificate. The triality /
   divisibility mechanism is dimension-independent.
5. **Internal tier only:** computed and self-adversarial (measured torsion / homomorphisms, derived CRT
   isomorphism, exact symbolic mod-3 law, non-vacuity controls), not externally replicated or peer-reviewed.

## Governance

Exploration-grade; **no paper edit made** (the frozen `located-not-forced` paper is not touched). The KILL is a
**proposal** for Section 9 that pauses for the maintainer: it closes the external-import-forcing branch (both
named imports are free choices) and composes with RS-S2's native-carrier KILL, leaving only the RS-S4 operator
gate (itself import-carried mod 3). The generation-count verdict is unchanged: **OPEN**. Any verdict/status flip
pauses for Joe.

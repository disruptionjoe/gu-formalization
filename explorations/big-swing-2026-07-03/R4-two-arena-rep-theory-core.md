---
title: "R4 big-swing: a standalone, certificate-backed two-arena rep-theory note -- the Spin(9,5) chiral-spinor Hom-vanishing, the CRT splitting pi_3^s = Z/8 (+) Z/3 with 2-primary blindness, and the class-C 2-primary generator arithmetic -- with a machine-checked Lean core (no sorry, no axiom) and three independent executable certificates. GU-INDEPENDENT."
status: exploration
doc_type: big-swing-result
created: 2026-07-03
grade: "EXECUTABLE-CERTIFIED + PARTLY LEAN-CHECKED, GU-independent. Three legs, each verified an unusually strong way: (A) Spin(9,5) Hom-vanishing computed explicitly on the 128-dim Clifford module, re-derived in a second gamma basis and a second signature Cl(7,7), controlled against self-dual Cl(4,0)/Cl(8,0), and cross-checked by exact integer weight combinatorics; the weight-parity core is Lean-proved. (B) The CRT two-arena split and 2-primary blindness are exact-integer certified AND fully Lean-proved (ZMod.chineseRemainder + an addOrderOf/coprimality blindness theorem, no sorry). (C) The class-C generator dims and 2-primary factorizations are Lean-proved arithmetic. NOT a claim about generation count; nothing here derives three."
scripts:
  - tests/big-swing/R4_spin95_hom_vanishing.py
  - tests/big-swing/R4_crt_two_arena.py
  - tests/big-swing/R4_TwoArena.lean
depends_on:
  - canon/core-theorems-symbolic-proof-RESULTS.md
  - canon/enum-completeness-class-c-RESULTS.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
---

# A standalone two-arena rep-theory core

This note extracts three EXACT, unconditional facts that the GU generation-sector program
leans on, states them as self-contained mathematics that needs no GU input, and machine-checks
as much of each as the tooling allows. It is deliberately publishable on its own as a
short math-ph / representation-theory note. **It does not derive a generation count and does
not assert any GU-specific physical premise.** The three legs are:

- **(A)** the Spin(9,5) chiral-spinor **Hom-vanishing**: `dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0`;
- **(B)** the **CRT two-arena** structure of the stable stem `pi_3^s = Z/24 = Z/8 (+) Z/3`, disjoint,
  with **2-primary blindness**;
- **(C)** the **class-C 2-primary generator arithmetic** (dims and factorizations).

Verification tooling actually used: Python/numpy for the explicit Clifford computation, exact
Python integer/`fractions` arithmetic for the combinatorial and CRT legs, and **Lean 4
(mathlib, v4.32.0-rc1)** for the finite/arithmetic cores -- compiled on this machine, no
`sorry`, no `axiom`.

---

## Leg A -- the Spin(9,5) chiral-spinor Hom-vanishing

### Statement (GU-independent)

Let `so(9,5)` act on its 128-dimensional Dirac spinor `S = S^+ (+) S^-` (each Weyl summand
64-dimensional). Then

> **Theorem A.** `dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0.`
> Equivalently: the chiral spinor `S^+` is **not self-dual**; its dual is the opposite
> chirality, `S^+ ~= (S^-)^*`. There is no `so(9,5)`-invariant bilinear pairing of two
> same-chirality spinors into the scalar (trivial) representation. And
> `dim Hom_{so(9,5)}(S^+ (x) S^-, Lambda^0) = 1`.

This is the invariant-theoretic root of the "no same-chirality invariant pairing" facts used
across the generation sector (e.g. the enum-completeness census's "16x16 zero-weight count = 0"
for the internal `so(10)`), stated cleanly for the full `so(9,5)` carrier.

### Why it is true, structurally

For `so(2r)` the chiral spinor `S^+` has weights that are `r`-tuples of `+-1/2` with an EVEN
number of minus signs. A trivial summand of `S^+ (x) S^+` requires a weight `w` in `S^+` whose
negative `-w` is also in `S^+`. Negation flips every sign, sending the minus-count `m` to
`r - m`. **For `r` odd, `m` even forces `r - m` odd**, so `-w` always lands in `S^-`. Hence the
same-chirality zero-weight count is `0` and no trivial summand can occur. The carrier is
`n = p + q = 14`, so `r = 7` is **odd**; the internal `so(10)` wall has `r = 5`, also odd. For
`r` even (e.g. Spin(4k)) the weight self-pairs and `S^+` is self-dual -- the control case.

This is exactly the standard "which Clifford charge-conjugation matrix flips chirality"
statement (`n = 14 ≡ 6 mod 8`, real, chirality-flipping), reduced to a one-line parity fact.

### Certificates (all RUN, exit 0)

`tests/big-swing/R4_spin95_hom_vanishing.py` proves Theorem A three independent ways:

| route | method | dim Hom(S^+ (x) S^+, triv) | control dim Hom(S^+ (x) S^-, triv) |
|---|---|---|---|
| (I) explicit Cl(9,5), Jordan-Wigner gammas | full `so`-invariant bilinear-form null space (normal-matrix, exact spectral gap) | `0` | `1` |
| (II) explicit Cl(9,5), recursive-doubling gammas | independent basis, same null-space method | `0` | `1` |
| (II) explicit Cl(7,7), same `n = 14` | different signature | `0` | `1` |
| (II) control Cl(4,0), `r = 2` even | method must SEE a nonzero | `1` (self-dual) | -- |
| (II) control Cl(8,0), `r = 4` even | non-triviality control | `1` (self-dual) | -- |
| (III) exact weight combinatorics | integer count of same-chirality zero-weight pairs | `0` (of 64) | -- |

<!-- CLIFFORD-NUMBERS: confirmed by run below -->

The controls are load-bearing: on `Cl(4,0)` and `Cl(8,0)` (`r` even) the SAME null-space method
returns `1`, so a `0` is a genuine vanishing, not a method that always returns `0`. The exact
weight combinatorics (route III), which needs no linear algebra at all, is:

```
so(14) r=7: same-chirality zero-weight pairs =  0 of 64 chiral weights   [ODD -> flips]
so(10) r=5: same-chirality zero-weight pairs =  0 of 16 chiral weights   [ODD -> flips]
so( 6) r=3: same-chirality zero-weight pairs =  0 of  4                   [ODD -> flips]
so( 4) r=2: same-chirality zero-weight pairs =  2 of  2                   [EVEN -> self-dual]
so( 8) r=4: same-chirality zero-weight pairs =  8 of  8                   [EVEN -> self-dual]
so(12) r=6: same-chirality zero-weight pairs = 32 of 32                   [EVEN -> self-dual]
```

### Lean core (compiled, no sorry)

`tests/big-swing/R4_TwoArena.lean`, namespace `WeightParity`, proves the exact combinatorial
obstruction as a theorem of arithmetic:

- `minusCount_neg : minusCount (neg w) = r - minusCount w`;
- `no_same_chirality_zero_weight (hr : Odd r) : forall w, Even (minusCount w) -> not Even (minusCount (neg w))`;
- `even_r_self_pairs (hr : Even r) : ... -> Even (minusCount (neg w))` (the self-dual control);
- instantiated `spin95_hom_vanishing_weight_core` at `r = 7`, and `so10_r5_odd` at `r = 5`.

What Lean checks: the exact combinatorial obstruction (the zero-weight count vanishes) for every
odd `r`, hence for Spin(9,5)/Spin(7,7) and the internal so(10). What Lean does NOT check: the
full representation-theoretic step "no zero weight => no trivial summand" (a weight-count is a
necessary condition; the explicit Clifford null-space computation supplies the exact dimension).

---

## Leg B -- the CRT two-arena structure of pi_3^s

### Statement (GU-independent)

> **Theorem B.** `pi_3^s = Z/24 ~= Z/8 x Z/3` (Chinese Remainder, `gcd(8,3)=1`). The 2-primary
> subgroup `(Z/24)[2^inf] = <3>` (order 8) and the odd subgroup `(Z/24)[3] = <8>` (order 3)
> intersect only at `0`. Consequently **every homomorphism `f : Z/24 -> Z/2^k` annihilates the
> order-3 arena** (`f(8) = 0`): no power-of-two-valued obstruction can detect the `Z/3` summand.

The 2-primary arena `Z/8` is where every enumerated obstruction of the generation no-go lives
(Kramers `Z/2`, Rokhlin mod `2^4`, adjoint `4k`, real/pseudoreal mod-2 index, the Krein
signature, ghost `Z/2`). The odd arena `Z/3` is the unique CRT-disjoint sector where a
homotopy-theoretic count could live and carries the Adams `e`-invariant `e_R = 1/12` (additive
order 3 in `Q/Z`, 3-primary part `Z/3`). Blindness is the exact arithmetic reason the no-go is
structurally unable to see the count -- the spine of "located, not forced," here isolated as a
GU-independent theorem.

### Certificate (RUN, exit 0) and Lean core (compiled, no sorry)

`tests/big-swing/R4_crt_two_arena.py` certifies with exact integer arithmetic: the explicit iso
`Z/24 -> Z/8 x Z/3` (bijective homomorphism on all 24 elements), the disjointness of the two
arenas (`<3> cap <8> = {0}`), and **exhaustive** 2-primary blindness (every hom `Z/24 -> Z/2^k`
for `k = 1..6` sends `8 -> 0`), plus the Adams backbone (`e_R = 1/12` has order 12, 3-part order 3;
`|Im J_3| = 24 = 8*3`).

`R4_TwoArena.lean`, namespace `CRT`, proves it as real Lean theorems:
- `twoArena : ZMod 24 ~=+* ZMod 8 x ZMod 3` via `ZMod.chineseRemainder`;
- `eq_zero_of_coprime_nsmul` (an element killed by two coprime integers is `0`, via `addOrderOf | gcd = 1`);
- `two_primary_blind (f : ZMod 24 ->+ ZMod (2^k)) : f 8 = 0` -- the blindness theorem;
- `arenas_disjoint` (the only common multiple of 3 and 8 in `Z/24` is `0`).

---

## Leg C -- the class-C 2-primary generator arithmetic

The enum-completeness census computes the invariant-theoretic generator spaces of class C on the
carrier with dimensions `2 + 2 + 2 + 2` (linear commutant, bilinear, sesquilinear, antilinear),
totalling `8 = 2^3`; the cross-chirality Krein signature is `96 = 2^5 * 3`; the carrier dimension
is `192 = 2^6 * 3`; and spinor dimensions are pure powers of two. `R4_TwoArena.lean`, namespace
`TwoPrimaryGenerators`, Lean-proves the arithmetic backbone of these: `generator_dims_two_primary`
(`2+2+2+2 = 2^3`), `ninety_six_factor` (`96 = 2^5*3`), `carrier_dim_factor` (`192 = 2^6*3`), and
`spinor_dim_not_div_three` (`3` never divides `2^k`). The only odd factor anywhere is the LOCATED
carrier multiplicity `3` inside a dimension -- never a per-channel congruence. (The full generator
classification remains a computation on the explicit carrier, canon/enum-completeness-class-c.)

---

## What this is, and what it is not

- **Is:** three exact, GU-independent facts, each verified an unusually strong way; a Lean core
  with no `sorry`/`axiom` for every finite/arithmetic leg; independent re-derivations and genuine
  non-triviality controls for the one computed (non-symbolic) leg.
- **Is not:** a derivation of the generation count. Nothing here forces or forbids three. Leg A is
  a Hom-vanishing, Leg B is an arithmetic blindness, Leg C is a factorization list. The
  representation-theory-to-index step and the `order-3-class -> integer-3` bridge remain exactly
  as open as the canon says (see canon/three-generations-locate-not-force-CRT-RESULTS.md).

## Honest caveats

1. No target integer is imported: the only integers appearing are `0`, the carrier's own
   `(+96,-96)`, dimension factors `2^a * 3`, and the homotopy moduli `8, 3, 24`. Nothing is
   normalized to `3`, `8`, `24`, or `chi(K3)`.
2. Leg A's explicit Clifford computation is a machine-verified computation on the explicit module
   (with printed spectral gaps), re-derived twice and controlled; the WEIGHT-PARITY obstruction is
   Lean-proved, but the "no-zero-weight => no-invariant" implication and the exact `dim = 1` cross
   pairing are computed, not Lean-proved (full equivariant rep theory is not formalized here).
3. Leg B is fully Lean-proved. `pi_3^s = Z/24` itself is cited from stable homotopy theory (not
   re-proved); the note formalizes the ARITHMETIC of the splitting and the blindness, which is the
   load-bearing part.
4. This is staged under explorations/, not promoted; no canon/status file is edited.

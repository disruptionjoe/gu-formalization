import Mathlib

set_option autoImplicit false

/-!
# R4 big-swing — machine-checked core of the two-arena rep-theory note

This file is a **standalone**, GU-independent Lean formalization of the two finite,
proof-shaped legs of the R4 note.  It is written to be compiled against the same
mathlib the repo already provisions:

    ~/.elan/bin/lake env lean tests/big-swing/R4_TwoArena.lean

There is no `sorry` and no `axiom`.  Two legs are proved:

* **Leg A (weight parity → chiral-spinor Hom-vanishing).**  For `Spin(2r)`, a chiral
  (Weyl) spinor weight is an `r`-tuple of signs with an EVEN number of minus signs.
  A trivial summand of `S⁺ ⊗ S⁺` needs a weight `w ∈ S⁺` with `-w ∈ S⁺` too.
  Negation sends the minus-count `m` to `r - m`; for `r` ODD this flips parity, so
  `-w` always lands in `S⁻`.  Hence the same-chirality zero-weight count is `0` and
  `dim Hom(S⁺ ⊗ S⁺, Λ⁰) = 0` (the leg's exact combinatorial obstruction).  The
  physically relevant cases `r = 7` (Spin(9,5), Spin(7,7); n = 14) and `r = 5`
  (internal so(10), the 16/16bar wall) are ODD.  For `r` EVEN (e.g. Spin(4k)) the
  weight always self-pairs — the self-dual control.

* **Leg B (CRT two-arena + 2-primary blindness).**  `ZMod 24 ≃+* ZMod 8 × ZMod 3`
  (Chinese Remainder, `gcd 8 3 = 1`); the 2-primary and 3-primary subgroups meet
  only at `0`; and EVERY additive hom `ZMod 24 →+ ZMod (2^k)` annihilates the
  order-3 arena `⟨8⟩` — the "2-primary blindness" that makes 'located, not forced'
  a theorem of arithmetic, GU-independent.

Nothing here derives a generation count or asserts any physical premise; the physics
(that these weights/groups are the ones the RS carrier realizes) is verified
numerically in the companion certificates `R4_spin95_hom_vanishing.py`,
`R4_crt_two_arena.py`, and enters here only as the choice of `r`, `24`.
-/

namespace R4TwoArena

/- ===================================================================== -/
/-  Leg A — spinor weight parity and same-chirality Hom-vanishing         -/
/- ===================================================================== -/

namespace WeightParity

/-- A chiral spinor weight of `Spin(2r)` is an `r`-tuple of signs; `w i = true`
    encodes a `-1/2` entry (a "minus sign"), `false` a `+1/2`. -/
abbrev Weight (r : ℕ) := Fin r → Bool

/-- The number of minus signs of a weight. -/
def minusCount {r : ℕ} (w : Weight r) : ℕ :=
  (Finset.univ.filter (fun i => w i = true)).card

/-- Weight negation flips every sign (`+1/2 ↔ -1/2`). -/
def neg {r : ℕ} (w : Weight r) : Weight r := fun i => ! (w i)

/-- Negation sends the minus-count `m` to `r - m` (the complement). -/
theorem minusCount_neg {r : ℕ} (w : Weight r) :
    minusCount (neg w) = r - minusCount w := by
  unfold minusCount neg
  have hcompl :
      (Finset.univ.filter (fun i => (! w i) = true))
        = Finset.univ \ Finset.univ.filter (fun i => w i = true) := by
    ext i
    simp [Finset.mem_filter, Finset.mem_sdiff, Bool.not_eq_true, Bool.not_eq_false]
  rw [hcompl, Finset.card_sdiff (Finset.filter_subset _ _)]
  simp [Finset.card_univ]

/-- **Chirality-flip lemma (r odd).**  If `r` is odd and `w` is in the even
    chirality class (`minusCount w` even), then `-w` is in the ODD class. -/
theorem neg_flips_chirality {r : ℕ} (hr : Odd r) (w : Weight r)
    (hw : Even (minusCount w)) : Odd (minusCount (neg w)) := by
  have hle : minusCount w ≤ r := by
    unfold minusCount
    calc (Finset.univ.filter (fun i => w i = true)).card
        ≤ (Finset.univ : Finset (Fin r)).card := Finset.card_filter_le _ _
      _ = r := by simp [Finset.card_univ]
  rw [minusCount_neg, Nat.odd_iff]
  rw [Nat.even_iff] at hw
  rw [Nat.odd_iff] at hr
  omega

/-- **Leg A, exact combinatorial obstruction.**  For `Spin(2r)` with `r` odd,
    NO even-chirality weight `w` has an even-chirality negative — the zero-weight
    count inside `S⁺ ⊗ S⁺` is `0`, hence `dim Hom(S⁺ ⊗ S⁺, Λ⁰) = 0`. -/
theorem no_same_chirality_zero_weight {r : ℕ} (hr : Odd r) :
    ∀ w : Weight r, Even (minusCount w) → ¬ Even (minusCount (neg w)) := by
  intro w hw
  have := neg_flips_chirality hr w hw
  rw [Nat.odd_iff] at this
  rw [Nat.even_iff]
  omega

/-- Contrast (self-dual control): for `r` EVEN, every even-chirality weight has an
    even-chirality negative — `S⁺` self-pairs. -/
theorem even_r_self_pairs {r : ℕ} (hr : Even r) (w : Weight r)
    (hw : Even (minusCount w)) : Even (minusCount (neg w)) := by
  have hle : minusCount w ≤ r := by
    unfold minusCount
    calc (Finset.univ.filter (fun i => w i = true)).card
        ≤ (Finset.univ : Finset (Fin r)).card := Finset.card_filter_le _ _
      _ = r := by simp [Finset.card_univ]
  rw [minusCount_neg, Nat.even_iff]
  rw [Nat.even_iff] at hw hr
  omega

/-- The physically realized odd cases: `Spin(9,5)` and `Spin(7,7)` have `r = 7`. -/
theorem spin14_r7_odd : Odd (7 : ℕ) := by decide

/-- The internal `so(10)` (16/16bar Majorana-Weyl wall) has `r = 5`, also odd. -/
theorem so10_r5_odd : Odd (5 : ℕ) := by decide

/-- Instantiated statement for `r = 7` (Spin(9,5)): the same-chirality zero-weight
    count vanishes. -/
theorem spin95_hom_vanishing_weight_core :
    ∀ w : Weight 7, Even (minusCount w) → ¬ Even (minusCount (neg w)) :=
  no_same_chirality_zero_weight spin14_r7_odd

end WeightParity

/- ===================================================================== -/
/-  Leg B — CRT two-arena structure and 2-primary blindness               -/
/- ===================================================================== -/

namespace CRT

/-- `8` and `3` are coprime — the arithmetic that makes `Z/24` split. -/
theorem coprime_eight_three : Nat.Coprime 8 3 := by decide

/-- **CRT isomorphism.**  `ZMod 24 ≃+* ZMod 8 × ZMod 3` (as rings, hence groups):
    `π₃ˢ = Z/24 = Z/8 ⊕ Z/3`, the two-arena splitting. -/
noncomputable def twoArena : ZMod 24 ≃+* ZMod 8 × ZMod 3 :=
  ZMod.chineseRemainder coprime_eight_three

/-- A general finite-group fact: an element killed by two coprime integers is `0`.
    (`addOrderOf x ∣ gcd m n = 1`.)  This is the engine of 2-primary blindness. -/
theorem eq_zero_of_coprime_nsmul {A : Type*} [AddGroup A] {x : A} {m n : ℕ}
    (hmn : Nat.Coprime m n) (hm : m • x = 0) (hn : n • x = 0) : x = 0 := by
  have hdm : addOrderOf x ∣ m := addOrderOf_dvd_of_nsmul_eq_zero hm
  have hdn : addOrderOf x ∣ n := addOrderOf_dvd_of_nsmul_eq_zero hn
  have h1 : addOrderOf x ∣ 1 := hmn ▸ Nat.dvd_gcd hdm hdn
  have : addOrderOf x = 1 := Nat.dvd_one.mp h1
  exact addOrderOf_eq_one_iff.mp this

/-- Every element of `ZMod (2^k)` is killed by `2^k`. -/
theorem pow_two_nsmul_zmod (k : ℕ) (y : ZMod (2 ^ k)) : (2 ^ k) • y = 0 := by
  rw [nsmul_eq_mul]
  have : ((2 ^ k : ℕ) : ZMod (2 ^ k)) = 0 := ZMod.natCast_self (2 ^ k)
  rw [this, zero_mul]

/-- The order-3 generator of the odd arena is killed by `3`. -/
theorem three_nsmul_eight : (3 : ℕ) • (8 : ZMod 24) = 0 := by decide

/-- **2-primary blindness.**  Every additive homomorphism from `ZMod 24` into a
    2-group `ZMod (2^k)` annihilates the order-3 arena element `8`.  No power-of-two
    obstruction can see the `Z/3` summand. -/
theorem two_primary_blind {k : ℕ} (f : ZMod 24 →+ ZMod (2 ^ k)) :
    f 8 = 0 := by
  have h3 : (3 : ℕ) • f 8 = 0 := by
    rw [← map_nsmul, three_nsmul_eight, map_zero]
  have h2 : (2 ^ k) • f 8 = 0 := pow_two_nsmul_zmod k (f 8)
  have hcop : Nat.Coprime 3 (2 ^ k) := Nat.Coprime.pow_right k (by decide)
  exact eq_zero_of_coprime_nsmul hcop h3 h2

/-- The order-3 (odd) arena of `Z/24` is the subgroup `⟨8⟩ = {0, 8, 16}`. -/
theorem odd_arena_orders :
    (3 : ℕ) • (8 : ZMod 24) = 0 ∧ (8 : ZMod 24) ≠ 0 ∧ (16 : ZMod 24) ≠ 0 := by
  refine ⟨three_nsmul_eight, ?_, ?_⟩ <;> decide

/-- The 2-primary arena `⟨3⟩` (order 8) and the odd arena `⟨8⟩` (order 3) meet only
    at `0`: the only element of `Z/24` that is both a multiple of `3` and a
    multiple of `8` is `0`. -/
theorem arenas_disjoint :
    ∀ x : ZMod 24, (∃ a : ZMod 24, x = 3 * a) → (∃ b : ZMod 24, x = 8 * b) → x = 0 := by
  decide

end CRT

/- ===================================================================== -/
/-  Leg C — the 2-primary generator arithmetic (self-contained recap)     -/
/- ===================================================================== -/

namespace TwoPrimaryGenerators

/-- Class-C census generator-space dimensions `2 + 2 + 2 + 2` total `8 = 2^3`
    (linear commutant, bilinear, sesquilinear, antilinear): purely 2-primary. -/
theorem generator_dims_two_primary : (2 + 2 + 2 + 2 : ℤ) = 2 ^ 3 := by norm_num

/-- The cross-chirality Krein signature `96 = 2^5 · 3`: the only odd factor is the
    LOCATED carrier multiplicity `3`, never a congruence. -/
theorem ninety_six_factor : (96 : ℤ) = 2 ^ 5 * 3 := by norm_num

/-- Carrier dimension `192 = 2^6 · 3`. -/
theorem carrier_dim_factor : (192 : ℤ) = 2 ^ 6 * 3 := by norm_num

/-- A spinor dimension `2^k` is never divisible by the odd prime `3`. -/
theorem spinor_dim_not_div_three (k : ℕ) : ¬ (3 ∣ 2 ^ k) := by
  intro h
  have hp : Nat.Prime 3 := by norm_num
  have h2 : (3 : ℕ) ∣ 2 := hp.dvd_of_dvd_pow h
  norm_num at h2

end TwoPrimaryGenerators

end R4TwoArena

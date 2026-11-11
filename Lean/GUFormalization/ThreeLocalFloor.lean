import Mathlib

/-!
Finite algebra for X-D1-P3. This does not formalize the topology or a datum floor.
The additive carrier of virtual C₂-representations is ℤ × ℤ, not ZMod 2.
Coordinates count trivial and sign summands. Forgetting holonomy is rank.
-/
namespace GUFormalization.ThreeLocalFloor

theorem zmod2_to_zmod3_addHom_trivial (f : ZMod 2 →+ ZMod 3) : f = 0 := by
  have heq : (1 : ZMod 2) + 1 = 0 := by decide
  have hz := congrArg f heq
  simp only [map_add, map_zero] at hz
  have hone : f 1 = 0 := (by decide : ∀ a : ZMod 3, a + a = 0 → a = 0) _ hz
  ext x
  fin_cases x
  · change f (0 : ZMod 2) = 0
    exact map_zero f
  · change f (1 : ZMod 2) = 0
    exact hone

theorem two_isUnit_zmod3 : IsUnit (2 : ZMod 3) := by
  exact isUnit_iff_ne_zero.mpr (by decide)

def dimensionCharacter : (ℤ × ℤ) →+ ZMod 3 where
  toFun x := (x.1 : ZMod 3) + (x.2 : ZMod 3)
  map_zero' := by norm_num
  map_add' := by intro a b; simp; ring

def involutionCharacter : (ℤ × ℤ) →+ ZMod 3 where
  toFun x := (x.1 : ZMod 3) - (x.2 : ZMod 3)
  map_zero' := by norm_num
  map_add' := by intro a b; simp; ring

theorem identical_forgotten_rank :
    dimensionCharacter (1, 0) = dimensionCharacter (0, 1) := by
  norm_num [dimensionCharacter]

theorem different_holonomy_character :
    involutionCharacter (1, 0) ≠ involutionCharacter (0, 1) := by
  change (1 : ZMod 3) - 0 ≠ 0 - 1
  decide

theorem character_cannot_factor_through_rank :
    ¬ ∃ g : ZMod 3 → ZMod 3,
      ∀ x, involutionCharacter x = g (dimensionCharacter x) := by
  rintro ⟨g, h⟩
  apply different_holonomy_character
  rw [h, h, identical_forgotten_rank]

end GUFormalization.ThreeLocalFloor

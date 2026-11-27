import Mathlib

/-! Finite algebra and rank core. The all-character classification, smooth
parallel-receiver factorization and native rank512 are written/reviewed
premises, not formalized here. No physical/source interpretation follows. -/
namespace GUFormalization.LocalComplement

theorem uniform_character (p s c d : ℚ) (hd : d ≠ 0)
    (hp : ((p-s)+c)*d=0) (hm : (-(p-s)+c)*d=0) : c=0 := by
  have h1 := (mul_eq_zero.mp hp).resolve_right hd
  have h2 := (mul_eq_zero.mp hm).resolve_right hd
  linarith

theorem minus_character_zero (a b : ℚ)
    (hb : b= -a) (hn : 30*a+8*b=0) : a=0 := by linarith

theorem plus_exception (p s c d : ℚ) (hd : d ≠ 0)
    (h : ((p-s)+c)*d=0) : p=s-c := by
  have he := (mul_eq_zero.mp h).resolve_right hd
  linarith

theorem port_exceptions : (-1:ℚ)-11/12= -23/12 ∧ (1:ℚ)-(-11/12)=23/12 := by norm_num

variable {K O S : Type*} [AddCommGroup K] [Module ℂ K]
  [AddCommGroup O] [Module ℂ O] [AddCommGroup S] [Module ℂ S]
  [FiniteDimensional ℂ S]

/-- Both zero-order and moving-graph terms factor through S × S. -/
theorem two_receiver_rank (B : O →ₗ[ℂ] K)
    (u : O →ₗ[ℂ] S × S) (v : S × S →ₗ[ℂ] K)
    (h : B = v.comp u) :
    Module.finrank ℂ (LinearMap.range B) ≤ 2 * Module.finrank ℂ S := by
  rw [h]
  calc
    Module.finrank ℂ (LinearMap.range (v.comp u)) ≤
        Module.finrank ℂ (LinearMap.range v) :=
      Submodule.finrank_mono (LinearMap.range_comp_le_range u v)
    _ ≤ Module.finrank ℂ (S × S) := LinearMap.finrank_range_le v
    _ = 2 * Module.finrank ℂ S := by rw [Module.finrank_prod]; omega

theorem native_rank_obstruction (r : ℕ) (h : r ≤ 2*128) (hr : r=512) : False := by omega

theorem exceptional_complex_dimension : 9*1024=9216 := by norm_num

end GUFormalization.LocalComplement

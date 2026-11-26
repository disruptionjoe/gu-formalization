import Mathlib

/-! Finite algebra for the actual candidate constraint reduction.
This does not formalize Clifford block classification, moving projectors,
PDE domains, the small-h analytic branch or physical interpretation. -/
namespace GUFormalization.CoupledGhost

theorem auxiliary_square_completion (κ c j w : ℝ) (hκ : κ ≠ 0) :
    w * (κ * c ^ 2 / 2 + c * j) =
      w * (κ * (c + j / κ) ^ 2 / 2 - j ^ 2 / (2 * κ)) := by
  field_simp
  <;> ring

theorem auxiliary_stationarity (κ j : ℝ) (hκ : κ ≠ 0) :
    κ * (-j / κ) + j = 0 := by
  field_simp
  <;> ring

theorem auxiliary_unique (κ c j : ℝ) (hκ : κ ≠ 0)
    (hc : κ * c + j = 0) : c = -j / κ := by
  apply (eq_div_iff hκ).2
  nlinarith [hc]

theorem eliminated_potential (κ j w : ℝ) (hκ : κ ≠ 0) :
    w * (κ * (-j / κ) ^ 2 / 2 + (-j / κ) * j) =
      -w * j ^ 2 / (2 * κ) := by
  field_simp
  <;> ring

theorem first_order_canonical_energy (w κ q p qdot pdot : ℝ) :
    (-24*w*p)*qdot + (24*w*q)*pdot -
      (24*w*(q*pdot-p*qdot) + κ*w*(q^2+48*p^2)/2) =
        -κ*w*(q^2+48*p^2)/2 := by ring

/-- A bounded remainder cannot repair a strictly negative leading energy. -/
theorem negative_leading_energy (κ a C r : ℝ)
    (ha : 0 < a) (hr : r ≤ C) (hκ : 2 * C / a < κ) :
    -κ * a / 2 + r < 0 := by
  have h : 2 * C < κ * a := (div_lt_iff₀ ha).mp hκ
  linarith

/-- The analogous positive witness is retained; an overall action sign does
not make a form with both witnesses positive. -/
theorem positive_leading_energy (κ a C r : ℝ)
    (ha : 0 < a) (hr : -C ≤ r) (hκ : 2 * C / a < κ) :
    0 < κ * a / 2 + r := by
  have h : 2 * C < κ * a := (div_lt_iff₀ ha).mp hκ
  linarith

/-- Exact arithmetic only; the native Clifford block proof supplies counts. -/
theorem full_connection_counts :
    14 * (8128 + 8256) = 229376 ∧
    64482 + 66430 = 130912 ∧ 49310 + 49154 = 98464 ∧
    130912 + 98464 = 229376 := by norm_num

end GUFormalization.CoupledGhost

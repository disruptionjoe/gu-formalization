import Mathlib

/-! Finite adapter cores only. Real-form identification, trace extension,
polynomial coefficient extraction, Spin/Clifford naturality and the inherited
Riemann classification are separately reviewed written dependencies. The
Hessian formulas below do not formalize a functional or a PDE. -/
namespace GUFormalization.RiemannRealForm

/-- Complexification in paired real coordinates. The written real-form
identification supplies x and y; no complex kernel inclusion is assumed. -/
theorem real_pair_kernel_transfer {U W Z : Type*}
    [AddCommGroup U] [Module ℝ U] [AddCommGroup W] [Module ℝ W]
    [AddCommGroup Z] [Module ℝ Z]
    (A : U →ₗ[ℝ] W) (B : U →ₗ[ℝ] Z)
    (h : ∀ x, A x = 0 → B x = 0) (x y : U)
    (hxy : (A x, A y) = (0, 0)) : (B x, B y) = (0, 0) := by
  have hx : A x = 0 := by simpa using congrArg Prod.fst hxy
  have hy : A y = 0 := by simpa using congrArg Prod.snd hxy
  exact Prod.ext (h x hx) (h y hy)

/-- The inherited rows eliminate complex coefficients under arbitrary
nonzero complex row scalings, including orientation/Hodge phases. -/
theorem complex_scaled_four_rows (a b c d s₀ s₁ s₂ s₃ : ℂ)
    (hs₀ : s₀ ≠ 0) (hs₁ : s₁ ≠ 0) (hs₂ : s₂ ≠ 0) (hs₃ : s₃ ≠ 0)
    (h₀ : s₀ * (264 * b) = 0)
    (h₁ : s₁ * (22 * a + 264 * b) = 0)
    (h₂ : s₂ * (312 * d) = 0)
    (h₃ : s₃ * (24 * c + 312 * d) = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 := by
  have hb' : (264 : ℂ) * b = 0 := (mul_eq_zero.mp h₀).resolve_left hs₀
  have hb : b = 0 := (mul_eq_zero.mp hb').resolve_left (by norm_num)
  have hd' : (312 : ℂ) * d = 0 := (mul_eq_zero.mp h₂).resolve_left hs₂
  have hd : d = 0 := (mul_eq_zero.mp hd').resolve_left (by norm_num)
  have ha' : (22 : ℂ) * a + 264 * b = 0 := (mul_eq_zero.mp h₁).resolve_left hs₁
  have hc' : (24 : ℂ) * c + 312 * d = 0 := (mul_eq_zero.mp h₃).resolve_left hs₃
  simp only [hb, mul_zero, add_zero] at ha'
  simp only [hd, mul_zero, add_zero] at hc'
  exact ⟨(mul_eq_zero.mp ha').resolve_left (by norm_num), hb,
    (mul_eq_zero.mp hc').resolve_left (by norm_num), hd⟩

def pulledHessian (q slope h a k b : ℝ) : ℝ :=
  2 * q * (a - slope * h) * (b - slope * k)

/-- The reference-family tangent has deltaA=dB[delta g]. -/
theorem joint_reference_tangent_radical (q slope h k b : ℝ) :
    pulledHessian q slope h (slope * h) k b = 0 := by
  simp [pulledHessian]

/-- A fixed-A metric block need not vanish in the connection chart. -/
theorem fixed_connection_metric_block (q slope h : ℝ) :
    pulledHessian q slope h 0 h 0 = 2 * q * slope ^ 2 * h ^ 2 := by
  unfold pulledHessian
  ring

theorem fixed_connection_metric_nonzero (q slope h : ℝ)
    (hq : q ≠ 0) (hs : slope ≠ 0) (hh : h ≠ 0) :
    pulledHessian q slope h 0 h 0 ≠ 0 := by
  rw [fixed_connection_metric_block]
  exact mul_ne_zero
    (mul_ne_zero (mul_ne_zero (by norm_num) hq) (pow_ne_zero _ hs))
    (pow_ne_zero _ hh)

end GUFormalization.RiemannRealForm

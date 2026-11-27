import Mathlib

/-! Finite characteristic-class and divisibility arithmetic only. The bundle
identifications, integral cohomology, Wu, spin signature and lattice theorems
are separate written/reviewed premises. No physical interpretation follows. -/
namespace GUFormalization.NormalSMCharacteristic

/-- Torsion-free degree-four classes are represented by integer coefficients. -/
theorem split_chern (p d2 w c : ℤ)
    (hw : w=0) (hq : p=d2-2*w) (hc : 5*p=d2-2*c) :
    d2=p ∧ c= -2*p ∧ c+w-d2= -3*p := by omega

/-- The U(1) embedding has zero total determinant weight. -/
theorem determinant_weights : 3*(2:ℤ)+2*(-3)=0 := by norm_num

/-- A product lift gives p=36 ell-squared; spin gives signature multiple16. -/
theorem product_lift_signature (s k n : ℤ)
    (hs : s=16*k) (hp : 3*s=36*n) : 48 ∣ s := by omega

/-- Hyperbolic-plane vector e+2m f has square4m. -/
theorem hyperbolic_lift_square (m : ℤ) :
    2*1*(2*m)=4*m ∧ 36*(2*1*(2*m))=3*(48*m) := by constructor <;> ring

/-- Determinant twisting removes the geometric zero of the weak second class. -/
theorem weak_untwist (n w : ℤ) (h : 0=w+9*n) : w= -9*n := by omega

/-- The rank-three twist contributes12 ell-squared. -/
theorem color_untwist (n c : ℤ) (h : -2*(36*n)=c+12*n) : c= -84*n := by omega

/-- The known signature-minus16 base cannot have a direct-product lift. -/
theorem quotient_not_product : ¬ (48:ℤ) ∣ -16 := by norm_num

/-- A fixed even determinant can fail the sixth-root test at signature zero. -/
theorem fixed_determinant_not_sixth : ¬ ∃ a : ℤ, 2=6*a := by omega

/-- Trace-free rational classes agree with the SU factors when lifted. -/
theorem tracefree_lift (n : ℚ) :
    -(36*n)/4= -9*n ∧ -(7*(36*n))/3= -84*n := by constructor <;> ring

end GUFormalization.NormalSMCharacteristic

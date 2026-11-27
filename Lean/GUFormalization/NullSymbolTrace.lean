import Mathlib

/-! Finite scalar cores only. Trace additivity on invariant images, the
representation calculation, principal-symbol covariance and source scope
are written arguments, not formalized by these arithmetic lemmas. -/
namespace GUFormalization.NullSymbolTrace

/-- Scalar telescope after short-exact-sequence trace additivity has been
established externally. -/
theorem image_trace_telescope (x y z : ℂ) :
    x - (x + y) + (y + z) - z = 0 := by
  ring

/-- Alternating shifted traces for dimensions e,n*e,n*e,e and scalar orders
a,b,c. The equality does not assume that an exact complex exists. -/
theorem shifted_trace_identity (n e r a b c : ℂ) :
    r - (n * r - a * (n * e)) +
      (n * r - (a + b) * (n * e)) -
      (r - (a + b + c) * e) =
    (a + c - (n - 1) * b) * e := by
  ring

/-- Dimension14 with first-order ends has no nonnegative integer middle
order satisfying the necessary trace balance. -/
theorem no_dimension14_middle_order (b : ℕ) : 13 * b ≠ 2 := by
  omega

end GUFormalization.NullSymbolTrace

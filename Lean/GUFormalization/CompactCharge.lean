import Mathlib

/-! Finite algebraic cores only. The smooth cutoff construction, local
normal-flux ODE, support statement, Stokes theorem, Killing identity and
continuum positivity argument remain written mathematical inputs. -/
namespace GUFormalization.CompactCharge

/-- Cancellation after a Stokes balance has been supplied. Neither the
balance nor its boundary hypotheses is established by this finite lemma. -/
theorem charge_zero_of_balance (initial final side : ℝ)
    (balance : final - initial + side = 0)
    (late_zero : final = 0) (side_zero : side = 0) : initial = 0 := by
  linarith

/-- Finite analogue only: this does not formalize a continuum integral. -/
theorem nonnegative_zero_sum {ι : Type*} [Fintype ι]
    (e : ι → ℝ) (nonnegative : ∀ i, 0 ≤ e i)
    (total_zero : ∑ i, e i = 0) : ∀ i, e i = 0 := by
  intro i
  have upper : e i ≤ ∑ j, e j :=
    Finset.single_le_sum (fun j _ => nonnegative j) (Finset.mem_univ i)
  rw [total_zero] at upper
  exact le_antisymm upper (nonnegative i)

end GUFormalization.CompactCharge

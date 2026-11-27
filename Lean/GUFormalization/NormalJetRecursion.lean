import Mathlib

/-! Finite recurrence cores only. The normal ODE, smooth parameter dependence,
jet realization, support and compact-charge theorem remain written inputs. -/
namespace GUFormalization.NormalJetRecursion

/-- A next coefficient depending only on the preceding finite history is
unique once the initial coefficient and right-hand side are fixed. The lower
history map need not be linear. -/
theorem causal_recurrence_unique {E : Type*} [Sub E]
    (rhs : ℕ → E)
    (lower : (n : ℕ) → (Fin (n + 1) → E) → E)
    (w z : ℕ → E) (hzero : w 0 = z 0)
    (hw : ∀ n, w (n + 1) = rhs n - lower n (fun i => w i))
    (hz : ∀ n, z (n + 1) = rhs n - lower n (fun i => z i)) :
    w = z := by
  funext n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    cases n with
    | zero => exact hzero
    | succ n =>
      have history : (fun i : Fin (n + 1) => w i) =
          (fun i : Fin (n + 1) => z i) := by
        funext i
        exact ih i.val i.isLt
      rw [hw n, hz n, history]

/-- Algebraic rearrangement used to solve for the next normal coefficient;
this is not an ODE existence result. -/
theorem recurrence_rearrangement {E : Type*} [AddCommGroup E]
    (nextCoeff lower rhs : E) :
    nextCoeff + lower = rhs ↔ nextCoeff = rhs - lower := by
  constructor
  · intro h
    calc
      nextCoeff = (nextCoeff + lower) - lower := by abel
      _ = rhs - lower := by rw [h]
  · intro h
    rw [h]
    abel

end GUFormalization.NormalJetRecursion

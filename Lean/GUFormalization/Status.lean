import Mathlib

set_option autoImplicit false

/-!
# Claim Status Kernel

This file formalizes the repo-local governance invariant:

If a claim depends on other claims, it cannot carry a stronger status than any
load-bearing dependency.

It is intentionally finite and administrative. It does not prove GU mathematics.
-/

namespace GUFormalization

/-- Repo-local claim status order, from weakest to strongest. -/
inductive ClaimStatus where
  | blocked
  | open
  | conditionallyResolved
  | resolved
  | verified
  deriving DecidableEq, Repr

namespace ClaimStatus

/-- Numeric rank used only to define the status preorder. -/
def rank : ClaimStatus -> Nat
  | blocked => 0
  | open => 1
  | conditionallyResolved => 2
  | resolved => 3
  | verified => 4

instance : LE ClaimStatus where
  le a b := rank a <= rank b

instance (a b : ClaimStatus) : Decidable (a <= b) :=
  inferInstanceAs (Decidable (rank a <= rank b))

theorem le_iff_rank_le (a b : ClaimStatus) : a <= b <-> rank a <= rank b :=
  Iff.rfl

theorem le_refl (a : ClaimStatus) : a <= a := by
  exact Nat.le_refl (rank a)

theorem le_trans {a b c : ClaimStatus} (hab : a <= b) (hbc : b <= c) : a <= c := by
  exact Nat.le_trans hab hbc

theorem verified_not_le_open : Not (verified <= open) := by
  decide

theorem resolved_not_le_open : Not (resolved <= open) := by
  decide

end ClaimStatus

/-- A claim is dependency-admissible when it is no stronger than every dependency. -/
def AllowedByDeps (claim : ClaimStatus) (deps : List ClaimStatus) : Prop :=
  forall dep, List.Mem dep deps -> claim <= dep

theorem allowedByDeps_nil (claim : ClaimStatus) : AllowedByDeps claim [] := by
  intro dep h
  cases h

theorem claim_le_first_dependency {claim dep : ClaimStatus} {deps : List ClaimStatus}
    (h : AllowedByDeps claim (dep :: deps)) : claim <= dep := by
  exact h dep (by simp)

theorem verified_not_allowed_over_open :
    Not (AllowedByDeps ClaimStatus.verified [ClaimStatus.open]) := by
  intro h
  exact ClaimStatus.verified_not_le_open (h ClaimStatus.open (by simp))

theorem resolved_not_allowed_over_open :
    Not (AllowedByDeps ClaimStatus.resolved [ClaimStatus.open]) := by
  intro h
  exact ClaimStatus.resolved_not_le_open (h ClaimStatus.open (by simp))

end GUFormalization

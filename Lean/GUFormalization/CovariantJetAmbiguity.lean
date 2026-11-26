import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Tactic

/-!
Finite algebra for the covariant finite-jet ambiguity result.

This file does NOT formalize the analytic Cauchy problem, the native operator,
Lorentz covariance, or physical admissibility. Those are supplied by the
separate analytic proof. It checks two finite algebraic consequences:

* lifts with an identical finite measurement form an affine kernel fibre;
  an injectively parameterized hidden family gives genuinely distinct lifts;
* the normal-line witnesses (2 s^2)^m have independent coefficients and
  vanish below their first possible normal order.
-/

namespace GUFormalization.CovariantJetAmbiguity

section AffineKernel

variable {k X V Z A : Type*} [Field k]
  [AddCommGroup X] [Module k X]
  [AddCommGroup V] [Module k V]
  [AddCommGroup Z] [Module k Z]
  [AddCommGroup A] [Module k A]

/-- Any measurement-invisible correction is also observation-invisible when
the observation is one component of that measurement. -/
theorem observation_kills_measurement_kernel
    (q : V →ₗ[k] X) (jet : V →ₗ[k] Z) (forget : Z →ₗ[k] X)
    (H : X →ₗ[k] V) (hq : q = forget.comp jet)
    (hH : jet.comp H = 0) : q.comp H = 0 := by
  rw [hq, LinearMap.comp_assoc, hH]
  simp

/-- Adding an invisible correction preserves both the observation right
inverse and every measurement in the fixed finite jet map. -/
theorem hidden_shift_preserves_lift
    (q : V →ₗ[k] X) (jet : V →ₗ[k] Z) (forget : Z →ₗ[k] X)
    (E H : X →ₗ[k] V) (hq : q = forget.comp jet)
    (hE : q.comp E = LinearMap.id) (hH : jet.comp H = 0) :
    q.comp (E + H) = LinearMap.id ∧ jet.comp (E + H) = jet.comp E := by
  have hqH := observation_kills_measurement_kernel q jet forget H hq hH
  constructor
  · rw [LinearMap.comp_add, hE, hqH, add_zero]
  · rw [LinearMap.comp_add, hH, add_zero]

/-- Completeness, not only a one-way construction: the entire space of lifts
with E's finite measurement is exactly E plus the measurement kernel. -/
theorem lift_fibre_eq_affine_kernel
    (q : V →ₗ[k] X) (jet : V →ₗ[k] Z) (forget : Z →ₗ[k] X)
    (E F : X →ₗ[k] V) (hq : q = forget.comp jet)
    (hE : q.comp E = LinearMap.id) :
    (q.comp F = LinearMap.id ∧ jet.comp F = jet.comp E) ↔
      ∃ H : X →ₗ[k] V, jet.comp H = 0 ∧ F = E + H := by
  constructor
  · intro hF
    refine ⟨F - E, ?_, ?_⟩
    · rw [LinearMap.comp_sub, hF.2, sub_self]
    · abel
  · rintro ⟨H, hH, rfl⟩
    exact hidden_shift_preserves_lift q jet forget E H hq hE hH

/-- Injectivity of a hidden family survives translation by a chosen lift.
This works for arbitrary parameter vector spaces, not merely one scalar. -/
theorem translated_hidden_family_injective
    (E : X →ₗ[k] V) (T : A →ₗ[k] (X →ₗ[k] V))
    (hT : Function.Injective T) :
    Function.Injective (fun a => E + T a) := by
  intro a b hab
  exact hT (add_left_cancel hab)

/-- A nonzero hidden map gives an injective scalar family of distinct lifts. -/
theorem scalar_hidden_family_injective
    (E H : X →ₗ[k] V) (hH : H ≠ 0) :
    Function.Injective (fun a : k => E + a • H) := by
  intro a b hab
  have hs : a • H = b • H := add_left_cancel hab
  have hz : (a - b) • H = 0 := by
    rw [sub_smul, hs, sub_self]
  exact sub_eq_zero.mp ((smul_eq_zero.mp hz).resolve_right hH)

/-- Every member of an arbitrary hidden parameter family stays in the same
measurement fibre and remains a right inverse. -/
theorem hidden_parameter_family
    (q : V →ₗ[k] X) (jet : V →ₗ[k] Z) (forget : Z →ₗ[k] X)
    (E : X →ₗ[k] V) (T : A →ₗ[k] (X →ₗ[k] V))
    (hq : q = forget.comp jet) (hE : q.comp E = LinearMap.id)
    (hT : ∀ a, jet.comp (T a) = 0) (a : A) :
    q.comp (E + T a) = LinearMap.id ∧
      jet.comp (E + T a) = jet.comp E := by
  exact hidden_shift_preserves_lift q jet forget E (T a) hq hE (hT a)

/-- The contrary control: a chosen observation right inverse is injective.
Invisible solutions in the ambient space do not give a kernel inside its
chosen image. -/
theorem chosen_right_inverse_injective
    (q : V →ₗ[k] X) (E : X →ₗ[k] V)
    (hE : q.comp E = LinearMap.id) : Function.Injective E := by
  intro x y hxy
  have hx : q (E x) = x := LinearMap.congr_fun hE x
  have hy : q (E y) = y := LinearMap.congr_fun hE y
  calc
    x = q (E x) := hx.symm
    _ = q (E y) := congrArg q hxy
    _ = y := hy

end AffineKernel

section EvenPolynomialWitnesses

open Polynomial
open scoped BigOperators

/-- Restriction of P(S)^m to S=s diag(1,-1,0,0), with coefficient a_m:
P(S)=2s^2, hence the witness is 2^m a_m s^(2m). -/
noncomputable def evenWitness (m : ℕ) (a : ℚ) : Polynomial ℚ :=
  Polynomial.monomial (2 * m) ((2 : ℚ) ^ m * a)

/-- Finite sums, not a convergence claim about infinite series. -/
noncomputable def finiteWitness (s : Finset ℕ) (a : ℕ → ℚ) : Polynomial ℚ :=
  ∑ m ∈ s, evenWitness m (a m)

theorem evenWitness_first_coefficient (m : ℕ) (a : ℚ) :
    (evenWitness m a).coeff (2 * m) = (2 : ℚ) ^ m * a := by
  simp [evenWitness]

theorem evenWitness_lower_coefficient (m j : ℕ) (a : ℚ) (h : j < 2 * m) :
    (evenWitness m a).coeff j = 0 := by
  apply Polynomial.coeff_monomial_of_ne
  omega

/-- Extraction isolates every member of any finite subfamily, even if the
chosen exponents are not consecutive. -/
theorem finiteWitness_isolate
    (s : Finset ℕ) (a : ℕ → ℚ) (m : ℕ) (hm : m ∈ s) :
    (finiteWitness s a).coeff (2 * m) = (2 : ℚ) ^ m * a m := by
  unfold finiteWitness
  rw [Polynomial.finsetSum_coeff]
  rw [Finset.sum_eq_single m]
  · exact evenWitness_first_coefficient m (a m)
  · intro b hb hbm
    apply Polynomial.coeff_monomial_of_ne
    omega
  · intro hnot
    exact False.elim (hnot hm)

/-- Linear independence in finite-sum form: no cancellation between
different even vanishing orders can hide a nonzero history coefficient. -/
theorem finiteWitness_zero_forces_all_coefficients_zero
    (s : Finset ℕ) (a : ℕ → ℚ) (hz : finiteWitness s a = 0) :
    ∀ m ∈ s, a m = 0 := by
  intro m hm
  have hi := finiteWitness_isolate s a m hm
  rw [hz, Polynomial.coeff_zero] at hi
  have hp : (2 : ℚ) ^ m ≠ 0 := pow_ne_zero m (by norm_num)
  exact (mul_eq_zero.mp hi.symm).resolve_left hp

/-- A finite family starting above order N is wholly invisible to every
polynomial coefficient of order at most N. -/
theorem finiteWitness_vanishes_through
    (s : Finset ℕ) (a : ℕ → ℚ) (N : ℕ)
    (hhigh : ∀ m ∈ s, N < 2 * m) (j : ℕ) (hj : j ≤ N) :
    (finiteWitness s a).coeff j = 0 := by
  unfold finiteWitness
  rw [Polynomial.finsetSum_coeff]
  apply Finset.sum_eq_zero
  intro m hm
  exact evenWitness_lower_coefficient m j (a m) (lt_of_le_of_lt hj (hhigh m hm))

/-- There are arbitrarily many distinct finite hidden coefficients above
any prescribed jet cutoff. This is the elementary degree bound used by the
analytic witness family; it makes no analytic convergence assertion. -/
theorem unbounded_even_orders (N count : ℕ) :
    ∀ i < count, N < 2 * (N + 1 + i) := by
  intro i hi
  omega

end EvenPolynomialWitnesses

end GUFormalization.CovariantJetAmbiguity

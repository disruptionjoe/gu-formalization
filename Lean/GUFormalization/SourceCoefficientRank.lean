import GUFormalization.SourceNativeFamilyOwnerIdentifiability

/-!
# Source coefficient rank discriminator

This module separates a generic exact coefficient constraint from the frozen
source packet that supplies no equation between the two quadratic-owner
coordinates. A nonzero kernel direction makes the homogeneous coefficient
solution nonunique. The strict packet's zero constraint therefore leaves the
`54` and `210` axes distinct.

The theorem does not claim that the source owns these coordinates as an action,
nor does it select a family covector, normalization, coefficient ratio, real
structure, mass, or physical quotient.
-/

set_option autoImplicit false

namespace GUFormalization
namespace SourceCoefficientRank

/-- A coefficient constraint is unique at zero exactly when its homogeneous
solution has no nonzero direction. -/
def UniqueHomogeneousSolution {K V W : Type*}
    [Field K] [AddCommGroup V] [Module K V]
    [AddCommGroup W] [Module K W] (A : V →ₗ[K] W) : Prop :=
  ∀ x, A x = 0 → x = 0

theorem uniqueHomogeneousSolution_iff_injective
    {K V W : Type*} [Field K]
    [AddCommGroup V] [Module K V]
    [AddCommGroup W] [Module K W] (A : V →ₗ[K] W) :
    UniqueHomogeneousSolution A ↔ Function.Injective A := by
  constructor
  · intro h x y hxy
    have hzero : A (x - y) = 0 := by
      rw [map_sub, hxy, sub_self]
    exact sub_eq_zero.mp (h (x - y) hzero)
  · intro hinj x hx
    apply hinj
    simpa using hx

/-- Any nonzero kernel direction gives a second solution through every
homogeneous solution. -/
theorem nonunique_of_nonzero_kernel
    {K V W : Type*} [Field K]
    [AddCommGroup V] [Module K V]
    [AddCommGroup W] [Module K W]
    (A : V →ₗ[K] W) {x k : V}
    (hx : A x = 0) (hk : A k = 0) (hk0 : k ≠ 0) :
    ∃ y, A y = 0 ∧ y ≠ x := by
  refine ⟨x + k, ?_, ?_⟩
  · rw [map_add, hx, hk, add_zero]
  · intro h
    apply hk0
    exact add_left_cancel (h.trans (add_zero x).symm)

/-- The two independent quadratic-owner coordinates. -/
inductive OwnerCoordinate where
  | d54
  | d210
  deriving DecidableEq, Repr

/-- Scalar coefficient space after family-copy exchange has been imposed
inside each owner coordinate. -/
abbrev OwnerSpace (K : Type*) := OwnerCoordinate → K

open OwnerCoordinate

/-- Unit packet supported on the `54` owner coordinate. -/
def owner54Axis (K : Type*) [Zero K] [One K] : OwnerSpace K
  | d54 => 1
  | d210 => 0

/-- Unit packet supported on the `210` owner coordinate. -/
def owner210Axis (K : Type*) [Zero K] [One K] : OwnerSpace K
  | d54 => 0
  | d210 => 1

/-- The strict frozen public-source packet supplies no homogeneous equation on
the owner coordinates. -/
def strictSourceConstraint (K : Type*) [Field K] :
    OwnerSpace K →ₗ[K] K := 0

theorem strictSource_owner54_solution (K : Type*) [Field K] :
    strictSourceConstraint K (owner54Axis K) = 0 := by
  rfl

theorem strictSource_owner210_solution (K : Type*) [Field K] :
    strictSourceConstraint K (owner210Axis K) = 0 := by
  rfl

theorem owner_axes_distinct (K : Type*) [Field K] :
    owner54Axis K ≠ owner210Axis K := by
  intro h
  have hcoord := congrFun h d54
  have : (1 : K) = 0 := by
    simpa [owner54Axis, owner210Axis] using hcoord
  exact one_ne_zero this

/-- The strict packet cannot uniquely select an owner coefficient packet: it
has at least the two distinct axis solutions. -/
theorem strictSource_does_not_select_owner (K : Type*) [Field K] :
    ¬ UniqueHomogeneousSolution (strictSourceConstraint K) := by
  intro h
  have h54 := h (owner54Axis K) (strictSource_owner54_solution K)
  have h210 := h (owner210Axis K) (strictSource_owner210_solution K)
  exact owner_axes_distinct K (h54.trans h210.symm)

/-- Stronger kernel-form receipt: a source extension can become unique only by
removing every nonzero kernel direction. -/
theorem sourceExtension_nonunique_until_kernel_closed
    {K W : Type*} [Field K] [AddCommGroup W] [Module K W]
    (A : OwnerSpace K →ₗ[K] W) {k : OwnerSpace K}
    (hk : A k = 0) (hk0 : k ≠ 0) :
    ¬ UniqueHomogeneousSolution A := by
  intro h
  exact hk0 (h k hk)

end SourceCoefficientRank
end GUFormalization

import GUFormalization.LocatedNotForcedLegs

set_option autoImplicit false

/-!
Targeted V15-6 certificate for finite complex Krein transversality.

This entrypoint checks the scalar field, sesquilinear form, finite dimensions,
intersection invariant, and complex-linear isometry transport exposed by the
proof-bearing module.
-/

namespace GUFormalization.KreinTransversality

variable {V : Type*} [AddCommGroup V] [Module ℂ V]

example (K : FiniteKreinForm V) :
    (K.form : V →ₗ⋆[ℂ] V →ₗ[ℂ] ℂ) = K.form :=
  rfl

example (K : FiniteKreinForm V) : K.form.IsSymm :=
  K.hermitian

example (K : FiniteKreinForm V) : K.form.Nondegenerate :=
  K.nondegenerate

example [FiniteDimensional ℂ V]
    (K : FiniteKreinForm V) (P Wp Wm : Submodule ℂ V)
    (hP : PositiveOn K P)
    (hWp : TotallyIsotropic K Wp) (hWm : TotallyIsotropic K Wm) :
    intersectionDifference P Wp Wm = 0 :=
  intersectionDifference_eq_zero K P Wp Wm hP hWp hWm

example [FiniteDimensional ℂ V]
    (K : FiniteKreinForm V) (P Wp Wm : Submodule ℂ V)
    (hVdim : Module.finrank ℂ V = 192)
    (hPdim : Module.finrank ℂ P = 96)
    (hWpdim : Module.finrank ℂ Wp = 96)
    (hWmdim : Module.finrank ℂ Wm = 96)
    (hP : PositiveOn K P)
    (hWp : TotallyIsotropic K Wp) (hWm : TotallyIsotropic K Wm) :
    intersectionDifference P Wp Wm = 0 :=
  carrier_intersectionDifference_eq_zero K P Wp Wm
    hVdim hPdim hWpdim hWmdim hP hWp hWm

example [FiniteDimensional ℂ V]
    (K : FiniteKreinForm V) (U : V ≃ₗ[ℂ] V)
    (P Wp Wm : Submodule ℂ V)
    (hU : Isometry K U) (hP : PositiveOn K P)
    (hWp : TotallyIsotropic K Wp) (hWm : TotallyIsotropic K Wm) :
    intersectionDifference
        (P.map U.toLinearMap) (Wp.map U.toLinearMap) (Wm.map U.toLinearMap) = 0 :=
  intersectionDifference_map_eq_zero K U P Wp Wm hU hP hWp hWm

#print axioms intersectionDifference_eq_zero
#print axioms carrier_intersectionDifference_eq_zero
#print axioms intersectionDifference_map_eq_zero

end GUFormalization.KreinTransversality

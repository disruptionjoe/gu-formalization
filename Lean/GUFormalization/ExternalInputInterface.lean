import Mathlib

/-!
# Exact external-input interfaces

This module gives a deliberately small set-level theorem for a proposed split
of an external-input type `E` into tagged tiebreaker and setting codes.

The theorem is conditional: an exact two-type interface exists for a supplied
classifier exactly when that classifier is bijective.  Surjectivity is the
no-missing-port obligation and injectivity is the no-collision/no-double-count
obligation.  The theorem does not prove that GU's physical external inputs
have been exhaustively collected, that a datum is physically external, or that
the live GU candidates realize either summand.

The final section records exact hostile controls.  In particular, set-level
bijection is not silently upgraded to an equivalence preserving automorphisms:
that compatibility is a separate premise.
-/

set_option autoImplicit false

namespace GUFormalization.ExternalInputInterface

universe u v w

/-- A proposed tiebreaker is not an untyped label: it names an obstruction or
indifference locus and supplies one Boolean branch.  Showing that a particular
obstruction is genuinely binary remains an application premise. -/
abbrev TiebreakerCode (Obstruction : Type v) := Obstruction × Bool

/-- A proposed setting is a point in a typed family of free values.  The index
names the modulus and the dependent fiber gives that modulus's value type. -/
abbrev SettingCode (Modulus : Type v) (Value : Modulus → Type w) :=
  Σ modulus, Value modulus

/-- A proposed implementation of the two-type interface.  `encode` classifies
an external input into a tagged tiebreaker/setting code; `decode` realizes a
code as an external input. -/
structure Interface (E : Type u) (Tie : Type v) (Setting : Type w) where
  encode : E → Tie ⊕ Setting
  decode : Tie ⊕ Setting → E

/-- Exactness requires both triangle identities.  The first forbids a missing
external port; the second forbids aliases, overlap, and double-counted codes. -/
def Exact {E : Type u} {Tie : Type v} {Setting : Type w}
    (I : Interface E Tie Setting) : Prop :=
  Function.LeftInverse I.decode I.encode ∧
    Function.RightInverse I.decode I.encode

/-- An exact implementation yields the advertised equivalence. -/
def equivOfExact {E : Type u} {Tie : Type v} {Setting : Type w}
    (I : Interface E Tie Setting) (h : Exact I) : E ≃ Tie ⊕ Setting where
  toFun := I.encode
  invFun := I.decode
  left_inv := h.1
  right_inv := h.2

/-- Sharp claim ceiling: for a fixed classifier, some exact decoder exists if
and only if the classifier is bijective.  This is a schema, not a proof that a
GU classifier satisfying either obligation has been constructed. -/
theorem exists_exact_decoder_iff_bijective
    {E : Type u} {Tie : Type v} {Setting : Type w}
    (encode : E → Tie ⊕ Setting) :
    (∃ decode : Tie ⊕ Setting → E,
      Function.LeftInverse decode encode ∧
        Function.RightInverse decode encode) ↔
      Function.Bijective encode := by
  constructor
  · rintro ⟨decode, hleft, hright⟩
    exact ⟨hleft.injective, hright.surjective⟩
  · intro h
    let e : E ≃ Tie ⊕ Setting := Equiv.ofBijective encode h
    exact ⟨e.symm, e.left_inv, e.right_inv⟩

/-- Every external input is realized from a code under exactness. -/
theorem no_missing_port {E : Type u} {Tie : Type v} {Setting : Type w}
    (I : Interface E Tie Setting) (h : Exact I) (e : E) :
    ∃ code : Tie ⊕ Setting, I.decode code = e :=
  ⟨I.encode e, h.1 e⟩

/-- An exact tagged coproduct cannot realize one external input from both a
tiebreaker code and a setting code. -/
theorem no_overlap {E : Type u} {Tie : Type v} {Setting : Type w}
    (I : Interface E Tie Setting) (h : Exact I) (tie : Tie) (setting : Setting) :
    I.decode (.inl tie) ≠ I.decode (.inr setting) := by
  intro hoverlap
  have hcodes := congrArg I.encode hoverlap
  rw [h.2 (.inl tie), h.2 (.inr setting)] at hcodes
  cases hcodes

/-- Exactness gives a unique code for every external input, making the
no-double-count condition explicit. -/
theorem unique_code {E : Type u} {Tie : Type v} {Setting : Type w}
    (I : Interface E Tie Setting) (h : Exact I) (e : E) :
    ∃! code : Tie ⊕ Setting, I.decode code = e := by
  refine ⟨I.encode e, h.1 e, ?_⟩
  intro code hcode
  calc
    code = I.encode (I.decode code) := (h.2 code).symm
    _ = I.encode e := congrArg I.encode hcode

/-! ## Automorphism data are a separate obligation -/

/-- A type together with one distinguished automorphism.  This is the least
structure needed to expose why a bare set equivalence cannot establish the
groupoid/automorphism part of the proposed physical interface. -/
structure SymmetricType where
  Carrier : Type u
  aut : Carrier ≃ Carrier

/-- A carrier equivalence respects the declared automorphisms exactly when it
intertwines them. -/
def SymmetryRespecting (A B : SymmetricType) (e : A.Carrier ≃ B.Carrier) : Prop :=
  ∀ x, e (A.aut x) = B.aut (e x)

/-- If the target automorphism is trivial, a symmetry-respecting equivalence
forces the source automorphism to be trivial too. -/
theorem source_aut_trivial_of_target_aut_trivial
    (A B : SymmetricType) (e : A.Carrier ≃ B.Carrier)
    (hTarget : B.aut = Equiv.refl B.Carrier)
    (hRespect : SymmetryRespecting A B e) :
    A.aut = Equiv.refl A.Carrier := by
  apply Equiv.ext
  intro x
  apply e.injective
  simpa [hTarget] using hRespect x

/-! ## Exact hostile controls -/

inductive ThreePort where
  | tiebreaker
  | setting
  | plantedThird
  deriving DecidableEq, Fintype

/-- A planted third external type cannot be equivalent to one singleton
tiebreaker plus one singleton setting. -/
theorem planted_third_type_control :
    ¬ Nonempty (ThreePort ≃ PUnit ⊕ PUnit) := by
  rintro ⟨e⟩
  have hcard := Fintype.card_congr e
  have hthree : Fintype.card ThreePort = 3 := by decide
  rw [hthree] at hcard
  norm_num at hcard

inductive TwoPort where
  | tiebreaker
  | setting
  deriving DecidableEq, Fintype

/-- Hostile implementation in which both tagged codes decode to the same
external port. -/
def overlappingInterface : Interface TwoPort PUnit PUnit where
  encode
    | .tiebreaker => .inl PUnit.unit
    | .setting => .inr PUnit.unit
  decode
    | .inl _ => .tiebreaker
    | .inr _ => .tiebreaker

theorem overlap_double_count_control : ¬ Exact overlappingInterface := by
  intro h
  have hright := h.2 (Sum.inr PUnit.unit)
  simp [overlappingInterface] at hright

/-- Hostile implementation in which the planted third port is never recovered
after encoding. -/
def missingPortInterface : Interface ThreePort PUnit PUnit where
  encode
    | .tiebreaker => .inl PUnit.unit
    | .setting => .inr PUnit.unit
    | .plantedThird => .inl PUnit.unit
  decode
    | .inl _ => .tiebreaker
    | .inr _ => .setting

theorem missing_port_control : ¬ Exact missingPortInterface := by
  intro h
  have hleft := h.1 ThreePort.plantedThird
  simp [missingPortInterface] at hleft

/-- The nontrivial Boolean flip automorphism. -/
def boolFlip : Bool ≃ Bool where
  toFun := Bool.not
  invFun := Bool.not
  left_inv x := by cases x <;> rfl
  right_inv x := by cases x <;> rfl

theorem boolFlip_nontrivial : boolFlip ≠ Equiv.refl Bool := by
  intro h
  have hfalse := Equiv.congr_fun h false
  simp [boolFlip] at hfalse

def nontrivialSymmetricPort : SymmetricType where
  Carrier := Bool
  aut := boolFlip

def trivialSymmetricCode : SymmetricType where
  Carrier := Bool
  aut := Equiv.refl Bool

/-- The carriers have the same cardinality, but no equivalence can erase the
nontrivial source automorphism while respecting symmetry. -/
theorem nontrivial_automorphism_control :
    ¬ ∃ e : nontrivialSymmetricPort.Carrier ≃ trivialSymmetricCode.Carrier,
      SymmetryRespecting nontrivialSymmetricPort trivialSymmetricCode e := by
  rintro ⟨e, hRespect⟩
  have htrivial := source_aut_trivial_of_target_aut_trivial
    nontrivialSymmetricPort trivialSymmetricCode e rfl hRespect
  exact boolFlip_nontrivial htrivial

/-- A selector that silently chooses the first enumerated solution changes
under reversal; order is therefore an extra input unless invariance is proved. -/
def firstOr (fallback : Bool) : List Bool → Bool
  | [] => fallback
  | x :: _ => x

theorem hidden_solver_order_control :
    firstOr false [false, true] ≠ firstOr false [true, false] := by
  decide

end GUFormalization.ExternalInputInterface

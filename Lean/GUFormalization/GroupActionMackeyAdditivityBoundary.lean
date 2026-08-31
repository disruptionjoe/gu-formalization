import GUFormalization.GroupActionMackeyCategory
import Mathlib.CategoryTheory.Limits.Shapes.ZeroObjects
import Mathlib.CategoryTheory.Preadditive.Basic

/-!
# Additivity boundary for the supplied-action Mackey theorem

The canonical Mackey natural isomorphism lives on the ordinary category of
supplied group actions.  That source category is not preadditive: for any
group, there is no morphism from the nonempty one-point trivial action to the
empty trivial action, whereas a preadditive category would provide a zero
morphism between every pair of objects.

Consequently the existing natural isomorphism is not, by itself, an additive
Mackey functor.  Such a construction needs a separately defined additive
source (for example a span/Burnside-style completion) together with owned
restriction and transfer data.  This file proves only the raw-source
obstruction.  It does not construct that completion or any physical action.
-/

set_option autoImplicit false

namespace GUFormalization
namespace GroupActionMackeyAdditivityBoundary

open CategoryTheory CategoryTheory.Limits

universe u v

variable (H : Type u) [Group H]

/-- The empty supplied `H`-action. -/
def emptyAction : Action (Type v) H := Action.trivial H PEmpty

/-- The nonempty one-point supplied `H`-action. -/
def pointAction : Action (Type v) H := Action.trivial H PUnit

/-- There is no action morphism from the one-point action to the empty action. -/
theorem no_point_to_empty (f : pointAction H ⟶ emptyAction H) : False :=
  PEmpty.elim (f.hom PUnit.unit)

/-- The ordinary category of supplied `H`-actions cannot be preadditive.

In a preadditive category every hom-set is an additive commutative group and
therefore contains a zero morphism.  The point-to-empty hom-set is empty. -/
theorem action_preadditive_false
    (h : Preadditive (Action (Type v) H)) : False := by
  letI : Preadditive (Action (Type v) H) := h
  exact no_point_to_empty H (0 : pointAction H ⟶ emptyAction H)

/-- The ordinary category of supplied `H`-actions also has no zero object.

A zero object would induce zero morphisms between every pair of actions, again
contradicting the point-to-empty obstruction. -/
theorem action_has_no_zero_object : ¬ HasZeroObject (Action (Type v) H) := by
  intro h
  letI : HasZeroObject (Action (Type v) H) := h
  letI : HasZeroMorphisms (Action (Type v) H) :=
    HasZeroObject.zeroMorphismsOfZeroObject
  exact no_point_to_empty H (0 : pointAction H ⟶ emptyAction H)

end GroupActionMackeyAdditivityBoundary
end GUFormalization

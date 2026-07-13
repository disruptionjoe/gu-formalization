set_option autoImplicit false

/-!
# W117: The Residual-Selection Lemma

ONE lemma, stated once at the shared level of generality, from which BOTH
machine-checked instances derive as corollaries:

- **Paper instance** (`papers/candidates/observer-value-selection-theorem/`):
  Lawvere no-closure and the no-invariant-valuation result for a two-element grading with the
  fixpoint-free swap involution.
- **TI instance** (temporal-issuance, `formal/lean/OnlineIssuance/
  Comparator.lean`, T5 `diagSem_escapes`): no countable total Nat-indexed
  Boolean family internally indexes its own extensional diagonal.

The shared core is Lawvere's fixed-point theorem in Yanofsky's elementary
form, phrased pointwise (funext-free — mirroring TI's own discipline: the
proofs below use `congrFun`-style pointwise disagreement only; no
function-extensionality axiom enters any escape proof).

Honesty notes (mirroring both repos' hostile-verifier vocabulary):
- The lemma itself is CLASSICAL (Lawvere 1969 / Yanofsky 2003; with
  `B = Bool` and `α = not` it is literally Cantor). The paper already
  grades novelty (b) NOVEL PACKAGING. The value of THIS file is not lemma
  novelty; it is the TWO-INSTANCE kernel anchor — the same checked lemma
  discharging both the self-valuation instance and the issuance instance.
- The TI corollary below is a SHAPE-REPRODUCTION: TI is a separate Lake
  project and cannot be imported here, so `SemFamily` / `InternallyIndexed`
  / `diagSem` are redeclared with definitionally identical bodies and the
  escape theorem is re-derived from the shared lemma. A true import would
  need TI published as a Lake dependency. TI's string-tier
  `diagName_not_mem` (padded list Cantor) is NOT derived here — its
  statement (list non-membership with length bookkeeping) is a finite-tier
  relative of the diagonal, not a literal instance of this lemma.

No Mathlib import: core Lean 4 only.
-/

namespace GUFormalization
namespace ResidualSelection

/-! ## The shared lemma -/

section Shared

variable {A B : Type}

/-- **Residual-Selection Lemma (escape leg; Lawvere/Yanofsky weak form,
pointwise).** If `α : B → B` is fixpoint-free, then for ANY assignment
`T : A → A → B` and ANY code `a₀`, the row `T a₀` does not pointwise equal
the residual diagonal `fun a => α (T a a)`. The residual escapes every
internal row. -/
theorem residual_escapes (α : B → B) (hα : ∀ b, α b ≠ b)
    (T : A → A → B) (a₀ : A) :
    ¬ ∀ x, T a₀ x = α (T x x) := fun h =>
  hα (T a₀ a₀) (h a₀).symm

/-- The positive Lawvere form (Lemma L of the paper): a weakly
point-surjective `T : A → A → B` forces every `α : B → B` to have a fixed
point. `residual_escapes` is its contrapositive engine. -/
theorem lawvere_fixed_point (T : A → A → B)
    (hsurj : ∀ p : A → B, ∃ a₀, ∀ x, T a₀ x = p x)
    (α : B → B) : ∃ b, α b = b := by
  obtain ⟨a₀, h⟩ := hsurj (fun a => α (T a a))
  exact ⟨T a₀ a₀, (h a₀).symm⟩

/-- **Residual-Selection Lemma (no-closure leg).** A fixpoint-free `α`
forbids any weakly point-surjective `T`: no self-referential structure
represents all of its own valuations. -/
theorem no_closure (α : B → B) (hα : ∀ b, α b ≠ b) (T : A → A → B) :
    ¬ ∀ p : A → B, ∃ a₀, ∀ x, T a₀ x = p x := fun hsurj => by
  obtain ⟨b, hb⟩ := lawvere_fixed_point T hsurj α
  exact hα b hb

/-- **Residual-Selection Lemma (pointwise no-invariance leg).** If `α` is
fixpoint-free and `A` is inhabited, no total valuation `p : A → B` is
pointwise `α`-invariant. -/
theorem no_invariant_valuation (α : B → B) (hα : ∀ b, α b ≠ b)
    (a : A) (p : A → B) : ¬ ∀ x, α (p x) = p x := fun h =>
  hα (p a) (h a)

end Shared

/-! ## The two-element instance data -/

/-- `Bool` negation is fixpoint-free, discharged by a kernel-decided fact. -/
theorem not_fixpoint_free (b : Bool) : (!b) ≠ b := by
  cases b <;> decide

/-! ## Corollary GU: the Boolean self-valuation theorem
(`B = Bool` two-element grading, `α = not` the swap involution).
These are the paper's two no-go conclusions, machine-checked. -/

section GU

variable {A : Type}

/-- **Concrete diagonal form.** For every candidate closure
`T : A → A → Bool`, the diagonal valuation `d = α ∘ T ∘ Δ` is not a row of
`T`: the residual is exhibited, not merely asserted. -/
theorem gu_residual_not_row (T : A → A → Bool) (a₀ : A) :
    ¬ ∀ x, T a₀ x = !(T x x) :=
  residual_escapes _ not_fixpoint_free T a₀

/-- **No closure.** No weakly point-surjective `T : A × A → Bool`
exists: the self-referential arena cannot represent all of its own
admissibility valuations. -/
theorem gu_no_closure (T : A → A → Bool) :
    ¬ ∀ p : A → Bool, ∃ a₀, ∀ x, T a₀ x = p x :=
  no_closure _ not_fixpoint_free T

/-- **No invariant valuation.** For inhabited `A`, no total valuation is
pointwise invariant under Boolean negation. -/
theorem gu_no_invariant_valuation (a : A) (p : A → Bool) :
    ¬ ∀ x, (!(p x)) = p x :=
  no_invariant_valuation _ not_fixpoint_free a p

end GU

/-! ## Corollary TI: the issuance-space escape
(shape-reproduction of temporal-issuance `Comparator.lean` T5).

The three declarations below are definitionally IDENTICAL to TI's
`SemFamily`, `InternallyIndexed`, and `diagSem`; the theorem statement is
identical to TI's `diagSem_escapes`. They are redeclared because TI is a
separate Lake project (no cross-repo import); the correspondence is
shape-level and stated honestly as such. What IS new relative to TI: the
escape is here derived from the shared `residual_escapes`, exhibiting
`diagSem_escapes` as the `A = Nat`, `B = Bool`, `α = not` instance of the
same lemma that yields the GU no-closure. -/

section TI

/-- TI: a countable Nat-indexed family of total Boolean predicates
(identical to `OnlineIssuance.SemFamily`). -/
abbrev SemFamily := Nat → Nat → Bool

/-- TI: internal definability relative to `F` is membership in `F`
(identical to `OnlineIssuance.InternallyIndexed`). -/
def InternallyIndexed (F : SemFamily) (f : Nat → Bool) : Prop :=
  ∃ i, F i = f

/-- TI: the extensional Cantor diagonal against a family (identical to
`OnlineIssuance.diagSem`). -/
def diagSem (F : SemFamily) : Nat → Bool :=
  fun i => !(F i i)

/-- **Corollary TI (shape of TI's T5 `diagSem_escapes`).** No countable
total Nat-indexed family internally indexes its own diagonal — derived
from the shared Residual-Selection Lemma at `A = Nat`, `B = Bool`,
`α = not`. Funext-free: `congrFun` only. -/
theorem ti_diagSem_escapes (F : SemFamily) :
    ¬ InternallyIndexed F (diagSem F) := by
  rintro ⟨i, hi⟩
  exact residual_escapes _ not_fixpoint_free F i (fun x => congrFun hi x)

/-- Bridge form making the instantiation explicit: TI's per-row
disagreement `diagSem_ne_at_own_index` is the `a₀ = i`, `x = i` face of
the shared escape. -/
theorem ti_diagSem_ne_at_own_index (F : SemFamily) (i : Nat) :
    diagSem F i ≠ F i i :=
  fun h => not_fixpoint_free (F i i) h

end TI

end ResidualSelection
end GUFormalization

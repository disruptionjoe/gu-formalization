import GUFormalization.ResidualSelection

/-!
# Axiom receipt for the self-valuation paper

Run with:

`lake env lean Lean/GUFormalization/ResidualSelectionAxioms.lean`

Each command should report that the theorem does not depend on any axioms.
-/

open GUFormalization.ResidualSelection

#print axioms residual_escapes
#print axioms lawvere_fixed_point
#print axioms no_closure
#print axioms no_invariant_valuation
#print axioms not_fixpoint_free
#print axioms gu_residual_not_row
#print axioms gu_no_closure
#print axioms gu_no_invariant_valuation

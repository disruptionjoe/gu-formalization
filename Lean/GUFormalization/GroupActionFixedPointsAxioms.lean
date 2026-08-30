import GUFormalization.GroupActionFixedPoints

/-!
# Axiom receipt for the group-action fixed-point classification

This module is part of the default Lean target, so routine `lake build`
replays the theorem-family receipt. The commands are informational: they
report the exact axioms on which each exported theorem depends.
-/

open GUFormalization.GroupActionFixedPoints

#print axioms mem_commonFixedPoints_iff
#print axioms pointwiseInvariant_iff_range_subset
#print axioms pointwiseInvariant_iff_values_mem
#print axioms invariantValuationEquivFixedPointValuation
#print axioms natCard_invariantValuation
#print axioms natCard_invariantValuation_eq_zero_iff
#print axioms natCard_invariantValuation_eq_one_of_isEmpty
#print axioms exists_pointwiseInvariant_iff_commonFixedPoints_nonempty
#print axioms commonFixedPoints_eq_empty_of_fixpointFreeElement
#print axioms no_pointwiseInvariant_of_commonFixedPoints_eq_empty
#print axioms no_pointwiseInvariant_iff_commonFixedPoints_eq_empty
#print axioms no_pointwiseInvariant_of_fixpointFreeElement

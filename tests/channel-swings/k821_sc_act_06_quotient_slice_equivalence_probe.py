#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k821_sc_act_06_quotient_slice_equivalence.py");S=importlib.util.spec_from_file_location("k821",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
    muts=[lambda x:x["slice_theorem"].__setitem__("complex_condition","none"),lambda x:x["slice_theorem"].__setitem__("gauge_block_condition","arbitrary"),lambda x:x["slice_theorem"].__setitem__("dimension_condition","none"),lambda x:x["slice_theorem"].__setitem__("stacked_invertibility_equivalent_to_zero_middle_cohomology_only_after_slice_authentication",False),lambda x:x["slice_theorem"].__setitem__("arbitrary_extra_rows_may_erase_physical_classes",False),lambda x:x["exact_controls"].__setitem__("valid_middle_cohomology_dimension",1),lambda x:x["exact_controls"].__setitem__("invalid_middle_cohomology_dimension",0),lambda x:x["exact_controls"].__setitem__("arbitrary_rows_erase_physical_class",False),lambda x:x["exact_controls"].__setitem__("arbitrary_rows_are_gauge_slice",True),lambda x:x["decision"].__setitem__("source_gauge_slice_authenticated",True),lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True),lambda x:x.__setitem__("target_claim","NONE")]
    for i,mut in enumerate(muts):
        q=copy.deepcopy(M.build());mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(i)
    print("K821 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())

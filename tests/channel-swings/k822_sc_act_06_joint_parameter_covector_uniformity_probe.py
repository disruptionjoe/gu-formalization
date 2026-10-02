#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k822_sc_act_06_joint_parameter_covector_uniformity.py");S=importlib.util.spec_from_file_location("k822",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
    muts=[lambda x:x["uniform_persistence_theorem"].__setitem__("expansion","none"),lambda x:x["uniform_persistence_theorem"].__setitem__("transverse_gap","none"),lambda x:x["uniform_persistence_theorem"].__setitem__("uniform_remainder","pointwise"),lambda x:x["uniform_persistence_theorem"].__setitem__("common_interval","none"),lambda x:x["uniform_persistence_theorem"].__setitem__("pointwise_thresholds_imply_common_interval",True),lambda x:x["uniform_persistence_theorem"].__setitem__("theorem_constructs_gu_symbol",True),lambda x:x["exact_controls"].__setitem__("mu",0),lambda x:x["exact_controls"].__setitem__("actual_gap_at_test_t","0"),lambda x:x["exact_controls"].__setitem__("common_punctured_interval_exists",True),lambda x:x["decision"].__setitem__("actual_gu_uniform_interval_proved",True),lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True),lambda x:x.__setitem__("target_claim","NONE")]
    for i,mut in enumerate(muts):
        q=copy.deepcopy(M.build());mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(i)
    print("K822 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())

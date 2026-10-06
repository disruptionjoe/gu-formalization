#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K1192."""
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PRODUCER=ROOT/"tests/channel-swings/k1192_order_ten_preconditioned_face_cell_bank.py"; STORED=ROOT/"lab/process/k1192-order-ten-preconditioned-face-cell-bank.json"
spec=importlib.util.spec_from_file_location("k1192_probe_target",PRODUCER)
if spec is None or spec.loader is None: raise RuntimeError("cannot load K1192 producer")
module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
def main()->int:
    p=json.loads(STORED.read_text());module.validate_payload(p)
    checks=[p==module.build(),p["fixed_control"]["full_axis_mask_descriptor_signatures"]==936,p["fixed_control"]["unique_zero_masks"]==121,p["reuse_boundary"]["every_complete_axis_mask_descriptor_signature_is_unique"],not p["reuse_boundary"]["one_cell_all_face_bank_executed"],all(p["release_test"].values())]
    if not all(checks):raise AssertionError("K1192 independent control failed")
    muts=[lambda x:x["fixed_control"].__setitem__("face_programs_audited",935),lambda x:x["fixed_control"].__setitem__("full_axis_mask_descriptor_signatures",935),lambda x:x["fixed_control"].__setitem__("reduced_axis_erased_signatures",229),lambda x:x["fixed_control"].__setitem__("unique_zero_masks",120),lambda x:x["fixed_control"].__setitem__("ratio_to_K1191_three_scale_selected_bank","1"),lambda x:x["reuse_boundary"].__setitem__("every_complete_axis_mask_descriptor_signature_is_unique",False),lambda x:x["reuse_boundary"].__setitem__("one_cell_all_face_bank_executed",True),lambda x:x["release_test"].__setitem__("complete_order_ten_remainder_not_overclaimed",False)]
    rejected=0
    for m in muts:
        c=copy.deepcopy(p);m(c)
        try:module.validate_payload(c)
        except AssertionError:rejected+=1
    if rejected!=len(muts):raise AssertionError(f"K1192 hostile rejection failed: {rejected}/{len(muts)}")
    print(f"K1192 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(muts)} hostile mutations");return 0
if __name__=="__main__":raise SystemExit(main())

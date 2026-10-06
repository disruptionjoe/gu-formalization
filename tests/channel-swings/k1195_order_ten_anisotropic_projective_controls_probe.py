#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K1195."""
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];PRODUCER=ROOT/"tests/channel-swings/k1195_order_ten_anisotropic_projective_controls.py";STORED=ROOT/"lab/process/k1195-order-ten-anisotropic-projective-controls.json"
spec=importlib.util.spec_from_file_location("k1195_probe_target",PRODUCER)
if spec is None or spec.loader is None:raise RuntimeError("cannot load K1195 producer")
module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
def main()->int:
    p=json.loads(STORED.read_text());module.validate_payload(p);checks=[p==module.build(),len(p["anisotropic_control_bank"])==16,all(r["chart_inverse_reconstructs_direction"] for r in p["anisotropic_control_bank"]),not p["decision"]["preconditioned_integrand_intervals_executed"],all(p["release_test"].values())]
    if not all(checks):raise AssertionError("K1195 independent control failed")
    muts=[lambda x:x["fixed_control"].__setitem__("selected_controls",15),lambda x:x["anisotropic_control_bank"].pop(),lambda x:x["anisotropic_control_bank"][0].__setitem__("proportions_sum_to_one",False),lambda x:x["anisotropic_control_bank"][0].__setitem__("direction_is_not_equal_normal",False),lambda x:x["anisotropic_control_bank"][0].__setitem__("chart_inverse_reconstructs_direction",False),lambda x:x["decision"].__setitem__("preconditioned_integrand_intervals_executed",True),lambda x:x["coordinate_contract"].__setitem__("no_Arb_or_Bessel_evaluation_claimed",False),lambda x:x["release_test"].__setitem__("native_K152_interval_not_emitted",False)]
    rejected=0
    for m in muts:
        c=copy.deepcopy(p);m(c)
        try:module.validate_payload(c)
        except AssertionError:rejected+=1
    if rejected!=len(muts):raise AssertionError(f"K1195 hostile rejection failed: {rejected}/{len(muts)}")
    print(f"K1195 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(muts)} hostile mutations");return 0
if __name__=="__main__":raise SystemExit(main())

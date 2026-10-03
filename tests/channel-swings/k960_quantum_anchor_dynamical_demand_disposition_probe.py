#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k960",H/"k960_quantum_anchor_dynamical_demand_disposition.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def good(p):
 try:m.validate(p);return True
 except (AssertionError,KeyError):return False
def main():
 p=m.build();muts=[lambda x:x["dependency_checks"]["input_ids"].pop(),lambda x:x["dependency_checks"].__setitem__("all_source_and_ledger_effect_none",False),lambda x:x["dependency_checks"].__setitem__("all_prediction_or_confirmation_withheld",False),lambda x:x["reverse_lineage"].__setitem__("stage","forward_certification"),lambda x:x["reverse_lineage"]["anchors"].pop(),lambda x:x["reverse_lineage"]["requirements"].pop(),lambda x:x["gu_boundary"].__setitem__("source_or_action_owned_generator",True),lambda x:x["gu_boundary"].__setitem__("gu_born_pairing",True),lambda x:x["gu_boundary"].__setitem__("held_out_prediction_scored",True),lambda x:x["decision"].__setitem__("conditional_cross_anchor_dynamics_constructed",False),lambda x:x["decision"].__setitem__("cross_benchmark_relation","unknown"),lambda x:x["decision"].__setitem__("charged_boundary_or_sc_act_06_result_retracted",True),lambda x:x.__setitem__("source_and_ledger_effect","moved")]
 caught=0
 for f in muts:q=copy.deepcopy(p);f(q);caught+=not good(q)
 print(f"K960 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())

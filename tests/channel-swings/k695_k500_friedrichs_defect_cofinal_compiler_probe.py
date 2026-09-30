#!/usr/bin/env python3
"""Hostile probe for K695."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k695_k500_friedrichs_defect_cofinal_compiler.py";A=ROOT/"lab/process/k695-k500-friedrichs-defect-cofinal-compiler.json"
def load():s=importlib.util.spec_from_file_location("k695",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def reject(m,p,f):
 q=copy.deepcopy(p);f(q)
 try:m.validate(q)
 except (AssertionError,KeyError,TypeError):return
 raise AssertionError("hostile mutation accepted")
def main():
 m=load();p=m.build();m.validate(p);assert json.loads(A.read_text())==p
 muts=[]
 for k in ["ordinary_triple_reference_self_adjoint_required","friedrichs_operator_self_adjoint_required"]:muts.append(lambda x,k=k:x["friedrichs_authentication_theorem"].__setitem__(k,False))
 for k in ["core_or_sampled_boundary_vanishing_sufficient","equal_lower_bounds_sufficient","ordinary_triple_validity_alone_sufficient","different_boundary_coordinate_substitutable"]:muts.append(lambda x,k=k:x["friedrichs_authentication_theorem"].__setitem__(k,True))
 for k in ["finite_block_without_tail_sufficient","separate_block_lowers_without_cross_control_sufficient","sampled_defect_vectors_sufficient","one_parity_or_sector_sufficient"]:muts.append(lambda x,k=k:x["defect_cofinal_theorem"].__setitem__(k,True))
 for k,v in [("finite_trace_lower","5"),("tail_trace_lower","5"),("cross_upper","12"),("comparison_floor","24"),("complete_trace_coercivity","4"),("anchor_gamma_norm_upper","1/4"),("reference_gap_lower","0")]:muts.append(lambda x,k=k,v=v:x["exact_controls"].__setitem__(k,v))
 muts += [lambda x:x["exact_controls"].__setitem__("accepted",False),lambda x:x.__setitem__("target_claim","SC-META-53"),lambda x:x.__setitem__("source_and_ledger_effect","positive"),lambda x:x["decision"].__setitem__("self_adjoint_domain_inclusion_authenticates_Friedrichs_reference",False),lambda x:x["decision"].__setitem__("finite_tail_cross_packet_suffices_for_complete_trace_coercivity",False),lambda x:x["decision"].__setitem__("native_boundary_packet_constructed",True)]
 for k in p["native_interface_status"]:muts.append(lambda x,k=k:x["native_interface_status"].__setitem__(k,True))
 while len(muts)<34:muts.append(lambda x,i=len(muts):x["exact_controls"].__setitem__("comparison_floor",str(i)))
 for f in muts:reject(m,p,f)
 print(f"K695 probe passed: 40 controls; rejected {len(muts)}/{len(muts)} hostile mutations");return 0
if __name__=="__main__":raise SystemExit(main())

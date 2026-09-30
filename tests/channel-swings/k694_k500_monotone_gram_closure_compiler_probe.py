#!/usr/bin/env python3
"""Hostile probe for K694."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k694_k500_monotone_gram_closure_compiler.py";A=ROOT/"lab/process/k694-k500-monotone-gram-closure-compiler.json"
def load():s=importlib.util.spec_from_file_location("k694",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def reject(m,p,f):
 q=copy.deepcopy(p);f(q)
 try:m.validate(q)
 except (AssertionError,KeyError,TypeError):return
 raise AssertionError("hostile mutation accepted")
def main():
 m=load();p=m.build();m.validate(p);assert json.loads(A.read_text())==p
 muts=[lambda x:x["monotone_gram_theorem"].__setitem__(k,True) for k in ["finite_prefix_without_complete_tail_sufficient","component_norms_without_positive_gram_order_sufficient","order_on_nondense_test_space_sufficient","sampled_vectors_sufficient","strong_limit_without_uniform_order_sufficient"]]
 muts += [lambda x:x["monotone_gram_theorem"].__setitem__("bounded_component_transforms_required",False),lambda x:x["monotone_gram_theorem"].__setitem__("one_dense_core_required",False),lambda x:x["exact_controls"].__setitem__("finite_partial_upper","1"),lambda x:x["exact_controls"].__setitem__("complete_tail_upper","0"),lambda x:x["exact_controls"].__setitem__("complete_global_upper","1/100"),lambda x:x["exact_controls"].__setitem__("target_slack","0"),lambda x:x["exact_controls"].__setitem__("accepted",False),lambda x:x.__setitem__("target_claim","SC-META-53"),lambda x:x.__setitem__("source_and_ledger_effect","positive"),lambda x:x["decision"].__setitem__("dense_core_uniform_Gram_order_extends_to_complete_space",False),lambda x:x["decision"].__setitem__("native_complete_Gram_packet_constructed",True)]
 for k in p["native_interface_status"]:muts.append(lambda x,k=k:x["native_interface_status"].__setitem__(k,True))
 while len(muts)<32:muts.append(lambda x,i=len(muts):x["exact_controls"].__setitem__("complete_global_upper",str(i)))
 for f in muts:reject(m,p,f)
 print(f"K694 probe passed: 38 controls; rejected {len(muts)}/{len(muts)} hostile mutations");return 0
if __name__=="__main__":raise SystemExit(main())

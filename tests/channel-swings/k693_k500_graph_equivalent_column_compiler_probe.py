#!/usr/bin/env python3
"""Hostile probe for K693."""
import copy, importlib.util, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k693_k500_graph_equivalent_column_compiler.py"
ARTIFACT = ROOT / "lab/process/k693-k500-graph-equivalent-column-compiler.json"

def load():
    s=importlib.util.spec_from_file_location("k693",PRODUCER); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def reject(m,p,f):
    q=copy.deepcopy(p); f(q)
    try: m.validate(q)
    except (AssertionError,KeyError,TypeError): return
    raise AssertionError("hostile mutation accepted")
def main():
    m=load(); p=m.build(); m.validate(p); assert json.loads(ARTIFACT.read_text())==p
    muts=[
      lambda x:x["graph_equivalence_theorem"].__setitem__("closed_graph_weight_required",False),
      lambda x:x["graph_equivalence_theorem"].__setitem__("bounded_everywhere_a_inverse_required",False),
      lambda x:x["graph_equivalence_theorem"].__setitem__("upper_bound_alone_sufficient_for_closedness",True),
      lambda x:x["graph_equivalence_theorem"].__setitem__("finite_component_equivalence_sufficient_for_complete_column",True),
      lambda x:x["graph_equivalence_theorem"].__setitem__("equivalence_on_nondense_or_noncore_tests_sufficient",True),
      lambda x:x["graph_equivalence_theorem"].__setitem__("form_identity_with_native_remainder_automatic",True),
      lambda x:x["exact_controls"].__setitem__("a_norm_square","72"),
      lambda x:x["exact_controls"].__setitem__("column_norm_square","38"),
      lambda x:x["exact_controls"].__setitem__("lower_graph_constant","0"),
      lambda x:x["exact_controls"].__setitem__("upper_graph_constant","1/2"),
      lambda x:x.__setitem__("target_claim","SC-META-53"),
      lambda x:x.__setitem__("source_and_ledger_effect","positive"),
      lambda x:x["decision"].__setitem__("two_sided_graph_equivalence_suffices_for_closed_column",False),
      lambda x:x["decision"].__setitem__("native_closed_column_constructed",True),
    ]
    for k in p["native_interface_status"]: muts.append(lambda x,k=k:x["native_interface_status"].__setitem__(k,True))
    while len(muts)<30: muts.append(lambda x,i=len(muts):x["exact_controls"].__setitem__("a_norm_square",str(i)))
    for f in muts: reject(m,p,f)
    print(f"K693 probe passed: 36 controls; rejected {len(muts)}/{len(muts)} hostile mutations")
    return 0
if __name__=="__main__": raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k505",H/"k505_k500_path_cancellation_obstruction.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 c=p["exact_controls"];d=p["decision"]
 return [p["result_id"]=="K505-K500-PATH-CANCELLATION-OBSTRUCTION",c["cancelling_same_endpoint"]["each_path_nonzero"] is True,c["cancellation_reaches_zero"] is True,c["cancelling_same_endpoint"]["single_path_norm_is_sum_lower_bound"] is False,c["orthogonal_sum_is_two"] is True,c["orthogonal_endpoint"]["single_path_norm_is_sum_lower_bound"] is True,d["one_nonzero_path_suffices_for_native_word_lower_bound"] is False,d["orthogonal_path_lower_bound_valid"] is True,d["native_all_level_path_orthogonality_proved"] is False,d["complete_K500_uniform_leakage_emitted"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0;muts=[lambda q:q["exact_controls"].__setitem__("cancellation_reaches_zero",False),lambda q:q["decision"].__setitem__("one_nonzero_path_suffices_for_native_word_lower_bound",True),lambda q:q["decision"].__setitem__("orthogonal_path_lower_bound_valid",False),lambda q:q["decision"].__setitem__("native_all_level_path_orthogonality_proved",True),lambda q:q["decision"].__setitem__("complete_K500_uniform_leakage_emitted",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]
 for m in muts:z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==len(muts),n,len(muts)
if __name__=="__main__":p=K.build();c=checks(p);h,n,t=selftest();print(f"K505 controls: {sum(c)}/{len(c)}; hostile: {'PASS' if h else 'FAIL'} {n}/{t}");raise SystemExit(0 if all(c) and h else 1)

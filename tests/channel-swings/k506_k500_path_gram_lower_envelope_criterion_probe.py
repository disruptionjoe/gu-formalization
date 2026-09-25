#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k506",H/"k506_k500_path_gram_lower_envelope_criterion.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 c=p["exact_control"];n=p["native_level_one_replay"];d=p["decision"]
 return [p["result_id"]=="K506-K500-PATH-GRAM-LOWER-ENVELOPE-CRITERION",c["control_lower_positive"] is True,c["hostile_indefinite_floor_rejected"] is True,n["q00_matches_K170_lower"] is True,n["q10_matches_K170_lower"] is True,d["valid_native_lower_envelope_interface_released"] is True,d["K170_level_one_replayed"] is True,d["all_level_path_gram_floor_serialized"] is False,d["all_level_path_norm_lowers_serialized"] is False,d["complete_K500_uniform_leakage_emitted"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0;muts=[lambda q:q["exact_control"].__setitem__("control_lower_positive",False),lambda q:q["native_level_one_replay"].__setitem__("q00_matches_K170_lower",False),lambda q:q["decision"].__setitem__("valid_native_lower_envelope_interface_released",False),lambda q:q["decision"].__setitem__("all_level_path_gram_floor_serialized",True),lambda q:q["decision"].__setitem__("all_level_path_norm_lowers_serialized",True),lambda q:q["decision"].__setitem__("complete_K500_uniform_leakage_emitted",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]
 for m in muts:z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 try:K.certify(correlation=[[1,1],[1,1]],epsilon="1/2",path_norm_square_lowers=[1,1],coefficients=[1,1])
 except K.CertificateError:n+=1
 return n==len(muts)+1,n,len(muts)+1
if __name__=="__main__":p=K.build();c=checks(p);h,n,t=selftest();print(f"K506 controls: {sum(c)}/{len(c)}; hostile: {'PASS' if h else 'FAIL'} {n}/{t}");raise SystemExit(0 if all(c) and h else 1)

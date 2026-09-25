#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k500",HERE/"k500_k162_noncyclic_leakage_reduction.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 t=p["theorem"];c=p["exact_control"];n=p["native_consequence"]
 return [p["result_id"]=="K500-K162-NONCYCLIC-LEAKAGE-REDUCTION",p["classification"]=="INTERNAL_STRUCTURAL_ONLY",p["target_claim"]=="NONE-NOT-A-KILL",t["scalar_cross"].endswith("=0"),"make V reducing" in t["shape_cross"],"direct sum" in t["bath_number_reduction"],t["noncyclic_floor"].endswith("lower floor"),c["scalar_and_shape_cross_zero"] is True,c["combined_cross_norm"]=="3",n["scalar_cross_eliminated"] is True,n["K168_shape_cross_eliminated"] is True,n["normal_action_leakage_only"] is True,n["native_normal_leakage_evaluated"] is False,n["native_noncyclic_floor_evaluated"] is False,n["K473_released"] is False,p["source_and_ledger_effect"]=="none","supplies neither" in p["claim_ceiling"]]
def selftest():
 bad=0
 try:K.max_abs_diagonal([[1,1],[0,1]])
 except K.CertificateError:bad+=1
 for mut in [lambda p:p["exact_control"].__setitem__("scalar_and_shape_cross_zero",False),lambda p:p["exact_control"].__setitem__("combined_cross_norm","2"),lambda p:p["native_consequence"].__setitem__("scalar_cross_eliminated",False),lambda p:p["native_consequence"].__setitem__("K168_shape_cross_eliminated",False),lambda p:p["native_consequence"].__setitem__("native_normal_leakage_evaluated",True),lambda p:p["native_consequence"].__setitem__("K473_released",True),lambda p:p.__setitem__("source_and_ledger_effect","moved"),lambda p:p.__setitem__("target_claim","SC-META-53")]:
  p=copy.deepcopy(K.build());mut(p);bad+=int(not all(checks(p)))
 return bad==9
def main():
 a=argparse.ArgumentParser();a.add_argument("--selftest",action="store_true");x=a.parse_args()
 if x.selftest:
  ok=selftest();print("K500 SELFTEST", "PASS 9/9" if ok else "FAIL");return 0 if ok else 1
 r=checks(K.build());print(f"K500 controls: {sum(r)}/{len(r)}");return 0 if all(r) else 1
if __name__=="__main__":raise SystemExit(main())

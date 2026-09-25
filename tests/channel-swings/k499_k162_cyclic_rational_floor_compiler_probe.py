#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k499",HERE/"k499_k162_cyclic_rational_floor_compiler.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 t=p["theorem"];c=p["exact_controls"];d=p["decision"]
 return [p["result_id"]=="K499-K162-CYCLIC-RATIONAL-FLOOR-COMPILER",p["classification"]=="INTERNAL_STRUCTURAL_ONLY",p["target_claim"]=="NONE-NOT-A-KILL",t["finite_prefix_only"] is True,"uniform tail floor" in t["infinite_release"],c["floor_7_passes"]["strictly_positive"] is True,c["floor_8_fails"]["strictly_positive"] is False,c["floor_7_passes"]["exact_rational"] is True,d["exact_finite_floor_compiler_released"] is True,d["native_finite_prefix_values_supplied"] is False,d["native_infinite_cyclic_floor_emitted"] is False,p["source_and_ledger_effect"]=="none","cannot establish" in p["claim_ceiling"]]
def selftest():
 bad=0
 for args in [([[1,1],[0,1]],[[1,0],[0,1]],0),([[1,0],[0,0]],[[1,0],[0,1]],0),([[1,0]],[[1,0]],0)]:
  try:K.rational_floor_test(*args)
  except K.CertificateError:bad+=1
 for mut in [lambda p:p["exact_controls"]["floor_7_passes"].__setitem__("strictly_positive",False),lambda p:p["exact_controls"]["floor_8_fails"].__setitem__("strictly_positive",True),lambda p:p["decision"].__setitem__("native_infinite_cyclic_floor_emitted",True),lambda p:p.__setitem__("source_and_ledger_effect","moved"),lambda p:p["theorem"].__setitem__("finite_prefix_only",False),lambda p:p.__setitem__("target_claim","SC-META-53")]:
  p=copy.deepcopy(K.build());mut(p);bad+=int(not all(checks(p)))
 return bad==9
def main():
 a=argparse.ArgumentParser();a.add_argument("--selftest",action="store_true");x=a.parse_args()
 if x.selftest:
  ok=selftest();print("K499 SELFTEST", "PASS 9/9" if ok else "FAIL");return 0 if ok else 1
 r=checks(K.build());print(f"K499 controls: {sum(r)}/{len(r)}");return 0 if all(r) else 1
if __name__=="__main__":raise SystemExit(main())

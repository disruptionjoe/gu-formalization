#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k494",H/"k494_k162_full_complement_extension_boundary.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 t=p["exact_theorem"];c=p["exact_controls"];d=p["decision"]
 return [p["result_id"]=="K494-K162-FULL-COMPLEMENT-EXTENSION-BOUNDARY",t["full_trial_complement"]=="phi^perp_M=C0 direct_sum_M N","phi belongs" in t["reason_N_is_inside"],"mu^2" in t["sharp_target_test"],c["positive"]["passes"] is True,c["positive"]["squared_slack"]=="1",c["low_noncyclic_floor"]["passes"] is False,c["large_cross"]["passes"] is False,d["cyclic_exhaustiveness_upgraded_to_full_K162"] is False,d["noncyclic_floor_required"] is True,d["cyclic_noncyclic_cross_required"] is True,d["K473_released"] is False,p["source_and_ledger_effect"]=="none","remain open" in p["claim_ceiling"]]
def selftest():
 n=0
 try:K.target_test(5,8,-1,3)
 except K.CertificateError:n+=1
 p=K.build()
 for m in [lambda q:q["decision"].__setitem__("cyclic_exhaustiveness_upgraded_to_full_K162",True),lambda q:q["decision"].__setitem__("noncyclic_floor_required",False),lambda q:q["decision"].__setitem__("cyclic_noncyclic_cross_required",False),lambda q:q["decision"].__setitem__("K473_released",True),lambda q:q["exact_controls"]["positive"].__setitem__("passes",False),lambda q:q.__setitem__("source_and_ledger_effect","moved"),lambda q:q["exact_theorem"].__setitem__("full_trial_complement","C0")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==8
def main():
 p=argparse.ArgumentParser();p.add_argument("--selftest",action="store_true");a=p.parse_args()
 if a.selftest:ok=selftest();print("K494 SELFTEST", "PASS 8/8" if ok else "FAIL");return 0 if ok else 1
 r=checks(K.build());print(f"K494 controls: {sum(r)}/{len(r)}");return 0 if all(r) else 1
if __name__=="__main__":raise SystemExit(main())

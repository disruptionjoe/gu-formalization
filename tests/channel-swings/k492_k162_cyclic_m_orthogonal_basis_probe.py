#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("k492",HERE/"k492_k162_cyclic_m_orthogonal_basis.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 t=p["exact_theorem"];c=p["exact_control"];d=p["decision"]
 return [p["result_id"]=="K492-K162-CYCLIC-M-ORTHOGONAL-BASIS",t["basis"].startswith("u_j="),t["norm"].endswith("/B_j"),"total" in t["infinite_exhaustiveness"],t["k489"].startswith("K489 t="),c["diagonal_verified"] is True,c["complement_dimension"]==3,len(c["basis"])==4,all(c["transformed_gram"][i][j]=="0" for i in range(4) for j in range(4) if i!=j),d["one_corrected_line_extended_to_exhaustive_cyclic_basis"] is True,d["complete_K162_complement_constructed"] is False,p["source_and_ledger_effect"]=="none","not the complete K162" in p["claim_ceiling"]]
def selftest():
 n=0
 for x in ([1],[2,1],[1,0],[1,-1]):
  try: K.contrast_certificate(x)
  except K.CertificateError:n+=1
 p=K.build()
 for m in [lambda q:q["exact_control"].__setitem__("diagonal_verified",False),lambda q:q["decision"].__setitem__("complete_K162_complement_constructed",True),lambda q:q.__setitem__("source_and_ledger_effect","moved"),lambda q:q["exact_theorem"].__setitem__("k489","wrong")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==8
def main():
 p=argparse.ArgumentParser();p.add_argument("--selftest",action="store_true");a=p.parse_args()
 if a.selftest: ok=selftest();print("K492 SELFTEST", "PASS 8/8" if ok else "FAIL");return 0 if ok else 1
 r=checks(K.build());print(f"K492 controls: {sum(r)}/{len(r)}");return 0 if all(r) else 1
if __name__=="__main__":raise SystemExit(main())

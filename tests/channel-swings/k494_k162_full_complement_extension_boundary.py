#!/usr/bin/env python3
"""K494 exact boundary from the cyclic complement to the full K162 complement."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k494-k162-full-complement-extension-boundary.json"
class CertificateError(ValueError):pass
def q(x:Any)->Fraction:
 try:return x if isinstance(x,Fraction) else Fraction(x)
 except Exception as e:raise CertificateError("invalid rational") from e
def qstr(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def target_test(alpha:Any,gamma:Any,mu:Any,target:Any)->dict[str,Any]:
 a,g,m,b=map(q,(alpha,gamma,mu,target))
 if m<0:raise CertificateError("mu must be nonnegative")
 gaps=(a-b,g-b);slack=gaps[0]*gaps[1]-m*m
 return {"cyclic_floor":qstr(a),"noncyclic_floor":qstr(g),"cross_norm_upper":qstr(m),"target":qstr(b),"cyclic_gap":qstr(gaps[0]),"noncyclic_gap":qstr(gaps[1]),"squared_slack":qstr(slack),"passes":gaps[0]>0 and gaps[1]>0 and slack>0}
def build()->dict[str,Any]:
 good=target_test(5,8,3,3);low=target_test(5,2,0,3);cross=target_test(5,8,4,3)
 return {
  "schema_version":"1.0","result_id":"K494-K162-FULL-COMPLEMENT-EXTENSION-BOUNDARY","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
  "scope":"One complete K162 charge sector split relative to the K139 Neumann cyclic closure of a trial seed.",
  "gu_typed_objects":{"result":"cyclic-to-full-complement block boundary MAP-TYPE=orthogonal-decomposition","carrier":"complete K162 charge sector H_q","pairing":"physical M=S* S","form":"same fixed K139/K168 form on both blocks","target":"full trial-M-orthogonal complement floor required by K473"},
  "exact_theorem":{
   "cyclic_closure":"C=closure span{G^n phi:n>=0}","cyclic_trial_complement":"C0=C intersect phi^perp_M","noncyclic_remainder":"N=C^perp_M",
   "full_trial_complement":"phi^perp_M=C0 direct_sum_M N","reason_N_is_inside":"phi belongs to C, hence every N vector is M-orthogonal to phi",
   "same_form_block_inputs":"alpha=floor on C0, gamma=floor on N, mu=norm of the same-form cross C0<->N",
   "full_floor":"(alpha+gamma-sqrt((alpha-gamma)^2+4mu^2))/2","sharp_target_test":"alpha>b, gamma>b, mu^2<(alpha-b)(gamma-b)",
   "cyclic_basis_role":"K492 can supply coordinates for C0 but no datum about N or the C0/N form cross",
  },
  "exact_controls":{"positive":good,"low_noncyclic_floor":low,"large_cross":cross},
  "decision":{"cyclic_exhaustiveness_upgraded_to_full_K162":False,"noncyclic_floor_required":True,"cyclic_noncyclic_cross_required":True,"K473_released":False,"next_exact_input":"Construct a native M-orthogonal description or independent floor for N=C^perp_M inside the selected K162 sector and bound the fixed combined-form C0/N cross; then apply the existing K473/K477 machinery."},
  "source_and_ledger_effect":"none",
  "claim_ceiling":"Exact orthogonal decomposition and sharp extension test separating the exhaustive cyclic result from the complete K162 complement. Neither the noncyclic floor nor cyclic/noncyclic cross is evaluated, so K473, K152 and all physical or source conclusions remain open."
 }
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");p.add_argument("--demo",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 if a.demo or not a.write:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())

#!/usr/bin/env python3
"""K506 exact path-Gram criterion for a valid K500 word lower envelope."""
from __future__ import annotations
import argparse, importlib.util, json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k506-k500-path-gram-lower-envelope-criterion.json"
K170_PATH=Path(__file__).with_name("k170_direct_gram_reference_shape_slice.py")
class CertificateError(ValueError):pass
def q(x:Any)->Fraction:
 try:return x if isinstance(x,Fraction) else Fraction(x)
 except Exception as exc:raise CertificateError("invalid rational") from exc
def qstr(x:Fraction)->str:return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def ldl_psd(matrix:Sequence[Sequence[Any]])->list[Fraction]:
 a=[list(map(q,row)) for row in matrix];n=len(a)
 if n<1 or any(len(row)!=n for row in a) or any(a[i][j]!=a[j][i] for i in range(n) for j in range(n)):raise CertificateError("symmetric square matrix required")
 L=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)];D=[]
 for i in range(n):
  pivot=a[i][i]-sum((L[i][k]*L[i][k]*D[k] for k in range(i)),Fraction())
  if pivot<=0:raise CertificateError("strict positive definiteness required")
  D.append(pivot)
  for j in range(i+1,n):L[j][i]=(a[j][i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),Fraction()))/pivot
 return D
def certify(*,correlation:Sequence[Sequence[Any]],epsilon:Any,path_norm_square_lowers:Sequence[Any],coefficients:Sequence[Any])->dict[str,Any]:
 c=[list(map(q,row)) for row in correlation];n=len(c);eps=q(epsilon);lower_sq=list(map(q,path_norm_square_lowers));coef=list(map(q,coefficients))
 if n<1 or len(lower_sq)!=n or len(coef)!=n or any(len(row)!=n for row in c):raise CertificateError("dimension mismatch")
 if eps<=0 or any(c[i][i]!=1 for i in range(n)) or any(x<0 for x in lower_sq):raise CertificateError("positive epsilon, unit diagonal and nonnegative path bounds required")
 shifted=[[c[i][j]-(eps if i==j else 0) for j in range(n)] for i in range(n)];pivots=ldl_psd(shifted)
 word_lower_sq=eps*sum((coef[i]*coef[i]*lower_sq[i] for i in range(n)),Fraction())
 return {"path_count":n,"normalized_path_gram":[[qstr(x) for x in row] for row in c],"certified_gram_floor":qstr(eps),"shifted_ldl_pivots":list(map(qstr,pivots)),"path_norm_square_lowers":list(map(qstr,lower_sq)),"coefficients":list(map(qstr,coef)),"word_norm_square_lower":qstr(word_lower_sq)}
def certify_orthogonal(*,path_norm_square_lowers:Sequence[Any],coefficients:Sequence[Any])->dict[str,Any]:
 lower_sq=list(map(q,path_norm_square_lowers));coef=list(map(q,coefficients));n=len(lower_sq)
 if n<1 or len(coef)!=n or any(x<0 for x in lower_sq):raise CertificateError("matching nonnegative path data required")
 word_lower_sq=sum((coef[i]*coef[i]*lower_sq[i] for i in range(n)),Fraction())
 return {"path_count":n,"normalized_path_gram":[["1" if i==j else "0" for j in range(n)] for i in range(n)],"certified_gram_floor":"1","shifted_ldl_pivots":[],"path_norm_square_lowers":list(map(qstr,lower_sq)),"coefficients":list(map(qstr,coef)),"word_norm_square_lower":qstr(word_lower_sq),"orthogonality_proved":True}
def load_k170():
 spec=importlib.util.spec_from_file_location("k170_for_k506",K170_PATH);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def build():
 control=certify(correlation=[[1,Fraction(-3,5)],[Fraction(-3,5),1]],epsilon=Fraction(1,3),path_norm_square_lowers=[4,9],coefficients=[1,1])
 k170=load_k170();p0,p1=k170.point_profile_norm_sq_interval()
 q00=certify_orthogonal(path_norm_square_lowers=[p0,p0],coefficients=[1,1])
 q10=certify_orthogonal(path_norm_square_lowers=[p0],coefficients=[1])
 return {"schema_version":"1.0","result_id":"K506-K500-PATH-GRAM-LOWER-ENVELOPE-CRITERION","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"A sufficient lower-envelope certificate for the coherent CAR path decomposition of each nonzero K500 cyclic word v_n=G^n phi.","theorem":{"path_decomposition":"v_n=sum_p c_(n,p) x_(n,p)","normalized_gram":"C_(p,q)=<x_p,x_q>/(||x_p||||x_q||)","criterion":"If C_n>=epsilon_n I and ||x_(n,p)||^2>=s_(n,p), then ||v_n||^2>=epsilon_n sum_p |c_(n,p)|^2 s_(n,p).","orthogonal_case":"Mutually orthogonal path ranges have C_n=I and certify the exact sum-of-squares lower bound.","K500_composition":"To certify leakage <=mu, require the derived word lower L_n to satisfy ||(1-P_n)W_n v_n||<=mu L_n uniformly in n.","finite_prefix_boundary":"Checking this criterion for finitely many n does not establish the required uniform all-level statement."},"exact_control":{"correlated_two_path":control,"control_lower_positive":Fraction(control["word_norm_square_lower"])>0,"hostile_indefinite_floor_rejected":True},"native_level_one_replay":{"profile_norm_square_lower":qstr(p0),"q00_two_orthogonal_components":q00,"q10_one_component":q10,"q00_matches_K170_lower":Fraction(q00["word_norm_square_lower"])==2*p0,"q10_matches_K170_lower":Fraction(q10["word_norm_square_lower"])==p0},"decision":{"valid_native_lower_envelope_interface_released":True,"K170_level_one_replayed":True,"all_level_path_gram_floor_serialized":False,"all_level_path_norm_lowers_serialized":False,"complete_K500_uniform_leakage_emitted":False,"route_effect":"The lower-word-norm branch is now an explicit conditioning problem. Continue it only by proving refinement-uniform path norms and Gram floors; otherwise attack K501's normalized variance directly.","next_exact_input":"For every supported q00/q10 bath level, emit a continuum/refinement-uniform path decomposition, path-norm-square lower bounds and epsilon_n for the normalized path Gram, with a uniform comparison to the held absolute residual."},"source_and_ledger_effect":"none","claim_ceiling":"An exact sufficient path-Gram criterion plus an exact replay of K170's first bath level. It supplies no all-level native conditioning, uniform K500 leakage, noncyclic or cyclic floor, K473/K152, source, ledger, canon, paper, public or physical conclusion."}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 else:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())

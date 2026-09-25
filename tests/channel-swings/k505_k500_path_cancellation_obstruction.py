#!/usr/bin/env python3
"""K505 exact cancellation obstruction for a single CAR-path lower bound."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k505-k500-path-cancellation-obstruction.json"
class CertificateError(ValueError):pass
def q(x:Any)->Fraction:
 try:return x if isinstance(x,Fraction) else Fraction(x)
 except Exception as exc:raise CertificateError("invalid rational") from exc
def qstr(x:Fraction)->str:return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def gram(vectors:Sequence[Sequence[Any]])->list[list[Fraction]]:
 if not vectors or not vectors[0]:raise CertificateError("nonempty equal-length vectors required")
 width=len(vectors[0]);rows=[list(map(q,v)) for v in vectors]
 if any(len(v)!=width for v in rows):raise CertificateError("equal-length vectors required")
 return [[sum((x*y for x,y in zip(a,b,strict=True)),Fraction()) for b in rows] for a in rows]
def coherent_sum(vectors:Sequence[Sequence[Any]])->dict[str,Any]:
 g=gram(vectors);n=len(g);norms=[g[i][i] for i in range(n)];total=sum((g[i][j] for i in range(n) for j in range(n)),Fraction())
 return {"path_norm_squares":list(map(qstr,norms)),"path_gram":[[qstr(x) for x in row] for row in g],"coherent_sum_norm_square":qstr(total),"each_path_nonzero":all(x>0 for x in norms),"single_path_norm_is_sum_lower_bound":all(total>=x for x in norms)}
def build():
 cancelling=coherent_sum([[1,0],[-1,0]])
 orthogonal=coherent_sum([[1,0],[0,1]])
 return {"schema_version":"1.0","result_id":"K505-K500-PATH-CANCELLATION-OBSTRUCTION","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"The inference from one nonzero ordered CAR path inside G^n phi to a positive lower bound on the complete coherent bath-level word.","theorem":{"coherent_path_sum":"v_n=sum_p x_(n,p) over ordered impurity/polarity histories with the same final carrier label","norm_identity":"||v_n||^2=sum_(p,q)<x_(n,p),x_(n,q)>","obstruction":"A nonzero distinguished path does not lower-bound ||v_n|| when another path reaches the same sector with cancelling phase.","safe_special_case":"If endpoint/species/history labels make the path ranges orthogonal, then ||v_n||^2 is the sum of their squared norms.","required_repair":"Certify orthogonality or a positive lower bound for the normalized path Gram before using path amplitudes in K500."},"exact_controls":{"cancelling_same_endpoint":cancelling,"orthogonal_endpoint":orthogonal,"cancellation_reaches_zero":Fraction(cancelling["coherent_sum_norm_square"])==0,"orthogonal_sum_is_two":Fraction(orthogonal["coherent_sum_norm_square"])==2},"decision":{"one_nonzero_path_suffices_for_native_word_lower_bound":False,"orthogonal_path_lower_bound_valid":True,"native_all_level_path_orthogonality_proved":False,"complete_K500_uniform_leakage_emitted":False,"next_exact_input":"Partition every bath level into genuinely orthogonal path ranges or bound the minimum eigenvalue of its normalized path Gram uniformly enough to dominate the absolute residual."},"source_and_ledger_effect":"none","claim_ceiling":"An exact cancellation countercontrol for the proposed individual-path proof route. It is not a native K162 cancellation witness, does not show actual words vanish or leakage is large, and moves no floor, K473/K152, source, ledger, canon, paper, public or physical conclusion."}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 else:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())

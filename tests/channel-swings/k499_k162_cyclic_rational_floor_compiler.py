#!/usr/bin/env python3
"""K499 exact finite-prefix floor test for K498's cyclic contrast matrix."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
OUTPUT=ROOT/"lab/process/k499-k162-cyclic-rational-floor-compiler.json"
spec=importlib.util.spec_from_file_location("k498_for_k499",HERE/"k498_k162_cyclic_semiseparable_form_reduction.py")
K498=importlib.util.module_from_spec(spec);sys.modules["k498_for_k499"]=K498;spec.loader.exec_module(K498)


class CertificateError(ValueError): pass
def q(x:Any)->Fraction:
    try:return x if isinstance(x,Fraction) else Fraction(x)
    except Exception as exc:raise CertificateError("invalid rational") from exc
def qstr(x:Fraction)->str:return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"


def rational_floor_test(metric,form,target)->dict[str,Any]:
    M=[[q(x) for x in row] for row in metric];R=[[q(x) for x in row] for row in form];b=q(target);n=len(M)
    if n<1 or any(len(row)!=n for row in M+R):raise CertificateError("equal nonempty square matrices required")
    if any(M[i][j]!=M[j][i] or R[i][j]!=R[j][i] for i in range(n) for j in range(n)):raise CertificateError("symmetric matrices required")
    if any(M[i][j] != (M[i][i] if i==j else 0) for i in range(n) for j in range(n)) or any(M[i][i]<=0 for i in range(n)):
        raise CertificateError("K492 diagonal positive metric required")
    A=[[R[i][j]-b*M[i][j] for j in range(n)] for i in range(n)]
    L=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)];pivots=[]
    for i in range(n):
        pivot=A[i][i]-sum((L[i][k]*L[i][k]*pivots[k] for k in range(i)),Fraction())
        pivots.append(pivot)
        if pivot==0:break
        for j in range(i+1,n):
            L[j][i]=(A[j][i]-sum((L[j][k]*L[i][k]*pivots[k] for k in range(i)),Fraction()))/pivot
    positive=len(pivots)==n and all(x>0 for x in pivots)
    return {"target_floor":qstr(b),"ldl_pivots":[qstr(x) for x in pivots],"strictly_positive":positive,"prefix_dimension":n,"exact_rational":True}


def build()->dict[str,Any]:
    control=K498.build()["exact_control"]
    metric=control["transformed_metric"];form=control["transformed_form"]
    pass7=rational_floor_test(metric,form,7);fail8=rational_floor_test(metric,form,8)
    if not pass7["strictly_positive"] or fail8["strictly_positive"]:raise AssertionError("control thresholds changed")
    return {
      "schema_version":"1.0","result_id":"K499-K162-CYCLIC-RATIONAL-FLOOR-COMPILER","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","gu_comparator_routing":K498.ROUTING,
      "scope":"Exact finite-prefix positivity decision for K498's cyclic contrast form relative to the diagonal K492 metric.",
      "gu_typed_objects":{"result":"cyclic rational floor compiler MAP-TYPE=finite-form-certificate","carrier":"finite prefix of the K492 cyclic M-orthogonal contrasts","pairing":"diagonal positive K492 M metric","form":"K498 transformed same fixed form","real_structure":"CAR adjoint on one fixed charge sector","grading":"contrast index/bath-number filtration","action_owner":"repository-supplied conditional operator","target":"finite-prefix input toward the infinite cyclic floor"},
      "theorem":{"test":"R_N-b M_N is strictly positive iff every exact no-pivot LDL diagonal is positive","arithmetic":"rational only; no floating generalized eigensolver","finite_prefix_only":True,"infinite_release":"combine expanding-prefix certificates with a separately proved uniform tail floor and boundary-cross bound"},
      "exact_controls":{"floor_7_passes":pass7,"floor_8_fails":fail8,"control_is_native_K162_packet":False},
      "decision":{"exact_finite_floor_compiler_released":True,"native_finite_prefix_values_supplied":False,"native_infinite_cyclic_floor_emitted":False,"next_exact_input":"Instantiate K498's native scalar sequences on expanding prefixes and prove a uniform tail floor plus prefix/tail boundary control before emitting the infinite cyclic alpha."},
      "source_and_ledger_effect":"none",
      "claim_ceiling":"Exact finite-prefix compiler only. A passing prefix cannot establish the infinite cyclic floor or the full K162 complement floor; no K473 beta, K152 interval, source, ledger, canon, paper, public or physical conclusion follows."
    }


def main():
    p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
    if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    else:print(json.dumps(d,indent=2,sort_keys=True))
    return 0
if __name__=="__main__":raise SystemExit(main())

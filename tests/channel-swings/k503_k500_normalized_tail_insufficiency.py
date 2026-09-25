#!/usr/bin/env python3
"""K503 reject absolute-orbit-tail substitution for normalized K500 leakage."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k503-k500-normalized-tail-insufficiency.json";Q=Fraction(3,8)
def qstr(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def control(levels:int=6)->list[dict[str,Any]]:
 if levels<3:raise ValueError("at least three levels required")
 rows=[]
 for n in range(levels):
  word_norm=Q**n/Fraction(n+1);leakage=Fraction(n+1);absolute=word_norm*leakage
  rows.append({"level":n,"word_norm":qstr(word_norm),"contraction_majorant":qstr(Q**n),"normal_leakage":qstr(leakage),"absolute_action_residual":qstr(absolute),"absolute_bound_saturated":absolute==Q**n,"word_norm_below_contraction_majorant":word_norm<=Q**n,"G_step_ratio":None if n==0 else qstr(Q*Fraction(n,n+1))})
 return rows
def build():
 rows=control()
 return {"schema_version":"1.0","result_id":"K503-K500-NORMALIZED-TAIL-INSUFFICIENCY","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"Logical implication from geometric upper bounds on unnormalized cyclic words and absolute action residuals to K500's uniform leakage on unit level vectors.","theorem":{"construction":"orthogonal two-dimensional bath levels with v_n=(3/8)^n/(n+1)e_n, G v_n=v_(n+1), and self-adjoint W_n exchanging e_n with its noncyclic partner at strength n+1","strict_contraction":"||G||=sup_n (3/8)(n+1)/(n+2)=3/8<1","absolute_orbit_bound":"||(1-P_n)W_n v_n||=(3/8)^n","normalized_leakage":"||(1-P_n)W_n v_n||/||v_n||=n+1 is unbounded","consequence":"a geometric absolute action-orbit tail plus an upper word-norm bound does not imply a uniform normalized leakage bound","sufficient_repair":"supply a native lower envelope for ||v_n|| relative to the absolute residual, or directly prove ||(1-P_n)W_n v_n||^2<=mu^2||v_n||^2 uniformly"},"exact_control":{"ratio":"3/8","levels":rows,"all_absolute_bounds_saturated":all(x["absolute_bound_saturated"] for x in rows),"all_word_norm_upper_bounds_hold":all(x["word_norm_below_contraction_majorant"] for x in rows),"sample_normalized_leakage_strictly_grows":all(Fraction(b["normal_leakage"])>Fraction(a["normal_leakage"]) for a,b in zip(rows,rows[1:])),"abstract_sequence_unbounded":True,"native_K162_counterexample":False},"decision":{"K175_K496_absolute_tails_sufficient_for_K500_leakage":False,"existing_native_tail_results_retracted":False,"complete_uniform_leakage_emitted":False,"route_effect":"Do not divide K175/K496 by an upper word-norm estimate. Acquire a native word-norm lower sequence or a directly normalized K501 variance estimate.","next_exact_input":"Exploit the explicit CAR path amplitudes to lower-bound nonzero ||G^n phi|| on the supported native levels, or evaluate the K501 variance directly with relative error uniform in n."},"source_and_ledger_effect":"none","claim_ceiling":"A logical insufficiency result for reusing current absolute orbit tails. The control is not a native K162 counterexample and does not show native leakage is large, obstruct a complement floor, move K473/K152, or change source, ledger, canon, paper, public or physical conclusions."}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 else:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())

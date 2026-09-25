#!/usr/bin/env python3
"""K496 transfer K495's kernel certificate into K176's orbit tail."""
from __future__ import annotations
import argparse,importlib.util,json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
OUTPUT=ROOT/"lab/process/k496-k176-sharp-exchange-tail.json"
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
K495=load("k495_for_k496","k495_k176_kernel_l2_outward.py")
Q=Fraction(3,8);MONOMIALS=16;KERNEL_NORM=Fraction(1,16);COEFFICIENT=MONOMIALS*KERNEL_NORM
def qstr(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def exchange_tail(n:int)->Fraction:
 if n<1:raise ValueError("resolve at least order one")
 return COEFFICIENT*Q**n*((n+1)-n*Q)/(1-Q)**3
def build():
 k=K495.build();assert k["decision"]["strict_release_test_passed"]
 return {"schema_version":"1.0","result_id":"K496-K176-SHARP-EXCHANGE-TAIL","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"K176's coefficient-complete 16-monomial exchange orbit on K162 zero-bath seeds, using K495's strict kernel norm certificate.","premises":{"kernel_certificate":"K495-K176-KERNEL-L2-OUTWARD","kernel_norm_upper":"1/16","exchange_monomials":MONOMIALS,"Hilbert_ratio":"3/8","finite_cutoff_normal_form":"K176-LAST-CONTRACTION-EXCHANGE-ORBIT-TAIL","cross_polarity_cancellation_used":False},"sharp_tail":{"coefficient_upper":qstr(COEFFICIENT),"order_n_bound":"n*(3/8)^(n-1)","formula_after_order_N":"(3/8)^N*((N+1)-N*(3/8))/(1-3/8)^3","after_order_1":qstr(exchange_tail(1)),"after_order_1_expected":"312/125","after_order_12":qstr(exchange_tail(12)),"strictly_improves_K176_coefficient":COEFFICIENT<Fraction(40,3),"all_order_tail_convergent":True},"decision":{"K176_coefficient_reduced_from":"40/3","K176_coefficient_reduced_to":"1","signed_orders_2_through_12_still_required_for_cross_decision":False},"source_and_ledger_effect":"none","claim_ceiling":"A sharper norm transfer inside K176's already coefficient-complete exchange orbit. It does not by itself decide a combined cross, complete complement floor, K152 interval, source, ledger, canon, paper, public or physical conclusion."}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 else:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())

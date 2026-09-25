#!/usr/bin/env python3
"""K497 close K493's q00/q10 cross signs with K496's complete tail."""
from __future__ import annotations
import argparse,importlib.util,json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
OUTPUT=ROOT/"lab/process/k497-k152-cross-sign-release.json"
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
K175=load("k175_for_k497","k175_matched_range_exchange_tail.py");K493=load("k493_for_k497","k493_k152_base_cross_prefix_tail_budget.py");K496=load("k496_for_k497","k496_k176_sharp_exchange_tail.py")
def qstr(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def row(r):
 low,high=map(Fraction,r["resolved_through_first_block_interval"]);h=Fraction(r["corrected_line_H_norm_upper"])
 tail=(K175.diagonal_tail(1)+K496.exchange_tail(1))*h
 total=(low-tail,high+tail)
 return {"charge":r["charge"],"seed":r["seed"],"resolved_through_first_block_interval":[qstr(low),qstr(high)],"corrected_line_H_norm_upper":qstr(h),"complete_post_order_1_normal_cross_abs_upper":qstr(tail),"complete_all_order_cross_interval":[qstr(total[0]),qstr(total[1])],"strictly_negative":total[1]<0,"zero_exclusion_margin":qstr(-total[1])}
def build():
 rows=[row(x) for x in K493.build()["native_sector_budgets"]]
 return {"schema_version":"1.0","result_id":"K497-K152-CROSS-SIGN-RELEASE","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"The combined K139/K156 base plus K168 shape cross between each K489 q00/q10 trial seed and its first corrected M-orthogonal cyclic line.","composition":{"signed_prefix":"K493 resolved base, shape and actual K172 first normal block","diagonal_tail":"K175 complete matched diagonal orbit after order one","exchange_tail":"K496 complete coefficient-level exchange orbit after order one","cauchy_schwarz_pairing":"multiply the summed action-column tail by K493's corrected-line H-norm upper","finite_orders_2_through_12_evaluated":False},"native_sector_releases":rows,"decision":{"both_crosses_strictly_negative":all(x["strictly_negative"] for x in rows),"signed_orders_2_through_12_retired_for_this_decision":all(x["strictly_negative"] for x in rows),"cyclic_complement_floor_emitted":False,"noncyclic_floor_or_cross_emitted":False,"K152_interval_emitted":False,"next_exact_input":"Use K492's exhaustive cyclic contrast basis to bound the same fixed form on the full cyclic complement, then construct the noncyclic C^perp_M floor and cyclic/noncyclic cross required by K494/K473."},"source_and_ledger_effect":"none","claim_ceiling":"The two first corrected cyclic-line crosses are strictly negative with complete all-order normal tails. This retires the order-2-through-12 calculation only for that sign decision. It does not prove a cyclic or complete-complement floor, K473 beta, K152 interval, source, ledger, canon, paper, public or physical conclusion."}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 else:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())

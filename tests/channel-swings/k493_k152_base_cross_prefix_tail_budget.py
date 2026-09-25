#!/usr/bin/env python3
"""K493 native first-block and complete later-order budget for K491's cross."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
OUTPUT=ROOT/"lab/process/k493-k152-base-cross-prefix-tail-budget.json"


def load(name,filename):
    s=importlib.util.spec_from_file_location(name,HERE/filename)
    if s is None or s.loader is None: raise RuntimeError(filename)
    m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m


K170=load("k170_for_k493","k170_direct_gram_reference_shape_slice.py")
K172=load("k172_for_k493","k172_continuum_first_block_graph_tail.py")
K175=load("k175_for_k493","k175_matched_range_exchange_tail.py")
K176=load("k176_for_k493","k176_last_contraction_exchange_orbit_tail.py")
K489=load("k489_for_k493","k489_native_neumann_word_m_orthogonalization.py")
K490=load("k490_for_k493","k490_k168_native_shape_cross_estimate.py")


def qstr(x:Fraction)->str:return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"


def sector_budget(k489:dict[str,Any],k490:dict[str,Any],seed_kind:str)->dict[str,Any]:
    b0,b1=map(Fraction,k489["B_tail_mass_interval"])
    a10,a11=map(Fraction,k489["first_word_norm_sq_interval"])
    c0=b0/(1+b0);c1=b1/(1+b1)
    t_h_sq_upper=a11+c1*c1
    t_h_upper=K170.sqrt_interval(t_h_sq_upper)[1]
    shape_abs0,shape_abs1=map(Fraction,k490["trial_to_corrected_tail_shape_cross_abs_interval"])
    if k490["trial_to_corrected_tail_shape_cross_sign"]=="positive": shape=(shape_abs0,shape_abs1)
    else: shape=(-shape_abs1,-shape_abs0)
    first=K172.first_block(seed_kind)
    h_upper=Fraction(first["profile_norm_interval"][1])
    # Vacuum: two components with multiplicity one. One-impurity: one
    # component with multiplicity two. Both give 2 <h,Dh>.
    correction_upper=h_upper/Fraction(8)
    correction_cross_upper=correction_upper/(1+b0)
    resolved_low=-256*c1+shape[0]
    resolved_high=-256*c0+shape[1]+correction_cross_upper
    after1=(K175.diagonal_tail(1)+K176.exchange_tail(1))*t_h_upper
    after12=(K175.diagonal_tail(12)+K176.exchange_tail(12))*t_h_upper
    return {
      "charge":k489["charge"],"seed":k489["seed"],
      "scalar_base_cross_interval":[qstr(-256*c1),qstr(-256*c0)],
      "complete_shape_cross_interval":[qstr(shape[0]),qstr(shape[1])],
      "native_first_block_normal_correction_interval":["0",qstr(correction_cross_upper)],
      "resolved_through_first_block_interval":[qstr(resolved_low),qstr(resolved_high)],
      "corrected_line_H_norm_upper":qstr(t_h_upper),
      "post_order_1_normal_cross_abs_upper":qstr(after1),
      "post_order_12_normal_cross_abs_upper":qstr(after12),
      "current_order_1_total_interval":[qstr(resolved_low-after1),qstr(resolved_high+after1)],
      "current_order_1_decides_nonzero":resolved_low-after1>0 or resolved_high+after1<0,
      "order_12_release_test":"after evaluating signed normal orders 2..12, enlarge the resulting interval by post_order_12_normal_cross_abs_upper and require zero exclusion",
      "order_12_tail_smaller_than_order_1_tail":after12<after1,
    }


def build()->dict[str,Any]:
    a=K489.build()["native_sectors"]; s=K490.build()["native_sector_bounds"]
    rows=[sector_budget(a[0],s[0],"vacuum"),sector_budget(a[1],s[1],"one_impurity")]
    return {
      "schema_version":"1.0","result_id":"K493-K152-BASE-CROSS-PREFIX-TAIL-BUDGET","created":"2026-09-25","status":"working_draft_verified",
      "classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"K491's combined base-plus-K168 cross on K489's q00/q10 corrected first-tail lines, using K172 first-block data and K175/K176 all-order tails.",
      "gu_typed_objects":{"result":"native combined-cross acquisition budget MAP-TYPE=interval-bound","carrier":"K489 q00/q10 corrected lines","pairing":"regular-coordinate Hilbert pairing with physical M orthogonality","form":"fixed K139/K156 base plus K168 shape","target":"signed cross prerequisite for a future same-form complement estimate"},
      "decomposition":{
        "base":"R0=A-256M-S*X S","scalar_cross":"<phi,(A-256M)t>=-256B/A because <phi,Mt>=0",
        "shape":"q00 +3O/A; q10 -3O/A","first_normal_block":"K172 gives 2<h,D_256 h>/A in both q00 and q10",
        "later_normal_action":"K175 matched diagonal plus K176 coefficient-complete exchange tail, paired with t by Cauchy-Schwarz",
        "no_separate_plus_minus_256_bounds":True,
      },
      "native_sector_budgets":rows,
      "decision":{
        "actual_native_first_block_used":True,"complete_later_order_tail_used":True,"order_1_bound_decides_cross":all(r["current_order_1_decides_nonzero"] for r in rows),
        "finite_orders_2_through_12_numerically_evaluated":False,
        "next_exact_input":"Evaluate only the signed K179/K456 normal cross through order 12, not the full 59,586-entry residual Gram. K176/K175 then leave the recorded small rigorous tail; exclude zero before using the cyclic cross in a floor estimate.",
      },
      "source_and_ledger_effect":"none",
      "claim_ceiling":"Actual native first-block and complete all-order remainder budgets for the cancellation-safe combined cross. The existing order-one enclosure is inconclusive; finite signed orders 2--12 remain unevaluated. No complete complement floor, K473 beta, K152 interval, source, ledger, canon, paper, public or physical conclusion follows."
    }


def main()->int:
    p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");p.add_argument("--demo",action="store_true");a=p.parse_args();d=build()
    if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    if a.demo or not a.write:print(json.dumps(d,indent=2,sort_keys=True))
    return 0
if __name__=="__main__":raise SystemExit(main())

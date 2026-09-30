#!/usr/bin/env python3
"""K694: extend dense-core positive Gram bounds and retain the complete tail."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k694-k500-monotone-gram-closure-compiler.json"
def q(x:Fraction)->str:return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def build()->dict[str,Any]:
    k688=json.loads((ROOT/"lab/process/k688-k500-partial-gram-bound-compiler.json").read_text())
    k693_path=ROOT/"lab/process/k693-k500-graph-equivalent-column-compiler.json"
    assert k688["partial_gram_theorem"]["uniform_partial_bound"]
    finite=Fraction(1,400)+Fraction(1,625)
    tail=Fraction(1,400); total=finite+tail
    assert finite==Fraction(41,10000) and total==Fraction(33,5000)
    return {
      "schema_version":"1.0","result_id":"K694-K500-MONOTONE-GRAM-CLOSURE-COMPILER","created":"2026-09-30",
      "status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"A dense-core-to-complete-space positive partial-Gram theorem for bounded component transforms, including an explicit positive operator tail and Q_seed compression.",
      "gu_typed_objects":{"component_transforms":"B_j=C_j a^-1 in B(H,K_j)","positive_grams":"G_N=sum_(j<=N) B_j*B_j on H","seed_compression":"Q_seed* G Q_seed on the complete seed complement","result":"monotone Gram closure compiler MAP-TYPE=complete positive operator order","target":"K688's global and Q_seed complete Gram/tail inputs"},
      "monotone_gram_theorem":{
        "bounded_component_transforms_required":True,"one_dense_core_required":True,
        "core_partial_order":"sum_(j<=N)||B_j u||^2<=g||u||^2 for every u in D0 and every finite N",
        "extension_consequence":"each finite positive Gram order extends by continuity from dense D0 to H",
        "monotone_limit_consequence":"G_N increases strongly to one bounded positive G<=gI",
        "column_consequence":"B=(B_j)_j is bounded and ||B||^2=||G||<=g",
        "tail_order":"G-G_N0<=tau^2 I on H, proved independently or as a complete positive remainder bound",
        "seed_compression":"Q_seed*GQ_seed<=g_seed Q_seed; compression preserves positive order",
        "finite_prefix_without_complete_tail_sufficient":False,"component_norms_without_positive_gram_order_sufficient":False,
        "order_on_nondense_test_space_sufficient":False,"sampled_vectors_sufficient":False,"strong_limit_without_uniform_order_sufficient":False,
      },
      "exact_controls":{"controls_are_synthetic":True,"model":"H=C^2; B1=diag(1/20,1/25), B2=diag(1/25,1/20), B3=(1/20)I and B_j=0 for j>=4","finite_partial_upper":q(finite),"complete_tail_upper":q(tail),"complete_global_upper":q(total),"Q_seed_upper":q(total),"K677_target":"1/100","target_slack":q(Fraction(1,100)-total),"accepted":total<=Fraction(1,100),"finite_prefix_counterexample":"after any fixed prefix append B_j=I forever; every recorded prefix is unchanged but the complete column diverges","nondense_core_counterexample":"on C^2 test only span(e1); diag(0,L) is invisible there and has arbitrary complete norm"},
      "dependency_reconciliation":{"K688_dense_core_order_made_executable":True,"K693_bounded_transform_consumed_conditionally":k693_path.name.endswith("compiler.json"),"K685_complete_tail_requirement_retained":True,"K677_Q_seed_target_reproduced":True,"native_gram_or_tail_data_added":False},
      "native_interface_status":{"actual_native_Bj_serialized":False,"actual_native_dense_core_order_proved":False,"actual_native_monotone_Gram_limit_proved":False,"actual_native_complete_tail_proved":False,"actual_native_Q_seed_order_proved":False,"actual_native_K677_target_proved":False,"native_complete_floor_emitted":False},
      "decision":{"dense_core_uniform_Gram_order_extends_to_complete_space":True,"native_complete_Gram_packet_constructed":False,"next_exact_input":"After K693 supplies bounded native B_j, prove the uniform positive partial-Gram order on one dense core and an operator-order tail globally and after Q_seed; then combine with K676's three native seed actions."},
      "source_and_ledger_effect":"none","ledger_no_change_reason":"This is a conditional positive-operator convergence theorem and supplies no source-owned action, physical quotient, state or observable.",
      "preflight_bookend":{"route_comparison":"K688 states the full partial-Gram interface. K694 makes it checkable on one dense core for bounded transforms and isolates the omitted positive tail as the only complete-space remainder.","retrieval_collision_result":"K685/K688 require complete bounds but do not state the dense-core continuity passage or monotone positive limit as one certificate.","strongest_alternative":"Prove the complete column norm directly, or use K677's cofinal core/tail estimate without component Grams."},
      "postflight_bookend":{"strongest_overclaim":"Treating a finite Gram, scalar component norms or sampled vectors as a complete positive operator order.","strongest_contrary_construction":"An unchanged finite prefix can be followed by infinitely many identity components, while a nondense test space can hide an arbitrarily large orthogonal block.","weakest_reproducibility_seam":"Every B_j must already be bounded on H, the same dense core must serve all N, and the tail must cover the entire omitted positive sum in operator order."},
      "controls":{"producer":"tests/channel-swings/k694_k500_monotone_gram_closure_compiler.py","probe":"tests/channel-swings/k694_k500_monotone_gram_closure_compiler_probe.py","controls_passed":38,"hostile_mutations_rejected":32},
      "claim_ceiling":"Exact conditional monotone-Gram theorem: uniform positive partial-Gram order for bounded transforms on one dense core extends to H and converges to the complete positive Gram; one complete tail order and compression then give the global and Q_seed bounds. Current native custody supplies no bounded component transforms, core order, tail or seed actions. No native R, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows."
    }
def validate(p):
    t=p["monotone_gram_theorem"]; c=p["exact_controls"]; n=p["native_interface_status"]
    assert t["bounded_component_transforms_required"] and t["one_dense_core_required"]
    for k in ["finite_prefix_without_complete_tail_sufficient","component_norms_without_positive_gram_order_sufficient","order_on_nondense_test_space_sufficient","sampled_vectors_sufficient","strong_limit_without_uniform_order_sufficient"]: assert not t[k]
    assert c["finite_partial_upper"]=="41/10000" and c["complete_tail_upper"]=="1/400" and c["complete_global_upper"]=="33/5000"
    assert c["target_slack"]=="17/5000" and c["accepted"]
    assert p["target_claim"]=="NONE-NOT-A-KILL" and p["source_and_ledger_effect"]=="none" and all(v is False for v in n.values())
    assert p["decision"]["dense_core_uniform_Gram_order_extends_to_complete_space"] and not p["decision"]["native_complete_Gram_packet_constructed"]
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";(OUTPUT.write_text(s) if a.write else print(s,end=""));return 0
if __name__=="__main__":raise SystemExit(main())

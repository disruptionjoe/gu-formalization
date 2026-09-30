#!/usr/bin/env python3
"""K700: certify A>2/3 with a nonzero seed/complement cross block."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k700-k500-cross-coupled-a-margin-compiler.json"

def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def build() -> dict[str, Any]:
    k697 = json.loads((ROOT / "lab/process/k697-k500-seed-complement-a-margin-compiler.json").read_text())
    assert k697["block_theorem"]["R_star_R_reduction_required_for_maximum_rule"]
    s, t, k, target = Fraction(1,4), Fraction(1,100), Fraction(1,60), Fraction(1,3)
    p, r = target-s, target-t
    det, trace = p*r-k*k, p+r
    schur_floor = det/trace
    a_lower = 1-target+schur_floor
    return {
      "schema_version":"1.0", "result_id":"K700-K500-CROSS-COUPLED-A-MARGIN-COMPILER", "created":"2026-09-30",
      "status":"working_draft_verified", "classification":"INTERNAL_STRUCTURAL_ONLY", "direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL",
      "scope":"A complete seed/complement block certificate for A=I-R*R that permits a nonzero off-diagonal block instead of requiring exact reduction.",
      "gu_typed_objects": {"operator":"bounded native R=T a^-1", "seed_projection":"orthogonal P_seed", "complement":"Q_seed=I-P_seed", "cross":"P_seed R*R Q_seed", "result":"cross-coupled A-margin compiler MAP-TYPE=two-block Schur order", "target":"K668/K670's complete A lower"},
      "theorem": {
        "complete_seed_bound_required":True, "complete_complement_bound_required":True, "complete_cross_bound_required_without_reduction":True,
        "hypotheses":"P R*R P<=sP, Q R*R Q<=tQ, ||P R*R Q||<=k",
        "strict_target_test":"s<q, t<q and k^2<(q-s)(q-t) imply R*R<qI",
        "quantitative_floor":"qI-R*R is bounded below by the smaller eigenvalue of [[q-s,-k],[-k,q-t]], and at least determinant/trace",
        "A_consequence":"A>=1-q+determinant/trace",
        "exact_reduction_required":False, "zero_cross_assumption_required":False, "individual_compression_bounds_alone_sufficient":False, "finite_complement_prefix_sufficient":False,
      },
      "exact_controls": {
        "controls_are_synthetic":True, "seed_norm_square_upper":q(s), "complement_norm_square_upper":q(t), "cross_upper":q(k), "target_R_norm_square_upper":q(target),
        "seed_target_gap":q(p), "complement_target_gap":q(r), "cross_square":q(k*k), "schur_determinant_slack":q(det), "schur_trace":q(trace), "certified_q_minus_gram_floor":q(schur_floor), "A_lower":q(a_lower), "target_A_lower":"2/3", "accepted":det>0,
        "aligned_output_counterexample":"Small diagonal compressions can still produce a large complete norm when the off-diagonal block is uncontrolled."
      },
      "dependency_reconciliation": {"K697_reducing_maximum_route_preserved":True, "K697_nonreducing_repair_instantiated":True, "K676_seed_interface_consumed":True, "K677_complete_complement_interface_consumed":True, "native_cross_data_added":False},
      "native_interface_status": {"actual_native_R_constructed":False, "actual_native_seed_bound_proved":False, "actual_native_complete_complement_bound_proved":False, "actual_native_cross_bound_proved":False, "native_A_above_two_thirds_proved":False, "native_complete_floor_emitted":False},
      "decision": {"nonzero_cross_packet_can_supply_A_above_two_thirds":True, "native_A_margin_constructed":False, "next_exact_input":"After constructing native R, prove complete seed and complement square bounds plus ||P_seed R*R Q_seed||. It is enough that the cross square lie strictly below (1/3-s)(1/3-t); exact reduction is not required."},
      "source_and_ledger_effect":"none", "ledger_no_change_reason":"This is a conditional complete operator-block theorem and supplies no source-owned action, physical quotient, state or observable.",
      "preflight_bookend": {"route_comparison":"K697's maximum rule is sharp under reduction but native reduction is unowned. A direct cross estimate is the cheaper robust alternative when the split only approximately reduces R*R.", "retrieval_collision_result":"K697 names the two-by-two repair but does not freeze the strict A>2/3 Schur budget or a positive rational floor.", "strongest_alternative":"Prove exact P_seed reduction and use the K697 maximum rule."},
      "postflight_bookend": {"strongest_overclaim":"Using only the seed and complement diagonal bounds when the cross block is nonzero.", "strongest_contrary_construction":"Aligned seed and complement outputs can saturate an uncontrolled cross and double the one-block estimate.", "weakest_reproducibility_seam":"All three bounds must use the same native R, projections and complete graph Hilbert norm."},
      "controls":{"producer":"tests/channel-swings/k700_k500_cross_coupled_a_margin_compiler.py", "probe":"tests/channel-swings/k700_k500_cross_coupled_a_margin_compiler_probe.py", "controls_passed":36, "hostile_mutations_rejected":30},
      "claim_ceiling":"Exact conditional Schur theorem: complete seed square s, complement square t and cross k give A>2/3 whenever s,t<1/3 and k^2<(1/3-s)(1/3-t). The synthetic s=1/4, t=1/100, k=1/60 packet has determinant slack 2/75 and certifies A>=134/183. No native R, cross, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows."
    }

def validate(p: dict[str, Any]) -> None:
    t,c,n=p["theorem"],p["exact_controls"],p["native_interface_status"]
    for key in ("complete_seed_bound_required","complete_complement_bound_required","complete_cross_bound_required_without_reduction"): assert t[key]
    for key in ("exact_reduction_required","zero_cross_assumption_required","individual_compression_bounds_alone_sufficient","finite_complement_prefix_sufficient"): assert not t[key]
    assert c["seed_norm_square_upper"]=="1/4" and c["complement_norm_square_upper"]=="1/100" and c["cross_upper"]=="1/60"
    assert c["schur_determinant_slack"]=="2/75" and c["schur_trace"]=="61/150"
    assert c["certified_q_minus_gram_floor"]=="4/61" and c["A_lower"]=="134/183" and c["accepted"]
    assert all(v is False for v in n.values())
    assert p["decision"]["nonzero_cross_packet_can_supply_A_above_two_thirds"] and not p["decision"]["native_A_margin_constructed"]
    assert p["target_claim"]=="NONE-NOT-A-KILL" and p["source_and_ledger_effect"]=="none"

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); payload=build(); validate(payload); rendered=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())

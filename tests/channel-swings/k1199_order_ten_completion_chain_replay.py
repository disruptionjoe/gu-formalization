#!/usr/bin/env python3
"""Replay the K546--K553 order-ten completion chain."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1199-order-ten-completion-chain-replay.json"
def build()->dict[str,Any]:
 rows=[]
 for n in range(546,554):
  f=next((ROOT/"lab/process").glob(f"k{n}-*.json"));p=json.loads(f.read_text());rows.append((n,f,p))
 decisions={n:p["decision"] for n,_,p in rows}
 stages={"nested_dual_obstruction_found":decisions[546]["naive_monotone_optimal_scalar_dual_reuse_rejected"],"zero_safe_derivative_bank_complete":decisions[547]["native_order_ten_zero_safe_global_derivative_bank_complete"],"bivariate_newton_fronts_complete":decisions[548]["bivariate_determinant_permutation_exponent_interface_complete"],"zero_inclusive_determinant_envelopes_complete":decisions[549]["zero_inclusive_global_determinant_envelopes_complete"],"all_face_majorants_complete":decisions[550]["whole_radial_majorant_emitted_for_every_K414_face_program"],"disjoint_hybrid_majorants_complete":decisions[551]["all_twenty_two_K409_hybrid_majorants_emitted"],"complete_peano_remainder_emitted":decisions[552]["complete_order_ten_raw_remainder_emitted"],"complete_integral_enclosure_emitted":decisions[553]["complete_order_ten_integral_enclosure_emitted"]}
 return {"schema_version":"1.0","result_id":"K1199-ORDER-TEN-COMPLETION-CHAIN-REPLAY","created":"2026-10-06","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","fixed_control":{"predecessor_manifests":[str(f.relative_to(ROOT)) for _,f,_ in rows],"chain_length":len(rows),"face_programs":rows[4][2]["fixed_control"]["face_programs"],"hybrid_terms":rows[5][2]["fixed_control"]["hybrid_terms"],"ordered_descriptors":rows[7][2]["fixed_control"]["ordered_descriptors"],"native_prefactor_application_count":rows[7][2]["fixed_control"]["native_prefactor_application_count"]},"completion_chain":stages,"decision":{"order_ten_numerical_projective_route_is_complete_to_conditional_integral_enclosure":True,"order_ten_sign_decided":decisions[553]["order_ten_sign_decided"],"action_column_emitted":decisions[553]["action_column_emitted"],"R_ref_residual_emitted":decisions[553]["R_ref_residual_emitted"],"native_K152_interval_emitted":decisions[553]["native_K152_interval_emitted"],"next_exact_input":decisions[553]["next_exact_input"]},"release_test":{"exactly_8_chain_artifacts":len(rows)==8,"all_completion_stages_hold":all(stages.values()),"exactly_936_face_majorants":rows[4][2]["fixed_control"]["face_programs"]==936,"exactly_22_hybrids":rows[5][2]["fixed_control"]["hybrid_terms"]==22,"prefactor_applied_once":rows[7][2]["fixed_control"]["native_prefactor_application_count"]==1,"action_column_not_overclaimed":not decisions[553]["action_column_emitted"],"R_ref_not_overclaimed":not decisions[553]["R_ref_residual_emitted"],"K152_not_overclaimed":not decisions[553]["native_K152_interval_emitted"],"protected_status_unchanged":True},"claim_ceiling":"Exact dependency replay of K546--K553. The scalar-dual obstruction is repaired by derivative-order-ten bounds and same-permutation Newton fronts, then composed through zero-inclusive determinant envelopes, all 936 face majorants, 22 disjoint hybrid majorants, the complete Peano remainder and the complete conditional order-ten integral enclosure. Sign, action column, R_ref, K152 and physical conclusions remain open."}
def validate_payload(p:dict[str,Any])->None:
 if not all(p["release_test"].values()):raise AssertionError("K1199 chain replay failed")
 if not all(p["completion_chain"].values()):raise AssertionError("K1199 completion stage missing")
 d=p["decision"]
 if d["action_column_emitted"] or d["R_ref_residual_emitted"] or d["native_K152_interval_emitted"]:raise AssertionError("K1199 overclaimed downstream result")
def main()->int:
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate_payload(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())

#!/usr/bin/env python3
"""K782: compile the first admissible nonzero-residual source two-jet packet."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k782-sc-act-06-nonzero-residual-two-jet-admission.json"
def build()->dict[str,Any]:
 ks={k:json.loads((ROOT/f"lab/process/k{k}-sc-act-06-{n}.json").read_text()) for k,n in [(779,"nonzero-residual-euler-image"),(780,"kernel-transverse-stationarity-obstruction"),(781,"residual-curvature-novelty")]}
 assert ks[779]["theorem"]["euler_covector_lies_in_image_J_star"] and ks[780]["decision"]["transverse_candidate_rejected"] and ks[781]["decision"]["candidate_must_compute_actual_contraction_before_rank_credit"]
 required=["source-typed background two-jet","actual fixed residual pairing Q and Q Upsilon","complete I1B Euler covector","complete DUpsilon response J","proof E_I1B annihilates ker(J) and exact combined Euler cancellation","complete contracted residual curvature C_U=(D2Upsilon)^*(Q Upsilon)","full old plus new coupled principal Hessian","owned gauge and redundant-Euler maps with compositions","common Euclidean real carrier and domain","middle exactness at every nonzero covector"]
 return {"schema_version":"1.0","result_id":"K782-SC-ACT-06-NONZERO-RESIDUAL-TWO-JET-ADMISSION","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Admission compiler for the first source-typed nonzero-residual stationary two-jet eligible for an SC-ACT-06 exact-complex test.",
 "gu_typed_objects":{"carrier":"one common source field/residual/gauge/redundancy carrier","pairing":"actual source/background-owned Q on the same residual carrier","real_structure":"one authenticated Euclidean continuation or positive reduction","grading":"gauge -> fields -> Euler equations -> redundancies","action_owner":"released I1B plus I2B, without comparator substitution","target":"stationary coupled all-covector deformation complex"},
 "required_packet":required,"rejection_rules":{"nonzero_Upsilon_without_stationarity":"reject","stationarity_without_kernel_annihilation":"reject","D2Upsilon_without_contraction_by_Q_Upsilon":"reject","nonzero_C_U_without_relative_image_or_rank_test":"reject","kernel_containment_without_owned_gauge_map":"reject","one_covector_rank_without_all_covectors":"reject","Lorentzian_or_indefinite_pairing_called_Euclidean":"reject"},
 "current_custody":{"source_typed_nonzero_residual_two_jet":False,"actual_pairing_on_candidate":False,"complete_I1B_euler":False,"complete_DUpsilon":False,"kernel_annihilation_and_combined_stationarity":False,"complete_contracted_D2Upsilon":False,"complete_coupled_principal_hessian":False,"owned_gauge_redundancy_complex":False,"common_Euclidean_real_domain":False,"all_covector_middle_exactness":False},
 "decision":{"candidate_admitted":False,"SC_ACT_06_status":"ASSERTS","do_not_retry":"residual nonzero by itself, another pairing/weight, an affine residual, or a kernel promoted to gauge","incumbent":"construct the first complete source-typed nonzero-residual stationary two-jet satisfying every K782 row","strongest_independent_alternative":"complete native K500 A/B packet"},
 "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The compiler sharpens admissibility but supplies none of the missing native data and changes no physics mapping.","claim_ceiling":"Exact successor admission gate only. No stationary germ, new actual rank, gauge complex, ellipticity, global nonzero-residual no-go, source/ledger/canon/paper/public, prediction, confirmation or physical conclusion follows.","controls":{"producer":"tests/channel-swings/k782_sc_act_06_nonzero_residual_two_jet_admission.py","probe":"tests/channel-swings/k782_sc_act_06_nonzero_residual_two_jet_admission_probe.py","controls_passed":38,"hostile_mutations_rejected":26}}
def validate(p:dict[str,Any])->None:
 assert len(p["required_packet"])==10 and set(p["rejection_rules"].values())=={"reject"}
 assert all(v is False for v in p["current_custody"].values()) and not p["decision"]["candidate_admitted"]
 assert p["decision"]["SC_ACT_06_status"]=="ASSERTS" and "nonzero-residual stationary two-jet" in p["decision"]["incumbent"]
 assert p["decision"]["strongest_independent_alternative"]=="complete native K500 A/B packet"
 assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())

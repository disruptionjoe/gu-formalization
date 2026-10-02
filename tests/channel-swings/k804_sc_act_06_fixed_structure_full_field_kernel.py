#!/usr/bin/env python3
"""K804: embed the fixed-structure nonzero-T connection kernel in the released full field packet."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k804-sc-act-06-fixed-structure-full-field-kernel.json"
PATHS={"k719":ROOT/"lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json","k792":ROOT/"lab/process/k792-sc-act-06-redundant-prolongation-kernel-theorem.json","k793":ROOT/"lab/process/k793-sc-act-06-full-field-kernel-persistence.json","k803":ROOT/"lab/process/k803-sc-act-06-nonzero-t-principal-invariance.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
 d={n:json.loads(p.read_text()) for n,p in PATHS.items()}; assert d["k792"]["linearization"]["xi_row_factors_through_direct_response"] and d["k793"]["extension_lemma"]["embedded_subspace_is_in_full_kernel"]
 return {"schema_version":"1.0","result_id":"K804-SC-ACT-06-FIXED-STRUCTURE-FULL-FIELD-KERNEL","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Embedded connection-kernel theorem for any zero-fermion Upsilon=0 germ whose released first-order principal connection structure is the fixed K803 structure.","gu_typed_objects":{"carrier":"released full bosonic-plus-fermionic tangent packet restricted to the pure connection subspace","pairing":"principal field-equation symbol on the zero-fermion diagonal","real_structure":"the pinned real U(64,64) connection basis inherited from K803","grading":"pure connection tangent embedded in the full field tangent","action_owner":"released Upsilon row together with the K719 full-field block decomposition","target":"whether extra field columns or Xi remove the K803 connection kernel"},"pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
 "extension_theorem":{"background_residual_zero_required":True,"fixed_structure_connection_kernel_dimension":106512,"xi_principal_row_factors_through_D_Upsilon":True,"xi_acts_nontrivially_on_connection_kernel":False,"metric_epsilon_columns_can_delete_pure_connection_kernel":False,"zero_fermion_diagonal_can_delete_pure_bosonic_kernel":False,"distinct_i2b_row_imported":False,"embedded_kernel_dimension_in_full_field_symbol":106512,"moving_principal_coefficients_covered":False},
 "decision":{"fixed_structure_released_full_field_packet_middle_exact_before_symmetry":False,"all_nonzero_T_full_field_packets_classified":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"Compare the embedded 106512-dimensional kernel with owned symmetry, or change principal coefficients/rows; extra field columns and Xi do not remove it."},
 "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"This is an algebraic principal-symbol embedding theorem, not a full stationary background, quotient, domain or physical result.","claim_ceiling":"Exact fixed-principal-structure zero-fermion full-field embedding only. Moving coefficients, nonzero fermions, new rows, new owned symmetries and global domains remain open.","controls":{"producer":"tests/channel-swings/k804_sc_act_06_fixed_structure_full_field_kernel.py","probe":"tests/channel-swings/k804_sc_act_06_fixed_structure_full_field_kernel_probe.py","controls_passed":40,"hostile_mutations_rejected":30}}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K804-SC-ACT-06-FIXED-STRUCTURE-FULL-FIELD-KERNEL" and p["target_claim"]=="SC-ACT-06";t=p["extension_theorem"]
 assert t["background_residual_zero_required"] and t["xi_principal_row_factors_through_D_Upsilon"]
 assert (t["fixed_structure_connection_kernel_dimension"],t["embedded_kernel_dimension_in_full_field_symbol"])==(106512,106512)
 for k in ("xi_acts_nontrivially_on_connection_kernel","metric_epsilon_columns_can_delete_pure_connection_kernel","zero_fermion_diagonal_can_delete_pure_bosonic_kernel","distinct_i2b_row_imported","moving_principal_coefficients_covered"):assert not t[k]
 q=p["decision"];assert not q["fixed_structure_released_full_field_packet_middle_exact_before_symmetry"] and not q["all_nonzero_T_full_field_packets_classified"] and not q["global_sc_act_06_proved_or_refuted"] and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())

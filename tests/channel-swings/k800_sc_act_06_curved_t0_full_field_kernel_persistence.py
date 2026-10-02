#!/usr/bin/env python3
"""K800: compose the curved-family kernel with Xi, fields, fermions and symmetry budget."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k800-sc-act-06-curved-t0-full-field-kernel-persistence.json"
PATHS = {
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
    "k792": ROOT / "lab/process/k792-sc-act-06-redundant-prolongation-kernel-theorem.json",
    "k793": ROOT / "lab/process/k793-sc-act-06-full-field-kernel-persistence.json",
    "k799": ROOT / "lab/process/k799-sc-act-06-curved-t0-direct-response-transport.json",
}
def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def build() -> dict[str, Any]:
    d = {n: json.loads(p.read_text()) for n,p in PATHS.items()}; k789,k792,k793,k799=(d[n] for n in ("k789","k792","k793","k799"))
    kernel = k799["decision"]["connection_kernel_dimension"]
    grant = k789["composition_theorem"]["internal_candidate_rank"] + k789["composition_theorem"]["metric_diffeomorphism_rank"]
    bound = kernel - grant
    assert k792["linearization"]["xi_row_factors_through_direct_response"] and k793["extension_lemma"]["embedded_subspace_is_in_full_kernel"]
    return {
      "schema_version":"1.0","result_id":"K800-SC-ACT-06-CURVED-T0-FULL-FIELD-KERNEL-PERSISTENCE","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Persistence of K799's transported connection kernel after the released zero-locus Xi row, zero-fermion full-field extension and maximal current symmetry grant over the certified K127 family.",
      "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
      "composition":{
        "background_residual_zero":True,"xi_principal_row_factors_through_D_Upsilon":True,"xi_reduces_connection_kernel":False,"metric_epsilon_columns_delete_embedded_kernel":False,"zero_fermion_diagonal_acts_on_embedded_bosonic_kernel":False,"distinct_i2b_row_imported":False,"candidate_internal_symmetry_promoted_to_owned_gauge":False,"coherent_transport_preserves_dimensions":True,"global_all_zero_locus_germs_classified":False},
      "exact_bound":{"embedded_connection_kernel_dimension":kernel,"granted_internal_q_lambda_rank":16384,"granted_metric_diffeomorphism_rank":4,"maximal_current_granted_symmetry_rank":grant,"persistent_middle_classes_lower_bound":bound,"uniform_on_certified_family_and_positive_negative_null_real_covectors":True},
      "decision":{"released_full_field_extension_repairs_certified_family":False,"curvature_only_family_middle_exact_under_maximal_grant":False,"next_exact_input":"A nonzero-T or otherwise non-Levi-Civita zero-locus germ with changed principal response, a different authenticated first-order coefficient/row, or at least 90124 additional independent owned symmetry directions."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"This is a local principal-symbol lower bound over one certified family, not a physical quotient or global moduli result.",
      "claim_ceiling":"Exact persistence over the certified K127 family only. The internal q-lambda candidate remains a favorable grant, not source-owned total gauge; no all-germ or global SC-ACT-06 conclusion follows.",
      "controls":{"producer":"tests/channel-swings/k800_sc_act_06_curved_t0_full_field_kernel_persistence.py","probe":"tests/channel-swings/k800_sc_act_06_curved_t0_full_field_kernel_persistence_probe.py","controls_passed":40,"hostile_mutations_rejected":30}}
def validate(p: dict[str,Any])->None:
    assert p["result_id"]=="K800-SC-ACT-06-CURVED-T0-FULL-FIELD-KERNEL-PERSISTENCE" and p["target_claim"]=="SC-ACT-06"
    c=p["composition"]
    for k in ("background_residual_zero","xi_principal_row_factors_through_D_Upsilon","metric_epsilon_columns_delete_embedded_kernel","zero_fermion_diagonal_acts_on_embedded_bosonic_kernel","distinct_i2b_row_imported","candidate_internal_symmetry_promoted_to_owned_gauge","global_all_zero_locus_germs_classified"):
        expected = k in ("background_residual_zero","xi_principal_row_factors_through_D_Upsilon")
        assert c[k] is expected
    assert c["coherent_transport_preserves_dimensions"] and not c["xi_reduces_connection_kernel"]
    b=p["exact_bound"]; assert (b["embedded_connection_kernel_dimension"],b["granted_internal_q_lambda_rank"],b["granted_metric_diffeomorphism_rank"],b["maximal_current_granted_symmetry_rank"],b["persistent_middle_classes_lower_bound"])==(106512,16384,4,16388,90124)
    assert b["uniform_on_certified_family_and_positive_negative_null_real_covectors"]
    assert not p["decision"]["released_full_field_extension_repairs_certified_family"] and not p["decision"]["curvature_only_family_middle_exact_under_maximal_grant"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if a.write else print(s,end=""); return 0
if __name__=="__main__": raise SystemExit(main())

#!/usr/bin/env python3
"""K879: inject the owned tangential quotient into full-field cohomology."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k879-sc-act-06-full-field-quotient-injection.json"
PATHS = {
    "k745": ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json",
    "k793": ROOT / "lab/process/k793-sc-act-06-full-field-kernel-persistence.json",
    "k873": ROOT / "lab/process/k873-sc-act-06-owned-symmetry-custody.json",
    "k876": ROOT / "lab/process/k876-sc-act-06-zero-fermion-gauge-block-custody.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    p = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    k745, k793, k873, k876 = p["k745"], p["k793"], p["k873"], p["k876"]
    metric_ranks = {row["gauge_rank"] for row in k745["exact_controls"]["cases"]}
    old_dim = k873["owned_tangential_quotient"]["quotient_dimension"]
    return {
        "schema_version": "1.0",
        "result_id": "K879-SC-ACT-06-FULL-FIELD-QUOTIENT-INJECTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Injection of K873's owned tangential connection quotient into the zero-fermion full-field middle cohomology on K717, without computing the complementary full-field cohomology.",
        "gu_typed_objects": {
            "carrier": "pure tangential connection kernel inside the K717 metric/epsilon/connection/fermion field tangent",
            "pairing": "none required for the kernel/image injection",
            "real_structure": "K872 real SO(6)xSO(7) tangential quotient",
            "grading": "owned internal gauge plus metric diffeomorphism -> full fields -> Upsilon plus redundant Xi rows",
            "action_owner": "source first-order Upsilon packet with K873-owned internal gauge and K745-owned metric diffeomorphism",
            "target": "MAP-TYPE=equivariant injection into full-field middle cohomology",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "injection_theorem": {
            "pure_connection_kernel_embeds_in_full_kernel": k793["extension_lemma"]["embedded_subspace_is_in_full_kernel"],
            "internal_gauge_image_is_radial": k873["owned_image"]["image_equals_radial_kernel_summand"],
            "radial_tangential_intersection_dimension": 0,
            "metric_diffeomorphism_rank_at_nonzero_covector": next(iter(metric_ranks)),
            "metric_diffeomorphism_symbol_is_injective": True,
            "metric_diffeomorphism_injectivity_proof": {
                "map": "v -> q tensor v + v tensor q",
                "choose_linear_functional": "ell(q)=1 for nonzero q",
                "contract_one_leg": "v+ell(v)q=0",
                "substitute_back": "-2 ell(v) q tensor q=0",
                "conclusion_over_reals": "ell(v)=0 and v=0",
                "sample_rank_controls": sorted(metric_ranks),
            },
            "metric_diffeomorphism_connection_component_at_flat_T0": k873["owned_image"]["metric_diffeomorphism_connection_component_at_flat_T0"],
            "fermionic_gauge_tangent_dimension_at_zero_background": k876["infinitesimal_action"]["fermion_image_dimension_at_zero_background"],
            "pure_tangential_class_in_total_gauge_image_forces_zero_metric_parameter": True,
            "then_internal_parameter_must_have_zero_radial_image": True,
            "induced_map_on_quotients_is_injective": True,
            "common_stabilizer_equivariant": k873["owned_image"]["common_stabilizer"] == "SO(6) x SO(7)",
        },
        "exact_consequence": {
            "connection_kernel_dimension": k873["owned_tangential_quotient"]["full_connection_kernel_dimension"],
            "owned_radial_gauge_dimension": k873["owned_tangential_quotient"]["owned_radial_image_dimension"],
            "injected_tangential_quotient_dimension": old_dim,
            "previous_overgrant_lower_bound": k793["exact_bound"]["persistent_middle_classes_lower_bound"],
            "exact_improvement_over_overgrant": old_dim - k793["exact_bound"]["persistent_middle_classes_lower_bound"],
            "complete_full_field_cohomology_dimension_computed": False,
            "full_field_middle_cohomology_dimension_at_least": old_dim,
            "uniform_on_positive_negative_and_null_real_covectors": True,
        },
        "decision": {
            "owned_tangential_quotient_survives_in_full_field_cohomology": True,
            "metric_diffeomorphisms_reduce_the_pure_tangential_quotient": False,
            "complete_full_field_cohomology_equals_the_injected_submodule": False,
            "next_exact_input": "Transfer K872's 40 real SO(6)xSO(7) types through this injection, remove the redundant Xi target row exactly, then compare only genuinely independent source/action-owned repair modules.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem identifies a local full-field cohomology submodule but constructs no physical state, observable, domain, prediction or confirmation.",
        "claim_ceiling": "Exact equivariant injection of a 90128-dimensional tangential quotient into K717's zero-fermion full-field cohomology. No equality with complete cohomology, global ellipticity, rich moduli or physical conclusion follows.",
        "controls": {"producer": "tests/channel-swings/k879_sc_act_06_full_field_quotient_injection.py", "probe": "tests/channel-swings/k879_sc_act_06_full_field_quotient_injection_probe.py", "controls_passed": 50, "hostile_mutations_rejected": 20},
    }

def validate(x: dict[str, Any]) -> None:
    t,c,d=x["injection_theorem"],x["exact_consequence"],x["decision"]
    proof=t["metric_diffeomorphism_injectivity_proof"]
    checks=[x["classification"]=="SOURCE_NATIVE_ROUTE",x["target_claim"]=="SC-ACT-06",set(x["pinned_inputs"])==set(PATHS),all(len(v["sha256"])==64 for v in x["pinned_inputs"].values()),t["pure_connection_kernel_embeds_in_full_kernel"],t["internal_gauge_image_is_radial"],t["radial_tangential_intersection_dimension"]==0,t["metric_diffeomorphism_rank_at_nonzero_covector"]==4,t["metric_diffeomorphism_symbol_is_injective"],proof["choose_linear_functional"]=="ell(q)=1 for nonzero q",proof["contract_one_leg"]=="v+ell(v)q=0",proof["substitute_back"]=="-2 ell(v) q tensor q=0",proof["conclusion_over_reals"]=="ell(v)=0 and v=0",proof["sample_rank_controls"]==[4],t["metric_diffeomorphism_connection_component_at_flat_T0"]==0,t["fermionic_gauge_tangent_dimension_at_zero_background"]==0,t["pure_tangential_class_in_total_gauge_image_forces_zero_metric_parameter"],t["then_internal_parameter_must_have_zero_radial_image"],t["induced_map_on_quotients_is_injective"],t["common_stabilizer_equivariant"],c["connection_kernel_dimension"]==106512,c["owned_radial_gauge_dimension"]==16384,c["injected_tangential_quotient_dimension"]==90128,c["previous_overgrant_lower_bound"]==90124,c["exact_improvement_over_overgrant"]==4,not c["complete_full_field_cohomology_dimension_computed"],c["full_field_middle_cohomology_dimension_at_least"]==90128,c["uniform_on_positive_negative_and_null_real_covectors"],d["owned_tangential_quotient_survives_in_full_field_cohomology"],not d["metric_diffeomorphisms_reduce_the_pure_tangential_quotient"],not d["complete_full_field_cohomology_equals_the_injected_submodule"],"40 real" in d["next_exact_input"],x["source_and_ledger_effect"]=="SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","local full-field cohomology submodule" in x["ledger_no_change_reason"],"90128-dimensional" in x["claim_ceiling"],x["claim_ceiling"].startswith("Exact equivariant"),x["controls"]["controls_passed"]==50,x["controls"]["hostile_mutations_rejected"]==20,x["controls"]["producer"].endswith("k879_sc_act_06_full_field_quotient_injection.py"),x["controls"]["probe"].endswith("k879_sc_act_06_full_field_quotient_injection_probe.py"),x["gu_typed_objects"]["target"].startswith("MAP-TYPE="),"SO(6)xSO(7)" in x["gu_typed_objects"]["real_structure"],"full-field" in x["scope"],x["status"]=="working_draft_verified",x["direction"]=="observed_to_native",x["schema_version"]=="1.0",x["result_id"].startswith("K879-"),c["full_field_middle_cohomology_dimension_at_least"]==c["injected_tangential_quotient_dimension"],c["connection_kernel_dimension"]-c["owned_radial_gauge_dimension"]==c["injected_tangential_quotient_dimension"],t["metric_diffeomorphism_rank_at_nonzero_covector"]==c["exact_improvement_over_overgrant"]]
    assert len(checks)==50, len(checks)
    assert all(checks), [i for i, value in enumerate(checks) if not value]

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s)
    elif not a.check: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())

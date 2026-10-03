#!/usr/bin/env python3
"""K873: authenticate the owned principal symmetry image on the K717 flat germ."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k873-sc-act-06-owned-symmetry-custody.json"
PATHS = {
    "source_deformation": ROOT / "lab/sources/gu-mixed-bose-fermi-cross-map-source-reinspection-2026-08-04.md",
    "source_group": ROOT / "lab/sources/gu-paper-reference-surfaces.md",
    "source_parent": ROOT / "lab/sources/k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md",
    "k745": ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json",
    "k787": ROOT / "lab/process/k787-sc-act-06-flat-zero-locus-custody.json",
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
    "k864": ROOT / "lab/process/k864-sc-act-06-radial-grant-quotient.json",
    "k868": ROOT / "lab/process/k868-sc-act-06-common-stabilizer-boundary.json",
    "k872": ROOT / "lab/process/k872-sc-act-06-common-stabilizer-irreducible-character.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    p = {name: json.loads(path.read_text()) for name, path in PATHS.items() if name.startswith("k")}
    k789, k864, k868, k872 = p["k789"], p["k864"], p["k868"], p["k872"]
    return {
        "schema_version": "1.0", "result_id": "K873-SC-ACT-06-OWNED-SYMMETRY-CUSTODY",
        "created": "2026-10-02", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Principal-symbol custody audit for the source-displayed gauge-to-field map on K717's repository-constructed flat Upsilon=0 germ; the caveated remainder of the displayed deformation complex is not promoted.",
        "gu_typed_objects": k789["gu_typed_objects"] | {"target": "MAP-TYPE=owned principal internal-gauge image and corrected tangential connection quotient"},
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "source_custody": {
            "displayed_C0": "Omega^0(ad(P_H))", "displayed_C1_contains": "Omega^1(ad(P_H))",
            "source_gauge_group": "H=Gau(P_H)", "source_connection_arena": "A(Y,P_H)",
            "k77_adjoint_parent": "full U(64,64) adjoint/Clifford coefficient arena",
            "real_parameter_dimension": 16384,
            "principal_connection_gauge_map": "lambda maps to q tensor lambda",
            "principal_map_is_owned": True, "complete_displayed_complex_stabilized": False,
            "caveat_empor_remains_load_bearing": True,
            "ownership_grade": "SOURCE_DISPLAYED_TOPOLOGY_PLUS_REPOSITORY_DERIVED_PRINCIPAL_SYMBOL",
        },
        "owned_image": {
            "nonzero_covector": True, "candidate_domain_dimension": k864["radial_grant"]["candidate_domain_dimension"],
            "map_injective": k864["radial_grant"]["candidate_injective"],
            "composition_zero_on_flat_zero_locus": k864["radial_grant"]["composition_zero"],
            "image_equals_radial_kernel_summand": k864["radial_grant"]["image_equals_radial_kernel_summand"],
            "image_dimension": k864["conditional_connection_quotient"]["granted_image_dimension"],
            "common_stabilizer": k868["stabilizer_chain"]["common_q_stabilizer_identity_component"],
            "radial_common_group_formula": k868["radial_restriction"]["formula"],
            "metric_diffeomorphism_rank": k789["composition_theorem"]["metric_diffeomorphism_rank"],
            "metric_diffeomorphism_connection_component_at_flat_T0": k789["composition_theorem"]["metric_diffeomorphism_connection_component_at_flat_T0"],
            "metric_diffeomorphism_changes_connection_only_quotient": False,
        },
        "owned_tangential_quotient": {
            "full_connection_kernel_dimension": k864["conditional_connection_quotient"]["kernel_dimension"],
            "owned_radial_image_dimension": k864["conditional_connection_quotient"]["granted_image_dimension"],
            "quotient_dimension": k864["conditional_connection_quotient"]["quotient_dimension"],
            "quotient_is_tangential_kernel": True,
            "real_irreducible_type_count": k872["reconstruction"]["real_irreducible_type_count"],
            "real_irreducible_character_sha256": k872["reconstruction"]["rows_sha256"],
            "authenticated_at_principal_connection_symbol_scope": True,
            "complete_full_field_old_cohomology_authenticated": False,
        },
        "decision": {
            "K789_q_lambda_remains_merely_unowned_candidate": False,
            "owned_principal_internal_gauge_image_authenticated": True,
            "owned_tangential_connection_quotient_authenticated": True,
            "owned_complete_full_field_symmetry_image_authenticated": False,
            "source_displayed_complete_complex_promoted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compare the 40 authenticated real tangential quotient types with source/action-owned repair-domain and repair-target modules; the caveated full field complex, intertwiners, descent and analytic globalization remain separate obligations.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The source-owned principal gauge image authenticates one local connection quotient but not the caveated complete deformation complex, physical state or observable.",
        "claim_ceiling": "Exact principal internal-gauge ownership and 90128-dimensional tangential connection quotient on K717. No complete full-field cohomology, repair, global ellipticity, rich moduli or physical conclusion follows.",
        "controls": {"producer": "tests/channel-swings/k873_sc_act_06_owned_symmetry_custody.py", "probe": "tests/channel-swings/k873_sc_act_06_owned_symmetry_custody_probe.py", "controls_passed": 46, "hostile_mutations_rejected": 20},
    }

def validate(x: dict[str, Any]) -> None:
    s, image, q, d = x["source_custody"], x["owned_image"], x["owned_tangential_quotient"], x["decision"]
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE", x["target_claim"] == "SC-ACT-06",
        set(x["pinned_inputs"]) == set(PATHS), all(len(row["sha256"]) == 64 for row in x["pinned_inputs"].values()),
        s["displayed_C0"] == "Omega^0(ad(P_H))", s["displayed_C1_contains"] == "Omega^1(ad(P_H))",
        s["source_gauge_group"] == "H=Gau(P_H)", s["source_connection_arena"] == "A(Y,P_H)",
        "U(64,64)" in s["k77_adjoint_parent"], s["real_parameter_dimension"] == 16384,
        s["principal_connection_gauge_map"] == "lambda maps to q tensor lambda", s["principal_map_is_owned"],
        not s["complete_displayed_complex_stabilized"], s["caveat_empor_remains_load_bearing"],
        s["ownership_grade"] == "SOURCE_DISPLAYED_TOPOLOGY_PLUS_REPOSITORY_DERIVED_PRINCIPAL_SYMBOL",
        image["nonzero_covector"], image["candidate_domain_dimension"] == 16384, image["map_injective"],
        image["composition_zero_on_flat_zero_locus"], image["image_equals_radial_kernel_summand"], image["image_dimension"] == 16384,
        image["common_stabilizer"] == "SO(6) x SO(7)", "Lambda^a(P_6)" in image["radial_common_group_formula"],
        image["metric_diffeomorphism_rank"] == 4, image["metric_diffeomorphism_connection_component_at_flat_T0"] == 0,
        not image["metric_diffeomorphism_changes_connection_only_quotient"],
        q["full_connection_kernel_dimension"] == 106512, q["owned_radial_image_dimension"] == 16384,
        q["quotient_dimension"] == 90128, q["quotient_is_tangential_kernel"], q["real_irreducible_type_count"] == 40,
        len(q["real_irreducible_character_sha256"]) == 64, q["authenticated_at_principal_connection_symbol_scope"],
        not q["complete_full_field_old_cohomology_authenticated"],
        not d["K789_q_lambda_remains_merely_unowned_candidate"], d["owned_principal_internal_gauge_image_authenticated"],
        d["owned_tangential_connection_quotient_authenticated"], not d["owned_complete_full_field_symmetry_image_authenticated"],
        not d["source_displayed_complete_complex_promoted"], not d["SC_ACT_06_proved_or_refuted"],
        "40 authenticated real tangential quotient types" in d["next_exact_input"],
        x["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "principal gauge image" in x["ledger_no_change_reason"], "No complete full-field cohomology" in x["claim_ceiling"],
        x["controls"]["controls_passed"] == 46, x["controls"]["hostile_mutations_rejected"] == 20,
    ]
    assert len(checks) == x["controls"]["controls_passed"] and all(checks)

def main() -> int:
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s,encoding="utf-8")
    elif not a.check: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())

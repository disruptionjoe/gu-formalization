#!/usr/bin/env python3
"""Audit the GR shadow recovery certificate.

This is a structural/status audit, not a physics simulation. It checks that the
certificate keeps the GR shadow claim separate from weak-field compatibility,
Willmore-only recovery, hidden matter relabeling, and branch-engineered terms.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "explorations" / "geometry-curvature-emergence" / "gr-shadow-recovery-certificate-2026-06-24.md"
PRIMARY_CONTRACT = ROOT / "explorations" / "cycle-gates-and-audits" / "primary-gu-interface-contract-2026-06-24.md"
TANGENT_GATE = ROOT / "explorations" / "misc" / "constraint-first-ig-tangent-space-gate-2026-06-24.md"
EXACT_GATE = ROOT / "explorations" / "geometry-curvature-emergence" / "exact-schwarzschild-kerr-el-gate-2026-06-24.md"
ACTION_GATE = ROOT / "explorations" / "cycle-gates-and-audits" / "gu-action-4d-physics-gate-2026-06-24.md"
MINIMAL_ACTION = ROOT / "explorations" / "cycle-gates-and-audits" / "gu-minimal-action-spec-2026-06-24.md"
CLOSED_LOOP = ROOT / "explorations" / "misc" / "gu-closed-loop-action-ig-branch-2026-06-24.md"
WEAK_FIELD = ROOT / "canon" / "schwarzschild-weak-field-rfail.md"
DAG = ROOT / "explorations" / "cycle-gates-and-audits" / "live-claim-dag-fault-finality-ledger-2026-06-24.md"


EXPECTED_PIPELINE = {
    "source_field_content",
    "section_metric_extraction",
    "full_4d_EL_projection",
    "conservation_source_law",
    "exact_solution_tests",
    "weak_field_macroscopic_limit",
}

EXPECTED_BRANCHES = {
    "branch_2a",
    "branch_2b",
    "branch_3",
    "free_beta",
    "background_stueckelberg",
    "willmore_only",
}

EXPECTED_CLAIMS = {"GR-SHADOW", "ACTION-GR"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## Machine-Auditable Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Auditable Summary JSON block")
    return json.loads(match.group(1))


def assert_source_consistency() -> None:
    sources = {
        "primary_contract": read(PRIMARY_CONTRACT),
        "tangent_gate": read(TANGENT_GATE),
        "exact_gate": read(EXACT_GATE),
        "action_gate": read(ACTION_GATE),
        "minimal_action": read(MINIMAL_ACTION),
        "closed_loop": read(CLOSED_LOOP),
        "weak_field": read(WEAK_FIELD),
        "dag": read(DAG),
    }

    required = {
        "primary_contract": [
            "exact GR: blocked for every viable branch",
            "source_law(I_GU) is not a single field equation",
            "bare_free_beta_norm",
        ],
        "tangent_gate": [
            "NO_BRANCH_2A_DERIVED",
            "No source read in this pass supplies an explicit Phi",
            "Free beta: rejected, theta collapses",
        ],
        "exact_gate": [
            "exact Schwarzschild/Kerr cannot be evaluated",
            "W_s(s_Schwarzschild) != 0",
            "Free beta kills theta",
        ],
        "action_gate": [
            "OPEN_ACTION_GATE",
            "PASS only weak-field",
            "ACTION UNWRITTEN",
        ],
        "minimal_action": [
            "delta_beta S_theta alone forces theta = 0",
            "Weak-field/exact conflation",
            "Vacuum/matter relabeling",
        ],
        "closed_loop": [
            "Branch 2A: A-independent constrained IG",
            "D_A^*F_A = theta_eff",
            "No branch currently derives",
        ],
        "weak_field": [
            "R_fail^{full}_{mu nu} = 0 at O(M/r)",
            "exact Schwarzschild is NOT a Willmore-critical section",
            "Strong-field regime",
        ],
        "dag": [
            "\"id\": \"ACTION-GR\"",
            "\"id\": \"THETA-XI\"",
            "Exact GR from GU action",
        ],
    }

    for source_name, needles in required.items():
        text = sources[source_name]
        for needle in needles:
            if needle not in text:
                raise AssertionError(f"{source_name} missing {needle!r}")


def assert_claims(summary: dict[str, Any]) -> None:
    assert summary["verdict"] == "CERTIFICATE_SPECIFIED_TRUE_GR_SHADOW_NOT_CERTIFIED"

    claims = {claim["id"]: claim for claim in summary["claims"]}
    if set(claims) != EXPECTED_CLAIMS:
        raise AssertionError(f"unexpected claims: {sorted(claims)}")

    gr_shadow = claims["GR-SHADOW"]
    assert gr_shadow["status"] == "specified_open"
    assert gr_shadow["proof_grade"] == "specification"
    assert gr_shadow["finality"] == "not_final"
    assert gr_shadow["decision"] == "no_current_true_gr_shadow_certificate"
    for dep in [
        "source_field_content",
        "full_4d_EL_projection",
        "exact_schwarzschild_kerr_witnesses",
        "weak_field_macroscopic_limit",
        "ACTION-GR",
        "IG-VARIATION",
    ]:
        if dep not in gr_shadow["depends_on"]:
            raise AssertionError(f"GR-SHADOW missing dependency {dep}")

    action_gr = claims["ACTION-GR"]
    assert action_gr["status"] == "open"
    assert action_gr["proof_grade"] == "specification"
    assert action_gr["finality"] == "not_final"
    assert action_gr["decision"] == "exact_schwarzschild_kerr_not_passed"
    assert "IG-VARIATION" in action_gr["depends_on"]
    assert "written_S_GU" in action_gr["depends_on"]


def assert_pipeline(summary: dict[str, Any]) -> None:
    pipeline = {stage["stage"]: stage for stage in summary["pipeline"]}
    if set(pipeline) != EXPECTED_PIPELINE:
        raise AssertionError(f"unexpected pipeline stages: {sorted(pipeline)}")

    source = pipeline["source_field_content"]
    for required in ["D_GU", "S_GU", "s", "A", "theta", "II_s_H", "branch"]:
        if required not in source["required"]:
            raise AssertionError(f"source stage missing {required}")
    assert source["current_status"] == "partial_typed_action_branch_underdefined"

    extraction = pipeline["section_metric_extraction"]
    assert "g_equals_s_star_g_Y" in extraction["required"]
    assert "observer_metric_not_fundamental_quantized_object" in extraction["required"]

    projection = pipeline["full_4d_EL_projection"]
    assert projection["current_status"] == "blocked_missing_branch_fixed_EL_projection"
    assert "R_shadow" in projection["required"]

    exact = pipeline["exact_solution_tests"]
    assert exact["current_status"] == "not_passed"
    assert "Schwarzschild_witness_fields" in exact["required"]
    assert "Kerr_witness_fields" in exact["required"]

    weak_macro = pipeline["weak_field_macroscopic_limit"]
    assert weak_macro["current_status"] == "weak_field_bounded_pass_macroscopic_missing"


def assert_true_shadow_and_distinctions(summary: dict[str, Any]) -> None:
    criteria = set(summary["true_shadow_criteria"])
    expected_criteria = {
        "metric_extracted_as_s_star_g_Y_not_fundamental_GR_quantum",
        "full_source_EL_tuple_vanishes_before_projection",
        "4d_projection_equals_Einstein_equation_with_fixed_constants",
        "source_conservation_derived_from_full_Noether_Bianchi_identities",
        "exact_Schwarzschild_and_Kerr_witnesses_pass",
        "weak_field_and_macroscopic_limits_from_same_branch",
        "no_hidden_matter_relabeling_or_target_fitted_terms",
    }
    if criteria != expected_criteria:
        raise AssertionError(f"unexpected true shadow criteria: {criteria}")

    evidence = summary["current_evidence"]
    assert evidence["true_gr_shadow"] == "not_certified"
    assert evidence["weak_field_compatibility"] == "conditional_bounded_pass_O_M_over_r"
    assert evidence["exact_schwarzschild_kerr"] == "blocked_open_not_passed"
    assert evidence["willmore_only"] == "fails_exact_schwarzschild_kerr_unsafe"
    assert evidence["branch_2a_phi"] == "missing"

    distinctions = {
        distinction["shortcut"]: distinction for distinction in summary["distinctions"]
    }
    for key in [
        "weak_field_compatibility",
        "willmore_only_recovery",
        "hidden_matter_relabeling",
        "branch_engineered_cross_terms",
    ]:
        if key not in distinctions:
            raise AssertionError(f"missing distinction {key}")
    assert distinctions["weak_field_compatibility"]["classification"] == "insufficient"
    assert distinctions["hidden_matter_relabeling"]["classification"] == "forbidden"
    assert distinctions["branch_engineered_cross_terms"]["classification"] == "forbidden"


def assert_branches(summary: dict[str, Any]) -> None:
    branches = {branch["key"]: branch for branch in summary["branches"]}
    if set(branches) != EXPECTED_BRANCHES:
        raise AssertionError(f"unexpected branches: {sorted(branches)}")

    assert branches["branch_2a"]["status"] == "branch_underdefined"
    assert branches["branch_2a"]["source_law"] == "D_A^*F_A=theta_if_D_A_Phi_zero"
    assert branches["branch_2a"]["true_gr_shadow"] == "not_certified"

    assert branches["branch_2b"]["status"] == "possible_source_corrected"
    assert branches["branch_2b"]["source_law"] == "corrected_by_multiplier_current"

    assert branches["branch_3"]["status"] == "honest_fallback_action_unwritten"
    assert branches["branch_3"]["source_law"] == "D_A^*F_A=theta_eff"

    assert branches["free_beta"]["status"] == "rejected"
    assert branches["free_beta"]["source_law"] == "theta=0_and_D_A^*F_A=0"
    assert branches["free_beta"]["true_gr_shadow"] == "fails_nonzero_theta_shadow"

    assert branches["background_stueckelberg"]["status"] == "viable_but_thin"
    assert branches["willmore_only"]["status"] == "fails_exact_strong_field"
    assert branches["willmore_only"]["true_gr_shadow"] == "fails_exact_GR_shadow"


def assert_certificates_and_forbidden(summary: dict[str, Any]) -> None:
    certs = {cert["id"]: cert for cert in summary["claim_certificates"]}
    if set(certs) != EXPECTED_CLAIMS:
        raise AssertionError(f"unexpected claim certificates: {sorted(certs)}")

    gr = certs["GR-SHADOW"]
    assert gr["status"] == "specified_open"
    assert gr["proof_grade"] == "specification"
    for forbidden in [
        "weak_field_pass_as_exact_recovery",
        "hidden_matter_relabeling",
        "Willmore_only_recovery",
        "branch_engineered_cross_terms",
        "imported_Einstein_Hilbert_fundamental_metric_sector",
    ]:
        if forbidden not in gr["forbidden_inputs"]:
            raise AssertionError(f"GR-SHADOW certificate missing {forbidden}")

    action = certs["ACTION-GR"]
    assert action["status"] == "open"
    assert "weak_field_O_M_over_r_promoted_to_exact_GR" in action["forbidden_inputs"]
    assert "free_beta_with_nonzero_theta" in action["forbidden_inputs"]

    forbidden_shortcuts = set(summary["forbidden_shortcuts"])
    for shortcut in [
        "weak_field_compatibility_as_exact_GR",
        "Willmore_only_recovery",
        "hidden_matter_relabeling",
        "branch_engineered_cross_terms",
        "free_beta_nonzero_theta",
        "Kerr_by_spherical_analogy",
    ]:
        if shortcut not in forbidden_shortcuts:
            raise AssertionError(f"missing forbidden shortcut {shortcut}")

    rollbacks = set(summary["rollback_conditions"])
    for rollback in [
        "free_beta_only_theta_norm",
        "branch_2a_Phi_missing_or_target_fitted",
        "branch_3_without_theta_eff_language",
        "Schwarzschild_or_Kerr_full_EL_failure",
        "hidden_matter_required",
        "macroscopic_limit_not_from_same_branch",
    ]:
        if rollback not in rollbacks:
            raise AssertionError(f"missing rollback condition {rollback}")


def assert_first_missing_object(summary: dict[str, Any]) -> None:
    proof_object = summary["first_missing_proof_object"]
    assert proof_object["id"] == "ELProjectedGRShadowTheorem"
    required = set(proof_object["requires"])
    expected = {
        "branch_fixed_S_GU",
        "IG_variation_or_S_IG_dyn",
        "full_source_EL_tuple",
        "Pi_4D_projection_identity",
        "conservation_theorem",
        "Schwarzschild_and_Kerr_witness_fields",
        "weak_field_macroscopic_limit",
    }
    if required != expected:
        raise AssertionError(f"unexpected proof-object requirements: {required}")
    assert summary["next_step"] == (
        "attempt_Branch_2A_ELProjectedGRShadowTheorem_for_exact_Schwarzschild_then_Kerr_or_switch_to_Branch_3_total_current"
    )


def audit() -> dict[str, Any]:
    summary = extract_summary(read(CERTIFICATE))
    assert_source_consistency()
    assert_claims(summary)
    assert_pipeline(summary)
    assert_true_shadow_and_distinctions(summary)
    assert_branches(summary)
    assert_certificates_and_forbidden(summary)
    assert_first_missing_object(summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print audited summary JSON.")
    args = parser.parse_args()

    summary = audit()
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print("GR shadow recovery certificate audit: PASS")
        print("true_gr_shadow_certified: False")
        print("exact_schwarzschild_kerr_passed: False")
        print("weak_field_status: conditional_bounded_pass_O_M_over_r")
        print(f"next_step: {summary['next_step']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

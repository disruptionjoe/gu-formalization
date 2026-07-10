#!/usr/bin/env python3
"""Audit the metric / marble prematurity gate.

This is a structural gate audit, not a physics proof. It checks that the
artifact keeps metric-as-shadow conditional, includes the requested extraction
obligations, covers exact Schwarzschild/Kerr, requires covariance/invariance
and causality/locality, and forbids claims that the metric shadow is already
proved.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "cycle-gates-and-audits" / "metric-marble-prematurity-gate-2026-06-24.md"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What \"Marble Is Premature\" Means And Does Not Mean",
    "## 3. Required Metric-Shadow Extraction Gate",
    "## 4. Failure Modes",
    "## 5. Branch Robustness And Rollback Table",
    "## 6. Claim Certificate Table",
    "## 7. First Exact Missing Proof Object",
    "## 8. Machine-Readable Summary",
    "## 9. Next Meaningful Proof/Computation Step",
]

EXPECTED_STAGES = {
    "source_object",
    "section_map",
    "induced_metric",
    "variation_space",
    "projected_einstein_tensor",
    "covariance_invariance",
    "causality_locality",
    "boundary_data",
    "exact_solutions",
}

EXPECTED_FAILURE_MODES = {
    "metric_imported",
    "EH_inserted_as_rescue",
    "bare_Lambda_counted_as_marble",
    "weak_field_promoted_to_exact",
    "hidden_matter_relabeling",
    "causality_loss",
    "covariance_invariance_loss",
    "target_fitted_branch",
}

EXPECTED_BRANCHES = {
    "source_geometry_primary",
    "branch_2a_constrained_ig",
    "branch_2b_constrained_ig",
    "branch_3_dynamical_ig",
    "background_stueckelberg",
    "operator_spine_only",
    "willmore_only",
    "bare_free_beta_theta_norm",
}

EXPECTED_CLAIMS = {
    "MARBLE-PREMATURITY",
    "METRIC-AS-SHADOW",
    "PROJECTED-EINSTEIN-TENSOR",
    "LAMBDA-PATCH",
    "GR-RECOVERY",
    "MARBLE-AND-WOOD-SHADOWS",
    "CAUSAL-LOCAL-SHADOW",
}

FORBIDDEN_PROVEN_PHRASES = [
    "metric-as-shadow is proved",
    "metric-as-shadow is proven",
    "metric shadow is proved",
    "metric shadow is proven",
    "metric-as-shadow is certified",
    "metric shadow is certified",
]


def load_text(path: Path = DOC) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing metric/marble gate: {path}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Summary JSON block")
    return json.loads(match.group(1))


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def audit_text(text: str, errors: list[str]) -> None:
    for heading in EXPECTED_HEADINGS:
        require(heading in text, f"missing heading {heading}", errors)

    lowered = text.lower()
    for needle in [
        "einstein's marble/wood complaint",
        "metric/geometric marble",
        "LambdaDarkEnergyProvenanceCertificate".lower(),
        "phenomenological stress-energy",
        "source geometry",
        "observer-facing shadows",
        "metric-as-shadow",
        "shadow",
        "extraction",
        "exact schwarzschild",
        "kerr",
        "covariance",
        "invariance",
        "causality",
        "locality",
        "rollback",
    ]:
        require(needle in lowered, f"text missing sentinel {needle!r}", errors)

    for phrase in FORBIDDEN_PROVEN_PHRASES:
        require(phrase not in lowered, f"forbidden overclaim phrase present: {phrase}", errors)

    require(
        "it does not mean the current repo has proved metric-as-shadow. it has not."
        in lowered,
        "missing explicit not-proven disclaimer",
        errors,
    )


def audit_summary(summary: dict[str, Any], errors: list[str]) -> None:
    require(
        summary.get("artifact") == "METRIC_MARBLE_PREMATURITY_GATE",
        "artifact id mismatch",
        errors,
    )
    require(
        summary.get("verdict")
        == "GATE_SPECIFIED_METRIC_AS_SHADOW_CONDITIONAL_NOT_CERTIFIED",
        "verdict mismatch",
        errors,
    )
    require(summary.get("metric_shadow_proven") is False, "metric_shadow_proven must be false", errors)
    require(
        summary.get("current_status") == "specified_open_not_final",
        "current status must remain specified_open_not_final",
        errors,
    )

    stages = {stage.get("stage"): stage for stage in summary.get("required_gate_stages", [])}
    require(set(stages) == EXPECTED_STAGES, f"gate stages mismatch: {sorted(stages)}", errors)
    for stage_name, stage in stages.items():
        required = stage.get("required")
        require(isinstance(required, list) and len(required) >= 4, f"{stage_name} has weak required list", errors)
        require(stage.get("current_status") not in {"closed", "proved", "proven"}, f"{stage_name} overclosed", errors)

    require(
        "g_equals_s_star_g_Y" in stages["induced_metric"]["required"],
        "induced metric stage missing g=s*g_Y sentinel",
        errors,
    )
    require(
        "G_plus_Lambda_minus_kappa_T_minus_R_shadow"
        in stages["projected_einstein_tensor"]["required"],
        "projected Einstein tensor stage missing projection form",
        errors,
    )
    require(
        "Lambda_eff_zero_imported_control_or_source_derived"
        in stages["projected_einstein_tensor"]["required"],
        "projected Einstein tensor stage missing Lambda provenance status",
        errors,
    )
    require(
        "exact_Schwarzschild_witness" in stages["exact_solutions"]["required"],
        "exact solutions stage missing Schwarzschild witness",
        errors,
    )
    require(
        "exact_Kerr_witness" in stages["exact_solutions"]["required"],
        "exact solutions stage missing Kerr witness",
        errors,
    )

    failure_modes = {mode.get("id"): mode for mode in summary.get("failure_modes", [])}
    require(
        set(failure_modes) == EXPECTED_FAILURE_MODES,
        f"failure modes mismatch: {sorted(failure_modes)}",
        errors,
    )
    for mode_name, mode in failure_modes.items():
        require(mode.get("decision"), f"{mode_name} missing decision", errors)
        require(mode.get("rollback"), f"{mode_name} missing rollback", errors)

    branches = {branch.get("id"): branch for branch in summary.get("branches", [])}
    require(set(branches) == EXPECTED_BRANCHES, f"branches mismatch: {sorted(branches)}", errors)
    require(
        branches["willmore_only"]["metric_shadow_status"] == "branch_fail_for_exact_GR",
        "willmore_only must stay exact-GR branch failure",
        errors,
    )
    require(
        branches["bare_free_beta_theta_norm"]["metric_shadow_status"]
        == "rejected_for_nonzero_theta",
        "bare free beta branch must reject nonzero theta",
        errors,
    )

    claims = {claim.get("id"): claim for claim in summary.get("claim_certificates", [])}
    require(set(claims) == EXPECTED_CLAIMS, f"claim certificates mismatch: {sorted(claims)}", errors)
    for claim_id, claim in claims.items():
        require(claim.get("status") not in {"closed", "proved", "proven", "certified"}, f"{claim_id} overclosed", errors)
        require(isinstance(claim.get("forbidden_inputs"), list) and claim["forbidden_inputs"], f"{claim_id} missing forbidden inputs", errors)
        require(claim.get("rollback_condition"), f"{claim_id} missing rollback condition", errors)

    require(claims["METRIC-AS-SHADOW"]["status"] == "not_certified", "metric-as-shadow must be not_certified", errors)
    require(claims["GR-RECOVERY"]["status"] == "still_owed", "GR recovery must stay owed", errors)

    forbidden_claims = set(summary.get("forbidden_claims", []))
    for forbidden in [
        "metric_shadow_already_proven",
        "GU_solves_marble_wood_problem",
        "weak_field_Schwarzschild_proves_metric_shadow",
        "Einstein_Hilbert_rescue_counts_as_shadow",
        "hidden_matter_counts_as_vacuum_GR",
        "emergent_metric_weakens_causality",
    ]:
        require(forbidden in forbidden_claims, f"missing forbidden claim {forbidden}", errors)

    rollbacks = set(summary.get("rollback_conditions", []))
    for rollback in [
        "metric_imported",
        "Einstein_Hilbert_inserted_as_rescue",
        "weak_field_promoted_to_exact",
        "hidden_matter_required",
        "covariance_or_invariance_loss",
        "causality_or_locality_loss",
        "Schwarzschild_or_Kerr_full_EL_failure",
    ]:
        require(rollback in rollbacks, f"missing rollback condition {rollback}", errors)

    proof_object = summary.get("first_missing_proof_object", {})
    require(
        proof_object.get("id") == "MetricShadowExtractionTheorem",
        "first missing proof object must be MetricShadowExtractionTheorem",
        errors,
    )
    require(
        proof_object.get("child_blocker") == "ELProjectedGRShadowTheorem",
        "missing ELProjectedGRShadowTheorem child blocker",
        errors,
    )
    for required in [
        "Pi_4D_projection_identity",
        "covariance_invariance_conservation",
        "causality_locality_theorem",
        "Schwarzschild_and_Kerr_witness_fields",
    ]:
        require(required in proof_object.get("requires", []), f"proof object missing {required}", errors)


def audit(path: Path = DOC) -> dict[str, Any]:
    text = load_text(path)
    summary = extract_summary(text)
    errors: list[str] = []
    audit_text(text, errors)
    audit_summary(summary, errors)
    if errors:
        raise AssertionError("\n".join(errors))
    return summary


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DOC
    try:
        summary = audit(path)
    except Exception as exc:  # noqa: BLE001 - audit CLI should report all failures plainly.
        print("metric/marble prematurity audit: FAIL")
        print(exc)
        return 1

    print("metric/marble prematurity audit: PASS")
    print(f"metric_shadow_proven: {summary['metric_shadow_proven']}")
    print(f"required_gate_stages: {len(summary['required_gate_stages'])}")
    print(f"failure_modes: {len(summary['failure_modes'])}")
    print(f"next_step: {summary['next_step']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

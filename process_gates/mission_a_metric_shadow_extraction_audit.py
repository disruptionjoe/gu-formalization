#!/usr/bin/env python3
"""Audit the Mission A exact Schwarzschild metric-shadow extraction attempt.

This is a structural audit, not a physics proof. It checks that the artifact
contains the requested theorem target, focuses on exact Schwarzschild, handles
the Branch 2A/Branch 3 fork, gives a constructive next object, states rollback
conditions, and does not claim exact GR recovery.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "geometry-curvature-emergence" / "mission-a-metric-shadow-extraction-schwarzschild-2026-06-24.md"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. If GU Is Correct, What Metric-Shadow Object Must Exist Here",
    "## 3. Branch 2A Construction Attempt",
    "## 4. Branch 3 Fallback Construction",
    "## 5. Exact Schwarzschild Witness Packet",
    "## 6. First Exact Obstruction Or Missing Proof Object",
    "## 7. Constructive Next Object",
    "## 8. Claim Certificate Table And Machine-Readable Summary",
]

EXPECTED_CLAIMS = {
    "SCHWARZSCHILD-METRIC-SHADOW-EXTRACTION",
    "BRANCH-2A-SCHWARZSCHILD",
    "BRANCH-3-TOTAL-CURRENT",
    "WEAK-FIELD-SCHWARZSCHILD",
    "EXACT-GR-RECOVERY",
}

FORBIDDEN_POSITIVE_RECOVERY_PATTERNS = [
    r"\bexact GR is recovered\b",
    r"\bexact GR has been recovered\b",
    r"\bGU recovers exact GR\b",
    r"\bexact Schwarzschild metric shadow is proved\b",
    r"\bexact Schwarzschild metric shadow has been proved\b",
    r"\bBranch 2A is accepted\b",
]


def read(path: Path = DOC) -> str:
    return path.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Claim Certificate Table And Machine-Readable Summary\s*.*?```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable summary JSON block")
    return json.loads(match.group(1))


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def audit_text(text: str, errors: list[str]) -> None:
    for heading in EXPECTED_HEADINGS:
        require(heading in text, f"missing heading {heading}", errors)

    lowered = text.lower()
    for needle in [
        "metricshadowextractiontheorem",
        "exact schwarzschild",
        "branch 2a",
        "branch 3",
        "constructive next object",
        "rollback",
        "theta_eff",
        "phi(epsilon,beta,s)",
        "s_m^* g_y = g_schwarzschild",
    ]:
        require(needle in lowered, f"missing required sentinel {needle!r}", errors)

    for pattern in FORBIDDEN_POSITIVE_RECOVERY_PATTERNS:
        require(
            re.search(pattern, text, flags=re.IGNORECASE) is None,
            f"forbidden exact-recovery overclaim pattern present: {pattern}",
            errors,
        )


def audit_summary(summary: dict[str, Any], errors: list[str]) -> None:
    require(
        summary.get("artifact") == "MISSION_A_METRIC_SHADOW_EXTRACTION_SCHWARZSCHILD",
        "artifact id mismatch",
        errors,
    )
    require(summary.get("theorem_target") == "MetricShadowExtractionTheorem", "missing theorem target", errors)
    require(summary.get("exact_target") == "exact_Schwarzschild", "exact target mismatch", errors)
    require(summary.get("exact_gr_recovered") is False, "exact_gr_recovered must be false", errors)
    require(
        summary.get("metric_shadow_extraction_proved") is False,
        "metric_shadow_extraction_proved must be false",
        errors,
    )

    branch_2a = summary.get("branch_2a", {})
    require(branch_2a.get("status") == "conditional_template_only", "Branch 2A status mismatch", errors)
    require(branch_2a.get("can_be_used_now") is False, "Branch 2A must not be usable now", errors)
    for required in [
        "primary_or_geometric_origin",
        "A_independent_D_A_Phi_zero",
        "gauge_covariant",
        "proper_beta_tangent_K_beta",
        "anti_smuggling",
    ]:
        require(required in branch_2a.get("requirements", []), f"Branch 2A missing {required}", errors)

    sources = {item.get("candidate"): item.get("status") for item in branch_2a.get("available_sources", [])}
    require(sources.get("fixed_reference_tau_plus") == "speculative_not_derived", "tau-plus status mismatch", errors)
    require(sources.get("dynamic_tau_plus_d_A") == "branch_2b_not_2a", "dynamic tau-plus must be 2B", errors)
    require(
        sources.get("exact_schwarzschild_matching_filter") == "forbidden_target_fitting",
        "exact Schwarzschild matching filter must be forbidden",
        errors,
    )

    branch_3 = summary.get("branch_3", {})
    require(branch_3.get("status") == "required_constructive_fallback", "Branch 3 status mismatch", errors)
    require(branch_3.get("required_object") == "S_IG_dyn_total_current", "Branch 3 missing total-current object", errors)
    require(branch_3.get("source_law") == "D_A^*F_A=theta_eff", "Branch 3 source law mismatch", errors)
    require(branch_3.get("conservation_target") == "D_A^*theta_eff=0", "Branch 3 conservation target mismatch", errors)

    packet = summary.get("schwarzschild_witness_packet", {})
    require(packet.get("status") == "specified_not_filled", "witness packet status mismatch", errors)
    for equation in [
        "s_M_star_g_Y_equals_g_Schwarzschild",
        "E_A_equals_0",
        "E_s_equals_0",
        "R_shadow_equals_0",
    ]:
        require(equation in packet.get("required_equations", []), f"witness packet missing {equation}", errors)
    require("Branch_2A_Phi" in packet.get("currently_missing", []), "packet must mark Branch 2A Phi missing", errors)
    require("Branch_3_S_IG_dyn" in packet.get("currently_missing", []), "packet must mark Branch 3 S_IG_dyn missing", errors)

    missing = summary.get("first_missing_proof_object", {})
    require(missing.get("id") == "SchwarzschildMetricShadowExtractionTheorem", "missing proof object id mismatch", errors)
    require(missing.get("parent") == "MetricShadowExtractionTheorem", "missing parent theorem", errors)
    require(missing.get("branch_2a_blocker") == "Phi_not_sourced", "Branch 2A blocker mismatch", errors)
    require(
        missing.get("branch_3_blocker") == "S_IG_dyn_total_current_not_written",
        "Branch 3 blocker mismatch",
        errors,
    )

    next_object = summary.get("constructive_next_object", {})
    require(
        next_object.get("id") == "TauSliceOrBranch3SchwarzschildSourcePacket",
        "constructive next object mismatch",
        errors,
    )
    require(next_object.get("kerr_deferred") is True, "Kerr should be deferred", errors)

    claims = {claim.get("id"): claim for claim in summary.get("claim_certificates", [])}
    require(set(claims) == EXPECTED_CLAIMS, f"claim set mismatch: {sorted(claims)}", errors)
    require(claims["EXACT-GR-RECOVERY"]["status"] == "not_claimed", "exact GR recovery must be not_claimed", errors)
    require(
        claims["BRANCH-2A-SCHWARZSCHILD"]["status"] == "conditional_template_only",
        "Branch 2A claim status mismatch",
        errors,
    )
    require(
        claims["BRANCH-3-TOTAL-CURRENT"]["status"] == "required_fallback",
        "Branch 3 claim status mismatch",
        errors,
    )

    rollbacks = set(summary.get("rollback_conditions", []))
    for rollback in [
        "Branch_2A_without_Phi",
        "Phi_A_dependent_so_Branch_2B",
        "Branch_3_without_theta_eff",
        "S_IG_dyn_absent",
        "hidden_matter_or_Q_TF_relabeling_required",
        "weak_field_promoted_to_exact",
        "R_shadow_nonzero_in_vacuum",
    ]:
        require(rollback in rollbacks, f"missing rollback condition {rollback}", errors)

    forbidden = set(summary.get("forbidden_claims", []))
    for claim in [
        "exact_GR_recovered",
        "exact_Schwarzschild_metric_shadow_proved",
        "Branch_2A_accepted_without_Phi",
        "bare_theta_conserved_in_Branch_3",
        "weak_field_pass_is_exact_black_hole_recovery",
    ]:
        require(claim in forbidden, f"missing forbidden claim {claim}", errors)


def audit(path: Path = DOC) -> dict[str, Any]:
    text = read(path)
    summary = extract_summary(text)
    errors: list[str] = []
    audit_text(text, errors)
    audit_summary(summary, errors)
    if errors:
        raise AssertionError("\n".join(errors))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DOC)
    parser.add_argument("--json", action="store_true", help="Print audited summary JSON.")
    args = parser.parse_args()

    try:
        summary = audit(args.path)
    except Exception as exc:  # noqa: BLE001 - audit CLI should report failures plainly.
        print("Mission A metric-shadow extraction audit: FAIL")
        print(exc)
        return 1

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print("Mission A metric-shadow extraction audit: PASS")
        print("theorem_target: MetricShadowExtractionTheorem")
        print("exact_target: exact_Schwarzschild")
        print("exact_gr_recovered: False")
        print(f"next_step: {summary['next_step']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

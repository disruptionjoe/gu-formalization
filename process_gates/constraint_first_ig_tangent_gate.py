"""Audit the constraint-first IG tangent-space gate.

This is not a physics simulation. It checks that the tangent-space no-go note keeps
the branch consequences synchronized with the action/IG, exact-GR, FLRW, and live-DAG
source documents:

* no current candidate is promoted to a derived Branch 2A constraint;
* free beta remains rejected because it collapses theta;
* A-dependent constraints report a corrected source law;
* no branch passes exact Schwarzschild/Kerr or generates negative xi_eff;
* forbidden target-success inputs remain forbidden.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "explorations" / "misc" / "constraint-first-ig-tangent-space-gate-2026-06-24.md"
GOAL = ROOT / "explorations" / "cycle-gates-and-audits" / "goal-draft-ig-constraint-derivation-2026-06-24.md"
IG_DYNAMICS = ROOT / "explorations" / "misc" / "ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
CLOSED_LOOP = ROOT / "explorations" / "misc" / "gu-closed-loop-action-ig-branch-2026-06-24.md"
EXACT_GR = ROOT / "explorations" / "geometry-curvature-emergence" / "exact-schwarzschild-kerr-el-gate-2026-06-24.md"
FLRW = ROOT / "explorations" / "dark-energy-cosmology" / "flrw-theta-xi-branch-reduction-2026-06-24.md"
DAG = ROOT / "explorations" / "cycle-gates-and-audits" / "live-claim-dag-fault-finality-ledger-2026-06-24.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_summary(note_text: str) -> dict[str, Any]:
    match = re.search(
        r"## Machine-Auditable Summary.*?```json\s*(\{.*?\})\s*```",
        note_text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Auditable Summary JSON block")
    return json.loads(match.group(1))


def assert_source_consistency() -> None:
    sources = {
        "goal": read(GOAL),
        "ig_dynamics": read(IG_DYNAMICS),
        "closed_loop": read(CLOSED_LOOP),
        "exact_gr": read(EXACT_GR),
        "flrw": read(FLRW),
        "dag": read(DAG),
    }

    required = {
        "goal": [
            "Branch 2A is not accepted until Phi(eps,beta,s)=0",
            "D_A Phi = 0",
            "invented only to avoid `theta=0` is not evidence",
        ],
        "ig_dynamics": [
            "E_beta = c_theta Ad(eps) theta = 0",
            "If the allowed `beta` variations are all of `Omega^1(Y,ad P)`",
            "Phi = D_A^* theta = 0",
        ],
        "closed_loop": [
            "Branch 2A: A-independent constrained IG",
            "No branch currently derives",
            "xi_eff < -0.319",
            "theta = 0",
        ],
        "exact_gr": [
            "exact Schwarzschild/Kerr cannot be evaluated",
            "D_A Phi = 0 for true Branch 2A",
            "Free beta kills theta",
        ],
        "flrw": [
            "NO_NEGATIVE_XI_GENERATED",
            "xi_eff = C_Rtheta / Z_theta",
            "bare free-beta branch:  theta mode absent",
        ],
        "dag": [
            "\"id\": \"IG-VARIATION\"",
            "\"id\": \"ACTION-GR\"",
            "\"id\": \"THETA-XI\"",
            "free beta plus only `|theta|^2` kills theta",
        ],
    }

    for source_name, needles in required.items():
        text = sources[source_name]
        for needle in needles:
            if needle not in text:
                raise AssertionError(f"{source_name} missing {needle!r}")


def assert_tangent_theorem(summary: dict[str, Any]) -> None:
    assert summary["verdict"] == "NO_BRANCH_2A_DERIVED"

    theorem = summary["tangent_theorem"]
    assert theorem["beta_space"] == "Omega^1(Y,ad P)"
    assert theorem["collapse_condition"] == "K_beta = Omega^1(Y,ad P)"
    assert theorem["current_repo_has_natural_branch_2a_phi"] is False

    requirements = set(theorem["branch_2a_requires"])
    expected_requirements = {
        "gauge_covariant_Phi",
        "D_A_Phi_equals_0",
        "proper_beta_tangent",
        "primary_or_geometric_origin",
        "no_target_success_inputs",
    }
    if requirements != expected_requirements:
        raise AssertionError(f"unexpected Branch 2A requirements: {requirements}")


def assert_forbidden_inputs(summary: dict[str, Any]) -> None:
    forbidden = set(summary["forbidden_target_success_inputs"])
    expected = {
        "Schwarzschild/Kerr exact solution",
        "weak-field O(M/r) as exact GR",
        "Q^TF(B_s) relabeled as vacuum matter",
        "xi_eff < -0.319",
        "xi ~= -0.6",
        "bare R theta^2",
        "bare Lambda",
        "unspecified S_IG-dyn",
    }
    if forbidden != expected:
        raise AssertionError(f"unexpected forbidden inputs: {forbidden}")


def assert_candidates(summary: dict[str, Any]) -> None:
    candidates = {candidate["key"]: candidate for candidate in summary["candidates"]}
    expected_keys = {
        "no_constraint_full_ig",
        "background_or_fixed_stueckelberg",
        "a_independent_geometric_graph",
        "tau_plus_graph",
        "projector_admissible_subbundle",
        "section_pullback_codazzi",
        "divergence_constraint",
        "flrw_scalar_xi_filter",
        "exact_gr_matching_constraint",
        "dynamical_ig_total_current",
    }
    if set(candidates) != expected_keys:
        raise AssertionError(f"unexpected candidate keys: {sorted(candidates)}")

    forbidden_positive_statuses = {
        "pass",
        "pass_2a",
        "branch_2a_derived",
        "exact_gr_pass",
        "negative_xi_generated",
    }
    for candidate in candidates.values():
        if candidate["status"] in forbidden_positive_statuses:
            raise AssertionError(f"unexpected positive candidate: {candidate}")

    assert candidates["no_constraint_full_ig"]["status"] == "fail_theta_collapse"
    assert candidates["no_constraint_full_ig"]["tangent"] == "K_beta_full"

    assert candidates["a_independent_geometric_graph"]["status"] == (
        "template_not_instantiated"
    )
    assert candidates["a_independent_geometric_graph"]["source_law"] == (
        "bare_theta_source_preserved_if_D_A_Phi_zero"
    )

    assert candidates["tau_plus_graph"]["status"] == "underdetermined_or_2b"
    assert candidates["tau_plus_graph"]["source_law"] == (
        "bare_if_fixed_reference_corrected_if_dynamic_A"
    )

    assert candidates["section_pullback_codazzi"]["status"] == (
        "reduction_identity_not_branch_2a_constraint"
    )
    assert candidates["section_pullback_codazzi"]["source_law"] == (
        "corrected_if_written_on_theta"
    )

    assert candidates["divergence_constraint"]["status"] == "branch_2b_source_corrected"
    assert candidates["divergence_constraint"]["source_law"] == (
        "corrected_by_multiplier_current"
    )

    assert candidates["flrw_scalar_xi_filter"]["status"] == "anti_smuggling_fail"
    assert candidates["exact_gr_matching_constraint"]["status"] == "anti_smuggling_fail"

    assert candidates["dynamical_ig_total_current"]["source_law"] == (
        "D_A^*F_A=theta_eff"
    )


def assert_branches(summary: dict[str, Any]) -> None:
    branches = {branch["key"]: branch for branch in summary["branches"]}
    expected_keys = {
        "constrained_ig_a_independent",
        "constrained_ig_a_dependent",
        "dynamical_ig_total_current",
        "bare_free_beta_norm",
    }
    if set(branches) != expected_keys:
        raise AssertionError(f"unexpected branch keys: {sorted(branches)}")

    assert branches["constrained_ig_a_independent"]["status"] == "branch_underdefined"
    assert branches["constrained_ig_a_independent"]["exact_gr"] == "not_passed"
    assert branches["constrained_ig_a_independent"]["theta_xi"] == "not_generated"

    assert branches["constrained_ig_a_dependent"]["source_law"] == (
        "corrected_by_multiplier_current"
    )
    assert branches["constrained_ig_a_dependent"]["exact_gr"] == "not_passed"
    assert branches["constrained_ig_a_dependent"]["theta_xi"] == "not_generated"

    assert branches["dynamical_ig_total_current"]["status"] == "honest_fallback"
    assert branches["dynamical_ig_total_current"]["source_law"] == (
        "D_A^*F_A=theta_eff"
    )
    assert branches["dynamical_ig_total_current"]["exact_gr"] == "not_passed"
    assert branches["dynamical_ig_total_current"]["theta_xi"] == "not_generated"

    assert branches["bare_free_beta_norm"]["status"] == "rejected"
    assert branches["bare_free_beta_norm"]["nonzero_theta"] == "fails_theta_equals_zero"
    assert branches["bare_free_beta_norm"]["source_law"] == "D_A^*F_A=0"
    assert branches["bare_free_beta_norm"]["theta_xi"] == "theta_scalar_absent"


def assert_claim_certificates(summary: dict[str, Any]) -> None:
    certificates = {
        certificate["id"]: certificate for certificate in summary["claim_certificates"]
    }
    if set(certificates) != {"ACTION-GR", "THETA-XI"}:
        raise AssertionError(f"unexpected certificates: {sorted(certificates)}")

    action = certificates["ACTION-GR"]
    assert action["status"] == "open"
    assert action["proof_grade"] == "specification"
    assert action["finality"] == "not_final"
    assert action["decision"] == "no_exact_GR_pass"
    assert "IG-VARIATION" in action["depends_on"]

    theta_xi = certificates["THETA-XI"]
    assert theta_xi["status"] == "open"
    assert theta_xi["proof_grade"] == "conditional_reconstruction"
    assert theta_xi["finality"] == "not_final"
    assert theta_xi["decision"] == "no_generated_negative_xi"
    assert "canonical_scalar_reduction" in theta_xi["depends_on"]


def audit() -> dict[str, Any]:
    note_text = read(NOTE)
    summary = extract_summary(note_text)
    assert_source_consistency()
    assert_tangent_theorem(summary)
    assert_forbidden_inputs(summary)
    assert_candidates(summary)
    assert_branches(summary)
    assert_claim_certificates(summary)
    assert summary["next_step"] == "tau_plus_slice_audit_before_exact_GR_or_FLRW"
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print audited summary JSON.")
    args = parser.parse_args()

    summary = audit()
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print("constraint-first IG tangent gate: PASS")
        print("branch_2a_derived: False")
        print("exact_gr_passed: False")
        print("negative_xi_generated: False")
        print("next_step: tau_plus_slice_audit_before_exact_GR_or_FLRW")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

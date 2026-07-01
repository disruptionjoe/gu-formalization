#!/usr/bin/env python3
"""Audit the hourly Cycle 3 loop-convergence calibration artifact.

This is a process/content audit, not a proof of mathematical convergence. It
checks that the artifact defines metrics, reports bounded sample counts,
includes a same-session guard, audits false negatives, and refuses to claim
convergence while the metrics are partial.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle3-loop-convergence-false-negative-calibration-2026-06-24.md"
)

EXPECTED_VERDICT = "UNDER_INSTRUMENTED_WITH_LOCAL_BLOCKER_CONVERGENCE"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Metric Definitions",
    "## 3. Current Sample / Readout From Loop Log And Hourly Cycles",
    "## 4. False-Negative Audit: Were Recent Demotions Warranted?",
    "## 5. Strongest Positive Convergence Finding",
    "## 6. First Exact Obstruction Or Missing Metric",
    "## 7. Impact For Future Automation Runs",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_METRICS = {
    "resolved_gain",
    "blocked_or_underdefined_precision_gain",
    "bounded_no_go_or_negative_selector_gain",
    "open_precision_gain",
    "repeated_blocker_rate",
    "downgrade_upgrade_churn",
    "same_session_circularity_pressure",
    "false_negative_rate",
}

REQUIRED_LEDGER_FIELDS = {
    "item_id",
    "lane_family",
    "session_id",
    "artifact_path",
    "previous_verdict",
    "new_verdict",
    "transition_type",
    "first_missing_object_id",
    "blocker_family",
    "evidence_basis",
    "flag_raised_session_id",
    "flag_closed_session_id",
    "same_session_guard",
    "target_import_guard",
    "audit_path",
}

FORBIDDEN_CONVERGENCE_OVERCLAIMS = [
    r"\bVerdict:\s+CONVERGED\b",
    r"\bthe loop is converged\b",
    r"\bfull convergence is established\b",
    r'"convergence_claimed"\s*:\s*true',
]


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing loop calibration artifact: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class HourlyCycle3LoopConvergenceFalseNegativeCalibrationAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_under_instrumented_and_does_not_claim_convergence(self) -> None:
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(self.summary["classification"], "under_instrumented")
        self.assertIs(self.summary["metrics_partial"], True)
        self.assertIs(self.summary["bounded_sample_only"], True)
        self.assertIs(self.summary["convergence_claimed"], False)
        self.assertIs(self.summary["thrashing_claimed"], False)
        for pattern in FORBIDDEN_CONVERGENCE_OVERCLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden convergence overclaim matched: {pattern}",
            )

    def test_metric_definitions_are_complete(self) -> None:
        definitions = self.summary["metric_definitions"]
        self.assertTrue(REQUIRED_METRICS.issubset(definitions.keys()))
        for metric in REQUIRED_METRICS:
            self.assertIn(metric, self.text)
            self.assertTrue(definitions[metric].strip())

    def test_sample_counts_match_required_sources(self) -> None:
        counts = self.summary["sample_counts"]
        self.assertEqual(counts["adversarial_log_runs"], 2)
        self.assertEqual(counts["adversarial_log_items_completed"], 19)
        self.assertEqual(counts["adversarial_log_issues_total"], 24)
        self.assertEqual(counts["adversarial_log_issues_fixed"], 19)
        self.assertGreaterEqual(counts["hourly_artifacts"], 10)
        self.assertGreaterEqual(counts["cycle3_census_candidates"], 10)

    def test_net_status_gain_keeps_closure_separate_from_blocker_precision(self) -> None:
        gain = self.summary["net_status_gain"]
        self.assertEqual(gain["resolved_gain"], 0)
        self.assertEqual(gain["blocked_or_underdefined_precision_gain"], 9)
        self.assertEqual(gain["bounded_no_go_or_negative_selector_gain"], 1)
        self.assertEqual(gain["open_precision_gain"], 10)
        self.assertIs(gain["net_research_closure_claimed"], False)
        self.assertIn("no sampled central claim was resolved", gain["interpretation"])

    def test_repeated_blocker_rate_is_reported_with_families(self) -> None:
        repeated = self.summary["repeated_blocker_rate"]
        self.assertEqual(
            repeated["hourly_artifact_instances_in_repeated_families"],
            repeated["hourly_artifact_count"],
        )
        self.assertEqual(repeated["rate"], 1.0)
        self.assertGreaterEqual(repeated["family_count"], 5)
        families = {family["family"] for family in repeated["families"]}
        for expected in [
            "qft_source_mode_quotient",
            "rs_physical_quotient_rank",
            "vz_actual_operator_subprincipal",
            "ig_theta_source_forced_selector",
            "phi_obs_fixed_data_target_provenance",
        ]:
            self.assertIn(expected, families)

    def test_downgrade_upgrade_churn_is_not_used_as_convergence(self) -> None:
        churn = self.summary["downgrade_upgrade_churn"]
        self.assertGreaterEqual(churn["explicit_log_downgrade_or_blocked_upgrade_events_lower_bound"], 9)
        self.assertEqual(churn["current_hourly_explicit_upgrades"], 0)
        self.assertEqual(churn["current_hourly_nonpromotion_or_demotion_gates"], 10)
        self.assertEqual(churn["ratio"], "undefined_zero_upgrades")
        self.assertIn("not_observed_upgrade_downgrade_oscillation", churn["interpretation"])

    def test_same_session_guard_is_machine_readable_and_blocks_same_session_closure(self) -> None:
        guard = self.summary["same_session_guard"]
        self.assertIs(guard["guard_required"], True)
        self.assertIs(guard["can_close_same_session_flags"], False)
        self.assertEqual(guard["adversarial_log_runs_with_same_session_pressure"], 2)
        self.assertEqual(guard["adversarial_log_runs"], 2)
        self.assertEqual(guard["same_session_pressure_rate"], 1.0)
        self.assertIs(guard["missing_machine_readable_same_session_field_in_prior_hourlies"], True)
        self.assertEqual(guard["next_required_field"], "same_session_guard")
        self.assertIn("DEFERRED_VERIFICATION", guard["required_decision"])

    def test_false_negative_audit_finds_no_over_deflated_recent_demotions(self) -> None:
        audit = self.summary["false_negative_audit"]
        self.assertEqual(audit["verdict"], "NO_FALSE_NEGATIVE_FOUND_IN_BOUNDED_SAMPLE")
        self.assertIs(audit["recent_demotions_warranted"], True)
        self.assertIs(audit["recent_demotions_over_deflated"], False)
        self.assertEqual(audit["over_deflated_count"], 0)
        self.assertEqual(audit["false_negative_rate"], 0.0)
        self.assertGreaterEqual(audit["audited_demotions_count"], 7)
        self.assertEqual(audit["audited_demotions_count"], len(audit["audited_demotions"]))
        for demotion in audit["audited_demotions"]:
            self.assertIs(demotion["warranted"], True, demotion["id"])
            self.assertTrue(demotion["reason"].strip())

    def test_positive_finding_is_limited_to_blocker_granularity(self) -> None:
        finding = self.summary["strongest_positive_convergence_finding"]
        self.assertIn("all_ten_hourly_artifacts", finding["finding"])
        self.assertEqual(finding["claim_scope"], "blocker_granularity_not_mathematical_closure")
        self.assertGreaterEqual(len(finding["families_with_named_next_objects"]), 5)

    def test_first_exact_missing_metric_is_transition_ledger_with_required_fields(self) -> None:
        missing = self.summary["first_exact_missing_metric_artifact"]
        self.assertEqual(missing["id"], "LOOP_STATE_TRANSITION_LEDGER_V1")
        self.assertEqual(missing["name"], "LoopStateTransitionLedger_v1")
        self.assertIn("prior and new verdict rows", missing["why_missing_first"])
        fields = set(missing["required_fields"])
        self.assertTrue(
            REQUIRED_LEDGER_FIELDS.issubset(fields),
            f"missing ledger fields: {sorted(REQUIRED_LEDGER_FIELDS - fields)}",
        )

    def test_future_automation_impact_keeps_deflation_and_adds_instrumentation(self) -> None:
        impact = self.summary["impact_for_future_automation_runs"]
        self.assertIs(impact["keep_deflation_guard"], True)
        self.assertIs(impact["relax_verdict_policy"], False)
        self.assertIs(impact["add_transition_ledger"], True)
        self.assertIs(impact["require_worker_transition_fields"], True)
        self.assertIn("mathematical_closure", impact["separate_dashboards"])
        self.assertIn("calibration_hygiene", impact["separate_dashboards"])
        status = impact["next_operational_status"]
        self.assertEqual(status["loop_status"], "UNDER_INSTRUMENTED")
        self.assertEqual(status["research_closure_status"], "NOT_YET_CONVERGED")
        self.assertEqual(status["next_required_artifact"], "LoopStateTransitionLedger_v1")


def audit_summary() -> dict[str, Any]:
    text = read_artifact()
    summary = extract_summary(text)
    return {
        "document": str(ARTIFACT.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "classification": summary["classification"],
        "convergence_claimed": summary["convergence_claimed"],
        "false_negative_verdict": summary["false_negative_audit"]["verdict"],
        "next_required_artifact": summary["first_exact_missing_metric_artifact"]["name"],
    }


def main(argv: list[str] | None = None) -> int:
    if argv and "--json" in argv:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle3LoopConvergenceFalseNegativeCalibrationAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

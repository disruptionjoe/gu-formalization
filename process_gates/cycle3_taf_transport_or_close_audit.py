#!/usr/bin/env python3
"""Audit the Cycle 3 TaF transport-or-close gate artifact.

This audit checks the gate contract, not Time-as-Finality itself. It enforces
that the artifact makes a real pursue/park/close/conditional decision, evaluates
multiple transport candidates, separates comparator/null-model language from
GU theorem transport, includes a wake trigger, and avoids claiming that TaF
evades GU no-go theorems.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = REPO_ROOT / "explorations" / "cycle3-taf-transport-or-close-gate-2026-06-24.md"

ALLOWED_VERDICTS = {"pursue", "park", "close", "conditional"}

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Candidate Transport Objects Evaluated",
    "## 3. Any Actual GU Theorem Impact Found",
    "## 4. Structural Parallels/Null-Models That Should Remain Exploration-Only",
    "## 5. Close/Park/Pursue Decision And Wake Trigger",
    "## 6. First Exact Obstruction",
    "## 7. Impact For GU Measurement/Observer Lanes",
    "## 8. Next Meaningful Step If Any",
    "## 9. Machine-Readable JSON Summary",
]

FORBIDDEN_NO_GO_EVASION_PATTERNS = [
    r"\b(?:TAF|TaF|Time as Finality)\s+(?:evades|bypasses|solves)\b.*\b(?:no-go|no go)\b",
    r"\b(?:no-go|no go)\b.*\b(?:evaded|bypassed|solved)\b.*\b(?:by|via|through)\s+(?:TAF|TaF|Time as Finality)\b",
]


def artifact_text() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"TaF gate artifact is missing: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "CYCLE3_TAF_TRANSPORT_OR_CLOSE_GATE":
            return data
    raise AssertionError("Cycle 3 TaF transport gate JSON summary not found")


class Cycle3TaFTransportOrCloseAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_allowed_and_machine_readable(self) -> None:
        verdict = self.summary["verdict"]
        self.assertIn(verdict, ALLOWED_VERDICTS)
        self.assertRegex(
            self.text,
            r"(?im)^Verdict:\s+\*\*(pursue|park|close|conditional)\*\*\.",
        )

    def test_at_least_three_transport_candidates_are_evaluated(self) -> None:
        candidates = self.summary["candidate_transport_objects_evaluated"]
        self.assertIsInstance(candidates, list)
        self.assertGreaterEqual(len(candidates), 3)
        for candidate in candidates:
            for key in ("candidate_id", "object", "status", "gu_theorem_impact", "first_obstruction"):
                self.assertIn(key, candidate)
                self.assertTrue(candidate[key])
        candidate_rows = re.findall(r"(?m)^\|\s*T\d+\s*\|", self.text)
        self.assertGreaterEqual(len(candidate_rows), 3)

    def test_no_claim_that_taf_evades_gu_no_go_theorems(self) -> None:
        self.assertFalse(self.summary["no_go_evasion_claim"])
        for pattern in FORBIDDEN_NO_GO_EVASION_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE | re.DOTALL))
        self.assertIn("Do not cite TAF as bypassing any GU no-go theorem.", self.text)

    def test_comparator_and_null_model_language_is_separated_from_theorem_transport(self) -> None:
        self.assertTrue(self.summary["separation_of_comparator_from_transport"])
        transport = self.summary["theorem_transport"]
        self.assertFalse(transport["found"])
        self.assertIn("required_shape", transport)
        self.assertIn("comparators_null_models", self.summary)
        self.assertGreaterEqual(len(self.summary["comparators_null_models"]), 3)
        self.assertIn("## 4. Structural Parallels/Null-Models That Should Remain Exploration-Only", self.text)
        self.assertIn("## 3. Any Actual GU Theorem Impact Found", self.text)

    def test_wake_trigger_and_json_summary_exist(self) -> None:
        wake = self.summary["wake_trigger"]
        self.assertEqual(wake["name"], "FR3-GU filtered-readout sensitivity fixture")
        self.assertGreaterEqual(len(wake["required_fields"]), 5)
        self.assertEqual(wake["wake_decision_if_satisfied"], "pursue")
        self.assertEqual(wake["decision_if_next_attempt_fails"], "close")
        self.assertIn("Wake trigger:", self.text)
        self.assertIn('"artifact": "CYCLE3_TAF_TRANSPORT_OR_CLOSE_GATE"', self.text)

    def test_current_gate_does_not_change_gu_proof_obligations(self) -> None:
        self.assertFalse(self.summary["transport_found"])
        self.assertFalse(self.summary["taf_changes_gu_proof_obligation"])
        self.assertEqual(self.summary["actual_gu_theorem_impact_found"], "none")
        self.assertEqual(
            self.summary["impact_for_measurement_observer_lanes"]["measurement_gate_changed"],
            False,
        )


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(Cycle3TaFTransportOrCloseAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

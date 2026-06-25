#!/usr/bin/env python3
"""Audit ManuscriptDGU01OperatorSourceCandidate_V1.

The audit enforces the Cycle 2 identity gate: normalized manuscript objects may
be recorded as positive source locators, but none may be accepted as the later
D_GU^epsilon 0/1 target unless source identity is explicit. It also keeps the
principal-symbol and downstream-physics promotions guarded.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle2-manuscript-dgu01-operator-source-identity.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_OBJECTS = {
    "omega",
    "T_omega",
    "B_omega",
    "Shiab_omega",
    "/D_omega",
    "Upsilon_omega",
    "delta_omega",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r'"accepted_receipt_count"\s*:\s*[1-9]',
    r'"passed"\s*:\s*true',
    r'"principal_symbol_computation_allowed"\s*:\s*true',
    r'"principal_symbol_claimed"\s*:\s*true',
    r'"proof_restart_allowed"\s*:\s*true',
    r"VZ evasion:\s*(claimed|established|true)",
    r"dark-energy recovery:\s*(claimed|established|true)",
    r"FLRW proof status:\s*(improved|closed|true)",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ManuscriptDGU01OperatorSourceIdentityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_scope(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ManuscriptDGU01OperatorSourceCandidate_V1",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["source_pdf"],
            "Geometric_UnityDraftApril1st2021.pdf",
        )
        self.assertEqual(
            self.summary["target_object"],
            "D_GU^epsilon 0/1 typed target",
        )
        self.assertEqual(
            self.summary["focused_pdf_pages"],
            [41, 42, 43, 44, 45, 46, 47, 48, 55, 56, 57, 58],
        )

    def test_normalized_source_objects_are_complete_and_unaccepted(self) -> None:
        rows = {row["name"]: row for row in self.summary["normalized_source_objects"]}
        self.assertEqual(set(rows), REQUIRED_OBJECTS)
        for name, row in rows.items():
            self.assertTrue(row["normalized_form"], name)
            self.assertTrue(row["pdf_pages"], name)
            self.assertIn(row["object_kind"], {
                "field_packet",
                "field_or_input_term",
                "connection_data",
                "algebraic_source_operator_family",
                "differential_operator",
                "EL_object",
                "deformation_operator",
            })
            self.assertFalse(row["identical_to_D_GU_epsilon_0_1"], name)
            self.assertFalse(row["explicitly_defines_D_GU_epsilon_0_1"], name)
            self.assertIn(row["acceptance_status"], {"quarantined", "rejected"})

    def test_identity_gate_blocks_acceptance(self) -> None:
        gate = self.summary["identity_gate"]
        self.assertFalse(gate["passed"])
        self.assertFalse(gate["source_emits_D_GU_epsilon_token"])
        self.assertFalse(gate["source_defines_target_0_1_domain_codomain"])
        self.assertFalse(gate["source_equates_any_normalized_object_to_target"])
        self.assertIn("SourceEstablishedIdentity", gate["required_identity"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(
            self.summary["candidate_status"],
            "quarantined_positive_source_locator",
        )

    def test_principal_symbol_guard_is_closed_before_identity(self) -> None:
        guard = self.summary["principal_symbol_guard"]
        self.assertFalse(guard["principal_symbol_computation_allowed"])
        self.assertFalse(guard["principal_symbol_claimed"])
        self.assertIn("identity gate failed", guard["reason"])
        self.assertIn(
            "compute_principal_symbol_only_after_identity_gate_passes",
            self.summary["next_meaningful_step"],
        )

    def test_target_import_flags_and_forbidden_promotions(self) -> None:
        for key, value in self.summary["target_import_flags"].items():
            self.assertIs(value, False, key)
        for key, value in self.summary["forbidden_promotions"].items():
            self.assertIs(value, False, key)

    def test_no_vz_dark_energy_flrw_or_proof_promotion_patterns(self) -> None:
        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive promotion matched: {pattern}",
            )

    def test_constructive_next_object_requires_identity_packet(self) -> None:
        self.assertEqual(
            self.summary["constructive_next_object"],
            "DGU01ManuscriptIdentityPacket_V1",
        )
        required = set(self.summary["constructive_next_object_requires"])
        self.assertIn("source_side_equality_definition_or_derivation", required)
        self.assertIn("principal_symbol_eligibility_after_identity_gate", required)
        self.assertIn("target_import_flags_all_false", required)


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
"""Audit RenderedCriticalDisplayTranscriptionPacket_DGU01_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
)

EXPECTED_PAGES = [43, 44, 45, 46, 47, 48, 55, 56, 57, 58]
EXPECTED_SHA256 = "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4"
EXPECTED_ROWS = {
    "DGU01-TR-01": {"9.1"},
    "DGU01-TR-02": {"9.2", "9.3"},
    "DGU01-TR-03": {"9.4", "9.5", "9.6"},
    "DGU01-TR-04": {"9.7", "9.8", "9.9", "9.10", "9.11", "9.12", "9.13", "9.14", "9.15"},
    "DGU01-TR-05": {"9.16", "9.17", "9.18", "9.19", "9.20"},
    "DGU01-TR-06": {"9.21", "9.22", "10.1", "10.2", "10.3"},
    "DGU01-TR-07": {"10.4", "10.5", "10.6", "10.7", "10.8", "10.9"},
    "DGU01-TR-08": {"12.2", "12.3"},
    "DGU01-TR-09": {"12.4", "12.5", "12.6", "12.7"},
    "DGU01-TR-10": {"12.8", "12.9", "12.10"},
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary block")
    return json.loads(match.group(1))


class RenderedDGU01IdentityTranscriptionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.text = DOC.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise AssertionError(f"missing artifact: {DOC}") from exc
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "RenderedCriticalDisplayTranscriptionPacket_DGU01_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0301")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0301_cycle3_rendered_dgu01_identity_transcription_audit.py",
        )

    def test_source_pdf_and_page_window(self) -> None:
        source = self.summary["source_pdf"]
        self.assertEqual(source["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(source["sha256"], EXPECTED_SHA256)
        self.assertEqual(source["page_count"], 69)
        self.assertEqual(self.summary["focused_pdf_pages"], EXPECTED_PAGES)

    def test_transcription_method_includes_rendered_manual_inspection(self) -> None:
        methods = self.summary["methods"]
        self.assertEqual(methods["text_extraction"]["tool"], "PyMuPDF get_text('text')")
        for token in ["D_GU", "DGU", "D GU", "D_GU^epsilon", "DGU01"]:
            self.assertIn(token, methods["text_extraction"]["full_pdf_tokens_absent"])
            self.assertIn(token, methods["text_extraction"]["checked_page_tokens_absent"])
        rendered = methods["rendered_manual_inspection"]
        self.assertIs(rendered["performed"], True)
        self.assertIn("visual/manual inspection", rendered["tool"])
        self.assertEqual(rendered["render_storage"], "temporary_outside_repo")
        self.assertEqual(set(rendered["render_hashes"]), {str(page) for page in EXPECTED_PAGES})

    def test_pages_and_equations_are_covered(self) -> None:
        rows = {row["row_id"]: row for row in self.summary["normalized_display_rows"]}
        self.assertEqual(set(rows), set(EXPECTED_ROWS))
        covered_pages = sorted({page for row in rows.values() for page in row["pages"]})
        self.assertEqual(covered_pages, EXPECTED_PAGES)
        for row_id, expected_equations in EXPECTED_ROWS.items():
            self.assertEqual(set(rows[row_id]["equations"]), expected_equations)

    def test_required_object_families_are_present(self) -> None:
        rows = self.summary["normalized_display_rows"]
        families = {row["object_family"] for row in rows}
        for family in ["Shiab", "action_EL", "/D_omega", "Upsilon", "delta_omega"]:
            self.assertIn(family, families)
        displays = " ".join(row["normalized_display"] for row in rows)
        for term in ["circledot_e", "/D_omega", "Upsilon_omega", "delta_2^omega", "delta_omega"]:
            self.assertIn(term, displays)

    def test_identity_gate_fails_without_accepting_receipts(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(
            self.summary["candidate_status"],
            "quarantined_positive_action_operator_EL_locator",
        )
        identity = self.summary["identity_gate"]
        self.assertEqual(identity["status"], "scoped_missing")
        self.assertIs(identity["passed"], False)
        self.assertIs(identity["source_emits_D_GU_epsilon_token"], False)
        self.assertIs(identity["source_defines_target_0_1_domain_codomain"], False)
        for key in [
            "source_equates_Shiab_action_EL_to_target",
            "source_equates_slash_D_omega_to_target",
            "source_equates_Upsilon_omega_to_target",
            "source_equates_delta_omega_to_target",
        ]:
            self.assertIs(identity[key], False, key)

    def test_principal_symbol_guard_is_closed(self) -> None:
        guard = self.summary["principal_symbol_guard"]
        self.assertEqual(guard["status"], "closed_before_computation")
        self.assertIs(guard["principal_symbol_computation_allowed"], False)
        self.assertIs(guard["principal_symbol_claimed"], False)
        self.assertIn("identity gate failed", guard["reason"])

    def test_status_decision_has_no_accepted_rows(self) -> None:
        decision = self.summary["status_decision"]
        self.assertEqual(decision["accepted"], [])
        self.assertIn("SourceEstablishedIdentity_to_D_GU_epsilon_0_1", decision["scoped_missing"])
        self.assertGreaterEqual(len(decision["quarantined"]), 8)
        rows = self.summary["normalized_display_rows"]
        for row in rows:
            self.assertIs(row["accepted_as_D_GU_epsilon_0_1"], False)

    def test_target_import_flags_and_forbidden_promotions(self) -> None:
        for key, value in self.summary["target_import_flags"].items():
            self.assertIs(value, False, key)
        forbidden = self.summary["forbidden_promotions"]
        for key in [
            "DGU_actual_operator_identified",
            "principal_symbol_emitted_or_computed",
            "VZ_evasion_established",
            "dark_energy_recovery_established",
            "DESI_agreement_established",
            "FLRW_proof_status_improved",
            "proof_restart_allowed",
        ]:
            self.assertIn(key, forbidden)
            self.assertIs(forbidden[key], False, key)

    def test_next_object_keeps_symbol_work_after_identity(self) -> None:
        self.assertEqual(
            self.summary["constructive_next_object"],
            "DGU01SourceEstablishedIdentityPacket_V1",
        )
        self.assertIn("otherwise emit NegativePrimarySourceReceiptInstance_V1", self.summary["next_meaningful_step"])
        self.assertIn("Do not compute a principal symbol next", self.text)


if __name__ == "__main__":
    unittest.main()

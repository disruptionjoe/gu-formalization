#!/usr/bin/env python3
"""Audit AuthorManuscriptReceiptAvailabilityPacket_V1.

The audit parses the embedded JSON summary and checks the manuscript/draft
availability decision, four-family blocker coverage, release-metadata rejection
as formula receipt, no claim promotion, and the constructive next acquisition
task.
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
    / "hourly-20260625-0203-cycle1-author-manuscript-receipt-availability.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Candidate Receipt Rows",
    "## 4. Strongest Positive Result",
    "## 5. First Exact Obstruction Or Missing Object",
    "## 6. Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 7. GU Claim Impact And Forbidden Promotions",
    "## 8. Next Meaningful Source-Mining Or Proof Step",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_OBJECTS = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}

REQUIRED_NO_PROMOTIONS = {
    "IG_K_IG_selected",
    "RS_d_RS_minus_1_source_derived",
    "QFT_P_fin_b_supplied",
    "DGU_actual_operator_identified",
    "VZ_evasion_closed",
    "dark_energy_or_FLRW_recovered",
    "QFT_state_or_CHSH_recovered",
    "physical_rank_or_generation_readout",
    "release_page_contains_formula_receipt",
    "draft_release_page_promotes_family_restart",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing manuscript availability packet: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class AuthorManuscriptReceiptAvailabilityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = {
            row["family"]: row for row in cls.summary["candidate_receipt_rows"]  # type: ignore[index]
        }

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptReceiptAvailabilityPacket_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_LOCAL_OR_INDEXED_AUTHOR_MANUSCRIPT_RECEIPTS",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle1-author-manuscript-receipt-availability.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle1_author_manuscript_receipt_availability_audit.py",
        )

    def test_manuscript_draft_availability_decision(self) -> None:
        decision = self.summary["manuscript_draft_availability_decision"]
        self.assertEqual(decision["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertIs(decision["local_author_manuscript_or_draft_present"], False)
        self.assertIs(decision["indexed_author_manuscript_locator_present"], False)
        self.assertIs(decision["official_release_metadata_present"], True)
        self.assertEqual(
            decision["release_page_classification"],
            "official_site_chronology_not_manuscript_receipt",
        )
        self.assertIs(decision["draft_itself_required_for_claim_extraction"], True)
        self.assertEqual(decision["decision"], "missing")

    def test_all_four_family_blockers_considered(self) -> None:
        self.assertEqual(set(self.summary["families_considered"]), REQUIRED_FAMILIES)
        self.assertEqual(self.summary["required_objects_considered"], REQUIRED_OBJECTS)
        self.assertEqual(set(self.rows), REQUIRED_FAMILIES)
        for family, required_object in REQUIRED_OBJECTS.items():
            row = self.rows[family]
            self.assertEqual(row["required_object"], required_object)
            self.assertEqual(row["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
            self.assertEqual(row["restart_gate"], "blocked")

    def test_official_release_metadata_not_accepted_as_formula_receipt(self) -> None:
        surface_rows = {
            row["source_id"]: row
            for row in self.summary["source_surface_classification"]  # type: ignore[index]
        }
        release = surface_rows["GU-MEDIA-2021-DRAFT-RELEASE"]
        self.assertEqual(release["source_kind_available_now"], "official_site_page")
        self.assertIs(release["accepted_as_formula_receipt"], False)
        self.assertIs(release["accepted_as_manuscript_receipt"], False)
        self.assertEqual(release["accepted_use"], "chronology_and_pointer_only")
        self.assertIn("locator", release["reason"])

        for family, row in self.rows.items():
            self.assertEqual(row["source_kind"], "official_site_page", family)
            self.assertEqual(row["emitted_object_type"], "none", family)
            self.assertIn("none supplied", row["emitted_formula_or_rule"], family)
            self.assertEqual(row["import_status"], "rejected", family)
            self.assertEqual(row["acceptance_status"], "rejected", family)

    def test_no_claim_promotion(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("No GU claim is promoted.", self.text)
        self.assertIn("The release page remains official-site chronology.", self.text)

    def test_next_object_points_to_receipt_map_with_manuscript_task(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertIn("RepoLocalPrimaryGUSourceReceiptMap_V1", obstruction["id"])
        self.assertIs(obstruction["missing"], True)

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RepoLocalPrimaryGUSourceReceiptMap_V1")
        self.assertEqual(next_object["task"], "manuscript_acquisition_and_locator_task")
        self.assertEqual(next_object["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(next_object["entry_type"], "PrimarySourceReceiptInstance_V1")
        self.assertIn("acquire or archive", next_object["next_step"])
        self.assertIn("page section equation or paragraph locators", next_object["next_step"])
        self.assertIn("RepoLocalPrimaryGUSourceReceiptMap_V1", self.summary["next_meaningful_step"])

    def test_forbidden_promotions_include_release_page_and_repo_drafts(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("official release metadata accepted as formula receipt", forbidden)
        self.assertIn("official release metadata accepted as author manuscript content", forbidden)
        self.assertIn("repo-authored reconstruction treated as primary GU manuscript", forbidden)
        self.assertIn("family proof restart from release chronology alone", forbidden)


if __name__ == "__main__":
    unittest.main()

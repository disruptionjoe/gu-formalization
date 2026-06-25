#!/usr/bin/env python3
"""Audit OxfordPortalReceiptMiningPacket_V1.

The audit parses the embedded JSON summary and checks source-surface identity,
four-family coverage, no claim promotion, acceptance discipline, honest
Oxford/Portal classification, and the next-object pointer.
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
    / "hourly-20260625-0203-cycle1-oxford-portal-receipt-mining-packet.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Candidate Receipt Rows",
    "## 4. Strongest Positive Result",
    "## 5. First Exact Obstruction Or Missing Object",
    "## 6. Constructive Next Object",
    "## 7. GU Claim Impact And Forbidden Promotions",
    "## 8. Next Meaningful Source-Mining Or Proof Step",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_SOURCE_SURFACES = {
    "GU-MEDIA-2013-OXFORD",
    "GU-MEDIA-2020-PORTAL-SPECIAL",
}

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
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Oxford/Portal packet: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class OxfordPortalReceiptMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = {
            row["family"]: row
            for row in cls.summary["candidate_receipt_rows"]  # type: ignore[index]
        }

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_source_surface_ids(self) -> None:
        self.assertEqual(self.summary["artifact"], "OxfordPortalReceiptMiningPacket_V1")
        self.assertEqual(self.summary["run"], "hourly-20260625-0203")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(
            set(self.summary["source_surface_ids"]),
            REQUIRED_SOURCE_SURFACES,
        )
        self.assertEqual(
            self.summary["protocol_used"],
            "PrimarySourceReceiptIntakeProtocol_V1",
        )

    def test_oxford_portal_status_is_honest(self) -> None:
        status = self.summary["source_surface_status"]
        self.assertEqual(
            status["GU-MEDIA-2013-OXFORD"]["mathematical_receipt_status"],
            "no_accepted_family_receipt",
        )
        self.assertEqual(
            status["GU-MEDIA-2020-PORTAL-SPECIAL"]["mathematical_receipt_status"],
            "no_accepted_family_receipt",
        )
        honest = self.summary["honest_classification"]
        self.assertEqual(
            honest["oxford_portal_status"],
            "official_source_surface_available_but_family_receipts_missing",
        )
        self.assertIs(honest["index_rows_are_receipts"], False)
        self.assertIs(honest["claim_mining_rows_are_mathematical_receipts"], False)
        self.assertIs(honest["portal_preface_postlecture_locally_mined"], False)
        self.assertIs(honest["transcript_or_locator_gap_blocks_acceptance"], True)

    def test_all_four_family_blockers_are_considered(self) -> None:
        self.assertIs(self.summary["all_four_family_blockers_considered"], True)
        self.assertEqual(set(self.rows), REQUIRED_FAMILIES)
        self.assertEqual(len(self.rows), 4)
        for family, required_object in REQUIRED_OBJECTS.items():
            self.assertEqual(self.rows[family]["required_object"], required_object)
            self.assertEqual(
                set(self.rows[family]["source_id"]),
                REQUIRED_SOURCE_SURFACES,
                family,
            )

    def test_no_claim_promotion(self) -> None:
        self.assertIs(self.summary["not_a_claim_promotion"], True)
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertEqual(self.summary["accepted_receipts"], [])

    def test_no_accepted_receipt_without_exact_locator_and_emitted_object(self) -> None:
        policy = self.summary["accepted_receipt_policy"]
        self.assertIs(policy["requires_exact_locator"], True)
        self.assertIs(policy["requires_emitted_object"], True)
        self.assertIs(policy["requires_emitted_formula_or_rule"], True)
        self.assertIs(policy["current_surface_has_accepted_receipt"], False)

        for family, row in self.rows.items():
            self.assertNotEqual(row["acceptance_status"], "accepted_for_routing", family)
            self.assertEqual(row["acceptance_status"], "quarantined", family)
            self.assertEqual(row["restart_gate"], "blocked", family)
            self.assertEqual(row["emitted_object_type"], "none_supplied", family)
            self.assertIn("none supplied", row["emitted_formula_or_rule"], family)
            self.assertIn("no", row["locator"], family)
            self.assertIn("locator", row["locator"], family)

    def test_next_object_points_to_receipt_map(self) -> None:
        self.assertEqual(
            self.summary["predecessor_missing_object"],
            "RepoLocalPrimaryGUSourceReceiptMap_V1",
        )
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RepoLocalPrimaryGUSourceReceiptMap_V1")
        self.assertEqual(next_object["entry_type"], "PrimarySourceReceiptInstance_V1")
        self.assertEqual(next_object["surface_batch"], "OxfordPortalExactLocatorBatch_V1")
        self.assertIn(
            "RepoLocalPrimaryGUSourceReceiptMap_V1",
            self.summary["next_meaningful_step"],
        )


if __name__ == "__main__":
    unittest.main()

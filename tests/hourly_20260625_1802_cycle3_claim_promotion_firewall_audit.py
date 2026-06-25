"""Audit CLAIM_PROMOTION_FIREWALL_AFTER_1802_C3_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1802-cycle3-claim-promotion-firewall.md"

EXPECTED_ARTIFACT_ID = "CLAIM_PROMOTION_FIREWALL_AFTER_1802_C3_L4_V1"
EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_PATH = "explorations/hourly-20260625-1802-cycle3-claim-promotion-firewall.md"
EXPECTED_AUDIT = "tests/hourly_20260625_1802_cycle3_claim_promotion_firewall_audit.py"

REQUIRED_CLAIM_IDS = {
    "ptuj_formula_packet",
    "keating_identity",
    "ig_selector_theorem",
    "ig_family_identity",
    "dgu_actual_packet",
    "vz_replay",
    "rs_typed_operator",
    "qft_raw_branch_packet",
    "qft_quotient_descent",
    "qft_rho_ab_bell_chsh",
    "major_gu_claim",
    "global_no_go",
}

REQUIRED_SUBSTITUTES = {
    "metadata",
    "partial_transcripts",
    "adjacent_surfaces",
    "transcript_locators",
    "schema_only_packets",
    "scoped_blockers",
}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing claim promotion firewall artifact: {DOC}") from exc


def extract_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("missing YAML frontmatter block")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def extract_json_summary(text: str) -> dict:
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not blocks:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(blocks[-1])


class ClaimPromotionFirewallAfter1802Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_json_summary(cls.text)
        cls.promotion_rows = cls.summary["promotion_rows"]
        cls.rows_by_claim = {row["claim_id"]: row for row in cls.promotion_rows}

    def test_frontmatter_and_json_identity_match_assignment(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.frontmatter["cycle"], "3")
        self.assertEqual(self.frontmatter["lane"], "4")
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["owned_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)

    def test_global_zero_promotion_invariants(self) -> None:
        self.assertEqual(self.summary["promotions_allowed_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["target_import_used"])

    def test_at_least_twelve_promotion_rows_and_required_claims(self) -> None:
        self.assertGreaterEqual(len(self.promotion_rows), 12)
        self.assertEqual(set(self.summary["required_claim_ids"]), REQUIRED_CLAIM_IDS)
        self.assertEqual(set(self.rows_by_claim), REQUIRED_CLAIM_IDS)

    def test_every_row_rejects_promotion_with_missing_object(self) -> None:
        for row in self.promotion_rows:
            with self.subTest(claim_id=row["claim_id"]):
                self.assertFalse(row["promotion_allowed"])
                self.assertTrue(row["forbidden"])
                self.assertIsInstance(row["missing_object"], str)
                self.assertNotEqual(row["missing_object"].strip(), "")
                self.assertIsInstance(row["cycle_1_2_source"], str)
                self.assertNotEqual(row["cycle_1_2_source"].strip(), "")

    def test_forbidden_substitutes_include_required_ids(self) -> None:
        substitutes = {row["id"]: row for row in self.summary["forbidden_substitutes"]}
        self.assertTrue(REQUIRED_SUBSTITUTES.issubset(substitutes))
        for substitute_id in REQUIRED_SUBSTITUTES:
            with self.subTest(substitute_id=substitute_id):
                self.assertFalse(substitutes[substitute_id]["promotion_allowed"])
                self.assertIsInstance(substitutes[substitute_id]["reason"], str)
                self.assertNotEqual(substitutes[substitute_id]["reason"].strip(), "")

    def test_required_claims_are_explicitly_rejected(self) -> None:
        required_fragments = {
            "ptuj_formula_packet": "SingleCompletePTUJBranchReceipt",
            "keating_identity": "formula_visibility",
            "ig_selector_theorem": "ProductBFullD7",
            "ig_family_identity": "FC_IRR",
            "dgu_actual_packet": "SourceEmittedDGU01SectorRule",
            "vz_replay": "same_operator_packet",
            "rs_typed_operator": "UCSDFrameSequence",
            "qft_raw_branch_packet": "QFTSourceDefinedIotaBAndTypedRRawBOReceipt",
            "qft_quotient_descent": "restriction_stability",
            "qft_rho_ab_bell_chsh": "non_imported_finite_extraction",
            "major_gu_claim": "cross_route_proof_object",
            "global_no_go": "class_level_no_go_theorem",
        }
        for claim_id, fragment in required_fragments.items():
            with self.subTest(claim_id=claim_id):
                row = self.rows_by_claim[claim_id]
                self.assertFalse(row["promotion_allowed"])
                self.assertIn(fragment, row["missing_object"])

    def test_text_names_assignment_rejections(self) -> None:
        for phrase in (
            "PTUJ formula packet",
            "Keating identity",
            "IG selector theorem",
            "IG family identity",
            "DGU actual packet",
            "VZ replay",
            "RS typed operator",
            "QFT raw branch packet",
            "quotient/descent",
            "rho_AB/Bell/CHSH",
            "major GU claim",
            "global no-go",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)


if __name__ == "__main__":
    unittest.main()

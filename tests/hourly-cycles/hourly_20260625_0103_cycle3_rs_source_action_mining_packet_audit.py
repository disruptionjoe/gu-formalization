#!/usr/bin/env python3
"""Audit RSSourceActionMiningPacket_V1.

This audit checks that the Cycle 3 RS packet is a decision-grade source-mining
contract, not a source-existence claim or rank/generation promotion.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle3-rs-source-action-mining-packet.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Derivations From Repo Sources",
    "## 3. Strongest Positive Packet",
    "## 4. First Exact Obstruction",
    "## 5. Constructive Next Object",
    "## 6. GU Impact",
    "## 7. Next Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_DIRECT_PATHS = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0103-cycle2-rs-source-action-noether-locator.md",
    "explorations/hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md",
    "sources/media-index.md",
    "sources/media-contributor-tasks-v1.md",
}

REQUIRED_SOURCE_KINDS = {
    "primary_action",
    "Euler_Lagrange_variation",
    "Noether_identity",
    "BRST_theorem",
    "actual_D_GU_operator",
}

REQUIRED_REJECTIONS = {
    "REJECT_NO_PRIMARY_LOCATOR",
    "REJECT_MEDIA_PARAPHRASE_ONLY",
    "REJECT_RECONSTRUCTION_PHRASE_ONLY",
    "REJECT_RAW_SYMBOL_ONLY",
    "REJECT_TYPED_SPINE_ONLY",
    "REJECT_NO_FIELD_PARAMETER_PAIR",
    "REJECT_NO_ACTION_NOETHER_BRST",
    "REJECT_NO_QUOTIENT_SEMANTICS",
    "REJECT_TARGET_INPUT",
    "REJECT_GENERATION_PROMOTION",
}

REQUIRED_EXTRACTION_FIELDS = {
    "source_id",
    "source_locator",
    "primary_source_kind",
    "exact_context",
    "emitted_RS_field",
    "emitted_spinor_parameter",
    "emitted_variation_or_complex",
    "differential_formula",
    "principal_symbol",
    "right_H_structure",
    "gamma_trace_or_RS_constraint",
    "quotient_semantics",
    "finality_semantics",
    "target_quarantine",
}

REQUIRED_FORBIDDEN_INPUTS = {
    "physical_rank_target",
    "H_index_target",
    "rank_3",
    "rank_4",
    "rank_8",
    "three_generations",
    "four_generations",
    "raw_projected_gauge_image_as_physical_loss",
    "target_normalization",
}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bsource action/Noether receipt (is|was|has been) found\b",
    r"\baccepted source receipt now\b",
    r"\bphysical rank is derived\b",
    r"\bH-index is derived\b",
    r"\brank\s*3\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\brank\s*4\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\brank\s*8\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\bthree generations\s+(are|is|have been|has been)\s+derived\b",
    r"\bfour generations\s+(are|is|have been|has been)\s+derived\b",
    r"\braw principal symbol proves d_RS,-1\b",
    r"\bAF4 .* proves d_RS,-1\b",
]


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing RSSourceActionMiningPacket_V1 JSON summary")
    data = json.loads(match.group(1))
    if data.get("artifact") != "RSSourceActionMiningPacket_V1":
        raise AssertionError("wrong artifact JSON summary")
    return data


class RSSourceActionMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_packet_identity_and_non_existence_claim(self) -> None:
        self.assertEqual(self.summary["artifact"], "RSSourceActionMiningPacket_V1")
        self.assertEqual(self.summary["verdict"], "BLOCKED_SOURCE_MINING_PACKET_REQUIRED")
        self.assertEqual(
            self.summary["decision"],
            "ISSUE_PACKET_FOR_PRIMARY_SOURCE_MINING",
        )
        self.assertFalse(self.summary["claims_source_exists"])
        self.assertFalse(self.summary["accepted_source_receipt_now"])

    def test_direct_derivations_cover_required_inputs(self) -> None:
        paths = {row["path"] for row in self.summary["direct_derivations"]}
        self.assertEqual(paths, REQUIRED_DIRECT_PATHS)
        derived_text = " ".join(row["derived"] for row in self.summary["direct_derivations"])
        self.assertIn("compatibility cannot be promoted to derivation", derived_text)
        self.assertIn("RS source action or Noether locator is missing", derived_text)
        self.assertIn("transcript timestamp and exact context", derived_text)

    def test_first_obstruction_is_source_action_or_noether_locator(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["field"], "source_action_or_noether_locator")
        self.assertEqual(obstruction["status"], "MISSING")
        self.assertIn("No accepted source row", obstruction["description"])
        self.assertIn("Noether identity", obstruction["description"])
        self.assertIn("BRST theorem", obstruction["description"])
        self.assertIn("rank_H_index_generation_readout", obstruction["blocks"])

    def test_constructive_next_object_has_source_action_noether_fields(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RS_SOURCE_ACTION_NOETHER_RECEIPT_V1")
        fields = set(next_object["required_fields"])
        for field in [
            "source_locator",
            "primary_source_kind",
            "emitted_RS_field",
            "emitted_spinor_parameter",
            "emitted_variation_or_complex",
            "action_or_operator_object",
            "noether_or_brst_object",
            "right_H_structure",
            "gamma_trace_or_RS_constraint",
            "differential_formula",
            "principal_symbol",
            "quotient_semantics",
            "finality_semantics",
            "rank_generation_quarantine",
        ]:
            self.assertIn(field, fields)

    def test_acceptance_source_kinds_are_primary_and_complete(self) -> None:
        kinds = {row["kind"] for row in self.summary["accepted_primary_source_evidence"]}
        self.assertEqual(kinds, REQUIRED_SOURCE_KINDS)
        requirements = " ".join(
            row["requires"] for row in self.summary["accepted_primary_source_evidence"]
        )
        self.assertIn("delta psi_RS = d_RS,-1 epsilon", requirements)
        self.assertIn("Noether", requirements)
        self.assertIn("BRST", requirements)
        self.assertIn("actual GU operator/action complex", requirements)

    def test_rejection_conditions_are_decision_grade(self) -> None:
        rejections = set(self.summary["rejection_conditions"])
        self.assertEqual(rejections, REQUIRED_REJECTIONS)
        for rejection in REQUIRED_REJECTIONS:
            self.assertIn(rejection, self.text)

    def test_required_extraction_fields_include_source_noether_and_quarantine(self) -> None:
        fields = set(self.summary["required_extraction_fields"])
        self.assertEqual(fields, REQUIRED_EXTRACTION_FIELDS)
        for field in REQUIRED_EXTRACTION_FIELDS:
            self.assertIn(field, self.text)

    def test_source_locator_query_targets_are_specific_and_ordered(self) -> None:
        targets = self.summary["source_locator_query_targets"]
        self.assertEqual([target["priority"] for target in targets], list(range(1, 8)))
        names = {target["source_target"] for target in targets}
        self.assertIn("GU_2021_draft_manuscript", names)
        self.assertIn("GU-MEDIA-2013-OXFORD and GU-MEDIA-2020-PORTAL-SPECIAL", names)
        self.assertIn("GU-POD-2021-JRE-1628", names)
        self.assertIn("GU-POD-2025-TOE-JAIMUNGAL-GU-40", names)
        self.assertIn("GU-POD-2026-JRE-2503", names)

        all_queries = {query for target in targets for query in target["queries"]}
        for query in ["Rarita", "Schwinger", "Noether", "BRST", "gauge", "action"]:
            self.assertIn(query, all_queries)

    def test_rank_generation_quarantine_is_active_and_no_promotions(self) -> None:
        quarantine = self.summary["quarantine"]
        self.assertEqual(quarantine["status"], "ACTIVE")
        self.assertEqual(set(quarantine["forbidden_inputs"]), REQUIRED_FORBIDDEN_INPUTS)

        promotions = quarantine["promotions"]
        for key in [
            "physical_rank_promoted",
            "H_index_promoted",
            "rank_3_promoted",
            "rank_4_promoted",
            "rank_8_promoted",
            "three_generations_promoted",
            "four_generations_promoted",
            "raw_symbol_promoted_to_source",
            "reconstruction_phrase_promoted_to_source",
        ]:
            self.assertIn(key, promotions)
            self.assertFalse(promotions[key])

    def test_candidate_statuses_are_non_accepting_or_quarantined(self) -> None:
        statuses = self.summary["candidate_statuses"]
        self.assertEqual(
            statuses["AF4_nabla_epsilon_phrase"],
            "NON_ACCEPTING_RECONSTRUCTION_CLUE",
        )
        self.assertEqual(
            statuses["epsilon_to_xi_tensor_epsilon_symbol"],
            "NON_ACCEPTING_RAW_SYMBOL_CONTEXT",
        )
        self.assertEqual(
            statuses["typed_D_roll_spine"],
            "NON_ACCEPTING_TYPED_CANDIDATE_UNTIL_SOURCE_CLOSED",
        )
        self.assertEqual(statuses["rank_generation_arithmetic"], "QUARANTINED")

    def test_gu_impact_keeps_branch_open_and_source_blocked(self) -> None:
        impact = self.summary["GU_impact"]
        self.assertFalse(impact["GU_RS_branch_falsified"])
        self.assertEqual(
            impact["current_status"],
            "SOURCE_ORIGIN_BLOCKED_WITH_MINING_PACKET_READY",
        )
        self.assertIn("target-free packet", impact["allowed_claim"])
        self.assertIn("found the source action Noether receipt", impact["forbidden_claim"])
        self.assertEqual(
            impact["rank_generation_claim_status"],
            "QUARANTINED_NOT_DERIVED",
        )

    def test_no_forbidden_promotion_language(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                msg=f"forbidden promotion pattern present: {pattern}",
            )


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Audit the cycle 3 receipt acceptance transition matrix."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle3-receipt-acceptance-transition-matrix.md"
)

EXPECTED_ROWS = {
    ("IG", 1, "AuthorManuscriptIGSelectorIdentityPacket_V1"),
    ("DGU", 1, "ActualDGU01OperatorReceiptCandidateFromAuthorManuscript_V1"),
    ("RS", 1, "AuthorManuscriptRSRuleExtractionCandidate_V1"),
    ("QFT", 1, "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1"),
    ("IG", 2, "IGSelectorRivalEliminatorMatrix_V1"),
    ("DGU", 2, "DGUBosonicTo01SectorIdentityFirewall_V1"),
    ("RS", 2, "RSNegativeReceiptScopeGate_V1"),
    ("QFT", 2, "QFTAlternatePrimarySourceRequirementGate_V1"),
}

REQUIRED_BLOCKERS = {
    "IG": [
        "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
        "family_identity_to_SourceForcedCodomainSelectorForK_IG",
    ],
    "DGU": [
        "missing_bosonic_to_D_GU_epsilon_0_1_sector_identity_rule",
        "domain",
        "codomain",
        "coefficient_packet",
        "principal_symbol",
        "projectors",
        "family_identity",
    ],
    "RS": [
        "missing_stable_RS_only_source_rule_for_d_RS_minus_1_in_checked_manuscript_windows",
        "source_space",
        "target_space",
        "degree_or_slot",
        "field_component",
        "rule_kind",
    ],
    "QFT": [
        "AcceptedPrimarySourceReceiptForQFTPFinB",
        "F_phys_b_O_domain",
        "K_b_target",
        "P_fin_b_or_equivalent_map",
        "primary_source_provenance",
        "local_mode_payload",
    ],
}

EXPECTED_HEADINGS = [
    "## 1. verdict",
    "## 2. source facts",
    "## 3. strongest positive transition attempt",
    "## 4. first obstruction",
    "## 5. impact if closed",
    "## 6. falsification/demotion condition",
    "## 7. next computation",
    "## 8. JSON summary",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing transition matrix artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary block")
    return json.loads(match.group(1))


class ReceiptAcceptanceTransitionMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_required_sections(self) -> None:
        self.assertEqual(
            self.summary["artifact_id"],
            "ReceiptAcceptanceTransitionMatrix_Cycle3_V1",
        )
        self.assertEqual(self.summary["artifact"], "ReceiptAcceptanceTransitionMatrix_Cycle3_V1")
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_all_relevant_cycle_rows_and_families_are_present(self) -> None:
        self.assertEqual(set(self.summary["families_checked"]), {"IG", "DGU", "RS", "QFT"})
        rows = self.summary["cycle_rows_checked"]
        observed = {(row["family"], row["cycle"], row["artifact"]) for row in rows}
        self.assertEqual(observed, EXPECTED_ROWS)
        self.assertEqual(len(rows), 8)

    def test_no_row_transitions_to_accepted_for_routing(self) -> None:
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)
        for row in self.summary["cycle_rows_checked"]:
            self.assertIs(row["accepted_for_routing"], False, row)
            self.assertIs(row["proof_restart_allowed"], False, row)
            self.assertEqual(row["transition_decision"], "not_accepted_for_routing")

    def test_transition_blockers_cover_all_requested_families(self) -> None:
        blockers = self.summary["family_transition_blockers"]
        self.assertEqual(set(blockers), {"IG", "DGU", "RS", "QFT"})
        for family, required_terms in REQUIRED_BLOCKERS.items():
            family_blockers = set(blockers[family])
            for term in required_terms:
                self.assertIn(term, family_blockers)

    def test_missing_transition_fields_are_named_on_each_row(self) -> None:
        for row in self.summary["cycle_rows_checked"]:
            missing = row.get("missing_transition_fields", [])
            self.assertGreaterEqual(len(missing), 5, row)
        all_missing = " ".join(
            " ".join(row["missing_transition_fields"])
            for row in self.summary["cycle_rows_checked"]
        )
        for required in [
            "source_emitted_representation_theory_Bianchi_selection_rule",
            "identity_to_actual_D_GU_epsilon_0_1_action_operator_or_EL",
            "stable_RS_only_source_action_operator_differential_gauge_Noether_BRST_rule",
            "finite_projector_or_local_representative_map",
        ]:
            self.assertIn(required, all_missing)


if __name__ == "__main__":
    unittest.main()

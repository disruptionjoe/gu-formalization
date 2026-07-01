#!/usr/bin/env python3
"""Audit the Y14/K3 bridge-loss ledger.

This audit is not a proof of the physical GU index. It checks that the ledger
keeps the current bridge-loss state honest: K3 promotion is disabled while the
required transport fields remain underdefined, the branch robustness rows are
present, and the claim certificates do not overstate RS-SYMBOL, GEN-COUNT, or
K3-CONTROL.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER = REPO_ROOT / "explorations" / "y14-k3-bridge-loss-ledger-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Bridge Stages And Data Payload",
    "## 3. Loss Ledger Table",
    "## 4. Promotion Rule: When K3 May Be Cited As Physical GU Index Evidence",
    "## 5. Claim Certificate Table For RS-SYMBOL, GEN-COUNT, And K3-CONTROL",
    "## 6. Branch/Bridge Robustness Table",
    "## 7. First Exact Missing Proof Object",
    "## 8. Next Meaningful Proof/Computation Step",
]

REQUIRED_PROMOTION_FIELDS = {
    "physical_rs_complex",
    "tau_discrete_projection",
    "weighted_fredholm_parametrix",
    "bounded_transform_family",
    "k3_reduction_or_aps_map",
    "right_h_structure",
    "background_ch2_f",
    "eta_spectral_flow",
    "noncircular_generation_readout",
}

REQUIRED_STAGE_IDS = {
    "physical_rs_complex",
    "tau_discrete_projection",
    "weighted_sobolev_closure",
    "bounded_transform_family",
    "compactification_or_k3_reduction",
    "h_linear_structure",
    "background_ch2",
    "eta_spectral_flow",
    "generation_readout",
}

REQUIRED_CLAIMS = {
    "RS-SYMBOL": ("specified_open", "not_final"),
    "GEN-COUNT": ("open", "not_final"),
    "K3-CONTROL": ("control_only", "conditional_finality_as_control"),
}

REQUIRED_BRANCHES = {
    "unprojected_y14": "NO_GO",
    "projected_weighted_y14": "CONDITIONAL_OPEN",
    "unitary_discrete_bridge": "UNDERDEFINED",
    "aps_bridge": "UNDERDEFINED",
    "raw_compact_k3": "CONTROL_ONLY",
}

FORBIDDEN_INPUTS = {
    "ind_H(D_RS)=8",
    "ind_H(D_GU)=24",
    "rank_eff=4",
    "rank_eff=8",
    "three_generations",
    "physical_DOF_count_as_index",
}


def ledger_text() -> str:
    return LEDGER.read_text(encoding="utf-8")


def extract_certificate(text: str) -> dict[str, object]:
    for match in re.finditer(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL):
        data = json.loads(match.group(1))
        if data.get("artifact") == "Y14_K3_BRIDGE_LOSS_LEDGER":
            return data
    raise AssertionError("Y14/K3 bridge-loss certificate JSON block not found")


class BridgeLossLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ledger_text()
        cls.cert = extract_certificate(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_current_verdict_blocks_k3_promotion(self) -> None:
        self.assertEqual(
            self.cert["verdict"],
            "K3_CONTROL_ONLY_NOT_PHYSICAL_GU_GENERATION_EVIDENCE",
        )
        self.assertFalse(self.cert["promotion_allowed_now"])
        self.assertEqual(
            self.cert["current_decision"],
            "DO_NOT_CITE_K3_AS_PHYSICAL_GU_GENERATION_COUNT_EVIDENCE",
        )
        self.assertIn("K3 raw RS index != physical noncompact GU index", self.text)

    def test_classification_vocabulary_is_complete(self) -> None:
        self.assertEqual(
            set(self.cert["classification_vocabulary"]),
            {"preserved", "lost", "corrected", "imported", "underdefined"},
        )
        for word in self.cert["classification_vocabulary"]:
            self.assertRegex(self.text, rf"\b{word}\b")

    def test_promotion_rule_fields_are_real_and_currently_open(self) -> None:
        rule = self.cert["promotion_rule"]
        self.assertFalse(rule["all_required_closed"])
        fields = rule["required_fields"]
        self.assertEqual(set(fields), REQUIRED_PROMOTION_FIELDS)
        for value in fields.values():
            self.assertEqual(value, "underdefined")
        self.assertEqual(set(rule["forbidden_inputs"]), FORBIDDEN_INPUTS)

    def test_stage_payloads_cover_full_bridge(self) -> None:
        stages = {stage["id"]: stage for stage in self.cert["stages"]}
        self.assertEqual(set(stages), REQUIRED_STAGE_IDS)
        for stage in stages.values():
            self.assertIn(stage["dominant_class"], self.cert["classification_vocabulary"])
            self.assertTrue(stage["must_transport"])
            self.assertTrue(stage["decision"])
        self.assertEqual(stages["eta_spectral_flow"]["dominant_class"], "corrected")
        self.assertEqual(stages["physical_rs_complex"]["decision"], "OPEN_MISSING_SYMBOL_DATA")

    def test_claim_certificates_do_not_overpromote(self) -> None:
        claims = {claim["id"]: claim for claim in self.cert["claims"]}
        self.assertEqual(set(claims), set(REQUIRED_CLAIMS))
        for claim_id, (status, finality) in REQUIRED_CLAIMS.items():
            self.assertEqual(claims[claim_id]["status"], status)
            self.assertEqual(claims[claim_id]["finality"], finality)
        self.assertIn("compact K3 formulas are controls", claims["K3-CONTROL"]["current_citation"])

    def test_branch_robustness_rows_have_expected_decisions(self) -> None:
        branches = {branch["id"]: branch for branch in self.cert["branches"]}
        self.assertEqual(set(branches), set(REQUIRED_BRANCHES))
        for branch_id, decision in REQUIRED_BRANCHES.items():
            self.assertEqual(branches[branch_id]["decision"], decision)
        self.assertIn("control arithmetic only", branches["raw_compact_k3"]["citation"])
        self.assertIn("not citable", branches["unprojected_y14"]["citation"])

    def test_loss_ledger_contains_specific_transport_failures(self) -> None:
        required_phrases = [
            "Projection intentionally discards it",
            "The scalar `SL(4,R)/SO_0(3,1)` route has no scalar discrete series",
            "Single-face b-calculus is not enough for the full fiber end",
            "Eta values for other boundary operators do not compute the physical RS correction",
            "using them triggers `INVALID_CIRCULAR`",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, self.text)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(BridgeLossLedgerTests)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

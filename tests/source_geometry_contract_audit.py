#!/usr/bin/env python3
"""Audit the source-geometry-not-quantized-gravity contract.

This is a structural contract audit, not a proof of GU. It checks that the
document keeps the source-geometry reframing tied to real source-to-shadow
certificate fields, forbidden-shortcut vocabulary, claim certificates, and
branch robustness decisions.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "source-geometry-not-quantized-gravity-contract-2026-06-24.md"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Steelman Problem Statement In Plain English And Formal Terms",
    "## 3. What Changes Compared With Conventional Quantum-Gravity Framing",
    "## 4. What Does Not Change: Obligations GU Still Owes",
    "## 5. Required Reduction Certificate Stack",
    "## 6. Claim Certificate Table",
    "## 7. Forbidden Shortcuts And Rollback Conditions",
    "## 8. Branch Robustness",
    "## 9. Next Meaningful Proof/Computation Step",
]

EXPECTED_STACK = [
    "source_object",
    "reduction_map",
    "provenance",
    "known_physics_recovery",
    "quantum_qft_recovery",
    "falsification_rollback",
]

EXPECTED_CLAIMS = {
    "SOURCE_GEOMETRY": {
        "status": "contract_open",
        "sentinels": {"source_geometry_by_name_only", "compatibility_as_recovery"},
    },
    "GR_SHADOW": {
        "status": "open",
        "sentinels": {"weak_field_as_exact_GR", "free_beta_nonzero_theta"},
    },
    "QFT_SHADOW": {
        "status": "open",
        "sentinels": {"metric_quantization_as_primary_start", "qft_recovery_by_slogan"},
    },
    "SM_MATTER": {
        "status": "partial_host_selector_open",
        "sentinels": {"host_as_selector", "compact_control_as_physical_index"},
    },
    "MEASUREMENT": {
        "status": "controls_only",
        "sentinels": {"ansatz_state_as_measurement", "observer_finality_as_physics_escape"},
    },
}

EXPECTED_FORBIDDEN_SHORTCUTS = {
    "metric_quantization_as_primary_start",
    "source_geometry_by_name_only",
    "phenomenological_term_without_source",
    "ansatz_state_as_measurement",
    "compact_control_as_physical_index",
    "host_as_selector",
    "compatibility_as_recovery",
    "observer_finality_as_physics_escape",
    "weak_field_as_exact_GR",
    "free_beta_nonzero_theta",
    "qft_recovery_by_slogan",
}

EXPECTED_BRANCH_DECISIONS = {
    "source_geometry_primary": "PRIMARY_PROGRAM_OPEN",
    "metric_quantization": "SECONDARY_SHADOW_ONLY",
    "phenomenological_insertion": "CONTROL_OR_TARGET_ONLY",
    "ansatz_only": "CONTROL_ONLY",
    "compact_control_only": "CONTROL_ONLY_NOT_PHYSICAL",
}

EXPECTED_CHANGED = {
    "primary_input_is_source_geometry_not_metric_quantization",
    "metric_quantization_is_downstream_shadow",
    "proof_object_is_source_to_shadow_reduction",
    "compact_controls_require_transport_certificate",
    "phenomenology_is_target_not_input",
}

EXPECTED_UNCHANGED = {
    "exact_GR_recovery",
    "QFT_recovery",
    "SM_finite_control",
    "anomaly_control",
    "measurement_state_and_observables",
    "falsification_and_rollback",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing source-geometry contract: {DOC}") from exc


def extract_contract(text: str) -> dict[str, Any]:
    match = re.search(
        r"## Machine-Readable Contract\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Contract JSON block")
    return json.loads(match.group(1))


class SourceGeometryContractAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.contract = extract_contract(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_contract_identity_and_verdict_are_stable(self) -> None:
        self.assertEqual(
            self.contract["artifact"],
            "SOURCE_GEOMETRY_NOT_QUANTIZED_GRAVITY_CONTRACT",
        )
        self.assertEqual(
            self.contract["verdict"],
            "SOURCE_GEOMETRY_REFRAME_ACCEPTED_AS_CONTRACT_NOT_PROOF",
        )
        self.assertEqual(
            self.contract["current_decision"],
            "REQUIRE_SOURCE_TO_SHADOW_CERTIFICATES_BEFORE_PROMOTION",
        )

    def test_certificate_stack_is_complete_and_real(self) -> None:
        self.assertEqual(self.contract["required_stack_order"], EXPECTED_STACK)
        stack = self.contract["certificate_stack"]
        self.assertEqual(set(stack), set(EXPECTED_STACK))

        for layer_name in EXPECTED_STACK:
            layer = stack[layer_name]
            fields = layer.get("required_fields")
            self.assertIsInstance(fields, list, layer_name)
            self.assertGreaterEqual(len(fields), 4, layer_name)
            self.assertEqual(len(fields), len(set(fields)), layer_name)
            self.assertIsInstance(layer.get("failure"), str, layer_name)
            self.assertGreater(len(layer["failure"]), 8, layer_name)

        qft_fields = set(stack["quantum_qft_recovery"]["required_fields"])
        for required in [
            "state_space_or_local_algebra",
            "positive_states",
            "admissible_observables",
            "locality_causality",
            "unitarity_or_reflection_positivity",
        ]:
            self.assertIn(required, qft_fields)

    def test_forbidden_shortcut_vocabulary_is_exact_and_used(self) -> None:
        vocabulary = set(self.contract["forbidden_shortcut_vocabulary"])
        self.assertEqual(vocabulary, EXPECTED_FORBIDDEN_SHORTCUTS)
        for shortcut in EXPECTED_FORBIDDEN_SHORTCUTS:
            self.assertIn(shortcut, self.text)

    def test_claim_certificates_cover_all_stack_layers(self) -> None:
        claims = {claim["id"]: claim for claim in self.contract["claims"]}
        self.assertEqual(set(claims), set(EXPECTED_CLAIMS))

        for claim_id, expected in EXPECTED_CLAIMS.items():
            claim = claims[claim_id]
            self.assertEqual(claim["status"], expected["status"])
            self.assertEqual(claim["finality"], "not_final")
            self.assertEqual(claim["required_certificates"], EXPECTED_STACK)
            self.assertTrue(claim["proof_grade"])
            self.assertTrue(claim["allowed_current_citation"])
            self.assertTrue(claim["rollback_condition"])

            forbidden = set(claim["forbidden_shortcuts"])
            self.assertTrue(forbidden <= EXPECTED_FORBIDDEN_SHORTCUTS)
            self.assertTrue(expected["sentinels"] <= forbidden)

    def test_changed_and_unchanged_obligations_are_explicit(self) -> None:
        self.assertEqual(set(self.contract["changed_obligations"]), EXPECTED_CHANGED)
        self.assertEqual(set(self.contract["unchanged_obligations"]), EXPECTED_UNCHANGED)

        for phrase in [
            "GR obligations remain",
            "QFT obligations remain",
            "Matter/SM obligations remain",
            "Measurement obligations remain",
            "Governance obligations remain",
        ]:
            self.assertIn(phrase, self.text)

    def test_branch_robustness_decisions_block_overpromotion(self) -> None:
        branches = {branch["id"]: branch for branch in self.contract["branch_robustness"]}
        self.assertEqual(set(branches), set(EXPECTED_BRANCH_DECISIONS))
        for branch_id, expected_decision in EXPECTED_BRANCH_DECISIONS.items():
            branch = branches[branch_id]
            self.assertEqual(branch["decision"], expected_decision)
            self.assertTrue(branch["allowed_use"])
            self.assertTrue(branch["forbidden_claim"])

        self.assertIn("primary_definition_of_GU", branches["metric_quantization"]["forbidden_claim"])
        self.assertIn(
            "noncompact_physical_index",
            branches["compact_control_only"]["forbidden_claim"],
        )

    def test_rollback_conditions_and_next_step_are_decision_grade(self) -> None:
        rollbacks = self.contract["rollback_conditions"]
        self.assertGreaterEqual(len(rollbacks), 5)
        for condition in rollbacks:
            self.assertGreater(len(condition), 12)

        self.assertEqual(
            self.contract["next_step"],
            "source_object_v0_plus_gr_qft_reduction_packet",
        )
        self.assertIn("SOURCE_OBJECT_V0", self.text)
        self.assertIn("REDUCTION_PACKET_V0", self.text)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(SourceGeometryContractAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

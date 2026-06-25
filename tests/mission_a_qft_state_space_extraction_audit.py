#!/usr/bin/env python3
"""Audit the Mission A QFT state-space extraction attempt.

This is a structural audit, not a proof of QFT recovery. It checks that the
artifact makes a constructive state-space attempt, keeps state/two-point/GNS
language explicit, separates construction from imports and blockers, carries
positivity/unitarity/locality/anomaly gates, and does not claim QFT is recovered.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "mission-a-qft-state-space-extraction-2026-06-24.md"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. If GU Is Correct, What QFT State-Space Object Must Exist",
    "## 3. Candidate Minimal Sector And Why It Is The Smallest Useful One",
    "## 4. Proposed Extraction Pipeline",
    "## 5. What Can Be Built From Repo Sources Now Versus Imported Or Blocked",
    "## 6. First Exact Obstruction Or Missing Proof Object",
    "## 7. Constructive Next Computation",
    "## 8. Claim Certificate Table",
    "## Machine-Readable Summary",
]

REQUIRED_TEXT = [
    "QFTStateSpaceExtractionCertificate",
    "PositivePhysicalTwoPointCertificate",
    "GNS",
    "two-point",
    "quasifree",
    "omega_b",
    "rho_AB",
    "observables",
    "positivity",
    "unitarity",
    "locality",
    "anomaly",
    "Import",
    "Blocked",
    "rollback",
]

REQUIRED_GATE_IDS = {"positivity", "unitarity", "locality", "anomaly", "observables"}

FORBIDDEN_RECOVERY_CLAIMS = [
    r"\bQFT is recovered\b",
    r"\bQFT recovery is closed\b",
    r"\bGU recovers QFT\b",
    r"\bhas recovered QFT\b",
    r"\bQFT-SHADOW is closed\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Mission A QFT extraction artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## Machine-Readable Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Summary JSON block")
    return json.loads(match.group(1))


class MissionAQFTStateSpaceExtractionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_deliverable_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_certificate_language_is_present(self) -> None:
        for required in REQUIRED_TEXT:
            self.assertIn(required, self.text)

    def test_machine_summary_identity_and_no_recovery_claim(self) -> None:
        self.assertEqual(self.summary["artifact"], "MISSION_A_QFT_STATE_SPACE_EXTRACTION")
        self.assertEqual(
            self.summary["verdict"],
            "CONDITIONAL_CONSTRUCTION_ATTEMPT_BLOCKED_AT_POSITIVE_PHYSICAL_TWO_POINT",
        )
        self.assertIs(self.summary["qft_recovered"], False)
        self.assertIs(self.summary["not_a_qft_recovery_theorem"], True)

        for pattern in FORBIDDEN_RECOVERY_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden recovery claim matched: {pattern}",
            )

    def test_minimal_sector_is_two_point_gns_ready_but_blocked(self) -> None:
        sector = self.summary["minimal_sector"]
        self.assertEqual(sector["id"], "QFT-SSX-PS-LR-QUASIFREE-v0")
        self.assertEqual(sector["state_route"], "two_point_or_quasifree_covariance")
        self.assertIn("CAR", sector["algebra_route"])
        self.assertIn("blocked", sector["status"])

        state_object = self.summary["state_space_object_required_if_gu_correct"]
        for key in [
            "local_algebra",
            "one_particle_space",
            "positive_pairing",
            "state",
            "two_point",
            "quasifree_covariance",
            "gns",
            "observables",
            "anomaly_shadow",
        ]:
            self.assertIn(key, state_object)

    def test_construction_import_and_blocked_labels_are_machine_readable(self) -> None:
        labels = self.summary["construction_labels"]
        self.assertGreaterEqual(len(labels["construction_from_repo_now"]), 4)
        self.assertIn("standard_CAR_algebra_theorem", labels["imports_if_used_now"])
        self.assertIn("standard_GNS_theorem", labels["imports_if_used_now"])
        self.assertIn("source_derived_covariance_C_b", labels["blocked_as_gu_derived"])
        self.assertIn("gu_admissible_observables", labels["blocked_as_gu_derived"])

    def test_gates_cover_observables_positivity_unitarity_locality_and_anomaly(self) -> None:
        gates = {gate["id"]: gate for gate in self.summary["gates"]}
        self.assertEqual(set(gates), REQUIRED_GATE_IDS)
        for gate_id, gate in gates.items():
            self.assertIn(gate["status"], {"blocked", "missing", "conditional_blocked", "open"})
            self.assertGreaterEqual(len(gate["required"]), 2, gate_id)

    def test_first_obstruction_is_exact_and_constructive(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "PositivePhysicalTwoPointCertificate")
        for required in [
            "D_phys_b",
            "K_b",
            "h_b",
            "C_b_or_W_b",
            "positivity",
            "source_provenance",
            "finite_reduction",
        ]:
            self.assertIn(required, obstruction["requires"])
        self.assertIn("imported_formalism", obstruction["why_first"])

    def test_claim_certificates_have_missing_objects_and_rollback(self) -> None:
        claims = {claim["claim"]: claim for claim in self.summary["claim_certificates"]}
        for claim_name in [
            "QFTStateSpaceExtractionCertificate",
            "QFTStateExtractionCertificate",
            "ObservableAdmissibilityCertificate",
            "UnitarityCertificate",
            "AnomalyShadowCertificate",
            "OBS-CHSH",
        ]:
            self.assertIn(claim_name, claims)
            self.assertNotEqual(claims[claim_name]["status"], "closed")
            self.assertGreater(len(claims[claim_name]["missing"]), 0)
            self.assertGreater(len(claims[claim_name]["rollback"]), 8)

    def test_forbidden_promotions_include_no_imported_qft_state_shortcuts(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for item in [
            "claiming_QFT_recovery_from_certificate_shell",
            "treating_Pati_Salam_labels_as_a_state",
            "copying_Bell_state_into_GU_slot",
            "treating_Pauli_controls_as_GU_admissible_observables",
            "importing_standard_free_vacuum_as_GU_derived",
        ]:
            self.assertIn(item, forbidden)

    def test_next_computation_targets_the_two_point_certificate(self) -> None:
        next_computation = self.summary["next_computation"]
        self.assertEqual(
            next_computation["id"],
            "compute_or_refute_PositivePhysicalTwoPointCertificate_for_QFT_SSX_PS_LR_QUASIFREE_v0",
        )
        self.assertIn("compute_source_derived_C_b_or_W_b", next_computation["steps"])
        self.assertIn("run_positivity_unitarity_locality_anomaly_gates", next_computation["steps"])


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(MissionAQFTStateSpaceExtractionAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

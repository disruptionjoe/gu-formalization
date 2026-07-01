#!/usr/bin/env python3
"""Audit the QFT shadow extraction certificate.

This is a structural certificate audit, not a proof of QFT recovery. It checks
that the certificate keeps the required extraction chain explicit, names the
missing proof objects, and does not allow VZ, CHSH controls, representation
labels, or ordinary SM anomaly formulas to be promoted into a full QFT shadow.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "qft-shadow-extraction-certificate-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Certificate Schema",
    "## 3. What Current Repo Supplies",
    "## 4. Missing Proof Objects",
    "## 5. Relation To VZ And CHSH Gates",
    "## 6. Claim Certificate Table",
    "## 7. Branch/Source Robustness Table",
    "## 8. Forbidden Shortcuts And Rollback Conditions",
    "## 9. Next Meaningful Proof/Computation Step",
    "## Machine-Readable QFT Shadow Certificate",
]

REQUIRED_STAGES = [
    "SourceGeometryCertificate",
    "PhysicalFieldComplexCertificate",
    "QFTStateSpaceExtractionCertificate",
    "QFTStateExtractionCertificate",
    "ObservableAdmissibilityCertificate",
    "BornProbabilityCertificate",
    "LocalityCausalityCertificate",
    "UnitarityCertificate",
    "SpinStatisticsCertificate",
    "AnomalyShadowCertificate",
]

REQUIRED_MISSING_OBJECTS = [
    "QFTStateSpaceExtractionCertificate",
    "QFTStateExtractionCertificate",
    "ObservableAdmissibilityCertificate",
    "BornProbabilityCertificate",
    "UnitarityCertificate",
    "SpinStatisticsCertificate",
    "AnomalyShadowCertificate",
    "rho_AB",
    "GU_measurement_postulate",
    "target_free_exact_SM_shadow",
]

REQUIRED_CLAIMS = {
    "QFT-SHADOW": "blocked",
    "OBS-CHSH": "blocked",
    "VZ-14D": "conditional",
    "ANOMALY": "open",
}

REQUIRED_FORBIDDEN_SHORTCUTS = {
    "geometry_means_quantum_recovery_unnecessary",
    "not_quantizing_GR_metric_means_no_QFT_debt",
    "representation_labels_as_quantum_state",
    "Bell_control_as_GU_state",
    "Pauli_controls_as_GU_measurements",
    "VZ_as_full_QFT_recovery",
    "ordinary_SM_anomaly_cancellation_as_full_GU_shadow",
    "import_A_F_G_SM_K_SM_or_n3",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing QFT shadow certificate: {DOC}") from exc


def extract_certificate(text: str) -> dict[str, object]:
    match = re.search(
        r"## Machine-Readable QFT Shadow Certificate\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable QFT shadow JSON block")
    return json.loads(match.group(1))


def claim_map(certificate: dict[str, object]) -> dict[str, dict[str, object]]:
    claims = certificate.get("claim_certificates", [])
    if not isinstance(claims, list):
        raise AssertionError("claim_certificates must be a list")
    return {str(claim["id"]): claim for claim in claims}


class QFTShadowDocumentAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.certificate = extract_certificate(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_blocks_current_qft_shadow(self) -> None:
        self.assertIn("`QFT-SHADOW` is not closed", self.text)
        self.assertIn("first hard blocker: QFTStateSpaceExtractionCertificate", self.text)
        self.assertEqual(
            self.certificate["verdict"],
            "QFT_SHADOW_SCHEMA_DEFINED_CURRENT_REPO_BLOCKED",
        )

    def test_metric_quantization_distinction_and_quantum_debt_are_explicit(self) -> None:
        self.assertIn("different from quantizing the GR metric", self.text)
        self.assertRegex(self.text, r"does not have to\s+start by promoting the 4D metric")
        self.assertIn("does not avoid quantum mechanics or QFT", self.text)
        self.assertIn("states, observables, amplitudes/probabilities", self.text)

    def test_stage_order_and_stage_records_are_complete(self) -> None:
        self.assertEqual(self.certificate["stage_order"], REQUIRED_STAGES)
        stages = self.certificate.get("stages", [])
        self.assertIsInstance(stages, list)
        self.assertEqual([stage["id"] for stage in stages], REQUIRED_STAGES)
        for stage in stages:
            self.assertIn(stage["status"], self.certificate["status_enum"])
            self.assertGreater(len(stage.get("required_fields", [])), 0, stage)
            self.assertGreater(len(stage.get("missing", [])), 0, stage)

    def test_missing_proof_object_names_are_present_in_text_and_claim_json(self) -> None:
        claims = claim_map(self.certificate)
        qft_missing = set(claims["QFT-SHADOW"]["missing_objects"])
        for obj in REQUIRED_MISSING_OBJECTS[:7]:
            self.assertIn(obj, self.text)
            self.assertIn(obj, qft_missing)
        for obj in REQUIRED_MISSING_OBJECTS[7:]:
            self.assertIn(obj, self.text)

    def test_claim_certificates_have_expected_statuses(self) -> None:
        claims = claim_map(self.certificate)
        self.assertEqual(set(claims), set(REQUIRED_CLAIMS))
        for claim_id, status in REQUIRED_CLAIMS.items():
            self.assertEqual(claims[claim_id]["status"], status)
            self.assertGreater(len(claims[claim_id].get("missing_objects", [])), 0)
            self.assertGreater(len(claims[claim_id].get("rollback_conditions", [])), 0)

    def test_obs_chsh_and_vz_are_not_promoted(self) -> None:
        claims = claim_map(self.certificate)
        self.assertIn("rho_AB", claims["OBS-CHSH"]["missing_objects"])
        self.assertIn("GU_measurement_postulate", claims["OBS-CHSH"]["missing_objects"])
        self.assertIn("primary_source_closed_D_GU", claims["VZ-14D"]["missing_objects"])
        self.assertIn("primary_D_GU_lacks_Phi_d", claims["VZ-14D"]["rollback_conditions"])
        self.assertIn("VZ is a causal-symbol gate only", self.text)
        self.assertIn("current violating states are controls or ansatz", self.text)

    def test_anomaly_certificate_remains_relative_and_open(self) -> None:
        claims = claim_map(self.certificate)
        self.assertEqual(claims["ANOMALY"]["status"], "open")
        self.assertIn("extra_mode_anomaly_calculation", claims["ANOMALY"]["missing_objects"])
        self.assertIn("ordinary_SM_shadow_assumed_not_derived", claims["ANOMALY"]["rollback_conditions"])
        self.assertIn("relative ordinary SM anomaly cancellation", self.text)

    def test_forbidden_shortcuts_are_machine_readable(self) -> None:
        shortcuts = set(self.certificate.get("forbidden_shortcuts", []))
        self.assertTrue(REQUIRED_FORBIDDEN_SHORTCUTS.issubset(shortcuts))

    def test_next_step_emits_real_state_and_observable_artifacts(self) -> None:
        next_step = self.certificate["next_step"]
        self.assertEqual(next_step["id"], "compute_GU_two_point_or_covariance_to_finite_rho_AB")
        self.assertEqual(next_step["preferred_lane"], "two_point_quasifree")
        must_emit = set(next_step["must_emit"])
        for artifact in [
            "positive_QFT_state_space",
            "GU_vacuum_or_two_point_state",
            "finite_covariance_K_AB",
            "rho_AB",
            "gu_admissible_local_observables",
            "anomaly_shadow_mode_list",
        ]:
            self.assertIn(artifact, must_emit)


def summary() -> dict[str, object]:
    text = read_doc()
    certificate = extract_certificate(text)
    claims = claim_map(certificate)
    return {
        "not_a_proof": True,
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": certificate["verdict"],
        "stage_count": len(certificate["stages"]),
        "claims": {claim_id: claim["status"] for claim_id, claim in sorted(claims.items())},
        "next_step": certificate["next_step"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit the QFT shadow extraction certificate.")
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(summary(), indent=2, sort_keys=True))
        return 0

    print("QFT shadow extraction audit: structural certificate only, not a proof.")
    print()
    suite = unittest.defaultTestLoader.loadTestsFromName("__main__.QFTShadowDocumentAudit")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

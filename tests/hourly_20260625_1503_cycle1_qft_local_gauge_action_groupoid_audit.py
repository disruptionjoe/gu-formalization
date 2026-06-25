#!/usr/bin/env python3
"""Audit LocalGaugeActionGroupoidOnObservedRawGUFields_V1."""

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
    / "hourly-20260625-1503-cycle1-qft-local-gauge-action-groupoid.md"
)

EXPECTED_ARTIFACT_ID = "LocalGaugeActionGroupoidOnObservedRawGUFields_V1"
EXPECTED_VERDICT = (
    "UNDERDEFINED_CANDIDATE_PACKET_DRAFTED_REPO_SOURCE_OBJECTS_MISSING_NO_GENERATOR_PROMOTED"
)
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1503-cycle1-qft-local-gauge-action-groupoid.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1503_cycle1_qft_local_gauge_action_groupoid_audit.py"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive result",
    "## 4. The first exact obstruction or missing proof object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for `F_phys`, `P_raw/P_fin`, `rho_AB`, and CHSH",
    "## 7. Next meaningful proof/computation step",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_SUMMARY_FIELDS = [
    "local_groupoid_defined",
    "typed_R_raw_b_O_defined",
    "restriction_stability_proved",
    "source_defined_generator_count",
    "F_phys_defined",
    "P_fin_defined",
    "CHSH_work_allowed",
    "target_import_used",
    "proof_restart_allowed",
]

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bderived\s+rho_AB\b",
    r"\brho_AB\s+is\s+derived\b",
    r"\bBell\s+state\s+is\s+source[- ]defined\b",
    r"\bBell\s+control\s+defines\s+the\s+gauge\s+equivalence\b",
    r"\bCHSH\s+control\s+defines\s+the\s+gauge\s+equivalence\b",
    r"\bCHSH\s+state\s+is\s+source[- ]defined\b",
    r"\bPauli\s+observables?\s+select\s+the\s+gauge\s+quotient\b",
    r"\btarget\s+Hilbert\s+state\s+selects\s+the\s+gauge\s+quotient\b",
    r"\btarget\s+density\s+matrix\s+selects\s+the\s+gauge\s+quotient\b",
    r"\bQFT[- ]state\s+proof\s+restart\s+allowed\b",
    r"\bF_phys\^b\(O\)\s+is\s+defined\b",
    r"\brepresentation[- ]carrier\s+labels?\s+select\s+the\s+gauge\s+quotient\b",
    r"\brepresentation[- ]carrier\s+labels?\s+define\s+physical\s+equivalence\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing frontmatter")
    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith("  - "):
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class LocalGaugeActionGroupoidAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.frontmatter = extract_frontmatter(cls.text)
        cls.summary = extract_summary(cls.text)

    def test_frontmatter_identity(self) -> None:
        self.assertEqual(self.frontmatter["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.frontmatter["verdict"], EXPECTED_VERDICT)
        self.assertEqual(self.frontmatter["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.frontmatter["companion_audit"], EXPECTED_AUDIT)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_json_identity_matches_frontmatter(self) -> None:
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1503")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "underdefined")

    def test_required_explicit_fields_present(self) -> None:
        for field in REQUIRED_SUMMARY_FIELDS:
            self.assertIn(field, self.summary)

    def test_candidate_written_but_repo_object_not_defined(self) -> None:
        self.assertIs(self.summary["candidate_local_groupoid_packet_written"], True)
        self.assertIs(self.summary["candidate_R_raw_b_O_specified"], True)
        self.assertIs(self.summary["candidate_G_b_O_specified"], True)
        self.assertIs(self.summary["candidate_action_maps_specified"], True)
        self.assertIs(self.summary["candidate_restriction_square_specified"], True)
        self.assertIs(self.summary["local_groupoid_defined"], False)
        self.assertIs(self.summary["typed_R_raw_b_O_defined"], False)
        self.assertIs(self.summary["branch_iota_b_defined"], False)

    def test_generator_not_promoted_without_source_branch_packet(self) -> None:
        self.assertIs(self.summary["restriction_stability_proved"], False)
        self.assertIs(self.summary["gauge_action_generator_source_defined"], False)
        self.assertEqual(self.summary["source_defined_generator_count"], 0)
        self.assertEqual(self.summary["restriction_stable_generator_count"], 0)

    def test_downstream_qft_objects_remain_blocked(self) -> None:
        for key in [
            "F_phys_defined",
            "physical_equivalence_relation_defined",
            "P_raw_descent_allowed",
            "P_fin_defined",
            "rho_AB_work_allowed",
            "CHSH_work_allowed",
            "proof_restart_allowed",
        ]:
            self.assertIs(self.summary[key], False, key)

    def test_no_target_import(self) -> None:
        self.assertIs(self.summary["target_import_used"], False)
        self.assertTrue(
            self.summary["strongest_positive_result"]["does_not_use_target_data"]
        )

    def test_first_obstruction_is_source_observed_raw_packet(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "SourceObservedRawFieldBranchPacketForRRawBO_V1",
        )
        self.assertTrue(obstruction["missing"])
        for required in [
            "source_defined_iota_b",
            "typed_R_raw_b_O",
            "admissible_gauge_groupoid_G_b_O",
            "restriction_commuting_square",
            "non_import_proof",
        ]:
            self.assertIn(required, obstruction["required_fields"])
        for blocked in [
            "local_groupoid_definition",
            "gauge_orbit_generator_promotion",
            "tilde_phys_b_O",
            "F_phys^b(O)",
            "P_fin^b",
            "rho_AB",
            "CHSH",
        ]:
            self.assertIn(blocked, obstruction["blocks"])

    def test_candidate_action_contains_expected_components(self) -> None:
        action_data = self.summary["candidate_action_data"]
        self.assertEqual(action_data["fiber_group"], "Sp(64)")
        self.assertTrue(action_data["connection_action_formula_present"])
        self.assertTrue(action_data["curvature_action_formula_present"])
        self.assertTrue(action_data["spinor_action_formula_present"])
        self.assertTrue(action_data["ad_valued_phi_equivariance_present"])
        self.assertTrue(action_data["inhomogeneous_distortion_equivariance_present"])

    def test_next_step_requires_source_packet(self) -> None:
        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(next_step["id"], "GaugeOrbitGeneratorRestrictionTest_V1")
        self.assertEqual(
            next_step["requires"],
            "SourceObservedRawFieldBranchPacketForRRawBO_V1",
        )
        self.assertEqual(
            next_step["first_promotable_output"],
            "one_source_defined_restriction_stable_gauge_orbit_generator_family",
        )

    def test_forbidden_promotions_are_explicit(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for item in [
            "target_Hilbert_state_as_gauge_congruence_selector",
            "target_density_matrix_as_gauge_congruence_selector",
            "Bell_or_CHSH_control_as_gauge_congruence_selector",
            "Pauli_observable_as_gauge_congruence_selector",
            "representation_carrier_label_as_gauge_congruence_selector",
            "ordinary_QFT_recovery_target_as_gauge_generator_selector",
        ]:
            self.assertIn(item, forbidden)

    def test_no_forbidden_promotion_phrases(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )


if __name__ == "__main__":
    unittest.main()

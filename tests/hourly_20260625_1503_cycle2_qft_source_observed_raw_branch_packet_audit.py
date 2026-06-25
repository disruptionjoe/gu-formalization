#!/usr/bin/env python3
"""Audit SourceObservedRawFieldBranchPacketForRRawBO_V1."""

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
    / "hourly-20260625-1503-cycle2-qft-source-observed-raw-branch-packet.md"
)

EXPECTED_ARTIFACT_ID = "SourceObservedRawFieldBranchPacketForRRawBO_V1"
EXPECTED_VERDICT = (
    "UNDERDEFINED_SOURCE_BRANCH_PACKET_ABSENT_CANDIDATE_TEMPLATE_NOT_PROMOTED"
)
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1503-cycle2-qft-source-observed-raw-branch-packet.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1503_cycle2_qft_source_observed_raw_branch_packet_audit.py"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. The strongest positive construction attempt",
    "## 4. The first exact obstruction or missing proof/source object",
    "## 5. The constructive next object that would remove or test the obstruction",
    "## 6. What this means for gauge generator promotion, `F_phys`, `P_fin`, and CHSH",
    "## 7. Next meaningful proof/source computation step",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_EXPLICIT_FIELDS = [
    "source_branch_packet_present",
    "branch_context_defined",
    "iota_b_source_defined",
    "U_b_O_defined",
    "typed_R_raw_b_O_defined",
    "G_b_O_defined",
    "restriction_maps_defined",
    "non_import_screen_present",
    "generator_promotion_allowed",
    "F_phys_defined",
    "P_fin_defined",
    "CHSH_work_allowed",
    "target_import_used",
]

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bderived\s+rho_AB\b",
    r"\brho_AB\s+is\s+derived\b",
    r"\bBell\s+state\s+is\s+source[- ]defined\b",
    r"\bBell\s+control\s+defines\s+the\s+branch\b",
    r"\bCHSH\s+control\s+defines\s+the\s+branch\b",
    r"\bPauli\s+settings?\s+define\s+R_raw\b",
    r"\bPauli\s+settings?\s+select\s+the\s+branch\b",
    r"\btarget\s+Hilbert\s+state\s+selects\s+the\s+branch\b",
    r"\btarget\s+density\s+matrix\s+selects\s+the\s+branch\b",
    r"\brepresentation[- ]carrier\s+labels?\s+select\s+the\s+branch\b",
    r"\bF_phys\^b\(O\)\s+is\s+defined\b",
    r"\bP_fin\^b\s+is\s+defined\b",
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


class SourceObservedRawBranchPacketAudit(unittest.TestCase):
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
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "underdefined")

    def test_required_explicit_fields_present(self) -> None:
        for field in REQUIRED_EXPLICIT_FIELDS:
            self.assertIn(field, self.summary)

    def test_packet_not_source_defined(self) -> None:
        for key in [
            "source_branch_packet_present",
            "branch_context_defined",
            "iota_b_source_defined",
            "U_b_O_defined",
            "typed_R_raw_b_O_defined",
            "G_b_O_defined",
            "restriction_maps_defined",
        ]:
            self.assertIs(self.summary[key], False, key)

    def test_non_import_screen_and_no_target_import(self) -> None:
        self.assertIs(self.summary["non_import_screen_present"], True)
        self.assertIs(self.summary["target_import_used"], False)
        self.assertTrue(
            self.summary["strongest_positive_construction_attempt"][
                "does_not_use_target_data"
            ]
        )

    def test_no_downstream_promotion(self) -> None:
        for key in [
            "generator_promotion_allowed",
            "F_phys_defined",
            "P_fin_defined",
            "CHSH_work_allowed",
        ]:
            self.assertIs(self.summary[key], False, key)
        impact = self.summary["downstream_impact"]
        for key in [
            "gauge_generator_promotion_allowed",
            "F_phys_defined",
            "P_raw_descent_allowed",
            "P_fin_defined",
            "rho_AB_work_allowed",
            "CHSH_work_allowed",
        ]:
            self.assertIs(impact[key], False, key)

    def test_candidate_template_is_only_template(self) -> None:
        self.assertIs(self.summary["candidate_template_written"], True)
        self.assertEqual(
            self.summary["candidate_branch_context"]["status"],
            "template_not_source_defined",
        )
        self.assertEqual(
            self.summary["candidate_iota_b"]["status"],
            "missing_source_definition",
        )
        self.assertEqual(
            self.summary["candidate_U_b_O"]["status"],
            "missing_because_iota_b_missing",
        )
        self.assertEqual(
            self.summary["candidate_restriction_maps"]["status"],
            "template_only",
        )

    def test_candidate_components_are_explicit(self) -> None:
        components = set(self.summary["candidate_R_raw_b_O_components"])
        for component in [
            "connection_A",
            "curvature_F_A",
            "spinor_psi",
            "ad_valued_two_form_alpha",
            "Phi_alpha_psi",
        ]:
            self.assertIn(component, components)
        self.assertEqual(
            self.summary["candidate_G_b_O"],
            "admissible_local_sections_of_AdP_over_U_b_O",
        )
        self.assertIn("res_R", self.summary["candidate_next_square"])
        self.assertIn("gamma_O", self.summary["candidate_next_square"])

    def test_first_obstruction_is_missing_packet(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], EXPECTED_ARTIFACT_ID)
        self.assertTrue(obstruction["missing"])
        self.assertEqual(
            obstruction["first_missing_subobject"],
            "source_defined_iota_b_and_typed_R_raw_b_O",
        )
        for required in [
            "branch_context_b_O_O_prime",
            "source_defined_iota_b",
            "local_Y_domain_U_b_O",
            "typed_R_raw_b_O",
            "admissible_G_b_O",
            "raw_field_restriction_res_R_O_O_prime",
            "gauge_parameter_restriction_res_G_O_O_prime",
            "non_import_screen",
        ]:
            self.assertIn(required, obstruction["required_fields"])
        for blocked in [
            "LocalGaugeActionGroupoidOnObservedRawGUFields_V1",
            "gauge_orbit_generator_promotion",
            "tilde_phys_b_O",
            "F_phys^b(O)",
            "P_fin^b",
            "rho_AB",
            "CHSH",
        ]:
            self.assertIn(blocked, obstruction["blocks"])

    def test_next_step_targets_packet_before_gauge_test(self) -> None:
        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(
            next_step["id"],
            "FindOrConstructSourceObservedRawFieldBranchPacketForRRawBO_V1",
        )
        self.assertEqual(next_step["then"], "GaugeOrbitGeneratorRestrictionTest_V1")
        self.assertEqual(
            next_step["first_promotable_output"],
            "one_source_defined_restriction_stable_gauge_orbit_generator_family",
        )

    def test_forbidden_selectors_are_explicit(self) -> None:
        forbidden = set(self.summary["forbidden_selectors"])
        for item in [
            "F_phys_as_selector_for_R_raw_b_O",
            "P_fin_as_selector_for_R_raw_b_O",
            "target_Hilbert_state_as_branch_selector",
            "target_density_matrix_as_branch_selector",
            "Bell_or_CHSH_control_as_branch_or_gauge_selector",
            "Pauli_setting_as_branch_or_gauge_selector",
            "representation_label_as_branch_or_gauge_selector",
            "ordinary_QFT_recovery_target_as_branch_packet_selector",
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

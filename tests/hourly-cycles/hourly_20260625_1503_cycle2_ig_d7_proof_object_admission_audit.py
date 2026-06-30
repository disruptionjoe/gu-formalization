import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md"
)

EXPECTED_ARTIFACT_ID = "IG_D7_FORMAL_OR_CAS_PROOF_OBJECT_ADMISSION_1503_C2_L2_V1"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1503_cycle2_ig_d7_proof_object_admission_audit.py"
)


def load_artifact():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("machine-readable JSON summary not found")
    return text, json.loads(match.group(1))


class IGD7ProofObjectAdmissionAudit(unittest.TestCase):
    def setUp(self):
        self.assertTrue(ARTIFACT.exists(), f"missing artifact: {ARTIFACT}")
        self.text, self.summary = load_artifact()

    def test_frontmatter_paths_and_json_identity(self):
        self.assertRegex(self.text, r"\A---\n")
        self.assertIn(f'artifact_id: "{EXPECTED_ARTIFACT_ID}"', self.text)
        self.assertIn('verdict: "BLOCKED_FORMAL_PROOF_NOT_ADMITTED"', self.text)
        self.assertIn(f'owned_path: "{EXPECTED_OWNED_PATH}"', self.text)
        self.assertIn(f'companion_audit: "{EXPECTED_AUDIT}"', self.text)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_required_explicit_fields_are_present_and_blocking(self):
        required = {
            "formal_proof_admitted",
            "raw_transcript_required",
            "FC_IRR_status",
            "FC_MULT_status",
            "FC_HW_status",
            "full_summand_lists_present",
            "dimension_checks_present",
            "accepted_selector_count",
            "target_import_used",
            "proof_restart_allowed",
        }
        self.assertLessEqual(required, set(self.summary))
        self.assertFalse(self.summary["formal_proof_admitted"])
        self.assertTrue(self.summary["raw_transcript_required"])
        self.assertFalse(self.summary["full_summand_lists_present"])
        self.assertFalse(self.summary["dimension_checks_present"])
        self.assertEqual(self.summary["accepted_selector_count"], 0)
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["proof_restart_allowed"])

    def test_fc_statuses_reject_premature_admission(self):
        for key in ("FC_IRR_status", "FC_MULT_status", "FC_HW_status"):
            self.assertIn("blocked", self.summary[key])
            self.assertNotRegex(self.summary[key], r"\b(closed|verified|resolved|admitted)\b")
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["K_IG_family_identity_verified"])
        self.assertFalse(self.summary["full_rival_row_elimination_completed"])

    def test_theorem_statements_and_obligations_are_specific(self):
        for key in (
            "FC_IRR_theorem_statement",
            "FC_MULT_theorem_statement",
            "FC_HW_theorem_statement",
        ):
            self.assertIn(key, self.summary)
            self.assertGreater(len(self.summary[key]), 40)

        obligations = set(self.summary["required_proof_obligations"])
        expected = {
            "PO_ROOT_D7_Dynkin_convention",
            "PO_FC_IRR_full_decomposition_of_V_omega1_tensor_V_omega7",
            "PO_FC_MULT_full_decomposition_of_V_omega2_tensor_V_omega6",
            "PO_FC_HW_highest_weight_of_ker_c",
            "PO_DIM_dimension_checks_for_every_reported_summand",
            "PO_NO_IMPORT_no_target_physics_or_desired_uniqueness",
        }
        self.assertEqual(obligations, expected)

    def test_rejects_chirality_only_and_reconstruction_grade_arguments(self):
        rejected = set(self.summary["rejected_admission_bases"])
        self.assertIn("chirality_only_argument_without_full_summand_list", rejected)
        self.assertIn("reconstruction_grade_kernel_irreducibility", rejected)
        self.assertIn("reconstruction_grade_highest_weight_assignment", rejected)
        self.assertIn("expected_decomposition_without_raw_output_or_formal_branching_proof", rejected)
        self.assertIn("target_physics_or_desired_selector_uniqueness", rejected)

        accepted = set(self.summary["accepted_narrow_results"])
        self.assertIn("chirality_exclusion_of_V_omega7", accepted)
        self.assertIn("chirality_exclusion_of_V_omega1_plus_omega7", accepted)
        self.assertNotIn("multiplicity_one_for_V_omega6", accepted)

    def test_admission_rubric_requires_full_finite_data(self):
        rubric = set(self.summary["admission_rubric_required_outputs"])
        expected = {
            "full_summand_list_for_V_omega1_tensor_V_omega7",
            "full_summand_list_for_V_omega2_tensor_V_omega6",
            "multiplicities_for_all_summands",
            "dimensions_for_all_summands",
            "tensor_product_total_dimension_checks",
            "proof_or_transcript_for_ker_c_irreducibility",
            "proof_or_transcript_for_ker_c_highest_weight",
            "explicit_presence_or_absence_of_V_omega6",
            "explicit_presence_or_absence_of_V_omega7",
            "explicit_presence_or_absence_of_V_omega1_plus_omega7",
            "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW",
        }
        self.assertEqual(rubric, expected)

    def test_no_forbidden_promotion_language(self):
        forbidden_patterns = [
            r"chirality(?:-| )only\s+(?:therefore|implies|proves|verifies|closes)",
            r"shiab existence\s+(?:therefore|implies|proves|verifies|closes)",
            r"target physics\s+(?:therefore|implies|proves|selects|admits)",
            r"formal_proof_admitted:\s*true",
            r'"formal_proof_admitted"\s*:\s*true',
            r"proof_restart_allowed:\s*true",
            r'"proof_restart_allowed"\s*:\s*true',
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

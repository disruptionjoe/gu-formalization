import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1702-cycle2-ig-finite-transcript-admission-matrix.md"
)

EXPECTED_ARTIFACT_ID = "IG_FINITE_TRANSCRIPT_ADMISSION_MATRIX_1702_C2_L2_V1"
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle2-ig-finite-transcript-admission-matrix.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle2_ig_finite_transcript_admission_matrix_audit.py"
)


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("machine-readable JSON summary not found")
    return text, json.loads(match.group(1))


class IGFiniteTranscriptAdmissionMatrixAudit(unittest.TestCase):
    def setUp(self):
        self.assertTrue(ARTIFACT.exists(), f"missing artifact: {ARTIFACT}")
        self.text, self.summary = load_summary()

    def test_identity_and_owned_paths(self):
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["decision_target"], "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1")
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_no_transcript_restart_import_or_family_identity(self):
        self.assertFalse(self.summary["accepted_transcript"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_selector_count"], 0)
        self.assertFalse(self.summary["raw_CAS_transcript_admitted"])
        self.assertFalse(self.summary["formal_D7_branching_proof_admitted"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_physics_used"])
        self.assertFalse(self.summary["desired_generation_count_used"])
        self.assertFalse(self.summary["desired_uniqueness_used"])
        self.assertFalse(self.summary["K_IG_family_identity_verified"])
        self.assertFalse(self.summary["family_identity_verified"])
        self.assertFalse(self.summary["selector_theorem_closed"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])

    def test_required_finite_field_rows_exist(self):
        rows = self.summary["finite_field_rows"]
        by_field = {row["field"]: row for row in rows}
        expected_fields = {
            "raw_or_formal_source_identity",
            "D7_convention",
            "product_A_decomposition",
            "product_A_kernel_cokernel_branch",
            "product_B_full_summands",
            "product_B_chirality_excluded_rivals",
            "FC_IRR_verdict",
            "FC_MULT_verdict",
            "FC_HW_verdict",
        }
        self.assertEqual(set(by_field), expected_fields)
        for field in expected_fields:
            self.assertTrue(by_field[field]["required"], field)
            self.assertIn("source_identity", by_field[field], field)
            self.assertIn("status", by_field[field], field)
            self.assertIn("admission_effect", by_field[field], field)

    def test_product_a_matrix_fields_are_blocked(self):
        rows = {row["field"]: row for row in self.summary["finite_field_rows"]}
        product_a = rows["product_A_decomposition"]
        self.assertEqual(product_a["expression"], "V(omega_1) tensor V(omega_7)")
        self.assertIsNone(product_a["full_summands"])
        self.assertIsNone(product_a["multiplicities"])
        self.assertIsNone(product_a["dimensions"])
        self.assertIsNone(product_a["total_dimension_check"])
        self.assertEqual(product_a["status"], "missing")

        branch = rows["product_A_kernel_cokernel_branch"]
        self.assertEqual(branch["map"], "c: V(omega_1) tensor V(omega_7) -> V(omega_6)")
        self.assertIsNone(branch["kernel_branch"])
        self.assertIsNone(branch["cokernel_branch"])
        self.assertIsNone(branch["highest_weight"])
        self.assertIsNone(branch["irreducibility"])
        self.assertEqual(branch["status"], "missing")

    def test_product_b_first_obstruction_fields_are_missing(self):
        rows = {row["field"]: row for row in self.summary["finite_field_rows"]}
        product_b = rows["product_B_full_summands"]
        self.assertEqual(product_b["expression"], "V(omega_2) tensor V(omega_6)")
        self.assertIsNone(product_b["full_summands"])
        self.assertIsNone(product_b["multiplicities"])
        self.assertIsNone(product_b["dimensions"])
        self.assertIsNone(product_b["total_dimension_check"])
        self.assertIsNone(product_b["multiplicity_of_V_omega6"])
        self.assertEqual(product_b["status"], "missing")
        self.assertEqual(product_b["admission_effect"], "first_obstruction_blocks_FC_MULT")

        missing = set(self.summary["first_missing_field_set"])
        expected_missing = {
            "product_B_full_summand_list",
            "product_B_multiplicities",
            "product_B_dimensions",
            "product_B_total_dimension_check",
            "multiplicity_of_V_omega6_in_B",
            "full_rival_presence_absence_checks",
        }
        self.assertEqual(missing, expected_missing)

    def test_product_b_chirality_is_partial_not_selector(self):
        rows = {row["field"]: row for row in self.summary["finite_field_rows"]}
        chirality = rows["product_B_chirality_excluded_rivals"]
        self.assertTrue(chirality["V_omega7_absent_by_chirality"])
        self.assertTrue(chirality["V_omega1_plus_omega7_absent_by_chirality"])
        self.assertFalse(chirality["full_rival_exclusions"])
        self.assertEqual(chirality["status"], "partial")
        self.assertEqual(chirality["admission_effect"], "narrow_positive_only")

        rivals = self.summary["rival_exclusions"]
        self.assertTrue(rivals["chirality_excludes_two_named_rivals"])
        self.assertFalse(rivals["chirality_promoted_to_selector"])
        self.assertFalse(rivals["full_rival_selector_exclusion_admitted"])

    def test_fc_verdicts_are_blocked(self):
        self.assertIn("blocked", self.summary["FC_IRR_verdict"])
        self.assertIn("blocked", self.summary["FC_MULT_verdict"])
        self.assertIn("blocked", self.summary["FC_HW_verdict"])
        self.assertIn("product_B", self.summary["FC_MULT_verdict"])

        rows = {row["field"]: row for row in self.summary["finite_field_rows"]}
        self.assertEqual(rows["FC_IRR_verdict"]["current_value"], "blocked")
        self.assertEqual(rows["FC_MULT_verdict"]["current_value"], "blocked")
        self.assertEqual(rows["FC_HW_verdict"]["current_value"], "blocked")

    def test_first_obstruction_and_next_object(self):
        self.assertEqual(
            self.summary["first_obstruction"],
            "ProductBFullSummandMultiplicityDimensionTableMissingFor_V_omega2_tensor_V_omega6",
        )
        self.assertEqual(
            self.summary["next_object"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )
        self.assertEqual(
            self.summary["constructive_next_object"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )

    def test_promotion_firewall_rejects_chirality_as_selector(self):
        firewall = self.summary["promotion_firewall"]
        expected = {
            "shiab_existence_not_selector_theorem",
            "chirality_exclusion_not_full_branching_transcript",
            "chirality_only_rejected_as_admission_basis",
            "target_generation_count_not_used",
            "desired_uniqueness_not_used",
            "target_import_not_used",
            "proof_restart_blocked",
            "GU_claim_not_promoted",
        }
        self.assertEqual(set(firewall), expected)
        for key in expected:
            self.assertIs(firewall[key], True, key)
        self.assertFalse(self.summary["chirality_alone_used_as_selector"])

    def test_no_forbidden_promotion_literals(self):
        forbidden_patterns = [
            r'"accepted_transcript"\s*:\s*true',
            r'"accepted_receipt_count"\s*:\s*[1-9]',
            r'"proof_restart_allowed"\s*:\s*true',
            r'"target_import_used"\s*:\s*true',
            r'"K_IG_family_identity_verified"\s*:\s*true',
            r'"family_identity_verified"\s*:\s*true',
            r'"chirality_alone_used_as_selector"\s*:\s*true',
            r'"chirality_promoted_to_selector"\s*:\s*true',
            r"chirality\s+alone\s+(?:proves|selects|admits|closes)",
            r"desired\s+uniqueness\s+(?:proves|selects|admits|closes)",
            r"target\s+generation\s+count\s+(?:proves|selects|admits|closes)",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

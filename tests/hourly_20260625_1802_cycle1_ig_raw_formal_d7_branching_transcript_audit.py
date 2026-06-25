import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md"
)

EXPECTED_ARTIFACT_ID = "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_1802_C1_L2_V1"
EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_PATH = (
    "explorations/hourly-20260625-1802-cycle1-ig-raw-formal-d7-branching-transcript.md"
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


class IGRawFormalD7BranchingTranscriptAudit(unittest.TestCase):
    def setUp(self):
        self.assertTrue(ARTIFACT.exists(), f"missing artifact: {ARTIFACT}")
        self.text, self.summary = load_summary()

    def test_identity_fields(self):
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(self.summary["owned_path"], EXPECTED_ARTIFACT_PATH)
        self.assertEqual(
            self.summary["decision_target"],
            "IG_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT_FOR_SHIAB_HOM_SPACE",
        )
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_transcript_receipt_not_admitted(self):
        self.assertFalse(self.summary["transcript_admitted"])
        self.assertFalse(self.summary["accepted_transcript"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["raw_CAS_transcript_present"])
        self.assertFalse(self.summary["raw_CAS_transcript_admitted"])
        self.assertFalse(self.summary["formal_D7_branching_proof_present"])
        self.assertFalse(self.summary["formal_D7_branching_proof_admitted"])

    def test_product_gate_admission_flags(self):
        self.assertFalse(self.summary["product_b_full_table_admitted"])
        self.assertFalse(self.summary["product_a_kernel_packet_admitted"])

        product_b = self.summary["product_B"]
        self.assertEqual(product_b["expression"], "V(omega_2) tensor V(omega_6)")
        self.assertEqual(product_b["expected_total_dimension"], 5824)
        self.assertFalse(product_b["full_summand_list_admitted"])
        self.assertFalse(product_b["multiplicities_admitted"])
        self.assertFalse(product_b["dimensions_admitted"])
        self.assertFalse(product_b["total_dimension_check_admitted"])
        self.assertFalse(product_b["multiplicity_of_V_omega6_admitted"])
        self.assertTrue(product_b["V_omega7_absence_chirality_excluded"])
        self.assertTrue(product_b["V_omega1_plus_omega7_absence_chirality_excluded"])
        self.assertFalse(product_b["full_rival_presence_absence_admitted"])

        product_a = self.summary["product_A"]
        self.assertEqual(product_a["expression"], "V(omega_1) tensor V(omega_7)")
        self.assertEqual(product_a["expected_total_dimension"], 896)
        self.assertFalse(product_a["kernel_branch_admitted"])
        self.assertFalse(product_a["cokernel_branch_admitted"])
        self.assertFalse(product_a["ker_c_irreducibility_admitted"])
        self.assertFalse(product_a["ker_c_highest_weight_admitted"])

    def test_fc_statuses_blocked(self):
        self.assertEqual(self.summary["fc_irr"], "blocked")
        self.assertEqual(self.summary["fc_mult"], "blocked")
        self.assertEqual(self.summary["fc_hw"], "blocked")
        self.assertEqual(self.summary["FC_IRR_status"], "blocked")
        self.assertEqual(self.summary["FC_MULT_status"], "blocked")
        self.assertEqual(self.summary["FC_HW_status"], "blocked")
        self.assertIn("blocked", self.summary["FC_IRR_verdict"])
        self.assertIn("blocked", self.summary["FC_MULT_verdict"])
        self.assertIn("blocked", self.summary["FC_HW_verdict"])
        self.assertFalse(self.summary["all_FC_gates_closed"])

    def test_proof_restart_firewall(self):
        if not self.summary["transcript_admitted"]:
            self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertEqual(
            self.summary["proof_restart_rule"],
            "proof_restart_allowed_must_be_false_unless_transcript_admitted_is_true",
        )
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])
        self.assertFalse(self.summary["selector_theorem_closed"])
        self.assertFalse(self.summary["K_IG_family_identity_verified"])
        self.assertFalse(self.summary["full_rival_row_elimination_completed"])

    def test_no_target_import(self):
        self.assertTrue(self.summary["no_target_import"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_physics_used"])
        self.assertFalse(self.summary["desired_generation_count_used"])
        self.assertFalse(self.summary["desired_uniqueness_used"])

    def test_missing_rows_and_receipt_requirements(self):
        missing = set(self.summary["finite_rows_missing"])
        required_missing = {
            "product_B_full_summand_list",
            "product_B_multiplicities",
            "product_B_dimensions",
            "product_B_total_dimension_check",
            "product_B_multiplicity_of_V_omega6",
            "product_A_kernel_branch",
            "product_A_kernel_irreducibility_or_full_decomposition",
            "product_A_kernel_highest_weight_or_corrected_weight",
            "FC_IRR_verdict_receipt",
            "FC_MULT_verdict_receipt",
            "FC_HW_verdict_receipt",
        }
        self.assertTrue(required_missing.issubset(missing))

        requirements = set(self.summary["valid_transcript_receipt_must_contain"])
        self.assertIn("root_system_D7_and_omega_convention", requirements)
        self.assertIn(
            "raw_CAS_tool_name_version_invocation_commands_raw_output_or_formal_D7_proof",
            requirements,
        )
        self.assertIn("explicit_no_target_import_statement", requirements)

    def test_first_obstruction_and_next_object(self):
        self.assertEqual(
            self.summary["first_obstruction"],
            "ProductBFullSummandMultiplicityDimensionTableMissingFor_V_omega2_tensor_V_omega6",
        )
        self.assertEqual(
            self.summary["first_missing_proof_source_object"],
            "FullBProductD7SummandMultiplicityDimensionTranscriptForShiabHomSpace_V1",
        )
        self.assertEqual(
            self.summary["second_missing_proof_source_object"],
            "ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6",
        )
        self.assertEqual(
            self.summary["constructive_next_object"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )

    def test_no_forbidden_promotion_literals(self):
        forbidden_patterns = [
            r'"transcript_admitted"\s*:\s*true',
            r'"accepted_receipt_count"\s*:\s*[1-9]',
            r'"product_b_full_table_admitted"\s*:\s*true',
            r'"product_a_kernel_packet_admitted"\s*:\s*true',
            r'"proof_restart_allowed"\s*:\s*true',
            r'"no_target_import"\s*:\s*false',
            r'"target_import_used"\s*:\s*true',
            r'"desired_generation_count_used"\s*:\s*true',
            r'"desired_uniqueness_used"\s*:\s*true',
            r'"K_IG_family_identity_verified"\s*:\s*true',
            r"target\s+generation\s+count\s+(?:proves|selects|admits|closes)",
            r"desired\s+uniqueness\s+(?:proves|selects|admits|closes)",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

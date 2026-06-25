import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1702-cycle1-ig-raw-formal-d7-branching-transcript.md"
)

EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_ARTIFACT_ID = (
    "RawOrFormalD7BranchingTranscriptForShiabHomSpace_1702_C1_L2_V1"
)
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle1-ig-raw-formal-d7-branching-transcript.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle1_ig_raw_formal_d7_branching_transcript_audit.py"
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

    def test_identity_and_owned_paths(self):
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(
            self.summary["decision_target"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )

    def test_blocked_no_receipt_no_restart_no_import(self):
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertIn("NO_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT", self.summary["verdict"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_selector_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_physics_used"])
        self.assertFalse(self.summary["desired_generation_count_used"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])

    def test_transcript_and_proof_source_booleans(self):
        self.assertFalse(self.summary["raw_CAS_transcript_present"])
        self.assertFalse(self.summary["raw_CAS_transcript_admitted"])
        self.assertFalse(self.summary["formal_D7_branching_proof_present"])
        self.assertFalse(self.summary["formal_D7_branching_proof_admitted"])
        self.assertFalse(self.summary["local_D7_CAS_tool_available"])

        proof_source = self.summary["transcript_or_proof_source_booleans"]
        expected_false = {
            "raw_CAS_tool_name_present",
            "raw_CAS_version_present",
            "raw_CAS_invocation_present",
            "raw_CAS_commands_present",
            "raw_CAS_output_present",
            "formal_branching_proof_present",
            "formal_highest_weight_proof_present",
            "formal_dimension_checks_present",
        }
        for key in expected_false:
            self.assertIs(proof_source[key], False, key)
        self.assertTrue(proof_source["repo_sources_only_used_for_admission"])

    def test_finite_data_fields_are_complete_and_blocked(self):
        fields = self.summary["finite_data_fields"]
        expected_present = {
            "root_system_D7_convention",
            "omega_1_vector",
            "omega_2_two_form_adjoint",
            "omega_6_positive_half_spin",
            "omega_7_negative_half_spin",
        }
        for key in expected_present:
            self.assertEqual(fields[key], "present_from_repo_sources", key)

        expected_missing = {
            "product_A_full_summand_list",
            "product_A_multiplicities",
            "product_A_dimensions",
            "product_A_total_dimension_check",
            "kernel_branch_for_c_A_to_V_omega6",
            "cokernel_branch_for_c_A_to_V_omega6",
            "ker_c_irreducibility_or_full_decomposition",
            "ker_c_highest_weight_or_corrected_weight",
            "product_B_full_summand_list",
            "product_B_multiplicities",
            "product_B_dimensions",
            "product_B_total_dimension_check",
            "multiplicity_of_V_omega6_in_B",
            "rival_selector_exclusions_full",
        }
        for key in expected_missing:
            self.assertEqual(fields[key], "missing_admitted_transcript", key)

        self.assertEqual(fields["FC_IRR_verdict"], "blocked")
        self.assertEqual(fields["FC_MULT_verdict"], "blocked")
        self.assertEqual(fields["FC_HW_verdict"], "blocked")

    def test_product_a_b_and_rival_selector_fields(self):
        product_a = self.summary["product_A"]
        self.assertEqual(product_a["expression"], "V(omega_1) tensor V(omega_7)")
        for key, value in product_a.items():
            if key != "expression":
                self.assertIs(value, False, key)

        product_b = self.summary["product_B"]
        self.assertEqual(product_b["expression"], "V(omega_2) tensor V(omega_6)")
        self.assertFalse(product_b["full_summand_list_admitted"])
        self.assertFalse(product_b["multiplicities_admitted"])
        self.assertFalse(product_b["dimensions_admitted"])
        self.assertFalse(product_b["multiplicity_of_V_omega6_admitted"])
        self.assertTrue(product_b["V_omega7_absence_chirality_excluded"])
        self.assertTrue(product_b["V_omega1_plus_omega7_absence_chirality_excluded"])

        rivals = self.summary["rival_selector_exclusions"]
        self.assertTrue(rivals["chirality_excludes_two_named_rivals"])
        self.assertFalse(rivals["full_rival_selector_exclusion_admitted"])
        self.assertIn("full_A_B_decompositions", rivals["reason"])

    def test_first_obstruction_and_next_object(self):
        self.assertIn("B_equals_V_omega2_tensor_V_omega6", self.summary["first_obstruction"])
        self.assertIn("every_summand", self.summary["first_obstruction"])
        self.assertIn("multiplicity", self.summary["first_obstruction"])
        self.assertIn("dimension", self.summary["first_obstruction"])
        self.assertEqual(
            self.summary["first_missing_proof_source_object"],
            "FullBProductD7SummandMultiplicityDimensionTranscriptForShiabHomSpace_V1",
        )
        self.assertEqual(
            self.summary["next_object"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )
        self.assertEqual(
            self.summary["constructive_next_object"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )

    def test_fc_gates_remain_blocked(self):
        self.assertFalse(self.summary["all_FC_gates_closed"])
        for key in ("FC_IRR_status", "FC_MULT_status", "FC_HW_status"):
            self.assertIn("blocked", self.summary[key])
            self.assertNotRegex(
                self.summary[key],
                r"\b(closed|resolved|admitted|verified)\b",
            )

    def test_promotion_firewall(self):
        firewall = self.summary["promotion_firewall"]
        expected = {
            "shiab_existence_not_selector_theorem",
            "chirality_exclusion_not_full_branching_transcript",
            "chirality_only_rejected_as_admission_basis",
            "pseudocode_not_raw_CAS_receipt",
            "reconstruction_grade_not_formal_proof",
            "target_physics_not_used",
            "desired_generation_count_not_used",
            "proof_restart_blocked",
            "GU_claim_not_promoted",
        }
        self.assertEqual(set(firewall), expected)
        for key in expected:
            self.assertIs(firewall[key], True, key)

    def test_direct_repo_results_do_not_overclaim(self):
        results = set(self.summary["directly_derived_repo_results"])
        self.assertIn("Cl_9_5_Shiab_contraction_exists", results)
        self.assertIn("D7_weight_convention_specified", results)
        self.assertIn("prior_LiE_Sage_material_is_pseudocode_or_expected_output_not_raw_transcript", results)
        self.assertNotIn("multiplicity_one_for_V_omega6_in_B_admitted", results)
        self.assertNotIn("RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1_admitted", results)

    def test_no_forbidden_positive_literals(self):
        forbidden_patterns = [
            r'"accepted_receipt_count"\s*:\s*[1-9]',
            r'"proof_restart_allowed"\s*:\s*true',
            r'"target_import_used"\s*:\s*true',
            r'"raw_CAS_transcript_admitted"\s*:\s*true',
            r'"formal_D7_branching_proof_admitted"\s*:\s*true',
            r'"major_GU_claim_promoted"\s*:\s*true',
            r'"all_FC_gates_closed"\s*:\s*true',
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

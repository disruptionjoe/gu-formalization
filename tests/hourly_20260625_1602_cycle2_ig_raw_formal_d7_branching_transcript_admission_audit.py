import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle2-ig-raw-formal-d7-branching-transcript-admission.md"
)

EXPECTED_ARTIFACT_ID = (
    "IG_RAW_FORMAL_D7_BRANCHING_TRANSCRIPT_ADMISSION_1602_C2_L2_V1"
)
EXPECTED_RUN_ID = "hourly-20260625-1602"


def load_artifact():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("machine-readable JSON summary not found")
    return text, json.loads(match.group(1))


class IGD7RawFormalBranchingTranscriptAdmissionAudit(unittest.TestCase):
    def setUp(self):
        self.assertTrue(ARTIFACT.exists(), f"missing artifact: {ARTIFACT}")
        self.text, self.summary = load_artifact()

    def test_identity_and_blocked_verdict(self):
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertIn("NO_ADMISSIBLE_RAW_OR_FORMAL_D7_BRANCHING_TRANSCRIPT", self.summary["verdict"])

    def test_no_accepted_receipt_selector_or_restart(self):
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_selector_count"], 0)
        self.assertFalse(self.summary["raw_CAS_transcript_admitted"])
        self.assertFalse(self.summary["formal_D7_branching_proof_admitted"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["selector_theorem_closed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_no_target_import_used(self):
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_physics_used"])
        self.assertIn(
            "no_target_physics_or_desired_uniqueness_used",
            self.summary["required_fields"],
        )

    def test_required_fields_include_full_finite_packet(self):
        required = set(self.summary["required_fields"])
        expected = {
            "A_full_summand_list_for_V_omega1_tensor_V_omega7",
            "A_multiplicities_for_all_summands",
            "A_dimensions_for_all_summands",
            "B_full_summand_list_for_V_omega2_tensor_V_omega6",
            "B_multiplicities_for_all_summands",
            "B_dimensions_for_all_summands",
            "irreducibility_of_ker_c_or_full_kernel_decomposition",
            "highest_weight_of_ker_c_or_corrected_weight",
            "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW",
        }
        self.assertLessEqual(expected, required)

    def test_missing_fields_are_explicit(self):
        missing = set(self.summary["missing_fields"])
        expected = {
            "raw_CAS_tool_version_invocation_and_output",
            "formal_D7_branching_proof",
            "A_full_summand_list_for_V_omega1_tensor_V_omega7",
            "B_full_summand_list_for_V_omega2_tensor_V_omega6",
            "B_multiplicities_for_all_summands",
            "B_dimensions_for_all_summands",
            "multiplicity_of_V_omega6_in_B",
            "irreducibility_of_ker_c_or_full_kernel_decomposition",
            "highest_weight_of_ker_c_or_corrected_weight",
        }
        self.assertLessEqual(expected, missing)
        self.assertGreaterEqual(len(missing), 10)

    def test_chirality_only_is_rejected_as_admission_basis(self):
        self.assertTrue(self.summary["chirality_only_rejected_as_admission_basis"])
        rows = self.summary["candidate_rows"]
        chirality_rows = [
            row for row in rows if row["candidate"] == "chirality_exclusions"
        ]
        self.assertEqual(len(chirality_rows), 1)
        self.assertEqual(
            chirality_rows[0]["decision"],
            "rejected_as_chirality_only_admission_basis",
        )
        accepted = set(self.summary["accepted_narrow_positives"])
        self.assertIn(
            "chirality_excludes_V_omega7_from_V_omega2_tensor_V_omega6",
            accepted,
        )
        self.assertNotIn("multiplicity_one_for_V_omega6", accepted)

    def test_candidate_matrix_rejects_all_rows(self):
        rows = self.summary["candidate_rows"]
        self.assertGreaterEqual(len(rows), 5)
        for row in rows:
            self.assertIn("rejected", row["decision"], row)
            self.assertIn("reason", row)
            self.assertTrue(row["reason"])

    def test_fc_gates_remain_blocked(self):
        self.assertFalse(self.summary["all_FC_gates_closed"])
        for key in ("FC_IRR_status", "FC_MULT_status", "FC_HW_status"):
            self.assertIn("blocked", self.summary[key])
            self.assertNotRegex(
                self.summary[key],
                r"\b(closed|verified|resolved|admitted)\b",
            )

    def test_next_object_and_first_obstruction_are_explicit(self):
        self.assertEqual(
            self.summary["next_object"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )
        self.assertIn("B_equals_V_omega2_tensor_V_omega6", self.summary["first_obstruction"])
        self.assertIn("full_summand_list", self.summary["first_obstruction"])
        self.assertIn("multiplicities", self.summary["first_obstruction"])
        self.assertIn("dimensions", self.summary["first_obstruction"])

    def test_promotion_firewall_is_complete(self):
        firewall = self.summary["promotion_firewall"]
        self.assertTrue(firewall)
        for key, value in firewall.items():
            self.assertIs(value, True, key)
        expected = {
            "shiab_existence_not_selector_theorem",
            "chirality_exclusion_not_full_branching_transcript",
            "chirality_only_rejected_as_admission_basis",
            "pseudocode_not_raw_CAS_receipt",
            "target_physics_not_used",
            "proof_restart_blocked",
            "GU_claim_not_promoted",
        }
        self.assertLessEqual(expected, set(firewall))

    def test_no_forbidden_promotion_literals(self):
        forbidden_patterns = [
            r'"accepted_receipt_count"\s*:\s*[1-9]',
            r'"proof_restart_allowed"\s*:\s*true',
            r'"target_import_used"\s*:\s*true',
            r'"raw_CAS_transcript_admitted"\s*:\s*true',
            r'"formal_D7_branching_proof_admitted"\s*:\s*true',
            r"chirality-only\s+(?:proves|closes|admits)",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

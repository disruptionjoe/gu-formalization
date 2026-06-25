import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md"
)

EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_PATH = (
    "explorations/hourly-20260625-1802-cycle2-ig-product-b-first-admission-gate.md"
)
EXPECTED_ARTIFACT_ID = "IG_PRODUCT_B_FIRST_ADMISSION_GATE_1802_C2_L2_V1"


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


class IGProductBFirstAdmissionGateAudit(unittest.TestCase):
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
            self.summary["decision_target"], "IG_PRODUCT_B_FIRST_ADMISSION_GATE"
        )
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_required_gate_flags(self):
        self.assertTrue(self.summary["product_b_first_required"])
        self.assertFalse(self.summary["bypass_allowed"])
        self.assertFalse(self.summary["target_generation_count_used"])
        self.assertFalse(self.summary["transcript_admitted"])
        self.assertFalse(self.summary["accepted_transcript"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])

    def test_specific_bypasses_rejected(self):
        self.assertFalse(self.summary["product_a_partials_bypass_allowed"])
        self.assertFalse(self.summary["chirality_exclusions_bypass_allowed"])
        self.assertFalse(self.summary["desired_multiplicity_bypass_allowed"])
        self.assertFalse(self.summary["target_generation_count_bypass_allowed"])
        self.assertFalse(self.summary["desired_multiplicity_used"])
        self.assertFalse(self.summary["desired_uniqueness_used"])

        bypasses = {row["route"]: row for row in self.summary["bypass_tests"]}
        for route in {
            "Product_A_partials",
            "chirality_exclusions",
            "desired_multiplicity",
            "target_generation_count",
        }:
            self.assertIn(route, bypasses)
            self.assertFalse(bypasses[route]["allowed"])

    def test_fc_gates_remain_blocked(self):
        self.assertEqual(self.summary["FC_IRR_status"], "blocked")
        self.assertEqual(self.summary["FC_MULT_status"], "blocked")
        self.assertEqual(self.summary["FC_HW_status"], "blocked")
        self.assertEqual(self.summary["fc_irr"], "blocked")
        self.assertEqual(self.summary["fc_mult"], "blocked")
        self.assertEqual(self.summary["fc_hw"], "blocked")
        self.assertFalse(self.summary["all_FC_gates_closed"])

    def test_next_object_is_product_b_or_raw_formal_receipt(self):
        next_object = self.summary["next_object"]
        self.assertRegex(
            next_object,
            r"(ProductBFullD7SummandMultiplicityDimensionTableReceipt|RawOrFormalD7BranchingTranscript)",
        )
        self.assertEqual(next_object, self.summary["constructive_next_object"])
        self.assertEqual(
            self.summary["first_missing_proof_object"],
            "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1",
        )

    def test_product_b_not_admitted(self):
        self.assertFalse(self.summary["product_b_full_table_admitted"])
        product_b = self.summary["product_B"]
        self.assertEqual(product_b["expression"], "V(omega_2) tensor V(omega_6)")
        self.assertEqual(product_b["expected_total_dimension"], 5824)
        self.assertFalse(product_b["full_summand_list_admitted"])
        self.assertFalse(product_b["multiplicities_admitted"])
        self.assertFalse(product_b["dimensions_admitted"])
        self.assertFalse(product_b["total_dimension_check_admitted"])
        self.assertFalse(product_b["multiplicity_of_V_omega6_admitted"])

    def test_product_a_packet_not_admitted(self):
        self.assertFalse(self.summary["product_a_kernel_packet_admitted"])
        product_a = self.summary["product_A"]
        self.assertEqual(product_a["expression"], "V(omega_1) tensor V(omega_7)")
        self.assertEqual(product_a["expected_total_dimension"], 896)
        self.assertFalse(product_a["kernel_branch_admitted"])
        self.assertFalse(product_a["cokernel_branch_admitted"])
        self.assertFalse(product_a["ker_c_irreducibility_admitted"])
        self.assertFalse(product_a["ker_c_highest_weight_admitted"])

    def test_proof_restart_and_target_import_firewall(self):
        self.assertFalse(self.summary["K_IG_family_identity_verified"])
        self.assertFalse(self.summary["selector_theorem_closed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["major_GU_claim_promoted"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_physics_used"])
        self.assertIn("transcript_admitted_is_true", self.summary["proof_restart_rule"])

    def test_dependency_order(self):
        order = self.summary["dependency_gate_order"]
        self.assertEqual(
            order[0], "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1"
        )
        self.assertEqual(
            order[1], "ProductAKernelCokernelHighestWeightPacketFor_c_A_to_V_omega6"
        )
        self.assertEqual(order[2], "FC_IRR_FC_MULT_FC_HW_verdicts")
        self.assertEqual(order[3], "K_IG_selector_family_identity_proof_restart")

    def test_forbidden_positive_literals_absent(self):
        forbidden_patterns = [
            r'"product_b_first_required"\s*:\s*false',
            r'"bypass_allowed"\s*:\s*true',
            r'"target_generation_count_used"\s*:\s*true',
            r'"transcript_admitted"\s*:\s*true',
            r'"accepted_receipt_count"\s*:\s*[1-9]',
            r'"proof_restart_allowed"\s*:\s*true',
            r'"FC_IRR_status"\s*:\s*"closed"',
            r'"FC_MULT_status"\s*:\s*"closed"',
            r'"FC_HW_status"\s*:\s*"closed"',
            r'"target_import_used"\s*:\s*true',
            r"target\s+generation\s+count\s+(?:proves|selects|admits|closes)",
            r"desired\s+multiplicity\s+(?:proves|selects|admits|closes)",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

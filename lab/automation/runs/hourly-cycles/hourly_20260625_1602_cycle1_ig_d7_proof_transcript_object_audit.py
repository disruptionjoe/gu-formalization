import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle1-ig-d7-proof-transcript-object.md"
)

EXPECTED_ARTIFACT_ID = "IG_D7_PROOF_TRANSCRIPT_OBJECT_1602_C1_L2_V1"
EXPECTED_RUN_ID = "hourly-20260625-1602"


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


class IGD7ProofTranscriptObjectAudit(unittest.TestCase):
    def setUp(self):
        self.assertTrue(ARTIFACT.exists(), f"missing artifact: {ARTIFACT}")
        self.text, self.summary = load_artifact()

    def test_identity_and_verdict_contract(self):
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertIn("BLOCKED", self.summary["verdict"])
        self.assertIn("NO_FORMAL_D7_PROOF_OR_RAW_TRANSCRIPT", self.summary["verdict"])

    def test_no_receipt_no_restart_no_import(self):
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_selector_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_physics_used"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["K_IG_selector_theorem_closed"])

    def test_no_full_proof_or_transcript_admitted(self):
        self.assertFalse(self.summary["formal_D7_branching_proof_object_present"])
        self.assertFalse(self.summary["raw_CAS_transcript_present"])
        self.assertFalse(self.summary["complete_multiplicity_highest_weight_transcript_present"])
        self.assertFalse(self.summary["formal_hand_proof_admitted"])

    def test_transcript_surfaces_checked_are_explicit(self):
        surfaces = self.summary["transcript_surfaces_checked"]
        self.assertGreaterEqual(len(surfaces), 6)
        required = {
            "canon/shiab-existence-cl95.md",
            "explorations/sc1-shiab-domain-codomain-2026-06-23.md",
            "explorations/sc1-oq1a-d7-clebsch-gordan-cas-2026-06-23.md",
            "DERIVATION-PROGRESS.md",
            "explorations/hourly-20260625-1503-cycle1-ig-d7-multiplicity-transcript.md",
            "explorations/hourly-20260625-1503-cycle2-ig-d7-proof-object-admission.md",
        }
        self.assertLessEqual(required, set(surfaces))

    def test_exact_missing_fields_include_required_math_objects(self):
        missing = " ".join(self.summary["exact_missing_fields"]).lower()
        for term in ("multiplicity", "irreducibility", "highest_weight"):
            self.assertIn(term, missing)
        self.assertIn("dimension_checks", missing)
        self.assertIn("raw_or_formal_provenance", missing)
        self.assertIn("fc_irr", missing)
        self.assertIn("fc_mult", missing)
        self.assertIn("fc_hw", missing)

    def test_next_object_is_explicit_and_constructive(self):
        self.assertEqual(
            self.summary["next_object"],
            "RawOrFormalD7BranchingTranscriptForShiabHomSpace_V1",
        )
        outputs = set(self.summary["next_object_required_outputs"])
        expected_outputs = {
            "A_full_summand_list_with_multiplicities_and_dimensions",
            "B_full_summand_list_with_multiplicities_and_dimensions",
            "ker_c_irreducibility_or_full_kernel_decomposition",
            "ker_c_highest_weight",
            "multiplicity_of_V_omega6_in_B",
            "gate_verdicts_for_FC_IRR_FC_MULT_FC_HW",
            "no_target_physics_or_desired_uniqueness_used",
        }
        self.assertLessEqual(expected_outputs, outputs)

    def test_promotion_firewall_booleans_are_all_true(self):
        firewall = self.summary["promotion_firewall"]
        self.assertIsInstance(firewall, dict)
        self.assertTrue(firewall)
        for key, value in firewall.items():
            self.assertIs(value, True, key)
        for required_key in (
            "shiab_existence_not_selector_theorem",
            "chirality_exclusion_not_multiplicity_proof",
            "pseudocode_not_raw_CAS_transcript",
            "target_physics_not_used",
            "proof_restart_blocked",
        ):
            self.assertIn(required_key, firewall)

    def test_fc_statuses_remain_blocked(self):
        for key in ("FC_IRR_status", "FC_MULT_status", "FC_HW_status"):
            self.assertIn("blocked", self.summary[key])
            self.assertNotRegex(
                self.summary[key],
                r"\b(closed|verified|resolved|admitted)\b",
            )

    def test_no_forbidden_promotion_language(self):
        forbidden_patterns = [
            r"accepted_receipt_count:\s*[1-9]",
            r'"accepted_receipt_count"\s*:\s*[1-9]',
            r"proof_restart_allowed:\s*true",
            r'"proof_restart_allowed"\s*:\s*true',
            r"target_import_used:\s*true",
            r'"target_import_used"\s*:\s*true',
            r"K_IG selector theorem closed",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

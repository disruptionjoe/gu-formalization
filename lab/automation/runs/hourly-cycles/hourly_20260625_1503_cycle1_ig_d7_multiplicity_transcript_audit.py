import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle1-ig-d7-multiplicity-transcript.md"
)

EXPECTED_ARTIFACT_ID = "IG_D7_MULTIPLICITY_TRANSCRIPT_1503_C1_L2_V1"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1503-cycle1-ig-d7-multiplicity-transcript.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1503_cycle1_ig_d7_multiplicity_transcript_audit.py"
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


class IGD7MultiplicityTranscriptAudit(unittest.TestCase):
    def setUp(self):
        self.assertTrue(ARTIFACT.exists(), f"missing artifact: {ARTIFACT}")
        self.text, self.summary = load_artifact()

    def test_frontmatter_and_identity_contract(self):
        self.assertRegex(self.text, r"\A---\n")
        self.assertIn(f'artifact_id: "{EXPECTED_ARTIFACT_ID}"', self.text)
        self.assertIn('verdict: "BLOCKED_NO_RAW_D7_TRANSCRIPT"', self.text)
        self.assertIn(f'owned_path: "{EXPECTED_OWNED_PATH}"', self.text)
        self.assertIn(f'companion_audit: "{EXPECTED_AUDIT}"', self.text)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_required_gate_fields_are_explicit_and_blocked(self):
        for key in ("FC_IRR", "FC_MULT", "FC_HW"):
            self.assertIn(key, self.summary)
            self.assertEqual(self.summary[key]["status"], "blocked")
            self.assertIn("needed_data", self.summary[key])
            self.assertNotRegex(
                json.dumps(self.summary[key]),
                r"\b(closed|verified|resolved)\b",
            )
        self.assertFalse(self.summary["all_FC_gates_closed"])

    def test_cas_availability_and_transcript_presence_are_explicit(self):
        self.assertIn("CAS_tool_availability", self.summary)
        tools = self.summary["CAS_tool_availability"]
        for tool in ("lie", "LiE", "sage", "sage.exe", "sage.bat"):
            self.assertEqual(tools[tool], "not_found_on_path")
        self.assertEqual(tools["wsl"], "present_but_wsl_not_installed")
        self.assertEqual(tools["python"], "present")
        self.assertEqual(tools["python_sympy"], "not_found")

        self.assertIn("transcript_presence", self.summary)
        transcript = self.summary["transcript_presence"]
        self.assertFalse(transcript["local_CAS_transcript_present"])
        self.assertFalse(transcript["repo_local_raw_transcript_present"])
        self.assertFalse(transcript["formal_proof_object_present"])
        self.assertEqual(transcript["repo_local_transcript_paths"], [])

    def test_selector_restart_and_target_import_remain_forbidden(self):
        self.assertEqual(self.summary["accepted_selector_count"], 0)
        self.assertEqual(self.summary["accepted_selectors"], [])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_physics_used"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["selector_theorem_closed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_missing_finite_data_are_specific(self):
        missing = set(self.summary["missing_finite_representation_data"])
        expected = {
            "full_decomposition_of_V_omega1_tensor_V_omega7",
            "irreducibility_of_kernel_of_c",
            "highest_weight_of_kernel_of_c",
            "full_decomposition_of_V_omega2_tensor_V_omega6",
            "multiplicity_of_V_omega6_in_V_omega2_tensor_V_omega6",
            "dimension_checks_for_all_reported_summands",
        }
        self.assertEqual(missing, expected)

    def test_no_forbidden_promotion_language(self):
        forbidden_patterns = [
            r"shiab existence\s+(?:therefore|implies|proves|verifies|closes)",
            r"chirality exclusion\s+(?:therefore|implies|proves|verifies|closes)\s+.*multiplicity",
            r"target physics\s+(?:therefore|implies|proves|selects)",
            r"proof restart allowed:\s*true",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

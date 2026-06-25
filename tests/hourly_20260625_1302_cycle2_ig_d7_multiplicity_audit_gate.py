import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle2-ig-d7-multiplicity-audit-gate.md"
)


def load_json_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("machine-readable JSON summary not found")
    return text, json.loads(match.group(1))


class IGD7MultiplicityAuditGate(unittest.TestCase):
    def setUp(self):
        self.text, self.summary = load_json_summary()

    def test_identity_fields(self):
        self.assertEqual(self.summary["artifact_id"], "IG_D7_MULTIPLICITY_AUDIT_GATE")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_statuses_are_not_inflated_without_transcript(self):
        self.assertFalse(self.summary["computation_transcript_present"])
        self.assertEqual(self.summary["repo_local_transcript_paths"], [])
        self.assertFalse(self.summary["local_computation_run"])
        for key in ("FC_IRR_status", "FC_MULT_status", "FC_HW_status"):
            self.assertIn("blocked", self.summary[key])
            self.assertNotRegex(self.summary[key], r"\b(closed|verified|resolved)\b")
        self.assertFalse(self.summary["all_FC_gates_closed"])
        self.assertIn(
            "missing_transcript_to_computation_verified",
            self.summary["forbidden_promotions"],
        )

    def test_selector_theorem_and_restart_remain_false_until_all_gates_close(self):
        all_gates_closed = self.summary["all_FC_gates_closed"]
        self.assertFalse(all_gates_closed)
        self.assertFalse(self.summary["selector_theorem_closed"])
        self.assertEqual(self.summary["accepted_selector_count"], 0)
        self.assertEqual(self.summary["accepted_selectors"], [])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_target_physics_is_unused(self):
        self.assertFalse(self.summary["target_physics_used"])
        self.assertIn(
            "target_physics_to_source_selector",
            self.summary["forbidden_promotions"],
        )
        self.assertNotRegex(
            self.text,
            r"(?:because|therefore|hence).{0,80}(?:Standard Model|generation count|physics target)",
            re.IGNORECASE | re.DOTALL,
        )

    def test_required_reproducible_packet_is_specific(self):
        fields = set(self.summary["required_reproducible_packet_fields"])
        expected = {
            "tool_name_and_version",
            "root_system_D7_convention",
            "Dynkin_label_convention",
            "raw_commands",
            "raw_output_transcript",
            "full_summand_lists_with_multiplicities",
            "dimension_checks",
            "FC_IRR_verdict",
            "FC_MULT_verdict",
            "FC_HW_verdict",
        }
        self.assertEqual(fields, expected)

    def test_tool_checks_record_absent_lie_and_sage(self):
        tools = {item["tool"]: item["status"] for item in self.summary["computation_tools_checked"]}
        for tool in ("lie", "LiE", "sage", "sage.exe", "sage.bat"):
            self.assertEqual(tools[tool], "not_found_on_path")
        self.assertEqual(tools["wsl"], "present_but_wsl_not_installed")
        self.assertEqual(tools["python"], "present_but_not_a_D7_Clebsch_Gordan_tool")

    def test_no_compatibility_or_conditional_promotion_phrases(self):
        forbidden_patterns = [
            r"compatib(?:le|ility)\s+(?:therefore|implies|proves|derives)",
            r"host(?:ed|ing)\s+(?:therefore|implies|proves|derives|selects)",
            r"conditional(?:ly)?\s+(?:therefore|implies|proves|derives|verifies)",
            r"chirality\s+exclusion\s+(?:therefore|implies|proves|derives)\s+(?:multiplicity|uniqueness)",
            r"missing\s+transcript\s+(?:therefore|implies|proves|derives)",
            r"target physics\s+(?:therefore|implies|proves|derives|selects)",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

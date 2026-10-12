#!/usr/bin/env python3
"""Regression tests for the read-only partial reader, not scientific validity."""
from contextlib import redirect_stdout, redirect_stderr
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("research_context", ROOT / "scripts/research_context.py")
READER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(READER)


def state():
    return {
        "revision_basis": "fixture",
        "purpose": "Test the actual object.",
        "current_result": {"status": "conditional"},
        "research_method_control": "source fidelity remains required",
        "current_question": "Current question, including its scope.",
        "next_condition": "Next candidate, not the only candidate.",
        "acceptance": "Scoped evidence",
        "contribution_path": "CONTRIBUTING.md",
        "what_needs_joe": "Nothing in this fixture",
    }


VERIFICATION = "# Verification\n\n## First section\nExact evidence.\n\n## Older section\nOlder evidence.\n"


class PartialContextTests(unittest.TestCase):
    def test_history_growth_does_not_expand_entry_or_delete_history(self):
        s = state()
        original = s["current_question"]
        baseline = READER.render_context(s, VERIFICATION)
        s["current_question"] += "\n" + "HISTORICAL_QUESTION\n" * 10000
        s["next_condition"] += "\nHISTORICAL_CONTINUATION"
        historical = s["current_question"]
        output = READER.render_context(s, VERIFICATION)
        self.assertEqual(output, baseline)
        self.assertEqual(s["current_question"], historical)
        self.assertIn(original, output)
        self.assertNotIn("HISTORICAL_QUESTION", output)

    def test_partial_fields_and_expansion_paths_are_explicit(self):
        output = READER.render_context(state(), VERIFICATION)
        data = yaml.safe_load(output.split("```yaml\n", 1)[1].split("```", 1)[0])
        self.assertNotIn("current_question", data)
        self.assertEqual(data["current_question_lead_partial"], state()["current_question"])
        self.assertIn("next_condition_lead_partial", data)
        self.assertEqual(data["research_method_control"], state()["research_method_control"])
        self.assertEqual(data["acceptance"], state()["acceptance"])
        self.assertEqual(data["what_needs_joe"], state()["what_needs_joe"])
        self.assertIn("not retired", output)
        self.assertIn("does not select work", output)
        for path in data["expanded_reading"].values():
            self.assertTrue((ROOT / path).is_file(), path)

    def test_leading_blank_lines_and_long_lead_are_not_silently_clipped(self):
        s = state()
        lead = "λ=1/2; source scope stays intact. " * 100
        s["current_question"] = "\n\n" + lead + "\nold paragraph"
        data = yaml.safe_load(READER.render_context(s, VERIFICATION).split("```yaml\n")[1].split("```")[0])
        self.assertEqual(data["current_question_lead_partial"], lead)

    def test_first_section_keeps_subheadings_and_fenced_headings(self):
        text = "# Title\n## First\n### Child\n```md\n## Inside fence\n```\nStill first.\n## Second\nHidden."
        section = READER.first_verification_section(text)
        self.assertIn("## Inside fence", section)
        self.assertIn("### Child", section)
        self.assertIn("Still first.", section)
        self.assertNotIn("Hidden.", section)

    def test_invalid_state_and_incomplete_verification_fail_visibly(self):
        for field in ("purpose", "current_question", "next_condition"):
            s = state()
            s[field] = "  "
            with self.assertRaises(ValueError):
                READER.render_context(s, VERIFICATION)
        with self.assertRaises(ValueError):
            READER.render_context([], VERIFICATION)
        s = state()
        s["current_result"] = None
        with self.assertRaises(ValueError):
            READER.render_context(s, VERIFICATION)
        for text in ("# No section", "## First\n```\nunclosed"):
            with self.assertRaises(ValueError):
                READER.first_verification_section(text)

    def test_main_reads_fresh_files_without_writing(self):
        original_root = READER.ROOT
        try:
            with tempfile.TemporaryDirectory() as directory:
                READER.ROOT = Path(directory)
                s = state()
                (READER.ROOT / "VERIFICATION.md").write_text(VERIFICATION)
                for question in ("First live question", "Changed live question"):
                    s["current_question"] = question
                    (READER.ROOT / "CURRENT-STATE.yaml").write_text(yaml.safe_dump(s))
                    before = {p.name: p.read_bytes() for p in READER.ROOT.iterdir()}
                    capture = io.StringIO()
                    with redirect_stdout(capture):
                        self.assertEqual(READER.main(), 0)
                    self.assertIn(question, capture.getvalue())
                    self.assertEqual(before, {p.name: p.read_bytes() for p in READER.ROOT.iterdir()})
                (READER.ROOT / "CURRENT-STATE.yaml").write_text("[invalid yaml")
                with redirect_stderr(io.StringIO()) as errors:
                    self.assertEqual(READER.main(), 1)
                self.assertIn("research_context:", errors.getvalue())
        finally:
            READER.ROOT = original_root


if __name__ == "__main__":
    unittest.main()

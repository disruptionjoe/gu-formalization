#!/usr/bin/env python3
"""Read-only context projection fixtures; never scientific-validity certification."""
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("research_context", ROOT / "scripts/research_context.py")
READER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(READER)
PACKET = "lab/process/work-packets/fixture.md"
VERIFICATION = "# Verification\n\n## First section\nExact evidence.\n\n## Older section\nOlder evidence.\n"


def state():
    return {
        "revision_basis": "fixture-base", "purpose": "Test the actual object.",
        "current_result": {"status": "conditional"},
        "research_method_control": {"work_posture": {"default_scale": "big_wave"}},
        "current_question": "Historical lead, not a selection owner.",
        "next_condition": "Counter is16; repeat old step5.",
        "program_focus": {"version": "fixture-current", "authority": "Joe fixture",
            "goal": "Resolve a source-required question.", "run_selection": ["Existing rule2"],
            "priority_packets": [PACKET], "priority_packet_selection": {"old_directed_override": "Historical exception"}},
        "what_needs_joe": "none",
    }


def matrix():
    return {
        "program_run_counter": {"count": 39},
        "directed_lc_carry_fixture": {"status": "consumed", "due_counter": 35},
        "cells": [{"row": "P3", "column": "global_index", "status": "open", "packet": PACKET,
            "packet_step_status": "ready", "next_run": "Stale copied instruction, not selection authority.",
            "evidence": ["explorations/fixture-result.md"],
            "native_domain": {"blocked_on": {"id": "NATIVE-DOMAIN", "reason": "Actual closed domain missing"}}}],
        "intersections": [{"id": "X-P1-P2-P3", "status": "open", "packet": PACKET,
                            "evidence": ["lab/sources/source-claim-register.yaml#SC-CHI-01"]}],
        "source_relevance_assumption_view": {"entries": [{"question": "Does the count use this grading?",
            "source_claim_refs": ["lab/sources/source-claim-register.yaml#SC-CHI-01"],
            "evidence": ["explorations/fixture-result.md"], "source_bridge": {"status": "conditional"}}]},
    }


def bets():
    return {"bets": [{"id": "BET-2PLUS1", "status": "active", "runs_used": 2,
        "question": "Source-native count?", "result": {"remaining_runs": 22, "next_condition": "Supply a domain"}},
        {"id": "BET-OLD", "status": "closed", "runs_used": 24}], "closed_bets": []}


def register():
    return {"claims": [{"id": "SC-CHI-01", "polarity": "ASSERTS", "claim": "Non-chiral total, observed split.",
        "verbatim": "The exact source quotation.", "locus": {"source": "draft-2021", "page": 52,
        "extraction": "lab/sources/extraction.md:140"}, "grade": "extraction-verified",
        "adherence": {"adherence": "ADHERED", "pinned_at": "old-evidence-pin", "date": "2026-08-11"},
        "phase_reading_reconciliation": {"receipt": "explorations/correction.md", "reading": "Conditional, not a universal no-go."}}]}


TABLE = """---
status: process
---
# Packet
| Step | Status | Target / tier |
|---|---|---|
| 0 | done | P3 / T3 |
| 5 | done | P3 / T3 |
"""


def rendered(**kwargs):
    inputs = dict(matrix=matrix(), bets=bets(), register=register(),
                  packets={PACKET: READER.packet_projection(TABLE, PACKET)}, revision="fixture-head")
    inputs.update(kwargs)
    return READER.render_context(state(), VERIFICATION, **inputs)


def data(output):
    return yaml.safe_load(output.split("```yaml\n", 1)[1].split("```", 1)[0])


class PartialContextTests(unittest.TestCase):
    def test_stale_lead_cannot_override_live_counter_or_carry(self):
        output = rendered()
        view = data(output)
        self.assertEqual(view["live_facts"]["counter"], 39)
        self.assertTrue(view["live_facts"]["ordinary_LC_arithmetic_condition"])
        self.assertEqual(view["live_facts"]["carry_records"]["directed_lc_carry_fixture"]["status"], "consumed")
        self.assertNotIn("Counter is16", output)
        self.assertNotIn("selected_target", output)
        self.assertIn("does not select work", output)
        self.assertEqual(view["snapshot"]["checked_out_revision"], "fixture-head")
        self.assertEqual(view["snapshot"]["state_revision_basis"], "fixture-base")
        self.assertEqual(view["live_facts"]["active_bets"], [{"id": "BET-2PLUS1", "runs_used": 2, "remaining_runs": 22}])

    def test_history_is_explicit_and_never_expands_default_view(self):
        s = state()
        baseline = READER.render_context(s, VERIFICATION)
        s["current_question"] += "\n" + "HISTORICAL_QUESTION\n" * 10000
        s["next_condition"] += "\nHISTORICAL_CONTINUATION"
        self.assertEqual(READER.render_context(s, VERIFICATION), baseline)
        full = data(READER.render_context(s, VERIFICATION, history=True))
        historical = full["history_not_live_selection"]
        self.assertIn("Counter is16", historical["next_condition_lead_partial"])
        self.assertIn("old_directed_override", historical["program_focus_provenance"]["priority_packet_selection"])
        self.assertIn("not retired", baseline)

    def test_cell_query_uses_packet_status_and_preserves_native_burden(self):
        view = data(rendered(target="P3xglobal_index"))["requested_context"]
        self.assertEqual(view["target"], "P3xglobal_index")
        self.assertEqual(view["packet_records"][0]["ready_steps"], [])
        self.assertEqual(view["packet_records"][0]["step_summary"], "all listed steps done")
        self.assertEqual(view["declared_missing_inputs"]["native_domain.blocked_on"]["id"], "NATIVE-DOMAIN")
        self.assertEqual(view["source_claims"][0]["polarity"], "ASSERTS")
        self.assertIn("explorations/fixture-result.md", view["linked_evidence_and_corrections"])
        self.assertNotIn("packet_step_status", view["recorded_target_fields"])

    def test_claim_query_keeps_quote_custody_correction_and_adherence_distinct(self):
        view = data(rendered(claim="SC-CHI-01"))["requested_context"]
        card = view["source_claim"]
        self.assertEqual(card["polarity"], "ASSERTS")
        self.assertEqual(card["verbatim"], "The exact source quotation.")
        self.assertEqual(card["locus"]["page"], 52)
        self.assertIn("explorations/correction.md", card["linked_evidence_and_custody"])
        self.assertIn("phase_reading_reconciliation", card["recorded_corrections_and_reconciliations"])
        self.assertEqual(card["adherence_record"]["pinned_at"], "old-evidence-pin")
        self.assertIn("not physical verification", card["ceiling"])
        self.assertIn("X-P1-P2-P3", view["targets_with_explicit_claim_reference"])

    def test_bet_and_intersection_queries_and_unknowns(self):
        bet = data(rendered(target="BET-2PLUS1"))["requested_context"]
        self.assertEqual(bet["recorded_result"]["remaining_runs"], 22)
        self.assertEqual(data(rendered(target="X-P1-P2-P3"))["requested_context"]["recorded_target_fields"]["status"], "open")
        for query in ({"target": "P3xwrong"}, {"claim": "SC-CHI-999"}, {"target": "BET-2PLUS1", "claim": "SC-CHI-01"}):
            with self.assertRaises(ValueError):
                rendered(**query)

    def test_yaml_packet_preserves_blocked_prerequisites_without_promoting_ready(self):
        text = """---
operational_state: blocked
---
```yaml
packet_status: parked_pending_input
steps:
- id: 1
  status: done
- id: 2
  status: blocked
  blocked_on: source operator
  depends_on: [1]
```
"""
        packet = READER.packet_projection(text, PACKET)
        self.assertEqual(packet["declared_status"], "parked_pending_input")
        self.assertEqual(packet["blocked_steps"], [2])
        self.assertEqual(packet["ready_steps"], [])
        self.assertEqual(packet["blocked_step_dependencies"]["2.blocked_on"], "source operator")
        unknown = READER.packet_projection("# An unstructured packet", PACKET)
        self.assertIn("no readiness inferred", unknown["readiness_note"])
        ready = READER.packet_projection("| Step | Status |\n|---|---|\n| 3 | ready |\n", PACKET)
        self.assertEqual(ready["ready_steps"], ["3"])

    def test_rendering_does_not_mutate_inputs_or_invent_absent_live_data(self):
        s, m, b, r = state(), matrix(), bets(), register()
        before = deepcopy((s, m, b, r))
        READER.render_context(s, VERIFICATION, matrix=m, bets=b, register=r, claim="SC-CHI-01")
        self.assertEqual((s, m, b, r), before)
        view = data(READER.render_context(s, VERIFICATION))
        self.assertIsNone(view["live_facts"]["counter"])
        self.assertIsNone(view["live_facts"]["ordinary_LC_arithmetic_condition"])
        self.assertIn("not supplied", view["live_facts"]["availability"])
        for path in view["expanded_reading"].values():
            self.assertTrue((ROOT / path).is_file(), path)

    def test_legacy_section_helper_keeps_fenced_headings(self):
        text = "# Title\n## First\n### Child\n```md\n## Inside fence\n```\nStill first.\n## Second\nHidden."
        section = READER.first_verification_section(text)
        self.assertIn("## Inside fence", section)
        self.assertIn("### Child", section)
        self.assertIn("Still first.", section)
        self.assertNotIn("Hidden.", section)
        for text in ("# No section", "## First\n```\nunclosed"):
            with self.assertRaises(ValueError):
                READER.first_verification_section(text)

    def test_invalid_state_fails_visibly(self):
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

    def test_cli_reads_fresh_files_and_unknown_query_writes_nothing(self):
        original_root = READER.ROOT
        try:
            with tempfile.TemporaryDirectory() as directory:
                READER.ROOT = Path(directory)
                files = {"CURRENT-STATE.yaml": yaml.safe_dump(state()), READER.MATRIX: json.dumps(matrix()),
                         READER.BETS: json.dumps(bets()), READER.SOURCES: yaml.safe_dump(register()), PACKET: TABLE}
                for name, text in files.items():
                    path = READER.ROOT / name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(text)
                def snapshot():
                    return {str(p.relative_to(READER.ROOT)): p.read_bytes() for p in READER.ROOT.rglob("*") if p.is_file()}
                for count in (39, 40):
                    m = matrix()
                    m["program_run_counter"]["count"] = count
                    (READER.ROOT / READER.MATRIX).write_text(json.dumps(m))
                    before = snapshot()
                    capture = io.StringIO()
                    with redirect_stdout(capture):
                        self.assertEqual(READER.main([]), 0)
                    self.assertEqual(data(capture.getvalue())["live_facts"]["counter"], count)
                    self.assertEqual(snapshot(), before)
                before = snapshot()
                with redirect_stderr(io.StringIO()) as errors:
                    self.assertEqual(READER.main(["--target", "NOT-A-TARGET"]), 1)
                self.assertIn("unknown target", errors.getvalue())
                self.assertEqual(snapshot(), before)
                (READER.ROOT / "CURRENT-STATE.yaml").write_text("[invalid yaml")
                with redirect_stderr(io.StringIO()) as errors:
                    self.assertEqual(READER.main([]), 1)
                self.assertIn("research_context:", errors.getvalue())
        finally:
            READER.ROOT = original_root


if __name__ == "__main__":
    unittest.main()

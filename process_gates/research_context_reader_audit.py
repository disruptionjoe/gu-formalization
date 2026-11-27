#!/usr/bin/env python3
"""Read-only context projection fixtures; never scientific-validity certification."""
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
import importlib.util
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

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


class ReuseContextTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.report = self.root / "explorations/fixture-result.md"
        self.report.parent.mkdir()
        self.report.write_text("A conditional fixture result.\n")
        self.probe = self.root / "tests/fixture-verifier.py"
        self.probe.parent.mkdir()
        self.probe.write_text("raise RuntimeError('cached verifier must never be imported or executed')\n")
        self.receipt = self.root / "lab/process/fixture-receipt.json"
        self.receipt.parent.mkdir(parents=True)
        self.receipt.write_text(json.dumps({"status": "PASS", "scope": "recorded fixture only"}))
        self.signature = {"object": "Riemann restriction", "carrier": "real K77 spin module",
                          "convention": {"adjoint": "B-skew", "action_owner": "one-third cubic"},
                          "class": "fixed linear Spin-equivariant", "premises": ["full translation tangent"]}
        self.verifier = {"command": "python3", "args": ["tests/fixture-verifier.py", "--exact"],
                         "environment": {"python": "fixture-version", "identity_status": "recorded fixture"}}
        self.entry = {"id": "fixture-result", "kind": "result", "owner_ref": "explorations/fixture-result.md",
                      "tested_statement": "A literal cyclic-kernel exclusion under fixed premises.",
                      "signature": self.signature, "attributed_status": "recorded PASS; conditional result",
                      "status_ref": "lab/process/fixture-receipt.json", "source_bridge_ref": "explorations/fixture-result.md#bridge",
                      "certificate_refs": [], "control_refs": [], "survivors_ref": "explorations/fixture-result.md#survivors",
                      "reopen_condition_ref": None, "superseded_by": None,
                      "cache": {"artifacts": [{"path": str(path.relative_to(self.root)),
                                                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                                               for path in (self.report, self.probe)],
                                "verifier": self.verifier, "receipt_ref": "lab/process/fixture-receipt.json"}}
        self.index = {"schema_version": "1.0", "coverage": {"scope": "Fixture only; no complete coverage claim"},
                      "entries": [self.entry]}

    def lookup(self, query="fixture-result", **kwargs):
        return READER.reuse_projection(self.index, query, root=self.root, **kwargs)

    def first(self, **kwargs):
        return self.lookup(**kwargs)["matches"][0]

    def test_literal_search_and_exact_id_have_no_semantic_selection(self):
        old = deepcopy(self.entry)
        old.update(id="fixture-result-old", kind="dead_end", superseded_by="fixture-result")
        self.index["entries"].insert(0, old)
        self.assertEqual([x["entry"]["id"] for x in self.lookup()["matches"]], ["fixture-result"])
        both = self.lookup("CYCLIC-KERNEL")
        self.assertEqual([x["entry"]["id"] for x in both["matches"]], ["fixture-result-old", "fixture-result"])
        self.assertIn("tested_statement", both["matches"][0]["matched_fields"])
        self.assertEqual(both["matches"][0]["entry"]["superseded_by"], "fixture-result")
        self.assertIn("index order retained", both["matching"])
        self.assertEqual(self.lookup("cyclic.*kernel")["match_count"], 0)
        self.assertEqual(self.lookup("equivalent theorem")["match_count"], 0)
        self.assertIn("partial index", self.lookup("no match")["absence_ceiling"])
        self.assertNotIn("selected_target", json.dumps(both))

    def test_signature_digest_is_declaration_equality_not_coverage(self):
        hypothesis = {"signature": dict(reversed(list(self.signature.items())))}
        comparison = self.first(hypothesis=hypothesis)["signature_comparison"]
        self.assertEqual(comparison["comparison"], "equal_declarations")
        self.assertEqual(comparison["recorded"]["sha256"], comparison["hypothesis"]["sha256"])
        self.assertEqual(comparison["applicability"], "not_certified")
        self.assertTrue(comparison["author_validation_required"])
        for key, replacement in (("adjoint", "Hermitian"), ("action_owner", "different quadratic action")):
            hypothesis = {"signature": deepcopy(self.signature)}
            hypothesis["signature"]["convention"][key] = replacement
            comparison = self.first(hypothesis=hypothesis)["signature_comparison"]
            self.assertEqual(comparison["comparison"], "different_declarations")
            self.assertEqual(comparison["different_fields"], ["convention"])
            self.assertNotEqual(comparison["recorded"]["sha256"], comparison["hypothesis"]["sha256"])

    def test_unknown_signature_cannot_become_applicable_even_when_identical(self):
        for value in (None, {}, 7, {**self.signature, "carrier": "unknown until supplied"},
                      {**self.signature, "premises": [{"source_bridge": None}]},
                      {key: value for key, value in self.signature.items() if key != "class"}):
            with self.subTest(value=value):
                self.entry["signature"] = value
                comparison = self.first(hypothesis={"signature": value})["signature_comparison"]
                self.assertEqual(comparison["comparison"], "unknown")
                self.assertTrue(comparison["recorded"]["unknown_fields"])
                self.assertEqual(comparison["applicability"], "not_certified")

    def test_cache_is_opt_in_and_never_fresh_verification(self):
        with patch.object(Path, "open", side_effect=AssertionError("default lookup must not hash files")):
            cache = self.first()["cache"]
        self.assertEqual(cache["hash_state"], "not_checked")
        with patch.object(READER.subprocess, "run", side_effect=AssertionError("no verifier execution")):
            cache = self.first(check_cache=True, hypothesis={"signature": self.signature, "verifier": self.verifier})["cache"]
        self.assertEqual(cache["hash_state"], "current")
        self.assertEqual(cache["cache_state"], "hash_current")
        self.assertIn("PASS", cache["recorded"]["attributed_status"])
        self.assertFalse(cache["freshly_executed"])
        self.assertEqual(cache["fresh_verification"], "not_run")
        self.assertEqual(cache["expected_verifier"]["comparison"], "equal_declarations")

    def test_stale_hash_and_expected_arguments_are_visible(self):
        expected = deepcopy(self.verifier)
        expected["args"].append("--different-carrier")
        cache = self.first(check_cache=True, hypothesis={"signature": self.signature, "verifier": expected})["cache"]
        self.assertEqual(cache["hash_state"], "current")
        self.assertEqual(cache["cache_state"], "stale")
        self.assertEqual(cache["expected_verifier"]["comparison"], "mismatch")
        self.assertEqual(cache["expected_verifier"]["different_fields"], ["args"])
        self.entry["cache"]["verifier"]["environment"] = {"status": "unknown"}
        cache = self.first(check_cache=True, hypothesis={"signature": self.signature, "verifier": expected})["cache"]
        self.assertEqual(cache["expected_verifier"]["comparison"], "mismatch")
        self.assertEqual(cache["expected_verifier"]["field_comparisons"]["args"], "mismatch")
        self.assertEqual(cache["expected_verifier"]["field_comparisons"]["environment"], "unknown")
        self.assertEqual(cache["cache_state"], "stale")
        self.report.write_text("Modified theorem premises.\n")
        cache = self.first(check_cache=True)["cache"]
        self.assertEqual(cache["hash_state"], "stale")
        self.assertEqual(cache["cache_state"], "stale")
        self.assertNotEqual(cache["artifacts"][0]["recorded_sha256"], cache["artifacts"][0]["current_sha256"])
        self.assertFalse(cache["freshly_executed"])

    def test_missing_cache_identity_or_inputs_is_unknown(self):
        baseline = deepcopy(self.entry["cache"])
        mutations = [lambda c: c.pop("verifier"), lambda c: c["verifier"].pop("args"),
                     lambda c: c["verifier"].update(environment={"status": "unknown"}),
                     lambda c: c.pop("artifacts"), lambda c: c["artifacts"][0].pop("sha256"),
                     lambda c: c.pop("receipt_ref")]
        for mutate in mutations:
            self.entry["cache"] = deepcopy(baseline)
            mutate(self.entry["cache"])
            cache = self.first(check_cache=True)["cache"]
            self.assertEqual(cache["cache_state"], "unknown")
            self.assertTrue(cache["unknown_fields"])
            self.assertFalse(cache["freshly_executed"])
        self.entry["cache"] = deepcopy(baseline)
        self.entry["cache"]["verifier"]["environment"] = {"status": "unknown"}
        self.probe.write_text("Drift despite unknown verifier environment.\n")
        self.assertEqual(self.first(check_cache=True)["cache"]["cache_state"], "stale")

    def test_reference_traversal_and_symlink_escapes_are_rejected_even_off_query(self):
        other = deepcopy(self.entry)
        other["id"] = "unmatched"
        self.index["entries"].append(other)
        for ref in ("../outside.md", "/tmp/outside.md", "C:\\outside.md", "lab/../../outside.md"):
            other["owner_ref"] = ref
            with self.subTest(ref=ref), self.assertRaises(ValueError):
                self.lookup()
        other["owner_ref"] = self.entry["owner_ref"]
        other["exclusions"] = [{"statement": "historical exclusion", "owner_ref": "../outside.md"}]
        with self.assertRaises(ValueError):
            self.lookup()
        other.pop("exclusions")
        with tempfile.TemporaryDirectory() as external:
            (self.root / "escape").symlink_to(external, target_is_directory=True)
            other["cache"]["artifacts"][0]["path"] = "escape/input.json"
            with self.assertRaises(ValueError):
                self.lookup()

    def test_cli_reuse_reads_only_index_hypothesis_and_opt_in_artifacts(self):
        index_path = self.root / READER.REUSE_INDEX
        index_path.write_text(json.dumps(self.index))
        hypothesis = self.root / "hypothesis.json"
        hypothesis.write_text(json.dumps({"signature": self.signature, "verifier": self.verifier}))
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        with patch.object(READER, "ROOT", self.root), patch.object(READER.subprocess, "run", side_effect=AssertionError("reuse needs no execution")):
            capture = io.StringIO()
            with redirect_stdout(capture):
                self.assertEqual(READER.main(["--reuse", "fixture-result", "--hypothesis", str(hypothesis), "--check-cache", "--history"]), 0)
            view = data(capture.getvalue())["requested_reuse"]
            self.assertEqual(view["match_count"], 1)
            self.assertFalse(view["matches"][0]["cache"]["freshly_executed"])
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                READER.main(["--check-cache"])
            hypothesis.write_text("[]")
            with redirect_stderr(io.StringIO()) as error:
                self.assertEqual(READER.main(["--reuse", "fixture-result", "--hypothesis", str(hypothesis)]), 1)
            self.assertIn("hypothesis JSON must be an object", error.getvalue())
        before.pop("hypothesis.json")
        after = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file() and p != hypothesis}
        self.assertEqual(before, after)

    def test_index_schema_and_duplicate_ids_fail_visibly(self):
        self.index["entries"].append(deepcopy(self.entry))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.lookup()
        self.index["schema_version"] = "unknown"
        with self.assertRaisesRegex(ValueError, "schema_version"):
            self.lookup()

    def test_curated_index_loads_through_the_same_read_only_projection(self):
        index = json.loads((ROOT / READER.REUSE_INDEX).read_text())
        before = deepcopy(index)
        for entry in index["entries"]:
            view = READER.reuse_projection(index, entry["id"], root=ROOT)
            self.assertEqual(view["match_count"], 1)
            self.assertEqual(view["matches"][0]["entry"], entry)
            self.assertEqual(view["matches"][0]["cache"]["hash_state"], "not_checked")
            self.assertFalse(view["matches"][0]["cache"]["freshly_executed"])
        self.assertEqual(index, before)


if __name__ == "__main__":
    unittest.main()

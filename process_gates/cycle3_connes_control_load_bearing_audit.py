#!/usr/bin/env python3
"""Audit the Cycle 3 finite Connes-control load-bearing artifact.

This is a structural documentation audit. It checks that the artifact makes a
decision, preserves the load-bearing/comparator split, keeps the GU
quaternionic/Type II1 distinction visible, includes rollback conditions, and
does not promote current SM recovery to a derivation.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "type-ii1-spectral" / "cycle3-connes-control-load-bearing-audit-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Load-Bearing Dependencies On Finite Connes Control",
    "## 3. Comparator/Control Uses That Are Not Load-Bearing",
    "## 4. What Breaks If Finite Control Is Relaxed",
    "## 5. Reframed Requirement If GU's Quaternionic/Type II1 Structure Is Primary",
    "## 6. First Exact Obstruction Or Decision Point",
    "## 7. Impact For Type II1/SM Selector Claims",
    "## 8. Next Meaningful Audit Or Computation",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_TERMS = [
    "finite Connes control",
    "Type II1",
    "quaternionic",
    "twisted real structure",
    "load-bearing/comparator distinction",
    "Mission A",
    "Mission B",
    "Rollback conditions",
]

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bSM is derived\b",
    r"\bStandard Model is derived\b",
    r"\bthe SM has been derived\b",
    r"\bthe Standard Model has been derived\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing audit artifact: {DOC}") from exc


def extract_json_summary(text: str) -> dict[str, Any]:
    marker = "## 9. Machine-Readable JSON Summary"
    if marker not in text:
        raise AssertionError("missing JSON summary heading")
    tail = text.split(marker, 1)[1]
    match = re.search(r"```json\s*(\{.*?\})\s*```", tail, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing fenced JSON summary block")
    return json.loads(match.group(1))


class Cycle3ConnesControlLoadBearingAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_json_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_core_terms_are_visible(self) -> None:
        lowered = self.text.lower()
        for term in REQUIRED_TERMS:
            self.assertIn(term.lower(), lowered)

    def test_verdict_is_explicit_and_matches_json(self) -> None:
        self.assertIn("**Verdict: CONDITIONAL_REFRAME.**", self.text)
        self.assertEqual(self.summary["verdict"], "CONDITIONAL_REFRAME")
        self.assertIn(
            "finite_Connes_control_is_load_bearing",
            self.summary["explicit_verdict"],
        )

    def test_load_bearing_and_comparator_buckets_are_nonempty(self) -> None:
        load_section = self.text.split(
            "## 2. Load-Bearing Dependencies On Finite Connes Control", 1
        )[1].split("## 3. Comparator/Control Uses That Are Not Load-Bearing", 1)[0]
        comparator_section = self.text.split(
            "## 3. Comparator/Control Uses That Are Not Load-Bearing", 1
        )[1].split("## 4. What Breaks If Finite Control Is Relaxed", 1)[0]

        for item in ["TYPEII1-HOST", "Connes-channel SM shadow", "Twisted-real-structure CC contact"]:
            self.assertIn(item, load_section)
        for item in ["GU quaternionic carrier", "Mission B semifinite NCG machinery"]:
            self.assertIn(item, comparator_section)

    def test_reframed_requirement_separates_mission_a_and_b(self) -> None:
        self.assertEqual(
            self.summary["reframed_requirement"],
            "finite_control_shadow_or_declared_replacement_shadow",
        )
        mission_split = self.summary["mission_split"]
        self.assertIn("GU_reconstruction", mission_split["mission_a"])
        self.assertIn("independent_math", mission_split["mission_b"])

    def test_no_sm_derivation_is_claimed(self) -> None:
        self.assertIs(self.summary["no_sm_derivation_claim"], True)
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text), pattern)
        self.assertIn("This artifact does not promote any Standard Model derivation", self.text)

    def test_rollback_conditions_and_decision_points_are_machine_readable(self) -> None:
        self.assertGreaterEqual(len(self.summary["rollback_conditions"]), 4)
        self.assertIn("FC_EPSILON_fails", self.summary["rollback_conditions"])
        self.assertIn(
            "exact_finite_Connes_channel_shadow_vs_GU_native_replacement_shadow",
            self.summary["first_decision_point"],
        )
        self.assertIn(
            "FC_EPSILON_verify_J_twisted_D_GU_equals_plus_D_GU_J_twisted_in_M64H",
            self.summary["first_obstructions"],
        )
        self.assertIn(
            "A_F_selector_without_forbidden_target_input",
            self.summary["first_obstructions"],
        )

    def test_type_ii1_selector_status_is_not_promoted(self) -> None:
        self.assertIn("current_instantiated_selectors_remain_no_go_or_host_only", self.summary["type_ii1_selector_impact"])
        self.assertIn("TYPEII1-SELECTOR", self.text)
        self.assertIn("negative filter", self.text)
        self.assertIn("fixed-data rigidity", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)

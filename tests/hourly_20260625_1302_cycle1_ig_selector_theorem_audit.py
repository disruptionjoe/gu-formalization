import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1302-cycle1-ig-selector-theorem.md"


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


class IGSelectorTheoremAudit(unittest.TestCase):
    def setUp(self):
        self.text, self.data = load_json_summary()

    def test_identity_fields(self):
        self.assertEqual(
            self.data["artifact_id"],
            "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
        )
        self.assertEqual(self.data["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.data["cycle"], 1)
        self.assertEqual(self.data["lane"], 2)

    def test_rival_rows_examined_match_0803_matrix(self):
        expected = {
            "displayed_or_canon_shiab_clifford_contraction",
            "exterior_covariant_derivative",
            "einstein_ricci_contraction_analog",
            "hodge_star_or_dimension_shift_analog",
            "symmetric_product_or_derivative",
            "projection_dependent_shiab_variant",
            "lower_order_dressed_variant",
            "oxford_visual_formula_variant",
            "ptuj_missing_sheet_variant",
            "ucsd_middle_map_variant",
        }
        self.assertEqual(set(self.data["rival_rows_examined"]), expected)

    def test_source_natural_eliminations_are_explicit_and_not_inflated(self):
        eliminations = self.data["source_natural_eliminations"]
        self.assertEqual(self.data["source_natural_elimination_count"], len(eliminations))
        self.assertEqual(len(eliminations), 2)
        self.assertFalse(self.data["source_natural_eliminations_are_full_rival_rows"])
        self.assertEqual(self.data["rival_row_eliminations"], [])
        self.assertEqual(self.data["rival_row_elimination_count"], 0)
        for item in eliminations:
            self.assertIn("id", item)
            self.assertIn("scope", item)
            self.assertIn("source_basis", item)
            self.assertFalse(item["eliminates_full_0803_rival_row"])

    def test_no_proof_restart_without_real_selector(self):
        self.assertFalse(self.data["theorem_closed"])
        self.assertEqual(self.data["accepted_selector_count"], 0)
        self.assertEqual(self.data["accepted_selectors"], [])
        self.assertFalse(self.data["proof_restart_allowed"])
        self.assertFalse(self.data["claim_promotion_allowed"])

    def test_ptuj_formula_packet_not_assumed(self):
        self.assertFalse(self.data["PTUJ_formula_packet_assumed"])
        self.assertFalse(self.data["target_physics_used"])
        self.assertIn(
            "PTUJ_locator_to_formula_packet",
            self.data["forbidden_promotions"],
        )

    def test_no_compatibility_or_hosting_promotion_phrases(self):
        forbidden_patterns = [
            r"compatib(?:le|ility)\s+(?:therefore|implies|proves|derives)",
            r"host(?:ed|ing)\s+(?:therefore|implies|proves|derives|selects)",
            r"existence\s+(?:therefore|implies|proves|derives)\s+selection",
            r"PTUJ\s+(?:therefore|implies|proves|derives)",
            r"target physics\s+(?:therefore|implies|proves|derives)",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

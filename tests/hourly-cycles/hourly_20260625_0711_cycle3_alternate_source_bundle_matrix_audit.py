import json
import re
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0711-cycle3-alternate-source-bundle-matrix.md"


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise AssertionError("JSON summary block not found")
    return json.loads(match.group(1))


class AlternateSourceBundleMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = load_summary()
        cls.routes = {row["route"]: row for row in cls.summary["route_bundles"]}

    def test_artifact_identity_and_global_no_go_false(self):
        self.assertEqual(self.summary["artifact"], "AlternateSourceBundleMatrixAfter0711_V1")
        self.assertEqual(self.summary["verdict_class"], "blocked_for_global_demotion")
        self.assertFalse(self.summary["global_no_go"])
        self.assertFalse(self.summary["global_demotion_allowed"])
        self.assertFalse(self.summary["complete_global_bundle_exists"])

    def test_all_required_routes_present(self):
        self.assertEqual(
            set(self.routes),
            {
                "RS_minus_one",
                "QFT_finite_extraction",
                "PTUJ_frame_asset",
                "IG_selector",
                "DGU_0_1_identity",
            },
        )

    def test_every_route_requires_alternate_bundle_and_blocks_global_demotion(self):
        for route, row in self.routes.items():
            with self.subTest(route=route):
                self.assertTrue(row["requires_alternate_primary_source_bundle_before_global_demotion"])
                self.assertFalse(row["global_demotion_allowed"])
                self.assertEqual(row["accepted_receipt_count"], 0)
                self.assertIn("Bundle_V1", row["minimum_bundle"])
                self.assertIn("next_step", row)

    def test_shared_required_bundle_fields(self):
        required = {
            "bundle_id",
            "covered_primary_source_surfaces",
            "query_log",
            "inspected_hit_ledger",
            "asset_capture_fields",
            "target_import_screen",
            "family_identity_check",
            "accepted_receipts",
            "negative_synthesis_rule",
            "rollback_conditions",
        }
        self.assertTrue(required.issubset(set(self.summary["shared_minimum_bundle_fields"])))

    def test_route_minimum_fields_are_populated(self):
        for route, row in self.routes.items():
            with self.subTest(route=route):
                self.assertGreaterEqual(len(row["minimum_source_coverage"]), 3)
                self.assertGreaterEqual(len(row["minimum_query_log_fields"]), 5)
                self.assertGreaterEqual(len(row["minimum_asset_capture_fields"]), 5)
                self.assertTrue(row["required_object"])
                self.assertTrue(row["global_status"])

    def test_scoped_vs_blocked_status(self):
        self.assertEqual(self.routes["RS_minus_one"]["current_status"], "underdefined_scoped_fail")
        self.assertEqual(self.routes["QFT_finite_extraction"]["current_status"], "underdefined")
        self.assertEqual(self.routes["PTUJ_frame_asset"]["current_status"], "blocked_tool_source_acquisition")
        self.assertTrue(self.routes["PTUJ_frame_asset"]["blocked_preserved"])
        self.assertFalse(self.routes["PTUJ_frame_asset"]["scoped_negative_preserved"])
        for route in ["RS_minus_one", "QFT_finite_extraction", "IG_selector", "DGU_0_1_identity"]:
            self.assertTrue(self.routes[route]["scoped_negative_preserved"])

    def test_first_obstruction_blocks_global_no_go(self):
        obstruction = self.summary["first_exact_obstruction_to_global_demotion"]
        self.assertEqual(
            obstruction["id"],
            "missing_complete_GlobalNegativeReceiptBundle_V1_after_0711_cycle2_inputs",
        )
        self.assertTrue(obstruction["missing"])
        self.assertTrue(obstruction["blocks_global_no_go"])

    def test_demotion_conditions_keep_global_no_go_false_until_complete_bundle(self):
        condition = self.summary["falsification_or_demotion_condition"]
        self.assertTrue(condition["global_no_go_remains_false_until_complete_global_bundle"])
        self.assertIn("complete GlobalNegativeReceiptBundle_V1", condition["global_no_go_condition"])
        self.assertIn("accepted_receipts_empty", condition["route_demotion_allowed_only_if"])
        self.assertIn("negative_synthesis_rule_declared", condition["route_demotion_allowed_only_if"])

    def test_next_steps_include_route_bundles_then_global_bundle(self):
        steps = self.summary["next_meaningful_source_bundle_step"]["steps"]
        for expected in [
            "assemble AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1",
            "assemble AlternatePrimarySourcePTUJFrameAssetBundle_V1",
            "assemble AlternatePrimarySourceQFTFiniteExtractionBundle_V1",
            "assemble AlternatePrimarySourceIGSelectorBundle_V1",
            "assemble AlternatePrimarySourceDGU01IdentityBundle_V1",
            "assemble GlobalNegativeReceiptBundle_V1 only after route bundles close",
        ]:
            self.assertIn(expected, steps)

    def test_forbidden_promotions_cover_global_and_route_overclaims(self):
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("global_GU_no_go_from_current_scoped_or_blocked_rows", forbidden)
        self.assertIn("PTUJ_route_fail_from_metadata_only", forbidden)
        self.assertIn("proof_restart_before_accepted_receipt_and_family_identity_check", forbidden)


if __name__ == "__main__":
    unittest.main()

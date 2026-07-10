#!/usr/bin/env python3
"""Audit the marble/wood local-minimum open-avenues ledger.

This is a structural route audit, not a proof of GU. It checks that the ledger
keeps all marble/wood avenues open as routes, gives every route allowed and
forbidden use, names proof debt and rollback conditions, includes a Hegelian
synthesis, and does not claim that any route is solved.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "marble-wood-local-minimum-open-avenues-ledger-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Route Taxonomy And Plain-English Meaning",
    "## 3. Route Ledger",
    "## 4. Hegelian Synthesis",
    "## 5. Update To The Next Standard Five-Lane Run Logic",
    "## 6. Machine-Readable Open-Avenues Ledger",
    "## 7. Next Meaningful Proof/Computation Step",
]

REQUIRED_ROUTES = [
    "WOOD_REPAIR_WITHIN_SHADOW_GR",
    "MARBLE_INTERROGATION",
    "LAMBDA_PATCH_DYNAMIC_SOURCE",
    "SOURCE_DERIVE_BOTH",
    "METRIC_QUANTIZATION_DOWNSTREAM",
    "COMPACT_FINITE_CONTROLS",
    "ORDINARY_GR_QFT_IMPORT_CONTROLS",
    "CLAIM_GOVERNANCE_INTERFACE",
]

REQUIRED_ROUTE_FIELDS = {
    "id",
    "short_name",
    "solved",
    "status",
    "can_do",
    "cannot_claim",
    "allowed_use",
    "forbidden_claim",
    "proof_debt",
    "next_experiment_or_computation",
    "progress_signal",
    "rollback_failure_condition",
}

LOCAL_MINIMUM_GUARDS = {
    "do_not_fix_wood_while_freezing_marble_as_final",
    "do_not_question_marble_while_dropping_exact_GR_recovery",
    "do_not_treat_Lambda_gmunu_as_principled_marble_without_source",
    "do_not_fit_xi_eff_or_dark_energy_to_DESI_Rubin_targets",
    "do_not_name_source_geometry_as_if_reductions_are_done",
    "do_not_discard_metric_quantization_or_standard_controls",
    "do_not_promote_compact_or_finite_controls_without_transport",
    "do_not_import_GR_QFT_SM_or_Bell_data_as_derived",
}

REQUIRED_NEXT_LOGIC = {
    "declare_route_id_in_every_lane",
    "include_at_least_one_marble_pressure_and_one_wood_source_pressure_lane_when_possible",
    "require_source_to_shadow_certificate_fields_for_source_geometry_lanes",
    "keep_compact_finite_and_standard_imports_tagged_as_controls_until_bridged",
    "place_metric_quantization_only_downstream_or_as_explicit_comparison_branch",
    "treat_Lambda_dark_energy_as_patch_route_with_DESI_Rubin_anti_fitting",
    "treat_clean_rollback_or_failure_as_frontier_progress",
}

OVERCLAIM_PATTERNS = [
    r"\broute\s+is\s+solved\b",
    r"\bGU\s+solves\s+Einstein'?s\s+marble/wood\s+complaint\b",
    r"\bsource\s+geometry\s+solves\s+the\s+marble/wood\s+problem\b",
    r"\bK3\s+gives\s+three\s+generations\b",
    r"\bnot\s+quantizing\s+the\s+metric\s+recovers\s+QFT\b",
    r"\bGU\s+derives\s+Lambda\b",
    r"\bGU\s+cancels\s+Lambda\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing marble/wood ledger: {DOC}") from exc


def extract_ledger(text: str) -> dict[str, object]:
    match = re.search(
        r"## 6\. Machine-Readable Open-Avenues Ledger\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable open-avenues JSON block")
    return json.loads(match.group(1))


def route_map(ledger: dict[str, object]) -> dict[str, dict[str, object]]:
    routes = ledger.get("routes", [])
    if not isinstance(routes, list):
        raise AssertionError("routes must be a list")
    return {str(route["id"]): route for route in routes}


class MarbleWoodOpenAvenuesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.ledger = extract_ledger(cls.text)
        cls.routes = route_map(cls.ledger)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_preserves_open_avenues_without_claim_promotion(self) -> None:
        self.assertEqual(
            self.ledger["artifact"],
            "MARBLE_WOOD_LOCAL_MINIMUM_OPEN_AVENUES_LEDGER",
        )
        self.assertEqual(self.ledger["verdict"], "OPEN_AVENUES_PRESERVED_NO_ROUTE_SOLVED")
        self.assertIn("NO_ROUTE_SOLVED", self.text)
        self.assertIn("NO_CLAIM_PROMOTION", self.text)
        self.assertIn("source_geometry_is_contract_not_proof", self.ledger["marble_wood_framing"]["anti_overclaim"])
        framing = self.ledger["marble_wood_framing"]
        self.assertIn("G_mu_nu", framing["marble"])
        self.assertIn("T_mu_nu", framing["wood"])
        self.assertIn("Lambda_g_mu_nu", framing["patch"])
        self.assertIn("dynamic", framing["dynamic_dark_energy_avenue"])
        self.assertIn("Lambda g_mu nu", self.text)

    def test_route_taxonomy_is_complete_and_ordered(self) -> None:
        self.assertEqual(self.ledger["route_order"], REQUIRED_ROUTES)
        self.assertEqual(set(self.routes), set(REQUIRED_ROUTES))
        for route_id in REQUIRED_ROUTES:
            self.assertIn(f"`{route_id}`", self.text)

    def test_each_route_has_required_fields_and_is_not_solved(self) -> None:
        for route_id, route in self.routes.items():
            self.assertEqual(set(route), REQUIRED_ROUTE_FIELDS, route_id)
            self.assertIs(route["solved"], False, route_id)
            self.assertNotIn("solved", str(route["status"]).lower(), route_id)
            for field in [
                "can_do",
                "cannot_claim",
                "allowed_use",
                "forbidden_claim",
                "next_experiment_or_computation",
                "progress_signal",
                "rollback_failure_condition",
            ]:
                self.assertIsInstance(route[field], str, route_id)
                self.assertGreater(len(route[field]), 20, f"{route_id}:{field}")
            self.assertIsInstance(route["proof_debt"], list, route_id)
            self.assertGreaterEqual(len(route["proof_debt"]), 3, route_id)

    def test_required_route_obligations_are_present(self) -> None:
        self.assertIn("GRShadowRecoveryCertificate", self.routes["MARBLE_INTERROGATION"]["proof_debt"])
        lambda_debt = self.routes["LAMBDA_PATCH_DYNAMIC_SOURCE"]["proof_debt"]
        self.assertIn("LambdaDarkEnergyProvenanceCertificate", lambda_debt)
        self.assertIn("generated_Z_theta", lambda_debt)
        self.assertIn("generated_C_Rtheta", lambda_debt)
        self.assertIn("xi_eff_provenance", lambda_debt)
        self.assertIn("DESI_Rubin_anti_fitting_test", lambda_debt)
        self.assertIn("bare_Lambda", self.routes["LAMBDA_PATCH_DYNAMIC_SOURCE"]["rollback_failure_condition"])
        self.assertIn("fitted_xi_eff", self.routes["LAMBDA_PATCH_DYNAMIC_SOURCE"]["rollback_failure_condition"])
        self.assertIn("QFTStateSpaceExtractionCertificate", self.routes["SOURCE_DERIVE_BOTH"]["proof_debt"])
        self.assertIn("QFTStateExtractionCertificate", self.routes["SOURCE_DERIVE_BOTH"]["proof_debt"])
        self.assertIn("RS_GU_phys", self.routes["COMPACT_FINITE_CONTROLS"]["proof_debt"])
        self.assertIn("source_replacement_for_state_space", self.routes["ORDINARY_GR_QFT_IMPORT_CONTROLS"]["proof_debt"])
        self.assertIn(
            "effective_metric_fluctuation_map",
            self.routes["METRIC_QUANTIZATION_DOWNSTREAM"]["proof_debt"],
        )

    def test_local_minimum_guards_are_explicit(self) -> None:
        self.assertEqual(set(self.ledger["local_minimum_guards"]), LOCAL_MINIMUM_GUARDS)
        for guard in LOCAL_MINIMUM_GUARDS:
            self.assertIn(guard, self.text)

    def test_hegelian_synthesis_steelmans_and_opposes_each_route(self) -> None:
        synthesis_section = self.text.split("## 4. Hegelian Synthesis", 1)[1]
        synthesis_section = synthesis_section.split("## 5. Update To The Next Standard Five-Lane Run Logic", 1)[0]
        self.assertIn("steelman thesis", synthesis_section)
        self.assertIn("opposing antithesis", synthesis_section)
        self.assertIn("synthesis: what survives", synthesis_section)
        for route_id in REQUIRED_ROUTES:
            self.assertIn(route_id, synthesis_section)

    def test_next_five_lane_logic_is_machine_readable(self) -> None:
        self.assertEqual(set(self.ledger["next_five_lane_logic"]), REQUIRED_NEXT_LOGIC)
        run_section = self.text.split("## 5. Update To The Next Standard Five-Lane Run Logic", 1)[1]
        run_section = run_section.split("## 6. Machine-Readable Open-Avenues Ledger", 1)[0]
        for phrase in [
            "Route declaration",
            "Opposition requirement",
            "Source-first burden",
            "Control honesty",
            "Metric quantization placement",
            "Lambda/dark-energy placement",
            "Failure as progress",
        ]:
            self.assertIn(phrase, run_section)

    def test_no_route_is_promoted_to_solved_by_text_or_json(self) -> None:
        self.assertEqual(
            self.ledger["horizon_claims"]["strongest_negative_guard"],
            "no_route_solved",
        )
        self.assertEqual(
            self.ledger["horizon_claims"]["forbidden_current_citation"],
            "GU solves Einstein's marble/wood complaint.",
        )
        allowed_markers = (
            "forbidden",
            "cannot",
            "not ",
            "no_route",
            "anti_overclaim",
            "do_not",
        )
        bad_lines: list[str] = []
        for pattern in OVERCLAIM_PATTERNS:
            for line in self.text.splitlines():
                if not re.search(pattern, line, flags=re.IGNORECASE):
                    continue
                if any(marker in line.lower() for marker in allowed_markers):
                    continue
                bad_lines.append(line)
        self.assertFalse(bad_lines, "\n".join(bad_lines))

    def test_next_meaningful_step_targets_both_shadows(self) -> None:
        next_step = self.ledger["next_meaningful_step"]
        self.assertIn("SOURCE_OBJECT_V0", next_step)
        self.assertIn("REDUCTION_PACKET_V0", next_step)
        final_section = self.text.split("## 7. Next Meaningful Proof/Computation Step", 1)[1]
        self.assertIn("R_GR attempt", final_section)
        self.assertIn("R_DE attempt", final_section)
        self.assertIn("R_QFT attempt", final_section)
        self.assertIn("exact Schwarzschild", final_section)
        self.assertIn("two-point", final_section)
        self.assertIn("DESI/Rubin", final_section)
        self.assertIn("fitted `xi_eff`", final_section)


def summary() -> dict[str, object]:
    text = read_doc()
    ledger = extract_ledger(text)
    routes = route_map(ledger)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": ledger["verdict"],
        "route_count": len(routes),
        "all_routes_unsolved": all(route["solved"] is False for route in routes.values()),
        "next_step": ledger["next_meaningful_step"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit the marble/wood open-avenues ledger.")
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args = parser.parse_args(argv)

    if args.json:
        print(json.dumps(summary(), indent=2, sort_keys=True))
        return 0

    print("Marble/wood open-avenues audit: structural route ledger only, not a proof.")
    print()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(MarbleWoodOpenAvenuesAudit)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

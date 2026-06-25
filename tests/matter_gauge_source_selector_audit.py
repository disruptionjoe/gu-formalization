#!/usr/bin/env python3
"""Audit the matter/gauge source-geometry selector gate.

This is a structural provenance audit, not a mathematical proof. It checks that
the gate declares the selector schema, records real provenance rows, keeps
high-risk SM target data out of the derived bucket, and emits claim certificates
for MATTER-SHADOW, SM-GAUGE, HIGGS, and GEN-COUNT.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "matter-gauge-source-geometry-selector-gate-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Source-Geometry Matter/Gauge Selector Schema",
    "## 3. Current Derived/Hosted/Imported/Failed Ledger",
    "## 4. Relation To Type II_1 Selectors And K3/Generation Bridge",
    "## 5. Claim Certificate Table For MATTER-SHADOW, SM-GAUGE, HIGGS, GEN-COUNT",
    "## 6. Branch/Selector Robustness Table",
    "## 7. Forbidden Shortcuts And Rollback Conditions",
    "## 8. First Exact Missing Proof Object",
    "## 9. Next Meaningful Proof/Computation Step",
    "## Machine-Readable Source-Geometry Selector Gate",
]

REQUIRED_SELECTOR_FIELDS = {
    "input_independence",
    "branch_closure",
    "gauge_quotient",
    "finite_algebra_if_used",
    "pati_salam_reps",
    "sm_reps",
    "hypercharge",
    "higgs",
    "anomaly_shadow",
    "generation_count",
    "branch_robustness",
    "rollback",
}

REQUIRED_CLAIMS = {"MATTER-SHADOW", "SM-GAUGE", "HIGGS", "GEN-COUNT"}

REQUIRED_CLAIM_FIELDS = {
    "claim",
    "current_status",
    "proof_grade",
    "derived_by_source_geometry",
    "hosted",
    "imported_or_failed",
    "missing_proof_object",
    "forbidden_inputs",
    "rollback_condition",
    "citation_language",
}

EXPECTED_HIGH_RISK_STATUSES = {
    "Finite Connes algebra A_F": "imported",
    "SM gauge quotient G_SM/Z_6": "failed",
    "SM Higgs quantum-number slot": "hosted",
    "Physical Higgs scalar and potential": "open",
    "Full anomaly-safe observer shadow": "open",
    "Exact generation count n_gen=3": "open",
    "Raw compact K3 RS arithmetic": "control_only",
    "Type II_1 fixed-data selector": "open_empty",
}

FORBIDDEN_SENTINELS_BY_CLAIM = {
    "MATTER-SHADOW": {"K_SM", "ordinary_SM_shadow"},
    "SM-GAUGE": {"A_F", "G_SM", "Z_6"},
    "HIGGS": {"physical_Higgs", "negative_mass_squared"},
    "GEN-COUNT": {"n_equals_3", "ind_H_D_RS_equals_8", "ind_H_D_GU_equals_24"},
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing selector gate: {DOC}") from exc


def extract_certificate(text: str) -> dict[str, object]:
    pattern = r"## Machine-Readable Source-Geometry Selector Gate\s*```json\s*(\{.*?\})\s*```"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing machine-readable selector gate JSON block")
    return json.loads(match.group(1))


class MatterGaugeSourceSelectorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.cert = extract_certificate(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_certificate_verdict_and_schema_are_specific(self) -> None:
        self.assertEqual(
            self.cert["artifact"],
            "MATTER_GAUGE_SOURCE_GEOMETRY_SELECTOR_GATE",
        )
        self.assertEqual(self.cert["verdict"], "NO_SOURCE_GEOMETRY_SELECTOR_YET")
        self.assertEqual(set(self.cert["required_selector_fields"]), REQUIRED_SELECTOR_FIELDS)
        self.assertIn("Phi_SG_MG", self.text)
        self.assertIn("Phi_SG_G", self.text)

    def test_forbidden_target_inputs_cover_smuggling_surface(self) -> None:
        forbidden = set(self.cert["forbidden_target_inputs"])
        for required in [
            "A_F",
            "G_SM",
            "Z_6",
            "K_SM",
            "physical_Higgs",
            "n_equals_3",
            "ind_H_D_RS_equals_8",
            "ind_H_D_GU_equals_24",
            "ordinary_anomaly_free_SM_shadow",
        ]:
            self.assertIn(required, forbidden)

    def test_ledger_rows_have_provenance_and_do_not_overderive_targets(self) -> None:
        status_enum = set(self.cert["status_enum"])
        ledger = self.cert["ledger"]
        self.assertGreaterEqual(len(ledger), 10)
        by_datum = {row["datum"]: row for row in ledger}

        for row in ledger:
            self.assertIn(row["status"], status_enum, row)
            self.assertIsInstance(row["provenance"], list, row)
            self.assertTrue(row["provenance"], row)
            self.assertGreater(len(row["missing_proof_object"].strip()), 10, row)

        for datum, expected_status in EXPECTED_HIGH_RISK_STATUSES.items():
            self.assertIn(datum, by_datum)
            self.assertEqual(by_datum[datum]["status"], expected_status)

        derived_rows = [row["datum"] for row in ledger if row["status"] == "derived"]
        derived_blob = "\n".join(derived_rows)
        self.assertNotIn("A_F", derived_blob)
        self.assertNotIn("G_SM", derived_blob)
        self.assertNotIn("n_gen=3", derived_blob)

    def test_claim_certificates_are_complete_and_guarded(self) -> None:
        certificates = self.cert["claim_certificates"]
        by_claim = {certificate["claim"]: certificate for certificate in certificates}
        self.assertEqual(set(by_claim), REQUIRED_CLAIMS)

        for claim, certificate in by_claim.items():
            self.assertEqual(set(certificate), REQUIRED_CLAIM_FIELDS)
            for list_field in ["derived_by_source_geometry", "hosted", "imported_or_failed", "forbidden_inputs"]:
                self.assertIsInstance(certificate[list_field], list, certificate)
                self.assertTrue(certificate[list_field], certificate)
            self.assertGreater(len(certificate["missing_proof_object"]), 15)
            self.assertGreater(len(certificate["rollback_condition"]), 15)
            self.assertGreater(len(certificate["citation_language"]), 20)

            forbidden_blob = " ".join(certificate["forbidden_inputs"])
            for sentinel in FORBIDDEN_SENTINELS_BY_CLAIM[claim]:
                self.assertIn(sentinel, forbidden_blob)

        self.assertEqual(by_claim["SM-GAUGE"]["current_status"], "failed")
        self.assertEqual(by_claim["GEN-COUNT"]["current_status"], "open")
        self.assertIn("Pati-Salam branch", by_claim["MATTER-SHADOW"]["citation_language"])

    def test_branch_robustness_rows_cover_live_lanes(self) -> None:
        rows = {row["branch"]: row for row in self.cert["branch_robustness"]}
        for branch in [
            "GU carrier",
            "Pati-Salam branching",
            "Pati-Salam-to-SM embedding",
            "Type II_1 current selectors",
            "K3 compact control",
            "Higgs source projection",
        ]:
            self.assertIn(branch, rows)
            self.assertTrue(rows[branch]["decision"])
            self.assertTrue(rows[branch]["missing"])

        self.assertEqual(rows["K3 compact control"]["decision"], "control_only")
        self.assertEqual(rows["Type II_1 current selectors"]["decision"], "failed_or_open_empty")

    def test_first_missing_object_and_next_step_are_concrete(self) -> None:
        self.assertEqual(
            self.cert["first_missing_proof_object"],
            "Phi_SG_MG source-geometry finite-control selector",
        )
        self.assertIn("Phi_SG_G", self.cert["next_step"])
        first_missing_section = self.text.split("## 8. First Exact Missing Proof Object", 1)[1]
        first_missing_section = first_missing_section.split("## 9. Next Meaningful Proof/Computation Step", 1)[0]
        self.assertIn("NoTargetInput", first_missing_section)
        self.assertIn("GaugeQuotient", first_missing_section)
        self.assertIn("Generation", first_missing_section)


if __name__ == "__main__":
    unittest.main(verbosity=2)

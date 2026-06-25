#!/usr/bin/env python3
"""Audit the Cycle 1 VZ subprincipal/E-block gate artifact.

This is a status-discipline audit. It checks that the artifact keeps the
principal-symbol result separate from subprincipal/extrinsic-curvature gates,
names FC-VZ-1 and FC-VZ-4 explicitly, and blocks any full-VZ-evasion claim unless
both proof gates are marked closed in the machine-readable summary.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Principal-Symbol Result That Remains Valid",
    "## 3. E-Block Invertibility Status and Direct-Proof Gap",
    "## 4. Subprincipal/Extrinsic-Curvature Characteristic Status",
    "## 5. First Exact Obstruction or Missing Proof Object",
    "## 6. What This Means for GU Causality/Hyperbolicity",
    "## 7. Next Meaningful Computation",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_E_BLOCK_CONDITIONS = {
    "actual_operator_has_Phi_d",
    "principal_coefficient_lambda_d_nonzero_for_Schur_route",
    "Q_sector_exact_E0_plus_Im_j",
    "coordinate_convention_fixed",
    "chirality_domains_fixed",
    "non_null_q_and_G_squared_equals_q_Id",
    "null_locus_exact",
    "determinant_free_kernel_or_inverse_proof",
}

REQUIRED_ROLLBACKS = {
    "actual_operator_lacks_Phi_d",
    "non_null_E_block_kernel_found",
    "II_s_sources_effective_first_order_spacelike_characteristics",
    "curved_section_symbol_not_real_principal_type",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Cycle 1 VZ gate artifact: {DOC}") from exc


def load_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class Cycle1VzSubprincipalEblockGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = load_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_fc_vz_1_and_fc_vz_4_are_explicit_in_text_and_json(self) -> None:
        for gate_id in ["FC-VZ-1", "FC-VZ-4"]:
            self.assertIn(gate_id, self.text)
            self.assertIn(gate_id, self.summary["gates"])

    def test_no_full_vz_evasion_claim_unless_both_gates_close(self) -> None:
        gates = self.summary["gates"]
        both_closed = all(gates[gate_id]["status"] == "closed" for gate_id in ["FC-VZ-1", "FC-VZ-4"])
        if self.summary.get("full_vz_evasion_claim"):
            self.assertTrue(both_closed, "full VZ evasion claimed before both gates closed")

        self.assertFalse(self.summary.get("full_vz_evasion_claim"))
        self.assertNotEqual(gates["FC-VZ-1"]["status"], "closed")
        self.assertNotEqual(gates["FC-VZ-4"]["status"], "closed")

        verdict_section = self.text.split("## 1. Verdict", 1)[1].split("## 2.", 1)[0]
        self.assertIn("does **not** contain enough to claim full VZ evasion", verdict_section)

    def test_principal_and_subprincipal_status_are_separated(self) -> None:
        principal = self.summary["principal_symbol_status"]
        subprincipal = self.summary["subprincipal_status"]
        self.assertTrue(principal["separated_from_subprincipal"])
        self.assertTrue(subprincipal["separated_from_principal"])
        self.assertIn("principal-symbol", self.text)
        self.assertIn("subprincipal", self.text)
        self.assertNotEqual(principal["status"], subprincipal["status"])

    def test_e_block_invertibility_conditions_are_named(self) -> None:
        conditions = set(self.summary["gates"]["FC-VZ-1"]["conditions_named"])
        missing = REQUIRED_E_BLOCK_CONDITIONS - conditions
        self.assertFalse(missing, f"missing E-block conditions: {sorted(missing)}")

    def test_verdict_and_rollback_conditions_are_machine_readable(self) -> None:
        self.assertEqual(self.summary["verdict"], "NOT_FULL_EVASION__GATES_NOT_CLOSED")
        rollbacks = set(self.summary.get("rollback_conditions", []))
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")
        self.assertGreaterEqual(len(rollbacks), 6)

    def test_next_computation_is_concrete_not_summary_only(self) -> None:
        next_steps = self.summary.get("next_meaningful_computation", [])
        self.assertIn("canonical_typed_D_GU_0_1_operator_certificate", next_steps)
        self.assertIn("explicit_sigma_0_inv_S_Rs_4D_full_with_II_s_H_Z_A_and_curved_frame_terms", next_steps)


if __name__ == "__main__":
    unittest.main(argv=sys.argv, verbosity=2)

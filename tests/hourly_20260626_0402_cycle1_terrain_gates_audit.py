"""Audit the 0402 cycle 1 terrain-gate frontier artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0402"
ARTIFACTS = {
    "PhysicalRSKTheoryClassGate": ROOT
    / "explorations/hourly-20260626-0402-cycle1-physical-rs-ktheory-class-gate.md",
    "VZSubprincipalCharacteristicLedger": ROOT
    / "explorations/hourly-20260626-0402-cycle1-vz-subprincipal-characteristic-ledger.md",
    "PrimaryGUVariationalInterface": ROOT
    / "explorations/hourly-20260626-0402-cycle1-primary-gu-variational-interface.md",
    "ThetaResidualTerrainAudit": ROOT
    / "explorations/hourly-20260626-0402-cycle1-theta-residual-terrain-audit.md",
    "IGRivalProjectorTerrainGate": ROOT
    / "explorations/hourly-20260626-0402-cycle1-ig-rival-projector-terrain-gate.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1TerrainGatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {lane: extract_summary(path) for lane, path in ARTIFACTS.items()}

    def test_all_lanes_are_run_scoped_and_non_promotional(self) -> None:
        self.assertEqual(set(self.summaries), set(ARTIFACTS))
        for lane, summary in self.summaries.items():
            with self.subTest(lane=lane):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertEqual(summary["lane"], lane)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_physical_rs_class_stays_before_generation_readout(self) -> None:
        rs = self.summaries["PhysicalRSKTheoryClassGate"]
        self.assertFalse(rs["generation_readout_allowed"])
        self.assertEqual(rs["physical_rs_class_decision"], "OPEN_MISSING_SYMBOL_DATA")
        self.assertFalse(rs["e_raw_physical"])
        self.assertFalse(rs["e_brst_physical"])
        self.assertTrue(rs["third_class_possible"])
        self.assertEqual(
            rs["first_missing_object"],
            "RS_GU^phys_source_clean_gauge_fixed_or_BRST_elliptic_symbol_packet",
        )
        self.assertEqual(rs["next_frontier_object"], "RSGUPhysSymbolPacket_V0")

    def test_vz_principal_symbol_is_not_full_closure(self) -> None:
        vz = self.summaries["VZSubprincipalCharacteristicLedger"]
        self.assertFalse(vz["principal_symbol_full_closure_claimed"])
        self.assertFalse(vz["e_block_invertibility_established"])
        self.assertFalse(vz["mixed_covector_characteristic_established"])
        self.assertIn("actual_D_GU", vz["first_missing_object"])
        self.assertEqual(
            vz["next_frontier_object"],
            "VZActualEBlockAndSubprincipalCharacteristicCertificate_V0",
        )

    def test_primary_variational_interface_requires_branch_fixed_packet(self) -> None:
        gr = self.summaries["PrimaryGUVariationalInterface"]
        self.assertFalse(gr["exact_gr_recovery_admitted"])
        self.assertFalse(gr["full_el_tuple_present"])
        self.assertFalse(gr["source_law_present"])
        self.assertTrue(gr["forbidden_shortcut_rejected"])
        self.assertIn("BranchFixedIGVariationPacket_V0", gr["first_missing_object"])
        self.assertEqual(gr["next_frontier_object"], "BranchFixedIGVariationPacket_V0")

    def test_theta_residual_route_rejects_target_fit_and_gaussian_assumption(self) -> None:
        theta = self.summaries["ThetaResidualTerrainAudit"]
        self.assertFalse(theta["theta_divergence_free_status_changed"])
        self.assertTrue(theta["gaussian_residual_assumption_rejected"])
        self.assertFalse(theta["xi_tuned_from_target_data"])
        self.assertFalse(theta["nonminimal_coupling_derived"])
        self.assertFalse(theta["residual_law_derived"])
        self.assertEqual(theta["next_frontier_object"], "ThetaNormalFluxCoefficientResidualPacket_V0")

    def test_ig_projector_identity_waits_for_source_locator(self) -> None:
        ig = self.summaries["IGRivalProjectorTerrainGate"]
        self.assertTrue(ig["product_a_b_rows_available"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["rival_projector_identity_evaluable"])
        self.assertFalse(ig["downstream_chirality_used"])
        self.assertEqual(
            ig["first_missing_object"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1.source_native_operator_locator",
        )
        self.assertEqual(ig["next_frontier_object"], "ProductABSourceOperatorSourceLocatorReceipt_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)

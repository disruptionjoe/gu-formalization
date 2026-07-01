import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "dgu-guarded-symbol-certificate-2026-06-26.md"
GATE = (
    ROOT
    / "active-research"
    / "topological-generation-count-families-k3-chi-gate-2026-06-26.md"
)


class DGUGuardedSymbolCertificateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.gate = GATE.read_text(encoding="utf-8")

    def test_records_zero_order_phi_without_ellipticity_overclaim(self):
        self.assertIn("Phi is zero-order", self.text)
        self.assertIn("sigma_1(Phi_hat)(xi) = 0", self.text)
        self.assertIn("sigma_1(D_GU)(xi) = c_Y(xi) tensor 1_S", self.text)
        self.assertIn("Standard Riemannian ellipticity is not obtained", self.text)
        self.assertNotIn("Ellipticity & Symbol Certificate (Now Closed)", self.text)

    def test_keeps_null_cone_characteristic_set(self):
        required = [
            "c_Y(xi)^2 = g_Y^{-1}(xi, xi) Id",
            "Char(D_GU) = { xi != 0 : g_Y^{-1}(xi, xi) = 0 }",
            "This is the light cone/null cone",
            "remove or deform that characteristic set",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)

    def test_does_not_close_families_pushforward(self):
        self.assertIn("OPEN_GATED; FAMILIES_PUSHFORWARD_NOT_CLOSED", self.text)
        self.assertIn("LOWER_ORDER_BUT_DOMAIN_OPEN", self.text)
        self.assertIn("not:", self.text)
        self.assertIn("INDEX_PRESERVING_HOMOTOPY", self.text)

    def test_machine_summary_blocks_shortcuts(self):
        match = re.search(
            r"```json\n(\{\n  \"artifact\": \"D_GU_GUARDED_SYMBOL_CERTIFICATE\".*?\n\})\n```",
            self.text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "machine-readable summary block not found")
        payload = json.loads(match.group(1))
        self.assertEqual(payload["phi_order"], 0)
        self.assertFalse(payload["standard_riemannian_ellipticity_for_physical_operator"])
        self.assertFalse(payload["families_pushforward_closed"])
        self.assertEqual(payload["safe_gate_value"], "LOWER_ORDER_BUT_DOMAIN_OPEN")
        self.assertIn(
            "phi_zero_order_implies_standard_ellipticity",
            payload["blocked_shortcuts"],
        )

    def test_active_gate_links_certificate_and_blocks_ellipticity_shortcut(self):
        self.assertIn("explorations/dgu-guarded-symbol-certificate-2026-06-26.md", self.gate)
        self.assertIn("phi_zero_order_implies_standard_ellipticity", self.gate)
        self.assertIn("LOWER_ORDER_BUT_DOMAIN_OPEN", self.gate)
        self.assertIn("current guarded certificate", self.gate)


if __name__ == "__main__":
    unittest.main()

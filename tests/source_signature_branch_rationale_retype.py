#!/usr/bin/env python3
"""Exact integration gate for source assertion versus derived signature.

The source explicitly uses Y^(7,7) and Spin(7,7), while its consistently
interpreted displayed block signatures add to (9,5) in repository notation.
This test protects both facts: K77 is an author-asserted conditional carrier,
not a consequence of the displayed metric-bundle inertia calculation.
"""

from pathlib import Path
import re
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


class SignatureBranchRationaleRetype(unittest.TestCase):

    def test_source_explicitly_uses_k77(self) -> None:
        extraction = (ROOT / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md").read_text()
        self.assertIn("Y^{7,7}", extraction)
        self.assertIn("Spin(7,7)", extraction)
        self.assertIn("N^{6,4}", extraction)

    def test_source_signature_notation_is_negative_first(self) -> None:
        source = [(3, 7), (3, 6), (4, 6)]
        computed_plus_first = [(7, 3), (6, 3), (6, 4)]
        self.assertEqual([(n, p) for p, n in source], computed_plus_first)

    def test_displayed_blocks_derive_k95_not_k77(self) -> None:
        # Source negative-first: (4,6)+(1,3)=(5,9).
        source_total = (4 + 1, 6 + 3)
        self.assertEqual(source_total, (5, 9))
        # Repository plus-first mirror: (9,5).
        self.assertEqual((source_total[1], source_total[0]), (9, 5))
        self.assertNotEqual(source_total, (7, 7))

    def test_real_clifford_source_use_and_geometric_derivation_are_distinct(self) -> None:
        registry = (ROOT / "lab/process/layer0-fork-registry.yaml").read_text()
        block = registry.split("- id: REAL-CLIFFORD-FORM", 1)[1].split("- id:", 1)[0]
        self.assertIn('settled_side: "Cl(7,7) = M128(R)"', block)
        self.assertIn("AUTHOR-ASSERTED", block)
        self.assertIn("GEOMETRY-DERIVED", block)
        self.assertNotIn("derived the real form from Curt/Eric's exact source-typed arithmetic", block)

    def test_k77_probe_is_a_conditional_metric_not_source_arithmetic(self) -> None:
        # The K77 probe deliberately combines plus-first (1,3) and (6,4).
        eta = sp.diag(1, -1, -1, -1)
        fibre = sp.diag(*([1] * 6 + [-1] * 4))
        total = sp.diag(eta, fibre)
        values = total.eigenvals()
        inertia = (
            sum(m for value, m in values.items() if value.is_positive),
            sum(m for value, m in values.items() if value.is_negative),
        )
        self.assertEqual(inertia, (7, 7))
        self.assertNotEqual(inertia, (9, 5))

    def test_next_gate_is_branch_aware(self) -> None:
        contract = (ROOT / "lab/methods/research-evidence-contract-v1.0.md").read_text()
        self.assertRegex(contract, re.compile(r"author-asserted.*K77", re.I | re.S))
        self.assertRegex(contract, re.compile(r"geometry-derived.*K95", re.I | re.S))
        self.assertIn("signature-generic", contract)


if __name__ == "__main__":
    unittest.main(verbosity=2)

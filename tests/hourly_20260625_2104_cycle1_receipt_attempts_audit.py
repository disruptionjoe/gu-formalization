"""Audit the 2104 cycle 1 producer receipt artifacts."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
import re
import unittest
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2104"
ARTIFACTS = {
    "PTUJ": ROOT / "explorations/hourly-20260625-2104-cycle1-ptuj-single-complete-branch-receipt-attempt.md",
    "IG": ROOT / "explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md",
    "DGU": ROOT / "explorations/hourly-20260625-2104-cycle1-dgu-sector-same-operator-receipt-attempt.md",
    "RS": ROOT / "explorations/hourly-20260625-2104-cycle1-rs-lawful-route-or-denial-receipt-attempt.md",
    "QFT": ROOT / "explorations/hourly-20260625-2104-cycle1-qft-iota-rraw-receipt-attempt.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


def char_product(left: Counter[tuple[int, ...]], right: Counter[tuple[int, ...]]) -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter()
    for a, ma in left.items():
        for b, mb in right.items():
            out[tuple(x + y for x, y in zip(a, b))] += ma * mb
    return out


def spinor_char(parity_minus: int) -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter()
    for mask in range(1 << 7):
        weight = []
        minus = 0
        for i in range(7):
            if mask & (1 << i):
                weight.append(-1)
                minus += 1
            else:
                weight.append(1)
        if minus % 2 == parity_minus:
            out[tuple(weight)] += 1
    return out


def vector_char() -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter()
    for i in range(7):
        pos = [0] * 7
        neg = [0] * 7
        pos[i] = 2
        neg[i] = -2
        out[tuple(pos)] += 1
        out[tuple(neg)] += 1
    return out


def adjoint_char() -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter({(0, 0, 0, 0, 0, 0, 0): 7})
    for i in range(7):
        for j in range(i + 1, 7):
            for si in (-2, 2):
                for sj in (-2, 2):
                    root = [0] * 7
                    root[i] = si
                    root[j] = sj
                    out[tuple(root)] += 1
    return out


def subtract_nonnegative(base: Counter[tuple[int, ...]], *subs: Counter[tuple[int, ...]]) -> Counter[tuple[int, ...]]:
    out = Counter(base)
    for sub in subs:
        for weight, mult in sub.items():
            out[weight] -= mult
            if out[weight] == 0:
                del out[weight]
    negatives = {weight: mult for weight, mult in out.items() if mult < 0}
    if negatives:
        raise AssertionError(f"negative character multiplicities: {negatives}")
    return out


def total_dimension(character: Counter[tuple[int, ...]]) -> int:
    return sum(character.values())


def weyl_dimension_d7(highest_weight_doubled: Iterable[int]) -> int:
    lam = [Fraction(x, 2) for x in highest_weight_doubled]
    rho = [Fraction(6 - i, 1) for i in range(7)]
    top = [x + r for x, r in zip(lam, rho)]
    dim = Fraction(1, 1)
    for i in range(7):
        for j in range(i + 1, 7):
            dim *= (top[i] - top[j]) / (rho[i] - rho[j])
            dim *= (top[i] + top[j]) / (rho[i] + rho[j])
    self_num = dim.numerator
    if dim.denominator != 1:
        raise AssertionError(f"nonintegral Weyl dimension {dim}")
    return self_num


class Cycle1ReceiptAttemptsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_cycle1_routes_present(self) -> None:
        self.assertEqual(set(self.summaries), {"PTUJ", "IG", "DGU", "RS", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_source_receipt_states(self) -> None:
        self.assertEqual(self.summaries["PTUJ"]["verdict_class"], "blocked")
        self.assertEqual(self.summaries["PTUJ"]["accepted_receipt_count"], 0)
        self.assertFalse(self.summaries["PTUJ"]["cross_branch_assembly_allowed"])

        self.assertEqual(self.summaries["DGU"]["verdict_class"], "blocked")
        self.assertEqual(self.summaries["DGU"]["accepted_receipt_count"], 0)
        self.assertFalse(self.summaries["DGU"]["sector_rule_source_emitted"])
        self.assertFalse(self.summaries["DGU"]["same_operator_witness_source_emitted"])

        self.assertEqual(self.summaries["QFT"]["verdict_class"], "underdefined")
        self.assertEqual(self.summaries["QFT"]["accepted_receipt_count"], 0)
        self.assertFalse(self.summaries["QFT"]["source_defined_iota_b_admitted"])
        self.assertFalse(self.summaries["QFT"]["typed_R_raw_b_O_admitted"])

    def test_rs_route_only_receipt_closed(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "closed_route_only")
        self.assertEqual(rs["accepted_receipt_count"], 1)
        self.assertTrue(rs["route_receipt_admitted"])
        self.assertFalse(rs["full_denial_packet_accepted"])
        self.assertFalse(rs["frame_packet_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertIn("RSFrameCropOCRChecksumManifest", rs["constructive_next_object"])

    def test_ig_product_b_table_summary(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(ig["verdict_class"], "closed_product_b_table")
        self.assertEqual(ig["accepted_receipt_count"], 1)
        self.assertTrue(ig["claim_status_consistency_triggered"])
        table = ig["product_b_table_candidate"]
        self.assertEqual(table["input_dimension_product"], 5824)
        self.assertEqual(table["dimension_sum"], 5824)
        self.assertEqual(table["multiplicity_of_V_omega6"], 1)
        self.assertEqual(table["V_omega7_status"], "absent")
        self.assertEqual(table["V_omega1_plus_omega7_status"], "present_multiplicity_1")

    def test_d7_product_b_character_decomposition(self) -> None:
        # doubled e_i coordinates, with omega_6 = (1,1,1,1,1,1,-1)
        # and omega_7 = (1,1,1,1,1,1,1).
        omega_2_plus_omega_6 = (3, 3, 1, 1, 1, 1, -1)
        omega_1_plus_omega_7 = (3, 1, 1, 1, 1, 1, 1)

        s_plus = spinor_char(parity_minus=1)
        s_minus = spinor_char(parity_minus=0)
        product_b = char_product(adjoint_char(), s_plus)
        vector_times_s_minus = char_product(vector_char(), s_minus)
        v_omega_1_plus_omega_7 = subtract_nonnegative(vector_times_s_minus, s_plus)
        v_omega_2_plus_omega_6 = subtract_nonnegative(product_b, s_plus, v_omega_1_plus_omega_7)

        self.assertEqual(total_dimension(product_b), 91 * 64)
        self.assertEqual(total_dimension(s_plus), 64)
        self.assertEqual(total_dimension(v_omega_1_plus_omega_7), 832)
        self.assertEqual(total_dimension(v_omega_2_plus_omega_6), 4928)

        self.assertEqual(weyl_dimension_d7(omega_1_plus_omega_7), 832)
        self.assertEqual(weyl_dimension_d7(omega_2_plus_omega_6), 4928)
        self.assertEqual(product_b[omega_2_plus_omega_6], 1)
        self.assertEqual(v_omega_1_plus_omega_7[omega_1_plus_omega_7], 1)
        self.assertEqual(product_b[(1, 1, 1, 1, 1, 1, 1)], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

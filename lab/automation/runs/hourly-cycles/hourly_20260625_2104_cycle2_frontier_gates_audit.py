"""Audit the 2104 cycle 2 frontier gate artifacts."""

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
    "PTUJ": ROOT / "explorations/hourly-20260625-2104-cycle2-ptuj-branch-local-source-packet-gate.md",
    "IG": ROOT / "explorations/hourly-20260625-2104-cycle2-ig-product-a-finite-control-packet.md",
    "DGU": ROOT / "explorations/hourly-20260625-2104-cycle2-dgu-source-stable-row-packet.md",
    "RS": ROOT / "explorations/hourly-20260625-2104-cycle2-rs-frame-ocr-manifest-gate.md",
    "QFT": ROOT / "explorations/hourly-20260625-2104-cycle2-qft-branch-observation-carrier.md",
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
    if dim.denominator != 1:
        raise AssertionError(f"nonintegral Weyl dimension {dim}")
    return dim.numerator


class Cycle2FrontierGatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_cycle2_routes_present(self) -> None:
        self.assertEqual(set(self.summaries), {"PTUJ", "IG", "DGU", "RS", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertFalse(summary["target_import_used"])

    def test_ptuj_source_packet_remains_branch_blocked(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["verdict_class"], "blocked")
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertFalse(ptuj["official_branch_accepted"])
        self.assertFalse(ptuj["lawful_local_branch_accepted"])
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertIn("one_complete_branch_local_PTUJ_source_packet", ptuj["constructive_next_object"])

    def test_ig_product_a_closed_but_selector_blocked(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(ig["verdict_class"], "closed_product_a_packet_selector_blocked")
        self.assertTrue(ig["product_b_receipt_consumed"])
        self.assertTrue(ig["product_a_packet_admitted"])
        self.assertEqual(ig["accepted_receipt_count"], 2)
        self.assertTrue(ig["claim_status_consistency_triggered"])
        self.assertFalse(ig["selector_restart_allowed"])

        product_a = ig["product_a"]
        self.assertEqual(product_a["total_dimension"], 896)
        self.assertEqual(product_a["kernel"], "V(omega_1 + omega_7)")
        self.assertEqual(product_a["image"], "V(omega_6)")
        self.assertEqual(product_a["cokernel"], "0")
        self.assertEqual([row["dimension"] for row in product_a["summands"]], [832, 64])

        finite = ig["finite_control_status"]
        self.assertEqual(finite["common_row_count"], 2)
        self.assertEqual(finite["common_rows"], ["V(omega_1 + omega_7)", "V(omega_6)"])
        self.assertFalse(finite["finite_common_row_uniqueness"])
        self.assertEqual(finite["selector_identity"], "blocked")
        self.assertFalse(ig["selector_identity_status"]["V_omega1_plus_omega7_rival_eliminated"])
        self.assertFalse(ig["selector_identity_status"]["proof_restart_allowed"])

    def test_dgu_scoped_negative_packet_has_no_positive_receipt(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["verdict_class"], "scoped_negative_receipt")
        self.assertTrue(dgu["source_stable_packet_admitted"])
        self.assertFalse(dgu["source_emitted_positive_receipt_admitted"])
        self.assertEqual(dgu["accepted_receipt_count"], 0)
        self.assertEqual(dgu["sector_rule_row_status"], "missing")
        self.assertEqual(dgu["same_operator_row_status"], "missing")
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])

    def test_rs_route_consumed_manifest_still_missing(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "blocked")
        self.assertTrue(rs["route_receipt_consumed"])
        self.assertFalse(rs["frame_manifest_admitted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["crop_or_ocr_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertFalse(rs["proof_restart_allowed"])

    def test_qft_carrier_remains_underdefined(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(qft["verdict_class"], "underdefined")
        self.assertFalse(qft["carrier_admitted"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["source_native_field_packet_admitted"])
        self.assertEqual(qft["accepted_receipt_count"], 0)
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertEqual(qft["first_obstruction"], "source_emitted_branch_label_and_branch_admissibility_rule_absent")

    def test_d7_product_a_character_decomposition(self) -> None:
        omega_1_plus_omega_7 = (3, 1, 1, 1, 1, 1, 1)
        omega_6 = (1, 1, 1, 1, 1, 1, -1)

        s_plus = spinor_char(parity_minus=1)
        s_minus = spinor_char(parity_minus=0)
        product_a = char_product(vector_char(), s_minus)
        v_omega_1_plus_omega_7 = subtract_nonnegative(product_a, s_plus)

        self.assertEqual(total_dimension(product_a), 14 * 64)
        self.assertEqual(total_dimension(s_plus), 64)
        self.assertEqual(total_dimension(v_omega_1_plus_omega_7), 832)
        self.assertEqual(weyl_dimension_d7(omega_1_plus_omega_7), 832)
        self.assertEqual(weyl_dimension_d7(omega_6), 64)
        self.assertEqual(product_a[omega_1_plus_omega_7], 1)
        self.assertEqual(s_plus[omega_6], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
"""Formula audit for the K3 Rarita-Schwinger symbol-index attempt.

This is not a proof of the GU generation count.  It checks only the
characteristic-class arithmetic used in
explorations/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md.

The physical gauge-fixed GU RS complex is intentionally marked open/skipped
until its symbol class and background Chern character are supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
import json
import sys
import unittest


@dataclass(frozen=True)
class K3Data:
    ahat: int = 2
    chi: int = 24
    sigma: int = -16
    p1: int = -48

    def validate(self) -> None:
        assert self.ahat == -self.sigma // 8
        assert self.p1 == 3 * self.sigma


def index_complex_for_v_plus_q(*, rank_c_f: int, ch2_f: int, q: int, k3: K3Data = K3Data()) -> int:
    """Return int_K3 Ahat ch((T_C^*K3 + q) tensor F).

    q=0 gives the full vector-spinor Dirac class.
    q=1 gives the raw gamma-trace-free RS class.
    q=-1 gives the common BRST/anomaly-style class, if independently derived.
    """

    k3.validate()
    return (4 + q) * rank_c_f * k3.ahat + rank_c_f * k3.p1 + (4 + q) * ch2_f


def spinor_index_complex(*, rank_c_f: int, ch2_f: int, k3: K3Data = K3Data()) -> int:
    """Return int_K3 Ahat ch(F)."""

    k3.validate()
    return rank_c_f * k3.ahat + ch2_f


def branch_summary(rank_c_f: int = 16, ch2_f: int = 0) -> dict[str, object]:
    full = index_complex_for_v_plus_q(rank_c_f=rank_c_f, ch2_f=ch2_f, q=0)
    raw = index_complex_for_v_plus_q(rank_c_f=rank_c_f, ch2_f=ch2_f, q=1)
    brst_style = index_complex_for_v_plus_q(rank_c_f=rank_c_f, ch2_f=ch2_f, q=-1)
    ghost = spinor_index_complex(rank_c_f=rank_c_f, ch2_f=ch2_f)
    return {
        "not_generation_count_proof": True,
        "rank_c_f": rank_c_f,
        "ch2_f": ch2_f,
        "k3": K3Data().__dict__,
        "index_complex": {
            "full_vector_spinor_q0": full,
            "raw_gamma_trace_free_q1": raw,
            "brst_style_if_derived_q_minus_1": brst_style,
            "spinor_ghost_complex": ghost,
        },
        "index_h_if_h_structure_verified": {
            "full_vector_spinor_q0": full / 2,
            "raw_gamma_trace_free_q1": raw / 2,
            "brst_style_if_derived_q_minus_1": brst_style / 2,
            "spinor_ghost_complex": ghost / 2,
        },
        "open_items": [
            "physical GU gauge-fixed RS symbol class",
            "right-H structure preservation by the pulled-back F connection",
            "actual ch_2(F)[K3] for the Sp(64) background",
            "APS eta/h terms if closed K3 is replaced by a boundary problem",
        ],
    }


class FormulaAuditTests(unittest.TestCase):
    def test_k3_data(self) -> None:
        K3Data().validate()

    def test_spinor_index_formula(self) -> None:
        self.assertEqual(spinor_index_complex(rank_c_f=16, ch2_f=0), 32)
        self.assertEqual(spinor_index_complex(rank_c_f=16, ch2_f=7), 39)

    def test_vector_spinor_formula_flat_f(self) -> None:
        self.assertEqual(index_complex_for_v_plus_q(rank_c_f=16, ch2_f=0, q=0), -640)

    def test_raw_gamma_trace_free_formula_flat_f(self) -> None:
        self.assertEqual(index_complex_for_v_plus_q(rank_c_f=16, ch2_f=0, q=1), -608)

    def test_brst_style_formula_flat_f_if_derived(self) -> None:
        self.assertEqual(index_complex_for_v_plus_q(rank_c_f=16, ch2_f=0, q=-1), -672)

    def test_brst_style_is_two_spinor_subtractions_from_raw(self) -> None:
        rank_c_f = 16
        ch2_f = 5
        raw = index_complex_for_v_plus_q(rank_c_f=rank_c_f, ch2_f=ch2_f, q=1)
        brst_style = index_complex_for_v_plus_q(rank_c_f=rank_c_f, ch2_f=ch2_f, q=-1)
        ghost = spinor_index_complex(rank_c_f=rank_c_f, ch2_f=ch2_f)
        self.assertEqual(brst_style, raw - 2 * ghost)

    @unittest.skip("The physical GU gauge-fixed RS complex has not supplied its symbol class.")
    def test_physical_gauge_fixed_gu_rs_index(self) -> None:
        raise NotImplementedError

    @unittest.skip("The actual Sp(64) background has not supplied ch_2(F)[K3].")
    def test_actual_background_ch2_f(self) -> None:
        raise NotImplementedError


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit K3 RS characteristic-class formulas.")
    parser.add_argument("--json", action="store_true", help="Print the flat-F branch summary as JSON.")
    args, remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(branch_summary(), indent=2, sort_keys=True))
        return 0

    print("K3 RS symbol-index formula audit: arithmetic only, not a generation-count proof.")
    print("Physical gauge-fixed GU RS symbol and ch_2(F) tests are intentionally skipped.")
    print()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FormulaAuditTests)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

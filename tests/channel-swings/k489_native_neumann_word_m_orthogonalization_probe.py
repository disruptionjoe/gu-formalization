#!/usr/bin/env python3
"""Independent controls and hostile mutations for K489."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k489_native_neumann_word_m_orthogonalization import build


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k489-native-neumann-word-m-orthogonalization.json"


def q(value: str) -> Fraction:
    return Fraction(value)


def checks(payload: dict) -> list[tuple[str, bool]]:
    theorem = payload["exact_theorem"]
    sectors = payload["native_sectors"]
    amplitudes = [Fraction(1), Fraction(1, 2), Fraction(1, 4)]
    a = sum((value * value for value in amplitudes), Fraction())
    b = sum((value * value for value in amplitudes[1:]), Fraction())
    coefficient = b / a
    direct_cross = b - coefficient * a
    direct_norm = b - 2 * coefficient * b + coefficient * coefficient * a
    out = [
        ("result id", payload["result_id"] == "K489-NATIVE-NEUMANN-WORD-M-ORTHOGONALIZATION"),
        ("native scope", payload["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("two sectors", [row["charge"] for row in sectors] == [[0, 0], [1, 0]]),
        ("word orthogonality", theorem["orthogonality"] == "<v_n,v_m>=0 for n!=m"),
        ("M block", theorem["M_block"] == "[[A,B],[B,B]]"),
        ("naive tail rejected", theorem["free_word_tail_equals_M_orthogonal_tail"] is False),
        ("corrected direction", theorem["corrected_tail"] == "t=G phi-(B/A)phi"),
        ("exact corrected norm", theorem["corrected_norm"] == "<t,Mt>=B/A"),
        ("multiplicities", [row["first_word_multiplicity"] for row in sectors] == [2, 1]),
        ("positive B", all(0 < q(row["B_tail_mass_interval"][0]) <= q(row["B_tail_mass_interval"][1]) for row in sectors)),
        ("nonzero naive cross", all(q(row["naive_M_cross_interval"][0]) > 0 for row in sectors)),
        ("projection below one", all(q(row["corrected_projection_coefficient_interval"][1]) < 1 for row in sectors)),
        ("positive determinant", all(row["two_vector_Gram_positive"] is True for row in sectors)),
        ("complete complement withheld", payload["decision"]["complete_M_orthogonal_complement_constructed"] is False),
        ("combined floor withheld", payload["decision"]["combined_K139_K168_floor_emitted"] is False),
        ("finite direct M cross vanishes", direct_cross == 0),
        ("finite direct corrected norm", direct_norm == b / a),
        ("finite Gram determinant", a * b - b * b == b),
    ]
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    stored = json.loads(MANIFEST.read_text())
    rebuilt = build()
    results = checks(stored)
    results.append(("deterministic rebuild", stored == rebuilt))
    if not all(ok for _, ok in results):
        raise AssertionError([name for name, ok in results if not ok])
    mutations = [
        lambda p: p["exact_theorem"].__setitem__("free_word_tail_equals_M_orthogonal_tail", True),
        lambda p: p["exact_theorem"].__setitem__("M_block", "I"),
        lambda p: p["exact_theorem"].__setitem__("corrected_norm", "B"),
        lambda p: p["native_sectors"].pop(),
        lambda p: p["native_sectors"][0].__setitem__("first_word_multiplicity", 1),
        lambda p: p["native_sectors"][0].__setitem__("naive_M_cross_interval", ["0", "0"]),
        lambda p: p["decision"].__setitem__("complete_M_orthogonal_complement_constructed", True),
        lambda p: p["decision"].__setitem__("combined_K139_K168_floor_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        if not all(ok for _, ok in checks(candidate)):
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError("hostile mutation survived")
    print(f"K489 CONTROL: {len(results)}/{len(results)} pass; hostile {rejected}/{len(mutations)} rejected")
    if args.selftest:
        print("K489 SELFTEST: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

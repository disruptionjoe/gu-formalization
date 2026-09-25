#!/usr/bin/env python3
"""Independent controls and hostile mutations for K473."""

from __future__ import annotations

import copy
from fractions import Fraction

from k473_k152_recursive_complement_floor import CertificateError, demo, recursive_floor


def checks(p):
    t, e, o, n = p["theorem"], p["exact_square_control"], p["outward_nonsquare_control"], p["native_release"]
    return [
        p["schema_version"] == "1.0",
        p["result_id"] == "K473-K152-RECURSIVE-COMPLEMENT-FLOOR",
        p["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        p["direction"] == "observed_to_native",
        "complete K162 complement" in t["decomposition"],
        len(t["premises"]) == 3,
        "beta" in t["floor"],
        t["target_test"] == "alpha>b, gamma>b, mu^2<(alpha-b)(gamma-b)",
        t["sharp_for_scalar_two_block"] is True,
        e["discriminant"] == "25",
        e["complete_complement_floor_outward_interval"] == ["2", "2"],
        e["strict_beta_above_b"] is True,
        e["same_fixed_limiting_form"] is True,
        e["complete_M_orthogonal_partition"] is True,
        o["discriminant"] == "8",
        Fraction(o["complete_complement_floor_outward_interval"][0]) > Fraction(5, 2),
        Fraction(o["sqrt_outward_interval"][1]) - Fraction(o["sqrt_outward_interval"][0]) == Fraction(1, 65536),
        n["finite_slice_packet_present"] is False,
        n["complete_tail_packet_present"] is False,
        n["cross_packet_present"] is False,
        n["native_beta_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("decomposition", "finite Ritz only"),
        lambda d: d["theorem"].__setitem__("premises", []),
        lambda d: d["theorem"].__setitem__("target_test", "mu unrestricted"),
        lambda d: d["theorem"].__setitem__("sharp_for_scalar_two_block", False),
        lambda d: d["exact_square_control"].__setitem__("discriminant", "24"),
        lambda d: d["exact_square_control"].__setitem__("complete_complement_floor_outward_interval", ["1", "2"]),
        lambda d: d["exact_square_control"].__setitem__("same_fixed_limiting_form", False),
        lambda d: d["exact_square_control"].__setitem__("complete_M_orthogonal_partition", False),
        lambda d: d["outward_nonsquare_control"].__setitem__("discriminant", "9"),
        lambda d: d["native_release"].__setitem__("native_beta_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        c = copy.deepcopy(packet); mutate(c)
        rejected += not all(checks(c))
    invalid = 0
    base_kwargs = dict(finite_slice_floor=3, tail_floor=6, cross_norm_upper=2,
                       target_threshold=1, finite_slice_ref="F", complete_tail_ref="T",
                       cross_block_ref="X", same_fixed_form=True,
                       complete_m_orthogonal_partition=True)
    for update in ({"finite_slice_floor": 1}, {"tail_floor": 1}, {"cross_norm_upper": 4},
                   {"cross_norm_upper": -1}, {"finite_slice_ref": None},
                   {"same_fixed_form": False}, {"complete_m_orthogonal_partition": False}):
        kw = dict(base_kwargs); kw.update(update)
        try: recursive_floor(**kw)
        except CertificateError: invalid += 1
    print(f"K473 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K473 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K473 INVALID INPUTS: {invalid}/7 rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == 7 else 1


if __name__ == "__main__":
    raise SystemExit(main())

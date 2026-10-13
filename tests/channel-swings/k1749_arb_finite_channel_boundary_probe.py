#!/usr/bin/env python3
"""Hostile mutations for K1749's finite-channel Arb certificate."""
from __future__ import annotations

import copy
import json
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1749-arb-finite-channel-boundary.json").read_text())


def valid(d):
    try:
        a, m, s, z, c, post = (d["arb_certificate"], d["method"],
                                d["singular_boundary_chart"], d["decision"],
                                d["controls"], d["post_flight"])
        gap = arb(a["whole_line_gap_fixed_minus_selected"])
        compact = arb(a["compact_gap_fixed_minus_selected"])
        tail = arb(a["combined_tail_upper"])
        boundary = a["boundary"]
        return all([
            d["schema_version"] == "1.0",
            d["claim_id"] == "K1749",
            d["backend"] == "python-flint==0.9.0",
            a["q"] == "1/1024",
            a["compact_radius"] == "11",
            a["cell_half_width"] == "1/16",
            a["taylor_order"] == 12,
            a["compact_cell_count"] == 352,
            gap > 0,
            compact > 0,
            tail > 0,
            tail.upper() < compact.lower(),
            arb(boundary["u_minus_q"]).contains(0),
            arb(boundary["t"]) == 1,
            arb(boundary["v"]) == 0,
            "strictly positive" in m["positive_denominator_form"],
            "Taylor" in m["compact_enclosure"],
            "Gaussian" in m["tail_enclosure"],
            s["fisher_status"] == "+infinity (extended-value convention)",
            "not a Lebesgue density" in s["typed_boundary"],
            z["positive_denominator_whole_line_integrand_derived"],
            z["compact_arb_and_analytic_tails_certified"],
            z["selected_beats_k1728_at_q_1_over_1024_proved"],
            z["u_equals_q_singular_chart_explicitly_handled"],
            not z["whole_two_radius_chart_ordered"],
            not z["global_two_radius_optimizer_proved"],
            not z["all_seed_optimizer_proved"],
            not z["source_or_physical_status_change"],
            c["producer_passes"] == 44,
            c["hostile_mutations_rejected"] == 20,
            "remote interior channel" in post["strongest_counterexample_seam"],
            "python-flint==0.9.0" in post["reproducibility_seam"],
        ])
    except (KeyError, TypeError, ValueError):
        return False


assert valid(DATA)
mutations = [
    lambda d: d.__setitem__("claim_id", "K1744"),
    lambda d: d.__setitem__("backend", "binary float"),
    lambda d: d["arb_certificate"].__setitem__("q", "1/1000"),
    lambda d: d["arb_certificate"].__setitem__("compact_radius", "0"),
    lambda d: d["arb_certificate"].__setitem__("cell_half_width", "1"),
    lambda d: d["arb_certificate"].__setitem__("taylor_order", 2),
    lambda d: d["arb_certificate"].__setitem__("compact_cell_count", 1),
    lambda d: d["arb_certificate"].__setitem__("whole_line_gap_fixed_minus_selected", "[-1e-13 +/- 1e-20]"),
    lambda d: d["arb_certificate"].__setitem__("combined_tail_upper", "[2e-13 +/- 1e-20]"),
    lambda d: d["arb_certificate"]["boundary"].__setitem__("u_minus_q", "1"),
    lambda d: d["arb_certificate"]["boundary"].__setitem__("t", "0.9"),
    lambda d: d["arb_certificate"]["boundary"].__setitem__("v", "0.1"),
    lambda d: d["method"].__setitem__("positive_denominator_form", "unchecked denominator"),
    lambda d: d["method"].__setitem__("tail_enclosure", "tails omitted"),
    lambda d: d["singular_boundary_chart"].__setitem__("fisher_status", "finite"),
    lambda d: d["decision"].__setitem__("selected_beats_k1728_at_q_1_over_1024_proved", False),
    lambda d: d["decision"].__setitem__("whole_two_radius_chart_ordered", True),
    lambda d: d["decision"].__setitem__("global_two_radius_optimizer_proved", True),
    lambda d: d["decision"].__setitem__("all_seed_optimizer_proved", True),
    lambda d: d["decision"].__setitem__("source_or_physical_status_change", True),
]
for index, mutation in enumerate(mutations, 1):
    altered = copy.deepcopy(DATA)
    mutation(altered)
    assert not valid(altered), index
    print(f"PASS {index:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")

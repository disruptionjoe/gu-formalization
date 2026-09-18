#!/usr/bin/env python3
"""Independent K229 cover arithmetic and spot replay of signed cell enclosures."""
from __future__ import annotations

import json
from fractions import Fraction as Q

from k221_order_six_signed_quadratic_cell_enclosure import K185, signed_quadratic_bounds
from k222_order_six_first_middle_shell_cover import SCALE, cosh, sinh
from k229_order_six_third_shell_signed_cost_stress import OUT, PI_LOWER


def run(doc):
    assert doc["candidate_count"] == 64 and doc["selected_cell_count"] == 16
    assert len(doc["cells"]) == 8
    source = json.loads(K185.read_text())
    shell_measure = Q(0)
    coarse = selected = (Q(0), Q(0))
    for j, row in enumerate(doc["cells"]):
        assert row["first_exceeding_coordinate"] == j
        bands = [(Q(1), Q(4))] * j + [(Q(4), Q(5))] + [(Q(1), Q(5))] * (7-j)
        measure = Q(1)
        for a, b in bands:
            measure *= sinh(b)-sinh(a)
        assert Q(row["coarse_measure"]) == measure
        shell_measure += measure
        assert 0 <= row["selected_axis"] < 8
        a, b = bands[row["selected_axis"]]
        cut = (a+b)/2
        assert Q(row["selected_cut_exp_t"]) == cut
        coarse = tuple(coarse[k]+Q(row["coarse_interval_without_pi8"][k]) for k in range(2))
        selected = tuple(selected[k]+Q(row["selected_interval_without_pi8"][k]) for k in range(2))
        options = list(map(Q, row["candidate_absolute_uppers_without_pi8"]))
        assert len(options) == 8 and (options[row["selected_axis"]], row["selected_axis"]) == min((v, k) for k, v in enumerate(options))
        assert max(-Q(row["selected_interval_without_pi8"][0]), Q(row["selected_interval_without_pi8"][1])) == options[row["selected_axis"]]
        # Reconstruct the selected children without calling producer interval/cover helpers.
        if j in (0, 3, 7):
            replay = [Q(0), Q(0)]
            for low, high in ((a, cut), (cut, b)):
                part = bands.copy()
                part[row["selected_axis"]] = (low, high)
                corners = (tuple(cosh(x) for x, _ in part), tuple(cosh(y) for _, y in part))
                core = signed_quadratic_bounds(source, *corners)["intersection_core"]
                weight = Q(1)
                for x, y in part:
                    weight *= sinh(y)-sinh(x)
                for k in range(2):
                    replay[k] += SCALE*weight*core[k]
            assert tuple(replay) == tuple(map(Q, row["selected_interval_without_pi8"]))
    assert shell_measure == Q(doc["exact_shell_measure"]) == sinh(Q(5))**8-sinh(Q(4))**8
    assert list(map(str, coarse)) == doc["coarse_interval_without_pi8"]
    assert list(map(str, selected)) == doc["selected_interval_without_pi8"]
    assert max(-selected[0], selected[1])/PI_LOWER**8 == Q(doc["selected_absolute_upper_using_pi_gt_31_over_10"])
    assert Q(doc["selected_upper_to_remaining_allocation"]) == Q(doc["selected_absolute_upper_using_pi_gt_31_over_10"])/Q(doc["remaining_all_farther_allocation"])


if __name__ == "__main__":
    data = json.loads(OUT.read_text())
    run(data)
    broken = json.loads(OUT.read_text())
    broken["cells"][3]["selected_axis"] = (broken["cells"][3]["selected_axis"]+1)%8
    try:
        run(broken)
    except AssertionError:
        pass
    else:
        raise AssertionError("hostile selected-axis mutation escaped")
    print("[PASS] K229 independent cover/selected-interval spot replay and hostile mutation")

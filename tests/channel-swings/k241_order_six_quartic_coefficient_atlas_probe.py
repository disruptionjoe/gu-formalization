#!/usr/bin/env python3
"""Independent K241 coefficient and budget controls."""
from __future__ import annotations

from fractions import Fraction as Q
import json

from k225_order_six_diagonal_cancellation import K185, terms
from k231_order_six_projected_diagonal_jet import orbit_jet
from k241_order_six_quartic_coefficient_atlas import (
    HEADROOM, OUT, signed_jet, symbolic_groups,
)


def main():
    manifest = json.loads(OUT.read_text())
    lower = Q(manifest["atlas"]["global_lower"])
    upper = Q(manifest["atlas"]["global_upper"])
    shell = Q(manifest["quartic_shell"]["upper"])
    raw_remainder = Q(manifest["raw_remainder_discriminator"]["full_q5_cube_upper"])
    items = list(terms(json.loads(K185.read_text())))
    groups = symbolic_groups(items)

    # Replay A in two genuinely different ways: the symbolic group jet and
    # K231's raw fifteen-pair orbit jet.
    for u, v in ((Q(1), Q(1)), (Q(5), Q(5)), (Q(5, 4), Q(17, 8)), (Q(7, 2), Q(9, 2))):
        grouped = signed_jet(groups, u, v)[0]
        raw = orbit_jet(items, (u, v) + (Q(1),)*6, 2)[4]
        assert grouped == raw
        assert lower <= raw <= upper

    assert 0 < shell < HEADROOM
    assert raw_remainder > HEADROOM
    # Hostile controls: the K233 raw absolute fifth method and an unsigned
    # replacement are not the grouped K241 coefficient theorem.
    unsigned = sum(abs(weight) for _, weight in groups)
    signed = sum(weight for _, weight in groups)
    assert unsigned > abs(signed)
    assert manifest["atlas"]["grid"] == [8, 8]
    assert manifest["domain"]["anchor_b"] == 1
    print("[PASS] K241 independent raw/grouped coefficient and shell-budget replay")


if __name__ == "__main__":
    main()

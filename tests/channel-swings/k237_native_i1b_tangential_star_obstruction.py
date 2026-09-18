#!/usr/bin/env python3
"""K237: full-grade tangential test of K236's selected normal-symbol star."""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K236 = ROOT / "lab/process/k236-native-i1b-invariant-mixed-grade-symbol.json"
OUT = ROOT / "lab/process/k237-native-i1b-tangential-star-obstruction.json"


def generate():
    with redirect_stdout(StringIO()) as log:
        m = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    full, one, zero = m["FULL"], m["ONE"], m["ZERO"]
    channels = ("comm", "symi", "symi")

    def direction(mu, blade):
        return {1 << mu: {blade: one}}

    tangent = direction(1, 0)

    def raw(left, right):
        image = m["shiab"](m["wedge_raw"](tangent, right), channels)
        value = m["wedge_raw"](left, image).get(full, {}).get(0, zero)
        assert value[1] == 0
        return value[0]

    def image_of(right):
        image = m["shiab"](m["wedge_raw"](tangent, right), channels)
        out = {}
        # A nonzero scalar pairing requires the complementary form leg and
        # the identical Clifford blade. Do not truncate to K235's 28 labels.
        for form_mask, blades in image.items():
            complement = full ^ form_mask
            if complement == 0 or complement & (complement - 1):
                continue
            mu = complement.bit_length() - 1
            for blade in blades:
                left = direction(mu, blade)
                euler = (raw(left, right) - raw(right, left)) / 2
                if euler:
                    out[(mu, blade)] = euler
        return out

    odd = direction(0, 1 << 1)
    spokes = [direction(j, (1 << 1) | (1 << j)) for j in range(2, 14)]
    odd_output = image_of(odd)
    assert odd_output == {(1, 3): Q(-1)}
    # Selected E pairings include reverse-only contributions; do not call a
    # forward-support enumeration the complete matrix image.
    selected_even = {}
    for mu, blade in ((0, 1), (2, 4), (13, 1 << 13)):
        left = direction(mu, blade)
        selected_even[(mu, blade)] = sum(
            ((raw(left, spoke) - raw(spoke, left)) / 2 for spoke in spokes), Q())
    assert selected_even == {(0, 1): Q(12), (2, 4): Q(10), (13, 1 << 13): Q(10)}
    return {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__LOCAL_SELECTED_SYMBOL_ONLY",
        "input_sha256": {"backend": sha256(BACKEND.read_bytes()).hexdigest(),
                         "k236": sha256(K236.read_bytes()).hexdigest()},
        "object": "Selected comm/symi/symi I1B formal Euler principal coefficient at dx1 on the same flat Ricci-flat T=0 zero-fermion germ as K236",
        "normal_star": "K236: o=dx0 gamma1, E=sum_j dxj gamma1 gammaj (j=2..13); N0(o)=-E and N0(E)=12o",
        "tangential_witnesses": [
            "<dx1 gamma01,N1(o)>=-1",
            "<dx0 gamma0,N1(E)>=12; <dx2 gamma2,N1(E)>=10; <dx13 gamma13,N1(E)>=10",
        ],
        "selected_odd_coefficient": [1, 3, "-1"],
        "selected_collective_coefficients": [[mu, blade, str(v)] for (mu, blade), v in sorted(selected_even.items())],
        "theorem": "The K236 rank-two star is not a common invariant subspace of the selected principal-symbol family: the dx1 gamma01 coefficient of N1(o) is -1 outside span{o,E}. Selected coefficients of N1(E) also escape. This is an exact local obstruction to that particular two-dimensional reduction, not an exhaustive output matrix, a larger-hull obstruction, or an obstruction to another source-admissible Shiab.",
        "claim_ceiling": "Exact selected local tangential-symbol output only. No full action-selected fermion operator, stationary common domain, quotient, propagating mode, source/physics/ledger/canon/public change, or signed-third-shell result."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K237 exact tangential escape from K236 rank-two star")

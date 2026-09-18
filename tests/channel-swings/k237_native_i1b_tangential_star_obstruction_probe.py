#!/usr/bin/env python3
"""Independent selected-contraction replay and hostile controls for K237."""
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
RECORD = ROOT / "lab/process/k237-native-i1b-tangential-star-obstruction.json"


def main():
    record = json.loads(RECORD.read_text())
    assert record["input_sha256"] == {
        "backend": sha256(BACKEND.read_bytes()).hexdigest(),
        "k236": sha256(K236.read_bytes()).hexdigest()}
    with redirect_stdout(StringIO()) as log:
        m = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full = m["ONE"], m["ZERO"], m["FULL"]

    def d(mu, blade):
        return {1 << mu: {blade: one}}

    def ordered(left, right, normal, channels=("comm", "symi", "symi")):
        im = m["shiab"](m["wedge_raw"](normal, right), channels)
        return m["wedge_raw"](left, im).get(full, {}).get(0, zero)

    n1, odd = d(1, 0), d(0, 2)
    out_odd = d(1, 3)
    assert ordered(out_odd, odd, n1) == (Q(-2), Q())
    assert ordered(odd, out_odd, n1) == zero
    assert (ordered(out_odd, odd, n1)[0] - ordered(odd, out_odd, n1)[0])/2 == -1

    # Full E: all twelve spokes contribute to the new dx0 gamma0 output;
    # a given dxj gammaj has eleven forward and one reverse contribution.
    spokes = [d(j, 2 | (1 << j)) for j in range(2, 14)]
    for target, expected in ((d(0, 1), 12), (d(2, 4), 10), (d(13, 1 << 13), 10)):
        forward = sum((ordered(target, spoke, n1)[0] for spoke in spokes), Q())
        reverse = sum((ordered(spoke, target, n1)[0] for spoke in spokes), Q())
        assert (forward - reverse)/2 == expected
    assert record["selected_odd_coefficient"] == [1, 3, "-1"]
    assert record["selected_collective_coefficients"] == [[0, 1, "12"], [2, 4, "10"], [13, 8192, "10"]]
    assert ordered(out_odd, odd, d(0, 0)) == zero
    assert ordered(out_odd, odd, n1, ("symi", "symi", "symi")) == zero
    assert sum((ordered(d(0, 1), spoke, n1)[0] for spoke in spokes[:-1]), Q()) != 24
    print("[PASS] K237 independent ordered replay, twelve-spoke counts and hostile normal/channel/omission controls")


if __name__ == "__main__":
    main()

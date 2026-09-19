#!/usr/bin/env python3
"""Independent source/support replay and hostile controls for K250."""
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K236 = ROOT / "lab/process/k236-native-i1b-invariant-mixed-grade-symbol.json"
K249 = ROOT / "lab/process/k249-native-i1b-common-principal-hull.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
EXTRACTION = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
RECORD = ROOT / "lab/process/k250-native-i1b-source-selection-and-all-direction-growth.json"
CHANNELS = ("comm", "symi", "symi")


def main() -> None:
    record = json.loads(RECORD.read_text())
    assert record["input_sha256"] == {
        "backend": sha256(BACKEND.read_bytes()).hexdigest(),
        "k236": sha256(K236.read_bytes()).hexdigest(),
        "k249": sha256(K249.read_bytes()).hexdigest(),
        "source_register": sha256(REGISTER.read_bytes()).hexdigest(),
        "source_extraction": sha256(EXTRACTION.read_bytes()).hexdigest(),
    }
    source = EXTRACTION.read_text()
    register = REGISTER.read_text()
    assert source.count("southeast-zero") == 5
    assert "SE=0` is the displayed 2021 candidate" in source
    assert "SE!=0` is explicitly source-admitted" in source
    assert "neither source supplies a uniqueness theorem" in source
    assert "- id: SC-OP-04\n  polarity: ASSERTS" in register
    assert "- id: SC-OP-05\n  polarity: UNCERTAIN" in register
    assert record["source_selection"]["decision"].endswith("unique full fermion operator")

    with redirect_stdout(StringIO()) as log:
        m = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full = m["ONE"], m["ZERO"], m["FULL"]

    def direction(mu: int, blade: int):
        return {1 << mu: {blade: one}}

    odd = direction(0, 1 << 1)
    observed = []
    for principal in range(1, 14):
        normal = direction(principal, 0)
        image = m["shiab"](m["wedge_raw"](normal, odd), CHANNELS)
        blade = (1 << 0) | (1 << principal)
        left = direction(1, blade)
        forward = m["wedge_raw"](left, image).get(full, {}).get(0, zero)
        reverse_image = m["shiab"](m["wedge_raw"](normal, left), CHANNELS)
        reverse = m["wedge_raw"](odd, reverse_image).get(full, {}).get(0, zero)
        label = blade ^ (1 << 1)
        assert forward == (Q(-2), Q()) and reverse == zero
        observed.append((principal, label, (forward[0] - reverse[0]) / 2))
    assert [row[2] for row in observed] == [Q(-1)] * 13
    outside = [label for principal, label, _ in observed if principal >= 2]
    assert outside == record["principal_symbol"]["outside_labels_p2_through_p13"]
    assert len(set(outside)) == 12 and not set(outside).intersection(range(4))

    # Independent sparse-coordinate rank replay.
    keys = [(0, 2)]
    spokes = [(j, 2 | (1 << j)) for j in range(2, 14)]
    images = [(1, 1 | (1 << p)) for p in range(1, 14)]
    universe = list(dict.fromkeys([*keys, *spokes, *images]))
    lookup = {key: i for i, key in enumerate(universe)}
    vectors = []
    odd_vector = sp.zeros(len(universe), 1)
    odd_vector[lookup[keys[0]]] = 1
    vectors.append(odd_vector)
    collective = sp.zeros(len(universe), 1)
    for key in spokes:
        collective[lookup[key]] = 1
    vectors.append(collective)
    for key in images:
        vector = sp.zeros(len(universe), 1)
        vector[lookup[key]] = 1
        vectors.append(vector)
    assert sp.Matrix.hstack(*vectors).rank() == 15
    assert sp.Matrix.hstack(*vectors[:-1]).rank() == 14  # hostile dropped direction
    assert sum(label in range(4) for label in outside) == 0  # hostile projection erases all 12

    assert "No complete all-direction hull" in record["claim_ceiling"]
    assert "does not select a unique" in record["source_selection"]["decision"]
    print("[PASS] K250 independent source/support replay and hostile controls")


if __name__ == "__main__":
    main()

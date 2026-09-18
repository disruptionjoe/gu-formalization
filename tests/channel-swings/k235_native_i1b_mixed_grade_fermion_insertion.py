#!/usr/bin/env python3
"""K235: one exact I1B mixed-grade symbol entry and formal four-field insertion."""
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
SOURCE = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
K132 = ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json"
OUT = ROOT / "lab/process/k235-native-i1b-mixed-grade-fermion-insertion.json"


def calculate(channels=("comm", "symi", "symi")):
    with redirect_stdout(StringIO()) as output:
        m = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in output.getvalue()
    one, zero, full = m["ONE"], m["ZERO"], m["FULL"]

    def direction(mu, blade):
        return {1 << mu: {blade: one}}

    def coefficient(left, right):
        normal = direction(0, 0)
        image = m["shiab"](m["wedge_raw"](normal, right), channels)
        return m["wedge_raw"](left, image).get(full, {}).get(0, zero)

    # T is a connection difference; on the T=0 background these independent
    # distortion directions have no separate gauge derivative (K132).
    odd = direction(0, 1 << 1)          # dx^0 tensor gamma_1 (Cl1)
    even = direction(2, (1 << 1) | (1 << 2))  # dx^2 tensor gamma_12 (Cl2)
    raw_odd_even = coefficient(odd, even)
    raw_even_odd = coefficient(even, odd)
    euler = tuple((a-b)/2 for a, b in zip(raw_odd_even, raw_even_odd))
    assert raw_odd_even == (Q(2), Q()) and raw_even_odd == zero
    assert euler == (Q(1), Q())

    # Complex Cl(7,7) Dirac chirality: its volume element anticommutes with
    # odd blades and commutes with even ones. This supplies local parity only.
    parity = {}
    squares = {}
    for name, blade in (("odd", 1 << 1), ("even", (1 << 1) | (1 << 2))):
        left = m["blade_product"](full, blade)
        right = m["blade_product"](blade, full)
        assert left[0] == right[0] and left[1] in (right[1], -right[1])
        parity[name] = "off_diagonal" if left[1] == -right[1] else "diagonal"
        square = m["blade_product"](blade, blade)
        assert square[0] == 0 and square[1] != 0
        squares[name] = square[1]
    assert parity == {"odd": "off_diagonal", "even": "diagonal"}
    assert squares == {"odd": -1, "even": -1}

    # First derivative of all sixteen displayed entries of draft eq. 9.16.
    # E and O are the even/odd block insertions; bar/star are NOT assigned a
    # reality condition. d0 stays fixed in this pure-distortion derivative.
    insertion = [
        ["*odot(E_pp)", "*odot(O_pm)", "E_pp", "O_pm"],
        ["*odot(O_mp)", "*odot(E_mm)", "O_mp", "E_mm"],
        ["-bar(E_pp)*", "-bar(O_pm)*", "0", "0"],
        ["-bar(O_mp)*", "-bar(E_mm)*", "0", "0"],
    ]
    source = SOURCE.read_text()
    assert "with operators like" in source and "non-trivial map in the lower right quadrant" in source
    assert "four distinct fields" in source and "S-FULL-DIRAC" in source
    return {
        "schema_version": "1.0", "classification": "SOURCE_NATIVE_ROUTE__LOCAL_FORMAL_CANDIDATE_ONLY",
        "input_sha256": {"backend": sha256(BACKEND.read_bytes()).hexdigest(),
                         "source_extraction": sha256(SOURCE.read_bytes()).hexdigest(),
                         "k132": sha256(K132.read_bytes()).hexdigest()},
        "background": "selected I1B local flat Ricci-flat T=0, zero-fermion germ; fixed metric and formal normal dx0",
        "mode": {"odd": "dx0 tensor gamma1", "even": "dx2 tensor gamma12",
                 "raw_odd_even": [str(x) for x in raw_odd_even],
                 "raw_even_odd": [str(x) for x in raw_even_odd],
                 "formal_euler_cross": [str(x) for x in euler],
                 "gauge_status": "non-gauge distortion directions at T=0; not a physical quotient mode"},
        "chirality_parity": parity,
        "clifford_squares": squares,
        "displayed_fermion_candidate_first_variation": insertion,
        "source_branch": "2021 displayed southeast-zero four-field matrix only; source admits an unspecified nonzero southeast rival",
        "underdetermination": "The local parity and matrix slots do not select the source-preferred Shiab, global plus/minus grading, barred-field reality/adjoint, density and common closed domain, stationary nonzero-fermion solution, gauge/BV quotient or positive physical state. No action-owned spectral mode follows.",
        "claim_ceiling": "Exact nonzero mixed Cl1-Cl2 bosonic symbol and all sixteen formal displayed fermion insertion slots at one local zero-fermion background. No full physical fermion Hessian/domain, common eigenmode, spectrum, 2+1, chirality, positivity, gravity, ledger, canon or source-status change."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = calculate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K235 exact native mixed-grade symbol and full displayed matrix insertion")

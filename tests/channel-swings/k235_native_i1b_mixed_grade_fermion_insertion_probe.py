#!/usr/bin/env python3
"""Independent 28-basis K235 block replay, parity and hostile channel controls."""
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
backend = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
source = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
prior = ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json"
record = json.loads((ROOT / "lab/process/k235-native-i1b-mixed-grade-fermion-insertion.json").read_text())
assert record["input_sha256"] == {
    "backend": sha256(backend.read_bytes()).hexdigest(),
    "source_extraction": sha256(source.read_bytes()).hexdigest(),
    "k132": sha256(prior.read_bytes()).hexdigest(),
}

with redirect_stdout(StringIO()) as output:
    m = runpy.run_path(str(backend))
assert "FAILURES=0" in output.getvalue()
one, zero, full, n = m["ONE"], m["ZERO"], m["FULL"], m["N"]
basis = [(label, mu, label ^ (1 << mu)) for label in (2, 3) for mu in range(n)]
lookup = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}

def direction(mu, mask):
    return {1 << mu: {mask: one}}

def form_coefficient(left, right):
    return m["wedge_raw"](left, right).get(full, {}).get(0, zero)

def block(channels):
    raw = sp.zeros(28)
    normal = direction(0, 0)
    for column, (_, mu, mask) in enumerate(basis):
        image = m["shiab"](m["wedge_raw"](normal, direction(mu, mask)), channels)
        for form_mask, element in image.items():
            complement = full ^ form_mask
            if not complement or complement & (complement - 1):
                continue
            nu = complement.bit_length() - 1
            for outmask in element:
                row = lookup.get((outmask ^ (1 << nu), nu))
                if row is None:
                    continue
                value = form_coefficient(direction(nu, outmask), image)
                assert value[1] == 0
                raw[row, column] += sp.Rational(value[0].numerator, value[0].denominator)
    return raw, (raw - raw.T) / 2

raw, euler = block(("comm", "symi", "symi"))
odd, even = lookup[(3, 0)], lookup[(2, 2)]
assert (odd, even) == (14, 2)
assert raw[odd, even] == 2 and raw[even, odd] == 0
assert euler[odd, even] == 1 and euler[even, odd] == -1
assert euler.rank() == 6 and euler.T == -euler
assert record["mode"]["formal_euler_cross"] == ["1", "0"]

# A wrong first product channel kills this selected cross entry; reversing one
# distortion direction reverses its sign. Neither plant tests an invented
# fermion domain or full Hessian.
wrong_channels = ("symi", "symi", "symi")
normal = direction(0, 0)
wrong_forward = m["shiab"](m["wedge_raw"](normal, direction(2, 6)), wrong_channels)
wrong_reverse = m["shiab"](m["wedge_raw"](normal, direction(0, 2)), wrong_channels)
assert form_coefficient(direction(0, 2), wrong_forward) == zero
assert form_coefficient(direction(2, 6), wrong_reverse) == zero
assert -euler[odd, even] == -1
assert {basis[odd][2].bit_count(), basis[even][2].bit_count()} == {1, 2}
assert record["chirality_parity"] == {"odd": "off_diagonal", "even": "diagonal"}
assert record["clifford_squares"] == {"odd": -1, "even": -1}
assert m["emul"](m["blade"](1), m["blade"](1)) == {0: (Q(-1), Q())}
assert m["emul"](m["blade"]((1, 2)), m["blade"]((1, 2))) == {0: (Q(-1), Q())}
matrix = record["displayed_fermion_candidate_first_variation"]
assert len(matrix) == 4 and all(len(row) == 4 for row in matrix)
assert [matrix[i][2:] for i in (2, 3)] == [["0", "0"], ["0", "0"]]
assert sum(cell != "0" for row in matrix for cell in row) == 12
assert "not a unique" in source.read_text()
print("[PASS] K235 independent full 28-basis replay, 12-slot insertion and hostile channel/sign controls")

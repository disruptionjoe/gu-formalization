#!/usr/bin/env python3
"""Independent raw source-arithmetic replay of the K236 twelve-spoke star."""
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K235 = ROOT / "lab/process/k235-native-i1b-mixed-grade-fermion-insertion.json"
K235_PROBE = ROOT / "tests/channel-swings/k235_native_i1b_mixed_grade_fermion_insertion_probe.py"
record = json.loads((ROOT / "lab/process/k236-native-i1b-invariant-mixed-grade-symbol.json").read_text())
assert record["input_sha256"] == {
    "backend": sha256(BACKEND.read_bytes()).hexdigest(),
    "k235_manifest": sha256(K235.read_bytes()).hexdigest(),
    "k235_probe": sha256(K235_PROBE.read_bytes()).hexdigest(),
}
with redirect_stdout(StringIO()) as output:
    m = runpy.run_path(str(BACKEND))
assert "FAILURES=0" in output.getvalue()

one, zero, full = m["ONE"], m["ZERO"], m["FULL"]
basis = [(label, mu, label ^ (1 << mu)) for label in (2, 3) for mu in range(14)]
normal = {1: {0: one}}

def direction(mu, mask):
    return {1 << mu: {mask: one}}

def raw(left, right, channels=("comm", "symi", "symi")):
    image = m["shiab"](m["wedge_raw"](normal, right), channels)
    return m["wedge_raw"](left, image).get(full, {}).get(0, zero)

vectors = [direction(mu, mask) for _, mu, mask in basis]
for j in range(2, 14):
    assert basis[j] == (2, j, 2 | (1 << j))
    assert raw(vectors[14], vectors[j]) == (Q(2), Q())
    assert raw(vectors[j], vectors[14]) == zero
    for i in range(28):
        forward = raw(vectors[i], vectors[j])
        reverse = raw(vectors[j], vectors[i])
        assert forward[1] == reverse[1] == 0
        assert (forward[0] - reverse[0])/2 == (1 if i == 14 else 0)
        forward = raw(vectors[i], vectors[14])
        reverse = raw(vectors[14], vectors[i])
        assert forward[1] == reverse[1] == 0
        assert (forward[0] - reverse[0])/2 == (-1 if 2 <= i <= 13 else 0)
    # Mutating the first source-permitted product channel kills this exact
    # cross, rather than preserving an accidental fitted spoke coefficient.
    wrong = ("symi", "symi", "symi")
    assert raw(vectors[14], vectors[j], wrong) == zero
    assert raw(vectors[j], vectors[14], wrong) == zero

assert len(record["even_spokes"]) == 12
assert len(record["eleven_exact_kernel_differences"]) == 11
assert record["restricted_matrix_basis_o_E"] == [[0, 12], [-1, 0]]
assert record["restricted_square"] == -12 and record["star_rank"] == 2
# A single spoke is not invariant: o maps to every one of the twelve.
assert raw(vectors[3], vectors[14]) == zero  # raw reverse is zero
assert raw(vectors[14], vectors[3]) == (Q(2), Q())
print("[PASS] K236 independent 12-by-28 raw replay and hostile omitted-spoke/channel controls")

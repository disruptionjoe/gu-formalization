#!/usr/bin/env python3
"""Independent reverse-basis replay for K276."""

from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / "lab/process/k276-sc-act-06-euclidean-principal-complex-data-gate.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"


def modular_rank(matrix: list[list[int]], prime: int = 1009) -> int:
    work = [[value % prime for value in row] for row in reversed(matrix)]
    if not work:
        return 0
    rows, cols = len(work), len(work[0])
    pivot_row = 0
    for col in reversed(range(cols)):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inv = pow(work[pivot_row][col], prime - 2, prime)
        work[pivot_row] = [(value * inv) % prime for value in work[pivot_row]]
        for r in range(pivot_row + 1, rows):
            if work[r][col]:
                factor = work[r][col]
                work[r] = [(work[r][c] - factor * work[pivot_row][c]) % prime for c in range(cols)]
        pivot_row += 1
    return pivot_row


def exterior_symbol(n: int, degree: int, xi: tuple[int, ...]) -> tuple[list[tuple[int, ...]], list[list[int]]]:
    inputs = list(reversed(list(combinations(range(n), degree))))
    outputs = list(reversed(list(combinations(range(n), degree + 1))))
    matrix = [[0 for _ in inputs] for _ in outputs]
    for c, basis in enumerate(inputs):
        for axis, coefficient in enumerate(xi):
            if not coefficient or axis in basis:
                continue
            position = sum(entry < axis for entry in basis)
            target = tuple(sorted((axis,) + basis))
            matrix[outputs.index(target)][c] = ((-1) ** position) * coefficient
    return outputs, matrix


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


certificate = json.loads(CERTIFICATE.read_text())
register = REGISTER.read_text()
assert "polarity: ASSERTS" in register[register.index("- id: SC-ACT-06") : register.index("- id: SC-FER-01")]

n = 14
xi = (2, 0, -3, 5, 0, 7, 0, 0, 11, 0, 0, 13, 0, 17)
_, gauge = exterior_symbol(n, 0, xi)
pairs, euler = exterior_symbol(n, 1, xi)
_, redundancy = exterior_symbol(n, 2, xi)
ranks = [modular_rank(gauge), modular_rank(euler), modular_rank(redundancy)]
assert ranks == [1, 13, 78]
assert not any(any(value for value in row) for row in multiply(euler, gauge))
assert not any(any(value for value in row) for row in multiply(redundancy, euler))

axis = (1,) + (0,) * 13
pairs_axis, euler_axis = exterior_symbol(n, 1, axis)
rows = [euler_axis[i] for i, pair in enumerate(pairs_axis) if 0 in pair]
assert len(rows) == 13 and modular_rank(rows) == 13
short = rows[1:]
assert len(short) == 12 and modular_rank(short) == 12
assert n - modular_rank(short) - 1 == 1

# Hostile controls: the zero covector is not an ellipticity test; deleting one
# transverse row creates cohomology; the Lorentzian defect route is excluded;
# and the source status is not silently promoted.
_, zero_gauge = exterior_symbol(n, 0, (0,) * n)
assert modular_rank(zero_gauge) == 0
assert certificate["exact_symbol_attempt"]["reduced_short_middle_cohomology"] == 1
assert certificate["lorentzian_k77_defects_used"] is False
assert certificate["source_status_changes"] == "NONE"
assert certificate["missing_source_datum"]["row_projector_required"] is True
assert certificate["missing_source_datum"]["full_euclidean_linearization_required"] is True

print("[PASS] K276 independent reverse-basis replay 8/8 exact, 4/4 hostile")

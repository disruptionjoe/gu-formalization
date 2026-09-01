#!/usr/bin/env python3
"""Exact certificate for the K84 local-frame factorization boundary."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k84-local-frame-factorization-universal-coupling-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k84-local-frame-factorization-universal-coupling-wave-2026-09-01.md"
)

Matrix3 = tuple[tuple[Fraction, Fraction, Fraction], ...]
Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
ETA: Matrix3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(-1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(-1)),
)
ROT12: Matrix3 = (
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(-1)),
    (Fraction(0), Fraction(1), Fraction(0)),
)
BOOST01: Matrix3 = (
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0)),
)
BOOST02: Matrix3 = (
    (Fraction(0), Fraction(0), Fraction(1)),
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0)),
)
U_OUTER: Matrix3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0)),
)
I2: Matrix2 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
J2: Matrix2 = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(3)))


def transpose(matrix: Matrix3) -> Matrix3:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def multiply(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def add(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(3)) for i in range(3)
    )


def residual(generator: Matrix3, coefficient: Matrix3) -> Matrix3:
    return add(multiply(generator, coefficient), multiply(coefficient, transpose(generator)))


def zero3() -> Matrix3:
    return tuple(tuple(Fraction(0) for _ in range(3)) for _ in range(3))


def symmetric_from_coordinates(values: tuple[Fraction, ...]) -> Matrix3:
    c00, c11, c22, c01, c02, c12 = values
    return ((c00, c01, c02), (c01, c11, c12), (c02, c12, c22))


def invariant_system() -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    for generator in (ROT12, BOOST01, BOOST02):
        basis_residuals = []
        for column in range(6):
            coordinates = tuple(Fraction(int(i == column)) for i in range(6))
            basis_residuals.append(residual(generator, symmetric_from_coordinates(coordinates)))
        for i in range(3):
            for j in range(3):
                rows.append([basis_residuals[column][i][j] for column in range(6)])
    return rows


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    work[row][c] - factor * work[pivot_row][c]
                    for c in range(len(work[row]))
                ]
        pivot_row += 1
    return pivot_row


def block_scale(spacetime: Matrix3, internal: Matrix2) -> tuple[tuple[Matrix2, ...], ...]:
    return tuple(
        tuple(
            tuple(tuple(spacetime[a][b] * internal[i][j] for j in range(2)) for i in range(2))
            for b in range(3)
        )
        for a in range(3)
    )


def matrix2_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(tuple(left[i][j] + right[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def quadratic(vector: tuple[Fraction, Fraction], form: Matrix2) -> Fraction:
    return sum(vector[i] * form[i][j] * vector[j] for i in range(2) for j in range(2))


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    factor = manifest["frame_factorization"]
    spurion = manifest["spurion_boundary"]
    system = invariant_system()
    h: Matrix2 = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(3)))
    temporal = matrix2_add(I2, J2)
    eta_blocks = block_scale(ETA, h)
    eta_coordinates = (Fraction(1), Fraction(-1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0))
    return [
        ("Lorentz invariant system has rank five", rank(system) == 5),
        ("Lorentz invariant symmetric tensor space is one dimensional", 6 - rank(system) == 1),
        ("metric line solves spatial rotation", residual(ROT12, ETA) == zero3()),
        ("metric line solves first boost", residual(BOOST01, ETA) == zero3()),
        ("metric line solves second boost", residual(BOOST02, ETA) == zero3()),
        ("metric coordinate vector solves the full system", all(sum(row[i] * eta_coordinates[i] for i in range(6)) == 0 for row in system)),
        ("internal factorization keeps one spacetime metric", eta_blocks[0][0] == h and eta_blocks[1][1] == tuple(tuple(-x for x in row) for row in h)),
        ("preferred vector retains spatial rotation", residual(ROT12, U_OUTER) == zero3()),
        ("preferred vector breaks first boost", residual(BOOST01, U_OUTER) != zero3()),
        ("preferred vector breaks second boost", residual(BOOST02, U_OUTER) != zero3()),
        ("spurion temporal form is positive on first mode", quadratic((1, 0), temporal) == 1),
        ("spurion temporal form is positive on second mode", quadratic((0, 1), temporal) == 4),
        ("spurion spatial form is positive", quadratic((2, -3), I2) == 13),
        ("first squared speed is one", I2[0][0] / temporal[0][0] == 1),
        ("second squared speed is one quarter", I2[1][1] / temporal[1][1] == Fraction(1, 4)),
        ("manifest records invariance equation", "X*C+C*X^T=0" in factor["invariance_equation"]),
        ("manifest records one-dimensional metric line", "dimension one" in factor["exact_nullspace"] and "diag(1,-1,-1)" in factor["exact_nullspace"]),
        ("manifest records internal factorization", "eta^{ab}*H" in factor["internal_extension"]),
        ("manifest records universal cone", "same unit eta-null" in factor["universal_cone"]),
        ("manifest separates coframe Euler owner", "dynamical coframe Euler" in factor["ward_owner"]),
        ("manifest records preferred vector family", "u^a*u^b*J" in spurion["preferred_vector_family"]),
        ("manifest records two-speed control", "1 and 1/4" in spurion["two_speed_control"]),
        ("manifest records residual stabilizer", "spatial rotation" in spurion["residual_symmetry"]),
        ("manifest records covariance nonselection", "do not exclude" in spurion["nonselection"]),
        ("manifest preserves source custody", "own no coefficient-complete" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no source full-carrier action" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states factorization", "C^{ab}_{AB} = eta^{ab} H_{AB}" in text),
        ("artifact states preferred-vector control", "C^{ab} = eta^{ab} H + u^a u^b J" in text),
        ("artifact states two speeds", "1 and 1/4" in text),
        ("artifact disclaims source theorem", "not a source-owned GU coframe or stress-tensor theorem" in text),
    ]


def mutate(manifest: dict, path: tuple[str, ...], value: object) -> dict:
    mutant = deepcopy(manifest)
    cursor = mutant
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    return mutant


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    text = ARTIFACT.read_text(encoding="utf-8")
    checks = evaluate(manifest, text)
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}|{name}")
    if any(not ok for _, ok in checks):
        return 1
    print(f"SUMMARY|checks_passed={len(checks)}|checks_total={len(checks)}")
    if "--selftest" not in sys.argv:
        return 0

    baseline = {name for name, ok in checks if ok}
    tokens = [
        "GU-COMPARATOR-ROUTING",
        "```gu-typed-objects",
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`",
        "C^{ab}_{AB} = eta^{ab} H_{AB}",
        "C^{ab} = eta^{ab} H + u^a u^b J",
        "1 and 1/4",
        "not a source-owned GU coframe or stress-tensor theorem",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("frame_factorization", "invariance_equation"), "none"),
        (("frame_factorization", "exact_nullspace"), "dimension six"),
        (("frame_factorization", "internal_extension"), "arbitrary C"),
        (("frame_factorization", "universal_cone"), "many cones"),
        (("frame_factorization", "ward_owner"), "coframe already dynamical"),
        (("spurion_boundary", "preferred_vector_family"), "none"),
        (("spurion_boundary", "two_speed_control"), "one speed"),
        (("spurion_boundary", "residual_symmetry"), "full Lorentz"),
        (("spurion_boundary", "nonselection"), "covariance selects"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "GU nonlinear gravity theorem"),
    ]
    for path, value in mutations:
        mutant_pass = {name for name, ok in evaluate(mutate(manifest, path, value), text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|mutate {'.'.join(path)}")
        caught += int(detected)

    total = len(tokens) + len(mutations)
    print(f"SUMMARY|hostile_caught={caught}|hostile_total={total}")
    return 0 if caught == total else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Exact certificate for the K84 BRST star-state descent boundary."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k84-brst-star-state-descent-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/k84-brst-star-state-descent-wave-2026-09-01.md"
)


@dataclass(frozen=True)
class QSqrt2:
    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __add__(self, other: object) -> "QSqrt2":
        value = coerce(other)
        return QSqrt2(self.rational + value.rational, self.radical + value.radical)

    __radd__ = __add__

    def __neg__(self) -> "QSqrt2":
        return QSqrt2(-self.rational, -self.radical)

    def __sub__(self, other: object) -> "QSqrt2":
        return self + (-coerce(other))

    def __rsub__(self, other: object) -> "QSqrt2":
        return coerce(other) - self

    def __mul__(self, other: object) -> "QSqrt2":
        value = coerce(other)
        return QSqrt2(
            self.rational * value.rational + 2 * self.radical * value.radical,
            self.rational * value.radical + self.radical * value.rational,
        )

    __rmul__ = __mul__


def coerce(value: object) -> QSqrt2:
    if isinstance(value, QSqrt2):
        return value
    return QSqrt2(Fraction(value))  # type: ignore[arg-type]


Q = QSqrt2
ZERO = Q()
ONE = Q(Fraction(1))
HALF = Q(Fraction(1, 2))
SQRT2 = Q(Fraction(0), Fraction(1))
INV_SQRT2 = Q(Fraction(0), Fraction(1, 2))
Matrix = tuple[tuple[QSqrt2, ...], ...]
Vector = tuple[QSqrt2, ...]
Layer = tuple[Matrix, Matrix]


def matrix(values: list[list[object]]) -> Matrix:
    return tuple(tuple(coerce(value) for value in row) for row in values)


def zeros(size: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(size)) for _ in range(size))


def identity(size: int) -> Matrix:
    return tuple(tuple(ONE if i == j else ZERO for j in range(size)) for i in range(size))


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left))) for i in range(len(left)))


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] - right[i][j] for j in range(len(left))) for i in range(len(left)))


def scale(value: object, source: Matrix) -> Matrix:
    scalar = coerce(value)
    return tuple(tuple(scalar * entry for entry in row) for row in source)


def multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(size)), ZERO) for j in range(size))
        for i in range(size)
    )


def transpose(source: Matrix) -> Matrix:
    return tuple(tuple(source[j][i] for j in range(len(source))) for i in range(len(source)))


def tensor(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i // len(right)][j // len(right)] * right[i % len(right)][j % len(right)] for j in range(len(left) * len(right)))
        for i in range(len(left) * len(right))
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return subtract(multiply(left, right), multiply(right, left))


def matvec(source: Matrix, vector: Vector) -> Vector:
    return tuple(sum((source[i][j] * vector[j] for j in range(len(vector))), ZERO) for i in range(len(vector)))


def inner(left: Vector, right: Vector) -> QSqrt2:
    return sum((left[i] * right[i] for i in range(len(left))), ZERO)


I2 = identity(2)
I4 = identity(4)
Z2 = zeros(2)
Z4 = zeros(4)
PAULI_X = matrix([[0, 1], [1, 0]])
PAULI_Z = matrix([[1, 0], [0, -1]])
A0 = tensor(PAULI_Z, I2)
A1 = tensor(PAULI_X, I2)
B0 = tensor(I2, scale(INV_SQRT2, add(PAULI_Z, PAULI_X)))
B1 = tensor(I2, scale(INV_SQRT2, subtract(PAULI_Z, PAULI_X)))
BELL: Vector = (INV_SQRT2, ZERO, ZERO, INV_SQRT2)
E0: Vector = (ONE, ZERO, ZERO, ZERO)


def layer_product(left: Layer, right: Layer) -> Layer:
    return multiply(left[0], right[0]), multiply(left[1], right[1])


def layer_star(value: Layer) -> Layer:
    return transpose(value[0]), transpose(value[1])


def boundary(value: Matrix) -> Layer:
    return Z4, value


def quotient(value: Layer) -> Matrix:
    return value[0]


def vector_state(vector: Vector, observable: Matrix) -> QSqrt2:
    return inner(vector, matvec(observable, vector))


def omega_good(value: Layer) -> QSqrt2:
    return vector_state(BELL, value[0])


def omega_bad(value: Layer) -> QSqrt2:
    return HALF * vector_state(BELL, value[0]) + HALF * vector_state(E0, value[1])


def is_nonnegative_rational(value: QSqrt2) -> bool:
    return value.radical == 0 and value.rational >= 0


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    descent = manifest["cohomology_descent"]
    control = manifest["finite_control"]
    sample = matrix([[1, 2, 0, -1], [0, 1, 3, 0], [2, 0, -1, 1], [1, 1, 0, 2]])
    sample2 = matrix([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]])
    unit: Layer = (I4, I4)
    exact = boundary(sample)
    cycle = (sample2, transpose(sample2))
    product_left = layer_product(cycle, exact)
    product_right = layer_product(exact, cycle)
    lift_a0: Layer = (A0, tensor(PAULI_X, I2))
    lift_a1: Layer = (A1, Z4)
    lift_b0: Layer = (B0, tensor(PAULI_Z, I2))
    lift_b1: Layer = (B1, Z4)
    chsh = add(multiply(A0, add(B0, B1)), multiply(A1, subtract(B0, B1)))
    x = subtract(A0, scale(INV_SQRT2, add(B0, B1)))
    y = subtract(A1, scale(INV_SQRT2, subtract(B0, B1)))
    sos_left = subtract(scale(2 * SQRT2, I4), chsh)
    sos_right = scale(INV_SQRT2, add(multiply(x, x), multiply(y, y)))
    lifted_cross_commutator = (
        commutator(lift_a0[0], lift_b0[0]),
        commutator(lift_a0[1], lift_b0[1]),
    )
    positive_sample = layer_product(layer_star((sample, sample2)), (sample, sample2))
    return [
        ("boundary ideal is closed under left multiplication", quotient(product_left) == Z4),
        ("boundary ideal is closed under right multiplication", quotient(product_right) == Z4),
        ("boundary ideal is star closed", quotient(layer_star(exact)) == Z4),
        ("quotient product is representative independent", quotient(layer_product(cycle, exact)) == multiply(quotient(cycle), quotient(exact))),
        ("good state is normalized", omega_good(unit) == ONE),
        ("good state annihilates boundaries", omega_good(exact) == ZERO),
        ("good state is positive on sampled square", is_nonnegative_rational(omega_good(positive_sample))),
        ("bad state is normalized", omega_bad(unit) == ONE),
        ("bad state does not annihilate unit boundary", omega_bad(boundary(I4)) == HALF),
        ("equivalent representatives disagree under bad state", omega_bad((I4, Z4)) != omega_bad(unit)),
        ("Alice zero is involutive in quotient", multiply(quotient(lift_a0), quotient(lift_a0)) == I4),
        ("Alice one is involutive in quotient", multiply(quotient(lift_a1), quotient(lift_a1)) == I4),
        ("Bob zero is involutive in quotient", multiply(quotient(lift_b0), quotient(lift_b0)) == I4),
        ("Bob one is involutive in quotient", multiply(quotient(lift_b1), quotient(lift_b1)) == I4),
        ("cross commutator is exact", quotient(lifted_cross_commutator) == Z4),
        ("chosen representatives need not literally commute", lifted_cross_commutator[1] != Z4),
        ("CHSH SOS identity holds in quotient", sos_left == sos_right),
        ("Bell quotient state saturates CHSH", omega_good((chsh, Z4)) == 2 * SQRT2),
        ("both SOS defects are state null", omega_good((multiply(x, x), Z4)) == ZERO and omega_good((multiply(y, y), Z4)) == ZERO),
        ("manifest records boundary ideal theorem", "two-sided ideal" in descent["ideal_theorem"] and "star ideal" in descent["ideal_theorem"]),
        ("manifest records observable quotient", "H0_Q=Z0/B0" in descent["observable_algebra"]),
        ("manifest records state iff", "iff omega annihilates" in descent["state_iff"]),
        ("manifest records modulo-exact local relations", "modulo B0" in descent["local_relations"]),
        ("manifest records SOS descent", "well-defined and positive" in descent["sos_descent"]),
        ("manifest records finite cycle algebra", "M4(R) direct_sum M4(R)" in control["cycle_algebra"]),
        ("manifest records boundary summand", "0 direct_sum M4(R)" in control["boundary_ideal"]),
        ("manifest records finite differential", "Q is the identity inclusion" in control["differential"] and "graded Leibniz" in control["differential"]),
        ("manifest records Bell saturation", "2*sqrt(2)" in control["positive_state"]),
        ("manifest records non-descent control", "cannot descend" in control["non_descent_control"]),
        ("manifest preserves source custody", "own no complete physical BRST or BFV" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no GU-native physical cohomology" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states cohomology quotient", "H0_Q = Z0 / B0" in text),
        ("artifact states state annihilation condition", "omega(B0) = 0" in text),
        ("artifact states exact commutation suffices", "Exact commutation is sufficient" in text),
        ("artifact disclaims GU state", "not a GU-native physical observable algebra, positive state or Born" in text),
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
        "H0_Q = Z0 / B0",
        "omega(B0) = 0",
        "Exact commutation is sufficient",
        "not a GU-native physical observable algebra, positive state or Born",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("cohomology_descent", "ideal_theorem"), "boundaries are only a subspace"),
        (("cohomology_descent", "observable_algebra"), "no quotient"),
        (("cohomology_descent", "state_iff"), "every state descends"),
        (("cohomology_descent", "local_relations"), "literal relations only"),
        (("cohomology_descent", "sos_descent"), "not positive"),
        (("finite_control", "cycle_algebra"), "R"),
        (("finite_control", "boundary_ideal"), "none"),
        (("finite_control", "differential"), "no differential supplied"),
        (("finite_control", "positive_state"), "classical bound"),
        (("finite_control", "non_descent_control"), "all states descend"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "GU Born theorem"),
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

#!/usr/bin/env python3
"""Exact hostile probe for the quantum-anchor reverse-scaffold interface."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from dataclasses import dataclass
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/quantum-anchor-reverse-scaffold-interface-wave.json"


@dataclass(frozen=True)
class Q2:
    """Exact a + b sqrt(2), with rational a and b."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Q2":
        rhs = as_q2(other)
        return Q2(self.a + rhs.a, self.b + rhs.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: object) -> "Q2":
        return self + (-as_q2(other))

    def __rsub__(self, other: object) -> "Q2":
        return as_q2(other) - self

    def __mul__(self, other: object) -> "Q2":
        rhs = as_q2(other)
        return Q2(
            self.a * rhs.a + 2 * self.b * rhs.b,
            self.a * rhs.b + self.b * rhs.a,
        )

    __rmul__ = __mul__


def as_q2(value: object) -> Q2:
    if isinstance(value, Q2):
        return value
    if isinstance(value, Fraction):
        return Q2(value)
    if isinstance(value, int):
        return Q2(Fraction(value))
    raise TypeError(value)


ZERO = Q2()
ONE = Q2(Fraction(1))
HALF = Q2(Fraction(1, 2))
INV_SQRT2 = Q2(Fraction(0), Fraction(1, 2))


def matrix(rows: list[list[object]]) -> list[list[Q2]]:
    return [[as_q2(value) for value in row] for row in rows]


def madd(left: list[list[Q2]], right: list[list[Q2]]) -> list[list[Q2]]:
    return [[a + b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def mscale(scale: object, value: list[list[Q2]]) -> list[list[Q2]]:
    return [[as_q2(scale) * item for item in row] for row in value]


def mmul(left: list[list[Q2]], right: list[list[Q2]]) -> list[list[Q2]]:
    cols = list(zip(*right))
    return [[sum((x * y for x, y in zip(row, col)), ZERO) for col in cols] for row in left]


def trace(value: list[list[Q2]]) -> Q2:
    return sum((value[i][i] for i in range(len(value))), ZERO)


def kron(left: list[list[Q2]], right: list[list[Q2]]) -> list[list[Q2]]:
    return [
        [left[i][j] * right[k][ell] for j in range(len(left[0])) for ell in range(len(right[0]))]
        for i in range(len(left))
        for k in range(len(right))
    ]


def event_probability(state: list[list[Q2]], effect: list[list[Q2]]) -> Q2:
    return trace(mmul(state, effect))


def partial_trace_alice(state: list[list[Q2]]) -> list[list[Q2]]:
    return [
        [sum((state[2 * a + b][2 * a + c] for a in range(2)), ZERO) for c in range(2)]
        for b in range(2)
    ]


I2 = matrix([[1, 0], [0, 1]])
X = matrix([[0, 1], [1, 0]])
Z = matrix([[1, 0], [0, -1]])
P0 = matrix([[1, 0], [0, 0]])
RHO_PLUS = matrix([[Fraction(1, 2), Fraction(1, 2)], [Fraction(1, 2), Fraction(1, 2)]])
RHO_MINUS = matrix([[Fraction(1, 2), Fraction(-1, 2)], [Fraction(-1, 2), Fraction(1, 2)]])
RHO_MIX = matrix([[Fraction(1, 2), 0], [0, Fraction(1, 2)]])
BELL = matrix([
    [Fraction(1, 2), 0, 0, Fraction(1, 2)],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [Fraction(1, 2), 0, 0, Fraction(1, 2)],
])


def dephase(state: list[list[Q2]], eta: Fraction) -> list[list[Q2]]:
    return [[state[0][0], eta * state[0][1]], [eta * state[1][0], state[1][1]]]


def local_dephase_alice(state: list[list[Q2]]) -> list[list[Q2]]:
    zi = kron(Z, I2)
    return mscale(HALF, madd(state, mmul(mmul(zi, state), zi)))


def local_hidden_chsh_bound() -> int:
    scores = []
    for a0, a1, b0, b1 in itertools.product((-1, 1), repeat=4):
        scores.append(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1)
    return max(abs(score) for score in scores)


def quantum_chsh(state: list[list[Q2]]) -> Q2:
    b0 = mscale(INV_SQRT2, madd(Z, X))
    b1 = mscale(INV_SQRT2, madd(Z, mscale(-1, X)))
    operator = madd(
        madd(kron(Z, b0), kron(Z, b1)),
        madd(kron(X, b0), mscale(-1, kron(X, b1))),
    )
    return event_probability(state, operator)


def q2_square(value: Q2) -> Q2:
    return value * value


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    coherent_plus = RHO_MIX if mutation == "erase_coherence" else RHO_PLUS
    bell = kron(P0, P0) if mutation == "factorize_bell" else BELL
    remote_after = partial_trace_alice(local_dephase_alice(BELL))
    if mutation == "signal_remote":
        remote_after = P0
    eta = Fraction(3, 2) if mutation == "amplify_decoherence" else Fraction(1, 3)

    checks: list[tuple[str, bool]] = []
    # Same-machinery controls run before foreground assertions.
    checks.append(("matrix identity control", mmul(I2, X) == X == mmul(X, I2)))
    checks.append(("state normalization control", trace(RHO_PLUS) == ONE and trace(BELL) == ONE))
    checks.append(("projector control", mmul(RHO_PLUS, RHO_PLUS) == RHO_PLUS))
    checks.append(("composition normalization control", trace(kron(RHO_PLUS, P0)) == ONE))

    checks.append(("phase plus recombines with unit probability", event_probability(coherent_plus, RHO_PLUS) == ONE))
    checks.append(("phase minus is orthogonal at recombination", event_probability(RHO_MINUS, RHO_PLUS) == ZERO))
    checks.append(("classical mixture loses phase discrimination", event_probability(RHO_MIX, RHO_PLUS) == HALF))
    decohered = dephase(RHO_PLUS, eta)
    expected_plus = Q2(Fraction(1, 2) + eta / 2)
    expected_minus = Q2(Fraction(1, 2) - eta / 2)
    checks.append(("dephasing preserves normalization", trace(decohered) == ONE))
    checks.append(("dephasing transfers eta to fringe visibility",
                   event_probability(decohered, RHO_PLUS) == expected_plus
                   and event_probability(decohered, RHO_MINUS) == expected_minus))
    checks.append(("dephasing parameter remains physical", Fraction(0) <= eta <= Fraction(1)))

    checks.append(("local hidden-variable CHSH ceiling is exact", local_hidden_chsh_bound() == 2))
    chsh = quantum_chsh(bell)
    checks.append(("Bell witness is exact 2 sqrt(2)", chsh == Q2(Fraction(0), Fraction(2))))
    checks.append(("Bell witness exceeds the local ceiling", q2_square(chsh) == Q2(Fraction(8))))
    checks.append(("nonselective local intervention preserves remote marginal",
                   remote_after == matrix([[Fraction(1, 2), 0], [0, Fraction(1, 2)]])))
    checks.append(("local intervention changes the joint correlation carrier",
                   local_dephase_alice(BELL) != BELL))
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    anchors = data.get("calibration_anchors", [])
    if len(anchors) != 2 or any(anchor.get("confirmation_credit") != "none" for anchor in anchors):
        failures.append("calibration_credit")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False:
        failures.append("holdout_firewall")
    r2_ids = {row.get("id") for row in data.get("r2_causal_dynamical_demands", [])}
    if "QD-R2-4" not in r2_ids:
        failures.append("instrument_no_signalling")
    r1 = data.get("r1_candidate_action_requirements", {})
    if r1.get("candidate_selected") is not False:
        failures.append("action_selection")
    if any(not row.get("lineage") for row in r1.get("requirements", [])):
        failures.append("demand_lineage")
    imports = {row.get("id"): row.get("classification") for row in data.get("import_accounting", [])}
    if len(imports) != 10 or any("imported" not in value and "assumed" not in value for value in imports.values()):
        failures.append("import_accounting")
    if "GU-native" not in data.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = []
    for name, update in (
        ("direction", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("calibration_credit", lambda d: d["calibration_anchors"][0].__setitem__("confirmation_credit", "prediction")),
        ("holdout_scoring", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
        ("no_signalling", lambda d: d.__setitem__("r2_causal_dynamical_demands", [row for row in d["r2_causal_dynamical_demands"] if row["id"] != "QD-R2-4"])),
        ("action_selection", lambda d: d["r1_candidate_action_requirements"].__setitem__("candidate_selected", True)),
        ("import_credit", lambda d: d["import_accounting"][0].__setitem__("classification", "forced_by_GU")),
    ):
        mutated = copy.deepcopy(data)
        update(mutated)
        mutations.append((name, bool(manifest_failures(mutated))))

    for name in ("erase_coherence", "factorize_bell", "signal_remote", "amplify_decoherence"):
        mutations.append((name, any(not passed for _, passed in model_checks(name))))

    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(caught for _, caught in mutations)}/{len(mutations)} caught")
    return 0 if all(caught for _, caught in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    failures = manifest_failures(data)
    checks.append(("manifest direction, firewall, lineage, imports and ceiling", not failures))
    failed = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failed += int(not passed)
    print(f"QUANTUM ANCHOR REVERSE SCAFFOLD: {len(checks) - failed}/{len(checks)} pass")
    if failures:
        print("manifest failures:", ", ".join(failures))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

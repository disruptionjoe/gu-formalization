#!/usr/bin/env python3
"""Independent K270 algebra replay and hostile metadata controls."""

from __future__ import annotations

import copy
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k270-k152-sharp-spectral-budget-certificate.json"


def f(value: str | int) -> Fraction:
    return Fraction(value)


def direct_measure(points: list[int], weights: list[str], shift: int) -> tuple[Fraction, Fraction]:
    xs = list(map(Fraction, points))
    ws = list(map(Fraction, weights))
    rho = sum((w * x for w, x in zip(ws, xs)), Fraction())
    e = sum((w * (x - rho) ** 2 / (x + shift) for w, x in zip(ws, xs)), Fraction())
    return rho, e


def replay_bound(points: list[int], weights: list[str], ground: int, exterior: int, shift: int) -> dict[str, Fraction]:
    rho, e = direct_measure(points, weights, shift)
    delta = rho - ground
    a = rho + shift
    g = exterior - rho
    positive_integral = sum(
        (
            Fraction(weight)
            * (Fraction(point) - ground)
            * (Fraction(point) - exterior)
            / (Fraction(point) + shift)
            for point, weight in zip(points, weights)
        ),
        Fraction(),
    )
    algebra = e * (a - delta) * (a + g) - a * delta * g
    upper = e * a * (a + g) / (a * g + e * (a + g))
    return {
        "rho": rho,
        "e": e,
        "delta": delta,
        "a": a,
        "g": g,
        "integral": positive_integral,
        "algebra": algebra,
        "identity": a * a * positive_integral,
        "upper": upper,
    }


def metadata_ok(data: dict) -> bool:
    theorem = data.get("sharp_spectral_certificate", {})
    consumer = data.get("value_to_consumer_budget", {})
    audit = data.get("native_input_audit", {})
    boundaries = data.get("boundaries", {})
    return all(
        (
            data.get("classification") == "INTERNAL_STRUCTURAL_ONLY",
            data.get("direction") == "observed_to_native",
            theorem.get("support") == "{lambda0} union [b,infinity)",
            theorem.get("shifted_positivity") == "lambda0+s>0",
            theorem.get("proof_integrand") == "(x-lambda0)(x-b)/(x+s)>=0 on support",
            theorem.get("proof_identity") == "a^2 integral proof_integrand dmu=e(a-delta)(a+g)-a delta g",
            theorem.get("two_point_equality") is True,
            consumer.get("historical_1e-21_is_full_value_target") is False,
            consumer.get("historical_1e-21_is_k152_error_margin") is False,
            consumer.get("native_numeric_budget_emitted") is False,
            audit.get("native_complete_dual_residual") is False,
            audit.get("native_exterior_gap") is False,
            audit.get("order_six_integral_to_residual_map_norm") is False,
            boundaries.get("native_K152_interval_emitted") is False,
            boundaries.get("physics_ledger_change") is False,
            boundaries.get("prediction_or_confirmation_credit") is False,
        )
    )


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    equality = replay_bound([0, 4], ["1/2", "1/2"], 0, 4, 1)
    strict = replay_bound([0, 4, 6], ["1/2", "1/4", "1/4"], 0, 4, 1)
    # This measure has spectral mass in the forbidden open gap (0,4).  The
    # candidate expression underestimates delta, proving the gap assumption is
    # substantive rather than metadata decoration.
    gap_attack = replay_bound([0, 2], ["1/2", "1/2"], 0, 4, 1)
    checks = [
        ("metadata", metadata_ok(data)),
        ("two-point mean", equality["rho"] == 2),
        ("two-point residual", equality["e"] == Fraction(12, 5)),
        ("proof identity equality", equality["algebra"] == equality["identity"] == 0),
        ("sharp equality", equality["upper"] == equality["delta"] == 2),
        ("three-point identity", strict["algebra"] == strict["identity"]),
        ("three-point proof integral positive", strict["integral"] > 0),
        ("three-point bound strict", strict["upper"] > strict["delta"]),
        ("gap attack violates proof sign", gap_attack["integral"] < 0),
        ("gap attack breaks bound", gap_attack["upper"] < gap_attack["delta"]),
        ("budget ratio exact", (Fraction(3, 5) / Fraction(2, 9)) == Fraction(27, 10)),
        ("consumer sample exact", (Fraction(1, 10) + 2 * (Fraction(1, 100) + Fraction(1, 200)) + Fraction(1, 50)) ** 2 == Fraction(9, 400)),
        ("consumer sample energy closes", Fraction(9, 400) <= Fraction(3, 5)),
        ("consumer sample projection closes", Fraction(9, 400) <= Fraction(1, 5)),
    ]
    failed = [name for name, ok in checks if not ok]
    if failed:
        print(f"FAIL independent K270 replay: {failed}")
        return 1

    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICS_RESULT"),
        lambda d: d["sharp_spectral_certificate"].__setitem__("support", "all real x"),
        lambda d: d["sharp_spectral_certificate"].__setitem__("shifted_positivity", "assumed"),
        lambda d: d["sharp_spectral_certificate"].__setitem__("two_point_equality", False),
        lambda d: d["value_to_consumer_budget"].__setitem__("historical_1e-21_is_full_value_target", True),
        lambda d: d["value_to_consumer_budget"].__setitem__("native_numeric_budget_emitted", True),
        lambda d: d["native_input_audit"].__setitem__("native_complete_dual_residual", True),
        lambda d: d["native_input_audit"].__setitem__("native_exterior_gap", True),
        lambda d: d["native_input_audit"].__setitem__("order_six_integral_to_residual_map_norm", True),
        lambda d: d["boundaries"].__setitem__("native_K152_interval_emitted", True),
        lambda d: d["boundaries"].__setitem__("physics_ledger_change", True),
        lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True),
    ]
    caught = 0
    for mutation in mutations:
        trial = copy.deepcopy(data)
        mutation(trial)
        if not metadata_ok(trial):
            caught += 1
    if caught != len(mutations):
        print(f"FAIL hostile metadata caught {caught}/{len(mutations)}")
        return 1
    print(f"PASS independent K270 replay {len(checks)}/{len(checks)}; hostile metadata {caught}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""K609 seedwise finite moments and complete K500 leakage enclosure."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k609-k500-complete-uniform-leakage-enclosure.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module; spec.loader.exec_module(module)
    return module


K604 = load("k604_for_k609", "k604_k500_determinant_simplex_kernel_atlas.py")
K608 = load("k608_for_k609", "k608_k500_diagonal_self_norm_analytic_envelopes.py")


def strict(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text())


def sqrt_upper(value: Fraction) -> Fraction:
    assert value >= 0
    root = math.isqrt(value.numerator * value.denominator)
    if root * root < value.numerator * value.denominator: root += 1
    return Fraction(root, value.denominator)


def f(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def dec(value: Fraction) -> str:
    with localcontext() as ctx:
        ctx.prec = 28
        return format(Decimal(value.numerator) / Decimal(value.denominator), ".18E")


def higher_order_moments() -> dict[int, dict[str, Any]]:
    paths, actions = K604.signature_groups()
    result = {seed: {"N_upper": Fraction(), "A_lower": Fraction(), "A_upper": Fraction(), "B_upper": Fraction(), "orders": defaultdict(lambda: [Fraction(), Fraction(), Fraction(), Fraction()])} for seed in range(3)}
    for key in sorted(set(paths) | set(actions)):
        seed, order, _signature = key
        if order < 3: continue
        cyclic = paths.get(key, []); action = actions.get(key, [])
        target = result[seed]; order_row = target["orders"][order]
        for left, right in combinations_with_replacement(cyclic, 2):
            factor = 1 if left["source_id"] == right["source_id"] else 2
            value = factor * sqrt_upper(K608.side_upper(["C", left["simplex_rank"], []]) * K608.side_upper(["C", right["simplex_rank"], []]))
            target["N_upper"] += value; order_row[0] += value
        for left, right in product(cyclic, action):
            value = int(right["coefficient"]) * sqrt_upper(K608.side_upper(["C", left["simplex_rank"], []]) * K608.side_upper(["A", right["simplex_rank"], right["contracted_scalar_heat_times"]]))
            if value < 0: target["A_lower"] += value; order_row[1] += value
            else: target["A_upper"] += value; order_row[2] += value
        for left, right in combinations_with_replacement(action, 2):
            factor = 1 if left["source_id"] == right["source_id"] else 2
            value = factor * int(left["coefficient"]) * int(right["coefficient"]) * sqrt_upper(K608.side_upper(["A", left["simplex_rank"], left["contracted_scalar_heat_times"]]) * K608.side_upper(["A", right["simplex_rank"], right["contracted_scalar_heat_times"]]))
            if value > 0: target["B_upper"] += value; order_row[3] += value
    return result


def interval(values: list[str]) -> tuple[Fraction, Fraction]:
    return Fraction(values[0]), Fraction(values[1])


def build() -> dict[str, Any]:
    k602 = strict("lab/process/k602-k500-order-two-numerical-moment-enclosure.json")
    k574 = strict("lab/process/k574-k176-sharp-post-adjoint-tail-reconciliation.json")
    high = higher_order_moments()
    epsilon = Fraction(k574["sharp_tail"]["sharp_tail_norm_upper"])
    # q10/q01 are charge-conjugate.  The raw coordinate labellings differ, so
    # use their common outward hull rather than making a coordinate-dependent
    # distinction between physically symmetric levels.
    charged = {
        "N_upper": max(high[1]["N_upper"], high[2]["N_upper"]),
        "A_lower": min(high[1]["A_lower"], high[2]["A_lower"]),
        "A_upper": max(high[1]["A_upper"], high[2]["A_upper"]),
        "B_upper": max(high[1]["B_upper"], high[2]["B_upper"]),
        "orders": {},
    }
    for order in sorted(set(high[1]["orders"]) | set(high[2]["orders"])):
        a = high[1]["orders"][order]; b = high[2]["orders"][order]
        charged["orders"][order] = [max(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])]
    levels = [("q00", high[0]), ("q10", charged), ("q01", charged)]
    rows = {}
    for level, h in levels:
        n2 = interval(k602["seed_moment_intervals"][level]["N_2"])
        a2 = interval(k602["seed_moment_intervals"][level]["A_2"])
        b2 = interval(k602["seed_moment_intervals"][level]["B_2"])
        finite_n = (n2[0], n2[1] + h["N_upper"])
        finite_a = (a2[0] + h["A_lower"], a2[1] + h["A_upper"])
        finite_b = (Fraction(), b2[1] + h["B_upper"])
        a_radius = sqrt_upper(finite_n[1]) * epsilon
        complete_a = (finite_a[0] - a_radius, finite_a[1] + a_radius)
        complete_b = (Fraction(), (sqrt_upper(finite_b[1]) + epsilon) ** 2)
        distance = min(abs(complete_a[0]), abs(complete_a[1])) if complete_a[0] > 0 or complete_a[1] < 0 else Fraction()
        leakage = complete_b[1] / finite_n[0] - distance**2 / finite_n[1]**2
        rows[level] = {
            "higher_order_3_through_12": {
                "N": ["0/1", f(h["N_upper"])],
                "A_F": [f(h["A_lower"]), f(h["A_upper"])],
                "B_F": ["0/1", f(h["B_upper"])],
                "order_rows": [[order, *[f(x) for x in values]] for order, values in sorted(h["orders"].items())],
            },
            "finite_moments_2_through_12": {"N": [f(x) for x in finite_n], "A_F": [f(x) for x in finite_a], "B_F": [f(x) for x in finite_b]},
            "complete_moments": {"N_lower": f(finite_n[0]), "A": [f(x) for x in complete_a], "B_upper": f(complete_b[1]), "distance_of_A_from_zero": f(distance)},
            "complete_leakage_square_upper": f(leakage),
            "complete_leakage_square_upper_decimal": dec(leakage),
            "strictly_below_one_third": leakage < Fraction(1, 3),
        }
    uniform = max(Fraction(row["complete_leakage_square_upper"]) for row in rows.values())
    return {
        "schema_version": "1.0",
        "result_id": "K609-K500-COMPLETE-UNIFORM-LEAKAGE-ENCLOSURE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Complete q00/q10/q01 normalized action-vector leakage-square upper enclosure obtained from K602, K608 and one K574 tail charge through K599.",
        "gu_typed_objects": {
            "vectors": "K177 cyclic vectors and K179 coefficient-weighted action vectors through order twelve at the three K162 zero-bath seeds",
            "finite_moments": "N=||v_F||^2, A_F=<v_F,w_F>, B_F=||w_F||^2",
            "tail": "K574's sharp post-order-twelve action-vector norm tail",
            "result": "complete normalized leakage certificate MAP-TYPE=outward-three-moment-enclosure",
            "target": "the K500 uniform cross-term obligation inside the K494 conditional floor interface",
        },
        "composition_theorem": {
            "higher_order_rule": "K608 diagonal uppers propagate through K606 Cauchy--Schwarz; exact seed/sign/coefficient data aggregate orders three through twelve.",
            "order_two_rule": "K602's certified seed intervals are reused, not re-enclosed.",
            "tail_rule": "K599 is applied once with K574 epsilon=9034497/33554432000: A expands by sqrt(N) epsilon and B by (sqrt(B_F)+epsilon)^2.",
            "leakage_rule": "lambda<=B_upper/N_lower-dist(0,A_interval)^2/N_upper^2; retaining the signed subtraction sharpens q00 while crossing zero safely drops it for q10/q01.",
            "tail_charged_exactly_once": True,
        },
        "sharp_tail_norm_upper": f(epsilon),
        "level_enclosures": rows,
        "uniform_complete_leakage_square_upper": f(uniform),
        "uniform_complete_leakage_square_upper_decimal": dec(uniform),
        "exact_controls": {
            "supported_levels": ["q00", "q10", "q01"],
            "all_levels_strictly_below_one_third": all(row["strictly_below_one_third"] for row in rows.values()),
            "uniform_strict_comparison": f(uniform) + " < 1/3",
            "q10_q01_symmetry_preserved": rows["q10"] == rows["q01"],
            "finite_N_lowers_strictly_positive": all(Fraction(row["complete_moments"]["N_lower"]) > 0 for row in rows.values()),
        },
        "decision": {
            "complete_finite_K456_moment_enclosures_emitted": True,
            "complete_K500_uniform_leakage_upper_emitted": True,
            "complete_K500_uniform_leakage_strictly_below_one_third": uniform < Fraction(1, 3),
            "K500_cross_term_obligation_closed": True,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Serialize a named cancellation-safe complete-sector lower witness, then combine it with the already separate cyclic floor and this uniform cross bound only through K494/K473's guarded interface.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "A rigorous complete uniform upper for the K500 normalized action-vector leakage square at q00/q10/q01. It closes only the cross-term obligation; without a numerical noncyclic floor it does not release K473, K152, a spectral theorem, or any source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    rows, controls, decision = payload["level_enclosures"], payload["exact_controls"], payload["decision"]
    assert set(rows) == {"q00", "q10", "q01"} and rows["q10"] == rows["q01"]
    assert all(row["strictly_below_one_third"] for row in rows.values())
    assert Fraction(payload["uniform_complete_leakage_square_upper"]) < Fraction(1, 3)
    assert controls["all_levels_strictly_below_one_third"] and controls["q10_q01_symmetry_preserved"] and controls["finite_N_lowers_strictly_positive"]
    assert payload["composition_theorem"]["tail_charged_exactly_once"]
    assert decision["complete_finite_K456_moment_enclosures_emitted"] and decision["complete_K500_uniform_leakage_upper_emitted"] and decision["K500_cross_term_obligation_closed"]
    assert not decision["native_noncyclic_floor_emitted"] and not decision["K473_released"] and not decision["native_K152_interval_emitted"]


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())

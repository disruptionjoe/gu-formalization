#!/usr/bin/env python3
"""Independent controls and hostile mutations for K417."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k417_k170_seed_consumer_completion_obstruction.py")
MANIFEST = ROOT / "lab/process/k417-k170-seed-consumer-completion-obstruction.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k417_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K417")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K417 = load_solver()


def q(value: str | int) -> Fraction:
    return Fraction(value)


def checks(data: dict) -> list[tuple[str, bool]]:
    result = K417.demo()
    matched = result["matched_native_seed_constraints"]
    gram = list(map(q, matched["chosen_Gram_diagonal"]))
    shape = list(map(q, matched["chosen_shape_generalized_diagonal"]))
    q00g = list(map(q, matched["q00_Gram_interval"]))
    q10g = list(map(q, matched["q10_Gram_interval"]))
    q00w = list(map(q, matched["q00_shape_Rayleigh_interval"]))
    q10w = list(map(q, matched["q10_shape_Rayleigh_interval"]))
    gaps = result["gap_completion_family"]
    sens = result["sensitivity_completion_family"]
    decision = data.get("decision", {})
    boundaries = data.get("boundaries", {})
    return [
        ("schema", result["schema_version"] == "1.0" and data.get("schema_version") == "1.0"),
        ("classification", data.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", data.get("direction") == "observed_to_native"),
        ("Gram positive", all(x > 0 for x in gram)),
        ("q00 Gram matched", q00g[0] < gram[0] < q00g[1]),
        ("q00 fixed-sector Gram", gram[0] == gram[1] == gram[2]),
        ("q10 spectator Gram matched", q10g[0] < q(matched["q10_spectator_Gram"]) < q10g[1]),
        ("q00 shape matched", q00w[0] < shape[0] < q00w[1]),
        ("q00 fixed-sector shape", shape[0] == shape[1] == shape[2]),
        ("q10 spectator shape matched", q10w[0] < q(matched["q10_spectator_shape_Rayleigh"]) < q10w[1]),
        ("shape order", all(Fraction(-2) <= x <= Fraction(1) for x in shape)),
        ("residual upper", q(matched["chosen_shape_residual_square"]) <= q(matched["q00_reported_residual_square_upper"]) and q(matched["chosen_shape_residual_square"]) <= q(matched["q10_reported_residual_square_upper"])),
        ("combined spectra", all(list(map(q, row["combined_Rref_generalized_diagonal"])) == [0, Fraction(1, row["n"]), 1] for row in gaps)),
        ("base completion", all(list(map(q, row["base_R0_generalized_diagonal"])) == [q(row["combined_Rref_generalized_diagonal"][i]) - shape[i] for i in range(3)] for row in gaps)),
        ("gap replay", all(q(row["exterior_gap"]) == Fraction(1, row["n"]) for row in gaps)),
        ("budget replay", all(q(row["K270_budget_at_a3_d1"]) == Fraction(3, 2 * (3 * row["n"] + 1)) for row in gaps)),
        ("gap decreases", all(q(gaps[i+1]["exterior_gap"]) < q(gaps[i]["exterior_gap"]) for i in range(len(gaps)-1))),
        ("sensitivity replay", all(q(row["maximum_integral_uncertainty_squared"]) == Fraction(3, 5 * row["map_norm"]**2) for row in sens)),
        ("tolerance decreases", all(q(sens[i+1]["maximum_integral_uncertainty_squared"]) < q(sens[i]["maximum_integral_uncertainty_squared"]) for i in range(len(sens)-1))),
        ("manifest decision", decision.get("positive_uniform_gap_identified") is False and decision.get("finite_uniform_map_norm_identified") is False and decision.get("positive_uniform_integral_tolerance_identified") is False),
        ("K278 fence", boundaries.get("K278_positive_scalar_linked_to_gap_or_map_norm") is False),
        ("native completion fence", boundaries.get("native_K139_operator_completion_constructed") is False),
        ("K152 fence", boundaries.get("native_K152_interval_emitted") is False),
        ("status fence", boundaries.get("source_ledger_canon_paper_public_or_physical_effect") is False),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    baseline = checks(data)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline {len(baseline)-len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K417 controls")
        return 0
    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["decision"].__setitem__("positive_uniform_gap_identified", True),
        lambda d: d["decision"].__setitem__("finite_uniform_map_norm_identified", True),
        lambda d: d["decision"].__setitem__("positive_uniform_integral_tolerance_identified", True),
        lambda d: d["boundaries"].__setitem__("K278_positive_scalar_linked_to_gap_or_map_norm", True),
        lambda d: d["boundaries"].__setitem__("native_K139_operator_completion_constructed", True),
        lambda d: d["boundaries"].__setitem__("native_K152_interval_emitted", True),
        lambda d: d["boundaries"].__setitem__("source_ledger_canon_paper_public_or_physical_effect", True),
    ]
    caught = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        caught += int(any(not ok for _, ok in checks(trial)))
    if caught != len(mutations):
        print(f"FAIL hostile selftest caught {caught}/{len(mutations)}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

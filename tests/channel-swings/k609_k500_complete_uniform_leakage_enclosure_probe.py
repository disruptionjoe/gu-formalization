#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K609."""

import copy
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k609_k500_complete_uniform_leakage_enclosure.py"
ARTIFACT = ROOT / "lab/process/k609-k500-complete-uniform-leakage-enclosure.json"


def load():
    spec = importlib.util.spec_from_file_location("k609_probe_source", SOURCE)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load(); payload = module.build(); module.validate(payload)
    assert payload == json.loads(ARTIFACT.read_text())
    checks = [
        set(payload["level_enclosures"]) == {"q00", "q10", "q01"},
        payload["level_enclosures"]["q10"] == payload["level_enclosures"]["q01"],
        Fraction(payload["uniform_complete_leakage_square_upper"]) < Fraction(1, 3),
        payload["composition_theorem"]["tail_charged_exactly_once"],
        payload["decision"]["complete_finite_K456_moment_enclosures_emitted"],
        payload["decision"]["K500_cross_term_obligation_closed"],
        not payload["decision"]["native_noncyclic_floor_emitted"],
        not payload["decision"]["K473_released"],
    ]
    mutations = [
        lambda p: p["level_enclosures"].pop("q01"),
        lambda p: p.__setitem__("uniform_complete_leakage_square_upper", "1/3"),
        lambda p: p["composition_theorem"].__setitem__("tail_charged_exactly_once", False),
        lambda p: p["exact_controls"].__setitem__("all_levels_strictly_below_one_third", False),
        lambda p: p["exact_controls"].__setitem__("q10_q01_symmetry_preserved", False),
        lambda p: p["exact_controls"].__setitem__("finite_N_lowers_strictly_positive", False),
        lambda p: p["decision"].__setitem__("complete_finite_K456_moment_enclosures_emitted", False),
        lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_upper_emitted", False),
        lambda p: p["decision"].__setitem__("K500_cross_term_obligation_closed", False),
        lambda p: p["decision"].__setitem__("native_noncyclic_floor_emitted", True),
        lambda p: p["decision"].__setitem__("K473_released", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        changed = copy.deepcopy(payload); mutate(changed)
        try: module.validate(changed)
        except (AssertionError, KeyError): rejected += 1
    assert all(checks) and rejected == len(mutations)
    print(f"K609 exact controls: {sum(checks)}/{len(checks)} passed")
    print(f"K609 hostile mutations: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())

#!/usr/bin/env python3
"""Independent controls and hostile mutations for K416."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k416_k77_stabilizer_symmetry_breaking_ladder.py")
MANIFEST = ROOT / "lab/process/k416-k77-stabilizer-symmetry-breaking-ladder.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k416_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K416 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K416 = load_solver()


def checks(data: dict) -> list[tuple[str, bool]]:
    result = K416.demo()
    full = result["full_stabilizer"]
    compact = result["maximal_compact"]
    diagonal = result["declared_diagonal_breaking"]
    decision = data.get("decision", {})
    boundaries = data.get("boundaries", {})
    return [
        ("schema", result["schema_version"] == "1.0" and data.get("schema_version") == "1.0"),
        ("classification", data.get("classification") == "BRIDGE_OR_SEMANTIC_BOUNDARY"),
        ("direction", data.get("direction") == "observed_to_native"),
        ("full source dimension", full["source_dimension"] == 70),
        ("full target dimension", full["target_dimension"] == 128),
        ("full Hom zero", full["equivariant_hom_rank"] == 0),
        ("subquotients zero", full["all_invariant_subquotients_obstructed"] is True),
        ("compact source dimension", compact["source_dimension"] == 70),
        ("compact target dimension", compact["target_dimension"] == 128),
        ("compact Hom zero", compact["equivariant_hom_rank"] == 0),
        ("diagonal source dimension", diagonal["source_dimension"] == 70),
        ("diagonal target dimension", diagonal["target_dimension"] == 128),
        ("diagonal Hom", diagonal["equivariant_hom_rank"] == 28 * 32 + 14 * 32 == 1344),
        ("repair boundary", decision.get("maximal_compact_repair") is False and decision.get("diagonal_representation_repair") is True),
        ("manifest diagonal Hom", decision.get("diagonal_hom_rank") == 1344),
        ("trace realization fence", boundaries.get("full_spinor_trace_realization_source_selected") is False),
        ("map fence", boundaries.get("action_owned_observation_map_constructed") is False),
        ("quotient fence", boundaries.get("quotient_descent_solved") is False),
        ("Green fence", boundaries.get("green_domain_solved") is False),
        ("ledger fence", boundaries.get("source_ledger_canon_paper_public_or_physical_effect") is False),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K416 controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["decision"].__setitem__("maximal_compact_repair", True),
        lambda d: d["decision"].__setitem__("diagonal_representation_repair", False),
        lambda d: d["decision"].__setitem__("diagonal_hom_rank", 0),
        lambda d: d["boundaries"].__setitem__("full_spinor_trace_realization_source_selected", True),
        lambda d: d["boundaries"].__setitem__("action_owned_observation_map_constructed", True),
        lambda d: d["boundaries"].__setitem__("quotient_descent_solved", True),
        lambda d: d["boundaries"].__setitem__("green_domain_solved", True),
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

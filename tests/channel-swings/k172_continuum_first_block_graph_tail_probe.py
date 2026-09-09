#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K172."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k172_continuum_first_block_graph_tail.py")
MANIFEST = ROOT / "lab/process/k172-continuum-first-block-graph-tail-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k172-continuum-first-block-graph-tail-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k172_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K172 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K172 = load_solver()


def q(value: str) -> Fraction:
    return Fraction(value)


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    blocks = data.get("native_continuum_blocks", {})
    for key in ("n0_exact", "n1_exact", "n1_norm_enclosed"):
        if blocks.get(key) is not True:
            failures.append(key)
    tail = data.get("graph_tail", {})
    if tail.get("symbolic_complete_theorem") is not True or tail.get("native_numeric_tail") is not False:
        failures.append("tail")
    if data.get("Hilbert_only_tail_route_killed") is not True:
        failures.append("counterexample")
    release = data.get("release_test", {})
    for key in ("native_n0_vector_serialized", "native_n1_vector_serialized", "native_n1_vector_norm_enclosed"):
        if release.get(key) is not True:
            failures.append(key)
    for key in ("complete_native_all_order_vector_tail_serialized", "complete_R_ref_form_dual_residual_serialized", "native_K152_interval_emitted"):
        if release.get(key) is not False:
            failures.append(key)
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K172.demo()
    vacuum, impurity = result["native_continuum_blocks"]
    release = result["release_test"]
    return [
        ("schema", result["schema_version"] == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("vacuum n0", vacuum["n0_exact"] == "W_0 phi=-256 phi"),
        ("impurity n0", impurity["n0_exact"] == "W_0 phi=-256 phi"),
        ("vacuum components", vacuum["n1_transition_components"] == 2),
        ("impurity components", impurity["n1_transition_components"] == 1),
        ("vacuum multiplicity", vacuum["normal_ordered_self_energy_multiplicity_per_component"] == 1),
        ("impurity multiplicity", impurity["normal_ordered_self_energy_multiplicity_per_component"] == 2),
        ("vacuum vector", vacuum["W1_g1_per_component"] == "(256-1*D_256(omega(p)))*h(p)"),
        ("impurity vector", impurity["W1_g1_per_component"] == "(256-2*D_256(omega(p)))*h(p)"),
        ("correction square", q(vacuum["D_h_norm_sq_upper"]) == Fraction(8, 2295)),
        ("correction norm", q(vacuum["D_h_norm_upper_used"]) == Fraction(1, 16)),
        ("vacuum norm positive", q(vacuum["full_n1_vector_norm_interval"][0]) > 12),
        ("impurity norm positive", q(impurity["full_n1_vector_norm_interval"][0]) > 8),
        ("graph formula", result["graph_tail_theorem"]["unresolved_after_order_N"] == "B*c*q_D^(N+1)/((1-q_D)*(1-q_H))"),
        ("graph positive", q(result["graph_tail_theorem"]["positive_control"]) == Fraction(8, 5)),
        ("numeric graph missing", result["graph_tail_theorem"]["native_numeric_tail_emitted"] is False),
        ("harmonic obstruction", result["Hilbert_only_counterexample"]["action_block_sum_diverges"] is True),
        ("counterexample fence", result["Hilbert_only_counterexample"]["native_continuum_counterexample"] is False),
        ("first blocks released", release["native_n0_vector_serialized"] is True and release["native_n1_vector_serialized"] is True),
        ("all-order tail open", release["complete_native_all_order_vector_tail_serialized"] is False),
        ("residual open", release["complete_R_ref_form_dual_residual_serialized"] is False),
        ("K152 open", release["native_K152_interval_emitted"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("native formulas prose", "W_0 phi=-256 phi.                                     (2)" in text and "(256-m D_256(omega(p)))h(p)" in text),
        ("graph theorem prose", "B c q_D^(N+1)/((1-q_D)(1-q_H))" in text),
        ("Hilbert counterexample prose", "1/(n+1)" in text),
        ("next numeric gate", "numerical graph contraction `q_D`" in text),
        ("ledger fence", all(v.endswith("_UNCHANGED") for v in result["ledger_effect"].values())),
        ("no physical selection", result["physical_or_source_selection"] is False),
        ("no export credit", result["Born_prediction_or_confirmation_credit"] is False),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline {len(baseline)-len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K172 exact controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["native_continuum_blocks"].__setitem__("n0_exact", False),
        lambda d: d["native_continuum_blocks"].__setitem__("n1_exact", False),
        lambda d: d["native_continuum_blocks"].__setitem__("n1_norm_enclosed", False),
        lambda d: d["graph_tail"].__setitem__("symbolic_complete_theorem", False),
        lambda d: d["graph_tail"].__setitem__("native_numeric_tail", True),
        lambda d: d.__setitem__("Hilbert_only_tail_route_killed", False),
        lambda d: d["release_test"].__setitem__("native_n1_vector_serialized", False),
        lambda d: d["release_test"].__setitem__("complete_native_all_order_vector_tail_serialized", True),
        lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True),
        lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True),
    ]
    caught = 0
    for mutate in mutations:
        mutant = copy.deepcopy(data)
        mutate(mutant)
        if manifest_failures(mutant):
            caught += 1
    prose_mutants = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("W_0 phi=-256 phi.                                     (2)", "W_0 phi=0.                                            (2)", 1),
        text.replace("B c q_D^(N+1)/((1-q_D)(1-q_H))", "B c", 1),
        text.replace("1/(n+1)", "q^n", 1),
        text.replace("numerical graph contraction `q_D`", "numerical contraction", 1),
    ]
    for mutant in prose_mutants:
        if any(not ok for _, ok in checks(data, mutant)):
            caught += 1
    expected = len(mutations) + len(prose_mutants)
    if caught != expected:
        print(f"FAIL hostile {caught}/{expected}")
        return 1
    print(f"PASS hostile {caught}/{expected} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

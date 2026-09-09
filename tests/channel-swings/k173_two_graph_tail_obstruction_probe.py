#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K173."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k173_two_graph_tail_obstruction.py")
MANIFEST = ROOT / "lab/process/k173-two-graph-tail-obstruction-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k173-two-graph-tail-obstruction-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k173_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K173 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K173 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    graphs = data.get("two_graph_replay", {})
    if graphs.get("free_energy_graph_finite_q_D") is not False:
        failures.append("free_graph")
    if graphs.get("particle_number_graph_finite_B") is not False:
        failures.append("number_graph")
    if data.get("mixed_graph_certificate_rejected") is not True:
        failures.append("mixed_graph")
    replacement = data.get("fractional_replacement", {})
    if replacement.get("quarter_graph_candidate_open") is not True:
        failures.append("replacement")
    if replacement.get("complete_native_constants_serialized") is not False:
        failures.append("replacement_ceiling")
    release = data.get("release_test", {})
    for key in (
        "complete_native_all_order_vector_tail_serialized",
        "complete_R_ref_form_dual_residual_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K173.demo()
    free = result["free_energy_graph"]
    number = result["particle_number_graph"]
    same = result["same_graph_contract"]
    frac = result["fractional_replacement"]
    release = result["release_test"]
    lower = [float(value) for value in result["self_energy_growth_control"]["lower_values"]]
    return [
        ("schema", result["schema_version"] == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("free graph domain", free["domain"] == "Dom(H0)"),
        ("free graph point tail", free["omega_h_in_L2"] is False),
        ("free graph invariant", free["G_maps_domain_to_itself"] is False),
        ("free graph q", free["finite_q_D"] is False),
        ("number graph contraction", number["G_contraction_upper"] == "3/4"),
        ("self energy lower", "log((e+257)/513)" in number["D_lower_bound"]),
        ("self energy unbounded", number["lower_bound_unbounded"] is True),
        ("number graph W", number["W_graph_to_H_bounded"] is False),
        ("growth samples", lower[0] < lower[1] < lower[2]),
        ("same domain id", same["requires_domain_id"] is True),
        ("same norm id", same["requires_norm_id"] is True),
        ("mixed graph rejected", same["mixing_q_D_and_B_across_graphs_rejected"] is True),
        ("abstract positive", same["abstract_positive_control_accepted"] is True),
        ("native tail refused", same["native_K172_tail_admitted"] is False),
        ("quarter domain", frac["candidate_domain"] == "Dom(dGamma(omega)^(1/4)+N+1)"),
        ("quarter point vector", frac["vacuum_transition"]["point_vector_in_domain"] is True),
        ("quarter D coefficient", frac["vacuum_transition"]["D_weight_coefficient_upper"] == "1/pi"),
        ("quarter vacuum subblock", frac["vacuum_transition"]["one_bath_diagonal_block_bound"] == "256+1/pi"),
        ("quarter impurity subblock", frac["one_impurity_transition"]["one_bath_diagonal_block_bound"] == "256+2/pi"),
        ("full fractional open", frac["native_complete_B_quarter_serialized"] is False),
        ("all order open", release["complete_native_all_order_vector_tail_serialized"] is False),
        ("residual open", release["complete_R_ref_form_dual_residual_serialized"] is False),
        ("K152 open", release["native_K152_interval_emitted"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("free graph prose", "omega h notin L2" in text),
        ("lower bound prose", "log((e+257)/513)" in text),
        ("same graph prose", "same explicitly normalized domain" in text),
        ("quarter route prose", "s=1/4" in text),
        ("ledger fence", all(value.endswith("_UNCHANGED") for value in result["ledger_effect"].values())),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K173 exact controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["two_graph_replay"].__setitem__("free_energy_graph_finite_q_D", True),
        lambda d: d["two_graph_replay"].__setitem__("particle_number_graph_finite_B", True),
        lambda d: d.__setitem__("mixed_graph_certificate_rejected", False),
        lambda d: d["fractional_replacement"].__setitem__("quarter_graph_candidate_open", False),
        lambda d: d["fractional_replacement"].__setitem__("complete_native_constants_serialized", True),
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
        text.replace("omega h notin L2", "omega h in L2", 1),
        text.replace("log((e+257)/513)", "0", 1),
        text.replace("same explicitly normalized domain", "different domains", 1),
        text.replace("s=1/4", "s=1", 1),
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

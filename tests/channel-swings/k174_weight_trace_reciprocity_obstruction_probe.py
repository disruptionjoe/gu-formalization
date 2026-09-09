#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K174."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k174_weight_trace_reciprocity_obstruction.py")
MANIFEST = ROOT / "lab/process/k174-weight-trace-reciprocity-obstruction-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k174-weight-trace-reciprocity-obstruction-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k174_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K174 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K174 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    quarter = data.get("quarter_graph", {})
    if quarter.get("G_graph_contraction_upper") != "131/300" or quarter.get("G_graph_contraction_strict") is not True:
        failures.append("quarter_contraction")
    if quarter.get("complete_W_graph_to_Hilbert_bounded") is not False:
        failures.append("quarter_W")
    theorem = data.get("weight_trace_reciprocity", {})
    if theorem.get("no_positive_diagonal_weight_satisfies_both") is not True:
        failures.append("reciprocity")
    if theorem.get("non_diagonal_or_cancellation_adapted_domains_ruled_out") is not False:
        failures.append("scope")
    orbit = data.get("orbit_tail_interface", {})
    if orbit.get("native_all_order_coefficient_tail_serialized") is not False:
        failures.append("native_tail")
    release = data.get("release_test", {})
    for key in (
        "coefficient_complete_base_R0_action_column_serialized",
        "complete_R_ref_form_dual_residual_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K174.demo()
    quarter = result["quarter_graph"]
    theorem = result["weight_trace_reciprocity"]
    orbit = result["orbit_tail_interface"]
    release = result["release_test"]
    powers = theorem["power_controls"]
    product_lowers = [float(x) for x in theorem["sample_product_lowers"]]
    return [
        ("schema", result["schema_version"] == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("quarter domain", "dGamma(omega)" in quarter["domain"]),
        ("quarter h", quarter["h_norm_upper"] == "1/27"),
        ("quarter weighted h", quarter["quarter_weighted_h_norm_upper"] == "9/50"),
        ("quarter multiplicity", quarter["outgoing_channel_multiplicity_upper"] == 2),
        ("quarter contraction", quarter["G_graph_contraction_upper"] == "131/300"),
        ("quarter strict", quarter["G_graph_contraction_strict"] is True),
        ("quarter diagonal", quarter["named_diagonal_self_energy_block_bounded"] is True),
        ("quarter trace", quarter["point_trace_continuous"] is False),
        ("quarter complete W", quarter["complete_W_graph_to_Hilbert_bounded"] is False),
        ("reciprocity formula", "log(R/257)^2/4" in theorem["finite_interval_product_lower"]),
        ("reciprocity growth", product_lowers[0] < product_lowers[1] < product_lowers[2]),
        ("reciprocity universal", theorem["no_positive_diagonal_weight_satisfies_both"] is True),
        ("power quarter", powers[0]["boundary_profile_in_graph"] is True and powers[0]["point_trace_continuous"] is False),
        ("power half", powers[1]["endpoint_half_has_two_logarithmic_divergences"] is True),
        ("power three quarters", powers[2]["boundary_profile_in_graph"] is False and powers[2]["point_trace_continuous"] is True),
        ("no power intersection", all(item["both"] is False for item in powers)),
        ("log control", theorem["finite_logarithmic_weights_admit_boundary_but_not_trace"] is True),
        ("scope fence", theorem["non_diagonal_or_cancellation_adapted_domains_ruled_out"] is False),
        ("orbit cancellation", orbit["requires_complete_renormalized_vectors_not_separate_singular_factors"] is True),
        ("orbit control", orbit["abstract_positive_control_tail"] == "9/1600"),
        ("orbit finite prefix rejected", orbit["native_finite_prefix_rejected"] is True),
        ("native orbit open", orbit["native_all_order_coefficient_tail_serialized"] is False),
        ("action open", release["coefficient_complete_base_R0_action_column_serialized"] is False),
        ("residual open", release["complete_R_ref_form_dual_residual_serialized"] is False),
        ("K152 open", release["native_K152_interval_emitted"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("cauchy prose", "Cauchy--Schwarz" in text),
        ("isolated exchange", "isolated nonzero exchange channel" in text),
        ("diagonal scope", "diagonal multiplication-weight graphs" in text),
        ("coefficient route", "coefficient-specific" in text),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K174 exact controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["quarter_graph"].__setitem__("G_graph_contraction_upper", "3/2"),
        lambda d: d["quarter_graph"].__setitem__("G_graph_contraction_strict", False),
        lambda d: d["quarter_graph"].__setitem__("complete_W_graph_to_Hilbert_bounded", True),
        lambda d: d["weight_trace_reciprocity"].__setitem__("no_positive_diagonal_weight_satisfies_both", False),
        lambda d: d["weight_trace_reciprocity"].__setitem__("non_diagonal_or_cancellation_adapted_domains_ruled_out", True),
        lambda d: d["orbit_tail_interface"].__setitem__("native_all_order_coefficient_tail_serialized", True),
        lambda d: d["release_test"].__setitem__("coefficient_complete_base_R0_action_column_serialized", True),
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
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING"),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", ""),
        text.replace("```gu-typed-objects", "```text"),
        text.replace("Cauchy--Schwarz", "triangle inequality"),
        text.replace("isolated nonzero exchange channel", "unisolated channel"),
        text.replace("diagonal multiplication-weight graphs", "all domains"),
        text.replace("coefficient-specific", "generic"),
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

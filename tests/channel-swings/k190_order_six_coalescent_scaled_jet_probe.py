#!/usr/bin/env python3
"""Independent exact, replay, reporting, and hostile controls for K190."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k190-order-six-coalescent-scaled-jet-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k190-order-six-coalescent-scaled-jet-wave-2026-09-10.md"
SOLVER = ROOT / "tests/channel-swings/k190_order_six_coalescent_scaled_jet.py"
K186 = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k190_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K190 = load_solver()


def symbolic_identity(size: int) -> bool:
    x = sp.symbols("x", nonzero=True)
    q_function = sp.Function("q")(x)
    g = q_function / x
    matrix = sp.Matrix(
        [
            [
                sp.diff(g, x, row + column)
                / (sp.factorial(row) * sp.factorial(column))
                for column in range(size)
            ]
            for row in range(size)
        ]
    )
    original = sp.expand(x ** (size * size) * matrix.det())
    symbols = sp.symbols("q a1 a2 a3 a4")
    replacement = {q_function: symbols[0]}
    for order in range(1, 5):
        replacement[sp.diff(q_function, x, order)] = symbols[order] / x**order
    original = sp.simplify(original.xreplace(replacement))
    candidate = sp.expand(K190.regularizer_from_scaled_jets(size, symbols))
    return sp.simplify(original - candidate) == 0


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    source = json.loads(K186.read_text())
    fixed = data.get("fixed_control", {})
    normal = data.get("exact_normal_form", {})
    certificate = data.get("arb_certificate", {})
    controls = data.get("independent_controls", {}).get("all_pattern_near_collision", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if (
        fixed.get("coalescent_argument_range") != "2^-200<=x<=1/4"
        or fixed.get("source_patterns") != 53
        or fixed.get("source_nontrivial_occurrences") != 468
        or fixed.get("source_time_gram_entries") != 234
        or fixed.get("source_coherent_groups") != 18
    ):
        failures.append("fixed")
    if normal.get("R2") != "q^2+q*a2-a1^2" or "q*a2*a4" not in normal.get("R3", ""):
        failures.append("normal_forms")
    if normal.get("negative_powers_cancel_before_evaluation") is not True:
        failures.append("negative_powers")
    if set(normal.get("jet_identities", {})) != {"a0", "a1", "a2", "a3", "a4"}:
        failures.append("jets")
    rows = certificate.get("dyadic_rows", [])
    if certificate.get("tested_radii") != 199 or len(rows) != 199:
        failures.append("radii_count")
    if [row.get("x") for row in rows] != [f"2^-{power}" for power in range(2, 201)]:
        failures.append("radii_sequence")
    if certificate.get("all_raw_hankel_balls_overlap_scaled_balls") is not True:
        failures.append("overlap")
    if certificate.get("all_scaled_R2_and_R3_balls_strictly_positive") is not True:
        failures.append("positivity")
    if certificate.get("R2_midpoint_range", [0])[0] <= 0.83:
        failures.append("R2_range")
    if certificate.get("R3_midpoint_range", [0])[0] <= 0.72:
        failures.append("R3_range")
    if certificate.get("minimum_width_gain_R2", 0) <= 3:
        failures.append("R2_width_gain")
    if certificate.get("minimum_width_gain_R3", 0) <= 30:
        failures.append("R3_width_gain")
    pattern_rows = controls.get("patterns", [])
    if controls.get("tested_patterns") != 53 or len(pattern_rows) != 53:
        failures.append("pattern_count")
    if {row.get("pattern_id") for row in pattern_rows} != set(source["unique_patterns"]):
        failures.append("pattern_ids")
    for row in pattern_rows:
        prior = source["unique_patterns"].get(row.get("pattern_id"), {})
        if row.get("left_canonical_positions") != prior.get("left_canonical_positions"):
            failures.append(f"left:{row.get('pattern_id')}")
        if row.get("right_canonical_positions") != prior.get("right_canonical_positions"):
            failures.append(f"right:{row.get('pattern_id')}")
        if row.get("gap_powers") != [10, 24]:
            failures.append(f"gaps:{row.get('pattern_id')}")
        errors = row.get("relative_errors_to_scaled_jet_limit", [])
        if len(errors) != 2 or errors[-1] >= 1e-20:
            failures.append(f"convergence:{row.get('pattern_id')}")
    if controls.get("maximum_finest_gap_relative_error", 1) >= 1e-20:
        failures.append("maximum_gap_error")
    required_true = (
        "exact_R2_scaled_jet_normal_form_banked",
        "exact_R3_scaled_jet_normal_form_banked",
        "directed_arb_dyadic_coalescent_spine_banked",
        "all_53_patterns_replayed_near_collision",
        "all_468_occurrences_remain_in_scope",
    )
    required_false = (
        "finite_gap_regularizer_interval_serialized",
        "duffy_jacobi_chain_rule_envelopes_serialized",
        "determinant_preserving_positive_radius_core_error_serialized",
        "complete_outward_order_six_total_error_serialized",
        "accurate_order_six_prefix_released",
        "complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true):
        failures.append("release_true")
    if any(release.get(key) is not False for key in required_false):
        failures.append("release_false")
    decision = data.get("decision", {})
    if decision.get("coalescent_singularity_is_numerically_resolved") is not True:
        failures.append("decision")
    if decision.get("finite_gap_outward_coverage_is_complete") is not False:
        failures.append("finite_gap_boundary")
    if "bivariate confluent" not in decision.get("next_exact_input", ""):
        failures.append("next_input")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()):
        failures.append("ledger")
    if data.get("physical_or_source_selection") is not False:
        failures.append("physical")
    if data.get("Born_prediction_or_confirmation_credit") is not False:
        failures.append("Born")
    if data.get("canon_paper_release_or_public_posture_move") is not False:
        failures.append("public")
    return failures


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    return [
        ("manifest", not failures),
        ("deterministic replay", K190.build() == data),
        ("symbolic R2 identity", symbolic_identity(2)),
        ("symbolic R3 identity", symbolic_identity(3)),
        ("artifact exists", ARTIFACT.exists()),
        ("solver exists", SOLVER.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("complete census", "53 distinct" in text and "468" in text),
        ("finite gap withheld", "no between-radius or nonzero-gap outward coverage" in text),
        ("prefix withheld", "accurate order-six prefix remains" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations = (
        ("wrong_range", lambda d: d["fixed_control"].__setitem__("coalescent_argument_range", "2^-199<=x<=1/4")),
        ("wrong_normal", lambda d: d["exact_normal_form"].__setitem__("R2", "q^2-q*a2-a1^2")),
        ("drop_jet", lambda d: d["exact_normal_form"]["jet_identities"].pop("a4")),
        ("restore_negative_power", lambda d: d["exact_normal_form"].__setitem__("negative_powers_cancel_before_evaluation", False)),
        ("drop_radius", lambda d: d["arb_certificate"]["dyadic_rows"].pop()),
        ("invent_overlap", lambda d: d["arb_certificate"].__setitem__("all_raw_hankel_balls_overlap_scaled_balls", False)),
        ("break_positivity", lambda d: d["arb_certificate"].__setitem__("all_scaled_R2_and_R3_balls_strictly_positive", False)),
        ("break_width", lambda d: d["arb_certificate"].__setitem__("minimum_width_gain_R3", 1)),
        ("drop_pattern", lambda d: d["independent_controls"]["all_pattern_near_collision"]["patterns"].pop()),
        ("wrong_position", lambda d: d["independent_controls"]["all_pattern_near_collision"]["patterns"][0].__setitem__("left_canonical_positions", [])),
        ("weak_gap", lambda d: d["independent_controls"]["all_pattern_near_collision"].__setitem__("maximum_finest_gap_relative_error", 1.0)),
        ("invent_finite_gap", lambda d: d["release_test"].__setitem__("finite_gap_regularizer_interval_serialized", True)),
        ("invent_chain", lambda d: d["release_test"].__setitem__("duffy_jacobi_chain_rule_envelopes_serialized", True)),
        ("invent_core", lambda d: d["release_test"].__setitem__("determinant_preserving_positive_radius_core_error_serialized", True)),
        ("invent_total", lambda d: d["release_test"].__setitem__("complete_outward_order_six_total_error_serialized", True)),
        ("invent_prefix", lambda d: d["release_test"].__setitem__("accurate_order_six_prefix_released", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_physical", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_public", lambda d: d.__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    results = []
    for name, mutate in mutations:
        broken = copy.deepcopy(data)
        mutate(broken)
        results.append((name, bool(manifest_failures(broken))))
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    checks = exact_checks(data)
    failed = [name for name, ok in checks if not ok]
    if failed:
        print(f"FAIL {len(failed)}/{len(checks)}: {', '.join(failed)}")
        return 1
    if args.selftest:
        hostile = hostile_checks(data)
        missed = [name for name, caught in hostile if not caught]
        if missed:
            print(f"HOSTILE FAIL {len(missed)}/{len(hostile)}: {', '.join(missed)}")
            return 1
        print(f"PASS {len(checks)}/{len(checks)}; hostile {len(hostile)}/{len(hostile)} caught")
        return 0
    print(f"PASS {len(checks)}/{len(checks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

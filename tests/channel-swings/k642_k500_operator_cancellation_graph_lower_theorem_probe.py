#!/usr/bin/env python3
"""Independent baseline and hostile controls for K642."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json"


def load_solver():
    path = Path(__file__).with_name("k642_k500_operator_cancellation_graph_lower_theorem.py")
    spec = importlib.util.spec_from_file_location("k642_probe_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    amp = data.get("spectator_amplification_theorem", {})
    operator = data.get("operator_lower_theorem", {})
    extension = data.get("controlled_extension_theorem", {})
    native = data.get("native_interface_status", {})
    decision = data.get("decision", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    required_amp = ("finite_or_infinite_spectator_space_allowed", "base_domain_dense", "direct_sum_decomposition_unique", "matched_Bochner_trace_continuous", "beta_squared_strictly_below_one_over_256", "proof_constant_independent_of_H_spec")
    if any(amp.get(key) is not True for key in required_amp):
        bad.append("amplification")
    if amp.get("spectator_dimension_restricted") is not False:
        bad.append("dimension_restriction")
    if operator.get("floor_function") != "min(1/2,m-1/128)" or operator.get("dimension_free") is not True:
        bad.append("operator_floor")
    if operator.get("finite_boundary_matrix_required") is not False or operator.get("operator_valued_spectator_action_allowed") is not True:
        bad.append("operator_type")
    if operator.get("reference_control_is_actual_K139_K168_floor") is not False:
        bad.append("reference_floor")
    if extension.get("floor_function") != "min(1/2-alpha,m-delta-1/128)":
        bad.append("extension_floor")
    if extension.get("same_cancellation_domain_required") is not True:
        bad.append("same_domain")
    if extension.get("separate_singular_factor_bounds_used") is not False or extension.get("mixed_incompatible_graphs_used") is not False:
        bad.append("graph_splice")
    if not extension.get("finite_controls") or any(row.get("passes") is not True for row in extension["finite_controls"]):
        bad.append("finite_controls")
    required_native_false = ("actual_K139_K168_to_D_op_intertwiner_identified", "actual_complete_boundary_form_B_identified", "actual_operator_lower_m_identified", "actual_remainder_alpha_delta_identified", "native_same_domain_form_identity_proved", "named_complete_sector_floor_emitted", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in required_native_false):
        bad.append("native_ceiling")
    if decision.get("correct_operator_valued_analytic_interface_constructed") is not True or decision.get("quantitative_native_complete_form_part_released") is not False:
        bad.append("decision")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("dimension-free", "Bochner", "alpha", "does not supply", "no native complete-sector floor"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    amp = data["spectator_amplification_theorem"]
    operator = data["operator_lower_theorem"]
    extension = data["controlled_extension_theorem"]
    native = data["native_interface_status"]
    controls = extension["finite_controls"]
    return [
        ("fresh theorem matches", fresh["operator_lower_theorem"] == operator),
        ("fresh extension matches", fresh["controlled_extension_theorem"] == extension),
        ("spectator unrestricted", amp["spectator_dimension_restricted"] is False),
        ("finite and infinite allowed", amp["finite_or_infinite_spectator_space_allowed"] is True),
        ("base dense", amp["base_domain_dense"] is True),
        ("conditional graph dense", amp["cancellation_domain_dense_when_B_form_domain_dense"] is True),
        ("decomposition unique", amp["direct_sum_decomposition_unique"] is True),
        ("projection norm one", amp["coefficient_projection_continuous_with_norm"] == "1"),
        ("Bochner trace", amp["matched_Bochner_trace_continuous"] is True),
        ("beta bound", amp["beta_squared_strictly_below_one_over_256"] is True),
        ("dimension-free beta", amp["proof_constant_independent_of_H_spec"] is True),
        ("operator hypothesis", "self-adjoint" in operator["hypothesis"]),
        ("operator floor", operator["floor_function"] == "min(1/2,m-1/128)"),
        ("unbounded B allowed", operator["bounded_boundary_operator_required"] is False),
        ("finite matrix unnecessary", operator["finite_boundary_matrix_required"] is False),
        ("operator action allowed", operator["operator_valued_spectator_action_allowed"] is True),
        ("dimension free theorem", operator["dimension_free"] is True),
        ("reference floor", operator["reference_control_floor"] == "-257/128"),
        ("reference nonnative", operator["reference_control_is_actual_K139_K168_floor"] is False),
        ("controlled floor", extension["floor_function"] == "min(1/2-alpha,m-delta-1/128)"),
        ("same domain", extension["same_cancellation_domain_required"] is True),
        ("no singular split", extension["separate_singular_factor_bounds_used"] is False),
        ("no graph splice", extension["mixed_incompatible_graphs_used"] is False),
        ("four dimensions", [row["spectator_dimension"] for row in controls] == [1, 2, 5, 8]),
        ("all exact controls", all(row["passes"] for row in controls)),
        ("native B withheld", native["actual_complete_boundary_form_B_identified"] is False),
        ("native floor withheld", native["named_complete_sector_floor_emitted"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("restrict spectator dimension", lambda d: d["spectator_amplification_theorem"].__setitem__("spectator_dimension_restricted", True)),
        ("erase infinite spaces", lambda d: d["spectator_amplification_theorem"].__setitem__("finite_or_infinite_spectator_space_allowed", False)),
        ("erase Bochner trace", lambda d: d["spectator_amplification_theorem"].__setitem__("matched_Bochner_trace_continuous", False)),
        ("erase beta", lambda d: d["spectator_amplification_theorem"].__setitem__("beta_squared_strictly_below_one_over_256", False)),
        ("erase dimension freedom", lambda d: d["spectator_amplification_theorem"].__setitem__("proof_constant_independent_of_H_spec", False)),
        ("wrong operator floor", lambda d: d["operator_lower_theorem"].__setitem__("floor_function", "m")),
        ("require finite matrix", lambda d: d["operator_lower_theorem"].__setitem__("finite_boundary_matrix_required", True)),
        ("forbid operator action", lambda d: d["operator_lower_theorem"].__setitem__("operator_valued_spectator_action_allowed", False)),
        ("invent native reference", lambda d: d["operator_lower_theorem"].__setitem__("reference_control_is_actual_K139_K168_floor", True)),
        ("wrong extension floor", lambda d: d["controlled_extension_theorem"].__setitem__("floor_function", "m-delta")),
        ("erase same domain", lambda d: d["controlled_extension_theorem"].__setitem__("same_cancellation_domain_required", False)),
        ("allow singular split", lambda d: d["controlled_extension_theorem"].__setitem__("separate_singular_factor_bounds_used", True)),
        ("allow graph splice", lambda d: d["controlled_extension_theorem"].__setitem__("mixed_incompatible_graphs_used", True)),
        ("fail control", lambda d: d["controlled_extension_theorem"]["finite_controls"][0].__setitem__("passes", False)),
        ("invent intertwiner", lambda d: d["native_interface_status"].__setitem__("actual_K139_K168_to_D_op_intertwiner_identified", True)),
        ("invent B", lambda d: d["native_interface_status"].__setitem__("actual_complete_boundary_form_B_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("actual_operator_lower_m_identified", True)),
        ("invent remainder", lambda d: d["native_interface_status"].__setitem__("actual_remainder_alpha_delta_identified", True)),
        ("invent form identity", lambda d: d["native_interface_status"].__setitem__("native_same_domain_form_identity_proved", True)),
        ("invent floor", lambda d: d["native_interface_status"].__setitem__("named_complete_sector_floor_emitted", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release native part", lambda d: d["decision"].__setitem__("quantitative_native_complete_form_part_released", True)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("bad alpha accepted", lambda d: d["controlled_extension_theorem"].__setitem__("remainder_hypothesis", "alpha unrestricted")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "native physical floor proved")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    try:
        SOLVER.controlled_floor(0, "1/2", 0)
    except SOLVER.CertificateError:
        caught[-2] = ("bad alpha rejected", True)
    else:
        caught[-2] = ("bad alpha rejected", False)
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    baseline = exact_checks(data)
    manifest_failures = failures(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K642 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

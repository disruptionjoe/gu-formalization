#!/usr/bin/env python3
"""Independent exact and hostile controls for K646."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k646-k500-parity-sector-lower-reduction.json"


def load_solver():
    path = Path(__file__).with_name("k646_k500_parity_sector_lower_reduction.py")
    spec = importlib.util.spec_from_file_location("k646_probe_solver", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    theorem = data.get("parity_reduction_theorem", {})
    tail = data.get("limit_and_tail_interface", {})
    composition = data.get("K644_composition", {})
    control = data.get("exact_control", {})
    native = data.get("native_interface_status", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    if theorem.get("sector_floor") != "m_n=min(m_n^+,m_n^-)" or theorem.get("global_floor") != "m=min(inf_n m_n^+,inf_n m_n^- )".replace("^- ", "^-"):
        bad.append("floors")
    if "=0" not in str(theorem.get("cross_parity_identity", "")) or "operator-valued" not in str(theorem.get("no_scalar_matrix_reduction", "")):
        bad.append("reduction")
    if "min(t_plus,t_minus)" not in str(tail.get("parity_tail_rule", "")) or "must be restored" not in str(tail.get("symmetry_breaking_remainder_rule", "")):
        bad.append("tail")
    if composition.get("K642_base_floor") != "min(1/2,m-1/128)" or composition.get("K642_controlled_floor") != "min(1/2-alpha,m-delta-1/128)":
        bad.append("K642")
    if control.get("commutes_with_flavor_involution") is not True or control.get("cross_parity_block_zero") is not True or control.get("control_is_synthetic_not_native") is not True:
        bad.append("control")
    required_false = ("actual_K139_K168_common_domain_identity_proved", "actual_parity_compression_forms_identified", "actual_parity_floors_identified", "actual_uniform_parity_tails_identified", "native_global_m_identified", "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("m_n=min", "independent uniform tails", "not a scalar three-channel model", "remain missing"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    theorem = data["parity_reduction_theorem"]
    tail = data["limit_and_tail_interface"]
    composition = data["K644_composition"]
    control = data["exact_control"]
    native = data["native_interface_status"]
    return [
        ("fresh theorem", fresh["parity_reduction_theorem"] == theorem),
        ("fresh tail", fresh["limit_and_tail_interface"] == tail),
        ("self-adjoint involution", "self-adjoint unitary" in theorem["involution"]),
        ("parity projections", "(I+J_n)/2" in theorem["projections"]),
        ("cross zero", theorem["cross_parity_identity"].endswith("=0")),
        ("orthogonal sum", "direct_sum" in theorem["orthogonal_form_sum"]),
        ("sector min", theorem["sector_floor"] == "m_n=min(m_n^+,m_n^-)"),
        ("global min", theorem["global_floor"] == "m=min(inf_n m_n^+,inf_n m_n^-)"),
        ("single falsifier", "rejects" in theorem["single_parity_falsifier"]),
        ("operator carrier preserved", "operator-valued" in theorem["no_scalar_matrix_reduction"]),
        ("finite covariance", "every finite" in tail["finite_prefix_covariance"]),
        ("closed limit", "norm resolvent" in tail["closed_limit_rule"]),
        ("parity tails", "min(t_plus,t_minus)" in tail["parity_tail_rule"]),
        ("prefix composition", "m=min" in tail["prefix_tail_composition"]),
        ("remainder paritywise", "alpha_plus" in tail["remainder_rule"]),
        ("broken symmetry restored", "must be restored" in tail["symmetry_breaking_remainder_rule"]),
        ("K644 local", "separately" in composition["parity_local_use"]),
        ("comparison eigenvalues", "lambda_min" in composition["parity_comparison_floors"]),
        ("sector output", "min(ell_n^+,ell_n^-)" in composition["sector_output"]),
        ("global output", "independent uniform parity tails" in composition["global_output"]),
        ("K642 base", composition["K642_base_floor"] == "min(1/2,m-1/128)"),
        ("K642 remainder", composition["K642_controlled_floor"] == "min(1/2-alpha,m-delta-1/128)"),
        ("commuting control", control["commutes_with_flavor_involution"] is True),
        ("zero cross control", control["cross_parity_block_zero"] is True),
        ("plus lower", control["plus_row_lower"] == "9/2"),
        ("minus lower", control["minus_row_lower"] == "7/4"),
        ("global lower", control["global_row_lower"] == "7/4"),
        ("synthetic scoped", control["control_is_synthetic_not_native"] is True),
        ("native m withheld", native["native_global_m_identified"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("wrong sector floor", lambda d: d["parity_reduction_theorem"].__setitem__("sector_floor", "m_n=m_n^+")),
        ("wrong global floor", lambda d: d["parity_reduction_theorem"].__setitem__("global_floor", "m=inf plus")),
        ("erase cross zero", lambda d: d["parity_reduction_theorem"].__setitem__("cross_parity_identity", "unknown")),
        ("claim scalar", lambda d: d["parity_reduction_theorem"].__setitem__("no_scalar_matrix_reduction", "scalar three-channel model")),
        ("erase tail", lambda d: d["limit_and_tail_interface"].__setitem__("parity_tail_rule", "prefix only")),
        ("drop broken remainder", lambda d: d["limit_and_tail_interface"].__setitem__("symmetry_breaking_remainder_rule", "discard cross block")),
        ("wrong base", lambda d: d["K644_composition"].__setitem__("K642_base_floor", "m")),
        ("wrong remainder", lambda d: d["K644_composition"].__setitem__("K642_controlled_floor", "m-delta")),
        ("noncommuting control", lambda d: d["exact_control"].__setitem__("commutes_with_flavor_involution", False)),
        ("cross control", lambda d: d["exact_control"].__setitem__("cross_parity_block_zero", False)),
        ("promote control", lambda d: d["exact_control"].__setitem__("control_is_synthetic_not_native", False)),
        ("invent identity", lambda d: d["native_interface_status"].__setitem__("actual_K139_K168_common_domain_identity_proved", True)),
        ("invent forms", lambda d: d["native_interface_status"].__setitem__("actual_parity_compression_forms_identified", True)),
        ("invent floors", lambda d: d["native_interface_status"].__setitem__("actual_parity_floors_identified", True)),
        ("invent tails", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("wrong routing", lambda d: d.__setitem__("classification", "PHYSICAL")),
        ("wrong direction", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("erase floor ceiling", lambda d: d.__setitem__("claim_ceiling", d["claim_ceiling"].replace("m_n=min", "m_n unknown"))),
        ("erase scalar warning", lambda d: d.__setitem__("claim_ceiling", d["claim_ceiling"].replace("not a scalar three-channel model", "is a scalar model"))),
        ("promote ceiling", lambda d: d.__setitem__("claim_ceiling", "native K152 floor proved")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    baseline = exact_checks(data)
    manifest_failures = failures(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K646 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    hostile = hostile_checks(data) if "--selftest" in sys.argv else []
    for name, ok in hostile:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    if hostile:
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
    return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

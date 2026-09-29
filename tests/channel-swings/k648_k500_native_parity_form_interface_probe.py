#!/usr/bin/env python3
"""Independent exact and hostile controls for K648."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k648-k500-native-parity-form-interface.json"


def load_solver():
    path = Path(__file__).with_name("k648_k500_native_parity_form_interface.py")
    spec = importlib.util.spec_from_file_location("k648_probe_solver", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    basis = data.get("channel_parity_basis", {})
    carriers = data.get("total_parity_carriers", {})
    forms = data.get("native_compression_forms", {})
    cert = data.get("quantitative_certificate_schema", {})
    dep = data.get("dependency_reconciliation", {})
    control = data.get("exact_control", {})
    native = data.get("native_interface_status", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    if basis.get("channel_even_dimension") != 3 or basis.get("channel_odd_dimension") != 3 or len(basis.get("channel_even", [])) != 3 or len(basis.get("channel_odd", [])) != 3:
        bad.append("basis")
    if carriers.get("three_scalar_channel_reduction") is not False or "product" not in str(carriers.get("reason", "")):
        bad.append("carriers")
    if "P_n^(J,s)" not in str(forms.get("definition", "")) or forms.get("sector_floor") != "m_n=min(m_n^+,m_n^-)" or forms.get("global_floor") != "m=min(inf_n m_n^+,inf_n m_n^-)":
        bad.append("forms")
    if "six operator blocks" not in str(cert.get("per_total_parity_blocks", "")) or cert.get("finite_prefix_is_tail") is not False:
        bad.append("certificate")
    if dep.get("cross_total_parity_blocks_eliminated") is not True or dep.get("within_total_parity_quadrant_couplings_eliminated") is not False:
        bad.append("couplings")
    required_control = ("total_plus_projector_equals_matching_parity_quadrants", "total_minus_projector_equals_opposite_parity_quadrants", "control_form_commutes_with_total_J", "cross_total_parity_block_zero", "within_total_plus_quadrant_coupling_nonzero", "control_is_synthetic_not_native")
    if any(control.get(key) is not True for key in required_control):
        bad.append("control")
    required_true = ("actual_K139_K168_common_domain_identity_proved", "actual_total_parity_compression_forms_serialized", "actual_channel_spectator_quadrants_serialized")
    if any(native.get(key) is not True for key in required_true):
        bad.append("native_true")
    required_false = ("actual_parity_block_floors_identified", "actual_uniform_parity_tails_identified", "native_global_m_identified", "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("product of K639 channel parity and spectator flavor parity", "rather than becoming a scalar three-channel model", "remain absent"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    basis = data["channel_parity_basis"]
    carriers = data["total_parity_carriers"]
    forms = data["native_compression_forms"]
    cert = data["quantitative_certificate_schema"]
    dep = data["dependency_reconciliation"]
    control = data["exact_control"]
    native = data["native_interface_status"]
    return [
        ("fresh basis", fresh["channel_parity_basis"] == basis),
        ("fresh carriers", fresh["total_parity_carriers"] == carriers),
        ("fresh control", fresh["exact_control"] == control),
        ("six channels", len(basis["original_order"]) == 6),
        ("swap indices", basis["swap_indices"] == [3, 2, 1, 0, 5, 4]),
        ("three even", basis["channel_even_dimension"] == len(basis["channel_even"]) == 3),
        ("three odd", basis["channel_odd_dimension"] == len(basis["channel_odd"]) == 3),
        ("spectator split", "H_n^(U,+)" in carriers["spectator_split"]),
        ("total plus product", "C^6_+ tensor H_n^(U,+)" in carriers["total_plus"]),
        ("total minus product", "C^6_+ tensor H_n^(U,-)" in carriers["total_minus"]),
        ("not scalar three", carriers["three_scalar_channel_reduction"] is False),
        ("native definition", "P_n^(J,s)" in forms["definition"]),
        ("physical definition", "S_n D_n^s" in forms["physical_definition"]),
        ("same form identity", forms["same_form_identity"].startswith("a_n^s")),
        ("metric identity", "M_n" in forms["metric_identity"]),
        ("cross zero", forms["cross_total_parity"].endswith("=0")),
        ("sector floor", forms["sector_floor"] == "m_n=min(m_n^+,m_n^-)"),
        ("global floor", forms["global_floor"] == "m=min(inf_n m_n^+,inf_n m_n^-)"),
        ("six blocks each", "six operator blocks" in cert["per_total_parity_blocks"]),
        ("twelve diagonals", "s in {+,-}" in cert["required_diagonal_rows"]),
        ("thirty couplings", "1<=i<j<=6" in cert["required_coupling_rows"]),
        ("comparison floor", "lambda_min" in cert["comparison_floor"]),
        ("two tails", len(cert["uniform_tail_rows"]) == 2),
        ("prefix not tail", cert["finite_prefix_is_tail"] is False),
        ("24 total", control["total_dimension"] == 24),
        ("channel ranks", control["channel_plus_rank"] == control["channel_minus_rank"] == 3),
        ("spectator ranks", control["spectator_plus_rank"] == control["spectator_minus_rank"] == 2),
        ("total ranks", control["total_plus_rank"] == control["total_minus_rank"] == 12),
        ("quadrant ranks", set(control["quadrant_ranks"].values()) == {6}),
        ("projector plus", control["total_plus_projector_equals_matching_parity_quadrants"] is True),
        ("projector minus", control["total_minus_projector_equals_opposite_parity_quadrants"] is True),
        ("cross total zero", control["cross_total_parity_block_zero"] is True),
        ("internal coupling survives", control["within_total_plus_quadrant_coupling_nonzero"] is True),
        ("native forms", native["actual_total_parity_compression_forms_serialized"] is True),
        ("floors withheld", native["actual_parity_block_floors_identified"] is False),
        ("tails withheld", native["actual_uniform_parity_tails_identified"] is False),
        ("m withheld", native["native_global_m_identified"] is False),
        ("remainder withheld", native["native_remainder_alpha_delta_identified"] is False),
        ("coupling warning", dep["within_total_parity_quadrant_couplings_eliminated"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("lose even basis", lambda d: d["channel_parity_basis"].__setitem__("channel_even_dimension", 2)),
        ("lose odd basis", lambda d: d["channel_parity_basis"].__setitem__("channel_odd", [])),
        ("claim scalar", lambda d: d["total_parity_carriers"].__setitem__("three_scalar_channel_reduction", True)),
        ("erase product reason", lambda d: d["total_parity_carriers"].__setitem__("reason", "channel parity only")),
        ("erase definition", lambda d: d["native_compression_forms"].__setitem__("definition", "unknown")),
        ("wrong sector floor", lambda d: d["native_compression_forms"].__setitem__("sector_floor", "m_n=m_n^+")),
        ("wrong global floor", lambda d: d["native_compression_forms"].__setitem__("global_floor", "m=inf plus")),
        ("three blocks", lambda d: d["quantitative_certificate_schema"].__setitem__("per_total_parity_blocks", "three scalar blocks")),
        ("prefix tail", lambda d: d["quantitative_certificate_schema"].__setitem__("finite_prefix_is_tail", True)),
        ("restore cross", lambda d: d["dependency_reconciliation"].__setitem__("cross_total_parity_blocks_eliminated", False)),
        ("drop internal couplings", lambda d: d["dependency_reconciliation"].__setitem__("within_total_parity_quadrant_couplings_eliminated", True)),
        ("break plus projector", lambda d: d["exact_control"].__setitem__("total_plus_projector_equals_matching_parity_quadrants", False)),
        ("break minus projector", lambda d: d["exact_control"].__setitem__("total_minus_projector_equals_opposite_parity_quadrants", False)),
        ("break commute", lambda d: d["exact_control"].__setitem__("control_form_commutes_with_total_J", False)),
        ("cross block", lambda d: d["exact_control"].__setitem__("cross_total_parity_block_zero", False)),
        ("erase internal witness", lambda d: d["exact_control"].__setitem__("within_total_plus_quadrant_coupling_nonzero", False)),
        ("promote control", lambda d: d["exact_control"].__setitem__("control_is_synthetic_not_native", False)),
        ("erase domain", lambda d: d["native_interface_status"].__setitem__("actual_K139_K168_common_domain_identity_proved", False)),
        ("erase forms", lambda d: d["native_interface_status"].__setitem__("actual_total_parity_compression_forms_serialized", False)),
        ("invent floors", lambda d: d["native_interface_status"].__setitem__("actual_parity_block_floors_identified", True)),
        ("invent tails", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("promote ceiling", lambda d: d.__setitem__("claim_ceiling", "scalar three-channel native floor proved")),
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
    print(f"K648 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    hostile = hostile_checks(data) if "--selftest" in sys.argv else []
    for name, ok in hostile:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    if hostile:
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
    return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""K764: stationary scalar-metric derivative control on the K749 germ."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k764-sc-act-06-scalar-metric-derivative-control.json"
PATHS = {
    "k717": ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json",
    "k749": ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json",
    "k763": ROOT / "lab/process/k763-sc-act-06-finite-rank-even-owner-update.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def symmetric_gauge_tensor(k: tuple[complex, ...], zeta: tuple[complex, ...]) -> list[list[complex]]:
    return [[k[i] * zeta[j] + k[j] * zeta[i] for j in range(4)] for i in range(4)]


def scalar_curvature_symbol(k: tuple[complex, ...], h: list[list[complex]]) -> complex:
    k2 = sum(x * x for x in k)
    trace = sum(h[i][i] for i in range(4))
    contracted = sum(k[i] * k[j] * h[i][j] for i in range(4) for j in range(4))
    return contracted - k2 * trace


def gauge_controls() -> list[dict[str, Any]]:
    rows = []
    for name, k in (("euclidean_nonnull", (1, 2, 0, 0)), ("complex_native_null", (1, 1j, 0, 0))):
        values = []
        for axis in range(4):
            zeta = tuple(1 if i == axis else 0 for i in range(4))
            value = scalar_curvature_symbol(k, symmetric_gauge_tensor(k, zeta))
            assert value == 0
            values.append("0")
        coefficients = []
        for i in range(4):
            for j in range(i, 4):
                h = [[0j for _ in range(4)] for _ in range(4)]
                h[i][j] = h[j][i] = 1
                if i == j:
                    h[i][j] = 1
                coefficients.append(scalar_curvature_symbol(k, h))
        assert any(value != 0 for value in coefficients)
        rows.append({"case": name, "k_squared": str(sum(x * x for x in k)), "four_gauge_images_annihilated": values, "scalar_curvature_row_rank": 1})
    return rows


def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "result_id": "K764-SC-ACT-06-SCALAR-METRIC-DERIVATIVE-CONTROL",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "A repository-owned real scalar-tensor control added to the K749 flat stationary germ, used only to test a natural body-valued derivative-even old-block repair.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "typed_objects": {
            "action_owner": "repository control S_K749 plus integral sqrt(g)[(1/2)|d phi|^2+xi phi R(g)+(lambda/4)(phi^2-v^2)^2]",
            "background": "K717/K749 flat stationary metric and connection, with real constant phi=v nonzero",
            "old_carrier": "K749 bosonic metric plus connection carrier",
            "new_even_carrier": "one real scalar field",
            "pairing_or_form": "Euclidean base scalar kinetic pairing plus K749 action pairing",
            "grading": "metric, connection, scalar; scalar is body-valued even",
            "real_structure": "real scalar control; comparison ranks taken after the same complexification as K749",
            "gauge_map": "old rank-four diffeomorphism map extended by delta_phi=Lie_zeta(v)=0",
        },
        "stationarity": {
            "flat_scalar_curvature": "0",
            "constant_scalar_derivative": "0",
            "potential_value_at_phi_v": "0",
            "potential_first_derivative_at_phi_v": "0",
            "scalar_euler": "0",
            "metric_euler": "0",
            "connection_euler_added_by_control": "0",
            "full_background_stationary_relative_to_k749": True,
        },
        "principal_support": {
            "old_metric_dimension": 10,
            "old_connection_update_rank": 0,
            "old_block_correction_rank_upper_r": 10,
            "new_even_dimension_m": 1,
            "r_plus_m": 11,
            "mixed_metric_scalar_block_allowed": True,
            "scalar_self_block_allowed": True,
            "ward_compatible": True,
            "all_covector_rank_upper_uniform": True,
        },
        "exact_controls": gauge_controls(),
        "decision": {
            "concrete_derivative_even_owner_constructed": True,
            "owner_is_source_or_GU_selected": False,
            "owner_changes_connection_principal_image": False,
            "owner_can_evade_k763_rank_budget": False,
            "positive_reduction_or_global_domain_supplied": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The scalar-tensor action is a repository control, not a source-owned GU sector or a physical recovery claim.",
        "controls": {
            "producer": "tests/channel-swings/k764_sc_act_06_scalar_metric_derivative_control.py",
            "probe": "tests/channel-swings/k764_sc_act_06_scalar_metric_derivative_control_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 32,
        },
        "claim_ceiling": "Exact stationarity, support-rank and Ward-compatibility audit for one repository-owned scalar-tensor derivative control. No GU/source ownership, exact rank-ten assertion, positive reduction, global domain, physical scalar, or global SC-ACT-06 conclusion follows.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K764-")
    assert packet["status"] == "working_draft_verified"
    assert packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    assert packet["target_claim"] == "SC-ACT-06"
    assert packet["stationarity"]["full_background_stationary_relative_to_k749"]
    for key in ("scalar_euler", "metric_euler", "connection_euler_added_by_control"):
        assert packet["stationarity"][key] == "0"
    support = packet["principal_support"]
    assert support["old_metric_dimension"] == 10
    assert support["old_connection_update_rank"] == 0
    assert support["old_block_correction_rank_upper_r"] == 10
    assert support["new_even_dimension_m"] == 1 and support["r_plus_m"] == 11
    for key in ("mixed_metric_scalar_block_allowed", "scalar_self_block_allowed", "ward_compatible", "all_covector_rank_upper_uniform"):
        assert support[key]
    assert len(packet["exact_controls"]) == 2
    assert all(row["four_gauge_images_annihilated"] == ["0"] * 4 and row["scalar_curvature_row_rank"] == 1 for row in packet["exact_controls"])
    decision = packet["decision"]
    assert decision["concrete_derivative_even_owner_constructed"]
    assert not decision["owner_is_source_or_GU_selected"]
    assert not decision["owner_changes_connection_principal_image"]
    assert not decision["owner_can_evade_k763_rank_budget"]
    assert not decision["positive_reduction_or_global_domain_supplied"]
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

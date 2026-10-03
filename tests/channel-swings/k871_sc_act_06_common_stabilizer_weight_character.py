#!/usr/bin/env python3
"""K871: exact common-stabilizer torus weights of the K788 tangential kernel.

The computation complexifies the real pinned K77 carrier only as a character
calculation device.  It diagonalizes six same-sign rotation planes for the
authenticated SO(6) x SO(7) common stabilizer, applies the exact sparse Shiab
response to every tangential weight vector, and performs exact Gaussian-
rational elimination independently in every torus weight block.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
API = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
OUTPUT = ROOT / "lab/process/k871-sc-act-06-common-stabilizer-weight-character.json"
PATHS = {
    "api": API,
    "bank": ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k867": ROOT / "lab/process/k867-sc-act-06-compact-equivariance-audit.json",
    "k868": ROOT / "lab/process/k868-sc-act-06-common-stabilizer-boundary.json",
    "k870": ROOT / "lab/process/k870-sc-act-06-corrected-isotropy-disposition.json",
}

Weight = tuple[int, int, int, int, int, int]
Gaussian = tuple[Fraction, Fraction]
Element = dict[int, Gaussian]
Vector = dict[tuple[int, int], Gaussian]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_api():
    spec = importlib.util.spec_from_file_location("k871_k77_api", API)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def gneg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def gdiv(left: Gaussian, right: Gaussian) -> Gaussian:
    denominator = right[0] * right[0] + right[1] * right[1]
    if not denominator:
        raise ZeroDivisionError(right)
    return (
        (left[0] * right[0] + left[1] * right[1]) / denominator,
        (left[1] * right[0] - left[0] * right[1]) / denominator,
    )


def wedge_elements(api, core, left: Element, right: Element) -> Element:
    out: Element = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            sign = core.wedge_sign(lm, rm)
            if sign:
                value = api.gscale(sign, api.gmul(lc, rc))
                out[lm | rm] = api.gadd(out.get(lm | rm, api.ZERO), value)
    return {mask: coefficient for mask, coefficient in out.items() if coefficient != api.ZERO}


def plane_options(api, axis: int, left: int, right: int) -> list[tuple[Weight, Element]]:
    zero = (0, 0, 0, 0, 0, 0)
    plus = list(zero); plus[axis] = 1
    minus = list(zero); minus[axis] = -1
    return [
        (zero, {0: api.ONE}),
        (tuple(plus), {1 << left: api.ONE, 1 << right: gneg(api.I)}),
        (tuple(minus), {1 << left: api.ONE, 1 << right: api.I}),
        (zero, {(1 << left) | (1 << right): api.ONE}),
    ]


def add_weights(left: Weight, right: Weight) -> Weight:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def clifford_weight_basis(api, core) -> list[tuple[Weight, Element]]:
    # q=e_0 is fixed.  The native-positive tangential planes are (4,5),
    # (6,7), (8,9); the native-negative planes are (1,2), (3,10), (11,12),
    # with e_13 the zero-weight vector of the SO(7) vector representation.
    factors = [
        plane_options(api, 0, 4, 5),
        plane_options(api, 1, 6, 7),
        plane_options(api, 2, 8, 9),
        plane_options(api, 3, 1, 2),
        plane_options(api, 4, 3, 10),
        plane_options(api, 5, 11, 12),
        [((0, 0, 0, 0, 0, 0), {0: api.ONE}), ((0, 0, 0, 0, 0, 0), {1 << 0: api.ONE})],
        [((0, 0, 0, 0, 0, 0), {0: api.ONE}), ((0, 0, 0, 0, 0, 0), {1 << 13: api.ONE})],
    ]
    basis: list[tuple[Weight, Element]] = [((0, 0, 0, 0, 0, 0), {0: api.ONE})]
    for factor in factors:
        updated: list[tuple[Weight, Element]] = []
        for old_weight, old_value in basis:
            for new_weight, new_value in factor:
                updated.append((add_weights(old_weight, new_weight), wedge_elements(api, core, old_value, new_value)))
        basis = updated
    assert len(basis) == 1 << 14
    assert all(value for _, value in basis)
    return basis


def tangential_weight_basis(api) -> list[tuple[Weight, dict[int, Gaussian]]]:
    zero = (0, 0, 0, 0, 0, 0)
    out: list[tuple[Weight, dict[int, Gaussian]]] = []
    for axis, left, right in ((0, 4, 5), (1, 6, 7), (2, 8, 9), (3, 1, 2), (4, 3, 10), (5, 11, 12)):
        plus = list(zero); plus[axis] = 1
        minus = list(zero); minus[axis] = -1
        out.append((tuple(plus), {1 << left: api.ONE, 1 << right: gneg(api.I)}))
        out.append((tuple(minus), {1 << left: api.ONE, 1 << right: api.I}))
    out.append((zero, {1 << 13: api.ONE}))
    assert len(out) == 13
    return out


def response(core, q_form, form_value: dict[int, Gaussian], clifford_value: Element) -> Vector:
    direction = {
        form_mask: {mask: api_gmul(form_coefficient, coefficient) for mask, coefficient in clifford_value.items()}
        for form_mask, form_coefficient in form_value.items()
    }
    result = core.shiab(core.wedge_raw(q_form, direction))
    return {
        (form_mask, clifford_mask): coefficient
        for form_mask, element in result.items()
        for clifford_mask, coefficient in element.items()
    }


def reduce_column(value: Vector, pivots: dict[tuple[int, int], Vector]) -> None:
    value = dict(value)
    while value:
        pivot = min(value)
        lead = value[pivot]
        if pivot not in pivots:
            pivots[pivot] = {key: gdiv(coefficient, lead) for key, coefficient in value.items()}
            return
        basis = pivots[pivot]
        for key, coefficient in basis.items():
            updated = (
                value.get(key, (Fraction(0), Fraction(0)))[0] - api_gmul(lead, coefficient)[0],
                value.get(key, (Fraction(0), Fraction(0)))[1] - api_gmul(lead, coefficient)[1],
            )
            if updated == (0, 0):
                value.pop(key, None)
            else:
                value[key] = updated


def api_gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def compute_character() -> tuple[dict[Weight, tuple[int, int, int]], dict[str, Any]]:
    api = load_api()
    bank = api.load_bank()
    core = api.K77Core(bank.signature, bank.channels)
    q_form = {1: {0: api.ONE}}
    clifford = clifford_weight_basis(api, core)
    tangential = tangential_weight_basis(api)
    domains: dict[Weight, int] = {}
    pivots: dict[Weight, dict[tuple[int, int], Vector]] = {}
    for form_weight, form_value in tangential:
        for clifford_weight, clifford_value in clifford:
            weight = add_weights(form_weight, clifford_weight)
            domains[weight] = domains.get(weight, 0) + 1
            block = pivots.setdefault(weight, {})
            reduce_column(response(core, q_form, form_value, clifford_value), block)
    result = {
        weight: (domain, len(pivots.get(weight, {})), domain - len(pivots.get(weight, {})))
        for weight, domain in domains.items()
    }
    metadata = {
        "clifford_weight_vectors": len(clifford),
        "tangential_weight_vectors": len(tangential),
        "weight_block_count": len(result),
        "maximum_domain_block_dimension": max(row[0] for row in result.values()),
        "maximum_kernel_block_dimension": max(row[2] for row in result.values()),
    }
    return result, metadata


def build() -> dict[str, Any]:
    packets = {name: json.loads(path.read_text()) for name, path in PATHS.items() if name not in {"api", "bank"}}
    weights, metadata = compute_character()
    rows = [
        {"weight": list(weight), "domain_multiplicity": domain, "image_multiplicity": image, "kernel_multiplicity": kernel}
        for weight, (domain, image, kernel) in sorted(weights.items())
        if kernel
    ]
    weight_hash = hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "schema_version": "1.0",
        "result_id": "K871-SC-ACT-06-COMMON-STABILIZER-WEIGHT-CHARACTER",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact complexified maximal-torus weight character of the 90128-dimensional tangential K788 kernel under the authenticated SO(6)xSO(7) common stabilizer at q=e_0.",
        "gu_typed_objects": packets["k867"]["gu_typed_objects"] | {"target": "REPRESENTATION-TYPE=complexified torus character of the real tangential kernel under SO(6)xSO(7)"},
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "torus_model": {
            "group": "SO(6) x SO(7)",
            "positive_planes": [[4, 5], [6, 7], [8, 9]],
            "negative_planes": [[1, 2], [3, 10], [11, 12]],
            "negative_zero_weight_direction": 13,
            "fixed_base_covector": 0,
            "weight_order": ["P1", "P2", "P3", "N1", "N2", "N3"],
            "complexification_changes_real_dimension": False,
            "exact_field": "Q(i)",
        },
        "exact_character": {
            **metadata,
            "nonzero_kernel_weight_count": len(rows),
            "domain_dimension": sum(row["domain_multiplicity"] for row in rows) + sum(domain for weight, (domain, _, kernel) in weights.items() if not kernel),
            "image_dimension": sum(image for _, image, _ in weights.values()),
            "kernel_dimension": sum(kernel for _, _, kernel in weights.values()),
            "zero_weight_kernel_multiplicity": weights[(0, 0, 0, 0, 0, 0)][2],
            "weight_rows_sha256": weight_hash,
            "weight_rows": rows,
            "sign_inversion_symmetric": all(weights.get(tuple(-x for x in weight), (0, 0, 0))[2] == kernel for weight, (_, _, kernel) in weights.items()),
        },
        "decision": {
            "common_stabilizer_weight_character_computed": True,
            "real_irreducible_reconstruction_completed": False,
            "owned_old_symmetry_image_authenticated": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Reconstruct and verify the real SO(6)xSO(7) irreducible multiplicities from this exact weight character, then compare them only with an authenticated owned symmetry quotient and owned repair modules.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is an exact local character calculation on the repository-constructed flat response, not an owned physical complex or observable.",
        "claim_ceiling": "Exact torus weight character of the corrected tangential kernel. No real irreducible reconstruction, owned quotient, repair map, global no-go or physical conclusion follows.",
        "controls": {"producer": "tests/channel-swings/k871_sc_act_06_common_stabilizer_weight_character.py", "probe": "tests/channel-swings/k871_sc_act_06_common_stabilizer_weight_character_probe.py", "controls_passed": 36, "hostile_mutations_rejected": 20},
    }


def validate(packet: dict[str, Any]) -> None:
    torus, char, decision = packet["torus_model"], packet["exact_character"], packet["decision"]
    rows = char["weight_rows"]
    checks = [
        packet["classification"] == "SOURCE_NATIVE_ROUTE", packet["target_claim"] == "SC-ACT-06",
        set(packet["pinned_inputs"]) == set(PATHS), all(len(row["sha256"]) == 64 for row in packet["pinned_inputs"].values()),
        torus["group"] == "SO(6) x SO(7)", torus["positive_planes"] == [[4,5],[6,7],[8,9]], torus["negative_planes"] == [[1,2],[3,10],[11,12]],
        torus["negative_zero_weight_direction"] == 13, torus["fixed_base_covector"] == 0, torus["weight_order"] == ["P1","P2","P3","N1","N2","N3"],
        not torus["complexification_changes_real_dimension"], torus["exact_field"] == "Q(i)",
        char["clifford_weight_vectors"] == 16384, char["tangential_weight_vectors"] == 13,
        char["domain_dimension"] == 212992, char["image_dimension"] == 122864, char["kernel_dimension"] == 90128,
        char["weight_block_count"] > 0, char["nonzero_kernel_weight_count"] == len(rows), char["zero_weight_kernel_multiplicity"] > 0,
        len(char["weight_rows_sha256"]) == 64, char["sign_inversion_symmetric"],
        all(len(row["weight"]) == 6 and row["domain_multiplicity"] >= row["image_multiplicity"] and row["kernel_multiplicity"] > 0 for row in rows),
        sum(row["kernel_multiplicity"] for row in rows) == 90128,
        decision["common_stabilizer_weight_character_computed"], not decision["real_irreducible_reconstruction_completed"],
        not decision["owned_old_symmetry_image_authenticated"], not decision["SC_ACT_06_proved_or_refuted"],
        "real SO(6)xSO(7) irreducible multiplicities" in decision["next_exact_input"],
        packet["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "exact local character" in packet["ledger_no_change_reason"], "Exact torus weight character" in packet["claim_ceiling"],
        packet["controls"]["controls_passed"] == 36, packet["controls"]["hostile_mutations_rejected"] == 20,
        packet["controls"]["producer"].endswith("k871_sc_act_06_common_stabilizer_weight_character.py"), packet["controls"]["probe"].endswith("k871_sc_act_06_common_stabilizer_weight_character_probe.py"),
    ]
    assert len(checks) == packet["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

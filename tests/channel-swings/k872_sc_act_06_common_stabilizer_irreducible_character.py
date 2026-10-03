#!/usr/bin/env python3
"""K872: reconstruct the real SO(6)xSO(7) kernel character from K871."""
from __future__ import annotations

import argparse
import functools
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k872-sc-act-06-common-stabilizer-irreducible-character.json"
PATHS = {
    "k865": ROOT / "lab/process/k865-sc-act-06-isotypic-repair-criterion.json",
    "k868": ROOT / "lab/process/k868-sc-act-06-common-stabilizer-boundary.json",
    "k870": ROOT / "lab/process/k870-sc-act-06-corrected-isotropy-disposition.json",
    "k871": ROOT / "lab/process/k871-sc-act-06-common-stabilizer-weight-character.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def permutation_sign(perm: tuple[int, ...]) -> int:
    return -1 if sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1


PERMS = list(itertools.permutations(range(3)))
WEYL_B3 = [
    (perm, signs, permutation_sign(perm) * signs[0] * signs[1] * signs[2])
    for perm in PERMS for signs in itertools.product((-1, 1), repeat=3)
]
WEYL_D3 = [row for row in WEYL_B3 if row[1][0] * row[1][1] * row[1][2] == 1]


def weyl_action(value, element):
    perm, signs, _ = element
    return tuple(signs[i] * value[perm[i]] for i in range(3))


def simple_coordinates(kind: str, value):
    x1, x2, x3 = value
    if kind == "B3":
        return x1, x1 + x2, x1 + x2 + x3
    return x1, (x1 + x2 - x3) / 2, (x1 + x2 + x3) / 2


def positive_roots(kind: str):
    roots = []
    for i in range(3):
        for j in range(i + 1, 3):
            for sign in (-1, 1):
                root = [0, 0, 0]; root[i] = 1; root[j] = sign
                roots.append(tuple(root))
    if kind == "B3":
        for i in range(3):
            root = [0, 0, 0]; root[i] = 1
            roots.append(tuple(root))
    return roots


SIMPLE_ROOTS = {
    kind: [tuple(int(item) for item in simple_coordinates(kind, tuple(Fraction(x) for x in root))) for root in positive_roots(kind)]
    for kind in ("D3", "B3")
}


@functools.lru_cache(None)
def kostant_partition(kind: str, target: tuple[int, int, int]) -> int:
    roots = SIMPLE_ROOTS[kind]

    @functools.lru_cache(None)
    def rec(index: int, remainder: tuple[int, int, int]) -> int:
        if index == len(roots):
            return int(remainder == (0, 0, 0))
        root = roots[index]
        total = 0
        current = remainder
        while all(item >= 0 for item in current):
            total += rec(index + 1, current)
            current = tuple(current[i] - root[i] for i in range(3))
        return total

    return rec(0, target)


def weight_multiplicity(kind: str, highest: tuple[int, int, int], weight: tuple[int, int, int]) -> int:
    rho = (Fraction(5, 2), Fraction(3, 2), Fraction(1, 2)) if kind == "B3" else (Fraction(2), Fraction(1), Fraction(0))
    weyl = WEYL_B3 if kind == "B3" else WEYL_D3
    shifted_highest = tuple(Fraction(highest[i]) + rho[i] for i in range(3))
    shifted_weight = tuple(Fraction(weight[i]) + rho[i] for i in range(3))
    total = 0
    for element in weyl:
        moved = weyl_action(shifted_highest, element)
        delta = tuple(moved[i] - shifted_weight[i] for i in range(3))
        coordinates = simple_coordinates(kind, delta)
        if all(item.denominator == 1 and item >= 0 for item in coordinates):
            total += element[2] * kostant_partition(kind, tuple(int(item) for item in coordinates))
    return total


@functools.lru_cache(None)
def irreducible_character(kind: str, highest: tuple[int, int, int]) -> dict[tuple[int, int, int], int]:
    bound = highest[0]
    out = {}
    for weight in itertools.product(range(-bound, bound + 1), repeat=3):
        multiplicity = weight_multiplicity(kind, highest, weight)
        if multiplicity:
            out[weight] = multiplicity
    return out


def dominant_d3(weight) -> bool:
    return weight[0] >= weight[1] >= abs(weight[2])


def dominant_b3(weight) -> bool:
    return weight[0] >= weight[1] >= weight[2] >= 0


def decompose(weights: dict[tuple[int, ...], int]):
    residual = dict(weights)
    candidates = [weight for weight in weights if dominant_d3(weight[:3]) and dominant_b3(weight[3:])]
    candidates.sort(key=lambda weight: (2 * weight[0] + weight[1] + 3 * weight[3] + 2 * weight[4] + weight[5], weight), reverse=True)
    decomposition = []
    for highest in candidates:
        multiplicity = residual.get(highest, 0)
        assert multiplicity >= 0
        if not multiplicity:
            continue
        d3 = irreducible_character("D3", highest[:3])
        b3 = irreducible_character("B3", highest[3:])
        dimension = sum(d3.values()) * sum(b3.values())
        decomposition.append({"highest_weight": highest, "multiplicity": multiplicity, "complex_dimension": dimension})
        for left_weight, left_multiplicity in d3.items():
            for right_weight, right_multiplicity in b3.items():
                key = left_weight + right_weight
                residual[key] = residual.get(key, 0) - multiplicity * left_multiplicity * right_multiplicity
                assert residual[key] >= 0
    assert not {key: value for key, value in residual.items() if value}
    return decomposition


def realify(decomposition):
    indexed = {row["highest_weight"]: row for row in decomposition}
    rows = []
    for row in decomposition:
        highest = row["highest_weight"]
        if highest[2] < 0:
            continue
        if highest[2] == 0:
            rows.append({
                "so6_highest_weights": [list(highest[:3])], "so7_highest_weight": list(highest[3:]),
                "real_type": "real_tensor_type", "multiplicity": row["multiplicity"],
                "real_irreducible_dimension": row["complex_dimension"],
            })
        else:
            conjugate = highest[:2] + (-highest[2],) + highest[3:]
            partner = indexed[conjugate]
            assert partner["multiplicity"] == row["multiplicity"] and partner["complex_dimension"] == row["complex_dimension"]
            rows.append({
                "so6_highest_weights": [list(highest[:3]), list(conjugate[:3])], "so7_highest_weight": list(highest[3:]),
                "real_type": "complex_conjugate_pair", "multiplicity": row["multiplicity"],
                "real_irreducible_dimension": 2 * row["complex_dimension"],
            })
    return rows


def build() -> dict[str, Any]:
    packets = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    k871 = packets["k871"]
    weights = {tuple(row["weight"]): row["kernel_multiplicity"] for row in k871["exact_character"]["weight_rows"]}
    complex_rows = decompose(weights)
    real_rows = realify(complex_rows)
    reconstruction_hash = hashlib.sha256(json.dumps(real_rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "schema_version": "1.0", "result_id": "K872-SC-ACT-06-COMMON-STABILIZER-IRREDUCIBLE-CHARACTER",
        "created": "2026-10-02", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Exact real irreducible reconstruction of K871's 90128-dimensional tangential-kernel character for SO(6)xSO(7).",
        "gu_typed_objects": k871["gu_typed_objects"] | {"target": "REPRESENTATION-TYPE=real irreducible SO(6)xSO(7) tangential-kernel character"},
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "reconstruction": {
            "root_systems": ["D3=so(6)", "B3=so(7)"], "method": "Kostant multiplicity formula plus descending highest-weight subtraction",
            "weyl_group_orders": {"D3": len(WEYL_D3), "B3": len(WEYL_B3)},
            "complex_highest_weight_row_count": len(complex_rows), "real_irreducible_type_count": len(real_rows),
            "real_tensor_type_count": sum(row["real_type"] == "real_tensor_type" for row in real_rows),
            "complex_pair_type_count": sum(row["real_type"] == "complex_conjugate_pair" for row in real_rows),
            "real_dimension_check": sum(row["multiplicity"] * row["real_irreducible_dimension"] for row in real_rows),
            "maximum_real_multiplicity": max(row["multiplicity"] for row in real_rows),
            "rows_sha256": reconstruction_hash, "real_irreducible_rows": real_rows,
            "exact_weight_reconstruction": True, "negative_residual_multiplicity_encountered": False,
        },
        "decision": {
            "common_stabilizer_weight_character_computed": True, "real_irreducible_multiplicities_computed": True,
            "owned_old_cohomology_module_authenticated": False, "owned_repair_modules_known": False,
            "typewise_capacity_decidable_from_current_inputs": False, "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Authenticate the actual source/action-owned old symmetry image on the pinned flat germ and quotient these 40 real types before comparing any source/action-owned repair-domain and repair-target multiplicities.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The corrected local irreducible character supplies no owned symmetry quotient, repair module, physical state or observable.",
        "claim_ceiling": "Exact real SO(6)xSO(7) irreducible character of the tangential K788 kernel. No owned quotient, repair capacity, intertwiner, global no-go or physical conclusion follows.",
        "controls": {"producer": "tests/channel-swings/k872_sc_act_06_common_stabilizer_irreducible_character.py", "probe": "tests/channel-swings/k872_sc_act_06_common_stabilizer_irreducible_character_probe.py", "controls_passed": 38, "hostile_mutations_rejected": 20},
    }


def validate(packet: dict[str, Any]) -> None:
    r, d = packet["reconstruction"], packet["decision"]
    rows = r["real_irreducible_rows"]
    checks = [
        packet["classification"] == "SOURCE_NATIVE_ROUTE", packet["target_claim"] == "SC-ACT-06",
        set(packet["pinned_inputs"]) == set(PATHS), all(len(row["sha256"]) == 64 for row in packet["pinned_inputs"].values()),
        r["root_systems"] == ["D3=so(6)", "B3=so(7)"], "Kostant" in r["method"],
        r["weyl_group_orders"] == {"D3": 24, "B3": 48}, r["complex_highest_weight_row_count"] == 51,
        r["real_irreducible_type_count"] == len(rows) == 40, r["real_tensor_type_count"] == 29, r["complex_pair_type_count"] == 11,
        r["real_dimension_check"] == 90128, r["maximum_real_multiplicity"] == 8, len(r["rows_sha256"]) == 64,
        r["exact_weight_reconstruction"], not r["negative_residual_multiplicity_encountered"],
        all(row["multiplicity"] > 0 and row["real_irreducible_dimension"] > 0 for row in rows),
        all(len(row["so6_highest_weights"]) == (1 if row["real_type"] == "real_tensor_type" else 2) for row in rows),
        sum(row["multiplicity"] * row["real_irreducible_dimension"] for row in rows) == 90128,
        d["common_stabilizer_weight_character_computed"], d["real_irreducible_multiplicities_computed"],
        not d["owned_old_cohomology_module_authenticated"], not d["owned_repair_modules_known"],
        not d["typewise_capacity_decidable_from_current_inputs"], not d["SC_ACT_06_proved_or_refuted"],
        "40 real types" in d["next_exact_input"],
        packet["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "no owned symmetry quotient" in packet["ledger_no_change_reason"], "Exact real SO(6)xSO(7)" in packet["claim_ceiling"],
        packet["controls"]["controls_passed"] == 38, packet["controls"]["hostile_mutations_rejected"] == 20,
        packet["controls"]["producer"].endswith("k872_sc_act_06_common_stabilizer_irreducible_character.py"),
        packet["controls"]["probe"].endswith("k872_sc_act_06_common_stabilizer_irreducible_character_probe.py"),
        any(row["real_type"] == "complex_conjugate_pair" for row in rows), any(row["real_type"] == "real_tensor_type" for row in rows),
        all(row["so7_highest_weight"][0] >= row["so7_highest_weight"][1] >= row["so7_highest_weight"][2] >= 0 for row in rows),
        all(hw[0] >= hw[1] >= abs(hw[2]) for row in rows for hw in row["so6_highest_weights"]),
        r["real_irreducible_type_count"] == r["real_tensor_type_count"] + r["complex_pair_type_count"],
    ]
    assert len(checks) == packet["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); parser.add_argument("--check", action="store_true"); args = parser.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())

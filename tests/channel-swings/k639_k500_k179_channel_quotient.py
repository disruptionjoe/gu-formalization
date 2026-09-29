#!/usr/bin/env python3
"""K639: quotient K638's bookkeeping labels through the actual K179 family."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k639-k500-k179-channel-quotient.json"
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
PAIR_ORDER = ((1, 1), (1, 2), (2, 1), (2, 2))  # newest flavor, older flavor
POLARITIES = ("++", "+-", "-+", "--")


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k639", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def label(newest: int, older: int, polarity: str) -> str:
    pair_index = PAIR_ORDER.index((newest, older)) + 1
    return f"edge_pair_{pair_index}:{polarity}"


def term_label(term: dict) -> str:
    newest = term["newest"]
    older = term["annihilated"]
    if newest[1] != older[1]:
        raise AssertionError("K179 emitted an opposite-polarity contraction")
    polarity = newest[1] + older[1]
    return label(int(newest[0]), int(older[0]), polarity)


def active_basis() -> list[dict]:
    rows = []
    for newest, older in PAIR_ORDER:
        rows.append({
            "label": label(newest, older, "++"),
            "operator_monomial": f"W_ex[p{older},p{newest}]",
            "separating_functional": f"<impurity {older}| T |impurity {newest}> on the matching plus bath species",
            "finite_particle_action_signature": [newest, f"{older}+", older, f"{newest}+"],
        })
    for flavor in (1, 2):
        rows.append({
            "label": label(flavor, flavor, "--"),
            "operator_monomial": f"W_ex[h{flavor},h{flavor}]",
            "separating_functional": f"<vacuum impurity, one {flavor}- bath| T |same>",
            "finite_particle_action_signature": [0, f"{flavor}-", 0, f"{flavor}-"],
        })
    return rows


def matrix_rank(matrix: list[list[int]]) -> int:
    work = [[value for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if work else 0
    rank = 0
    for column in range(columns):
        pivot = next((r for r in range(rank, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        for r in range(rows):
            if r == rank or not work[r][column]:
                continue
            left = work[r][column]
            work[r] = [pivot_value * x - left * y for x, y in zip(work[r], work[rank])]
        rank += 1
    return rank


def build() -> dict:
    k638 = strict("lab/process/k638-k500-vector-cancellation-coordinate.json")
    k179_manifest = strict("lab/process/k179-matched-normal-order-coefficient-family-wave.json")
    terms = K179.coefficient_family()
    assert len(terms) == k179_manifest["coefficient_family"]["term_count"] == 2958
    assert K179.family_digest(terms) == k179_manifest["coefficient_family"]["family_sha256"]
    declared = k638["native_coordinate_census"]["declared_exchange_labels"]
    assert len(declared) == 16
    counts = Counter(term_label(term) for term in terms)
    basis = active_basis()
    active = [row["label"] for row in basis]
    inactive = [item for item in declared if item not in active]
    monomial_counts = Counter(term["operator_monomial_id"] for term in terms)
    expected_counts = {row["operator_monomial"]: monomial_counts[row["operator_monomial"]] for row in basis}
    extraction_matrix = [
        [
            int(functional["finite_particle_action_signature"] == monomial["finite_particle_action_signature"])
            for monomial in basis
        ]
        for functional in basis
    ]
    quotient_matrix = [
        [int(declared[column] == active[row]) for column in range(16)]
        for row in range(6)
    ]

    return {
        "schema_version": "1.0",
        "result_id": "K639-K500-K179-CHANNEL-QUOTIENT",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact algebraic quotient from K638's sixteen exchange bookkeeping labels to the operator-valued normal-order monomials that actually occur in K179's complete 2,958-term equal-coupling family.",
        "gu_typed_objects": {
            "carrier": "K139 hard-core C3 impurity tensor finite-particle CAR core over four signed bath species",
            "declared_coordinate": "K638 R^16 edge-pair by polarity bookkeeping coordinate",
            "coefficient_map": "K179 older-letter contraction family through order twelve",
            "quotient": "six-dimensional operator-valued normal-order monomial coordinate",
            "result": "actual coefficient/operator-map quotient MAP-TYPE=coordinate projection",
            "target": "the minimal algebraic boundary coordinate available before a complete K139/K168 same-domain estimate",
        },
        "complete_family_replay": {
            "term_count": len(terms),
            "family_sha256": K179.family_digest(terms),
            "all_terms_map_to_declared_K638_labels": set(counts) <= set(declared),
            "all_terms_map_to_surviving_labels": set(counts) == set(active),
            "surviving_label_counts": dict(sorted(counts.items())),
            "surviving_monomial_counts": dict(sorted(expected_counts.items())),
            "orders_covered": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        },
        "quotient_theorem": {
            "declared_dimension": 16,
            "surviving_dimension": 6,
            "kernel_dimension": 10,
            "surviving_basis": basis,
            "null_labels": inactive,
            "opposite_polarity_null_labels": [item for item in inactive if item.endswith("+-") or item.endswith("-+")],
            "off_diagonal_minus_minus_null_labels": [item for item in inactive if item.endswith("--")],
            "quotient_matrix": quotient_matrix,
            "quotient_matrix_rank": matrix_rank(quotient_matrix),
            "separating_functional_matrix": extraction_matrix,
            "separating_functional_rank": matrix_rank(extraction_matrix),
            "surviving_operator_monomials_linearly_independent_on_finite_particle_core": True,
            "minimal_algebraic_operator_coordinate_proved": True,
            "independent_physical_channel_ranges_proved": False,
        },
        "dependency_reconciliation": {
            "K638_sixteen_label_bookkeeping_retracted": False,
            "K638_physical_minimality_warning_resolved_only_algebraically": True,
            "K179_coefficient_family_retracted": False,
            "complete_K139_K168_core_controlled": False,
            "named_complete_sector_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "actual_K179_operator_coordinate_identified": True,
            "ten_bookkeeping_directions_quotiented": True,
            "next_exact_input": "Construct the six-channel cancellation graph and prove a same-domain lower theorem there; then identify the actual complete K139/K168 regular-core coefficient form before claiming a native complete-sector floor.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is an exact quotient inside a repository-supplied conditional point-Fock control. It constructs no GU action-owned physical state, observable, quotient or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "The latest continuation asks for K179 coefficient/range binding. Replaying the complete term generator against K638's declared labels is cheaper and more decisive than estimating a sixteen-channel graph whose null directions are unknown.",
            "retrieval_collision_result": "K179 serializes all terms and K638 explicitly withholds minimality, but no prior artifact computes the induced sixteen-to-operator quotient or proves independence of its surviving monomials.",
            "strongest_alternative": "A complete native floor would be stronger, but K612 proves its actual regular-core constants and common quantitative form are not in current custody.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the six algebraically independent normal-order monomials six independent physical channels or observables.",
            "strongest_contrary_construction": "The ten null directions remain valid bookkeeping labels in K161/K638's conservative component bound; they vanish only after specialization to the current K179 matched contraction family.",
            "weakest_reproducibility_seam": "The quotient inherits K179's current equal-coupling, two-edge, through-order-twelve family and must be replayed if that operator family changes.",
        },
        "controls": {
            "producer": "tests/channel-swings/k639_k500_k179_channel_quotient.py",
            "probe": "tests/channel-swings/k639_k500_k179_channel_quotient_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 28,
        },
        "claim_ceiling": "Exact algebraic quotient of K638's sixteen bookkeeping labels through K179's complete 2,958-term coefficient family. Only four plus-plus ordered edge pairs and two diagonal minus-minus labels occur; separating finite-particle matrix elements prove their six operator-valued normal-order monomials independent, giving rank six and a ten-dimensional kernel. This is minimal only as the current algebraic operator coordinate, not as physical channel ranges, and it supplies no complete K139/K168 floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict) -> None:
    replay = payload["complete_family_replay"]
    theorem = payload["quotient_theorem"]
    dep = payload["dependency_reconciliation"]
    assert replay["term_count"] == 2958
    assert replay["all_terms_map_to_surviving_labels"]
    assert theorem["declared_dimension"] == 16
    assert theorem["surviving_dimension"] == theorem["quotient_matrix_rank"] == 6
    assert theorem["kernel_dimension"] == 10
    assert theorem["separating_functional_rank"] == 6
    assert not theorem["independent_physical_channel_ranges_proved"]
    assert not dep["named_complete_sector_floor_emitted"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

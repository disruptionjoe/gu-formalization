#!/usr/bin/env python3
"""K251: typed ambient compiler and exact depth-five I1B principal growth."""
from __future__ import annotations

import argparse
from collections import Counter, deque
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import re
import runpy


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K250 = ROOT / "lab/process/k250-native-i1b-source-selection-and-all-direction-growth.json"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
OUT = ROOT / "lab/process/k251-native-i1b-depth-five-principal-growth.json"
CHANNELS = ("comm", "symi", "symi")
MAX_DEPTH = 5


def claim_block(text: str, claim_id: str) -> str:
    match = re.search(rf"(?ms)^- id: {re.escape(claim_id)}\n.*?(?=^- id: |\Z)", text)
    assert match is not None
    return match.group(0)


def calculate() -> dict[str, object]:
    register = SOURCE_REGISTER.read_text()
    ledger = LEDGER.read_text()
    assert "polarity: ASSERTS" in claim_block(register, "SC-OP-04")
    assert "polarity: UNCERTAIN" in claim_block(register, "SC-OP-05")
    assert all(f'"id": "{row}"' in ledger for row in ("LT-GR6b", "LT-SM8"))

    with redirect_stdout(StringIO()) as log:
        backend = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full, n = (
        backend["ONE"], backend["ZERO"], backend["FULL"], backend["N"]
    )
    assert n == 14

    def direction(mu: int, blade: int):
        return {1 << mu: {blade: one}}

    raw_support_checks = 0

    def raw_block(label: int, principal: int) -> list[list[Q]]:
        nonlocal raw_support_checks
        out_label = label ^ (1 << principal)
        normal = direction(principal, 0)
        columns: list[list[Q]] = []
        for mu in range(n):
            vector = direction(mu, label ^ (1 << mu))
            image = backend["shiab"](
                backend["wedge_raw"](normal, vector), CHANNELS
            )
            for form_mask, element in image.items():
                assert form_mask.bit_count() == n - 1
                complement = full ^ form_mask
                assert complement and not complement & (complement - 1)
                nu = complement.bit_length() - 1
                for out_blade in element:
                    assert out_blade ^ (1 << nu) == out_label
                    raw_support_checks += 1
            column: list[Q] = []
            for nu in range(n):
                out_blade = out_label ^ (1 << nu)
                value = backend["wedge_raw"](
                    direction(nu, out_blade), image
                ).get(full, {}).get(0, zero)
                assert value[1] == 0
                column.append(value[0])
            columns.append(column)
        return columns

    cache: dict[tuple[int, int], list[list[Q]]] = {}

    def negative_transpose(matrix: list[list[Q]]) -> list[list[Q]]:
        return [[-matrix[j][i] for j in range(n)] for i in range(n)]

    def action_block(label: int, principal: int) -> list[list[Q]]:
        other = label ^ (1 << principal)
        lower = min(label, other)
        key = (lower, principal)
        if key not in cache:
            forward = raw_block(lower, principal)
            reverse = raw_block(other, principal)
            cache[key] = [
                [
                    (forward[mu][nu] - reverse[nu][mu]) / 2
                    for mu in range(n)
                ]
                for nu in range(n)
            ]
        matrix = cache[key]
        return matrix if label == lower else negative_transpose(matrix)

    def multiply(matrix: list[list[Q]], vector: list[Q]) -> list[Q]:
        return [
            sum((matrix[i][j] * vector[j] for j in range(n)), Q())
            for i in range(n)
        ]

    def insert(basis: dict[int, list[Q]], vector: list[Q]) -> list[Q] | None:
        value = list(vector)
        while True:
            pivot = next((i for i, entry in enumerate(value) if entry), None)
            if pivot is None:
                return None
            if pivot not in basis:
                lead = value[pivot]
                value = [entry / lead for entry in value]
                basis[pivot] = value
                return value
            coefficient = value[pivot]
            retained = basis[pivot]
            value = [
                entry - coefficient * retained_entry
                for entry, retained_entry in zip(value, retained)
            ]

    seed = [Q(1), *([Q()] * (n - 1))]
    sector_bases: dict[int, dict[int, list[Q]]] = {3: {0: seed}}
    queue = deque([(3, seed, 0)])
    depth_increments: Counter[int] = Counter()
    while queue:
        label, vector, depth = queue.popleft()
        depth_increments[depth] += 1
        if depth >= MAX_DEPTH:
            continue
        for principal in range(n):
            out_label = label ^ (1 << principal)
            basis = sector_bases.setdefault(out_label, {})
            added = insert(basis, multiply(action_block(label, principal), vector))
            if added is not None:
                queue.append((out_label, added, depth + 1))
            if not basis:
                sector_bases.pop(out_label)

    cumulative_growth: list[int] = []
    total = 0
    for depth in range(MAX_DEPTH + 1):
        total += depth_increments[depth]
        cumulative_growth.append(total)
    rank_distribution = Counter(len(basis) for basis in sector_bases.values())
    assert cumulative_growth == [1, 15, 52, 388, 623, 1705], cumulative_growth
    assert total == sum(len(basis) for basis in sector_bases.values()) == 1705
    assert len(sector_bases) == 755
    assert rank_distribution == Counter({2: 286, 1: 286, 4: 144, 3: 25, 14: 14})
    assert len(cache) == 3532
    assert raw_support_checks == 308092
    assert raw_support_checks > 0

    return {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__CONDITIONAL_SELECTED_LOCAL_SYMBOL_ONLY",
        "input_sha256": {
            "backend": sha256(BACKEND.read_bytes()).hexdigest(),
            "k250": sha256(K250.read_bytes()).hexdigest(),
            "source_register": sha256(SOURCE_REGISTER.read_bytes()).hexdigest(),
            "physics_ledger_v0_263": sha256(LEDGER.read_bytes()).hexdigest(),
        },
        "object": "selected comm/symi/symi I1B formal Euler principal-symbol family on the flat Ricci-flat T=0 zero-fermion germ",
        "ambient_carrier": {
            "space": "T-star tensor Cl(7,7)",
            "basis_rule": "(label,mu,label xor 2^mu), label in [0,2^14), mu in [0,14)",
            "dimension": n * (1 << n),
            "grading_status": "local Clifford-label bookkeeping only; no source-selected barred-field reality or global physical grading",
        },
        "principal_action_compiler": {
            "directions": n,
            "sector_dimension": n,
            "support_rule": "on every block compiled for generation through depth five, direction p maps label lambda only to lambda xor 2^p",
            "euler_block_rule": "one half of the forward ordered 14-by-14 block minus the transpose of the reverse ordered block",
            "compiled_unordered_label_edges_through_depth_four": len(cache),
            "support_terms_checked": raw_support_checks,
        },
        "generated_space": {
            "seed": "o=dx0 tensor gamma1, label 3, leg 0",
            "definition": "span of every word of length at most d in the fourteen selected principal actions applied to o",
            "maximum_word_length": MAX_DEPTH,
            "dimension_growth_d0_through_d5": cumulative_growth,
            "dimension": total,
            "nonzero_label_sectors": len(sector_bases),
            "local_rank_distribution": {
                str(rank): count for rank, count in sorted(rank_distribution.items())
            },
            "minimal_hull_lower_bound": total,
            "minimality_statement": "Every common invariant hull for all fourteen selected principal actions that contains o contains this depth-five generated space.",
        },
        "interpretation": "K250's 15-dimensional first-layer bound is the d=1 entry of a much larger exact Krylov ladder. The full typed ambient and block compiler are now explicit, while complete closure remains uncomputed.",
        "source_routing": "SC-OP-04 ASSERTS and SC-OP-05 UNCERTAIN are preserved; SC-ACT-01/02 ASSERTS, SC-META-53 UNCERTAIN, and LT-GR6b/LT-SM8 NEEDS do not move.",
        "claim_ceiling": "Exact typed ambient carrier, label-toggle block compiler, and 1705-dimensional depth-five lower bound for one conditional selected local principal family. No stabilized or complete all-direction hull, source-selected full fermion operator, lower-order/common domain, quotient, spectrum, positivity, ledger/canon/public change, or K218 cancellation theorem.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = calculate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K251 typed ambient and exact depth-five 1705D principal growth")

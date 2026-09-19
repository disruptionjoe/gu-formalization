#!/usr/bin/env python3
"""K252: restart-safe exact depth-seven I1B principal growth."""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import re
import runpy
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K251 = ROOT / "lab/process/k251-native-i1b-depth-five-principal-growth.json"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
OUT = ROOT / "lab/process/k252-native-i1b-depth-seven-restartable-growth.json"
CHANNELS = ("comm", "symi", "symi")
MAX_DEPTH = 7
CHECKPOINT_SCHEMA = "k252-exact-generation-checkpoint-v1"


def claim_block(text: str, claim_id: str) -> str:
    match = re.search(rf"(?ms)^- id: {re.escape(claim_id)}\n.*?(?=^- id: |\Z)", text)
    assert match is not None
    return match.group(0)


def input_hashes() -> dict[str, str]:
    return {
        "backend": sha256(BACKEND.read_bytes()).hexdigest(),
        "k251": sha256(K251.read_bytes()).hexdigest(),
        "source_register": sha256(SOURCE_REGISTER.read_bytes()).hexdigest(),
        "physics_ledger_v0_263": sha256(LEDGER.read_bytes()).hexdigest(),
    }


def encode_q(value: Q) -> str:
    return f"{value.numerator}/{value.denominator}"


def decode_q(value: str) -> Q:
    numerator, denominator = value.split("/", 1)
    return Q(int(numerator), int(denominator))


def encode_vector(vector: list[Q]) -> list[str]:
    return [encode_q(entry) for entry in vector]


def decode_vector(vector: list[str]) -> list[Q]:
    return [decode_q(entry) for entry in vector]


def checkpoint_payload(
    completed_depth: int,
    growth: list[int],
    sector_bases: dict[int, dict[int, list[Q]]],
    frontier: list[tuple[int, list[Q]]],
    edge_support_checks: dict[tuple[int, int], int],
) -> dict[str, Any]:
    return {
        "schema_version": CHECKPOINT_SCHEMA,
        "input_sha256": input_hashes(),
        "channels": list(CHANNELS),
        "target_maximum_word_length": MAX_DEPTH,
        "completed_depth": completed_depth,
        "cumulative_growth": growth,
        "sector_bases": {
            str(label): {
                str(pivot): encode_vector(vector)
                for pivot, vector in sorted(basis.items())
            }
            for label, basis in sorted(sector_bases.items())
        },
        "frontier": [
            {"label": label, "vector": encode_vector(vector)}
            for label, vector in frontier
        ],
        "edge_support_checks": {
            f"{label}:{principal}": count
            for (label, principal), count in sorted(edge_support_checks.items())
        },
    }


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
    temporary.replace(path)


def load_checkpoint(path: Path) -> tuple[
    int,
    list[int],
    dict[int, dict[int, list[Q]]],
    list[tuple[int, list[Q]]],
    dict[tuple[int, int], int],
]:
    payload = json.loads(path.read_text())
    assert payload["schema_version"] == CHECKPOINT_SCHEMA
    assert payload["input_sha256"] == input_hashes()
    assert payload["channels"] == list(CHANNELS)
    assert payload["target_maximum_word_length"] == MAX_DEPTH
    completed_depth = payload["completed_depth"]
    assert isinstance(completed_depth, int) and 0 <= completed_depth <= MAX_DEPTH
    growth = payload["cumulative_growth"]
    assert len(growth) == completed_depth + 1
    sector_bases = {
        int(label): {
            int(pivot): decode_vector(vector)
            for pivot, vector in basis.items()
        }
        for label, basis in payload["sector_bases"].items()
    }
    frontier = [
        (entry["label"], decode_vector(entry["vector"]))
        for entry in payload["frontier"]
    ]
    edge_support_checks = {
        tuple(map(int, key.split(":"))): count
        for key, count in payload["edge_support_checks"].items()
    }
    assert growth[-1] == sum(len(basis) for basis in sector_bases.values())
    assert len(frontier) == growth[-1] - (growth[-2] if completed_depth else 0)
    return completed_depth, growth, sector_bases, frontier, edge_support_checks


def calculate(
    checkpoint: Path | None = None,
    resume: Path | None = None,
    stop_after_depth: int = MAX_DEPTH,
) -> dict[str, Any]:
    assert 0 <= stop_after_depth <= MAX_DEPTH
    register = SOURCE_REGISTER.read_text()
    ledger = LEDGER.read_text()
    assert "polarity: ASSERTS" in claim_block(register, "SC-OP-04")
    assert "polarity: UNCERTAIN" in claim_block(register, "SC-OP-05")
    assert all(f'"id": "{row}"' in ledger for row in ("LT-GR6b", "LT-SM8"))

    with redirect_stdout(StringIO()) as log:
        backend = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full, n = backend["ONE"], backend["ZERO"], backend["FULL"], backend["N"]
    assert n == 14

    def direction(mu: int, blade: int):
        return {1 << mu: {blade: one}}

    def raw_block(label: int, principal: int) -> tuple[list[list[Q]], int]:
        out_label = label ^ (1 << principal)
        normal = direction(principal, 0)
        columns: list[list[Q]] = []
        checks = 0
        for mu in range(n):
            vector = direction(mu, label ^ (1 << mu))
            image = backend["shiab"](backend["wedge_raw"](normal, vector), CHANNELS)
            for form_mask, element in image.items():
                assert form_mask.bit_count() == n - 1
                complement = full ^ form_mask
                assert complement and not complement & (complement - 1)
                nu = complement.bit_length() - 1
                for out_blade in element:
                    assert out_blade ^ (1 << nu) == out_label
                    checks += 1
            column: list[Q] = []
            for nu in range(n):
                out_blade = out_label ^ (1 << nu)
                value = backend["wedge_raw"](
                    direction(nu, out_blade), image
                ).get(full, {}).get(0, zero)
                assert value[1] == 0
                column.append(value[0])
            columns.append(column)
        return columns, checks

    cache: dict[tuple[int, int], list[list[Q]]] = {}
    if resume is None:
        seed = [Q(1), *([Q()] * (n - 1))]
        completed_depth = 0
        growth = [1]
        sector_bases: dict[int, dict[int, list[Q]]] = {3: {0: seed}}
        frontier: list[tuple[int, list[Q]]] = [(3, seed)]
        edge_support_checks: dict[tuple[int, int], int] = {}
    else:
        completed_depth, growth, sector_bases, frontier, edge_support_checks = load_checkpoint(resume)

    def negative_transpose(matrix: list[list[Q]]) -> list[list[Q]]:
        return [[-matrix[j][i] for j in range(n)] for i in range(n)]

    def action_block(label: int, principal: int) -> list[list[Q]]:
        other = label ^ (1 << principal)
        lower = min(label, other)
        key = (lower, principal)
        if key not in cache:
            forward, forward_checks = raw_block(lower, principal)
            reverse, reverse_checks = raw_block(other, principal)
            checks = forward_checks + reverse_checks
            if key not in edge_support_checks:
                edge_support_checks[key] = checks
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

    for depth in range(completed_depth, stop_after_depth):
        next_frontier: list[tuple[int, list[Q]]] = []
        for label, vector in frontier:
            for principal in range(n):
                out_label = label ^ (1 << principal)
                basis = sector_bases.setdefault(out_label, {})
                added = insert(basis, multiply(action_block(label, principal), vector))
                if added is not None:
                    next_frontier.append((out_label, added))
                if not basis:
                    sector_bases.pop(out_label)
        frontier = next_frontier
        completed_depth = depth + 1
        growth.append(sum(len(basis) for basis in sector_bases.values()))
        if checkpoint is not None:
            write_checkpoint(
                checkpoint,
                checkpoint_payload(
                    completed_depth,
                    growth,
                    sector_bases,
                    frontier,
                    edge_support_checks,
                ),
            )

    rank_distribution = Counter(len(basis) for basis in sector_bases.values())
    complete = completed_depth == MAX_DEPTH
    if complete:
        assert growth == [1, 15, 52, 388, 623, 1705, 6644, 21724], growth
        assert sum(len(basis) for basis in sector_bases.values()) == 21724
        assert len(sector_bases) == 3472
        assert rank_distribution == Counter({6: 1210, 4: 935, 5: 792, 14: 469, 3: 66})
        assert len(edge_support_checks) == 17282
        assert sum(edge_support_checks.values()) == 1503132

    return {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__CONDITIONAL_SELECTED_LOCAL_SYMBOL_ONLY",
        "input_sha256": input_hashes(),
        "object": "selected comm/symi/symi I1B formal Euler principal-symbol family on the flat Ricci-flat T=0 zero-fermion germ",
        "ambient_carrier": {
            "space": "T-star tensor Cl(7,7)",
            "basis_rule": "(label,mu,label xor 2^mu), label in [0,2^14), mu in [0,14)",
            "dimension": n * (1 << n),
            "grading_status": "local Clifford-label bookkeeping only; no source-selected barred-field reality or global physical grading",
        },
        "restart_contract": {
            "schema_version": CHECKPOINT_SCHEMA,
            "state": "completed depth, cumulative dimensions, normalized exact sector bases, exact next frontier, and input-bound edge-support census",
            "input_binding": "backend, K251, source register, physics ledger, channels, and target maximum depth must match exactly",
            "durability": "deterministic JSON written to a same-directory temporary file and atomically replaced after each completed depth",
            "scientific_role": "continuation state only; a checkpoint is not independent evidence and cannot establish closure",
        },
        "principal_action_compiler": {
            "directions": n,
            "sector_dimension": n,
            "support_rule": "on every block compiled for generation through depth seven, direction p maps label lambda only to lambda xor 2^p",
            "euler_block_rule": "one half of the forward ordered 14-by-14 block minus the transpose of the reverse ordered block",
            "compiled_unordered_label_edges_through_depth_six": len(edge_support_checks),
            "support_terms_checked": sum(edge_support_checks.values()),
        },
        "generated_space": {
            "seed": "o=dx0 tensor gamma1, label 3, leg 0",
            "definition": "span of every word of length at most d in the fourteen selected principal actions applied to o",
            "maximum_word_length": completed_depth,
            "complete_target_depth": complete,
            "dimension_growth_d0_through_completed_depth": growth,
            "dimension": growth[-1],
            "nonzero_label_sectors": len(sector_bases),
            "local_rank_distribution": {
                str(rank): count for rank, count in sorted(rank_distribution.items())
            },
            "new_dimensions_at_depth_six_and_seven": growth[6] - growth[5] if completed_depth >= 6 else None,
            "new_dimensions_at_depth_seven": growth[7] - growth[6] if completed_depth >= 7 else None,
            "saturated_local_sectors": rank_distribution.get(n, 0),
            "minimal_hull_lower_bound": growth[-1] if complete else None,
            "minimality_statement": "Every common invariant hull for all fourteen selected principal actions that contains o contains this generated space.",
        },
        "interpretation": "The restart-safe exact engine extends K251's lower-bound ladder by two depths. Rapid nonzero growth at depth seven proves that the certified prefix is not stabilized; complete closure still requires farther exact continuation or a structural reduction.",
        "source_routing": "SC-OP-04 ASSERTS and SC-OP-05 UNCERTAIN are preserved; SC-ACT-01/02 ASSERTS, SC-META-53 UNCERTAIN, and LT-GR6b/LT-SM8 NEEDS do not move.",
        "claim_ceiling": "Exact restart-safe generation and a 21724-dimensional depth-seven lower bound for one conditional selected local principal family. No stabilized or complete all-direction hull, source-selected full fermion operator, lower-order/common domain, quotient, spectrum, positivity, ledger/canon/public change, or K218 cancellation theorem.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--stop-after-depth", type=int, default=MAX_DEPTH)
    parser.add_argument("--summary-json", type=Path)
    args = parser.parse_args()
    result = calculate(args.checkpoint, args.resume, args.stop_after_depth)
    if args.write:
        assert result["generated_space"]["complete_target_depth"]
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    if args.summary_json is not None:
        args.summary_json.write_text(json.dumps(result, sort_keys=True) + "\n")
    status = "complete" if result["generated_space"]["complete_target_depth"] else "checkpointed"
    print(
        f"[PASS] K252 {status} exact principal growth: "
        f"depth={result['generated_space']['maximum_word_length']} "
        f"dimension={result['generated_space']['dimension']}"
    )

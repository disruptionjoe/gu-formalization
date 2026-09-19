#!/usr/bin/env python3
"""K253: exact sparse compiler and closure campaign for the K252 I1B family."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K252 = ROOT / "lab/process/k252-native-i1b-depth-seven-restartable-growth.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
OUT = ROOT / "lab/process/k253-native-i1b-sparse-closure.json"
N = 14
FULL = (1 << N) - 1
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
CHANNELS = ("comm", "symi", "symi")
PRIMES = (1_000_003, 1_000_033)
RATIONAL_DEPTH = 8
CHECKPOINT_SCHEMA = "k253-rational-generation-checkpoint-v1"
G = tuple[int, int]
ZERO: G = (0, 0)
ONE: G = (1, 0)
I: G = (0, 1)


def claim_block(text: str, claim_id: str) -> str:
    match = re.search(rf"(?ms)^- id: {re.escape(claim_id)}\n.*?(?=^- id: |\Z)", text)
    assert match is not None
    return match.group(0)


def input_hashes() -> dict[str, str]:
    return {
        "backend": sha256(BACKEND.read_bytes()).hexdigest(),
        "k252": sha256(K252.read_bytes()).hexdigest(),
        "source_register": sha256(REGISTER.read_bytes()).hexdigest(),
        "physics_ledger_v0_263": sha256(LEDGER.read_bytes()).hexdigest(),
    }


def indices(mask: int):
    return (i for i in range(N) if mask & (1 << i))


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    return -1 if inversions % 2 else 1


def blade_product(left: int, right: int) -> tuple[int, int]:
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    sign = -1 if inversions % 2 else 1
    for i in indices(left & right):
        sign *= ETA[i]
    return left ^ right, sign


def gadd(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]


def gsub(a: G, b: G) -> G:
    return a[0] - b[0], a[1] - b[1]


def gmul(a: G, b: G) -> G:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gscale(value: int, a: G) -> G:
    return value * a[0], value * a[1]


def ghalfscale(value: int, a: G) -> G:
    assert (value * a[0]) % 2 == 0 and (value * a[1]) % 2 == 0
    return value * a[0] // 2, value * a[1] // 2


def singleton_product(left: int, a: G, right: int, b: G) -> tuple[int, G]:
    mask, sign = blade_product(left, right)
    return mask, gscale(sign, gmul(a, b))


def singleton_channel(left: int, a: G, right: int, b: G, channel: str) -> tuple[int, G]:
    mask1, ab = singleton_product(left, a, right, b)
    mask2, ba = singleton_product(right, b, left, a)
    assert mask1 == mask2
    if channel == "comm":
        return mask1, gsub(ab, ba)
    assert channel == "symi"
    return mask1, gmul(I, gadd(ab, ba))


def sparse_raw_block(label: int, principal: int) -> list[list[int]]:
    """Return the original ordered 14 columns without materializing Forms.

    Hodge support leaves only the two omitted indices in the first term.  The
    Phi2 term uses their unique bivector and contributes one output per leg.
    """
    out_label = label ^ (1 << principal)
    columns: list[list[Q]] = []
    for mu in range(N):
        if mu == principal:
            columns.append([0] * N)
            continue
        column = [ZERO] * N
        pair_form = (1 << principal) | (1 << mu)
        complement = FULL ^ pair_form
        blade_in = label ^ (1 << mu)
        star_scale = (
            wedge_sign(1 << principal, 1 << mu)
            * wedge_sign(pair_form, complement)
            * ETA[principal]
            * ETA[mu]
        )

        for phi_index, nu in ((principal, mu), (mu, principal)):
            output_form = complement | (1 << phi_index)
            coefficient = gscale(
                star_scale * wedge_sign(1 << phi_index, complement), ONE
            )
            blade_out, coefficient = singleton_channel(
                1 << phi_index, ONE, blade_in, coefficient, "comm"
            )
            target = out_label ^ (1 << nu)
            assert blade_out == target
            scalar, coefficient = singleton_product(target, ONE, blade_out, coefficient)
            assert scalar == 0
            coefficient = gscale(wedge_sign(1 << nu, output_form), coefficient)
            column[nu] = gadd(column[nu], coefficient)

        lo, hi = sorted((principal, mu))
        pair_blade, phi2 = singleton_product(1 << lo, ONE, 1 << hi, ONE)
        middle_blade, middle = singleton_channel(
            pair_blade,
            phi2,
            blade_in,
            gscale(star_scale * wedge_sign(pair_form, complement), ONE),
            "symi",
        )
        assert middle_blade == label ^ (1 << principal)
        middle = gscale(-1, middle)  # product of the fourteen metric signs
        for nu in range(N):
            blade_out, coefficient = singleton_channel(
                1 << nu, ONE, middle_blade, middle, "symi"
            )
            one_form = 1 << nu
            coefficient = ghalfscale(
                -wedge_sign(one_form, FULL ^ one_form) * ETA[nu],
                coefficient,
            )
            target = out_label ^ (1 << nu)
            assert blade_out == target
            scalar, coefficient = singleton_product(target, ONE, blade_out, coefficient)
            assert scalar == 0
            coefficient = gscale(wedge_sign(one_form, FULL ^ one_form), coefficient)
            column[nu] = gadd(column[nu], coefficient)

        assert all(value[1] == 0 for value in column)
        columns.append([value[0] for value in column])
    return columns


SparseMatrix = list[list[tuple[int, int]]]


class Compiler:
    def __init__(self) -> None:
        self.cache: dict[tuple[int, int], tuple[SparseMatrix, SparseMatrix]] = {}

    def block(self, label: int, principal: int) -> SparseMatrix:
        other = label ^ (1 << principal)
        lower = min(label, other)
        key = lower, principal
        if key not in self.cache:
            forward = sparse_raw_block(lower, principal)
            reverse = sparse_raw_block(other, principal)
            numerators = [
                [forward[mu][nu] - reverse[nu][mu] for mu in range(N)]
                for nu in range(N)
            ]
            assert all(value % 2 == 0 for row in numerators for value in row)
            dense = [[value // 2 for value in row] for row in numerators]
            assert all(isinstance(value, int) for row in dense for value in row)
            direct = [
                [(column, value) for column, value in enumerate(row) if value]
                for row in dense
            ]
            opposite = [
                [(column, -dense[column][row]) for column in range(N) if dense[column][row]]
                for row in range(N)
            ]
            self.cache[key] = direct, opposite
        direct, opposite = self.cache[key]
        return direct if label == lower else opposite


def multiply_mod(matrix: SparseMatrix, vector: list[int], prime: int) -> list[int]:
    return [sum(value * vector[column] for column, value in row) % prime for row in matrix]


def insert_mod(basis: dict[int, list[int]], vector: list[int], prime: int) -> list[int] | None:
    value = list(vector)
    while True:
        pivot = next((i for i, entry in enumerate(value) if entry), None)
        if pivot is None:
            return None
        if pivot not in basis:
            inverse = pow(value[pivot], -1, prime)
            value = [(entry * inverse) % prime for entry in value]
            basis[pivot] = value
            return value
        coefficient = value[pivot]
        retained = basis[pivot]
        value = [(entry - coefficient * old) % prime for entry, old in zip(value, retained)]


def modular_closure(prime: int, compiler: Compiler, reverse: bool = False) -> dict[str, Any]:
    seed = [1] + [0] * (N - 1)
    bases: dict[int, dict[int, list[int]]] = {3: {0: seed}}
    frontier: list[tuple[int, list[int]]] = [(3, seed)]
    growth = [1]
    order = tuple(reversed(range(N))) if reverse else tuple(range(N))
    while frontier:
        next_frontier: list[tuple[int, list[int]]] = []
        for label, vector in reversed(frontier) if reverse else frontier:
            for principal in order:
                target = label ^ (1 << principal)
                basis = bases.setdefault(target, {})
                added = insert_mod(
                    basis, multiply_mod(compiler.block(label, principal), vector, prime), prime
                )
                if added is not None:
                    next_frontier.append((target, added))
                if not basis:
                    bases.pop(target)
        frontier = next_frontier
        growth.append(sum(len(basis) for basis in bases.values()))
        print(
            f"[K253 modular p={prime}] depth={len(growth) - 1} "
            f"dimension={growth[-1]} frontier={len(frontier)} sectors={len(bases)}",
            flush=True,
        )
        assert len(growth) <= 64
    distribution = Counter(len(basis) for basis in bases.values())
    exceptional = {
        str(label): len(bases.get(label, {}))
        for label in range(1 << N)
        if len(bases.get(label, {})) < N
    }
    return {
        "prime": prime,
        "traversal": "reverse" if reverse else "forward",
        "dimension_growth": growth,
        "stabilization_depth": len(growth) - 1,
        "dimension": growth[-1],
        "nonzero_label_sectors": len(bases),
        "local_rank_distribution": {str(k): v for k, v in sorted(distribution.items())},
        "exceptional_label_ranks": exceptional,
        "full_ambient": growth[-1] == N * (1 << N),
    }


def multiply_q(matrix: SparseMatrix, vector: list[Q]) -> list[Q]:
    return [sum((Q(value) * vector[column] for column, value in row), Q()) for row in matrix]


def insert_q(basis: dict[int, list[Q]], vector: list[Q]) -> list[Q] | None:
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
        value = [entry - coefficient * old for entry, old in zip(value, retained)]


def encode_q(value: Q) -> str:
    return f"{value.numerator}/{value.denominator}"


def decode_q(value: str) -> Q:
    numerator, denominator = value.split("/", 1)
    return Q(int(numerator), int(denominator))


def checkpoint_payload(
    depth: int,
    growth: list[int],
    bases: dict[int, dict[int, list[Q]]],
    frontier: list[tuple[int, list[Q]]],
) -> dict[str, Any]:
    return {
        "schema_version": CHECKPOINT_SCHEMA,
        "input_sha256": input_hashes(),
        "channels": list(CHANNELS),
        "target_rational_depth": RATIONAL_DEPTH,
        "completed_depth": depth,
        "growth": growth,
        "bases": {
            str(label): {
                str(pivot): [encode_q(entry) for entry in vector]
                for pivot, vector in sorted(basis.items())
            }
            for label, basis in sorted(bases.items())
        },
        "frontier": [
            {"label": label, "vector": [encode_q(entry) for entry in vector]}
            for label, vector in frontier
        ],
    }


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
    temporary.replace(path)


def load_checkpoint(path: Path):
    payload = json.loads(path.read_text())
    assert payload["schema_version"] == CHECKPOINT_SCHEMA
    assert payload["input_sha256"] == input_hashes()
    assert payload["channels"] == list(CHANNELS)
    assert payload["target_rational_depth"] == RATIONAL_DEPTH
    bases = {
        int(label): {
            int(pivot): [decode_q(entry) for entry in vector]
            for pivot, vector in basis.items()
        }
        for label, basis in payload["bases"].items()
    }
    frontier = [
        (entry["label"], [decode_q(value) for value in entry["vector"]])
        for entry in payload["frontier"]
    ]
    return payload["completed_depth"], payload["growth"], bases, frontier


def rational_generation(
    compiler: Compiler,
    checkpoint: Path | None = None,
    resume: Path | None = None,
    stop_after_depth: int = RATIONAL_DEPTH,
) -> dict[str, Any]:
    if resume is None:
        seed = [Q(1)] + [Q()] * (N - 1)
        depth, growth = 0, [1]
        bases: dict[int, dict[int, list[Q]]] = {3: {0: seed}}
        frontier: list[tuple[int, list[Q]]] = [(3, seed)]
    else:
        depth, growth, bases, frontier = load_checkpoint(resume)
    assert depth <= stop_after_depth <= RATIONAL_DEPTH
    while depth < stop_after_depth:
        next_frontier: list[tuple[int, list[Q]]] = []
        for label, vector in frontier:
            for principal in range(N):
                target = label ^ (1 << principal)
                basis = bases.setdefault(target, {})
                added = insert_q(basis, multiply_q(compiler.block(label, principal), vector))
                if added is not None:
                    next_frontier.append((target, added))
                if not basis:
                    bases.pop(target)
        frontier = next_frontier
        depth += 1
        growth.append(sum(len(basis) for basis in bases.values()))
        if checkpoint is not None:
            write_checkpoint(checkpoint, checkpoint_payload(depth, growth, bases, frontier))
    distribution = Counter(len(basis) for basis in bases.values())
    return {
        "maximum_word_length": depth,
        "dimension_growth": growth,
        "dimension": growth[-1],
        "new_dimensions_at_final_depth": growth[-1] - growth[-2] if depth else 1,
        "nonzero_label_sectors": len(bases),
        "local_rank_distribution": {str(k): v for k, v in sorted(distribution.items())},
        "stabilized": not frontier,
    }


def calculate(checkpoint: Path | None = None, resume: Path | None = None) -> dict[str, Any]:
    register = REGISTER.read_text()
    ledger = LEDGER.read_text()
    assert "polarity: ASSERTS" in claim_block(register, "SC-OP-04")
    assert "polarity: UNCERTAIN" in claim_block(register, "SC-OP-05")
    assert all(f'"id": "{row}"' in ledger for row in ("LT-GR6b", "LT-SM8"))
    compiler = Compiler()
    modular = [modular_closure(prime, compiler, reverse=bool(i)) for i, prime in enumerate(PRIMES)]
    rational = rational_generation(compiler, checkpoint, resume)
    k252_growth = json.loads(K252.read_text())["generated_space"]["dimension_growth_d0_through_completed_depth"]
    assert rational["dimension_growth"][:8] == k252_growth
    modular_agreement = all(item["dimension_growth"] == modular[0]["dimension_growth"] for item in modular[1:])
    full = all(item["full_ambient"] for item in modular)
    return {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__CONDITIONAL_SELECTED_LOCAL_SYMBOL_ONLY",
        "input_sha256": input_hashes(),
        "object": "selected comm/symi/symi I1B formal Euler principal-symbol family on the flat Ricci-flat T=0 zero-fermion germ",
        "ambient_carrier": {
            "space": "T-star tensor Cl(7,7)",
            "dimension": N * (1 << N),
            "grading_status": "local Clifford-label bookkeeping only; no source-selected barred-field reality or global physical grading",
        },
        "sparse_compiler": {
            "derivation": "Hodge support leaves the two omitted indices for the first Shiab term; the Phi2 term uses their unique bivector and one diagonal output family",
            "coefficient_arithmetic": "exact signed Clifford single-blade multiplication over the K77 metric",
            "compiled_unordered_label_edges": len(compiler.cache),
            "matrix_entries_integral": True,
        },
        "modular_closure": {
            "runs": modular,
            "cross_prime_growth_agreement": modular_agreement,
            "characteristic_zero_lower_bound": max(item["dimension"] for item in modular),
            "characteristic_zero_inference": (
                "Full modular rank supplies an integer word minor nonzero modulo each prime and therefore nonzero over Q."
                if full else
                "Non-full modular closure is not used as a characteristic-zero upper bound."
            ),
        },
        "rational_generation": rational,
        "interpretation": (
            "The conditional selected principal family generates the complete typed ambient carrier over Q."
            if full else
            "The modular word span proves a 229359-dimensional characteristic-zero lower bound, while complete characteristic-zero closure remains open within the final seventeen ambient dimensions."
        ),
        "source_routing": "SC-OP-04 ASSERTS and SC-OP-05 UNCERTAIN are preserved; SC-ACT-01/02 ASSERTS, SC-META-53 UNCERTAIN, and LT-GR6b/LT-SM8 NEEDS do not move.",
        "claim_ceiling": "Exact sparse compilation, modular closure evidence, and rational generated-space growth for one conditional selected local principal family. No source-selected full fermion operator, lower-order/common domain, quotient, spectrum, positivity, ledger/canon/public change, or K218 cancellation theorem.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--modular-only", type=int)
    args = parser.parse_args()
    if args.modular_only:
        result = modular_closure(args.modular_only, Compiler())
        print(json.dumps(result, sort_keys=True))
    else:
        result = calculate(args.checkpoint, args.resume)
        if args.write:
            OUT.write_text(json.dumps(result, indent=2) + "\n")
        rational = result["rational_generation"]
        modular = result["modular_closure"]["runs"][0]
        print(
            f"[PASS] K253 sparse closure: modular={modular['dimension']} "
            f"depth={modular['stabilization_depth']} rational={rational['dimension']}"
        )

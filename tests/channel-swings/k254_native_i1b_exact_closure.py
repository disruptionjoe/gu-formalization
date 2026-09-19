#!/usr/bin/env python3
"""K254: repair caller-dependent edge orientation and certify the exact I1B hull."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import pickle
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K253_PRODUCER = ROOT / "tests/channel-swings/k253_native_i1b_sparse_closure.py"
K253_RECORD = ROOT / "lab/process/k253-native-i1b-sparse-closure.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
OUT = ROOT / "lab/process/k254-native-i1b-exact-closure.json"
N = 14
LABEL_COUNT = 1 << N
PRIMES = (1_000_003, 1_000_033)
DEFAULT_COMPILER_CACHE = ROOT / "_local/k254/compiler-cache.pkl"


def load_k253():
    spec = importlib.util.spec_from_file_location("k253_producer", K253_PRODUCER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DeterministicCompiler:
    """K253's sparse formula with endpoint order frozen independently of caller."""

    def __init__(self, k253) -> None:
        self.k253 = k253
        self.cache: dict[tuple[int, int], tuple[Any, Any]] = {}

    def block(self, label: int, principal: int):
        adjacent = label ^ (1 << principal)
        lower = min(label, adjacent)
        upper = lower ^ (1 << principal)
        key = lower, principal
        if key not in self.cache:
            forward = self.k253.sparse_raw_block(lower, principal)
            reverse = self.k253.sparse_raw_block(upper, principal)
            numerators = [
                [forward[mu][nu] - reverse[nu][mu] for mu in range(N)]
                for nu in range(N)
            ]
            assert all(value % 2 == 0 for row in numerators for value in row)
            dense = [[value // 2 for value in row] for row in numerators]
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


def claim_block(text: str, claim_id: str) -> str:
    match = re.search(rf"(?ms)^- id: {re.escape(claim_id)}\n.*?(?=^- id: |\Z)", text)
    assert match is not None
    return match.group(0)


def input_hashes() -> dict[str, str]:
    return {
        "k253_producer": sha256(K253_PRODUCER.read_bytes()).hexdigest(),
        "k253_record": sha256(K253_RECORD.read_bytes()).hexdigest(),
        "source_register": sha256(REGISTER.read_bytes()).hexdigest(),
        "physics_ledger_v0_263": sha256(LEDGER.read_bytes()).hexdigest(),
    }


def local_ranks(bases: dict[int, dict[int, list[int]]]) -> dict[str, Any]:
    distribution = Counter(len(bases.get(label, {})) for label in range(LABEL_COUNT))
    return {
        "dimension": sum(len(basis) for basis in bases.values()),
        "nonzero_label_sectors": len(bases),
        "local_rank_distribution_including_zero": {
            str(k): v for k, v in sorted(distribution.items())
        },
    }


def save_compiler_cache(path: Path | None, compiler) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    with temporary.open("wb") as handle:
        pickle.dump(
            {
                "construction": "deterministic_upper_endpoint_eager_lexicographic_v2",
                "k253_producer_sha256": input_hashes()["k253_producer"],
                "cache_sha256": compiler_cache_digest(compiler.cache),
                "cache": compiler.cache,
            },
            handle,
            protocol=pickle.HIGHEST_PROTOCOL,
        )
    temporary.replace(path)


def compiler_cache_digest(cache) -> str:
    return sha256(pickle.dumps(cache, protocol=pickle.HIGHEST_PROTOCOL)).hexdigest()


def load_compiler_cache(path: Path | None, compiler) -> bool:
    if path is None or not path.exists():
        return False
    with path.open("rb") as handle:
        payload = pickle.load(handle)
    if payload.get("construction") not in {
        "eager_lexicographic_all_unordered_edges_v1",
        "deterministic_upper_endpoint_eager_lexicographic_v2",
    }:
        return False
    if payload.get("k253_producer_sha256") != input_hashes()["k253_producer"]:
        return False
    assert payload["cache_sha256"] == compiler_cache_digest(payload["cache"])
    compiler.cache = payload["cache"]
    return True


def prepare_compiler(compiler, path: Path | None) -> str:
    if not load_compiler_cache(path, compiler):
        compiler.cache = {}
        for principal in range(N):
            for lower in range(LABEL_COUNT):
                if lower & (1 << principal):
                    continue
                compiler.block(lower, principal)
            print(
                f"[K254 compiler] principal={principal} edges={len(compiler.cache)}",
                flush=True,
            )
        assert len(compiler.cache) == N * LABEL_COUNT // 2
        save_compiler_cache(path, compiler)
    return compiler_cache_digest(compiler.cache)


def frontier_closure(prime: int, compiler, k253, reverse: bool = False):
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
                added = k253.insert_mod(
                    basis,
                    k253.multiply_mod(compiler.block(label, principal), vector, prime),
                    prime,
                )
                if added is not None:
                    next_frontier.append((target, added))
                if not basis:
                    bases.pop(target)
        frontier = next_frontier
        growth.append(sum(len(basis) for basis in bases.values()))
        print(
            f"[K254 frontier p={prime}] depth={len(growth) - 1} "
            f"dimension={growth[-1]} frontier={len(frontier)} sectors={len(bases)}",
            flush=True,
        )
        assert len(growth) <= 64
    return bases, growth


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


def multiply_q(matrix, vector: list[Q]) -> list[Q]:
    return [sum((Q(value) * vector[column] for column, value in row), Q()) for row in matrix]


def audit_modular_invariance(prime: int, compiler, k253, bases) -> int:
    checks = 0
    for label, basis in bases.items():
        for vector in basis.values():
            for principal in range(N):
                target = label ^ (1 << principal)
                trial = dict(bases.get(target, {}))
                image = k253.multiply_mod(compiler.block(label, principal), vector, prime)
                assert k253.insert_mod(trial, image, prime) is None
                checks += 1
    return checks


def run_modular(prime: int, compiler, k253, reverse: bool) -> dict[str, Any]:
    bases, growth = frontier_closure(prime, compiler, k253, reverse)
    state = local_ranks(bases)
    invariance_checks = audit_modular_invariance(prime, compiler, k253, bases)
    assert growth == [1, 15, 66, 402, 546, 1106, 1106]
    assert state["dimension"] == 1106
    assert state["nonzero_label_sectors"] == 470
    return {
        "prime": prime,
        "traversal": "reverse" if reverse else "forward",
        "dimension_growth": growth,
        "stabilization_depth": len(growth) - 1,
        "state": state,
        "generator_invariance_checks": invariance_checks,
    }


def rational_closure(compiler, k253) -> dict[str, Any]:
    seed = [Q(1)] + [Q()] * (N - 1)
    bases: dict[int, dict[int, list[Q]]] = {3: {0: seed}}
    frontier: list[tuple[int, list[Q]]] = [(3, seed)]
    growth = [1]
    while frontier:
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
        growth.append(sum(len(basis) for basis in bases.values()))
        assert len(growth) <= 32
    checks = 0
    for label, basis in bases.items():
        for vector in basis.values():
            for principal in range(N):
                target = label ^ (1 << principal)
                trial = dict(bases.get(target, {}))
                assert insert_q(trial, multiply_q(compiler.block(label, principal), vector)) is None
                checks += 1
    distribution = Counter(len(bases.get(label, {})) for label in range(LABEL_COUNT))
    assert growth == [1, 15, 66, 402, 546, 1106, 1106]
    return {
        "dimension_growth": growth,
        "stabilization_depth": len(growth) - 1,
        "dimension": growth[-1],
        "nonzero_label_sectors": len(bases),
        "local_rank_distribution_including_zero": {
            str(rank): count for rank, count in sorted(distribution.items())
        },
        "generator_invariance_checks": checks,
    }


def calculate(
    one_prime: int | None = None, compiler_cache: Path | None = DEFAULT_COMPILER_CACHE
) -> dict[str, Any]:
    register = REGISTER.read_text()
    ledger = LEDGER.read_text()
    assert "polarity: ASSERTS" in claim_block(register, "SC-OP-04")
    assert "polarity: UNCERTAIN" in claim_block(register, "SC-OP-05")
    assert all(f'"id": "{row}"' in ledger for row in ("LT-GR6b", "LT-SM8"))
    k253 = load_k253()
    compiler = DeterministicCompiler(k253)
    frozen_compiler_digest = prepare_compiler(compiler, compiler_cache)
    selected = (one_prime,) if one_prime else PRIMES
    modular = [
        run_modular(
            prime,
            compiler,
            k253,
            reverse=(prime == PRIMES[1]),
        )
        for prime in selected
    ]
    rational = rational_closure(compiler, k253)
    assert compiler_cache_digest(compiler.cache) == frozen_compiler_digest
    assert all(run["state"]["dimension"] == rational["dimension"] for run in modular)
    k253_record = json.loads(K253_RECORD.read_text())
    assert k253_record["modular_closure"]["characteristic_zero_lower_bound"] == 229_359
    return {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__CONDITIONAL_SELECTED_LOCAL_SYMBOL_ONLY",
        "input_sha256": input_hashes(),
        "compiled_edge_table_sha256": frozen_compiler_digest,
        "object": k253_record["object"],
        "correction": {
            "superseded_results": {
                "K251_depth_five_dimension": 1705,
                "K252_depth_seven_dimension": 21724,
                "K253_depth_eight_dimension": 42822,
                "K253_modular_terminal_dimension": 229359,
            },
            "defect": (
                "K251-K253 formed the reverse endpoint block from label xor 2^p relative to the caller. "
                "When the upper endpoint first populated the cache, that value equals the lower endpoint, "
                "so both ordered blocks were compiled from the same label. The resulting cache and generated "
                "space depended on traversal order. K254 freezes upper=lower xor 2^p before compilation."
            ),
            "corrected_exact_dimension": 1106,
            "correction_scope": "The raw sparse single-blade formula survives; the cached Euler edge orientation and every generated-space dimension beyond depth one are superseded.",
        },
        "modular_closure": {
            "runs": modular,
            "cross_prime_growth_agreement": len(modular) == 2 and modular[0]["dimension_growth"] == modular[1]["dimension_growth"],
        },
        "exact_rational_closure": rational,
        "exact_characteristic_zero_dimension": rational["dimension"],
        "interpretation": (
            "The Q-generated hull of the conditional selected local principal family has exact dimension 1106 and codimension 228270 in T-star tensor Cl(7,7)."
        ),
        "source_routing": "SC-OP-04 ASSERTS and SC-OP-05 UNCERTAIN are preserved; SC-ACT-01/02 ASSERTS, SC-META-53 UNCERTAIN, and LT-GR6b/LT-SM8 NEEDS do not move.",
        "claim_ceiling": "Exact generated-space dimension and invariant rational hull for one conditional selected local principal family. No source-selected full fermion operator, lower-order/common domain, quotient, spectrum, positivity, ledger/canon/public change, or K218 cancellation theorem.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--one-prime", type=int, choices=PRIMES)
    parser.add_argument("--compiler-cache", type=Path, default=DEFAULT_COMPILER_CACHE)
    args = parser.parse_args()
    result = calculate(args.one_prime, args.compiler_cache)
    if args.write:
        assert args.one_prime is None
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(
        f"[PASS] K254 exact I1B closure: dimension={result['exact_characteristic_zero_dimension']} "
        f"codimension={N * LABEL_COUNT - result['exact_characteristic_zero_dimension']}"
    )

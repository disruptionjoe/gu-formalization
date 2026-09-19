#!/usr/bin/env python3
"""Independent backend replay and caller-order regression control for K254."""
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import importlib.util
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K253_PRODUCER = ROOT / "tests/channel-swings/k253_native_i1b_sparse_closure.py"
K253_RECORD = ROOT / "lab/process/k253-native-i1b-sparse-closure.json"
K254_RECORD = ROOT / "lab/process/k254-native-i1b-exact-closure.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
CHANNELS = ("comm", "symi", "symi")
N = 14
LABEL_COUNT = 1 << N
FULL = LABEL_COUNT - 1
EXPECTED_GROWTH = [1, 15, 66, 402, 546, 1106, 1106]


def load_k253():
    spec = importlib.util.spec_from_file_location("k253_probe_dependency", K253_PRODUCER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    record = json.loads(K254_RECORD.read_text())
    assert record["input_sha256"] == {
        "k253_producer": sha256(K253_PRODUCER.read_bytes()).hexdigest(),
        "k253_record": sha256(K253_RECORD.read_bytes()).hexdigest(),
        "source_register": sha256(REGISTER.read_bytes()).hexdigest(),
        "physics_ledger_v0_263": sha256(LEDGER.read_bytes()).hexdigest(),
    }
    with redirect_stdout(StringIO()) as log:
        backend = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full, n = backend["ONE"], backend["ZERO"], backend["FULL"], backend["N"]
    assert n == N and full == FULL

    def direction(mu: int, blade: int):
        return {1 << mu: {blade: one}}

    def ordered_columns(label: int, principal: int) -> list[list[Q]]:
        target = label ^ (1 << principal)
        normal = direction(principal, 0)
        columns: list[list[Q]] = []
        for mu in reversed(range(N)):
            image = backend["shiab"](
                backend["wedge_raw"](normal, direction(mu, label ^ (1 << mu))),
                CHANNELS,
            )
            observed = set()
            for form_mask, element in image.items():
                complement = FULL ^ form_mask
                assert complement and not complement & (complement - 1)
                nu = complement.bit_length() - 1
                observed.update(blade ^ (1 << nu) for blade in element)
            assert observed <= {target}
            column = []
            for nu in reversed(range(N)):
                value = backend["wedge_raw"](
                    direction(nu, target ^ (1 << nu)), image
                ).get(FULL, {}).get(0, zero)
                assert value[1] == 0
                column.append(value[0])
            columns.append(column)
        return [list(reversed(column)) for column in reversed(columns)]

    cache: dict[tuple[int, int], list[list[Q]]] = {}

    def negative_transpose(matrix: list[list[Q]]) -> list[list[Q]]:
        return [[-matrix[j][i] for j in range(N)] for i in range(N)]

    def block(label: int, principal: int) -> list[list[Q]]:
        adjacent = label ^ (1 << principal)
        lower = min(label, adjacent)
        upper = lower ^ (1 << principal)
        key = lower, principal
        if key not in cache:
            forward = ordered_columns(lower, principal)
            reverse = ordered_columns(upper, principal)
            cache[key] = [
                [(forward[mu][nu] - reverse[nu][mu]) / 2 for mu in range(N)]
                for nu in range(N)
            ]
        return cache[key] if label == lower else negative_transpose(cache[key])

    # Minimal K251-K253 regression witness: first-caller direction changed the
    # matrix cached for the same unordered label edge.
    k253 = load_k253()
    old_from_lower = k253.Compiler()
    old_from_lower.block(0, 0)
    old_from_upper = k253.Compiler()
    old_from_upper.block(1, 0)
    assert old_from_lower.cache[(0, 0)] != old_from_upper.cache[(0, 0)]

    # The corrected construction is first-caller independent.
    upper_first = block(1, 0)
    lower_after = block(0, 0)
    assert upper_first == negative_transpose(lower_after)

    def multiply(matrix: list[list[Q]], vector: list[Q]) -> list[Q]:
        return [
            sum((matrix[i][j] * vector[j] for j in range(N)), Q())
            for i in range(N)
        ]

    # Reverse generator order and greatest-pivot elimination are independent of
    # K254's sparse compiler and least-pivot basis.
    def insert(basis: dict[int, list[Q]], vector: list[Q]) -> list[Q] | None:
        value = list(vector)
        while True:
            pivot = next((i for i in reversed(range(N)) if value[i]), None)
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

    seed = [Q(1), *([Q()] * (N - 1))]
    bases: dict[int, dict[int, list[Q]]] = {3: {0: seed}}
    frontier: list[tuple[int, list[Q]]] = [(3, seed)]
    growth = [1]
    while frontier:
        next_frontier: list[tuple[int, list[Q]]] = []
        for label, vector in reversed(frontier):
            for principal in reversed(range(N)):
                target = label ^ (1 << principal)
                basis = bases.setdefault(target, {})
                added = insert(basis, multiply(block(label, principal), vector))
                if added is not None:
                    next_frontier.append((target, added))
                if not basis:
                    bases.pop(target)
        frontier = next_frontier
        growth.append(sum(len(basis) for basis in bases.values()))
        assert len(growth) <= 32

    distribution = Counter(len(bases.get(label, {})) for label in range(LABEL_COUNT))
    exact = record["exact_rational_closure"]
    assert growth == exact["dimension_growth"] == EXPECTED_GROWTH, growth
    assert growth[-1] == exact["dimension"] == record["exact_characteristic_zero_dimension"] == 1106
    assert len(bases) == exact["nonzero_label_sectors"] == 470
    assert {str(rank): count for rank, count in sorted(distribution.items())} == exact[
        "local_rank_distribution_including_zero"
    ] == {"0": 15914, "2": 455, "13": 14, "14": 1}
    assert all(run["dimension_growth"] == growth for run in record["modular_closure"]["runs"])
    assert record["modular_closure"]["cross_prime_growth_agreement"]

    correction = record["correction"]
    assert correction["corrected_exact_dimension"] == 1106
    assert correction["superseded_results"] == {
        "K251_depth_five_dimension": 1705,
        "K252_depth_seven_dimension": 21724,
        "K253_depth_eight_dimension": 42822,
        "K253_modular_terminal_dimension": 229359,
    }
    assert "conditional selected local principal family" in record["claim_ceiling"]
    assert "No source-selected full fermion operator" in record["claim_ceiling"]
    assert "SC-OP-05 UNCERTAIN" in record["source_routing"]
    assert "LT-GR6b/LT-SM8 NEEDS" in record["source_routing"]
    print("[PASS] K254 independent exact closure replay and caller-order controls")


if __name__ == "__main__":
    main()

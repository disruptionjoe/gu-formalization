#!/usr/bin/env python3
"""Independent reverse-order replay and hostile controls for K251."""
from collections import Counter, deque
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K250 = ROOT / "lab/process/k250-native-i1b-source-selection-and-all-direction-growth.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
RECORD = ROOT / "lab/process/k251-native-i1b-depth-five-principal-growth.json"
CHANNELS = ("comm", "symi", "symi")
MAX_DEPTH = 5


def main() -> None:
    record = json.loads(RECORD.read_text())
    assert record["input_sha256"] == {
        "backend": sha256(BACKEND.read_bytes()).hexdigest(),
        "k250": sha256(K250.read_bytes()).hexdigest(),
        "source_register": sha256(REGISTER.read_bytes()).hexdigest(),
        "physics_ledger_v0_263": sha256(LEDGER.read_bytes()).hexdigest(),
    }
    with redirect_stdout(StringIO()) as log:
        backend = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full, n = (
        backend["ONE"], backend["ZERO"], backend["FULL"], backend["N"]
    )

    def direction(mu: int, blade: int):
        return {1 << mu: {blade: one}}

    def ordered_columns(label: int, principal: int) -> list[list[Q]]:
        target = label ^ (1 << principal)
        normal = direction(principal, 0)
        columns: list[list[Q]] = []
        for mu in reversed(range(n)):
            image = backend["shiab"](
                backend["wedge_raw"](
                    normal, direction(mu, label ^ (1 << mu))
                ),
                CHANNELS,
            )
            observed = set()
            for form_mask, element in image.items():
                complement = full ^ form_mask
                assert complement and not complement & (complement - 1)
                nu = complement.bit_length() - 1
                observed.update(blade ^ (1 << nu) for blade in element)
            assert observed <= {target}
            column = []
            for nu in reversed(range(n)):
                value = backend["wedge_raw"](
                    direction(nu, target ^ (1 << nu)), image
                ).get(full, {}).get(0, zero)
                assert value[1] == 0
                column.append(value[0])
            columns.append(column)
        # Restore ordinary row/column indices after intentionally reversed traversal.
        return [list(reversed(column)) for column in reversed(columns)]

    cache: dict[tuple[int, int], list[list[Q]]] = {}

    def negative_transpose(matrix: list[list[Q]]) -> list[list[Q]]:
        return [[-matrix[j][i] for j in range(n)] for i in range(n)]

    def block(label: int, principal: int) -> list[list[Q]]:
        target = label ^ (1 << principal)
        lower = min(label, target)
        key = (lower, principal)
        if key not in cache:
            forward = ordered_columns(lower, principal)
            reverse = ordered_columns(target, principal)
            cache[key] = [
                [
                    (forward[mu][nu] - reverse[nu][mu]) / 2
                    for mu in range(n)
                ]
                for nu in range(n)
            ]
        return cache[key] if label == lower else negative_transpose(cache[key])

    def multiply(matrix: list[list[Q]], vector: list[Q]) -> list[Q]:
        return [
            sum((matrix[i][j] * vector[j] for j in range(n)), Q())
            for i in range(n)
        ]

    # Deliberately use greatest-pivot elimination and reversed principal order.
    def insert(basis: dict[int, list[Q]], vector: list[Q]) -> list[Q] | None:
        value = list(vector)
        while True:
            pivot = next((i for i in reversed(range(n)) if value[i]), None)
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
    bases: dict[int, dict[int, list[Q]]] = {3: {0: seed}}
    queue = deque([(3, seed, 0)])
    increments: Counter[int] = Counter()
    while queue:
        label, vector, depth = queue.popleft()
        increments[depth] += 1
        if depth >= MAX_DEPTH:
            continue
        for principal in reversed(range(n)):
            target = label ^ (1 << principal)
            basis = bases.setdefault(target, {})
            added = insert(basis, multiply(block(label, principal), vector))
            if added is not None:
                queue.append((target, added, depth + 1))
            if not basis:
                bases.pop(target)

    total = 0
    growth = []
    for depth in range(MAX_DEPTH + 1):
        total += increments[depth]
        growth.append(total)
    distribution = Counter(len(basis) for basis in bases.values())
    generated = record["generated_space"]
    assert growth == generated["dimension_growth_d0_through_d5"]
    assert total == generated["dimension"] == 1705
    assert len(bases) == generated["nonzero_label_sectors"] == 755
    assert {str(k): v for k, v in sorted(distribution.items())} == generated["local_rank_distribution"]

    # Hostile readings: K250's first layer and K249's four-label projection
    # both erase certified K251 content, while depth five remains non-closed.
    assert growth[1] == 15 and growth[-1] > 70 * growth[1]
    assert len(bases) > 4
    assert generated["maximum_word_length"] == 5
    assert "No stabilized or complete" in record["claim_ceiling"]
    assert "does not select a unique full fermion operator" in K250.read_text()
    print("[PASS] K251 reverse-order exact depth-five replay and hostile controls")


if __name__ == "__main__":
    main()

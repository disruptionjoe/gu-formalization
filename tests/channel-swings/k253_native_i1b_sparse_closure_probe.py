#!/usr/bin/env python3
"""Independent original-backend replay and hostile controls for K253."""
from __future__ import annotations

from contextlib import redirect_stdout
from fractions import Fraction as Q
from io import StringIO
import importlib.util
import json
from pathlib import Path
import random
import runpy


ROOT = Path(__file__).resolve().parents[2]
PRODUCER_PATH = ROOT / "tests/channel-swings/k253_native_i1b_sparse_closure.py"
BACKEND_PATH = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
RECORD_PATH = ROOT / "lab/process/k253-native-i1b-sparse-closure.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k253_producer", PRODUCER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    producer = load_producer()
    with redirect_stdout(StringIO()) as log:
        backend = runpy.run_path(str(BACKEND_PATH))
    assert "FAILURES=0" in log.getvalue()
    n, full = backend["N"], backend["FULL"]
    one, zero = backend["ONE"], backend["ZERO"]
    channels = ("comm", "symi", "symi")
    assert n == 14

    def direction(mu: int, blade: int):
        return {1 << mu: {blade: one}}

    def original_raw_block(label: int, principal: int) -> list[list[Q]]:
        out_label = label ^ (1 << principal)
        normal = direction(principal, 0)
        columns: list[list[Q]] = []
        for mu in range(n):
            image = backend["shiab"](
                backend["wedge_raw"](
                    normal, direction(mu, label ^ (1 << mu))
                ),
                channels,
            )
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

    # Cover boundary labels, complements, alternating masks, and 256 seeded
    # labels across every principal direction rather than trusting the reduced
    # compiler alone.
    rng = random.Random(253)
    labels = {
        0,
        1,
        2,
        3,
        full,
        full ^ 1,
        full ^ 2,
        full ^ 3,
        int("10101010101010", 2),
        int("01010101010101", 2),
    }
    labels.update(rng.sample(range(1 << n), 256))
    checks = 0
    for label in sorted(labels):
        for principal in range(n):
            original = original_raw_block(label, principal)
            reduced = producer.sparse_raw_block(label, principal)
            assert original == reduced
            checks += 1

    record = json.loads(RECORD_PATH.read_text())
    modular = record["modular_closure"]
    runs = modular["runs"]
    expected = [
        1, 15, 52, 388, 623, 1705, 6644, 21724, 42822, 78638,
        134342, 184172, 209406, 220572, 227760, 229124, 229359, 229359,
    ]
    assert [run["prime"] for run in runs] == [1_000_003, 1_000_033]
    assert runs[0]["traversal"] == "forward"
    assert runs[1]["traversal"] == "reverse"
    assert all(run["dimension_growth"] == expected for run in runs)
    assert all(run["dimension"] == 229359 for run in runs)
    assert all(not run["full_ambient"] for run in runs)
    assert all(
        run["exceptional_label_ranks"] == {"0": 0, "16380": 13, "16383": 12}
        for run in runs
    )
    assert modular["cross_prime_growth_agreement"]
    assert modular["characteristic_zero_lower_bound"] == 229359

    rational = record["rational_generation"]
    assert rational["dimension_growth"] == [
        1, 15, 52, 388, 623, 1705, 6644, 21724, 42822
    ]
    assert rational["new_dimensions_at_final_depth"] == 21098
    assert not rational["stabilized"]

    # Hostile interpretations: modular non-fullness is not a rational upper
    # bound, and neither calculation selects the missing physical structures.
    assert modular["characteristic_zero_inference"].startswith("Non-full")
    assert "No source-selected full fermion operator" in record["claim_ceiling"]
    assert "SC-OP-05 UNCERTAIN" in record["source_routing"]
    assert record["ambient_carrier"]["dimension"] - runs[0]["dimension"] == 17
    print(f"[PASS] K253 original-backend replay: {checks} blocks and hostile controls")


if __name__ == "__main__":
    main()

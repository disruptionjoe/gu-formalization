#!/usr/bin/env python3
"""One-time builder for the versioned K77 exact coefficient-bank fixture.

This is the only path allowed to execute the historical recursive producer.
Consumers use ``k77_exact_bank_api.py`` and never call this builder.  The
builder captures every nested ``runpy.run_path`` dependency, hashes it, and
serializes the branch-independent rational polynomial bank canonically.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from fractions import Fraction
from hashlib import sha256
from io import StringIO
from pathlib import Path
import argparse
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/selected_k77_fixed_operator_metric_epsilon_leakage_probe.py"
DEFAULT_OUTPUT = ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json"
SOURCE_CUSTODY = (
    ROOT / "lab/sources/selected-k77-metric-epsilon-hessian-source-reinspection-2026-08-09.md",
    ROOT / "lab/sources/selected-k77-moving-epsilon-first-action-source-reinspection-2026-08-09.md",
)
PRODUCER_SUMMARY = re.compile(r"^(?:RESULT:\s*)?PASS\s+(\d+)/(\d+)(?:\s.*)?$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rational(value) -> list[int]:
    value = Fraction(value)
    return [value.numerator, value.denominator]


def sparse(component) -> list[list[int]]:
    return [
        [int(row), *rational(value)]
        for row, value in sorted(component.items())
    ]


def canonical(payload: dict) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def require_producer_pass(output: str, failures, label: str) -> tuple[int, int]:
    """Require one positive final N/N certificate without pinning N itself."""
    summary = None
    for line in reversed(output.splitlines()):
        match = PRODUCER_SUMMARY.fullmatch(line.strip())
        if match:
            summary = tuple(map(int, match.groups()))
            break
    failure_list = list(failures)
    if failure_list or summary is None or summary[0] <= 0 or summary[0] != summary[1]:
        tail = [line for line in output.splitlines() if line.strip()][-8:]
        raise RuntimeError(
            f"{label} did not pass: summary={summary!r}; "
            f"failures={failure_list!r}; output_tail={tail!r}"
        )
    return summary


def build() -> dict:
    dependencies: set[Path] = {PRODUCER}
    original = runpy.run_path

    def tracked(path_name, *args, **kwargs):
        path = Path(path_name).resolve()
        if path.is_relative_to(ROOT):
            dependencies.add(path)
        return original(path_name, *args, **kwargs)

    runpy.run_path = tracked
    capture = StringIO()
    try:
        with redirect_stdout(capture):
            namespace = tracked(str(PRODUCER))
    finally:
        runpy.run_path = original

    require_producer_pass(
        capture.getvalue(), namespace["FAILURES"], "immutable v0.122 producer"
    )

    carrier = namespace["C"]
    algebra = carrier["M"]
    grade2 = [
        direction
        for direction, grade in zip(carrier["directions"], carrier["direction_grades"])
        if grade == 2
    ]
    receiver_labels = []
    for direction in grade2:
        flat = algebra["flatten"](direction)
        if len(flat) != 1:
            raise RuntimeError("grade-two receiver is not atomically labelled")
        (form_mask, clifford_mask), coefficient = next(iter(flat.items()))
        receiver_labels.append({
            "form_mask": int(form_mask),
            "clifford_mask": int(clifford_mask),
            "coefficient": [rational(coefficient[0]), rational(coefficient[1])],
        })

    columns = {}
    for causal, bank in namespace["COEFFICIENT_COLUMNS"].items():
        rows = []
        metric_index = epsilon_index = 0
        for constant, b_part, t_part, kind in bank:
            if kind == "metric":
                index = metric_index
                metric_index += 1
            elif kind == "epsilon":
                index = epsilon_index
                epsilon_index += 1
            else:
                raise RuntimeError(kind)
            rows.append({
                "kind": kind,
                "index": index,
                "constant": sparse(constant),
                "b": sparse(b_part),
                "t": sparse(t_part),
            })
        if (metric_index, epsilon_index) != (10, 91):
            raise RuntimeError((metric_index, epsilon_index))
        columns[causal] = rows

    for path in SOURCE_CUSTODY:
        dependencies.add(path)

    relative_hashes = {
        str(path.relative_to(ROOT)): digest(path)
        for path in sorted(dependencies)
    }
    source_hashes = {
        str(path.relative_to(ROOT)): digest(path)
        for path in SOURCE_CUSTODY
    }
    payload = {
        "schema_version": "1.0",
        "bank_id": "K77_SELECTED_SPIN_FIRST_ACTION_FIXED_OPERATOR_GRADE2_V1",
        "generated_from": str(PRODUCER.relative_to(ROOT)),
        "dependency_hashes": relative_hashes,
        "source_revision_hashes": source_hashes,
        "carrier": {
            "dimension": 14,
            "signature_diagonal": list(algebra["ETA"]),
            "real_form": "Cl(7,7)",
            "coefficient_field": "QQ(i)",
            "selected_shiab_channels": list(carrier["SELECTED"]),
            "epsilon_generators": [list(pair) for pair in carrier["pairs14"]],
        },
        "receivers": {
            "grade": 2,
            "dimension": 1274,
            "horizontal_rows": sorted(namespace["horizontal_rows"]),
            "offslice_rows": sorted(namespace["offslice_rows"]),
            "labels": receiver_labels,
        },
        "causal_covectors": {
            name: [rational(value) for value in carrier["P"]["G"]["S"]["orbits"][name]]
            for name in ("timelike", "spacelike", "null")
        },
        "coefficient_basis": ["constant", "b", "t"],
        "columns": columns,
        "epsilon_completion": {
            "lower_cartan_grade2": "ZERO",
            "moving_shiab_grade2": "ZERO",
            "complete_equals_fixed_coefficientwise": True,
            "evidence": "lab/process/selected-k77-moving-epsilon-first-action-completion.json",
        },
        "scientific_scope": {
            "action": "FIRST_TRANSGRESSION",
            "parent": "SELECTED_REAL_SPIN77",
            "two_U32_32_halves": "NOT_PORTED",
            "full_U64_64": "NOT_PORTED",
            "quotient": "NONE_PROMOTED",
        },
    }
    payload["construction_hash"] = sha256(canonical(payload)).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output = args.output.resolve()
    if output != DEFAULT_OUTPUT.resolve():
        raise SystemExit(f"refusing noncanonical output: {output}")
    payload = build()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(canonical(payload))
    print(f"WROTE={output.relative_to(ROOT)}")
    print(f"CONSTRUCTION_HASH={payload['construction_hash']}")
    print(f"DEPENDENCIES={len(payload['dependency_hashes'])}")
    print(f"BYTES={output.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

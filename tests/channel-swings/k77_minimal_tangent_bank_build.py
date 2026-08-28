#!/usr/bin/env python3
"""One-time builder for the exact selected-K77 rank-594 tangent bank.

Ordinary consumers must use ``k77_minimal_tangent_bank_api.py``. This builder
is the only path allowed to replay the heavier v0.126 closure producer.
"""

from collections import deque
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
import argparse
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/selected_k77_minimal_hessian_tangent_closure_probe.py"
DEFAULT_OUTPUT = ROOT / "tests/fixtures/k77_minimal_tangent_bank_v1.json"
DEPENDENCIES = (
    PRODUCER,
    ROOT / "tests/channel-swings/k77_exact_bank_api.py",
    ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json",
    ROOT / "lab/process/selected-k77-minimal-hessian-tangent-closure.json",
    ROOT / "explorations/conditional-build/selected-k77-minimal-hessian-tangent-closure-2026-08-09.md",
    ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-minimal-hessian-tangent-closure-review.md",
)
PRODUCER_SUMMARY = re.compile(r"^(?:RESULT:\s*)?PASS\s+(\d+)/(\d+)(?:\s.*)?$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rational(value):
    return [value.numerator, value.denominator]


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
    capture = StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(str(PRODUCER))
    require_producer_pass(
        capture.getvalue(), namespace["FAILURES"], "v0.126 tangent producer"
    )

    basis = namespace["SparseEchelon"]()
    frontier = deque()
    for value in namespace["full_joint_seed"]:
        inserted = basis.insert(value)
        if inserted is not None:
            frontier.append(inserted)
    while frontier:
        value = frontier.popleft()
        for operator, _ in namespace["branch_operators"]:
            inserted = basis.insert(namespace["matvec"](operator, value))
            if inserted is not None:
                frontier.append(inserted)
    if basis.rank != 594:
        raise RuntimeError(f"unexpected tangent rank {basis.rank}")

    vectors = []
    for pivot, vector in sorted(basis.pivots.items()):
        entries = []
        for row, (real, radical) in sorted(vector.items()):
            entries.append([row, *rational(real), *rational(radical)])
        vectors.append({"pivot": pivot, "entries": entries})

    base_bank = namespace["bank"]
    payload = {
        "schema_version": "1.0",
        "bank_id": "K77_SELECTED_SPIN_FIRST_ACTION_MINIMAL_TANGENT_V1",
        "generated_from": str(PRODUCER.relative_to(ROOT)),
        "dependency_hashes": {
            str(path.relative_to(ROOT)): digest(path) for path in DEPENDENCIES
        },
        "coefficient_field": "QQ(sqrt(3))",
        "ambient": {
            "representation": "OFFSLICE_PART_OF_VSTAR_TENSOR_LAMBDA2_V",
            "dimension": len(namespace["offslice"]),
            "offslice_global_rows": list(namespace["offslice"]),
            "signature_diagonal": list(base_bank.signature),
            "horizontal_dimension": len(namespace["horizontal"]),
        },
        "tangent": {
            "rank": basis.rank,
            "nnz": sum(len(vector) for vector in basis.pivots.values()),
            "vectors": vectors,
            "total_selected_dimension": 321 + basis.rank,
        },
        "construction": {
            "fixed_symbol_image_rank": 89,
            "fixed_symbol_closure_rank": 174,
            "three_representative_closure_rank": 464,
            "full_X4_both_branch_closure_rank": 594,
        },
        "scientific_scope": {
            "action": "FIRST_TRANSGRESSION",
            "parent": "SELECTED_REAL_SPIN77",
            "differential_grade": "LOCAL_PRINCIPAL",
            "two_U32_32_halves": "NOT_PORTED",
            "full_U64_64": "NOT_PORTED",
            "lower_order": "OPEN",
            "quotient": "NONE_PROMOTED",
        },
    }
    unsigned = dict(payload)
    payload["construction_hash"] = sha256(canonical(unsigned)).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output = args.output.resolve()
    if output != DEFAULT_OUTPUT.resolve():
        raise SystemExit(f"refusing noncanonical output: {output}")
    payload = build()
    output.write_bytes(canonical(payload))
    print(f"WROTE={output.relative_to(ROOT)}")
    print(f"CONSTRUCTION_HASH={payload['construction_hash']}")
    print(f"RANK={payload['tangent']['rank']}")
    print(f"NNZ={payload['tangent']['nnz']}")
    print(f"BYTES={output.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

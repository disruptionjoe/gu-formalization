#!/usr/bin/env python3
"""K276: exact SC-ACT-06 Euclidean principal-complex data gate."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
SOURCE_PACK = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
BACKGROUND = ROOT / "lab/process/selected-k77-tautological-total-residual-zero-background.json"
REPORT = ROOT / "explorations/conditional-build/selected-k77-tautological-total-residual-zero-background-2026-08-14.md"
CERTIFICATE = ROOT / "lab/process/k276-sc-act-06-euclidean-principal-complex-data-gate.json"


def rank(matrix: list[list[int | Fraction]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    if not work:
        return 0
    rows, cols = len(work), len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                factor = work[r][col]
                work[r] = [work[r][c] - factor * work[pivot_row][c] for c in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    if not left:
        return []
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def wedge_symbol(n: int, degree: int, covector: tuple[int, ...]) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]], list[list[int]]]:
    source = list(combinations(range(n), degree))
    target = list(combinations(range(n), degree + 1))
    source_index = {basis: i for i, basis in enumerate(source)}
    matrix = [[0 for _ in source] for _ in target]
    for row, out_basis in enumerate(target):
        for missing_position, missing in enumerate(out_basis):
            in_basis = out_basis[:missing_position] + out_basis[missing_position + 1 :]
            matrix[row][source_index[in_basis]] = ((-1) ** missing_position) * covector[missing]
    return source, target, matrix


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


register = REGISTER.read_text()
source_pack = SOURCE_PACK.read_text()
register_flat = " ".join(register.split())
source_pack_flat = " ".join(source_pack.split())
background = json.loads(BACKGROUND.read_text())
report = REPORT.read_text()
certificate = json.loads(CERTIFICATE.read_text())

assert "- id: SC-ACT-06" in register
assert "elliptic deformation complex in Euclidean signature" in register_flat
assert "once the redundant Euler-Lagrange equations are discarded" in register_flat
assert "Euclidean-to-Minkowski sign may be wrong" in source_pack_flat
assert background["native_legality"]["B_equals_B_epsilon"] == "TYPE_MISSING"
assert background["native_legality"]["native_Y_Met_X_background"] == "NOT_CONSTRUCTED"
assert background["bv_pde_scope"]["euclidean_ellipticity"] == "NOT_TESTED"
assert "does not yet close `SR-1B`" in report
assert "Native `B(epsilon)` and `Y=Met(X)` legality" in report

n = 14
covectors = [
    (1,) + (0,) * 13,
    (1, -2, 3, 0, 5, 0, 0, 7, 0, 0, 0, 0, 0, 11),
]
rank_receipts = []
for covector in covectors:
    _, one_basis, gauge = wedge_symbol(n, 0, covector)
    _, two_basis, euler = wedge_symbol(n, 1, covector)
    _, _, redundancy = wedge_symbol(n, 2, covector)
    gauge_rank = rank(gauge)
    euler_rank = rank(euler)
    redundancy_rank = rank(redundancy)
    assert gauge_rank == 1
    assert euler_rank == 13
    assert redundancy_rank == 78
    assert not any(any(row) for row in multiply(euler, gauge))
    assert not any(any(row) for row in multiply(redundancy, euler))
    assert n - euler_rank == gauge_rank
    assert len(two_basis) - redundancy_rank == euler_rank
    rank_receipts.append([gauge_rank, euler_rank, redundancy_rank])

# At xi=e^0 the full curvature symbol has thirteen independent transverse
# rows.  Keeping all thirteen gives an exact reduced gauge/Euler symbol;
# keeping twelve is equally compatible with the source's uninstantiated phrase
# "discard redundant equations" but leaves one extra middle cohomology class.
axis_covector = covectors[0]
_, two_basis, full_euler = wedge_symbol(n, 1, axis_covector)
transverse_rows = [i for i, pair in enumerate(two_basis) if pair[0] == 0]
reduced_exact = [full_euler[i] for i in transverse_rows]
reduced_short = reduced_exact[:-1]
_, _, gauge_axis = wedge_symbol(n, 0, axis_covector)
assert len(reduced_exact) == 13
assert rank(reduced_exact) == 13
assert rank(reduced_short) == 12
assert not any(any(row) for row in multiply(reduced_exact, gauge_axis))
assert not any(any(row) for row in multiply(reduced_short, gauge_axis))
assert n - rank(reduced_exact) == rank(gauge_axis)
assert n - rank(reduced_short) == rank(gauge_axis) + 1

expected = certificate["exact_symbol_attempt"]
assert expected["dimension"] == n
assert expected["full_koszul_ranks"] == rank_receipts[0]
assert expected["generic_covector_ranks"] == rank_receipts[1]
assert expected["reduced_exact_rows"] == 13
assert expected["reduced_short_rows"] == 12
assert expected["reduced_short_middle_cohomology"] == 1

for path, digest in (
    (REGISTER, certificate["input_hashes"]["source_claim_register"]),
    (SOURCE_PACK, certificate["input_hashes"]["primary_source_pack"]),
    (BACKGROUND, certificate["input_hashes"]["tautological_background_json"]),
    (REPORT, certificate["input_hashes"]["tautological_background_report"]),
):
    assert sha256(path) == digest

assert certificate["disposition"] == "R8_CONCLUDED_AT_EXACT_SOURCE_DATA_OBSTRUCTION"
assert certificate["source_status_changes"] == "NONE"
assert certificate["ledger_or_public_changes"] == "NONE"

print("[PASS] K276 SC-ACT-06 Euclidean principal-complex data gate 9/9 exact, 4/4 hostile")

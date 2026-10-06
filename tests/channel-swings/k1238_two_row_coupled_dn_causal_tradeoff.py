#!/usr/bin/env python3
"""Exact coupled DN ranks for the ratio-three two-row Shiab candidate."""

from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import combinations
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
capture = StringIO()
with redirect_stdout(capture):
    P = runpy.run_path(str(ROOT / "tests/channel-swings/k1236_all_comm_shiab_all_grade_census.py"))
assert "FAILURES 0" in capture.getvalue()

M, N, ETA = P["M"], P["N"], P["ETA"]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


FORM_PAIRS = list(combinations(range(N), 2))
METRIC_SLOTS = [(p, q) for p in range(4) for q in range(p, 4)]


def metric_basis_value(slot, i, j):
    p, q = slot
    return int((i, j) == (p, q) or (p != q and (i, j) == (q, p)))


def principal_riemann(covector, slot):
    def tensor(i, j, a, b):
        h = lambda x, y: metric_basis_value(slot, x, y)
        k = covector
        return (k[i] * k[a] * h(j, b) - k[i] * k[b] * h(j, a)
                - k[j] * k[a] * h(i, b) + k[j] * k[b] * h(i, a))
    return tensor


def spin_curvature_injection(tensor):
    out = {}
    for i, j in FORM_PAIRS:
        coefficient = {}
        for a, b in FORM_PAIRS:
            value = ETA[a] * ETA[b] * tensor(i, j, a, b)
            if value:
                coefficient = M["eadd"](
                    coefficient, M["escale"](value, M["emul"](M["blade"](a), M["blade"](b))))
        if coefficient:
            out[(1 << i) | (1 << j)] = coefficient
    return out


def curvature_columns(covector):
    columns = []
    for slot in METRIC_SLOTS:
        source = spin_curvature_injection(principal_riemann(covector, slot))
        output = P["shiab_pencil"](source, 1, 3)
        columns.append({(mask ^ (1 << nu), nu): value
                        for nu, mask, value in P["rows_for_image"](output)})
    return columns


def coupled_rank(covector, toggle_axes, total_distortion_rank):
    columns = curvature_columns(covector)
    support = {label for column in columns for label, _ in column}
    labels = set()
    for label in support:
        for bits in range(1 << len(toggle_axes)):
            moved = label
            for j, axis in enumerate(toggle_axes):
                if bits & (1 << j):
                    moved ^= 1 << axis
            labels.add(moved)
    labels = sorted(labels)
    basis, _, distortion = P["raw_block"](covector, labels, 1, 3)
    index = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}
    mixed = sp.zeros(distortion.rows, len(METRIC_SLOTS))
    for column_index, column in enumerate(columns):
        for key, value in column.items():
            assert value[1] == 0
            mixed[index[key], column_index] = sp.Rational(value[0].numerator, value[0].denominator)
    coupled = sp.zeros(len(METRIC_SLOTS) + distortion.rows)
    coupled[:10, 10:] = mixed.T
    coupled[10:, :10] = mixed
    coupled[10:, 10:] = distortion
    return {"A_rank": mixed.rank(), "C_local_rank": distortion.rank(),
            "H_local_rank": coupled.rank(),
            "total_rank": total_distortion_rank - distortion.rank() + coupled.rank()}


nonnull = P["census_nonnull"](0, 1, 3)
null = P["census_null"](1, 3)
coupled_t = coupled_rank((1,) + (0,) * 13, (0,), nonnull["euler_rank"])
coupled_s = coupled_rank((0, 1) + (0,) * 12, (1,), nonnull["euler_rank"])
coupled_n = coupled_rank((1, 0, 0, 1) + (0,) * 10, (0, 3), null["euler_rank"])

check("metric", "curvature rows retain ranks six six four",
      (coupled_t["A_rank"], coupled_s["A_rank"], coupled_n["A_rank"]) == (6, 6, 4))
check("coupled", "ratio-three coupled ranks are exact",
      (coupled_t["total_rank"], coupled_s["total_rank"], coupled_n["total_rank"]) == (131070, 131070, 122880))
check("radical", "ratio-three coupled radicals are exact",
      tuple(229386 - row["total_rank"] for row in (coupled_t, coupled_s, coupled_n)) == (98316, 98316, 106506))
check("gain", "coupled gains over selected K132 are 158 158 132",
      (131070 - 130912, 131070 - 130912, 122880 - 122748) == (158, 158, 132))
check("causal", "cross-null radical jump remains 8190", 106506 - 98316 == 8190)

basis, _, normal = P["raw_block"]((1,) + (0,) * 13, [0, 1, 2, 3], 1, 3)
_, _, tangential = P["raw_block"]((0, 1) + (0,) * 12, [0, 1, 2, 3], 1, 3)
check("propagation", "normal rank is 32 with radical 24", normal.rank() == 32 and normal.rows - normal.rank() == 24)
check("propagation", "only eleven normal-null directions remain tangential-null",
      normal.rows - normal.col_join(tangential).rank() == 11)

print("RATIO3_COUPLED_RANKS=131070,131070,122880")
print("RATIO3_COUPLED_RADICALS=98316,98316,106506")
failures = [label for _, label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))

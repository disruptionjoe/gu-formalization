"""Independent Sage/FLINT rank replay for the frozen metric/epsilon gate."""

from io import StringIO
from pathlib import Path
import contextlib
import runpy

from sage.all import QuadraticField, matrix


ROOT = Path(__file__).resolve().parents[2]
PRIMARY = ROOT / "tests/channel-swings/selected_k77_fixed_operator_metric_epsilon_leakage_probe.py"
capture = StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PRIMARY))
assert not P["FAILURES"]

K = QuadraticField(3, "s")
s = K.gen()


def in_k(value):
    polynomial = value.as_poly(P["sqrt3"])
    if polynomial is None:
        return K(int(value.p)) / int(value.q)

    def qrat(item):
        return K(int(item.p)) / int(item.q)

    return qrat(polynomial.nth(0)) + qrat(polynomial.nth(1)) * s


def rank(columns, rows=None):
    if rows is None:
        row_map = {row: row for row in range(1274)}
    else:
        row_map = {row: index for index, row in enumerate(sorted(rows))}
    entries = {}
    for column_index, column in enumerate(columns):
        for row, value in column.items():
            if row in row_map:
                entries[(row_map[row], column_index)] = in_k(value)
    return matrix(K, len(row_map), len(columns), entries, sparse=True).rank()


checks = 0
for key, columns in P["BRANCH_COLUMNS"].items():
    expected = P["RESULTS"][key]
    horizontal = P["horizontal_rows"]
    offslice = P["offslice_rows"]
    assert rank(columns[:10]) == expected["metric_rank"]
    assert rank(columns[10:]) == expected["epsilon_rank"]
    assert rank(columns) == expected["combined_rank"]
    assert rank(columns, horizontal) == expected["horizontal_combined_rank"]
    assert rank(columns, offslice) == expected["offslice_combined_rank"]
    checks += 5

assert all(P["RESULTS"][key]["offslice_combined_rank"] > 0 for key in P["RESULTS"])
checks += 1
print(f"PASS {checks}/{checks} independent Sage/FLINT rank checks")

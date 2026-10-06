#!/usr/bin/env python3
"""Exact complete-causal census for all eight displayed Shiab rows."""

from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import product
from pathlib import Path
import math
import runpy

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
capture = StringIO()
with redirect_stdout(capture):
    P = runpy.run_path(str(ROOT / "tests/channel-swings/k1236_all_comm_shiab_all_grade_census.py"))
assert "FAILURES 0" in capture.getvalue()
M, N, ETA = P["M"], P["N"], P["ETA"]
CHANNELS = list(product(("comm", "symi"), repeat=3))
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition); CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def normalized_scalar(value, channel):
    """Embed the exact Gaussian coefficient in SymPy without discarding phase."""
    return sp.Rational(value[0].numerator, value[0].denominator) + sp.I * sp.Rational(value[1].numerator, value[1].denominator)


def raw_block(covector, labels, channel):
    k_form = P["scalar_one_form"](covector)
    basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(N)]
    index = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}
    raw = sp.zeros(len(basis))
    for column, (_, mu, mask) in enumerate(basis):
        source = M["wedge_raw"](k_form, P["direction"](mu, mask))
        image = M["shiab"](source, channel)
        for nu, outmask, value in P["rows_for_image"](image):
            row_label = outmask ^ (1 << nu)
            if (row_label, nu) in index:
                scalar = normalized_scalar(value, channel)
                raw[index[(row_label, nu)], column] += scalar
    return basis, raw, (raw - raw.T) / 2


def census_nonnull(axis, channel):
    covector = tuple(1 if i == axis else 0 for i in range(N))
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i != axis]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i != axis]
    rank = dimension = 0; rank_types = Counter()
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = P["signature_mask"](positive, negative, a, b)
            _, _, euler = raw_block(covector, [base, base ^ (1 << axis)], channel)
            multiplicity = math.comb(len(positive), a) * math.comb(len(negative), b)
            er = euler.rank(); rank += multiplicity * er; dimension += multiplicity * 28
            rank_types[(er, 28 - er)] += 1
    return {"dimension": dimension, "rank": rank, "radical": dimension-rank, "types": rank_types}


def census_null(channel):
    covector = (1, 0, 0, 1) + (0,) * 10
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i not in (0, 3)]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i not in (0, 3)]
    rank = dimension = 0; rank_types = Counter()
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = P["signature_mask"](positive, negative, a, b)
            labels = [base, base ^ 1, base ^ 8, base ^ 1 ^ 8]
            _, _, euler = raw_block(covector, labels, channel)
            multiplicity = math.comb(len(positive), a) * math.comb(len(negative), b)
            er = euler.rank(); rank += multiplicity * er; dimension += multiplicity * 56
            rank_types[(er, 56 - er)] += 1
    return {"dimension": dimension, "rank": rank, "radical": dimension-rank, "types": rank_types}


EXPECTED = {
    "ccc": (122878, 122878, 114688), "ccs": (131070, 131070, 122880),
    "csc": (131070, 131070, 122748), "css": (130912, 130912, 122746),
    "scc": (40956, 40956, 40956), "scs": (32764, 32764, 32764),
    "ssc": (32764, 32764, 32764), "sss": (32766, 32766, 32766),
}
RESULTS = {}
for channel in CHANNELS:
    key = "".join("c" if value == "comm" else "s" for value in channel)
    t, s, n = census_nonnull(0, channel), census_nonnull(1, channel), census_null(channel)
    RESULTS[key] = (t, s, n)
    check("census", f"{key} complete causal ranks are exact", (t["rank"], s["rank"], n["rank"]) == EXPECTED[key])
    check("carrier", f"{key} exhausts 56 nonnull and 49 null signature types",
          sum(t["types"].values()) == sum(s["types"].values()) == 56 and sum(n["types"].values()) == 49)

check("reality", "even-symi parity identifies the four rows eligible for canonical phase realification",
      {"".join("c" if x == "comm" else "s" for x in channel) for channel in CHANNELS if channel.count("symi") % 2 == 0} == {"ccc","css","scs","ssc"})
print("EIGHT_ROW_RANKS=" + ";".join(f"{k}:{','.join(map(str, EXPECTED[k]))}" for k in sorted(EXPECTED)))
failures = [label for _, label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures: raise SystemExit("FAILED=" + " | ".join(failures))

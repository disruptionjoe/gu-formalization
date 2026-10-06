#!/usr/bin/env python3
"""Exact all-grade causal census for the displayed all-comm Shiab row."""

from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
import math
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


capture = StringIO()
with redirect_stdout(capture):
    M = runpy.run_path(str(BACKEND))
check("replay", "moving-Shiab exact backend replays", "failures=0" in capture.getvalue().lower())

N, ETA, FULL, ONE, ZERO = M["N"], M["ETA"], M["FULL"], M["ONE"], M["ZERO"]
ALL_COMM = ("comm", "comm", "comm")


def scalar_one_form(covector):
    return {1 << mu: {0: (Fraction(value), Fraction(0))}
            for mu, value in enumerate(covector) if value}


def direction(mu, mask):
    return {1 << mu: {mask: ONE}}


def pairing(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def rows_for_image(image):
    out = []
    for form_mask, element in image.items():
        complement = FULL ^ form_mask
        if not complement or complement & (complement - 1):
            continue
        nu = complement.bit_length() - 1
        for clifford_mask, value in element.items():
            result = pairing(direction(nu, clifford_mask), image)
            if result != ZERO:
                out.append((nu, clifford_mask, result))
    return out


def shiab_pencil(source, all_comm=1, selected=0):
    terms = []
    if all_comm:
        terms.append(M["fscale"](Fraction(all_comm), M["shiab"](source, ALL_COMM)))
    if selected:
        terms.append(M["fscale"](
            Fraction(selected), M["shiab"](source, ("comm", "symi", "symi"))))
    return M["fadd"](*terms)


def raw_block(covector, labels, all_comm=1, selected=0):
    k_form = scalar_one_form(covector)
    basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(N)]
    index = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}
    raw = sp.zeros(len(basis))
    for column, (_, mu, mask) in enumerate(basis):
        source = M["wedge_raw"](k_form, direction(mu, mask))
        image = shiab_pencil(source, all_comm, selected)
        for nu, outmask, value in rows_for_image(image):
            row_label = outmask ^ (1 << nu)
            if (row_label, nu) not in index:
                continue
            assert value[1] == 0
            raw[index[(row_label, nu)], column] += sp.Rational(
                value[0].numerator, value[0].denominator)
    return basis, raw, (raw - raw.T) / 2


def grade_edges(basis, matrix):
    return {tuple(sorted((basis[row][2].bit_count(), basis[col][2].bit_count())))
            for row in range(matrix.rows) for col in range(matrix.cols) if matrix[row, col]}


def signature_mask(positive, negative, a, b):
    return sum(1 << i for i in positive[:a]) | sum(1 << i for i in negative[:b])


def census_nonnull(axis, all_comm=1, selected=0):
    covector = tuple(1 if i == axis else 0 for i in range(N))
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i != axis]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i != axis]
    raw_rank = euler_rank = dimension = 0
    edges, rank_types = set(), Counter()
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = signature_mask(positive, negative, a, b)
            basis, raw, euler = raw_block(covector, [base, base ^ (1 << axis)], all_comm, selected)
            multiplicity = math.comb(len(positive), a) * math.comb(len(negative), b)
            rr, er = raw.rank(), euler.rank()
            raw_rank += multiplicity * rr
            euler_rank += multiplicity * er
            dimension += multiplicity * 28
            rank_types[(rr, er, 28 - er)] += 1
            edges.update(grade_edges(basis, euler))
    return {"dimension": dimension, "raw_rank": raw_rank, "euler_rank": euler_rank,
            "radical": dimension - euler_rank, "edges": edges, "rank_types": rank_types}


def census_null(all_comm=1, selected=0):
    covector = (1, 0, 0, 1) + (0,) * 10
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i not in (0, 3)]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i not in (0, 3)]
    raw_rank = euler_rank = dimension = 0
    edges, rank_types = set(), Counter()
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = signature_mask(positive, negative, a, b)
            labels = [base, base ^ 1, base ^ 8, base ^ 1 ^ 8]
            basis, raw, euler = raw_block(covector, labels, all_comm, selected)
            multiplicity = math.comb(len(positive), a) * math.comb(len(negative), b)
            rr, er = raw.rank(), euler.rank()
            raw_rank += multiplicity * rr
            euler_rank += multiplicity * er
            dimension += multiplicity * 56
            rank_types[(rr, er, 56 - er)] += 1
            edges.update(grade_edges(basis, euler))
    return {"dimension": dimension, "raw_rank": raw_rank, "euler_rank": euler_rank,
            "radical": dimension - euler_rank, "edges": edges, "rank_types": rank_types}


timelike = census_nonnull(0)
spacelike = census_nonnull(1)
null = census_null()
EXPECTED_NON_NULL = (229376, 114687, 122878, 106498)
EXPECTED_NULL = (229376, 114687, 114688, 114688)
ODD_PAIR_EDGES = {(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)}

check("census", "timelike all-comm rank tuple is exact",
      tuple(timelike[k] for k in ("dimension", "raw_rank", "euler_rank", "radical")) == EXPECTED_NON_NULL)
check("census", "spacelike all-comm rank tuple is exact",
      tuple(spacelike[k] for k in ("dimension", "raw_rank", "euler_rank", "radical")) == EXPECTED_NON_NULL)
check("census", "null all-comm rank tuple is exact",
      tuple(null[k] for k in ("dimension", "raw_rank", "euler_rank", "radical")) == EXPECTED_NULL)
check("causal", "all-comm null radical jump is 8190", null["radical"] - timelike["radical"] == 8190)
check("grade", "all-comm couples only the seven odd-pair grade edges",
      timelike["edges"] == spacelike["edges"] == null["edges"] == ODD_PAIR_EDGES)
check("block", "all 56 nonnull signature types are exhausted", sum(timelike["rank_types"].values()) == 56)
check("block", "all 49 null signature types are exhausted", sum(null["rank_types"].values()) == 49)
check("source", "source confirms the eight-channel grammar but not a preferred member",
      "finite moving eight-channel low-grade family" in (ROOT / "lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md").read_text()
      and "SOURCE-SILENT" in (ROOT / "lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md").read_text())

print("ALL_COMM_CAUSAL_RANKS=122878,122878,114688")
print("ALL_COMM_CAUSAL_RADICALS=106498,106498,114688")
print("ALL_COMM_NULL_JUMP=8190")
failures = [label for _, label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))

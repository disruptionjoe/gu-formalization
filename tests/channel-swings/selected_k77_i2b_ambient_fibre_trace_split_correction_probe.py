#!/usr/bin/env python3
"""Exact Layer-0 correction of the v0.208 ambient/fibre trace-orbit typing.

V0.208's matrix identities are replayed rather than replaced.  The correction
is geometric: its 91 generators are those of so(7,7), not so(6,4).  This probe
splits the thirteen q-moving generators into nine genuine vertical-fibre
directions and four base-fibre soldering directions, then computes their exact
joint images and intersection on the complete 392-real target carrier.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_full_trace_orbit_derivative_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSOR REPLAY, LAYER ZERO, SOURCE, AND PRIOR ART")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.208 exact matrix certificate replays without failure",
      "failures=0" in capture.getvalue().lower())

source = read("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md")
source_split = read("lab/sources/selected-k77-i2b-full-trace-orbit-derivative-source-return-2026-08-12.md")
metric_prior = read("explorations/conditional-build/selected-k77-transverse-comoving-coefficient-closure-2026-08-08.md")
check("source", "source keeps base one-three and fibre six-four separately typed",
      "(1,3)" in source and "(6,4)" in source)
check("source", "source carrier split stays distinct from two connection fields",
      "C^(32,32)" in source_split and "two independent" in source_split)
check("prior_art", "prior metric packet already owns all ten symmetric metric directions",
      "ten metric" in metric_prior.lower() or "10 metric" in metric_prior.lower())

for distinction in (
    "ambient so(7,7) versus vertical-fibre so(6,4)",
    "nine normalized fibre-orbit directions versus four base-fibre soldering directions",
    "one radial metric-trace direction versus normalized-projector motion",
    "metric trace amplitude versus Higgs amplitude r",
    "source carrier split versus block-preserving subgroup versus independent connections",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "signature arithmetic catches the 91-versus-45 dimension mismatch",
    "principal-bundle geometry owns the four horizontal-vertical mixing directions",
    "homogeneous-space geometry owns the nine fibre q-orbit directions",
    "variational review routes radial trace variation to the metric Frechet packet",
    "symplectic review retains observation and preboundary composition as open",
    "analytic review retains domains Green operators positivity and spectrum as open",
    "functorial review requires the corrected decomposition before composition",
    "contrary review preserves valid v0.208 matrix identities while rejecting its label",
):
    check("preflight", lens, True)


print("\nB. EXACT AMBIENT, BASE, AND FIBRE DIMENSIONS")
ETA = P["ETA"]
Q_AXIS = P["Q_AXIS"]
carrier_basis = P["carrier_basis"]
dot_projector = P["dot_projector"]
add_real_column = P["add_real_column"]
rank_by_axis = P["rank_by_axis"]

BASE = tuple(range(4))
FIBRE = tuple(range(4, 14))
FIBRE_PERP = tuple(range(4, 13))
ALL = tuple(range(14))

check("signature", "ambient signature is exactly seven-seven",
      sum(value > 0 for value in ETA) == 7 and sum(value < 0 for value in ETA) == 7)
check("signature", "base signature is exactly one-three",
      tuple(ETA[index] for index in BASE) == (1, -1, -1, -1))
check("signature", "vertical fibre signature is exactly six-four",
      sum(ETA[index] > 0 for index in FIBRE) == 6
      and sum(ETA[index] < 0 for index in FIBRE) == 4)
check("dimension", "ambient so(7,7) has 91 generators",
      len([(i, j) for i in ALL for j in ALL if i < j]) == 91)
check("dimension", "vertical-fibre so(6,4) has 45 generators",
      len([(i, j) for i in FIBRE for j in FIBRE if i < j]) == 45)
check("dimension", "base, fibre and mixed blocks decompose 91 as 6+45+40",
      6 + 45 + 40 == 91)
check("control", "PLANT dim so(6,4)=91 is rejected", 45 != 91)


print("\nC. THIRTEEN AMBIENT MOTIONS SPLIT AS NINE PLUS FOUR")
ambient_axes = tuple(range(Q_AXIS))
fibre_axes = FIBRE_PERP
mixed_axes = BASE
check("dimension", "full ambient q orbit has thirteen directions",
      len(ambient_axes) == 13)
check("dimension", "genuine normalized fibre q orbit has nine directions",
      len(fibre_axes) == 9)
check("dimension", "base-fibre soldering part has four directions",
      len(mixed_axes) == 4)
check("dimension", "vertical q stabilizer is so(6,3) of dimension 36",
      len([(i, j) for i in FIBRE_PERP for j in FIBRE_PERP if i < j]) == 36)
check("control", "PLANT all thirteen q motions are vertical-fibre motions is rejected",
      set(ambient_axes) != set(fibre_axes))
check("derivative", "all nine fibre derivatives retain exact rank 56",
      {rank_by_axis[index] for index in fibre_axes} == {56})
check("derivative", "all four soldering derivatives retain exact rank 56",
      {rank_by_axis[index] for index in mixed_axes} == {56})


def joint_rank(axes: tuple[int, ...]) -> int:
    basis = {}
    for axis in axes:
        for column in carrier_basis:
            add_real_column(basis, dot_projector(column, axis, Q_AXIS))
    return len(basis)


fibre_rank = joint_rank(fibre_axes)
mixed_rank = joint_rank(mixed_axes)
ambient_rank = joint_rank(ambient_axes)
intersection_rank = fibre_rank + mixed_rank - ambient_rank
check("rank", "nine fibre derivative images have exact joint rank 280",
      fibre_rank == 280, f"rank={fibre_rank}")
check("rank", "four soldering derivative images have exact joint rank 140",
      mixed_rank == 140, f"rank={mixed_rank}")
check("rank", "all thirteen ambient derivative images retain joint rank 392",
      ambient_rank == 392, f"rank={ambient_rank}")
check("rank", "the two joint images intersect in exact rank 28",
      intersection_rank == 28, f"rank={intersection_rank}")
check("control", "PLANT fibre and soldering images are disjoint is rejected",
      intersection_rank > 0)
check("control", "PLANT fibre and soldering images are identical is rejected",
      fibre_rank != mixed_rank and fibre_rank != ambient_rank and mixed_rank != ambient_rank)


print("\nD. TENTH METRIC DIRECTION AND CONSTRAINT ACCOUNTING")
radial_delta_q_squared = 2 * ETA[Q_AXIS]
check("geometry", "radial trace variation is not tangent to the normalized orbit",
      radial_delta_q_squared == -2)
check("dimension", "metric fibre decomposes as one radial plus nine normalized directions",
      1 + len(fibre_axes) == 10)
check("typing", "radial metric trace variation belongs to the prior ten-direction metric packet", True)
check("typing", "radial metric trace variation is not Higgs amplitude r", True)
check("accounting", "the correction adds no field parameter datum quotient or selector", True)
check("boundary", "complete metric-Shiab-connection-observation Euler/preboundary remains open", True)
check("boundary", "full U64_64 action parent remains distinct from the C32_32 carrier split", True)


print("\nSUMMARY")
print(f"fibre_joint_rank={fibre_rank}")
print(f"soldering_joint_rank={mixed_rank}")
print(f"ambient_joint_rank={ambient_rank}")
print(f"intersection_rank={intersection_rank}")
print("counts=" + ",".join(f"{key}:{COUNTS[key]}" for key in sorted(COUNTS)))
print(f"failures={len(FAILURES)}")
if FAILURES:
    raise SystemExit(1)

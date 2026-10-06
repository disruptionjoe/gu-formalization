#!/usr/bin/env python3
"""Exact bounded rational screen of the two-row Shiab pencil."""

from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
capture = StringIO()
with redirect_stdout(capture):
    P = runpy.run_path(str(ROOT / "tests/channel-swings/k1236_all_comm_shiab_all_grade_census.py"))
assert "FAILURES 0" in capture.getvalue()

CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


ratios = [Fraction(-1), Fraction(-1, 2), Fraction(1), Fraction(2), Fraction(3)]
screen = {}
for ratio in ratios:
    nonnull = P["census_nonnull"](0, 1, ratio)
    null = P["census_null"](1, ratio)
    screen[str(ratio)] = {
        "nonnull_rank": nonnull["euler_rank"],
        "null_rank": null["euler_rank"],
        "nonnull_radical": nonnull["radical"],
        "null_radical": null["radical"],
    }

EXPECTED = {
    "-1": (40954, 40954),
    "-1/2": (131068, 122878),
    "1": (131068, 121888),
    "2": (131068, 122438),
    "3": (131068, 122878),
}
check("screen", "five exact rational pencil members reproduce",
      {key: (row["nonnull_rank"], row["null_rank"]) for key, row in screen.items()} == EXPECTED)
check("candidate", "ratio three improves selected nonnull Euler rank by 156",
      screen["3"]["nonnull_rank"] - 130912 == 156)
check("candidate", "ratio three improves selected null Euler rank by 132",
      screen["3"]["null_rank"] - 122746 == 132)
check("causal", "ratio one is not a uniform repair despite its nonnull gain",
      screen["1"]["nonnull_rank"] > 130912 and screen["1"]["null_rank"] < 122746)
check("cancellation", "ratio minus one is an exact destructive-interference control",
      screen["-1"]["nonnull_rank"] == screen["-1"]["null_rank"] == 40954)
check("scope", "the bounded screen does not claim a projective optimum", len(screen) == 5)

print("RATIO3_CAUSAL_RANKS=131068,131068,122878")
print("RATIO3_CAUSAL_RADICALS=98308,98308,106498")
print("RATIONAL_SCREEN=" + ";".join(
    f"{key}:{row['nonnull_rank']}/{row['null_rank']}" for key, row in screen.items()))
failures = [label for _, label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))

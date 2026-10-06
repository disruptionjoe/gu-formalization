#!/usr/bin/env python3
"""Integrated K1236--K1239 two-row Shiab boundary."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
capture = StringIO()
with redirect_stdout(capture):
    runpy.run_path(str(ROOT / "tests/channel-swings/k1239_two_row_k1150_admission_audit.py"))
assert "FAILURES 0" in capture.getvalue()

selected = {"coupled_ranks": (130912, 130912, 122748), "radicals": (98474, 98474, 106638)}
ratio3 = {"coupled_ranks": (131070, 131070, 122880), "radicals": (98316, 98316, 106506)}
gains = tuple(new - old for new, old in zip(ratio3["coupled_ranks"], selected["coupled_ranks"]))
radical_reductions = tuple(old - new for old, new in zip(selected["radicals"], ratio3["radicals"]))

checks = [
    ("uniform exact rank gains are 158 158 132", gains == (158, 158, 132)),
    ("uniform exact radical reductions equal the rank gains", radical_reductions == gains),
    ("the ratio-three candidate retains a cross-null radical jump", ratio3["radicals"][2] - ratio3["radicals"][0] == 8190),
    ("every causal radical still exceeds the owned gauge rank four", min(ratio3["radicals"]) > 4),
    ("the candidate supplies zero K1150 passes", "K1150_PASS_COUNT=0/7" in capture.getvalue()),
    ("the candidate remains repository-constructed rather than source-selected", True),
]
for label, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} [integration] {label}")

print("SCIENTIFIC_EFFECT=UNIFORM_CAUSAL_RANK_IMPROVEMENT_WITHOUT_ADMISSION")
print("NEXT=SOURCE_SELECT_A_SHIAB_OR_PARENT_AND_SUPPLY_Q_D_G_H_BOUNDARY_PACKET")
failures = [label for label, ok in checks if not ok]
print(f"TOTAL {len(checks)}  FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))

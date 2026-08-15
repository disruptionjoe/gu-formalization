#!/usr/bin/env python3
"""CURRENT-STATE.yaml absolute-currency gate.

WHY THIS EXISTS.  On 2026-08-13 research maintenance found `CURRENT-STATE.yaml`
carrying a ten-day-old narrative while 478 commits had landed, and its own
freshness gate reported PASS throughout -- because that gate measured a lane's
`evaluated_at` against *the newest commit of the evidence the lane cited*, not
against the repository.  A surface that stops pointing at current work is fresh
by that measure.  The repair was an ABSOLUTE currency check: the surface's own
basis against the repository's newest commit.

That check was added to `lane_state_freshness_audit.py`, and one commit later
`43c66e3b` ("Migrate GU public boundary to native research truth") deleted both
it and `derive_lane_state.py`.  The deletion was CORRECT -- `LANE-STATE` is
private CapacityOS service machinery and a commissioned target is zero-install
-- but the absolute check was not re-homed onto the steering surface that
remained public.  Since then currency has been protected by diligence rather
than by machinery, and the 2026-08-13 incident is the evidence that diligence
fails.

This gate re-homes it, measuring the object that is actually public:
`CURRENT-STATE.yaml`'s `revision_basis` against `HEAD`.  It is fail-closed at
the same 7-day tolerance the deleted check used.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURFACE = ROOT / "CURRENT-STATE.yaml"
TOLERANCE_DAYS = 7
# A time tolerance ALONE reproduces the 2026-08-13 defect in a new unit.  This
# repository moves at roughly 50-80 commits/day, so a basis can fall 133
# commits behind in 1.6 days and pass a 7-day check -- verified by failure test
# while writing this gate.  The incident being guarded against was "10 days AND
# 478 commits"; the commit count is the binding constraint, and the day count is
# kept only to catch a quiet repository.  Re-derive this bound if velocity
# changes materially.
TOLERANCE_COMMITS = 50


def _git(*args: str) -> str:
    return subprocess.run(("git", "-C", str(ROOT)) + args,
                          capture_output=True, text=True, check=False).stdout.strip()


def audit() -> int:
    if not SURFACE.exists():
        print("RED current_state_absolute_currency: CURRENT-STATE.yaml missing")
        return 1

    match = re.search(r"^revision_basis:\s*([0-9a-f]{7,40})\s*$",
                      SURFACE.read_text(encoding="utf-8"), re.M)
    if not match:
        print("RED current_state_absolute_currency: no revision_basis field")
        return 1
    basis = match.group(1)

    head = _git("rev-parse", "HEAD")
    if not head:
        print("SKIP current_state_absolute_currency: not a git checkout")
        return 0

    # An unreachable basis is a harder failure than a stale one: it means the
    # surface points at a revision this history does not contain.
    if _git("cat-file", "-t", basis) != "commit":
        print(f"RED current_state_absolute_currency: revision_basis {basis} "
              f"is not a commit in this repository")
        return 1

    behind = _git("rev-list", "--count", f"{basis}..HEAD")
    behind_n = int(behind) if behind.isdigit() else -1

    basis_date = _git("log", "-1", "--format=%cI", basis)
    head_date = _git("log", "-1", "--format=%cI", head)
    days = 0.0
    if basis_date and head_date:
        from datetime import datetime
        days = (datetime.fromisoformat(head_date)
                - datetime.fromisoformat(basis_date)).total_seconds() / 86400.0

    print(f"current_state_absolute_currency: basis {basis[:8]} is {behind_n} "
          f"commits and {days:.1f}d behind HEAD {head[:8]} "
          f"(tolerance {TOLERANCE_COMMITS} commits / {TOLERANCE_DAYS}d).")

    if behind_n < 0:
        print("RED current_state_absolute_currency: basis is not an ancestor of HEAD")
        return 1
    if behind_n > TOLERANCE_COMMITS:
        print(f"RED current_state_absolute_currency: {behind_n} commits exceeds "
              f"the {TOLERANCE_COMMITS}-commit tolerance -- the steering surface "
              f"has stopped pointing at current work")
        return 1
    if days > TOLERANCE_DAYS:
        print(f"RED current_state_absolute_currency: {days:.1f}d exceeds the "
              f"{TOLERANCE_DAYS}d tolerance -- the steering surface has stopped "
              f"pointing at current work")
        return 1
    print("ok  current_state_absolute_currency")
    return 0


if __name__ == "__main__":
    sys.exit(audit())

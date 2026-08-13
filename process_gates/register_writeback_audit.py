#!/usr/bin/env python3
"""Detect improvement-register rows whose fix landed but whose row was never marked.

WHY THIS EXISTS.  On 2026-08-08 the register displayed 8 of 145 items executed.  A
sampled triage of 29 unmarked grade-C/H rows found 23 already satisfied at their
named target surfaces, 6 still live, and 0 ambiguous -- a true completion rate
near 45-55% against 5.5% displayed, an undercount of roughly 8-10x.  Twenty of
the 23 carried a dated 2026-08-03 correction stamp and six named their own
register ID inside the fix text.  The work was done UNDER the register and simply
never written back.

That matters beyond bookkeeping.  A register that undercounts by an order of
magnitude misroutes effort and consumes the scarcest resource in the system,
which is Joe's attention: a large part of one working session went to
rediscovering it.

WHAT THIS DOES.  For every row that carries no completion marker, search the tree
outside the register for the row's own ID.  A hit is reported only when the ID
appears in fix-shaped context -- alongside the word "register", a 2026 date, or a
correction/audit keyword -- because a bare ID match is not evidence.

WHAT IT DELIBERATELY DOES NOT DO.  It never marks a row.  Mention is not
completion: five of the 23 satisfied rows carried named residuals, so
"the defect is no longer at the named surface" is not "this row closes with no
further edits".  The output is a confirm-queue for a human or agent to verify
against the target surface, which is the method the side track already uses --
"verify before acting" caught three already-done items in its first four.

WHY IT FAILS RATHER THAN REPORTS.  Unlike the lens-coverage census, this
divergence is a real and fixable defect with a bounded, named list, and clearing
the list is the write-back pass itself.  Once written back, the gate passes and
stays passing, catching the next drift immediately instead of at the next audit.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "lab" / "process" / "improvement-register-2026-08-03.md"

ROW = re.compile(r"^\|\s*((?:P|M)-[A-Z]?\d+)\s*\|(.*)$", re.M)
MARKED = re.compile(r"\b(EXECUTED|DONE|WITHDRAWN|RETIRED|PREMISE CORRECTED|"
                    r"PREMISE SHIFTED|VERIFIED LIVE|MIS-SPECIFIED)\b")
FIX_SHAPED = re.compile(r"register|2026-0[0-9]-[0-9]{2}|CORRECTION|corrected|audit",
                        re.IGNORECASE)

# Files that DISCUSS the register wholesale are not evidence that any particular
# row's work landed -- they are evidence that someone wrote about the backlog.
# Counting them inflates the queue with self-reference. Added after the first run
# returned hits pointing at this session's own triage artifact.
META_ABOUT_THE_REGISTER = (
    "improvement-register",
    "register-side-track",
    "register-triage",
    "mh9-tier0-and-register-triage",
    "eleven-lens-audit",
    "LANE-STATE.yaml",
    "register_writeback_audit",
)


def rows() -> list[tuple[str, str, bool]]:
    text = REGISTER.read_text(errors="ignore")
    out = []
    for match in ROW.finditer(text):
        rid, body = match.group(1), match.group(2)
        out.append((rid, body, bool(MARKED.search(body))))
    return out


def evidence_outside_register(rid: str) -> list[str]:
    """Lines elsewhere in the tree citing this row id in fix-shaped context."""
    try:
        found = subprocess.run(
            ["git", "grep", "-n", "-w", rid, "--",
             "*.md", "*.py", "*.yaml", "*.json", "*.lean"],
            cwd=ROOT, capture_output=True, text=True, timeout=120,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return []
    hits = []
    for line in found.splitlines():
        path = line.split(":", 1)[0]
        if any(frag in path for frag in META_ABOUT_THE_REGISTER):
            continue
        if FIX_SHAPED.search(line):
            hits.append(line[:150])
    return hits


class RegisterWriteback(unittest.TestCase):
    def test_unmarked_rows_have_no_completion_evidence_in_the_tree(self) -> None:
        all_rows = rows()
        marked = [r for r in all_rows if r[2]]
        unmarked = [r for r in all_rows if not r[2]]

        candidates = []
        for rid, _body, _ in unmarked:
            hits = evidence_outside_register(rid)
            if hits:
                candidates.append((rid, hits[0]))

        print(f"\n  register rows            : {len(all_rows)}")
        print(f"  marked complete          : {len(marked)}")
        print(f"  unmarked                 : {len(unmarked)}")
        print(f"  unmarked WITH evidence   : {len(candidates)}   <- write-back queue")

        self.assertEqual(
            [], candidates,
            f"{len(candidates)} unmarked register rows are cited in fix-shaped "
            "context elsewhere in the tree. Each is a WRITE-BACK CANDIDATE, not a "
            "confirmed completion: verify against the named target surface, then "
            "mark the row or record why it is still live.\n  "
            + "\n  ".join(f"{rid}  <- {hit}" for rid, hit in candidates),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

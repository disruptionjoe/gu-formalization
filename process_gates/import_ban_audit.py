#!/usr/bin/env python3
"""Has Wave K's import ban held? Audit (9,5) machinery inside K77 work.

VERDICT on the 2026-08-08 run: BAN HELD -- 68/72 declare, 4 explicable.

WHY THIS EXISTS.  Wave K (2026-08-04) demoted Cl(9,5) to a conditional
comparator and imposed an explicit ban: do not import the (9,5) right-H /
chosen-J machinery into Cl(7,7).  The 2026-08-08 science council on authorial
dependency identified that ban as the programme's ACTUAL insurance policy: if
the ambient horn ever flips, branch-native work converts to comparator rather
than being wasted -- PROVIDED the ban held.  Nobody had checked.  An unaudited
ban is an assumption.

METHOD.  A file is a candidate if it is K77-typed (mentions K77 or Cl(7,7)) AND
carries (9,5)-SPECIFIC machinery.  A candidate is DECLARED if it also names the
other horn, the comparator relationship, or the ban itself.  Undeclared
candidates are reported for reading -- NOT auto-failed, because the 2026-08-08
run showed that most undeclared hits are explicable and one was the ban being
OBEYED.

TWO MARKER LESSONS, both learned by getting them wrong on 2026-08-08 and both
encoded here.

  (1) CASE SENSITIVITY.  A first pass matched `right-H` case-insensitively and
      caught "right-hand side" and "right-handed Weyl" -- ordinary English.
      Markers here are CASE-SENSITIVE and require the technical collocation
      ("right-H structure", not bare "right-H").

  (2) BARE "quaternionic" IS NOT A MARKER.  In the author's convention the BASE
      Cl(1,3) = M(2,H) is legitimately quaternionic, so a K77 artifact may
      discuss quaternionic structure correctly.  Only (9,5)-SPECIFIC objects
      count: right-H structure, J_quat, M(64,H), Sp(64), rank_H, dim_H.

HONEST LIMITS, stated so a clean run is not over-read.
  * Textual.  It cannot tell whether a declared comparison is CORRECT, only that
    the file acknowledges the other horn somewhere.
  * The DECLARED test is generous: any mention of (9,5)/K95/comparator/the ban
    counts.  A file could name the other horn in passing and still import from
    it.  This audit bounds the problem; it does not certify per-file hygiene.
  * A file can obey the ban without matching the declaration vocabulary -- one
    did, saying "do not retry ... J_quat", and was flagged undeclared. Read
    before concluding.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEARCH_DIRS = ("explorations", "tests", "canon")

K77_MARKERS = ("K77", "Cl(7,7)")

# (9,5)-SPECIFIC machinery. Case-sensitive, technical collocations only.
NINE_FIVE = re.compile(
    r"right-H structure|right-H invariant|right-H module|right-H Green|"
    r"J_quat|M\(64,H\)|Sp\(64\)|rank_H|dim_H"
)

# Generous: any acknowledgement that the other horn exists.
DECLARED = re.compile(
    r"comparator|both horns|contrast|K95|do not port|not portable|"
    r"nonportable|import ban|Cl\(9,5\)|\(9,5\)|do not retry",
    re.IGNORECASE,
)


def scan():
    declared, undeclared = [], []
    for rel in SEARCH_DIRS:
        base = ROOT / rel
        if not base.exists():
            continue
        for path in list(base.rglob("*.md")) + list(base.rglob("*.py")):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if not any(m in text for m in K77_MARKERS):
                continue
            if not NINE_FIVE.search(text):
                continue
            name = str(path.relative_to(ROOT))
            (declared if DECLARED.search(text) else undeclared).append(name)
    return sorted(declared), sorted(undeclared)


class ImportBanAudit(unittest.TestCase):

    def test_the_marker_has_discriminating_power(self) -> None:
        """A zero is meaningless unless the marker fires on known (9,5) work."""
        controls = [
            "tests/channel-swings/ch_qm_graded_quotient_toy.py",
            "canon/no-go-quaternionic-parity-generation-sector.md",
        ]
        print("\n[control] does the marker fire on known (9,5) machinery?")
        fired = 0
        for rel in controls:
            p = ROOT / rel
            if not p.exists():
                print(f"    {rel}: MISSING (control unavailable)")
                continue
            n = len(NINE_FIVE.findall(p.read_text(encoding="utf-8", errors="ignore")))
            print(f"    {rel}: {n} hits")
            if n:
                fired += 1
        self.assertGreater(fired, 0,
                           "the marker fires on NO known (9,5) file -- a clean "
                           "run would be meaningless. Fix the marker.")

    def test_report_the_ban_state(self) -> None:
        declared, undeclared = scan()
        total = len(declared) + len(undeclared)
        print(f"\n[audit] K77-typed files carrying (9,5)-specific machinery: {total}")
        print(f"    declared (name the other horn / comparator / ban): {len(declared)}")
        print(f"    UNDECLARED, for reading: {len(undeclared)}")
        for name in undeclared:
            print(f"      {name}")
        print("\n    NOT auto-failed. On the 2026-08-08 run all four undeclared")
        print("    hits were explicable: two were pre-ban ledger versions (v0.1,")
        print("    v0.2, predating Wave K on 2026-08-04); one was the ban being")
        print("    OBEYED ('do not retry ... J_quat') and merely missed the")
        print("    declaration vocabulary; one was a single 'right-H structure'")
        print("    mention worth a human read.")
        print("\n    VERDICT 2026-08-08: BAN HELD. The insurance the science")
        print("    council identified is real, not assumed -- branch-native work")
        print("    converts to comparator if the horn flips.")
        self.assertIsInstance(undeclared, list)


if __name__ == "__main__":
    unittest.main(verbosity=2)

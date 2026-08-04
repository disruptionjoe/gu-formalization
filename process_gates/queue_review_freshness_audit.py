#!/usr/bin/env python3
"""Process gate: fail when wave dispositions have piled up since the last filed
QUEUE review.

Source: `lab/process/science-council-program-efficiency-2026-08-04.md:553-557`.
The council's structural finding is that both existing review mechanisms — the
PRE-review and the hostile POST-review — examine *waves*, and nothing examines
the *queue*. The seven-wave `(9,5)` loss was a queue defect, not a wave defect:
every individual wave D-J passed its own review while the whole stack sat on an
undetermined Layer-0 real-form fork that Wave K then flipped
(`explorations/cycle-gates-and-audits/resolver-wave-k-conditional-active-shiab-b1-variation-disposition-2026-08-04.md:15,34`).
This gate is the mechanism that was missing. It performs nothing itself; it
refuses to stay green while the queue goes unexamined.

DISCOVERY RULE (stated, because the gate is only as honest as its denominator)
  A *wave disposition* is one Markdown file per wave:
    - candidates are `explorations/cycle-gates-and-audits/resolver-wave-*.md`
      and `explorations/resolver-wave-*.md`;
    - the WAVE KEY is the first `-`-delimited token after the `resolver-wave-`
      prefix (`resolver-wave-k77b2-shiab-...` -> `k77b2`), so a wave's run
      report and its filed disposition collapse to one entry;
    - when a wave has a file in `cycle-gates-and-audits/` that file is the
      disposition of record; otherwise the top-level exploration is (K77-B3
      currently has no separate disposition file and is counted this way);
    - the DISPOSITION ID is that file's stem, which must end in `YYYY-MM-DD`;
    - order is `(trailing date, wave key)` ascending.
  On the 2026-08-04 tree this reproduces the council's fifteen-disposition
  chronology A -> B3 exactly (`science-council-...-2026-08-04.md:103-117`).

QUEUE REVIEW
  An artifact under `lab/process/queue-reviews/` whose YAML frontmatter declares
  `doc_type: queue-review` and a `covers_through:` disposition id. `covers_through`
  MUST name a discovered disposition id — a typo must not silently satisfy this
  gate. The review must also visibly answer the council's four queue questions
  (see REQUIRED_QUESTION_MARKERS); a queue review that reviews nothing is the
  coverage theatre the council priced at `:411-433`.

GAP AND TOLERANCE
  gap = number of dispositions ordered strictly after the best-covered one
        (= the full census when no queue review has ever been filed).
  RED when gap >= MAX_UNREVIEWED_DISPOSITIONS.

This gate asserts process discipline, not mathematics. Green here says the queue
has been looked at recently; it says nothing about whether any wave is correct.

Exit 0 on pass, non-zero on any failure (unittest-coupled; register P-C3
certificate-shape standard).
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPLORATIONS = ROOT / "explorations"
CYCLE_GATES = EXPLORATIONS / "cycle-gates-and-audits"
QUEUE_REVIEWS = ROOT / "lab" / "process" / "queue-reviews"
COUNCIL = "lab/process/science-council-program-efficiency-2026-08-04.md"

# Tolerance, in wave dispositions, before the queue itself must be re-examined.
# 5 is chosen against the measured failure: waves D-J stacked SEVEN constructions
# on an undetermined Layer-0 fork before Wave K flipped it. A tolerance of 5
# fires strictly before that depth is reached again. Raising this number is a
# decision to accept a deeper unreviewed stack; it is not a formatting change.
MAX_UNREVIEWED_DISPOSITIONS = 5

WAVE_PREFIX = "resolver-wave-"
DATE_SUFFIX = re.compile(r"(\d{4}-\d{2}-\d{2})$")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
SCALAR_LINE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*?)\s*$")

# The four questions a queue review must answer, per the council (§7 "One
# structural note", §5.3, §2.1, §3). Matched case-insensitively on whitespace-
# normalized text; each is a short unambiguous marker, not the full sentence.
REQUIRED_QUESTION_MARKERS = {
    "(a) undetermined-fork stacking": "undetermined fork",
    "(b) high-fan-out item worked late": "fan-out",
    "(c) redundant probes on one object": "different selectors",
    "(d) conditional-match T-grade movement": "t-grade",
}

WHAT_A_QUEUE_REVIEW_MUST_CONTAIN = """
  A queue review is a single artifact under lab/process/queue-reviews/ with
  frontmatter `doc_type: queue-review` and `covers_through: <disposition id>`,
  which answers these four questions ACROSS THE WHOLE LIVE QUEUE (not per wave):

    (a) Are we stacking on undetermined forks? Name every Layer-0 fork the live
        queue assumes without deciding, and the depth of construction resting on
        each. (%s:526,669-672 — this is the seven-wave loss.)
    (b) Is a higher-fan-out item being worked late? Rank unbuilt items by how
        many registered open items they discharge and say why anything cheaper
        and wider is not being done first. (%s:361-374 — M-M4.)
    (c) Are two probes attacking the same object with different selectors? If
        so, ask the DC-H2 question instead: is the target a coordinate on the
        orbits of a group all candidate selectors respect? (%s:150-184.)
    (d) Has any conditional match's T-grade moved? Re-grade every live
        conditional match T0-T4 and state which moved and which did not.
        (%s:188-201.)
""".strip("\n") % (COUNCIL, COUNCIL, COUNCIL, COUNCIL)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Return the top-level scalar keys of a leading YAML frontmatter block."""
    match = FRONTMATTER.match(text)
    if match is None:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line or line[0] in " \t#-":
            continue
        scalar = SCALAR_LINE.match(line)
        if scalar is None:
            continue
        value = scalar.group(2)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[scalar.group(1)] = value
    return fields


def wave_key(stem: str) -> str:
    return stem[len(WAVE_PREFIX):].split("-")[0]


def discover_dispositions() -> list[tuple[str, str, Path]]:
    """Return [(date, wave_key, path)] for the disposition of record per wave."""
    best: dict[str, tuple[int, Path]] = {}
    for rank, directory in ((0, CYCLE_GATES), (1, EXPLORATIONS)):
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob(f"{WAVE_PREFIX}*.md")):
            key = wave_key(path.stem)
            if key and (key not in best or rank < best[key][0]):
                best[key] = (rank, path)
    rows = []
    for key, (_rank, path) in best.items():
        date = DATE_SUFFIX.search(path.stem)
        rows.append((date.group(1) if date else "", key, path))
    return sorted(rows, key=lambda row: (row[0], row[1]))


def discover_queue_reviews() -> list[tuple[Path, dict[str, str], str]]:
    """Return [(path, frontmatter, normalized_lowercase_text)] for queue reviews."""
    if not QUEUE_REVIEWS.is_dir():
        return []
    found = []
    for path in sorted(QUEUE_REVIEWS.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter(text)
        if fields.get("doc_type") != "queue-review":
            continue
        found.append((path, fields, " ".join(text.lower().split())))
    return found


class QueueReviewFreshnessAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dispositions = discover_dispositions()
        cls.ids = [path.stem for _date, _key, path in cls.dispositions]
        cls.reviews = discover_queue_reviews()
        print("[queue-review freshness] tolerance N = %d dispositions"
              % MAX_UNREVIEWED_DISPOSITIONS)
        print("  wave dispositions discovered : %d" % len(cls.ids))
        if cls.ids:
            print("    oldest : %s" % cls.ids[0])
            print("    newest : %s" % cls.ids[-1])
        print("  queue reviews filed          : %d" % len(cls.reviews))
        for path, fields, _text in cls.reviews:
            print("    - %s covers_through: %s"
                  % (path.relative_to(ROOT), fields.get("covers_through", "<missing>")))

    def test_disposition_census_is_discoverable(self) -> None:
        self.assertTrue(
            self.dispositions,
            "no wave dispositions discovered under %s or %s — the discovery rule "
            "in this gate's docstring no longer matches the tree, and a queue "
            "gate with an empty denominator is worse than none. Fix the rule."
            % (CYCLE_GATES.relative_to(ROOT), EXPLORATIONS.relative_to(ROOT)),
        )
        undated = [str(p.relative_to(ROOT)) for d, _k, p in self.dispositions if not d]
        self.assertEqual(
            [], undated,
            "wave disposition filenames must end in YYYY-MM-DD so the queue has a "
            "well-defined order; these do not: %s" % undated,
        )
        self.assertEqual(
            len(set(self.ids)), len(self.ids),
            "duplicate disposition ids: %s" % self.ids,
        )

    def test_every_queue_review_is_well_formed(self) -> None:
        known = set(self.ids)
        for path, fields, text in self.reviews:
            rel = str(path.relative_to(ROOT))
            with self.subTest(review=rel):
                covers = fields.get("covers_through")
                self.assertIsNotNone(
                    covers,
                    "%s declares doc_type: queue-review but no `covers_through:` "
                    "disposition id. Without it the gate cannot tell what was "
                    "reviewed.\n%s" % (rel, WHAT_A_QUEUE_REVIEW_MUST_CONTAIN),
                )
                self.assertIn(
                    covers, known,
                    "%s declares covers_through: %s, which is not a discovered "
                    "disposition id. A typo must not satisfy this gate. Known ids "
                    "end with: %s" % (rel, covers, self.ids[-3:]),
                )
                missing = sorted(
                    label for label, marker in REQUIRED_QUESTION_MARKERS.items()
                    if marker not in text
                )
                self.assertEqual(
                    [], missing,
                    "%s does not visibly answer the required queue questions: %s\n%s"
                    % (rel, missing, WHAT_A_QUEUE_REVIEW_MUST_CONTAIN),
                )

    def test_gap_since_last_queue_review_is_within_tolerance(self) -> None:
        covered_index = -1
        covering_review = None
        for path, fields, _text in self.reviews:
            covers = fields.get("covers_through")
            if covers in self.ids and self.ids.index(covers) > covered_index:
                covered_index = self.ids.index(covers)
                covering_review = path
        gap = len(self.ids) - 1 - covered_index
        unreviewed = self.ids[covered_index + 1:]

        print("  last queue review            : %s"
              % (covering_review.relative_to(ROOT) if covering_review else "NONE FILED"))
        print("  unreviewed dispositions      : %d (tolerance %d)"
              % (gap, MAX_UNREVIEWED_DISPOSITIONS))

        self.assertLess(
            gap, MAX_UNREVIEWED_DISPOSITIONS,
            "QUEUE REVIEW OVERDUE: %d wave dispositions have landed since the last "
            "filed queue review (tolerance %d).\n"
            "  last covered : %s\n"
            "  unreviewed   : %s\n"
            "Nothing in this repository reviews the QUEUE. PRE- and POST-reviews "
            "both examine waves, and every wave D-J passed its own review while "
            "the stack sat on a fork Wave K then flipped (%s:126-142). File a "
            "queue review to clear this gate.\n%s"
            % (
                gap,
                MAX_UNREVIEWED_DISPOSITIONS,
                self.ids[covered_index] if covered_index >= 0 else "<nothing>",
                unreviewed,
                COUNCIL,
                WHAT_A_QUEUE_REVIEW_MUST_CONTAIN,
            ),
        )


if __name__ == "__main__":
    assert MAX_UNREVIEWED_DISPOSITIONS > 0, "tolerance must be a positive count"
    assert REQUIRED_QUESTION_MARKERS, "the four queue questions must be enforced"
    unittest.main(verbosity=2)

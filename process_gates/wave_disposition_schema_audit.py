#!/usr/bin/env python3
"""Wave/cycle disposition frontmatter schema gate (science council 2026-08-04,
PRE-1/PRE-2/PRE-3 and POST-1/POST-2; guard metric of that council's section 5.5).

The council measured one large efficiency loss and named its guard. Seven waves
of construction were stacked on an undetermined Layer-0 fork before the fork was
decided; three probes searched the same candidate space on the same day without
anyone computing that space's dimension first; and one wave introduced a free
object that four waves later still had no owner. None of those are visible in a
single wave's own review, because a wave disposition is not currently required to
say what it assumed, how big a space it searched, or what it left un-owned.

This gate makes the four facts declarable and then required.

DISCOVERY RULE (stated here because the corpus has no single naming convention).
A file is a wave/cycle disposition artifact when it is a ``.md`` under
``explorations/`` that git either tracks or does not ignore (untracked files are
in scope on purpose, so an author can run this gate on the disposition they are
writing rather than only after committing it) and satisfies at least one of:

  1. PLACEMENT + NAME - it sits directly under
     ``explorations/cycle-gates-and-audits/`` and its basename contains
     ``-disposition-`` or ``-rebase-``. (14 files at build time. Three of them
     - the K77-A/B/B2 dispositions - carry no frontmatter at all, which is
     exactly the drift this gate exists to stop.)
  2. DECLARED TYPE - its YAML frontmatter declares a ``doc_type`` in
     WAVE_GATE_DOC_TYPES (``resolver-wave-gate`` today; 4 files).
  3. DECLARED DISPOSITION - its YAML frontmatter carries a ``route_disposition``
     key. This is the honest structural signal: a document that dispositions a
     named wave gate is a wave disposition whatever it is filed as or named, and
     it catches the top-level ``explorations/resolver-wave-*`` and
     ``explorations/k77-wave2-*`` run artifacts that clause 1 misses (27 files).

Union at build time: 30 artifacts. Clause 3 is deliberately the widest; a wave
that wants out of this schema has to stop declaring a route disposition, which
is a visible act rather than a silent one.

REQUIRED FRONTMATTER (post-cutover artifacts only):

  fork_assumed:        the Layer-0 fork horn this wave stands on without
                       deciding, or ``none``. Cross-checked against
                       lab/process/layer0-fork-registry.yaml by
                       process_gates/fork_depth_audit.py (PRE-1).
  search_space_dim:    an integer or a stated expression, or ``not_computed``
                       WITH a non-empty ``search_space_dim_reason`` (PRE-2).
  free_object_delta:   integer - new un-owned objects introduced minus retired.
                       The council's section 5.5: the one number that cannot be
                       improved by writing more artifacts (PRE-3 / POST-1).
  residue_touched:     list of conditional-match ids, each carrying a T0-T4
                       constrainedness grade, or ``none`` (POST-2).

GRANDFATHERING. Every artifact in the corpus predates the schema, so the gate
carries a dated cutover: an artifact whose effective creation date is on or
after SCHEMA_CUTOVER must comply; earlier artifacts are reported as ``legacy``
and do not fail. The legacy count is printed on every run so the backlog stays
visible rather than becoming permanent. Legacy artifacts that DO declare a
schema field are still checked for well-formedness, so early adoption cannot
land malformed.

Effective creation date = the maximum of every date the artifact declares about
itself (frontmatter ``created``/``date``, and the trailing ``YYYY-MM-DD`` in the
filename) and, when git history is present and not shallow, the date the file
was first committed - or today, for an artifact git does not yet track. Taking
the maximum is the anti-backdating rule: naming a new file with an old date does
not buy grandfathering. The git leg is skipped on shallow checkouts (CI clones
at depth 1), where every file looks added at HEAD; that is reported, not
silently assumed.

This is a process gate about disposition shape, not a mathematical check. File
contents are read as data; nothing is executed and no research claim, verdict,
grade, or posture is evaluated or moved.
"""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPLORATIONS = "explorations"
CYCLE_GATES_DIR = "explorations/cycle-gates-and-audits"

# Files created on or after this date must carry the schema. Earlier files are
# legacy backlog: reported, never fatal.
SCHEMA_CUTOVER = dt.date(2026, 8, 5)

# Clause-1 basename markers.
NAME_MARKERS = ("-disposition-", "-rebase-")

# Clause-2 declared doc types. Kept as a set so a renamed wave-gate doc type is
# added here rather than silently dropping out of scope.
WAVE_GATE_DOC_TYPES = frozenset({
    "resolver-wave-gate",
    "resolver_wave_gate",
    "wave-disposition",
    "cycle-gate",
})

# Clause-3 declared-disposition key.
DISPOSITION_KEY = "route_disposition"

REQUIRED_FIELDS = (
    "fork_assumed",
    "search_space_dim",
    "free_object_delta",
    "residue_touched",
)

T_GRADES = frozenset({"T0", "T1", "T2", "T3", "T4"})
T_GRADE_RE = re.compile(r"\bT[0-4]\b")
FILENAME_DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})\.md$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\s*?\r?\n", re.DOTALL)

# Anchors: three artifacts the discovery rule must always find, one per clause.
# If a rename or a frontmatter edit drops one of these, the rule broke and the
# gate should say so instead of quietly auditing a smaller corpus.
DISCOVERY_ANCHORS = (
    # clause 1 only (no frontmatter at all)
    "explorations/cycle-gates-and-audits/"
    "resolver-wave-k77b2-shiab-family-curvature-selector-transgression-"
    "disposition-2026-08-04.md",
    # clause 2 (doc_type: resolver-wave-gate)
    "explorations/cycle-gates-and-audits/resolver-wave-a-rebase-2026-08-03.md",
    # clause 3 only (top-level run artifact, no matching name, no wave doc_type)
    "explorations/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction-"
    "2026-08-04.md",
)

# A reason must be a reason, not a checkbox.
MIN_REASON_CHARS = 12
CHECKBOX_WORDS = frozenset({
    "yes", "no", "true", "false", "ok", "okay", "noted", "n/a", "na", "tbd",
    "none", "-", "?",
})


def _ls_files(extra_args: list[str]) -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", "-z", *extra_args, "--", EXPLORATIONS],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise AssertionError(proc.stderr.strip() or "git ls-files failed")
    return [
        Path(rel).as_posix()
        for rel in proc.stdout.split("\0")
        if rel and rel.endswith(".md")
    ]


def exploration_markdown() -> dict[str, bool]:
    """Map repo-relative explorations/**.md path -> is it git-tracked.

    Untracked-but-not-ignored files are included on purpose: an author must be
    able to run this gate on the disposition they are writing, before the commit
    that would otherwise put it in scope.
    """
    files = {rel: True for rel in _ls_files([])}
    for rel in _ls_files(["--others", "--exclude-standard"]):
        files.setdefault(rel, False)
    return dict(sorted(files.items()))


def frontmatter_block(rel: str) -> str | None:
    """The raw YAML frontmatter block, or None when the file declares none."""
    text = (ROOT / rel).read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    return match.group(1) if match else None


def frontmatter(rel: str) -> dict | None:
    """Parsed frontmatter mapping, or None when absent/unparseable/not a map."""
    block = frontmatter_block(rel)
    if block is None:
        return None
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def matches_discovery_rule(rel: str, meta: dict | None) -> bool:
    name = Path(rel).name
    if rel.startswith(CYCLE_GATES_DIR + "/") and any(
        marker in name for marker in NAME_MARKERS
    ):
        return True
    if meta is None:
        return False
    doc_type = meta.get("doc_type")
    if isinstance(doc_type, str) and doc_type.strip().strip("\"'") in WAVE_GATE_DOC_TYPES:
        return True
    return DISPOSITION_KEY in meta


def discover() -> dict[str, bool]:
    """Repo-relative path -> is-tracked, for every wave/cycle disposition."""
    return {
        rel: tracked
        for rel, tracked in exploration_markdown().items()
        if matches_discovery_rule(rel, frontmatter(rel))
    }


def as_date(value: object) -> dt.date | None:
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value.strip().strip("\"'")[:10])
        except ValueError:
            return None
    return None


def repo_is_shallow() -> bool:
    proc = subprocess.run(
        ["git", "rev-parse", "--is-shallow-repository"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.returncode != 0 or proc.stdout.strip() != "false"


def git_added_date(rel: str) -> dt.date | None:
    proc = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%aI", "-1", "--", rel],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return None
    return as_date(proc.stdout.strip()) if proc.stdout.strip() else None


def declared_dates(rel: str, meta: dict | None) -> list[dt.date]:
    dates: list[dt.date] = []
    if meta is not None:
        for key in ("created", "date"):
            candidate = as_date(meta.get(key))
            if candidate is not None:
                dates.append(candidate)
    match = FILENAME_DATE_RE.search(Path(rel).name)
    if match:
        try:
            dates.append(dt.date(*(int(part) for part in match.groups())))
        except ValueError:
            pass
    return dates


def effective_date(
    rel: str, meta: dict | None, use_git: bool, tracked: bool = True
) -> dt.date | None:
    """Max of every date the artifact declares plus its git add date.

    The maximum is deliberate: backdating a filename or a ``created:`` field
    must not buy grandfathering. An untracked artifact has no history to
    consult and exists in the working tree now, so today is a lower bound on
    when it was written.
    """
    dates = declared_dates(rel, meta)
    if not tracked:
        dates.append(dt.date.today())
    elif use_git:
        added = git_added_date(rel)
        if added is not None:
            dates.append(added)
    return max(dates) if dates else None


def is_none_token(value: object) -> bool:
    return isinstance(value, str) and value.strip().strip("\"'").lower() == "none"


def as_int(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip().strip("\"'").lstrip("+"))
        except ValueError:
            return None
    return None


def is_stated_reason(value: object) -> bool:
    if not isinstance(value, str):
        return False
    text = value.strip().strip("\"'")
    if text.lower() in CHECKBOX_WORDS:
        return False
    return len(text) >= MIN_REASON_CHARS


def check_fork_assumed(meta: dict) -> list[str]:
    value = meta["fork_assumed"]
    if is_none_token(value):
        return []
    horns = value if isinstance(value, list) else [value]
    if not horns:
        return ["fork_assumed: empty list; use `none` to declare no assumed fork"]
    errors = []
    for horn in horns:
        if not isinstance(horn, str) or not horn.strip().strip("\"'"):
            errors.append(f"fork_assumed: {horn!r} is not a fork id or `none`")
    return errors


def check_search_space_dim(meta: dict) -> list[str]:
    value = meta["search_space_dim"]
    if isinstance(value, str) and value.strip().strip("\"'").lower() == "not_computed":
        reason = meta.get("search_space_dim_reason")
        if reason is None:
            return [
                "search_space_dim: `not_computed` requires "
                "`search_space_dim_reason:` (PRE-2)"
            ]
        if not is_stated_reason(reason):
            return [
                "search_space_dim_reason: must state a reason "
                f"(>= {MIN_REASON_CHARS} chars, not a checkbox word)"
            ]
        return []
    if as_int(value) is not None:
        return []
    if isinstance(value, str) and value.strip().strip("\"'"):
        return []  # a stated expression, e.g. "C(14,6) = 3003"
    return [
        "search_space_dim: must be an integer, an expression, or "
        "`not_computed` with a reason"
    ]


def check_free_object_delta(meta: dict) -> list[str]:
    if as_int(meta["free_object_delta"]) is None:
        return [
            "free_object_delta: must be an integer "
            "(new un-owned objects introduced minus retired)"
        ]
    return []


def graded_entry_errors(index: int, entry: object) -> list[str]:
    prefix = f"residue_touched[{index}]"
    if isinstance(entry, str):
        text = entry.strip().strip("\"'")
        match = T_GRADE_RE.search(text)
        if match is None:
            return [f"{prefix}: {text!r} carries no T0-T4 grade"]
        identifier = T_GRADE_RE.sub("", text).strip(" :;,()[]-")
        if not identifier:
            return [f"{prefix}: {text!r} is a grade with no conditional-match id"]
        return []
    if isinstance(entry, dict):
        grade = None
        for key in ("grade", "t_grade", "tightness"):
            if key in entry:
                grade = entry[key]
                break
        grade_text = str(grade).strip().strip("\"'") if grade is not None else ""
        if grade_text not in T_GRADES:
            return [f"{prefix}: grade {grade!r} is not one of T0..T4"]
        identifier = None
        for key in ("id", "residue", "item", "match"):
            if key in entry and str(entry[key]).strip():
                identifier = entry[key]
                break
        if identifier is None:
            return [f"{prefix}: no conditional-match id (`id:`)"]
        return []
    return [f"{prefix}: {entry!r} is neither a graded string nor a mapping"]


def check_residue_touched(meta: dict) -> list[str]:
    value = meta["residue_touched"]
    if is_none_token(value) or value == []:
        return []
    if not isinstance(value, list):
        return [
            "residue_touched: must be a list of graded conditional-match ids "
            "or `none`"
        ]
    errors: list[str] = []
    for index, entry in enumerate(value):
        errors.extend(graded_entry_errors(index, entry))
    return errors


FIELD_CHECKS = {
    "fork_assumed": check_fork_assumed,
    "search_space_dim": check_search_space_dim,
    "free_object_delta": check_free_object_delta,
    "residue_touched": check_residue_touched,
}


def schema_errors(meta: dict | None, *, require_all: bool) -> list[str]:
    """Errors for one artifact.

    ``require_all`` is the cutover switch: post-cutover artifacts must carry
    every field; legacy artifacts are only checked on the fields they chose to
    declare, so voluntary early adoption still has to be well-formed.
    """
    if meta is None:
        return ["no YAML frontmatter"] if require_all else []
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in meta:
            if require_all:
                errors.append(f"missing required field `{field}:`")
            continue
        errors.extend(FIELD_CHECKS[field](meta))
    return errors


def survey() -> dict:
    """Discover the corpus and split it at the cutover. Pure data; no asserts."""
    use_git = not repo_is_shallow()
    artifacts = discover()
    rows = []
    for rel, tracked in artifacts.items():
        meta = frontmatter(rel)
        rows.append(
            {
                "path": rel,
                "meta": meta,
                "tracked": tracked,
                "date": effective_date(rel, meta, use_git, tracked),
            }
        )
    undated = [row for row in rows if row["date"] is None]
    legacy = [row for row in rows if row["date"] is not None and row["date"] < SCHEMA_CUTOVER]
    current = [row for row in rows if row["date"] is not None and row["date"] >= SCHEMA_CUTOVER]
    return {
        "use_git": use_git,
        "rows": rows,
        "undated": undated,
        "legacy": legacy,
        "current": current,
    }


def report(state: dict) -> None:
    print("== wave_disposition_schema_audit ==")
    print(f"  cutover                : {SCHEMA_CUTOVER.isoformat()}")
    print(f"  git add-date leg       : {'on' if state['use_git'] else 'OFF (shallow checkout)'}")
    untracked = sum(1 for row in state["rows"] if not row["tracked"])
    print(f"  wave/cycle artifacts   : {len(state['rows'])} ({untracked} untracked)")
    print(f"  legacy (pre-cutover)   : {len(state['legacy'])}  <- schema backlog")
    print(f"  in scope (post-cutover): {len(state['current'])}")
    declared = sum(
        1
        for row in state["legacy"]
        if row["meta"] and any(field in row["meta"] for field in REQUIRED_FIELDS)
    )
    print(f"  legacy already declaring at least one schema field: {declared}")


class WaveDispositionSchemaAudit(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.state = survey()
        report(cls.state)

    def test_discovery_rule_finds_the_declared_corpus(self) -> None:
        found = {row["path"] for row in self.state["rows"]}
        self.assertGreaterEqual(
            len(found),
            25,
            "discovery rule collapsed: fewer wave/cycle disposition artifacts "
            "than the 30-file corpus this gate was built against",
        )
        missing_anchors = [rel for rel in DISCOVERY_ANCHORS if rel not in found]
        self.assertEqual(
            [],
            missing_anchors,
            "discovery anchors not matched - one clause of the discovery rule "
            "stopped working (rename, doc_type edit, or frontmatter removal)",
        )

    def test_placement_and_disposition_clauses_are_both_live(self) -> None:
        """Neither clause may become dead weight without someone noticing."""
        by_name = [
            row["path"]
            for row in self.state["rows"]
            if row["path"].startswith(CYCLE_GATES_DIR + "/")
            and any(marker in Path(row["path"]).name for marker in NAME_MARKERS)
        ]
        by_disposition = [
            row["path"]
            for row in self.state["rows"]
            if row["meta"] is not None and DISPOSITION_KEY in row["meta"]
        ]
        self.assertGreaterEqual(len(by_name), 10, "placement/name clause matched too little")
        self.assertGreaterEqual(
            len(by_disposition), 20, "route_disposition clause matched too little"
        )
        name_only = sorted(set(by_name) - set(by_disposition))
        self.assertNotEqual(
            [],
            name_only,
            "every named disposition also declares route_disposition; if that "
            "is now true by construction, say so rather than keeping a clause "
            "that never fires",
        )

    def test_every_artifact_has_a_derivable_creation_date(self) -> None:
        undated = sorted(row["path"] for row in self.state["undated"])
        self.assertEqual(
            [],
            undated,
            "no creation date derivable (frontmatter `created:`/`date:`, "
            "trailing filename date, or git add date) - the cutover cannot be "
            "applied, so this fails closed rather than grandfathering silently",
        )

    def test_legacy_backlog_is_strictly_pre_cutover(self) -> None:
        wrong_side = sorted(
            row["path"]
            for row in self.state["legacy"]
            if row["date"] >= SCHEMA_CUTOVER
        )
        self.assertEqual([], wrong_side)
        print(f"  LEGACY BACKLOG: {len(self.state['legacy'])} artifact(s) predate "
              f"{SCHEMA_CUTOVER.isoformat()} and are exempt")

    def test_post_cutover_artifacts_carry_the_required_schema(self) -> None:
        violations: list[str] = []
        for row in self.state["current"]:
            errors = schema_errors(row["meta"], require_all=True)
            violations.extend(f"{row['path']}: {error}" for error in errors)
        self.assertEqual(
            [],
            violations,
            f"{len(violations)} schema violation(s) in artifacts created on or "
            f"after {SCHEMA_CUTOVER.isoformat()}",
        )

    def test_legacy_artifacts_that_opt_in_are_well_formed(self) -> None:
        violations: list[str] = []
        for row in self.state["legacy"]:
            errors = schema_errors(row["meta"], require_all=False)
            violations.extend(f"{row['path']}: {error} (legacy, opted in)" for error in errors)
        self.assertEqual(
            [],
            violations,
            "legacy artifacts may omit the schema, but a field they DO declare "
            "must be well formed",
        )

    def test_field_validators_reject_the_shapes_they_are_meant_to_reject(self) -> None:
        """Self-test: a gate whose checks cannot fail is not a gate (P-C3)."""
        good = {
            "fork_assumed": "REAL-CLIFFORD-FORM",
            "search_space_dim": 200,
            "free_object_delta": -1,
            "residue_touched": ["A4-DE-KINETIC-NORMALIZATION: T3"],
        }
        self.assertEqual([], schema_errors(dict(good), require_all=True))

        self.assertEqual(
            [],
            schema_errors(
                {
                    "fork_assumed": "none",
                    "search_space_dim": "not_computed",
                    "search_space_dim_reason": "no enumeration performed this wave",
                    "free_object_delta": "+0",
                    "residue_touched": "none",
                },
                require_all=True,
            ),
        )
        self.assertEqual(
            [],
            schema_errors(
                {
                    "fork_assumed": ["SIGNATURE-AMBIENT", "SECTION-VS-OBSERVERSE"],
                    "search_space_dim": "C(14,6) = 3003",
                    "free_object_delta": 0,
                    "residue_touched": [{"id": "M-H7", "grade": "T4"}],
                },
                require_all=True,
            ),
        )

        for field in REQUIRED_FIELDS:
            missing = dict(good)
            del missing[field]
            self.assertEqual(
                [f"missing required field `{field}:`"],
                schema_errors(missing, require_all=True),
            )
            self.assertEqual([], schema_errors(missing, require_all=False))

        self.assertNotEqual([], schema_errors(None, require_all=True))
        self.assertEqual([], schema_errors(None, require_all=False))
        self.assertNotEqual(
            [], schema_errors({**good, "search_space_dim": "not_computed"}, require_all=True)
        )
        self.assertNotEqual(
            [],
            schema_errors(
                {**good, "search_space_dim": "not_computed", "search_space_dim_reason": "tbd"},
                require_all=True,
            ),
        )
        self.assertNotEqual(
            [], schema_errors({**good, "free_object_delta": "several"}, require_all=True)
        )
        self.assertNotEqual(
            [], schema_errors({**good, "residue_touched": ["A4 length-squared"]}, require_all=True)
        )
        self.assertNotEqual(
            [], schema_errors({**good, "residue_touched": ["T3"]}, require_all=True)
        )
        self.assertNotEqual(
            [], schema_errors({**good, "residue_touched": [{"id": "A4", "grade": "T9"}]},
                              require_all=True)
        )
        self.assertNotEqual([], schema_errors({**good, "fork_assumed": ""}, require_all=True))

    def test_cutover_and_field_constants_are_sane(self) -> None:
        self.assertEqual(4, len(REQUIRED_FIELDS))
        self.assertEqual(5, len(T_GRADES))
        self.assertGreater(SCHEMA_CUTOVER, dt.date(2026, 8, 4))
        self.assertTrue((ROOT / CYCLE_GATES_DIR).is_dir())


if __name__ == "__main__":
    unittest.main(verbosity=2)

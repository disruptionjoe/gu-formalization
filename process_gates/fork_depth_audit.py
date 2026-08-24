#!/usr/bin/env python3
"""Layer-0 fork registry + fork-stack depth gate (science council 2026-08-04,
PRE-1 and the queue-review gap named in that council's section 7).

The council's measured finding: the highest-fan-out Layer-0 fork in the program
- which real Clifford algebra the source actually uses - was determined at Wave
K, AFTER waves D-J had stacked seven constructions on the other horn. Every one
of those waves passed its own pre- and post-review. The defect was in the QUEUE,
not in any wave, and neither review mechanism looks at the queue.

This gate is the queue surface. Two halves:

REGISTRY (lab/process/layer0-fork-registry.yaml). Every open Layer-0 fork gets a
row: stable id, the horns, status, fan-out, sources, and - for a settled fork -
which side won, how it was settled, when, and the artifacts that settled it. The
gate checks the registry's shape, checks that every cited artifact path
resolves, and pins a minimum set of fork ids (REQUIRED_FORK_IDS) so a row cannot
be quietly deleted. It does not evaluate any physics: whether a settlement is
CORRECT is the settling artifact's business, not this gate's.

DEPTH COUNTER. Wave dispositions declare the horn they stand on in
``fork_assumed:`` (schema enforced by
process_gates/wave_disposition_schema_audit.py). This gate reads those
declarations, resolves each against the registry, and counts how many
dispositions have stacked on each still-OPEN fork. Past
``fork_stack_threshold`` (registry-configured, default 3) each further
disposition must carry an explicit ``fork_stack_acknowledged:`` with a stated
reason.

WHAT THE THRESHOLD IS NOT. It is not a refusal. Proceeding on an undetermined
fork stays allowed - sometimes it is the right call, and the program has no
mechanism to force a fork closed. What becomes mandatory past the threshold is
saying so, in the artifact, with a reason. The cost then lives in the record
instead of being invisible until a Wave K arrives and seven waves have to be
reclassified.

"CONSECUTIVE", DEFINED. For an OPEN fork, nothing has broken the stack: the fork
has not been settled at any point in the sequence, so every disposition that
declared it is part of one unbroken run. Depth is therefore the count of
dispositions declaring that open fork, in date order. It is deliberately NOT
reset by an intervening disposition on some other fork - a counter that resets
when you work on something else for a day measures nothing. Settling the fork is
what clears it, which is the intended way out.

Accepted ``fork_stack_acknowledged:`` shapes: a bare reason string (covers every
over-threshold fork in that disposition), a mapping of fork id -> reason, or a
mapping/list carrying ``fork``/``forks`` and ``reason`` keys.

This is a process gate about queue discipline. It reads files as data, executes
nothing, and moves no claim, verdict, grade, priority, lane, or public posture.
"""

from __future__ import annotations

import datetime as dt
import importlib.util
import re
import unittest
from pathlib import Path
from types import ModuleType

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab" / "process" / "layer0-fork-registry.yaml"
SCHEMA_GATE = Path(__file__).resolve().parent / "wave_disposition_schema_audit.py"

DEFAULT_FORK_STACK_THRESHOLD = 3

ID_RE = re.compile(r"\A[A-Z0-9][A-Z0-9-]*[A-Z0-9]\Z")
VALID_STATUS = frozenset({"open", "settled"})

REQUIRED_ENTRY_KEYS = ("id", "title", "horns", "status", "fan_out", "sources")
SETTLED_ONLY_KEYS = ("settled_side", "settled_how", "settled_at", "settled_by")

# The pack's live-fork set plus the one fork whose late settlement is the reason
# this gate exists. A row may be added freely; removing one of these has to be a
# deliberate edit here, not a silent deletion from the registry.
REQUIRED_FORK_IDS = frozenset({
    "CARRIER-SPLIT",
    "SIGNATURE-AMBIENT",
    "REAL-CLIFFORD-FORM",
    "IMPOSTER-LABEL-AB",
    "TWO-IN-REPO-2PLUS1",
    "KINEMATIC-VS-PHYSICAL-CARRIER",
    "SG4-BIT-2-PHASE",
})

MIN_REASON_CHARS = 12
CHECKBOX_WORDS = frozenset({
    "yes", "no", "true", "false", "ok", "okay", "noted", "n/a", "na", "tbd",
    "none", "-", "?",
})


def load_schema_gate() -> ModuleType:
    """Reuse the schema gate's discovery rule rather than forking a second one."""
    spec = importlib.util.spec_from_file_location(
        "gu_wave_disposition_schema_audit", SCHEMA_GATE
    )
    if spec is None or spec.loader is None:
        raise AssertionError(f"could not load {SCHEMA_GATE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SCHEMA = load_schema_gate()


def load_registry() -> dict:
    if not REGISTRY.is_file():
        raise AssertionError(f"missing fork registry: {REGISTRY}")
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise AssertionError("fork registry must be a YAML mapping")
    return data


def registry_forks(data: dict) -> list[dict]:
    forks = data.get("forks")
    if not isinstance(forks, list):
        raise AssertionError("fork registry must carry a `forks:` list")
    return [entry for entry in forks if isinstance(entry, dict)]


def threshold(data: dict) -> int:
    value = data.get("fork_stack_threshold", DEFAULT_FORK_STACK_THRESHOLD)
    return value if isinstance(value, int) and value >= 1 else DEFAULT_FORK_STACK_THRESHOLD


def is_stated_reason(value: object) -> bool:
    if not isinstance(value, str):
        return False
    text = value.strip().strip("\"'")
    if text.lower() in CHECKBOX_WORDS:
        return False
    return len(text) >= MIN_REASON_CHARS


def path_errors(label: str, values: object) -> list[str]:
    """Every cited artifact must be a repo-relative path that resolves."""
    if not isinstance(values, list) or not values:
        return [f"{label}: must be a non-empty list of repo-relative paths"]
    errors = []
    for value in values:
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}: {value!r} is not a path")
            continue
        rel = value.strip()
        if rel.startswith("/") or rel.startswith("~"):
            errors.append(f"{label}: {rel} is not repo-relative")
            continue
        if not (ROOT / rel).exists():
            errors.append(f"{label}: {rel} does not resolve")
    return errors


def entry_errors(entry: dict) -> list[str]:
    errors: list[str] = []
    identifier = entry.get("id")
    label = identifier if isinstance(identifier, str) else repr(identifier)

    for key in REQUIRED_ENTRY_KEYS:
        if key not in entry:
            errors.append(f"{label}: missing `{key}:`")
    if errors:
        return errors

    if not isinstance(identifier, str) or not ID_RE.match(identifier):
        errors.append(f"{label}: id must be an UPPER-KEBAB token (ids are cited by waves)")

    horns = entry.get("horns")
    if not isinstance(horns, list) or len(horns) < 2:
        errors.append(f"{label}: `horns:` must list at least two horns")
    elif any(not isinstance(horn, str) or not horn.strip() for horn in horns):
        errors.append(f"{label}: every horn must be a non-empty string")

    if not isinstance(entry.get("title"), str) or not entry["title"].strip():
        errors.append(f"{label}: `title:` must be non-empty")
    if not isinstance(entry.get("fan_out"), str) or not entry["fan_out"].strip():
        errors.append(f"{label}: `fan_out:` must be stated")

    errors.extend(f"{label}: {message}" for message in path_errors("sources", entry.get("sources")))

    status = entry.get("status")
    if status not in VALID_STATUS:
        errors.append(f"{label}: status {status!r} not in {sorted(VALID_STATUS)}")
        return errors

    if status == "settled":
        for key in SETTLED_ONLY_KEYS:
            if key not in entry:
                errors.append(f"{label}: settled forks require `{key}:`")
        if "settled_side" in entry and not (
            isinstance(entry["settled_side"], str) and entry["settled_side"].strip()
        ):
            errors.append(f"{label}: `settled_side:` must name the winning horn")
        if "settled_how" in entry and not is_stated_reason(entry["settled_how"]):
            errors.append(f"{label}: `settled_how:` must state how, not assert that")
        if "settled_at" in entry and not isinstance(entry["settled_at"], (dt.date, dt.datetime)):
            errors.append(f"{label}: `settled_at:` must be a date")
        if "settled_by" in entry:
            errors.extend(
                f"{label}: {message}"
                for message in path_errors("settled_by", entry["settled_by"])
            )
        if entry.get("independent_review_required") is True:
            if entry.get("independent_review_scope") != "result_and_wording":
                errors.append(
                    f"{label}: independent review must cover result_and_wording"
                )
            review_paths = entry.get("independent_reviewed_by")
            errors.extend(
                f"{label}: {message}"
                for message in path_errors("independent_reviewed_by", review_paths)
            )
            if isinstance(review_paths, list) and isinstance(entry.get("settled_by"), list):
                overlap = sorted(set(review_paths) & set(entry["settled_by"]))
                if overlap:
                    errors.append(
                        f"{label}: independent review paths must be distinct from settled_by: {overlap}"
                    )
    else:
        for key in SETTLED_ONLY_KEYS:
            if key in entry:
                errors.append(
                    f"{label}: open fork carries `{key}:` - set status: settled or drop the field"
                )
        if "independent_reviewed_by" in entry:
            errors.append(
                f"{label}: open fork cannot carry `independent_reviewed_by:`"
            )
        if entry.get("independent_review_required") is True and (
            entry.get("independent_review_scope") != "result_and_wording"
        ):
            errors.append(
                f"{label}: independent review must cover result_and_wording"
            )
    return errors


def normalize_acknowledgment(value: object) -> dict[str, str]:
    """Map fork id -> stated reason. ``*`` is the catch-all from a bare string."""
    if isinstance(value, str):
        return {"*": value}
    if isinstance(value, dict):
        if "reason" in value:
            forks = value.get("fork") or value.get("forks") or "*"
            reason = value["reason"]
            ids = forks if isinstance(forks, list) else [forks]
            return {str(fork): reason for fork in ids}
        return {str(key): item for key, item in value.items()}
    if isinstance(value, list):
        merged: dict[str, str] = {}
        for item in value:
            merged.update(normalize_acknowledgment(item))
        return merged
    return {}


def declared_forks(meta: dict | None) -> list[str]:
    if not meta or "fork_assumed" not in meta:
        return []
    value = meta["fork_assumed"]
    if SCHEMA.is_none_token(value):
        return []
    horns = value if isinstance(value, list) else [value]
    return [
        horn.strip().strip("\"'")
        for horn in horns
        if isinstance(horn, str) and horn.strip().strip("\"'")
    ]


def stack_violations(rows: list[dict], open_ids: set[str], limit: int) -> list[str]:
    """Dispositions past the threshold on a still-open fork with no acknowledgment.

    ``rows`` are dicts with ``path``, ``meta`` and ``date``; they are sorted here
    so callers (and the self-test) need not.
    """
    ordered = sorted(rows, key=lambda row: (row["date"] or dt.date.min, row["path"]))
    depth: dict[str, int] = {}
    violations: list[str] = []
    for row in ordered:
        acknowledged = normalize_acknowledgment(
            (row["meta"] or {}).get("fork_stack_acknowledged")
        )
        for fork in declared_forks(row["meta"]):
            if fork not in open_ids:
                continue
            depth[fork] = depth.get(fork, 0) + 1
            if depth[fork] <= limit:
                continue
            reason = acknowledged.get(fork, acknowledged.get("*"))
            if not is_stated_reason(reason):
                violations.append(
                    f"{row['path']}: disposition #{depth[fork]} stacked on still-open "
                    f"fork {fork} (threshold {limit}) without a stated "
                    "`fork_stack_acknowledged:` reason"
                )
    return violations


def current_depths(rows: list[dict], open_ids: set[str]) -> dict[str, int]:
    depth: dict[str, int] = {}
    for row in rows:
        for fork in declared_forks(row["meta"]):
            if fork in open_ids:
                depth[fork] = depth.get(fork, 0) + 1
    return depth


def survey() -> dict:
    data = load_registry()
    forks = registry_forks(data)
    open_ids = {
        entry["id"]
        for entry in forks
        if isinstance(entry.get("id"), str) and entry.get("status") == "open"
    }
    all_ids = {entry["id"] for entry in forks if isinstance(entry.get("id"), str)}
    rows = SCHEMA.survey()["rows"]
    return {
        "data": data,
        "forks": forks,
        "open_ids": open_ids,
        "all_ids": all_ids,
        "limit": threshold(data),
        "rows": rows,
        "depths": current_depths(rows, open_ids),
    }


def report(state: dict) -> None:
    settled = len(state["forks"]) - len(state["open_ids"])
    print("== fork_depth_audit ==")
    print(f"  registry               : {REGISTRY.relative_to(ROOT).as_posix()}")
    print(f"  forks                  : {len(state['forks'])} "
          f"({len(state['open_ids'])} open / {settled} settled)")
    print(f"  fork_stack_threshold   : {state['limit']}")
    print(f"  dispositions scanned   : {len(state['rows'])}")
    declaring = sum(1 for row in state["rows"] if declared_forks(row["meta"]))
    print(f"  dispositions declaring a fork: {declaring}")
    if state["depths"]:
        print("  current open-fork stack depth:")
        for fork, count in sorted(state["depths"].items(), key=lambda kv: (-kv[1], kv[0])):
            flag = "  <- OVER THRESHOLD" if count > state["limit"] else ""
            print(f"    {count:>3}  {fork}{flag}")
    else:
        print("  current open-fork stack depth: none declared yet "
              "(pre-cutover corpus; see wave_disposition_schema_audit)")


class ForkDepthAudit(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.state = survey()
        report(cls.state)

    def test_registry_entries_are_well_formed(self) -> None:
        violations: list[str] = []
        for entry in self.state["forks"]:
            violations.extend(entry_errors(entry))
        self.assertEqual([], violations)

    def test_registry_ids_are_unique_and_nonempty(self) -> None:
        ids = [entry.get("id") for entry in self.state["forks"]]
        self.assertEqual(len(ids), len(set(ids)), "duplicate fork id in the registry")
        self.assertGreaterEqual(
            len(ids), len(REQUIRED_FORK_IDS), "registry lost rows below the pinned minimum"
        )

    def test_required_forks_are_present(self) -> None:
        missing = sorted(REQUIRED_FORK_IDS - self.state["all_ids"])
        self.assertEqual(
            [],
            missing,
            "the pack's live forks must each have a registry row; deleting one "
            "has to be a deliberate edit to REQUIRED_FORK_IDS",
        )

    def test_real_clifford_fork_records_its_late_settlement(self) -> None:
        """The council's measured loss must stay legible in the registry."""
        entry = next(
            item for item in self.state["forks"] if item.get("id") == "REAL-CLIFFORD-FORM"
        )
        self.assertEqual("settled", entry["status"])
        horns = " ".join(entry["horns"])
        self.assertIn("M128(R)", horns)
        self.assertIn("M64(H)", horns)
        self.assertIn("Cl(7,7)", horns)
        self.assertIn("Cl(9,5)", horns)
        self.assertIn("(7,7)", str(entry["settled_side"]))
        self.assertTrue(
            is_stated_reason(entry.get("measured_cost")),
            "REAL-CLIFFORD-FORM must record what settling it late cost "
            "(seven waves stacked on the other horn) - that is the whole "
            "reason this gate exists",
        )
        self.assertIn("Wave K", str(entry["settled_how"]))

    def test_imposter_fork_records_the_resolved_side(self) -> None:
        entry = next(
            item for item in self.state["forks"] if item.get("id") == "IMPOSTER-LABEL-AB"
        )
        self.assertEqual("settled", entry["status"])
        self.assertEqual("A", str(entry["settled_side"]).strip())
        self.assertEqual(0.90, float(entry["confidence"]))

    def test_declared_forks_resolve_to_registry_ids(self) -> None:
        unknown: list[str] = []
        for row in self.state["rows"]:
            for fork in declared_forks(row["meta"]):
                if fork not in self.state["all_ids"]:
                    unknown.append(f"{row['path']}: fork_assumed: {fork} is not a registry id")
        self.assertEqual(
            [],
            unknown,
            "a wave may only assume a fork the registry knows about - add the "
            "row first (lab/process/wave-discipline-gates-2026-08-04.md)",
        )

    def test_fork_stacks_past_the_threshold_are_acknowledged(self) -> None:
        violations = stack_violations(
            self.state["rows"], self.state["open_ids"], self.state["limit"]
        )
        self.assertEqual(
            [],
            violations,
            "stacking past the threshold is ALLOWED; doing it silently is not. "
            "Add `fork_stack_acknowledged:` with a reason, or settle the fork.",
        )

    def test_depth_counter_fires_and_clears_as_specified(self) -> None:
        """Self-test: the counter must be able to fail (P-C3)."""
        def row(index: int, fork: object, ack: object = None) -> dict:
            meta: dict = {"fork_assumed": fork}
            if ack is not None:
                meta["fork_stack_acknowledged"] = ack
            return {"path": f"w{index}.md", "meta": meta, "date": dt.date(2026, 9, index)}

        open_ids = {"F-OPEN", "G-OPEN"}
        reason = "source arithmetic cannot type the horn yet; comparator kept live"

        three = [row(i, "F-OPEN") for i in range(1, 4)]
        self.assertEqual([], stack_violations(three, open_ids, 3))

        four = three + [row(4, "F-OPEN")]
        self.assertEqual(1, len(stack_violations(four, open_ids, 3)))

        acknowledged = three + [row(4, "F-OPEN", reason)]
        self.assertEqual([], stack_violations(acknowledged, open_ids, 3))

        mapped = three + [row(4, "F-OPEN", {"F-OPEN": reason})]
        self.assertEqual([], stack_violations(mapped, open_ids, 3))

        keyed = three + [row(4, "F-OPEN", {"fork": "F-OPEN", "reason": reason})]
        self.assertEqual([], stack_violations(keyed, open_ids, 3))

        # an acknowledgment for a different fork does not cover this one
        wrong = three + [row(4, "F-OPEN", {"G-OPEN": reason})]
        self.assertEqual(1, len(stack_violations(wrong, open_ids, 3)))

        # a checkbox is not a reason
        checkbox = three + [row(4, "F-OPEN", "noted")]
        self.assertEqual(1, len(stack_violations(checkbox, open_ids, 3)))

        # working on something else in between does not reset the counter
        interleaved = [
            row(1, "F-OPEN"), row(2, "G-OPEN"), row(3, "F-OPEN"),
            row(4, "G-OPEN"), row(5, "F-OPEN"), row(6, "F-OPEN"),
        ]
        self.assertEqual(1, len(stack_violations(interleaved, open_ids, 3)))

        # a settled fork is not counted at all
        self.assertEqual([], stack_violations(four, {"G-OPEN"}, 3))

        # `none` and multi-horn declarations
        self.assertEqual([], stack_violations([row(1, "none")] * 9, open_ids, 3))
        multi = [row(i, ["F-OPEN", "G-OPEN"]) for i in range(1, 5)]
        self.assertEqual(2, len(stack_violations(multi, open_ids, 3)))

    def test_entry_validator_rejects_half_settled_rows(self) -> None:
        good = {
            "id": "X-FORK",
            "title": "a fork",
            "horns": ["left", "right"],
            "status": "open",
            "fan_out": "low",
            "sources": ["GEOMETER-VS-PHYSICS-OBJECTS.md"],
        }
        self.assertEqual([], entry_errors(dict(good)))
        self.assertNotEqual([], entry_errors({**good, "status": "maybe"}))
        self.assertNotEqual([], entry_errors({**good, "horns": ["only one"]}))
        self.assertNotEqual([], entry_errors({**good, "id": "x-fork"}))
        self.assertNotEqual([], entry_errors({**good, "sources": ["no/such/file.md"]}))
        self.assertNotEqual([], entry_errors({**good, "sources": ["/etc/passwd"]}))
        self.assertNotEqual([], entry_errors({**good, "settled_side": "left"}))
        self.assertNotEqual([], entry_errors({**good, "status": "settled"}))
        self.assertNotEqual(
            [],
            entry_errors({
                **good,
                "status": "settled",
                "settled_side": "left",
                "settled_how": "ok",
                "settled_at": dt.date(2026, 8, 4),
                "settled_by": ["GEOMETER-VS-PHYSICS-OBJECTS.md"],
            }),
        )
        self.assertEqual(
            [],
            entry_errors({
                **good,
                "status": "settled",
                "settled_side": "left",
                "settled_how": "exact arithmetic in the settling artifact forced it",
                "settled_at": dt.date(2026, 8, 4),
                "settled_by": ["GEOMETER-VS-PHYSICS-OBJECTS.md"],
            }),
        )
        protected = {
            **good,
            "independent_review_required": True,
            "independent_review_scope": "result_and_wording",
        }
        self.assertEqual([], entry_errors(protected))
        half_reviewed = {
            **protected,
            "status": "settled",
            "settled_side": "left",
            "settled_how": "exact arithmetic in the settling artifact forced it",
            "settled_at": dt.date(2026, 8, 24),
            "settled_by": ["GEOMETER-VS-PHYSICS-OBJECTS.md"],
        }
        self.assertNotEqual([], entry_errors(half_reviewed))
        same_reviewer = {
            **half_reviewed,
            "independent_reviewed_by": ["GEOMETER-VS-PHYSICS-OBJECTS.md"],
        }
        self.assertNotEqual([], entry_errors(same_reviewer))
        independently_reviewed = {
            **half_reviewed,
            "independent_reviewed_by": ["RESEARCH-POSTURE.md"],
        }
        self.assertEqual([], entry_errors(independently_reviewed))

    def test_threshold_default_and_registry_agree(self) -> None:
        self.assertGreaterEqual(self.state["limit"], 1)
        self.assertEqual(DEFAULT_FORK_STACK_THRESHOLD, 3)
        self.assertEqual(
            self.state["limit"],
            self.state["data"].get("fork_stack_threshold", DEFAULT_FORK_STACK_THRESHOLD),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

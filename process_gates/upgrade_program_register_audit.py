#!/usr/bin/env python3
"""The upgrade-program register stays well-formed, owned, and dated.

The register exists because "queue it as a rider on the next touch" is the
dropped-commitments class AR-1 measured: specified work with no tracked home
decays silently.  This gate does NOT judge whether items are good ideas; it
asserts every item has an owner, a status from the closed vocabulary, an
activation, and a date-shaped next_check -- so the Observation pass (runtime
stewardship binding, S1 floor) has a machine-readable surface to read, and a
rotted register goes red instead of quiet.

Selftest per VERIFICATION.md "Probe and mutation-harness discipline"
(2026-08-17): clean baseline FIRST, then planted corruptions on a COPY, each
required to fail via a genuine named check.
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

import yaml
from yaml.constructor import ConstructorError

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "lab" / "process" / "upgrade-program-register.yaml"
REQUIRED = ("id", "title", "origin", "owner", "status", "activation", "next_check")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

FAIL: list[str] = []
DUE: list[str] = []
N = 0


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects silently overwritten mapping keys."""


def construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict:
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def check(label: str, ok: bool) -> None:
    global N
    N += 1
    if not ok:
        FAIL.append(label)
        print(f"[FAIL] {label}")


def parse_date(value: object) -> date | None:
    text = str(value)
    if not DATE.match(text):
        return None
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def resolve_as_of(value: str | None) -> date:
    """Resolve an explicit audit date, defaulting visibly to the UTC day."""
    if value is None:
        return datetime.now(timezone.utc).date()
    parsed = parse_date(value)
    if parsed is None:
        raise ValueError("--as-of must be a real calendar date in YYYY-MM-DD form")
    return parsed


def audit(path: Path, as_of: date | None = None) -> int:
    global N, FAIL, DUE
    N, FAIL, DUE = 0, [], []
    as_of = as_of or resolve_as_of(None)
    try:
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        check("register parses with unique mapping keys", False)
        print(f"  {exc}")
        return 1
    check("register parses with unique mapping keys", True)
    check("register parses to a mapping", isinstance(data, dict))
    vocab = data.get("status_vocabulary", [])
    check("status vocabulary is the closed four-value set",
          vocab == ["QUEUED", "ACTIVE", "DONE", "DECLINED"])
    items = data.get("items", [])
    check("at least one item", len(items) >= 1)
    ids = [i.get("id") for i in items]
    check("item ids unique", len(ids) == len(set(ids)))
    for i in items:
        iid = i.get("id", "<missing>")
        for f in REQUIRED:
            check(f"{iid}: field `{f}` present and nonempty", bool(i.get(f)))
        check(f"{iid}: status in vocabulary", i.get("status") in vocab)
        next_check = parse_date(i.get("next_check", ""))
        check(f"{iid}: next_check is a real calendar date", next_check is not None)
        if (
            next_check is not None
            and next_check < as_of
            and i.get("status") not in ("DONE", "DECLINED")
        ):
            DUE.append(iid)
        # DONE and DECLINED must carry their receipt/grounds inside `activation`
        # or `origin` -- an item may not leave the queue bare.
        if i.get("status") in ("DONE", "DECLINED"):
            blob = str(i.get("activation", "")) + str(i.get("origin", ""))
            check(f"{iid}: {i['status']} carries a receipt or grounds",
                  len(blob) > 20)
    active = [i["id"] for i in items if i.get("status") == "ACTIVE"]
    due_text = ", ".join(DUE) if DUE else "none"
    print(f"upgrade_program_register_audit: as_of={as_of.isoformat()}; "
          f"{len(DUE)} overdue nonterminal: {due_text}")
    print(f"upgrade_program_register_audit: {len(items)} items "
          f"({len(active)} ACTIVE: {', '.join(active) if active else 'none'}); "
          f"{len(FAIL)} failed of {N} checks.")
    return 1 if FAIL else 0


def selftest(as_of: date) -> int:
    print("SELFTEST: clean baseline FIRST")
    if audit(REGISTER, as_of) != 0:
        print("BASELINE RED -- mutation results would be meaningless. ABORT.")
        return 1
    print("baseline GREEN; planting corruptions on a copy\n")
    src = REGISTER.read_text(encoding="utf-8")
    plants = (
        ("status outside vocabulary", "status: ACTIVE", "status: SOMEDAY"),
        ("owner deleted", "owner: Joe", "owner: \"\""),
        ("next_check not a date", 'next_check: "2026-08-19"', 'next_check: "soon"'),
        ("duplicate id", "id: CT-4-DIAGRAM-INVARIANT", "id: CT-1-BASE-CATEGORIES"),
        (
            "duplicate mapping key",
            '    next_check: "2026-08-24"',
            '    next_check: "2026-08-24"\n    next_check: "2026-08-19"',
        ),
    )
    ok = True
    with tempfile.TemporaryDirectory(prefix="gu-upgrade-register-") as tmpdir:
        tmp = Path(tmpdir) / "register-mutant.yaml"
        for label, old, new in plants:
            if old not in src:
                print(f"  PLANT NOT APPLICABLE (needle missing): {label}")
                ok = False
                continue
            tmp.write_text(src.replace(old, new, 1), encoding="utf-8")
            rc = audit(tmp, as_of)
            caught = rc == 1 and FAIL  # genuine [FAIL] lines, not a crash
            print(f"  {'caught via genuine [FAIL]' if caught else 'NOT CAUGHT'}: {label}\n")
            ok = ok and bool(caught)
    print("SELFTEST " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Audit upgrade-program register structure and report overdue "
            "nonterminal review rows without activating or reprioritizing them."
        )
    )
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument(
        "--as-of",
        metavar="YYYY-MM-DD",
        help="deterministic review date (default: current UTC date)",
    )
    args = parser.parse_args()
    try:
        as_of = resolve_as_of(args.as_of)
    except ValueError as exc:
        parser.error(str(exc))
    return selftest(as_of) if args.selftest else audit(REGISTER, as_of)


if __name__ == "__main__":
    sys.exit(main())

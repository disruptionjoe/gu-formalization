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

import re
import sys
from pathlib import Path

import yaml
from yaml.constructor import ConstructorError

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "lab" / "process" / "upgrade-program-register.yaml"
REQUIRED = ("id", "title", "origin", "owner", "status", "activation", "next_check")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

FAIL: list[str] = []
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


def audit(path: Path) -> int:
    global N, FAIL
    N, FAIL = 0, []
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
        check(f"{iid}: next_check is date-shaped", bool(DATE.match(str(i.get("next_check", "")))))
        # DONE and DECLINED must carry their receipt/grounds inside `activation`
        # or `origin` -- an item may not leave the queue bare.
        if i.get("status") in ("DONE", "DECLINED"):
            blob = str(i.get("activation", "")) + str(i.get("origin", ""))
            check(f"{iid}: {i['status']} carries a receipt or grounds",
                  len(blob) > 20)
    active = [i["id"] for i in items if i.get("status") == "ACTIVE"]
    print(f"upgrade_program_register_audit: {len(items)} items "
          f"({len(active)} ACTIVE: {', '.join(active) if active else 'none'}); "
          f"{len(FAIL)} failed of {N} checks.")
    return 1 if FAIL else 0


def selftest() -> int:
    print("SELFTEST: clean baseline FIRST")
    if audit(REGISTER) != 0:
        print("BASELINE RED -- mutation results would be meaningless. ABORT.")
        return 1
    print("baseline GREEN; planting corruptions on a copy\n")
    src = REGISTER.read_text(encoding="utf-8")
    tmp = REGISTER.parent / "_upgrade_register_mutant.yaml"
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
    for label, old, new in plants:
        if old not in src:
            print(f"  PLANT NOT APPLICABLE (needle missing): {label}")
            ok = False
            continue
        tmp.write_text(src.replace(old, new, 1), encoding="utf-8")
        rc = audit(tmp)
        caught = rc == 1 and FAIL  # genuine [FAIL] lines, not a crash
        print(f"  {'caught via genuine [FAIL]' if caught else 'NOT CAUGHT'}: {label}\n")
        ok = ok and bool(caught)
    tmp.unlink(missing_ok=True)
    print("SELFTEST " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else audit(REGISTER))

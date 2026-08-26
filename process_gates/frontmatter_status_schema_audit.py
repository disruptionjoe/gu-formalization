#!/usr/bin/env python3
"""Ratchet the protected frontmatter-status population and future typed axes."""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "lab/process/frontmatter-status-population.yaml"
STATUS = re.compile(r"(?m)^status:\s*(.*?)\s*$")
AXIS = re.compile(r"(?m)^(status_axis|claim_verdict|operational_state):\s*\S")


def tracked_markdown() -> list[str]:
    raw = subprocess.check_output(["git", "ls-files", "-z", "*.md"], cwd=ROOT)
    return sorted(x for x in raw.decode().split("\0") if x)


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    return text[4:end] if end >= 0 else None


def status_map(paths: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for rel in paths:
        fm = frontmatter((ROOT / rel).read_text(errors="replace"))
        if fm is None:
            continue
        match = STATUS.search(fm)
        if match:
            out[rel] = match.group(1).strip().strip("\"'")
    return out


def digest(mapping: dict[str, str]) -> str:
    body = "".join(f"{p}\0{mapping[p]}\n" for p in sorted(mapping))
    return hashlib.sha256(body.encode()).hexdigest()


def baseline_status(revision: str, rel: str) -> str | None:
    got = subprocess.run(
        ["git", "show", f"{revision}:{rel}"], cwd=ROOT,
        text=True, capture_output=True, check=False,
    )
    if got.returncode != 0:
        return None
    fm = frontmatter(got.stdout)
    match = STATUS.search(fm or "")
    return match.group(1).strip().strip("\"'") if match else None


def audit() -> list[str]:
    data = yaml.safe_load(MANIFEST.read_text())
    paths = tracked_markdown()
    mapping = status_map(paths)
    roles = set(data["axes"]["document_role"]["values"])
    failures: list[str] = []
    observed = {
        "tracked_markdown": len(paths),
        "status_bearing": len(mapping),
        "document_role": sum(v in roles for v in mapping.values()),
        "legacy_untyped": sum(v not in roles for v in mapping.values()),
        "distinct_values": len(set(mapping.values())),
        "distinct_legacy_values": len({v for v in mapping.values() if v not in roles}),
    }
    if observed != data["counts"]:
        failures.append(f"population counts changed: {observed!r}")
    mapping_changed = digest(mapping) != data["mapping_digest_sha256"]
    if mapping_changed:
        failures.append("protected path/status mapping digest changed")
        rev = str(data["frozen_revision"])
        for rel, value in mapping.items():
            old = baseline_status(rev, rel)
            if old is None and value not in roles:
                failures.append(f"{rel}: new document uses legacy non-role status")
            elif old != value:
                fm = frontmatter((ROOT / rel).read_text(errors="replace")) or ""
                if value not in roles and not AXIS.search(fm):
                    failures.append(f"{rel}: new/changed non-role status lacks typed axis")
    return failures


def selftest() -> int:
    failures = audit()
    if failures:
        print("BASELINE RED -- aborting mutations")
        for item in failures:
            print(f"[FAIL] {item}")
        return 1
    sample = {"a.md": "process", "b.md": "OPEN"}
    clean = digest(sample)
    caught = [
        digest({**sample, "b.md": "complete"}) != clean,
        digest({**sample, "c.md": "active"}) != clean,
        len(set(sample.values())) != len(set({**sample, "b.md": "process"}.values())),
    ]
    for i, ok in enumerate(caught, 1):
        print(f"[{'PASS' if ok else 'FAIL'}] planted population mutation {i}")
    return 0 if all(caught) else 1


if __name__ == "__main__":
    result = selftest() if "--selftest" in sys.argv else int(bool(audit()))
    if "--selftest" not in sys.argv:
        failures = audit()
        for item in failures:
            print(f"[FAIL] {item}")
        print(f"frontmatter_status_schema_audit: {len(failures)} failures")
        result = int(bool(failures))
    raise SystemExit(result)

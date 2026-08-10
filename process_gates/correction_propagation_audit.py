#!/usr/bin/env python3
"""Corrections must propagate along citation edges (report-only for seeded baseline, fail on regressions).

THE finding of the 2026-08-10 canon-spine hostile sweep: zero arithmetic failures in 22 spine files,
while every material defect sat where a correction chain stopped propagating -- a correction lands on
the file that was wrong and never reaches the files that cite it (the synthesis composing corrected
dependencies at uncorrected strength; an addendum with zero banners beside a twice-bannered parent).

This gate walks the machine-readable ledger lab/process/correction-registry.yaml. For each
enforce: true correction, every canon/ or docs/ file citing a trigger_ref must contain an
ack_marker. Citers known-unacknowledged at seeding are REPORTED as NEEDS_RECHECK (the absorption
backlog); NEW unacknowledged citers FAIL. Per the ratified posture (Joe, direct chat 2026-08-10),
NEEDS_RECHECK is report-only, never blocking.
"""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab" / "process" / "correction-registry.yaml"
SURFACES = ("canon", "docs")


def load_registry() -> list[dict]:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    return data["corrections"]


def repo_files() -> list[Path]:
    out: list[Path] = []
    for surface in SURFACES:
        out.extend(sorted((ROOT / surface).glob("*.md")))
    return out


class CorrectionPropagationAudit(unittest.TestCase):
    def test_registry_parses_and_owners_exist(self) -> None:
        entries = load_registry()
        self.assertGreater(len(entries), 0)
        for entry in entries:
            self.assertIn("id", entry)
            self.assertTrue((ROOT / entry["owner"]).exists(), f"registry owner missing: {entry['owner']}")

    def test_no_new_unacknowledged_citers(self) -> None:
        entries = [e for e in load_registry() if e.get("enforce")]
        new_bad: list[str] = []
        for entry in entries:
            rid = entry["id"]
            triggers = entry.get("trigger_refs") or [Path(entry["owner"]).stem]
            acks = [m.lower() for m in (entry.get("ack_markers") or [rid])]
            known = set(entry.get("known_unacknowledged") or [])
            owner_stem = Path(entry["owner"]).stem
            for path in repo_files():
                rel = str(path.relative_to(ROOT))
                if Path(entry["owner"]).name == path.name:
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
                low = text.lower()
                cites = any(t.lower() in low for t in triggers)
                if not cites or path.stem in [Path(t).stem for t in triggers] or path.stem == owner_stem:
                    continue
                acked = any(m in low for m in acks)
                if acked:
                    continue
                if rel in known:
                    print(f"NEEDS_RECHECK (known at seeding 2026-08-10): {rel} cites {triggers} without acknowledging [{rid}]")
                else:
                    new_bad.append(f"{rel} cites {triggers} without acknowledging [{rid}]")
        self.assertEqual(
            new_bad, [],
            "NEW unacknowledged citation of a corrected result (acknowledge the correction id or add to "
            "known_unacknowledged with a dated reason):\n" + "\n".join(new_bad),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

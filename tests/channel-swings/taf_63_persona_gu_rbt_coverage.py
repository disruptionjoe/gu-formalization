"""Check completeness and independence scaffolding for the TaF-to-GU panel."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PANEL_DIR = ROOT / "explorations" / "taf-63-persona-gu-rbt-2026-07-20"
BATCH_RE = re.compile(r"^(0[1-9])-batch-p\d{2}-p\d{2}\.md$")
HEADING_RE = re.compile(r"^### P(\d{2})\. .+$", re.MULTILINE)
FIELDS = (
    "Summary of understanding",
    "Strongest insight",
    "Strongest criticism",
    "Hidden assumptions",
    "Rose",
    "Bud",
    "Thorn",
    "Confidence",
    "Suggested experiment",
    "Suggested theorem or mathematical direction",
    "Suggested falsification test",
    "Evidence touched",
)


def fail(messages: list[str]) -> None:
    for message in messages:
        print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    batch_files = sorted(
        path for path in PANEL_DIR.iterdir() if path.is_file() and BATCH_RE.match(path.name)
    )
    errors: list[str] = []
    if len(batch_files) != 9:
        errors.append(f"expected 9 batch files, found {len(batch_files)}")

    seen: Counter[int] = Counter()
    for path in batch_files:
        text = path.read_text(encoding="utf-8")
        matches = list(HEADING_RE.finditer(text))
        if len(matches) != 7:
            errors.append(f"{path.name}: expected 7 persona headings, found {len(matches)}")
        if re.search(r"^#{1,6} .*synthesis", text, re.IGNORECASE | re.MULTILINE):
            errors.append(f"{path.name}: contains a synthesis heading")

        for index, match in enumerate(matches):
            persona_id = int(match.group(1))
            seen[persona_id] += 1
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            section = text[match.start() : end]
            for field in FIELDS:
                count = section.count(f"- **{field}:")
                if count != 1:
                    errors.append(
                        f"{path.name} P{persona_id:02}: field {field!r} appears {count} times"
                    )

    expected = set(range(1, 64))
    actual = set(seen)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    duplicates = sorted(persona_id for persona_id, count in seen.items() if count != 1)
    if missing:
        errors.append(f"missing persona IDs: {missing}")
    if extra:
        errors.append(f"unexpected persona IDs: {extra}")
    if duplicates:
        errors.append(f"non-unique persona IDs: {duplicates}")

    if errors:
        fail(errors)
    print("PASS: 63/63 personas appear exactly once across 9 independent batch files.")
    print("PASS: every persona section contains all 12 required fields.")
    print("PASS: no batch file contains a synthesis heading.")


if __name__ == "__main__":
    main()

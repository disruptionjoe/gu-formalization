#!/usr/bin/env python3
"""Audit changed publishable files for absolute home-path leaks.

This is a scheduled-run hygiene gate, not a research-content check. It scans
the current tracked Git diff plus untracked non-ignored files so public commits
do not accidentally publish local machine paths.
"""

from __future__ import annotations

import re
import subprocess
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

HOME_PATH_PATTERNS = (
    ("escaped_windows_home", re.compile(r"[A-Za-z]:\\\\Users\\\\[A-Za-z0-9._-]+")),
    ("windows_home", re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+[A-Za-z0-9._-]+")),
    ("posix_users_home", re.compile(r"/Users/[A-Za-z0-9._-]+")),
    ("posix_home", re.compile(r"/home/[A-Za-z0-9._-]+")),
)


@dataclass(frozen=True)
class HomePathLeak:
    relpath: str
    line: int
    kind: str
    match: str


def normalize_path(path: str) -> str:
    return path.strip().replace("\\", "/").lstrip("./")


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def run_git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def git_path_lines(*args: str) -> list[str]:
    result = run_git(*args)
    if result.returncode != 0:
        command = "git " + " ".join(args)
        raise AssertionError(result.stderr.strip() or f"{command} failed")

    return [normalize_path(line) for line in result.stdout.splitlines() if line.strip()]


def changed_publishable_paths() -> list[str]:
    paths = set(git_path_lines("diff", "--name-only", "HEAD", "--"))
    paths.update(git_path_lines("ls-files", "--others", "--exclude-standard"))
    return sorted(paths)


def read_text_if_safe(path: Path) -> str | None:
    if not path.is_file():
        return None

    data = path.read_bytes()
    if b"\x00" in data:
        return None

    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def find_home_path_leaks(rel: str, text: str) -> list[HomePathLeak]:
    leaks: list[HomePathLeak] = []
    occupied_spans: list[tuple[int, int]] = []
    for kind, pattern in HOME_PATH_PATTERNS:
        for match in pattern.finditer(text):
            span = match.span()
            if any(max(start, span[0]) < min(end, span[1]) for start, end in occupied_spans):
                continue
            occupied_spans.append(span)
            leaks.append(
                HomePathLeak(
                    relpath=rel,
                    line=line_number(text, match.start()),
                    kind=kind,
                    match=match.group(0),
                )
            )
    return sorted(leaks, key=lambda leak: (leak.line, leak.kind, leak.match))


def scan_changed_paths(paths: list[str]) -> list[HomePathLeak]:
    leaks: list[HomePathLeak] = []
    for rel in paths:
        path = ROOT / rel
        text = read_text_if_safe(path)
        if text is None:
            continue
        leaks.extend(find_home_path_leaks(rel, text))
    return leaks


class ChangedPublicPathHygieneAudit(unittest.TestCase):
    def test_home_path_patterns_cover_common_public_leaks(self) -> None:
        windows = "C:" + "/Users/" + "sample/project/file.txt"
        escaped = "C:" + "\\\\" + "Users" + "\\\\" + "sample" + "\\\\" + "project"
        mac = "/" + "Users/" + "sample/project/file.txt"
        linux = "/" + "home/" + "sample/project/file.txt"
        text = "\n".join([windows, escaped, mac, linux])

        leaks = find_home_path_leaks("sample.txt", text)
        self.assertEqual(
            ["windows_home", "escaped_windows_home", "posix_users_home", "posix_home"],
            [leak.kind for leak in leaks],
        )

    def test_path_normalization_is_repository_relative(self) -> None:
        self.assertEqual("process_gates/example.py", normalize_path(r".\process_gates\example.py"))
        self.assertEqual("tests/example.py", normalize_path("./tests/example.py"))

    def test_binary_files_are_skipped(self) -> None:
        binary_path = ROOT / "_local" / "path-hygiene-binary-probe.bin"
        binary_path.parent.mkdir(exist_ok=True)
        binary_path.write_bytes(b"\x00not text")
        try:
            self.assertIsNone(read_text_if_safe(binary_path))
        finally:
            binary_path.unlink(missing_ok=True)

    def test_current_changed_publishable_files_do_not_contain_home_paths(self) -> None:
        leaks = scan_changed_paths(changed_publishable_paths())
        rendered = [
            f"{leak.relpath}:{leak.line}: {leak.kind}: {leak.match}"
            for leak in leaks
        ]
        self.assertEqual([], rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)

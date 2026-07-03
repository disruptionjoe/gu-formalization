"""Compute a bounded convergence read from the loop adversarial log.

This script is process instrumentation, not a research-claim validator. It parses
the tracked loop log and refuses to infer metrics the log does not encode.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = ROOT / "lab" / "process" / "loop-adversarial-log.md"
REPORT_PATH = ROOT / "lab" / "process" / "convergence-read-2026-07-03.md"

RUN_HEADING_RE = re.compile(
    r"^## Run (?P<date>\d{4}-\d{2}-\d{2}) .+? "
    r"(?P<completed>\d+)/(?P<total>\d+) completed, (?P<fixed>\d+) fixed\s*$",
    re.MULTILINE,
)
ISSUE_SUMMARY_RE = re.compile(
    r"\*\*Issue summary:\*\* (?P<total>\d+) total "
    r"\((?P<critical_moderate>\d+) critical/moderate, (?P<minor>\d+) minor\)"
)

ABSOLUTE_HOME_PATH_RE = re.compile(r"[A-Za-z]:\\Users\\")

PATTERN_RULES = {
    "same_session_self_resolution": [
        "same-session self-resolution",
        "same-session circularity",
        "cannot be closed by a reconstruction-grade file produced in the same session",
    ],
    "verdict_grade_inflation": [
        "verdict grade mismatch",
        "resolved verdict",
        "resolved canon entries",
        "reconstruction grade is not a valid basis for resolved",
    ],
    "candidate_selection_inflation": [
        "verdict inflation through candidate selection",
        "two equally-supported candidates",
        "both candidates are undismissed guesses",
    ],
    "internal_contradiction_closed": [
        "internal contradiction labeled resolved",
        "an explicit internal contradiction",
    ],
}


def _split_run_sections(log_text: str) -> list[str]:
    matches = list(RUN_HEADING_RE.finditer(log_text))
    sections = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(log_text)
        sections.append(log_text[start:end])
    return sections


def _round_ratio(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(numerator / denominator, 3)


def _pattern_hits(section: str) -> list[str]:
    lowered = section.lower()
    hits = []
    for pattern, needles in PATTERN_RULES.items():
        if any(needle in lowered for needle in needles):
            hits.append(pattern)
    return hits


def compute_metrics(log_path: Path = LOG_PATH) -> dict[str, Any]:
    log_text = log_path.read_text(encoding="utf-8")
    run_matches = list(RUN_HEADING_RE.finditer(log_text))
    sections = _split_run_sections(log_text)
    issue_matches = [ISSUE_SUMMARY_RE.search(section) for section in sections]

    if len(run_matches) != len(sections):
        raise AssertionError("run heading parse mismatch")
    if any(match is None for match in issue_matches):
        raise AssertionError("each parsed run section must contain an issue summary")

    completed_items = sum(int(match.group("completed")) for match in run_matches)
    total_items = sum(int(match.group("total")) for match in run_matches)
    fixed_count = sum(int(match.group("fixed")) for match in run_matches)
    issue_total = sum(int(match.group("total")) for match in issue_matches if match)
    critical_moderate = sum(int(match.group("critical_moderate")) for match in issue_matches if match)
    minor = sum(int(match.group("minor")) for match in issue_matches if match)

    per_run_patterns = [_pattern_hits(section) for section in sections]
    pattern_counts: dict[str, int] = {}
    for hits in per_run_patterns:
        for hit in hits:
            pattern_counts[hit] = pattern_counts.get(hit, 0) + 1
    repeated_patterns = sorted(pattern for pattern, count in pattern_counts.items() if count > 1)
    unique_patterns = sorted(pattern_counts)

    missing_metrics = [
        "net_resolved_gain",
        "admitted_object_fraction",
        "status_transition_churn",
    ]

    return {
        "source": "lab/process/loop-adversarial-log.md",
        "run_count": len(run_matches),
        "completed_items": completed_items,
        "total_items": total_items,
        "completion_rate": _round_ratio(completed_items, total_items),
        "reported_fixed_count": fixed_count,
        "issue_total": issue_total,
        "critical_moderate_issues": critical_moderate,
        "minor_issues": minor,
        "fixed_to_issue_ratio": _round_ratio(fixed_count, issue_total),
        "critical_moderate_issue_share": _round_ratio(critical_moderate, issue_total),
        "unique_pattern_count": len(unique_patterns),
        "repeated_pattern_count": len(repeated_patterns),
        "repeat_rate": _round_ratio(len(repeated_patterns), len(unique_patterns)),
        "repeated_patterns": repeated_patterns,
        "under_instrumented_metrics": missing_metrics,
        "convergence_status": "UNDER_INSTRUMENTED_WITH_REPEATING_GRADE_RISK",
        "convergence_claimed": False,
    }


def _extract_report_json(report_text: str) -> dict[str, Any]:
    start_marker = "<!-- convergence-read-json:start -->"
    end_marker = "<!-- convergence-read-json:end -->"
    if start_marker not in report_text or end_marker not in report_text:
        raise AssertionError("missing convergence-read JSON markers in report")
    block = report_text.split(start_marker, 1)[1].split(end_marker, 1)[0].strip()
    if block.startswith("```json"):
        block = block.split("\n", 1)[1]
    if block.endswith("```"):
        block = block.rsplit("```", 1)[0]
    return json.loads(block.strip())


def check_report(report_path: Path = REPORT_PATH, log_path: Path = LOG_PATH) -> None:
    metrics = compute_metrics(log_path)
    report_text = report_path.read_text(encoding="utf-8")
    if ABSOLUTE_HOME_PATH_RE.search(report_text):
        raise AssertionError("report contains an absolute home path")
    reported = _extract_report_json(report_text)
    if reported != metrics:
        raise AssertionError(
            "report JSON does not match computed metrics:\n"
            f"computed={json.dumps(metrics, sort_keys=True)}\n"
            f"reported={json.dumps(reported, sort_keys=True)}"
        )
    if "does not claim convergence" not in report_text:
        raise AssertionError("report must explicitly refuse a convergence claim")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-report", action="store_true", help="validate the companion report JSON")
    args = parser.parse_args(argv)

    if args.check_report:
        check_report()
        return 0

    print(json.dumps(compute_metrics(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

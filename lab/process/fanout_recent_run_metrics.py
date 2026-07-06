"""Measure the recent Progress fan-out packet sequence from local run receipts.

Report-only instrumentation. This script reads a pinned snapshot of ignored
`steward/runs/` receipts and the corresponding git commits. It does not promote
any claim, change any verdict, or infer mathematical convergence.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RUN_DIR = ROOT / "steward" / "runs"
REPORT_PATH = ROOT / "lab" / "process" / "fanout-recent-run-convergence-2026-07-06.md"

SNAPSHOT_RUN_FILES = [
    "2026-07-05-progress-fanout-165-theta-source-carrier-packet.md",
    "2026-07-05-progress-fanout-167-weak-field-source-current-carrier.md",
    "2026-07-05-progress-fanout-168-anomaly-green-schwarz-carrier.md",
    "2026-07-05-progress-fanout-171-rs-brst-carrier.md",
    "2026-07-05-progress-fanout-174-r4-twoarena-timeout.md",
    "2026-07-05-progress-fanout-r4-lean-api-drift.md",
    "2026-07-05-progress-fanout-177-families-pushforward-carrier.md",
    "2026-07-05-progress-fanout-178-boundary-spectral-section-packet.md",
    "2026-07-05-progress-fanout-181-non-equivariant-compensator-packet.md",
    "2026-07-06-progress-fanout-signed-readout-uii-gap.md",
    "2026-07-06-progress-fanout-sp1-2primary-anomaly-gate.md",
]

STATUS_RE = re.compile(r"^status:\s*(?P<status>\S+)\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^# Progress Fan-Out Run:\s*(?P<title>.+?)\s*$", re.MULTILINE)
OUTCOME_RE = re.compile(r"^Outcome:\s*(?P<outcome>[A-Za-z0-9_-]+)\.\s*$", re.MULTILINE)
COMMIT_RE = re.compile(r"^Commit/push:\s*`(?P<sha>[0-9a-f]{7,40})\b", re.MULTILINE)
ABSOLUTE_HOME_PATH_RE = re.compile(r"[A-Za-z]:" + r"\\Users\\" + "|" + "/" + "Users/")


def _git(args: list[str]) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        check=True,
        text=True,
    ).stdout


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _classify_lane(filename: str, title: str, changed_paths: list[str]) -> str:
    joined = " ".join([filename, title, *changed_paths]).lower()
    if "signed-readout" in joined or "uii" in joined:
        return "signed_readout_uii_gate"
    if "sp1" in joined or "anomaly/" in joined or "sp(1)" in joined:
        return "anomaly_2primary_gate"
    if "r4" in joined or "lean" in joined or "twoarena" in joined:
        return "lean_maintenance"
    if "absorbed/gu-source-action" in joined or "source-action" in joined:
        return "source_action_attack_gate"
    return "other"


def _extract_changed_paths(text: str) -> list[str]:
    marker = "Files changed for versioned repository knowledge:"
    if marker not in text:
        return []
    after = text.split(marker, 1)[1]
    paths = []
    seen_bullet = False
    for line in after.splitlines()[1:]:
        stripped = line.strip()
        if not stripped and not seen_bullet:
            continue
        if not stripped:
            break
        if stripped.startswith("- `") and stripped.endswith("`"):
            seen_bullet = True
            paths.append(stripped[3:-1].replace("\\", "/"))
    return paths


def _name_status_for_commit(sha: str) -> dict[str, str]:
    status_by_path: dict[str, str] = {}
    for line in _git(["show", "--name-status", "--format=", "--no-renames", sha]).splitlines():
        if not line.strip():
            continue
        status, path = line.split("\t", 1)
        status_by_path[path.replace("\\", "/")] = status
    return status_by_path


def _infer_commit_from_paths(changed_paths: list[str]) -> str | None:
    if not changed_paths:
        return None
    # Use the first versioned path as a fallback when a local receipt was closed
    # before central closeout filled in the commit line.
    out = _git(["log", "-1", "--format=%h", "--", changed_paths[0]])
    return out.strip() or None


def _parse_run(filename: str) -> dict[str, Any]:
    path = RUN_DIR / filename
    text = path.read_text(encoding="utf-8")
    status = STATUS_RE.search(text)
    title = TITLE_RE.search(text)
    outcome = OUTCOME_RE.search(text)
    commit_match = COMMIT_RE.search(text)
    changed_paths = _extract_changed_paths(text)
    recorded_sha = commit_match.group("sha") if commit_match else None
    inferred_sha = None if recorded_sha else _infer_commit_from_paths(changed_paths)
    sha = recorded_sha or inferred_sha
    name_status = _name_status_for_commit(sha) if sha else {}
    added = sorted(path for path in changed_paths if name_status.get(path) == "A")
    modified = sorted(path for path in changed_paths if name_status.get(path) == "M")

    return {
        "receipt": _relative(path),
        "status": status.group("status") if status else "unknown",
        "title": title.group("title") if title else filename,
        "outcome": outcome.group("outcome") if outcome else "unknown",
        "commit": sha,
        "commit_source": "receipt" if recorded_sha else ("git_path_inference" if inferred_sha else "missing"),
        "lane": _classify_lane(filename, title.group("title") if title else "", changed_paths),
        "changed_path_count": len(changed_paths),
        "added_path_count": len(added),
        "modified_path_count": len(modified),
        "added_paths": added,
        "modified_paths": modified,
    }


def compute_metrics() -> dict[str, Any]:
    runs = [_parse_run(filename) for filename in SNAPSHOT_RUN_FILES]
    lane_counts = Counter(run["lane"] for run in runs)
    completed_count = sum(1 for run in runs if run["status"] == "complete")
    pushed_count = sum(1 for run in runs if run["commit"])
    added_paths = sorted({path for run in runs for path in run["added_paths"]})
    modified_paths = sorted({path for run in runs for path in run["modified_paths"]})
    repeated_lanes = sorted(lane for lane, count in lane_counts.items() if count > 1)
    repeated_run_count = sum(count for lane, count in lane_counts.items() if count > 1)

    return {
        "source": "steward/runs pinned local receipts plus referenced git commits",
        "snapshot_run_count": len(runs),
        "snapshot_receipts": SNAPSHOT_RUN_FILES,
        "completed_run_count": completed_count,
        "pushed_commit_count": pushed_count,
        "all_runs_complete": completed_count == len(runs),
        "all_runs_pushed": pushed_count == len(runs),
        "lane_counts": dict(sorted(lane_counts.items())),
        "repeated_lanes": repeated_lanes,
        "repeated_lane_run_share": round(repeated_run_count / len(runs), 3),
        "added_path_count": len(added_paths),
        "modified_path_count": len(modified_paths),
        "create_rework_ratio": round(len(added_paths) / len(modified_paths), 3)
        if modified_paths
        else None,
        "runs": runs,
        "convergence_claimed": False,
        "claim_status_changed": False,
        "canon_changed": False,
        "verdict_changed": False,
        "read": "RECENT_FANOUT_PRODUCTIVE_BUT_LANE_REPETITION_HIGH",
    }


def _extract_report_json(report_text: str) -> dict[str, Any]:
    start_marker = "<!-- fanout-recent-json:start -->"
    end_marker = "<!-- fanout-recent-json:end -->"
    if start_marker not in report_text or end_marker not in report_text:
        raise AssertionError("missing fanout recent JSON markers in report")
    block = report_text.split(start_marker, 1)[1].split(end_marker, 1)[0].strip()
    if block.startswith("```json"):
        block = block.split("\n", 1)[1]
    if block.endswith("```"):
        block = block.rsplit("```", 1)[0]
    return json.loads(block.strip())


def check_report(report_path: Path = REPORT_PATH) -> None:
    report_text = report_path.read_text(encoding="utf-8")
    if ABSOLUTE_HOME_PATH_RE.search(report_text):
        raise AssertionError("report contains an absolute home path")
    if "does not claim convergence" not in report_text:
        raise AssertionError("report must explicitly refuse a convergence claim")
    reported = _extract_report_json(report_text)
    computed = compute_metrics()
    if reported != computed:
        raise AssertionError(
            "report JSON does not match computed metrics:\n"
            f"computed={json.dumps(computed, sort_keys=True)}\n"
            f"reported={json.dumps(reported, sort_keys=True)}"
        )


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

"""Convergence metrics for the automated GU research loop (OBJ-CONVERGE meta-audit).

Report-only instrumentation. Computes reproducible cadence / churn / creation
metrics from `git log` and from on-disk run artifacts. It does NOT promote any
claim and does NOT modify canon, status, or the paper.

What is computed programmatically (trust the numbers):
  - commits per day
  - added vs modified files per day (create/rework ratio)
  - canon RESULTS/SPEC file first-add cadence (net-new admitted-object proxy)
  - hourly-cycle generator activity per day (from filenames)
  - steward "progress fan-out" run cadence per day
  - keyword classification of commit subjects: research-substance vs process/meta
  - rework-signal commit share (relabel/normalize/demote/hygiene/fix/audit/...)
  - repeat-touch count for the most-churned anchor objects

What is NOT computed (honest gaps, must be judged by hand):
  - true verdict-transition ledger (promotions vs downgrades/re-openings): the
    repo does not carry a machine-readable per-object verdict history, so
    "net RESOLVED gain" here is a proxy (canon file adds) plus a hand read.

Run:  python lab/process/convergence_metrics_2026-07-03.py
"""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Keyword rules for classifying a commit SUBJECT line. These are heuristics;
# the report flags them as judgment-assisted, not ground truth.
PROCESS_KEYS = [
    "hygiene", "gate", "scrub", "path leak", "home-path", "de-theater",
    "steward", "fan-out", "fanout", "fleet", "template", "routing link",
    "conform", "relabel", "normalize", "roster", "process", "posture",
    "publishing internal", "pointer", "crosswalk", "division of labor",
    "vocabulary", "readiness pass", "publication materials", "convergence read",
    "work lanes", "attack gate", "attack frontier", "memory log",
]
RESEARCH_KEYS = [
    "result", "results", "theorem", "proof", "index", "eta", "antilinear",
    "enum", "spectral", "aps", "dirac", "higgs", "shiab", "source action",
    "curvature", "residual", "cas", "generation", "bordism", "discharge",
    "land ", "probe", "family index", "boundary", "located-not-forced",
    "chase-to-kill", "verdict",
]
REWORK_KEYS = [
    "demote", "downgrade", "reopen", "re-open", "supersede", "relabel",
    "normalize", "de-theater", "scrub", "hygiene", "fix", "repair", "conform",
    "consolidat", "audit", "correct", "update", "stale", "rescope", "merge",
]


def git(args: list[str]) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True, text=True, check=True,
    ).stdout


def commits_per_day() -> dict[str, int]:
    out = git(["log", "--date=short", "--pretty=%ad"]).splitlines()
    return dict(sorted(Counter(out).items()))


def add_mod_per_day() -> dict[str, dict[str, int]]:
    out = git(["log", "--diff-filter=AM", "--date=short",
               "--pretty=format:COMMIT %ad", "--name-status"]).splitlines()
    add: dict[str, int] = defaultdict(int)
    mod: dict[str, int] = defaultdict(int)
    day = None
    for line in out:
        if line.startswith("COMMIT "):
            day = line.split()[1]
        elif line.startswith("A\t"):
            add[day] += 1
        elif line.startswith("M\t"):
            mod[day] += 1
    days = sorted(set(add) | set(mod))
    res = {}
    for d in days:
        a, m = add[d], mod[d]
        res[d] = {"added": a, "modified": m,
                  "create_rework_ratio": round(a / m, 2) if m else None}
    return res


def canon_adds_per_day() -> dict[str, int]:
    out = git(["log", "--diff-filter=A", "--date=short",
               "--pretty=format:COMMIT %ad", "--name-only", "--", "canon/"]).splitlines()
    day = None
    per = Counter()
    for line in out:
        if line.startswith("COMMIT "):
            day = line.split()[1]
        elif line.startswith("canon/") and line.endswith(".md") and "README" not in line:
            per[day] += 1
    return dict(sorted(per.items()))


def subject_classification() -> dict[str, object]:
    subs = git(["log", "--pretty=%s"]).splitlines()
    research = process = both = neither = 0
    rework = 0
    for s in subs:
        low = s.lower()
        r = any(k in low for k in RESEARCH_KEYS)
        p = any(k in low for k in PROCESS_KEYS)
        if any(k in low for k in REWORK_KEYS):
            rework += 1
        if r and p:
            both += 1
        elif r:
            research += 1
        elif p:
            process += 1
        else:
            neither += 1
    total = len(subs)
    return {
        "total_commits": total,
        "research_only": research,
        "process_meta_only": process,
        "both": both,
        "neither": neither,
        "rework_signal_commits": rework,
        "rework_signal_share": round(rework / total, 3),
        "process_or_both_share": round((process + both) / total, 3),
    }


def recent_window_classification(since: str) -> dict[str, object]:
    subs = git(["log", f"--since={since}", "--pretty=%s"]).splitlines()
    research = process = 0
    for s in subs:
        low = s.lower()
        r = any(k in low for k in RESEARCH_KEYS)
        p = any(k in low for k in PROCESS_KEYS)
        # bias a commit that trips both toward process if it names a gate/steward
        if p and not r:
            process += 1
        elif r and not p:
            research += 1
        elif r and p:
            # count as research substance only if it lands a result
            if any(k in low for k in ("result", "land ", "discharge", "theorem",
                                      "probe", "eta", "index", "verdict")):
                research += 1
            else:
                process += 1
        else:
            process += 1  # untagged maintenance
    total = len(subs)
    return {
        "since": since,
        "commits": total,
        "research_substance": research,
        "process_meta": process,
        "research_share": round(research / total, 3) if total else None,
    }


def hourly_cycle_activity() -> dict[str, int]:
    d = ROOT / "explorations" / "hourly-cycles"
    per = Counter()
    if d.exists():
        for f in d.iterdir():
            m = re.match(r"hourly-(\d{8})", f.name)
            if m:
                s = m.group(1)
                per[f"{s[:4]}-{s[4:6]}-{s[6:8]}"] += 1
    return dict(sorted(per.items()))


def steward_run_cadence() -> dict[str, int]:
    d = ROOT / "steward" / "runs"
    per = Counter()
    if d.exists():
        for f in d.iterdir():
            m = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
            if m:
                per[m.group(1)] += 1
    return dict(sorted(per.items()))


def repeat_touch_anchors(top: int = 8) -> list[list[object]]:
    """How many DISTINCT commits touched each repeatedly-revised path."""
    out = git(["log", "--pretty=format:COMMIT", "--name-only"]).splitlines()
    touches = Counter()
    for line in out:
        if line and line != "COMMIT" and "/" in line:
            touches[line] += 1
    return [[p, n] for p, n in touches.most_common(top)]


def main() -> None:
    metrics = {
        "commits_per_day": commits_per_day(),
        "add_mod_per_day": add_mod_per_day(),
        "canon_adds_per_day": canon_adds_per_day(),
        "hourly_cycle_activity_per_day": hourly_cycle_activity(),
        "steward_run_cadence_per_day": steward_run_cadence(),
        "subject_classification_all_history": subject_classification(),
        "recent_window_since_0630": recent_window_classification("2026-06-30"),
        "most_re_touched_paths": repeat_touch_anchors(),
        "notes": {
            "net_resolved_gain": "PROXY ONLY (canon adds). No machine verdict ledger; hand-judged in report.",
            "classification": "keyword heuristic; treat as judgment-assisted, not ground truth.",
        },
    }
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Print a read-only entry view; no maintained state, cache, or work selection."""
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
NOTICE = (
    "PARTIAL ENTRY VIEW — fresh reads of CURRENT-STATE.yaml and VERIFICATION.md. "
    "The summary history and wider frontier are omitted. This view does not select "
    "work, certify freshness, or replace the full state, remaining verification "
    "sections, source-routing rules, and exact artifacts required for a reused claim."
)


def first_verification_section(text):
    """Keep the first level-two section, including subheadings and fenced code."""
    section, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is not None:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
        elif re.match(r"^ {0,3}#{1,2}\s+", line):
            if section:
                break
            if not re.match(r"^ {0,3}##\s+", line):
                continue
            section.append(line)
            continue
        if section:
            section.append(line)
    if not section or fence is not None:
        raise ValueError("VERIFICATION.md lacks a complete first level-two section")
    return "\n".join(section).rstrip()


def render_context(state, verification):
    if not isinstance(state, dict):
        raise ValueError("CURRENT-STATE.yaml must be a mapping")
    for field in ("purpose", "current_question", "next_condition"):
        if not isinstance(state.get(field), str) or not state[field].strip():
            raise ValueError(f"CURRENT-STATE.yaml needs nonempty {field}")
    result = state.get("current_result")
    if not isinstance(result, dict):
        raise ValueError("CURRENT-STATE.yaml needs a current_result mapping")
    entry = {
        "revision_basis": state.get("revision_basis"),
        "purpose": state["purpose"],
        "result_status": result.get("status"),
        "research_method_control": state.get("research_method_control"),
        "current_question": state["current_question"],
        "next_condition_lead_partial": state["next_condition"].strip().splitlines()[0],
        "acceptance": state.get("acceptance"),
        "contribution_path": state.get("contribution_path"),
        "what_needs_joe": state.get("what_needs_joe"),
    }
    return (NOTICE + "\n\n```yaml\n" + yaml.safe_dump(entry, sort_keys=False, allow_unicode=True)
            + "```\n\nFirst VERIFICATION.md section in file order (not an inferred newest result):\n\n"
            + first_verification_section(verification) + "\n")


def main():
    try:
        state = yaml.safe_load((ROOT / "CURRENT-STATE.yaml").read_text(encoding="utf-8"))
        print(render_context(state, (ROOT / "VERIFICATION.md").read_text(encoding="utf-8")), end="")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"research_context: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

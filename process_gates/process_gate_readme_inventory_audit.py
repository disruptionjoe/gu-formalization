#!/usr/bin/env python3
"""Guard that process_gates/README.md names every live process gate script.

This is a documentation/process inventory check. It does not validate the
research content of any gate.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROCESS_GATES_DIR = REPO_ROOT / "process_gates"
README = PROCESS_GATES_DIR / "README.md"


def live_gate_scripts() -> set[str]:
    return {
        path.name
        for path in PROCESS_GATES_DIR.glob("*.py")
        if path.name != "__init__.py"
    }


def documented_gate_scripts(readme_text: str) -> set[str]:
    """Return local process-gate script names documented as Markdown code spans."""
    names = set()
    for match in re.finditer(r"`([^`]+\.py)`", readme_text):
        candidate = match.group(1).replace("\\", "/")
        if "/" in candidate:
            continue
        names.add(candidate)
    return names


def inventory_delta(live: set[str], documented: set[str]) -> tuple[list[str], list[str]]:
    process_gate_names = {
        name
        for name in documented
        if name.endswith(("_audit.py", "_gate.py", "_certificate.py", "_checker.py"))
    }
    missing = sorted(live - documented)
    stale = sorted(process_gate_names - live)
    return missing, stale


def run_self_tests() -> None:
    sample_readme = """
    - `alpha_audit.py`
    - `beta_gate.py`
    - `not/a/local_gate.py`
    - `notes.py`
    """
    documented = documented_gate_scripts(sample_readme)
    assert documented == {"alpha_audit.py", "beta_gate.py", "notes.py"}
    missing, stale = inventory_delta(
        {"alpha_audit.py", "gamma_gate.py"},
        documented | {"stale_audit.py"},
    )
    assert missing == ["gamma_gate.py"]
    assert stale == ["beta_gate.py", "stale_audit.py"]


def main() -> int:
    run_self_tests()
    readme_text = README.read_text(encoding="utf-8")
    live = live_gate_scripts()
    documented = documented_gate_scripts(readme_text)
    missing, stale = inventory_delta(live, documented)

    print("[process-gate README inventory]")
    print(f"  live process gate scripts : {len(live)}")
    print(f"  documented local scripts  : {len(documented & live)}")

    if missing:
        print("  missing from README:")
        for name in missing:
            print(f"    - {name}")

    if stale:
        print("  stale README entries:")
        for name in stale:
            print(f"    - {name}")

    assert not missing, "README is missing live process gate script names"
    assert not stale, "README names stale local process gate scripts"
    print("VERDICT: PASS - process_gates/README.md names every live process gate script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

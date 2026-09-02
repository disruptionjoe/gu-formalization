#!/usr/bin/env python3
"""Run the integrated extra-vector certificate and its four upstream controls."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COMMANDS = (
    ("integrated baseline", "tests/attention-shots/declared_content_extra_vector_obstruction.py"),
    ("integrated hostile selftest", "tests/attention-shots/declared_content_extra_vector_obstruction.py", "--selftest"),
    ("PV-1 orbit census", "tests/channel-swings/joe_directed_extra_vector_stabilizer_probe.py"),
    ("PV-2 observation split", "tests/channel-swings/joe_directed_observation_reduction_probe.py"),
    ("MV-1 empirical comparator control", "tests/channel-swings/joe_directed_neff_fifth_force_massless_vector_probe.py"),
    ("MV-2 mass-route closure", "tests/channel-swings/joe_directed_stueckelberg_probe.py"),
)


def interpreter_for(relative: str) -> str:
    """Use the repo's local compute environment for the SymPy-only MV-1 control."""
    if "neff_fifth_force" not in relative:
        return sys.executable
    available = subprocess.run(
        [sys.executable, "-c", "import sympy"], capture_output=True
    ).returncode == 0
    if available:
        return sys.executable
    local_python = ROOT / "_local" / "cas-venv" / "bin" / "python"
    if local_python.exists():
        return str(local_python)
    raise RuntimeError(
        "MV-1 is a non-load-bearing empirical control but requires SymPy; "
        "install requirements.txt or run the integrated certificate directly"
    )


def main() -> int:
    failures = []
    for label, relative, *arguments in COMMANDS:
        print(f"\n=== {label} ===", flush=True)
        try:
            interpreter = interpreter_for(relative)
        except RuntimeError as exc:
            print(f"DEPENDENCY ERROR: {exc}")
            failures.append(label)
            continue
        result = subprocess.run([interpreter, str(ROOT / relative), *arguments], cwd=ROOT)
        if result.returncode:
            failures.append(label)
    print(f"\nVERDICT: {len(COMMANDS) - len(failures)}/{len(COMMANDS)} commands passed")
    if failures:
        print("FAILED: " + ", ".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

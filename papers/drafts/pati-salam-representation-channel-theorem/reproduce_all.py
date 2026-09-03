#!/usr/bin/env python3
"""Run the representation-channel theorem and its upstream controls."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COMMANDS = (
    (
        "integrated baseline",
        sys.executable,
        "tests/attention-shots/pati_salam_representation_channel_theorem.py",
    ),
    (
        "integrated hostile selftest",
        sys.executable,
        "tests/attention-shots/pati_salam_representation_channel_theorem.py",
        "--selftest",
    ),
    (
        "upstream exact character and owner control",
        sys.executable,
        "tests/channel-swings/source_native_adjoint_144_coupling_probe.py",
        "--selftest",
    ),
    (
        "Lean finite intersection kernel",
        "lake",
        "env",
        "lean",
        "Lean/GUFormalization/SourceNativeAdjointCoupling.lean",
    ),
)


def main() -> int:
    failures = []
    for label, *command in COMMANDS:
        print(f"\n=== {label} ===", flush=True)
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            failures.append(label)
    print(f"\nVERDICT: {len(COMMANDS) - len(failures)}/{len(COMMANDS)} commands passed")
    if failures:
        print("FAILED: " + ", ".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

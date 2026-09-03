#!/usr/bin/env python3
"""Run the literal-observation obstruction and its upstream controls."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COMMANDS = (
    (
        "integrated baseline",
        sys.executable,
        "tests/attention-shots/literal_observation_gamma_kernel_obstruction.py",
    ),
    (
        "integrated hostile selftest",
        sys.executable,
        "tests/attention-shots/literal_observation_gamma_kernel_obstruction.py",
        "--selftest",
    ),
    (
        "upstream Spin(6,4) and literal-pullback control",
        sys.executable,
        "tests/channel-swings/source_native_spin64_observation_sector_probe.py",
    ),
    (
        "Lean general literal-pullback obstruction",
        "lake",
        "env",
        "lean",
        "Lean/GUFormalization/SourceNativeSpin64Observation.lean",
    ),
    (
        "independent corrected-projector escape control",
        sys.executable,
        "tests/channel-swings/source_native_corrected_observation_probe.py",
    ),
    (
        "Lean corrected-projector escape kernel",
        "lake",
        "env",
        "lean",
        "Lean/GUFormalization/SourceNativeCorrectedObservation.lean",
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

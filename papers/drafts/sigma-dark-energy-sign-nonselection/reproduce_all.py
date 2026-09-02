#!/usr/bin/env python3
"""Run the integrated sigma-sign certificate and its four upstream controls."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COMMANDS = (
    ("integrated baseline", "tests/attention-shots/sigma_dark_energy_sign_nonselection.py"),
    ("integrated hostile selftest", "tests/attention-shots/sigma_dark_energy_sign_nonselection.py", "--selftest"),
    ("Q2-FREE binary-domain control", "tests/channel-swings/q2_sector_bit_standpoint_probe.py"),
    ("W211 five-method proxy control", "tests/W211_five_method_convergence.py"),
    ("W219 native correction control", "tests/W219_native_good_stable_stabilizer_gate.py"),
    ("CC-1 gauge-sign control", "tests/channel-swings/joe_directed_lambda_sign_probe.py"),
)


def interpreter_for(relative: str) -> str:
    """Use the repository's local compute environment for the SymPy CC-1 control."""
    if "joe_directed_lambda_sign" not in relative:
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
        "CC-1 requires SymPy; install requirements.txt or provide "
        "_local/cas-venv"
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

#!/usr/bin/env python3
"""Mutation-backed custody gate for the numerical and scope hardening wave."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/numerical-scope-hardening-wave.json"
REGISTER = ROOT / "lab/process/improvement-register-2026-08-03.md"
H44 = ROOT / "tests/wave25/H44_de_backreacted_background.py"
W129 = ROOT / "tests/W129_oq2_m2_band_sweep.py"


def evaluate(manifest: dict, register: str, h44: str, w129: str) -> list[tuple[str, bool]]:
    rows = {row["id"]: row for row in manifest.get("records", [])}
    return [
        ("four exact records", set(rows) == {"P-M25", "P-L12", "P-L13", "M-M32"}),
        ("P-M25 protected disposition", rows.get("P-M25", {}).get("result") == "PATI_SALAM_SCOPE_FENCE_SPECIFIED_BUT_NOT_APPLIED"),
        ("H44 scale-aware result", rows.get("P-L12", {}).get("result") == "H44_FIXED_POINT_STOP_IS_SCALE_AWARE"),
        ("H44 relative stop", "if drel < rtol:" in h44 and "if dmax < tol:" not in h44),
        ("H44 dual diagnostic", "converged_relative_delta" in h44 and "converged_absolute_delta" in h44),
        ("W129 direct-root result", rows.get("P-L13", {}).get("result") == "W129_DCHI2_CROSSING_IS_DIRECTLY_ROOT_SOLVED"),
        ("W129 direct Brent solve", "f0_9 = float(brentq(" in w129 and "np.interp(9.0" not in w129),
        ("M-M32 assumption fence", rows.get("M-M32", {}).get("result") == "M_M20_BOUNDARY_CONSEQUENCE_IS_EXPLICITLY_CONDITIONAL"),
        ("register dispositions current", all(token in register for token in (
            "P-M25 | PS-chain verification file: signature-stale (rooted at Spin(7,7), no banner, updated 06-20), ships inside the LNF zenodo package while canon asserts (9,5) | **VERIFIED LIVE; PROTECTED APPLY REMAINS",
            "P-L12 | H44 fixed-point tol",
            "P-L13 | W129 f0_9 log-interp",
            "M-M20 | **VERIFIED LIVE; CONDITIONAL AT THE ASSUMPTION-FENCE CEILING",
            "M-M32 | **EXECUTED (verified 2026-08-27 at the assumption-fence ceiling)",
        ))),
    ]


def load() -> tuple[dict, str, str, str]:
    return (
        json.loads(MANIFEST.read_text()), REGISTER.read_text(), H44.read_text(),
        W129.read_text(),
    )


def selftest(inputs: tuple[dict, str, str, str]) -> int:
    mutations = []
    mutators = (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0]["records"][0].update(result="AMBIENT_SIGNATURE_SETTLED"),
        lambda x: x.__setitem__(1, x[1].replace("PROTECTED APPLY REMAINS", "EXECUTED")),
        lambda x: x.__setitem__(2, x[2].replace("if drel < rtol:", "if dmax < tol:")),
        lambda x: x.__setitem__(2, x[2].replace("converged_absolute_delta", "absolute_delta_removed")),
        lambda x: x.__setitem__(3, x[3].replace("f0_9 = float(brentq(", "f0_9 = float(np.interp(9.0, [da, db], np.log([fa, fb]))) # ")),
        lambda x: x[0]["records"][3].update(result="BOUNDARY_IDENTIFICATIONS_PROVED"),
    )
    for mutate in mutators:
        trial = [copy.deepcopy(v) for v in inputs]
        mutate(trial)
        mutations.append(any(not ok for _, ok in evaluate(*trial)))
    caught = sum(mutations)
    print(f"numerical-scope mutation controls: {caught}/{len(mutations)} caught")
    return 0 if caught == len(mutations) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"numerical-scope hardening: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())

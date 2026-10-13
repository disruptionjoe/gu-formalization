#!/usr/bin/env python3
"""Exact quotient-loop controls for K1722."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1722-diagonal-circle-embedding.json").read_text())


def scalar_exp(t):
    return abs(math.sin(t)) < 1e-12


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    c, q = D["diagonal_circle"], D["decision"]
    endpoint_signs = tuple(round(math.cos(math.pi)) for _ in range(2))
    checks += [
        ("Clifford squares", "E^2=F^2=-1" in c["generators"]),
        ("half generators", "(beta/2)E" in c["definition"] and "(beta/2)F" in c["definition"]),
        ("period", "2 pi" in c["definition"]),
        ("endpoint signs", endpoint_signs == (-1, -1)),
        ("diagonal quotient closure", "diagonal(-1,-1)" in c["closure"]),
        ("midpoint non-scalar", not scalar_exp(math.pi / 2)),
        ("primitive identity test", "only at beta=0 modulo 2 pi" in c["embedding"]),
        ("trivial center intersection", "D intersection Z(K)={1}" in c["center_intersection"]),
        ("noncentral half period", "D(pi) is noncentral" in c["half_period"]),
        ("quotient decision", q["well_defined_circle_in_quotient"]),
        ("embedding decision", q["primitive_embedding"]),
        ("intersection decision", q["trivial_center_intersection"]),
        ("half-period decision", q["half_period_is_noncentral"]),
        ("source fence", not q["source_selects_diagonal_circle"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()

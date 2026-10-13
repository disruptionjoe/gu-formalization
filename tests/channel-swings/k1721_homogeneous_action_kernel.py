#!/usr/bin/env python3
"""Exact structural controls for K1721's homogeneous action kernel."""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1721-homogeneous-action-kernel.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    k, q = D["kernel_theorem"], D["decision"]
    checks += [
        ("connected K", "connected" in k["group"]),
        ("finite M", "finite" in k["subgroup"]),
        ("normal core", "core_K(M)" in k["homogeneous_kernel"] and "intersection_k" in k["homogeneous_kernel"]),
        ("finite-normal argument", all(s in k["core_to_center"] for s in ("finite normal", "connected K", "singleton"))),
        ("center reverse inclusion", all(s in k["center_to_core"] for s in ("centralizes A", "every conjugate"))),
        ("two-element center", "{1,z}" in k["center"] and "z=[-1,1]" in k["center"]),
        ("full L2 kernel", "same kernel" in k["hilbert_kernel"] and "positive measure" in k["hilbert_kernel"]),
        ("homogeneous decision", q["homogeneous_kernel_equals_center"]),
        ("Hilbert decision", q["hilbert_kernel_equals_center"]),
        ("order-two decision", q["kernel_has_order_two"]),
        ("hypothesis fence", q["depends_on_connected_K_and_finite_M"]),
        ("physical fence", not q["physical_quotient_constructed"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()

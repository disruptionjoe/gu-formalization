#!/usr/bin/env python3
"""Governance surface audit for conditional physics ledger v0.17."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


checks = {
    "machine ledger exists": (ROOT / "lab/process/conditional-physics-ledger-v0.17.json").exists(),
    "human ledger exists": (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.17.md").exists(),
    "result exists": (ROOT / "explorations/conditional-build/selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md").exists(),
    "registry exists": (ROOT / "lab/process/selected-cubic-qft-threshold-and-numerator-gate.json").exists(),
    "hostile review exists": (ROOT / "lab/process/hostile-reviews/2026-08-05-selected-cubic-qft-threshold-and-numerator-gate-review.md").exists(),
    "source record exists": (ROOT / "lab/sources/selected-cubic-qft-threshold-and-numerator-gate-source-reinspection-2026-08-05.md").exists(),
    "LANES points to v0.17": "conditional-physics-ledger-v0.17.json" in read("LANES.yaml"),
    "NEXT-STEPS points to v0.17": "conditional-physics-ledger-v0.17" in read("NEXT-STEPS.md"),
    "RESEARCH-STATUS points to result": "selected-cubic-qft-threshold-and-numerator-gate" in read("RESEARCH-STATUS.md"),
    "context pack points to v0.17": "conditional-physics-ledger-v0.17" in read("lab/process/agent-context-pack.md"),
    "contract points to v0.17": "conditional-physics-ledger-v0.17" in read("lab/process/functional-channel-operating-contract-v1.0.md"),
    "contract JSON points to v0.17": "conditional-physics-ledger-v0.17" in read("lab/process/functional-channel-operating-contract-v1.0.json"),
    "tests README names probe": "selected_cubic_qft_threshold_numerator_probe.py" in read("tests/README.md"),
    "process README names ledger audit": "conditional_physics_ledger_v017_scope_audit.py" in read("process_gates/README.md"),
    "explorations README names result": "selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md" in read("explorations/README.md"),
    "lab process README names registry": "selected-cubic-qft-threshold-and-numerator-gate.json" in read("lab/process/README.md"),
    "lab sources README names source": "selected-cubic-qft-threshold-and-numerator-gate-source-reinspection-2026-08-05.md" in read("lab/sources/README.md"),
    "P2 remains unconsumed": "P1/P2/P3 remain unused" in read("explorations/conditional-build/selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md"),
    "Q1 pole remains conditional": "No interacting `C`, Q1 pole" in read("explorations/conditional-build/selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md"),
    "symplectic hostile lens is durable": (
        "Symplectic geometry" in read("lab/process/hostile-reviews/2026-08-05-selected-cubic-qft-threshold-and-numerator-gate-review.md")
        and "presymplectic characteristic kernel" in read("lab/process/hostile-reviews/2026-08-05-selected-cubic-qft-threshold-and-numerator-gate-review.md")
        and "unreduced cubic density is not a physical transition" in read("lab/process/hostile-reviews/2026-08-05-selected-cubic-qft-threshold-and-numerator-gate-review.md")
    ),
}

failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("FAIL: " + "; ".join(failed))

print("PASS: v0.17 wires the exact three-species odd-channel shells while keeping the selected on-shell numerator, Q1, physical sheet, common domain and P1/P2/P3 open")

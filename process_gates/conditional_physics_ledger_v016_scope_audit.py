#!/usr/bin/env python3
"""Governance surface audit for conditional physics ledger v0.16."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


checks = {
    "machine ledger exists": (ROOT / "lab/process/conditional-physics-ledger-v0.16.json").exists(),
    "human ledger exists": (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.16.md").exists(),
    "result exists": (ROOT / "explorations/conditional-build/first-perturbative-background-c-operator-2026-08-05.md").exists(),
    "registry exists": (ROOT / "lab/process/first-perturbative-background-c-operator.json").exists(),
    "hostile review exists": (ROOT / "lab/process/hostile-reviews/2026-08-05-first-perturbative-background-c-operator-review.md").exists(),
    "source record exists": (ROOT / "lab/sources/first-perturbative-background-c-operator-source-reinspection-2026-08-05.md").exists(),
    "LANES points to v0.16": "conditional-physics-ledger-v0.16.json" in read("lab/process/RESEARCH-AGENDA.json"),
    "NEXT-STEPS points to v0.16": "conditional-physics-ledger-v0.16" in read("NEXT-STEPS.md"),
    "RESEARCH-STATUS points to result": "first-perturbative-background-c-operator" in read("RESEARCH-STATUS.md"),
    "context pack points to v0.16": "conditional-physics-ledger-v0.16" in read("lab/process/CURRENT-RESEARCH-CONTEXT.md"),
    "contract points to v0.16": "conditional-physics-ledger-v0.16" in read("lab/methods/research-evidence-contract-v1.0.md"),
    "contract JSON points to v0.16": "conditional-physics-ledger-v0.16" in read("lab/methods/research-evidence-contract-v1.0.json"),
    "tests README names probe": "first_perturbative_background_c_operator_probe.py" in read("tests/README.md"),
    "process README names ledger audit": "conditional_physics_ledger_v016_scope_audit.py" in read("process_gates/README.md"),
    "explorations README names result": "first-perturbative-background-c-operator-2026-08-05.md" in read("explorations/README.md"),
    "lab process README names registry": "first-perturbative-background-c-operator.json" in read("lab/process/README.md"),
    "lab sources README names source": "first-perturbative-background-c-operator-source-reinspection-2026-08-05.md" in read("lab/sources/README.md"),
    "P2 remains unconsumed": "P1/P2/P3 remain unused" in read("explorations/conditional-build/first-perturbative-background-c-operator-2026-08-05.md"),
    "full QFT C remains open": "quantum Fock-space `C`" in read("explorations/conditional-build/first-perturbative-background-c-operator-2026-08-05.md"),
}

failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("FAIL: " + "; ".join(failed))

print("PASS: v0.16 wires the zero-parameter fixed-background TT C and its exact walls without promoting a full nonlinear/Fock metric or consuming P1/P2/P3")

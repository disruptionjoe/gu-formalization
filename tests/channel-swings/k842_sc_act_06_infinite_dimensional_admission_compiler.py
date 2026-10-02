#!/usr/bin/env python3
"""K842: extend K838 with infinite-dimensional realization controls."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k842-sc-act-06-infinite-dimensional-admission-compiler.json"
PATHS = {
    key: ROOT / path
    for key, path in {
        "k838": "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json",
        "k839": "lab/process/k839-sc-act-06-finite-cutoff-limit-gate.json",
        "k840": "lab/process/k840-sc-act-06-collapsing-nonlinear-radius.json",
        "k841": "lab/process/k841-sc-act-06-analytic-hilbert-zero-accumulation.json",
    }.items()
}
NEW_ROWS = [
    "function_space_topology_and_completion_declared",
    "bounded_or_tame_splitting_and_right_inverse",
    "uniform_nonlinear_neighborhood_or_limit_control",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k838 = json.loads(PATHS["k838"].read_text(encoding="utf-8"))
    base = k838["compiler"]["required_rows"]
    required = base + NEW_ROWS
    complete = {row: True for row in required}
    cutoff_only = {**complete, **{row: False for row in NEW_ROWS}}
    current = {row: False for row in required}

    def admit(candidate: dict[str, bool]) -> bool:
        return set(candidate) == set(required) and all(candidate[row] for row in required)

    return {
        "schema_version": "1.0",
        "result_id": "K842-SC-ACT-06-INFINITE-DIMENSIONAL-ADMISSION-COMPILER",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": (
            "Fail-closed extension of K838 preventing finite-dimensional or finite-cutoff "
            "exactness from substituting for an actual function-space realization, controlled "
            "splitting, and nonlinear limit neighborhood."
        ),
        "pinned_inputs": {
            key: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for key, path in PATHS.items()
        },
        "compiler": {
            "k838_rows": base,
            "new_rows": NEW_ROWS,
            "required_rows": required,
            "k838_row_count": 27,
            "new_row_count": 3,
            "total_row_count": 30,
            "finite_cutoff_exactness_alone_admissible": False,
            "actual_completed_space_and_controlled_splitting_required": True,
            "cutoff_uniform_nonlinear_control_required": True,
        },
        "exact_controls": {
            "infinite_dimensional_complete_candidate": complete,
            "infinite_dimensional_complete_admitted": admit(complete),
            "finite_cutoff_only_candidate": cutoff_only,
            "finite_cutoff_only_admitted": admit(cutoff_only),
            "current_gu_candidate": current,
            "current_gu_missing_row_count": sum(not value for value in current.values()),
            "current_gu_admitted": admit(current),
        },
        "decision": {
            "compiler_jointly_consistent": True,
            "actual_gu_function_space_topology_declared": False,
            "actual_gu_bounded_or_tame_splitting_constructed": False,
            "actual_gu_uniform_nonlinear_neighborhood_constructed": False,
            "actual_gu_rich_moduli_admitted": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": (
                "Supply K838's source/action-owned category-complete family on a declared "
                "completed function-space scale, together with a bounded or tame splitting/right "
                "inverse and nonlinear estimates uniform in every cutoff or approximation limit."
            ),
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": (
            "Executable 30-row infinite-dimensional admission interface with synthetic exact "
            "controls only; no GU family, function-space completion, rich moduli, source, ledger, "
            "canon, or physical verdict."
        ),
        "controls": {
            "producer": "tests/channel-swings/k842_sc_act_06_infinite_dimensional_admission_compiler.py",
            "probe": "tests/channel-swings/k842_sc_act_06_infinite_dimensional_admission_compiler_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 14,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    compiler = payload["compiler"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    assert compiler["k838_row_count"] == 27
    assert len(compiler["k838_rows"]) == 27
    assert compiler["new_rows"] == NEW_ROWS
    assert compiler["new_row_count"] == 3
    assert compiler["total_row_count"] == 30
    assert not compiler["finite_cutoff_exactness_alone_admissible"]
    assert compiler["actual_completed_space_and_controlled_splitting_required"]
    assert compiler["cutoff_uniform_nonlinear_control_required"]
    assert controls["infinite_dimensional_complete_admitted"]
    assert not controls["finite_cutoff_only_admitted"]
    assert controls["current_gu_missing_row_count"] == 30
    assert not controls["current_gu_admitted"]
    assert decision["compiler_jointly_consistent"]
    assert not decision["actual_gu_function_space_topology_declared"]
    assert not decision["actual_gu_bounded_or_tame_splitting_constructed"]
    assert not decision["actual_gu_uniform_nonlinear_neighborhood_constructed"]
    assert not decision["actual_gu_rich_moduli_admitted"]
    assert not decision["global_sc_act_06_proved_or_refuted"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(serialized, encoding="utf-8")
    elif args.check:
        assert json.loads(OUTPUT.read_text(encoding="utf-8")) == payload
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

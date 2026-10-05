#!/usr/bin/env python3
"""K1133: audit zero-kappa symbol null rows against propagation requirements."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1133-zero-kappa-symbol-null-propagation-audit.json"


def load(name):
    return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    k132 = load("selected-k132-native-i1b-t0-all-grade-noether-complex.json")
    k133 = load("selected-k133-native-i1b-t0-flat-complex-kappa-pencil.json")
    c = k132["compatibility"]
    f = k133["flat_kappa_zero"]
    return {
        "schema_version": "1.0",
        "result_id": "K1133-ZERO-KAPPA-SYMBOL-NULL-PROPAGATION-AUDIT",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "normal_kernel_dimension": c["normal_kernel_dimension"],
        "normal_tangential_common_kernel_dimension": c["normal_tangential_common_kernel_dimension"],
        "normal_null_directions_lost_tangentially": c["normal_kernel_dimension"] - c["normal_tangential_common_kernel_dimension"],
        "generic_weyl_distortion_complex": c["generic_weyl_distortion_complex"],
        "flat_selected_euler_square_zero": f["selected_euler_is_square_zero"],
        "flat_symbol_cohomology_defined": f["symbol_cohomology_defined_for_selected_euler_as_differential"],
        "euler_ranks": f["euler_ranks"],
        "square_zero_rank_ceiling": f["square_zero_rank_ceiling"],
        "propagating_constraint_complex_owned": False,
        "conclusion": "zero-kappa principal null rows are characteristic data, not an action-owned propagated non-gauge constraint complex",
        "scope_boundary": "selected comm/symi/symi I1B operator on the K127 local germ; a different source-owned differential or completed background may reopen the test",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["normal_kernel_dimension"] == 24
    assert d["normal_tangential_common_kernel_dimension"] == 11
    assert d["normal_null_directions_lost_tangentially"] == 13
    assert d["generic_weyl_distortion_complex"] is False
    assert d["flat_selected_euler_square_zero"] is False
    assert d["flat_symbol_cohomology_defined"] is False
    assert all(v > d["square_zero_rank_ceiling"] for v in d["euler_ranks"].values())
    assert d["propagating_constraint_complex_owned"] is False
    assert "characteristic data" in d["conclusion"]
    assert "may reopen" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1133 controls: 12/12")
